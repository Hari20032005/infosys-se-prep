# PROGRESS

**Target:** Infosys Systems Engineer (Trainee), Rs 3.6 LPA, Campus Recruitment Program 2026-27. Hari, VIT Vellore, Integrated M.Tech SE, May 2027.
**Nomination closed 24 Sep 2026. Application Form pending (personal email). Evaluation date unknown; coaches expect campus drives late Sep / early Oct 2026. In person, college labs.**
A fresh session should be able to resume from this file alone.

---

## Status

| Phase | State | Output |
|---|---|---|
| 0 — Ground truth | **DONE** 2026-09-25 | `research/00-official-terms.md`, `01-APPLICATION-CHECKLIST.md` |
| 1 — Research and corpus | **DONE** 2026-09-25 | `research/02-online-research-log.md`, `research/03-pattern-synthesis.md`, `data/questions-observed.csv` (88 rows), `data/questions-discarded.csv` (16), `data/reviews-online.csv` (18), `data/syllabus-claims.csv` (66), `question-banks/QB-99-OBSERVED-POOL.md` (60 items) |
| 2 — Quantify | **DONE — signed off ("go") 2026-09-30** | `data/analyze.py`, `data/weightage.json`, `data/analysis-tables.md` |
| 3 — Build | **DONE** 2026-10-01 | 49 topic/interview files, 35 banks, MOCK-01, 7 index/strategy/plan files |
| 4 — QA | **DONE** 2026-10-01 | `research/04-qa-report.md`, `data/run_all_verifiers.sh` |
| 5 — Publish | **DONE** 2026-10-02 (v5: Core Course added) | https://claude.ai/artifact/WDiiHkYG2c4g4kPXD818kq · 210 pages · `verify_site.py` 28/28 |
| 6 — Audio | **declined by Hari** | |
| 7 — Previous-year question sources | **DONE** 2026-10-01 | `research/05-source-credibility.md`, `question-banks/QB-98-OFFICIAL-SAMPLE-SOLVED.md`, `data/official_sample.py` |
| 8 — Core Course (22 easy, advanced-capable lessons) | **DONE** 2026-10-02 | `core-course/` (start at `00-START-HERE.md`), `research/06-method-sources.md`, `data/verify_core_course.py`; spec and plan in `../docs/superpowers/` |
| 9 — Reddit pass via Arctic Shift (asked 2026-10-02) | **DONE locally** 2026-10-03; **not republished** (Hari chose local files only; the artifact stays at v5) | `research/07-reddit-arctic-shift.md` (tool vetting, counts, findings); new `interview/00-AFTER-SELECTION.md` and `00-UPGRADE-TRACK.md`; `interview/00-INTERVIEW-FORMAT.md` §6–7 (cloud, OSI); a paragraph and an "After the test" section in `core-course/00-START-HERE.md`; research notes 02, 03, 04 §8, 05 §6 updated; all verifiers pass |

**NEXT ACTION: Hari checks the personal inbox/spam for the Infosys Application Form, then works `core-course/00-START-HERE.md` (diagnostic first) and `99-STUDY-PLAN.md` for the days left.**

## Verification state, last run 2026-09-25

| Check | Result |
|---|---|
| `data/verify_observed.py` | 61 answers recomputed by execution, 0 mismatches (2 verifier bugs found and fixed first; content untouched) |
| `data/analyze.py` | questions reconcile 60.00/60, marks 75.00/75 |

## Decisions made

1. `infosys/` contained only `prompt.md`; no HackWithInfy PDFs to exclude.
2. **Planning model: 7 sections, 60 Q, 120 min, 75 marks + essay** (B1 first-hand May 2025 + C1, C2, V1, V5). Per-section counts `[LIKELY]`; model confidence Medium.
3. **Reasoning (15) and Technical Ability (10) are pooled into one 25-Q aptitude block** because C1 and the 2026 coaches disagree on which topics sit in which.
4. **ROI runs on expected marks**, because Pseudocode, Puzzle and Grammar carry 2 marks per question.
5. **Section floor** (new vs L&T): every section has its own cut-off, so the top-ROI subtopics covering 60% of each section's marks are lifted to at least T2. Ties lift together.
6. **English Writing is a gate**, tiered T1 by rule (marks unpublished).
7. **TCS 450 Infosys-puzzles file NOT used**: it is classic brain-teasers; the 2025-26 section is grid-number puzzles.
8. **No `coding/` folder**: the SE test has no coding `[CONFIRMED]`. The optional DSE/SP upgrade test is coding (3 Q / 180 min); its material stays in the Accenture coding library unless Hari asks.
9. Offload: DeepSeek via `ds.py` drafted question extraction from 8 transcripts (12 jobs); every item re-read against raw transcripts and re-solved.

## Facts established (do not re-research)

- Test venue: **college computer labs**, `rec-test.infosys.com`, Chrome/Edge, **proctored in person**, **no calculator**, **stationery allowed**, **15-minute login window**, window-switching tracked. College ID + govt ID mandatory. (Official 2026-batch guidelines.)
- **No coding** in the SE test. Sectional cut-offs exist; values unknown. No negative marking reported.
- Sectional timers and no return to previous sections (B1, V4); one account says otherwise (B5).
- Interview: F2F, 15-40 min; SDLC in 4 of 5 accounts; OOP, joins, project; HR incl. relocation, stress, **GenAI opinion and daily AI use** (B5).
- **Upgrade path exists:** after clearing SE test + interview, optional programming test + in-person interview for DSE 6.25 LPA / SP 9.5 LPA (KIIT notice Sep 2025).
- 2025 SE offer letter (one): Mysore on joining, 18-month probation, Rs 1,00,000 early-exit compensation, Rs 25,000/month gross first 6 months.
- 2025-cycle SE exam dates reported: 4, 11, 16 Oct 2025; 3 Dec 2025 (B3).

## Reddit pass, 2026-10-03 (do not redo; read `research/07-reddit-arctic-shift.md`)

- **No 2027-batch SE test report exists** in r/Infosys, r/infosysmysore, r/Infosys_DSE_2026 or r/PlacementsPrep. r/developersIndia and r/Btechtards could not be searched (Arctic Shift times out).
- Oct 2025 – Jan 2026 SE accounts agree with the model: easy test, puzzles/pseudocode sectional cut-offs, ~20 min offline resume-led interview. New interview questions: cloud models, OSI layers.
- **Offer letters for SE selections are slow and uneven** (people selected Oct–Nov 2025 waited about ten months) `[LIKELY]`. Documented in `interview/00-AFTER-SELECTION.md`.
- **Mysuru pre-test** (aptitude, English, Java, DBMS, OOP; >65% lets you pick a stream) and FA1/FA2 (65% pass) are `[REPORTED]`. Pay and incentive figures are disputed and deliberately not used.
- **10 June 2026:** Infosys deferred SP and DSE trainee tests for 20,000+ candidates (impersonation). `[CONFIRMED]` news, two outlets. SE not mentioned.
- Tool: Arctic Shift has no licence file, no API key, a dynamic rate limit; no usernames were stored. Raw posts were kept outside the library.
- **Not done, on purpose:** no practice banks for the DSE/SP coding track; the Core Course lessons and tiers are unchanged; the artifact was not republished.

## Open questions

- The 2027-batch test itself (nobody has reported sitting it).
- Cut-off values. Separate behavioural instrument in 2027? Exact VIT evaluation date.
- Verbal and Grammar content at question level for the 2025-26 test (1 observed item; the 2020 official sample supplies 20 verbal items).
- Whether the 2020 sample's heavy logic-set share (20 of its 25 reasoning and technical questions) survives in the current test.

## Tooling

- `python3 data/build_observed.py && python3 data/verify_observed.py && python3 data/build_qb99.py && python3 data/build_qb98.py && python3 data/build_reviews.py && python3 data/analyze.py`
- Transcript capture: built-in browser loads captions, `scratchpad/ytcap.sh <id> '<signed url>'` saves `tr-<id>.txt`. Scribd text: `scratchpad/scribd.py <docid>`.
- Bulk drafting: `python3 ~/.claude/bin/ds.py --batch <jobs.tsv>`.


## Final state (2026-10-01)

**Published:** https://claude.ai/artifact/WDiiHkYG2c4g4kPXD818kq (version 5, 210 pages, 2026-10-02). The publish tool reported it as shared "Anyone with the link"; check the Share menu if that is not what you want, because the library names your projects in `IV4`. Source of the page: `../artifact/` (index.html + content/infosys-se.js + assets/fulltext.js). Rebuild: `cd .. && python3 build_site.py && python3 verify_site.py && python3 build_artifact.py`, then republish the same path.

**Verifiers (all passing 2026-10-01, after the official sample was added):** `bash data/run_all_verifiers.sh` — official sample 54 items (31 by execution, 21 judgement, 2 unsolved, 0 failed); observed 61/61 by execution; generated 548 + real Java (36 + 24 + the 24 printed texts + 15/15); mock 59/59; cheatsheet 38/38; copied banks 49 confirmed, 1 source defect fixed; keys 901/901; structure all passed; links 131/137 (6 answer a bot 403; the official PDF host sends an incomplete certificate chain). Details: `research/04-qa-report.md`.

**Rebuild order:** `build_observed.py` → `verify_observed.py` → `build_qb99.py` → `build_qb98.py` → `build_reviews.py` → `analyze.py` → `copy_reused.py` → `build_topics.py` → `build_interview.py` → `build_mock.py` → `build_docs.py` → `build_cheatsheet.py` → `build_plan.py` → `check_links.py` → `build_resources.py` → `run_all_verifiers.sh`.

**Open items for Hari:** name your WasteZero module (repo fork shows no commits by you); redeploy the RAG backend; confirm the patent filing month; read your own offer letter for training/probation terms; Phase 6 audio declined.


## Previous-year questions (2026-10-01)

Hari asked for previous-year Systems Engineer questions from trustworthy sources, analysed before use. Result: **one** trustworthy source of question text exists, Infosys's own 2020 sample paper (A7). It is solved in `QB-98`. Aggregator sites (Talent Battle, PrepInsta, CodeQuotient, placementpapers.app) state no origin or contradict first-hand accounts, so nothing was imported; GitHub holds only SP/DSE material. Tier list moved: A6, V3, V6 to T1; A4, A21 to T2; P6 to T3; V5, A9, A11 down to T3. Reasons and limits: `research/05-source-credibility.md`.


## Core Course (2026-10-02)

Hari asked for advanced study material that is easy to understand, deeply researched and focused on what matters. Built as 22 short lessons (the Tier 1 and Tier 2 topics, about 58 of 75 expected marks) in `core-course/`, each with the idea, what Infosys asks, a numbered method, shortcuts and when they fail, five worked examples, traps, 15 practice questions at three levels, a recap and sources. Numeric, logic and code answers are checked by running code; English lessons are labelled judgement. Every web source used was opened and read (`research/06-method-sources.md`), and where a tool's summary disagreed with the page, the page won. Rebuild: `python3 data/build_core_course.py && python3 data/verify_core_course.py`. QA: `research/04-qa-report.md` §6.
