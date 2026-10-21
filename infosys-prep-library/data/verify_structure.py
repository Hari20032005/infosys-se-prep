#!/usr/bin/env python3
"""Structural QA for the whole library.

 1. every topic file's frontmatter agrees with data/weightage.json (tier, confidence, hours, questions)
 2. COMPLETENESS: every subtopic and interview theme in weightage.json has a topic file AND a question bank
    inside this library
 3. the ten-section template is present in every main topic file
 4. every internal link resolves and none points outside the library
 5. answer-letter distribution per key block and library-wide; not a repeating cycle
 6. no self-refuting answer-key signatures
 7. every Markdown file ends cleanly; no empty folders
Exit code 1 on any failure.
"""
import collections, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
W = json.loads((ROOT / 'data' / 'weightage.json').read_text())
TOP = {t['code']: t for t in W['topics']}
IVT = {t['code']: t for t in W['interview_topics']}
FM = json.loads((ROOT / 'data' / 'filemap.json').read_text())
fails = []
DIRS = ('topics', 'puzzles', 'pseudocode', 'interview')


def fm_of(p):
    m = re.match(r'---\n(.*?)\n---\n', p.read_text(), re.S)
    return dict(re.findall(r'(?m)^(\w+):\s*(.+)$', m.group(1))) if m else {}


topic_files = [p for d in DIRS for p in sorted((ROOT / d).glob('*.md')) if p.name[:2] != '00']
print("1. FRONTMATTER vs weightage.json")
ok = 0
for p in topic_files:
    f = fm_of(p)
    code = f.get('code')
    t = TOP.get(code) or IVT.get(code)
    if not t:
        fails.append(f"{p.name}: code {code!r} not in weightage.json"); continue
    bad = []
    if f.get('tier') != str(t['tier']): bad.append(('tier', f.get('tier'), t['tier']))
    if f.get('confidence') != t['conf']: bad.append(('confidence', f.get('confidence'), t['conf']))
    if f.get('est_study_hours') != str(t['hours']): bad.append(('est_study_hours', f.get('est_study_hours'), t['hours']))
    want_q = f"{t['est_q']:.2f}" if code in TOP else str(t['questions'])
    if f.get('est_questions') != want_q: bad.append(('est_questions', f.get('est_questions'), want_q))
    if bad:
        for k, g, w in bad: fails.append(f"{p.name}: {k} = {g!r}, weightage.json says {w!r}")
    else:
        ok += 1
print(f"   {ok}/{len(topic_files)} topic files match weightage.json exactly")

print("2. COMPLETENESS: topic file and question bank for every subtopic")
qb = list((ROOT / 'question-banks').glob('QB-*.md'))
miss = 0
for code in list(TOP) + list(IVT):
    mains = [p for p in topic_files if fm_of(p).get('code') == code and 'supporting_for' not in fm_of(p)]
    if not mains:
        fails.append(f"{code}: no topic file"); miss += 1; continue
    banks = [b for b in qb if re.match(rf'QB-{code}-', b.name)]
    txt = mains[0].read_text()
    sec = re.search(r'(?ms)^## 7\. .*?(?=^## 8\. )', txt)
    inline = len(re.findall(r'(?m)^(?:\*\*)?\d+[\.\)]', sec.group(0))) if sec else 0
    if not banks and inline < 5:
        fails.append(f"{code}: no question bank (no QB file and only {inline} inline items)"); miss += 1
print(f"   {len(TOP) + len(IVT)} codes checked, {miss} missing")

print("3. TEN-SECTION TEMPLATE")
REQ = ["Why this topic matters", "Exactly what gets asked", "Concept notes", "Must-memorise", "Worked examples", "Traps", "Practice", "Resources", "Self-check", "Sources"]
n_ok = 0
mains = [p for p in topic_files if 'supporting_for' not in fm_of(p)]
for p in mains:
    txt = p.read_text()
    missing = [r for r in REQ if not re.search(r'(?mi)^##\s*\d*\.?\s*' + re.escape(r), txt)]
    if missing: fails.append(f"{p.name}: missing sections {missing}")
    else: n_ok += 1
print(f"   {n_ok}/{len(mains)} main topic files have all ten sections")

print("4. INTERNAL LINKS (none may leave the library)")
tot = bad = 0
for f in ROOT.rglob('*.md'):
    if '/_' in str(f.relative_to(ROOT)): continue
    text = re.sub(r'(?s)```.*?```', '', f.read_text())
    for m in re.finditer(r'\[[^\]]*\]\(((?!https?:|mailto:|#)[^)\s]+)\)', text):
        tot += 1
        target = (f.parent / m.group(1).split('#')[0]).resolve()
        if not target.exists() or ROOT.resolve() not in target.parents and target != ROOT.resolve():
            bad += 1; fails.append(f"{f.relative_to(ROOT)}: bad link -> {m.group(1)}")
print(f"   {tot - bad}/{tot} internal links resolve inside the library")

print("5. ANSWER LETTERS")
KEY = re.compile(r'(?m)^\s*\*{0,2}(?:Q\s*)?(\d{1,3})[\.\)]?\s*\*{0,2}\s*[-–—]?\s*\*{0,2}\(?([a-d])\)?\*{0,2}\b')
dist, lib = collections.Counter(), collections.Counter()
for f in sorted(ROOT.rglob('*.md')):
    t = f.read_text()
    i = max(t.upper().rfind('ANSWER KEY'), t.upper().rfind('ANSWERS AND WORKING'))
    if i < 0 and 'ANSWERS' not in f.name: continue
    tail = t[i:] if i >= 0 else t
    ks = {}
    for m in KEY.finditer(tail):
        ks.setdefault(int(m.group(1)), m.group(2))
    if len(ks) < 6: continue
    d = collections.Counter(ks.values()); lib.update(d)
    seq = ''.join(ks[k] for k in sorted(ks))
    cyc = len(seq) >= 8 and any(seq == (seq[:p] * (len(seq) // p + 1))[:len(seq)] for p in range(1, 7))
    if max(d.values()) / len(ks) > 0.45 and len(ks) >= 8: fails.append(f"{f.name}: answer letters clustered {dict(d)}")
    if cyc: fails.append(f"{f.name}: answer letters form a repeating cycle {seq[:12]}…")
n = sum(lib.values())
print(f"   {n} keys; library-wide {dict(sorted(lib.items()))}; most common {max(lib.values()) / n:.1%} (target <= 30%)")
if max(lib.values()) / n > 0.30: fails.append(f"library-wide letter skew {max(lib.values()) / n:.1%}")

print("6. SELF-REFUTING SIGNATURES")
SIG = re.compile(r'(correction:|corrected:|corrected answer|so option [a-d]\b|ignore the above)', re.I)
hits = 0
for f in ROOT.rglob('*.md'):
    if f.name == '04-qa-report.md': continue
    for i, l in enumerate(f.read_text().split('\n'), 1):
        if SIG.search(l):
            hits += 1; fails.append(f"{f.relative_to(ROOT)}:{i}: {l.strip()[:80]}")
print(f"   {hits} found (target 0)")

print("7. ENDINGS AND EMPTY FOLDERS")
for f in ROOT.rglob('*.md'):
    if 'data' in f.relative_to(ROOT).parts: continue
    t = f.read_text().rstrip()
    if not t.endswith(('.', '|', '`', ')', ']', '**', '!', '*', '>', ':', '"', '”', '’', '?', '-')) and not t.endswith('</details>'):
        fails.append(f"{f.relative_to(ROOT)}: does not end cleanly -> {t[-40:]!r}")
for d in ROOT.rglob('*'):
    if d.is_dir() and not any(d.iterdir()) and '__pycache__' not in str(d):
        fails.append(f"empty folder: {d.relative_to(ROOT)}")

print("\n8. QUESTION/KEY COUNTS (data/verify_keys.py)")
r = subprocess.run([sys.executable, str(ROOT / 'data' / 'verify_keys.py')], capture_output=True, text=True)
print('   ' + r.stdout.strip().split('\n')[-2])
if r.returncode: fails.append('verify_keys.py reported issues')

print("=" * 74)
if fails:
    print(f"{len(fails)} STRUCTURAL ISSUES:")
    for x in fails: print('   ' + x)
else:
    print('All structural checks passed.')
print("=" * 74)
sys.exit(1 if fails else 0)
