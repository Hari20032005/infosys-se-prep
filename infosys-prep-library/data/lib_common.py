"""Shared helpers for the Phase 3 builders: weightage lookup, front matter, and a
question-bank renderer with a per-file, seeded, BALANCED answer-letter assignment.

Known failure modes this guards (see research/04-qa-report.md of the Accenture build):
  * options clustering on (a)            -> balanced multiset of target letters
  * predictable a,b,c,d,a,b,c,d keys     -> multiset shuffled with a seed from the file name
"""
import hashlib, json, pathlib, random, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
W = json.loads((ROOT / 'data' / 'weightage.json').read_text())
TOP = {t['code']: t for t in W['topics']}
IVT = {t['code']: t for t in W['interview_topics']}
TODAY = '2026-09-30'
TOTAL_MARKS = W['total_marks_excl_essay']
REASONING = {'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A19', 'A20', 'A21'}
SEC_NAME = {'verbal': 'Verbal Ability', 'pseudocode': 'Pseudocode', 'puzzle': 'Numerical Puzzle',
            'grammar': 'English Grammar', 'writing': 'English Writing', 'interview': 'Interview'}
SEC_SECONDS = {'reasoning': 100, 'technical': 210, 'verbal': 60, 'pseudocode': 120, 'puzzle': 150, 'grammar': 120, 'writing': 600}


def block(code):
    t = TOP.get(code)
    if not t:
        return 'Interview'
    if t['section'] == 'aptitude':
        return 'Reasoning Ability' if code in REASONING else 'Technical Ability'
    return SEC_NAME[t['section']]


def pace(code):
    t = TOP.get(code)
    if not t:
        return None
    if t['section'] == 'aptitude':
        return SEC_SECONDS['reasoning' if code in REASONING else 'technical']
    return SEC_SECONDS[t['section']]


def frontmatter(code, title, extra=None):
    """Front matter that agrees with weightage.json by construction."""
    t = TOP.get(code) or IVT.get(code)
    if code in TOP:
        pct = f"{100 * t['est_marks'] / TOTAL_MARKS:.1f}% of marks" if t['est_marks'] is not None else 'gate (marks unpublished)'
        eq = f"{t['est_q']:.2f}"
        sec = block(code)
    else:
        pct, eq, sec = 'interview stage', str(t['questions']), 'Interview'
    fm = [('title', title), ('code', code), ('section', sec), ('weightage_pct', pct), ('est_questions', eq),
          ('tier', t['tier']), ('difficulty', t.get('difficulty', 'Medium')), ('est_study_hours', t['hours']),
          ('confidence', t['conf']), ('last_updated', TODAY)]
    if extra:
        fm += list(extra.items())
    return '---\n' + '\n'.join(f'{k}: {v}' for k, v in fm) + '\n---\n'


# ---------------------------------------------------------------- question banks
def letters_for(n, seed):
    """Balanced multiset of target letters, shuffled with a seed derived from the file name."""
    base = 'abcd' * (n // 4) + 'abcd'[: n % 4]
    for salt in range(50):
        pool = list(base)
        random.Random(int(hashlib.sha256((seed + (str(salt) if salt else '')).encode()).hexdigest(), 16) % (2 ** 32)).shuffle(pool)
        seq = ''.join(pool)
        cyclic = n >= 8 and any(seq == (seq[:p] * (n // p + 1))[:n] for p in range(1, 7))
        if not cyclic:
            return pool                    # a guessable repeating key (a,b,c,d,a,b,c,d...) is never accepted
    raise RuntimeError('no non-cyclic letter assignment found')


def render_questions(qs, seed, start=1, targets=None):
    """qs: list of dicts: q (str, may be multi-line), opts (4 strings, correct first), why (str),
    tag (optional str). Returns (questions_md, key_md, letters)."""
    targets = targets or letters_for(len(qs), seed)
    rng = random.Random(int(hashlib.sha256((seed + 'opts').encode()).hexdigest(), 16) % (2 ** 32))
    qmd, kmd, used = [], [], []
    for i, (q, tgt) in enumerate(zip(qs, targets), start):
        opts = list(q['opts'])
        assert len(opts) == 4 and len(set(map(str, opts))) == 4, f"duplicate or missing options in Q{i}: {opts}"
        correct = opts[0]
        if q.get('fixed'):                      # a fixed scale (1/2/3/4): the letter is dictated by the answer
            arranged = sorted(opts, key=str)
            tgt = 'abcd'[arranged.index(correct)]
        else:
            rest = opts[1:]
            rng.shuffle(rest)
            ti = 'abcd'.index(tgt)
            arranged = rest[:ti] + [correct] + rest[ti:]
        head = f"**{i}.** " + (f"**[{q['tag']}]** " if q.get('tag') else '') + q['q']
        if q.get('pre'):
            qmd.append(q['pre'])
        qmd.append(head + '\n' + '\n'.join(f"{'abcd'[j]}) {arranged[j]}" for j in range(4)) + '\n')
        kmd.append(f"{i}. **{tgt}** — {q['why']}")
        used.append(tgt)
    return '\n'.join(qmd), '\n'.join(kmd), used


def write_bank(path, code, title, qs, intro, seed=None):
    """Write a standalone question bank file with the ANSWER KEY anchor the verifiers expect."""
    seed = seed or path.name
    qmd, kmd, used = render_questions(qs, seed)
    t = TOP.get(code) or IVT.get(code)
    tier = t['tier']
    body = f"""# QB-{code} — {title}

**{block(code)}** · **Tier {tier}** · {len(qs)} questions · topic file: see the `{code}` file in `topics/`, `puzzles/`, `pseudocode/` or `interview/`

{intro}

**How to use this bank.** Attempt every question before opening the key. Answer letters are balanced across a–d and not in a repeating pattern, so guessing the pattern will not help.

---

## Practice questions

{qmd}
### ANSWER KEY

{kmd}
"""
    path.write_text(body, encoding='utf-8')
    return used


def clean_num(x):
    """Render ints as ints, floats trimmed."""
    if isinstance(x, float):
        if abs(x - round(x)) < 1e-9:
            return str(int(round(x)))
        return f"{x:.2f}".rstrip('0').rstrip('.')
    return str(x)
