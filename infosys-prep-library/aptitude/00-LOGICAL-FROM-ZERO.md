# Logical-and-Analytical-Reasoning — From Zero

*Adapted from `L&T/lt-prep-library/aptitude/00-LOGICAL-FROM-ZERO.md`; verified in that library's QA. §1 and §2 regenerated for Infosys; the source's crash plan is replaced by `../99-STUDY-PLAN.md`.*

## 1. What this section is

In the Infosys test this is **Reasoning Ability**: 15 questions, 15 marks, 25 minutes (about 100 seconds a question), with its own cut-off. The 2025 pattern deck lists data sufficiency, data interpretation and syllogisms here; coaches add coding-decoding, series and blood relations. Sources disagree on which topics sit in Reasoning and which in Technical Ability, so this library prepares both as one 25-question aptitude block.

Conditions that shape every technique in this guide: **no calculator** (official guidelines), rough paper and stationery allowed, sections are timed and cannot be revisited once closed `[LIKELY]`, and no negative marking has been reported. Answer everything.

*The rest of this guide is adapted from `L&T/lt-prep-library/aptitude/00-LOGICAL-FROM-ZERO.md`; its method and speed techniques transfer, its counts and timings do not.*
## 2. The topic map

From `data/weightage.json`. Marks are expected marks on the Infosys test, not the source paper.

| Code | Topic | Est. marks | Hours | Tier | Conf. |
|---|---|---|---|---|---|
| A2 | Number and letter series | 2.8 | 1.0 | T1 | High |
| A1 | Coding and decoding | 2.1 | 0.8 | T1 | High |
| A6 | Data sufficiency | 1.9 | 0.8 | T1 | High |
| A4 | Syllogisms and logical deduction | 1.6 | 0.8 | T2 | High |
| A3 | Operator logic and equation balancing | 1.2 | 0.6 | T2 | High |
| A19 | Logic puzzle sets: seating, conditional rules, direction sense | 1.2 | 1.2 | T4 | Medium |
| A5 | Blood relations | 1.2 | 0.5 | T2 | Medium |
| A21 | Non-verbal reasoning | 1.1 | 0.4 | T2 | Medium |
| A20 | Cryptarithmetic | 0.7 | 0.6 | T4 | Medium |
## 3. The order to learn them in

1. **Number & letter series.** Cheap, self-contained, teaches pattern-scanning in 20 seconds flat. Three marks for five hours.
2. **Percentages, profit & loss, SI/CI.** Everything downstream — DI, ratio, approximation — leans on this. Learn the fraction–percentage table cold before moving on.
3. **Ratio, proportion, averages, mixtures.** Same mental machinery, one level up. Averages carry a two-line trick that answers questions instantly.
4. **Verbal: error spotting and sentence completion.** Purely rule-based, no calculation, and reliably 3 marks. Do this early so it is banked.
5. **Coding–decoding.** Two formulas (letter shift, reverse alphabet) cover nearly every question ever set.
6. **Blood relations & direction sense.** Draw the diagram once, read the answer off it. Very high certainty per minute invested.
7. **Syllogisms.** Venn circles, three marks, and a hard rule about what "some" can and cannot imply.
8. **Time–speed–distance, time & work.** The arithmetic here is real work; learn it after percentages so unit conversions and fractions are automatic.
9. **Data interpretation & approximation.** Only worth learning once you can do percentages and ratios in your head.
10. **Seating arrangement & puzzles.** The single biggest hours sink. Deliberately late, so if you run out of time you drop it, not percentages.
11. **Permutation, probability, counting.** Medium-hard, two marks, decent return only at the end.
12. **Clocks & calendars.** One mark, three hours. Do it last, or skip it entirely if the clock is ticking.

The logic of this order: **cheap high-yield first, hours-hungry puzzles last.** A topic you can finish in three hours should never be sitting behind a topic that takes ten.

## 4. The core method for this section

The single most important habit: **run two passes with a 45-second tripwire, and never leave a blank.**

Concretely:

- **First pass.** Read the question. If you can see the path to the answer, take it and cap yourself at 45 seconds. If you reach 45 seconds without a clear finish line, stop mid-calculation, mark the question on your rough sheet, and move on. Do not "just finish this one." The paper punishes that.
- **Finish pass.** Come back to marked questions only if time remains. Anything still unsolved — and every unanswered question in the section — gets a **filled bubble**. No negative marking means the blank is strictly worse than any guess. If you can eliminate even one option, guess from the remaining three.

Pair this with **archetype recognition**. Around 80% of this section's questions are one of about fifteen recurring archetypes: "net change after +x% and −y%", "train crossing a pole", "how many between A and B", "all A are B, some B are C", "coding by letter shift". The first three seconds should be spent naming the archetype, not solving. Naming it correctly means you already know the formula or the diagram.

## 5. Speed techniques

**Quantitative.**

*Fraction–percentage equivalents.* Memorise: 1/8 = 12.5%, 3/8 = 37.5%, 1/6 = 16.67%, 5/6 = 83.33%, 1/16 = 6.25%, 1/12 = 8.33%, 1/7 = 14.28%. They convert divisions into multiplications.
*Example:* "A shop marks up 37.5% and offers 20% discount. Net result?" — 37.5% = 3/8, so selling price = 11/8 × 0.8 = 11/8 × 4/5 = 44/40 = 1.10 → **10% profit**, in five seconds.

*Unit conversion done once.* Convert km/h to m/s by multiplying by 5/18, and write the converted number down. Never re-convert mid-calculation.
*Example:* 54 km/h → 54 × 5/18 = 15 m/s. A 180 m train crosses a pole in 180/15 = **12 seconds**.

*Back-substitution.* When the question asks for a value and the options are plain numbers, plug them in.
*Example:* "x + 1/x = 10/3." Try 3: 3 + 1/3 = 10/3. **Done** — no quadratic, no formula.

*Option elimination by magnitude.* Work out the rough size before the exact value.
*Example:* "Average of 20 numbers is 35. The number 45 is replaced by 60. New average?" The change is +15 spread over 20 numbers = +0.75, so the answer must be 35.75 — eliminate 36, 37.5, 35.0 immediately.

*Approximation.* Round to friendly numbers, then check the options are far enough apart.
*Example:* 48.7% of 812. Half of 812 is 406; 48.7% is slightly less → about **395**. If options are 312, 355, 395, 445, that is enough.

**Logical.**

*Grid building.* For any arrangement question, draw the skeleton (slots, rows, or a 2×N table) before reading the clues twice. The grid does the remembering so your head does not have to.

*Most-constrained-clue-first.* Read all clues, then start with the one that pins something to a fixed position — "A is at the extreme left", "C sits third from the right" — never with the loosest one.

*Set abandonment.* If a 3-mark puzzle has not cracked after 90 seconds of grid work, leave it. Three marks are not worth four minutes, and the puzzle is deliberately engineered to be a time trap.

*Example (blood relations):* "She is the daughter of my grandfather's only son." Grandfather's only son = my father. My father's daughter = my sister. One line, ten seconds.

*Example (direction):* 5 km north, turn right 3 km, turn right 5 km. Net displacement = 3 km east. Draw the L-path — the two north-south legs cancel.

**Verbal.**

*Questions before passage.* Read the question stems first, then scan the passage. You will spot the relevant sentence on the first read instead of the third.

*Error-hunting order.* Check in this fixed sequence: **(1) subject–verb agreement, (2) tense consistency, (3) preposition/article, (4) pronoun agreement.** Most errors in this exam are category 1 or 2.
*Example:* "One of my friend is a doctor." — "One of" takes a plural noun → **"One of my friends is a doctor."**

## 6. Twenty practice questions

**1.** A number is increased by 25% and then decreased by 20%. The net change is:
a) 5% increase b) 5% decrease c) No change d) 10% decrease

**2.** The average of five consecutive odd numbers is 21. The largest of them is:
a) 25 b) 27 c) 23 d) 29

**3.** ₹1350 is divided between A and B in the ratio 4:5. A's share is:
a) ₹750 b) ₹600 c) ₹540 d) ₹650

**4.** A train 180 m long running at 54 km/h crosses a pole in:
a) 10 s b) 12 s c) 18 s d) 14 s

**5.** Find the next term: 2, 6, 12, 20, 30, ?
a) 40 b) 38 c) 44 d) 42

**6.** If FRIEND is coded as 6-18-9-5-14-4, then CANDLE is coded as:
a) 3-1-14-4-11-5 b) 3-1-13-4-12-5 c) 3-1-14-4-12-5 d) 4-1-14-4-12-5

**7.** What is the angle between the hands of a clock at 3:40?
a) 120° b) 140° c) 130° d) 125°

**8.** Pointing to a photograph, a man says, "She is the daughter of my grandfather's only son." How is she related to him?
a) Mother b) Cousin c) Niece d) Sister

**9.** A man walks 5 km north, turns right and walks 3 km, then turns right and walks 5 km. How far is he from the starting point, and in which direction?
a) 3 km west b) 5 km east c) 3 km east d) 8 km north

**10.** A bag contains 4 red and 6 green balls. Two balls are drawn at random without replacement. The probability that both are red is:
a) 1/5 b) 2/15 c) 4/25 d) 2/9

**11.** A sum of money doubles in 8 years at simple interest. In how many years will it triple?
a) 12 b) 20 c) 24 d) 16

**12.** P, Q, R, S and T sit in a row facing north. P is at the extreme left, R at the extreme right, and Q is second from the left. T is not adjacent to R. Who sits in the middle?
a) T b) Q c) P d) S

**13.** 37% of 842 is approximately:
a) 312  b) 282  c) 342  d) 372

**14.** 8 : 512 :: 6 : ?
a) 196 b) 256 c) 236 d) 216

**15.** Statements: All roses are flowers. All flowers are plants. Some plants are trees.
Conclusions: I. All roses are plants. II. Some trees are flowers.
a) Only II follows  b) Neither follows  c) Both follow  d) Only I follows

**16.** Find the next term: 3, 8, 15, 24, 35, ?
a) 48 b) 47 c) 46 d) 49

**17.** A can finish a job in 12 days and B in 18 days. Working together, they finish it in:
a) 7.2 days b) 7 days c) 7.5 days d) 8 days

**18.** Choose the grammatically correct sentence:
a) One of my friend are a doctor.
b) One of my friends is a doctor.
c) One of my friends are a doctor.
d) One of my friend is doctor.

**19.** How many three-digit numbers can be formed from the digits 1, 2, 3, 4 without repeating any digit?
a) 12 b) 16 c) 24 d) 64

**20.** In a row of 40 students, A is 12th from the left and B is 15th from the right. How many students sit between A and B?
a) 12 b) 13 c) 14 d) 15

### ANSWER KEY

1. **c** — 1.25 × 0.80 = 1.00, so there is no net change.
2. **a** — The middle (third) number is 21, so the largest is 21 + 4 = 25.
3. **b** — 1350 × 4/9 = ₹600.
4. **b** — 54 km/h = 15 m/s; 180 ÷ 15 = 12 seconds.
5. **d** — Differences are 4, 6, 8, 10; the next difference is 12, giving 42.
6. **c** — Each letter is replaced by its alphabet position: C=3, A=1, N=14, D=4, L=12, E=5.
7. **c** — Minute hand 240°, hour hand 110°; difference = 130°.
8. **d** — Grandfather's only son is his father; his father's daughter is his sister.
9. **c** — The two north-south legs cancel, leaving a net 3 km east.
10. **b** — (4/10) × (3/9) = 12/90 = 2/15.
11. **d** — Doubling in 8 years means 12.5% per year; tripling needs 200% interest = 16 years.
12. **a** — Order is P, Q, T, S, R; T occupies the middle position.
13. **a** — 0.37 × 842 = 311.5 ≈ 312.
14. **d** — 8³ = 512, so 6³ = 216.
15. **d** — "All roses are plants" follows; trees need not be flowers, so II does not.
16. **a** — Terms are n² − 1: 2²−1 up to 6²−1; the next is 7² − 1 = 48.
17. **a** — Combined rate = 1/12 + 1/18 = 5/36, so time = 36/5 = 7.2 days.
18. **b** — "One of" takes a plural noun, so "One of my friends is a doctor."
19. **c** — 4 × 3 × 2 = 24 arrangements.
20. **b** — B is 26th from the left; students between = 26 − 12 − 1 = 13.
