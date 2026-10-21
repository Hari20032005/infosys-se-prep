#!/usr/bin/env python3
"""Independent re-verification of the GENERATED material.

1. Re-runs every generator with its build seed; each question's check() (a second route to the answer)
   must equal its key -- gen_core.run asserts this.
2. The files on disk must match the regeneration exactly (determinism), so nothing was hand-edited after a check.
3. Pseudocode: every P4 increment question and every Infosys-dialect trace question is re-run as REAL Java
   (javac + java) and compared with the keyed answer.
4. The worked examples written by hand in P4.md are run in Java as well.

    python3 data/verify_generated.py
"""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gen_core, gen_code as GC, gen_oop
import build_topics as B
from lib_common import *

fails = []
print("1-2. regenerate every question bank and compare with disk")
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    before = {p: p.read_text() for p in (ROOT / 'question-banks').glob('QB-*.md')}
    before.update({p: p.read_text() for d in ('topics', 'puzzles', 'pseudocode') for p in (ROOT / d).glob('*.md') if p.name[0] in 'ZAVGWP' and 'adapted_from' not in p.read_text()[:600]})
    B.main()
diff = [p.name for p, t in before.items() if p.read_text() != t]
total_checked = gen_core.STATS['checked']
print(f"   {total_checked} generated questions passed their independent check(); files changed on regeneration: {diff or 'none'}")
if diff: fails.append(f"regeneration changed {diff}")

print("3. real Java on P4 increment questions and P1 dialect traces")
seed = 1000 + sum(ord(c) for c in 'P4')
qs = gen_core.run(GC.gen_incr, seed, 12 + 24)
java = GC.java_incr_check([q['meta'][:3] for q in qs])
bad = 0
for q, line in zip(qs, java):
    res, fin = line.split()
    ask = q['meta'][3]
    want = {'result': res, 'i': fin, 'both': f"{res} {fin}"}[ask]
    if want != q['opts'][0]:
        bad += 1; fails.append(f"P4 Java disagrees: {q['q'][:60]!r} java={want} key={q['opts'][0]}")
print(f"   P4: {len(qs)} questions run in Java, {bad} disagreements")

seed = 5000 + sum(ord(c) for c in 'P1')
tq = gen_core.run(GC.gen_trace, seed, 24)
outs = GC.java_batch([q['prog'] for q in tq])
bad = sum(1 for q, o in zip(tq, outs) if ' '.join(o) != q['opts'][0])
print(f"   P1 traces: {len(tq)} programs run in Java, {bad} disagreements")
if bad: fails.append("P1 Java disagreement")
# the same programs again, but executing the PRINTED text a student reads (parsed back out of each question), not the internal program
codes = [re.search(r'```text\n(.*?)\n```', q['q'], re.S).group(1).split('\n') for q in tq]
touts = GC.java_batch_text(codes)
bad_t = sum(1 for q, o in zip(tq, touts) if ' '.join(o) != q['opts'][0])
print(f"   P1 traces, printed official-dialect text translated to Java and run: {len(tq)} programs, {bad_t} disagreements")
if bad_t: fails.append("P1 printed-text Java disagreement")
seed = 1000 + sum(ord(c) for c in 'P4')

print("4. hand-written P4 examples in Java")
src = """public class Ex { public static void main(String[] a) {
  { int i = 5; int r = ++i; System.out.println("E1a " + r + " " + i); }
  { int i = 5; int r = i++; System.out.println("E1b " + r + " " + i); }
  { int i = 5; int r = i + 1; System.out.println("E1c " + r + " " + i); }
  { int i = 5; int r = --i + 2; System.out.println("E1d " + r + " " + i); }
  { int i = 2; int r = ++i + ++i; System.out.println("E2a " + r + " " + i); }
  { int i = 2; int r = i++ + i++; System.out.println("E2b " + r + " " + i); }
  { int i = 2; int r = i++ + ++i; System.out.println("E2c " + r + " " + i); }
  { int i = 2; int r = ++i + i++; System.out.println("E2d " + r + " " + i); }
  { int i = 7; int r = i-- + i; System.out.println("E4 " + r + " " + i); }
  { int i = 4; int r = ++i - i--; System.out.println("E5 " + r + " " + i); }
  { int x = 0; int k = 0; do { ++x; x--; k++; } while (x >= -1 && k < 5); System.out.println("E3 x=" + x + " passes=" + k); }
} }"""
import tempfile, subprocess
d = pathlib.Path(tempfile.mkdtemp()); (d / 'Ex.java').write_text(src)
r = subprocess.run(['javac', 'Ex.java'], cwd=d, capture_output=True, text=True); assert r.returncode == 0, r.stderr
out = subprocess.run(['java', '-cp', str(d), 'Ex'], capture_output=True, text=True).stdout.split('\n')
exp = {'E1a': '6 6', 'E1b': '5 6', 'E1c': '6 5', 'E1d': '6 4', 'E2a': '7 4', 'E2b': '5 4', 'E2c': '6 4', 'E2d': '6 4', 'E4': '13 6', 'E5': '0 4', 'E3': 'x=0 passes=5'}
got = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in out if l}
for k, v in exp.items():
    ok = got.get(k) == v
    if not ok: fails.append(f"P4 example {k}: java {got.get(k)!r}, text says {v!r}")
print(f"   {sum(got.get(k) == v for k, v in exp.items())}/{len(exp)} hand-written claims match real Java")

print("5. the observed pseudocode pool (P01-P15) re-run as real Java")
import csv
obs = {r['qid']: r['verified_answer'] for r in csv.DictReader(open(ROOT / 'data' / 'questions-observed.csv'))}
jsrc = """import java.util.*;
public class Obs {
  static int fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }
  static int pw(int a, int b) { return b == 0 ? 1 : a * pw(a, b - 1); }
  static int f(int x, int y) { return y == 0 ? x : f(x + y, y - 1); }
  public static void main(String[] args) {
    { StringBuilder o = new StringBuilder(); for (int w = 0; w <= 5; w++) if (w % 2 == 0 && w / 2 == 0) o.append(w).append(' '); System.out.println("P01 " + o.toString().trim()); }
    { int x = 27 % 7; StringBuilder o = new StringBuilder(); for (int i = 0; i <= x; i++) o.append(i).append(' '); System.out.println("P02 " + o.toString().trim()); }
    { int p = 1, q = 1; p = p ^ 1 & 1 + q ^ 1 & 1; System.out.println("P03 " + (p + q)); }
    { int x = 0, k = 0; do { ++x; x--; k++; } while (x >= -1 && k < 50); System.out.println("P04 " + (k == 50 ? "infinite loop printing 1" : "ended")); }
    { int n = 26, i = 0; while (n % 8 != 0) { n = n + 5; i++; } n = n + i; System.out.println("P05 " + n); }
    { int x = 3, y = 2, r = 0; for (int i = 1; i <= y; i++) r = r + x * i; System.out.println("P06 " + r); }
    System.out.println("P07 " + fact(5));
    { int n = 123, s = 0; while (n > 0) { s = s + n % 10; n = n / 10; } System.out.println("P08 " + s); }
    { int n = 6, s = 0; for (int i = 1; i <= n; i++) { if (i % 2 == 0) s = s + i * i; else s = s + i; } System.out.println("P09 " + s); }
    System.out.println("P10 " + pw(6, 3));
    System.out.println("P11 " + f(7, 2));
    { int[] a = {2, 3, 4, 5}; int t = 1; for (int v : a) t *= v; StringBuilder o = new StringBuilder(); for (int v : a) o.append(t / v).append(' '); System.out.println("P12 " + o.toString().trim()); }
    { int i = 5; int r = ++i; System.out.println("P13 " + (r == 6 && i == 6 ? "result = ++i" : "no")); }
    { int i = 2; int r = ++i + ++i; System.out.println("P14 " + r); }
    { int[] a = {1, 2, 2, 3, 4, 5, 1}; int cur = 1, best = 1; for (int i = 1; i < a.length; i++) { if (a[i] > a[i - 1]) { cur++; best = Math.max(best, cur); } else cur = 1; } System.out.println("P15 " + best); }
  }
}"""
d2 = pathlib.Path(tempfile.mkdtemp()); (d2 / 'Obs.java').write_text(jsrc)
r2 = subprocess.run(['javac', 'Obs.java'], cwd=d2, capture_output=True, text=True); assert r2.returncode == 0, r2.stderr[:600]
jout = subprocess.run(['java', '-cp', str(d2), 'Obs'], capture_output=True, text=True).stdout.strip().split('\n')
jg = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in jout}
# P14's keyed answer is the winning expression ('++i + ++i (3 + 4)'); Java prints its value, 7
obs['P14'] = '7' if obs['P14'].startswith('++i + ++i') else obs['P14']
badp = [k for k, v in jg.items() if obs.get(k) != v]
print(f"   {len(jg) - len(badp)}/{len(jg)} observed pseudocode answers match real Java; mismatches: {badp or 'none'}")
if badp: fails.append(f"observed pseudocode Java mismatch {badp}")
print("=" * 70)
print("PASS" if not fails else f"{len(fails)} FAILURES:\n  " + '\n  '.join(fails))
sys.exit(1 if fails else 0)
