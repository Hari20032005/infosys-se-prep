---
title: Percentages and successive change
code: A12
section: Technical Ability
weightage_pct: 0.7% of marks
est_questions: 0.53
tier: 4
difficulty: Medium
est_study_hours: 1.0
confidence: Low
last_updated: 2026-09-30
adapted_from: L&T/lt-prep-library/topics/Q1-percentages-and-successive-change.md
---
<!-- Drafted by DeepSeek V4.1 Flash via ds.py; reviewed by Claude 2026-09-21. Answer
     letters rebalanced by data/shuffle.py (correctness-preserving: option text is
     swapped and the key letter repointed). Numeric keys re-checked by
     data/verify_keys.py. -->

# A12 — Percentages and successive change

*Adapted from `L&T/lt-prep-library/topics/Q1-percentages-and-successive-change.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.5 questions and 0.5 marks** on this topic (about 0.7% of the 75 scored marks). It sits in **Technical Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 4**, 1.0 hours to reach reliable recall, confidence **Low**.

**No Infosys question on this topic was recovered.** It rests on syllabus lists or first-hand naming only (C1), so its share is an allocation, not an observation.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.32 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

No question on this topic was recovered. Listed by: C1.

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



The clearest evidence available is a question observed on an old (probably 2007-08) IndiaBIX paper: *"Cost of an item is x, value increases by p% then decreases by p%, new value is 1 rupee, find the actual value."* That single item tells you the two things that matter most — **successive change** and **working backwards from a final value to the original**.

| Sub-pattern | How it appears | Roughly how often |
|---|---|---|
| Successive change, up then down | Increase by p%, decrease by p%, find net change or the original value | Very common — the signature pattern |
| Reverse percentage (find original) | "Final value is ₹1 after +20% then −20%, find x" | Common, often paired with the above |
| Two successive changes, different rates | Two discounts, two hikes, two years of growth | Common |
| Percentage more/less than (comparison) | "A is 25% more than B; B is what % less than A" | Occasional |
| Consumption / expenditure adjustment | Price rises r%, how much must consumption fall | Occasional |
| Percentage point vs percentage change | Rate moves from 8% to 10%, "how much has it risen" | Occasional, usually a trap option |
| Fraction↔percentage conversion | Speed work inside a bigger question | Constant background skill |

## 3. Concept notes

### 3.1 What a percentage actually is

A percentage is a fraction with denominator 100. "30%" is the number 0.30, which is the number 3/10. Every percentage question becomes fast the moment you stop thinking "thirty per cent" and start thinking "0.30" or "3/10".

*Example:* 30% of 250 = 0.30 × 250 = 75.

### 3.2 Percentage increase and decrease

Percentage increase from A to B = **(B − A)/A × 100**.
Percentage decrease from A to B = **(A − B)/A × 100**.

The denominator is always the **original** value, never the new one. This one sentence prevents more errors than any other in the topic.

*Example:* 40 → 50 is an increase of 10/40 × 100 = 25%.

### 3.3 The multiplier method

Convert every change into a single number you multiply by.

| Change | Multiplier |
|---|---|
| Increase 20% | 1.20 |
| Increase 5% | 1.05 |
| Decrease 25% | 0.75 |
| Decrease 4% | 0.96 |
| Unchanged | 1.00 |

To apply a change: **new = original × multiplier**.
To reverse a change: **original = new ÷ multiplier**.

*Example:* After a 25% rise a price is ₹500. Original = 500 ÷ 1.25 = ₹400.

This replaces every "let x be the original, then x + 25% of x = 500" setup. That setup costs about 45 seconds. The multiplier costs about 8.

### 3.4 Successive percentage change

For two successive changes of a% and b% (positive = increase, negative = decrease):

**Net % change = a + b + (ab/100)**

*Example:* +10% then +20% → 10 + 20 + (200/100) = **32%**.

For a chain of three or more changes, do **not** add the pairwise results into one formula. Multiply the multipliers instead:

**Net multiplier = m₁ × m₂ × m₃ …**, then convert back to a percentage.

*Example:* +15%, +20%, −10% → 1.15 × 1.2 × 0.9 = 1.242 → **24.2% increase**.

### 3.5 The p% up, p% down result

If a value is increased by p% and then decreased by p% (same p), the net change is a **loss of p²/100 percent**, always a loss, and it does not depend on the original value.

Net multiplier = (1 + p/100)(1 − p/100) = **1 − p²/10000**.

| p | Net change |
|---|---|
| 10% | −1% |
| 20% | −4% |
| 25% | −6.25% |
| 50% | −25% |

*Example:* +20% then −20% → multiplier 0.96 → 4% loss overall.

### 3.6 The ₹1 reverse problem (observed pattern)

Value increases by p% then decreases by p%, and the new value is ₹1. Then:

Original = 1 ÷ (1 − p²/10000) = **10000/(10000 − p²)**

*Example:* p = 20 → original = 1 ÷ 0.96 = **₹25/24 ≈ ₹1.0417**. Note it is always slightly **more** than ₹1, because the up-then-down sequence ends with a loss.

### 3.7 Price-up, consumption-down

If the price of a commodity rises by r%, consumption must fall by:

**Reduction % = r/(100 + r) × 100**

*Example:* Price up 25% → reduce consumption by 25/125 × 100 = **20%**.

The mirror case: if price falls by r%, consumption can rise by r/(100 − r) × 100.

*Example:* Price down 20% → consumption can rise 20/80 = **25%**.

### 3.8 "A is x% more than B"

If A is x% more than B, then B is **x/(100 + x) × 100** percent less than A.

*Example:* A is 25% more than B → B is 25/125 = **20%** less than A.

The base changes, so the percentage changes. B is not 25% less than A.

### 3.9 Percentage change vs percentage point

A **percentage point** is the raw difference between two percentages. A **percentage change** is that difference divided by the starting percentage.

*Example:* A rate moves from 8% to 10%. That is a rise of **2 percentage points**, but a rise of 2/8 × 100 = **25 per cent**.

If a question says "the rate went up by 2%", almost every exam intends 2 percentage points. Read the options: if option (a) is 25% and option (b) is 2%, the examiner is testing exactly this distinction.

### 3.10 The fraction table does the heavy lifting

Most exam percentages are chosen so the fraction is clean. Convert, cancel, move on.

*Example:* 37.5% of 96 = 3/8 × 96 = **36**. Doing 0.375 × 96 by long multiplication invites a slip.

### 3.11 Percentages inside other topics

- **Profit and loss:** SP = CP × (1 + profit%) × discount multipliers. Marked price 40% above cost with a 25% discount gives 1.4 × 0.75 = 1.05 → 5% profit.
- **Simple interest:** the rate is a percentage of principal per year.
- **Compound interest:** successive percentage change applied n times, multiplier (1 + r/100)ⁿ.
- **Data interpretation:** almost every DI question ends in a percentage change calculation.

## 4. Must-memorise block

**Core formulas**

| Purpose | Formula |
|---|---|
| % change | (new − old)/old × 100 |
| Successive, two changes | a + b + ab/100 |
| Same p up then p down | −p²/100 |
| Reverse a change | original = new ÷ multiplier |
| p up then p down, new = ₹1 | original = 10000/(10000 − p²) |
| Price +r% → cut consumption | r/(100 + r) × 100 |
| Price −r% → raise consumption | r/(100 − r) × 100 |
| A is x% more than B | B is x/(100 + x) × 100 % less than A |
| n identical changes | multiplierⁿ |

**p²/100 loss table:** 10%→1%, 20%→4%, 25%→6.25%, 30%→9%, 40%→16%, 50%→25%.

**Fraction ↔ percentage**

| Fraction | % | Fraction | % |
|---|---|---|---|
| 1/2 | 50 | 1/9 | 11.11 |
| 1/3 | 33.33 | 1/10 | 10 |
| 1/4 | 25 | 1/11 | 9.09 |
| 1/5 | 20 | 1/12 | 8.33 |
| 1/6 | 16.67 | 1/15 | 6.67 |
| 1/7 | 14.28 | 1/16 | 6.25 |
| 1/8 | 12.5 | 1/20 | 5 |
| 3/8 | 37.5 | 1/25 | 4 |

**Instant rules**
- Up-then-down by the same p is **always a net loss**.
- Multipliers multiply; percentages do not add.
- The base for a percentage change is always the **starting** value.
- **2 percentage points ≠ 2%.**

## 5. Worked examples

**Example 1 — the observed pattern.** An item's cost is x. Its value increases by 20% and then decreases by 20%. The new value is ₹1. Find x.

Fast method: up-then-down by the same p gives multiplier (1 − p²/10000) = 1 − 400/10000 = **0.96**. So 0.96x = 1, giving **x = 100/96 = ₹25/24 ≈ ₹1.0417**.

A slow method sets x + 0.2x − 0.2(x + 0.2x) = 1 and expands. It gets the same answer in four times the time and is the single most common way candidates lose a minute here.

**Example 2 — three successive changes.** A number is increased by 15%, then by 20%, then decreased by 10%. Net change?

Multiply all three multipliers: 1.15 × 1.2 = 1.38; 1.38 × 0.9 = **1.242**. Net change = **24.2% increase**.

Do not chain the two-change formula: 15 + 20 + 3 = 38, then 38 − 10 − 3.8 = 24.2 works here only because the arithmetic happens to be correct — but it is slower and error-prone. Multiplying is one line.

**Example 3 — consumption adjustment.** The price of rice rises by 40%. By what percentage must a household reduce consumption to keep spending unchanged?

Formula: r/(100 + r) × 100 = 40/140 × 100 = **28.57% (2/7)**.

Test it: 100 × 1.4 = 140 spent per unit-of-consumption; to spend 100 you need 100/140 = 5/7 of the old quantity, i.e. a 2/7 cut. The formula is just the test with the algebra already done.

**Example 4 — comparison.** A's income is 25% more than B's. By what percentage is B's income less than A's?

B = 100, A = 125. Difference = 25 on a base of 125: 25/125 × 100 = **20%**.

The trap answer is 25%. The base changed from B to A, and the percentage changed with it.

**Example 5 — mark-up and discount chain.** A shopkeeper marks his goods 60% above cost and then offers two successive discounts of 10% and 20%. Profit percent?

Marked price = 1.6C. Selling price = 1.6C × 0.9 × 0.8 = 1.6C × 0.72 = 1.152C. Profit = **15.2%**.

Do not add 60 − 10 − 20 = 30. The discounts apply to the marked price, and the two discounts compound.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Adding successive percentages | 10% + 20% feels like 30% | Use a + b + ab/100, or multiply multipliers |
| Assuming +p% then −p% is neutral | Intuition says the two cancel | Memorise: it is always a loss of p²/100 |
| Using the new value as the base | "B is what % less than A" invites dividing by the wrong number | The denominator is the value you are comparing *from* |
| Percentage point vs percentage change | 8% → 10% is 2 points but 25% | Check the option wording before computing |
| Forgetting that a discount applies to marked price, not cost | 40% mark-up then 25% off looks like 15% profit | Compute SP = CP × markup × discount |
| Treating a 0.96 multiplier as a 4% gain | Sign confusion on reverse problems | Up-then-down is a loss; the original is always *more* than ₹1 |
| Rounding 33.33% to 33% mid-calculation | Small rounding compounds across steps | Keep fractions (1/3, 1/6, 1/7) until the final line |
| Applying a percentage to the wrong year | In two-year growth, year-2 growth applies to the year-1 figure | Year 2 = base × m₁ × m₂, never base × (1 + r₁ + r₂) |

## 7. Practice questions

**1.** An item's price is increased by 20% and then decreased by 20%. The net change is:
a) no change b) 4% increase c) 4% decrease d) 2% decrease

**2.** A number is increased by 25% and then the result is decreased by 20%. The net change is:
a) 5% decrease b) 5% increase c) no change d) 2.5% decrease

**3.** Two successive discounts of 10% and 20% are equivalent to a single discount of:
a) 30% b) 25% c) 28% d) 32%

**4.** The price of sugar rises by 25%. By what percent must a family reduce consumption so that expenditure stays the same?
a) 25% b) 20% c) 16.67% d) 22.5%

**5.** A value increases by 50% and then decreases by 50%. If the new value is ₹1, the original value is:
a) ₹3/4 b) ₹4/3 c) ₹2 d) ₹3/2

**6.** A's salary is 20% more than B's. B's salary is what percent less than A's?
a) 20% b) 25% c) 15% d) 16 2/3%

**7.** Two successive increases of 10% and 20% together equal a single increase of:
a) 32% b) 30% c) 31% d) 33%

**8.** A town's population is 50,000. It grows by 10% in the first year and 10% in the second year. The population after two years is:
a) 60,000 b) 61,000 c) 60,250 d) 60,500

**9.** The price of an article is reduced by 25%. By what percent must the reduced price be raised to restore the original price?
a) 33 1/3% b) 25% c) 30% d) 40%

**10.** A state's unemployment rate rises from 8% to 10%. The percentage increase in the rate is:
a) 12.5% b) 2% c) 20% d) 25%

**11.** In an examination, a student scoring 35% fails by 40 marks, while a student scoring 45% gets 20 marks more than the pass mark. The total marks are:
a) 600 b) 550 c) 650 d) 500

**12.** A shopkeeper marks his goods 40% above cost price and allows a discount of 25% on the marked price. His profit percent is:
a) 15% b) 5% c) 10% d) 2.5%

### ANSWER KEY

1. **c** — 1.2 × 0.8 = 0.96, so the net change is −p²/100 = −4%, a decrease.
2. **c** — 1.25 × 0.8 = 1.00 exactly, so there is no net change.
3. **c** — 0.9 × 0.8 = 0.72, which is a 28% discount, not 30%.
4. **b** — reduction = r/(100 + r) × 100 = 25/125 × 100 = 20%.
5. **b** — 1.5 × 0.5 = 0.75, so original = 1 ÷ 0.75 = ₹4/3.
6. **d** — B = 100, A = 120, so B is 20/120 = 1/6 = 16 2/3% less than A.
7. **a** — 1.1 × 1.2 = 1.32, so the combined increase is 32%.
8. **d** — 50,000 × 1.1 × 1.1 = 50,000 × 1.21 = 60,500.
9. **a** — B = 75, A = 100, so the rise needed is 25/75 = 33 1/3%.
10. **d** — percentage change = 2/8 × 100 = 25% (2 percentage points).
11. **a** — the 10% gap between 35% and 45% equals 40 + 20 = 60 marks, so total = 60/0.10 = 600.
12. **b** — SP = 1.4C × 0.75 = 1.05C, so profit = 5%.

## 8. Resources

- **Percentage - Aptitude Questions and Answers** — https://www.indiabix.com/aptitude/percentage/ — MCQ set with options, answers and explanations (verified).
- **Introduction to Percents** — https://www.mathsisfun.com/percentage.html — page content not classified - read it before relying on it.
- **Percentage - Wikipedia** — https://en.wikipedia.org/wiki/Percentage — reference article.

## 9. Self-check

1. Can you state the net result of increasing by 20% and then decreasing by 20%, without calculating?
2. Can you convert a two-step change of +15% then −10% into a single percentage in under fifteen seconds?
3. Can you write down the formula for "price rises by r%, how much must consumption fall" and apply it to r = 50?
4. Do you instantly know that 37.5% is 3/8 and that 6.25% is 1/16?
5. Can you explain, in one sentence, why A being 20% more than B does not mean B is 20% less than A?
6. Given "value rises 20% then falls 20% and is now ₹1", can you produce ₹25/24 without writing an equation?

## 10. Sources

**Teaching content (§3–§9)** is adapted from `L&T/lt-prep-library/topics/Q1-percentages-and-successive-change.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions none in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A12`). Confidence **Low**. Nothing in this file is a published Infosys syllabus.
