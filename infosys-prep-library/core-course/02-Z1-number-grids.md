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
course: core
lesson: 2
---

# Lesson 02. Number grids and matrices

*Topic `Z1` · about 4.3 of the 75 marks · plan about 1.2 hours.*

## 1. The idea

A grid puzzle shows rows of numbers and one gap. The numbers follow a pattern, and your job is to find it. It is the cousin of the pair puzzle in Lesson 01, but here the pattern lives inside a row, a column or a whole grid.

There are only a few kinds, and each has a quick way in:

- **Rows with a rule.** In each row, one number is made from the others by a fixed rule.
- **A constant total.** Every row (or column) adds up to the same number.
- **A repeated number.** The first two numbers in each row are the same, so only one of them matters.
- **Two grids.** The second grid follows the first, and the link is usually in the row sums.

Learn to tell them apart in five seconds. After that, each one is easy.

## 2. What Infosys actually asks

The Numerical Puzzle section is 4 questions in 10 minutes, worth 10 marks. In the official 2020 sample the marks were 3, 2, 2 and 3 `[CONFIRMED — official sample 2020]`. Its grid question showed two 3 × 3 grids. The row sums of the first grid went up by 3 each row, and the second grid carried the same series on. One cell was missing.

Candidates in 2025 reported these shapes `[REPORTED]`:

- rows of four numbers where the last number comes from the first three;
- rows of three numbers where one is hidden;
- a grid where every row adds up to the same total;
- a table whose first two columns repeat (4 4 10, 5 5 15, and so on).

One coaching site also mentions a puzzle where digits cannot repeat in a row or column, with sums given (a Kakuro-style puzzle). No actual question of that kind was ever found `[REPORTED]`, so Level 3 uses it only as a stretch.

## 3. The method

1. **Look at the shape.** Rows of three or four? Does every row have the same total? Do the first two columns repeat? Are there two grids?
2. **Check for a total first.** Add the first full row. Add the second. If the totals match, the missing number is the total minus the others. This takes ten seconds.
3. **Otherwise, fit the first row only.** Try rules from the ladder below. Stop at the first rule that works.
4. **Confirm on the second row, then the third.** A real rule fits every row.
5. **Apply it to the last row** and check your answer once.

The rule ladder for rows, cheapest first:

| Order | Rule | The signal |
|---|---|---|
| 1 | Sum of the numbers | The answer is a little more than the biggest input |
| 2 | Difference | The answer is smaller than the inputs |
| 3 | Product of two numbers | The answer is much larger |
| 4 | Product plus or minus a number | The product fits except for a small gap |
| 5 | A square plus or minus another number | The answer is near a perfect square |
| 6 | Product of two, plus or minus the third | Most four-number rows |

## 4. Shortcuts and when they fail

**The total test.** Add one full row, then another. If both give the same number, you have a constant total. *It fails when only some rows match.* Then look for a rule.

**The repeated-number trick.** If the first two numbers in every row are the same, ignore one of them. Write the third numbers next to n and look for a formula. Triangular numbers (3, 6, 10, 15, 21) and n squared plus n (2, 6, 12, 20, 30) come up often. *It fails if the repeated columns differ in even one row.*

**The last-digit check.** If two answer options both seem to fit, compare last digits. A product of two numbers ends in the product of their last digits. *It fails for digit-based rules and division.*

**The row-sum trick for two grids.** Add every row in both grids and write the totals as a list. If the totals form a steady series, the missing cell is the next total minus the other two cells. *It fails if the totals do not form a series.* Then compare columns.

## 5. Worked examples

**Example 1 (a constant total).** Rows: `6 2 7`, `4 9 2`, `5 ? 8`. Find ?.

Row 1 adds to 15. Row 2 adds to 15. So every row adds to 15. Row 3: 5 + 8 = 13, so ? = 15 − 13 = **2**.

**Example 2 (three-number rows).** Rows are written as the answer first, then two numbers: `14 3 4`, `38 6 6`, `12 5 2`, and `? 7 3`.

The products are 12, 36 and 10. Each answer is 2 more. So the rule is "second × third + 2". Check row 2: 6 × 6 + 2 = 38. Yes. Answer: 7 × 3 + 2 = **23**.

**Example 3 (four-number rows).** Rows: `2 3 4 → 14`, `5 2 6 → 17`, `3 4 5 → 23`, and `6 5 3 → ?`.

Try the product of the last two plus the first. Row 1: 3 × 4 + 2 = 14. Row 2: 2 × 6 + 5 = 17. Row 3: 4 × 5 + 3 = 23. All fit. Answer: 5 × 3 + 6 = **21**.

**Example 4 (a repeated number).** Rows: `3 3 12`, `4 4 20`, `6 6 42`, and `8 8 ?`.

Only n matters. For n = 3, 4, 6 the third numbers are 12, 20, 42. Try n × n + n: 9 + 3 = 12, 16 + 4 = 20, 36 + 6 = 42. Yes. Answer: 64 + 8 = **72**.

**Example 5 (two grids, the official kind).** Grid 1 has rows `3 2 5`, `6 1 6`, `4 7 5`. Grid 2 has rows `9 4 6`, `7 ? 9`, `8 9 8`. Find ?.

Add the rows of grid 1: 10, 13, 16. The totals go up by 3. The series carries on into grid 2: 19, 22, 25. Check row 1 of grid 2: 9 + 4 + 6 = 19. Yes. Row 2 must total 22, so ? = 22 − 7 − 9 = **6**.

## 6. Traps

- **Fitting one row only.** Always check a second row.
- **Adding a fudge number.** If your rule needs a different constant in each row, the rule is wrong.
- **Forgetting the other grid.** With two grids, the clue is usually between them, not inside one.
- **Missing a total.** Check for a constant total before anything cleverer. It is the fastest win.
- **Spending too long.** Each puzzle gets about two and a half minutes. After a minute with no rule, move on.


## 7. Practice questions

Attempt each level before opening the key. Level 3 is harder than anything in the 2020 official sample, on purpose: if you can do Level 3, the real paper will feel easy.

### Level 1: warm-up

*Easy rules, small numbers, and a total you can find in one step.*

**1.** **[Sum grid]** Every row of this grid adds up to the same number. Find the missing number:  

```text
 9   3   9
 9   7   5
 6   7   ?
```

a) 4  
b) 13  
c) 8  
d) 10  

**2.** **[Three-column rows]** Find the missing number in the last row, using the rule the first three rows follow:  

```text
  15  3  5
  12  2  6
  18  9  2
   ?  5  8
```

a) 40  
b) 38  
c) 39  
d) 45  

**3.** **[Three-column rows]** Find the missing number in the last row, using the rule the first three rows follow:  

```text
  30  8  7
  18  3  6
  16  2  6
   ?  5  2
```

a) 14  
b) 20  
c) 9  
d) 16  

**4.** **[Repeated-number table]** Find the missing number:  

```text
5  5  26
7  7  50
8  8  65
10  10  ?
```

a) 91  
b) 100  
c) 103  
d) 101  

**5.** **[Row sums as a series]** Two 3x3 grids relate in the same way. Find the missing number in the second grid.  

```text
Grid 1          Grid 2
 5   1   4       6   7   ?
 1   3   9       8   4  10
 6   6   4       6   6  13
```

a) 9  
b) 13  
c) 6  
d) 3  

### Level 2: exam level

*The kinds seen in reports and in the official sample, with squares and a second step.*

**6.** **[Three-column rows]** Find the missing number in the last row, using the rule the first three rows follow:  

```text
  23  7  3
  66  8  8
  10  4  2
   ?  4  7
```

a) 42  
b) 30  
c) 31  
d) 20  

**7.** **[Four-column rows]** Find the missing number:  

```text
2  6  3    20
8  6  6    44
4  2  4    12
9  4  6     ?
```

a) 33  
b) 28  
c) 41  
d) 34  

**8.** **[Repeated-number table]** Find the missing number:  

```text
3  3  6
5  5  15
6  6  21
11  11  ?
```

a) 66  
b) 78  
c) 61  
d) 71  

**9.** **[Row sums as a series]** Two 3x3 grids relate in the same way. Find the missing number in the second grid.  

```text
Grid 1          Grid 2
 5   1   6       9   5   ?
 4   6   4       8   4   8
 4   5   7       4   7  11
```

a) 2  
b) 6  
c) 9  
d) 4  

**10.** **[Sum grid]** Every column of this grid adds up to the same number. Find the missing number:  

```text
 7   5   3   4
 4   4   8   1
 4   5   2   6
 7   8   9   ?
```

a) 13  
b) 11  
c) 24  
d) 15  

### Level 3: beyond the exam

*Bigger grids and harder rules, and one distinct-digit grid as a stretch, which no Infosys source has shown.*

**11.** **[Four-column rows]** Find the missing number:  

```text
3  7  4    37
4  2  2    20
5  9  2    43
6  3  7     ?
```

a) 53  
b) 47  
c) 67  
d) 57  

**12.** **[Four-column rows]** Find the missing number:  

```text
8  8  4    64
2  5  9    63
4  3  7    49
7  7  4     ?
```

a) 55  
b) 56  
c) 68  
d) 52  

**13.** **[Repeated-number table]** Find the missing number:  

```text
5  5  10
7  7  21
10  10  45
12  12  ?
```

a) 68  
b) 66  
c) 69  
d) 64  

**14.** **[Sum grid]** Every row of this grid adds up to the same number. Find the missing number:  

```text
 8   9   1   5
 2   4   2  15
 8   8   1   6
 3   9   9   ?
```

a) 4  
b) 21  
c) 2  
d) 0  

**15.** **[Distinct-digit sum grid]** Fill the grid with digits 1–9 so that **no digit repeats in any row or column**, each row adds up to the number on its left and each column to the number above it. A dot is another empty cell. What number replaces ‘?’ ?  

```text
      16  12  18
    +------------
 19 |  .   .   9
 15 |  2   9   .
 12 |  .   ?   .
```

a) 9  
b) 5  
c) 1  
d) 2  

### ANSWER KEY

1. **c** — The complete rows add up to 21 (e.g. 9 + 3 + 9 = 21). The last row has 6 + 7 = 13, so the missing number is 21 − 13 = **8**.
2. **a** — The rule is **first = second × third**: 15 from 3 and 5; 12 from 2 and 6; 18 from 9 and 2. Last row: **40**.
3. **a** — The rule is **first = (second + third) × 2**: 30 from 8 and 7; 18 from 3 and 6; 16 from 2 and 6. Last row: **14**.
4. **d** — Only the repeated number matters: the third number is **n² + 1**. n=5 → 26; n=7 → 50; n=8 → 65. For n = 10: **101**.
5. **c** — Add each row of grid 1: 10, 13, 16. The totals rise by 3 each row, and the series carries on into grid 2: 19, 22, 25. The first row of grid 2 must total 19, so ? = 19 − 6 − 7 = **6**.
6. **b** — The rule is **first = second × third + 2**: 23 from 7 and 3; 66 from 8 and 8; 10 from 4 and 2. Last row: **30**.
7. **a** — For a row (a, b, c, d) the rule is **d = b × c + a**: 2,6,3 → 20; 8,6,6 → 44; 4,2,4 → 12. The last row gives **33**.
8. **a** — Only the repeated number matters: the third number is **n(n+1)/2**. n=3 → 6; n=5 → 15; n=6 → 21. For n = 11: **66**.
9. **d** — Add each row of grid 1: 12, 14, 16. The totals rise by 2 each row, and the series carries on into grid 2: 18, 20, 22. The first row of grid 2 must total 18, so ? = 18 − 9 − 5 = **4**.
10. **b** — Each column adds up to 22. The last column has 4 + 1 + 6 = 11, so the missing number is 22 − 11 = **11**.
11. **d** — For a row (a, b, c, d) the rule is **d = a² + b × c**: 3,7,4 → 37; 4,2,2 → 20; 5,9,2 → 43. The last row gives **57**.
12. **b** — For a row (a, b, c, d) the rule is **d = (a + b) × c**: 8,8,4 → 64; 2,5,9 → 63; 4,3,7 → 49. The last row gives **56**.
13. **b** — Only the repeated number matters: the third number is **n(n−1)/2**. n=5 → 10; n=7 → 21; n=10 → 45. For n = 12: **66**.
14. **c** — The complete rows add up to 23 (e.g. 8 + 9 + 1 + 5 = 23). The last row has 3 + 9 + 9 = 21, so the missing number is 23 − 21 = **2**.
15. **c** — Work from the row or column with the fewest unknowns. The only grid that satisfies every sum with no repeats has row 3 = [6, 1, 5], so ‘?’ = **1**. (Checked by trying every filling: exactly one exists.)

## 8. Recap in 60 seconds

- Five seconds to decide the kind: rows with a rule, constant total, repeated number, two grids.
- **Check the total first.** Then fit the first row, confirm on the second and third.
- Rule ladder: sum, difference, product, product ± number, square, product ± third number.
- Repeated first two columns? Only n matters. Think triangular numbers and n² + n.
- Two grids? Add every row; the totals make a series.
- Stuck for a minute? Move on.

## 9. Sources

- Infosys's own 2020 sample paper, section 5: the two-grid question and the 3, 2, 2, 3 marks (see `../research/05-source-credibility.md`).
- `../question-banks/QB-98-OFFICIAL-SAMPLE-SOLVED.md` and `../question-banks/QB-99-OBSERVED-POOL.md`: the grid items, solved by running code.
- Every rule and number in the five examples is checked by code in `data/cc_examples.py`: each rule is shown to fit every row and to be the only rule in the library that does. No outside website is cited, because this is arithmetic and not a language rule (see `../research/06-method-sources.md`).
