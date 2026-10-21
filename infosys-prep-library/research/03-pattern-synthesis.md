# 03 — Pattern Synthesis

**As of 2026-09-25, updated 2026-10-01** with Infosys's own 2020 sample paper (A7) and one 2026-batch account (B7); see `research/05-source-credibility.md` for why each source was or was not used. Built from `research/02-online-research-log.md`, `data/reviews-online.csv` (20 accounts), `data/questions-observed.csv` (63 exam rows, 25 interview rows) and the 54 solved sample items in `data/official_sample.py`.

**Recency rule applied.** Anything that only appears in pre-2024 material is treated as a hypothesis, not a fact. The planning model below rests on accounts of tests sat between Nov 2024 and Dec 2025. **No first-hand account of the 2027-batch (2026-27) test exists yet.** The coaching videos from 15–20 Sep 2026 relay the 2027 notice but describe the pattern "as of the last exam, October 2025".

---

## 1. The planning model

| # | Section | Questions | Marks | Minutes | Tag |
|---|---|---|---|---|---|
| 1 | Reasoning Ability | 15 | 15 | 25 | `[LIKELY]` |
| 2 | Technical Ability (= mathematical ability, **not** CS theory) | 10 | 10 | 35 | `[LIKELY]` |
| 3 | Verbal Ability | 20 | 20 | 20 | `[LIKELY]` |
| 4 | Pseudocode | 5 | **10** (2 each) | 10 | `[CONFIRMED — official 2020 sample]` for the 2 marks each; `[LIKELY]` for the section itself |
| 5 | Numerical Puzzle | 4 | **10** (2 × 2 + 2 × 3) | 10 | `[CONFIRMED — official 2020 sample]` for 3, 2, 2, 3 marks; `[LIKELY]` for the section itself |
| 6 | English Grammar (cloze-based) | 5 | **10** | 10 | `[LIKELY]` |
| 7 | English Writing (essay or email) | 1 | not stated | 10 | `[LIKELY]` |
| | **Total** | **60** | **75 + essay** | **120** | |

**Why [LIKELY] and not [CONFIRMED].** Seven sections and 120 minutes are confirmed by four first-hand accounts (B1, B2, B4, B5). The **per-section counts** come from one first-hand account (B1, on-campus test of 12 May 2025) plus two 2025 pattern decks (C1, C2) and three coaching videos (V1, V2, V5) that agree exactly. The decks and videos may share an upstream source, so they are not treated as three more independent confirmations. Confidence in any number derived from this table is **capped at Medium**, the same cap the L&T build used for its single-source split.

**What the official sample (A7) settles, and what it does not.** It is Infosys's own paper, so the *style* of every section is `[CONFIRMED — official 2020 sample]`: the pseudocode dialect, the 2-mark pseudocode items, the 3 / 2 / 2 / 3 puzzle marks, the data-sufficiency 1-2-3-4 scale, the deductive-reasoning format, and the fact that the Technical Ability section mixes maths with a logic puzzle set. It has **five** sections, 54 questions and 100 minutes, so it does **not** confirm the seven-section 2025-26 layout; it predates the Grammar and Writing sections. Its mark values for Reasoning, Technical and Verbal are stated as "one mark each" in its own header.

**Marks weighting matters more than question count.** Pseudocode, Puzzle and Grammar carry 2 marks a question. Their 14 questions are worth 30 of 75 marks.

## 2. Mechanics

| Item | Finding | Tag | Sources |
|---|---|---|---|
| Venue | Computer labs on the college campus | `[CONFIRMED]` | A1, A2 (official guidelines), B2, B3 |
| Platform | `rec-test.infosys.com`, Chrome/Edge | `[CONFIRMED — official]` | A1, A2 |
| Proctoring | In person, for the whole test; switching windows is auto-tracked | `[CONFIRMED — official]` | A1, A2 |
| Calculator | **Not allowed** | `[CONFIRMED — official]` | A1, A2 |
| Rough work | "You may keep stationery items with you" | `[CONFIRMED — official]` | A1, A2 |
| Login | Must start within **15 minutes** of slot time or lose the test | `[CONFIRMED — official]` | A1, A2 |
| ID | Original **college ID and government photo ID**, carried for the whole process | `[CONFIRMED — official]` | A1 |
| Negative marking | **None reported** by any source; one first-hand account states none | `[LIKELY]` | B5, C-series |
| Sectional cut-off | **Yes, every section** | `[CONFIRMED]` | B2, B5, V1, V2, V3 |
| Cut-off value | **Not discoverable as of 2026-09-25.** Claims of 75% (B5) and ~70% (V1) are unsourced | — | — |
| Section timers | Each section has its own timer and closes on expiry | `[LIKELY]` | B1, V4 (conflict: B5) |
| Navigation | Sequential; no return to a previous section; skipped questions cannot be reopened | `[LIKELY]` | B1, V4 (conflict: B5) |
| Coding | **None** in the SE test | `[CONFIRMED]` | B1, B2, B3, B4, B5, V1, V2, V5 |
| Pass rate | "only 5% of people cleared the assessment" at one campus | `[REPORTED]` | B2 |

## 3. Section content (from the observed questions)

| Section | What recurs | Evidence |
|---|---|---|
| Reasoning | Coding-decoding (letter sums, position rules, swaps, reverse + shift), number and alphanumeric series, operator-logic puzzles (`264 * 2 = 6`), syllogisms, blood relations with symbols, data sufficiency. **Official sample:** one 5-question logic set (a thief, three computers, tools and months), 5 data-sufficiency items on a 1-2-3-4 scale, 5 deductive-reasoning items | 20 observed items; A7 (15 items) |
| Technical Ability | Arithmetic: ages/ratio, averages, linear equations (heads-and-legs), number properties, mensuration, **data interpretation** ("Infosys favourite" — three coaches say DI appears in every paper). **Official sample:** cryptarithmetic, onto-assignment counting, arrangements with constraints, a prime-gap series, mixture replacement, **plus a 5-question if-then attendance puzzle** (half the section) | 8 observed items + C1 syllabus; A7 (10 items) |
| Verbal | Error spotting, sentence correction, reading comprehension, para-jumbles, synonyms/antonyms. **Official sample:** 3 critical-reasoning items (strengthen, weaken, inference), 4 "English Corrective Usage" fill-in-the-blank items, 4 "English Error Correction" items (best phrasing of an underlined part), 4 "English Error Identification" items (identify the correct sentence), one 5-question reading passage | 1 observed item; C1 and V1 syllabus; A7 (20 items) |
| Pseudocode | Loop traces, `mod` and integer division, recursion (power, factorial, accumulating arguments), bitwise precedence, do-while termination, **pre/post-increment fill-the-blank**, array passes. **Official dialect:** numbered lines, `Integer a, b`, `Set a = 6, b = 3`, `For (each i from 1 to 5)` … `End-for`, `If (…) then` … `Else` … `End-if`, `While(b)`, `a MOD b`, `Integer func(Integer a, Integer b)` … `End-function` | 15 observed items; A7 (5 items) |
| Numerical Puzzle | **Number grids and figures with a hidden arithmetic rule**: 3×3 and 4×4 matrices, pairs mapping to a value, outer numbers to a centre. Two items worth 2 marks, two worth 3. **Official sample:** two 3×3 grids whose row sums continue a series; a plus-shaped figure whose centre is twice the sum of the arms; circles with cubes feeding a box (a³ + b³ + a + b); zig-zag rows of digit sums of the neighbours above | 15 observed items; V3 "three cross three … four cross four matrix puzzles"; A7 (4 items) |
| English Grammar | Cloze passage, 5 blanks: tense, articles, prepositions, parts of speech | C1 ("Close Test based"), V1 |
| English Writing | One essay or formal email on a general topic in ~10 minutes; ~190–200 words targeted | B1 ("Write an essay on Ozone layer depletion"), V1, V2 |

**Puzzle type — decisive for reuse.** The 2025-26 Numerical Puzzle section is grid-number reasoning. It is **not** the classic Infosys brain-teaser (escalators, weighings, river crossings) that fills pre-2020 "Infosys puzzle" collections. The conditional source `tcs_new/_analysis/text2/TCS_TCS_ninja_450_Infosys_Puzzles.pdf.txt` is exactly that older type, so **it was not used**.

## 4. The behavioural component (thread D)

| Reading | Evidence | Verdict |
|---|---|---|
| A separate behavioural/psychometric test | None. No 2024-26 SE account mentions one | Not supported |
| "Behavioral guidelines" in the official test instructions | A1/A2: dress code, no earphones, no communication — **conduct rules**, not an assessment | This is what the phrase means in the 2026-batch documents |
| Behaviour assessed in the interview | B2 (handling rejection, time management), B5 (stress, relocation, GenAI opinion, daily AI use), A2 ("in-person interview … technical skills and behavioural competencies" for SP) | **Most likely.** `[INFERRED]` |

**Resolved as far as evidence allows:** prepare behavioural answers for the interview. Whether the 2027 drive adds a separate behavioural instrument is **unresolved**; the drive email's phrase "technical and behavioural competencies" is compatible with either.

**"AI-driven vision" in practice.** One first-hand 2025 interview asked for an opinion on generative AI and how the candidate uses AI day to day (B5). That is the only concrete trace. `[REPORTED]`

## 5. Upgrade path (thread E) — exists

| Item | Finding | Tag |
|---|---|---|
| Upgrade route | SE candidates who clear the test **and** interview can sit an optional extra programming test + in-person interview for **DSE (Rs 6.25 LPA)** or **SP (Rs 9.5 LPA)**. "This is optional and will have no impact on their initial offer." | `[CONFIRMED]` — A3 (official KIIT notice, Sep 2025), B1, B5 |
| Upgrade test format | Programming test, 3 questions, 180 minutes (the SP/DSE format) | `[LIKELY]` — A2, A4, DSE Jun 2025 account |
| Upgrade interview | Includes a live coding task (45 min, 2 medium-hard problems, solve one) plus Java/OOP/DBMS/SQL | `[REPORTED]` — DSE Jun 2025 account |
| 2027 upgrade pay | Direct 2027 SP drives list L1 Rs 10 L + 1 L bonus, L2 16 L, L3 21 L, DSE 6.25 L + 75k bonus. **Whether SE-upgrade SP maps to L1 in 2027 is not discoverable** | `[REPORTED]` |

## 6. Interview (thread F)

Format: face to face, on campus, **15–40 minutes**, usually the day after the test or a few weeks later. Technical and HR are often one conversation. `[CONFIRMED]` (B1–B5)

| Theme | Observed questions |
|---|---|
| SDLC and process | SDLC and why it is needed; SDLC models; Waterfall vs Agile; Scrum Master; sprint planning — **asked in 4 of 5 accounts** |
| OOP / Java | Four pillars; overloading vs overriding; Java access specifiers; Java or Python and why |
| DBMS/SQL | Joins and their types |
| Coding (light) | Palindrome program |
| Projects | Final-year / capstone project in detail |
| HR / behavioural | Why Infosys; rejections; time management; stress; relocation; job vs higher studies; CGPA decline; extracurriculars; GenAI opinion; daily AI use |

**Documents:** college ID and government ID are mandatory throughout (official). Certificates were reviewed at the end of one interview (B6, stale source).

## 7. Infosys-specific terms (verify, do not assert)

| Item | What the evidence says | Tag |
|---|---|---|
| Training | Residential foundation programme at the Global Education Centre, Mysuru; length varies by stream (reported 12–23 weeks) | `[LIKELY]` — Infosys careers page, Hechinger Report |
| Joining location | A July 2025 SE Trainee offer letter gives **Mysore** as the location of employment on joining | `[REPORTED]` (one letter) |
| Probation | **18 months** training/probation from joining, in that letter | `[REPORTED]` |
| Early-exit clause | Compensation of **Rs 1,00,000** if leaving before completing probation, in that letter. Older letters describe a "Service Agreement" of 12 months from Practice Unit allocation | `[REPORTED]` |
| Pay during training | Rs 25,000/month gross in the first six months, in that letter | `[REPORTED]` |
| Relocation | "Candidate should be willing to relocate to any location as required by Infosys" | `[CONFIRMED — official eligibility]` |

## 8. Conflict table

| Question | Source A says | Source B says | Believed | Why |
|---|---|---|---|---|
| Number of sections / duration | 5 sections, 54 Q, 100 min (**A7, Infosys's own 2020 sample**; C3, 2021; many SEO pages) | 7 sections, 60 Q, 120 min (B1, C1, C2, V1) | **7 / 60 / 120** | The 5-section pattern is real, but it is the *older* one: A7 is dated 2020 and every first-hand account from Nov 2024 onward describes 7 sections and 2 hours. A7 is the best evidence of question *style*, not of the current layout. One 2026-batch account (B7, Oct 2025) says 90 minutes and does not list counts; it is the only source with that duration |
| Coding in the SE test | 2 coding questions (C4) | No coding (8 sources incl. 5 first-hand) | **No coding** | C4 conflicts with every first-hand account and matches the SP/DSE format |
| Section timers and navigation | No sectional timing, free navigation (B5, pool campus, Jan 2025) | Fixed per-section timers, sequential, no revisiting (B1, May 2025; V4, Nov 2024) | **Sectional timers, no return** | Two sources vs one, and B1 gives the per-section minutes. Prepare for the stricter format; it costs nothing if the looser one appears |
| Cut-off value | 75% per section (B5) | ~70% per section (V1, coach) | **Unknown** | Both are unsourced assertions; record "not discoverable" |
| "Technical Ability" content | "basic computer science concepts" (B3) | Mathematical ability: percentages, TSD, P&C, series… (C1, V1, V2) | **Maths** | C1 lists maths topics under it; coaches state it explicitly. B3's "basic CS" most plausibly refers to the pseudocode section |
| Proctoring | In-person invigilators (A1 official, B3) | Webcam + AI proctoring in the lab (V1, coach) | **In person, window-switch tracking** | Official document; the AI claim is unsourced |
| Pseudocode difficulty | "bit difficult / moderate" (V4, Nov 2024) | "simple ... there is difficult question" (V5) | **Easy–medium with one or two hard traps** | The observed pool has 9 easy, 3 medium, 3 hard |
| Stale test (35 min, 20 aptitude + 40 English) | B6 (GfG, shown as Aug 2025) | All other 2024-25 accounts | **Stale** | Matches the pre-2019 Infosys test; GfG re-dates migrated posts |

## 9. Repeat rate (thread for Phase 2)

- **Cross-slot repeats cannot be measured.** No source ties the same question to two different slots or dates.
- **Cross-source recurrence:** 3 of 60 unique exam questions appear in two independent channels (BURST/LAKE/VERSATILE, the 48/72 ages ratio, the 400-student height table), all from coaching videos in Sep 2025. **5.0%.** Both channels may have copied the same upstream PYQ PDF, so this is an upper bound on independence, not a measured exam repeat rate.
- **Same-channel reuse** is heavy (OnlineStudy4u re-presents nine items across three videos a year apart). That is marketing reuse, not evidence of exam repeats.
- The coaches' claim that "Infosys repeats previous year questions" is `[REPORTED]` and self-interested.

## 10. What is still unknown

1. **The 2027-batch test itself.** No one has reported sitting it. The pattern could change.
2. Cut-off values.
3. Whether a separate behavioural instrument exists in the 2027 drive.
4. The exact evaluation date for VIT. Coaches expect "end of September or first week of October" 2026 for campus drives.
5. Verbal and Grammar content at question level for the **2025-26** test. The 2020 official sample supplies 20 verbal items (see `question-banks/QB-98-OFFICIAL-SAMPLE-SOLVED.md`), but no 2025-26 verbal question has been recovered beyond one item and one essay topic.
6. Whether the logic-set share seen in the 2020 sample (20 of its 25 reasoning and technical questions) has survived into the 2025-26 test. The reported 2025-26 questions are mostly single items, so this is `[INFERRED]` at best.

## 11. The Reddit pass (2026-10-03)

Detail: `07-reddit-arctic-shift.md`. It bears on this synthesis in four ways. None changes a number in §1.

| Point | Reddit evidence | Effect |
|---|---|---|
| 2027-batch test | Two posts (18 and 26 Sep 2026) ask what the test is; neither has an answer | §10 stays open: nobody has reported it |
| Sectional cut-offs | Two separate posters (Oct 2025) say puzzles, and puzzles with pseudocode, are where people fail the cut-off | `[REPORTED]` support for the existing `[CONFIRMED]` rule that every section has a cut-off. Puzzle and pseudocode stay as high-value sections |
| Difficulty | The Oct 2025 written test and the interview are called "easy" by several posters | Self-selected; does not change the plan. Keep preparing for the stricter format |
| Interview | Three more first-hand accounts: about 20 minutes, offline, resume-led, with cloud basics and OSI layers named once each | Added as `interview/00-INTERVIEW-FORMAT.md` §6–7; the B1–B5 tallies are unchanged |
| Upgrade path (§5) | Reports of offline invigilated upgrade tests, a June 2026 pause of SP/DSE tests (`[CONFIRMED]` news), and a 2026 SP/DSE format of four coding problems then an interview | New digest `interview/00-UPGRADE-TRACK.md`. Sources disagree on timing and mode |

