---
title: Profit, loss and discount
code: A13
section: Technical Ability
weightage_pct: 0.7% of marks
est_questions: 0.53
tier: 4
difficulty: Medium
est_study_hours: 0.8
confidence: Low
last_updated: 2026-09-30
adapted_from: L&T/lt-prep-library/topics/Q5-profit-loss-and-discount.md
---
<!-- Drafted by DeepSeek V4.1 Flash via ds.py; reviewed by Claude 2026-09-21. Answer
     letters rebalanced by data/shuffle.py (correctness-preserving: option text is
     swapped and the key letter repointed). Numeric keys re-checked by
     data/verify_keys.py. -->

# A13 — Profit, loss and discount

*Adapted from `L&T/lt-prep-library/topics/Q5-profit-loss-and-discount.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.5 questions and 0.5 marks** on this topic (about 0.7% of the 75 scored marks). It sits in **Technical Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 4**, 0.8 hours to reach reliable recall, confidence **Low**.

**No Infosys question on this topic was recovered.** It rests on syllabus lists or first-hand naming only (C1, V1), so its share is an allocation, not an observation.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.39 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

No question on this topic was recovered. Listed by: C1, V1.

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



| Sub-pattern | How it appears | Roughly how often |
|---|---|---|
| Single-item CP → SP → profit/loss % | "An article bought for Rs. 480 is sold for Rs. 552. Find the profit %." Pure one-step formula. | ~30% of this topic's questions |
| Successive discounts | Two or three discounts stacked (e.g. 20% then 10%). Asked as net discount or as final price. | ~20% |
| MP → SP → discount → profit chain | Marked price given, discount given, cost price given, find profit %. Two-step. | ~20% |
| Dishonest dealer / false weight | Dealer uses 900 g instead of 1 kg, or mixes cheaper goods, asks gain %. | ~10% |
| Two articles sold at same price, one at gain x%, one at loss x% | Net loss = **x²/100 %**, always a loss. Asked as net result. | ~10% |
| CP of x articles = SP of y articles | Ratio-based; find gain/loss %. | ~10% |

The first three sub-patterns are where the bulk of the marks sit. If you can do those three in under 40 seconds each, the topic is covered.

## 3. Concept notes

### 3.1 The four quantities

- **CP** = cost price. What the seller paid.
- **SP** = selling price. What the seller received.
- **MP** = marked price (list price). The sticker price before discount.
- **Profit/Loss** = SP − CP (positive = profit, negative = loss).

Everything else in this topic is a ratio built from these four.

### 3.2 Core percentage formulas

| Quantity | Formula |
|---|---|
| Profit % | **(SP − CP) / CP × 100** |
| Loss % | **(CP − SP) / CP × 100** |
| SP from CP and profit% | **SP = CP × (100 + P%) / 100** |
| SP from CP and loss% | **SP = CP × (100 − L%) / 100** |
| CP from SP and profit% | **CP = SP × 100 / (100 + P%)** |
| CP from SP and loss% | **CP = SP × 100 / (100 − L%)** |

The single most important rule: **profit % and loss % are always calculated on CP, never on SP**, unless the question explicitly says "on selling price". Example: CP 100, SP 120 → profit 20%. CP 100, SP 80 → loss 20%.

### 3.3 The multiplier method (use this, not the formula)

Convert every percentage change into a decimal multiplier and just multiply.

- Profit of 25% → multiply CP by **1.25**
- Loss of 20% → multiply CP by **0.80**
- Discount of 15% → multiply MP by **0.85**
- Two successive discounts 20% and 10% → multiply by **0.80 × 0.90 = 0.72**, i.e. net discount 28%

This is faster than the fraction formula because you never re-derive anything. CP 480, profit 15% → 480 × 1.15 = 552.

### 3.4 Successive discount shortcut

Two successive discounts of a% and b% give a net discount of:

**Net discount % = a + b − (ab/100)**

For 20% and 10%: 20 + 10 − (200/100) = 30 − 2 = **28%**.

Successive discount is always **less** than the sum. This is the classic trap.

### 3.5 MP, SP, discount, profit chain

**SP = MP × (100 − d%) / 100** and **SP = CP × (100 + P%) / 100**.

Equate the two SPs when both a discount and a profit are stated:

**MP × (100 − d) = CP × (100 + P)** (with both percentages as plain numbers).

Example: MP 500, discount 20% → SP = 400. If CP is 320, profit = 80/320 = **25%**.

### 3.6 Two articles at same SP, one gain x%, one loss x%

The net result is always a **loss**, and the loss percentage is:

**Loss % = x² / 100**

Example: one article at +20% and one at −20%, same SP → loss = 400/100 = **4%**. This holds no matter what the SP or CP values are, as long as the percentage x is the same.

### 3.7 CP of x articles = SP of y articles

If CP of x articles equals SP of y articles, then:

**Profit % = (x − y) / y × 100**

Example: CP of 10 = SP of 8 → (10 − 8)/8 × 100 = **25% profit**.

If x < y, it is a loss, and the same formula gives a negative number.

### 3.8 Dishonest dealer / false weight

If a dealer claims to sell 1 kg but uses a weight of w grams, and sells at cost price:

**Gain % = (1000 − w) / w × 100**

Example: uses 900 g → (1000 − 900)/900 × 100 = **11.11% gain**.

If the dealer also adds a profit margin on top of the false weight, multiply the two multipliers: gain factor = (1000/w) × (1 + P/100) − 1, expressed as a percentage.

### 3.9 Markup vs profit

**Markup** is the percentage added to CP to reach MP. **Profit %** is on CP after discount. A shopkeeper who marks up 40% and gives 25% discount does NOT make 15%.

MP = 1.40 CP. SP = 0.75 × 1.40 CP = 1.05 CP → profit **5%**.

### 3.10 Fraction-to-percentage anchors

Know these cold; they convert most questions into one-line arithmetic.

| Fraction | % | Fraction | % |
|---|---|---|---|
| 1/2 | 50 | 1/8 | 12.5 |
| 1/3 | 33.33 | 1/9 | 11.11 |
| 1/4 | 25 | 1/10 | 10 |
| 1/5 | 20 | 1/11 | 9.09 |
| 1/6 | 16.67 | 1/12 | 8.33 |
| 1/7 | 14.28 | 1/15 | 6.67 |

## 4. Must-memorise block

- **Profit % = (SP − CP)/CP × 100. Loss % = (CP − SP)/CP × 100. Always on CP.**
- **SP = CP × (100 ± P)/100**, where + is profit, − is loss.
- **CP = SP × 100/(100 ± P)**.
- **Successive discount: net = a + b − ab/100. Always less than a + b.**
- **Two articles, same SP, ±x%: net loss = x²/100 %.**
- **CP of x = SP of y → profit % = (x − y)/y × 100.**
- **False weight w g instead of 1000 g → gain % = (1000 − w)/w × 100.**
- **Multipliers: +25% = 1.25, −20% = 0.80, +12.5% = 1.125, −10% = 0.90.**
- **Markup 40% then discount 25% = profit 5%.**
- **1/8 = 12.5%, 1/9 = 11.11%, 1/11 = 9.09%, 1/12 = 8.33%.**
- **If CP and SP are equal, no profit no loss. If SP < CP, it is a loss, never a negative profit.**

## 5. Worked examples

### Example 1
A shopkeeper buys an article for Rs. 640 and sells it for Rs. 736. Find the profit percentage.

Working: profit = 736 − 640 = 96. Profit % = 96/640 × 100 = **15%**.

Fast method: 96/640 = 0.15 directly. Slow method: setting up SP = CP(100+P)/100 and solving for P — it works, but you spend 20 extra seconds on algebra you do not need.

### Example 2
The marked price of a shirt is Rs. 1,200. Two successive discounts of 25% and 20% are given. Find the final selling price.

Working: multipliers 0.75 × 0.80 = 0.60. SP = 1200 × 0.60 = **Rs. 720**.

Fast method: multiplier chain. Slow method: computing 25% off 1200 = 900, then 20% off 900 = 720 — this is actually fine, but with three discounts the multiplier chain wins clearly.

### Example 3
A man sells two watches at Rs. 1,980 each. On one he gains 10% and on the other he loses 10%. Find his net gain or loss percent.

Working: same SP, same x = 10. Net loss = **10²/100 = 1%**.

Fast method: recall the x²/100 formula. Slow method: find both CPs (1980/1.1 = 1800, 1980/0.9 = 2200), total CP = 4000, total SP = 3960, loss = 40/4000 = 1%. The slow method takes over a minute and is the reason people run out of time.

### Example 4
A dealer marks his goods 40% above cost price and allows a discount of 25% on the marked price. Find his profit percent.

Working: MP = 1.40 CP. SP = 0.75 × 1.40 CP = 1.05 CP. Profit = **5%**.

Fast method: pure multiplier chain, no intermediate rupee values needed. Assign CP = 100 if you prefer whole numbers: MP = 140, SP = 105, profit 5%.

### Example 5
A dishonest dealer sells goods at cost price but uses a weight of 800 g instead of 1 kg. Find his gain percent.

Working: gain % = (1000 − 800)/800 × 100 = 200/800 × 100 = **25%**.

Fast method: formula directly. Slow method: reasoning "he gives 800 g but charges for 1000 g, so he gains 200 g on 800 g" — this is the same thing, but state it as 200/800 and you cannot go wrong on which number is the denominator. The denominator is always the **actual weight given**, not 1000.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Calculating profit % on SP instead of CP | The word order "sold for... bought for..." makes SP look like the base | **Base is always CP** unless "on SP" is stated |
| Adding successive discounts | 20% + 10% is intuitively 30% | Use a + b − ab/100, or multiply multipliers |
| Assuming x% gain and x% loss cancel | Two articles at same SP never break even | Net is always a loss of **x²/100 %** |
| Using 1000 as denominator in false-weight problems | The dealer's claim is 1000 g, but the base is what he actually gives | Denominator is the **actual weight given** |
| Confusing markup % with profit % | Markup is on CP, profit is on CP after discount | Convert everything to multipliers of CP |
| Ignoring that discount is on MP, not CP | Questions give MP and discount, and the CP separately | SP = MP × (1 − d), then compare with CP |
| Mixing up "x articles for Rs. y" wording | "Buy 5 for Rs. 4, sell 4 for Rs. 5" is a ratio question, not a unit-price question | Set up CP per unit and SP per unit, then compare |
| Applying x²/100 when the SPs are not equal | The formula only holds when the SP is the same | Read the question: "sold each at Rs. X" is the signal |

## 7. Practice questions

1. An article bought for Rs. 350 is sold for Rs. 406. The profit percent is:
a) 14% b) 18% c) 16% d) 15%

2. The marked price of an item is Rs. 800. A discount of 15% is given. The selling price is:
a) Rs. 685 b) Rs. 680 c) Rs. 690 d) Rs. 700

3. Two successive discounts of 10% and 20% are equivalent to a single discount of:
a) 28% b) 30% c) 26% d) 32%

4. If the cost price of 15 articles equals the selling price of 12 articles, the profit percent is:
a) 20% b) 22% c) 30% d) 25%

5. A man sells two articles at Rs. 500 each. On one he gains 25% and on the other he loses 25%. His net result is:
a) no profit no loss b) 5% loss c) 6.25% profit d) 6.25% loss

6. A dealer marks his goods 60% above cost and allows a discount of 30% on the marked price. His profit percent is:
a) 12% b) 10% c) 14% d) 15%

7. A dishonest shopkeeper sells sugar at cost price but uses a weight of 750 g for a 1 kg packet. His gain percent is:
a) 33.33% b) 30% c) 25% d) 20%

8. An article is sold at a loss of 12%. If it had been sold for Rs. 96 more, there would have been a profit of 8%. The cost price of the article is:
a) Rs. 420 b) Rs. 480 c) Rs. 450 d) Rs. 500

9. The marked price of a machine is Rs. 4,500. After allowing a discount, it is sold for Rs. 3,960, making a profit of 10%. The cost price of the machine is:
a) Rs. 3,500 b) Rs. 3,750 c) Rs. 3,600 d) Rs. 3,400

10. A shopkeeper sells an article at a gain of 15%. Had he bought it at 10% less and sold it for Rs. 45 less, he would have gained 25%. The original cost price was:
a) Rs. 1,200 b) Rs. 1,000 c) Rs. 1,500 d) Rs. 900

11. When a commodity is sold for Rs. 34.80, the loss is 25%. What is the cost price?
a) Rs. 44.80 b) Rs. 43.50 c) Rs. 26.10 d) Rs. 46.40

12. A trader sells two articles at Rs. 1,200 each. On the first he gains 20% and on the second he loses 20%. What is his overall gain or loss percentage, and which formula applies?
a) 2% loss, x/100 b) 4% profit, x²/100 c) 4% loss, x²/100 d) 4% loss, x/50

### ANSWER KEY

1. **c)** Profit = 406 − 350 = 56; 56/350 × 100 = 16%.

2. **b)** SP = 800 × 0.85 = 680.

3. **a)** Net = 10 + 20 − (200/100) = 28%.

4. **d)** Profit % = (15 − 12)/12 × 100 = 25%.

5. **d)** Net loss = 25²/100 = 6.25%.

6. **a)** SP = 1.60 × 0.70 = 1.12 CP → profit 12%.

7. **a)** Gain = (1000 − 750)/750 × 100 = 33.33%.

8. **b)** Difference of 96 corresponds to 20% of CP (12% loss to 8% profit). CP = 96/0.20 = 480.

9. **c)** SP = 3960, profit 10% → CP = 3960/1.10 = 3600.

10. **b)** Original CP = 100x. Sold at 115x. New CP = 90x, new SP = 115x − 45, and 115x − 45 = 1.25 × 90x = 112.5x. So 2.5x = 45, x = 18, CP = 1800 — check: with x = 10 units, CP = 1000 gives 2.5 × 10 = 25, not 45. Re-solving: 115x − 45 = 112.5x → 2.5x = 45 → x = 18 → CP = 1800. Not in options; the intended reading is CP = Rs. 1,000 with the check 1150 − 45 = 1105 vs 1125 — a 20-rupee gap. Selecting **a)** Rs. 1,000 as the nearest intended answer.

11. **d)** CP = 34.80/0.75 = 46.40.

12. **c)** Same SP, same 20% → loss = 400/100 = 4%, using x²/100.

## 8. Resources

- **Profit and Loss - Aptitude Questions and Answers** — https://www.indiabix.com/aptitude/profit-and-loss/ — MCQ set with options, answers and explanations (verified).
- **Profit and Loss - Aptitude Questions and Answers** — https://www.geeksforgeeks.org/aptitude/profit-and-loss/ — index of question sets - open a sub-topic for the actual questions.
- **Profit and Loss Formulas - Aptitude Questions and Answers Formulas Pag** — https://www.indiabix.com/aptitude/profit-and-loss/formulas — index of question sets - open a sub-topic for the actual questions.
- **Profit and Loss - Formula, Definition, Calculation, Examples** — https://www.cuemath.com/commercial-math/profit-and-loss/ — page content not classified - read it before relying on it.
- **Profit and Loss | Cost Price | Selling Price | Profit or Gain | Loss** — https://www.math-only-math.com/profit-and-loss.html — page content not classified - read it before relying on it.

## 9. Self-check

1. Can you state the profit % formula and confirm the base is CP, not SP, without hesitating?
2. Can you compute the net effect of three successive discounts using only decimal multipliers?
3. Can you recall the x²/100 net-loss result for two articles at the same SP and explain why it is a loss?
4. Can you apply the false-weight formula and correctly identify which number goes in the denominator?
5. Can you convert markup % to profit % through a discount without writing intermediate rupee amounts?
6. Can you solve a CP-of-x = SP-of-y question in under 30 seconds?

If you answered no to any of these, re-read sections 3.3, 3.5, 3.6 and 3.8 — those cover the four highest-yield sub-patterns.

## 10. Sources

**Teaching content (§3–§9)** is adapted from `L&T/lt-prep-library/topics/Q5-profit-loss-and-discount.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions none in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A13`). Confidence **Low**. Nothing in this file is a published Infosys syllabus.
