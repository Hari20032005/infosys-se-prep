#!/usr/bin/env python3
"""Rebalance MCQ answer-letter distribution, correctness-preserving by construction.

Two defects shipped from this tool on the Accenture build. Both are guarded here:

  1. Generated sets clustered on option (a) -- one was 7 of 7.
     Fix: assign each question a target letter from a BALANCED MULTISET.

  2. The first fix assigned targets by cycling a,b,c,d, producing keys that read
     a,b,c,d,a,b,c,d -- balanced but perfectly guessable.
     Fix: shuffle the multiset with a seed derived from the FILE NAME. Deterministic
     across reruns, different per file, not predictable by a reader.

  3. A parser pulled option text out of a traps TABLE into the questions, and another
     split on a <details> tag that appeared inside an option.
     Fix: operate ONLY inside the practice-questions section, never parse table rows,
     and REFUSE any question whose four options cannot be parsed unambiguously.

Correctness is preserved because the correct option's TEXT is swapped with whatever
text occupies the target slot, and the key letter is rewritten to match. The set of
options is unchanged; only their order and the pointer move.

    python3 data/shuffle.py <file.md> [...]      # rewrites in place
    python3 data/shuffle.py --check <file.md>    # report only
"""
import collections
import hashlib
import random
import re
import sys

OPT = re.compile(r'^(\s*)([a-d])\)\s+(.*)$')
QNUM = re.compile(r'^\s*(?:\*\*)?(\d{1,2})[\.\)]')
KEYLINE = re.compile(
    r'^(?P<pre>\s*(?:\*\*)?(?:Q\s*)?(?P<n>\d{1,2})[\.\)]?\s*(?:\*\*)?\s*[-–—]?\s*)'
    r'(?P<open>\*\*|)(?P<letter>[a-d])(?P<close>\*\*|)(?P<rest>\b.*)$')
KEYHEAD = re.compile(r'answer\s*key', re.I)
# Heading variants actually produced: "## 7. Practice questions",
# "## 8. Ten practice MCQs", "## 7. Twenty practice questions".
PRACTICE = re.compile(r'^##\s*\d*\.?\s*\w*\s*practice\s+(questions|mcqs)', re.I)
# BUGFIX 2026-09-21: the first parser assumed ONE OPTION PER LINE. The generator
# actually emits all four on a single line: "a) foo b) bar c) baz d) qux".
# That layout is handled by INLINE below; the one-per-line layout is still
# supported. Anything else is refused rather than guessed at.
INLINE = re.compile(r'(?<![A-Za-z0-9])([a-d])\)\s')
NEXTSEC = re.compile(r'^##\s')


def split_regions(lines):
    """Return (start, key_start, end) for the practice section, or None.

    start..key_start is where questions live; key_start..end is the answer key.
    Anything outside this range -- concept notes, traps tables, sources -- is never touched.
    """
    start = key = None
    for i, l in enumerate(lines):
        if start is None and PRACTICE.match(l):
            start = i
            continue
        if start is not None and key is None and l.startswith('#') and KEYHEAD.search(l):
            key = i
            continue
        if start is not None and key is not None and NEXTSEC.match(l) and i > key:
            return start, key, i
    if start is not None and key is not None:
        return start, key, len(lines)
    return None


def parse_inline(line):
    """Split "a) foo b) bar c) baz d) qux" into {letter: text}, or None if not that."""
    hits = list(INLINE.finditer(line))
    letters = [h.group(1) for h in hits]
    if letters != ['a', 'b', 'c', 'd']:
        return None
    out = {}
    for n, h in enumerate(hits):
        end = hits[n + 1].start() if n + 1 < len(hits) else len(line)
        out[h.group(1)] = line[h.end():end].rstrip()
    return out


def parse_questions(lines, lo, hi):
    """Collect questions. Returns (usable, refused).

    usable entries are (qnum, kind, payload):
      kind 'inline' -> payload is (line_index, {letter: text})
      kind 'block'  -> payload is {letter: line_index}
    Anything that does not parse to exactly a,b,c,d is REFUSED, never guessed.
    """
    out, refused = [], []
    cur, opts = None, {}

    def flush():
        nonlocal cur, opts
        if cur is not None:
            if set(opts) == set('abcd') and -1 not in opts.values():
                out.append((cur, 'block', dict(opts)))
            elif opts:
                refused.append(cur)
        cur, opts = None, {}

    for i in range(lo, hi):
        l = lines[i]
        if '|' in l:                      # never parse a table row -- Accenture defect 3
            continue
        inline = parse_inline(l)
        if inline is not None:
            qn = cur
            if qn is None:                # option line with no question number seen
                refused.append(i)
                continue
            flush_num = qn
            cur, opts = None, {}
            out.append((flush_num, 'inline', (i, inline)))
            continue
        m = OPT.match(l)
        if m and cur is not None:
            letter = m.group(2)
            opts[letter] = -1 if letter in opts else i
            continue
        qm = QNUM.match(l)
        if qm and not m:
            flush()
            cur = int(qm.group(1))
    flush()
    return out, refused


def balanced_targets(n, seed_text):
    """A balanced multiset of a/b/c/d, shuffled deterministically by file name."""
    base = (['a', 'b', 'c', 'd'] * (n // 4 + 1))[:n]
    seed = int(hashlib.sha256(seed_text.encode()).hexdigest()[:16], 16)
    rnd = random.Random(seed)
    for _ in range(64):                   # reshuffle until it is not a clean cycle
        rnd.shuffle(base)
        if n < 8:
            break
        if not (len(set(base[:4])) == 4 and base[:4] == base[4:8]):
            break
    return base


# DEFECT FOUND AND FIXED 2026-09-21: shuffling a DATA SUFFICIENCY question is wrong.
# Its four options are a fixed convention ("statement 1 alone", "statement 2 alone",
# "both together", "neither"), so permuting them makes option (c) mean different things
# in different questions. The first run did exactly that to L2 and had to be rebuilt by
# hand. Any file whose practice options are canonical is refused here.
CANONICAL = (
    'statement 1 alone', 'statement 2 alone', 'both together',
    'alone sufficient', 'alone not sufficient', 'data sufficiency',
    'assertion', 'reason',
)


def has_canonical_options(text):
    low = text.lower()
    return sum(phrase in low for phrase in CANONICAL) >= 2


def process(path, check_only=False):
    raw = open(path, encoding='utf-8').read()
    if has_canonical_options(raw):
        return path, 'REFUSED: canonical option set (do not shuffle)', None, None
    lines = raw.split('\n')
    reg = split_regions(lines)
    if not reg:
        return path, 'no practice section', None, None
    lo, key_lo, key_hi = reg
    qs, refused = parse_questions(lines, lo, key_lo)
    if not qs:
        return path, 'no parseable questions', None, None

    # map question number -> key line index and its current letter
    keymap = {}
    for i in range(key_lo, key_hi):
        if '|' in lines[i]:
            continue
        m = KEYLINE.match(lines[i])
        if m:
            n = int(m.group('n'))
            if n not in keymap:
                keymap[n] = (i, m)

    usable = [q for q in qs if q[0] in keymap]
    before = collections.Counter(keymap[n][1].group('letter') for n, _, _ in usable)
    if not usable:
        return path, 'no questions with a matching key', before, None

    targets = balanced_targets(len(usable), path)
    for (n, kind, payload), tgt in zip(usable, targets):
        ki, km = keymap[n]
        cur = km.group('letter')
        if cur == tgt or check_only:
            continue
        if kind == 'inline':
            li, texts = payload
            texts = dict(texts)
            texts[cur], texts[tgt] = texts[tgt], texts[cur]
            indent = lines[li][:len(lines[li]) - len(lines[li].lstrip())]
            lines[li] = indent + ' '.join(f'{L}) {texts[L]}' for L in 'abcd')
        else:
            i_cur, i_tgt = payload[cur], payload[tgt]
            mc, mt = OPT.match(lines[i_cur]), OPT.match(lines[i_tgt])
            lines[i_cur] = f"{mc.group(1)}{cur}) {mt.group(3)}"
            lines[i_tgt] = f"{mt.group(1)}{tgt}) {mc.group(3)}"
        lines[ki] = (km.group('pre') + km.group('open') + tgt
                     + km.group('close') + km.group('rest'))
        keymap[n] = (ki, KEYLINE.match(lines[ki]))

    after = collections.Counter(keymap[n][1].group('letter') for n, _, _ in usable)
    if not check_only:
        open(path, 'w', encoding='utf-8').write('\n'.join(lines))
    return path, f'{len(usable)} questions' + (
        f', {len(refused)} REFUSED' if refused else ''), before, after


if __name__ == '__main__':
    args = sys.argv[1:]
    check = '--check' in args
    files = [a for a in args if not a.startswith('--')]
    tot_b, tot_a = collections.Counter(), collections.Counter()
    for f in files:
        p, note, b, a = process(f, check)
        name = p.split('/')[-1]
        if b is None:
            print(f"  --   {name:54s} {note}")
            continue
        tot_b.update(b)
        tot_a.update(a or b)
        mx = max((a or b).values()) / sum((a or b).values())
        print(f"  {'ok' if mx <= 0.45 else 'XX'}   {name:54s} {note:24s} "
              f"{dict(sorted(b.items()))} -> {dict(sorted((a or b).items()))}")
    print(f"\n  TOTAL before: {dict(sorted(tot_b.items()))}")
    print(f"  TOTAL after : {dict(sorted(tot_a.items()))}")
    n = sum(tot_a.values())
    if n:
        worst = max(tot_a.values()) / n
        print(f"  most-common letter: {worst:.1%} of {n} questions "
              f"({'OK' if worst <= 0.30 else 'STILL SKEWED'})")
