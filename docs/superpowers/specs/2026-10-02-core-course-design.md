# Core Course: advanced, easy, focused study material for the Infosys Systems Engineer test

**Date:** 2026-10-02 · **Approved by Hari:** 2026-10-02 ("yes") · **Path:** architectural · **Approach:** hybrid (hand-written lessons + generated, code-checked practice)

## Goal

Hari asked for "advanced study material, easy to understand, deeply researched, focused on the important things, actually beneficial". The existing library is complete but heavy (about 300,000 words; many topic files run 3,000-8,000 words and began as other companies' files). The gap is an **easy, focused layer** that teaches the topics that carry the marks, from zero, and then pushes past the exam's difficulty.

## Scope

22 lessons = the Tier 1 (15) and Tier 2 (7) topics in `data/weightage.json`. Together they are about 58 of 75 expected marks in about 19 study hours.

| Section | Topics |
|---|---|
| Reasoning and puzzles | A1 coding-decoding, A2 series, A3 operator logic, A4 syllogisms and deduction, A5 blood relations, A6 data sufficiency, A21 non-verbal, Z1 number grids, Z2 pair and figure rules |
| Technical (maths) | A7 data interpretation, A8 linear equations and ages |
| Verbal | V1 reading comprehension, V2 error spotting, V3 sentence correction, V6 critical reasoning |
| Grammar and writing | G1 cloze, G2 tense/articles/prepositions, W1 essay and email |
| Pseudocode | P1 loops and traces, P3 bitwise, P4 increments, P5 arrays |

Plus `00-START-HERE` (how to use it, order, a 60-minute diagnostic) and `99-LAST-48-HOURS`.

**Not in scope:** a new hard-mode mock; the CampusPrep hub site (rebuild only if Hari asks); the Tier 3-4 topics; audio.

## Lesson format (about 1,000-1,500 words each)

1. The idea, in plain words.
2. What Infosys actually asks (from the 2020 official sample, `QB-98`, and the reported pool; paraphrased, with IDs).
3. The method: a numbered recipe of 3-6 steps.
4. Safe shortcuts, each with the condition under which it breaks.
5. Worked examples: five, easy to advanced, with full working.
6. Traps: three to five.
7. Practice in three levels of five questions: **L1 warm-up, L2 exam level, L3 beyond the exam** (more steps, tighter traps than the 2020 sample). Answer key at the end of each lesson.
8. A 60-second recap.
9. Sources: what was opened, who published it, its date, and what it was used for.

## Rules

- **Correctness:** every numeric or logical practice answer is verified by a second route in code (existing generators and `check()` pattern). Anything judgement-based (verbal, grammar choices) is labelled as judgement and its rule is cross-checked against two vetted sources.
- **Sources are vetted before use** (Hari's standing instruction): open the page, record publisher and date, confirm the page type, state only what was observed. Methods and rules only; no copied text. Log in `research/06-method-sources.md`.
- **Easy to read:** every term is defined where it first appears; short sentences; a readability gate (average sentence length and a Flesch score) is run on every lesson.
- **The official sample is copyrighted/watermarked:** paraphrase only, as in `QB-98`.
- **No fabricated evidence tags:** keep the library's `[CONFIRMED]/[LIKELY]/[REPORTED]/[INFERRED]` convention where a claim is about the exam.
- `ds.py` may draft bulky low-risk boilerplate; lessons' explanations, methods, answers and framing are written and checked by Claude.
- No git commits in `$HOME` (the home directory is a repo with everything untracked).

## Delivery

- Files: `infosys-prep-library/core-course/NN-*.md` (frontmatter consistent with the library's, so the site and `verify_structure.py` accept them), generators in `data/gen_core_course.py`, builder `data/build_core_course.py`, verifier `data/verify_core_course.py`.
- Site: add the folder to the Infosys site builder, rebuild, `verify_site.py`, then republish to the same artifact URL.
- Update `PROGRESS.md`, `00-MASTER-INDEX.md` (via `build_docs.py`), the QA report, and the memory file.

## Order of work

1. Source vetting and the shared lesson template.
2. **Three pilot lessons** (one puzzle, one English, one pseudocode). Hari reads them before the rest. This is the "is it easy enough" checkpoint.
3. Remaining 19 lessons and their practice levels.
4. Verification, site rebuild, republish.

## Success criteria

- A learner can start any lesson from zero and finish it in 10-15 minutes of reading.
- Every practice answer has an independent check that passes; judgement items are labelled.
- Every external source is logged as opened and vetted.
- L3 practice is demonstrably harder than the official sample (more reasoning steps; recorded in the verifier output).
- All existing verifiers still pass.

## Self-review

- Placeholders: none. Consistency: scope table matches the 22 Tier 1-2 topics (15 + 7). Scope: one plan is enough because the pilot checkpoint gates the remaining lessons. Ambiguity: "advanced" is defined as L3 practice that exceeds the 2020 sample's difficulty; "easy" is defined by the readability gate plus the term-definition rule.
