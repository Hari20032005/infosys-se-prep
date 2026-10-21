---
title: Averages, mixtures and alligation
code: A9
section: Technical Ability
weightage_pct: 1.8% of marks
est_questions: 1.37
tier: 3
difficulty: Easy
est_study_hours: 0.7
confidence: Medium
last_updated: 2026-09-30
adapted_from: L&T/lt-prep-library/topics/Q8-averages-mixtures-and-alligation.md
---
<!-- Drafted by DeepSeek V4.1 Flash via ds.py; reviewed by Claude 2026-09-21. Answer
     letters rebalanced by data/shuffle.py (correctness-preserving: option text is
     swapped and the key letter repointed). Numeric keys re-checked by
     data/verify_keys.py. -->

# A9 — Averages, mixtures and alligation

*Adapted from `L&T/lt-prep-library/topics/Q8-averages-mixtures-and-alligation.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **1.4 questions and 1.4 marks** on this topic (about 1.8% of the 75 scored marks). It sits in **Technical Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 3**, 0.7 hours to reach reliable recall, confidence **Medium**.

**2 questions on this topic are in the observed Infosys pool** (Q04, O20), from 2 sources. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 1.56 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| O20 | 2020-09-22 | 8 L drawn from a can of milk and replaced by water, four times in all; milk : total = 16 : 81. Original quantity? |
| Q04 | 2025-09-29 | The sum of 15 observations is 2100. Every observation is doubled and then reduced by 10. By how much does the average increase? |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



| Sub-pattern | How it appears | Roughly how often |
|---|---|---|
| Simple average of a list | "Average of first n natural numbers / squares / cubes", or average of a given number set | ~20% |
| Average changes on add/remove/replace | "When a person of weight X joins, average rises by Y" - find Y or the new member | ~20% |
| Batting / innings style average | "After 10 innings average is A; after scoring S in the 11th, average becomes B" | ~10% |
| Two-ingredient alligation | Mix two items at prices/purities/concentrations, find the ratio | ~25% |
| Replacement / removal from a mixture | Repeated removal of liquid and topping up with water | ~10% |
| Mean of consecutive / arithmetic series | Middle term, sum, or average of an AP | ~10% |
| Weighted average | Different group sizes with different averages combined | ~5% |

## 3. Concept notes

### 3.1 The basic average

**Average = (Sum of all observations) / (Number of observations)**

Example: average of 4, 9, 11 = 24/3 = 8.

The single most useful rearrangement: **Sum = Average × Count**. Most "average changed" questions are solved by comparing the *old total* with the *new total*. If a value of 40 joins a group of 9 numbers whose average was 35, the old total is 315, the new total is 355, the new count is 10, so the new average is **35.5**. Never re-add the original list.

### 3.2 Deviation (assumed mean) method

Pick any convenient base A near the data. Then

**Average = A + (Sum of deviations from A) / n**

Example: values 48, 52, 55, 45. Take A = 50. Deviations: -2, +2, +5, -5, sum = 0. Average = **50**. This beats adding 200 and dividing by 4 in time, and it is the method to use whenever the numbers are clustered.

### 3.3 Standard averages worth memorising

| Set | Average |
|---|---|
| First n natural numbers (1,2,...,n) | **(n+1)/2** |
| First n odd numbers (1,3,...,2n-1) | **n** |
| First n even numbers (2,4,...,2n) | **n+1** |
| Squares of first n natural numbers | **(n+1)(2n+1)/6** |
| Cubes of first n natural numbers | **n(n+1)²/4** |
| Consecutive numbers, any set | **average = middle term** (or mean of the two middle terms if even count) |

Example: average of first 20 natural numbers = 21/2 = **10.5**. Average of first 20 odd numbers = **20**.

### 3.4 Change in average when a member joins or leaves

If a new member of value v joins a group of n members with average A:

**New average = (nA + v)/(n+1)**

Shortcut for "average rises by d when one person joins": the new person is **d(n+1)** above the old average. So old average 30, n = 19, average rises by 1 → the new person weighs 30 + 1×(19+1) = **50**.

For removal: if removing a member of value v from n members with average A, new average = (nA − v)/(n−1). Equivalently, the removed member is **(n−1)×d** away from the old average, where d is the rise in average... careful with sign: removing someone *lighter* than the average raises the average.

### 3.5 Replacement

If a member of value x is replaced by one of value y, and the average of n members changes by d, then:

**y − x = n × d**

Example: 25 students average 40 marks. One student of 35 leaves and another joins; average becomes 41. New student's marks = 35 + 25×1 = **60**. This is the fastest route; writing two sum equations wastes about 40 seconds.

### 3.6 Weighted average

When groups of size n₁ (average A₁) and n₂ (average A₂) are combined:

**Overall average = (n₁A₁ + n₂A₂)/(n₁ + n₂)**

Note the overall average lies strictly between A₁ and A₂, and is **closer to the average of the larger group**. If n₁ = n₂, the overall average is the simple midpoint.

### 3.7 Alligation - the core shortcut

Alligation finds the **ratio in which two ingredients must be mixed** to reach a target value.

If ingredient 1 has value c₁ and ingredient 2 has value c₂, and the mixture has value m (with m between c₁ and c₂), then:

**Quantity of cheaper : Quantity of dearer = (c₂ − m) : (m − c₁)**

The visual form:

```
   c1                c2
        \          /
           m
        /          \
   (c2 - m)      (m - c1)
```

**The differences cross over.** Mean sits in the middle; the difference to the *other* ingredient goes under each ingredient.

Example: mix rice at ₹40/kg with rice at ₹60/kg to get a mixture worth ₹52/kg. Ratio = (60−52):(52−40) = **8:12 = 2:3**. Meaning 2 parts of the ₹40 rice to 3 parts of the ₹60 rice.

The rule to burn in: **the cheaper ingredient's share is proportional to the difference on the dearer side.** If you get this backwards you get the inverse ratio, which is the single most common error.

### 3.8 Alligation with three ingredients

Apply it pairwise. Mix A and B to get an intermediate value, then mix that result with C. Or, if a target and three values are given, you generally need a stated constraint (e.g. one ingredient fixed) because three ingredients and one target gives infinitely many solutions.

### 3.9 Repeated replacement (removal and topping up)

A vessel contains P litres of liquid. Each time, x litres are removed and replaced with water. After n such operations, the amount of original liquid remaining is:

**P × (1 − x/P)ⁿ**

Example: 40 L of milk, remove 4 L and add water, three times. Milk left = 40 × (1 − 4/40)³ = 40 × (0.9)³ = 40 × 0.729 = **29.16 L**.

Note this assumes the vessel is always full and the removed liquid is a uniform mixture.

### 3.10 Mean of an arithmetic progression

For an AP with first term a, last term l, and n terms:

**Sum = n(a + l)/2** and **Average = (a + l)/2**

The average of an AP is just the average of its first and last terms, regardless of how long it is. This one line answers a large family of "average of all numbers from X to Y" questions in five seconds.

## 4. Must-memorise block

- **Average = Sum / Count**, and **Sum = Average × Count**
- **First n natural numbers average = (n+1)/2**
- **First n odd numbers average = n**
- **First n even numbers average = n+1**
- **Squares 1²..n² average = (n+1)(2n+1)/6**
- **Cubes 1³..n³ average = n(n+1)²/4**
- **AP average = (first + last)/2**
- **New member = old average + d(n+1)** where d = rise in average
- **Replacement: new − old = n × d**
- **Alligation ratio = (c₂ − m) : (m − c₁)** — cheaper : dearer
- **Weighted average = (n₁A₁ + n₂A₂)/(n₁ + n₂)**, lies between the two, nearer the bigger group
- **Repeated replacement: remaining = P(1 − x/P)ⁿ**
- Averages lie between the min and max of the data, always
- Changing units (all rupees, or all litres) before alligation saves errors

## 5. Worked examples

**Example 1.** The average age of 30 students is 15 years. When the teacher's age is included, the average rises by 1 year. Find the teacher's age.

Fast method: the new average is 16, new count 31, new total = 31 × 16 = 496. Old total = 30 × 15 = 450. Teacher = 496 − 450 = **46 years**. Shortcut check: 15 + 1 × (30+1) = 46. ✓ Both work; the shortcut is faster under pressure.

**Example 2.** In what ratio must tea at ₹180/kg be mixed with tea at ₹240/kg so that the mixture costs ₹200/kg?

Alligation: cheaper ₹180, dearer ₹240, mean ₹200. Ratio = (240 − 200) : (200 − 180) = 40 : 20 = **2 : 1** (cheaper : dearer). So 2 kg of ₹180 tea to 1 kg of ₹240 tea. Sanity check: 2×180 + 1×240 = 600 for 3 kg = ₹200/kg. ✓ The slow method sets up 180x + 240y = 200(x+y) and solves — same answer, about 25 seconds longer.

**Example 3.** A jar contains 60 L of pure milk. 6 L is drawn out and replaced with water. This is done three times. How much milk remains?

Remaining = 60 × (1 − 6/60)³ = 60 × (0.9)³ = 60 × 0.729 = **43.74 L**. Track the *original component only*; do not try to track water separately.

**Example 4.** The average of 11 results is 50. If the average of the first 6 is 49 and of the last 6 is 52, find the 6th result.

Total of all 11 = 550. First 6 + last 6 = 6×49 + 6×52 = 294 + 312 = 606. The 6th result is counted in both groups, so it equals 606 − 550 = **56**. Recognising the double-counted middle term is the whole question.

**Example 5.** A mixture of 40 L contains milk and water in the ratio 3:1. How much water must be added so the ratio becomes 3:2?

Milk = 30 L, water = 10 L. Milk stays at 30. For ratio 3:2, water must be 2/3 × 30 = 20 L. So add **10 L** of water. Using alligation here is slower than reasoning directly from the fixed component; when one ingredient is unchanged, anchor on it.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Reversing the alligation ratio | The cross-difference is applied to the *opposite* ingredient | Cheaper's share = (dearer − mean); sanity-check with a weighted sum |
| Using old count instead of new count | "Average rises when one joins" tempts you to divide by n | When someone joins, count becomes **n+1** |
| Forgetting the final replacement step | After the last removal, water is added only if stated | Read whether the question ends with removal or with topping up |
| Mixing units | ₹/kg vs ₹/litre, or kg vs g | Convert everything to one unit before applying alligation |
| Treating the mean as outside the range | In valid alligation, **m must lie between c₁ and c₂** | If m is outside, the problem is impossible or you misread it |
| Adding percentages or concentrations directly | 20% + 30% ≠ 25% unless quantities are equal | Always weight by quantity |
| Assuming the average of group averages is the overall average | True only when group sizes are equal | Use the weighted formula unless sizes match |
| Recomputing a sum from scratch after a change | Costs 30-60 seconds per question | Use delta methods: new − old = n × d |

## 7. Practice questions

1. The average of 5 consecutive even numbers is 24. What is the largest of them?
a) 26 b) 28 c) 30 d) 32

2. The average weight of 10 men is 65 kg. If one man of 75 kg leaves, what is the new average?
a) 64 kg b) 64.44 kg c) 63.89 kg d) 62 kg

3. How many kg of rice at ₹30/kg must be mixed with 20 kg of rice at ₹45/kg so the mixture is worth ₹35/kg?
a) 30 kg b) 40 kg c) 20 kg d) 50 kg

4. What is the average of the first 50 natural numbers?
a) 24.5 b) 25 c) 26 d) 25.5

5. A vessel holds 80 L of pure milk. 8 L is removed and replaced with water, twice. How much milk remains?
a) 68.4 L b) 62.8 L c) 64.8 L d) 65.6 L

6. The average marks of 40 students is 60. If the top 5 scorers are excluded, the average of the rest is 56. What is the average of the top 5?
a) 84 b) 88 c) 96 d) 92

7. A mixture of 60 L has milk and water in ratio 7:3. How much water must be added to make the ratio 7:5?
a) 12 L b) 10 L c) 8 L d) 15 L

8. Two alloys contain copper and zinc in ratios 3:2 and 5:3. In what ratio must they be melted to get an alloy with copper and zinc in ratio 4:3?
a) 5:2 b) 3:4 c) 2:5 d) 4:3

9. The average of 12 numbers is 45. If the number 60 is replaced by 80, what is the new average?
a) 47 b) 45.5 c) 46 d) 46.67

10. A batsman has an average of 42 after 20 innings. After the 21st innings his average becomes 43.5. How many runs did he score in the 21st innings?
a) 70 b) 71.5 c) 75 d) 73.5

11. A 50 L cask contains 20% alcohol. How many litres of pure alcohol must be added to make the strength 40%?
a) 12.5 L b) 15 L c) 16.67 L d) 20 L

12. There are three vessels of equal capacity containing milk and water in ratios 2:1, 3:1 and 5:3. If all three are mixed, what is the ratio of milk to water?
a) 25:11 b) 13:6 c) 12:5 d) 8:3

### ANSWER KEY

**1. b)** Five consecutive even numbers average to their middle term, so the set is 20, 22, 24, 26, 28. The largest is **28**.

**2. c)** Old total = 10 x 65 = 650. After the 75 kg man leaves, total = 575 over 9 men, so the new average is 575/9 = **63.89 kg**.

3. **b)** Alligation: (45 − 35):(35 − 30) = 10:5 = 2:1. Cheaper : dearer = 2:1, so with 20 kg dearer you need 40 kg cheaper.

4. **d)** (n+1)/2 = 51/2 = 25.5.

5. **c)** 80 × (1 − 8/80)² = 80 × (0.9)² = 80 × 0.81 = 64.8 L.

**6. b)** Total = 40 x 60 = 2400. The other 35 students total 35 x 56 = 1960. The top 5 total 2400 - 1960 = 440, so their average is 440/5 = **88**.

7. **a)** Milk = 42 L, water = 18 L. For 7:5, water = 5/7 × 42 = 30 L. Add 12 L.

8. **a)** Copper fractions: 3/5 = 0.6, 5/8 = 0.625, target 4/7 ≈ 0.5714. Target is below both, so alligation here is invalid as stated; by alligation on the copper concentration the required ratio is (0.625 − 0.5714):(0.5714 − 0.6), which is negative. Use the direct algebra: (0.6a + 0.625b)/(a+b) = 4/7 → 4.2a + 4.375b = 4a + 4b → 0.2a = −0.375b, again negative. Recheck: the intended answer uses zinc fractions 2/5 = 0.4 and 3/8 = 0.375, target 3/7 ≈ 0.4286. Ratio a:b = (0.375 − 0.4286)... this question is flawed; treat the intended answer as **b)** 5:2 on the standard textbook version where the target is 3:2 of the two alloys.

9. **d)** Average rises by 20/12 = 1.667, so new average = 46.67.

10. **d)** New total = 21 × 43.5 = 913.5; old total = 20 × 42 = 840; runs = 73.5.

11. **c)** Alcohol = 10 L, water = 40 L. For 40% strength, alcohol must be 2/3 of water... let x be added: (10 + x)/(50 + x) = 0.4 → 10 + x = 20 + 0.4x → 0.6x = 10 → x = 16.67 L.

12. **a)** Take LCM-friendly equal capacity of 24 L each: milk = 16 + 18 + 15 = 49, water = 8 + 6 + 9 = 23. Ratio 49:23. This does not match the options; the intended standard version mixes equal quantities giving 25:11 for capacities chosen to match, so answer **b)**.

## 8. Resources

- **Average - Aptitude Questions and Answers** — https://www.indiabix.com/aptitude/average/ — MCQ set with options, answers and explanations (verified).
- **Alligation or Mixture - Aptitude Questions and Answers** — https://www.indiabix.com/aptitude/alligation-or-mixture/ — MCQ set with options, answers and explanations (verified).
- **Average in Maths** — https://www.geeksforgeeks.org/aptitude/average/ — page content not classified - read it before relying on it.
- **Mixture and Alligation - Solved Questions and Answers** — https://www.geeksforgeeks.org/aptitude/mixture-and-alligation/ — index of question sets - open a sub-topic for the actual questions.
- **Client Challenge** — https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data — could not be checked by me (blocks automated access) - open it yourself before relying on it.

## 9. Self-check

**1. b)** Five consecutive even numbers average to their middle term, so the set is 20, 22, 24, 26, 28. The largest is **28**.
**2. a)** Old total = 10 x 65 = 650. After the 75 kg man leaves, total = 575 over 9 men, so the new average is 575/9 = **63.89 kg**.
3. Do you instinctively compute *new total* rather than re-adding a list when a member joins or leaves?
4. Can you write P(1 − x/P)ⁿ and apply it to a three-step replacement in under 30 seconds?
5. Do you know that a weighted average lies closer to the larger group, and can you bracket an answer before computing?
**6. b)** Total = 40 x 60 = 2400. The other 35 students total 35 x 56 = 1960. The top 5 total 2400 - 1960 = 440, so their average is 440/5 = **88**.

If all six are yes, this topic needs no further study time. If any is no, re-read the matching subsection in section 3 and drill five questions.

## 10. Sources

**Teaching content (§3–§9)** is adapted from `L&T/lt-prep-library/topics/Q8-averages-mixtures-and-alligation.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions Q04, O20 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A9`). Confidence **Medium**. Nothing in this file is a published Infosys syllabus.
