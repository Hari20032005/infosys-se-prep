---
title: Number grids and matrices
code: Z1
section: Numerical Puzzle
weightage_pct: 5.7% of marks
est_questions: 1.71
tier: 1
difficulty: Easy
est_study_hours: 1.2
confidence: High
last_updated: 2026-09-30
---

# Z1 — Number grids and matrices

## 1. Why this topic matters here

Expect about **1.7 questions and 4.3 marks** on this topic (about 5.7% of the 75 scored marks). It sits in **Numerical Puzzle**: 4 questions, 10 marks, 10 minutes. **Tier 1**, 1.2 hours to reach reliable recall, confidence **High**.

**6 questions on this topic are in the observed Infosys pool** (Z01, Z02, Z07, Z09, Z11, O51), from 2 sources. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 3.57 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

The Numerical Puzzle section is **4 questions in 10 minutes, worth 10 marks**: two questions worth 2 marks and two worth 3 marks `[REPORTED]`. Coaches describe a mix of easy and difficult items, including 3×3 and 4×4 matrix puzzles, and say puzzle and verbal were the two sections most candidates failed the cut-off on `[REPORTED]` (YT-5XTG, Oct 2025).

| Sub-pattern | How it appears | Observed |
|---|---|---|
| Four-column rows, last number from the first three | `8 3 6 → 26`, `4 9 12 → 112`, `5 7 2 → 19`, `9 6 4 → ?` (rule: second × third + first) | Z07 |
| Rows built from a pair, its product and its square | `7 6 42 36`, `8 4 32 16`, `10 12 120 ?` | Z02 |
| Three-column rows, blank in the first column | `20 4 5`, `48 6 8`, `? 8 4` (first = second × third) | Z09 |
| Every row adds up to the same total | 4×4 grid of small numbers, one blank | Z01 |
| Repeated-number table | `4 4 10`, `5 5 15`, `6 6 21`, `8 8 36`, `9 9 ?` (triangular numbers) | Z11 |
| Distinct-digit grid with row and column sums (Kakuro style) | "numbers in each row and column must be unique and add up to the number given" | `[REPORTED]` by an aggregator; no instance recovered |
| **Two 3×3 grids: the row sums of the first run on into the second** | First grid's row sums 12, 15, 18; second grid has one blank; the sums continue 21, 24, 27 (3 marks) | `[CONFIRMED — official sample 2020]`, item O51 |

Two facts from the coaches worth using: the rule is **the same for every row or column of the puzzle** (YT-6UFT: "that logic should work everywhere"), and if the numbers are big, the rule usually runs down the **column** rather than along the row.

## 3. Concept notes

### 3.1 The one-minute method

1. **Look at the shape.** Rows of three or four numbers, or a grid with a constant total? Are the last numbers much bigger than the others (product/square) or smaller (difference/digit work)?
2. **Fit the first row only.** Try the rules in the ladder below, cheapest first. Stop at the first rule that reproduces the row.
3. **Confirm on the second row.** If it fails, discard the rule. Do not bend it with a constant to fit.
4. **Apply to the last row.** Compare with the options. If two options survive, check the last digit or parity.
5. **Time cap: 2.5 minutes** (10 minutes for 4 puzzles). No negative marking has been reported, so guess and move on.

### 3.2 The rule ladder for rows

Try these in order on `a b c → d` (or `a b → c`):

| Order | Rule | Quick signal |
|---|---|---|
| 1 | Sum of the numbers | Answer a bit larger than the largest input |
| 2 | Difference | Answer smaller than the inputs |
| 3 | Product of two numbers | Answer much larger; last digit = product of last digits |
| 4 | Product ± a number | Product fits except for a small constant gap |
| 5 | Square of one number ± another | Answer near a perfect square |
| 6 | Product of two, plus (or minus) the third | Most four-column rows (Z07: `b × c + a`) |
| 7 | Pair, product, square (`a, b, a×b, b²`) | The third equals the product of the first two (Z02) |
| 8 | Division then something | Answer smaller; inputs divisible |
| 9 | Digit-wise rules | Two-digit inputs, small outputs |

### 3.3 Grids with a constant total

If each row (or column) of a grid adds up to the same number, the missing entry is **total − the others**. Find the total from any complete row. Z01: rows 1, 2, 3 each sum to 15 (1+5+6+3, 9+1+2+3, 1+1+6+7), so the last row's blank is 15 − (4+1+2) = **8**.

### 3.4 Repeated-number tables

When the first two columns repeat (`4 4`, `5 5`), only one number matters. Write the third numbers against n and look for a formula:

| n | 4 | 5 | 6 | 8 | 9 |
|---|---|---|---|---|---|
| third | 10 | 15 | 21 | 36 | **45** |

10, 15, 21, 36 are n(n+1)/2 → 9 × 10 / 2 = **45**.

### 3.5 Distinct-digit sum grids (Kakuro style)

Each row and column holds **different digits from 1 to 9** and adds to the number given. Method: find a line with exactly one empty cell and subtract; repeat. When two cells are empty in a line, list the digit pairs that make the sum and strike out digits already in that line or crossing line.

Sums with a single digit pair or triple worth memorising:

| Sum | In 2 cells | Sum | In 3 cells |
|---|---|---|---|
| 3 | 1+2 | 6 | 1+2+3 |
| 4 | 1+3 | 7 | 1+2+4 |
| 16 | 7+9 | 23 | 6+8+9 |
| 17 | 8+9 | 24 | 7+8+9 |

### 3.6 Two grids, one series (official sample)

When the puzzle shows **two** grids of nine numbers, "the second works the same way as the first" does not mean the same rule row for row. In the official sample the first grid's row sums are 12, 15, 18 (a step of 3) and the second grid's rows continue the same series: 21, 24, 27. So find the series from grid one, carry it on, and solve the blank as `sum − the other two cells`. The generator `gridsums` in `data/gen_puzzles.py` builds this type, and the bank `QB-Z1-number-grids-and-matrices` includes it.

## 4. Must-memorise block

| Item | Values |
|---|---|
| Squares 1–20 | 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400 |
| Cubes 1–10 | 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000 |
| Triangular numbers | 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66 |
| Last-digit test | The last digit of a product depends only on the last digits of the factors |
| Parity test | even × anything = even; odd × odd = odd; odd + odd = even |

**Reading order:** row-wise first; if the numbers are big, column-wise; if neither works, digit-wise; if that fails, look for a repeated number.

## 5. Worked examples

**Example 1 — four-column rows (observed Z07).** Rows `8 3 6 26`, `4 9 12 112`, `5 7 2 19`, `9 6 4 ?`.
Try product of the last two: 3×6 = 18, 18 + 8 = 26 ✓. Second row: 9×12 = 108, + 4 = 112 ✓. Third: 7×2 = 14, + 5 = 19 ✓. Last row: 6×4 = 24, + 9 = **33**.

**Example 2 — pair, product, square (Z02).** `7 6 42 36`, `8 4 32 16`, `10 12 120 ?`. Third = first × second (7×6 = 42), fourth = second squared (6² = 36). Last row: 12² = **144**.

**Example 3 — blank in the first column (Z09).** `20 4 5`, `48 6 8`, `? 8 4`. First = second × third (4×5 = 20, 6×8 = 48). So ? = 8×4 = **32**.

**Example 4 — constant row total (Z01).** Each row totals 15. Last row `4 1 2 ?` → 15 − 7 = **8**.

**Example 5 — a Kakuro-style grid.** Row totals on the left, column totals on top; `.` is empty.

```text
         13  13  16
   15 |   4   .   8
   15 |   .   2   .
   12 |   1   .   .
```

Peel one unknown at a time:
1. Row 1 has one empty cell: 15 − 4 − 8 = **3**.
2. Column 1 now has one empty cell: 13 − 4 − 1 = **8** (row 2, column 1).
3. Column 2 has one empty cell: 13 − 3 − 2 = **8** (row 3, column 2).
4. Row 2 has one empty cell: 15 − 8 − 2 = **5**.
5. Row 3 has one empty cell: 12 − 1 − 8 = **3**.

Result `4 3 8 / 8 2 5 / 1 8 3`. Check: no repeats in any row or column, columns 13, 13, 16 ✓. (A search over all fillings confirms it is the only one.)

**Example 6 — repeated numbers (Z11).** Worked in 3.4: **45**.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Fitting a rule to the first row only | Many rules fit one row | Confirm on the second row before using it |
| Adding a constant to force a fit | "+3" on one row, "+5" on the next is not a rule | The rule must be the same in every row |
| Reading across when the rule runs down | Big numbers usually mean columns | Try the column when row rules fail |
| Missing the repeated-number shortcut | Two identical columns mean only one variable | Tabulate n against the answer |
| Stopping at the first option that fits | Two options may fit a half-rule | Check both the rule and the last digit |
| Treating Kakuro as guess-and-check | Wastes the whole 2.5 minutes | Always peel a line with one unknown first |
| Over-investing in one puzzle | 4 puzzles in 10 minutes, worth 10 marks | 2.5 minutes each, then guess |

## 7. Practice questions

More questions: [`QB-Z1-number-grids-and-matrices.md`](../question-banks/QB-Z1-number-grids-and-matrices.md).

**1.** **[Four-column rows]** Find the missing number:

```text
4  5  3    31
5  9  3    52
5  4  8    57
6  2  7     ?
```

a) 51
b) 50
c) 46
d) 45

**2.** **[Three-column rows]** Find the missing number in the last row, using the rule the first three rows follow:

```text
  28  7  3
  18  3  5
  20  2  9
   ?  3  3
```

a) 12
b) 17
c) 10
d) 11

**3.** **[Four-column rows]** Find the missing number:

```text
5  5  4    45
6  5  4    56
2  6  3    22
2  3  2     ?
```

a) 13
b) 7
c) 10
d) 9

**4.** **[Four-column rows]** Find the missing number:

```text
9  5  7    58
3  3  5    12
3  4  6    14
9  9  6     ?
```

a) 45
b) 44
c) 50
d) 55

**5.** **[Sum grid]** Every row of this grid adds up to the same number. Find the missing number:

```text
 2   1  15
 2   6  10
 8   6   ?
```

a) 4
b) 1
c) 14
d) 6

**6.** **[Four-column rows]** Find the missing number:

```text
8  2  8    80
8  4  2    24
3  3  2    12
5  4  7     ?
```

a) 75
b) 67
c) 63
d) 60

**7.** **[Three-column rows]** Find the missing number in the last row, using the rule the first three rows follow:

```text
  51  7  2
  41  6  5
  42  6  6
   ?  8  8
```

a) 82
b) 84
c) 72
d) 73

**8.** **[Three-column rows]** Find the missing number in the last row, using the rule the first three rows follow:

```text
  67  8  3
  38  6  2
  69  8  5
   ?  7  7
```

a) 60
b) 51
c) 46
d) 56

**9.** **[Four-column rows]** Find the missing number:

```text
4  7  4     9
5  8  9    37
2  3  8    13
8  5  8     ?
```

a) 63
b) 67
c) 69
d) 59

**10.** **[Three-column rows]** Find the missing number in the last row, using the rule the first three rows follow:

```text
  12  4  3
  24  4  6
  28  7  4
   ?  3  2
```

a) 7
b) 6
c) 8
d) 4

**11.** **[Four-column rows]** Find the missing number:

```text
7  7  4    77
4  2  8    32
4  5  7    51
8  7  8     ?
```

a) 116
b) 126
c) 125
d) 120

**12.** **[Four-column rows]** Find the missing number:

```text
5  9  9    86
9  8  2    25
8  8  7    64
9  2  6     ?
```

a) 22
b) 21
c) 29
d) 27

### ANSWER KEY

1. **b** — For a row (a, b, c, d) the rule is **d = a² + b × c**: 4,5,3 → 31; 5,9,3 → 52; 5,4,8 → 57. The last row gives **50**.
2. **a** — The rule is **first = second × (third + 1)**: 28 from 7 and 3; 18 from 3 and 5; 20 from 2 and 9. Last row: **12**.
3. **c** — For a row (a, b, c, d) the rule is **d = a² + b × c**: 5,5,4 → 45; 6,5,4 → 56; 2,6,3 → 22. The last row gives **10**.
4. **a** — For a row (a, b, c, d) the rule is **d = a × c − b**: 9,5,7 → 58; 3,3,5 → 12; 3,4,6 → 14. The last row gives **45**.
5. **a** — The complete rows add up to 18 (e.g. 2 + 1 + 15 = 18). The last row has 8 + 6 = 14, so the missing number is 18 − 14 = **4**.
6. **c** — For a row (a, b, c, d) the rule is **d = (a + b) × c**: 8,2,8 → 80; 8,4,2 → 24; 3,3,2 → 12. The last row gives **63**.
7. **c** — The rule is **first = second² + third**: 51 from 7 and 2; 41 from 6 and 5; 42 from 6 and 6. Last row: **72**.
8. **d** — The rule is **first = second² + third**: 67 from 8 and 3; 38 from 6 and 2; 69 from 8 and 5. Last row: **56**.
9. **d** — For a row (a, b, c, d) the rule is **d = a × c − b**: 4,7,4 → 9; 5,8,9 → 37; 2,3,8 → 13. The last row gives **59**.
10. **b** — The rule is **first = second × third**: 12 from 4 and 3; 24 from 4 and 6; 28 from 7 and 4. Last row: **6**.
11. **d** — For a row (a, b, c, d) the rule is **d = a² + b × c**: 7,7,4 → 77; 4,2,8 → 32; 4,5,7 → 51. The last row gives **120**.
12. **b** — For a row (a, b, c, d) the rule is **d = b × c + a**: 5,9,9 → 86; 9,8,2 → 25; 8,8,7 → 64. The last row gives **21**.

## 8. Resources

- **https://prepinsta.com/infosys/puzzle-questions-and-answers-pdf/** — Infosys puzzle collection with answers; use it only to recognise rule families, and re-solve each item yourself.
- **https://prepdrive.in/infosys/puzzle/infosys-puzzle** — practice puzzles in the Infosys style.
- **https://en.wikipedia.org/wiki/Kakuro** — the clue-sum logic behind the distinct-digit grids.

## 9. Self-check

1. Can you list the rule ladder from memory and say which rule gave Z07, Z02 and Z09?
2. Given `3 5 → 16` and `4 6 → 22`, can you name two rules that fit the first line and show which one the second line kills?
3. Can you state the total, then the blank, in a 4×4 constant-sum grid in under 30 seconds?
4. Can you peel the Kakuro grid in Example 5 without looking?
5. What do you do when the 2.5-minute timer expires?

## 10. Sources

This file was written for this library. **Infosys evidence:** observed questions Z01, Z02, Z07, Z09, Z11, O51 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `Z1`). Confidence **High**. Practice questions in §7 and the bank were generated and checked by execution (brute force, simulation or inverse); see `../research/04-qa-report.md`. Nothing here is a published Infosys syllabus.
