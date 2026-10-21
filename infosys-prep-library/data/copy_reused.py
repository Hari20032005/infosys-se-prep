#!/usr/bin/env python3
"""Copy the already-QA'd study files from the L&T and Accenture libraries into this one.

Rules from the brief, all enforced here:
  * copy with the filesystem, not by reading files into a model's context
  * rewrite frontmatter from data/weightage.json by script (lib_common.frontmatter)
  * leave the teaching body (concept notes, worked examples, traps, practice) ALONE
  * add one provenance line under the title
  * never link out: banks link to the copied topic file, not to the source library

Three sections of a copied topic file describe the SOURCE paper, not Infosys, so they are
regenerated from Infosys data: 1 (why it matters -- carries paper-specific numbers),
the top of 2 (an Infosys evidence table is inserted; the original pattern notes are kept
and labelled), and 10 (sources). Everything else is byte-for-byte the source body.

    python3 data/copy_reused.py
"""
import csv, pathlib, re, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lib_common import *

PROJ = ROOT.parent.parent                      # .../my projects
LT = PROJ / 'L&T' / 'lt-prep-library'
AC = PROJ / 'accenture-prep-final' / 'accenture-prep-library'
OBS = {r['qid']: r for r in csv.DictReader(open(ROOT / 'data' / 'questions-observed.csv'))}
OBS_DUP = {}
for r in OBS.values():
    if r['duplicate_of']:
        OBS_DUP.setdefault(r['duplicate_of'], []).append(r['qid'])

# code, source file, destination (relative to library), source QB (Accenture only)
TOPICS = [
    ('A1',  LT / 'topics/L4-coding-and-decoding.md',                 'topics/A1-coding-and-decoding.md', None),
    ('A2',  LT / 'topics/L3-number-and-letter-series.md',            'topics/A2-number-and-letter-series.md', None),
    ('A4',  LT / 'topics/L6-syllogisms-and-logical-deduction.md',    'topics/A4-syllogisms-and-logical-deduction.md', None),
    ('A6',  LT / 'topics/L2-data-sufficiency.md',                    'topics/A6-data-sufficiency.md', None),
    ('A9',  LT / 'topics/Q8-averages-mixtures-and-alligation.md',    'topics/A9-averages-mixtures-and-alligation.md', None),
    ('A12', LT / 'topics/Q1-percentages-and-successive-change.md',   'topics/A12-percentages.md', None),
    ('A13', LT / 'topics/Q5-profit-loss-and-discount.md',            'topics/A13-profit-loss-and-discount.md', None),
    ('A14', LT / 'topics/Q6-simple-and-compound-interest.md',        'topics/A14-simple-and-compound-interest.md', None),
    ('A15', LT / 'topics/Q2-time-speed-distance-and-trains.md',      'topics/A15-time-speed-distance.md', None),
    ('A17', LT / 'topics/Q4-ratio-proportion-and-cost-models.md',    'topics/A17-ratio-and-proportion.md', None),
    ('A19', LT / 'topics/L1-analytical-puzzle-sets-on-shared-premises.md', 'topics/A19-seating-and-analytical-puzzle-sets.md', None),
    ('V1',  LT / 'topics/V1-reading-comprehension.md',               'topics/V1-reading-comprehension.md', None),
    ('V2',  LT / 'topics/V2-spotting-errors-and-grammar-rules.md',   'topics/V2-spotting-errors-and-grammar-rules.md', None),
    ('V3',  LT / 'topics/V3-sentence-correction-and-improvement.md', 'topics/V3-sentence-correction.md', None),
    ('V4',  LT / 'topics/V4-synonyms-antonyms-and-vocabulary.md',    'topics/V4-synonyms-antonyms-and-vocabulary.md', None),
    ('G1',  LT / 'topics/V5-fill-in-the-blanks-and-cloze.md',        'topics/G1-fill-in-the-blanks-and-cloze.md', None),
    ('G2',  LT / 'topics/V7-active-and-passive-voice.md',            'topics/G2a-active-and-passive-voice.md', None),   # supporting file for G2
    ('P1',  AC / 'topics/T25-B1-loops-iteration.md',   'pseudocode/P1-loops-iteration.md',        AC / 'question-banks/QB-T25-B1-loops-iteration.md'),
    ('P2',  AC / 'topics/T31-B6-recursion.md',         'pseudocode/P2-recursion.md',              AC / 'question-banks/QB-T31-B6-recursion.md'),
    ('P3',  AC / 'topics/T11-B7-bitwise-operators.md', 'pseudocode/P3-bitwise-operators.md',      AC / 'question-banks/QB-T11-B7-bitwise-operators.md'),
    ('P5',  AC / 'topics/T15-B3-arrays-1d-2d.md',      'pseudocode/P5-arrays.md',                 AC / 'question-banks/QB-T15-B3-arrays-1d-2d.md'),
    ('P6',  AC / 'topics/T07-B2-conditionals-nested-if.md', 'pseudocode/P6-conditionals-nested-if.md', AC / 'question-banks/QB-T07-B2-conditionals-nested-if.md'),
    ('P7',  AC / 'topics/T35-B5-functions-scope.md',   'pseudocode/P7-functions-scope.md',        AC / 'question-banks/QB-T35-B5-functions-scope.md'),
    ('P8',  AC / 'topics/T32-B9-snippet-complexity.md', 'pseudocode/P8-snippet-complexity.md',    AC / 'question-banks/QB-T32-B9-snippet-complexity.md'),
    ('P10', AC / 'topics/T36-B4-strings-ascii.md',     'pseudocode/P10-strings-ascii.md',         AC / 'question-banks/QB-T36-B4-strings-ascii.md'),
    ('IV1', AC / 'topics/T33-D8-sdlc-agile-testing.md', 'interview/IV1-sdlc-agile-testing.md',    AC / 'question-banks/QB-T33-D8-sdlc-agile-testing.md'),
    ('IV2', AC / 'topics/T05-D1-oop-four-pillars.md',  'interview/IV2-oop-four-pillars.md',       AC / 'question-banks/QB-T05-D1-oop-four-pillars.md'),
    ('IV3', AC / 'topics/T08-D6-dbms-sql.md',          'interview/IV3-dbms-sql.md',               AC / 'question-banks/QB-T08-D6-dbms-sql.md'),
]
FROM_ZERO = [
    ('quant',   LT / 'aptitude/00-QUANT-FROM-ZERO.md',   'aptitude/00-QUANT-FROM-ZERO.md',   'Technical Ability'),
    ('logical', LT / 'aptitude/00-LOGICAL-FROM-ZERO.md', 'aptitude/00-LOGICAL-FROM-ZERO.md', 'Reasoning Ability'),
    ('verbal',  LT / 'aptitude/00-VERBAL-FROM-ZERO.md',  'aptitude/00-VERBAL-FROM-ZERO.md',  'Verbal Ability'),
]
QUANT_CODES = {'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18'}

FENCE = re.compile(r'^\s*```')


def split_sections(body):
    """Split on '## ' headings that are outside fenced code blocks."""
    lines, in_code, secs, cur = body.split('\n'), False, [], None
    pre = []
    for l in lines:
        if FENCE.match(l):
            in_code = not in_code
        if not in_code and l.startswith('## '):
            cur = [l]; secs.append(cur)
        elif cur is None:
            pre.append(l)
        else:
            cur.append(l)
    return pre, secs


def sec_num(sec):
    m = re.match(r'##\s*(\d+)\.', sec[0])
    return int(m.group(1)) if m else None


KEYWORDS = {1: 'why this topic matters', 2: 'exactly what gets asked', 10: 'sources'}


def is_sec(sec, n, seen):
    """True for the FIRST heading whose number and wording match section n. Some source files
    use '## 1.'..'## 6.' as sub-headings inside their concept notes (P2 does); those must not match."""
    if sec_num(sec) != n or KEYWORDS[n] not in sec[0].lower() or n in seen:
        return False
    seen.add(n)
    return True


def obs_table(code):
    t = TOP.get(code)
    qids = list(t['qids']) if t else []
    ids = qids + [d for q in qids for d in OBS_DUP.get(q, [])]
    rows = [OBS[i] for i in ids if i in OBS]
    if not rows:
        return None
    L = ['| ID | Source date | What was asked |', '|---|---|---|']
    for r in sorted(rows, key=lambda r: r['qid']):
        txt = r['question_text'].replace('|', '/').replace('\n', ' ')
        L.append(f"| {r['qid']} | {r['source_date']} | {txt[:150]}{'…' if len(txt) > 150 else ''} |")
    return '\n'.join(L)


def why_tier(t):
    b = t['tier_basis']
    if b == 'roi':
        return (f"expected marks per study hour, weighted by confidence, is {t['roi']:.2f} against a paper average of {W['mean_roi']:.2f} "
                f"(`../data/analysis-tables.md` §6)")
    if b.startswith('section floor'):
        return "its ROI alone would place it lower, but this section has its own cut-off and this topic is needed to reach 60% of the section's marks"
    return b


def section1(code):
    if code in TOP:
        t = TOP[code]
        em = f"{t['est_marks']:.1f}" if t['est_marks'] is not None else 'an unpublished number of'
        ch = len(t['channels'])
        n_obs = t['observed'] + t['discarded_sightings']
        if n_obs:
            ev = (f"**{t['observed']} question{'s' if t['observed'] != 1 else ''} on this topic are in the observed Infosys pool** "
                  f"({', '.join(t['qids']) or 'discarded items only'}), from {ch} source{'s' if ch != 1 else ''}. "
                  f"They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.")
        elif t['named_by'] or t['listed_by']:
            by = ', '.join(t['named_by'] + t['listed_by'])
            ev = (f"**No Infosys question on this topic was recovered.** It rests on syllabus lists or first-hand naming only ({by}), "
                  "so its share is an allocation, not an observation.")
        else:
            ev = "**No source lists or reports this topic for the Infosys test.** It is here for completeness."
        return (f"## 1. Why this topic matters here\n\n"
                f"Expect about **{t['est_q']:.1f} questions and {em} marks** on this topic "
                f"({'about ' + format(100 * t['est_marks'] / TOTAL_MARKS, '.1f') + '% of the ' + str(TOTAL_MARKS) + ' scored marks' if t['est_marks'] is not None else 'a pass/fail gate'}). "
                + (f"It sits in **{block(code)}**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). "
                   if t['section'] == 'aptitude' else
                   f"It sits in **{block(code)}**: {W['sections'][t['section']]['questions']} questions, {W['sections'][t['section']]['marks']} marks, {W['sections'][t['section']]['minutes']} minutes. ") +
                f"**Tier {t['tier']}**, {t['hours']} hours to reach reliable recall, confidence **{t['conf']}**.\n\n"
                f"{ev}\n\n"
                f"**Why the tier:** {why_tier(t)}. Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. "
                f"There is no calculator. Negative marking: none reported.\n")
    t = IVT[code]
    accts = ', '.join(t['accounts'])
    return (f"## 1. Why this topic matters here\n\n"
            f"This is interview material, not test material. **{t['questions']} question{'s' if t['questions'] != 1 else ''} on this theme** were reported across "
            f"**{len(t['accounts'])} first-hand interview account{'s' if len(t['accounts']) != 1 else ''}** ({accts}), so it is **Tier {t['tier']}** for the interview stage, "
            f"{t['hours']} hours to prepare. Interviews are face to face on campus, 15–40 minutes, technical and HR usually in one conversation "
            f"(`../research/03-pattern-synthesis.md` §6). The questions are at textbook level; the teaching body below is sized to answer them aloud, not to pass a written exam.\n")


def section2_prefix(code):
    if code in IVT:
        ids = {'IV1': ['I01', 'I02', 'I09', 'I10', 'I11', 'I13', 'I15'], 'IV2': ['I03', 'I04', 'I12', 'I19'], 'IV3': ['I16']}.get(code, [])
        rows = [OBS[i] for i in ids]
        L = ['| ID | Account | Date | Question |', '|---|---|---|---|'] + [f"| {r['qid']} | {r['source']} | {r['source_date']} | {r['question_text']} |" for r in rows]
        tbl = '\n'.join(L)
        return f"### What Infosys interviewers asked\n\n{tbl}\n\n> The pattern notes below come from the library this file was adapted from; their frequency remarks describe that source, not Infosys.\n"
    tbl = obs_table(code)
    if tbl:
        head = f"### What Infosys asked\n\n{tbl}\n"
    else:
        t = TOP[code]
        by = ', '.join(t['named_by'] + t['listed_by'])
        head = f"### What Infosys asked\n\nNo question on this topic was recovered. Listed by: {by or 'nobody'}.\n"
    return head + "\n> The pattern notes below come from the library this file was adapted from. Any frequency or \"observed paper\" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.\n"


def section10(code, src):
    rel = src.relative_to(PROJ)
    if code in TOP:
        t = TOP[code]
        ids = ', '.join(t['qids']) if t['qids'] else 'none'
        return (f"## 10. Sources\n\n**Teaching content (§3–§9)** is adapted from `{rel}`, which lists its own sources and was verified in that library's QA. "
                f"**Infosys evidence** for this file: observed questions {ids} in `../data/questions-observed.csv`; section structure and marks in "
                f"`../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `{code}`). "
                f"Confidence **{t['conf']}**. Nothing in this file is a published Infosys syllabus.\n")
    return (f"## 10. Sources\n\n**Teaching content (§3–§9)** is adapted from `{rel}`, verified in that library's QA. **Infosys evidence:** first-hand interview accounts "
            f"in `../data/reviews-online.csv` and `../data/questions-observed.csv` (rows `I01`–`I25`); interview format in `../research/03-pattern-synthesis.md` §6.\n")


def convert(code, src, dest, title_code):
    text = src.read_text(encoding='utf-8')
    m = re.search(r'^---\n(.*?)\n---\n', text, re.S | re.M)
    fm = dict(re.findall(r'(?m)^(\w+):\s*(.+)$', m.group(1)))
    comment = re.search(r'<!--.*?-->', text[: m.start()], re.S)
    body = text[m.end():]
    # resources that only make sense for the source paper (an L&T PGET syllabus listing)
    body = '\n'.join(l for l in body.split('\n') if not ('PGET' in l and l.lstrip().startswith(('-', '*'))))
    # source defect (Accenture QA report 1.9, recurred in T32-T36): a heading glued to the end of the previous line
    body = re.sub(r'([^\n#])(## \d{1,2}\. [A-Z])', r'\1\n\n\2', body)
    # source defect: a multiplication asterisk pairs with the next one and italicises the text between ("2*pi*r" rendered as 2<em>pi</em>r)
    for old, new in TEXT_FIXES:
        body = body.replace(old, new)
    pre, secs = split_sections(body)
    h1 = next((l for l in pre if l.startswith('# ')), None)
    title = fm.get('title', (h1 or code)[2:])
    out_secs, seen = [], set()
    for s in secs:
        if is_sec(s, 1, seen):
            out_secs.append(section1(code).rstrip('\n').split('\n') + [''])
        elif is_sec(s, 2, seen):
            out_secs.append([s[0], ''] + section2_prefix(code).split('\n') + [''] + s[1:])
        elif is_sec(s, 10, seen):
            out_secs.append(section10(code, src).rstrip('\n').split('\n'))
        else:
            out_secs.append(s)
    assert seen == {1, 2, 10}, f"{code}: did not find sections 1, 2 and 10 (found {sorted(seen)})"
    note = (f"*Adapted from `{src.relative_to(PROJ)}`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; "
            f"§2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so \"observed\" in the worked examples refers to the source paper.*")
    extra = {'adapted_from': str(src.relative_to(PROJ))}
    if dest.name.startswith('G2a'):
        extra['supporting_for'] = 'G2'
    parts = [frontmatter(code, title.strip(), extra)]
    if comment:
        parts.append(comment.group(0) + '\n')
    parts.append(f"\n# {code} — {title.strip()}\n\n{note}\n\n")
    parts.append('\n'.join('\n'.join(s) for s in out_secs).rstrip() + '\n')
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(''.join(parts), encoding='utf-8')
    return title.strip(), len(secs)


TEXT_FIXES = [('2*pi*r = 12*pi', '2×π×r = 12π'), ('36*pi sq cm', '36π sq cm')]

QB_PATCHES = {   # (bank file stem, old, new): defects found when the source answers were re-executed in this library
    'QB-P5': [("Row 0 gives 3*2 + 4/2 = 8; row 1 gives 5*2 + 6/2 = 13.", "Row 0 gives 3×2 + 4/2 = 8; row 1 gives 5×2 + 6/2 = 13."),
              ("Row 0 contributes +1*2 and −2; row 1 contributes +3*2 and −4; row 2 contributes +5*2 and −6.", "Row 0 contributes +1×2 and −2; row 1 contributes +3×2 and −4; row 2 contributes +5×2 and −6.")],
    'QB-P3': [(
        "**9. (d) Y**\nInside `if`, `==` has higher precedence than `&`, so the condition is `n & (3 == 0)`, i.e. `12 & 0`, which is 0 (false). The `else` branch prints `Y`.\n\n- (a) X — this is what you get if you (incorrectly) group it as `(n & 3) == 0`; `12 & 3 = 0`, which is true and would print X.",
        "**9. (a) X**\nInside `if`, `==` has higher precedence than `&`, so the condition is `n & (3 == 0)`, i.e. `12 & 0`, which is 0 (false). The `else` branch runs and prints `X`. (The source key said (d) Y; compiling and running the code prints X, so the key here is (a).)\n\n- (d) Y — this is what you get if you (incorrectly) group it as `(n & 3) == 0`; `12 & 3 = 0`, which is true, so the `if` branch would print Y."),
    ],
}


def convert_qb(code, src, dest_topic, dest, title):
    t = src.read_text(encoding='utf-8')
    for old, new in QB_PATCHES.get('QB-' + code, []):
        assert old in t, f"QB patch target missing for {code}"
        t = t.replace(old, new)
    i = t.index('\n---\n')
    body = t[i:]
    nq = len(re.findall(r'(?m)^\*\*\d+\.\*\*\s', t[:t.find('ANSWER')] if 'ANSWER' in t else t)) or len(re.findall(r'(?m)^\*\*\d+\. \([a-d]\)', body))
    tier = (TOP.get(code) or IVT[code])['tier']
    rel = pathlib.Path('..') / dest_topic
    head = (f"# QB-{code} — {title}\n\n**{block(code)}** · **Tier {tier}** · {nq} questions\n\n"
            f"Topic file: [`{dest_topic.name}`]({rel.as_posix()})\n\n"
            f"*Adapted from `{src.relative_to(PROJ)}`; verified in that library's QA. Questions and answer key are unchanged.*\n\n"
            f"**How to use this bank.** Attempt every question before opening the key, at the real pace for this section "
            f"({pace(code) or 120} seconds a question). Answer letters are balanced across a–d.\n")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(head + body, encoding='utf-8')
    return nq


def from_zero(kind, src, dest, blockname):
    text = src.read_text(encoding='utf-8')
    comment = re.search(r'<!--.*?-->', text, re.S)
    body = text[comment.end():] if comment else text
    pre, secs = split_sections(body)
    h1 = next(l for l in pre if l.startswith('# '))
    codes = [c for c in TOP if (block(c) == blockname)]
    if kind == 'verbal':
        codes = [c for c in TOP if TOP[c]['section'] in ('verbal', 'grammar')]
    T = [TOP[c] for c in codes]
    tb = ['| Code | Topic | Est. marks | Hours | Tier | Conf. |', '|---|---|---|---|---|---|']
    for t in sorted(T, key=lambda t: -(t['est_marks'] or 0)):
        tb.append(f"| {t['code']} | {t['label']} | {t['est_marks']:.1f} | {t['hours']} | T{t['tier']} | {t['conf']} |" if t['est_marks'] is not None
                  else f"| {t['code']} | {t['label']} | gate | {t['hours']} | T{t['tier']} | {t['conf']} |")
    s = W['sections']
    if kind == 'verbal':
        facts = (f"In the Infosys test this block is two sections: **Verbal Ability** ({s['verbal']['questions']} Q, {s['verbal']['marks']} marks, {s['verbal']['minutes']} min) and "
                 f"**English Grammar** ({s['grammar']['questions']} Q, {s['grammar']['marks']} marks, {s['grammar']['minutes']} min, cloze-based). Each has its own cut-off. "
                 f"The English Writing section (one essay or email, 10 min) is taught in `W1-english-writing.md`.")
    elif kind == 'logical':
        facts = (f"In the Infosys test this is **Reasoning Ability**: 15 questions, 15 marks, 25 minutes (about 100 seconds a question), with its own cut-off. "
                 f"The 2025 pattern deck lists data sufficiency, data interpretation and syllogisms here; coaches add coding-decoding, series and blood relations. "
                 f"Sources disagree on which topics sit in Reasoning and which in Technical Ability, so this library prepares both as one 25-question aptitude block.")
    else:
        facts = (f"In the Infosys test this is **Technical Ability**, which means *mathematical* ability, not computer-science theory: 10 questions, 10 marks, **35 minutes** "
                 f"(the most generous timing on the paper, about 3.5 minutes a question), with its own cut-off. Reasoning topics and maths topics are prepared together as one 25-question aptitude block.")
    sec1 = (f"## 1. What this section is\n\n{facts}\n\n"
            f"Conditions that shape every technique in this guide: **no calculator** (official guidelines), rough paper and stationery allowed, sections are timed and cannot be revisited once closed "
            f"`[LIKELY]`, and no negative marking has been reported. Answer everything.\n\n"
            f"*The rest of this guide is adapted from `{src.relative_to(PROJ)}`; its method and speed techniques transfer, its counts and timings do not.*\n")
    sec2 = "## 2. The topic map\n\nFrom `data/weightage.json`. Marks are expected marks on the Infosys test, not the source paper.\n\n" + '\n'.join(tb) + '\n'
    out = []
    for sct in secs:
        n = sec_num(sct)
        if n == 1: out.append(sec1.rstrip('\n').split('\n'))
        elif n == 2: out.append(sec2.rstrip('\n').split('\n'))
        elif n == 6: continue                              # the source's two-day crash plan: replaced by 99-STUDY-PLAN.md
        elif n == 7: out.append([re.sub(r'##\s*7\.', '## 6.', sct[0])] + sct[1:])
        else: out.append(sct)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(f"{h1}\n\n*Adapted from `{src.relative_to(PROJ)}`; verified in that library's QA. §1 and §2 regenerated for Infosys; the source's crash plan is replaced by `../99-STUDY-PLAN.md`.*\n\n"
                    + '\n'.join('\n'.join(s) for s in out).rstrip() + '\n', encoding='utf-8')


def main():
    filemap = {}
    for code, src, dest, qb in TOPICS:
        d = ROOT / dest
        title, n = convert(code, src, d, code)
        filemap[code if not dest.endswith('G2a-active-and-passive-voice.md') else 'G2a'] = dest
        line = f"{code:4s} {dest:58s} {n} sections"
        if qb:
            qd = ROOT / 'question-banks' / f"QB-{code}-{pathlib.Path(dest).stem.split('-', 1)[1]}.md"
            nq = convert_qb(code, qb, d, qd, title)
            filemap[f'QB-{code}'] = str(qd.relative_to(ROOT))
            line += f" + QB {nq} Q"
        print(line)
    for kind, src, dest, blk in FROM_ZERO:
        from_zero(kind, src, ROOT / dest, blk)
        filemap[f'FZ-{kind}'] = dest
        print('from-zero', dest)
    (ROOT / 'data' / 'filemap.json').write_text(__import__('json').dumps(filemap, indent=2) + '\n')


if __name__ == '__main__':
    main()
