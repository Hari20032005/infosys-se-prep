# 03 — Test Strategy

How to sit the Infosys Systems Engineer test. Every fact is tagged; the evidence is in `research/03-pattern-synthesis.md`. The 2027-batch test has not been reported yet, so treat the section figures as the last known pattern (Oct 2025), not a guarantee.

## 1. Facts that shape the strategy

| Fact | Consequence | Tag |
|---|---|---|
| Seven sections, 60 questions, 120 minutes, 75 marks + an essay | Pace by section, not by the clock | `[LIKELY]` |
| **Each section has its own cut-off** (value unknown) | A zero in one section can end your chances however well you do elsewhere | `[CONFIRMED]` |
| Sections are timed and **cannot be revisited** | Time saved in one section is lost; time overspent in one costs only that section | `[LIKELY]` (one account says otherwise) |
| No negative marking reported | Answer every question; never leave a blank | `[LIKELY]` |
| **No calculator**; rough paper and stationery allowed | Mental arithmetic and written working only | `[CONFIRMED — official]` |
| In-person proctoring in college labs; switching windows is tracked; login window 15 minutes | Arrive early; never leave the test screen | `[CONFIRMED — official]` |
| Pseudocode, puzzle and grammar carry **2 marks a question** | 14 questions are worth 30 of the 75 marks | `[LIKELY]` |
| No coding in the Systems Engineer test | Do not spend preparation hours on coding problems | `[CONFIRMED]` |

## 2. Time per question and what to do when it runs out

| Section | Q | Minutes | Seconds a question | Rule |
|---|---|---|---|---|
| 1 Reasoning | 15 | 25 | **100** | Easy ones first within the section only if you can see all questions; if not, move on after 150 s and guess |
| 2 Technical (maths) | 10 | 35 | **210** | The most generous section. Use it: write working, check the data-interpretation base, re-check arithmetic |
| 3 Verbal | 20 | 20 | **60** | Reading comprehension costs most; do the short items first and the passage last |
| 4 Pseudocode | 5 | 10 | **120** | Draw a trace table. A wrong trace is worth 0, a slow right one is worth 2 |
| 5 Puzzle | 4 | 10 | **150** | Fit the rule on line 1, confirm on line 2, apply on line 3. Cap at 2.5 minutes, then guess by last digit |
| 6 Grammar | 5 | 10 | **120** | Read the passage once, then fix each blank from the words on both sides |
| 7 Writing | 1 | 10 | 600 | Plan 1 minute, write 7, proofread 2 |

**When to guess.** With no negative marking, a blank is always worse than a guess. When the section timer is at its last 15 seconds, fill every unanswered question with the same letter you have used least.

**When to move on.** If you have no rule after the per-question limit above, mark your best guess and go. One puzzle should never take the time of two.

## 3. Marks at stake by effort

Expected marks per study hour (`data/analysis-tables.md` §6) say where each hour pays most: Grammar and Puzzle first (10 + 10 marks, 2–3 marks a question), then series, coding and data interpretation, then the English reading and error-spotting items. Writing is a gate: a poor essay can fail a section whose marks are not even published.

## 4. What to do first in the room

1. **Carry** your original college ID card and a government photo ID. Both are mandatory throughout `[CONFIRMED — official]`.
2. **Login within the first 15 minutes** of the slot; after that the login closes and you lose the test `[CONFIRMED — official]`.
3. Close every other program; phones, smart watches and calculators stay outside `[CONFIRMED — official]`.
4. Do not wear headphones, do not talk to anyone, follow the dress code `[CONFIRMED — official]`.
5. Use the 60 seconds before the first section to write on your rough sheet: `EJOTY = 5 10 15 20 25` (letter anchors), squares 11–25, and the rule ladder for puzzles.
6. Read the on-screen instructions once; the section structure may differ from the planning model, and the screen is the authority.

## 5. Section by section

**Reasoning (100 s).** Coding-decoding: try the letter sum, then the position rule, then reverse-and-shift. Series: write the differences, then squares/cubes, then two interleaved series. Operator logic: divide-then-digit-sum, digit products. Blood relations: translate symbols to words, draw. Data sufficiency: solve statement I alone, then II alone, then both.

**Technical (210 s).** Data interpretation first if the table is clear: it is the topic coaches say appears every time. Percentage change uses the **old** value as the base. Heads-and-legs: assume all one kind. Mensuration: solve for r first.

**Verbal (60 s).** Error spotting: read each part for agreement, tense, preposition. Para-jumbles: decide the opener, then follow the pointer words. Critical reasoning: find the conclusion first.

**Pseudocode (120 s).** Read the declarations. Treat `/` as integer division, `mod` as remainder, `++`/`--` as Java. Write the variable values after each loop pass. Check the last pass twice.

**Puzzle (150 s).** The rule is the same on every line. Try product-based rules before sums; try the column when the numbers are big. If two options survive, compare the last digit.

**Grammar (120 s).** Read the passage once. Since/for, a/an, singular/plural subject, had + V3, passive. Re-read the sentence with your choice.

**Writing (10 min).** Four paragraphs, about 190 words, present tense. For an email: subject, purpose, details, request, close.

## 6. Mistakes that cost the most

| Mistake | Cost | Fix |
|---|---|---|
| Leaving a section for the end of its timer | Lost marks cannot be recovered after the timer | Answer as you go |
| Ignoring puzzle and grammar because they are “small” | 20 marks and two cut-offs | Practise them first |
| Spending 3 minutes on one reasoning question | Two other questions go unanswered | 150-second limit |
| Changing windows or talking | Application cancelled | Never |
| Over-trusting a leaked “answer key” | Published keys are often wrong | Re-derive |

## 7. The night before and the morning of

Pack the two IDs and a pen. Eat. Read `91-CHEATSHEET.md` once, then stop. Arrive early enough to log in within the window. After the test, note any questions you remember: they are the only Infosys evidence that does not exist yet for the 2027 batch (see `research/03-pattern-synthesis.md` §10).
