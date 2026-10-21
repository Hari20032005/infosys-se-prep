---
title: Operator logic and equation balancing
code: A3
section: Reasoning Ability
weightage_pct: 1.6% of marks
est_questions: 1.20
tier: 2
difficulty: Medium
est_study_hours: 0.6
confidence: High
last_updated: 2026-09-30
---

# A3 — Operator logic and equation balancing

## 1. Why this topic matters here

Expect about **1.2 questions and 1.2 marks** on this topic (about 1.6% of the 75 scored marks). It sits in **Reasoning Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 2**, 0.6 hours to reach reliable recall, confidence **High**.

**2 questions on this topic are in the observed Infosys pool** (R09, R12), from 2 sources. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 2.00 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

"Operator logic" here means a made-up operator whose rule you must infer from two worked lines, plus sign-swap and interchange items. Two items were recovered from the 2025–26 pool `[REPORTED]`; a third (interchange two numbers) was seen but its operators were lost in the recording.

| Sub-pattern | How it appears | Observed |
|---|---|---|
| Divide, then add the digits of the quotient | `264 * 2 = 6`, `870 * 3 = 11`, `735 * 5 = ?` | R09 |
| An operator acting on the digits of a number | `$59 = 135`, `$48 = 122`, `$96 = 144`, `$136 = ?` | R12 |
| Interchange two numbers or signs to fix an equation | `17 ? 2 ? 3 + 5 ? 6 = 12` with options like "2 and 5", "6 and 3" | X01 (discarded: operators unreadable) |
| Replace the signs by the stated meanings, then evaluate | "if + means −, − means +, × means ÷ …" | authored from the pattern |

## 3. Concept notes

### 3.1 How to find the rule

Take the **first** line and try, in this order: (1) a single operation on the two numbers; (2) an operation, then **digit work** on the result; (3) an operation on the **digits** of one number; (4) a constant added or subtracted. Confirm on the second line. Apply to the third.

### 3.2 Divide, then digit-sum (R09)

`264 * 2 = 6`: 264 ÷ 2 = 132, digits 1 + 3 + 2 = 6 ✓. `870 * 3 = 11`: 870 ÷ 3 = 290, 2 + 9 + 0 = 11 ✓ (**not** reduced again to 2). `735 * 5`: 147, 1 + 4 + 7 = **12**.

The coach's point: stop after one digit sum. If the first example had said 2, you would reduce again; it says 11, so you do not.

### 3.3 Operators on the digits (R12)

`$59 = 135`: 5 × 9 = 45; 135 − 45 = 90. `$48 = 122`: 32; 122 − 32 = 90. `$96 = 144`: 54; 144 − 54 = 90. So `$ab = a × b + 90`.

**The ambiguity.** `$136` has three digits. Read as 13 and 6: 13 × 6 + 90 = **168**, the option offered. Read as 1, 3, 6: 1×3×6 + 90 = 108. On the real test, the rule that produces an offered option is the intended one.

### 3.4 Sign substitution

Replace every sign by what it *stands for* first, then use BODMAS. Write the new expression out. Example: if × means ÷ and ÷ means ×, then `12 ÷ 6 × 8` becomes `12 × 6 ÷ 8` = 72 ÷ 8 = **9**.

### 3.5 Interchange to make the equation correct

Try every pair: there are only six pairs among four numbers. Compute the left side after each swap and compare with the right side. The wrong options fail, the right one gives exactly the target.

## 4. Must-memorise block

| Item | Rule |
|---|---|
| Step order | one operation → operation + digit work → operation on digits → constant |
| BODMAS | brackets, orders, division and multiplication (left to right), addition and subtraction (left to right) |
| Sign substitution | swap first, then evaluate |
| Digit-sum | stop after **one** pass unless the example reduced further |

## 5. Worked examples

**Example 1 (R09).** Above: **12**.

**Example 2 (R12).** Above: **168** (with the ambiguity noted).

**Example 3 — sign substitution.** If ‘+’ means ‘×’, ‘×’ means ‘−’, ‘−’ means ‘÷’, ‘÷’ means ‘+’, find `8 + 3 − 6 × 2 ÷ 5`. Substitute: `8 × 3 ÷ 6 − 2 + 5`. Evaluate: 8 × 3 = 24; 24 ÷ 6 = 4; 4 − 2 + 5 = **7**.

**Example 4 — interchange two numbers.** Which two numbers must be interchanged for `3 + 8 × 5 − 2 = 39`? Left side now: 3 + 40 − 2 = 41. Try swapping 3 and 8: 8 + 3 × 5 − 2 = 21. Swap 8 and 5: 3 + 5 × 8 − 2 = 41. Swap 5 and 2: 3 + 8 × 2 − 5 = 14. Swap 3 and 2: 2 + 8 × 5 − 3 = 39 ✓. The answer is **3 and 2**.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Reducing the digit sum twice | Habit | Copy the first example's behaviour exactly |
| Ignoring a constant | The product fits except for +90 | Compare output with the plain product |
| Evaluating before substituting | The symbols look normal | Rewrite the expression before any arithmetic |
| Wrong order (left-to-right only) | BODMAS puts × and ÷ first | Write the intermediate values |
| Three-digit inputs | Ambiguity | Choose the reading that gives an offered option |
| Checking only one line | The rule can be a coincidence | Verify on the second line |

## 7. Practice questions

More questions: [`QB-A3-operator-logic.md`](../question-banks/QB-A3-operator-logic.md).

**1.** **[Digit product plus constant]** If $81 = 38 and $88 = 94, what is $91 ? (Here $ is a mathematical operator acting on the two digits.)
a) 39
b) 40
c) 9
d) 49

**2.** **[Divide then digit-sum]** If 1116 ★ 9 = 7 and 340 ★ 5 = 14, find 584 ★ 8.
a) 73
b) 10
c) 7
d) 11

**3.** **[Divide then digit-sum]** If 424 ★ 8 = 8 and 1098 ★ 9 = 5, find 240 ★ 5.
a) 12
b) 13
c) 48
d) 2

**4.** **[Sign substitution]** If ‘+’ means ‘×’, ‘−’ means ‘+’, ‘×’ means ‘÷’, ‘÷’ means ‘−’, what is the value of 8 ÷ 5 + 4 ÷ 2 ?
a) -10
b) -14
c) 14
d) -12

**5.** **[Sign substitution]** If ‘+’ means ‘−’, ‘−’ means ‘÷’, ‘×’ means ‘+’, ‘÷’ means ‘×’, what is the value of 7 ÷ 4 + 4 × 4 ?
a) 32
b) 30
c) 28
d) -28

**6.** **[Sign substitution]** If ‘+’ means ‘−’, ‘−’ means ‘+’, what is the value of 11 + 8 ÷ 11 × 11 ?
a) 19
b) -3
c) 3
d) 5

**7.** **[Divide then digit-sum]** If 605 ★ 5 = 4 and 660 ★ 6 = 2, find 408 ★ 8.
a) 51
b) 7
c) 18
d) 6

**8.** **[Sign substitution]** If ‘+’ means ‘×’, ‘×’ means ‘÷’, ‘÷’ means ‘+’, what is the value of 6 ÷ 6 + 4 − 10 ?
a) -5
b) 22
c) 20
d) -20

**9.** **[Digit product plus constant]** If $63 = 118 and $61 = 106, what is $69 ? (Here $ is a mathematical operator acting on the two digits.)
a) 164
b) 154
c) 54
d) 115

**10.** **[Sign substitution]** If ‘+’ means ‘÷’, ‘−’ means ‘×’, ‘×’ means ‘−’, ‘÷’ means ‘+’, what is the value of 12 + 6 × 8 ÷ 7 ?
a) 5
b) -1
c) 3
d) 1

**11.** **[Sign substitution]** If ‘+’ means ‘−’, ‘−’ means ‘÷’, ‘×’ means ‘+’, ‘÷’ means ‘×’, what is the value of 7 × 2 + 3 × 10 ?
a) 44
b) 18
c) -16
d) 16

**12.** **[Divide then digit-sum]** If 88 ★ 2 = 8 and 1080 ★ 8 = 9, find 738 ★ 6.
a) 6
b) 8
c) 123
d) 7

### ANSWER KEY

1. **a** — Split each number into its digits, multiply them and add 30: 8×1 + 30 = 38; 8×8 + 30 = 94. So $91 = 9×1 + 30 = **39**.
2. **b** — Divide, then add the digits of the quotient **once**. 1116 ÷ 9 = 124 → 7; 340 ÷ 5 = 68 → 14. 584 ÷ 8 = 73 → **10**.
3. **a** — Divide, then add the digits of the quotient **once**. 424 ÷ 8 = 53 → 8; 1098 ÷ 9 = 122 → 5. 240 ÷ 5 = 48 → **12**.
4. **b** — Swap each sign for what it stands for first: 8 ÷ 5 + 4 ÷ 2 becomes 8 − 5 × 4 − 2. Now apply BODMAS (division and multiplication before addition and subtraction): **-14**.
5. **c** — Swap each sign for what it stands for first: 7 ÷ 4 + 4 × 4 becomes 7 × 4 − 4 + 4. Now apply BODMAS (division and multiplication before addition and subtraction): **28**.
6. **c** — Swap each sign for what it stands for first: 11 + 8 ÷ 11 × 11 becomes 11 − 8 ÷ 11 × 11. Now apply BODMAS (division and multiplication before addition and subtraction): **3**.
7. **d** — Divide, then add the digits of the quotient **once**. 605 ÷ 5 = 121 → 4; 660 ÷ 6 = 110 → 2. 408 ÷ 8 = 51 → **6**.
8. **c** — Swap each sign for what it stands for first: 6 ÷ 6 + 4 − 10 becomes 6 + 6 × 4 − 10. Now apply BODMAS (division and multiplication before addition and subtraction): **20**.
9. **b** — Split each number into its digits, multiply them and add 100: 6×3 + 100 = 118; 6×1 + 100 = 106. So $69 = 6×9 + 100 = **154**.
10. **d** — Swap each sign for what it stands for first: 12 + 6 × 8 ÷ 7 becomes 12 ÷ 6 − 8 + 7. Now apply BODMAS (division and multiplication before addition and subtraction): **1**.
11. **d** — Swap each sign for what it stands for first: 7 × 2 + 3 × 10 becomes 7 + 2 − 3 + 10. Now apply BODMAS (division and multiplication before addition and subtraction): **16**.
12. **a** — Divide, then add the digits of the quotient **once**. 88 ÷ 2 = 44 → 8; 1080 ÷ 8 = 135 → 9. 738 ÷ 6 = 123 → **6**.

## 8. Resources

- **https://www.geeksforgeeks.org/bodmas-rule/** — the order-of-operations rule with examples.
- **https://www.indiabix.com/puzzles/number-puzzles/** — number puzzles where a hidden operation must be inferred from worked lines.

## 9. Self-check

1. Can you state the four-step rule-finding order?
2. Why is `870 * 3 = 11` not reduced to 2?
3. Can you recompute `$136` in both readings and say which one to choose?
4. Can you solve a sign-substitution expression without writing the wrong symbols?
5. How many pairs do you need to try in an interchange question with four numbers?

## 10. Sources

This file was written for this library. **Infosys evidence:** observed questions R09, R12 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A3`). Confidence **High**. Practice questions in §7 and the bank were generated and checked by execution (brute force, simulation or inverse); see `../research/04-qa-report.md`. Nothing here is a published Infosys syllabus.
