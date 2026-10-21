---
title: Pair and figure rules
code: Z2
section: Numerical Puzzle
weightage_pct: 7.6% of marks
est_questions: 2.29
tier: 1
difficulty: Medium
est_study_hours: 1.2
confidence: High
last_updated: 2026-09-30
---

# Z2 — Pair and figure rules

## 1. Why this topic matters here

Expect about **2.3 questions and 5.7 marks** on this topic (about 7.6% of the 75 scored marks). It sits in **Numerical Puzzle**: 4 questions, 10 marks, 10 minutes. **Tier 1**, 1.2 hours to reach reliable recall, confidence **High**.

**13 questions on this topic are in the observed Infosys pool** (Z03, Z04, Z05, Z06, Z08, Z10, Z12, Z13, Z14, Z15, O52, O53, O54), from 3 sources. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 4.77 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

This is the largest family in the observed pool: **ten of the fifteen puzzle items** are "a pair or a figure of numbers gives a value; apply the same rule to the last one". Two marks or three marks each `[REPORTED]`.

| Sub-pattern | How it appears | Observed |
|---|---|---|
| Pair → value with a product and a constant | `(5, 11) → 58`, `(12, 8) → 99`, `(16, 7) → ?` | Z06 |
| Pair → value with squares | `(15, 10) → 125`, `(18, 11) → 203`, `(21, 16) → ?` | Z08 (students called it hard) |
| Opposite pairs → value | `36 & 12 → 48`, `8 & 32 → 40`, `16 & 25 → 41`, `39 & 7 → ?` | Z04 |
| Four outer numbers → centre, with two products | `3, 7, 5, 1 → 16`; `9, 8, 34, 2 → 4`; `15, 12, 21, 8 → ?` | Z03 |
| Four outer numbers → centre, sum of products | `(11, 4) (2, 2) → 48`; `(7, 7) (5, 6) → 79`; `(8, 8) (12, 9) → ?` | Z05 |
| Boxes where each entry is a product | `(2,2)→4, (3,3)→9, (5,4)→20`; `(4,2)→8, (4,3)→12, (?,4)→28` | Z12 |
| Two-digit numbers, digit products | `(58, 75) → 5`, `(96, 38) → 30`, `(62, 23) → ?` | Z13 |
| Two-digit numbers, digit sum of the sum | `(43, 17) → 6`, `(63, 27) → 9`, `(44, 56) → ?` | Z14 |
| Two-digit numbers in rows, digit products added | `35 32 51 / 43 46 61 / ? 30 11` | Z10 |
| Plain product | `(11, 32) → 352`, `(12, 33) → 396`, `(13, 34) → ?` | Z15 |
| **Plus-shaped figure: centre from the four arms** | Arms 7, 4, 6, 8 give 50; arms 1, 12, 20, 7 give 80; find the centre for 13, 11, 9, 14 (centre = 2 × sum of arms) | `[CONFIRMED — official sample 2020]`, O52 |
| **Circles with cubes feeding a box** | 4 and 3 inside circles, box 98; 6 and 2, box 232; then 9 and a letter (box = a³ + b³ + a + b) | `[CONFIRMED — official sample 2020]`, O53 |
| **Zig-zag rows of digit sums** | Rows 16 25 36 49 64 / 14 16 22 23 / 12 X 9: each number is the digit sum of its upper-left neighbour plus the digit sum of its upper-right neighbour | `[CONFIRMED — official sample 2020]`, O54 |

## 3. Concept notes

### 3.1 Where the pair sits

A pair or figure puzzle gives 2–3 worked lines and one blank. The rule is a function of the numbers in the line, not of their position on the page.

### 3.2 The pair-rule catalogue

Try these on the first line, in this order. **a** and **b** are the first and second number of the pair.

| Family | Rules seen or likely | Signal |
|---|---|---|
| Product-based | a×b, a×b ± k, a×(b+1), a×b + a + b, a×b − a − b | Output near the product |
| Sum-based | k(a+b), ka + b, a + kb, (a+b)² | Output near a multiple of the sum |
| Square-based | a² − b², a² + b², a² ± b, a + b² | Output near a square; difference of squares gives (a−b)(a+b) |
| Digit-based (two-digit inputs) | product of digits, digit sum, difference of digit products, digit sum of (a+b) | Outputs far smaller than the inputs |

**Difference of squares shortcut.** a² − b² = (a − b)(a + b). For (15, 10): 5 × 25 = 125 ✓. For (21, 16): 5 × 37 = **185**.

### 3.3 Figure rules (four outer numbers → centre)

Write the four outer numbers as a, b, c, d in reading order (top, right, bottom, left, or as listed). The usual shapes:

| Rule | Example |
|---|---|
| a×b − c×d | `3,7,5,1 → 16`: 3×7 − 5×1 = 16 |
| a×b + c×d | `11,4,2,2 → 48`: 11×4 + 2×2 = 48 |
| Sum of all four + constant | quick to test first |
| Opposite pair sums | `36 & 12 → 48` |

If the figure is drawn as two crossing pairs, pair the numbers **along each axis** (top with bottom, left with right) before trying anything else.

### 3.4 Digit-based rules

Split each two-digit number into tens and units. Try: **product of digits** (5×8 = 40), **sum of digits**, and the **digit sum of a sum or product**.

Z13: `(58, 75) → 5`: digit products 40 and 35; 40 − 35 = 5 ✓. `(96, 38) → 30`: 54 − 24 = 30 ✓. `(62, 23)`: 12 − 6 = **6**.

### 3.5 Eliminating wrong options fast

- **Last digit.** If the rule is a product, the answer's last digit is fixed by the last digits of the factors.
- **Parity.** even × anything is even.
- **Size.** A rule with squares gives an answer close to a square.

### 3.6 The three figure types in the official sample

| Figure | Test first | Why it is quick |
|---|---|---|
| Plus shape, centre unknown | Sum the four arms, then compare with the centre of a worked example (here the centre is exactly twice the sum) | One number to compare; try ×2, ×3, or sum plus a constant |
| Circles feeding a box | Cube each circle number (4³ = 64, 3³ = 27), add, and see what is left over (98 − 91 = 7 = 4 + 3) | Small numbers, so powers are the obvious first guess |
| Zig-zag rows (each row one shorter than the one above) | A cell depends on the **two cells above it**: try sum, difference, product, then digit sums | If the sums are large and the result small, the rule is almost always digit-based |

The generators `cubebox` and `zigzag` in `data/gen_puzzles.py` build these types, and `QB-Z2-pair-and-figure-rules` includes them.

## 4. Must-memorise block

| Item | Values |
|---|---|
| Difference of squares | a² − b² = (a − b)(a + b) |
| Sum of squares identity | (a + b)² = a² + 2ab + b² |
| Squares 11–25 | 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625 |
| Digit product / digit sum | For 58: product 5×8 = 40, sum 5+8 = 13 |

**Rule-testing order:** product → product ± constant → squares → sums → digits.

## 5. Worked examples

**Example 1 — product plus constant (Z06).** `(5, 11) → 58`, `(12, 8) → 99`, `(16, 7) → ?`. 5×11 = 55, +3 = 58; 12×8 = 96, +3 = 99. So 16×7 + 3 = 112 + 3 = **115**.

**Example 2 — difference of squares (Z08).** `(15, 10) → 125`, `(18, 11) → 203`, `(21, 16) → ?`. 225 − 100 = 125 ✓; 324 − 121 = 203 ✓. 441 − 256 = **185**.

**Example 3 — centre from two products (Z03).** `3, 7, 5, 1 → 16`; `9, 8, 34, 2 → 4`; `15, 12, 21, 8 → ?`. 3×7 − 5×1 = 16 ✓; 9×8 − 34×2 = 72 − 68 = 4 ✓. 15×12 − 21×8 = 180 − 168 = **12**.

**Example 4 — centre from a sum of products (Z05).** `(11,4)(2,2) → 48`; `(7,7)(5,6) → 79`; `(8,8)(12,9) → ?`. 44 + 4 = 48 ✓; 49 + 30 = 79 ✓. 64 + 108 = **172**.

**Example 5 — digit products (Z13).** Worked in 3.4: **6**.

**Example 6 — digit sum of a sum (Z14).** `(43, 17) → 6` (60 → 6); `(63, 27) → 9` (90 → 9); `(44, 56)`: 100 → **1**.

**Example 7 — when the rule is ambiguous.** `(3, 14) → 23` and `(2, 18) → 22` fit **a² + b** (9 + 14, 4 + 18). Two lines are rarely enough to rule out every alternative, so check the rule against all the lines before you apply it.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Stopping at a rule that fits one line | Several rules fit one line | Verify on every worked line |
| Applying a digit rule to a plain-number puzzle | Two-digit inputs tempt it | Only go digit-wise when plain arithmetic fails |
| Mixing the pair order | a² − b² is not b² − a² | Keep the order fixed from line one |
| Forgetting the constant | "a×b" fits except for +3 | Compare the product with the output directly |
| Wrong figure axes | Pairing neighbours instead of opposite numbers | Pair numbers along each axis first |
| Spending more than 2.5 minutes | 10 minutes for 4 puzzles | Guess by last digit and move on |

## 7. Practice questions

More questions: [`QB-Z2-pair-and-figure-rules.md`](../question-banks/QB-Z2-pair-and-figure-rules.md).

**1.** **[Powers in a box]** Each set shows four circles and a box. The right-hand circle of each pair holds the square of the left-hand one. Find the value in the last box.

```text
set 1:  top 8, 64   bottom 3, 9   box 84
set 2:  top 6, 36   bottom 4, 16   box 62
set 3:  top 5, 25   bottom 8, 64   box ?
```

a) 129
b) 102
c) 104
d) 89

**2.** **[Figure rule]** Each figure has four outer numbers in the order (a, b, c, d) and one centre number. Find the missing centre number:

```text
outer [9, 6, 7, 3] → centre 48
outer [11, 11, 4, 4] → centre 51
outer [6, 9, 13, 5] → centre 118
outer [5, 5, 12, 9] → centre ?
```

a) 61
b) 56
c) 53
d) 54

**3.** **[Pair rule]** Find the missing number, using the same rule in every line:

```text
(6, 9) → 42
(13, 8) → 45
(14, 4) → 30
(5, 20) → ?
```

a) 82
b) 85
c) 89
d) 75

**4.** **[Figure rule]** Each figure has four outer numbers in the order (a, b, c, d) and one centre number. Find the missing centre number:

```text
outer [5, 6, 3, 11] → centre 73
outer [4, 2, 9, 4] → centre 34
outer [6, 11, 7, 3] → centre 95
outer [15, 10, 12, 14] → centre ?
```

a) 330
b) 340
c) 338
d) 328

**5.** **[Figure rule]** Each figure has four outer numbers in the order (a, b, c, d) and one centre number. Find the missing centre number:

```text
outer [4, 7, 6, 15] → centre 118
outer [2, 14, 2, 6] → centre 40
outer [9, 4, 9, 14] → centre 162
outer [6, 13, 15, 6] → centre ?
```

a) 174
b) 167
c) 176
d) 168

**6.** **[Zig-zag rows]** Each number in a lower row comes from the two numbers above it, by one rule used throughout. Find X.

```text
 12    21    34    43    56
    33    55    77    99
       88     X   176
```

a) 22
b) 129
c) 132
d) 6

**7.** **[Powers in a box]** Each set shows four circles and a box. The right-hand circle of each pair holds the cube of the left-hand one. Find the value in the last box.

```text
set 1:  top 5, 125   bottom 6, 216   box 352
set 2:  top 3, 27   bottom 6, 216   box 252
set 3:  top 3, 27   bottom 7, 343   box ?
```

a) 370
b) 391
c) 380
d) 382

**8.** **[Pair rule]** Find the missing number, using the same rule in every line:

```text
(14, 15) → 421
(5, 14) → 221
(10, 8) → 164
(11, 5) → ?
```

a) 146
b) 154
c) 151
d) 144

**9.** **[Zig-zag rows]** Each number in a lower row comes from the two numbers above it, by one rule used throughout. Find X.

```text
 13    34    73    77    82
    11    17    24    24
       10     X    12
```

a) 41
b) 7
c) 14
d) 5

**10.** **[Zig-zag rows]** Each number in a lower row comes from the two numbers above it, by one rule used throughout. Find X.

```text
 13    14    19    46    69
     9    15    20    25
       15     8     X
```

a) 9
b) 5
c) 7
d) 45

**11.** **[Powers in a box]** Each set shows four circles and a box. The right-hand circle of each pair holds the cube of the left-hand one. Find the value in the last box.

```text
set 1:  top 2, 8   bottom 7, 343   box 360
set 2:  top 4, 64   bottom 8, 512   box 588
set 3:  top 2, 8   bottom 6, 216   box ?
```

a) 224
b) 236
c) 234
d) 232

**12.** **[Pair rule]** Find the missing number, using the same rule in every line:

```text
(3, 19) → 35
(13, 5) → 47
(3, 17) → 31
(7, 5) → ?
```

a) 18
b) 33
c) 21
d) 23

### ANSWER KEY

1. **b** — Box = square of the first + square of the second + the two small numbers added: 64 + 9 + 11 = 84; 36 + 16 + 10 = 62. Set 3: 25 + 64 + 13 = **102**.
2. **b** — The rule that fits all three figures is **centre = a + b×c - d**. [9, 6, 7, 3] → 48; [11, 11, 4, 4] → 51; [6, 9, 13, 5] → 118. For [5, 5, 12, 9] it gives **56**.
3. **b** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **a + 4b**: (6, 9) → 42; (13, 8) → 45; (14, 4) → 30. Applied to (5, 20) it gives **85**. (44 candidate rules were tried; only this one fits.)
4. **a** — The rule that fits all three figures is **centre = a×d + b×c**. [5, 6, 3, 11] → 73; [4, 2, 9, 4] → 34; [6, 11, 7, 3] → 95. For [15, 10, 12, 14] it gives **330**.
5. **d** — The rule that fits all three figures is **centre = a×b + c×d**. [4, 7, 6, 15] → 118; [2, 14, 2, 6] → 40; [9, 4, 9, 14] → 162. For [6, 13, 15, 6] it gives **168**.
6. **c** — The rule is **left + right**. Row 2: (12, 21) → 33; (21, 34) → 55… Row 3: (55, 77) → **132**.
7. **c** — Box = cube of the first + cube of the second + the two small numbers added: 125 + 216 + 11 = 352; 27 + 216 + 9 = 252. Set 3: 27 + 343 + 10 = **380**.
8. **a** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **a² + b²**: (14, 15) → 421; (5, 14) → 221; (10, 8) → 164. Applied to (11, 5) it gives **146**. (44 candidate rules were tried; only this one fits.)
9. **c** — The rule is **digit-sum(left) + digit-sum(right)**. Row 2: (13, 34) → 11; (34, 73) → 17… Row 3: (17, 24) → **14**.
10. **a** — The rule is **digit-sum(left) + digit-sum(right)**. Row 2: (13, 14) → 9; (14, 19) → 15… Row 3: (20, 25) → **9**.
11. **d** — Box = cube of the first + cube of the second + the two small numbers added: 8 + 343 + 9 = 360; 64 + 512 + 12 = 588. Set 3: 8 + 216 + 8 = **232**.
12. **d** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **a×b - a - b**: (3, 19) → 35; (13, 5) → 47; (3, 17) → 31. Applied to (7, 5) it gives **23**. (44 candidate rules were tried; only this one fits.)

## 8. Resources

- **https://prepinsta.com/infosys/puzzle-questions-and-answers-pdf/** — Infosys puzzles with answers; re-solve each yourself before trusting its key.
- **https://prepdrive.in/infosys/puzzle/infosys-puzzle** — Infosys-style number puzzle practice.
- **https://www.indiabix.com/logical-reasoning/number-series/** — number patterns that train the same rule-spotting skill.

## 9. Self-check

1. Can you state the difference-of-squares shortcut and use it on 21 and 16?
2. For `(58, 75) → 5`, can you say which rule gives it and why it is digit-based?
3. Given a four-number figure, can you write the two rules that combine them with products?
4. Can you explain why `a² + b` and `a×b + k` can both fit one line?
5. What are your three quick option-elimination tests?

## 10. Sources

This file was written for this library. **Infosys evidence:** observed questions Z03, Z04, Z05, Z06, Z08, Z10, Z12, Z13, Z14, Z15, O52, O53, O54 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `Z2`). Confidence **High**. Practice questions in §7 and the bank were generated and checked by execution (brute force, simulation or inverse); see `../research/04-qa-report.md`. Nothing here is a published Infosys syllabus.
