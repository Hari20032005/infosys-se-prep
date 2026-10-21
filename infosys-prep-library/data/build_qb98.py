"""Generates question-banks/QB-98-OFFICIAL-SAMPLE-SOLVED.md from data/official_sample.py.

The source is Infosys's own sample test (a 2020 PDF, linked below). It carries a CONFIDENTIAL watermark although it
is hosted at a public path, so this file does NOT reproduce its wording: every item is a short paraphrased gist with
the PDF's own section and question number, followed by the answer worked out here and how it was decided.
Because the text comes from official_sample.ITEMS, the document cannot drift from the data that
`python3 data/official_sample.py` checks by execution."""
import pathlib
import official_sample as OFF

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = "https://infytq.onwingspan.com/public-assets/InfosysCampusRecruitmentSampleTest-SystemsEngineer.pdf"

# (first qid, last qid, section heading in the PDF, set name inside it)
SETS = [
    (1, 5, "Section 1: Reasoning Ability", "logic set: a thief, three computers (data interpretation)"),
    (6, 10, "Section 1: Reasoning Ability", "data sufficiency"),
    (11, 15, "Section 1: Reasoning Ability", "deductive reasoning"),
    (16, 20, "Section 2: Technical Ability", "mathematical questions"),
    (21, 25, "Section 2: Technical Ability", "logic set: who attends the wedding"),
    (26, 28, "Section 3: Verbal Ability", "critical reasoning (strengthen, weaken, inference)"),
    (29, 32, "Section 3: Verbal Ability", "English Corrective Usage (fill in the blank)"),
    (33, 36, "Section 3: Verbal Ability", "English Error Correction (best phrasing of the underlined part)"),
    (37, 40, "Section 3: Verbal Ability", "English Error Identification (identify the correct sentence)"),
    (41, 45, "Section 3: Verbal Ability", "reading comprehension"),
    (46, 50, "Section 4: Pseudocode (2 marks each)", "pseudocode"),
    (51, 54, "Section 5: Puzzle", "number puzzles"),
]
HOW = {'executed': 'decided by running code', 'judgement': 'judgement (no machine check possible)', 'unsolved': 'NOT SOLVED'}


def where(n):
    for lo, hi, sec, name in SETS:
        if lo <= n <= hi:
            return f"{sec} · {name} · question {n - lo + 1}"
    raise KeyError(n)


def main():
    items = OFF.ITEMS
    cnt = {k: sum(1 for i in items if i['how'] == k) for k in HOW}
    out = [f"""# QB-98 — The official sample paper, solved

**Source:** Infosys's own sample test for Systems Engineer, a PDF made by Infosys Ltd in September 2020: [open the PDF]({PDF}). Open it beside this file; the question numbers below are the PDF's own.

**What this is.** {len(items)} questions in five timed sections (Reasoning 25 min, Technical 35 min, Verbal 20 min, Pseudocode 10 min, Puzzle 10 min). It is the only first-party sample question paper I could find for this exam, which is why it ranks above every video and blog in this library (see `../research/05-source-credibility.md`).

**What this is not.**
- It is a **2020** sample with five sections. The 2027-batch test is reported to have seven. Treat it as the best evidence of *question style*, not of the current section counts.
- The PDF has a CONFIDENTIAL watermark although it sits at a public address. So this file links to it and gives only a **paraphrased gist** of each question plus my own answer and working. Nothing is copied.
- The PDF **has no answer key**. Every answer here was worked out for this library, not copied from anywhere.

**How each answer was decided** ({cnt['executed']} by running code · {cnt['judgement']} by judgement · {cnt['unsolved']} not solved):
- *decided by running code*: brute force over the real constraints, a simulation, or a model search. Re-run it with `python3 data/official_sample.py`; it exits non-zero if any check fails.
- *judgement*: verbal and unit-reasoning items. These are the least certain answers in the library, so read the reason, not just the letter.
- *NOT SOLVED*: the two multi-select deduction items. They never say which triples count as "related", and the key is not published, so no answer is invented.

Two answers deserve a warning. Deductive items 3 to 5 (O13 to O15 here) are answered on the reading that *the first two statements must entail the third*; on a looser reading the answer to O15 changes. The code states both readings.

---
"""]
    cur = None
    for it in items:
        n = int(it['qid'][1:])
        sec = where(n).split(' · ')[0] + ' · ' + where(n).split(' · ')[1]
        if sec != cur:
            cur = sec
            out.append(f"\n## {sec}\n")
        out.append(f"### {it['qid']} · {where(n).split(' · ')[1]} · question {where(n).split(' · ')[2].split()[-1]}\n")
        out.append(f"- **Asks (paraphrased):** {it['gist']}")
        ans = it['answer']
        out.append(f"- **Answer:** {ans}")
        out.append(f"- **Why:** {it['method']}")
        out.append(f"- **How decided:** {HOW[it['how']]} · topic `{it['taxon']}`\n")
    out.append("\n## What this paper tells you\n")
    by = {}
    for it in items:
        by.setdefault(it['taxon'], []).append(it['qid'])
    out.append("| Topic | Items in this paper |\n|---|---|")
    for t in sorted(by, key=lambda k: (-len(by[k]), k)):
        out.append(f"| `{t}` | {len(by[t])} ({', '.join(by[t])}) |")
    logic = sum(len(by[t]) for t in ('A19', 'A6', 'A4'))
    apt = sum(1 for i in items if i['section'] in ('reasoning', 'technical'))
    out.append(f"""
Logic sets (`A19`, `A6`, `A4`) are {logic} of the {apt} questions in the Reasoning and Technical sections of this paper, so they are worth more practice than a plain topic-count suggests. Practise data sufficiency on the **1 / 2 / 3 / 4** scale used here (the banks `QB-A6-…`, `QB-A19-…`, `QB-A4-…` do). Pseudocode uses a numbered-line dialect with `Set`, `For (each i from a to b)`, `End-for` and `MOD`; the bank `QB-P1-…` prints its traces in exactly that dialect.
""")
    path = ROOT / 'question-banks' / 'QB-98-OFFICIAL-SAMPLE-SOLVED.md'
    path.write_text('\n'.join(out), encoding='utf-8')
    print(f"wrote {path.relative_to(ROOT)}: {len(items)} items ({cnt['executed']} executed, {cnt['judgement']} judgement, {cnt['unsolved']} unsolved)")


if __name__ == '__main__':
    main()
