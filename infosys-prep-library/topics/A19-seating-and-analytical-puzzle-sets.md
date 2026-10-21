---
title: Analytical puzzle SETS on shared premises
code: A19
section: Reasoning Ability
weightage_pct: 1.6% of marks
est_questions: 1.19
tier: 4
difficulty: Medium
est_study_hours: 1.2
confidence: Medium
last_updated: 2026-09-30
adapted_from: L&T/lt-prep-library/topics/L1-analytical-puzzle-sets-on-shared-premises.md
---
<!-- Drafted by DeepSeek V4.1 Flash via ds.py; reviewed by Claude 2026-09-21. Answer
     letters rebalanced by data/shuffle.py (correctness-preserving: option text is
     swapped and the key letter repointed). Numeric keys re-checked by
     data/verify_keys.py. -->

# A19 — Analytical puzzle SETS on shared premises

*Adapted from `L&T/lt-prep-library/topics/L1-analytical-puzzle-sets-on-shared-premises.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **1.2 questions and 1.2 marks** on this topic (about 1.6% of the 75 scored marks). It sits in **Reasoning Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 4**, 1.2 hours to reach reliable recall, confidence **Medium**.

**10 questions on this topic are in the observed Infosys pool** (O01, O02, O03, O04, O05, O21, O22, O23, O24, O25), from 1 source. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.79 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| O01 | 2020-09-22 | Thief, three computers, three tools: which tool was used on Tejas? |
| O02 | 2020-09-22 | Same set: in which month was the keyboard taken? |
| O03 | 2020-09-22 | Same set: which peripheral did Prithvi lose? |
| O04 | 2020-09-22 | Same set: in which month was the wire cutter used? (fill in) |
| O05 | 2020-09-22 | Same set: which computer lost its monitor? |
| O21 | 2020-09-22 | Wedding guests with if-then rules: if Qhorin comes, who must stay away? |
| O22 | 2020-09-22 | If Ramsay does not come, what must be true? |
| O23 | 2020-09-22 | If Umar comes, which statement must NOT be true? |
| O24 | 2020-09-22 | Which listed group could be exactly the attendees? |
| O25 | 2020-09-22 | Who can attend regardless of who else attends? |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



A setup paragraph of 2-5 sentences, then a cluster of questions on it. Because there is no negative marking, the correct play is: if the setup cracks in under 90 seconds, answer the whole cluster; if it does not, abandon the whole cluster and move on. Half-solving one question inside a set is the worst possible outcome.

| Sub-pattern | How it appears | Roughly how often |
|---|---|---|
| Linear seating (row, facing north/south) | 5-8 people, 4-6 clues, 3 questions | Common |
| Circular seating (facing centre / outside) | 6-8 people, 5 clues, 2-3 questions | Common |
| Floor / building puzzle | 5-7 floors, people or flats | Common |
| Categorisation grid | 4 people x 2-3 attributes, match them | Occasional |
| Conditional chain | "If funded then audited", test what follows | Occasional |
| Selection / group formation | Pick a committee under constraints | Rare |

## 3. Concept notes

### 3.1 Reading a setup once — the grid method

Draw, do not hold it in your head. Allocate a fixed strip of paper or the margin.

- **Linear**: draw `1 2 3 4 5 6 7` and mark left/right arrows with the facing direction.
- **Circular**: draw a circle, mark 6 or 8 seats, number them clockwise.
- **Floors**: draw a vertical stack, floor 1 at the bottom (**always** — floor 1 is the ground floor).
- **Grids**: draw rows = people, columns = attributes.

Then process clues in **descending order of restrictiveness**: absolute positions first ("T is second from the right"), then adjacency, then relative-distance clues, and finally negative clues ("R is not adjacent to S") as the last filter.

### 3.2 Linear seating — the facing rule

Left and right are from the **person's own point of view**, not yours.

- Facing **north** (towards the top of the page): their left = your left.
- Facing **south** (towards the bottom): their left = your right. Mirror everything.

"**Third to the left of X**" = three seats away, with exactly two people in between. "**Immediately left of X**" = the seat directly adjacent. These are different and the paper exploits the difference deliberately.

If a row says "some face north, some face south", only adjacency and "second to the left" clues survive — solve adjacency first.

### 3.3 Circular seating — the one rule that decides everything

Standing in a circle:

| Arrangement | Their right is | Their left is |
|---|---|---|
| Facing the **centre** | **Anticlockwise** | **Clockwise** |
| Facing **outside** | **Clockwise** | **Anticlockwise** |

Everything else follows. **Opposite** seat in a circle of n people = n/2 seats away (only defined when n is even). In a circle of 8, seat 1 is opposite seat 5. In a circle of 6, seat 1 is opposite seat 4.

Number of ways to seat n distinct people in a circle = **(n − 1)!**. In a row it is **n!**.

### 3.4 Floor puzzles

Floor 1 is the lowest. "A lives immediately above B" → A's floor = B's floor + 1. "A lives two floors above B" → A = B + 2, with exactly one floor between. "A lives above B" means only A > B, distance unknown — this is the weakest clue, save it for last. Draw the stack vertically before you place anything.

### 3.5 Categorisation grids

Attribute-matching: n people, n values for each attribute, all distinct. Build a matrix and tick/cross. The engine is the **negative clue**: once "Amit has a cat" is fixed, every other person gets a cross in the cat column. Two attributes filled in = the third is forced by elimination.

### 3.6 Conditional chains

Learn the two legal moves:

- **If A then B** ⟺ **If not B then not A** (contrapositive). *"If it is funded it is audited"* ⟺ *"If it is not audited it is not funded."* These are the same statement.
- **If A then B** does **not** give "if B then A". *"Funded → audited"* says nothing about unaudited items being unfunded items' business.

The word **"some"** means **at least one, possibly all**. "Some X are Y" and "Some Y are X" are the same statement. "Some X are Y" never lets you conclude "some X are not Y" unless it is stated.

### 3.7 Quick counting

| Situation | Count |
|---|---|
| n people in a row | **n!** |
| n people in a circle | **(n − 1)!** |
| n people in a circle, clockwise/anticlockwise considered the same | **(n − 1)! / 2** |
| Choosing r from n, order irrelevant | **nCr = n! / (r!(n − r)!)** |
| Choosing r from n, order matters | **nPr = n! / (n − r)!** |

Memorise: 4! = 24, 5! = 120, 6! = 720, 7! = 5040, 8! = 40320.

## 4. Must-memorise block

- **Facing centre: right = anticlockwise. Facing outside: right = clockwise.**
- **Floor 1 is the bottom floor.**
- **"Third to the left" = 3 seats away. "Immediately left" = 1 seat away.**
- **Left/right are from the subject's viewpoint, never yours.**
- **Contrapositive: "If A then B" ⟺ "If not B then not A".**
- **"Some" = at least one. Never implies "some are not".**
- **Circular arrangements: (n − 1)!. Linear: n!.**
- **Opposite seat in an even circle: n/2 seats away.**
- **Clue priority: absolute position → adjacency → relative distance → negatives.**
- **Abandon rule: no crack in 90 s ⇒ skip the entire set.**

## 5. Worked examples

### Example 1 — Linear row

Seven students P, Q, R, S, T, U, V sit in a row facing north. V is fourth to the left of T. T is second from the right end. R is adjacent to T. Q is exactly in the middle. S is immediately to the right of Q. P is at the extreme left. Who is third to the left of T?

Seats 1-7, left to right.
- T second from the right → **T = 6**.
- V fourth to the left of T → V = 6 − 4 = **2**.
- Q in the middle → **Q = 4**.
- S immediately right of Q → **S = 5**.
- R adjacent to T → seat 5 or 7; 5 is taken → **R = 7**.
- P at extreme left → **P = 1**. Remaining **U = 3**.

Row: P V U Q S T R. Third to the left of T (seat 6) → seat 3 → **U**.

*Slow method:* case-splitting on every possible seat for R. It burns 3 minutes and cannot be done at this pace.

### Example 2 — Circular seating

Six people A, B, C, D, E, F sit around a circle facing the centre. D is at seat 1. A is second to the right of D. B is immediately left of A. C is opposite D. E and F occupy the remaining two seats. Who is second to the left of C?

Number seats 1-6 clockwise. Facing centre ⇒ **right = anticlockwise, left = clockwise**.
- D = 1.
- A is second to the right of D → two seats anticlockwise → 6, then 5 → **A = 5**.
- B is immediately left of A → left = clockwise → next clockwise from 5 is 6 → **B = 6**.
- C opposite D → 1 + 3 → **C = 4**.
- E, F fill seats 2 and 3 (adjacent, so both clues satisfied).

Second to the left of C (seat 4): left = clockwise → 5, then 6 → **B**.

### Example 3 — Floors

Five floors, 1 (bottom) to 5 (top), occupied by A, B, C, D, E. D lives on floor 2. C lives on the top floor. B lives below D. E lives immediately above A. Who lives on floor 4?

- **C = 5**, **D = 2**.
- B below D → B = **1**.
- Floors 3 and 4 remain for A and E, and E is immediately above A → **A = 3, E = 4**.

Answer: **E**.

### Example 4 — Categorisation grid

Three friends X, Y, Z have distinct professions (doctor, engineer, lawyer) and distinct cities (Delhi, Chennai, Kolkata). X is not the doctor. The engineer is from Kolkata. Y is from Chennai. Z is the doctor. Who is the engineer?

- Z = doctor. So X and Y are engineer/lawyer.
- Y is from Chennai; the engineer is from Kolkata → Y ≠ engineer → **Y = lawyer**, and **X = engineer**.
- Then X is from Kolkata; Y from Chennai; **Z from Delhi**.

Answer: **X**.

### Example 5 — Conditional chain

Premises: All Z are Y. All Y are X. Some X are W.
Which conclusion definitely follows? (i) All Z are X. (ii) Some Z are W.

Chain: Z → Y → X, so **all Z are X** follows (statement i). The "some X are W" set may sit entirely outside Z, so statement ii does **not** follow.

Answer: **only i follows**.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Reading "left" as your left | In a row facing south, or a circle facing outside, it is mirrored | Check facing direction before writing any left/right |
| Confusing "second to the left" with "immediately left" | Both sound like "next to" | Second = 2 seats, immediately = 1 seat |
| Starting with "A is above B" | Weakest clue, gives no distance | Do absolute positions and adjacency first |
| Assuming floor 5 is the ground floor | Leftover habit from "top floor" phrasing | Floor 1 is always the bottom |
| "Some X are Y" ⇒ "some X are not Y" | Feels natural | "Some" = at least one; no negative is implied |
| Reversing a conditional | "If A then B" ≠ "if B then A" | Only the contrapositive is valid |
| Rebuilding the setup per question | The set is meant to be solved once | Fix the arrangement on paper, answer all questions off it |
| Sunk cost on a broken set | You have already spent 4 minutes | Decide at 90 s: crack it or leave all of it |

## 7. Practice questions

**Questions 1-3.** Six friends A, B, C, D, E, F sit in a row facing north. A sits third to the left of D. B sits at the extreme right end. E sits second to the left of B. C sits immediately to the right of A.

1. Who sits at the extreme left end?
   a) A  b) F  c) B  d) E

2. Who sits immediately to the left of D?
   a) C b) F c) A d) E

3. How many people sit between A and E?
   a) Three b) Two c) None d) One

**Questions 4-6.** In a six-storey building, floors 1 (bottom) to 6 (top) are occupied by A, B, C, D, E, F, one per floor. D lives on floor 3. F lives on the top floor. B lives immediately above E. C lives on floor 1.

4. Who lives on floor 2?
   a) B b) E c) C d) A

5. How many floors are there between D and F?
   a) Two b) Four c) Three d) One

6. Which of these pairs occupies two consecutive floors, in that order from bottom to top?
   a) E and B b) D and E c) C and A d) A and D

**Questions 7-9.** Four friends — Amit, Bela, Chetan, Divya — each have a different pet (cat, dog, fish, parrot) and live in a different city (Delhi, Mumbai, Pune, Kochi). Amit has a cat. Chetan has a parrot and is not from Kochi. Bela is from Mumbai and has a dog. Divya is from Pune.

7. Who is from Kochi?
   a) Amit b) Bela c) Chetan d) Divya

8. Which pet does Divya have?
   a) Cat b) Fish c) Dog d) Parrot

9. Which city-pet pair is correct?
   a) Kochi-parrot b) Mumbai-dog c) Delhi-fish d) Pune-cat

**Questions 10-12.** Premises: Every project that is funded must be audited. Every audited project is reviewed. Some reviewed projects fail.

10. Which of the following must be true?
    a) No audited project fails b) Some funded projects fail c) Every funded project is reviewed d) Every reviewed project is funded

11. If a project is not reviewed, then:
    a) It is not funded b) It is not audited c) Both of the above d) It may still be funded

12. The statement "Some reviewed projects fail" guarantees that:
    a) All reviewed projects fail b) No funded project fails c) At least one reviewed project fails d) Every funded project fails

### ANSWER KEY

1. **b)** The row resolves to F A C E D B; A is third to the left of D only if A = 2, D = 5, giving F at seat 1.
2. **d)** D is at seat 5 and E at seat 4, so E is immediately to D's left.
3. **d)** A is at seat 2 and E at seat 4, with only C at seat 3 between them.
4. **d)** B immediately above E with floors 2, 4, 5 free forces E = 4, B = 5, leaving A = 2.
5. **a)** D is on floor 3 and F on floor 6, so floors 4 and 5 lie between them.
6. **a)** E is on floor 4 and B on floor 5, consecutive and in that order.
7. **a)** Chetan is not from Kochi and Bela is Mumbai, Divya is Pune, so Kochi must be Amit's.
8. **b)** Cat, parrot and dog are taken by Amit, Chetan and Bela, leaving fish for Divya.
9. **b)** By elimination Amit is Kochi-cat, Chetan Delhi-parrot, Divya Pune-fish, Bela Mumbai-dog.
10. **c)** Funded → audited → reviewed is a valid chain; the "some fail" set need not contain a funded project.
11. **c)** Not reviewed → not audited (contrapositive), and not audited → not funded (contrapositive), so both hold.
12. **c)** "Some" means at least one; nothing stronger is implied.

## 8. Resources

- **Seating Arrangement - Verbal Reasoning Questions and Answers** — https://www.indiabix.com/verbal-reasoning/seating-arrangement/ — MCQ set with options, answers and explanations (verified).
- **Logical Deduction - Logical Reasoning Questions and Answers** — https://www.indiabix.com/logical-reasoning/logical-deduction/ — MCQ set with options, answers and explanations (verified).
- **Puzzles** — https://www.geeksforgeeks.org/puzzles/ — page content not classified - read it before relying on it.
- **Syllogism - Wikipedia** — https://en.wikipedia.org/wiki/Syllogism — reference article.

## 9. Self-check

1. Can you state, without hesitating, which way a person's right points when they face the centre of a circle?
2. Can you convert "if audited then reviewed" into its contrapositive in under five seconds?
3. Do you write the number strip or floor stack on paper before reading the clues?
4. Do you process clues in the order absolute → adjacency → distance → negative?
5. Have you practised abandoning a set at 90 seconds without finishing it?
6. Can you quote (n − 1)! for circular seating and n! for a row without deriving it?

If all six are "yes", stop revising this topic.

## 10. Sources

**Teaching content (§3–§9)** is adapted from `L&T/lt-prep-library/topics/L1-analytical-puzzle-sets-on-shared-premises.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions O01, O02, O03, O04, O05, O21, O22, O23, O24, O25 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A19`). Confidence **Medium**. Nothing in this file is a published Infosys syllabus.
