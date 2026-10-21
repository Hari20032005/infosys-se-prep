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
course: core
lesson: 7
---

# Lesson 07. Operator logic and equation balancing

*Topic `A3` · about 1.2 of the 75 marks · plan about 0.6 hours.*

## 1. The idea

In operator logic, the usual signs are given new meanings. A made-up symbol such as ★ or $ does something to the numbers, and you must find out what. Sometimes the ordinary signs +, −, × and ÷ swap roles, and you have to work through the swap carefully.

You never need advanced maths. You need a calm way to find the rule: look at the first example, try a few simple ideas, and confirm on the second.

There are four types, and they are easy to tell apart:

- **A hidden rule.** Two lines show what ★ does. Find the rule and use it.
- **A rule on the digits.** The symbol works on the digits of a number, not the number.
- **Swapped signs.** "+ means −" and so on. Swap first, then calculate.
- **Interchange.** Swap two numbers so the equation becomes true.

## 2. What Infosys actually asks

Two operator questions were found in the 2025 reports `[REPORTED]`:

- `264 * 2 = 6` and `870 * 3 = 11`, then `735 * 5 = ?`. The rule: divide, then add the digits of the answer. The answer is 12.
- `$59 = 135`, `$48 = 122`, `$96 = 144`, then `$136 = ?`. The rule: multiply the two digits and add 90. The offered answer is 168, but the question is unclear for a three-digit number, so treat it with care.

A third type, interchanging two numbers to make an equation true, was seen but its signs were unreadable in the source, so it is included as practice but is not counted as an Infosys item.

The official 2020 sample had no question of this kind. The Reasoning section is 15 questions in 25 minutes, about 100 seconds each.

## 3. The method

1. **Take the first line.** Try the simplest idea: one operation on the two numbers.
2. **If that fails, try the next idea.** In order:
    - an operation, then digit work on the result (adding the digits);
    - an operation on the **digits** of a number;
    - an operation with a constant added or subtracted.
3. **Confirm on the second line.** If it fails, drop the rule.
4. **Apply to the last line.** Compute carefully and check against the options.
5. **For swapped signs:** write the new expression with every sign replaced by what it stands for. Only then calculate, using BODMAS (brackets first, then division and multiplication, then addition and subtraction).
6. **For interchange:** there are only six pairs among four numbers. Try each pair and see which gives the target.

BODMAS means: brackets, orders (powers), division and multiplication, addition and subtraction. When a line has only multiplication and division, go left to right. The same goes for addition and subtraction.

## 4. Shortcuts and when they fail

**Last-digit check.** To test a rule quickly, compare only the last digits of the result. *It fails for digit rules* because those change the last digit in a different way.

**Digit-sum of a quotient: stop once.** If the example shows 11, it did not reduce further. Match what the example does. *It fails if the example reduced to a single digit.*

**For the interchange question, test the bigger numbers first.** A big number in a multiplication spot changes the result the most. *It fails for equations with only plus and minus*, where position does not matter.

**Use the third example.** If your rule fits two lines, test it on a third line if there is one. *It fails only if there is no third line.*

## 5. Worked examples

All the answers below were checked by code.

**Example 1 (divide, then add the digits).** If 360 ★ 4 = 9 and 496 ★ 8 = 8, find 574 ★ 7.

360 ÷ 4 = 90 and 9 + 0 = 9. 496 ÷ 8 = 62 and 6 + 2 = 8. So the rule is divide, then add the digits of the answer. 574 ÷ 7 = 82 and 8 + 2 = **10**.

**Example 2 (a rule on the digits).** If $37 = 31 and $52 = 20, find $84.

Split the number into digits. 3 × 7 = 21, and 31 − 21 = 10. 5 × 2 = 10, and 20 − 10 = 10. So the rule is "multiply the digits and add 10". $84 = 8 × 4 + 10 = **42**.

**Example 3 (swapped signs).** In a code, + means −, − means ×, and × means +. Find the value of 8 × 3 + 4 − 2.

Swap each sign: × becomes +, + becomes −, − becomes ×. The expression is now 8 + 3 − 4 × 2. Multiply first: 4 × 2 = 8. Then 8 + 3 − 8 = **3**.

**Example 4 (interchange).** Which two numbers must be swapped to make 3 + 8 × 5 − 2 = 39?

The left side is now 41. Try the swaps: 3 and 8 give 21. 8 and 5 give 41. 5 and 2 give 14. 3 and 5 give 27. 8 and 2 give 5. 3 and 2 give 2 + 8 × 5 − 3 = 39. The answer is **3 and 2**, and no other pair works.

**Example 5 (a nested operator).** If a ★ b = 2a + b, find (3 ★ 4) ★ 5.

Do the bracket first: 3 ★ 4 = 6 + 4 = 10. Then 10 ★ 5 = 20 + 5 = **25**. Notice that 3 ★ (4 ★ 5) would give 19, so the brackets matter.

## 6. Traps

- **Reducing the digit sum too far.** If the example says 11, stop at 11.
- **Calculating before swapping.** Replace every sign first. Then use BODMAS.
- **Reading a three-digit number as two digits.** Be clear about how the rule treats extra digits. In the unclear case, pick the reading that gives one of the options.
- **Leaving out the brackets.** In (3 ★ 4) ★ 5, the bracket goes first.
- **Testing a rule on one line only.** A coincidence on one line is common.


## 7. Practice questions

Attempt each level before opening the key. Level 3 is harder than anything in the 2020 official sample, on purpose: if you can do Level 3, the real paper will feel easy.

### Level 1: warm-up

*One-step rules between two numbers, a simple sign swap, and a bracket with a rule you are told.*

**1.** **[Inferred operator]** A new operation ★ works the same way every time. If 7 ★ 8 = 30, 7 ★ 3 = 20, 9 ★ 4 = 26, find 8 ★ 4.  
a) 24  
b) 30  
c) 21  
d) 14  

**2.** **[Inferred operator]** A new operation ★ works the same way every time. If 5 ★ 8 = 18, 2 ★ 5 = 9, 4 ★ 7 = 15, find 7 ★ 6.  
a) 21  
b) 18  
c) 20  
d) 24  

**3.** **[Inferred operator]** A new operation ★ works the same way every time. If 5 ★ 9 = 28, 6 ★ 9 = 30, 4 ★ 6 = 20, find 4 ★ 9.  
a) 27  
b) 28  
c) 29  
d) 26  

**4.** **[Sign substitution]** If ‘+’ means ‘×’, ‘−’ means ‘+’, ‘×’ means ‘÷’, ‘÷’ means ‘−’, what is the value of 2 ÷ 5 − 8 − 10 ?  
a) 19  
b) -15  
c) 17  
d) 15  

**5.** **[Nested operator]** If a ★ b = a + 2b, find the value of (2 ★ 6) ★ 2.  
a) 30  
b) 18  
c) 16  
d) 22  

### Level 2: exam level

*The kinds seen in reports: divide then add digits, a rule on digits, a rule with two steps, a sign swap, and an interchange.*

**6.** **[Divide then digit-sum]** If 639 ★ 9 = 8 and 364 ★ 7 = 7, find 412 ★ 4.  
a) 103  
b) 4  
c) 5  
d) 16  

**7.** **[Digit product plus constant]** If $67 = 122 and $51 = 85, what is $35 ? (Here $ is a mathematical operator acting on the two digits.)  
a) 95  
b) 105  
c) 15  
d) 88  

**8.** **[Inferred operator]** A new operation ★ works the same way every time. If 5 ★ 4 = 29, 8 ★ 5 = 53, 9 ★ 8 = 89, find 3 ★ 7.  
a) 36  
b) 35  
c) 31  
d) 39  

**9.** **[Sign substitution]** If ‘+’ means ‘÷’, ‘−’ means ‘+’, ‘×’ means ‘−’, ‘÷’ means ‘×’, what is the value of 10 ÷ 5 ÷ 9 × 3 ?  
a) -447  
b) 449  
c) 451  
d) 447  

**10.** **[Interchange numbers]** Which two **numbers** must be interchanged for the equation to be correct?  

5 × 4 + 10 + 9 = 54
a) 4 and 9  
b) 5 and 10  
c) 10 and 9  
d) 4 and 5  

### Level 3: beyond the exam

*Two nested operators in one line, and interchange and digit-rule questions with larger numbers.*

**11.** **[Nested operator]** If a ★ b = a² − b, find the value of (7 ★ 5) ★ 7.  
a) 51  
b) 31  
c) 1929  
d) 5  

**12.** **[Nested operator]** If a ★ b = a × b + b, find the value of (2 ★ 2) ★ 4.  
a) 30  
b) 10  
c) 28  
d) 36  

**13.** **[Interchange numbers]** Which two **numbers** must be interchanged for the equation to be correct?  

8 − 11 + 13 − 12 = −6
a) 11 and 12  
b) 11 and 13  
c) 12 and 8  
d) 13 and 8  

**14.** **[Interchange numbers]** Which two **numbers** must be interchanged for the equation to be correct?  

5 + 15 − 8 + 7 = 21
a) 8 and 7  
b) 15 and 7  
c) 5 and 8  
d) 5 and 7  

**15.** **[Digit product plus constant]** If $17 = 47 and $51 = 45, what is $34 ? (Here $ is a mathematical operator acting on the two digits.)  
a) 52  
b) 47  
c) 62  
d) 12  

### ANSWER KEY

1. **a** — Test rules on the first line, then confirm on the others. The rule that fits all three is **(2)(a+b)**: 7 ★ 8 → 30; 7 ★ 3 → 20; 9 ★ 4 → 26. So 8 ★ 4 = **24**.
2. **c** — Test rules on the first line, then confirm on the others. The rule that fits all three is **2a + b**: 5 ★ 8 → 18; 2 ★ 5 → 9; 4 ★ 7 → 15. So 7 ★ 6 = **20**.
3. **d** — Test rules on the first line, then confirm on the others. The rule that fits all three is **(2)(a+b)**: 5 ★ 9 → 28; 6 ★ 9 → 30; 4 ★ 6 → 20. So 4 ★ 9 = **26**.
4. **d** — Swap each sign for what it stands for first: 2 ÷ 5 − 8 − 10 becomes 2 − 5 + 8 + 10. Now apply BODMAS (division and multiplication before addition and subtraction): **15**.
5. **b** — Work out the bracket first: 2 ★ 6 = 14. Then 14 ★ 2 = **18**. (Doing 6 ★ 2 first would give 22, which is a different question.)
6. **b** — Divide, then add the digits of the quotient **once**. 639 ÷ 9 = 71 → 8; 364 ÷ 7 = 52 → 7. 412 ÷ 4 = 103 → **4**.
7. **a** — Split each number into its digits, multiply them and add 80: 6×7 + 80 = 122; 5×1 + 80 = 85. So $35 = 3×5 + 80 = **95**.
8. **c** — Test rules on the first line, then confirm on the others. The rule that fits all three is **a×b + a + b**: 5 ★ 4 → 29; 8 ★ 5 → 53; 9 ★ 8 → 89. So 3 ★ 7 = **31**.
9. **d** — Swap each sign for what it stands for first: 10 ÷ 5 ÷ 9 × 3 becomes 10 × 5 × 9 − 3. Now apply BODMAS (division and multiplication before addition and subtraction): **447**.
10. **b** — Try the swaps. Interchanging 5 and 10 gives 10 × 4 + 5 + 9 = 54 (BODMAS). No other pair of these numbers works.
11. **c** — Work out the bracket first: 7 ★ 5 = 44. Then 44 ★ 7 = **1929**. (Doing 5 ★ 7 first would give 31, which is a different question.)
12. **c** — Work out the bracket first: 2 ★ 2 = 6. Then 6 ★ 4 = **28**. (Doing 2 ★ 4 first would give 36, which is a different question.)
13. **b** — Try the swaps. Interchanging 11 and 13 gives 8 − 13 + 11 − 12 = −6 (BODMAS). No other pair of these numbers works.
14. **a** — Try the swaps. Interchanging 8 and 7 gives 5 + 15 − 7 + 8 = 21 (BODMAS). No other pair of these numbers works.
15. **a** — Split each number into its digits, multiply them and add 40: 1×7 + 40 = 47; 5×1 + 40 = 45. So $34 = 3×4 + 40 = **52**.

## 8. Recap in 60 seconds

- Find the rule on line 1, confirm on line 2, then use it.
- Order of ideas: one operation, operation then digit work, operation on digits, add a constant.
- Digit-sum: stop after one pass unless the example reduced further.
- Swapped signs: replace every sign first, then BODMAS.
- Interchange: try all six pairs.
- Brackets first when the operator is nested.

## 9. Sources

- `../question-banks/QB-99-OBSERVED-POOL.md`: the two operator items reported in 2025, solved by running code.
- Every result in the five examples is computed and checked in `data/cc_examples.py`. No outside website is cited, because the rules are arithmetic and the order of operations is standard (see `../research/06-method-sources.md`).
