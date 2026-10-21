---
title: Number and letter series
code: A2
section: Reasoning Ability
weightage_pct: 3.7% of marks
est_questions: 2.75
tier: 1
difficulty: Easy
est_study_hours: 1.0
confidence: High
last_updated: 2026-09-30
adapted_from: L&T/lt-prep-library/topics/L3-number-and-letter-series.md
---
<!-- Drafted by DeepSeek V4.1 Flash via ds.py; reviewed by Claude 2026-09-21. Answer
     letters rebalanced by data/shuffle.py (correctness-preserving: option text is
     swapped and the key letter repointed). Numeric keys re-checked by
     data/verify_keys.py. -->

# A2 — Number and letter series

*Adapted from `L&T/lt-prep-library/topics/L3-number-and-letter-series.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **2.8 questions and 2.8 marks** on this topic (about 3.7% of the 75 scored marks). It sits in **Reasoning Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 1**, 1.0 hours to reach reliable recall, confidence **High**.

**11 questions on this topic are in the observed Infosys pool** (R02, R03, R07, R08, R11, R16, R17, R18, R19, R20, O19), from 4 sources. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 2.75 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| O19 | 2020-09-22 | Missing term in 0, 2, 5, 10, 17, _, 41 |
| R02 | 2026-09-22 | Find the missing term: 3, 14, 39, 84, 155, ?, 399 |
| R03 | 2026-09-22 | Find the next term: H47F, I48G, K50I, ? |
| R07 | 2025-09-29 | Find the next term: 0, 1, 2, 6, 16, 44, 120, ? |
| R08 | 2025-09-29 | Find the next term: 144, 441, 169, 961, 196, ? |
| R11 | 2025-09-29 | Find the next term: 3Y6, 8W8, 15U10, 24S12, 35Q14, ? |
| R16 | 2025-10-09 | Find the next term: 13, 17, 19, 23, 29, ? |
| R17 | 2024-11-04 | Replace ?: 1D, ?, 5H, 7J, 9L |
| R18 | 2024-11-04 | Replace ?: 12M, ?, 14Q, 15S |
| R19 | 2024-11-04 | Find the next term: 100, 20, 80, 50, 60, 80, ? |
| R20 | 2025-09-25 | Find the missing term: 91, 94, 100, 109, ?, 136 |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



| Sub-pattern | How it appears | Roughly how often |
|---|---|---|
| Number series, constant difference | 4, 9, 14, 19, __ | Most common single form |
| Number series, growing difference | 2, 6, 12, 20, __ | Very common |
| Number series, multiply / divide ratio | 3, 6, 12, 24, __ | Common |
| Multiply-then-add mixed rule | 5, 11, 23, 47, __ | Common |
| Square / cube / prime base | 1, 4, 9, 16, __ | Common |
| Interleaved two-series | odd and even positions follow different rules | Occasional |
| Letter series, forward shift | B, E, H, K, __ | Common |
| Letter pair series, opposed shift | AZ, BY, CX, __ | Occasional |
| Alphanumeric mixed series | A1, C3, E5, __ | Occasional |
| Wrong-term identification | one term of a series is incorrect | Occasional |
| Missing middle term | blank sits in the middle, not the end | Occasional |

## 3. Concept notes

### 3.1 Letter position values

Every letter has a fixed position 1-26 from the front and 1-26 from the back.

**A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8, I=9, J=10, K=11, L=12, M=13, N=14, O=15, P=16, Q=17, R=18, S=19, T=20, U=21, V=22, W=23, X=24, Y=25, Z=26.**

Position from the back = **27 minus position from the front**. Example: C is 3rd from the front and 27-3 = 24th from the back.

Do not count on your fingers. Anchor with **EJOTY: E=5, J=10, O=15, T=20, Y=25**. Example: to find R, go back two from T=20, so R=18.

### 3.2 The first-difference method

Write the gaps between consecutive terms. If the gaps are constant, the series is arithmetic. Example: 7, 11, 15, 19 has gaps 4, 4, 4.

If gaps are not constant, write the gaps of the gaps (the second difference). A constant second difference means a quadratic series. Example: 2, 5, 10, 17 has first gaps 3, 5, 7 and second gaps 2, 2.

The next term is always the last term plus the next gap. Example: 2, 5, 10, 17, __ → next gap 9 → 26.

### 3.3 Alternating and second-order differences

When gaps alternate in sign or size, read odd gaps and even gaps separately. Example: 10, 20, 15, 30, 25 has gaps +10, -5, +15, -5 → next is +20 → 45.

### 3.4 Multiply, divide, and mixed rules

Test each term against the one before it:

- Constant ratio: term × k. Example: 5, 15, 45, 135 (k = 3).
- Multiply then add a counter: term × 2 + 1, then × 2 + 2, then × 2 + 3. Example: 3, 7, 16, 35 (3×2+1=7, 7×2+2=16, 16×2+3=35).
- Multiply then subtract a constant: term × 2 − 1. Example: 4, 7, 13, 25.
- Divide then add: term ÷ 2 + 1. Example: 64, 33, 17.5 — rare, exam series usually stay integral.

### 3.5 Square, cube, prime and Fibonacci bases

| Base | Series | Rule |
|---|---|---|
| Squares | 1, 4, 9, 16, 25 | n² |
| Squares ±1 | 2, 5, 10, 17, 26 | n² + 1 |
| Squares ±k | 3, 8, 15, 24, 35 | n² − 1 |
| Cubes | 1, 8, 27, 64, 125 | n³ |
| Primes | 2, 3, 5, 7, 11, 13 | primes only |
| Fibonacci | 1, 1, 2, 3, 5, 8, 13 | term = sum of previous two |
| Product form | 2, 6, 12, 20, 30 | n(n+1) |

Recognise n(n+1) instantly: 2, 6, 12, 20, 30, 42 is the sequence of products of consecutive integers. It is the same as 1×2, 2×3, 3×4, 4×5, 5×6, 6×7.

### 3.6 Interleaved series

Long series with 7 or more terms are often two series shuffled together. Split into positions 1, 3, 5, 7 and positions 2, 4, 6, 8 and solve each separately. Example: 3, 100, 6, 90, 12, 80, 24 → odd positions double (3, 6, 12, 24), even positions drop by 10 (100, 90, 80).

### 3.7 Letter series rules

Apply the same difference method to letter positions. Example: B(2), E(5), H(8), K(11) has gap +3 each time, so the next is N(14).

For letter pairs, treat each letter as its own series. Example: AZ, BY, CX, DW → first letters A, B, C, D advance by +1; second letters Z, Y, X, W retreat by −1. Next is EV.

For a pair moving in opposite directions, note that the two positions always add to 27. Example: A+Z = 1+26 = 27, B+Y = 2+25 = 27. This is a fast cross-check.

### 3.8 Wrong-term identification

Find the rule using the first four terms, then test every later term. The first term that breaks the rule is the answer. Do not hunt for a rule that fits all seven terms — in a wrong-term question no such rule exists by construction.

### 3.9 The 30-second decision tree

1. Write first differences. Constant? Answer.
2. Not constant — write second differences. Constant? Answer.
3. Ratio between consecutive terms roughly constant? Answer by multiplication.
4. Ratio near 2 with a small offset? Test ×2 ± 1, ×2 ± 2, ×2 ± 3.
5. Terms look like 1, 4, 9, 16 or 1, 8, 27, 64? Answer by square or cube.
6. More than 7 terms? Split odd and even positions.
7. Letters? Convert to numbers first, then run steps 1-6.

## 4. Must-memorise block

**Reverse position rule: front position + back position = 27.**

**EJOTY anchors: E=5, J=10, O=15, T=20, Y=25.**

**Mid-alphabet anchor: M=13, N=14.**

| Squares 1-15 | 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225 |
|---|---|
| **Cubes 1-10** | **1, 8, 27, 64, 125, 216, 343, 512, 729, 1000** |
| **Primes below 50** | **2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47** |
| **Fibonacci** | **1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144** |
| **n(n+1) series** | **2, 6, 12, 20, 30, 42, 56, 72, 90, 110** |
| **n²+1 series** | **2, 5, 10, 17, 26, 37, 50, 65** |
| **n²−1 series** | **0, 3, 8, 15, 24, 35, 48, 63** |

Fast arithmetic pairings used in wrong-term questions: ×2+1 (3→7→15→31→63), ×2−1 (4→7→13→25→49→97), ×3+1 (2→7→22→67).

## 5. Worked examples

**Example 1.** Find the next term: 2, 6, 12, 20, 30, __

First differences: 4, 6, 8, 10. These rise by 2 each time, so the next difference is 12. 30 + 12 = **42**. Cross-check: the terms are n(n+1), and 6×7 = 42. The slow method — testing a quadratic formula by hand — costs 40 seconds and gains nothing.

**Example 2.** Find the next term: 5, 11, 23, 47, 95, __

Each term is roughly double the previous. Test ×2+1: 5×2+1 = 11, 11×2+1 = 23, 23×2+1 = 47, 47×2+1 = 95. Rule confirmed. 95×2+1 = **191**. The slow method of computing differences (6, 12, 24, 48) works too, but you then need a second step to see the doubling; the ratio test answers in one line.

**Example 3.** Find the next term: AZ, BY, CX, DW, __

Split the pair. First letters: A(1), B(2), C(3), D(4) → +1 → E(5). Second letters: Z(26), Y(25), X(24), W(23) → −1 → V(22). Check: 5 + 22 = 27, the reverse-pair rule holds. Answer **EV**.

**Example 4.** Find the next term: 3, 7, 16, 35, 74, __

Ratio is just over 2. Test ×2+k with k rising: 3×2+1 = 7, 7×2+2 = 16, 16×2+3 = 35, 35×2+4 = 74. Rule confirmed. 74×2+5 = **153**. The difference method gives 4, 9, 19, 39 which is not obviously patterned — ratio-first is strictly faster here.

**Example 5.** Find the wrong term: 5, 8, 13, 20, 31, 40

Differences: 3, 5, 7, 11, 9. The first three gaps rise by 2 (3, 5, 7), so the pattern is odd numbers 3, 5, 7, 9, 11. The fourth gap should be 9, giving 20 + 9 = 29, not 31. Then 29 + 11 = 40 matches the given last term. The wrong term is **31**.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Stopping at the first difference | A series with gaps 4, 6, 8 looks irregular until you see the gaps rise by 2 | Always compute the second difference before giving up on a series |
| Assuming doubling when the rule is ×2+k | 5, 11, 23, 47 looks like pure doubling at a glance | Compute ×2+k for the actual first term and check k against later terms |
| Counting letters on fingers | Costs 20-30 seconds per question and introduces off-by-one errors | Use EJOTY anchors and add or subtract from them |
| Forgetting the reverse alphabet | A series running Z, X, V, T looks negative when it is just −2 | Convert to numbers immediately; Z=26, so Z, X, V, T is 26, 24, 22, 20 |
| Ignoring interleaving on long series | Seven-term series are usually two series, not one complex rule | Split odd and even positions when the term count is 7 or more |
| In wrong-term questions, hunting for a rule that fits everything | No such rule exists; the question is built so one term breaks it | Derive the rule from the first four terms only, then test forward |
| Treating a missing middle term as a missing last term | 2, 5, __, 17, 26 needs the gap pattern, and the gaps are 3, 5, 7, 9 | Write all known gaps first, then fill the blank |
| Assuming a series must use one operation throughout | Mixed rules like ×2+1 then +3 then ×2+1 are standard | Test the operation pair, not a single operation |

## 7. Practice questions

**1.** Find the next term: 4, 9, 14, 19, 24, __
a) 27 b) 28 c) 30 d) 29

**2.** Find the next term: 3, 6, 12, 24, 48, __
a) 72 b) 96 c) 108 d) 84

**3.** Find the next term: B, E, H, K, __
a) M b) O c) N d) L

**4.** Find the next term: 1, 4, 9, 16, 25, __
a) 30 b) 36 c) 49 d) 42

**5.** Find the next term: 2, 3, 5, 7, 11, __
a) 15 b) 12 c) 13 d) 17

**6.** Find the next term: 7, 14, 28, 56, __
a) 84 b) 98 c) 120 d) 112

**7.** Find the next term: AZ, CX, EV, GT, __
a) HS b) IQ c) JR d) IR

**8.** Find the next term: 2, 5, 10, 17, 26, __
a) 35 b) 36 c) 37 d) 39

**9.** Find the next term: 4, 7, 13, 25, 49, __
a) 95 b) 97 c) 96 d) 99

**10.** Find the next term: 1, 8, 27, 64, __
a) 125 b) 100 c) 121 d) 144

**11.** Find the next term: 6, 11, 21, 41, 81, __
a) 161 b) 162 c) 160 d) 151

**12.** Find the wrong term: 2, 6, 12, 20, 30, 42, 58
a) 58 b) 42 c) 30 d) 20

### ANSWER KEY

1. **d** — Constant difference of 5: 24 + 5 = 29.
2. **b** — Constant ratio ×2: 48 × 2 = 96.
3. **c** — Positions 2, 5, 8, 11 rise by 3, so the next is 14 = N.
4. **b** — Consecutive squares: 1² to 5², next is 6² = 36.
5. **c** — Consecutive primes: 2, 3, 5, 7, 11, next is 13.
6. **d** — Constant ratio ×2: 56 × 2 = 112.
7. **d** — First letters A, C, E, G advance by 2 → I(9); second letters Z, X, V, T retreat by 2 → R(18); 9 + 18 = 27 confirms the pairing, so IR.
8. **c** — Terms are n² + 1: 1+1, 4+1, 9+1, 16+1, 25+1, next is 36+1 = 37.
9. **b** — Rule ×2 − 1 throughout: 4→7, 7→13, 13→25, 25→49, next 49×2−1 = 97.
10. **a** — Consecutive cubes: 1³, 2³, 3³, 4³, next is 5³ = 125.
11. **a** — Rule ×2 − 1 throughout: 6→11, 11→21, 21→41, 41→81, next 81×2−1 = 161.
12. **a** — Terms are n(n+1): 1×2, 2×3, 3×4, 4×5, 5×6, 6×7 = 42, 7×8 = 56, so 58 is wrong and should be 56.

## 8. Resources

- **Number Series - Logical Reasoning Questions and Answers** — https://www.indiabix.com/logical-reasoning/number-series/ — MCQ set with options, answers and explanations (verified).
- **Letter and Symbol Series - Logical Reasoning Questions and Answers** — https://www.indiabix.com/logical-reasoning/letter-and-symbol-series/ — MCQ set with options, answers and explanations (verified).
- **Aptitude Questions and Answers** — https://www.geeksforgeeks.org/quantitative-aptitude/ — index of question sets - open a sub-topic for the actual questions.
- **Aptitude Questions and Answers** — https://www.geeksforgeeks.org/quantitative-aptitude/ — index of question sets - open a sub-topic for the actual questions.
- **Fibonacci sequence - Wikipedia** — https://en.wikipedia.org/wiki/Fibonacci_sequence — reference article.

## 9. Self-check

1. Can you state the position of any letter A-Z without counting from A?
2. Can you give the back-alphabet position of any letter using the 27-minus rule in under two seconds?
3. Can you write the squares 1-15 and cubes 1-10 from memory without hesitating?
4. Do you write second differences automatically when first differences are irregular?
5. Do you split any series with 7 or more terms into odd and even positions before trying anything else?
6. In a wrong-term question, do you derive the rule from the first four terms only and then test forward?

If all six are yes, stop studying this topic.

## 10. Sources

**Teaching content (§3–§9)** is adapted from `L&T/lt-prep-library/topics/L3-number-and-letter-series.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions R02, R03, R07, R08, R11, R16, R17, R18, R19, R20, O19 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A2`). Confidence **High**. Nothing in this file is a published Infosys syllabus.
