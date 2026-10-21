---
title: Number system: primes, divisibility, powers and roots
code: A10
section: Technical Ability
weightage_pct: 1.0% of marks
est_questions: 0.74
tier: 4
difficulty: Medium
est_study_hours: 0.8
confidence: Medium
last_updated: 2026-09-30
---

# A10 — Number system: primes, divisibility, powers and roots

## 1. Why this topic matters here

Expect about **0.7 questions and 0.7 marks** on this topic (about 1.0% of the 75 scored marks). It sits in **Technical Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 4**, 0.8 hours to reach reliable recall, confidence **Medium**.

**1 question on this topic are in the observed Infosys pool** (Q06), from 1 source. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.74 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

Tier 4, recognise-only. One observed item plus the syllabus lists: the “non-prime digits on a telephone keypad” item (Q06, cube root of the product), which tests the definition of prime/composite and a perfect-cube root. The 2025 deck and 2026 coach list divisibility, HCF, LCM, decimals and fractions `[REPORTED]`.

| Sub-pattern | How it appears | Observed |
|---|---|---|
| Product of a set of numbers, then a root | Non-prime keypad digits, cube root | Q06 |
| HCF and LCM | Two numbers, find HCF or LCM | syllabus list |
| Divisibility tests | Which number is divisible by 9, 11 … | syllabus list |
| Last digit and remainder of a power | `7^48`, remainder of `3^50` by 7 | syllabus list |
| Number of factors | 360 has how many factors | syllabus list |

## 3. Concept notes

- **Prime:** exactly two factors (2, 3, 5, 7, 11, …). **Composite:** more than two factors (4, 6, 8, 9, …). **0 and 1 are neither** composite nor prime; “non-prime” technically includes them, so read the question for the intended set.
- **HCF × LCM = product of the two numbers.**
- **Number of factors:** write n = p^a × q^b × … ; factors = (a+1)(b+1)…
- **Last digit of a power:** the cycle of the last digit repeats (2: 2,4,8,6; 3: 3,9,7,1; 7: 7,9,3,1; 4: 4,6; 9: 9,1; 0,1,5,6: fixed).
- **Divisibility:** 3 and 9 (digit sum), 4 (last two digits), 8 (last three), 11 (alternating digit sum), 6 (even and divisible by 3).

## 4. Must-memorise block

| Test | Rule |
|---|---|
| 2 / 5 / 10 | last digit |
| 3 / 9 | digit sum divisible by 3 / 9 |
| 4 / 8 | last 2 / 3 digits divisible by 4 / 8 |
| 11 | (sum of odd-place digits) − (sum of even-place digits) divisible by 11 |
| Primes below 50 | 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 |

## 5. Worked examples

**Example 1 (Q06).** Composite digits on a keypad: 4, 6, 8, 9. Product = 4 × 6 × 8 × 9 = 1728 = 12³. Cube root **12**.

**Example 2 — HCF/LCM.** HCF(36, 48) = 12; LCM = 36 × 48 / 12 = **144**.

**Example 3 — last digit.** 7^48: cycle 7, 9, 3, 1 (length 4); 48 mod 4 = 0 → last digit **1**.

**Example 4 — factors.** 360 = 2³ × 3² × 5 → (3+1)(2+1)(1+1) = **24**.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Counting 1 as prime | It has one factor | Primes start at 2 |
| “Non-prime” vs “composite” | 0 and 1 are non-prime | Choose the reading that gives an offered option |
| Using exponent instead of cycle | Last digit repeats | Take the exponent modulo the cycle length |
| HCF×LCM for three numbers | The identity is for two numbers | Use it only for pairs |

## 7. Practice questions

More questions: [`QB-A10-number-system.md`](../question-banks/QB-A10-number-system.md).

**1.** **[Number of factors]** How many positive factors does 24 have?
a) 8
b) 4
c) 3
d) 10

**2.** **[Remainder of a power]** What is the remainder when 12^7 is divided by 11?
a) 1
b) 2
c) 5
d) 6

**3.** **[Number of factors]** How many positive factors does 360 have?
a) 32
b) 26
c) 6
d) 24

**4.** **[HCF]** Find the HCF of 44 and 90.
a) 46
b) 1980
c) 2
d) 4

**5.** **[Remainder of a power]** What is the remainder when 13^10 is divided by 9?
a) 5
b) 0
c) 3
d) 4

**6.** **[Number of factors]** How many positive factors does 72 have?
a) 5
b) 12
c) 6
d) 14

**7.** **[Remainder of a power]** What is the remainder when 9^13 is divided by 11?
a) 4
b) 3
c) 9
d) 8

**8.** **[Last digit]** What is the last digit of 7^87?
a) 5
b) 7
c) 3
d) 9

### ANSWER KEY

1. **a** — 24 = 2^3 × 3. Number of factors = (3+1) × (1+1) = **8**.
2. **a** — Reduce the base first: 12 ≡ 1 (mod 11). Repeated multiplication mod 11 gives remainder **1**.
3. **d** — 360 = 2^3 × 3^2 × 5. Number of factors = (3+1) × (2+1) × (1+1) = **24**.
4. **c** — Euclid: HCF(44, 90) = **2**.
5. **d** — Reduce the base first: 13 ≡ 4 (mod 9). Repeated multiplication mod 9 gives remainder **4**.
6. **b** — 72 = 2^3 × 3^2. Number of factors = (3+1) × (2+1) = **12**.
7. **b** — Reduce the base first: 9 ≡ 9 (mod 11). Repeated multiplication mod 11 gives remainder **3**.
8. **c** — Only the last digit of the base matters: 7. Its powers end in the repeating cycle 7, 9, 3, 1 (length 4). 87 mod 4 = 3, so the last digit is **3**.

## 8. Resources

- **https://www.indiabix.com/aptitude/numbers/** — numbers practice.
- **https://www.indiabix.com/aptitude/problems-on-hcf-and-lcm/** — HCF and LCM practice.

## 9. Self-check

1. Is 1 prime? Is 0?
2. What is HCF × LCM for 12 and 18?
3. What is the cycle of last digits of powers of 3?
4. How many factors does 100 have?
5. What is the divisibility test for 11?

## 10. Sources

This file was written for this library. **Infosys evidence:** observed questions Q06 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A10`). Confidence **Medium**. Practice questions in §7 and the bank were generated and checked by execution (brute force, simulation or inverse); see `../research/04-qa-report.md`. Nothing here is a published Infosys syllabus.
