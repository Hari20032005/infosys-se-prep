#!/usr/bin/env python3
"""Assemble the Core Course: core-course/NN-<code>-<slug>.md from data/cc_src/<CODE>.md (hand-written parts) plus the
practice sets in data/cc_practice.py (parts 7). Also 00-START-HERE and 99-LAST-48-HOURS.

    python3 data/build_core_course.py [--only CODE]
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lib_common import ROOT, TOP, W, block, frontmatter, letters_for, render_questions
import cc_practice as CP

SRC = ROOT / 'data' / 'cc_src'
OUT = ROOT / 'core-course'

# (order, code, slug, title)   -- the recommended study order
LESSONS = [
    (1, 'Z2', 'pair-and-figure-puzzles', 'Pair and figure puzzles'),
    (2, 'Z1', 'number-grids', 'Number grids and matrices'),
    (3, 'A2', 'number-and-letter-series', 'Number and letter series'),
    (4, 'A1', 'coding-and-decoding', 'Coding and decoding'),
    (5, 'A6', 'data-sufficiency', 'Data sufficiency'),
    (6, 'A4', 'syllogisms-and-deduction', 'Syllogisms and logical deduction'),
    (7, 'A3', 'operator-logic', 'Operator logic and equation balancing'),
    (8, 'A5', 'blood-relations', 'Blood relations'),
    (9, 'A21', 'non-verbal-reasoning', 'Non-verbal reasoning'),
    (10, 'A7', 'data-interpretation', 'Data interpretation'),
    (11, 'A8', 'linear-equations-and-ages', 'Linear equations, ages and heads-and-legs'),
    (12, 'G1', 'cloze-and-fill-in-the-blanks', 'Cloze and fill in the blanks'),
    (13, 'G2', 'tenses-articles-prepositions', 'Tenses, articles and prepositions'),
    (14, 'V2', 'spotting-errors', 'Spotting errors and grammar rules'),
    (15, 'V3', 'sentence-correction', 'Sentence correction and completion'),
    (16, 'V1', 'reading-comprehension', 'Reading comprehension'),
    (17, 'V6', 'critical-reasoning', 'Critical reasoning'),
    (18, 'W1', 'essay-and-email', 'The essay and the email'),
    (19, 'P1', 'loops-and-traces', 'Loops and trace tables'),
    (20, 'P4', 'increment-operators', 'Pre- and post-increment'),
    (21, 'P3', 'bitwise-operators', 'Bitwise operators'),
    (22, 'P5', 'arrays', 'Arrays'),
]
BY_CODE = {c: (n, slug, title) for n, c, slug, title in LESSONS}
REQUIRED_SRC = (1, 2, 3, 4, 5, 6, 8, 9)
LEVELS = {1: 'Level 1: warm-up', 2: 'Level 2: exam level', 3: 'Level 3: beyond the exam'}


def split_sections(text: str) -> dict:
    parts = [p for p in re.split(r'(?m)^(?=## \d+\. )', text) if p.strip()]
    return {int(re.match(r'## (\d+)\.', p).group(1)): p.rstrip('\n') + '\n' for p in parts if re.match(r'## (\d+)\.', p)}


def core_letters(code: str) -> list:
    """Balanced answer letters for the 15 questions, never a repeating cycle and never the same letter three times running."""
    for salt in range(300):
        t = letters_for(15, f'cc-{code}' + (f'-{salt}' if salt else ''))
        if not any(t[i] == t[i + 1] == t[i + 2] for i in range(13)):
            return t
    raise RuntimeError(f'{code}: no letter order without a run of three')


def practice_markdown(code: str, level_notes: dict) -> tuple[str, list]:
    """Part 7: three levels of five questions and one answer key. Returns (markdown, letters used)."""
    sets = CP.PRACTICE[code]()
    targets = core_letters(code)
    blocks, keys, used = [], [], []
    for lvl in (1, 2, 3):
        qs = []
        for q in sets[lvl]:
            q = dict(q)
            if q.get('judgement'):
                q['why'] = '*Judgement:* ' + q['why']
            qs.append(q)
        qmd, kmd, u = render_questions(qs, f'cc-{code}-L{lvl}', start=(lvl - 1) * 5 + 1, targets=targets[(lvl - 1) * 5: lvl * 5])
        note = level_notes.get(lvl, '')
        blocks.append(f"### {LEVELS[lvl]}\n\n" + (f"{note}\n\n" if note else '') + qmd)
        keys.append(kmd)
        used += u
    md = ("## 7. Practice questions\n\nAttempt each level before opening the key. Level 3 is harder than anything in the 2020 official sample, on purpose: "
          "if you can do Level 3, the real paper will feel easy.\n\n" + '\n'.join(blocks) + "\n### ANSWER KEY\n\n" + '\n'.join(keys) + '\n')
    return md, used


def level_notes_of(sections: dict) -> dict:
    """Optional `<!-- L3: ... -->` comments in part 6 or 7 of the source give the one-line reason each level is harder."""
    notes = {}
    for lvl in (1, 2, 3):
        m = re.search(rf'<!--\s*L{lvl}:\s*(.*?)\s*-->', '\n'.join(sections.values()), re.S)
        if m:
            notes[lvl] = f"*{m.group(1).strip()}*"
    return notes


def lesson_text(code: str) -> str:
    n, slug, title = BY_CODE[code]
    t = TOP[code]
    src = split_sections((SRC / f'{code}.md').read_text(encoding='utf-8'))
    missing = set(REQUIRED_SRC) - set(src)
    assert not missing, f"{code}: cc_src is missing parts {sorted(missing)}"
    prac, _ = practice_markdown(code, level_notes_of(src))
    # a Markdown line break (two trailing spaces) after the question line and after every option, so the options stack instead of running together
    prac = re.sub(r'(?m)^(\*\*\d+\.\*\* .*?|[a-d]\) .*?)[ ]*$', lambda m: m.group(1) + '  ', prac)
    marks = f"about {t['est_marks']:.1f} of the 75 marks" if t['est_marks'] is not None else 'a pass/fail gate'
    head = (frontmatter(code, title, {'course': 'core', 'lesson': n}) +
            f"\n# Lesson {n:02d}. {title}\n\n"
            f"*Topic `{code}` · {marks} · plan about {t['hours']} hours.*\n")
    body = [src[1], src[2], src[3], src[4], src[5], src[6], prac, src[8], src[9]]
    text = head + '\n' + '\n'.join(re.sub(r'<!--\s*L\d:.*?-->\n?', '', b, flags=re.S) for b in body)
    text = re.sub(r'(?m)^ {2,3}([-*] )', r'    \1', text)          # the site's Markdown engine needs four spaces to nest a list
    return text.rstrip('\n') + '\n'


def build(code: str, write: bool = True) -> str:
    text = lesson_text(code)
    if write:
        n, slug, _ = BY_CODE[code]
        OUT.mkdir(exist_ok=True)
        (OUT / f'{n:02d}-{code}-{slug}.md').write_text(text, encoding='utf-8')
    return text


def lesson_file(code: str) -> str:
    n, slug, _ = BY_CODE[code]
    return f'{n:02d}-{code}-{slug}.md'


def recap_of(code: str) -> str:
    src = split_sections((SRC / f'{code}.md').read_text(encoding='utf-8'))
    return re.sub(r'(?m)^## 8\..*\n+', '', src[8]).strip()


# the 12 diagnostic questions: Level 2, question 6 of each named lesson (the first Level 2 question)
DIAGNOSTIC = [('Numerical puzzles', ['Z2', 'Z1']), ('Reasoning', ['A2', 'A4']), ('Technical (maths)', ['A7', 'A8']),
              ('Verbal', ['V2', 'V6']), ('Grammar', ['G2', 'G1']), ('Pseudocode', ['P1', 'P3'])]


def start_here() -> str:
    tot_marks = sum(TOP[c]['est_marks'] or 0 for _, c, _, _ in LESSONS)
    tot_hours = sum(TOP[c]['hours'] for _, c, _, _ in LESSONS)
    rows = '\n'.join(f"| {n} | [{title}]({lesson_file(c)}) | {block(c)} | {('%.1f' % TOP[c]['est_marks']) if TOP[c]['est_marks'] is not None else 'gate'} | {TOP[c]['hours']} |"
                     for n, c, _, title in LESSONS)
    diag = '\n'.join(f"| {sec} | " + ' · '.join(f"[{BY_CODE[c][2]}, Level 2, question 6]({lesson_file(c)})" for c in cs) + " |" for sec, cs in DIAGNOSTIC)
    return f"""---
title: Core Course. Start here
course: core
---

# Core Course: start here

*Twenty-two short lessons on the topics that carry about {tot_marks:.0f} of the 75 marks. Reading and practice take about {tot_hours:.0f} hours in all.*

## What this is

Every lesson explains one topic in plain words, shows the method, works five examples through, and then gives you 15 practice questions in three levels. Level 3 is harder than anything in the 2020 official sample, on purpose. Every answer to a number, logic or code question was checked by running code; the English questions are marked as judgement and tied to a page I opened and read.

The lessons are in a good order for most people, but you do not have to go straight through. Use the diagnostic below to find where to start.

## The test at a glance

The planning model is **7 timed sections, 60 questions, 120 minutes, 75 marks plus an essay**: reasoning 15, technical (maths) 10, verbal 20, pseudocode 5, numerical puzzle 4, grammar 5, writing 1 `[LIKELY]`. Every section has its own cut-off, the value is not known, there is no coding and no calculator `[CONFIRMED]`. The full evidence is in [the pattern synthesis](../research/03-pattern-synthesis.md). Nobody has yet reported the 2027-batch test itself, so the section counts are the best current estimate and not a promise.

Candidates who posted on Reddit about the October 2025 drives call the written test easy, and two of them say puzzles and pseudocode are where people miss a section cut-off `[REPORTED]`. That fits the model above and changes no lesson. The method and the limits are in [the Reddit research](../research/07-reddit-arctic-shift.md).

## How to use a lesson

1. Read the **idea** and **what Infosys actually asks** (five minutes).
2. Read the **method** and the **shortcuts**, then follow the five worked examples with a pencil.
3. Do **Level 1**. If you miss more than one, re-read the method.
4. Do **Level 2** against the clock. This is the level of the real test.
5. Do **Level 3** when Level 2 feels easy.
6. Last, read the **60-second recap**. Come back to it the night before.

## A 30-minute diagnostic

Do these 12 questions in 30 minutes, with no help. They are the first Level 2 question of each lesson named. Check the answers in each lesson's key.

| Section | The questions |
|---|---|
{diag}

Score each section out of 2. If you got **0**, do that section's lessons first, in order. If you got **1**, do them after the first group. If you got **2**, read the recaps and go straight to Level 3.

## The 22 lessons, in the recommended order

| # | Lesson | Section | Marks | Hours |
|---|---|---|---|---|
{rows}

*Marks and hours come from the library's weightage analysis (`../02-TOPIC-WEIGHTAGE-ANALYSIS.md`). They are estimates, not promises.*

## After the test

Selection is not the end. Candidates report a long and uneven wait for the offer letter, and a pre-test in the first week at Mysuru that covers aptitude, English, Java, DBMS and OOP. When you have time, read [what happens after you are selected](../interview/00-AFTER-SELECTION.md). The optional DSE and SP upgrade is a different, coding-heavy test; [what candidates report about it](../interview/00-UPGRADE-TRACK.md) is there so you can decide whether to try it.

## When time is short

- **Three days left:** do the Tier 1 lessons (the first column of the weightage analysis) and read the recap of every other lesson.
- **A week left:** do all the lessons once, Level 2 only, and then go to [the last 48 hours](99-LAST-48-HOURS.md) page.
- **Two days left:** go straight to [the last 48 hours](99-LAST-48-HOURS.md).

For a day-by-day plan see [the study plan](../99-STUDY-PLAN.md); for what is still unknown see [the pattern synthesis](../research/03-pattern-synthesis.md) §10.
"""


def last_48() -> str:
    blocks = '\n'.join(f"### {n}. {title}\n\n{recap_of(c)}\n\n[Open the lesson]({lesson_file(c)})\n" for n, c, _, title in LESSONS)
    return f"""---
title: Core Course. The last 48 hours
course: core
---

# The last 48 hours

*Do not start new topics now. Revise, practise under the clock, and rest.*

## What to do

1. **Read the 22 recaps below once** (about 40 minutes). They are the 60-second recaps from the lessons, in order.
2. **Do Level 2 of your three weakest lessons** against the clock. Your diagnostic score or your last mock tells you which.
3. **Do one full mock** under section timers: [MOCK-01](../question-banks/MOCK-01.md). Mark it with [the answers](../question-banks/MOCK-01-ANSWERS.md).
4. **Skip Level 3 now.** It builds skill over days, not hours.
5. **Sleep.** An extra hour of sleep helps more than an extra hour of study.

## What is known about the day

These facts come from the official guidelines for the 2026 batch `[CONFIRMED — official]` unless marked otherwise (see [the pattern synthesis](../research/03-pattern-synthesis.md) §2).

- The test is in person, in the college computer labs, on Infosys's own platform. You may keep stationery, but **no calculator** and no phone.
- Log in within **15 minutes** of your slot or you lose the test.
- Carry your **original college ID and a government photo ID**.
- Every section has its own cut-off, so never abandon a section to save another. The cut-off value is not known.
- No coding in this test. No negative marking has been reported `[LIKELY]`.
- Sections are reported to be timed one after another, with no return to an earlier section `[LIKELY]`. Prepare for the stricter version.

## The recaps

{blocks}
"""


def available() -> list:
    return [c for _, c, _, _ in LESSONS if (SRC / f'{c}.md').exists()]


def main(argv):
    only = argv[argv.index('--only') + 1] if '--only' in argv else None
    codes = [only] if only else available()
    for c in codes:
        build(c)
        print(f"built lesson {BY_CODE[c][0]:02d} {c}")
    if not only and len(codes) == len(LESSONS):
        (OUT / '00-START-HERE.md').write_text(start_here(), encoding='utf-8')
        (OUT / '99-LAST-48-HOURS.md').write_text(last_48(), encoding='utf-8')
        print('built 00-START-HERE and 99-LAST-48-HOURS')
    print(f"{len(codes)} lesson(s) built into {OUT.relative_to(ROOT)}/")


if __name__ == '__main__':
    main(sys.argv[1:])
