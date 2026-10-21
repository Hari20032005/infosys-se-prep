#!/usr/bin/env python3
"""Check every answer key in the library against its own question and explanation.

Three checks, all of them cheap and all of them catching real defects seen before:

  1. SELF-REFUTING KEYS. Two keys on the Accenture build ended with a literal
     "Correction:" sentence that contradicted the letter they stated. Grep for that
     family of signatures.

  2. KEY POINTS AT A REAL OPTION. The stated letter must exist among the question's
     four options. After a shuffle this is the thing that would break first.

  3. NUMERIC AGREEMENT. Where the explanation ends in a number and the keyed option
     contains a number, they must match. This is what catches a key that was
     repointed without its option text moving with it.

  4. COUNTS. Question count must equal key count, and the file must not end mid-key.

    python3 data/verify_keys.py            # whole library
    python3 data/verify_keys.py <file>...  # specific files
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# BUGFIX 2026-09-21: the first pattern MISSED "Corrected: option b" (it only matched
# "correction:") and FALSE-POSITIVED on a grammar example sentence containing the words
# "this is wrong". Broadened, and now applied ONLY inside the answer-key region.
SELF_REFUTING = re.compile(
    r'(correction[:\s]|corrected[:\s]|corrected answer|actually,? the (correct )?answer is|'
    r'so option [a-d]\b|ignore the above|scratch that|i made an error)', re.I)
INLINE = re.compile(r'(?<![A-Za-z0-9])([a-d])\)\s')
OPTLINE = re.compile(r'^\s*([a-d])\)\s+(.*)$')
# BUGFIX 2026-09-21: the variant files number questions '**Q1.**', which this pattern
# rejected -- reported as '0 questions vs 10 keys'. The optional Q is now allowed.
QNUM = re.compile(r'^\s*(?:\*\*)?Q?\s*(\d{1,2})[\.\)]')
KEYLINE = re.compile(r'^\s*(?:\*\*)?(?:Q\s*)?(\d{1,2})[\.\)]?\s*(?:\*\*)?\s*[-–—]?\s*'
                     r'(?:\*\*)?([a-d])\)?(?:\*\*)?\b(.*)$')
PRACTICE = re.compile(r'^##\s*\d*\.?\s*\w*\s*practice\s+(questions|mcqs)', re.I)
KEYHEAD = re.compile(r'answer\s*key', re.I)
NUM = re.compile(r'-?\d[\d,]*\.?\d*')


def nums(s):
    # BUGFIX 2026-09-21: the generator writes U+2212 MINUS SIGN and en-dashes, which the
    # ASCII-hyphen regex silently dropped -- "-1" read as "1". That produced two false
    # NUMERIC-MISMATCH reports against keys that were correct (T2 q7 and q12).
    s = s.replace('\u2212', '-').replace('\u2013', '-').replace('\u2014', '-')
    return {n.replace(',', '').rstrip('.') for n in NUM.findall(s)}


def keys_in(lines, lo, hi):
    """Answer-key entries in a line range, as {question number: letter}."""
    found = {}
    for i in range(lo, hi):
        if lines[i].lstrip().startswith('|'):
            continue
        m = KEYLINE.match(lines[i])
        if m and int(m.group(1)) not in found:
            found[int(m.group(1))] = m.group(2)
    return found


def check(path):
    lines = path.read_text(encoding='utf-8').split('\n')
    issues = []

    start = key = None
    for i, l in enumerate(lines):
        if start is None and PRACTICE.match(l):
            start = i
        elif start is not None and key is None and l.startswith('#') and KEYHEAD.search(l):
            key = i
        elif start is not None and key is not None and l.startswith('## ') and i > key:
            end = i
            break
    else:
        end = len(lines)
    if start is None or key is None:
        return issues, 0, 0

    # Some sections declare ONE canonical option block for every question (data
    # sufficiency does this). Those questions carry no per-question options, so the
    # question/key count check does not apply and numeric matching is meaningless.
    section = '\n'.join(lines[start:key]).lower()
    if 'statement 1 alone is sufficient' in section:
        return issues, len(keys_in(lines, key, end)), len(keys_in(lines, key, end))

    # questions: number -> {letter: text}
    # BUGFIX 2026-09-21: the first version handled ONLY the "all four options on their
    # own line" layout and reported 0 questions for files using the other two layouts
    # that the generator actually emits. Five COUNT-MISMATCH reports were this bug, not
    # missing questions. All three layouts are now parsed:
    #   (1) question line, then "a) .. b) .. c) .. d) .." on the next line
    #   (2) question line, then one option per line
    #   (3) question and all four options on the SAME line
    qs, cur, block = {}, None, {}

    def flush_block():
        nonlocal cur, block
        if cur is not None and set(block) == set('abcd'):
            qs[cur] = dict(block)
        cur, block = None, {}

    in_fence = False
    for i in range(start, key):
        l = lines[i]
        if l.lstrip().startswith('```'):          # numbered pseudocode lines ("1) Integer c, n") are not question numbers
            in_fence = not in_fence
            continue
        if in_fence or l.lstrip().startswith('|'):
            continue
        hits = list(INLINE.finditer(l))
        letters = [h.group(1) for h in hits]
        qm = QNUM.match(l)
        if letters == ['a', 'b', 'c', 'd']:
            texts = {h.group(1): l[h.end():(hits[n + 1].start() if n + 1 < len(hits) else len(l))]
                     for n, h in enumerate(hits)}
            n_for = int(qm.group(1)) if qm else cur      # layout 3 vs layout 1
            if n_for is not None:
                qs[n_for] = texts
            cur, block = None, {}
            continue
        m = OPTLINE.match(l)
        if m and cur is not None:                        # layout 2
            block[m.group(1)] = m.group(2)
            continue
        if qm:
            flush_block()
            cur = int(qm.group(1))
    flush_block()

    keys = {}
    for i in range(key, end):
        if lines[i].lstrip().startswith('|'):
            continue
        m = KEYLINE.match(lines[i])
        if m and int(m.group(1)) not in keys:
            keys[int(m.group(1))] = (m.group(2), m.group(3))

    for i in range(key, end):                     # scoped to the answer-key region only
        if SELF_REFUTING.search(lines[i]):
            issues.append(("SELF-REFUTING", i + 1, lines[i].strip()[:90]))

    for n, (letter, expl) in sorted(keys.items()):
        if n not in qs:
            continue
        opts = qs[n]
        if letter not in opts:
            issues.append(("KEY-POINTS-NOWHERE", n, f"key says ({letter}), options are {sorted(opts)}"))
            continue
        on, en = nums(opts[letter]), nums(expl)
        if on and en and not (on & en):
            # only flag when the explanation states a final value that is nowhere in the option
            other = [L for L, t in opts.items() if nums(t) & en]
            if other:
                issues.append(("NUMERIC-MISMATCH", n,
                               f"key ({letter})='{opts[letter].strip()[:30]}' but explanation "
                               f"numbers {sorted(en)[:3]} match option(s) {other}"))
    if len(qs) != len(keys):
        issues.append(("COUNT-MISMATCH", 0, f"{len(qs)} questions vs {len(keys)} keys"))
    return issues, len(qs), len(keys)


files = [pathlib.Path(a) for a in sys.argv[1:]] or sorted(
    list(ROOT.glob("topics/*.md")) + list(ROOT.glob("puzzles/*.md")) + list(ROOT.glob("pseudocode/*.md"))
    + list(ROOT.glob("interview/*.md")) + list(ROOT.glob("aptitude/*.md")) + list(ROOT.glob("question-banks/*.md"))
    + list(ROOT.glob("core-course/*.md")))

tot_i = tot_q = tot_k = 0
clean = 0
for f in files:
    iss, nq, nk = check(f)
    tot_q += nq
    tot_k += nk
    if iss:
        tot_i += len(iss)
        print(f"\n{f.relative_to(ROOT)}  ({nq} questions, {nk} keys)")
        for kind, where, msg in iss:
            print(f"   {kind:20s} @{where}: {msg}")
    elif nq:
        clean += 1

print("\n" + "=" * 74)
print(f"{len(files)} files checked · {tot_q} questions · {tot_k} keys · "
      f"{clean} files clean · {tot_i} issues")
print("=" * 74)
sys.exit(1 if tot_i else 0)
