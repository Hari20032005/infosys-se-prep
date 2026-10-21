#!/usr/bin/env python3
"""MOCK-01: a full-length Systems Engineer mock in the observed 7-section structure (60 questions + essay,
75 marks + essay, 120 minutes). Questions in MOCK-01.md, answers and working in MOCK-01-ANSWERS.md.
Every generated item carries an independent check(); syllogisms and seating are exhaustively searched;
pseudocode is executed. verify_mock.py re-derives every key.

    python3 data/build_mock.py
"""
import hashlib, pathlib, random, re, sys
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gen_core, gen_puzzles as GP, gen_reasoning as GR, gen_quant as GQ, gen_code as GC, bank_verbal as BV, bank_mock as BM
from gen_core import Q
from lib_common import *

SEED = 2027


def profit_q(rng):
    m, d = rng.choice([(40, 25), (50, 20), (60, 25), (20, 10), (30, 20), (50, 30), (25, 20)])
    cp = rng.choice([200, 400, 500, 800, 1000])
    sp = Fraction(cp) * (100 + m) / 100 * (100 - d) / 100
    pr = (sp - cp) * 100 / cp
    ans = f"{float(pr):g}%" if pr >= 0 else f"{float(-pr):g}% loss"
    wrong = [f"{m - d}%", f"{float(pr) + 5:g}%", f"{float(pr) - 5:g}%"]
    wrong = [w for w in dict.fromkeys(wrong) if w != ans][:3]
    if len(wrong) < 3 or pr == 0: return None
    q = f"A shopkeeper marks an article {m}% above its cost price of ₹{cp} and then allows a discount of {d}% on the marked price. What is his profit percentage?"
    why = f"Marked price = {cp} × {100 + m}/100 = {cp * (100 + m) // 100}. Selling price = marked × {100 - d}/100 = {float(sp):g}. Profit = ({float(sp):g} − {cp}) / {cp} × 100 = **{ans}**. (Not {m} − {d} = {m - d}%: the discount applies to the marked price.)"
    def check():
        x = cp * (100 + m) * (100 - d) / 10000
        p = (x - cp) * 100 / cp
        return f"{p:g}%"
    return Q(q, [ans] + wrong, why, check, 'Profit and discount')


def pick(gen, seed, n=1):
    return gen_core.run(gen, seed, n)


def build():
    gen_core.STATS['generated'] = gen_core.STATS['checked'] = 0
    S = {}
    # ---- 1 Reasoning (15)
    r = []
    r += pick(GR.gen_coding, SEED + 1, 3)
    r += pick(GR.gen_series, SEED + 2, 4)
    r += pick(GR.gen_operator, SEED + 3, 2)
    r += pick(GR.gen_blood, SEED + 4, 1)
    r += [BM.DS]
    r += BM.SYL
    r += BM.seating_questions(seed=7)
    assert len(r) == 15, len(r)
    S['reasoning'] = r
    # ---- 2 Technical Ability (10)
    t = []
    t += pick(GQ.di_freq_table, SEED + 5, 1) + pick(GQ.di_pie, SEED + 6, 1) + pick(GQ.di_bar, SEED + 7, 1)
    t += pick(GQ.gen_linear, SEED + 8, 2)
    t += pick(GQ.gen_mensuration, SEED + 9, 1)
    t += pick(GQ.gen_timework, SEED + 10, 1)
    t += pick(GQ.gen_pc, SEED + 11, 1)
    t += pick(GQ.gen_numsys, SEED + 12, 1)
    t += pick(profit_q, SEED + 13, 1)
    assert len(t) == 10
    S['technical'] = t
    # ---- 3 Verbal (20)
    v = list(BM.RC) + list(BM.ERR) + list(BM.SC) + BV.jumble_questions([18, 19]) + list(BM.VOC) + BV.cr_questions([14, 15])
    assert len(v) == 20, len(v)
    S['verbal'] = v
    # ---- 4 Pseudocode (5)
    p = pick(GC.gen_trace, SEED + 14, 2) + pick(GC.gen_incr, SEED + 15, 1) + [BM.pseudo_recursion(), BM.pseudo_bitwise()]
    S['pseudocode'] = p
    # ---- 5 Puzzle (4): two 2-mark, two 3-mark
    z = pick(lambda rng: GP.gen_mixed(rng, ['pair', 'row3', 'sumgrid', 'seqtable']), SEED + 16, 2) + \
        pick(lambda rng: GP.gen_mixed(rng, ['figure', 'row4', 'digitpair', 'kakuro']), SEED + 17, 2)
    S['puzzle'] = z
    # ---- 6 Grammar (5)
    S['grammar'] = list(BM.CLOZE_MOCK)
    return S


SECTIONS = [
    ('reasoning', 'Section 1 — Reasoning Ability', 15, 15, 25, 1),
    ('technical', 'Section 2 — Technical Ability (mathematical)', 10, 10, 35, 1),
    ('verbal', 'Section 3 — Verbal Ability', 20, 20, 20, 1),
    ('pseudocode', 'Section 4 — Pseudocode', 5, 10, 10, 2),
    ('puzzle', 'Section 5 — Numerical Puzzle', 4, 10, 10, None),
    ('grammar', 'Section 6 — English Grammar', 5, 10, 10, 2),
]


def render(S):
    allq = [q for key, *_ in SECTIONS for q in S[key]]
    n = len(allq)
    targets = letters_for(n, 'MOCK-01')
    qm, km = ['# MOCK-01 — Full-length Systems Engineer mock test\n'], ['# MOCK-01 — Answers and working\n']
    qm.append("""**Structure** (the observed Systems Engineer pattern, `research/03-pattern-synthesis.md` §1): 7 sections, 60 questions, **120 minutes**, **75 marks plus an essay**. No negative marking has been reported, so answer every question.

| # | Section | Questions | Marks | Minutes |
|---|---|---|---|---|
| 1 | Reasoning Ability | 15 | 15 | 25 |
| 2 | Technical Ability (mathematical) | 10 | 10 | 35 |
| 3 | Verbal Ability | 20 | 20 | 20 |
| 4 | Pseudocode | 5 | 10 | 10 |
| 5 | Numerical Puzzle | 4 | 10 (2 + 2 + 3 + 3) | 10 |
| 6 | English Grammar | 5 | 10 | 10 |
| 7 | English Writing | 1 | unpublished | 10 |

**How to sit it.** One sitting, phone away, **no calculator**, rough paper only. Set a timer for each section and **stop when it ends**, even mid-question: the real sections are timed and cannot be revisited `[LIKELY]`. Do not look at `MOCK-01-ANSWERS.md` until the essay is finished.

**Pace.** Reasoning ≈ 100 s a question · Technical ≈ 3.5 min · Verbal ≈ 60 s · Pseudocode ≈ 2 min · Puzzle ≈ 2.5 min · Grammar ≈ 2 min.

---
""")
    km.append("""Mark each answer, add up the sections, and compare with the targets. **Cut-off values for the real test are not known**; one coach says roughly 70% per section applied in the previous year `[UNVERIFIED]`. Use 70% per section as a safe target.

""")
    num = 0
    allkeys = {}
    for key, title, nq, marks, mins, per in SECTIONS:
        qs = S[key]
        assert len(qs) == nq, (key, len(qs), nq)
        tg = targets[num:num + nq]
        qmd, kmd, used = render_questions(qs, 'MOCK-01', start=num + 1, targets=tg)
        qm.append(f"\n## {title}\n\n**{nq} questions · {marks} marks · {mins} minutes**\n")
        if key == 'puzzle':
            qm.append(f"Questions {num + 1} and {num + 2} are worth **2 marks** each; questions {num + 3} and {num + 4} are worth **3 marks** each.\n")
        qm.append(qmd)
        km.append(f"\n## {title}\n\n{kmd}\n")
        allkeys[key] = (num + 1, num + nq, used)
        num += nq
    qm.append(f"\n## Section 7 — English Writing\n\n**1 question · 10 minutes**\n\n{BM.ESSAY_PROMPT}\n")
    km.append("""
## Section 7 — English Writing

There is no key. Mark yourself with this checklist (1 point each, out of 6): on topic · clear introduction · three developed points · a conclusion · grammar and spelling checked · about 190 words. Four or more is a safe pass. Compare your structure with `topics/W1-english-writing.md`.

## Score sheet

| Section | Your score | Out of | Target (70%) |
|---|---|---|---|
| Reasoning Ability | | 15 | 11 |
| Technical Ability | | 10 | 7 |
| Verbal Ability | | 20 | 14 |
| Pseudocode (2 marks each) | | 10 | 7 |
| Numerical Puzzle (2, 2, 3, 3) | | 10 | 7 |
| English Grammar (2 marks each) | | 10 | 7 |
| Writing (checklist) | | 6 | 4 |

Any section under its target is where the next hour goes. Go to the topic file named in the `[tag]` of each question you missed.
""")
    return '\n'.join(qm), '\n'.join(km), allkeys


def main():
    S = build()
    q, k, keys = render(S)
    out = ROOT / 'question-banks'
    (out / 'MOCK-01.md').write_text(q, encoding='utf-8')
    (out / 'MOCK-01-ANSWERS.md').write_text(k, encoding='utf-8')
    total = sum(len(v) for v in S.values())
    import collections
    dist = collections.Counter(l for _, _, u in keys.values() for l in u)
    print(f"MOCK-01: {total} questions across {len(S)} sections + essay; generated/checked {gen_core.STATS['checked']}; letters {dict(sorted(dist.items()))}")


if __name__ == '__main__':
    main()
