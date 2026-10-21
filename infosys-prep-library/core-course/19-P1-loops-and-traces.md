---
title: Loops and trace tables
code: P1
section: Pseudocode
weightage_pct: 3.6% of marks
est_questions: 1.34
tier: 1
difficulty: Easy
est_study_hours: 1.0
confidence: High
last_updated: 2026-09-30
course: core
lesson: 19
---

# Lesson 19. Loops and trace tables

*Topic `P1` · about 2.7 of the 75 marks · plan about 1.0 hours.*

## 1. The idea

A trace question shows a few lines of code and asks what it prints. You do not have to understand the purpose of the program. You only have to act like the computer: go line by line, keep track of each variable, and write down what is printed.

The tool for this is the **trace table**. Draw a column for each variable. Each time a line changes a variable, write its new value in a new row. When the program ends, the last row and the printed output give the answer.

Loops are the part that needs care. A loop repeats its lines. A trace table shows you each repeat, so you never lose count.

Three loop forms matter:

- **`For (each i from a to b)`** runs once for every whole number from a up to **and including** b.
- **`While (condition)`** checks the condition first. It runs the lines while the condition is true. If it is false at the start, it never runs.
- **`Do` … `While (condition)`** runs the lines once, then checks the condition. So it always runs at least once.

## 2. What Infosys actually asks

Pseudocode is 5 questions worth 10 marks in 10 minutes, so each question is worth 2 marks and has about two minutes `[CONFIRMED — official sample 2020]` for the marks, `[LIKELY]` for the section size in the current test.

Seven loop questions were reported from 2024 and 2025 `[REPORTED]`: a loop with a condition on `mod`, a loop that counts to a number found by `mod`, a loop that never ends, a loop that adds 5 until a number divides by 8, a loop that adds multiples, a loop that adds the digits of 123, and a loop that adds squares for even numbers and plain numbers for odd ones.

The official 2020 sample had two loop questions: one that prints a series with two variables changing together, and one with a loop inside a loop where the inner loop starts from the value of the outer one `[CONFIRMED — official sample 2020]`. The programs were written in numbered lines with `For (each i from 1 to 5)` and `End-for`.

## 3. The method

1. **List the variables** in a table, one column each, plus a column for what is printed.
2. **Fill in the starting values** from the `Set` lines.
3. **Run the loop one turn at a time.** On each turn, write a new row.
4. **Check the loop condition each time.** For `For`, count the turns from a to b, inclusive. For `While`, test the condition before each turn.
5. **Note each `Print` as it happens.**
6. **When the loop ends, read the answer** from the table, and re-read the question to see whether it asks for the last value or the whole list printed.

Words you will meet:

| Word | Meaning |
|---|---|
| `x MOD y` | the remainder when x is divided by y |
| `x / y` with whole numbers | the whole-number part of the answer (45 / 10 is 4) |
| `c++` | add 1 to c |
| `break` | leave the loop at once |
| `continue` | skip the rest of this turn and start the next |

## 4. Shortcuts and when they fail

**Count the turns first.** `For (each i from 1 to 5)` runs 5 times. If each turn adds 3, the result changes by 15. *It fails when the loop has a `break`* or when the body changes `i`.

**Look for a pattern after two turns.** If the table shows 1, 3, 6, 10, you can see the pattern. *It fails when the pattern changes.* Trace the whole loop for small counts.

**Nested loops multiply.** An outer loop of 3 turns and an inner loop of 4 turns run the inner body 12 times. *It fails when the inner loop depends on the outer variable.* Then add up the inner turns one by one.

**Test the first and last turn of a `While`.** Check the very first condition and the one that ends it. *It fails if the loop may never end.* Check that the variable moves towards the stopping point.

## 5. Worked examples

Every program below was translated to Java and run, and the output matches the answer.

**Example 1 (a sum).**

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 1 to 5)
4)   s = s + i
5) End-for
6) Print s
```

| turn | i | s |
|---|---|---|
| start | | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |
| 4 | 4 | 10 |
| 5 | 5 | 15 |

The loop runs for i = 1, 2, 3, 4, 5. Answer: **15**.

**Example 2 (a `While` that cuts a number down).**

```text
1) Integer n, c
2) Set n = 4529
3) Set c = 0
4) While (n > 0)
5)   n = n / 10
6)   c++
7) End-while
8) Print c
```

The numbers go 4529, 452, 45, 4, 0. That is four turns, so c is 4. Answer: **4**. (This counts the digits.)

**Example 3 (a condition with `MOD`).**

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 1 to 10)
4)   If (i MOD 3 == 0) then
5)     s = s + i
6)   End-if
7) End-for
8) Print s
```

Only the multiples of 3 are added: 3, 6 and 9. Answer: 3 + 6 + 9 = **18**.

**Example 4 (a loop inside a loop).**

```text
1) Integer i, j, c
2) Set c = 0
3) For (each i from 1 to 3)
4)   For (each j from 1 to i)
5)     c++
6)   End-for
7) End-for
8) Print c
```

When i = 1, the inner loop runs once. When i = 2, twice. When i = 3, three times. The total is 1 + 2 + 3 = **6**.

**Example 5 (a series with two changing variables).**

```text
1) Integer i, j, k
2) Set j = 1, k = 2
3) For (each i from 1 to 5)
4)   Print k
5)   j = j + 2
6)   k = k + j
7) End-for
```

| turn | prints | j after | k after |
|---|---|---|---|
| 1 | 2 | 3 | 5 |
| 2 | 5 | 5 | 10 |
| 3 | 10 | 7 | 17 |
| 4 | 17 | 9 | 26 |
| 5 | 26 | 11 | 37 |

Notice that the program prints k **before** it changes. Answer: **2 5 10 17 26**.

## 6. Traps

- **Missing the last turn.** `from 1 to 5` includes 5.
- **Printing before or after the change.** Check the order of `Print` and the lines that change the variable.
- **Whole-number division.** 45 / 10 is 4, not 4.5.
- **A `While` that never ends.** If the variable never moves towards the stop, the answer is "infinite loop".
- **Counting the inner loop wrongly.** In Example 4 the inner count depends on i.
- **Not reading what is asked.** The question may ask for the last value printed, the whole list, or one variable.


## 7. Practice questions

Attempt each level before opening the key. Level 3 is harder than anything in the 2020 official sample, on purpose: if you can do Level 3, the real paper will feel easy.

### Level 1: warm-up

*Short programs of six to eight lines with one loop.*

**1.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 24 to 1 step -4)
4)   s = s + i
5) End-for
6) Print s
```

a) 84  
b) 83  
c) 85  
d) 86  

**2.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 36 to 8 step -2)
4)   s = s + i
5) End-for
6) Print s
```

a) 330  
b) 332  
c) 331  
d) 329  

**3.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer c, n
2) Set n = 145
3) Set c = 0
4) While (n > 1)
5)   n = n / 2
6)   c++
7) End-while
8) Print c
```

a) 6  
b) 9  
c) 7  
d) 8  

**4.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 40 to 4 step -2)
4)   s = s + i
5) End-for
6) Print s
```

a) 419  
b) 418  
c) 420  
d) 417  

**5.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer x
2) Set x = 3
3) Do
4)   x = x * 2
5)   Print x
6) While (x < 33)
```

a) 49  
b) 6 12 24 48  
c) 50  
d) 47  

### Level 2: exam level

*Programs of nine to eleven lines with conditions, remainders and division.*

**6.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer i, n, s
2) Set s = 0
3) Set n = 7
4) For (each i from 1 to n)
5)   If (i MOD 4 == 1) then
6)     s = s + i * 2
7)   End-if
8) End-for
9) Print s
```

a) 14  
b) 13  
c) 12  
d) 11  

**7.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer c, i, j
2) Set c = 0
3) Set j = 0
4) For (each i from 1 to 6)
5)   For (each j from i to 4)
6)     If ((i + j) MOD 2 == 0) then
7)       c++
8)     End-if
9)   End-for
10) End-for
11) Print c
```

a) 4  
b) 5  
c) 7  
d) 6  

**8.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer a, b
2) Set a = 51
3) Set b = 71
4) While (a != b)
5)   If (a > b) then
6)     a = a - b
7)   Else
8)     b = b - a
9)   End-if
10) End-while
11) Print a
```

a) 0  
b) 1  
c) 3  
d) 2  

**9.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer i, n, s
2) Set s = 0
3) Set n = 13
4) For (each i from 1 to n)
5)   If (i MOD 4 == 0) then
6)     s = s + i * 3
7)   End-if
8) End-for
9) Print s
```

a) 72  
b) 74  
c) 73  
d) 71  

**10.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer i, n, s
2) Set s = 0
3) Set n = 6
4) For (each i from 1 to n)
5)   If (i MOD 2 == 1) then
6)     s = s + i * 2
7)   End-if
8) End-for
9) Print s
```

a) 19  
b) 20  
c) 17  
d) 18  

### Level 3: beyond the exam

*Thirteen-line programs with a loop inside a loop, or with break and continue.*

**11.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 1 to 13)
4)   If (i MOD 3 == 0) then
5)     continue
6)   End-if
7)   If (i > 10) then
8)     break
9)   End-if
10)   s = s + i
11) End-for
12) Print s
13) Print i
```

a) 37 11  
b) 10  
c) 27 10  
d) 12  

**12.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 1 to 16)
4)   If (i MOD 2 == 0) then
5)     continue
6)   End-if
7)   If (i > 7) then
8)     break
9)   End-if
10)   s = s + i
11) End-for
12) Print s
13) Print i
```

a) 10  
b) 12 8  
c) 16 9  
d) 9 7  

**13.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 1 to 16)
4)   If (i MOD 3 == 0) then
5)     continue
6)   End-if
7)   If (i > 14) then
8)     break
9)   End-if
10)   s = s + i
11) End-for
12) Print s
13) Print i
```

a) 61 14  
b) 75 16  
c) 15  
d) 17  

**14.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 1 to 8)
4)   If (i MOD 2 == 0) then
5)     continue
6)   End-if
7)   If (i > 6) then
8)     break
9)   End-if
10)   s = s + i
11) End-for
12) Print s
13) Print i
```

a) 8  
b) 6  
c) 9 7  
d) 12 8  

**15.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)  

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 1 to 14)
4)   If (i MOD 3 == 0) then
5)     continue
6)   End-if
7)   If (i > 6) then
8)     break
9)   End-if
10)   s = s + i
11) End-for
12) Print s
13) Print i
```

a) 8  
b) 9  
c) 6  
d) 12 7  

### ANSWER KEY

1. **a** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 24 | 24 |
| 2 | 20 | 44 |
| 3 | 16 | 60 |
| 4 | 12 | 72 |
| 5 | 8 | 80 |
| 6 | 4 | 84 |

The program prints 84. Output: **84**.
2. **a** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 36 | 36 |
| 2 | 34 | 70 |
| 3 | 32 | 102 |
| 4 | 30 | 132 |
| 5 | 28 | 160 |
| 6 | 26 | 186 |
| 7 | 24 | 210 |

(… 8 more passes)

The program prints 330. Output: **330**.
3. **c** — Trace it, recording the variables at the end of each pass:

| pass | c | n |
|---|---|---|
| 1 | 1 | 72 |
| 2 | 2 | 36 |
| 3 | 3 | 18 |
| 4 | 4 | 9 |
| 5 | 5 | 4 |
| 6 | 6 | 2 |
| 7 | 7 | 1 |

The program prints 7. Output: **7**.
4. **b** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 40 | 40 |
| 2 | 38 | 78 |
| 3 | 36 | 114 |
| 4 | 34 | 148 |
| 5 | 32 | 180 |
| 6 | 30 | 210 |
| 7 | 28 | 238 |

(… 12 more passes)

The program prints 418. Output: **418**.
5. **b** — Trace it, recording the variables at the end of each pass:

| pass | x |
|---|---|
| 1 | 6 |
| 2 | 12 |
| 3 | 24 |
| 4 | 48 |

The program prints 6, 12, 24, 48 in that order. Output: **6 12 24 48**.
6. **c** — Trace it, recording the variables at the end of each pass:

| pass | i | n | s |
|---|---|---|---|
| 1 | 1 | 7 | 2 |
| 2 | 2 | 7 | 2 |
| 3 | 3 | 7 | 2 |
| 4 | 4 | 7 | 2 |
| 5 | 5 | 7 | 12 |
| 6 | 6 | 7 | 12 |
| 7 | 7 | 7 | 12 |

The program prints 12. Output: **12**.
7. **d** — Trace it, recording the variables at the end of each pass:

| pass | c | i | j |
|---|---|---|---|
| 1 | 2 | 1 | 4 |
| 2 | 4 | 2 | 4 |
| 3 | 5 | 3 | 4 |
| 4 | 6 | 4 | 4 |
| 5 | 6 | 5 | 4 |
| 6 | 6 | 6 | 4 |

The program prints 6. Output: **6**.
8. **b** — Trace it, recording the variables at the end of each pass:

| pass | a | b |
|---|---|---|
| 1 | 51 | 20 |
| 2 | 31 | 20 |
| 3 | 11 | 20 |
| 4 | 11 | 9 |
| 5 | 2 | 9 |
| 6 | 2 | 7 |
| 7 | 2 | 5 |

(… 3 more passes)

The program prints 1. Output: **1**.
9. **a** — Trace it, recording the variables at the end of each pass:

| pass | i | n | s |
|---|---|---|---|
| 1 | 1 | 13 | 0 |
| 2 | 2 | 13 | 0 |
| 3 | 3 | 13 | 0 |
| 4 | 4 | 13 | 12 |
| 5 | 5 | 13 | 12 |
| 6 | 6 | 13 | 12 |
| 7 | 7 | 13 | 12 |

(… 6 more passes)

The program prints 72. Output: **72**.
10. **d** — Trace it, recording the variables at the end of each pass:

| pass | i | n | s |
|---|---|---|---|
| 1 | 1 | 6 | 2 |
| 2 | 2 | 6 | 2 |
| 3 | 3 | 6 | 8 |
| 4 | 4 | 6 | 8 |
| 5 | 5 | 6 | 18 |
| 6 | 6 | 6 | 18 |

The program prints 18. Output: **18**.
11. **a** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 4 | 7 |
| 4 | 5 | 12 |
| 5 | 7 | 19 |
| 6 | 8 | 27 |
| 7 | 10 | 37 |

The program prints 37, 11 in that order. Output: **37 11**.
12. **c** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 3 | 4 |
| 3 | 5 | 9 |
| 4 | 7 | 16 |

The program prints 16, 9 in that order. Output: **16 9**.
13. **b** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 4 | 7 |
| 4 | 5 | 12 |
| 5 | 7 | 19 |
| 6 | 8 | 27 |
| 7 | 10 | 37 |

(… 3 more passes)

The program prints 75, 16 in that order. Output: **75 16**.
14. **c** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 3 | 4 |
| 3 | 5 | 9 |

The program prints 9, 7 in that order. Output: **9 7**.
15. **d** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 4 | 7 |
| 4 | 5 | 12 |

The program prints 12, 7 in that order. Output: **12 7**.

## 8. Recap in 60 seconds

- Trace table: a column per variable, a new row per change.
- `For (each i from a to b)` includes b. `While` checks first. `Do … While` runs once before it checks.
- `MOD` = remainder. Whole-number `/` drops the fraction.
- Nested loops: add up the inner turns, one outer turn at a time.
- Check the order of `Print` and the change in each turn.
- Re-read what the question asks for.

## 9. Sources

- Infosys's own 2020 sample paper, pseudocode section: the dialect, the 2-mark weight and the two loop questions (see `../research/05-source-credibility.md`).
- [The Java Tutorials: the while and do-while statements](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/while.html), [the for statement](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html) and [Branching statements](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/branch.html): a do-while body runs at least once; a `for` runs its start once, tests before each turn, and runs its increment after each turn; `break` and `continue` (S2 in `../research/06-method-sources.md`).
- Every output above comes from translating the printed program to Java and running it (`data/cc_examples.py`).
