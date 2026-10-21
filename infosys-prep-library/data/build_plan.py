#!/usr/bin/env python3
"""99-STUDY-PLAN.md: 3-, 7- and 14-day plans. Hours for every topic come from weightage.json, so the
day totals are arithmetic, not guesses. Extras (mock, review, rehearsal) carry explicit hours.
    python3 data/build_plan.py
"""
import json, os, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lib_common import *

FM = json.loads((ROOT / 'data' / 'filemap.json').read_text())
HRS = {t['code']: t['hours'] for t in W['topics']}
HRS.update({t['code']: t['hours'] for t in W['interview_topics']})
LABEL = {t['code']: t['label'] for t in W['topics']}
LABEL.update({t['code']: t['label'] for t in W['interview_topics']})
COPIED = {t['code'] for t in W['topics'] if t['reuse']}
BOOKED = set()


def lk(c):
    f = FM.get(c)
    return f"[{c}]({f})" if f else c


def day(n, title, codes, extras):
    h = sum(HRS[c] for c in codes) + sum(x[1] for x in extras)
    for c in codes: BOOKED.add(c)
    L = [f"### Day {n} — {title} · {h:.1f} h\n", "| What | Hours |\n|---|---|"]
    for c in codes:
        L.append(f"| {lk(c)} {LABEL[c]} | {HRS[c]} |")
    for lbl, hh in extras:
        L.append(f"| {lbl} | {hh} |")
    L.append('')
    return '\n'.join(L), h


OFFICIAL = ("Attempt the official sample's Reasoning section (15 questions, 25 minutes) from [the PDF](https://infytq.onwingspan.com/public-assets/InfosysCampusRecruitmentSampleTest-SystemsEngineer.pdf), then check with [QB-98](question-banks/QB-98-OFFICIAL-SAMPLE-SOLVED.md)", 0.5)
MOCK = ("Sit [MOCK-01](question-banks/MOCK-01.md) under section timers, then mark it with [the answers](question-banks/MOCK-01-ANSWERS.md)", 2.0)
POOL = ("Read and re-solve the observed items for today's topics in [QB-99](question-banks/QB-99-OBSERVED-POOL.md)", 1.0)


def plan(days_def, total_label):
    out, tot = [], 0.0
    for n, title, codes, extras in days_def:
        s, h = day(n, title, codes, extras)
        out.append(s); tot += h
    out.append(f"**Total: {tot:.1f} hours over {len(days_def)} days.**\n")
    return '\n'.join(out), tot


P3 = [
    (1, 'Puzzles and reasoning', ['Z2', 'Z1', 'A2', 'A1', 'A8', 'A7', 'A6'], [("Read and re-solve the puzzle and reasoning items in [QB-99](question-banks/QB-99-OBSERVED-POOL.md)", 1.5)]),
    (2, 'English and pseudocode', ['G2', 'G1', 'V2', 'V1', 'V3', 'V6', 'W1', 'P1', 'P4'], [("Write one timed essay and one timed email (10 minutes each), compare with the W1 outlines", 0.5)]),
    (3, 'Mock and interview', ['A3', 'A5', 'IV1', 'IV2', 'IV5'], [MOCK, ("Review every miss and read the topic file named in its tag", 1.0)]),
]
P7 = [
    (1, 'Puzzles and series', ['Z2', 'Z1', 'A2', 'A1'], [POOL, ("Do the Z2 and Z1 banks, timed at 2.5 minutes each", 1.0)]),
    (2, 'Maths and logic', ['A8', 'A7', 'A3', 'A5', 'A6', 'A9', 'A11'], [("Do the banks for A8, A7, A3 (about 40 questions)", 1.0)]),
    (3, 'English', ['G2', 'G1', 'V2', 'V1', 'W1', 'V5', 'V6'], [("G2 cloze bank (25 questions) and two timed essays", 1.5)]),
    (4, 'Pseudocode and vocabulary', ['P1', 'P4', 'P3', 'P5', 'V3', 'V4'], [("Do QB-P1 (Infosys-dialect traces) and QB-P4 under 2 minutes a question", 1.0)]),
    (5, 'Mock and gaps', ['A4', 'A12', 'A13'], [MOCK, ("Review every miss; retake the weakest section's bank", 1.5), OFFICIAL]),
    (6, 'Interview', ['IV1', 'IV2', 'IV5', 'IV4', 'IV3', 'IV6', 'IV7'], [("Rehearse the 60-second introduction, one project answer and two STAR stories aloud", 1.0)]),
    (7, 'Final pass', ['A19', 'P6'], [("Retake any section of MOCK-01 scored under 70%", 1.5), ("Re-read [the cheat sheet](91-CHEATSHEET.md) and [the strategy](03-TEST-STRATEGY.md)", 1.0), ("One timed puzzle set (Z2 bank, 10 questions)", 0.5), ("Rest", 0.0)]),
]
P14 = [
    (1, 'The shape of the test and puzzles', ['Z2', 'Z1'], [("Read [the pattern synthesis](research/03-pattern-synthesis.md) §1–§3", 1.0), ("Z2 bank, timed at 2.5 minutes each", 0.6)]),
    (2, 'Series, coding, algebra', ['A2', 'A1', 'A8'], [("A1 and A2 banks (60 questions)", 1.0), POOL]),
    (3, 'Data and short reasoning', ['A7', 'A3', 'A5', 'A6'], [("A7, A3 and A5 banks", 1.0)]),
    (4, 'Grammar', ['G2', 'G1', 'V2'], [("G2 cloze bank (25 questions)", 1.0)]),
    (5, 'Verbal and writing', ['V1', 'V5', 'V6', 'W1'], [("V5 and V6 banks", 0.5)]),
    (6, 'Mock 1', ['A9', 'A11'], [MOCK, ("Review every miss", 1.0)]),
    (7, 'Pseudocode 1', ['P1', 'P4', 'P3', 'V3'], [("QB-P1 traces, QB-P4 and QB-P3, timed at 2 minutes each", 1.0)]),
    (8, 'Pseudocode 2', ['P5', 'P2', 'P6', 'P7', 'V4'], []),
    (9, 'Pseudocode tail', ['P8', 'P9', 'P10', 'A4', 'A12'], []),
    (10, 'Arithmetic', ['A13', 'A14', 'A15', 'A17', 'A10'], []),
    (11, 'Counting and logic tail', ['A16', 'A18', 'A19', 'A20', 'A21'], []),
    (12, 'Interview 1', ['IV1', 'IV2', 'IV5'], [("Rehearse the 60-second introduction and two STAR stories aloud", 1.0)]),
    (13, 'Interview 2', ['IV4', 'IV3', 'IV6', 'IV7'], [("Three timed essays and two timed emails", 1.0)]),
    (14, 'Mock 2', [], [MOCK, ("Review every miss", 1.0), ("Re-read [the cheat sheet](91-CHEATSHEET.md)", 0.5), OFFICIAL]),
]


def main():
    global BOOKED
    L = ["# 99 — Study Plan\n",
         "**The evaluation date is not stated.** The drive email gives none, and coaches expect campus drives in late September or early October 2026 `[REPORTED]`. Your invitation (sent to your personal email after you complete the Application Form) will name the date; until then keep the 3-day plan ready. Hours below come from `data/weightage.json`, so every day's total is the sum of its rows.\n",
         "## Pick a plan by days left\n",
         "| Days left | Plan | Roughly |\n|---|---|---|",
         "| 1–4 | [3-day plan](#3-day-plan) | Tier 1 plus a mock and interview basics |",
         "| 5–9 | [7-day plan](#7-day-plan) | Tier 1 and 2, most of Tier 3, one mock, the whole interview |",
         "| 10 or more | [14-day plan](#14-day-plan) | Everything, two mocks, spare hours for revision |\n",
         "**Rules for every plan.** (1) Every section has its own cut-off, so never abandon a section to save another. (2) Do each bank **timed at the real pace** (`03-TEST-STRATEGY.md` §2). (3) After each mock, study the section you scored lowest in, not the one you like. (4) Sleep the night before; nothing in this library is worth a tired morning.\n"]
    BOOKED = set()
    t3, h3 = plan(P3, '3'); b3 = set(BOOKED)
    T1 = [t for t in W['topics'] if t['tier'] == 1]
    t1m, n1 = sum(t['est_marks'] or 0 for t in T1), len(T1)
    assert all(t['code'] in b3 for t in T1), [t['code'] for t in T1 if t['code'] not in b3]   # the 3-day plan promises all of Tier 1
    L += ["## 3-day plan\n", f"For when the test is within about four days. Tier 1 is {t1m:.0f} of the 75 expected marks ({n1} topics); this plan covers all of it, plus two short Tier 2 topics and the interview basics. **It is heavy: about 8 hours a day.** With fewer hours, cut in this order: the Day 3 interview rows, A3 and A5, the timed essay; never cut the mock.\n", t3]
    skip3 = sorted(set(HRS) - b3)
    L.append("**Skipped on purpose** (about " + f"{sum(HRS[c] for c in skip3):.0f} hours): " + ', '.join(skip3) + ". If you reach the end early, add P3, P5, V5 (0.6 h), A9 and A11 first.\n")
    BOOKED = set()
    t7, h7 = plan(P7, '7'); b7 = set(BOOKED)
    L += ["## 7-day plan\n", t7]
    skip7 = sorted(set(HRS) - b7)
    L.append("**Skipped on purpose:** " + (', '.join(skip7) or 'nothing') + ". These are Tier 4 topics, or topics reported only once; if you have time left, add A21 (0.4 h) and A15 (copied from the L&T library) first.\n")
    BOOKED = set()
    t14, h14 = plan(P14, '14'); b14 = set(BOOKED)
    L += ["## 14-day plan\n", "Every topic once and two mocks, with no day above about four and a half hours. Use spare minutes for flash revision of the cheat sheet.\n", t14]
    missing = sorted(set(HRS) - b14)
    L.append("**Not booked:** " + (', '.join(missing) or 'nothing — every subtopic and interview theme is covered') + ".\n")
    L += ["## If you have already done the L&T aptitude\n",
          "Several topic files here were copied from the L&T library. If you finished them there, **do not redo them**; a fifteen-minute skim of the cheat sheet is enough:\n",
          "| Already done (copied) | " + ', '.join(sorted(c for c in COPIED if c.startswith(('A', 'V', 'G')))) + " |\n|---|---|\n",
          "Spend that time on what is new for Infosys and was not in L&T:\n",
          "| New for Infosys | Why it matters |\n|---|---|",
          f"| {lk('Z2')}, {lk('Z1')} | The 10-mark puzzle section; the one most candidates fail |",
          f"| {lk('G2')}, {lk('W1')} | 15 of the 30 English marks, including the essay gate |",
          f"| {lk('A7')}, {lk('A8')}, {lk('A3')}, {lk('A5')} | Reported every time (data interpretation) and cheap to learn |",
          f"| {lk('P4')}, {lk('P1')} | Pseudocode in the Infosys dialect, including pre/post increment |",
          f"| Interview {lk('IV4')}, {lk('IV5')}, {lk('IV6')} | Projects, behaviour and the AI questions |",
          f"| [MOCK-01](question-banks/MOCK-01.md) | The structure is different from the L&T test: 7 timed sections, a cut-off in each |\n",
          "## If you have already done the Accenture pseudocode\n",
          "P1, P2, P3, P5–P8 and P10 are copied from it. Do only P4 (the dialect and the increment rule) and the Infosys-dialect trace bank `QB-P1-infosys-dialect-traces`.\n"]
    (ROOT / '99-STUDY-PLAN.md').write_text('\n'.join(L), encoding='utf-8')
    print(f"3-day {h3:.1f} h, skipped {len(skip3)} items; 7-day {h7:.1f} h; 14-day {h14:.1f} h; not booked in 14-day: {missing}")


if __name__ == '__main__':
    main()
