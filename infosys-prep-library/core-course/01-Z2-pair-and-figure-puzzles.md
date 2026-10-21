---
title: Pair and figure puzzles
code: Z2
section: Numerical Puzzle
weightage_pct: 7.6% of marks
est_questions: 2.29
tier: 1
difficulty: Medium
est_study_hours: 1.2
confidence: High
last_updated: 2026-09-30
course: core
lesson: 1
---

# Lesson 01. Pair and figure puzzles

*Topic `Z2` · about 5.7 of the 75 marks · plan about 1.2 hours.*

## 1. The idea

A pair puzzle is a small mystery. You get a few lines of numbers. Every line was made by the same secret rule. Your job is to find the rule and use it on the last line.

Here is a tiny one. The lines are `(2, 5) → 11`, `(3, 4) → 13` and `(4, 6) → 25`. The rule is "multiply the two numbers, then add 1". Check it: 2 × 5 + 1 = 11. Yes. Now you can answer `(6, 3) → ?`. It is 6 × 3 + 1 = 19.

That is the whole skill. You do not need clever maths. You need a short list of rules to try, a fast way to test each one, and the habit of checking every line before you trust a rule.

The same idea works for other shapes. A **figure** puzzle gives four outer numbers and one centre number. A **box** puzzle gives some circles and one number in a box. A **zig-zag** puzzle gives rows where each number comes from the two above it. The rule is always hidden, and it is always the same in every line of that puzzle.

## 2. What Infosys actually asks

The Numerical Puzzle section has 4 questions in 10 minutes. That is about 150 seconds a question. In the official 2020 sample the four questions were worth 3, 2, 2 and 3 marks `[CONFIRMED — official sample 2020]`. The section is 10 marks out of 75, and it has its own cut-off. Coaches say puzzles and verbal are where most candidates miss the cut-off `[REPORTED]`. That makes this section worth practising.

Three shapes appeared in the official sample, all rule-finding puzzles:

- a plus-shaped figure, where the centre equals twice the sum of the four arms;
- circles that hold a number and its cube, with a box holding the sum of both cubes and both small numbers;
- zig-zag rows, where each number is the digit sum of its upper-left neighbour plus the digit sum of its upper-right neighbour.

Reports from 2025 candidates show the same family: pairs with a product and a constant, pairs with squares, pairs of two-digit numbers where you work with the digits, and four outer numbers giving a centre `[REPORTED]`. The exact items are listed in `question-banks/QB-98-OFFICIAL-SAMPLE-SOLVED.md` and `question-banks/QB-99-OBSERVED-POOL.md`.

## 3. The method

Use these five steps, in this order.

1. **Look at the sizes.** Do small inputs give a big output? Then think multiply or square. Are the outputs about as big as the inputs? Then think add or subtract.
2. **Pick a rule from the ladder below** and test it on line 1 only. If it fails, throw it away at once.
3. **If it fits line 1, test it on line 2, then line 3.** A real rule fits every line. A rule that fits only some lines is a coincidence.
4. **Apply the rule to the question line.**
5. **Check your answer once.** Put your rule back into line 1 and make sure it still gives the right number.

The rule ladder, from most likely to least likely:

| Try first | Examples |
|---|---|
| Add or subtract | a + b, a − b, 2(a + b), 3a − b |
| Multiply, maybe with a constant | a × b, a × b + 1, a × b − 3 |
| Squares and cubes | a² − b, a + b², a² + b², a³ + b³ |
| Digits of the numbers | digit sum, digit product |
| Two or three steps joined | a × b + a + b, a × b − a − b |

If you have spent about a minute and nothing fits, move on. You can come back at the end.

## 4. Shortcuts and when they fail

**Size test.** If the output is close to a × b, the rule is probably a product plus or minus a small number. If it is close to a², think squares. *It fails when* the rule adds a large constant, because then every output looks bigger than it should.

**Last-digit test.** The last digit of a sum, a difference or a product depends only on the last digits of the inputs. So you can reject a rule by looking only at last digits. *It fails for digit rules and for division*, because those do not work digit by digit.

**One-step-at-a-time test.** Suppose two lines have the same second number, and the first numbers differ by 1. If the rule is "a times something, plus something", the output jumps by exactly that "something". For 3a + b it jumps by 3. For a × b + 1 it jumps by b. *It fails when no two lines share a number, and it fails for squares.*

**The plus-shape rule.** For a plus-shaped figure, add the four arms and compare the total with the centre. Try × 2 first. If that fails, try × 3, or the total plus a constant. *It fails when the centre is built from products of arms.* Then use the figure rules from Example 3.

**The cube-and-box rule.** When circles hold a number and its square or cube, add the two powers and see what is left over in the box. In the official sample the leftover was the sum of the two small numbers. *It fails when the leftover is something else*, such as zero or a product. The leftover tells you which case you are in.

## 5. Worked examples

**Example 1 (easy). Three lines.** Lines: `(2, 5) → 11`, `(3, 4) → 13`, `(4, 6) → 25`. Find `(6, 3)`.

The outputs are close to the products (10, 12, 24), and each is 1 more. So the rule is a × b + 1. Check line 3: 4 × 6 + 1 = 25. Yes. Answer: 6 × 3 + 1 = **19**.

Notice what the third line did. The first two lines alone also fit "3a + b" (3 × 2 + 5 = 11 and 3 × 3 + 4 = 13). That rule would give 21. Only the third line removes it.

**Example 2 (squares). Two lines.** Lines: `(4, 3) → 13`, `(5, 6) → 19`. Find `(7, 2)`.

Try a × b + 1 on line 1: 4 × 3 + 1 = 13. It fits. On line 2: 5 × 6 + 1 = 31, not 19. So it was a coincidence. Try a² − b: 16 − 3 = 13, and 25 − 6 = 19. Both fit. Answer: 49 − 2 = **47**.

**Example 3 (a figure).** Each figure has outer numbers in the order (a, b, c, d). `[4, 5, 2, 3] → 14` and `[6, 3, 4, 2] → 10`. Find the centre for `[5, 5, 3, 4]`.

With four numbers, a common move is to join them in two pairs. Try a × b − c × d: 20 − 6 = 14. Yes. Line 2: 18 − 8 = 10. Yes. Answer: 25 − 12 = **13**.

**Example 4 (cube and box, from the official style).** Circles hold a number and its cube. Set 1 has 2 (cube 8) and 3 (cube 27), box 40. Set 2 has 2 (cube 8) and 5 (cube 125), box 140. Find the box for 3 (cube 27) and 5 (cube 125).

Add the cubes in set 1: 8 + 27 = 35. The box is 40, so 5 is left over. And 2 + 3 = 5. So the box is the two cubes plus the two small numbers. Set 2: 8 + 125 + 7 = 140. Yes. Answer: 27 + 125 + 8 = **160**.

**Example 5 (zig-zag, advanced).** Row 1 is 14, 27, 35, 62, 48. Row 2 is 14, 17, 16, 20. Row 3 is 13, X, 9. Find X.

Sums and differences of the top numbers do not give row 2 (14 + 27 = 41). Try digit sums: 14 gives 5 and 27 gives 9, and 5 + 9 = 14. Next, 27 gives 9 and 35 gives 8, and 17 is right. The rule is "digit sum of the left plus digit sum of the right". Row 3: the left cell is 14 and the next is 17, giving 5 + 8 = 13. Yes. For X, use 17 and 16: 8 + 7 = **15**.

## 6. Traps

- **Stopping after one line.** Example 1 shows why. Two lines can fit two different rules.
- **Swapping the order.** Rules like a² − b are not the same as b² − a. Keep (a, b) in the order they are written.
- **A slip in the arithmetic.** If a rule fails by a small amount, check your sums before you throw the rule away.
- **Forgetting the digits.** If the numbers are two digits and the outputs are small, the rule probably works on the digits.
- **Too clever a rule.** Real rules are short. In the official sample the longest rule had five steps. If yours has more, look again.


## 7. Practice questions

Attempt each level before opening the key. Level 3 is harder than anything in the 2020 official sample, on purpose: if you can do Level 3, the real paper will feel easy.

### Level 1: warm-up

*One or two steps. Small numbers.*

**1.** **[Pair rule]** Find the missing number, using the same rule in every line:  

```text
(5, 7) → 35
(3, 6) → 18
(8, 5) → 40
(2, 3) → ?
```

a) 6  
b) 14  
c) 1  
d) 2  

**2.** **[Pair rule]** Find the missing number, using the same rule in every line:  

```text
(6, 2) → 14
(6, 5) → 17
(6, 7) → 19
(2, 5) → ?
```

a) 5  
b) 6  
c) 9  
d) 15  

**3.** **[Pair rule]** Find the missing number, using the same rule in every line:  

```text
(7, 4) → 27
(4, 2) → 7
(6, 9) → 53
(3, 7) → ?
```

a) 20  
b) 10  
c) 15  
d) 17  

**4.** **[Pair rule]** Find the missing number, using the same rule in every line:  

```text
(2, 5) → 14
(7, 2) → 18
(9, 3) → 24
(6, 9) → ?
```

a) 33  
b) 32  
c) 30  
d) 58  

**5.** **[Zig-zag rows]** Each number in a lower row comes from the two numbers above it, by one rule used throughout. Find X.  

```text
 11    22    33    44    55
    33    55    77    99
       88     X   176
```

a) 22  
b) 129  
c) 132  
d) 6  

### Level 2: exam level

*The kinds of rule in the official sample. Two or three steps, with cubes and digits.*

**6.** **[Pair rule]** Find the missing number, using the same rule in every line:  

```text
(14, 20) → 314
(5, 13) → 83
(17, 18) → 341
(17, 11) → ?
```

a) 221  
b) 215  
c) 227  
d) 223  

**7.** **[Pair rule]** Find the missing number, using the same rule in every line:  

```text
(89, 46) → 27
(36, 22) → 13
(22, 86) → 18
(33, 99) → ?
```

a) 34  
b) 26  
c) 36  
d) 24  

**8.** **[Figure rule]** Each figure has four outer numbers in the order (a, b, c, d) and one centre number. Find the missing centre number:  

```text
outer [4, 15, 5, 2] → centre 70
outer [5, 11, 11, 12] → centre 187
outer [9, 7, 2, 9] → centre 81
outer [9, 11, 11, 11] → centre ?
```

a) 221  
b) 226  
c) 210  
d) 220  

**9.** **[Powers in a box]** Each set shows four circles and a box. The right-hand circle of each pair holds the cube of the left-hand one. Find the value in the last box.  

```text
set 1:  top 8, 512   bottom 9, 729   box 1258
set 2:  top 9, 729   bottom 2, 8   box 748
set 3:  top 8, 512   bottom 4, 64   box ?
```

a) 608  
b) 576  
c) 588  
d) 590  

**10.** **[Zig-zag rows]** Each number in a lower row comes from the two numbers above it, by one rule used throughout. Find X.  

```text
 16    25    36    49    64
     9    11    13    15
        2     X     2
```

a) 2  
b) 6  
c) 1  
d) 24  

### Level 3: beyond the exam

*Rules with six steps, which is more than any rule in the official sample, and the same cube-and-box idea with bigger numbers.*

**11.** **[Pair rule]** Find the missing number, using the same rule in every line:  

```text
(8, 12) → 120
(10, 7) → 89
(2, 8) → 54
(2, 6) → ?
```

a) 28  
b) 30  
c) 34  
d) 35  

**12.** **[Pair rule]** Find the missing number, using the same rule in every line:  

```text
(8, 4) → 100
(7, 8) → 154
(5, 2) → 32
(12, 11) → ?
```

a) 370  
b) 374  
c) 378  
d) 386  

**13.** **[Pair rule]** Find the missing number, using the same rule in every line:  

```text
(12, 4) → 188
(10, 9) → 119
(11, 7) → 160
(6, 2) → ?
```

a) 50  
b) 52  
c) 56  
d) 54  

**14.** **[Figure rule]** Each figure has four outer numbers in the order (a, b, c, d) and one centre number. Find the missing centre number:  

```text
outer [9, 6, 3, 3] → centre 117
outer [6, 4, 6, 2] → centre 46
outer [8, 2, 2, 2] → centre 72
outer [9, 7, 9, 4] → centre ?
```

a) 101  
b) 103  
c) 111  
d) 113  

**15.** **[Powers in a box]** Each set shows four circles and a box. The right-hand circle of each pair holds the cube of the left-hand one. Find the value in the last box.  

```text
set 1:  top 3, 27   bottom 7, 343   box 380
set 2:  top 6, 216   bottom 3, 27   box 252
set 3:  top 12, 1728   bottom 6, 216   box ?
```

a) 1964  
b) 2016  
c) 1944  
d) 1962  

### ANSWER KEY

1. **a** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **a×b**: (5, 7) → 35; (3, 6) → 18; (8, 5) → 40. Applied to (2, 3) it gives **6**. (44 candidate rules were tried; only this one fits.)
2. **c** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **2a + b**: (6, 2) → 14; (6, 5) → 17; (6, 7) → 19. Applied to (2, 5) it gives **9**. (44 candidate rules were tried; only this one fits.)
3. **a** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **a×b - 1**: (7, 4) → 27; (4, 2) → 7; (6, 9) → 53. Applied to (3, 7) it gives **20**. (44 candidate rules were tried; only this one fits.)
4. **c** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **(2)(a+b)**: (2, 5) → 14; (7, 2) → 18; (9, 3) → 24. Applied to (6, 9) it gives **30**. (44 candidate rules were tried; only this one fits.)
5. **c** — The rule is **left + right**. Row 2: (11, 22) → 33; (22, 33) → 55… Row 3: (55, 77) → **132**.
6. **b** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **a×b + a + b**: (14, 20) → 314; (5, 13) → 83; (17, 18) → 341. Applied to (17, 11) it gives **215**. (44 candidate rules were tried; only this one fits.)
7. **d** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **digit-sum(a) + digit-sum(b)**: (89, 46) → 27; (36, 22) → 13; (22, 86) → 18. Applied to (33, 99) it gives **24**. (5 candidate rules were tried; only this one fits.)
8. **d** — The rule that fits all three figures is **centre = a×b + c×d**. [4, 15, 5, 2] → 70; [5, 11, 11, 12] → 187; [9, 7, 2, 9] → 81. For [9, 11, 11, 11] it gives **220**.
9. **c** — Box = cube of the first + cube of the second + the two small numbers added: 512 + 729 + 17 = 1258; 729 + 8 + 11 = 748. Set 3: 512 + 64 + 12 = **588**.
10. **a** — The rule is **|left - right|**. Row 2: (16, 25) → 9; (25, 36) → 11… Row 3: (11, 13) → **2**.
11. **b** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **a² + b² - a×b + a**: (8, 12) → 120; (10, 7) → 89; (2, 8) → 54. Applied to (2, 6) it gives **30**. (48 candidate rules were tried; only this one fits.)
12. **b** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **(a+b)² - a×b - a - b**: (8, 4) → 100; (7, 8) → 154; (5, 2) → 32. Applied to (12, 11) it gives **374**. (48 candidate rules were tried; only this one fits.)
13. **a** — Test rules on the first line, then confirm on the second. The rule that fits all three lines is **a×b + a² - b² + a**: (12, 4) → 188; (10, 9) → 119; (11, 7) → 160. Applied to (6, 2) it gives **50**. (48 candidate rules were tried; only this one fits.)
14. **b** — The rule that fits all three figures is **centre = a² + b² - c×d + a**. [9, 6, 3, 3] → 117; [6, 4, 6, 2] → 46; [8, 2, 2, 2] → 72. For [9, 7, 9, 4] it gives **103**.
15. **d** — Box = cube of the first + cube of the second + the two small numbers added: 27 + 343 + 10 = 380; 216 + 27 + 9 = 252. Set 3: 1728 + 216 + 18 = **1962**.

## 8. Recap in 60 seconds

- Every line uses the **same** hidden rule.
- Look at sizes, pick a rule from the ladder, test on line 1, then line 2, then line 3.
- Add or subtract first, then multiply, then squares and cubes, then digits, then joined steps.
- Plus shape: centre = 2 × the sum of the arms. Cube and box: two cubes plus the two small numbers. Zig-zag: digit sum of each neighbour, added.
- One minute with no rule? Move on and come back.

## 9. Sources

- Infosys's own 2020 sample paper (Systems Engineer), section 5: the three shapes and the 3, 2, 2, 3 marks. See `../research/05-source-credibility.md` for how it was checked.
- `../question-banks/QB-98-OFFICIAL-SAMPLE-SOLVED.md` and `../question-banks/QB-99-OBSERVED-POOL.md`: the puzzle items, solved by running code.
- Every rule and every number in the worked examples is checked by code in `data/cc_examples.py`: each rule is shown to fit every line and to be the only rule that does, out of 48 competing pair rules or 16 figure rules. No outside website is cited for this lesson, because it is arithmetic and not a language rule (see `../research/06-method-sources.md`).
