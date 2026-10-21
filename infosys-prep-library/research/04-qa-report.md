# 04 — QA Report

**Date:** 2026-10-02 (re-run after the Core Course was added) · **Scope:** the whole library: 140 Markdown files outside `data/`, about 363,000 words, 49 subtopic and interview-theme files, 39 question banks (`QB-*`), one full mock, and the 24-page Core Course (§6).

Checks were **run**, not asserted. Every verifier is in `data/`; `data/run_all_verifiers.sh` re-runs all of them and prints the same summary lines.

---

## Summary

| Check | Result |
|---|---|
| Core Course (`verify_core_course.py`) | 22 lessons, 104 worked-example claims executed, 0 failures; see §6 |
| Observed pool (`verify_observed.py`) | 61 answers recomputed by execution, 0 mismatches; 27 items are verbal, essay or interview (not machine-checkable) |
| Official sample (`official_sample.py`) | 54 items: **31 decided by execution** (brute force, simulation, model search), 21 by judgement (verbal, units), 2 not solved because no key is published; 0 failed checks |
| Observed pseudocode in real Java | **15 / 15** of P01–P15 match |
| Generated banks (`verify_generated.py`) | **548** generated questions, each with an independent `check()`; regenerating gives byte-identical files, also under different `PYTHONHASHSEED` values |
| Pseudocode traces and increments in real Java | **36 + 24** programs compiled and run, 0 disagreements; the **24 printed official-dialect texts** (parsed back out of the questions and translated to Java, not the internal program) also match their keys; **11 / 11** hand-written P4 claims match Java |
| Mock (`verify_mock.py`) | 59 / 59 answers re-derived by a second route; keys 59 for 59 questions; letters a15 b15 c15 d14; no repeating cycle |
| Cheat sheet (`build_cheatsheet.py --verify`) | 38 numeric and formula claims executed, 0 failed; 8 qualitative lines are listed as unchecked |
| Copied Accenture banks re-executed (`verify_copied.py`) | 66 code questions inspected; **49 output keys confirmed by compiling or running the code**; **1 source defect found and fixed** (below); 17 ask for something other than printed text or cannot be run |
| Question and key counts (`verify_keys.py`) | 1,231 questions, 1,231 keys, 0 issues across 126 files |
| Topic frontmatter against `weightage.json` | **52 / 52** exact (tier, confidence, hours, questions) |
| Completeness | all 49 subtopic and interview codes have a topic file and a question bank inside the library; 0 missing |
| Ten-section template | 49 / 49 main topic files |
| Internal links | **410 / 410** resolve and none leaves the library |
| External links | 168 URLs: **160 resolve**; 8 do not for automated clients (see §3 and §6) |
| Answer-letter distribution | 1,250 keys: a 319 · b 322 · c 308 · d 301; most common 25.8%; no repeating cycle in any block. The data-sufficiency bank prints its options on the fixed 1-2-3-4 scale as the real paper does, with the four answers balanced 6 / 6 / 6 / 6 |
| Self-refuting signatures (`Correction:` and similar) | 0 |
| Section reconciliation (`analyze.py`) | questions 60.00 / 60, marks 75.00 / 75 |

---

## 1. Defects found and fixed

### 1.1 A wrong key in the copied Accenture material

`QB-P3-bitwise-operators.md` question 9 asks for the output of

```c
int n = 12;
if (n & 3 == 0) printf("Y"); else printf("X");
```

The source key said **(d) Y** and its explanation said the else branch prints Y. Compiling and running the code prints **X**: `==` binds tighter than `&`, so the condition is `12 & 0`, which is false, and the else branch is `printf("X")`. The source's explanation for the distractor also contradicted its own code. Found only because the answers were re-executed here; the Accenture QA had checked 45 pseudocode answers and missed it. The key in this library is now **(a) X** and the explanation says why (`QB_PATCHES` in `data/copy_reused.py`, so it survives regeneration).

### 1.2 Source formatting defect in three copied files

`P7-functions-scope`, `P10-strings-ascii` and `P8-snippet-complexity` had headings glued to the end of a table row (`…|## 7. Practice questions`), so the section was invisible to any parser. This is the same defect the Accenture QA report listed as 1.9. `copy_reused.py` now inserts the missing line break.

### 1.3 Source-paper claims inside copied files

Sections 1, 2 and 10 of every copied topic file carried numbers and evidence from the **L&T** or **Accenture** paper (“3.81 questions, 2.9% of the paper”, “a question observed on a real L&T paper”). Section 1 and 10 are now regenerated from `weightage.json`; section 2 gains an Infosys evidence table and keeps the original pattern notes under an explicit warning. One resource bullet that only made sense for L&T (“Careers360 / Shiksha L&T PGET syllabus pages”) was removed from `A6`. Remaining mentions (“the observed L&T pattern” in worked examples of A12, A15, A17) are covered by the provenance line under each title.

### 1.4 Own errors, caught on re-reading

| # | Mistake | How it was caught | Fix |
|---|---|---|---|
| 1 | A para-jumble said the Eiffel Tower was **“designed by a British engineer”**, which is false | Re-reading the authored text | Reworded to “designed by the engineers of Gustave Eiffel’s company” and “1889 Paris World Fair” |
| 2 | Para-jumble Example 3 had two defensible orders (RPQ and PRQ) | Re-reading for uniqueness | Rewritten so each sentence points back at the one before; every set's uniqueness is asserted in `bank_verbal.py` |
| 3 | The mock's seating questions asked “who sits in the middle” while a clue said so | Reading the rendered mock | They now ask who sits at the extreme left and second from the right |
| 4 | Data-interpretation questions started with a table row, which the key parser skips: `COUNT-MISMATCH 18 vs 24` | `verify_keys.py` | A sentence now precedes every table |
| 5 | The mock's bitwise question produced only two distinct wrong options | An assertion in `render_questions` | Two more distractors added; assertion kept |
| 6 | The seeded shuffle produced `c,d,a,b,c,d,a,b` for the A20 bank, a guessable cycle | `verify_structure.py` | `letters_for` now rejects any repeating-cycle assignment |
| 7 | The 14-day plan claimed “no day above four hours” while one day was 6.2 h | Printing every day's total | Plan rebalanced to a 4.5 h maximum; the claim is now true |
| 8 | `QB-99` said P03 and P14 were “re-run as real Java in `pseudocode/verify/`”, a folder that did not exist | Reading my own summary against the tree | Replaced by a real check: all 15 observed pseudocode items run in Java |
| 9 | `IV4` said project questions were asked in “three of five” accounts and `IV5` “four of five” for HR | Re-reading the interview rows | Corrected to two and three; an unverified attribution (“B2 assisted candidates”) was removed |
| 10 | A tier-reason line printed the internal token `roi` | Reading a generated topic file | Replaced by an explanation with the actual numbers |
| 11 | A20 Example 2 asserted `E ∈ {5, 6, 0}` without reason | Re-reading | Rewritten with the actual argument |

### 1.5 The verifier was wrong, not the content (three times)

Following the rule from the earlier builds (“debug the verifier before editing content”):

| Verifier | False report | Cause |
|---|---|---|
| `verify_observed.py` R04 | “mismatch” | The verifier returned only the verdict; the CSV key also stated the working. It now returns both |
| `verify_observed.py` R11 | “35O16 vs 48O16” | The verifier took the wrong term of the square sequence (6², not 7²−1). Content was right |
| `verify_generated.py` P14 | “mismatch” | The CSV keys the winning **expression** (`++i + ++i (3 + 4)`); Java prints its **value**, 7. Comparison now maps one to the other |

### 1.6 Dead links

Sixteen URLs failed on the first sweep (fifteen 404s and one that did not connect): seven IndiaBIX pages that had moved or never existed (`/verbal-ability/articles/`, `/aptitude/hcf-and-lcm/`, …), seven GeeksforGeeks pages (`/blood-relations-reasoning/`, `/para-jumbles/`, …), the Indeed STAR page and the British Council writing page. Each was replaced by a page that resolves, or the bullet was removed. Replacement IndiaBIX paths were taken from the site's own index pages, not guessed. A further five answered with a 403 and are covered in §3.

---

### 1.7 Defects found while adding the official sample (2026-10-01)

| # | Defect | How it was caught | Fix |
|---|---|---|---|
| 1 | My first-pass answers to four official-sample items were wrong (the Ramsay question, the data-sufficiency classification helper, the order of the deductive triples, the option letter for LET + LEE = ALL) | Re-deriving each by brute force over the real constraints | `official_sample.py` holds only computed answers; the deductive items are labelled a *reading* because the key is unpublished |
| 2 | The new data-sufficiency generator **could never produce answers 1 or 2**: no statement alone fixed x, so the bank was all 3s and 4s with the letters hidden by shuffling | Counting distinct questions per answer (0, 0, 335, 1,061) instead of only checking that each key matched its check | Four self-determining statement types added (`x³ = k`, `2x + 3 = k`, two `x² = k and …` forms); the bank now has six of each answer, in the paper's fixed 1-2-3-4 option order |
| 3 | `QB-A4-ordered-deduction.md` changed between two runs | `verify_generated.py` ("files changed on regeneration") | The option list was a Python `set`, whose order depends on the hash seed; now a list. Determinism confirmed under two different seeds |
| 4 | `build_reviews.py` was older than the CSV it writes: re-running it dropped three later hand edits (the marks for each section, two notes) and broke `analyze.py` with `StopIteration` | The crash itself | The edits were recovered from the session transcript and moved into the script, so a rebuild is lossless |
| 5 | `verify_keys.py` reported two false count mismatches | Its own output (5 questions vs 24 keys; 30 vs 29) | It skipped any line containing a pipe, so a key that says `|left - right|` vanished, and it read numbered pseudocode lines (`1) Integer c, n`) as question numbers. It now skips only table rows and fenced code. The content was right |
| 6 | The link checker reported the official PDF as dead (status 000) | `check_links.py` | The host sends an incomplete certificate chain: strict clients such as `curl` and Python refuse it, a browser loads it. The checker now retries without verification only to tell this case from a dead host and says so |

## 2. What each verifier actually proves, and what it does not

| Material | Proof | Limit |
|---|---|---|
| Official sample (54 items) | 31 answers decided by code over the real constraints; the paraphrased gists are mine | 21 are judgement (verbal, units) and 2 are unsolved; the deductive answers rest on one stated reading of "related". The PDF has no key, so there is nothing to compare against |
| Observed pool (61 numeric/trace items) | Recomputed from the question text by code; 15 pseudocode items also in Java | The question texts were reconstructed from auto-captions; where the caption lost data the item was discarded or flagged (R12, R14, Q06, Q07) |
| Generated banks (548) | Two routes to each answer (rule search, brute force, simulation, or inverse); puzzles are unique against a library of 40+ competing rules | A rule outside the library could also fit; distractors are plausible wrong routes, not exhaustive |
| Pseudocode traces | Two Python evaluators and real Java agree; the printed text is also translated and run | Programs avoid negative numbers so Java and Python division agree. The translator knows only the dialect the generator prints |
| Increment questions | Real Java left-to-right semantics | In C the same expressions are undefined behaviour; the library says so |
| Syllogisms, seating | Exhaustive search over all models / all 120 arrangements | The syllogism checker assumes every named class is non-empty (the usual exam convention) |
| Verbal, grammar, writing (~100 items) | **Authored; one best answer by design; no machine check.** Para-jumble uniqueness follows from declared pointer words | This is the least verifiable part of the library. Reading comprehension and critical reasoning keys depend on judgement |
| Copied L&T files (aptitude, verbal) | Verified in the L&T library (400 questions, 0 issues there) and re-run through `verify_keys.py` here | Their evidence sections were rewritten here; their teaching bodies were not re-derived |
| Copied Accenture banks | 49 output keys re-executed here (1 defect found); the other copied pseudocode, `IV1`–`IV3` banks rely on the Accenture QA | Not exhaustively re-run; the defect in §1.1 shows that source QA missed at least one |
| Cheat sheet | 38 claims executed | Grammar and method lines are not checkable |

---

## 3. External links

`data/check_links.py` fetched every URL with a browser user agent and followed redirects. **131 of 137 resolve (2xx or 3xx).** Six answer automated requests with a 403:

| URL | Result in a real browser |
|---|---|
| `www.infosys.com/services/data-ai-topaz.html` | Loads (page title “Infosys Topaz: An AI-first offering…”) |
| `www.merriam-webster.com/thesaurus` | Loads |
| `artofproblemsolving.com/wiki/index.php/Ratio` | Loads |
| `dictionary.cambridge.org/` and `/grammar/british-grammar/` | Serve a Cloudflare “Just a moment” check; the site is live but cannot be fetched without passing it |
| `claude.ai/artifact/WDiiHkYG2c4g4kPXD818kq` (in `PROGRESS.md`) | The published study site; private, so it answers an unauthenticated client with a 403 |

The official sample PDF (`infytq.onwingspan.com/…SystemsEngineer.pdf`) counts as resolved: its server sends an incomplete certificate chain, so the checker only reaches it after retrying without verification; the built-in browser opened it (it offered the PDF as a download). The certificate itself names `Infosys Limited, Bengaluru` as the holder, issued by DigiCert.

The test platform address printed in the official guidelines (`rec-test.infosys.com/web/en/systemCheck`) returns 404 from outside Infosys's network; it is mentioned in text and deliberately not linked.

---

## 4. Claims that stay unverified, and why

| Claim | Tag | Why it matters |
|---|---|---|
| Section counts 15 / 10 / 20 / 5 / 4 / 5 / 1 | `[LIKELY]` | One first-hand account plus decks and coaches that may share a source; nobody has reported the 2027-batch test |
| Sectional timers and no revisiting | `[LIKELY]` | One first-hand account in 2025 says there are no sectional timers and free navigation |
| Cut-off value | **not claimed** | Claims of 70% and 75% are unsourced |
| Share of logic sets in the 2025-26 test | `[INFERRED]` at best | The 2020 official sample is about 20 of its 25 reasoning-and-technical questions; no 2025-26 source shows whether that held |
| Official-sample verbal answers (about 21 items) | judgement | No machine check exists for them, and the PDF has no key |
| No negative marking | `[LIKELY]` | One first-hand account states it; the official text is silent |
| Repeat rate | 3 of 60 across independent channels | Cross-slot repeats cannot be measured |
| Joining terms (Mysuru, 18-month probation, Rs 1 lakh compensation) | `[REPORTED]` | One 2025 offer letter; read your own |
| Project facts in `IV4` | from your own `HARIHARAN_INTERVIEW_CONTEXT.md` | Not independently re-checked here; the WasteZero authorship caveat is yours to resolve |

---

## 6. The Core Course (added 2026-10-02)

22 lessons, `00-START-HERE` and `99-LAST-48-HOURS`, in `core-course/`. Checked by `data/verify_core_course.py` (also run by `run_all_verifiers.sh`).

| Check | Result |
|---|---|
| Lessons | 22 of 22 present, each with all nine parts and 15 practice questions (5 per level) with 15 keys |
| Worked examples | **104 claims executed** in `data/cc_examples.py` (brute force, exact fractions, two independent syllogism searches, and real Java for every printed program); 0 failed. Each lesson that quotes a program, essay or email is also checked to contain exactly the text that was run or counted |
| Generated practice | Every generated question has an independent `check()`; the lessons regenerate byte for byte from `cc_practice.py` |
| Pseudocode practice | Printed programs (P1, P3, P5) are translated back from the printed text to Java and run; 0 disagreements |
| Difficulty | Mean `steps` rises from Level 1 to Level 2 to Level 3 in every lesson that has a measure; in Z2 at least three Level 3 puzzles use more steps than the 2020 sample's hardest rule (5) |
| Readability (parts 1-6 and 8) | Prose 717 to 1,179 words; average sentence 6.8 to 9.6 words; Flesch reading ease 74 to 87. Gate: at most 14 words per sentence and at least 65 |
| Answer letters | Balanced (no letter more than 6 of 15), no repeating cycle, no letter three times in a row (the data-sufficiency lesson is on the fixed 1-2-3-4 scale and is exempt from the last rule) |
| Sources | Every link in a lesson's part 9 is a "used" source in `research/06-method-sources.md` (24 sources listed there; the pages opened and not used are listed there too) |
| Copying | No 12-word run from the official sample PDF text appears in any lesson |
| Whole library | 126 files, **1,231 questions and 1,231 keys**, 0 issues; 168 URLs, 160 resolve (the other 8 are the bot-blocked sites already listed in §3 and the British Council pages, which refuse `curl` but load in a browser; both used pages were opened in the browser) |

### 6.1 Defects found while building the Core Course

| # | Defect | How it was caught | Fix |
|---|---|---|---|
| 1 | **The site rendered `**a*b + c*d**` as "a" and "b + c" in italics**: a multiplication asterisk pairs with the next one. 5 files, including answer keys in the existing Z2 topic and bank | Rendering the lesson in Chrome and scanning every page for intra-word emphasis | Rules are shown with `×` and `²` (`gen_puzzles.disp`); two copied files patched in `copy_reused.py`; rescan: 0 hits |
| 2 | **Every topic page showed its raw front matter as a paragraph** ("title: … code: … tier: …") | The same screenshot | `build_site.py` strips it and shows one metadata line |
| 3 | A fetch tool's summary said Java's `i++ + ++i` "depends on implementation details" | Reading the Java Language Specification text directly (§15.7: operands are evaluated from left to right) | Summary discarded; both quotes are in `research/06-method-sources.md` |
| 4 | A search snippet said the British Council page explains when to use *Yours sincerely* versus *Yours faithfully*; the page does not | Opening the page | Rule not taught |
| 5 | The generated blood-relations practice contained a child with two male parents | Reading generated questions | A consistency filter (`family_consistent`) rejects such instances |
| 6 | The syllogism table listed 2 of the 3 conclusions that follow from "All X are Y, no Y are Z" (it missed "Some Z are not X") | The strict set-equality check in `cc_examples.py` | Row corrected |
| 7 | My expected value for `3 * (4 * 5)` was 27; real value 19 | The example check | Text and check corrected |
| 8 | The 12-word copy check flagged a section heading quoted from the sample | `verify_core_course.py` | Heading paraphrased |
| 9 | Three unsupported statements ("about one question in four keeps the original", "an hour of practice clears it for most people", "the standard ones in similar exams") | Searching lesson text for generalisations | Removed or restated as my own choice |
| 10 | `verify_keys.py` read the numbered statements in a syllogism question as question numbers (5 questions vs 15 keys) | Its own output | The statements are now written "Statement 1:" and "Statement 2:". The verifier already skipped numbered lines inside code fences |
| 11 | An early sample of the generated puzzle practice had two identical rule names in Level 1, and a data-sufficiency pool that could not make answer 2 | Counting distinct questions per answer | One named rule per question; a larger statement pool for answer 2 |

### 6.2 What the Core Course does not prove

- The English lessons (G1, G2, V1, V2, V3, V6, W1) are **judgement**. Each practice item is labelled, each rule is tied to a page that was opened and read, and each item was written to have one best answer, but no program checks them.
- Non-verbal reasoning (A21) has no Infosys question behind it; the lesson says so.
- "Level 3 is harder than the sample" is measured by a count of steps where a count makes sense (puzzles, series, code, algebra). For the English lessons it means "a tempting wrong answer sits next to the right one", which is a description, not a measurement.
- Readability scores say the sentences are short and plain. They do not say the explanations are good; only a learner can.

## 7. Reproducing these checks

```bash
bash data/run_all_verifiers.sh                 # every verifier, summary lines only
python3 data/check_links.py                    # external links
python3 data/build_topics.py && python3 data/verify_generated.py   # regenerate and compare
```

## 8. The Reddit pass (added 2026-10-03)

**What was checked**

- **The tool.** Arctic Shift's README, API docs and data notes were read as raw files, the licence was checked (none), and the API was exercised with small requests before any crawl.
- **The articles.** The June 2026 pause was checked in the raw text of two pages (Storyboard18, HRKatha): date, roles named, and the absence of Systems Engineer. The Times of India original was not opened.
- **The definitions.** NIST SP 800-145 was read in full; IBM's OSI page was read for the seven layer names and jobs.
- **Every claim in the three new documents** (`00-AFTER-SELECTION.md`, `00-UPGRADE-TRACK.md`, `00-INTERVIEW-FORMAT.md` §6–7) was re-read against the thread it came from before the files were finalised.
- **The library.** `bash data/run_all_verifiers.sh` exits 0 after the rebuild. The 22 course lessons rebuild byte-identical; only `00-START-HERE.md` changed. Backticked file references in the new documents were checked to exist.

**Defects found and fixed during this pass**

| # | Defect | Fix |
|---|---|---|
| 1 | The first topic count used every long DSE/SP-related post (792), including questions and waiting-for-results posts | Narrowed to 267 posts that read as first-hand accounts; a sample of 14 was read by eye. A minority are still not accounts, so percentages are rough |
| 2 | Keyword patterns for SQL, OS and networks matched "join" (joining the company), "process" and "query" | Tightened; SQL recounted strictly (48%), OS and networks recounted |
| 3 | A draft tagged the absence of a 2027 report `[CONFIRMED]`, and said "seven accounts" | Reworded: absence in four communities is not proof; "about ten comments across ten threads" |
| 4 | Four interview threads were cited from their titles only | Read in full before citing; their specifics were added and one tag corrected |
| 5 | A draft row said candidates in the same hall get different test sets as a `[LIKELY]` fact | Reduced to one poster's claim |

**Stays unverified**

- Everything from Reddit. It is anonymous and could not be cross-checked against any official source.
- Whether the FA1/FA2 and pre-test structure applies to the 2027 cohort.
- Pay and incentive figures during training: the replies contradict each other, so none is used.
- r/developersIndia and r/Btechtards, which Arctic Shift could not search.
- The ISO OSI standard and the original Times of India article.

