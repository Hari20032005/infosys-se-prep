# Quantitative – From Zero

*Adapted from `L&T/lt-prep-library/aptitude/00-QUANT-FROM-ZERO.md`; verified in that library's QA. §1 and §2 regenerated for Infosys; the source's crash plan is replaced by `../99-STUDY-PLAN.md`.*

## 1. What this section is

In the Infosys test this is **Technical Ability**, which means *mathematical* ability, not computer-science theory: 10 questions, 10 marks, **35 minutes** (the most generous timing on the paper, about 3.5 minutes a question), with its own cut-off. Reasoning topics and maths topics are prepared together as one 25-question aptitude block.

Conditions that shape every technique in this guide: **no calculator** (official guidelines), rough paper and stationery allowed, sections are timed and cannot be revisited once closed `[LIKELY]`, and no negative marking has been reported. Answer everything.

*The rest of this guide is adapted from `L&T/lt-prep-library/aptitude/00-QUANT-FROM-ZERO.md`; its method and speed techniques transfer, its counts and timings do not.*
## 2. The topic map

From `data/weightage.json`. Marks are expected marks on the Infosys test, not the source paper.

| Code | Topic | Est. marks | Hours | Tier | Conf. |
|---|---|---|---|---|---|
| A7 | Data interpretation: tables and charts | 2.3 | 1.0 | T1 | High |
| A8 | Linear equations: ages, heads-and-legs, two-variable systems | 1.8 | 0.7 | T1 | High |
| A9 | Averages, mixtures and alligation | 1.4 | 0.7 | T3 | Medium |
| A11 | Mensuration: area, surface area, volume | 1.2 | 0.7 | T3 | Medium |
| A18 | Permutations, combinations and probability | 0.8 | 1.2 | T4 | Medium |
| A10 | Number system: primes, divisibility, powers and roots | 0.7 | 0.8 | T4 | Medium |
| A12 | Percentages | 0.5 | 1.0 | T4 | Low |
| A13 | Profit, loss and discount | 0.5 | 0.8 | T4 | Low |
| A14 | Simple and compound interest | 0.5 | 0.7 | T4 | Low |
| A15 | Time, speed and distance | 0.5 | 1.0 | T4 | Low |
| A16 | Time and work | 0.5 | 0.8 | T4 | Low |
| A17 | Ratio and proportion | 0.5 | 0.6 | T4 | Low |
## 3. The order to learn them in

Learn cheap-and-frequent first. Every hour you spend on percentages pays back across profit & loss, SI/CI, DI and mixtures; every hour on clocks pays back once.

1. **Fractions ↔ percentages table and the percentage change rules.** Prerequisite for everything. Expect to know 1/8 = 12.5% instantly.
2. **Percentages, profit & loss, discount, successive change.** The largest single block of marks.
3. **Ratio, proportion, partnership, alligation.** Turns most mixture and ages questions into one line of cross-multiplication.
4. **Averages.** Feeds DI, ages, mixtures and even reasoning sets.
5. **SI and CI.** Two formulas, then variations. Cheap.
6. **Data interpretation.** Not a new topic — it is percentages, ratios and averages applied to a table. Do it early because the questions are easy per mark.
7. **Time & work, pipes & cisterns.** One idea: convert everything to work-per-day.
8. **Time, speed, distance, trains, boats.** Same idea, different units. Do the unit-conversion drill once and it becomes easy.
9. **Mensuration and geometry basics.** Formula recall, not reasoning. Circles, triangles, cylinders, cubes.
10. **Number system rules.** Divisibility tests, LCM/HCF, unit digit cycles, remainders.
11. **Algebra basics.** Linear and quadratic equations, inequalities, basic word problems.
12. **Progressions.** Two formulas.
13. **P&C and probability.** Do last among the medium topics; learn five formulas and how to apply them, not the theory.
14. **Logs, surds, indices.** Two rules each.
15. **Clocks, calendars, coordinate geometry.** Skip unless you have spare time.

The reasoning for this order: items 1–6 cover roughly **20 of the 30 marks** and take about 15 hours. Items 7–11 add another 6–7 marks for 12 hours. Items 12–15 are the expensive tail.

## 4. The core method for this section

**Two passes, with a hard 60-second abandon rule and a translation line before any calculation.**

Concretely, when the section starts:

- **Pass 1 (target: 20 minutes).** Read every question. Classify it in your head the moment you finish reading:
  - **S** — I can see the answer path in one step (roughly 40 seconds).
  - **M** — I know the method but it takes three or four lines (40–75 seconds).
  - **X** — I don't immediately see it, or it looks like two minutes of arithmetic.
  Do every S. Skip every M and X. Do not be tempted by an M question that "looks almost done".
- **Pass 2 (target: 20 minutes).** Return to the M questions and clear them.
- **Pass 3 (remaining ~15 minutes).** Attack X questions. On the first X that takes more than 60 seconds, abandon it and move to the next. At the very end, bubble a guess for every blank.

The **translation line** is the second half of the method and the part candidates skip. Before computing anything, write one line on your rough sheet: what is given, what is asked, in symbols. For example: *"CP = 400, SP = 460, ask profit%"*. This costs five seconds and prevents the single most common quant failure — correctly calculating a number that isn't the one being asked for. Under time pressure you will compute B's share when the question wants A's; the translation line catches it.

The reason the abandon rule works is the no-negative-marking structure. A question worth one mark that eats 150 seconds has cost you roughly three other questions. Abandoning is not giving up; it is budgeting.

## 5. Speed techniques

### 5.1 Quantitative

**Option elimination — rule out without calculating.** "A price is raised 25% and then cut 25%." Options: a) no change b) 6.25% decrease c) 6.25% increase d) 12.5% decrease. You never multiply 100 × 1.25 × 0.75. A rise followed by an equal fall always ends *below* the start, and only one option is a decrease. Answer in three seconds.

**Back-substitution.** "Which of 1, 2, 3, 4 satisfies x² − 5x + 6 = 0?" Put x = 2: 4 − 10 + 6 = 0. Done. Never factorise under a 55-second clock — test the middle option first, since options are usually ordered.

**Approximation, then pick the nearest option.** "61.8% of 419." Use 0.6 × 420 = 252. Options 218, 259, 275, 301 → 259. The gap between options tells you how much precision you need; if options are far apart, one rounded multiplication is enough.

**Unit conversion done once.** Write `1 km/h = 5/18 m/s` and `1 m/s = 18/5 km/h` at the top of your rough sheet in the first minute. Never re-derive it. 54 km/h = 54 × 5/18 = 15 m/s.

**Fraction–percentage equivalents.** Memorise: 1/2 = 50, 1/3 = 33.33, 1/4 = 25, 1/5 = 20, 1/6 = 16.67, 1/7 ≈ 14.29, 1/8 = 12.5, 1/9 = 11.11, 1/10 = 10, 1/11 = 9.09, 1/12 = 8.33, 1/15 = 6.67, 1/16 = 6.25, 1/20 = 5, 1/25 = 4. "12.5% of 640" becomes 640/8 = 80 instantly.

**Ratio-scaling chaining.** A:B = 3:4 and B:C = 6:5. Make B common: 9:12 and 12:10, so A:C = 9:10. One line, no algebra.

**Never solve for a variable you can cancel.** Work in ratios and fractions wherever possible; the question rarely needs absolute values.

### 5.2 Logical reasoning

**Grid building.** Draw the table or row *before* you engage with the clues, with the exact number of slots and the exact set of names. Half the set is solved by the act of drawing it.

**Most-constrained-clue-first.** Start with the clue that fixes the most, not the first clue printed. A clue of the form "Q is second from the left" pins a slot absolutely; an adjacency clue pins a pair. Example: five people P, Q, R, S, T in a row; Q is second from the left; R is immediately right of T; S is not at either end. Place Q first, then place the T–R block, then apply S — the arrangement falls out without a full grid.

**Set abandonment.** Puzzle sets come in groups of three or four questions on one arrangement. If the first question of a set takes more than 90 seconds, abandon the entire set and move on. Sets are all-or-nothing; a half-solved grid rarely yields a mark.

### 5.3 Verbal ability

**Questions before passage.** Read the question stems first — not the options. Two stems in, you know whether the passage is asking about the author's tone, a specific fact, or an inference, and you read accordingly. Reading the passage first means reading it twice.

**Error-hunting order.** Check in this fixed sequence and stop at the first hit: subject–verb agreement → tense consistency → pronoun reference → preposition/idiom → article → misplaced modifier → parallelism. Example: "Each of the students have submitted the report." Agreement first — "Each" is singular, so "has". You find it in two seconds without reading for style.

**Long passage skeleton.** Read the first and last sentence of each paragraph, then answer. For detail questions, go back to the line reference; do not rely on memory.

## 6. Twenty practice questions

**1.** If 40% of a number is 96, the number is:
a) 180 b) 220 c) 240 d) 280

**2.** ₹540 is divided between A and B in the ratio 4:5. A's share is:
a) ₹270 b) ₹300 c) ₹240 d) ₹216

**3.** The average of 5 numbers is 18. If the number 22 is removed, the new average is:
a) 17 b) 16 c) 17.5 d) 18

**4.** An article costing ₹400 is sold for ₹460. The profit percentage is:
a) 12% b) 13.5% c) 15% d) 16.5%

**5.** A can do a job in 12 days and B in 18 days. Working together, they finish it in:
a) 7⅕ days b) 7 days c) 7½ days d) 8 days

**6.** A car covers 150 km in 2 hours 30 minutes. Its speed is:
a) 60 km/h b) 55 km/h c) 65 km/h d) 50 km/h

**7.** Two successive discounts of 10% and 20% are equivalent to a single discount of:
a) 28% b) 30% c) 25% d) 32%

**8.** The simple interest on ₹5,000 at 8% per annum for 3 years is:
a) ₹1,000 b) ₹1,200 c) ₹1,100 d) ₹1,400

**9.** In what ratio must rice at ₹40/kg be mixed with rice at ₹52/kg so that the mixture costs ₹46/kg?
a) 2:1 b) 1:1 c) 1:2 d) 3:2

**10.** The average age of 20 students is 15. When the teacher's age is included, the average becomes 16. The teacher's age is:
a) 36 b) 34 c) 38 d) 40

**11.** The area of a circle of radius 7 cm is (take π = 22/7):
a) 44 cm² b) 49 cm² c) 77 cm² d) 154 cm²

**12.** The compound interest on ₹10,000 at 10% per annum for 2 years is:
a) ₹2,000 b) ₹2,050 c) ₹2,200 d) ₹2,100

**13.** Two dice are thrown. The probability that the sum is 9 is:
a) 1/6 b) 1/12 c) 1/9 d) 5/36

**14.** In how many ways can 2 students be selected from 6?
a) 12 b) 36 c) 30 d) 15

**15.** Pipe A fills a tank in 6 hours and pipe B in 12 hours. Together they fill it in:
a) 5 hours b) 4.5 hours c) 4 hours d) 3 hours

**16.** The largest 4-digit number divisible by 8 is:
a) 9996 b) 9992 c) 9984 d) 9988

**17.** The 20th term of the arithmetic progression 5, 9, 13, … is:
a) 79 b) 77 c) 85 d) 81

**18.** A man walking at 5 km/h reaches his office 10 minutes late; at 6 km/h he reaches 5 minutes early. The distance to his office is:
a) 5 km b) 6 km c) 7 km d) 7.5 km

**19.** The angles of a triangle are in the ratio 2:3:4. The largest angle is:
a) 60° b) 80° c) 70° d) 90°

**20.** A shopkeeper marks his goods 40% above cost and gives a 25% discount. His profit percentage is:
a) 4% b) 5% c) 10% d) 15%

### ANSWER KEY

1. **c)** 96 ÷ 0.4 = 240.
2. **c)** A's share = (4/9) × 540 = ₹240.
3. **a)** Sum = 5 × 18 = 90; (90 − 22) ÷ 4 = 17.
4. **c)** Profit = 60 on 400 = 15%.
5. **a)** LCM method: 36 units in 36 days at 3 + 2 = 5 units/day → 36/5 = 7⅕ days.
6. **a)** 2 h 30 min = 2.5 h; 150 ÷ 2.5 = 60 km/h.
7. **a)** Net = 10 + 20 − (10 × 20)/100 = 28%.
8. **b)** SI = (5000 × 8 × 3)/100 = ₹1,200.
9. **b)** Alligation: (52 − 46) : (46 − 40) = 6 : 6 = 1:1.
10. **a)** 21 × 16 = 336; 336 − 300 = 36.
11. **d)** (22/7) × 7 × 7 = 154 cm².
12. **d)** 10,000 × 1.1² = 12,100; CI = ₹2,100.
13. **c)** 4 favourable outcomes (3+6, 4+5, 5+4, 6+3) out of 36 = 1/9.
14. **d)** 6C2 = (6 × 5)/2 = 15.
15. **c)** 1/6 + 1/12 = 1/4, so 4 hours.
16. **b)** 10,000 is divisible by 8, so subtract 8 → 9,992.
17. **d)** a + 19d = 5 + 19 × 4 = 81.
18. **d)** Time gap = 15 min = ¼ h; d/5 − d/6 = ¼ → d/30 = ¼ → d = 7.5 km.
19. **b)** (4/9) × 180 = 80°.
20. **b)** Take cost = 100, MP = 140, SP = 140 × 0.75 = 105 → 5% profit.
