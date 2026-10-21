---
title: Pre/post-increment and fill-the-blank
code: P4
section: Pseudocode
weightage_pct: 1.3% of marks
est_questions: 0.48
tier: 2
difficulty: Medium
est_study_hours: 0.6
confidence: Medium
last_updated: 2026-09-30
---

# P4 — Pre/post-increment and fill-the-blank

## 1. Why this topic matters here

Expect about **0.5 questions and 1.0 marks** on this topic (about 1.3% of the 75 scored marks). It sits in **Pseudocode**: 5 questions, 10 marks, 10 minutes. **Tier 2**, 0.6 hours to reach reliable recall, confidence **Medium**.

**2 questions on this topic are in the observed Infosys pool** (P13, P14), from 1 source. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** its ROI alone would place it lower, but this section has its own cut-off and this topic is needed to reach 60% of the section's marks. Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

Pre- and post-increment items appear **three times** in the 2025–26 pseudocode pool, all in the 2026-09-18 “PYQ” video (said to be asked in 2025) `[REPORTED]`: two “fill the blank” items and one `do … while` using `++x` and `x--`. Nothing else in the pool is so easy to lose marks on: the rule takes two minutes to learn and a five-question section is 10 marks.

| Sub-pattern | How it appears | Observed |
|---|---|---|
| Choose the statement so result and i both end at 6 | “i = 5 … which option makes both 6?” | P13 |
| Choose the expression so the printed result is 7 | “i = 2 … options use i++ and ++i” | P14 |
| Loop body with `++x`, `x--` and a stop condition | `do { ++x; display x; x--; } while (x >= -1)` | P04 (infinite loop) |
| Plain reads of `i` mixed with increments | authored from the pattern | — |

### The Infosys pseudocode dialect, as seen in the pool

Observed wording is C/Java-like, not Python-like, and differs from the Accenture dialect already in `pseudocode/P1`:

| Feature | Seen in the Infosys pool | Accenture dialect in P1 |
|---|---|---|
| Declaration | “Integer P and Q. Set value of P as 1” / “Set integer X is equal to 0” | `x = 0` |
| Output | `Display` or `Print` | `print` |
| Remainder | `mod` and `%` both appear | `%` or `mod` |
| Loops | “for loop 1 to Y”, `for w = 0 to 5`, `while (n mod 8 not equal to 0) { … }`, `Do … While` | `for i = 1 to 5:`, `while cond:` |
| Increment | `++X`, `X--`, `i++` | `i = i + 1` |
| Integer division | `/` on integers truncates (`n / 10`) | explicit note |

Read the code as if it were Java: integer arithmetic, left-to-right evaluation, `++` and `--` as real operators.

### The dialect in Infosys's own sample paper (2020) `[CONFIRMED — official sample]`

The five pseudocode questions in the official sample are printed with **numbered lines** and a small fixed vocabulary. This is the dialect to expect on the page, and the bank `QB-P1-infosys-dialect-traces` prints its traces the same way:

| Feature | Written like this in the official sample |
|---|---|
| Declaration | `Integer i, j, k, n` |
| Assignment | `Set j=1, k=1` for the first values, then plain `j=j+1`, `k=k+j` |
| Counted loop | `For (each i from 1 to 5)` … `End-for`; an inner loop can start from the outer variable: `For (each j from the value of i to 1)` |
| Condition loop | `While(b)` … `End-while` (the condition is `b` alone, so the loop runs while `b` is non-zero; my reading) |
| Branch | `If (cond) then` … `Else` … `End-if` (casing is not consistent: `if`, `Else`, `end-if` all appear) |
| Logic | `and`, `&&`; remainder is written `MOD` |
| Output | `display "text"` or `print expression` |
| Function | `Integer func (Integer a, Integer b)` … `return a` … `End-function func()` |

Two habits from these five items: two of the five are `If` questions whose condition turns out **false** (one fails exactly at its boundary, `Number>90` with `Number=90`), so check the `Else` branch first; and a `While(b)` loop built on `a MOD b` is Euclid's algorithm. Do not be thrown by the mixed casing; read the structure, not the spelling.

## 3. Concept notes

### 3.1 The one rule

- **`++i` (pre-increment):** add 1 to i, **then** use i.
- **`i++` (post-increment):** use i, **then** add 1 to i.
- Same for `--`.

In both cases **i ends one higher (or lower)**; only the value *used in the expression* differs.

### 3.2 Evaluate left to right

Java (and the pseudocode that mirrors it) evaluates operands **from left to right**, updating i as it goes. So each occurrence of `i`, `i++`, `++i` sees the current value.

Start i = 2:
- `++i + ++i` → (3) + (4) = **7** and i = 4.
- `i++ + i++` → (2) + (3) = 5 and i = 4.
- `i++ + ++i` → (2) + (4) = 6 and i = 4.
- `++i + i++` → (3) + (3) = 6 and i = 4.

### 3.3 A loop with `++x` and `x--`

`do { ++x; display x; x--; } while (x >= -1)` with x = 0: `++x` makes 1; it displays 1; `x--` returns it to 0; the test `0 >= -1` is true; so it repeats forever, printing 1 each time.

### 3.4 Fill-the-blank questions

Write the start value; try each option in turn; compute result and i after each; pick the option that gives both required values. Do not try to reason about “which operator”; just run all four.

### 3.5 Undefined in C

In C, an expression that changes the same variable twice with no sequencing (like `i++ + i++`) is undefined behaviour. The pseudocode in these tests assumes the Java left-to-right reading, so use that.

## 4. Must-memorise block

| Code | i before | Value used | i after |
|---|---|---|---|
| `i++` | 5 | 5 | 6 |
| `++i` | 5 | 6 | 6 |
| `i--` | 5 | 5 | 4 |
| `--i` | 5 | 4 | 4 |

**Whichever form, `i` changes by exactly one.** Only the value used differs.

## 5. Worked examples

**Example 1 — observed P13.** i = 5. Which statement leaves result = 6 and i = 6?
- `result = ++i` → i = 6, result = 6 ✓
- `result = i++` → result = 5, i = 6 ✗
- `result = i + 1` → result = 6, i = 5 ✗
- `result = --i + 2` → i = 4, result = 6 ✗
Only **`result = ++i`**.

**Example 2 — observed P14.** i = 2, result printed must be 7: `++i + ++i` = 3 + 4 = **7**. The others give 5, 6, 6.

**Example 3 — observed P04.** The `do … while` above: **infinite loop printing 1**.

**Example 4 — mixed.** i = 7; `result = i-- + i`. `i--` uses 7, then i = 6; then `i` reads 6; result = 13, i = 6. Output **13 6**.

**Example 5 — mixed with a minus.** i = 4; `result = ++i - i--`. `++i` → 5; then `i--` uses 5, then i = 4; result = 5 − 5 = **0**, i = 4.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Forgetting that `i` changes in a post-increment | `i++` “does nothing” to the value used | Track i on a line of its own |
| Treating `++i + ++i` as `2 × (i+1)` | The second `++i` sees the updated value | Evaluate left to right |
| Reading the expression right to left | C habit | Left to right |
| Stopping after the result | Questions ask for i as well | Finish both columns |
| Assuming a loop terminates | `x--` after `++x` can restore the start | Trace two passes |
| Using C's undefined behaviour as an excuse | The test intends Java order | Use left to right |

## 7. Practice questions

More questions: [`QB-P4-increment-operators-and-dialect.md`](../question-banks/QB-P4-increment-operators-and-dialect.md).

**1.** **[Increment operators]** What is the final value of `i` after this code runs?

```text
int i = 2;
int result = ++i - i++;
print(result, i);
```

a) 4
b) 3
c) 5
d) 2

**2.** **[Increment operators]** What is the final value of `i` after this code runs?

```text
int i = 6;
int result = i - i++ + i++;
print(result, i);
```

a) 9
b) 8
c) 6
d) 7

**3.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 7;
int result = i++ - ++i;
print(result, i);
```

a) -1
b) -3
c) 0
d) -2

**4.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 3;
int result = --i + i;
print(result, i);
```

a) 6
b) 4
c) 5
d) 3

**5.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 5;
int result = ++i + i--;
print(result, i);
```

a) 11
b) 13
c) 12
d) 10

**6.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 7;
int result = i++ + i-- + i--;
print(result, i);
```

a) 22
b) 24
c) 21
d) 23

**7.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 7;
int result = --i + --i;
print(result, i);
```

a) 14
b) 13
c) 11
d) 12

**8.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 5;
int result = --i - i++ - i--;
print(result, i);
```

a) -4 4
b) -5 4
c) 4 -5
d) -5 5

**9.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 3;
int result = --i + --i + --i;
print(result, i);
```

a) 9 3
b) 3 3
c) 6 0
d) 3 0

**10.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 2;
int result = i-- + i;
print(result, i);
```

a) 5
b) 4
c) 3
d) 2

**11.** **[Increment operators]** What is the final value of `i` after this code runs?

```text
int i = 4;
int result = i++ + ++i;
print(result, i);
```

a) 6
b) 7
c) 5
d) 4

**12.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 6;
int result = ++i + i--;
print(result, i);
```

a) 15 6
b) 13 6
c) 12 6
d) 14 6

### ANSWER KEY

1. **a** — Each `++`/`--` changes `i` once, wherever it sits: +2 in total, so `i` ends at 2 +2 = **4**. (result is 0.)
2. **b** — Each `++`/`--` changes `i` once, wherever it sits: +2 in total, so `i` ends at 6 +2 = **8**. (result is 7.)
3. **d** — `i` starts at 7. Evaluate left to right: `i++` reads 7 then i becomes 8; `++i` makes i 9 then reads 9 → result = **-2**, and `i` ends at 9.
4. **b** — `i` starts at 3. Evaluate left to right: `--i` makes i 2 then reads 2; `i` reads 2 → result = **4**, and `i` ends at 2.
5. **c** — `i` starts at 5. Evaluate left to right: `++i` makes i 6 then reads 6; `i--` reads 6 then i becomes 5 → result = **12**, and `i` ends at 5.
6. **a** — `i` starts at 7. Evaluate left to right: `i++` reads 7 then i becomes 8; `i--` reads 8 then i becomes 7; `i--` reads 7 then i becomes 6 → result = **22**, and `i` ends at 6.
7. **c** — `i` starts at 7. Evaluate left to right: `--i` makes i 6 then reads 6; `--i` makes i 5 then reads 5 → result = **11**, and `i` ends at 5.
8. **b** — Left to right: `--i` makes i 4 then reads 4; `i++` reads 4 then i becomes 5; `i--` reads 5 then i becomes 4. result = -5, i = 4 → **-5 4**.
9. **d** — Left to right: `--i` makes i 2 then reads 2; `--i` makes i 1 then reads 1; `--i` makes i 0 then reads 0. result = 3, i = 0 → **3 0**.
10. **c** — `i` starts at 2. Evaluate left to right: `i--` reads 2 then i becomes 1; `i` reads 1 → result = **3**, and `i` ends at 1.
11. **a** — Each `++`/`--` changes `i` once, wherever it sits: +2 in total, so `i` ends at 4 +2 = **6**. (result is 10.)
12. **d** — Left to right: `++i` makes i 7 then reads 7; `i--` reads 7 then i becomes 6. result = 14, i = 6 → **14 6**.

## 8. Resources

- **https://docs.oracle.com/javase/tutorial/java/nutsandbolts/op1.html** — the Java tutorial page on the increment and decrement operators.
- **https://www.geeksforgeeks.org/java/operators-in-java/** — Java operators, including the increment and decrement operators.

## 9. Self-check

1. Can you say what `x = i++` leaves in x and in i, starting from i = 5?
2. Can you evaluate `++i + ++i` from i = 2 in five seconds?
3. Why does `do { ++x; display x; x--; } while (x >= -1)` never stop?
4. What is different about increments in C and in Java?
5. List the Infosys dialect differences from the Accenture dialect.

## 10. Sources

This file was written for this library. **Infosys evidence:** observed questions P13, P14 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `P4`). Confidence **Medium**. Practice questions in §7 and the bank were generated and checked by execution (brute force, simulation or inverse); see `../research/04-qa-report.md`. Nothing here is a published Infosys syllabus.
