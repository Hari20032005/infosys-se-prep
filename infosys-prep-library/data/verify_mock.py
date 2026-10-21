#!/usr/bin/env python3
"""Re-derive every answer in MOCK-01 and compare with the files on disk.
  * regenerate the whole mock (deterministic); every generated question's independent check() must agree;
  * the files on disk must equal the regeneration (no hand edits after verification);
  * syllogism conclusions were decided by exhaustive model search, seating by trying all 120 arrangements
    (asserted inside data/bank_mock.py at import);
  * pseudocode trace and increment questions are re-run as real Java;
  * key count equals question count, and the answer letters are balanced and not a repeating cycle.
"""
import collections, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_mock as M, gen_code as GC, gen_core
from lib_common import ROOT

fails = []
S = M.build()
q_txt, k_txt, keys = M.render(S)
for name, txt in (('MOCK-01.md', q_txt), ('MOCK-01-ANSWERS.md', k_txt)):
    if (ROOT / 'question-banks' / name).read_text() != txt:
        fails.append(f"{name} on disk differs from regeneration")
n_q = sum(len(v) for v in S.values())
n_check = 0
for key, qs in S.items():
    for q in qs:
        got = str(q['check']())
        if got != q['opts'][0]:
            fails.append(f"{key}: check {got!r} != key {q['opts'][0]!r}")
        n_check += 1
print(f"1. {n_check}/{n_q} mock questions re-derived by an independent route; disagreements: {sum('check' in f for f in fails)}")

# real Java for the pseudocode trace and increment questions
pc = S['pseudocode']
traces = [q for q in pc if 'prog' in q]
incs = [q for q in pc if 'meta' in q]
outs = GC.java_batch([q['prog'] for q in traces])
bad = sum(1 for q, o in zip(traces, outs) if ' '.join(o) != q['opts'][0])
java = GC.java_incr_check([q['meta'][:3] for q in incs])
for q, line in zip(incs, java):
    res, fin = line.split(); ask = q['meta'][3]
    if {'result': res, 'i': fin, 'both': f"{res} {fin}"}[ask] != q['opts'][0]: bad += 1
print(f"2. Java re-run of {len(traces) + len(incs)} pseudocode questions, {bad} disagreements")
if bad: fails.append('Java disagreement in the mock')

# key count, letter balance, no repeating cycle
ans = (ROOT / 'question-banks' / 'MOCK-01-ANSWERS.md').read_text()
letters = re.findall(r'(?m)^(\d+)\. \*\*([a-d])\*\*', ans)
nums = [int(n) for n, _ in letters]
if nums != list(range(1, n_q + 1)): fails.append(f"key numbering is {nums[:3]}…{nums[-3:]}, expected 1..{n_q}")
seq = ''.join(l for _, l in letters)
dist = collections.Counter(seq)
cyc = any(seq == (seq[:p] * (len(seq) // p + 1))[:len(seq)] for p in range(1, 9))
print(f"3. {len(letters)} keys for {n_q} questions; letters {dict(sorted(dist.items()))}; repeating cycle: {cyc}")
if len(letters) != n_q: fails.append('key count != question count')
if max(dist.values()) / n_q > 0.32 or cyc: fails.append('letter distribution')
qs_txt = (ROOT / 'question-banks' / 'MOCK-01.md').read_text()
n_opts = len(re.findall(r'(?m)^a\) ', qs_txt))
print(f"4. {n_opts} question stems with options in MOCK-01.md")
if n_opts != n_q: fails.append(f'{n_opts} stems vs {n_q}')
print('=' * 70); print('PASS' if not fails else '\n'.join(fails)); sys.exit(1 if fails else 0)
