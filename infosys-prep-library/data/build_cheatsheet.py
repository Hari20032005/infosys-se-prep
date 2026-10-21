#!/usr/bin/env python3
"""91-CHEATSHEET.md. Every numeric or formula claim is paired with a check that is EXECUTED here;
qualitative claims (grammar rules, method lines) are listed separately and counted as unchecked.
    python3 data/build_cheatsheet.py            # writes the file and runs the checks
    python3 data/build_cheatsheet.py --verify   # regenerates in memory and compares with the file on disk
"""
import itertools, json, math, pathlib, sys
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lib_common import ROOT, W

C = []   # (section, markdown line, check or None)


def add(sec, line, check=None):
    C.append((sec, line, check))


pos = lambda c: ord(c) - 64
# ----------------------------------------------------------------------- the test
S = W['sections']
add('The test', f"**{W['total_questions']} questions · {W['total_marks_excl_essay']} marks + an essay · {W['total_minutes']} minutes**, seven sections, a cut-off in each, no calculator, no coding.",
    lambda: W['total_questions'] == 60 and W['total_marks_excl_essay'] == 75 and W['total_minutes'] == 120)
add('The test', "Seconds a question: Reasoning **100** · Technical **210** · Verbal **60** · Pseudocode **120** · Puzzle **150** · Grammar **120**.",
    lambda: [round(25 * 60 / 15), round(35 * 60 / 10), round(20 * 60 / 20), round(10 * 60 / 5), round(10 * 60 / 4), round(10 * 60 / 5)] == [100, 210, 60, 120, 150, 120])
add('The test', "Marks: Reasoning 15 · Technical 10 · Verbal 20 · Pseudocode 10 (2 each) · Puzzle 10 (2+2+3+3) · Grammar 10 (2 each) = **75**.", lambda: 15 + 10 + 20 + 10 + 10 + 10 == 75 and 2 + 2 + 3 + 3 == 10)
# ----------------------------------------------------------------------- number facts
add('Numbers', "Squares 11–25: 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625.", lambda: [n * n for n in range(11, 26)] == [121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625])
add('Numbers', "Cubes 1–10: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000.", lambda: [n ** 3 for n in range(1, 11)] == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])
add('Numbers', "Triangular numbers: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66.", lambda: [n * (n + 1) // 2 for n in range(1, 12)] == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66])
add('Numbers', "Primes below 50: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.", lambda: [p for p in range(2, 50) if all(p % d for d in range(2, p))] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
add('Numbers', "Fractions: 1/6 = 16.67% · 1/7 = 14.29% · 1/9 = 11.11% · 1/11 = 9.09% · 1/12 = 8.33% · 1/16 = 6.25% · 3/8 = 37.5%.",
    lambda: [round(100 / d, 2) for d in (6, 7, 9, 11, 12, 16)] == [16.67, 14.29, 11.11, 9.09, 8.33, 6.25] and 3 / 8 * 100 == 37.5)
add('Numbers', "Last-digit cycles: 2 → 2,4,8,6 · 3 → 3,9,7,1 · 7 → 7,9,3,1 · 4 → 4,6 · 9 → 9,1.",
    lambda: all([pow(b, k, 10) for k in range(1, n + 1)] == cyc for b, n, cyc in ((2, 4, [2, 4, 8, 6]), (3, 4, [3, 9, 7, 1]), (7, 4, [7, 9, 3, 1]), (4, 2, [4, 6]), (9, 2, [9, 1]))))
add('Numbers', "Letter anchors: E = 5, J = 10, O = 15, T = 20, Y = 25. BURST = 80, LAKE = 29, VERSATILE = 111.",
    lambda: (pos('E'), pos('J'), pos('O'), pos('T'), pos('Y')) == (5, 10, 15, 20, 25) and sum(map(pos, 'BURST')) == 80 and sum(map(pos, 'LAKE')) == 29 and sum(map(pos, 'VERSATILE')) == 111)
# ----------------------------------------------------------------------- percentages and money
add('Percent', "Up p% then down p% is always a **loss of p²/100 %**: 20% up then 20% down = −4%.", lambda: abs((1.2 * 0.8 - 1) * 100 + 4) < 1e-9 and abs((1.1 * 0.9 - 1) * 100 + 1) < 1e-9)
add('Percent', "Two successive discounts of 10% and 20% = **28%**, not 30%.", lambda: abs((1 - 0.9 * 0.8) * 100 - 28) < 1e-9)
add('Percent', "Change is measured from the **old** value: 730 → 560 is −23.3%, not −30.4%.", lambda: round((560 - 730) / 730 * 100, 1) == -23.3 and round((560 - 730) / 560 * 100, 1) == -30.4)
add('Percent', "Mark-up 40% then discount 25% = **5% profit**.", lambda: abs(1.4 * 0.75 - 1.05) < 1e-12)
# ----------------------------------------------------------------------- algebra and work
add('Algebra', "Heads and legs: 45 heads, 130 legs, cows (4) and hens (2): cows = (130 − 90)/2 = **20**.", lambda: (130 - 45 * 2) // 2 == 20 and 20 * 4 + 25 * 2 == 130)
add('Algebra', "2x + 3y = 7 and 5x + 8y = 2 give **x = 50, y = −31** (so x > y).", lambda: 2 * 50 + 3 * -31 == 7 and 5 * 50 + 8 * -31 == 2)
add('Algebra', "Ages 48 and 72: three years ago and three years hence give **45 : 75 = 3 : 5**.", lambda: Fraction(45, 75) == Fraction(3, 5))
add('Algebra', "Consecutive numbers: the average is the middle value. Four consecutive evens summing to 132: 30, 32, 34, 36.", lambda: sum([30, 32, 34, 36]) == 132 and 132 / 4 == 33)
add('Work', "Two workers together: ab/(a+b). A 12 days, B 15 days → **6⅔ days**. Tap 10 h, leak 15 h → ab/(b−a) = **30 h**.", lambda: Fraction(12 * 15, 27) == Fraction(20, 3) and Fraction(10 * 15, 5) == 30)
add('Work', "Work = men × days: 12 men × 8 days = 96 man-days; 16 men → **6 days**.", lambda: 12 * 8 // 16 == 6)
add('Counting', "n! / repeats!: LEVEL → 5!/(2!·2!) = **30**. C(8,3) = **56**. P(5,3) = **60**. Factors of 360 = (3+1)(2+1)(1+1) = **24**.",
    lambda: math.factorial(5) // (2 * 2) == 30 and math.comb(8, 3) == 56 and math.perm(5, 3) == 60 and len([d for d in range(1, 361) if 360 % d == 0]) == 24)
add('Counting', "Two dice: 36 outcomes, sum 7 in 6 ways. King or heart: 16/52 = 4/13.", lambda: sum(1 for a, b in itertools.product(range(1, 7), repeat=2) if a + b == 7) == 6 and Fraction(16, 52) == Fraction(4, 13))
# ----------------------------------------------------------------------- mensuration and non-verbal
add('Mensuration', "Sphere 4πr², (4/3)πr³. r = 3.5: area **154**, volume **179.67** (π = 22/7).", lambda: 4 * Fraction(22, 7) * Fraction(7, 2) ** 2 == 154 and round(float(Fraction(4, 3) * Fraction(22, 7) * Fraction(7, 2) ** 3), 2) == 179.67)
add('Mensuration', "Cylinder r = 7, h = 10: volume **1540**, curved area **440**. Cone r = 3, h = 4: slant **5**.", lambda: Fraction(22, 7) * 49 * 10 == 1540 and 2 * Fraction(22, 7) * 7 * 10 == 440 and math.hypot(3, 4) == 5)
add('Mensuration', "Path 2 m wide outside a 20×12 lawn: (24×16) − 240 = **144** m².", lambda: 24 * 16 - 20 * 12 == 144)
add('Non-verbal', "Cube cut into 4³: painted faces 3/2/1/0 → **8 / 24 / 24 / 8**. Squares in a 4×4 grid **30**; rectangles **100**.",
    lambda: [8, 12 * 2, 6 * 4, 2 ** 3] == [8, 24, 24, 8] and sum(i * i for i in range(1, 5)) == 30 and (4 * 5 // 2) ** 2 == 100)
add('Non-verbal', "Mirror image of a clock time = 12:00 − t. Mirror of 3:15 is **8:45**.", lambda: 12 * 60 - (3 * 60 + 15) == 8 * 60 + 45)
# ----------------------------------------------------------------------- puzzles
add('Puzzles', "Difference of squares: a² − b² = (a−b)(a+b). (21, 16) → 5 × 37 = **185**. (15, 10) → 125.", lambda: 21 * 21 - 16 * 16 == 185 == 5 * 37 and 15 * 15 - 10 * 10 == 125)
add('Puzzles', "Pair rule a×b + 3: (5,11)→58, (12,8)→99, (16,7)→**115**.", lambda: [5 * 11 + 3, 12 * 8 + 3, 16 * 7 + 3] == [58, 99, 115])
add('Puzzles', "Four-column rows, d = b×c + a: 8 3 6→26, 4 9 12→112, 5 7 2→19, 9 6 4→**33**.", lambda: [3 * 6 + 8, 9 * 12 + 4, 7 * 2 + 5, 6 * 4 + 9] == [26, 112, 19, 33])
add('Puzzles', "Repeated-number table 4,5,6,8,9 → 10, 15, 21, 36, **45** (n(n+1)/2).", lambda: [n * (n + 1) // 2 for n in (4, 5, 6, 8, 9)] == [10, 15, 21, 36, 45])
add('Puzzles', "Kakuro sums (digits 1–9, no repeats): 2 cells 16 = 7+9, 17 = 8+9; 3 cells 6 = 1+2+3, 24 = 7+8+9.",
    lambda: [c for c in itertools.combinations(range(1, 10), 2) if sum(c) == 16] == [(7, 9)] and [c for c in itertools.combinations(range(1, 10), 2) if sum(c) == 17] == [(8, 9)]
    and [c for c in itertools.combinations(range(1, 10), 3) if sum(c) == 6] == [(1, 2, 3)] and [c for c in itertools.combinations(range(1, 10), 3) if sum(c) == 24] == [(7, 8, 9)])
add('Puzzles', "Digit rule (58,75)→5, (96,38)→30, (62,23)→**6** (digit-product of the first minus the second).", lambda: (5 * 8 - 7 * 5, 9 * 6 - 3 * 8, 6 * 2 - 2 * 3) == (5, 30, 6))
# ----------------------------------------------------------------------- pseudocode
def _inc(expr, i):
    j = i
    vals = []
    for t in expr:
        if t == '++i': j += 1; vals.append(j)
        elif t == 'i++': vals.append(j); j += 1
        elif t == '--i': j -= 1; vals.append(j)
        elif t == 'i--': vals.append(j); j -= 1
    return vals, j
add('Pseudocode', "`++i` adds 1 **then** uses i; `i++` uses i **then** adds 1. From i = 5: `++i` → 6 (i=6), `i++` → 5 (i=6), `--i` → 4 (i=4), `i--` → 5 (i=4).",
    lambda: _inc(['++i'], 5) == ([6], 6) and _inc(['i++'], 5) == ([5], 6) and _inc(['--i'], 5) == ([4], 4) and _inc(['i--'], 5) == ([5], 4))
add('Pseudocode', "Left to right from i = 2: `++i + ++i` = **7**; `i++ + i++` = 5; `i++ + ++i` = 6; `++i + i++` = 6; i ends at 4.",
    lambda: [sum(_inc(e, 2)[0]) for e in (['++i', '++i'], ['i++', 'i++'], ['i++', '++i'], ['++i', 'i++'])] == [7, 5, 6, 6] and _inc(['++i', '++i'], 2)[1] == 4)
add('Pseudocode', "Bitwise 12 & 10 = **8**, 12 | 10 = **14**, 12 ^ 10 = **6**; precedence: arithmetic > shifts > relational > & > ^ > | > && > ||.", lambda: (12 & 10, 12 | 10, 12 ^ 10) == (8, 14, 6) and (1 ^ 1 & 1 + 1 ^ 1 & 1) == (1 ^ (1 & (1 + 1)) ^ (1 & 1)))
add('Pseudocode', "`n / 10` on integers drops the last digit; `n mod 10` is the last digit. 123 → digit sum **6**.", lambda: 123 // 10 == 12 and 123 % 10 == 3 and sum(map(int, '123')) == 6)
add('Pseudocode', "Recursion trace: f(3,4) with f(x,y) = y==0 ? x : f(2x, y−1) is **48**; power 6³ = **216**.", lambda: (lambda f: f(3, 4))(lambda x, y: x if y == 0 else (lambda g: g(g, x, y))(lambda g, a, b: a if b == 0 else g(g, 2 * a, b - 1))) == 48 and 6 ** 3 == 216)
# ----------------------------------------------------------------------- qualitative (not machine-checkable)
Q_LINES = [
    ('Grammar', "since = a point in time; for = a length of time. a/an follows the **sound** (an hour, a university). had + V3 marks the earlier of two past events. Each/every/neither take a singular verb."),
    ('Grammar', "Passive = be + past participle (future: will be + V3). Look at the word before AND after each cloze blank."),
    ('Para-jumbles', "Opener: self-contained, no this/that/he/she/however. Pointer words (this, such, those, that is why) must follow what they point to."),
    ('Critical reasoning', "Assumption: negate it and the argument collapses. Weaken: offer another cause. Inference: must be true, stay inside the passage."),
    ('Writing', "Four paragraphs, ~190 words, 10 minutes: define → causes → effects → conclusion. Email: subject, purpose line, details, request, polite close, no contractions."),
    ('Method', "Puzzles: fit the first line, confirm on the second, apply to the third, 2.5-minute cap. Coding-decoding: try letter sum, then position rule, then reverse/shift."),
    ('Method', "Blood relations: translate symbols into words, draw up/down/side, take gender only from the relation word."),
    ('Interview', "SDLC, OOP pillars, project (name your part), relocation yes, technologies yes, one true AI-use example. Carry college ID + government ID."),
]


def render():
    out = ["# 91 — Cheat Sheet\n", "One page of revision. **Every number and formula below is executed by `data/build_cheatsheet.py`** (the run prints how many claims were checked); the last block is method advice that cannot be executed and is counted separately.\n"]
    sec = None
    for s, line, _ in C:
        if s != sec:
            out.append(f"\n## {s}\n"); sec = s
        out.append(f"- {line}")
    out.append("\n## Method and language (not machine-checkable)\n")
    for s, line in Q_LINES:
        out.append(f"- **{s}.** {line}")
    out.append("")
    return '\n'.join(out)


def run_checks():
    ok = bad = 0
    for s, line, chk in C:
        if chk is None: continue
        try:
            good = bool(chk())
        except Exception as e:
            good = False
        if good: ok += 1
        else:
            bad += 1; print('FAILED CLAIM:', s, '|', line)
    return ok, bad


if __name__ == '__main__':
    ok, bad = run_checks()
    text = render()
    path = ROOT / '91-CHEATSHEET.md'
    if '--verify' in sys.argv:
        same = path.exists() and path.read_text() == text
        print(f"verify_cheatsheet: {ok} numeric/formula claims executed, {bad} failed, {len(Q_LINES)} qualitative lines unchecked; file matches regeneration: {same}")
        sys.exit(0 if (bad == 0 and same) else 1)
    path.write_text(text, encoding='utf-8')
    print(f"cheatsheet written: {ok} claims checked, {bad} failed, {len(Q_LINES)} qualitative lines unchecked")
    sys.exit(1 if bad else 0)
