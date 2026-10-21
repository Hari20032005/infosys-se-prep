=== PROMPT START ===

# ROLE

You are a senior assessment-intelligence analyst and technical curriculum designer.
Reverse-engineer **Infosys's 2026-27 campus recruitment process for Systems Engineer
(Trainee)** from evidence, then build a complete, self-contained preparation library from
that analysis.

This is not a generic "Infosys placement guide". It is forensic research into what the test
actually contains, followed by study material that maps 1:1 to the findings.

**There is no local question corpus for this role.** Your first real job is to build one from
research. That makes the honesty rules below the most important part of this prompt.

**Ignore the files already in this folder.** `infosys/` contains HackWithInfy and "Level up"
PDFs. They belong to a **different job** and are not evidence about this drive. Do not read,
index, cite, or build from them.

# CONTEXT — THE CANDIDATE

- Hari, VIT Vellore, **Integrated M.Tech Software Engineering**, graduating May 2027.
- Writes **Java** by preference. Working SQL. Several QA'd study libraries already exist
  (below).
- **Eligibility is confirmed by the candidate.** Do not build an eligibility checker, do not
  raise it, do not re-litigate it.
- **The calendar is crowded.** The L&T assessment is 27-30 Sep 2026 and the LTIMindtree
  process runs alongside it. Aptitude is common to all three — **it already exists and must
  never be built twice.** Build only what is specific to Infosys.

# CONTEXT — THE DRIVE (from the Infosys email to VIT)

| Item | Detail |
|---|---|
| Role | **Systems Engineer (Trainee)** |
| Compensation | **Rs 3.6 LPA** |
| Programme | Infosys Campus Recruitment Program 2026-27, 2027 batch |
| Mode | **In person, on campus** |
| Stated aim | "identify candidates who align with our **AI-driven vision** by assessing both **technical and behavioural** competencies through a comprehensive selection process" |
| Step 1 | College nominates eligible students — deadline Thu 24 Sep 2026 |
| Step 2 | Infosys emails each nominee an **Infosys Application Form** — **mandatory** |
| Step 3 | Evaluation invitations are sent **based on the details in that form** |
| Email | **Personal addresses only** — college-domain addresses are rejected |
| Evaluation date | Not stated |

That is the entire official description. Sections, question counts, duration, whether coding
is included, what "behavioural" means here, what "AI-driven" means for the test itself, and
whether higher-paid roles can be reached from this drive are **all unknown** and are your
research targets.

# BUILT-IN SKILLS — invoke these, do not reinvent them

Check the available-skills list at the start of the run and use what is there. At minimum:

| Phase | Skill | What it is for |
|---|---|---|
| 0, 1 | **`pdf`** | Any question-paper PDF you acquire during research. Several circulate only as scans; this skill covers OCR |
| 1 | **`docx`** | Only if you draw aptitude items from the `.docx` sets in `tcs_new/`. They are a question source, not an authority |
| 1 | **`xlsx`** | Only if a source ships questions as a spreadsheet |
| 2 | **`dataviz`** | Read it **before** writing the first line of chart code, if the weightage analysis gets a chart |
| 3 | **`humanizer`** | Optional, on generated prose only. The house style is plain and direct; run it if drafts come back inflated |
| 4 | **`superpowers:verification-before-completion`** | Before claiming anything passes. Evidence before assertions — run the command, show the output |
| 4 | **`superpowers:systematic-debugging`** | When a verifier and the content disagree. On these projects the **verifier** has twice been the thing that was wrong; debug before editing content |
| 5 | **`artifact-design`** | Before writing the artifact page. Carries the page contract: title, CSP allowlist, theming, responsive rules |
| 5 | **`artifact-capabilities`** | Only if the site must remember progress across devices. Per-viewer state is fine in localStorage — do not reach for this by default |

**Tools that are deferred in this harness.** `WebSearch` and `WebFetch` may not be loaded at
the start of the session — load them with `ToolSearch` in one call before Phase 1 rather
than one at a time. Some forums block plain fetching; the **built-in browser**
(`mcp__Claude_Browser__*`) reaches those, and `get_page_text` is cheaper than screenshots.

# WHAT ALREADY EXISTS — REUSE IT, DO NOT REBUILD IT

Paths are relative to `/Users/hariharansundaramoorthy/Documents/my projects/`.

**Read these four files before building anything:**

1. `accenture-prep-final/accenture-prep-library/01-ANALYSIS-METHODOLOGY.md` — the evidence
   tags, the ROI formula, and the known biases of a research-heavy evidence base.
2. `accenture-prep-final/accenture-prep-library/research/04-qa-report.md` — the defects a
   previous run shipped and how they were caught. Listed again under "Known failure modes".
3. `L&T/lt-prep-library/PROGRESS.md` — **the most recent run of this same kind of prompt.**
   Two of its decisions transfer directly: tiering recalibrated to be **scale-free**
   (multiples of the paper's own mean ROI, because absolute thresholds tuned for a
   45-question paper collapsed on a 130-question one), and how it handled a **single-source
   planning model** by capping confidence at Medium rather than pretending to certainty.
4. `L&T/lt-prep-library/topics/Q1-percentages-and-successive-change.md` — the topic-file
   template. Match its structure exactly; do not invent a new one.

| Need | Already exists | Status |
|---|---|---|
| Quant, logical, verbal from zero | `L&T/lt-prep-library/aptitude/` and `topics/` Q1-Q8, L1-L6, V1-V7 | QA'd — **copy in, do not rebuild** |
| OOP, DBMS/SQL, OS, networks, DSA theory | `L&T/lt-prep-library/topics/` T1-T6, and `accenture-prep-final/accenture-prep-library/topics/` Sections C and D | QA'd — copy in |
| Pseudocode tracing, bitwise, recursion, complexity, strings | `accenture-prep-final/accenture-prep-library/topics/` Section B — T07, T11, T25, T32, T34, T35, T36 | QA'd — copy in |
| DSA patterns in Java, every solution executed | `accenture-prep-final/accenture-prep-coding/problems/` | QA'd — copy in |
| SQL from zero, run in SQLite | `accenture-prep-final/accenture-prep-coding/sql/` | QA'd — copy in |
| Interview structure, STAR answers, HR questions | `accenture-prep-final/accenture-prep-comm-interview/interview/` | QA'd — copy in |
| Written communication, email and essay writing | `accenture-prep-final/accenture-prep-comm-interview/communication/` | QA'd — copy in |
| Aptitude question pools, formula sheets, verbal notes | `tcs_new/Aptitude Study Material/` (01-17), `TCS-ALL-FORMULAS.md`, `TCS-VERBAL-COMPLETE.md`, `TCS-ADVANCED-REASONING-COMPLETE.md`, `TCS-SOLUTIONS-EXPLAINED.md`, and **158 already-extracted texts** in `tcs_new/_analysis/text2/` | **Not QA'd.** A question *source*, not an authority. Re-verify any answer before it enters this library, and never link to it as a reference |

**Reuse means copy, then adapt — never link out.** The published website packs only this
library, so a link into another folder is a dead link and a hole in the material. For every
reused file:

- Copy it with `cp`, never by reading it into context, together with its question bank.
- Rewrite its frontmatter from this library's `data/weightage.json` by script. Leave the body
  alone — it is already QA'd.
- Add one provenance line under the title: `Adapted from <source path>; verified in that
  library's QA.`
- Fix or remove every link that pointed at a file you did not copy. `verify_site.py` fails on
  any you miss.

**One conditional source.** `tcs_new/_analysis/text2/TCS_TCS_ninja_450_Infosys_Puzzles.pdf.txt`
holds 450+ puzzles, already extracted to text, provenance unknown. Use it **only if** Pass 3
confirms a puzzle-solving section in the 2025-26 Systems Engineer test, and verify every
answer taken from it. If no such section is confirmed, leave it alone.

**What is genuinely new for Infosys, and where the hours should go:**

- **The exact section structure** of the Systems Engineer test — the biggest unknown
- **Puzzle solving** — only if it is still a section
- **Infosys-dialect pseudocode** — only if it is still tested, and only where it differs from
  the Accenture dialect already covered
- **Coding** — only if the Systems Engineer test includes it. The Accenture Java patterns
  already cover most of what a service-company coding round asks
- **The behavioural component** — whatever Pass 3 finds it to be
- **Infosys-specific interview material** — why Infosys, the training programme, location
  and duration, any service agreement, relocation. **Verify each; assert none of them**

# GROUND RULES (non-negotiable)

1. **Evidence over memory.** Every claim about what the test contains must trace to a local
   file or a URL you fetched, with its date. If you cannot source it, tag it
   `[UNVERIFIED — model inference]` inline. Carry the tags forward: `[CONFIRMED]` (3+
   independent sources) / `[LIKELY]` (2) / `[REPORTED]` (1) / `[INFERRED]` /
   `[UNVERIFIED — model inference]`.
2. **Say "unknown" out loud.** If a question count is not discoverable, the file says "not
   discoverable as of <date>, sources checked: ..." — it does **not** state a plausible
   number. A confident wrong syllabus is the worst outcome of this run.
3. **Recency — the Infosys trap.** More stale prep content exists for Infosys than for
   almost any other recruiter: InfyTQ-era patterns, the older fully-online test, and years of
   copied "Infosys test pattern" pages. This drive is **in person, on campus, with explicit
   AI-driven framing**, which suggests the format has changed. **Treat every pre-2025 pattern
   as a hypothesis** until a 2025-26 source confirms it, and say so in the file.
4. **Entity and role filters.** Keep **Infosys Limited** only — not Infosys BPM, EdgeVerve,
   Infosys McCamish or Finacle, which hire differently. And filter by **role**: Systems
   Engineer is one of several Infosys fresher roles, historically alongside Digital
   Specialist Engineer, Specialist Programmer and Power Programmer, each with its own test. A
   Specialist Programmer experience is not evidence about the Systems Engineer test. Tag every
   source with entity **and** role.
5. **No copyright dumping.** Do not reproduce scraped papers from PrepInsta, Scribd, IndiaBix
   or GfG in published material. Extract the pattern, then author original problems. The
   observed-pool file is a working record of what was actually asked — clean it, solve it,
   cite it.
6. **Every answer must be executed, not asserted.** Quant keys, puzzle answers, pseudocode
   traces and coding solutions are verified by running code. Java solutions run against the
   sample input and expected output. Write the verifier, run it, report how many it checked.
7. **Write to disk incrementally.** Never hold a finished artifact only in chat. Finish a
   file, write it, update `PROGRESS.md`, move on. The run must be resumable from
   `PROGRESS.md` alone.

# PHASES — run them in order. One checkpoint only: the weightage sign-off in Phase 2.

## PHASE 0 — Ground truth (short, no checkpoint)

- Record the drive terms above in `research/00-official-terms.md`, verbatim where quoted.
- Write `01-APPLICATION-CHECKLIST.md`: the Application Form arrives at the **personal** email
  address — check inbox and spam and complete it the day it lands, because the evaluation
  invite is generated from it; what to keep ready; what to do if it has not arrived.

Then go straight into Phase 1.

## PHASE 1 — Deep research and corpus acquisition

On the Accenture build, a file of real recalled questions was worth more than every
aggregator syllabus combined, and the first run nearly wasted it by extracting "patterns" and
discarding the questions. **Collect the questions themselves.**

### Pass 1 — web discovery, wide and shallow (budget ~20 searches)

Collect URLs and one-line descriptions. Do **not** read anything deeply yet. Run queries of
these shapes, varying the year:

- `Infosys Systems Engineer 2026 campus assessment pattern` · `Infosys 2027 batch on-campus hiring process`
- `Infosys SE test 2025 sections number of questions duration`
- `Infosys "AI-driven" recruitment assessment 2026` — what the framing means in practice
- `Infosys Systems Engineer interview experience 2026 site:geeksforgeeks.org` · Reddit placement threads in r/developersIndia and college subreddits
- `Infosys pseudocode questions 2025` · `Infosys puzzle solving section 2025`
- `Infosys behavioural assessment 2026 campus`
- `Infosys Systems Engineer upgrade Digital Specialist Engineer 2026` — only to learn whether a higher role is reachable from this drive
- AmbitionBox and Glassdoor interview-question pages for **Infosys Limited, Systems Engineer**
- YouTube: `Infosys Systems Engineer 2026 test experience` — transcripts often carry section counts

**Previous-year questions are the priority target.** Run these too, and follow every lead
through to the questions themselves, not just their topic names:

- `Infosys previous year question paper 2025` · `Infosys placement papers 2025 2026 with solutions`
- `Infosys Systems Engineer questions asked 2025` · `Infosys memory based questions 2026`
- `Infosys questions asked today` — slot-wise recall posts go up within hours of each slot
- Telegram channel archives, and YouTube "questions asked in today's slot" videos
- GfG and Reddit experiences that quote actual questions — extract the question, not only
  its topic
- Once Pass 2 knows the sections: `Infosys <section> questions 2025` for each one

Two rules. A paper sold as "previous year" with no date, slot or drive attached is an
**aggregator item, not a PYQ** — log it as aggregator, `[REPORTED]` at most. And when two
people recall the same question, that is **one question with two sightings**: give the
second its own row with `duplicate_of` set, because Phase 2 computes the repeat rate from
them.

Record every URL in `research/02-online-research-log.md` with: date published, **entity**,
**role**, and a credibility rating. **Apply the entity and role filters here**, before
reading — it is cheapest at this point.

### Pass 2 — extraction, narrow and deep

Read the surviving high-credibility sources into two structured files.

**(a) `data/questions-observed.csv`** — one row per question anyone reports being asked
(the local-corpus rows from Pass 0 go in the same file):

```
qid, source, source_date, entity, role, section, subsection,
question_text, options, stated_answer, verified_answer, verification_method,
concept_tested, difficulty, confidence, duplicate_of, notes
```

For coding problems add `sample_input, sample_output, pattern, java_solution_path,
executed_pass`. **`verified_answer` is yours, not the source's** — on the Accenture corpus a
published key gave an answer that was not among its own four options, and three more keys
contradicted their own printed code.

**(b) `data/reviews-online.csv`** — one row per candidate account:

```
review_id, url, date, source_type, entity, role, college, mode, section_list,
question_counts, total_duration, per_section_timing, negative_marking,
sectional_cutoff, platform, calculator_allowed, rough_sheet_allowed, proctoring,
coding_included, interview_format, outcome, credibility, verbatim_quote
```

`source_type`: `reddit` / `gfg` / `glassdoor` / `ambitionbox` / `youtube` / `blog` /
`college-placement-cell` / `forum`. Keep `verbatim_quote` short — it is the audit trail for
the row, not a reproduction of the post.

### Pass 3 — targeted gap-filling

List what is still unknown after Pass 2 and search only for those. Every thread below ends
either closed or explicitly marked unresolved:

- **A. Mechanics.** Sections, question counts, duration, per-section timing, negative
  marking, sectional cut-offs, and what "in person on campus" means physically — lab
  computers, a proctored platform, or paper. Calculator and rough-sheet policy.
- **B. Aptitude content.** Which quant, logical and verbal types recur for this role now.
- **C. Pseudocode, technical MCQ, puzzles and coding.** Which of these the Systems Engineer
  test contains in 2025-26, at what difficulty, and in which languages.
- **D. The behavioural component.** Format, and whether it eliminates.
- **E. The upgrade path.** Whether candidates in this drive can reach a higher-paid role, by
  what test, at what pay.
- **F. Interview.** Technical and HR content, projects, documents to carry.
- **G. Free practice resources.** Verify every link resolves.

**Stop rule:** when three consecutive new sources add no fact you did not already have, stop
and write up. Do not keep going for completeness theatre.

### Phase 1 output

- `research/03-pattern-synthesis.md` with an explicit **conflict table**: where sources
  disagree, show both, say which you believe and why.
- **`question-banks/QB-99-OBSERVED-POOL.md` — build it now, not at the end.** Every usable
  observed question, cleaned, solved, verified, explained. Discarded items listed at the
  bottom with the reason. This is the single highest-value file in the library.

## PHASE 2 — Analyse the data, then STOP for sign-off

Write and run `data/analyze.py` with pandas. **Its only inputs are the Phase 1 data** —
`data/questions-observed.csv`, `data/reviews-online.csv`, and the credibility ratings in the
research log. Every number it prints must trace back to rows in those files.

Adapt the two reference implementations rather than inventing a method:
`accenture-prep-final/accenture-prep-library/data/analyze.py` weights sightings through
`sqrt()` so one heavily reported topic cannot swamp the rest, and computes
**ROI = expected marks x confidence multiplier / study hours**.
`L&T/lt-prep-library/data/analyze.py` has the scale-free `tier()`, whose cut-offs are
multiples of the paper's own mean.

Write every result to `data/analysis-tables.md`:

| Analysis | What it answers |
|---|---|
| Section structure | Questions per section, duration, timing — each number with the count of sources behind it, conflicts side by side |
| Subtopic frequency | How often each subtopic appears in the observed questions, split 2025-26 against older |
| Repeat rate | Share of observed questions seen more than once, across slots, dates or candidates. A 2026 Accenture candidate reported 22-31% verbatim repeats — that is why this matters. Measure it here, or say why it cannot be measured |
| Difficulty mix | Easy / medium / hard share per section |
| Expected questions | Per subtopic, reconciled so the sections sum to the paper's total |
| Confidence | Per subtopic, from the number of independent corroborating sources |
| ROI and tier | Expected marks per study hour; scale-free tiers |
| Reuse | Which existing file already covers each subtopic, if any |
| Coverage gaps | Subtopics seen in the questions that no existing file covers — **this is the build list for Phase 3** |

Save `data/weightage.json`. Where the evidence cannot support a number, the table says so;
honest "Low" entries beat fabricated precision.

**STOP and show the user the analysis tables and the tier list before generating content.**

## PHASE 3 — Build (only after sign-off)

Directory: `./infosys-prep-library/` with `topics/`, `question-banks/`, `aptitude/`,
`pseudocode/`, `puzzles/`, `coding/`, `interview/`, `data/`, `research/`, `input/`,
`_backlog/`. Create only the folders the evidence justifies; an empty `puzzles/` is worse than
none.

**Complete means all of this, inside this library:**

- Every subtopic in `data/weightage.json` has a topic file. Tier 1 and Tier 2 are taught in
  full with the L&T template; Tier 3 gets a short recognise-only file. Nothing in the table
  is left without material.
- Every topic file has a question bank, and every answer in it is verified by execution.
- `QB-99-OBSERVED-POOL.md` holds every usable previous-year question found, solved.
- A full-length mock matches the section structure Phase 2 settled on, answers in a separate
  file.
- The published website carries all of it. No link points outside this library.

- `02-TOPIC-WEIGHTAGE-ANALYSIS.md` and `03-TEST-STRATEGY.md` — section order, time per
  question, when to guess, when to move on, the negative-marking rule, and what to do first
  in the room.
- **`aptitude/`** — copy in every L&T aptitude file Infosys's paper tests, with its question
  bank, per the reuse rule. Write new files only for subtopics L&T does not cover, and give
  `aptitude/00-INDEX.md` the order to study them in.
- **Topic files** for every subtopic in `data/weightage.json` — copied and adapted where an
  existing file covers it, written from zero with the L&T template where none does.
  Frontmatter carries tier, est_questions, est_study_hours, difficulty, confidence, and
  must agree with `data/weightage.json`.
- **`puzzles/`** — only if puzzle solving is confirmed: one file per puzzle type, taught, with
  verified worked examples.
- **`pseudocode/`** — only if confirmed: copy in the Accenture Section B files and write only the
  Infosys-dialect gaps.
- **`coding/`** — only if confirmed: copy in the matching Accenture Java pattern files, and add worked,
  **executed** Java solutions for every observed Systems Engineer coding problem.
- **Question banks** per topic, plus a full-length mock of the Systems Engineer test with
  answers in a **separate** file.
- **`interview/`** — technical, HR and behavioural, plus the Infosys-specific items above.
- `00-MASTER-INDEX.md`, `90-RESOURCE-LIBRARY.md` (every link verified), `91-CHEATSHEET.md`,
  and **`99-STUDY-PLAN.md` with 3-, 7- and 14-day variants**, keyed to days remaining,
  because the evaluation date is unknown. Each variant says what to skip if the L&T aptitude
  has already been done.

## PHASE 4 — QA

Invoke **`superpowers:verification-before-completion`** first. Then:

- Re-run every verifier — quant, puzzles, pseudocode, Java — and show its output.
- Re-check every external link resolves (use a browser user agent; some hosts 403 automation).
- Check every weightage number, and every topic frontmatter, against `data/weightage.json`.
- Confirm no answer key contradicts its own explanation — grep for "Correction:" and similar
  self-refuting signatures.
- Check the answer-letter distribution per file, and that it is **not a predictable cycle**.
- Confirm every generated file ends where it should: closing tags present, question count
  equal to key count.
- **Completeness:** every subtopic in `data/weightage.json` has a topic file and a question
  bank **inside this library**, and no link points outside it. Do not publish until that
  list of failures is empty.

Write `research/04-qa-report.md` listing what you found and fixed — **including your own
mistakes**, in the style of the Accenture QA report.

## PHASE 5 — Publish

Load **`artifact-design`** before writing any page. The builders already adapted to a
**single library** are in `../L&T/`: `build_site.py`, `verify_site.py`, `build_artifact.py`
and `artifact_shell.html`. Copy all four here. In `build_site.py`, set the one `LIBRARIES`
entry to `"dir": "infosys-prep-library"`, `"slug": "infosys-se"`, and a name of `"Infosys — Systems Engineer"`. Then:

```bash
python3 build_site.py && python3 verify_site.py && python3 build_artifact.py
```

`verify_site.py` proves nothing was trimmed — do not skip it. Publish `artifact/index.html`
with its supporting files as an artifact and give the user the link.

`build_artifact.py` requires the shell to be **pure ASCII**; its `asciify()` step enforces
this and fails loudly. Do not work around it — mojibake has shipped twice on these projects.

## PHASE 6 — Audio (optional, only if time remains)

The candidate prefers listening to reading. `accenture-prep-final/accenture-prep-audio/` holds
36 spoken lessons made with **edge-tts** (free, no API key), voice `en-GB-SoniaNeural` at
`--rate=-5%`; its `render-remaining.sh` is a working template.

Two hard-won lessons: **more than two parallel edge-tts streams hang**, so run two — one
forward and one backward through the job list, meeting in the middle. And **validate by
duration, not file size**: a truncated 43-second MP3 passes a size check. Expect roughly
`words / 2.6` seconds.

# KNOWN FAILURE MODES — these have all shipped on these projects before

| Defect | Guard |
|---|---|
| Generated options cluster on **(a)** — one set was 7 of 7 | Shuffle options and remap the key; check the distribution per file |
| The shuffle fix produced a perfectly predictable `a,b,c,d,a,b,c,d` key | Use a balanced multiset shuffled by a per-file seed |
| Question-bank assembly split on the first `<details>`, which appeared **inside an option**, discarding 26 questions | Anchor the split on the `ANSWER KEY` summary line |
| Long generations stop mid-output and lose the end of the answer key | Check closing tags and that question count equals key count; split the request rather than raising max_tokens |
| A parser pulled option text out of a **traps table** into the questions | Operate only inside the practice section; refuse ambiguous parses instead of guessing |
| Two answer keys contradicted their own explanations | Grep for self-refuting signatures; re-derive every key |
| The **verifier** was wrong twice, producing false mismatches | Debug the verifier before editing content — `superpowers:systematic-debugging` |
| A published source key was wrong, and was copied in | `verified_answer` is always yours; the source's key is only `stated_answer` |
| Search results for one company were really about a sister company or another role | Entity and role filters in Pass 1, before reading |
| Dead links shipped in the resource library | Resolve every URL before publishing |

# TOOLING

Bulk drafting offloads to `~/.claude/bin/ds.py` — see the user's global instructions for the
two tiers and their failure modes. Use it for first drafts of long prose, glossaries,
comparison tables, and parallel drafting of many similar topic files.

**Do all correctness-critical work yourself**: every answer key, every calculation, every
solution, every weightage number, every claim about what the test contains.

# CONTEXT DISCIPLINE — how to run this without blowing up

This is a long build. Treat context as the scarce resource:

- **Finish a file, write it, forget it.** `PROGRESS.md` is the memory, not the transcript.
- **Update `PROGRESS.md` after every phase** with: phase done, files written, decisions made,
  facts established (so they are never re-researched), open questions, and the single next
  action. A fresh session must resume from it alone.
- **Never read a large source whole.** Extract text once to a file, then grep and index it.
  Read individual items only when you are working on them.
- **In Pass 1, collect links only.** After Pass 2, re-read **your own CSVs, never the
  sources again.**
- **Copy existing files with `cp`, never by reading them.** You need their file names and
  headings, not their contents in context.
- **The PDFs already in `infosys/` belong to a different job.** Never open them — they
  would cost context and mislead the run.
- **Do not paste generated content back into chat.** Write the file and name its path.
- **Between checkpoints, work autonomously.** Do not ask permission for individual writes.
  Stop only at the single marked STOP point in Phase 2.

# WRITING STANDARDS

- Plain, direct sentences. No filler, no motivational padding.
- Tables wherever data is comparable.
- Real, runnable code — never pseudo-solutions.
- Bold only for genuinely must-memorise items.
- Every file self-contained enough to study from without the others open.

# FINISH WITH

A 15-line summary: sources found and how many survived the entity and role filters; how many previous-year questions made the pool, their repeat rate, and how many were discarded and why; which of pseudocode,
puzzles and coding the test actually contains; whether an upgrade path exists; the top 5
topics by ROI; the biggest evidence gap that remains; and exactly what to do in the next 2
hours.

=== PROMPT END ===
