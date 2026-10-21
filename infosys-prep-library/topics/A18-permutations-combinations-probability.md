---
title: Permutations, combinations and probability
code: A18
section: Technical Ability
weightage_pct: 1.1% of marks
est_questions: 0.82
tier: 4
difficulty: Medium
est_study_hours: 1.2
confidence: Medium
last_updated: 2026-09-30
---

# A18 — Permutations, combinations and probability

## 1. Why this topic matters here

Expect about **0.8 questions and 0.8 marks** on this topic (about 1.1% of the 75 scored marks). It sits in **Technical Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 4**, 1.2 hours to reach reliable recall, confidence **Medium**.

**2 questions on this topic are in the observed Infosys pool** (O17, O18), from 1 source. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.55 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

Tier 4, recognise-only. Permutations, combinations and probability are listed by the 2025 deck and the 2026 coach for Technical Ability `[REPORTED]`; one data-sufficiency probability item (discarded, X03) shows the flavour. Forms:

| Sub-pattern | How it appears |
|---|---|
| Arrangements of letters | How many ways can the letters of LEVEL be arranged |
| Selections | A committee of 3 from 8 |
| Probability from a bag | Two balls drawn together, both the same colour |
| Dice, cards and coins | Two dice sum to 7; a king or a heart; exactly 2 heads in 4 tosses |

## 3. Concept notes

- **Factorial:** n! = n × (n−1) × … × 1.
- **Arrangements (order matters):** P(n, r) = n! / (n−r)!.
- **Selections (order does not matter):** C(n, r) = n! / (r!(n−r)!).
- **Letters with repeats:** n! divided by the factorial of each repeat count.
- **Probability** = favourable / total. **Complement:** P(not A) = 1 − P(A). **Or** (exclusive): add. **And** (independent): multiply.
- **Two dice:** 36 outcomes; sum 7 has 6.

## 4. Must-memorise block

| Item | Value |
|---|---|
| C(n, 2) | n(n−1)/2 |
| C(n, r) = C(n, n−r) | symmetry |
| Dice sums | 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1 |
| Cards | 52 = 4 suits × 13; 4 kings; 12 faces |

## 5. Worked examples

**Example 1.** Arrangements of LEVEL: 5 letters, L twice, E twice → 5! / (2! × 2!) = 120/4 = **30**.

**Example 2.** Committee of 3 from 8: C(8,3) = **56**.

**Example 3.** Bag with 3 red, 5 blue, 6 green; two balls drawn together, both the same colour: C(3,2) + C(5,2) + C(6,2) = 3 + 10 + 15 = 28; total C(14,2) = 91; probability 28/91 = **4/13**.

**Example 4.** King or heart: 4 + 13 − 1 = 16 cards → 16/52 = **4/13**.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Using P when order does not matter | Confusing selection with arrangement | Ask “does swapping people change the outcome?” |
| Forgetting repeats | LEVEL is not 5! | Divide by each repeat's factorial |
| Adding instead of multiplying | “And” means multiply | Write the structure first |
| Double counting | King of hearts counted twice | Subtract the overlap |

## 7. Practice questions

More questions: [`QB-A18-permutations-combinations-probability.md`](../question-banks/QB-A18-permutations-combinations-probability.md).

**1.** **[Arrangements]** In how many distinct ways can the letters of the word BANANA be arranged?
a) 30
b) 120
c) 720
d) 60

**2.** **[Coin tosses]** A fair coin is tossed 5 times. What is the probability of getting exactly 4 heads?
a) 5/16
b) 5/32
c) 4/5
d) 1/32

**3.** **[Coin tosses]** A fair coin is tossed 3 times. What is the probability of getting exactly 1 head?
a) 1/8
b) 1/3
c) 3/4
d) 3/8

**4.** **[Arrangements]** In how many distinct ways can the letters of the word APPLE be arranged?
a) 60
b) 120
c) 66
d) 30

**5.** **[Complement]** A bag has 3 red, 6 blue and 4 green balls. One ball is drawn at random. What is the probability that it is **not** green?
a) 3/13
b) 3/4
c) 9/13
d) 4/13

**6.** **[Complement]** A bag has 2 red, 6 blue and 3 green balls. One ball is drawn at random. What is the probability that it is **not** green?
a) 8/11
b) 2/11
c) 4/5
d) 3/11

**7.** **[Two draws]** A bag has 7 red, 4 blue and 2 green balls. Two balls are drawn together at random. What is the probability that both are the same colour?
a) 28/169
b) 56/169
c) 14/39
d) 29/78

**8.** **[Onto placements]** 4 different chocolates are placed in 3 different boxes, each box able to hold all 4. In how many ways can this be done if no box is left empty?
a) 15
b) 36
c) 18
d) 81

### ANSWER KEY

1. **d** — 6! = 720, divided by the factorials of the repeats (A ×3, N ×2): 720 ÷ 12 = **60**.
2. **b** — C(5,4) = 5 favourable sequences out of 2^5 = 32: **5/32**.
3. **d** — C(3,1) = 3 favourable sequences out of 2^3 = 8: **3/8**.
4. **a** — 5! = 120, divided by the factorials of the repeats (P ×2): 120 ÷ 2 = **60**.
5. **c** — 1 − 4/13 = 9/13 = **9/13**.
6. **a** — 1 − 3/11 = 8/11 = **8/11**.
7. **c** — Same colour: C(7,2) + C(4,2) + C(2,2) = 28. All pairs: C(13,2) = 78. Probability = **14/39**.
8. **b** — Inclusion–exclusion: +C(3,0)·(3)^4 −C(3,1)·(2)^4 +C(3,2)·(1)^4 = **36**. Listing all 81 placements and keeping those that use every box also gives 36.

## 8. Resources

- **https://www.indiabix.com/aptitude/permutation-and-combination/** — practice.
- **https://www.indiabix.com/aptitude/probability/** — practice.

## 9. Self-check

1. When do you use C and when P?
2. How many arrangements of the letters of BOOK?
3. What is P(not A)?
4. How many outcomes do two dice have, and how many sum to 7?
5. What is C(10, 2)?

## 10. Sources

This file was written for this library. **Infosys evidence:** observed questions O17, O18 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A18`). Confidence **Medium**. Practice questions in §7 and the bank were generated and checked by execution (brute force, simulation or inverse); see `../research/04-qa-report.md`. Nothing here is a published Infosys syllabus.
