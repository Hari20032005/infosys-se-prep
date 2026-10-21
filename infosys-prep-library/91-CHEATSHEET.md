# 91 — Cheat Sheet

One page of revision. **Every number and formula below is executed by `data/build_cheatsheet.py`** (the run prints how many claims were checked); the last block is method advice that cannot be executed and is counted separately.


## The test

- **60 questions · 75 marks + an essay · 120 minutes**, seven sections, a cut-off in each, no calculator, no coding.
- Seconds a question: Reasoning **100** · Technical **210** · Verbal **60** · Pseudocode **120** · Puzzle **150** · Grammar **120**.
- Marks: Reasoning 15 · Technical 10 · Verbal 20 · Pseudocode 10 (2 each) · Puzzle 10 (2+2+3+3) · Grammar 10 (2 each) = **75**.

## Numbers

- Squares 11–25: 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625.
- Cubes 1–10: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000.
- Triangular numbers: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66.
- Primes below 50: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.
- Fractions: 1/6 = 16.67% · 1/7 = 14.29% · 1/9 = 11.11% · 1/11 = 9.09% · 1/12 = 8.33% · 1/16 = 6.25% · 3/8 = 37.5%.
- Last-digit cycles: 2 → 2,4,8,6 · 3 → 3,9,7,1 · 7 → 7,9,3,1 · 4 → 4,6 · 9 → 9,1.
- Letter anchors: E = 5, J = 10, O = 15, T = 20, Y = 25. BURST = 80, LAKE = 29, VERSATILE = 111.

## Percent

- Up p% then down p% is always a **loss of p²/100 %**: 20% up then 20% down = −4%.
- Two successive discounts of 10% and 20% = **28%**, not 30%.
- Change is measured from the **old** value: 730 → 560 is −23.3%, not −30.4%.
- Mark-up 40% then discount 25% = **5% profit**.

## Algebra

- Heads and legs: 45 heads, 130 legs, cows (4) and hens (2): cows = (130 − 90)/2 = **20**.
- 2x + 3y = 7 and 5x + 8y = 2 give **x = 50, y = −31** (so x > y).
- Ages 48 and 72: three years ago and three years hence give **45 : 75 = 3 : 5**.
- Consecutive numbers: the average is the middle value. Four consecutive evens summing to 132: 30, 32, 34, 36.

## Work

- Two workers together: ab/(a+b). A 12 days, B 15 days → **6⅔ days**. Tap 10 h, leak 15 h → ab/(b−a) = **30 h**.
- Work = men × days: 12 men × 8 days = 96 man-days; 16 men → **6 days**.

## Counting

- n! / repeats!: LEVEL → 5!/(2!·2!) = **30**. C(8,3) = **56**. P(5,3) = **60**. Factors of 360 = (3+1)(2+1)(1+1) = **24**.
- Two dice: 36 outcomes, sum 7 in 6 ways. King or heart: 16/52 = 4/13.

## Mensuration

- Sphere 4πr², (4/3)πr³. r = 3.5: area **154**, volume **179.67** (π = 22/7).
- Cylinder r = 7, h = 10: volume **1540**, curved area **440**. Cone r = 3, h = 4: slant **5**.
- Path 2 m wide outside a 20×12 lawn: (24×16) − 240 = **144** m².

## Non-verbal

- Cube cut into 4³: painted faces 3/2/1/0 → **8 / 24 / 24 / 8**. Squares in a 4×4 grid **30**; rectangles **100**.
- Mirror image of a clock time = 12:00 − t. Mirror of 3:15 is **8:45**.

## Puzzles

- Difference of squares: a² − b² = (a−b)(a+b). (21, 16) → 5 × 37 = **185**. (15, 10) → 125.
- Pair rule a×b + 3: (5,11)→58, (12,8)→99, (16,7)→**115**.
- Four-column rows, d = b×c + a: 8 3 6→26, 4 9 12→112, 5 7 2→19, 9 6 4→**33**.
- Repeated-number table 4,5,6,8,9 → 10, 15, 21, 36, **45** (n(n+1)/2).
- Kakuro sums (digits 1–9, no repeats): 2 cells 16 = 7+9, 17 = 8+9; 3 cells 6 = 1+2+3, 24 = 7+8+9.
- Digit rule (58,75)→5, (96,38)→30, (62,23)→**6** (digit-product of the first minus the second).

## Pseudocode

- `++i` adds 1 **then** uses i; `i++` uses i **then** adds 1. From i = 5: `++i` → 6 (i=6), `i++` → 5 (i=6), `--i` → 4 (i=4), `i--` → 5 (i=4).
- Left to right from i = 2: `++i + ++i` = **7**; `i++ + i++` = 5; `i++ + ++i` = 6; `++i + i++` = 6; i ends at 4.
- Bitwise 12 & 10 = **8**, 12 | 10 = **14**, 12 ^ 10 = **6**; precedence: arithmetic > shifts > relational > & > ^ > | > && > ||.
- `n / 10` on integers drops the last digit; `n mod 10` is the last digit. 123 → digit sum **6**.
- Recursion trace: f(3,4) with f(x,y) = y==0 ? x : f(2x, y−1) is **48**; power 6³ = **216**.

## Method and language (not machine-checkable)

- **Grammar.** since = a point in time; for = a length of time. a/an follows the **sound** (an hour, a university). had + V3 marks the earlier of two past events. Each/every/neither take a singular verb.
- **Grammar.** Passive = be + past participle (future: will be + V3). Look at the word before AND after each cloze blank.
- **Para-jumbles.** Opener: self-contained, no this/that/he/she/however. Pointer words (this, such, those, that is why) must follow what they point to.
- **Critical reasoning.** Assumption: negate it and the argument collapses. Weaken: offer another cause. Inference: must be true, stay inside the passage.
- **Writing.** Four paragraphs, ~190 words, 10 minutes: define → causes → effects → conclusion. Email: subject, purpose line, details, request, polite close, no contractions.
- **Method.** Puzzles: fit the first line, confirm on the second, apply to the third, 2.5-minute cap. Coding-decoding: try letter sum, then position rule, then reverse/shift.
- **Method.** Blood relations: translate symbols into words, draw up/down/side, take gender only from the relation word.
- **Interview.** SDLC, OOP pillars, project (name your part), relocation yes, technologies yes, one true AI-use example. Carry college ID + government ID.
