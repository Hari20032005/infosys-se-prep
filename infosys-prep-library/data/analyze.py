#!/usr/bin/env python3
"""Weightage, ROI and tiering for the Infosys Systems Engineer library.

Inputs are the Phase 1 data only:
    questions-observed.csv    one row per observed question (+ duplicate sightings)
    questions-discarded.csv   items too garbled to use, which still identify a topic
    reviews-online.csv        one row per account; section counts, marks, credibility
    syllabus-claims.csv       topic lists as stated by source C1 (2025 deck) and V1 (2026 coach)

Model: adapted from accenture-prep-library/data/analyze.py (sqrt-weighted sightings,
ROI = expected marks x confidence multiplier / hours) and L&T/lt-prep-library/data/analyze.py
(scale-free tier()). Two changes, both forced by this paper:
  1. Sections carry different marks per question (pseudocode, puzzle, grammar = 2), so ROI
     runs on expected MARKS, not expected questions.
  2. Every section has its own cut-off, so a section left entirely in Tier 3/4 would be a
     plan to fail. A section floor lifts the top-ROI subtopics covering 60% of each
     section's marks to at least Tier 2.

    python3 data/analyze.py   ->  data/weightage.json, data/analysis-tables.md
"""
import csv, json, math, pathlib, re
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).resolve().parent
rd = lambda f: list(csv.DictReader(open(HERE / f)))
OBS, DISC, REV, SYL = rd('questions-observed.csv'), rd('questions-discarded.csv'), rd('reviews-online.csv'), rd('syllabus-claims.csv')

# ------------------------------------------------------------ paper structure, from reviews
SE_REV = [r for r in REV if 'Systems Engineer' in r['role']]
count_votes = Counter(r['question_counts'] for r in SE_REV if r['question_counts'])
PLAN_COUNTS, _ = count_votes.most_common(1)[0]
plan_sources = [r['review_id'] for r in SE_REV if r['question_counts'] == PLAN_COUNTS]
q = list(map(int, PLAN_COUNTS.split(';')))
t = list(map(int, next(r for r in SE_REV if r['question_counts'] == PLAN_COUNTS and r['per_section_timing'])['per_section_timing'].split(';')))
mk_src = next(r for r in SE_REV if re.search(r'\d+M', r['section_list']))
# explicit parse of "Reasoning 15M; Technical ... 10M; ... English Written NA"
marks = []
for part in mk_src['section_list'].split(';'):
    m = re.search(r'(\d+)M\s*$', part.strip())
    marks.append(int(m.group(1)) if m else None)
assert len(q) == len(t) == len(marks) == 7, (q, t, marks)
total_75 = [r['review_id'] for r in SE_REV if 'total 75' in r['section_list']]
assert sum(m for m in marks if m) == 75

SECTIONS = {   # name: (questions, marks, minutes)
    'aptitude':   (q[0] + q[1], marks[0] + marks[1], t[0] + t[1]),   # Reasoning + Technical Ability pooled
    'verbal':     (q[2], marks[2], t[2]),
    'pseudocode': (q[3], marks[3], t[3]),
    'puzzle':     (q[4], marks[4], t[4]),
    'grammar':    (q[5], marks[5], t[5]),
    'writing':    (q[6], marks[6], t[6]),                              # scored, marks unpublished: a gate
}
TOTAL_Q = sum(v[0] for v in SECTIONS.values())
TOTAL_MARKS = sum(v[1] for v in SECTIONS.values() if v[1])
TOTAL_MIN = sum(v[2] for v in SECTIONS.values())

# ------------------------------------------------------------ taxonomy
# code, section, label, observed qids, discarded topic_hint, keywords, hours, reuse source
REUSE_LT = 'L&T/lt-prep-library/topics/'
REUSE_AC = 'accenture-prep-final/accenture-prep-library/topics/'
TAX = [
 ('A1','aptitude','Coding and decoding',['R01','R05','R06','R14','R15'],None,['coding','decoding'],0.8,REUSE_LT+'L4-coding-and-decoding.md'),
 ('A2','aptitude','Number and letter series',['R02','R03','R07','R08','R11','R16','R17','R18','R19','R20'],'aptitude-series',['series','sequence'],1.0,REUSE_LT+'L3-number-and-letter-series.md'),
 ('A3','aptitude','Operator logic and equation balancing',['R09','R12'],'aptitude-operator',['operator','symbol'],0.6,''),
 ('A4','aptitude','Syllogisms and logical deduction',['R10'],None,['syllogism','deduction'],0.8,REUSE_LT+'L6-syllogisms-and-logical-deduction.md'),
 ('A5','aptitude','Blood relations',['R13'],None,['blood'],0.5,''),
 ('A6','aptitude','Data sufficiency',['R04'],'aptitude-ds',['sufficiency'],0.8,REUSE_LT+'L2-data-sufficiency.md'),
 ('A7','aptitude','Data interpretation: tables and charts',['Q03','Q07'],'aptitude-di',['interpretation',r'\bDI\b'],1.0,''),
 ('A8','aptitude','Linear equations: ages, heads-and-legs, two-variable systems',['Q01','Q02','Q05'],None,['ages','linear'],0.7,''),
 ('A9','aptitude','Averages, mixtures and alligation',['Q04'],None,['average','mixture','alligation'],0.7,REUSE_LT+'Q8-averages-mixtures-and-alligation.md'),
 ('A10','aptitude','Number system: primes, divisibility, powers and roots',['Q06'],None,['number system','prime','divisib','hcf','lcm'],0.8,''),
 ('A11','aptitude','Mensuration: area, surface area, volume',['Q08'],None,['mensuration'],0.7,''),
 ('A12','aptitude','Percentages',[],None,['percentage'],1.0,REUSE_LT+'Q1-percentages-and-successive-change.md'),
 ('A13','aptitude','Profit, loss and discount',[],None,['profit'],0.8,REUSE_LT+'Q5-profit-loss-and-discount.md'),
 ('A14','aptitude','Simple and compound interest',[],None,['si ci','interest'],0.7,REUSE_LT+'Q6-simple-and-compound-interest.md'),
 ('A15','aptitude','Time, speed and distance',[],None,['time and distance','time speed distance'],1.0,REUSE_LT+'Q2-time-speed-distance-and-trains.md'),
 ('A16','aptitude','Time and work',[],None,['time and work'],0.8,''),
 ('A17','aptitude','Ratio and proportion',[],None,['ratio','proportion'],0.6,REUSE_LT+'Q4-ratio-proportion-and-cost-models.md'),
 ('A18','aptitude','Permutations, combinations and probability',[],None,['permutation','probability'],1.2,''),
 ('A19','aptitude','Logic puzzle sets: seating, conditional rules, direction sense',[],None,['seating','direction'],1.2,REUSE_LT+'L1-analytical-puzzle-sets-on-shared-premises.md'),
 ('A20','aptitude','Cryptarithmetic',[],None,['cryptarithmetic'],0.6,''),
 ('A21','aptitude','Non-verbal reasoning',[],None,['non-verbal'],0.4,''),
 ('V1','verbal','Reading comprehension',[],None,['comprehension'],1.2,REUSE_LT+'V1-reading-comprehension.md'),
 ('V2','verbal','Spotting errors and grammar rules',['V01'],None,['error'],1.2,REUSE_LT+'V2-spotting-errors-and-grammar-rules.md'),
 ('V3','verbal','Sentence correction and completion',[],None,['sentence completion','correct sentence','corrective usage'],1.0,REUSE_LT+'V3-sentence-correction-and-improvement.md'),
 ('V4','verbal','Synonyms, antonyms and vocabulary',[],None,['synonym','vocabulary'],1.0,REUSE_LT+'V4-synonyms-antonyms-and-vocabulary.md'),
 ('V5','verbal','Para-jumbles',[],None,['para jumble'],0.6,''),
 ('V6','verbal','Critical reasoning',[],None,['critical reasoning'],0.6,''),
 ('G1','grammar','Cloze and fill-in-the-blanks',[],None,['cloze','grammar'],0.8,REUSE_LT+'V5-fill-in-the-blanks-and-cloze.md'),
 ('G2','grammar','Tense, articles, prepositions and voice',[],None,['voice','tense','articles','prepositions','parts of speech','punctuation','grammar'],0.7,REUSE_LT+'V7-active-and-passive-voice.md'),
 ('P1','pseudocode','Loops and trace tables',['P01','P02','P04','P05','P06','P08','P09'],None,['loop','code debugging'],1.0,REUSE_AC+'T25-B1-loops-iteration.md'),
 ('P2','pseudocode','Recursion',['P07','P10','P11'],None,['recursion'],1.0,REUSE_AC+'T31-B6-recursion.md'),
 ('P3','pseudocode','Bitwise operators and precedence',['P03'],None,['bitwise'],0.8,REUSE_AC+'T11-B7-bitwise-operators.md'),
 ('P4','pseudocode','Pre/post-increment and fill-the-blank',['P13','P14'],None,['increment'],0.6,''),
 ('P5','pseudocode','Arrays',['P12','P15'],None,['array'],0.8,REUSE_AC+'T15-B3-arrays-1d-2d.md'),
 ('P6','pseudocode','Conditionals and nested if',[],None,['conditional'],0.6,REUSE_AC+'T07-B2-conditionals-nested-if.md'),
 ('P7','pseudocode','Functions and scope',[],None,['function'],0.6,REUSE_AC+'T35-B5-functions-scope.md'),
 ('P8','pseudocode','Complexity, sorting and searching',[],None,['sorting','complexity'],0.8,REUSE_AC+'T32-B9-snippet-complexity.md'),
 ('P9','pseudocode','OOP in pseudocode: inheritance and overriding',[],None,['inheritance','overriding'],0.6,''),
 ('P10','pseudocode','Strings and ASCII',[],None,['string'],0.6,REUSE_AC+'T36-B4-strings-ascii.md'),
 ('Z1','puzzle','Number grids and matrices',['Z01','Z02','Z07','Z09','Z11'],'puzzle-grid',['grid','puzzle','pattern solving'],1.2,''),
 ('Z2','puzzle','Pair and figure rules',['Z03','Z04','Z05','Z06','Z08','Z10','Z12','Z13','Z14','Z15'],'puzzle-pair',['puzzle','pattern solving'],1.2,''),
 ('W1','writing','English writing: essay and email',['W01'],None,['essay','email','writing','written'],1.0,''),
]
# the official sample paper (Sep 2020): attach each item to its taxonomy code
import official_sample as OFFS
_by = {t[0]: i for i, t in enumerate(TAX)}
TAX = [list(t) for t in TAX]
for _it in OFFS.ITEMS:
    TAX[_by[_it['taxon']]][3] = list(TAX[_by[_it['taxon']]][3]) + [_it['qid']]
TAX = [tuple(t) for t in TAX]
DUP_OF = {r['qid']: r['duplicate_of'] for r in OBS if r['duplicate_of']}
ROW = {r['qid']: r for r in OBS}
CHANNEL = {'OFF-2020': 'Infosys (official sample)', 'YT-5XTG': 'OnlineStudy4u', 'YT-2YHL': 'OnlineStudy4u', 'YT-U7HK': 'OnlineStudy4u', 'YT-2MBO': 'OnlineStudy4u',
           'YT-6UFT': 'OnlineStudy4u', 'YT-2NTB': 'Placement Walaa', 'YT-HZGK': 'Code Bashers', 'YT-KC2G': 'Tekno UF', 'B1': 'B1'}
SRC_DATE = {r['source']: r['source_date'] for r in OBS}
SRC_DATE.update({'YT-2YHL/YT-U7HK': SRC_DATE['YT-2YHL']})
RECENT = lambda d: d >= '2025'
CONF_MULT = {'High': 1.00, 'Medium': 0.80, 'Low': 0.60}
FIRST_HAND = [r for r in SE_REV if r['credibility'].startswith('B')]
hit = lambda kws, text: any(re.search(k if k.startswith(r'\b') else re.escape(k), text, re.I) for k in kws)

def evidence(qids, hint, kws, sec):
    items = [ROW[x] for x in qids] + [ROW[d] for d, o in DUP_OF.items() if o in qids]
    disc = [d for d in DISC if hint and d['topic_hint'] == hint]
    recent = sum(RECENT(i['source_date']) for i in items) + sum(RECENT(SRC_DATE.get(d['source'], '2025')) for d in disc)
    old = len(items) + len(disc) - recent
    channels = {CHANNEL[i['source']] for i in items}
    named = [r['review_id'] for r in FIRST_HAND if hit(kws, r['section_list'])]
    agg = sorted({s['review_id'] for s in SYL if hit(kws, s['topic_as_stated']) and (s['section'] == sec or sec == 'aptitude' and s['section'] in ('reasoning', 'technical'))})
    return items, disc, recent, old, channels, named, agg

def confidence(n_obs, n_channels, named, agg):
    if n_obs >= 3 and n_channels >= 2: return 'High'
    if n_obs >= 1 or (named and agg): return 'Medium'
    return 'Low'

def freq_weight(recent, old, named, agg):
    """Accenture formula, unchanged: sqrt so one heavily-filmed topic cannot swamp the rest."""
    return 6.0 * math.sqrt(recent) + 2.0 * math.sqrt(old) + 5.0 * bool(named) + 4.0 * bool(agg) + 1.0

def tier(roi, est_m, conf, mean_roi, mean_m):
    """L&T scale-free tier(): cut-offs are multiples of this paper's own means."""
    r, m = roi / mean_roi, est_m / mean_m
    if conf == 'Low': return 3 if r >= 0.55 else 4
    if r >= 1.15 and m >= 0.90: return 1
    if r >= 0.85 or m >= 1.10: return 2
    if r >= 0.55: return 3
    return 4

rows, by_sec = [], defaultdict(list)
for code, sec, label, qids, hint, kws, hours, reuse in TAX:
    items, disc, recent, old, ch, named, agg = evidence(qids, hint, kws, sec)
    conf = confidence(len(items) + len(disc), len(ch), named, agg)
    d = Counter(i['difficulty'] for i in items)
    r = dict(code=code, section=sec, label=label, observed=len(items), discarded_sightings=len(disc), recent=recent, old=old,
             channels=sorted(ch), named_by=named, listed_by=agg, hours=hours, reuse=reuse, conf=conf,
             w=freq_weight(recent, old, named, agg), difficulty=(d.most_common(1)[0][0] if d else 'Medium'), qids=qids)
    by_sec[sec].append(r); rows.append(r)

for sec, (nq, nm, _) in SECTIONS.items():
    tw = sum(i['w'] for i in by_sec[sec])
    for i in by_sec[sec]:
        i['est_q'] = nq * i['w'] / tw
        i['marks_per_q'] = (nm / nq) if nm else None
        i['est_marks'] = i['est_q'] * i['marks_per_q'] if nm else None
        i['roi'] = i['est_marks'] * CONF_MULT[i['conf']] / i['hours'] if nm else None

scored = [r for r in rows if r['roi'] is not None]
MEAN_ROI = sum(r['roi'] for r in scored) / len(scored)
MEAN_M = sum(r['est_marks'] for r in scored) / len(scored)
for r in rows:
    if r['roi'] is None:
        r['tier'], r['tier_basis'] = 1, 'gate: scored section with unpublished marks and its own cut-off; 1 hour clears it'
    else:
        r['tier'], r['tier_basis'] = tier(r['roi'], r['est_marks'], r['conf'], MEAN_ROI, MEAN_M), 'roi'
# section floor: every section is a gate, so its top-ROI subtopics covering 60% of its marks are >= Tier 2
FLOOR = 0.60
for sec, (nq, nm, _) in SECTIONS.items():
    if not nm: continue
    acc, last = 0.0, None
    for r in sorted(by_sec[sec], key=lambda r: -r['roi']):
        if acc >= FLOOR * nm and (last is None or abs(r['roi'] - last) > 1e-9): break   # ties lift together
        acc += r['est_marks']; last = r['roi']
        if r['tier'] > 2:
            r['tier'], r['tier_basis'] = 2, f"section floor (was T{r['tier']}): needed to reach {int(FLOOR*100)}% of {sec} marks"
recon = {s: round(sum(i['est_q'] for i in by_sec[s]), 2) for s in SECTIONS}
assert abs(sum(recon.values()) - TOTAL_Q) < 0.05, recon
recon_m = {s: round(sum(i['est_marks'] for i in by_sec[s]), 2) for s in SECTIONS if SECTIONS[s][1]}
assert abs(sum(recon_m.values()) - TOTAL_MARKS) < 0.05, recon_m

# ------------------------------------------------------------ interview stage (not scored on the paper)
IVT = [
 ('IV1', 'SDLC, Agile and Scrum', ['I01', 'I02', 'I09', 'I10', 'I11', 'I13', 'I15'], 1.0, REUSE_AC + 'T33-D8-sdlc-agile-testing.md'),
 ('IV2', 'OOP and Java basics', ['I03', 'I04', 'I12', 'I19'], 1.0, REUSE_AC + 'T05-D1-oop-four-pillars.md'),
 ('IV3', 'DBMS and SQL', ['I16'], 1.0, REUSE_AC + 'T08-D6-dbms-sql.md'),
 ('IV4', 'Projects and resume', ['I07', 'I17'], 1.0, ''),
 ('IV5', 'HR and behavioural', ['I05', 'I06', 'I08', 'I14', 'I20', 'I21', 'I22', 'I23'], 1.5, ''),
 ('IV6', 'Generative AI and everyday AI use', ['I24', 'I25'], 0.5, ''),
 ('IV7', 'Light coding in Java', ['I18'], 0.7, ''),
]
iv_rows = []
for code, label, ids, hrs, reuse in IVT:
    accts = sorted({ROW[i]['source'] for i in ids})
    tr = 1 if len(accts) >= 3 else 2 if len(accts) == 2 else 3
    iv_rows.append(dict(code=code, section='interview', label=label, questions=len(ids), accounts=accts, tier=tr,
                        hours=hrs, reuse=reuse, conf='High' if len(accts) >= 3 else 'Medium' if len(accts) == 2 else 'Low',
                        tier_basis='interview: T1 if named in >= 3 first-hand accounts, T2 if 2, T3 if 1'))

# ------------------------------------------------------------ repeat rate and difficulty
exam = [r for r in OBS if r['section'] != 'interview' and r['source'] != 'OFF-2020']     # official sample reported separately
unique = [r for r in exam if not r['duplicate_of']]
dups = [r for r in exam if r['duplicate_of']]
same_channel = [r for r in unique if re.search(r'Re-used in|Also YT|Also in YT', r['notes'])]
diff = defaultdict(Counter)
for r in unique: diff[r['section']][r['difficulty']] += 1

# ------------------------------------------------------------ weightage.json
def slim(r):
    keep = ('code', 'section', 'label', 'est_q', 'marks_per_q', 'est_marks', 'hours', 'conf', 'roi', 'tier', 'tier_basis',
            'difficulty', 'observed', 'discarded_sightings', 'recent', 'old', 'channels', 'named_by', 'listed_by', 'reuse', 'qids')
    return {k: (round(r[k], 3) if isinstance(r[k], float) else r[k]) for k in keep}
out = dict(
    generated='2026-09-25',
    planning_model=f"{len(q)} sections, {sum(q)} questions, {sum(t)} minutes, {TOTAL_MARKS} marks + essay (counts {PLAN_COUNTS})",
    planning_model_sources=plan_sources, marks_source=mk_src['review_id'], total_marks_corroborated_by=total_75,
    planning_model_confidence='Medium — per-section counts rest on one first-hand account (B1) plus decks and coaches that may share a source',
    sections={k: dict(questions=v[0], marks=v[1], minutes=v[2]) for k, v in SECTIONS.items()},
    section_note='aptitude = Reasoning Ability (15 Q, 25 min) + Technical Ability (10 Q, 35 min), pooled because sources disagree on which topics sit in which',
    total_questions=TOTAL_Q, total_marks_excl_essay=TOTAL_MARKS, total_minutes=TOTAL_MIN,
    negative_marking=False, sectional_cutoffs=True, cutoff_value='not discoverable as of 2026-09-25',
    mean_roi=round(MEAN_ROI, 4), mean_est_marks=round(MEAN_M, 4), section_floor=FLOOR,
    section_reconciliation_questions=recon, section_reconciliation_marks=recon_m,
    topics=[slim(r) for r in sorted(rows, key=lambda r: (list(SECTIONS).index(r['section']), int(r['code'][1:])))],
    interview_topics=iv_rows,
    repeat_rate=dict(unique_exam_questions=len(unique), independent_second_sightings=len(dups),
                     rate=round(len(dups) / len(unique), 4), same_channel_reuse=len(same_channel),
                     cross_slot='not measurable: no source ties one question to two slots'),
)
(HERE / 'weightage.json').write_text(json.dumps(out, indent=2) + '\n')

# ------------------------------------------------------------ analysis-tables.md
L = []; A = L.append
A('# Analysis Tables\n')
A('Generated by `data/analyze.py` from `questions-observed.csv`, `questions-discarded.csv`, `reviews-online.csv` and `syllabus-claims.csv`. Regenerate with `python3 data/analyze.py`.\n')
A(f"**Planning model:** {out['planning_model']}.  \n**Confidence in the model itself:** {out['planning_model_confidence']}.\n")
A('---\n')
A('## 1. Section structure\n')
A('| # | Section | Questions | Marks | Minutes | Sec/question | Sources agreeing on the count |')
A('|---|---|---|---|---|---|---|')
names = ['Reasoning Ability', 'Technical Ability (maths)', 'Verbal Ability', 'Pseudocode', 'Numerical Puzzle', 'English Grammar', 'English Writing']
for i, n in enumerate(names):
    A(f"| {i+1} | {n} | {q[i]} | {marks[i] if marks[i] else 'unpublished'} | {t[i]} | {round(t[i]*60/q[i])} | {len(plan_sources)}: {', '.join(plan_sources)} |")
A(f"| | **Total** | **{sum(q)}** | **{TOTAL_MARKS} + essay** | **{sum(t)}** | {round(sum(t)*60/sum(q))} | |\n")
A(f"Marks per section come from {mk_src['review_id']}; the 75-mark total is corroborated by {', '.join(total_75)}.\n")
A('**Conflicting counts, side by side** (every SE account that states a count):\n')
A('| Counts | Minutes | Sources | Credibility | Verdict |\n|---|---|---|---|---|')
for cnt, n in count_votes.most_common():
    srcs = [r for r in SE_REV if r['question_counts'] == cnt]
    A(f"| {cnt} | {', '.join(sorted({r['total_duration'] for r in srcs}))} | {', '.join(r['review_id'] for r in srcs)} | {', '.join(r['credibility'].split(' ')[0] for r in srcs)} | {'**planning model**' if cnt == PLAN_COUNTS else ('older pattern: official 2020 sample, see research/03 §8' if any(r['credibility'].startswith('A') for r in srcs) else 'rejected — see research/03 §8')} |")
A('')
A('## 2. Subtopic frequency — 2025-26 against older\n')
A('Sightings = usable observed questions + independent second sightings + discarded items whose topic is still identifiable. "Recent" = source dated 2025 or later.\n')
A('| Code | Subtopic | Recent | Older | Usable items | Channels | First-hand named | Syllabus lists |\n|---|---|---|---|---|---|---|---|')
for r in sorted(rows, key=lambda r: -(r['recent'] + r['old'])):
    if r['recent'] + r['old'] == 0: continue
    A(f"| {r['code']} | {r['label']} | {r['recent']} | {r['old']} | {r['observed']} | {len(r['channels'])} | {', '.join(r['named_by']) or '-'} | {', '.join(r['listed_by']) or '-'} |")
A(f"\n{sum(1 for r in rows if r['recent']+r['old']==0)} further subtopics have no sighting and rest on syllabus lists or first-hand naming only (§8).\n")
A('## 3. Repeat rate\n')
A(f"- Unique exam questions: **{len(unique)}**. Independent second sightings (a second channel or candidate): **{len(dups)}** → **{100*len(dups)/len(unique):.1f}%** ({', '.join(d['duplicate_of'] for d in dups)}).")
A(f"- Same-channel reuse (one coach re-showing a slide): {len(same_channel)} items. Not counted — it is marketing reuse, not an exam repeat.")
A('- **Cross-slot repeats cannot be measured.** No source ties one question to two slots or dates. The Accenture figure (22-31%) has no Infosys counterpart.\n')
A('## 4. Difficulty mix (unique observed questions)\n')
A('| Section | Easy | Medium | Hard | n |\n|---|---|---|---|---|')
for s in ('reasoning', 'quant', 'pseudocode', 'puzzle', 'verbal', 'essay'):
    c = diff[s]; n = sum(c.values())
    if n: A(f"| {s} | {c['Easy']} ({100*c['Easy']//n}%) | {c['Medium']} ({100*c['Medium']//n}%) | {c['Hard']} ({100*c['Hard']//n}%) | {n} |")
A('\nDifficulty is our rating at extraction (Easy = one rule or one step; Medium = two steps or a non-obvious rule; Hard = a rule that must be found among several candidates, or a trap).\n')
A('## 5. Expected questions and marks, reconciled\n')
A('| Section | Questions | Marks | Subtopics | Questions reconcile to | Marks reconcile to |\n|---|---|---|---|---|---|')
for s, (nq, nm, _) in SECTIONS.items():
    A(f"| {s} | {nq} | {nm or 'gate'} | {len(by_sec[s])} | {recon[s]:.2f} | {recon_m.get(s, '-')} |")
A(f"| **Total** | **{TOTAL_Q}** | **{TOTAL_MARKS}** | **{len(rows)}** | **{sum(recon.values()):.2f}** | **{sum(recon_m.values()):.2f}** |\n")
A('## 6. Every subtopic by ROI\n')
A('ROI = `(expected marks × confidence multiplier) / hours`. Confidence: High = ≥3 sightings from ≥2 channels; Medium = ≥1 sighting, or named first-hand and listed by a syllabus; Low = syllabus only. Multipliers 1.0 / 0.8 / 0.6.\n')
A('| Rank | Code | Subtopic | Section | Est. Q | Est. marks | Hours | Conf. | ROI | Tier | Reuse |\n|---|---|---|---|---|---|---|---|---|---|---|')
for n, r in enumerate(sorted(scored, key=lambda r: -r['roi']), 1):
    A(f"| {n} | {r['code']} | {r['label']} | {r['section']} | {r['est_q']:.2f} | {r['est_marks']:.2f} | {r['hours']} | {r['conf']} | **{r['roi']:.2f}** | **T{r['tier']}** | {'copy' if r['reuse'] else '**new**'} |")
w1 = next(r for r in rows if r['code'] == 'W1')
A(f"| — | W1 | {w1['label']} | writing | 1.00 | unpublished | {w1['hours']} | {w1['conf']} | gate | **T1** | **new** |\n")
A('## 7. Tier list\n')
A(f"Relative to this paper's means: ROI **{MEAN_ROI:.2f}**, expected marks per subtopic **{MEAN_M:.2f}**. T1 = ROI ≥ 1.15× mean and marks ≥ 0.90× mean. T2 = ROI ≥ 0.85× or marks ≥ 1.10×. T3 = ROI ≥ 0.55×. Low confidence is capped at T3. **Section floor:** in each section the top-ROI subtopics covering 60% of its marks are lifted to at least T2, because every section has its own cut-off.\n")
for tt in (1, 2, 3, 4):
    g = [r for r in rows if r['tier'] == tt]
    if not g: continue
    em = sum(r['est_marks'] or 0 for r in g); hrs = sum(r['hours'] for r in g)
    A(f"### Tier {tt} — {len(g)} subtopics · {em:.1f} expected marks · {hrs:.1f} hours\n")
    A('| Code | Subtopic | Section | Est. marks | Hours | Conf. | Basis |\n|---|---|---|---|---|---|---|')
    for r in sorted(g, key=lambda r: -(r['est_marks'] or 99)):
        em_s = f"{r['est_marks']:.2f}" if r['est_marks'] is not None else 'gate'
        A(f"| {r['code']} | {r['label']} | {r['section']} | {em_s} | {r['hours']} | {r['conf']} | {r['tier_basis']} |")
    A('')
A('### Interview stage (not on the paper)\n')
A('| Code | Theme | Questions seen | First-hand accounts | Tier | Hours | Covered by |\n|---|---|---|---|---|---|---|')
for r in iv_rows:
    A(f"| {r['code']} | {r['label']} | {r['questions']} | {len(r['accounts'])} ({', '.join(r['accounts'])}) | T{r['tier']} | {r['hours']} | {'copy of ' + r['reuse'].split('/')[-1] if r['reuse'] else 'new interview file'} |")
A('')
A('## 8. Confidence\n')
A('| Confidence | Subtopics | Expected marks | % of scored marks |\n|---|---|---|---|')
for c in ('High', 'Medium', 'Low'):
    g = [r for r in scored if r['conf'] == c]; m = sum(r['est_marks'] for r in g)
    A(f"| {c} | {len(g)} | {m:.1f} | {100*m/TOTAL_MARKS:.0f}% |")
A('')
A('## 9. Reuse — which existing file covers each subtopic\n')
A('| Code | Subtopic | Existing file (copied in, body untouched) |\n|---|---|---|')
for r in rows:
    A(f"| {r['code']} | {r['label']} | {r['reuse'] or '— none: build new'} |")
for r in iv_rows:
    A(f"| {r['code']} | {r['label']} | {r['reuse'] or '— none: build new (interview/)'} |")
A('')
A('## 10. Coverage gaps — the Phase 3 build list\n')
gaps_obs = [r for r in rows if not r['reuse'] and r['observed'] + r['discarded_sightings'] > 0]
gaps_syl = [r for r in rows if not r['reuse'] and r['observed'] + r['discarded_sightings'] == 0]
A(f"**Seen in the questions, no existing file ({len(gaps_obs)}):** " + '; '.join(f"{r['code']} {r['label']} (T{r['tier']})" for r in gaps_obs) + '.\n')
A(f"**Syllabus-only, no existing file ({len(gaps_syl)}):** " + '; '.join(f"{r['code']} {r['label']} (T{r['tier']})" for r in gaps_syl) + '.\n')
A('**Interview files to write:** ' + '; '.join(f"{r['code']} {r['label']}" for r in iv_rows if not r['reuse']) + '.\n')
zero = [r for r in scored if r['observed'] + r['discarded_sightings'] == 0]
A(f"**Evidence gap:** {len(zero)} of {len(scored)} scored subtopics, carrying {sum(r['est_marks'] for r in zero):.1f} of {TOTAL_MARKS} marks, have no observed question. Verbal and Grammar ({SECTIONS['verbal'][1] + SECTIONS['grammar'][1]} marks) rest on one observed item.\n")
A('## 11. Time budget\n')
A('| Tier | Subtopics | Hours | Expected marks | Marks per hour |\n|---|---|---|---|---|')
for tt in (1, 2, 3, 4):
    g = [r for r in rows if r['tier'] == tt]
    if not g: continue
    h = sum(r['hours'] for r in g); m = sum(r['est_marks'] or 0 for r in g)
    A(f"| T{tt} | {len(g)} | {h:.1f} | {m:.1f} | {m/h:.2f} |")
A(f"| Interview | {len(iv_rows)} | {sum(r['hours'] for r in iv_rows):.1f} | — | — |")
A(f"| **All** | **{len(rows)+len(iv_rows)}** | **{sum(r['hours'] for r in rows)+sum(r['hours'] for r in iv_rows):.1f}** | **{TOTAL_MARKS} + essay** | |\n")
(HERE / 'analysis-tables.md').write_text('\n'.join(L) + '\n')

print(f"planning model {PLAN_COUNTS} from {plan_sources}; marks {marks} from {mk_src['review_id']}")
print(f"{len(rows)} subtopics + {len(iv_rows)} interview themes; questions reconcile {sum(recon.values()):.2f}/{TOTAL_Q}, marks {sum(recon_m.values()):.2f}/{TOTAL_MARKS}")
print('tiers: ' + ', '.join(f"T{x}={sum(1 for r in rows if r['tier']==x)}" for x in (1, 2, 3, 4)) +
      ' | floor lifts: ' + str(sum(1 for r in rows if r['tier_basis'].startswith('section floor'))))
print('confidence: ' + ', '.join(f"{c}={sum(1 for r in rows if r['conf']==c)}" for c in ('High', 'Medium', 'Low')))
print(f"repeat rate {len(dups)}/{len(unique)} = {100*len(dups)/len(unique):.1f}%; hours {sum(r['hours'] for r in rows):.1f} + interview {sum(r['hours'] for r in iv_rows):.1f}")
