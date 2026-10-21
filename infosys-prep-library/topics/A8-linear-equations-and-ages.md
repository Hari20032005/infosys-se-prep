---
title: Linear equations: ages, heads-and-legs, two-variable systems
code: A8
section: Technical Ability
weightage_pct: 2.4% of marks
est_questions: 1.79
tier: 1
difficulty: Easy
est_study_hours: 0.7
confidence: High
last_updated: 2026-09-30
---

# A8 — Linear equations: ages, heads-and-legs, two-variable systems

## 1. Why this topic matters here

Expect about **1.8 questions and 1.8 marks** on this topic (about 2.4% of the 75 scored marks). It sits in **Technical Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 1**, 0.7 hours to reach reliable recall, confidence **High**.

**4 questions on this topic are in the observed Infosys pool** (Q01, Q02, Q05), from 2 sources. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 2.55 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

Three observed items are plain school algebra presented as word problems: ages, heads-and-legs, and two equations in two unknowns `[REPORTED]`. The family is cheap: each item is a 45–90 second question with an exact answer and no tricks beyond careful reading.

| Sub-pattern | How it appears | Observed |
|---|---|---|
| Ages, ratio after years pass | Ages 48 and 72; ratio of the first 3 years ago to the second 3 years from now | Q02 (three sightings) |
| Heads and legs | Cows and hens, 45 heads, 130 legs, find the cows | Q05 |
| Two equations, compare x and y | 2x + 3y = 7 and 5x + 8y = 2, which relation holds | Q01 |
| Consecutive numbers with a sum | Sum of four consecutive even numbers is 132 | R04 (data sufficiency form) |
| Cost of items from two purchases | authored from the pattern | — |

## 3. Concept notes

### 3.1 Translate, then solve

Name the unknowns; turn each sentence into an equation; solve by **elimination** (two equations) or by the **assume-all** shortcut (heads and legs).

### 3.2 Elimination

Multiply one or both equations so a variable has the same coefficient, then subtract.
2x + 3y = 7 and 5x + 8y = 2. Multiply the first by 5: 10x + 15y = 35. Multiply the second by 2: 10x + 16y = 4. Subtract: y = −31. Then 2x = 7 + 93 = 100, so x = 50.

### 3.3 Heads and legs: assume all one kind

Suppose every animal is a hen (2 legs): 45 × 2 = 90 legs. The real total is 130, so 40 legs are extra. Each cow adds 2 extra legs, so cows = 40 / 2 = **20**.

### 3.4 Ages

- "x years ago" subtracts from **every** person's age; "x years hence" adds.
- If ages are in a ratio a : b now, write them as ak and bk.
- Two ages differ by the same amount forever.

### 3.5 Consecutive numbers

For n consecutive numbers with sum S, the **average** is the middle value: S / n. For four consecutive even numbers summing to 132, the average is 33, so the numbers are 30, 32, 34, 36.

### 3.6 Cost problems

Two purchases give two equations. Solve for the price of each item, then compute the third basket. Often you can skip solving: combine the equations to get exactly the basket asked for.

## 4. Must-memorise block

| Item | Rule |
|---|---|
| Heads and legs | extra legs ÷ (legs difference) = number of the higher-leg animal |
| Elimination | make coefficients equal, subtract |
| n consecutive numbers | average = middle term = sum ÷ n |
| Age ratio | use ak : bk; ages differ by a constant |
| Sum of first n natural numbers | n(n+1)/2 |

## 5. Worked examples

**Example 1 — ages (observed Q02).** Ages 48 and 72. Three years ago: 45. Three years hence: 75. 45 : 75 = **3 : 5**.

**Example 2 — heads and legs (Q05).** 45 heads, 130 legs, cows (4 legs) and hens (2 legs). All hens → 90 legs. Extra 40 legs ÷ 2 per cow = **20 cows** (and 25 hens: 80 + 50 = 130 ✓).

**Example 3 — two equations (Q01).** x = 50 and y = −31 (section 3.2). So **x > y**.

**Example 4 — a cost problem.** 3 pens and 2 pencils cost ₹34; 2 pens and 3 pencils cost ₹31. Add: 5 pens + 5 pencils = ₹65, so 1 pen + 1 pencil = ₹13. Subtract: 1 pen − 1 pencil = ₹3. So a pen is ₹8 and a pencil ₹5. Check: 24 + 10 = 34 ✓; 16 + 15 = 31 ✓.

**Example 5 — consecutive even numbers.** Sum 132, four numbers: average 33, so 30, 32, 34, 36. Smallest **30**.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Subtracting years from one person only | "3 years ago" applies to everyone | Change every age in the sentence |
| Using legs when the question gives wheels | Bikes have 2 wheels, cars 4 | Read the object carefully |
| Dividing the extra legs by the wrong number | The divisor is the **difference** in legs per animal | Write "4 − 2 = 2 extra per cow" |
| Sign mistakes in elimination | Subtracting a negative | Write each step on its own line |
| Reporting x when y is asked | Two unknowns | Re-read the last sentence |
| Forgetting "even" steps by 2 | Consecutive evens differ by 2 | Write the numbers out |

## 7. Practice questions

More questions: [`QB-A8-linear-equations-and-ages.md`](../question-banks/QB-A8-linear-equations-and-ages.md).

**1.** **[Cost of items]** 6 pens and 1 pencils cost ₹77. 3 pens and 6 pencils cost ₹66. What is the cost of 1 pen and 3 pencils?
a) 143
b) 27
c) 22
d) 39

**2.** **[Ages]** The present ages of Gautam and Goru are 24 and 40 years. Find the ratio of Gautam's age 3 years ago to Goru's age 5 years from now.
a) 21:37
b) 3:5
c) 7:15
d) 29:37

**3.** **[Consecutive numbers]** The sum of 3 consecutive even numbers is 114. What is the largest of them?
a) 38
b) 37
c) 40
d) 46

**4.** **[Heads and legs]** A yard has some tables and some stools. There are 28 items in all and 89 legs in total (tables have 4 legs each, stools have 3 each). How many stools are there?
a) 5
b) 12
c) 2
d) 23

**5.** **[Heads and legs]** A yard has some tables and some stools. There are 27 items in all and 102 legs in total (tables have 4 legs each, stools have 3 each). How many tables are there?
a) 14
b) 23
c) 6
d) 21

**6.** **[Heads and legs]** A yard has some cars and some bikes. There are 33 items in all and 122 wheels in total (cars have 4 wheels each, bikes have 2 each). How many cars are there?
a) 28
b) 5
c) 20
d) 30

**7.** **[Ages]** The present ages of Gautam and Goru are 40 and 64 years. Find the ratio of Gautam's age 3 years ago to Goru's age 2 years from now.
a) 37:66
b) 42:61
c) 43:66
d) 37:61

**8.** **[Two equations]** 4x + 5y = 76 and 1x + 7y = -50. Which relation holds between x and y?
a) cannot be determined
b) x > y
c) x < y
d) x = y

**9.** **[Consecutive numbers]** The sum of 5 consecutive numbers is 35. What is the smallest of them?
a) 8
b) 7
c) 5
d) 6

**10.** **[Ages]** The present ages of Gautam and Goru are 24 and 40 years. Find the ratio of Gautam's age 3 years ago to Goru's age 4 years from now.
a) 21:44
b) 28:37
c) 27:44
d) 21:37

**11.** **[Heads and legs]** A yard has some cars and some bikes. There are 34 items in all and 84 wheels in total (cars have 4 wheels each, bikes have 2 each). How many bikes are there?
a) 8
b) 14
c) 22
d) 26

**12.** **[Two equations]** 3x + 1y = 110 and 5x + 6y = 218. Which relation holds between x and y?
a) x = y
b) x > y
c) x < y
d) cannot be determined

### ANSWER KEY

1. **b** — Solve the pair: a pen costs ₹12, a pencil ₹5. Then 1×12 + 3×5 = **₹27**.
2. **c** — 24 − 3 = 21; 40 + 5 = 45. Ratio 21 : 45 = **7:15**.
3. **c** — The middle/average term is 114/3 = 38. The numbers are 36, 38, 40, so the largest is **40**.
4. **d** — Suppose all 28 are tables: 28 × 4 = 112. The excess 23 comes from stools, each over-counted by 1. So stools = 23/1 = **23**.
5. **d** — Suppose all 27 are stools: 27 × 3 = 81. The extra 21 comes from tables, each adding 1. So tables = 21/1 = **21**.
6. **a** — Suppose all 33 are bikes: 33 × 2 = 66. The extra 56 comes from cars, each adding 2. So cars = 56/2 = **28**.
7. **a** — 40 − 3 = 37; 64 + 2 = 66. Ratio 37 : 66 = **37:66**.
8. **b** — Eliminate one variable (multiply and subtract): x = 34, y = -12. So **x > y**.
9. **c** — The middle/average term is 35/5 = 7. The numbers are 5, 6, 7, 8, 9, so the smallest is **5**.
10. **a** — 24 − 3 = 21; 40 + 4 = 44. Ratio 21 : 44 = **21:44**.
11. **d** — Suppose all 34 are cars: 34 × 4 = 136. The excess 52 comes from bikes, each over-counted by 2. So bikes = 52/2 = **26**.
12. **b** — Eliminate one variable (multiply and subtract): x = 34, y = 8. So **x > y**.

## 8. Resources

- **https://www.indiabix.com/aptitude/problems-on-ages/** — ages practice with solutions.
- **https://www.indiabix.com/aptitude/problems-on-numbers/** — number and equation word problems.
- **https://www.geeksforgeeks.org/system-linear-equations/** — elimination and substitution, worked.

## 9. Self-check

1. Can you solve 2x + 3y = 7, 5x + 8y = 2 in under 90 seconds?
2. Can you solve a heads-and-legs problem without setting up two equations?
3. If ages are 48 and 72, can you write the ratio of the first 5 years ago to the second 4 years hence?
4. Can you find the four consecutive even numbers summing to 132?
5. Given two shopping baskets, can you get the third basket's price without finding each price?

## 10. Sources

This file was written for this library. **Infosys evidence:** observed questions Q01, Q02, Q05 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A8`). Confidence **High**. Practice questions in §7 and the bank were generated and checked by execution (brute force, simulation or inverse); see `../research/04-qa-report.md`. Nothing here is a published Infosys syllabus.
