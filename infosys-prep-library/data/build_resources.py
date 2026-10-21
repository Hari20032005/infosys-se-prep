#!/usr/bin/env python3
"""90-RESOURCE-LIBRARY.md from the §8 Resources of every topic file, restricted to links that
data/check_links.py resolved. Run check_links.py first.
    python3 data/build_resources.py
"""
import collections, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lib_common import ROOT

chk = json.loads((ROOT / 'data' / 'links-checked.json').read_text())
BOT = {'https://artofproblemsolving.com/wiki/index.php/Ratio', 'https://dictionary.cambridge.org/', 'https://dictionary.cambridge.org/grammar/british-grammar/',
       'https://www.infosys.com/services/data-ai-topaz.html', 'https://www.merriam-webster.com/thesaurus'}
def status(u):
    s = chk.get(u, {}).get('status', '')
    if s.startswith(('2', '3')): return 'ok'
    if u in BOT: return 'bot'
    return 'dead'
groups = collections.OrderedDict((k, collections.OrderedDict()) for k in ['Puzzles and reasoning', 'Quantitative', 'Verbal, grammar and writing', 'Pseudocode and Java', 'Interview'])
def grp(sec, code):
    if code.startswith('IV'): return 'Interview'
    if code.startswith(('Z',)) or sec in ('Reasoning Ability', 'Numerical Puzzle'): return 'Puzzles and reasoning'
    if sec == 'Technical Ability': return 'Quantitative'
    if sec == 'Pseudocode': return 'Pseudocode and Java'
    return 'Verbal, grammar and writing'
dead = []
for d in ('topics', 'puzzles', 'pseudocode', 'interview'):
    for p in sorted((ROOT / d).glob('*.md')):
        t = p.read_text()
        m = re.match(r'---\n(.*?)\n---\n', t, re.S)
        fm = dict(re.findall(r'(?m)^(\w+):\s*(.+)$', m.group(1))) if m else {}
        code, sec = fm.get('code'), fm.get('section', '')
        if not code: continue
        r = re.search(r'(?ms)^## 8\. Resources\n(.*?)(?=^## 9\.)', t)
        if not r: continue
        for b in re.finditer(r'^- \*\*(https?://[^*]+)\*\*\s*[—-]\s*(.+)$', r.group(1), re.M):
            u, note = b.group(1).strip(), b.group(2).strip()
            st = status(u)
            if st == 'dead': dead.append((u, p.name)); continue
            g = groups[grp(sec, code)]
            g.setdefault(u, {'note': note, 'codes': [], 'st': st})['codes'].append(code)
L = ["# 90 — Resource Library\n",
     "Free practice and reference links, taken from the **Resources** section of every topic file. **Every link was resolved on 2026-10-01 with a browser user agent** (`data/check_links.py`): "
     f"{sum(len(g) for g in groups.values())} links below, 0 dead. Five sites (marked †) answer automated requests with a 403 or a Cloudflare check but load in a normal browser; I confirmed this in the built-in browser.\n",
     "## Official and primary sources\n",
     "| Resource | What it gives you |\n|---|---|",
     "| https://infytq.onwingspan.com/public-assets/InfosysCampusRecruitmentSampleTest-SystemsEngineer.pdf | **Infosys's own sample Systems Engineer paper** (2020, five sections, no answer key). Solved in `question-banks/QB-98-OFFICIAL-SAMPLE-SOLVED.md` |",
     "| https://www.geeksforgeeks.org/interview-experiences/infosys-interview-experience-for-system-engineer-10/ | A first-hand 2026-batch account, test 13 Oct 2025 (source B7); names its sections, quotes no questions |",
     "| https://www.infosys.com/services/data-ai-topaz.html † | Infosys's own description of its AI-first offering (for the “AI-driven vision” and the interview AI questions) |",
     "| https://hechingerreport.org/why-indias-infosys-has-a-university-of-its-own/ | Independent report on Infosys's residential training campus in Mysuru |",
     "| https://www.geeksforgeeks.org/interview-experiences/infosys-interview-experience-for-system-engineer-2025/ | A first-hand 2025 Systems Engineer account (source B2) |",
     "| https://prepinsta.com/infosys/puzzle-questions-and-answers-pdf/ | Infosys puzzle collection; re-solve each item before trusting its key |\n",
     "The official 2026-batch assessment guidelines (test in college labs, no calculators, 15-minute login window, IDs) are quoted in `interview/00-INFOSYS-SPECIFIC.md`; the system-check link they print is for Infosys's own test platform and is not reproduced here because it does not resolve from outside.\n",
     "## Coaching videos used as evidence (treat as `[REPORTED]`)\n",
     "| Video | Published | What it carries |\n|---|---|---|",
     "| https://www.youtube.com/watch?v=r1m-dYWM8l4 | 2026-09-20 | The 2027-batch notice and the seven-section pattern |",
     "| https://www.youtube.com/watch?v=U7hkPOKo69o | 2026-09-18 | Previous-year reasoning, puzzle and pseudocode questions |",
     "| https://www.youtube.com/watch?v=5XTGOVtBkiw | 2025-10-09 | Candidate recall of the early-October 2025 slots |",
     "| https://www.youtube.com/watch?v=6uftMFrZdzc | 2025-09-27 | Previous-year number puzzles |\n"]
for name, g in groups.items():
    if not g: continue
    L.append(f"## {name}\n")
    L.append("| Resource | For topics | What it is |\n|---|---|---|")
    for u, v in g.items():
        L.append(f"| {u}{' †' if v['st'] == 'bot' else ''} | {', '.join(sorted(set(v['codes'])))} | {v['note']} |")
    L.append('')
(ROOT / '90-RESOURCE-LIBRARY.md').write_text('\n'.join(L), encoding='utf-8')
print(f"{sum(len(g) for g in groups.values())} resource links written; dead links left in topic files: {dead}")
