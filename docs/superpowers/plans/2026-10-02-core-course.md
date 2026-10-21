# Core Course Implementation Plan

> **Status: executed 2026-10-02** (all tasks done; pilots approved with "go"; 22 lessons, start-here and last-48-hours pages, verifiers, site rebuilt and republished as artifact version 5).

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. *(In this session the plan is executed inline by the author; the system rules say no subagents unless the user asks.)*

**Goal:** Add 22 easy, focused, advanced-capable lessons (the Tier 1 and 2 topics) to the Infosys Systems Engineer library, each with three practice levels whose answers are verified by code, and republish the study site.

**Architecture:** Hand-written lesson text lives in `data/cc_src/<CODE>.md`. Practice questions come from `data/cc_practice.py`, which reuses the existing generators (`gen_core.Q` with a `check()`), adds a harder "L3" parameter set, and wraps hand-written items with a `judgement` flag. `data/build_core_course.py` assembles `core-course/NN-<code>-<slug>.md`; `data/verify_core_course.py` gates structure, keys, balance and readability.

**Tech Stack:** Python 3 (stdlib `unittest`, existing `data/` generators), Java 20 (execution checks), the existing `build_site.py` / `verify_site.py` / `build_artifact.py`.

**Spec:** `docs/superpowers/specs/2026-10-02-core-course-design.md`

## Global Constraints

- Scope is exactly 22 lessons: A1 A2 A3 A4 A5 A6 A21 Z1 Z2 (reasoning and puzzles), A7 A8 (technical), V1 V2 V3 V6 (verbal), G1 G2 W1 (grammar and writing), P1 P3 P4 P5 (pseudocode); plus `00-START-HERE` and `99-LAST-48-HOURS`.
- Lesson length 1,000-1,500 words of prose; nine parts in the spec's order; practice = L1, L2, L3 with 5 questions each.
- Every numeric or logical answer has an independent `check()` that passes; judgement items are labelled `judgement`.
- Sources are opened and vetted before use; log in `research/06-method-sources.md`; rules and methods only, no copied text; the official sample is paraphrased only.
- Evidence tags `[CONFIRMED]/[LIKELY]/[REPORTED]/[INFERRED]` are used for claims about the exam, never for general method.
- Readability gate on parts 1-6 and 8 of every lesson (provisional: average sentence at most 20 words, Flesch reading ease at least 50; recalibrated once after the pilots and the new values recorded in the verifier).
- No git commits (the home directory is a repository with everything untracked). No audio. No hub rebuild unless Hari asks.
- Answer letters balanced across the 15 practice questions of a lesson and not a repeating cycle.
- Work in `/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library`; run scripts from there as `python3 data/<script>.py`.

## File structure

| File | Responsibility |
|---|---|
| `research/06-method-sources.md` | Every method source opened: publisher, date, page type, verdict, what it was used for |
| `data/cc_readability.py` | `readability(md)` and the gate |
| `data/cc_practice.py` | `PRACTICE[code]() -> {1: [Q]*5, 2: [Q]*5, 3: [Q]*5}` |
| `data/cc_src/<CODE>.md` | Hand-written parts 1-6, 8, 9 of each lesson |
| `data/build_core_course.py` | Assemble lessons, `00-START-HERE`, `99-LAST-48-HOURS` |
| `data/verify_core_course.py` | Structure, keys, balance, readability, difficulty metadata |
| `data/test_core_course.py` | `unittest` for the readability function and builder helpers |
| `core-course/*.md` | Generated output |
| `build_site.py` (parent dir) | Add the `core-course` section |

---

### Task 1: Vet the method sources

**Files:** Create `research/06-method-sources.md`

**Interfaces:** Produces the list of vetted sources that each lesson's part 9 cites. Each entry: id, URL, publisher, date (or "undated, inferred from X"), page type, verdict (used / not used), exactly what it supports.

- [ ] **Step 1: Candidate list.** Open each page itself (WebFetch or the built-in browser), not a search snippet:
  - Pseudocode: the Java Language Specification chapter on operators and evaluation order (docs.oracle.com/javase/specs); Oracle's Java Tutorials page on operators.
  - Grammar and writing: Purdue OWL (subject-verb agreement, articles, prepositions, tense); British Council LearnEnglish Grammar; Merriam-Webster usage notes where a rule is disputed.
  - Critical reasoning and reading comprehension: GMAC and ETS official free-prep pages (argument structure, strengthen/weaken/assumption; RC strategy).
  - Data sufficiency and logic sets: GMAC's published description of the data-sufficiency format; LSAC's published description of analytical-reasoning ("logic game") question types and diagramming.
  - Maths and series: Art of Problem Solving wiki; Khan Academy pages for ratios, linear equations, number sequences.
- [ ] **Step 2: For each page record** URL, publisher, date shown, page type (reference, tutorial, forum, sales page), what the page actually says that I will use, and verdict. A page that answers 200 but is an index, a soft 404, a sales page, or off-topic is **not used**.
- [ ] **Step 3: Write `research/06-method-sources.md`** as a table plus a short "what was rejected and why" list. State only what was observed.
- [ ] **Step 4: Verify** every URL in the file resolves and that each "used" row names a specific claim: `python3 data/check_links.py` must show no new dead link.

### Task 2: Lesson infrastructure (tests first)

**Files:** Create `data/cc_readability.py`, `data/test_core_course.py`, `data/build_core_course.py` (skeleton), `data/verify_core_course.py` (skeleton), `data/cc_practice.py` (skeleton).

**Interfaces:**
- Produces `cc_readability.readability(md: str) -> dict(words:int, sentences:int, avg_words:float, flesch:float)` and `cc_readability.prose(md: str) -> str`.
- Produces `cc_practice.PRACTICE: dict[str, Callable[[], dict[int, list[dict]]]]` (each question is a `gen_core.Q` dict with an optional `judgement: bool` and optional `diff: int`).
- Produces `build_core_course.LESSONS: list[tuple[int, str, str]]` = (order, code, slug) and `build_core_course.build(code) -> pathlib.Path`.

- [ ] **Step 1: Write the failing test** in `data/test_core_course.py`:

```python
import unittest, cc_readability as R

class ReadabilityTests(unittest.TestCase):
    def test_strips_code_tables_and_frontmatter(self):
        md = "---\ntitle: x\n---\n# H\n\nShort plain sentence here. Another one follows.\n\n```python\nprint(1)\n```\n\n| a | b |\n|---|---|\n"
        p = R.prose(md)
        self.assertNotIn("print", p); self.assertNotIn("title", p); self.assertNotIn("|", p)

    def test_counts_and_scores(self):
        r = R.readability("The cat sat on the mat. The dog ran to the park.")
        self.assertEqual(r["sentences"], 2); self.assertEqual(r["words"], 12)
        self.assertGreater(r["flesch"], 90)

    def test_hard_prose_scores_lower(self):
        easy = R.readability("It is easy. We can do it now.")["flesch"]
        hard = R.readability("Notwithstanding considerable epistemological complications, the aforementioned methodology necessitates comprehensive reconsideration.")["flesch"]
        self.assertLess(hard, easy)

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run to confirm it fails:** `cd data && python3 test_core_course.py` -> `ModuleNotFoundError: No module named 'cc_readability'`.
- [ ] **Step 3: Implement** `data/cc_readability.py`:

```python
"""Plain-language gate for the Core Course: strips everything that is not running prose, then measures it."""
import re

def prose(md: str) -> str:
    t = re.sub(r'(?s)\A---\n.*?\n---\n', '', md)
    t = re.sub(r'(?s)```.*?```', ' ', t)
    t = re.sub(r'(?m)^\s*\|.*$', ' ', t)
    t = re.sub(r'(?m)^#+\s.*$', ' ', t)
    t = re.sub(r'`[^`]*`', ' thing ', t)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = re.sub(r'(?m)^\s*(?:[-*+]|\d+[.)])\s+', '', t)
    return re.sub(r'[*_>]', '', t)

def _syll(w: str) -> int:
    w = w.lower()
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and not w.endswith(('le', 'ee')) and n > 1: n -= 1
    return max(n, 1)

def readability(md: str) -> dict:
    t = prose(md)
    sents = [s for s in re.split(r'(?<=[.!?])\s+|\n{2,}', t) if re.search(r'[A-Za-z]', s)]
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", t)
    if not sents or not words:
        return dict(words=0, sentences=0, avg_words=0.0, flesch=100.0)
    syl = sum(_syll(w) for w in words)
    asl, asw = len(words) / len(sents), syl / len(words)
    return dict(words=len(words), sentences=len(sents), avg_words=round(asl, 1),
                flesch=round(206.835 - 1.015 * asl - 84.6 * asw, 1))
```

- [ ] **Step 4: Run to confirm it passes:** `cd data && python3 test_core_course.py` -> `OK`.
- [ ] **Step 5: Skeletons.** Create `cc_practice.py` with `PRACTICE = {}` and a helper `judge(q, correct, wrong, why)` that wraps `bank_verbal.T(...)` and sets `judgement=True`. Create `build_core_course.py` with `LESSONS` (the 22 in spec order, numbered 01-22) and a `build(code)` that: reads `cc_src/<code>.md`, splits `## N.` sections, draws 15 questions from `PRACTICE[code]()`, computes `targets = letters_for(15, f"cc-{code}")`, renders each level with `render_questions(qs, seed, start=(lvl-1)*5+1, targets=targets[(lvl-1)*5:lvl*5])`, prefixes judgement keys with "*Judgement:* ", writes frontmatter via `lib_common.frontmatter(code, title, {'course': 'core', 'lesson': n})`, and writes `core-course/NN-<code>-<slug>.md`. Create `verify_core_course.py` with checks listed in Task 11.
- [ ] **Step 6: Run** `python3 data/test_core_course.py` -> `OK`; `python3 data/verify_core_course.py` -> reports 0 lessons found without crashing.

### Task 3: Three pilot lessons: Z2, G1, P4

**Files:** Create `data/cc_src/Z2.md`, `data/cc_src/G1.md`, `data/cc_src/P4.md`; modify `data/cc_practice.py` (+ `data/gen_puzzles.py`, `data/gen_code.py` if an L3 parameter is needed); output `core-course/01-...`, etc.

**Interfaces:** Consumes `lib_common.render_questions`, `lib_common.letters_for`, `gen_core.run`, `gen_puzzles.FAMILIES`, `gen_code.gen_incr` / `gen_trace`, `bank_verbal.T`. Produces the first three lesson files and the lesson procedure below.

**Lesson procedure (used by Tasks 3, 5-9; one lesson = these steps):**

- [ ] **Step 1: Read what exists for the topic:** its topic file in `topics/`, `puzzles/` or `pseudocode/`, its bank in `question-banks/`, its `QB-98` items (grep `topic \`CODE\``), and `data/src/<CODE>.md`. Note the patterns Infosys actually used.
- [ ] **Step 2: Method check against vetted sources** from Task 1 (open the cited page again if the method is a rule, not arithmetic). For arithmetic methods, verify by a short script.
- [ ] **Step 3: Write `data/cc_src/<CODE>.md`**: `## 1. The idea` / `## 2. What Infosys asks` / `## 3. The method` / `## 4. Shortcuts and when they fail` / `## 5. Worked examples` (five, with full working) / `## 6. Traps` / `## 8. Recap` / `## 9. Sources`. Plain words, every term defined at first use, no sentence over about 25 words.
- [ ] **Step 4: Write the practice builder** `PRACTICE[CODE]`: L1 five warm-ups, L2 five exam-level, L3 five beyond-exam (more steps or tighter distractors than the 2020 sample). Prefer generator families with a level parameter; each question has an independent `check()`; hand-written items use `judge(...)`.
- [ ] **Step 5: Build and verify:** `python3 data/build_core_course.py --only CODE && python3 data/verify_core_course.py --only CODE` -> `PASS`.
- [ ] **Step 6: Read the lesson once as a beginner** (open the file) and fix anything that assumes knowledge not yet defined.

- [ ] **Step 7: Pilot lessons.** Run the procedure for Z2 (generators `pair`, `figure`, `cubebox`, `zigzag`, L3 = rules that need two steps), G1 (hand-written cloze items with `judge`, L3 = two plausible words that differ in collocation), P4 (generator `gen_incr`, L3 = three increment terms and a loop; verified in Java).
- [ ] **Step 8: Recalibrate the readability gate** from the three pilots (record the numbers and the final thresholds in `verify_core_course.py`).
- [ ] **Step 9: Run** `python3 data/test_core_course.py && python3 data/verify_core_course.py` -> `PASS` for the three lessons.

### Task 4: Checkpoint with Hari

- [ ] **Step 1:** Send the three pilot files to Hari with their word counts and readability numbers and ask whether they are easy enough and the right depth. **Stop here until Hari answers.** Apply the feedback to the template, `cc_src` files and gate before Task 5.

### Task 5: Reasoning and puzzles, 8 lessons: A1 A2 A3 A4 A5 A6 A21 Z1

**Files:** `data/cc_src/{A1,A2,A3,A4,A5,A6,A21,Z1}.md`; extend `data/cc_practice.py`. **Interfaces:** consumes the generators `gen_reasoning` (`gen_ds`, `gen_conditional`, `gen_deductive`, series families), `gen_puzzles` (`row3`, `row4`, `gridsums`, `sumgrid`, `kakuro`), `gen_quant`. Run the lesson procedure once per code. A6 uses `gen_ds` on the 1-2-3-4 scale; A4 uses `gen_deductive` plus a Venn-style method; A21 is judged from the vetted source (pattern families only) because no Infosys item exists.

- [ ] **Step 1-8:** one lesson each via the procedure; after each, `python3 data/verify_core_course.py --only CODE` -> `PASS`.

### Task 6: Technical, 2 lessons: A7 A8

**Files:** `data/cc_src/{A7,A8}.md`; extend `data/cc_practice.py`. A7 data interpretation uses the existing table generator; A8 uses linear-equation and ages generators. Each answer re-derived with `fractions.Fraction`.

- [ ] **Step 1-2:** one lesson each via the procedure.

### Task 7: Verbal, 4 lessons: V1 V2 V3 V6

**Files:** `data/cc_src/{V1,V2,V3,V6}.md`. All practice is hand-written with `judge(...)`; V6 methods from the vetted GMAC/ETS pages; V2 and V3 rules cross-checked against two vetted grammar sources. Reading passages are original.

- [ ] **Step 1-4:** one lesson each via the procedure; keys labelled judgement.

### Task 8: Grammar and writing, 2 lessons: G2 W1

**Files:** `data/cc_src/{G2,W1}.md`. G2 practice hand-written (`judge`), W1 has a model essay and a model email with a scoring checklist instead of MCQs (three levels = three prompts of rising difficulty, five check-points each).

- [ ] **Step 1-2:** one lesson each; for W1 the verifier checks the presence of the checklist rather than keys.

### Task 9: Pseudocode, 3 lessons: P1 P3 P5

**Files:** `data/cc_src/{P1,P3,P5}.md`. Traces printed in the official dialect via `gen_code.render_official`; every answer is run in Java using `gen_code.java_batch_text`. P3 bitwise questions are run in Java.

- [ ] **Step 1-3:** one lesson each via the procedure; `python3 data/verify_generated.py` still passes.

### Task 10: Start-here and last-48-hours pages

**Files:** Modify `data/build_core_course.py`.

- [ ] **Step 1:** Generate `core-course/00-START-HERE.md` from `weightage.json`: the test at a glance, the 22 lessons in recommended order with marks and hours, how to use a lesson (read, do L1, L2, L3, read the recap), and a 60-minute diagnostic (two questions from each section's L2 sets, with a scoring table that points to the lessons to do first).
- [ ] **Step 2:** Generate `core-course/99-LAST-48-HOURS.md`: what to re-read (all 22 recaps, concatenated from part 8), what to practise, what to skip, test-day rules.
- [ ] **Step 3:** `python3 data/build_core_course.py` builds all 24 files; `python3 data/verify_core_course.py` -> `PASS`.

### Task 11: Verify, integrate, republish

**Files:** Modify `data/verify_core_course.py`, `data/run_all_verifiers.sh`, `data/build_docs.py`, `build_site.py`, `research/04-qa-report.md`, `PROGRESS.md`.

- [ ] **Step 1: Verifier checks** (`verify_core_course.py` must assert): 22 lesson files + 2 pages exist; every lesson has parts 1-9; exactly 15 questions and 15 keys; letters balanced (no letter above 40% of 15) and not a repeating cycle; every non-judgement practice question had a passing `check()`; every lesson's prose passes the readability gate; every URL in part 9 appears in `research/06-method-sources.md` with verdict "used"; L3 declared difficulty is not below L2 where `diff` is set; no copied sentence from the official sample (a 12-word-run overlap test against the PDF text in the scratchpad when present).
- [ ] **Step 2:** Add `verify_core_course.py` to `run_all_verifiers.sh`; add the Core Course to `build_docs.py`'s master index (first entry under "highest-value files"); in `build_site.py` add `("core-course", "Core Course: start here")` to `SECTION_ORDER` right after `("", "Start here")`.
- [ ] **Step 3: Run everything:** `bash data/run_all_verifiers.sh` -> exit 0; `python3 data/check_links.py` -> no new dead link; `cd .. && python3 build_site.py && python3 verify_site.py && python3 build_artifact.py` -> all checks pass.
- [ ] **Step 4: Republish** to the same artifact URL (`https://claude.ai/artifact/WDiiHkYG2c4g4kPXD818kq`) with the artifact files, label "v3: Core Course".
- [ ] **Step 5: Record**: update `research/04-qa-report.md` (new numbers, defects found), `PROGRESS.md`, and the memory file `infosys-se-prep-library.md`.
- [ ] **Step 6: Report to Hari:** what was built, what was verified by execution vs judgement, sources used and rejected, limits.

## Self-review

- **Spec coverage:** 22 lessons (Tasks 3, 5-9); start-here and last-48-hours (Task 10); lesson format and three practice levels (Tasks 2, 3); sources vetted (Task 1, enforced in Task 11); readability gate (Tasks 2, 3, 11); verification and republish (Task 11); pilot checkpoint (Task 4). No gaps.
- **Placeholders:** none; infrastructure code is given in full; per-lesson content is written during execution under the stated procedure, which is concrete.
- **Type consistency:** `readability()` returns `words, sentences, avg_words, flesch` everywhere; `PRACTICE[code]()` returns `{1,2,3: [Q]}`; `LESSONS` is `(order, code, slug)`.
