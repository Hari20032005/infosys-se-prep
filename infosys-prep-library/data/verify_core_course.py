#!/usr/bin/env python3
"""Verify the Core Course. Exit 1 on any failure.

    python3 data/verify_core_course.py [--only CODE]

Checks, per lesson: all parts present; prose length and readability gate (parts 1-6 and 8); 15 questions and 15 keys;
answer letters balanced and not a repeating cycle; practice regenerates byte-identically (deterministic); every
generated question's independent check ran (gen_core.run asserts it); the Java checks for pseudocode lessons; the
worked-example assertions in cc_examples.py; difficulty (steps) rises from L1 to L3 and L3 goes beyond the 2020 sample;
every URL in part 9 is a 'used' source in research/06-method-sources.md; no 12-word run copied from the official PDF text.
"""
import pathlib
import re
import statistics
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lib_common import ROOT
import build_core_course as B
import cc_practice as CP
import cc_readability as R
import cc_examples as EX
import gen_code as GC

# Calibrated on the 22 lessons as built: prose 717-1,179 words, average sentence 6.8-9.6 words, Flesch 74-87. The gate leaves room above the worst lesson
# but is tight enough to catch a lesson that drifts into long, hard sentences.
GATE = dict(min_words=700, max_words=1800, max_avg_sentence=14.0, min_flesch=65.0)
JUDGEMENT_ONLY = {'G1', 'G2', 'V1', 'V2', 'V3', 'V6', 'W1', 'A21'}      # no machine-checkable worked examples
OFFICIAL_TXT = pathlib.Path('/private/tmp/claude-501/-Users-hariharansundaramoorthy-Documents-my-projects-infosys/'
                            'bd9015d7-fb83-4fdd-88b1-e9043a0f9b7f/scratchpad/infosys-official-sample.txt')
SOURCES = (ROOT / 'research' / '06-method-sources.md').read_text(encoding='utf-8')
fails = []


def fail(code, msg):
    fails.append(f"{code}: {msg}")


def part(text, n):
    m = re.search(rf'(?ms)^## {n}\. .*?(?=^## \d+\. |\Z)', text)
    return m.group(0) if m else ''


def words_of(s):
    return re.findall(r"[a-z0-9']+", s.lower())


def check_text(code, text):
    for n in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        if not part(text, n):
            fail(code, f"missing part {n}")
    prose = ''.join(part(text, n) for n in (1, 2, 3, 4, 5, 6, 8))
    r = R.readability(prose)
    if not (GATE['min_words'] <= r['words'] <= GATE['max_words']):
        fail(code, f"prose is {r['words']} words (allowed {GATE['min_words']}-{GATE['max_words']})")
    if r['avg_words'] > GATE['max_avg_sentence']:
        fail(code, f"average sentence is {r['avg_words']} words (max {GATE['max_avg_sentence']})")
    if r['flesch'] < GATE['min_flesch']:
        fail(code, f"Flesch reading ease {r['flesch']} (min {GATE['min_flesch']})")
    # sources: every link in part 9 must be a source that research/06 lists
    for url in re.findall(r'\]\((https?://[^)\s]+)\)', part(text, 9)):
        if url not in SOURCES:
            fail(code, f"part 9 cites {url}, which is not in research/06-method-sources.md")
    if not re.search(r'(?m)^- ', part(text, 9)):
        fail(code, "part 9 lists no sources")
    # questions and keys
    prac = part(text, 7)
    key = prac.split('### ANSWER KEY')[-1] if '### ANSWER KEY' in prac else ''
    qs = re.findall(r'(?m)^\*\*(\d{1,2})\.\*\*', prac.split('### ANSWER KEY')[0])
    ks = re.findall(r'(?m)^(\d{1,2})\. \*\*([a-d])\*\*', key)
    if len(qs) != 15 or len(ks) != 15:
        fail(code, f"{len(qs)} questions and {len(ks)} keys (need 15 and 15)")
    letters = ''.join(k[1] for k in ks)
    if letters:
        top = max(letters.count(c) for c in 'abcd')
        if top > 6:
            fail(code, f"answer letter appears {top} times out of 15 (max 6): {letters}")
        if any(letters == (letters[:p] * (len(letters) // p + 1))[:len(letters)] for p in range(1, 6)):
            fail(code, f"answer letters repeat in a cycle: {letters}")
    if code != 'A6' and any(letters[i] == letters[i + 1] == letters[i + 2] for i in range(len(letters) - 2)):
        fail(code, f"the same answer letter three times in a row: {letters}")
    for lvl in (1, 2, 3):
        if f"### {B.LEVELS[lvl]}" not in prac:
            fail(code, f"missing heading for {B.LEVELS[lvl]}")
    return r, letters


def check_practice(code, text):
    """Regenerate, compare with disk, run Java for code lessons, check difficulty metadata."""
    sets = CP.PRACTICE[code]()
    if B.lesson_text(code) != text:
        fail(code, "regenerating the lesson does not reproduce the file on disk (stale or non-deterministic)")
    allq = [q for lvl in (1, 2, 3) for q in sets[lvl]]
    for q in allq:
        if not q.get('judgement') and not callable(q.get('check')):
            fail(code, f"question without an independent check: {q['q'][:50]!r}")
    # Java
    metas = [q for q in allq if 'meta' in q]
    if metas:
        java = GC.java_incr_check([q['meta'][:3] for q in metas])
        for q, line in zip(metas, java):
            res, fin = line.split()
            want = {'result': res, 'i': fin, 'both': f"{res} {fin}"}[q['meta'][3]]
            if want != q['opts'][0]:
                fail(code, f"Java disagrees with the key for {q['q'][:50]!r}: java {want}, key {q['opts'][0]}")
    traces = [q for q in allq if 'prog' in q]
    if traces:
        codes = [re.search(r'```text\n(.*?)\n```', q['q'], re.S).group(1).split('\n') for q in traces]
        for q, out in zip(traces, GC.java_batch_text(codes)):
            if ' '.join(out) != q['opts'][0]:
                fail(code, f"printed trace run as Java gives {' '.join(out)!r}, key says {q['opts'][0]!r}")
    jq = [q for q in allq if 'jcode' in q]
    if jq:
        for q, out in zip(jq, GC.java_batch_text([q['jcode'] for q in jq])):
            if ' '.join(out) != q['opts'][0]:
                fail(code, f"printed program run as Java gives {' '.join(out)!r}, key says {q['opts'][0]!r}: {q['q'][:60]!r}")
    # difficulty
    means = []
    for lvl in (1, 2, 3):
        st = [q['steps'] for q in sets[lvl] if q.get('steps')]
        means.append(statistics.mean(st) if st else None)
    if all(m is not None for m in means):
        if not (means[0] < means[1] < means[2]):
            fail(code, f"mean steps do not rise L1<L2<L3: {means}")
        hard = sum(1 for q in sets[3] if q.get('steps', 0) > CP.OFFICIAL_MAX_STEPS)
        if code == 'Z2' and hard < 3:
            fail(code, f"only {hard} Level 3 puzzles go beyond the official sample's {CP.OFFICIAL_MAX_STEPS} steps (need 3)")
    return means


def check_examples(code):
    if code in EX.EXAMPLES:
        res = EX.EXAMPLES[code]()
        bad = [lbl for lbl, ok in res if not ok]
        for b in bad:
            fail(code, f"worked-example claim failed: {b}")
        return len(res)
    if code not in JUDGEMENT_ONLY:
        fail(code, "no worked-example checks in cc_examples.py (and the lesson is not marked judgement-only)")
    return 0


def check_copy(code, text):
    """No run of 12 words copied from the official sample PDF text (lessons paraphrase only)."""
    if not OFFICIAL_TXT.exists():
        return None
    off = words_of(OFFICIAL_TXT.read_text(encoding='utf-8', errors='replace'))
    runs = {' '.join(off[i:i + 12]) for i in range(len(off) - 11)}
    mine = words_of(re.sub(r'(?s)```.*?```', ' ', text))
    for i in range(len(mine) - 11):
        if ' '.join(mine[i:i + 12]) in runs:
            fail(code, f"12-word run copied from the official sample: {' '.join(mine[i:i + 12])!r}")
            return False
    return True


def main(argv):
    only = argv[argv.index('--only') + 1] if '--only' in argv else None
    codes = [only] if only else [c for _, c, slug, _ in B.LESSONS if (B.OUT / f'{B.BY_CODE[c][0]:02d}-{c}-{B.BY_CODE[c][1]}.md').exists()]
    if not codes:
        print("verify_core_course: 0 lessons found")
        return 0
    n_ex = 0
    for code in codes:
        n, slug, _ = B.BY_CODE[code]
        path = B.OUT / f'{n:02d}-{code}-{slug}.md'
        text = path.read_text(encoding='utf-8')
        r, letters = check_text(code, text)
        means = check_practice(code, text)
        n_ex += check_examples(code)
        cp = check_copy(code, text)
        print(f"  {code:4s} {r['words']:5d} words · avg sentence {r['avg_words']:4.1f} · Flesch {r['flesch']:4.1f} · keys {letters} · "
              f"steps {[round(m, 1) if m else None for m in means]} · copy-check {'skipped' if cp is None else 'clean'}")
    if not only and len(codes) == len(B.LESSONS):
        sh, l48 = (B.OUT / '00-START-HERE.md'), (B.OUT / '99-LAST-48-HOURS.md')
        if not sh.exists() or not l48.exists():
            fail('pages', "00-START-HERE.md or 99-LAST-48-HOURS.md is missing")
        else:
            if sh.read_text(encoding='utf-8') != B.start_here() or l48.read_text(encoding='utf-8') != B.last_48():
                fail('pages', "the two navigation pages do not match a fresh build")
            t = sh.read_text(encoding='utf-8')
            for n, c, _, _ in B.LESSONS:
                if B.lesson_file(c) not in t:
                    fail('pages', f"00-START-HERE does not link to lesson {n:02d} {c}")
            if len(re.findall(r'(?m)^### \d+\. ', l48.read_text(encoding='utf-8'))) != len(B.LESSONS):
                fail('pages', "99-LAST-48-HOURS does not hold 22 recaps")
            print("  pages: 00-START-HERE and 99-LAST-48-HOURS match a fresh build; every lesson is linked; 22 recaps")
    print(f"verify_core_course: {len(codes)} lesson(s), {n_ex} worked-example claims executed, {len(fails)} failure(s)")
    for f in fails:
        print("  FAIL", f)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
