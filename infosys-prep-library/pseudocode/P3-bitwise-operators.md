---
title: Bitwise Operators and Operator Precedence
code: P3
section: Pseudocode
weightage_pct: 1.5% of marks
est_questions: 0.56
tier: 2
difficulty: Hard
est_study_hours: 0.8
confidence: Medium
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-library/topics/T11-B7-bitwise-operators.md
---

# P3 — Bitwise Operators and Operator Precedence

*Adapted from `accenture-prep-final/accenture-prep-library/topics/T11-B7-bitwise-operators.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.6 questions and 1.1 marks** on this topic (about 1.5% of the 75 scored marks). It sits in **Pseudocode**: 5 questions, 10 marks, 10 minutes. **Tier 2**, 0.8 hours to reach reliable recall, confidence **Medium**.

**1 question on this topic are in the observed Infosys pool** (P03), from 1 source. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** its ROI alone would place it lower, but this section has its own cut-off and this topic is needed to reach 60% of the section's marks. Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| P03 | 2025-09-25 | Integer p = 1, q = 1. p = p ^ 1 & 1 + q ^ 1 & 1. Print p + q. |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



Five shapes, all observed:

1. **Trace a 10–12 line snippet where a bitwise op decides a branch.** The dominant shape. You are given three integers, a condition containing `&` or `^`, and asked to print a sum at the end. The arithmetic is trivial; the bitwise evaluation is the whole question.

**1. (a) 8.** `12 = 1100`, `10 = 1010`. AND keeps only bits set in both → `1000` = 8.
- *(b) 22* is `12 + 10` — the add-instead-of-AND trap.
- *(c) 2* is `12 - 10`.
- *(d) 14* is `12 | 10` (OR), a deliberate near-miss.

---

2. **Bitwise inside a 2D array expression.** `arr[1][0] = (4 + 1) & arr[1][1]` — combines B3 and B7. Four local items do this.

**2. (d) 5.** `6 = 110`, `3 = 011`. XOR sets a bit where they **differ** → `101` = 5.
- *(a) 9* is `6 + 3`.
- *(b) 2* is `6 & 3`.
- *(c) 7* is `6 | 3`.

---

3. **Precedence discrimination.** `(8 & r+q)` — you must know `+` binds tighter than `&`. Getting this backwards flips the branch and gives a plausible wrong answer that is always among the options.

**3. (c) 20.** Left shift by 2 multiplies by 2² = 4, so `5 × 4 = 20`. In binary `101` → `10100`.
- *(a) 7* is `5 + 2`, *(b) 10* is one shift only, *(d) 25* is `5²`.

---

4. **`&` versus `&&`.** A condition mixes bitwise AND with logical AND in the same expression, e.g. `if((7 && b) > (a && 7))`.

**4. (d) 13.** `5 = 0101`, `12 = 1100`. AND → `0100` = 4. XOR → `1001` = 9. `4 + 9 = 13`.
- *(a) 17* is `5 + 12` — worth noting that `(a & d) + (a ^ d)` always equals `a + b` when there are no carries, which is a useful sanity check.
- *(c) 4* and *(b) 9* are each only half the expression.

---

5. **XOR chains.** `(q^p^9)` evaluated left to right.

> **No pen and paper is allowed.** You must do `3 & 4 → 011 & 100 → 000 → 0` in your head, in under ten seconds. That is the actual skill being tested.

## 3. Concept notes

### 3.1 Binary basics

Place values (8-bit):

| Position | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

**Doubling trick** — memorise the sequence, it is every power of two in order:

```
1, 2, 4, 8, 16, 32, 64, 128
```

**Fast decimal → binary (0–255), method A: subtract largest fit**
Take 29. Largest place value ≤ 29 is 16 → remainder 13. Largest ≤ 13 is 8 → remainder 5. Largest ≤ 5 is 4 → remainder 1. Largest ≤ 1 is 1 → remainder 0. Record a 1 in the 16, 8, 4, 1 positions and 0 elsewhere: `00011101`. Check: 16 + 8 + 4 + 1 = 29.

Take 57. 32 → 25, 16 → 9, 8 → 1, 1 → 0. Bits at 32, 16, 8, 1: `00111001`. Check: 32 + 16 + 8 + 1 = 57.

**Method B: halve and record remainders, read bottom-up**
29 ÷ 2 = 14 r **1**; 14 ÷ 2 = 7 r **0**; 7 ÷ 2 = 3 r **1**; 3 ÷ 2 = 1 r **1**; 1 ÷ 2 = 0 r **1**. Read the remainders upward: `11101`.

**Lookup table, decimal 0–16**

| Dec | Bin | Dec | Bin |
|---|---|---|---|
| 0 | 0000 | 8 | 1000 |
| 1 | 0001 | 9 | 1001 |
| 2 | 0010 | 10 | 1010 |
| 3 | 0011 | 11 | 1011 |
| 4 | 0100 | 12 | 1100 |
| 5 | 0101 | 13 | 1101 |
| 6 | 0110 | 14 | 1110 |
| 7 | 0111 | 15 | 1111 |
| 16 | 10000 | | |

### 3.2 The six bitwise operators

```
&   bitwise AND
|   bitwise OR
^   bitwise XOR
~   bitwise NOT (complement)
<<  left shift
>>  right shift
```

**1-bit truth tables** (a and b are single bits):

| a | b | a AND b | a OR b | a XOR b |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

| a | NOT a |
|---|---|
| 0 | 1 |
| 1 | 0 |

`~x` flips every bit. For a signed integer, `~x = -(x + 1)`: `~0 = -1`, `~1 = -2`, `~5 = -6`, `~10 = -11`.

### 3.3 AND — worked binary columns

Line the bits up to the same width. Write 1 only where **both** rows have 1.

```
  3 = 0 1 1
  4 = 1 0 0
      -----
&     0 0 0   = 0
```

```
   8 = 1 0 0 0
  10 = 1 0 1 0
       -------
&      1 0 0 0  = 8
```

```
  10 = 1 0 1 0
   1 = 0 0 0 1
       -------
&      0 0 0 0   = 0
```

```
  29 = 1 1 1 0 1
   4 = 0 0 1 0 0
       ---------
&      0 0 1 0 0  = 4
```

```
  57 = 1 1 1 0 0 1
   4 = 0 0 0 1 0 0
       -----------
&      0 0 0 0 0 0  = 0
```

```
   5 = 1 0 1
   1 = 0 0 1
       -----
&      0 0 1   = 1
```

**Key intuition:** AND keeps only bits set in **both** operands. If the two operands share no set bit position, the answer is 0. That is why 3 AND 4 = 0, 10 AND 1 = 0, and 57 AND 4 = 0 — in each pair the set bits never overlap.

### 3.4 OR

Write 1 where **either** row has 1.

```
   5 = 1 0 1
   2 = 0 1 0
       -----
|      1 1 1   = 7
```

```
  10 = 1 0 1 0
   1 = 0 0 0 1
       -------
|      1 0 1 1   = 11
```

### 3.5 XOR

Write 1 where the bits **differ**, 0 where they are the same.

```
   3 = 0 1 1
   4 = 1 0 0
       -----
^      1 1 1   = 7
```

```
   7 = 0 1 1 1
   9 = 1 0 0 1
       -------
^      1 1 1 0  = 14
```

```
  23 = 1 0 1 1 1
   4 = 0 0 1 0 0
       ---------
^      1 0 0 1 1  = 19
```

```
   8 = 1 0 0 0
   4 = 0 1 0 0
       -------
^      1 1 0 0   = 12
```

**Properties**

| Property | Statement |
|---|---|
| Self-inverse | x XOR x = 0 |
| Identity | x XOR 0 = x |
| Own inverse | (x XOR y) XOR y = x |
| Commutative | x XOR y = y XOR x |
| Associative | (x XOR y) XOR z = x XOR (y XOR z) |
| Bit toggle | x XOR 1 flips the lowest bit |

### 3.6 Left and right shift

- `a << k` appends k zeros on the right → multiply by 2^k.
- `a >> k` drops the k rightmost bits → divide by 2^k and **truncate** (floor for non-negative values).

| Expression | Bit change | Decimal |
|---|---|---|
| 5 << 1 | 101 → 1010 | 10 |
| 5 << 2 | 101 → 10100 | 20 |
| 3 << 3 | 011 → 011000 | 24 |
| 20 >> 1 | 10100 → 1010 | 10 |
| 20 >> 2 | 10100 → 101 | 5 |
| 7 >> 1 | 111 → 11 | 3 (not 3.5) |
| 1 >> 1 | 1 → 0 | 0 |

Right shift truncates: `7 >> 1 = 3`, discarding the remainder.

### 3.7 Useful bit tricks

| Goal | Expression | Example |
|---|---|---|
| n is odd | n AND 1 = 1 | 7 AND 1 = 1 |
| n is even | n AND 1 = 0 | 8 AND 1 = 0 |
| n is a power of 2 (n > 0) | (n AND (n−1)) = 0 | 8 AND 7 = 0; 10 AND 9 = 8 (not a power of 2) |
| Multiply by 2 | n << 1 | 5 << 1 = 10 |
| Multiply by 2^k | n << k | 3 << 3 = 24 |
| Divide by 2 (floor) | n >> 1 | 7 >> 1 = 3 |
| Divide by 2^k (floor) | n >> k | 20 >> 2 = 5 |
| Swap a and b | a=a XOR b; b=a XOR b; a=a XOR b | 5,3 → 3,5 |
| Toggle bit k | n XOR (1 << k) | 5 XOR (1<<1) = 7 |
| Clear bit k | n AND NOT(1 << k) | 7 AND NOT 2 = 5 |
| Set bit k | n OR (1 << k) | 4 OR 2 = 6 |
| Test bit k | (n >> k) AND 1 | (5 >> 2) AND 1 = 1 |

Caveat on the power-of-two test: it must be `n > 0`. `0 AND (−1) = 0`, but 0 is not a power of two.

### 3.8 Bitwise AND (`&`) versus logical AND (`&&`)

This is the single most examined confusion.

| | `&` (bitwise AND) | `&&` (logical AND) |
|---|---|---|
| Works on | each bit position separately | the whole operand's truth value |
| Operand type | integers | truth values |
| Rule | 1 only where both bits are 1 | true only if both operands are true |
| Returns | an integer | a boolean |
| Evaluation | both sides always evaluated | short-circuits: right side skipped if left is false |
| 3 & 4 | 0 | — |
| 3 && 4 | — | true |

**Truthiness rule in these papers:** any non-zero integer is true, 0 is false.

So `3 && 4` = true && true = **true**, while `3 & 4` = 011 AND 100 = 000 = **0**. The integer 0 that comes out of `3 & 4` is itself falsy, which is exactly why candidates mix the two up.

Same split for OR: `|` is bitwise, `||` is logical. There is no `^^`; `^` is always bitwise XOR. `!` is logical NOT (`!5` = false, `!0` = true); `~` is bitwise NOT (`~5` = −6).

Precedence between them: `&` binds tighter than `&&`, so `a & b && c` means `(a & b) && c`.

### 3.9 Operator precedence

Highest to lowest, C/C++/Java-style (the convention used in these papers):

| Level | Operators | Associativity |
|---|---|---|
| 1 (highest) | ( ) | — |
| 2 | unary `!` `~` `+` `-` `++` `--` (prefix) | right to left |
| 3 | `*` `/` `%` | left to right |
| 4 | `+` `-` (binary) | left to right |
| 5 | `<<` `>>` | left to right |
| 6 | `<` `<=` `>` `>=` | left to right |
| 7 | `==` `!=` | left to right |
| 8 | `&` (bitwise AND) | left to right |
| 9 | `^` (bitwise XOR) | left to right |
| 10 | `\|` (bitwise OR) | left to right |
| 11 | `&&` (logical AND) | left to right |
| 12 | `\|\|` (logical OR) | left to right |
| 13 (lowest) | `=` `+=` `-=` `*=` `/=` `%=` | right to left |

**Rules to repeat until automatic:**

- Arithmetic `*` `/` `%` bind tighter than `+` `-`, which bind tighter than shifts.
- **Arithmetic `+` and `-` bind TIGHTER than bitwise `&` `^` `|`.**
- **Bitwise `&` `^` `|` bind TIGHTER than logical `&&` `||`.**
- **Bitwise `&` `^` `|` bind LOOSER than the relational and equality operators `<` `<=` `>` `>=` `==` `!=`.**
- Same precedence level → evaluate left to right (except unary and assignment, right to left).

**Worked examples**

`8 & 7 + 3`
`+` binds tighter than `&` → `7 + 3 = 10` → `8 & 10` = 1000 AND 1010 = 1000 = **8**.
It is NOT `(8 & 7) + 3 = 0 + 3 = 3`.

`1 << 2 + 3`
`+` binds tighter than `<<` → `2 + 3 = 5` → `1 << 5 = 1 × 2^5 = 32`.
It is NOT `(1 << 2) + 3 = 4 + 3 = 7`.

`3 ^ 4 ^ 9`
`^` is left-associative → `3 ^ 4 = 7`, then `7 ^ 9 = 14`. Result **14**. (XOR is also associative, so the grouping does not change the answer here.)

`x & 3 == 1` — the classic trap
`==` binds tighter than `&` → `3 == 1` gives 0 → `x & 0 = 0` for every x. If you meant "the low two bits of x equal 1", write `(x & 3) == 1`.

`5 | 2 * 3`
`*` first → `2 * 3 = 6` → `5 | 6` = 101 OR 110 = 111 = **7**.

`10 - 2 << 1`
`-` binds tighter than `<<` → `10 - 2 = 8` → `8 << 1 = 16`. Not `10 - (2 << 1) = 6`.

`3 + 4 == 7 && 2 < 5`
`+` → 7; `==` → true; `<` → true; `&&` → **true**.

In all of these, parentheses would override everything — `( )` sits at level 1.

### 3.10 Integer division and modulo

- `/` between two integers drops the fractional part; it does not round.
- `%` returns the remainder.

Non-negative operands:

| Expression | Result |
|---|---|
| 7 / 2 | 3 |
| 7 % 2 | 1 |
| 10 / 3 | 3 |
| 10 % 3 | 1 |
| 9 / 3 | 3 |
| 9 % 3 | 0 |
| 2 / 5 | 0 |
| 2 % 5 | 2 |

Negative operands, C/Java/C++ style:

| Expression | Result | Rule |
|---|---|---|
| −7 / 2 | −3 | division truncates toward zero |
| 7 / −2 | −3 | division truncates toward zero |
| −7 / −2 | 3 | division truncates toward zero |
| −7 % 2 | −1 | remainder takes the sign of the left operand |
| 7 % −2 | 1 | remainder takes the sign of the left operand |
| −7 % −2 | −1 | remainder takes the sign of the left operand |

Identity that always holds (b ≠ 0): `(a / b) * b + (a % b) = a`.
Check: (−7 / 2) × 2 + (−7 % 2) = (−3) × 2 + (−1) = −7.

Caution: Python-flavoured pseudocode floors instead of truncating and gives the remainder the sign of the divisor: `−7 // 2 = −4`, `−7 % 2 = 1`. If the paper supplies a sample question, match its convention. C-style is the norm in these exams.

### 3.11 Pre-increment versus post-increment

| Form | Name | Meaning |
|---|---|---|
| `++x` | pre-increment | increment x first, then use the new value |
| `x++` | post-increment | use the current value, then increment x |
| `--x` | pre-decrement | decrement x first, then use the new value |
| `x--` | post-decrement | use the current value, then decrement x |

Worked example:

```
a = 5
b = a++     // b gets 5, then a becomes 6
c = ++a     // a becomes 7, then c gets 7
```

Final: a = 7, b = 5, c = 7.

```
x = 10
y = x--     // y gets 10, then x becomes 9
z = --x     // x becomes 8, then z gets 8
```

Final: x = 8, y = 10, z = 8.

Notes:
- When the increment is a standalone statement (`x++;`), pre and post leave x with the same final value.
- Avoid `x++ + ++x` in one expression. In C/C++ it is undefined (two unsequenced writes to x). Java evaluates left to right: x = 5 gives 5 + 7 = 12.

## 4. Must-memorise block

**Truth tables**

| a | b | a AND b | a OR b | a XOR b |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

NOT: 0 → 1, 1 → 0. `~x = −(x + 1)`.

**Decimal → binary, 0–16**

| Dec | Bin | Dec | Bin |
|---|---|---|---|
| 0 | 0000 | 8 | 1000 |
| 1 | 0001 | 9 | 1001 |
| 2 | 0010 | 10 | 1010 |
| 3 | 0011 | 11 | 1011 |
| 4 | 0100 | 12 | 1100 |
| 5 | 0101 | 13 | 1101 |
| 6 | 0110 | 14 | 1110 |
| 7 | 0111 | 15 | 1111 |
| 16 | 10000 | | |

Place values: 1, 2, 4, 8, 16, 32, 64, 128.

**Precedence ladder, high → low**

```
1  ( )
2  unary  !  ~  +  -  ++  --
3  *  /  %
4  +  -
5  <<  >>
6  <  <=  >  >=
7  ==  !=
8  &        bitwise AND
9  ^        bitwise XOR
10 |        bitwise OR
11 &&
12 ||
13 =  +=  -=  *=  /=  %=
```

Arithmetic `+ -` bind TIGHTER than `& ^ |`. Bitwise `& ^ |` bind TIGHTER than `&& ||`. Bitwise `& ^ |` bind LOOSER than `< <= > >= == !=`. Same level → left to right.

**`&` versus `&&`**

| Input | `&` result | `&&` result |
|---|---|---|
| 3, 4 | 0 (integer) | true |
| 1, 0 | 0 | false |
| 0, 0 | 0 | false |
| 5, 2 | 0 | true |

Rule: `&` works bit by bit and returns an integer; `&&` works on truth values and returns true/false. Non-zero is true, 0 is false.

**Bit tricks**

| Goal | Expression |
|---|---|
| Odd | n AND 1 = 1 |
| Even | n AND 1 = 0 |
| Power of two (n > 0) | (n AND (n−1)) = 0 |
| × 2 | n << 1 |
| × 2^k | n << k |
| ÷ 2 (floor) | n >> 1 |
| ÷ 2^k (floor) | n >> k |
| Swap a, b | a=a XOR b; b=a XOR b; a=a XOR b |
| Toggle bit k | n XOR (1 << k) |
| Set bit k | n OR (1 << k) |
| Clear bit k | n AND NOT(1 << k) |
| Test bit k | (n >> k) AND 1 |

**Six verified AND results**

| Expression | Binary | Answer |
|---|---|---|
| 3 AND 4 | 011 AND 100 | 0 |
| 8 AND 10 | 1000 AND 1010 | 8 |
| 10 AND 1 | 1010 AND 0001 | 0 |
| 29 AND 4 | 11101 AND 00100 | 4 |
| 57 AND 4 | 111001 AND 000100 | 0 |
| 5 AND 1 | 101 AND 001 | 1 |

**Verified XOR results**

| Expression | Binary | Answer |
|---|---|---|
| 3 XOR 4 | 011 XOR 100 | 7 |
| 7 XOR 9 | 0111 XOR 1001 | 14 |
| 23 XOR 4 | 10111 XOR 00100 | 19 |
| 8 XOR 4 | 1000 XOR 0100 | 12 |

**Verified precedence results**

| Expression | Parses as | Answer |
|---|---|---|
| 8 & 7 + 3 | 8 & 10 | 8 |
| 1 << 2 + 3 | 1 << 5 | 32 |
| 3 ^ 4 ^ 9 | (3 ^ 4) ^ 9 | 14 |
| 5 \| 2 * 3 | 5 \| 6 | 7 |
| 10 - 2 << 1 | (10 - 2) << 1 | 16 |

**Verified shift results:** 5 << 1 = 10, 5 << 2 = 20, 3 << 3 = 24, 20 >> 1 = 10, 20 >> 2 = 5, 7 >> 1 = 3, 1 >> 1 = 0.

## 5. Worked examples

Every result below was verified by execution.

### Example 1 — The core move: AND with no shared bits

```
1. Integer p, q, r
2. Set p = 1, q = 8, r = 9
3. q = (11 + 9) & q
4. p = q + q
5. Print p + q + r
```

**Trace.**

| Line | Working | p | q | r |
|---|---|---|---|---|
| 2 | initial | 1 | 8 | 9 |
| 3 | `11+9 = 20`. **`+` before `&`.** `20 & 8` → `10100 & 01000` → `00000` | 1 | **0** | 9 |
| 4 | `0 + 0` | **0** | 0 | 9 |
| 5 | `0 + 0 + 9` | | | **9** |

**Answer: 9.**

The intuition to internalise: **20 is `10100` and 8 is `01000`. They share no set bit, so the AND is 0.** Once `q` collapses to 0, `p` follows and only `r` survives.

### Example 2 — Precedence decides the branch

```
1. Integer p, q, r
2. Set p = 4, q = 3, r = 7
3. if((q ^ p ^ 9) < (8 & r + q))
4.     r = (7 ^ 7) + q
5.     q = (q + r) + p
6. End if
7. r = q + p
8. Print p + q + r
```

**Left side:** `3 ^ 4` → `011 ^ 100` → `111` = 7. Then `7 ^ 9` → `0111 ^ 1001` → `1110` = **14**.

**Right side:** this is where the question is won or lost. `+` binds tighter than `&`, so it is `8 & (7+3)` = `8 & 10` → `1000 & 1010` → `1000` = **8**. (Reading it as `(8 & 7) + 3` gives `0 + 3` = 3 — a different number, and the wrong branch.)

`14 < 8` is **false**, so lines 4–5 never run.

| Line | p | q | r |
|---|---|---|---|
| 2 | 4 | 3 | 7 |
| 3 | condition false — skip body | | |
| 7 | `r = 3 + 4` | | **7** |
| 8 | `4 + 3 + 7` | | |

**Answer: 14.**

### Example 3 — The value must be re-read after reassignment

```
1. Integer p, q, r
2. Set p = 4, q = 8, r = 6
3. if((p + r) > (q - p))
4.     q = (q + 7) + q
5.     if((4 + q ^ p) < (7 + p + r))
6.         p = (q ^ p) ^ r
7.     Else
8.         r = 5 + q
9.     End if
10. End if
11. Print p + q + r
```

**Trace.**

| Line | Working | p | q | r |
|---|---|---|---|---|
| 2 | initial | 4 | 8 | 6 |
| 3 | `(4+6)=10 > (8-4)=4` → **true**, enter | 4 | 8 | 6 |
| 4 | `(8+7)+8 = 23` | 4 | **23** | 6 |
| 5 | **`q` is now 23, not 8.** `23 ^ 4` → `10111 ^ 00100` → `10011` = 19. Left = `4+19` = 23. Right = `7+4+6` = 17. `23 < 17` → **false** | | | |
| 8 | Else: `r = 5 + 23` | 4 | 23 | **28** |
| 11 | `4 + 23 + 28` | | | |

**Answer: 55.**

Using the original `q = 8` gives `8 ^ 4 = 12`, left `= 16`, `16 < 17` true, and you take the wrong branch. **Always re-read the current value at the line you are on.**

### Example 4 — `&` inside a loop, changing each pass

```
1. Integer a, b, c
2. Set a = 8, b = 5, c = 6
3. for(each c from 3 to 4)
4.     b = 9 + b
5.     b = (b + 7) + a
6.     b = (b & 4) + b
7. End for
8. Print a + b
```

`for c from 3 to 4` is **inclusive** — exactly 2 iterations.

| Pass | Line 4 | Line 5 | Line 6 working | b after |
|---|---|---|---|---|
| 1 | `9+5 = 14` | `(14+7)+8 = 29` | `29 & 4` → `11101 & 00100` → `00100` = 4; `4+29` | **33** |
| 2 | `9+33 = 42` | `(42+7)+8 = 57` | `57 & 4` → `111001 & 000100` → `000000` = 0; `0+57` | **57** |

`Print a + b` = `8 + 57`. **Answer: 65.**

Note `b & 4` gives **4** on the first pass and **0** on the second. Assuming it is constant is the trap.

### Example 5 — `&` versus `&&`

```
Integer a = 2, b = 1
Print (a & b)
Print (a && b)
```

- `a & b` = `10 & 01` = `00` = **0**
- `a && b` — both operands are non-zero, therefore both truthy — = **true**

Same operands, opposite answers. `&` works bit by bit and returns a number; `&&` asks "are both non-zero?" and returns a boolean.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid |
|---|---|---|
| **Reading `&` as `+`** | Under time pressure `3 & 4` looks like it should be 7 | `&` **never** produces a bit neither operand has. `3 & 4 = 0`, not 7 |
| **`8 & 7 + 3` evaluated left to right** | We read left to right, so we compute `8 & 7` first | **`+` and `-` bind tighter than `&`, `^`, `\|`.** Do the arithmetic, then the bitwise op |
| **Confusing `&` with `&&`** | One character apart, and both are called "and" | `&` = bitwise, returns an integer. `&&` = logical, returns true/false. Non-zero is truthy |
| **Using a variable's pre-update value** | The condition sits below the assignment and you remember the initial value | Re-state all three variables after every assignment line |
| **Assuming `x & k` is constant in a loop** | It looks like a fixed mask | `x` changes each pass, so the AND result changes. Recompute every iteration |
| **Forgetting XOR is self-inverse** | `3 ^ 5 ^ 3` looks like it needs three steps | `x ^ x = 0` and `x ^ 0 = x`, so `3 ^ 5 ^ 3 = 5`. XOR is commutative and associative |
| **Right shift on an odd number** | `7 >> 1` feels like it should be 3.5 | Integer shift truncates: `7 >> 1 = 3` |
| **Not converting to binary at all** | Trying to reason about `&` decimally | Convert both operands to binary **first, every time**. It takes 3 seconds and removes all guesswork |

## 7. Practice questions

Attempt all 12 before opening the key. Target: 40 seconds each.

1. **[Easy]** *(B7 — AND)* What is `12 & 10`?
   (a) 8 (b) 22 (c) 2 (d) 14

2. **[Easy]** *(B7 — XOR)* What is `6 ^ 3`?
   (a) 9 (b) 2 (c) 7 (d) 5

3. **[Easy]** *(B7 — shift)* What is `5 << 2`?
   (a) 7 (b) 10 (c) 20 (d) 25

4. **[Medium]** *(B7 — combined)* `Integer a = 5, b = 12`. What does `Print (a & b) + (a ^ b)` output?
   (a) 17 (b) 9 (c) 4 (d) 13

5. **[Medium]** *(B7 — precedence)* What does `Print 12 & 5 + 3` output?
   (a) 8 (b) 4 (c) 3 (d) 15

**5. (a) 8.** `+` binds tighter than `&`, so this is `12 & (5 + 3)` = `12 & 8` = `1100 & 1000` = `1000` = 8.
- *(c) 3* is the precedence trap: `(12 & 5) + 3` = `4 + 3` = 7 — and note even that is not 3, so anyone picking (c) has made two errors.
- *(b) 4* is `12 & 5` alone.
- *(d) 15* is `12 | 3`.

---

6. **[Medium]** *(B7 — bit trick)* `Integer x = 7`. What does `Print x & (x - 1)` output?
   (a) 7 (b) 6 (c) 1 (d) 0

**6. (b) 6.** `x = 7 = 0111`, `x - 1 = 6 = 0110`. AND → `0110` = 6.
- *(d) 0* is the trap: `n & (n-1) == 0` is the **power-of-two test**, and 7 is not a power of two, so it does not give 0. It gives 0 only for 1, 2, 4, 8, 16…

---

7. **[Medium]** *(B7 — XOR properties)* What is `3 ^ 5 ^ 3`?
   (a) 0 (b) 3 (c) 6 (d) 5

**7. (d) 5.** XOR is its own inverse: `3 ^ 3 = 0`, and XOR is commutative and associative, so `3 ^ 5 ^ 3 = 5 ^ (3 ^ 3) = 5 ^ 0 = 5`.
- *(a) 0* would be right for `3 ^ 3` alone.
- *(c) 6* is `3 ^ 5` with the third operand ignored.

---

8. **[Hard]** *(B7 + B2 — branch selection)* Trace and print.
   ```
   1. Integer a, b, c
   2. Set a = 6, b = 9, c = 4
   3. if((a & b) > (c - 2))
   4.     b = (a ^ c) + b
   5. Else
   6.     b = (a & c) + b
   7. End if
   8. Print a + b + c
   ```
   (a) 19 (b) 25 (c) 23 (d) 21

**8. (c) 23.**

| Line | Working | a | b | c |
|---|---|---|---|---|
| 2 | initial | 6 | 9 | 4 |
| 3 | `a & b` = `0110 & 1001` = `0000` = **0**. `c - 2` = 2. `0 > 2` → **false** | | | |
| 6 | Else branch: `a & c` = `0110 & 0100` = `0100` = **4**. `b = 4 + 9` | 6 | **13** | 4 |
| 8 | `6 + 13 + 4` | | | **23** |

- *(d) 21* comes from taking the **if** branch: `a ^ c` = `0010` = 2, `b = 2 + 9 = 11`, total 21. That is the answer if you wrongly evaluate `6 & 9` as non-zero.
- *(a) 19* is the untouched total `6 + 9 + 4`.
- *(b) 25* is arithmetic noise.

---

9. **[Hard]** *(B7 + B2 — dead branch)* Trace and print.
   ```
   1. Integer p, q, r
   2. Set p = 5, q = 3, r = 8
   3. if((p ^ q) < (r & 6))
   4.     q = (p & r) + q
   5.     r = q + p
   6. End if
   7. Print p + q + r
   ```
   (a) 13 (b) 16 (c) 21 (d) 11

**9. (b) 16.**

| Line | Working | p | q | r |
|---|---|---|---|---|
| 2 | initial | 5 | 3 | 8 |
| 3 | `p ^ q` = `101 ^ 011` = `110` = **6**. `r & 6` = `1000 & 0110` = `0000` = **0**. `6 < 0` → **false** | | | |
| 6 | body skipped entirely | 5 | 3 | 8 |
| 7 | `5 + 3 + 8` | | | **16** |

The whole body is dead code. Evaluating the guard first answers this in about fifteen seconds.
- *(a) 13* assumes line 4 ran: `p & r` = `0101 & 1000` = 0, so `q` would still be 3 — meaning even people who wrongly enter the branch should get 16 unless they also miscompute `p & r`.
- *(c) 21* and *(d) 11* are distractor arithmetic.

---

10. **[Medium]** *(B7 — `&` vs `&&`)* `Integer a = 2, b = 1`. Which statement is correct?
    (a) `a & b` is 0 and `a && b` is true (b) both are 0 (c) `a & b` is 1 and `a && b` is true (d) both are true

**10. (a) `a & b` is 0 and `a && b` is true.** `2 & 1` = `10 & 01` = `00` = 0. But both 2 and 1 are non-zero, so both are truthy and `a && b` is true.
- *(c)* gets the bitwise result wrong.
- *(b)* and *(d)* assume the two operators agree, which is exactly the misconception this tests.

---

11. **[Medium]** *(B7 — odd check)* Which expression is true exactly when integer `n` is odd?
    (a) `n & 2` (b) `n ^ 1` (c) `n >> 1` (d) `n & 1`

**11. (d) `n & 1`.** The least significant bit is 1 for every odd number and 0 for every even number, so `n & 1` isolates it.
- *(a) `n & 2`* tests the **second** bit — true for 2, 3, 6, 7… which is not oddness.
- *(b) `n ^ 1`* flips the last bit rather than testing it; it is non-zero for almost every n.
- *(c) `n >> 1`* is integer division by 2 and discards the very bit you need.

---

12. **[Hard]** *(B7 — mixed operators)* What does `Print (8 & 12) ^ (8 | 12)` output?
    (a) 4 (b) 8 (c) 12 (d) 0

---

**12. (a) 4.** `8 = 1000`, `12 = 1100`. AND → `1000` = 8. OR → `1100` = 12. Then `8 ^ 12` = `1000 ^ 1100` = `0100` = **4**.
- *(d) 0* would require the two results to be equal.
- *(c) 12* is the OR alone; *(b) 8* is the AND alone.

---
## 8. Resources

| Resource | Type | Link | Free/Paid | Time | Why this one |
|---|---|---|---|---|---|
| GfG — Bitwise operators | Article | https://www.geeksforgeeks.org/cpp/bitwise-operators-in-c-cpp/ | Free | 25 min | Truth tables and worked examples in exactly the notation the paper uses |
| CodeChef — Accenture interview questions | Practice set | https://www.codechef.com/practice/accenture-interview-questions | Free | 60 min | Company-tagged practice including bitwise output prediction |
| PrepInsta — Accenture pseudocode | Practice set | https://prepinsta.com/accenture/pseudo-code/general-pseudo-code/ | Free | 45 min | Large volume of output-prediction items in the observed style |
| `question-banks/QB-T11-B7-bitwise-operators.md` | Question bank | (this library) | Free | 40 min | 35 original questions mirroring the observed difficulty mix |

*All external links verified resolving 2026-09-16.*

## 9. Self-check

- [ ] I can convert any decimal 0–63 to binary in under 5 seconds
- [ ] I can state the AND, OR and XOR truth tables without hesitating
- [ ] I can compute `3 & 4`, `8 & 10`, `29 & 4` and `57 & 4` mentally and correctly
- [ ] I know that `+` binds tighter than `&`, and I apply it without being reminded
- [ ] I can explain the difference between `&` and `&&` with a concrete example where they disagree
- [ ] I know `x ^ x = 0`, `x ^ 0 = x`, and that XOR is commutative and associative
- [ ] I know `n & 1` tests oddness and `n & (n-1) == 0` tests powers of two
- [ ] Given a 10-line snippet, I evaluate the **guard** before tracing the body
- [ ] I scored 10/12 or better on the practice questions in under 8 minutes

## 10. Sources

**Teaching content (§3–§9)** is adapted from `accenture-prep-final/accenture-prep-library/topics/T11-B7-bitwise-operators.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions P03 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `P3`). Confidence **Medium**. Nothing in this file is a published Infosys syllabus.
