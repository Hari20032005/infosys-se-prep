---
title: Bitwise operators
code: P3
section: Pseudocode
weightage_pct: 1.5% of marks
est_questions: 0.56
tier: 2
difficulty: Hard
est_study_hours: 0.8
confidence: Medium
last_updated: 2026-09-30
course: core
lesson: 21
---

# Lesson 21. Bitwise operators

*Topic `P3` · about 1.1 of the 75 marks · plan about 0.8 hours.*

## 1. The idea

A computer stores a whole number as a row of bits, which are 0s and 1s. Bitwise operators work on those bits, one position at a time. They are easy once you write the numbers in binary, and they are risky if you try to do them in your head.

There are only a few operators:

- **`&` (AND):** a bit is 1 only if both bits are 1.
- **`|` (OR):** a bit is 1 if at least one bit is 1.
- **`^` (XOR):** a bit is 1 if the two bits are different.
- **`<<` (shift left):** moves the bits left. Shifting left by k multiplies by 2 to the power k.
- **`>>` (shift right):** moves the bits right. Shifting right by k divides by 2 to the power k and drops the fraction.

The other thing to know is **precedence**: which operator is done first when several appear in one line.

## 2. What Infosys actually asks

One question of this kind was reported from the 2025 exams: a line using `^` and `&` and `+` together with two variables, asking for the value printed. The answer was 1 `[REPORTED]`. The official 2020 sample had no bitwise question.

Pseudocode is 5 questions worth 10 marks in 10 minutes, so each question is worth about 2 marks and two minutes. Bitwise questions are rare, so this lesson is short. The one skill that pays off is the **order of operations**, because that is where the reported question tricked people.

## 3. The method

1. **Fill in the values.** Replace each variable with its number.
2. **Put the operators in order.** Highest first:

| Order | Operators |
|---|---|
| 1 (first) | `*`, then `+` and `-` |
| 2 | `<<` and `>>` |
| 3 | `&` |
| 4 | `^` |
| 5 (last) | `|` |

3. **Add brackets in your head** around the operator that goes first, then the next.
4. **For `&`, `|` and `^`, write the numbers in binary**, one under the other, and work column by column.
5. **For a shift, use multiplying and dividing:** `x << k` is x times 2 to the k, and `x >> k` is x divided by 2 to the k with the fraction dropped.
6. **Convert back** to an ordinary number.

A quick way to remember the order: arithmetic first, then shifts, then AND, then XOR, then OR. Arithmetic operators are done before bitwise ones.

## 4. Shortcuts and when they fail

**Powers of 2.** `1 << k` is 2 to the k: 2, 4, 8, 16, 32. A number and `x & 1` tell you whether x is odd (the answer is 1) or even (0). *It fails if you forget that `&` works on every bit, not only the last.*

**XOR with itself is 0.** `x ^ x` is 0, and `x ^ 0` is x. *It fails for numbers that are not equal.*

**AND can only lower or keep a number.** `x & y` is never bigger than the smaller of the two. OR can only raise or keep it. *These help you reject options that are too big or too small.*

**Always write the binary.** Eight bits are enough for numbers below 256. *It fails only when you make a slip in converting*, so convert back and check.

## 5. Worked examples

Every output was checked by running the printed program as Java.

**Example 1 (the three operators on 12 and 10).**

```text
1) Print 12 & 10
2) Print 12 | 10
3) Print 12 ^ 10
```

In binary 12 is 1100 and 10 is 1010. Column by column: AND gives 1000, which is 8. OR gives 1110, which is 14. XOR gives 0110, which is 6. Output: **8 14 6**.

**Example 2 (shifts).**

```text
1) Print 5 << 2
2) Print 20 >> 1
```

Shifting left by 2 multiplies by 4: 5 becomes 20. Shifting right by 1 divides by 2: 20 becomes 10. Output: **20 10**.

**Example 3 (arithmetic before AND).**

```text
1) Print 3 + 4 & 5
```

The plus goes first: 3 + 4 = 7. Then 7 & 5: 111 and 101 give 101, which is 5. Output: **5**. (If you did the AND first you would get 4 & 5 = 4, then 3 + 4 = 7. That is wrong.)

**Example 4 (AND before OR).**

```text
1) Print 6 | 3 & 5
```

The AND goes first: 3 & 5 is 011 and 101, which gives 001, which is 1. Then 6 | 1 is 110 and 001, which is 111, which is 7. Output: **7**.

**Example 5 (an assignment with three operators).**

```text
1) Integer x, y
2) Set x = 5, y = 3
3) Set x = x ^ 6 & y + 1
4) Print x
```

Put in the values: 5 ^ 6 & 3 + 1. The plus goes first: 3 + 1 = 4. Then AND: 6 & 4 = 4. Then XOR: 5 ^ 4 = 1. Output: **1**. Reading left to right would give (5 ^ 6) & 3 + 1 = 3 & 4 = 0, which is wrong.

## 6. Traps

- **Reading left to right.** The bitwise operators have their own order.
- **Doing `&` before `+`.** The plus goes first, which surprises many people.
- **Comparing with `==` in the same line.** In Java, `n & 3 == 0` does not compile, because `==` binds tighter than `&`. If you see it in an exam, work out which way the question means it.
- **Shifting a negative number.** The questions here use positive numbers only.
- **Forgetting that `>>` drops the fraction.** 7 >> 1 is 3.


## 7. Practice questions

Attempt each level before opening the key. Level 3 is harder than anything in the 2020 official sample, on purpose: if you can do Level 3, the real paper will feel easy.

### Level 1: warm-up

*One operator on two numbers.*

**1.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 23, b = 27, c = 20
3) Print c & a
```

a) 21  
b) 18  
c) 20  
d) 22  

**2.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 27, b = 11, c = 19
3) Print a << 1
```

a) 55  
b) 52  
c) 54  
d) 56  

**3.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 6, b = 17, c = 29
3) Print c >> 2
```

a) 6  
b) 7  
c) 9  
d) 5  

**4.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 4, b = 15, c = 4
3) Print 12 ^ c
```

a) 6  
b) 9  
c) 8  
d) 10  

**5.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 21, b = 15, c = 24
3) Print 3 << 1
```

a) 8  
b) 6  
c) 4  
d) 7  

### Level 2: exam level

*Two operators, and arithmetic mixed with a shift or an AND.*

**6.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 31, b = 10, c = 17
3) Print 3 ^ a + 11
```

a) 39  
b) 43  
c) 40  
d) 41  

**7.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 18, b = 30, c = 11
3) Print a ^ c & c
```

a) 25  
b) 24  
c) 9  
d) 27  

**8.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 5, b = 7, c = 20
3) Print 11 & b << 2
```

a) 12  
b) 8  
c) 10  
d) 9  

**9.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 25, b = 22, c = 29
3) Print a | a << 1
```

a) 59  
b) 50  
c) 58  
d) 61  

**10.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 10, b = 30, c = 16
3) Print c ^ b << 1
```

a) 45  
b) 44  
c) 28  
d) 46  

### Level 3: beyond the exam

*Three or four operators in one assignment, where reading left to right gives a different answer.*

**11.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 4, b = 5, c = 19
3) Set a = 12 | c * c & 4
4) Print a
```

a) 12  
b) 14  
c) 4  
d) 13  

**12.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 10, b = 27, c = 7
3) Set a = b ^ b + 9 & b
4) Print a
```

a) 27  
b) 29  
c) 9  
d) 26  

**13.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 18, b = 4, c = 8
3) Set a = 11 * a ^ b * b
4) Print a
```

a) 216  
b) 215  
c) 776  
d) 214  

**14.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 15, b = 29, c = 8
3) Set a = b | 7 >> 3 << 3
4) Print a
```

a) 24  
b) 31  
c) 29  
d) 28  

**15.** **[Bitwise operators]** What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)  

```text
1) Integer a, b, c
2) Set a = 13, b = 22, c = 25
3) Set a = 9 ^ 14 & 12 & b << 2
4) Print a
```

a) 3  
b) 16  
c) 0  
d) 1  

### ANSWER KEY

1. **c** — 20 is 10100 in binary and 23 is 10111. Applying & bit by bit gives 10100, which is **20**.
2. **c** — 27 is 11011 in binary and 1 is 1. Applying << bit by bit gives 110110, which is **54**.
3. **b** — 29 is 11101 in binary and 2 is 10. Applying >> bit by bit gives 111, which is **7**.
4. **c** — 12 is 1100 in binary and 4 is 100. Applying ^ bit by bit gives 1000, which is **8**.
5. **b** — 3 is 11 in binary and 1 is 1. Applying << bit by bit gives 110, which is **6**.
6. **d** — Work out the operator that binds tightest first (order: `*` and `+`, then `<<` `>>`, then `&`, then `^`, then `|`). With the values filled in the expression is `3 ^ 31 + 11`, and the result is **41**. (Reading it left to right would wrongly give 39.)
7. **a** — Work out the operator that binds tightest first (order: `*` and `+`, then `<<` `>>`, then `&`, then `^`, then `|`). With the values filled in the expression is `18 ^ 11 & 11`, and the result is **25**. (Reading it left to right would wrongly give 9.)
8. **b** — Work out the operator that binds tightest first (order: `*` and `+`, then `<<` `>>`, then `&`, then `^`, then `|`). With the values filled in the expression is `11 & 7 << 2`, and the result is **8**. (Reading it left to right would wrongly give 12.)
9. **a** — Work out the operator that binds tightest first (order: `*` and `+`, then `<<` `>>`, then `&`, then `^`, then `|`). With the values filled in the expression is `25 | 25 << 1`, and the result is **59**. (Reading it left to right would wrongly give 50.)
10. **b** — Work out the operator that binds tightest first (order: `*` and `+`, then `<<` `>>`, then `&`, then `^`, then `|`). With the values filled in the expression is `16 ^ 30 << 1`, and the result is **44**. (Reading it left to right would wrongly give 28.)
11. **a** — Work out the operator that binds tightest first (order: `*` and `+`, then `<<` `>>`, then `&`, then `^`, then `|`). With the values filled in the expression is `12 | 19 * 19 & 4`, and the result is **12**. (Reading it left to right would wrongly give 4.)
12. **a** — Work out the operator that binds tightest first (order: `*` and `+`, then `<<` `>>`, then `&`, then `^`, then `|`). With the values filled in the expression is `27 ^ 27 + 9 & 27`, and the result is **27**. (Reading it left to right would wrongly give 9.)
13. **d** — Work out the operator that binds tightest first (order: `*` and `+`, then `<<` `>>`, then `&`, then `^`, then `|`). With the values filled in the expression is `11 * 18 ^ 4 * 4`, and the result is **214**. (Reading it left to right would wrongly give 776.)
14. **c** — Work out the operator that binds tightest first (order: `*` and `+`, then `<<` `>>`, then `&`, then `^`, then `|`). With the values filled in the expression is `29 | 7 >> 3 << 3`, and the result is **29**. (Reading it left to right would wrongly give 24.)
15. **d** — Work out the operator that binds tightest first (order: `*` and `+`, then `<<` `>>`, then `&`, then `^`, then `|`). With the values filled in the expression is `9 ^ 14 & 12 & 22 << 2`, and the result is **1**. (Reading it left to right would wrongly give 16.)

## 8. Recap in 60 seconds

- `&` both 1, `|` at least one 1, `^` different bits.
- `<<` multiplies by 2 each step. `>>` divides by 2 each step and drops the fraction.
- Order: arithmetic, then shifts, then `&`, then `^`, then `|`.
- Write the binary. Work column by column. Convert back.
- Add brackets in your head for the operator that goes first.
- Do not read left to right.

## 9. Sources

- [The Java Tutorials: Bitwise and Bit Shift Operators](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/op3.html): `&` is bitwise AND, `^` bitwise exclusive OR, `|` bitwise inclusive OR, and the shift operators (S2 in `../research/06-method-sources.md`).
- [The Java Tutorials: Operators](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html): the precedence table, with multiplicative and additive operators above shifts, and shifts above relational, equality, `&`, `^` and `|`.
- Every output above comes from translating the printed program to Java and running it (`data/cc_examples.py`).
