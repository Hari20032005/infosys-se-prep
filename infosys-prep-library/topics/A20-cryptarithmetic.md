---
title: Cryptarithmetic
code: A20
section: Reasoning Ability
weightage_pct: 1.0% of marks
est_questions: 0.74
tier: 4
difficulty: Medium
est_study_hours: 0.6
confidence: Medium
last_updated: 2026-09-30
---

# A20 — Cryptarithmetic

## 1. Why this topic matters here

Expect about **0.7 questions and 0.7 marks** on this topic (about 1.0% of the 75 scored marks). It sits in **Reasoning Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 4**, 0.6 hours to reach reliable recall, confidence **Medium**.

**1 question on this topic are in the observed Infosys pool** (O16), from 1 source. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.98 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

Tier 4, recognise-only. Cryptarithmetic (letters standing for digits) is listed by the 2025 deck (C1) and the 2026 coach under reasoning `[REPORTED]`. No observed item.

| Sub-pattern | How it appears |
|---|---|
| Addition | AB + BA = CDC |
| Multiplication by a single digit | JE × J = EAE |
| Subtraction | rarely |

## 3. Concept notes

1. **Different letters are different digits; the first letter of a number is not 0.**
2. Start with the **carry**: in a sum of two 2-digit numbers equal to a 3-digit number, the leading digit of the result is **1**.
3. Use the **units column** first, then carries leftwards.
4. Use the **options**: substitute and check.
5. A letter that repeats on both sides usually narrows quickly.

## 4. Must-memorise block

| Fact | Use |
|---|---|
| Two 2-digit numbers sum to at most 198 | The leading digit of a 3-digit result is 1 |
| A digit times itself ends in: 0,1,4,9,6,5 | Narrows units-digit squares |
| Nothing ×0 or ×1 | Usually excluded by “different letters” |

## 5. Worked examples

**Example 1.** `AB + BA = CDC`. Two 2-digit numbers: C = 1. Units: B + A ends in 1, so B + A = 11 (it cannot be 1). Tens: A + B + 1 (carry) = 12, so D = 2. Result 121. Any pair with A + B = 11 works (e.g. 29 + 92 = 121). **C = 1, D = 2.**

**Example 2.** `JE × J = EAE`. The units digit of E×J is E, and E is also the first letter of the result, so E ≠ 0; that leaves E = 5 with J odd. Try J = 7: 75 × 7 = 525 ✓ (A = 2). Try J = 9: 95 × 9 = 855 ✗. So **J = 7, E = 5, A = 2**.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Letting a leading letter be 0 | Not allowed | Check the first letters |
| Forgetting carries | Columns interact | Write carries above each column |
| Multiple solutions in Example 1 | The question asks only for C and D | Read what is asked |

## 7. Practice questions

More questions: [`QB-A20-cryptarithmetic.md`](../question-banks/QB-A20-cryptarithmetic.md).

**1.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  LL
+ FI
= LIL
```

What is the value of **F**?
a) 9
b) 7
c) 8
d) 6

**2.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  DL
× L
= EEK
```

What is the value of **L**?
a) 0
b) 1
c) 5
d) 4

**3.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  HF
+ HH
= FHC
```

What is the value of **C**?
a) 5
b) 0
c) 3
d) 4

**4.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  HA
+ DD
= DAD
```

What is the value of **D**?
a) 7
b) 1
c) 2
d) 4

**5.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  BC
+ KB
= CCK
```

What is the value of **K**?
a) 9
b) 5
c) 6
d) 8

**6.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  AL
× A
= DLL
```

What is the value of **A**?
a) 5
b) 8
c) 9
d) 4

**7.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  BB
+ JI
= BIB
```

What is the value of **J**?
a) 5
b) 4
c) 6
d) 9

**8.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  KK
+ KL
= FLK
```

What is the value of **F**?
a) 1
b) 0
c) 6
d) 3

### ANSWER KEY

1. **a** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is F = 9, I = 0, L = 1 (that is 11 + 90 = 101). So F = **9**. A search over all assignments finds exactly one.
2. **d** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is D = 8, E = 3, K = 6, L = 4 (that is 84 × 4 = 336). So L = **4**. A search over all assignments finds exactly one.
3. **b** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is C = 0, F = 1, H = 9 (that is 91 + 99 = 190). So C = **0**. A search over all assignments finds exactly one.
4. **b** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is A = 0, D = 1, H = 9 (that is 90 + 11 = 101). So D = **1**. A search over all assignments finds exactly one.
5. **c** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is B = 5, C = 1, K = 6 (that is 51 + 65 = 116). So K = **6**. A search over all assignments finds exactly one.
6. **c** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is A = 9, D = 8, L = 5 (that is 95 × 9 = 855). So A = **9**. A search over all assignments finds exactly one.
7. **d** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is B = 1, I = 0, J = 9 (that is 11 + 90 = 101). So J = **9**. A search over all assignments finds exactly one.
8. **a** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is F = 1, K = 5, L = 0 (that is 55 + 50 = 105). So F = **1**. A search over all assignments finds exactly one.

## 8. Resources

- **https://en.wikipedia.org/wiki/Verbal_arithmetic** — cryptarithms (verbal arithmetic) explained, with the classic SEND+MORE example.
- **https://www.indiabix.com/logical-reasoning/logical-problems/** — related logic puzzles.

## 9. Self-check

1. What is the leading digit of a 3-digit sum of two 2-digit numbers?
2. Which column do you start from?
3. Can a leading letter be 0?
4. How do options help?
5. What does “different letters are different digits” tell you?

## 10. Sources

This file was written for this library. **Infosys evidence:** observed questions O16 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A20`). Confidence **Medium**. Practice questions in §7 and the bank were generated and checked by execution (brute force, simulation or inverse); see `../research/04-qa-report.md`. Nothing here is a published Infosys syllabus.
