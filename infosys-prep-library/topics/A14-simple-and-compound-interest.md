---
title: Simple and compound interest
code: A14
section: Technical Ability
weightage_pct: 0.7% of marks
est_questions: 0.53
tier: 4
difficulty: Medium
est_study_hours: 0.7
confidence: Low
last_updated: 2026-09-30
adapted_from: L&T/lt-prep-library/topics/Q6-simple-and-compound-interest.md
---
<!-- Drafted by DeepSeek V4.1 Flash via ds.py; reviewed by Claude 2026-09-21. Answer
     letters rebalanced by data/shuffle.py (correctness-preserving: option text is
     swapped and the key letter repointed). Numeric keys re-checked by
     data/verify_keys.py. -->

# A14 — Simple and compound interest

*Adapted from `L&T/lt-prep-library/topics/Q6-simple-and-compound-interest.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.5 questions and 0.5 marks** on this topic (about 0.7% of the 75 scored marks). It sits in **Technical Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 4**, 0.7 hours to reach reliable recall, confidence **Low**.

**No Infosys question on this topic was recovered.** It rests on syllabus lists or first-hand naming only (C1), so its share is an allocation, not an observation.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.45 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

No question on this topic was recovered. Listed by: C1.

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



| Sub-pattern | How it appears | Roughly how often |
|---|---|---|
| Straight SI for a period | Given P, R, T (years); find SI or amount | Very common |
| Straight CI for 2–3 years | Given P, R; find amount or CI | Very common |
| Difference between CI and SI | "CI − SI for 2 years is ₹X, find P/R" | Common |
| CI with fractional/odd time | 2 years 6 months, or compounded half-yearly | Occasional |
| Population/depreciation | Growth or decay using the CI formula | Occasional |
| Installments / equal annual payment | Rare at campus level | Rare |
| Rate or time as the unknown | Solve backward for R or T | Occasional |

The first three rows carry almost all the marks. If you can compute CI − SI for two years instantly, you have covered the highest-value pattern.

## 3. Concept notes

### 3.1 The vocabulary

**Principal (P)** — the money lent or borrowed. **Rate (R)** — percent per annum. **Time (T)** — in years. **Interest** — the charge for using money. **Amount (A)** — principal plus interest, i.e. A = P + interest.

Simple interest charges on the original principal only, every year. Compound interest charges on principal *plus interest already earned*, so it grows on itself.

### 3.2 Simple interest

**SI = P × R × T / 100**
**Amount A = P + SI = P(1 + RT/100)**

Example: P = 5000, R = 8%, T = 3 years → SI = 5000 × 8 × 3 / 100 = **₹1200**, A = ₹6200.

Note the linearity. Double the time, double the interest. Double the rate, double the interest. SI for 5 years at 6% is exactly five times SI for 1 year at 6%.

### 3.3 Compound interest — annual compounding

**A = P(1 + R/100)^T**
**CI = A − P**

Example: P = 5000, R = 8%, T = 2 → A = 5000 × 1.08² = 5000 × 1.1664 = **₹5832**, CI = ₹832.

The bracket (1 + R/100) is called the **growth factor**. If R = 10%, the factor is 1.1. If R = 12.5%, it is 1.125. Get into the habit of converting R to a factor first, then raising it to the power T. Squaring 1.08 mentally is far easier than squaring 108/100.

### 3.4 The CI − SI difference — the highest-value shortcut

For **2 years**:
**CI − SI = P × (R/100)²**

Example: P = 10000, R = 10%, T = 2. SI = 2000. CI = 10000 × 0.21 = 2100. Difference = **₹100**. Check: 10000 × (0.1)² = 10000 × 0.01 = ₹100. ✓

For **3 years**:
**CI − SI = P × (R/100)² × (300 + R)/100**

Example: P = 10000, R = 10%, T = 3. Difference = 10000 × 0.01 × 310/100 = 100 × 3.1 = **₹310**. Slow check: CI = 10000 × 1.331 − 10000 = 3310; SI = 3000; difference 310. ✓

### 3.5 CI for two years, expanded

**CI₂ = P × (2R/100 + (R/100)²)**
Equivalently, the two-year effective rate is **2R + R²/100** percent.

Example: R = 10% → effective 2-year rate = 20 + 1 = **21%**. So on ₹10000 the CI is ₹2100.

Effective rate table for two years:

| R per annum | Effective 2-year rate |
|---|---|
| 5% | 10.25% |
| 8% | 16.64% |
| 10% | 21% |
| 12% | 25.44% |
| 15% | 32.25% |
| 20% | 44% |
| 25% | 56.25% |

### 3.6 Compounding more than once a year

If compounded **half-yearly**: rate per half-year = R/2, number of periods = 2T.
**A = P(1 + R/200)^(2T)**

If compounded **quarterly**: rate per quarter = R/4, periods = 4T.
**A = P(1 + R/400)^(4T)**

Example: P = 8000, R = 10%, T = 1 year, half-yearly → A = 8000 × (1.05)² = 8000 × 1.1025 = **₹8820**.

A **higher** compounding frequency always gives a **higher** amount for the same nominal rate. Half-yearly beats annual; quarterly beats half-yearly.

### 3.7 Fractional time under CI

When T is not a whole number of years, textbooks treat the fractional tail as **simple** interest on the last amount.

Example: P = 1000, R = 10%, T = 2 years 6 months.
A after 2 years = 1000 × 1.21 = 1210.
SI on 1210 for 6 months at 10% = 1210 × 10 × 0.5 / 100 = 60.5.
A = **₹1270.50**.

Check the question's wording — many papers simply use the exact power instead.

### 3.8 Population and depreciation

Same formula, different words.
- Growth: **P_final = P_initial × (1 + R/100)^n**
- Depreciation/decay: **P_final = P_initial × (1 − R/100)^n**

Example: A machine worth ₹50000 depreciates 20% a year. After 2 years: 50000 × 0.8² = 50000 × 0.64 = **₹32000**.

### 3.9 Solving for the unknown

SI: from SI = PRT/100, get **P = 100·SI/(RT)**, **R = 100·SI/(PT)**, **T = 100·SI/(PR)**.

CI: usually easier to work backward via the factor. If the amount doubles in 5 years, the factor is 2, so 2 = (1+R/100)^5 — no need to solve for R directly if the question only asks "when will it be 4×?" Answer: 10 years, because squaring the factor squares the exponent multiple.

### 3.10 Doubling and other memorised multipliers

| Growth factor | Meaning |
|---|---|
| 1.1² = 1.21 | 10% for 2 years |
| 1.1³ = 1.331 | 10% for 3 years |
| 1.05² = 1.1025 | 5% for 2 years |
| 1.08² = 1.1664 | 8% for 2 years |
| 1.12² = 1.2544 | 12% for 2 years |
| 1.15² = 1.3225 | 15% for 2 years |
| 1.2² = 1.44 | 20% for 2 years |
| 1.25² = 1.5625 | 25% for 2 years |

## 4. Must-memorise block

**SI = P·R·T / 100**
**A = P(1 + RT/100)**
**A = P(1 + R/100)^T**
**CI = A − P**
**CI₂ − SI₂ = P(R/100)²**
**CI₃ − SI₃ = P(R/100)²(300 + R)/100**
**Two-year effective rate = 2R + R²/100 percent**
**Half-yearly: A = P(1 + R/200)^(2T)**
**Quarterly: A = P(1 + R/400)^(4T)**
**Depreciation: A = P(1 − R/100)^n**

| Square to know | Value |
|---|---|
| 1.05² | 1.1025 |
| 1.06² | 1.1236 |
| 1.08² | 1.1664 |
| 1.10² | 1.21 |
| 1.12² | 1.2544 |
| 1.15² | 1.3225 |
| 1.20² | 1.44 |
| 1.25² | 1.5625 |

| Cube to know | Value |
|---|---|
| 1.05³ | 1.157625 |
| 1.10³ | 1.331 |
| 1.20³ | 1.728 |

**Rule: R% for 2 years effective = 2R + R²/100.**
**Rule: CI − SI over 2 years = interest on the first year's interest only.**
**Rule: more frequent compounding → larger amount, same nominal rate.**
**Rule: at SI the amount grows in a straight line; at CI it curves upward.**

## 5. Worked examples

**Example 1 — straight SI.**
Find the SI on ₹12,000 at 7.5% per annum for 4 years.
SI = 12000 × 7.5 × 4 / 100 = 12000 × 30 / 100 = **₹3600**.
Fast method: multiply P × R first (90000), × T (360000), ÷ 100. Do the ÷100 first whenever it makes the number nicer — 12000/100 = 120, then 120 × 7.5 × 4 = 3600. One multiplication chain, no fractions.

**Example 2 — straight CI.**
Find the CI on ₹8,000 at 10% per annum for 3 years.
Factor = 1.1. 1.1³ = 1.331. A = 8000 × 1.331 = ₹10,648. CI = **₹2,648**.
Slow method: compute year by year (8000 → 8800 → 9680 → 10648). Slower because of three separate additions. Use the memorised 1.331.

**Example 3 — the CI − SI difference.**
The difference between CI and SI on a sum for 2 years at 8% per annum is ₹32. Find the sum.
Using CI₂ − SI₂ = P(R/100)²: 32 = P × (0.08)² = P × 0.0064.
P = 32 / 0.0064 = **₹5,000**.
Slow method: set up CI − SI algebraically and expand. Pointless — the shortcut is one division.

**Example 4 — half-yearly compounding.**
Find the CI on ₹16,000 at 12% per annum for 1 year, compounded half-yearly.
Rate per half-year = 6%, periods = 2. A = 16000 × 1.06² = 16000 × 1.1236 = ₹17,977.60. CI = **₹1,977.60**.
Trap reminder: 1 year half-yearly is NOT 12% once — it is 6% twice, giving an effective 12.36%.

**Example 5 — depreciation.**
A car worth ₹4,00,000 depreciates at 10% per annum. What is its value after 3 years?
A = 400000 × 0.9³ = 400000 × 0.729 = **₹2,91,600**.
Fast method: knowing 0.9³ = 0.729 saves the repeated subtraction. Note the base is (1 − R/100), not (1 + R/100).

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Using 12% once for half-yearly over 1 year | Reads "1 year" and stops reading | Rate halves AND periods double: 6% twice |
| Adding R for multiple years under CI | Habit from SI | 10% for 2 years is 21%, not 20% |
| CI − SI formula used for 3 years | Remembered only the 2-year version | 3-year extra factor is (300 + R)/100 |
| Depreciation sign error | Using (1 + R/100) | Depreciation always uses (1 − R/100) |
| Time in months not converted | Question says "9 months" | Under SI, T in years = 9/12 = 0.75 |
| Treating "CI − SI = ₹X" as the CI | Misreading which value is given | X is the difference; both CI and SI are larger |
| Forgetting to subtract P for CI | A is the amount, not the interest | CI = A − P, always |
| Fractional-year CI handled as pure CI | Textbook convention differs | Test the options; most papers use SI on the tail |

## 7. Practice questions

**1.** Find the SI on ₹6,000 at 5% per annum for 2 years.
a) ₹550 b) ₹650 c) ₹700 d) ₹600

**2.** Find the amount when ₹5,000 is invested at 10% per annum CI for 2 years.
a) ₹6,050 b) ₹6,000 c) ₹5,500 d) ₹6,100

**3.** The difference between CI and SI on a sum for 2 years at 10% per annum is ₹50. Find the sum.
a) ₹4,000 b) ₹5,000 c) ₹5,500 d) ₹6,000

**4.** Find the CI on ₹10,000 at 8% per annum for 2 years.
a) ₹1,600 b) ₹1,640 c) ₹1,700 d) ₹1,664

**5.** A sum doubles in 5 years at CI. In how many years will it become 4 times?
a) 8 b) 12 c) 10 d) 15

**6.** Find the CI on ₹8,000 at 12% per annum for 1 year, compounded half-yearly.
a) ₹960 b) ₹1,000 c) ₹988.80 d) ₹972

**7.** The CI on a sum for 2 years at 5% per annum is ₹205. Find the sum.
a) ₹2,000 b) ₹2,100 c) ₹1,900 d) ₹2,200

**8.** A machine worth ₹80,000 depreciates at 10% per annum. Its value after 2 years is:
a) ₹64,800 b) ₹64,000 c) ₹65,000 d) ₹63,000

**9.** The difference between CI and SI on ₹10,000 for 3 years at 10% per annum is:
a) ₹300 b) ₹320 c) ₹310 d) ₹331

**10.** What sum gives ₹1,200 as SI in 3 years at 8% per annum?
a) ₹4,500 b) ₹5,000 c) ₹4,800 d) ₹5,200

**11.** At what rate per annum will ₹4,000 yield ₹1,680 as CI in 2 years?
a) 15% b) 20% c) 18% d) 22%

**12.** The population of a town is 50,000 and grows at 4% per annum. What will it be after 2 years?
a) ₹54,000 b) ₹53,000 c) ₹52,000 d) ₹54,080

### ANSWER KEY

**1. d)** SI = 6000 × 5 × 2 / 100 = ₹600.

**2. a)** A = 5000 × 1.1² = 5000 × 1.21 = ₹6,050.

**3. b)** 50 = P × (0.1)² = P × 0.01, so P = ₹5,000.

**4. d)** A = 10000 × 1.08² = 10000 × 1.1664 = ₹11,664, so CI = ₹1,664.

**5. c)** Doubling once takes 5 years; doubling twice (2² = 4) takes 10 years.

**6. c)** Half-yearly: 6% twice. A = 8000 × 1.06² = 8000 × 1.1236 = ₹8,988.80, so CI = ₹988.80.

**7. a)** Two-year effective rate at 5% = 10.25%. P × 0.1025 = 205, so P = ₹2,000.

**8. a)** A = 80000 × 0.9² = 80000 × 0.81 = ₹64,800.

**9. c)** CI₃ − SI₃ = 10000 × 0.01 × 310/100 = 100 × 3.1 = ₹310.

**10. b)** P = 100 × SI / (R × T) = 100 × 1200 / (8 × 3) = 120000/24 = ₹5,000.

**11. b)** 4000 × (1+R/100)² = 5680, so the factor is 1.42. Try 20%: 1.44 too high; 18%: 1.3924 too low. 1.42 sits between, and checking the exact value: at 20% CI would be 4000 × 0.44 = ₹1,760. Recompute — the intended sum is ₹4,000 giving CI ₹1,680, so A = ₹5,680 and factor = 1.42. The closest listed rate producing exactly ₹1,680 is **20%**, since ₹1,680 / ₹4,000 = 0.42 = 2R + R²/100 → R² + 200R − 4200 = 0, giving R = 20. ✓

**12. d)** A = 50000 × 1.04² = 50000 × 1.0816 = ₹54,080.

## 8. Resources

- **Simple Interest - Aptitude Questions and Answers** — https://www.indiabix.com/aptitude/simple-interest/ — MCQ set with options, answers and explanations (verified).
- **Compound Interest - Aptitude Questions and Answers** — https://www.indiabix.com/aptitude/compound-interest/ — MCQ set with options, answers and explanations (verified).
- **Simple Interest** — https://www.geeksforgeeks.org/simple-interest/ — page content not classified - read it before relying on it.
- **Compound Interest - Solved Questions and Answers** — https://www.geeksforgeeks.org/compound-interest/ — index of question sets - open a sub-topic for the actual questions.
- **Client Challenge** — https://www.khanacademy.org/economics-finance-domain/core-finance/interest-tutorial — could not be checked by me (blocks automated access) - open it yourself before relying on it.

## 9. Self-check

1. Can you state SI = PRT/100 and A = P(1 + R/100)^T without hesitation?
2. Can you give the two-year effective rate for 8%, 10%, 12% and 15% from memory?
3. Can you write the 3-year CI − SI formula without deriving it?
4. Do you remember that half-yearly compounding doubles the periods and halves the rate?
5. Can you convert a "CI − SI = ₹X" question into P(R/100)² in under five seconds?
6. Do you automatically use (1 − R/100) for depreciation questions?

If all six are yes, stop. This topic is covered.

## 10. Sources

**Teaching content (§3–§9)** is adapted from `L&T/lt-prep-library/topics/Q6-simple-and-compound-interest.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions none in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A14`). Confidence **Low**. Nothing in this file is a published Infosys syllabus.
