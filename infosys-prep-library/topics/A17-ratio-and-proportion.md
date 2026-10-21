---
title: Ratio, proportion and cost models
code: A17
section: Technical Ability
weightage_pct: 0.7% of marks
est_questions: 0.53
tier: 4
difficulty: Medium
est_study_hours: 0.6
confidence: Low
last_updated: 2026-09-30
adapted_from: L&T/lt-prep-library/topics/Q4-ratio-proportion-and-cost-models.md
---
<!-- Drafted by DeepSeek V4.1 Flash via ds.py; reviewed by Claude 2026-09-21. Answer
     letters rebalanced by data/shuffle.py (correctness-preserving: option text is
     swapped and the key letter repointed). Numeric keys re-checked by
     data/verify_keys.py. -->

# A17 — Ratio, proportion and cost models

*Adapted from `L&T/lt-prep-library/topics/Q4-ratio-proportion-and-cost-models.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.5 questions and 0.5 marks** on this topic (about 0.7% of the 75 scored marks). It sits in **Technical Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 4**, 0.6 hours to reach reliable recall, confidence **Low**.

**No Infosys question on this topic was recovered.** It rests on syllabus lists or first-hand naming only (C1, V1), so its share is an allocation, not an observation.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.53 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

No question on this topic was recovered. Listed by: C1, V1.

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



The observed question from an old (probably 2007-08) IndiaBIX paper:

> *"For 15 people each pays Rs 20, for 20 people each pays Rs 18, for 40 people how much each?"*

This is a **fixed cost plus variable cost per head** model. Convert each statement into a total, then solve two simultaneous equations:

- 15 people × Rs 20 = **Rs 300** total
- 20 people × Rs 18 = **Rs 360** total
- Difference: 5 extra people cost Rs 60 → **Rs 12 per head (variable)**
- Fixed: 300 − (15 × 12) = **Rs 120**
- 40 people: 120 + (40 × 12) = Rs 600 → **Rs 15 per head**

| Sub-pattern | How it appears | Roughly how often |
|---|---|---|
| Fixed + variable cost model | Two (people, rate) pairs, cost per head asked for a third count | The observed question; expect ~1 of the 2-3 |
| Direct proportion | "If 5 machines make 200 units in 4 hours..." | Common, usually combined with inverse |
| Inverse proportion | More workers, fewer days; more speed, less time | Common |
| Partnership profit sharing | Capital ratios, sometimes with different time periods | Occasional, 1 in 3 papers |
| Simple ratio split | Divide an amount in a given ratio | Occasional, easiest of the set |
| Ratio chain / combining | a:b and b:c given, find a:c | Occasional |
| Mean / third proportional | "Mean proportional between 4 and 25" | Rare |

## 3. Concept notes

### 3.1 Ratio basics

A ratio `a : b` compares two quantities of the **same unit**. It is a fraction, `a/b`, and it can be scaled freely: **3 : 4 = 6 : 8 = 30 : 40**.

To split a total `T` in the ratio `a : b : c`:
- Total parts = `a + b + c`
- One part = `T / (a + b + c)`
- Share of A = `a × T / (a + b + c)`

*Example:* Rs 1,200 split 2 : 3 : 5 → 10 parts, one part = 120, shares = **240, 360, 600**.

**Ratio of fractions:** multiply every term by the LCM of the denominators. `1/2 : 1/3 : 1/4` → multiply by 12 → **6 : 4 : 3**.

**Combining two ratios** where the middle term is common: for `a : b = 3 : 4` and `b : c = 6 : 7`, make `b` the same in both (LCM of 4 and 6 is 12): `a : b = 9 : 12`, `b : c = 12 : 14`, so **a : b : c = 9 : 12 : 14** and **a : c = 9 : 14**.

### 3.2 Proportion

Four quantities are in proportion when `a : b = c : d`, written `a : b :: c : d`, and then **a × d = b × c** (product of extremes = product of means). This cross-multiplication is the single most-used tool in the topic.

- **Mean proportional** between `a` and `c` is `√(a × c)`. Mean proportional between 4 and 25 is **10**.
- **Third proportional** to `a` and `b` is `b²/a`. Third proportional to 9 and 12 is `144/9` = **16**.

A quantity `x` added to each of four numbers keeps them proportional only when `(a+x)(d+x) = (b+x)(c+x)` — a quadratic in which the `x²` terms usually cancel, leaving a linear equation.

### 3.3 Direct and inverse variation

**Direct:** `y = kx`. Double `x`, double `y`.

*Example:* 4 kg costs Rs 200 → 7 kg costs `7 × 50` = Rs 350.

**Inverse:** `y = k/x`, equivalently `x₁y₁ = x₂y₂`. Double `x`, halve `y`.

*Example:* 8 workers take 12 days → 6 workers take `8 × 12 / 6` = **16 days**.

**Multi-variable (the chain rule):** write the relation as a product and keep units consistent.

`Work = Rate × Machines × Hours`

*Example:* 5 machines, 200 units, 4 hours → per machine-hour = `200 / (5 × 4)` = 10 units. Then 8 machines for 6 hours = `8 × 6 × 10` = **480 units**.

### 3.4 The fixed + variable cost model

Total cost = **Fixed cost `F` + (variable rate `v` × quantity `n`)**.

```
Total = F + v·n
```

Given two observations `(n₁, Total₁)` and `(n₂, Total₂)`:

```
v = (Total₂ − Total₁) / (n₂ − n₁)
F = Total₁ − v·n₁
```

Two warnings that decide whether you get this right:

1. **The question may give the per-unit rate, not the total.** "Each pays Rs 20" with 15 people means total = 300. Convert first, always.
2. **The question may ask for the per-unit rate at the new quantity**, not the total. Compute the total, then divide.

### 3.5 Partnership profit sharing

Profit is shared in the ratio of **capital × time**.

| Case | Profit ratio |
|---|---|
| Same time | `C₁ : C₂` |
| Different times | `C₁T₁ : C₂T₂` |
| Money added/withdrawn mid-term | Split each partner's period into segments and sum |

*Example:* A invests Rs 5,000 for 12 months, B invests Rs 6,000 for 8 months. Ratio = 60,000 : 48,000 = **5 : 4**. On a profit of Rs 9,000, B gets `4/9 × 9000` = Rs 4,000.

For a sleeping partner (invests money, no work), the ratio is still capital × time; the active partner's extra is taken out first as a salary if the question says so.

### 3.6 Speed shortcuts worth drilling

| Situation | Shortcut |
|---|---|
| Ratio `a : b`, sum known | One part = Sum / (a + b) |
| Ratio `a : b`, difference known | One part = Difference / (a − b) |
| Two numbers, ratio and HCF known | Numbers = `aH` and `bH`; **LCM = a·b·H** |
| Two numbers, ratio and LCM known | **Product = LCM × HCF** |
| Adding x to make four terms proportional | Cross-multiply, cancel `x²`, solve linear |

For ratio 5 : 7 with HCF 6: numbers are 30 and 42, LCM = `5 × 7 × 6` = **210**.

## 4. Must-memorise block

**Core**

- **a : b = ka : kb** for any `k ≠ 0`
- Split in `a : b : c` → one part = **Total / (a + b + c)**
- **a × d = b × c** when `a : b :: c : d`
- Mean proportional of `a`, `c` = **√(ac)**; third proportional to `a`, `b` = **b²/a**

**Variation**

- Direct: **x₁/y₁ = x₂/y₂**
- Inverse: **x₁y₁ = x₂y₂**
- Machines/hours/work: **M₁D₁H₁ / W₁ = M₂D₂H₂ / W₂**

**Cost model**

- **Total = F + v·n**
- **v = ΔTotal / Δn**; **F = Total − v·n**

**Partnership**

- Profit ratio = **Capital × Time**
- Same capital, different time → ratio of times
- Same time, different capital → ratio of capitals

**Numbers**

- Product of two numbers = **LCM × HCF**
- Ratio `a : b`, HCF `h` → numbers `ah`, `bh`; LCM = `abh`
- Speed and time: inverse; Speed and distance (fixed time): direct
- Work and time: inverse; Work and workers (fixed time): direct

## 5. Worked examples

### Example 1 - the observed pattern (old paper)

For 15 people each pays Rs 20; for 20 people each pays Rs 18. For 40 people, how much does each pay?

**Fast method:**
Totals: 15 × 20 = 300; 20 × 18 = 360.
ΔTotal = 60 over Δn = 5 → **v = Rs 12 per head**.
F = 300 − (15 × 12) = **Rs 120**.
For 40: Total = 120 + 480 = **Rs 600** → per head = **Rs 15**.

**Slow method:** setting up `F + 15v = 300` and `F + 20v = 360` and subtracting algebraically takes 90 seconds instead of 30. Same arithmetic, more writing. Do the subtraction in your head.

### Example 2 - fixed + variable with the rate given

A caterer charges Rs 60 per plate for 50 plates and Rs 51 per plate for 80 plates. Find the fixed charge.

Totals: 50 × 60 = 3,000; 80 × 51 = 4,080.
Δ = 1,080 over 30 plates → **v = Rs 36 per plate**.
F = 3,000 − (50 × 36) = 3,000 − 1,800 = **Rs 1,200**.

Note the trap: the *per-plate rate falls* as plates rise. That is the whole point of a fixed cost — it is the observation that gives it away, not a contradiction.

### Example 3 - partnership with unequal time

A, B and C invest in the ratio 2 : 3 : 5 for 6, 4 and 3 months respectively. Total profit is Rs 13,000. Find C's share.

Profit ratio = 2×6 : 3×4 : 5×3 = 12 : 12 : 15 = **4 : 4 : 5**.
Total parts = 13 → one part = 13,000 / 13 = 1,000.
C = 5 × 1,000 = **Rs 5,000**.

**Slow method:** computing each product as a rupee figure for every partner wastes 40 seconds. Reduce the ratio to lowest terms first, then divide.

### Example 4 - chain rule

If 5 machines produce 200 units in 4 hours, how many units will 8 machines produce in 6 hours?

Rate per machine-hour = 200 / (5 × 4) = **10 units**.
Output = 8 × 6 × 10 = **480 units**.

Notice the two-step structure: reduce everything to a *unit rate*, then scale up. Any "X machines, Y hours" question reduces to this.

### Example 5 - making four terms proportional

What must be added to each of 3, 5, 12 and 18 so the results are proportional?

Set up: `(3 + x) / (5 + x) = (12 + x) / (18 + x)`.
Cross-multiply: `(3+x)(18+x) = (5+x)(12+x)`
`54 + 21x + x² = 60 + 17x + x²`
`4x = 6` → **x = 1.5**.

The `x²` cancelling is not a coincidence — it always cancels in this pattern. Knowing that, you can cross-multiply and jump straight to `4x = 6`.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Using the per-head rate as if it were the total | "Each pays Rs 20" reads like a total | Multiply rate × count the instant you read it |
| Assuming a constant per-head rate | The observed question deliberately varies it | If the rate changes with the count, it is a fixed + variable model |
| Answering the total when the per-head rate was asked | Both numbers appear in your working | Underline the unit asked for: "how much **each**" |
| Forgetting to multiply by time in partnerships | Capital ratio alone gives the wrong split | Ask: "did they invest for the same number of months?" |
| Mixing direct and inverse variation | "More workers → fewer days" feels backwards | More of X giving less of Y is inverse; write `x₁y₁ = x₂y₂` |
| Cancelling the `x` in `(3+x)/(5+x)` | Looks like a fraction to simplify | You can only cancel factors, never added terms |
| Computing LCM from ratio + HCF by multiplying the ratio terms | `5 × 7 = 35` is not the LCM | LCM = **ratio product × HCF** = 5 × 7 × 6 = 210 |
| Leaving a blank because the topic "looks" small | No negative marking | A 25% blind guess beats a guaranteed zero |

## 7. Practice questions

**1.** Rs 1,200 is divided among A, B and C in the ratio 2 : 3 : 5. What is C's share?
a) 240 b) 360 c) 600 d) 500

**2.** For 15 people each pays Rs 20. For 20 people each pays Rs 18. For 40 people, how much does each pay?
a) 12 b) 15 c) 16 d) 18

**3.** If a : b = 3 : 4 and b : c = 6 : 7, find a : c.
a) 7 : 9 b) 21 : 24 c) 9 : 14 d) 4 : 7

**4.** 8 workers build a wall in 12 days. How many days will 6 workers take?
a) 9 b) 16 c) 14 d) 18

**5.** A invests Rs 5,000 for 12 months and B invests Rs 6,000 for 8 months. Total profit is Rs 9,000. What is B's share?
a) 5,000 b) 4,000 c) 4,500 d) 3,600

**6.** A service charges a fixed fee plus an amount per head. For 10 people the total is Rs 1,000; for 25 people the total is Rs 1,750. What is the total for 40 people?
a) 2,500 b) 2,250 c) 2,000 d) 3,000

**7.** Two numbers are in the ratio 5 : 7 and their HCF is 6. What is their LCM?
a) 42 b) 105 c) 210 d) 126

**8.** In 60 litres of a mixture, milk and water are in the ratio 2 : 1. How much water must be added to make the ratio 1 : 1?
a) 20 litres b) 10 litres c) 30 litres d) 40 litres

**9.** If 5 machines produce 200 units in 4 hours, how many units will 8 machines produce in 6 hours?
a) 384 b) 720 c) 600 d) 480

**10.** A, B and C invest in the ratio 2 : 3 : 5 for 6, 4 and 3 months respectively. Total profit is Rs 13,000. Find C's share.
a) 5,000 b) 4,500 c) 4,000 d) 6,000

**11.** A caterer charges a fixed amount plus a rate per plate. For 50 plates the charge is Rs 60 per plate; for 80 plates it is Rs 51 per plate. What is the fixed charge?
a) 800 b) 1,000 c) 1,500 d) 1,200

**12.** What must be added to each of 3, 5, 12 and 18 so that the results are in proportion?
a) 2 b) 3 c) 6 d) 1.5

### ANSWER KEY

**1. c)** 10 parts, one part = 120; C = 5 × 120 = 600.
**2. b)** Totals 300 and 360; v = 60/5 = 12; F = 300 − 180 = 120; for 40 → (120 + 480)/40 = 15.
**3. c)** Make b common: a : b : c = 9 : 12 : 14, so a : c = 9 : 14.
**4. b)** Inverse proportion: 8 × 12 / 6 = 16 days.
**5. b)** Ratio = 60,000 : 48,000 = 5 : 4; B = 4/9 × 9,000 = 4,000.
**6. a)** v = 750/15 = 50; F = 1,000 − 500 = 500; total = 500 + 40×50 = 2,500.
**7. c)** Numbers are 30 and 42; LCM = 5 × 7 × 6 = 210.
**8. a)** Milk 40, water 20; need 40 water, so add 20 litres.
**9. d)** Unit rate = 200/(5×4) = 10; output = 8 × 6 × 10 = 480.
**10. a)** Profit ratio = 12 : 12 : 15 = 4 : 4 : 5; one part = 1,000; C = 5,000.
**11. d)** Totals 3,000 and 4,080; v = 1,080/30 = 36; F = 3,000 − 1,800 = 1,200.
**12. d)** (3+x)(18+x) = (5+x)(12+x) → 54 + 21x = 60 + 17x → 4x = 6 → x = 1.5.

## 8. Resources

- **Ratio and Proportion - Aptitude Questions and Answers** — https://www.indiabix.com/aptitude/ratio-and-proportion/ — MCQ set with options, answers and explanations (verified).
- **Partnership - Aptitude Questions and Answers** — https://www.indiabix.com/aptitude/partnership/ — MCQ set with options, answers and explanations (verified).
- **Client Challenge** — https://www.khanacademy.org/math/pre-algebra/pre-algebra-ratios-rates — could not be checked by me (blocks automated access) - open it yourself before relying on it.
- **artofproblemsolving.com** — https://artofproblemsolving.com/wiki/index.php/Ratio — could not be checked by me (blocks automated access) - open it yourself before relying on it.
- **Aptitude Questions and Answers** — https://www.geeksforgeeks.org/aptitude-questions-and-answers/ — index of question sets - open a sub-topic for the actual questions.

## 9. Self-check

Answer yes or no to each. Six yes answers means you can stop studying this topic.

1. Can you convert "15 people each pays Rs 20" into a total in under five seconds?
2. Can you write the fixed-plus-variable rule `Total = F + v·n` from memory and compute `v` and `F` from two totals without setting up simultaneous equations on paper?
3. Do you instantly know that "more workers, fewer days" means inverse proportion, and can you apply `x₁y₁ = x₂y₂`?
4. Can you compute a partnership profit ratio using **capital × time** without being prompted?
5. Do you know that LCM = ratio product × HCF, and that product of two numbers = LCM × HCF?
6. Can you spot the difference between "find the total" and "find the amount each pays" in a word problem?

## 10. Sources

**Teaching content (§3–§9)** is adapted from `L&T/lt-prep-library/topics/Q4-ratio-proportion-and-cost-models.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions none in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A17`). Confidence **Low**. Nothing in this file is a published Infosys syllabus.
