#!/usr/bin/env python3
"""Interview folder: IV4-IV7 (new), copied STAR stories and technology-flexibility answer (adapted),
plus the four plain documents 00-INTERVIEW-FORMAT.md, 00-INFOSYS-SPECIFIC.md, 00-AFTER-SELECTION.md and 00-UPGRADE-TRACK.md.
    python3 data/build_interview.py
"""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lib_common import *
import copy_reused as CR, gen_iv7

SRC = ROOT / 'data' / 'src'
AC_INT = CR.AC.parent / 'accenture-prep-comm-interview' / 'interview'

DRILLS = {
 'IV4': [
  ("Explain your RAG project in 90 seconds.", "Problem (finding one fact in a long paper) → approach (chunk, embed, retrieve, cite) → your part (solo) → result shown, not measured → one improvement (evaluation set, real multi-turn)."),
  ("Explain the Sugarcane system. What was your part?", "Two inputs (image + questionnaire), YOLOv8 plus a fusion score, team of four, hackathon prize; your own module named specifically; say accuracy was not measured."),
  ("Which module of WasteZero did you build?", "A module name, the milestone, how it connected to the rest; if the consolidated repo belongs to a teammate, say so first."),
  ("Why did you choose ChromaDB?", "Embedded, no separate service, free-tier friendly; at scale you would use pgvector or a managed store."),
  ("How does JWT authentication work in WasteZero?", "Signed token with id and role in an httpOnly cookie, a `protect` middleware reading it, role guards; then the localStorage weakness you found."),
  ("How do you prevent duplicate applications?", "A compound unique index on (opportunity, volunteer): the database enforces it even under concurrent requests."),
  ("How did you test your project?", "Only what is true: pytest for the RAG backend and its CI; say which parts had no tests."),
  ("What was the hardest bug, and how did you find it?", "A real bug: symptom, how you reproduced it, where it lived, the fix, how you know it is fixed."),
 ],
 'IV5': [
  ("Tell me about yourself.", "60 seconds: who you are, Java, two projects, one line of motivation."),
  ("Why do you want to join Infosys?", "Two true reasons from `00-INFOSYS-SPECIFIC.md`, each with one sentence of evidence."),
  ("How do you handle rejection?", "A real example, what you did next, what you changed."),
  ("How do you manage your time and priorities?", "A method you use and one week where it was tested."),
  ("Why has your CGPA changed this way? (if it has)", "One honest cause, the change you made, the recovery shown in numbers."),
  ("How do you handle stressful situations?", "One habit (break down the task, ask for help, sleep) and one example."),
  ("What do you do beyond academics?", "Open source, patents, hackathon: one specific activity and what you learned."),
  ("Are you willing to relocate anywhere in India?", "“Yes”, if true. It is in the official eligibility text."),
  ("Job or higher studies?", "The truth about your plan, and what you will do if you hold the offer."),
  ("Tell me about a time you worked in a team.", "A STAR story from `IV5a-star-stories.md`, with “I” for your actions."),
 ],
 'IV6': [
  ("What is your opinion of generative AI?", "Value + limit + your rule; one example from your RAG project."),
  ("How do you use AI in your daily life?", "True uses, and how you check the output."),
  ("What is RAG, and why did you cite sources?", "Retrieve first, answer from the text, cite so the answer is checkable."),
  ("What is hallucination?", "Fluent output that is false; it is reduced, not removed, by retrieval."),
  ("Will AI take developer jobs?", "It changes the work; verifying and designing systems gains value."),
  ("What are the risks of using AI with client data?", "Confidentiality, privacy, and accountability for the result."),
 ],
}


def drills_md(code):
    L = ["## 7. Practice questions", '', 'These are spoken drills. Answer aloud, in 60–90 seconds, then compare with the outline.', '']
    for i, (q, a) in enumerate(DRILLS[code], 1):
        L.append(f"{i}. **{q}**")
    L += ['', '### Model answers (outlines)', '']
    for i, (q, a) in enumerate(DRILLS[code], 1):
        L.append(f"- **{i}.** {a}")
    return '\n'.join(L) + '\n'


def exercises_section():
    outs = gen_iv7.exercise_outputs()
    body = gen_iv7.exercises_md()
    return "## 7. Practice questions\n\nEight short programs. " + body + '\n'


def section10(code):
    t = IVT[code]
    return (f"## 10. Sources\n\nWritten for this library. **Evidence:** first-hand interview accounts B1–B6 (`../data/reviews-online.csv`), questions {', '.join(i for i in ['I01'] )} … I25 in `../data/questions-observed.csv`, "
            f"and the format notes in `00-INTERVIEW-FORMAT.md`. Project facts are taken from your own verified file `HARIHARAN_INTERVIEW_CONTEXT.md` (27 Sep 2026), not from the web. "
            f"Confidence **{t['conf']}**; the interview data is five accounts.\n")


def assemble(code):
    t = IVT[code]
    src = (SRC / f"{code}.md").read_text(encoding='utf-8')
    if code == 'IV7':
        src = src.replace('{{WORKED}}', gen_iv7.worked_md()).replace('{{SQL}}', gen_iv7.sql_md())
    parts = [p for p in re.split(r'(?m)^(?=## \d+\. )', src) if p.strip()]
    by = {int(re.match(r'## (\d+)\.', p).group(1)): p.rstrip('\n') + '\n' for p in parts}
    s7 = exercises_section() if code == 'IV7' else drills_md(code)
    title = t['label']
    body = [CR.section1(code).rstrip('\n') + '\n'] + [by[n] for n in (2, 3, 4, 5, 6)] + [s7, by[8], by[9], section10(code)]
    names = {'IV4': 'IV4-projects-and-resume', 'IV5': 'IV5-hr-and-behavioural', 'IV6': 'IV6-generative-ai', 'IV7': 'IV7-light-coding-in-java'}
    path = ROOT / 'interview' / f"{names[code]}.md"
    path.write_text(frontmatter(code, title) + f"\n# {code} — {title}\n\n" + '\n'.join(body), encoding='utf-8')
    return path


def copy_adapt(code, src, dest, title, patches, provenance):
    text = src.read_text(encoding='utf-8')
    for a, b in patches:
        assert a in text, f"patch target missing in {src.name}: {a[:50]}"
        text = text.replace(a, b)
    body = text.split('\n', 1)[1] if text.startswith('# ') else text
    h1 = text.split('\n', 1)[0].lstrip('# ').strip()
    fm = frontmatter(code, title, {'adapted_from': str(src.relative_to(CR.PROJ)), 'supporting_for': code})
    (ROOT / 'interview' / dest).write_text(fm + f"\n# {code} — {title}\n\n*{provenance}*\n" + body, encoding='utf-8')


def main():
    (ROOT / 'interview').mkdir(exist_ok=True)
    for code in ('IV4', 'IV5', 'IV6', 'IV7'):
        print('built', assemble(code).name)
    for name in ('00-INTERVIEW-FORMAT', '00-INFOSYS-SPECIFIC', '00-AFTER-SELECTION', '00-UPGRADE-TRACK'):
        (ROOT / 'interview' / f"{name}.md").write_text((SRC / f"{name}.md").read_text(encoding='utf-8'), encoding='utf-8')
    copy_adapt('IV5', AC_INT / 'STAR-STORIES.md', 'IV5a-star-stories.md', 'STAR stories from your own work',
               [("**R** — Both applications were filed and published in May 2026 — application numbers 202641056093 and 202641065392.",
                 "**R** — Both applications were filed in spring 2026 and have since been published (application numbers 202641056093 and 202641065392). Your own context file notes that the specification is dated April 2026 while the resume says May: confirm the month from your paperwork before you state one.")],
               "Adapted from `accenture-prep-final/accenture-prep-comm-interview/interview/STAR-STORIES.md`; written from your real work and verified in that library's QA. One patent-date line updated to match your later context file. Fill every `[YOU FILL IN]` truthfully before rehearsing.")
    copy_adapt('IV5', AC_INT / 'TECH-STACK-ANSWER.md', 'IV5b-technology-flexibility.md', 'Are you willing to work in any technology?',
               [("Asked verbatim of a selected candidate in the batch-2026 drive. `[REPORTED]`",
                 "Infosys's official eligibility text requires candidates to be “willing to work in different technologies as required by Infosys” `[CONFIRMED — official]`, and one 2025 interview asked “Java or Python, and why?” `[REPORTED]`. Expect the question in some form."),
                ("Accenture is an IT services company.", "Infosys is an IT services company."),
                ("understand Accenture staffs across many roles", "understand Infosys staffs across many roles")],
               "Adapted from `accenture-prep-final/accenture-prep-comm-interview/interview/TECH-STACK-ANSWER.md`; verified in that library's QA, with the company name and evidence line changed.")
    import json
    fmp = ROOT / 'data' / 'filemap.json'
    fm = json.loads(fmp.read_text())
    for code, name in (('IV4', 'IV4-projects-and-resume'), ('IV5', 'IV5-hr-and-behavioural'), ('IV6', 'IV6-generative-ai'), ('IV7', 'IV7-light-coding-in-java')):
        fm[code] = f'interview/{name}.md'
    fm['IV5a'] = 'interview/IV5a-star-stories.md'; fm['IV5b'] = 'interview/IV5b-technology-flexibility.md'
    fmp.write_text(json.dumps(fm, indent=2) + '\n')
    print('copied IV5a, IV5b; wrote 00-INTERVIEW-FORMAT, 00-INFOSYS-SPECIFIC, 00-AFTER-SELECTION, 00-UPGRADE-TRACK; filemap updated')


if __name__ == '__main__':
    main()
