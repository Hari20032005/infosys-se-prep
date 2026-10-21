#!/usr/bin/env python3
"""Generate the navigation documents from weightage.json and filemap.json so they cannot drift:
02-TOPIC-WEIGHTAGE-ANALYSIS.md, 00-MASTER-INDEX.md, and the folder indexes
(aptitude/00-INDEX.md, puzzles/00-INDEX.md, pseudocode/00-INDEX.md, interview/00-INDEX.md).
    python3 data/build_docs.py
"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lib_common import *

FM = json.loads((ROOT / 'data' / 'filemap.json').read_text())
BK = FM.get('_banks', {})


def banks(code):
    out = list(BK.get(code, []))
    if f'QB-{code}' in FM:
        out.append(FM[f'QB-{code}'])
    return out


def link(path, label=None, frm='.'):
    rel = pathlib.PurePosixPath(path)
    base = pathlib.PurePosixPath(frm)
    import os
    r = os.path.relpath(path, frm)
    return f"[{label or rel.name}]({r})"


def tfile(code):
    return FM.get(code)


def row_files(code, frm='.'):
    f = tfile(code)
    b = banks(code)
    s = link(f, code, frm) if f else code
    if b:
        s += ' · ' + ' · '.join(link(x, 'bank', frm) for x in b)
    return s


def analysis():
    T = W['topics']
    L = ["# 02 — Topic Weightage Analysis\n",
         "How the 75 scored marks are expected to fall across subtopics, and what to study first. Every number is generated from `data/weightage.json` (itself produced by `data/analyze.py` from the observed questions and accounts); the full method and the ROI table are in `data/analysis-tables.md`. **Treat this as a study-priority guide, not a syllabus**: the 2027-batch test has not been reported by anyone yet, and the per-section counts rest on one first-hand account plus coaching sources that may share a source.\n",
         "## 1. The paper this library plans for\n",
         "| # | Section | Questions | Marks | Minutes |\n|---|---|---|---|---|",
         "| 1 | Reasoning Ability | 15 | 15 | 25 |", "| 2 | Technical Ability (mathematical) | 10 | 10 | 35 |", "| 3 | Verbal Ability | 20 | 20 | 20 |",
         "| 4 | Pseudocode | 5 | 10 | 10 |", "| 5 | Numerical Puzzle | 4 | 10 | 10 |", "| 6 | English Grammar | 5 | 10 | 10 |", "| 7 | English Writing | 1 | unpublished | 10 |",
         "| | **Total** | **60** | **75 + essay** | **120** |\n",
         "Every section has its own cut-off (value unknown). No coding. No calculator. No negative marking reported. Source and confidence: `research/03-pattern-synthesis.md` §1–§2 (Medium).\n",
         "## 2. Tiers\n",
         f"Tiers compare each subtopic's expected marks per study hour with this paper's own average ({W['mean_roi']:.2f}). Because every section has a cut-off, the best-value topics in each section are lifted to at least Tier 2 (the *section floor*). Low-confidence topics are capped at Tier 3 before the floor.\n"]
    for tt in (1, 2, 3, 4):
        g = [t for t in T if t['tier'] == tt]
        em = sum(t['est_marks'] or 0 for t in g); hh = sum(t['hours'] for t in g)
        L.append(f"### Tier {tt} — {len(g)} subtopics · {em:.1f} expected marks · {hh:.1f} hours\n")
        L.append("| Code | Subtopic | Section | Marks | Hours | Confidence | File and bank |\n|---|---|---|---|---|---|---|")
        for t in sorted(g, key=lambda t: -(t['est_marks'] if t['est_marks'] is not None else 99)):
            m = f"{t['est_marks']:.1f}" if t['est_marks'] is not None else 'gate'
            L.append(f"| {t['code']} | {t['label']} | {block(t['code'])} | {m} | {t['hours']} | {t['conf']} | {row_files(t['code'])} |")
        L.append('')
    L.append("### Interview stage\n")
    L.append("| Code | Theme | Questions seen | Accounts | Tier | Hours | File |\n|---|---|---|---|---|---|---|")
    for t in W['interview_topics']:
        L.append(f"| {t['code']} | {t['label']} | {t['questions']} | {len(t['accounts'])} | T{t['tier']} | {t['hours']} | {row_files(t['code'])} |")
    allh = sum(t['hours'] for t in T); ih = sum(t['hours'] for t in W['interview_topics'])
    L += ['', f"**Full coverage costs {allh:.1f} hours for the test and {ih:.1f} for the interview.** `99-STUDY-PLAN.md` says what to drop when you have less.\n",
          "## 3. Where the evidence is thin\n",
          f"- **{sum(1 for t in T if t['observed'] + t['discarded_sightings'] == 0)} of {len(T)} subtopics have no observed question**; their share is an allocation from syllabus lists. Verbal and Grammar (30 of 75 marks) rest on one observed item.",
          "- The observed pool is 60 questions from coaching videos and one first-hand account. Each is `[REPORTED]` at best.",
          "- Repeat rate: 3 of 60 questions (5.0%) were presented independently by two channels. Repeats across test slots cannot be measured, so there is no Infosys equivalent of the Accenture repeat figure.",
          "- Coding is not in the Systems Engineer test (eight sources). It appears only in the optional upgrade test, which this library does not cover.",
          "- The Numerical Puzzle section in 2025–26 is grid-number reasoning; the classic brain-teaser collections that circulate under “Infosys puzzles” describe an older test and were deliberately not used.\n",
          "## 4. How this was produced\n",
          "`data/analyze.py` reads `questions-observed.csv`, `questions-discarded.csv`, `reviews-online.csv` and `syllabus-claims.csv`; weights sightings by `sqrt` so one heavily-filmed topic cannot swamp the rest; runs ROI on expected **marks** (three sections carry two marks a question); and checks that sections reconcile to 60 questions and 75 marks. Change `SECTIONS` there to test another structure and rerun.\n"]
    (ROOT / '02-TOPIC-WEIGHTAGE-ANALYSIS.md').write_text('\n'.join(L), encoding='utf-8')


def folder_index(folder, title, intro, codes, extra=''):
    L = [f"# {title}\n", intro + '\n', "| Code | Topic | Tier | Files |\n|---|---|---|---|"]
    for c in codes:
        t = TOP.get(c) or IVT.get(c)
        L.append(f"| {c} | {t['label']} | T{t['tier']} | {row_files(c, folder)} |")
    (ROOT / folder / '00-INDEX.md').write_text('\n'.join(L) + '\n' + extra, encoding='utf-8')


def aptitude_index():
    order = [  # study order: highest value and cheapest first
        ('1', ['A2', 'A1', 'A8', 'A7'], 'Tier 1: the reasoning and maths items Infosys is reported to ask every time.'),
        ('2', ['A3', 'A5', 'A6', 'A9', 'A11'], 'Tier 2: short topics with a method you can learn in under an hour each.'),
        ('3', ['A4'], 'Tier 3: recognise and attempt.'),
        ('4', ['A12', 'A13', 'A14', 'A15', 'A17', 'A10', 'A16', 'A18', 'A19', 'A20', 'A21'], 'Tier 4: only if time remains. If you finished the L&T aptitude, you have already done A12–A15, A17 and A19.'),
    ]
    L = ["# Aptitude — what to study and in what order\n",
         "The aptitude block is **Reasoning Ability (15 Q, 25 min) + Technical Ability (10 Q, 35 min)**: 25 marks. Sources disagree on which topic sits in which half, so this library prepares them as one 25-question block. If you have already done the L&T aptitude (the topic files copied here from that library), skip the files marked **copied** and spend the time on those marked **new**.\n",
         "Three method guides cover the whole of aptitude and verbal; read the one for your weakest block first:\n",
         "- [Quant from zero](00-QUANT-FROM-ZERO.md) · [Logical from zero](00-LOGICAL-FROM-ZERO.md) · [Verbal from zero](00-VERBAL-FROM-ZERO.md)\n"]
    for n, codes, why in order:
        L.append(f"## Step {n}\n\n{why}\n")
        L.append("| Code | Topic | Hours | Origin | Files |\n|---|---|---|---|---|")
        for c in codes:
            t = TOP[c]
            L.append(f"| {c} | {t['label']} | {t['hours']} | {'copied' if t['reuse'] else '**new**'} | {row_files(c, 'aptitude')} |")
        L.append('')
    L.append("**Mock first, then drill.** After Step 1, sit `MOCK-01` (`../question-banks/MOCK-01.md`) and let the score sheet tell you which step to repeat.\n")
    (ROOT / 'aptitude' / '00-INDEX.md').write_text('\n'.join(L), encoding='utf-8')


def master():
    L = ["# 00 — Master Index: Infosys Systems Engineer (Trainee), campus 2026-27\n",
         "A self-contained preparation library built from evidence, not from memory. **Start with `99-STUDY-PLAN.md`** and the days you have left.\n",
         "## What the test is (planning model, confidence Medium)\n",
         "Seven timed sections, **60 questions, 120 minutes, 75 marks plus an essay**, in person on the college lab computers, **no coding**, **no calculator**, a cut-off in every section. Details, the evidence and the conflicts: `research/03-pattern-synthesis.md`.\n",
         "## Read these first\n",
         "| File | Why |\n|---|---|",
         "| [99-STUDY-PLAN.md](99-STUDY-PLAN.md) | 3-, 7- and 14-day plans keyed to days left |",
         "| [01-APPLICATION-CHECKLIST.md](01-APPLICATION-CHECKLIST.md) | The Application Form arrives at your personal email; the invite depends on it |",
         "| [03-TEST-STRATEGY.md](03-TEST-STRATEGY.md) | Time per question, what to do first in the room |",
         "| [02-TOPIC-WEIGHTAGE-ANALYSIS.md](02-TOPIC-WEIGHTAGE-ANALYSIS.md) | Tiers, hours, files |",
         "| [91-CHEATSHEET.md](91-CHEATSHEET.md) | One-page revision, every claim machine-checked |",
         "| [90-RESOURCE-LIBRARY.md](90-RESOURCE-LIBRARY.md) | Free practice, every link verified |\n",
         "## Folders\n",
         "| Folder | Contents |\n|---|---|",
         "| [aptitude/](aptitude/00-INDEX.md) | Study order for reasoning and maths, three from-zero guides |",
         "| [puzzles/](puzzles/00-INDEX.md) | The Numerical Puzzle section: number grids and pair/figure rules |",
         "| [pseudocode/](pseudocode/00-INDEX.md) | Loops, recursion, bitwise, arrays, increments, OOP tracing; the Infosys dialect |",
         "| [topics/](aptitude/00-INDEX.md) | Verbal, grammar, writing and aptitude topic files (one per subtopic) |",
         "| [interview/](interview/00-INDEX.md) | Format, Infosys-specific facts, technical, HR, projects, generative AI, light coding |",
         "| [core-course/](core-course/00-START-HERE.md) | The Core Course: 22 lessons, a diagnostic, and the last-48-hours revision page |",
         "| [question-banks/](question-banks/QB-99-OBSERVED-POOL.md) | Observed pool, one bank per topic, the full mock and its answers |",
         "| [research/](research/03-pattern-synthesis.md) | Official terms, research log, pattern synthesis, QA report, source-credibility review |",
         "| data/ | CSVs, generators, verifiers, `weightage.json` |\n",
         "## The highest-value files\n",
         "0. **[Core Course: start here](core-course/00-START-HERE.md)**: 22 short, plain-language lessons on the topics that carry about 58 of the 75 marks, each with three levels of practice. Begin here.",
         "1. [QB-98-OFFICIAL-SAMPLE-SOLVED.md](question-banks/QB-98-OFFICIAL-SAMPLE-SOLVED.md): Infosys's own sample paper (2020), 54 questions solved here; the only first-party question text there is. Read [the source review](research/05-source-credibility.md) for why websites that sell \"previous year questions\" were not used.",
         "2. [QB-99-OBSERVED-POOL.md](question-banks/QB-99-OBSERVED-POOL.md): the 60 questions candidates reported, each solved and executed.",
         "3. [MOCK-01.md](question-banks/MOCK-01.md): a full-length mock in the observed structure; answers in [MOCK-01-ANSWERS.md](question-banks/MOCK-01-ANSWERS.md).",
         "4. [Z2](puzzles/Z2-pair-and-figure-rules.md) and [Z1](puzzles/Z1-number-grids-and-matrices.md): the puzzle section is 10 marks and the one most candidates fail.",
         "5. [G2](topics/G2-grammar-tense-articles-prepositions.md), [G1](topics/G1-fill-in-the-blanks-and-cloze.md), [V2](topics/V2-spotting-errors-and-grammar-rules.md), [W1](topics/W1-english-writing.md): 30 marks of English that coaches say sinks candidates.\n",
         "## How much to trust it\n",
         "Tags used throughout: `[CONFIRMED]` three or more independent sources or an official document; `[LIKELY]` two; `[REPORTED]` one; `[INFERRED]`; `[UNVERIFIED — model inference]`. The 2027-batch test has not been reported by anyone, so every section figure carries Medium confidence at best. The cut-off value is not discoverable. See the open gaps in `research/03-pattern-synthesis.md` §10.\n"]
    (ROOT / '00-MASTER-INDEX.md').write_text('\n'.join(L), encoding='utf-8')


def main():
    analysis()
    folder_index('puzzles', 'Numerical Puzzle — index',
                 "The Numerical Puzzle section: **4 questions, 10 minutes, 10 marks** (two worth 2, two worth 3) `[REPORTED]`. Coaches say it and verbal are where most candidates miss the cut-off. Study Z2 first (ten of the fifteen observed puzzles), then Z1.\n\n"
                 "**The 60-second method:** (1) look at the shape; (2) fit the rule on the first line; (3) confirm on the second; (4) apply to the last; (5) cap at 2.5 minutes and guess by last digit.\n", ['Z2', 'Z1'])
    folder_index('pseudocode', 'Pseudocode — index',
                 "Pseudocode: **5 questions, 10 minutes, 10 marks** (2 each) `[LIKELY]`. Infosys shows C/Java-like code with `Set integer`, `mod` or `%`, `++`/`--`, and `Display`/`Print`; P4 sets out the dialect and how it differs from the Accenture style used in P1, P2, P3, P5–P8, P10. Each file here has two banks where one exists: the Accenture-style bank and, for P1, an Infosys-dialect trace bank.\n",
                 ['P1', 'P4', 'P3', 'P5', 'P2', 'P6', 'P7', 'P8', 'P9', 'P10'])
    folder_index('interview', 'Interview — index',
                 "Start with [00-INTERVIEW-FORMAT.md](00-INTERVIEW-FORMAT.md) (what is known) and [00-INFOSYS-SPECIFIC.md](00-INFOSYS-SPECIFIC.md) (training, joining terms, upgrade path: each fact tagged). Supporting files: [IV5a STAR stories](IV5a-star-stories.md) and [IV5b technology flexibility](IV5b-technology-flexibility.md). Added from the Reddit pass of 2026-10-03: [00-AFTER-SELECTION.md](00-AFTER-SELECTION.md) (offer-letter wait, Mysore pre-test and FA exams) and [00-UPGRADE-TRACK.md](00-UPGRADE-TRACK.md) (what DSE/SP candidates report; a different test from the SE test).\n",
                 ['IV1', 'IV2', 'IV5', 'IV4', 'IV3', 'IV6', 'IV7'])
    aptitude_index()
    master()
    print('wrote 02-TOPIC-WEIGHTAGE-ANALYSIS, 00-MASTER-INDEX, aptitude/puzzles/pseudocode/interview 00-INDEX')


if __name__ == '__main__':
    main()
