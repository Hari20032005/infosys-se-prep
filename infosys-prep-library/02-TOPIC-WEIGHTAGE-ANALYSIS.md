# 02 — Topic Weightage Analysis

How the 75 scored marks are expected to fall across subtopics, and what to study first. Every number is generated from `data/weightage.json` (itself produced by `data/analyze.py` from the observed questions and accounts); the full method and the ROI table are in `data/analysis-tables.md`. **Treat this as a study-priority guide, not a syllabus**: the 2027-batch test has not been reported by anyone yet, and the per-section counts rest on one first-hand account plus coaching sources that may share a source.

## 1. The paper this library plans for

| # | Section | Questions | Marks | Minutes |
|---|---|---|---|---|
| 1 | Reasoning Ability | 15 | 15 | 25 |
| 2 | Technical Ability (mathematical) | 10 | 10 | 35 |
| 3 | Verbal Ability | 20 | 20 | 20 |
| 4 | Pseudocode | 5 | 10 | 10 |
| 5 | Numerical Puzzle | 4 | 10 | 10 |
| 6 | English Grammar | 5 | 10 | 10 |
| 7 | English Writing | 1 | unpublished | 10 |
| | **Total** | **60** | **75 + essay** | **120** |

Every section has its own cut-off (value unknown). No coding. No calculator. No negative marking reported. Source and confidence: `research/03-pattern-synthesis.md` §1–§2 (Medium).

## 2. Tiers

Tiers compare each subtopic's expected marks per study hour with this paper's own average (1.84). Because every section has a cut-off, the best-value topics in each section are lifted to at least Tier 2 (the *section floor*). Low-confidence topics are capped at Tier 3 before the floor.

### Tier 1 — 15 subtopics · 50.0 expected marks · 14.2 hours

| Code | Subtopic | Section | Marks | Hours | Confidence | File and bank |
|---|---|---|---|---|---|---|
| W1 | English writing: essay and email | English Writing | gate | 1.0 | Medium | [W1](topics/W1-english-writing.md) · [bank](question-banks/QB-W1-writing-prompts.md) |
| G1 | Cloze and fill-in-the-blanks | English Grammar | 5.8 | 0.8 | Medium | [G1](topics/G1-fill-in-the-blanks-and-cloze.md) |
| Z2 | Pair and figure rules | Numerical Puzzle | 5.7 | 1.2 | High | [Z2](puzzles/Z2-pair-and-figure-rules.md) · [bank](question-banks/QB-Z2-pair-and-figure-rules.md) |
| V2 | Spotting errors and grammar rules | Verbal Ability | 5.3 | 1.2 | High | [V2](topics/V2-spotting-errors-and-grammar-rules.md) · [bank](question-banks/QB-V2-identify-the-correct-sentence.md) |
| V1 | Reading comprehension | Verbal Ability | 5.1 | 1.2 | Medium | [V1](topics/V1-reading-comprehension.md) |
| Z1 | Number grids and matrices | Numerical Puzzle | 4.3 | 1.2 | High | [Z1](puzzles/Z1-number-grids-and-matrices.md) · [bank](question-banks/QB-Z1-number-grids-and-matrices.md) |
| G2 | Tense, articles, prepositions and voice | English Grammar | 4.2 | 0.7 | Medium | [G2](topics/G2-grammar-tense-articles-prepositions.md) · [bank](question-banks/QB-G2-cloze-passages.md) |
| V3 | Sentence correction and completion | Verbal Ability | 3.2 | 1.0 | Medium | [V3](topics/V3-sentence-correction.md) |
| V6 | Critical reasoning | Verbal Ability | 3.0 | 0.6 | Medium | [V6](topics/V6-critical-reasoning.md) · [bank](question-banks/QB-V6-critical-reasoning.md) |
| A2 | Number and letter series | Reasoning Ability | 2.8 | 1.0 | High | [A2](topics/A2-number-and-letter-series.md) · [bank](question-banks/QB-A2-number-and-letter-series.md) |
| P1 | Loops and trace tables | Pseudocode | 2.7 | 1.0 | High | [P1](pseudocode/P1-loops-iteration.md) · [bank](question-banks/QB-P1-infosys-dialect-traces.md) · [bank](question-banks/QB-P1-loops-iteration.md) |
| A7 | Data interpretation: tables and charts | Technical Ability | 2.3 | 1.0 | High | [A7](topics/A7-data-interpretation.md) · [bank](question-banks/QB-A7-data-interpretation.md) |
| A1 | Coding and decoding | Reasoning Ability | 2.1 | 0.8 | High | [A1](topics/A1-coding-and-decoding.md) · [bank](question-banks/QB-A1-coding-decoding.md) |
| A6 | Data sufficiency | Reasoning Ability | 1.9 | 0.8 | High | [A6](topics/A6-data-sufficiency.md) · [bank](question-banks/QB-A6-data-sufficiency-1234.md) |
| A8 | Linear equations: ages, heads-and-legs, two-variable systems | Technical Ability | 1.8 | 0.7 | High | [A8](topics/A8-linear-equations-and-ages.md) · [bank](question-banks/QB-A8-linear-equations-and-ages.md) |

### Tier 2 — 7 subtopics · 8.5 expected marks · 4.5 hours

| Code | Subtopic | Section | Marks | Hours | Confidence | File and bank |
|---|---|---|---|---|---|---|
| A4 | Syllogisms and logical deduction | Reasoning Ability | 1.6 | 0.8 | High | [A4](topics/A4-syllogisms-and-logical-deduction.md) · [bank](question-banks/QB-A4-ordered-deduction.md) |
| P5 | Arrays | Pseudocode | 1.4 | 0.8 | Medium | [P5](pseudocode/P5-arrays.md) · [bank](question-banks/QB-P5-arrays.md) |
| A3 | Operator logic and equation balancing | Reasoning Ability | 1.2 | 0.6 | High | [A3](topics/A3-operator-logic.md) · [bank](question-banks/QB-A3-operator-logic.md) |
| A5 | Blood relations | Reasoning Ability | 1.2 | 0.5 | Medium | [A5](topics/A5-blood-relations.md) · [bank](question-banks/QB-A5-blood-relations.md) |
| P3 | Bitwise operators and precedence | Pseudocode | 1.1 | 0.8 | Medium | [P3](pseudocode/P3-bitwise-operators.md) · [bank](question-banks/QB-P3-bitwise-operators.md) |
| A21 | Non-verbal reasoning | Reasoning Ability | 1.1 | 0.4 | Medium | [A21](topics/A21-non-verbal-reasoning.md) · [bank](question-banks/QB-A21-non-verbal-reasoning.md) |
| P4 | Pre/post-increment and fill-the-blank | Pseudocode | 1.0 | 0.6 | Medium | [P4](pseudocode/P4-increment-operators-and-dialect.md) · [bank](question-banks/QB-P4-increment-operators-and-dialect.md) |

### Tier 3 — 5 subtopics · 6.8 expected marks · 3.6 hours

| Code | Subtopic | Section | Marks | Hours | Confidence | File and bank |
|---|---|---|---|---|---|---|
| V4 | Synonyms, antonyms and vocabulary | Verbal Ability | 1.8 | 1.0 | Low | [V4](topics/V4-synonyms-antonyms-and-vocabulary.md) |
| V5 | Para-jumbles | Verbal Ability | 1.8 | 0.6 | Low | [V5](topics/V5-para-jumbles.md) · [bank](question-banks/QB-V5-para-jumbles.md) |
| A9 | Averages, mixtures and alligation | Technical Ability | 1.4 | 0.7 | Medium | [A9](topics/A9-averages-mixtures-and-alligation.md) · [bank](question-banks/QB-A9-replacement-mixtures.md) |
| A11 | Mensuration: area, surface area, volume | Technical Ability | 1.2 | 0.7 | Medium | [A11](topics/A11-mensuration.md) · [bank](question-banks/QB-A11-mensuration.md) |
| P6 | Conditionals and nested if | Pseudocode | 0.8 | 0.6 | Medium | [P6](pseudocode/P6-conditionals-nested-if.md) · [bank](question-banks/QB-P6-conditionals-nested-if.md) |

### Tier 4 — 15 subtopics · 9.7 expected marks · 12.3 hours

| Code | Subtopic | Section | Marks | Hours | Confidence | File and bank |
|---|---|---|---|---|---|---|
| A19 | Logic puzzle sets: seating, conditional rules, direction sense | Reasoning Ability | 1.2 | 1.2 | Medium | [A19](topics/A19-seating-and-analytical-puzzle-sets.md) · [bank](question-banks/QB-A19-if-then-rules.md) |
| P2 | Recursion | Pseudocode | 0.9 | 1.0 | Medium | [P2](pseudocode/P2-recursion.md) · [bank](question-banks/QB-P2-recursion.md) |
| A18 | Permutations, combinations and probability | Technical Ability | 0.8 | 1.2 | Medium | [A18](topics/A18-permutations-combinations-probability.md) · [bank](question-banks/QB-A18-permutations-combinations-probability.md) |
| A10 | Number system: primes, divisibility, powers and roots | Technical Ability | 0.7 | 0.8 | Medium | [A10](topics/A10-number-system.md) · [bank](question-banks/QB-A10-number-system.md) |
| A20 | Cryptarithmetic | Reasoning Ability | 0.7 | 0.6 | Medium | [A20](topics/A20-cryptarithmetic.md) · [bank](question-banks/QB-A20-cryptarithmetic.md) |
| P7 | Functions and scope | Pseudocode | 0.7 | 0.6 | Medium | [P7](pseudocode/P7-functions-scope.md) · [bank](question-banks/QB-P7-functions-scope.md) |
| A12 | Percentages | Technical Ability | 0.5 | 1.0 | Low | [A12](topics/A12-percentages.md) |
| A13 | Profit, loss and discount | Technical Ability | 0.5 | 0.8 | Low | [A13](topics/A13-profit-loss-and-discount.md) |
| A14 | Simple and compound interest | Technical Ability | 0.5 | 0.7 | Low | [A14](topics/A14-simple-and-compound-interest.md) |
| A15 | Time, speed and distance | Technical Ability | 0.5 | 1.0 | Low | [A15](topics/A15-time-speed-distance.md) |
| A16 | Time and work | Technical Ability | 0.5 | 0.8 | Low | [A16](topics/A16-time-and-work.md) · [bank](question-banks/QB-A16-time-and-work.md) |
| A17 | Ratio and proportion | Technical Ability | 0.5 | 0.6 | Low | [A17](topics/A17-ratio-and-proportion.md) |
| P8 | Complexity, sorting and searching | Pseudocode | 0.5 | 0.8 | Low | [P8](pseudocode/P8-snippet-complexity.md) · [bank](question-banks/QB-P8-snippet-complexity.md) |
| P9 | OOP in pseudocode: inheritance and overriding | Pseudocode | 0.5 | 0.6 | Low | [P9](pseudocode/P9-oop-in-pseudocode.md) · [bank](question-banks/QB-P9-oop-in-pseudocode.md) |
| P10 | Strings and ASCII | Pseudocode | 0.5 | 0.6 | Low | [P10](pseudocode/P10-strings-ascii.md) · [bank](question-banks/QB-P10-strings-ascii.md) |

### Interview stage

| Code | Theme | Questions seen | Accounts | Tier | Hours | File |
|---|---|---|---|---|---|---|
| IV1 | SDLC, Agile and Scrum | 7 | 4 | T1 | 1.0 | [IV1](interview/IV1-sdlc-agile-testing.md) · [bank](question-banks/QB-IV1-sdlc-agile-testing.md) |
| IV2 | OOP and Java basics | 4 | 3 | T1 | 1.0 | [IV2](interview/IV2-oop-four-pillars.md) · [bank](question-banks/QB-IV2-oop-four-pillars.md) |
| IV3 | DBMS and SQL | 1 | 1 | T3 | 1.0 | [IV3](interview/IV3-dbms-sql.md) · [bank](question-banks/QB-IV3-dbms-sql.md) |
| IV4 | Projects and resume | 2 | 2 | T2 | 1.0 | [IV4](interview/IV4-projects-and-resume.md) |
| IV5 | HR and behavioural | 8 | 3 | T1 | 1.5 | [IV5](interview/IV5-hr-and-behavioural.md) |
| IV6 | Generative AI and everyday AI use | 2 | 1 | T3 | 0.5 | [IV6](interview/IV6-generative-ai.md) |
| IV7 | Light coding in Java | 1 | 1 | T3 | 0.7 | [IV7](interview/IV7-light-coding-in-java.md) |

**Full coverage costs 34.6 hours for the test and 6.7 for the interview.** `99-STUDY-PLAN.md` says what to drop when you have less.

## 3. Where the evidence is thin

- **13 of 42 subtopics have no observed question**; their share is an allocation from syllabus lists. Verbal and Grammar (30 of 75 marks) rest on one observed item.
- The observed pool is 60 questions from coaching videos and one first-hand account. Each is `[REPORTED]` at best.
- Repeat rate: 3 of 60 questions (5.0%) were presented independently by two channels. Repeats across test slots cannot be measured, so there is no Infosys equivalent of the Accenture repeat figure.
- Coding is not in the Systems Engineer test (eight sources). It appears only in the optional upgrade test, which this library does not cover.
- The Numerical Puzzle section in 2025–26 is grid-number reasoning; the classic brain-teaser collections that circulate under “Infosys puzzles” describe an older test and were deliberately not used.

## 4. How this was produced

`data/analyze.py` reads `questions-observed.csv`, `questions-discarded.csv`, `reviews-online.csv` and `syllabus-claims.csv`; weights sightings by `sqrt` so one heavily-filmed topic cannot swamp the rest; runs ROI on expected **marks** (three sections carry two marks a question); and checks that sections reconcile to 60 questions and 75 marks. Change `SECTIONS` there to test another structure and rerun.
