"""Practice sets for the Core Course.

PRACTICE[code]() -> {1: [Q x5], 2: [Q x5], 3: [Q x5]}   (L1 warm-up, L2 exam level, L3 beyond the exam)

Every Q is a gen_core.Q dict. Generated questions carry an independent check() (run by gen_core.run).
Hand-written questions go through judge() and are labelled `judgement` (no machine check exists for them).
`steps`, where present, is an approximate count of the operations a solver must carry out; verify_core_course.py
requires the mean to rise from L1 to L3 and requires L3 to go beyond the most complex item in the 2020 official sample (5)."""
import re

import gen_core
import gen_code as GC
import gen_puzzles as GP
import bank_verbal as BV

PRACTICE = {}
OFFICIAL_MAX_STEPS = 5      # the cube-and-box puzzle (a^3 + b^3 + a + b) is the most complex rule in the 2020 sample


def ops(rule: str) -> int:
    """Approximate number of operations in a rule written like 'a*b + a + b' or 'digit-sum(a + b)'."""
    r = rule.replace('×', '*').replace('−', '-').replace('²', '^2').replace('³', '^3')
    if '=' in r:
        r = r.split('=')[-1]
    n = len(re.findall(r'digit-(?:sum|product)', r))
    r = re.sub(r'digit-(?:sum|product)', '', r)
    n += r.count('|') // 2
    n += len(re.findall(r'[*+\-/^]', r))
    n += len(re.findall(r'\d(?=[a-d(])', r)) + len(re.findall(r'\)\(', r))
    return n


def seed(code: str, level: int, tag: int = 0) -> int:
    return 9000 + 17 * sum(map(ord, code)) + 100 * level + tag


def draw(gen, n, code, level, tag=0, **kw):
    """n distinct generated questions, each checked by its own check()."""
    return gen_core.run(gen, seed(code, level, tag), n, **kw)


def judge(q, correct, wrong, why, tag=None, **extra):
    """A hand-written question: one best answer by design, no machine check."""
    d = BV.T(q, correct, wrong, why, tag)
    d['judgement'] = True
    d.update(extra)
    return d


def with_steps(qs):
    for q in qs:
        if q.get('rule') and 'steps' not in q:
            q['steps'] = ops(q['rule'])
    return qs


def finish(parts, code):
    """Concatenate per-level lists, check sizes and that no stem repeats within the lesson."""
    out = {lvl: with_steps(list(qs)) for lvl, qs in parts.items()}
    assert {k: len(v) for k, v in out.items()} == {1: 5, 2: 5, 3: 5}, (code, {k: len(v) for k, v in out.items()})
    stems = [q['q'] + '|' + '|'.join(sorted(q['opts'])) for lvl in (1, 2, 3) for q in out[lvl]]     # a stem may repeat ("Identify the correct sentence") if the options differ
    assert len(set(stems)) == 15, f"{code}: repeated question stem"
    return out


# ============================================================================ Z2: pair and figure puzzles
PAIR_HARD = {      # more operations than anything in the 2020 sample; used only for Level 3
    'a^2 + b^2 - a*b + a': lambda a, b: a * a + b * b - a * b + a,
    'a*b + a^2 - b^2 + a': lambda a, b: a * b + a * a - b * b + a,
    '(a+b)^2 - a*b - a - b': lambda a, b: (a + b) ** 2 - a * b - a - b,
    'a^2 + b^2 - a*b + a - b': lambda a, b: a * a + b * b - a * b + a - b,
}
FIG_HARD = {
    'a^2 + b^2 - c*d + a': lambda a, b, c, d: a * a + b * b - c * d + a,
    'a*b + c*d - a - d': lambda a, b, c, d: a * b + c * d - a - d,
    'a*b + c^2 - d + b': lambda a, b, c, d: a * b + c * c - d + b,
}
PAIR_ALL = {**GP.PAIR, **PAIR_HARD}
FIG_ALL = {**GP.FIG, **FIG_HARD}


def z2():
    def pair(n, level, tag, name, **kw):                     # one question for one named rule: no rule repeats in a level
        return draw(GP.gen_pair, n, 'Z2', level, tag, names=[name], **kw)
    L1 = ([q for t, nm in enumerate(['a*b', '2a + b', 'a*b - 1', '(2)(a+b)'], 1) for q in pair(1, 1, t, nm, span=(2, 9))]
          + draw(GP.gen_zigzag, 1, 'Z2', 1, 9, names=['left + right']))
    L2 = (pair(1, 2, 1, 'a*b + a + b')
          + draw(GP.gen_pair, 1, 'Z2', 2, 2, digit=True, names=['digit-sum(a + b)', 'digit-sum(a) + digit-sum(b)'])
          + draw(GP.gen_figure, 1, 'Z2', 2, 3, names=['a*b - c*d', 'a*b + c*d', 'a*d - b*c', 'a*c + b*d'])
          + draw(GP.gen_cubebox, 1, 'Z2', 2, 4, ks=(3,), top=9)
          + draw(GP.gen_zigzag, 1, 'Z2', 2, 5, names=['|left - right|', 'digit-sum(left + right)']))
    L3 = ([q for t, nm in enumerate(['a^2 + b^2 - a*b + a', '(a+b)^2 - a*b - a - b', 'a*b + a^2 - b^2 + a'], 1)
           for q in draw(GP.gen_pair, 1, 'Z2', 3, t, names=[nm], lib=PAIR_ALL, span=(2, 12))]
          + draw(GP.gen_figure, 1, 'Z2', 3, 4, names=['a^2 + b^2 - c*d + a'], lib=FIG_ALL, top=9)
          + draw(GP.gen_cubebox, 1, 'Z2', 3, 5, ks=(3,), top=12))
    return finish({1: L1, 2: L2, 3: L3}, 'Z2')


PRACTICE['Z2'] = z2


# ============================================================================ P4: increment operators
def _has_inc(prog):
    for st in prog:
        if st[0] == 'inc':
            return True
        sub = []
        if st[0] == 'for': sub = st[5]
        elif st[0] == 'while': sub = st[2]
        elif st[0] == 'dowhile': sub = st[1]
        elif st[0] == 'if': sub = st[2] + (st[3] or [])
        if _has_inc(sub):
            return True
    return False


def gen_trace_with_inc(rng):
    q = GC.gen_trace(rng)
    if q is None or not _has_inc(q['prog']):
        return None
    return q


def p4():
    L1 = draw(GC.gen_incr, 5, 'P4', 1, 1, n_terms=2, asks=['result', 'i'])
    L2 = draw(GC.gen_incr, 5, 'P4', 2, 1)
    L3 = draw(GC.gen_incr, 3, 'P4', 3, 1, n_terms=3, asks=['both']) + draw(gen_trace_with_inc, 2, 'P4', 3, 2)
    for q in L1: q['steps'] = len(q['meta'][0])
    for q in L2: q['steps'] = len(q['meta'][0]) + 1
    for q in L3[:3]: q['steps'] = len(q['meta'][0]) + 2
    for q in L3[3:]: q['steps'] = 6
    return finish({1: L1, 2: L2, 3: L3}, 'P4')


PRACTICE['P4'] = p4


# ============================================================================ G1: cloze and fill in the blanks (hand-written, judgement)
def g1():
    J = judge
    L1 = [
        J("She has been working here ___ 2019.", "since", ["for", "during", "by"],
          "2019 is a point in time, so use **since**. *For* needs a length of time, such as *for five years* (Purdue OWL, prepositions of time).", 'Preposition'),
        J("My brother is ___ engineer.", "an", ["a", "the", "no article"],
          "*Engineer* begins with a vowel **sound**, so the article is **an** (Purdue OWL, a versus an).", 'Article'),
        J("The committee ___ its decision yesterday.", "announced", ["has announced", "announces", "will announce"],
          "*Yesterday* names a finished time, so the past simple **announced** is right. The present perfect is not used when the time is stated (British Council, present perfect).", 'Tense'),
        J("Each of the students ___ a laptop.", "has", ["have", "are having", "were"],
          "*Each* is singular, so the verb is singular: **has** (Purdue OWL, subject-verb agreement).", 'Agreement'),
        J("We must finish the report ___ Friday.", "by", ["until", "since", "during"],
          "*By* sets a deadline: the work must be done at or before Friday (Purdue OWL, prepositions of time).", 'Preposition'),
    ]
    L2 = [
        J("Neither the manager nor the engineers ___ aware of the delay.", "were", ["was", "is", "has been"],
          "With *nor*, the verb agrees with the nearer subject. *Engineers* is plural, so **were** (Purdue OWL, subject-verb agreement).", 'Agreement'),
        J("The ___ you gave me was very useful.", "information", ["informations", "informational", "informing"],
          "*Information* is uncountable: it has no plural form, and the verb *was* is singular. The word is **information** (Purdue OWL, uncountable nouns).", 'Noun form'),
        J("She was tired ___ she had slept for ten hours.", "although", ["because", "so", "unless"],
          "Sleeping a lot would normally stop you being tired, so the two parts are in contrast. *Although* shows contrast.", 'Connector'),
        J("By the time the audience arrived, the speaker ___ the final slide.", "had finished", ["has finished", "finishes", "will finish"],
          "Two past events: finishing happened first, arriving second. The earlier one takes the past perfect, **had finished** (Purdue OWL, active verb tenses).", 'Tense'),
        J("By next June, the team ___ the new system.", "will have launched", ["launched", "has launched", "is launching"],
          "*By next June* names a future deadline, so the future perfect **will have launched** is used for an action completed by then (Purdue OWL, active verb tenses).", 'Tense'),
    ]
    L3 = [
        J("The new tax rules will ___ every small business in the state.", "affect", ["effect", "affects", "effects"],
          "*Will* needs a base verb, and the meaning is \"have an influence on\". That is **affect**. *Effect* as a verb means \"bring about\", which does not fit \"a business\".", 'Confusable words'),
        J("The report, along with the supporting documents, ___ been sent to the client.", "has", ["have", "are", "were"],
          "The subject is *the report*. The phrase *along with the supporting documents* sits in between and does not change the verb, so **has** (Purdue OWL, a phrase between subject and verb).", 'Agreement'),
        J("The plan was approved in March. ___, work did not start until July.", "However", ["Therefore", "Moreover", "Similarly"],
          "The second sentence goes against what the first leads you to expect (approval, so a start). A word of contrast is needed: **However**.", 'Connector'),
        J("She ___ in Chennai since 2016, and she still lives there.", "has lived", ["lived", "had lived", "lives"],
          "*Since 2016* with a state that is still true now needs the present perfect, **has lived** (British Council, present perfect; Purdue OWL).", 'Tense'),
        J("When I reached the station, the train ___ already left.", "had", ["has", "was", "will"],
          "Two past events: the train leaving came before my arriving. The earlier event takes the past perfect, so the helper is **had** (*had already left*). *Has already left* is present perfect and clashes with the past time (Purdue OWL, active verb tenses).", 'Tense'),
    ]
    return finish({1: L1, 2: L2, 3: L3}, 'G1')


PRACTICE['G1'] = g1


# ============================================================================ Z1: number grids and matrices
def z1():
    def one(gen, level, tag, **kw):
        return draw(gen, 1, 'Z1', level, tag, **kw)
    L1 = (one(GP.gen_sumgrid, 1, 1, shapes=[(3, 3)])
          + one(GP.gen_row3, 1, 2, names=['first = second × third'])
          + one(GP.gen_row3, 1, 3, names=['first = (second + third) × 2'])
          + one(GP.gen_seqtable, 1, 4, names=['n² + 1', 'n² − 1'])
          + one(GP.gen_gridsums, 1, 5))
    L2 = (one(GP.gen_row3, 2, 1, names=['first = second² − third', 'first = (second + third) × third', 'first = second × third + 2'])
          + one(GP.gen_row4, 2, 2, names=['d = b × c + a', 'd = a × b − c', 'd = a × b + c'])
          + one(GP.gen_seqtable, 2, 3, names=['n(n+1)/2', 'n² + n', 'n² + 2n'])
          + one(GP.gen_gridsums, 2, 4)
          + one(GP.gen_sumgrid, 2, 5, shapes=[(4, 4)]))
    L3 = (one(GP.gen_row4, 3, 1, names=['d = a² + b × c'])
          + one(GP.gen_row4, 3, 2, names=['d = b² − a × c', 'd = (a + b) × c'])
          + one(GP.gen_seqtable, 3, 3, names=['n³', 'n(n−1)/2'])
          + one(GP.gen_sumgrid, 3, 4, shapes=[(4, 4)])
          + one(GP.gen_kakuro, 3, 5, givens=(3,)))
    for q in L1 + L2 + L3:
        if q.get('tag') == 'Sum grid': q['steps'] = 3
        if q.get('tag') == 'Row sums as a series': q['steps'] = 4
        if q.get('tag') == 'Distinct-digit sum grid': q['steps'] = 8
    for q in L3:
        if q.get('tag') == 'Sum grid': q['steps'] = 5
        if q.get('rule'): q['steps'] = ops(q['rule']) + 2          # three example rows to read, one rule to find
    for q in L1 + L2:
        if q.get('rule'): q['steps'] = ops(q['rule']) + (1 if q in L2 else 0)
    return finish({1: L1, 2: L2, 3: L3}, 'Z1')


PRACTICE['Z1'] = z1


# ============================================================================ helpers for generator-backed levels
def mk(fn, steps):
    """Wrap a question generator so every question it makes carries a `steps` value (separate ideas the solver must find)."""
    def g(rng, **kw):
        q = fn(rng, **kw)
        if q is not None:
            q['steps'] = steps
        return q
    g.__name__ = fn.__name__
    return g


def seq(code, level, spec):
    """spec: list of (generator, steps). One question from each, each with its own seed."""
    out = []
    for tag, (fn, st) in enumerate(spec, 1):
        out += draw(mk(fn, st), 1, code, level, tag)
    return out


# ============================================================================ A1: coding and decoding
import gen_reasoning as GR


def a1():
    L1 = seq('A1', 1, [(GR.cd_lettersum, 2), (GR.cd_shift, 2), (GR.cd_substitution, 2), (GR.cd_lettersum, 2), (GR.cd_shift, 2)])
    L2 = seq('A1', 2, [(GR.cd_mean, 3), (GR.cd_position, 3), (GR.cd_swap, 3), (GR.cd_lettersum, 3), (GR.cd_position, 3)])
    L3 = seq('A1', 3, [(GR.cd_reverse_shift, 4), (GR.cd_reverse_shift, 4), (GR.cd_swap, 4), (GR.cd_reverse_shift, 4), (GR.cd_mean, 4)])
    return finish({1: L1, 2: L2, 3: L3}, 'A1')


PRACTICE['A1'] = a1


# ============================================================================ A2: number and letter series
from gen_core import Q, distinct_wrong
AZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def s_arith(rng):
    a, d = rng.randint(2, 30), rng.randint(3, 12)
    t = [a + d * i for i in range(6)]
    ans = a + 6 * d
    wrong = distinct_wrong(ans, [ans + d, ans - d, t[-1] * 2 - t[-3]], rng, lo=1)
    q = f"Find the next term: {', '.join(map(str, t))}, ?"
    why = f"The gap is the same every time ({d}): {t[1]} − {t[0]} = {d}. So the next term is {t[-1]} + {d} = **{ans}**."
    return Q(q, [ans] + wrong, why, lambda: t[-1] + (t[-1] - t[-2]), 'Constant gap')


def s_geom(rng):
    a, k = rng.randint(1, 4), rng.choice([2, 3])
    t = [a * k ** i for i in range(6)]
    ans = a * k ** 6
    wrong = distinct_wrong(ans, [t[-1] + t[-2], t[-1] + (t[-1] - t[-2]), ans + k], rng, lo=1)
    q = f"Find the next term: {', '.join(map(str, t))}, ?"
    why = f"Each term is the one before **× {k}**: {t[0]} × {k} = {t[1]}. So the next term is {t[-1]} × {k} = **{ans}**."
    return Q(q, [ans] + wrong, why, lambda: t[-1] * (t[1] // t[0]), 'Constant ratio')


def s_letters(rng):
    d0, g = rng.randint(1, 3), rng.randint(1, 2)          # first gap, and how much each gap grows
    gaps = [d0 + g * i for i in range(5)]
    start = rng.randint(1, 4)
    p = [start]
    for gp in gaps: p.append(p[-1] + gp)
    if p[-1] > 26: return None
    t = [AZ[x - 1] for x in p[:5]]
    ans = AZ[p[5] - 1]
    wrong = [AZ[(p[5] - 1 + o) % 26] for o in (1, -1, 2, -2) if AZ[(p[5] - 1 + o) % 26] != ans][:3]
    q = f"Find the next letter: {', '.join(t)}, ?"
    why = (f"Turn the letters into places in the alphabet: {', '.join(map(str, p[:5]))}. The gaps are {', '.join(map(str, gaps[:4]))}, growing by {g}, so the next gap is {gaps[4]}. "
           f"{p[4]} + {gaps[4]} = {p[5]}, which is **{ans}**.")
    return Q(q, [ans] + wrong, why, lambda: chr(64 + (ord(t[-1]) - 64) + (ord(t[-1]) - ord(t[-2])) + g), 'Letter series')


def a2():
    L1 = seq('A2', 1, [(s_arith, 1), (s_geom, 1), (GR.s_primes, 2), (GR.s_fibo, 2), (GR.s_diff_ap, 2)])
    L2 = seq('A2', 2, [(s_letters, 3), (GR.s_poly, 3), (GR.s_primegap, 3), (GR.s_mulplus, 3), (GR.s_interleave, 3)])
    L3 = seq('A2', 3, [(GR.s_alnum, 4), (GR.s_alnum, 4), (GR.s_square_rev, 4), (GR.s_square_rev, 4), (GR.s_interleave, 3)])
    return finish({1: L1, 2: L2, 3: L3}, 'A2')


PRACTICE['A2'] = a2


# ============================================================================ A6: data sufficiency (official 1-2-3-4 scale)
import itertools


def persist(fn, tries=4000):
    """Keep drawing until the generator accepts: some (answer, pool) pairs are rare."""
    def g(rng, **kw):
        for _ in range(tries):
            q = fn(rng, **kw)
            if q is not None:
                return q
        return None
    g.__name__ = fn.__name__
    return g


def ds_classify(universe, ask, s1, s2):
    """1 = exactly one statement alone gives a single answer, 2 = either alone, 3 = only together, 4 = even together not enough."""
    def values(*preds):
        return {ask(u) for u in universe if all(p(u) for p in preds)}
    a, b, both = len(values(s1)) == 1, len(values(s2)) == 1, len(values(s1, s2)) == 1
    if a and b: return 2
    if a != b: return 1
    return 3 if both else 4


def ds_coins(rng, want=None):
    """Word-problem data sufficiency about two kinds of coins, decided by trying every (a, b) pair."""
    c1, c2 = rng.choice([(2, 5), (1, 2), (5, 10), (1, 5), (2, 10)])
    a0, b0 = rng.randint(2, 14), rng.randint(1, 9)
    n, v, k = a0 + b0, c1 * a0 + c2 * b0, b0 + rng.randint(0, 2)
    stm = {
        'N': (f"She has {n} coins in all.", lambda u: u[0] + u[1] == n),
        'V': (f"The coins are worth Rs {v} in all.", lambda u: c1 * u[0] + c2 * u[1] == v),
        'M': (f"She has more {c1}-rupee coins than {c2}-rupee coins.", lambda u: u[0] > u[1]),
        'B': (f"She has at most {k} {c2}-rupee coins.", lambda u: u[1] <= k),
        'E': (f"The number of {c1}-rupee coins is even.", lambda u: u[0] % 2 == 0),
    }
    k1, k2 = rng.sample(list(stm), 2)
    (t1, p1), (t2, p2) = stm[k1], stm[k2]
    U = [(a, b) for a in range(0, 31) for b in range(0, 31) if a + b > 0]
    ask = lambda u: u[1]
    cl = ds_classify(U, ask, p1, p2)
    if want and cl != want:
        return None
    q = (f"Rita has only {c1}-rupee and {c2}-rupee coins. How many {c2}-rupee coins does she have? Mark **1** if exactly one statement alone is enough, "
         f"**2** if either statement alone is enough, **3** if both together are needed, **4** if even both together are not enough.\n\nI. {t1}\nII. {t2}\n")
    why = (f"Try every pair (number of {c1}-rupee coins, number of {c2}-rupee coins) up to 30 each. Statement I alone leaves "
           f"{sorted({ask(u) for u in U if p1(u)})[:6]}{'…' if len({ask(u) for u in U if p1(u)}) > 6 else ''} as possible counts of {c2}-rupee coins; "
           f"statement II alone leaves {sorted({ask(u) for u in U if p2(u)})[:6]}{'…' if len({ask(u) for u in U if p2(u)}) > 6 else ''}; together they leave "
           f"{sorted({ask(u) for u in U if p1(u) and p2(u)})[:6]}. So the mark is **{cl}**.")
    U2 = [(a, b) for b in range(0, 41) for a in range(0, 41) if a + b > 0]              # a different search order and a larger range
    chk = lambda: ds_classify(U2, lambda u: u[1], p1, p2)
    return Q(q, [cl] + [c for c in (1, 2, 3, 4) if c != cl], why, chk, tag='Data sufficiency (coins)', fixed=True)


EASY = ['x + y = {k}', 'y = {k}', 'x > {k}', 'x < {k}', 'x is even', 'x is a positive number', '2x + 3 = {k}']
MID = EASY + ['x - y = {k}', 'x × y = {k}', 'x² = {k}', 'x³ = {k}']
HARD = MID + ['x² = {k} and x is positive', 'x² = {k} and x < 0']


def a6():
    def ds(level, tag, want, pool, steps):
        qs = draw(persist(GR.gen_ds), 1, 'A6', level, tag, want=want, pool=pool)
        qs[0]['steps'] = steps
        return qs

    def coins(level, tag, want, steps):
        qs = draw(persist(ds_coins), 1, 'A6', level, tag, want=want)
        qs[0]['steps'] = steps
        return qs
    E2 = EASY + ['x³ = {k}']                                   # an "either alone" answer needs two statements that each fix x
    L1 = ds(1, 1, 3, EASY, 2) + ds(1, 2, 2, E2, 2) + ds(1, 3, 1, EASY, 2) + ds(1, 4, 4, EASY, 2) + ds(1, 5, 3, EASY, 2)
    L2 = ds(2, 1, 1, MID, 3) + ds(2, 2, 4, MID, 3) + ds(2, 3, 2, MID, 3) + coins(2, 4, 3, 3) + ds(2, 5, 4, MID, 3)
    L3 = coins(3, 1, 4, 4) + ds(3, 2, 3, HARD, 4) + coins(3, 3, 1, 4) + ds(3, 4, 2, HARD, 4) + ds(3, 5, 1, HARD, 4)
    return finish({1: L1, 2: L2, 3: L3}, 'A6')


PRACTICE['A6'] = a6


# ============================================================================ A4: syllogisms and deduction
import gen_syllogism as SY


def a4():
    def syl(level, tag, want, steps, forms=('all', 'some', 'no', 'some_not')):
        qs = draw(persist(SY.gen_syllogism), 1, 'A4', level, tag, want=want, forms=forms)
        qs[0]['steps'] = steps
        return qs

    def ded(level, tag, steps):
        qs = draw(persist(GR.gen_deductive), 1, 'A4', level, tag)
        qs[0]['steps'] = steps
        return qs
    simple = ('all', 'some')
    L1 = syl(1, 1, 'both', 2, simple) + syl(1, 2, 'neither', 2, simple) + syl(1, 3, 'only1', 2, simple) + syl(1, 4, 'neither', 2, simple) + syl(1, 5, 'only2', 2, simple)
    L2 = syl(2, 1, 'neither', 3) + syl(2, 2, 'either', 3) + syl(2, 3, 'only1', 3) + syl(2, 4, 'only2', 3) + ded(2, 5, 3)
    L3 = syl(3, 1, 'either', 4) + syl(3, 2, 'both', 4) + ded(3, 3, 5) + ded(3, 4, 5) + ded(3, 5, 5)
    return finish({1: L1, 2: L2, 3: L3}, 'A4')


PRACTICE['A4'] = a4


# ============================================================================ A3: operator logic
def op_star(rng, names=None):
    """A made-up operator, rule inferred from worked lines: 'If 3 ★ 4 = 15 and 2 ★ 5 = 12, find 6 ★ 2'."""
    name = rng.choice(list(names))
    f = PAIR_ALL[name]
    pts = [(rng.randint(2, 9), rng.randint(2, 9)) for _ in range(4)]
    if len(set(pts)) < 4 or any(a == b for a, b in pts):
        return None
    vals = [f(*p) for p in pts]
    if any(v < 0 or v > 300 for v in vals) or len(set(vals)) < 4:
        return None
    ex, qp = list(zip(pts[:3], vals[:3])), pts[3]
    ans = vals[3]
    fit = GP._fit(PAIR_ALL, ex, qp)
    if set(fit.values()) != {ans}:
        return None
    near = [v for v in GP._fit(PAIR_ALL, ex[:2], qp).values() if v != ans and v >= 0]
    wrong = distinct_wrong(ans, near, rng, lo=0)
    ln = ', '.join(f"{a} ★ {b} = {v}" for (a, b), v in ex)
    q = f"A new operation ★ works the same way every time. If {ln}, find {qp[0]} ★ {qp[1]}."
    why = (f"Test rules on the first line, then confirm on the others. The rule that fits all three is **{GP.disp(name)}**: "
           + '; '.join(f"{a} ★ {b} → {v}" for (a, b), v in ex) + f". So {qp[0]} ★ {qp[1]} = **{ans}**.")
    qd = Q(q, [ans] + wrong, why, lambda: GP.sole(fit), tag='Inferred operator')
    qd['rule'] = name
    return qd


NESTED = {'2a + b': lambda a, b: 2 * a + b, 'a × b − a': lambda a, b: a * b - a, 'a² − b': lambda a, b: a * a - b,
          'a + 2b': lambda a, b: a + 2 * b, 'a × b + b': lambda a, b: a * b + b, '3a − b': lambda a, b: 3 * a - b}


def op_nested(rng, names=None):
    """The operator is GIVEN; evaluate a nested expression: 'If a ★ b = 2a + b, find (3 ★ 4) ★ 5'."""
    name = rng.choice(list(names or NESTED))
    f = NESTED[name]
    x, y, z = rng.randint(2, 7), rng.randint(2, 7), rng.randint(2, 7)
    inner = f(x, y)
    ans = f(inner, z)
    if inner <= 0 or ans <= 0:
        return None
    other = f(x, f(y, z))                                  # the other bracketing
    wrong = distinct_wrong(ans, [other, f(z, inner), f(x, y) + z], rng, lo=1)
    q = f"If a ★ b = {GP.disp(name).replace('*', '×')}, find the value of ({x} ★ {y}) ★ {z}."
    why = f"Work out the bracket first: {x} ★ {y} = {inner}. Then {inner} ★ {z} = **{ans}**. (Doing {y} ★ {z} first would give {other}, which is a different question.)"
    return Q(q, [ans] + wrong, why, lambda: NESTED[name](NESTED[name](x, y), z), 'Nested operator')


def a3():
    easy = ['a*b', 'a*b + 1', 'a*b - 1', '(2)(a+b)', '2a + b', 'a + 2b']
    mid = ['a^2 - b', 'a + b^2', 'a*b + a + b', 'a*b - a - b', '3a - b']
    L1 = seq('A3', 1, [(lambda r: op_star(r, easy), 2), (lambda r: op_star(r, easy), 2), (lambda r: op_star(r, easy), 2),
                       (GR.op_substitute, 3), (lambda r: op_nested(r, ['2a + b', 'a + 2b']), 3)])
    L2 = seq('A3', 2, [(GR.op_digitsum_quot, 3), (GR.op_dollar, 3), (lambda r: op_star(r, mid), 3), (GR.op_substitute, 3), (GR.op_interchange, 4)])
    L3 = seq('A3', 3, [(lambda r: op_nested(r, ['a × b − a', 'a² − b', '3a − b']), 5), (lambda r: op_nested(r, ['a × b + b', 'a² − b']), 5),
                       (GR.op_interchange, 4), (GR.op_interchange, 4), (GR.op_dollar, 4)])
    return finish({1: L1, 2: L2, 3: L3}, 'A3')


PRACTICE['A3'] = a3


# ============================================================================ A5: blood relations
def family_consistent(triples):
    """triples: (a, word, b) meaning 'a is the <word> of b'. False if some child would need two parents of the same sex
    (for example two different fathers), once brothers and sisters are given the same parents."""
    from collections import defaultdict
    sex, parents = {}, defaultdict(set)
    kind = {'father': ('P', 'M'), 'mother': ('P', 'F'), 'son': ('C', 'M'), 'daughter': ('C', 'F'), 'brother': ('S', 'M'), 'sister': ('S', 'F'),
            'husband': ('W', 'M'), 'wife': ('W', 'F')}
    sibs = []
    for a, w, b in triples:
        k, sx = kind[w]
        sex[a] = sx
        if k == 'P': parents[b].add(a)
        if k == 'C': parents[a].add(b)
        if k == 'S': sibs.append((a, b))
    for _ in range(3):
        for a, b in sibs:
            both = parents[a] | parents[b]
            parents[a], parents[b] = set(both), set(both)
    for child, ps in parents.items():
        for sx in ('M', 'F'):
            if len({x for x in ps if sex.get(x) == sx}) > 1:
                return False
    return True


def blood_chain(rng, n_st):
    q = GR.gen_blood(rng, n_st=n_st)
    if q is None:
        return None
    import re as _re
    triples = _re.findall(r"(\w) is the ([a-z-]+) of (\w)\.", q['q'])
    return q if family_consistent(triples) else None


def blood_symbols(rng):
    """Observed style: symbols stand for relations; read a chain like  P - Q + R x S  and name the relation of P to S."""
    syms = ['+', '−', '×']
    rels = rng.sample(['sister', 'brother', 'father', 'mother', 'son', 'daughter'], 3)
    legend = dict(zip(syms, rels))
    chain = [rng.choice(syms) for _ in range(3)]
    people = rng.sample('PQRSTUVW', 4)
    words = [legend[c] for c in chain]
    # statement i: people[i] is the <word> of people[i+1]
    sex = {}
    for i, w in enumerate(words):
        kind, sx = GR.WORD[w]
        if sex.get(people[i], sx) != sx:
            return None
        sex[people[i]] = sx
    for i, w in enumerate(words):
        if GR.WORD[w][0] == GR.SPOUSE:
            return None
    path = [GR.WORD[w][0] for w in reversed(words)]                 # from people[-1] back to people[0]
    red = GR.reduce_path(path)
    if red is None or red not in GR.NAME or red == (GR.UP, GR.SIDE, GR.DOWN):
        return None
    ans = GR.NAME[red][0 if sex[people[0]] == 'M' else 1]
    pool = [x for x in ['father', 'mother', 'brother', 'sister', 'uncle', 'aunt', 'grandfather', 'grandmother', 'son', 'daughter', 'nephew', 'niece'] if x != ans]
    male = {'father', 'brother', 'uncle', 'grandfather', 'son', 'nephew'}
    same = [x for x in pool if (x in male) == (sex[people[0]] == 'M')]
    rng.shuffle(same)
    wrong = same[:3]
    if len(wrong) < 3:
        return None
    if not family_consistent([(people[i], words[i], people[i + 1]) for i in range(3)]):
        return None
    expr = f"{people[0]} {chain[0]} {people[1]} {chain[1]} {people[2]} {chain[2]} {people[3]}"
    leg = '; '.join(f"‘x {sy} y’ means x is the {rl} of y" for sy, rl in legend.items())
    q = f"{leg}. In the expression **{expr}**, how is {people[0]} related to {people[3]}?"
    why = (f"Read each sign as its relation: " + '; '.join(f"{people[i]} is the {words[i]} of {people[i + 1]}" for i in range(3)) +
           f". Walking back from {people[3]} to {people[0]} gives ‘{' then '.join(red)}’, and {people[0]} is {'male' if sex[people[0]] == 'M' else 'female'}: **{ans}**.")

    def check():
        conv = {GR.UP: GR.DOWN, GR.DOWN: GR.UP, GR.SIDE: GR.SIDE, GR.SPOUSE: GR.SPOUSE}
        names = GR.NAME[red]
        back = GR.reduce_path([conv[k] for k in reversed(red)])             # the reverse reading must also reduce
        assert back is not None
        return names[0] if sex[people[0]] == 'M' else names[1]
    return Q(q, [ans] + wrong, why, check, 'Relations written as signs')


def a5():
    L1 = seq('A5', 1, [(persist(lambda r: blood_chain(r, 2)), 2)] * 5)
    L2 = seq('A5', 2, [(persist(lambda r: blood_chain(r, 3)), 3)] * 3 + [(persist(blood_symbols), 3)] * 2)
    L3 = seq('A5', 3, [(persist(blood_symbols), 4)] * 3 + [(persist(lambda r: blood_chain(r, 3)), 4)] * 2)
    return finish({1: L1, 2: L2, 3: L3}, 'A5')


PRACTICE['A5'] = a5


# ============================================================================ A21: non-verbal reasoning (text forms)
def a21():
    L1 = seq('A21', 1, [(GR.nv_dice, 1), (GR.nv_dice, 1), (GR.nv_cube, 2), (GR.nv_mirror_clock, 2), (GR.nv_cube, 2)])
    L2 = seq('A21', 2, [(GR.nv_cube, 2), (GR.nv_mirror_clock, 3), (GR.nv_squares, 3), (GR.nv_cube, 3), (GR.nv_squares, 3)])
    L3 = seq('A21', 3, [(GR.nv_squares, 4), (GR.nv_squares, 4), (GR.nv_mirror_clock, 4), (GR.nv_cube, 4), (GR.nv_squares, 4)])
    return finish({1: L1, 2: L2, 3: L3}, 'A21')


PRACTICE['A21'] = a21


# ============================================================================ A7: data interpretation, and A8: linear equations
import gen_quant as GQ
from fractions import Fraction


def di_multi(rng, kind=None):
    """Harder table questions (two or three steps) built on the two-plant output table."""
    yrs = [2019, 2020, 2021, 2022, 2023]
    A = [rng.randint(20, 90) * 10 for _ in yrs]
    B = [rng.randint(20, 90) * 10 for _ in yrs]
    tbl = '| Year | Plant A (units) | Plant B (units) |\n|---|---|---|\n' + '\n'.join(f"| {y} | {a} | {b} |" for y, a, b in zip(yrs, A, B))
    kind = kind or rng.choice(['combined_change', 'greatest_rise', 'avg_gap'])
    if kind == 'combined_change':
        i = rng.randint(1, 4)
        s0, s1 = A[i - 1] + B[i - 1], A[i] + B[i]
        ans = Fraction((s1 - s0) * 100, s0)
        if abs(ans) > 200: return None
        sign = (lambda f: GQ.pct_str(f) if f >= 0 else '−' + GQ.pct_str(-f))
        correct = sign(ans)
        wrong = [sign(Fraction((s1 - s0) * 100, s1)), sign(Fraction((A[i] - A[i - 1]) * 100, A[i - 1])), sign(Fraction((B[i] - B[i - 1]) * 100, B[i - 1])), sign(-ans)]
        wrong = [w for w in dict.fromkeys(wrong) if w != correct][:3]
        if len(wrong) < 3: return None
        q = f"Study the table.\n\n{tbl}\n\nBy what percentage did the **combined** output of both plants change from {yrs[i - 1]} to {yrs[i]}? (A negative sign means a fall.)"
        why = (f"Combined output: {yrs[i - 1]} = {A[i - 1]} + {B[i - 1]} = {s0}; {yrs[i]} = {A[i]} + {B[i]} = {s1}. Change = {s1 - s0}. As a percentage of the starting year: "
               f"{s1 - s0}/{s0} × 100 = **{correct}**.")
        return Q(q, [correct] + wrong, why, lambda: sign(Fraction(100 * s1, s0) - 100), 'Change in a combined total')
    if kind == 'greatest_rise':
        rises = [Fraction(B[i], B[i - 1]) for i in range(1, 5)]
        best = max(rises)
        if sorted(rises).count(best) != 1: return None
        ans_year = yrs[1 + rises.index(best)]
        wrong = [str(y) for y in yrs[1:] if y != ans_year][:3]
        q = f"Study the table.\n\n{tbl}\n\nIn which year did Plant B's output show the **greatest percentage increase** over the previous year?"
        why = ("Compare B(this year) ÷ B(last year): " + '; '.join(f"{yrs[i]}: {B[i]}/{B[i - 1]} = {float(rises[i - 1]):.2f}" for i in range(1, 5)) + f". The largest ratio is for **{ans_year}**.")
        return Q(q, [str(ans_year)] + wrong, why, lambda: str(yrs[1 + max(range(4), key=lambda j: B[j + 1] / B[j])]), 'Greatest rise')
    ans_n = Fraction(sum(A[:3]) - sum(B[:3]), 3)
    if ans_n.denominator != 1: return None
    ans = abs(int(ans_n))
    if ans == 0: return None
    who = 'A' if ans_n > 0 else 'B'
    correct = f"Plant {who} by {ans}"
    other = 'B' if who == 'A' else 'A'
    wrong = [f"Plant {other} by {ans}", f"Plant {who} by {ans + 30}", f"Plant {who} by {abs(sum(A) - sum(B)) // 5}"]
    wrong = [w for w in dict.fromkeys(wrong) if w != correct][:3]
    if len(wrong) < 3: return None
    q = (f"Study the table.\n\n{tbl}\n\nOver the first three years ({yrs[0]} to {yrs[2]}), which plant had the higher average yearly output, and by how many units?")
    why = (f"Average of A = {sum(A[:3])}/3 = {sum(A[:3]) // 3}; average of B = {sum(B[:3])}/3 = {sum(B[:3]) // 3}. "
           f"Plant {who} is higher by **{ans}**.")
    return Q(q, [correct] + wrong, why, lambda: (lambda d: f"Plant {'A' if d > 0 else 'B'} by {abs(d)}")((sum(A[:3]) - sum(B[:3])) // 3), 'Compare two averages')


def a7():
    L1 = seq('A7', 1, [(GQ.di_bar, 2), (GQ.di_bar, 2), (GQ.di_freq_table, 2), (GQ.di_bar, 2), (GQ.di_freq_table, 2)])
    L2 = seq('A7', 2, [(GQ.di_pie, 3), (GQ.di_pie, 3), (GQ.di_freq_table, 3), (GQ.di_bar, 3), (GQ.di_pie, 3)])
    L3 = seq('A7', 3, [(lambda r: di_multi(r, 'combined_change'), 4), (lambda r: di_multi(r, 'greatest_rise'), 4), (lambda r: di_multi(r, 'avg_gap'), 4),
                       (lambda r: di_multi(r, 'combined_change'), 4), (lambda r: di_multi(r, 'greatest_rise'), 4)])
    return finish({1: L1, 2: L2, 3: L3}, 'A7')


PRACTICE['A7'] = a7


def lin_ages_system(rng):
    """Two statements about two ages (a ratio some years ago, and a sum now); ages found by trying every pair."""
    k = rng.choice([2, 3, 4])
    t = rng.randint(2, 8)
    y0 = rng.randint(t + 3, 30)                      # B's present age
    x0 = k * (y0 - t) + t                            # A's present age
    if x0 > 90 or x0 == y0: return None
    s = x0 + y0
    who = rng.choice(['A', 'B'])
    ans = x0 if who == 'A' else y0
    wrong = distinct_wrong(ans, [s - ans, ans + t, ans - t, (x0 if who == 'B' else y0)], rng, lo=1)
    q = f"{t} years ago, A was {k} times as old as B. The sum of their present ages is {s} years. What is {who}'s present age?"
    why = (f"Let B's age {t} years ago be b. Then A's age then was {k}b. Now they are b + {t} and {k}b + {t}, and the sum is {k + 1}b + {2 * t} = {s}, so b = {(s - 2 * t) // (k + 1)}. "
           f"Now B = {y0} and A = {x0}. {who}'s present age is **{ans}**.")

    def check():
        sols = [(x, y) for x in range(1, 121) for y in range(1, 121) if x + y == s and x - t == k * (y - t) and y > t]
        assert len(sols) == 1
        return sols[0][0] if who == 'A' else sols[0][1]
    return Q(q, [ans] + wrong, why, check, 'Ages from two statements')


def a8():
    L1 = seq('A8', 1, [(GQ.lin_consec, 2), (GQ.lin_ages, 2), (GQ.lin_legs, 2), (GQ.lin_consec, 2), (GQ.lin_cost, 2)])
    L2 = seq('A8', 2, [(GQ.lin_system, 3), (GQ.lin_legs, 3), (GQ.lin_ages, 3), (GQ.lin_cost, 3), (GQ.lin_system, 3)])
    L3 = seq('A8', 3, [(lin_ages_system, 4), (lin_ages_system, 4), (GQ.lin_cost, 4), (GQ.lin_legs, 4), (lin_ages_system, 4)])
    return finish({1: L1, 2: L2, 3: L3}, 'A8')


PRACTICE['A8'] = a8


# ============================================================================ V2: spotting errors, in the official "identify the correct sentence" form
STEM = "Identify the grammatically correct sentence."


def v2():
    J = lambda right, wrong, why, tag: judge(STEM, right, wrong, why, tag)
    L1 = [
        J("Each of the boys has a bag.", ["Each of the boys have a bag.", "Each of the boys are carrying a bag.", "Each of the boy has a bag."],
          "*Each* is singular, so the verb is **has**. The other options use a plural verb with *each* or leave *boy* in the singular after *of the* (Purdue OWL, subject-verb agreement).", 'Agreement'),
        J("She has lived here for five years.", ["She has lived here since five years.", "She lives here since five years.", "She has lived here during five years."],
          "Five years is a length of time, so **for**. *Since* needs a starting point such as a year or a day (Purdue OWL, prepositions of time).", 'Time words'),
        J("I met him yesterday.", ["I have met him yesterday.", "I meet him yesterday.", "I am meeting him yesterday."],
          "*Yesterday* names a finished time, so the past simple **met** is used. The present perfect does not go with a stated time (British Council, present perfect).", 'Tense'),
        J("He is an honest man.", ["He is a honest man.", "He is honest a man.", "He is an honest a man."],
          "The *h* in *honest* is silent, so the word starts with a vowel sound and takes **an** (Purdue OWL, a versus an).", 'Article'),
        J("The information you gave me was useful.", ["The informations you gave me were useful.", "The information you gave me were useful.", "The informations you gave me was useful."],
          "*Information* is uncountable: no *s*, and the verb is singular, **was** (Purdue OWL, uncountable nouns).", 'Uncountable noun'),
    ]
    L2 = [
        J("The manager, along with his assistants, is attending the meeting.", ["The manager, along with his assistants, are attending the meeting.", "The manager, along with his assistants, are attended the meeting.", "The manager, along with his assistants, is attend the meeting."],
          "The subject is *the manager*. The phrase *along with his assistants* sits in between and does not change the verb: **is attending** (Purdue OWL, a phrase between subject and verb).", 'Agreement'),
        J("Neither the teacher nor the students were present.", ["Neither the teacher nor the students was present.", "Neither the teacher nor the students is present.", "Neither the teachers nor the student were present."],
          "With *nor*, the verb agrees with the nearer subject. *Students* is plural, so **were**. In the last option the nearer subject is *student*, which needs *was* (Purdue OWL, subject-verb agreement).", 'Agreement'),
        J("The number of applicants has increased this year.", ["The number of applicants have increased this year.", "The numbers of applicant has increased this year.", "A number of applicants has increased this year."],
          "*The number of* takes a singular verb, as in the dictionary's example *The number of homeless people has increased*. *A number of* means *some* and takes a plural verb (Oxford Learner's Dictionaries, *number*).", 'Number of'),
        J("The girls brought their lunch boxes.", ["The girls brought her lunch boxes.", "The girl brought their lunch box.", "The girls brought its lunch boxes."],
          "A pronoun agrees in number with its noun: plural *girls* takes **their** (Purdue OWL, using pronouns clearly).", 'Pronoun agreement'),
        J("She likes reading, writing and painting.", ["She likes reading, writing and to paint.", "She likes to read, writing and painting.", "She likes read, writing and painting."],
          "The three items must have the same form. All three are -ing words here (Purdue OWL, parallel structure).", 'Parallel structure'),
    ]
    L3 = [
        J("After finishing the report, Meera sent it to the client.", ["After finishing the report, it was sent to the client.", "After finishing the report, the client received it.", "Having finished the report, the email was sent by Meera."],
          "The opening phrase names an action, so the person who did it must be the subject that follows. Only *Meera* finished the report (Purdue OWL, dangling modifiers).", 'Dangling modifier'),
        J("When people are tired, they make more mistakes.", ["When people are tired, you make more mistakes.", "When people are tired, one make more mistakes.", "When people are tired, it makes more mistakes."],
          "Do not shift person or number in one sentence: *people* is third person plural, so the pronoun is **they** (Purdue OWL, using pronouns clearly).", 'Pronoun agreement'),
        J("By the time we reached the hall, the show had started.", ["By the time we reached the hall, the show has started.", "By the time we reached the hall, the show starts.", "By the time we reached the hall, the show will start."],
          "Two past events: the show starting came before we reached the hall. The earlier one takes the past perfect, **had started** (Purdue OWL, active verb tenses).", 'Tense'),
        J("She apologised for arriving late.", ["She apologised for arrive late.", "She apologised to arriving late.", "She apologised for to arrive late."],
          "After the preposition *for*, the verb takes its -ing form, **arriving**. A gerund can be the object of a preposition (Purdue OWL, gerunds).", 'Gerund after a preposition'),
        J("Small habits on their own have the power to change a career, whatever their size.", ["Small habits on their own has the power to change a career, whatever their size.", "Small habits on its own have the power to change a career, whatever their size.", "Small habits on their own have the power to changing a career, whatever its size."],
          "The subject *habits* is plural, so **have**; the pronouns *their* match it. The other options mix *has*, *its* and *to changing* (Purdue OWL, agreement and pronouns).", 'Combined'),
    ]
    return finish({1: L1, 2: L2, 3: L3}, 'V2')


PRACTICE['V2'] = v2


# ============================================================================ V3: sentence correction (choose the best phrasing of the part in brackets)
def v3():
    def item(sentence, right, wrong, why, tag):
        stem = ("In the sentence below, the part in [square brackets] may need correction. Choose the best phrasing for that part "
                f"(one option keeps it unchanged).\n\n> {sentence}\n")
        return judge(stem, right, wrong, why, tag)
    L1 = [
        item("The results of the survey [was published] last week.", "were published", ["was published", "has published", "have publish"],
             "The subject is *results*, which is plural, so the verb is **were published** (Purdue OWL, subject-verb agreement).", 'Agreement'),
        item("She [has worked] here since 2019.", "has worked", ["works", "worked", "is working"],
             "*Since 2019* with a state that is still true needs the present perfect. The part is already correct, so keep **has worked** (Purdue OWL, prepositions of time; British Council, present perfect).", 'No change'),
        item("Please read the [past history] of the project.", "history", ["past history", "history of the past", "old past history"],
             "*History* already means the past, so *past history* repeats itself. Purdue OWL lists *past history* among its redundant pairs. The best phrasing is **history**.", 'Redundancy'),
        item("Please send [me the informations] by Monday.", "me the information", ["me the informations", "me an information", "to me the informations"],
             "*Information* is uncountable: no plural, no *an* (Purdue OWL, uncountable nouns). The best phrasing is **me the information**.", 'Uncountable noun'),
        item("The seminar will take place [in Friday].", "on Friday", ["in Friday", "at Friday", "to Friday"],
             "Days take **on** (Purdue OWL, prepositions of time).", 'Preposition'),
    ]
    L2 = [
        item("Neither of the answers [are] correct.", "is", ["are", "were", "have been"],
             "*Neither* is singular, so the verb is **is** (Purdue OWL, subject-verb agreement).", 'Agreement'),
        item("The course teaches students writing clearly, thinking logically and [to speak confidently].", "speaking confidently", ["to speak confidently", "speak confidently", "how to speak confidently"],
             "The first two items end in -ing, so the third must too: **speaking confidently** (Purdue OWL, parallel structure).", 'Parallel structure'),
        item("All the employees must carry [his identity card] at all times.", "their identity cards", ["his identity card", "its identity card", "your identity card"],
             "A plural subject takes a plural pronoun, and the sentence stays in the third person: **their identity cards** (Purdue OWL, using pronouns clearly).", 'Pronoun agreement'),
        item("The flood was a [terrible tragedy] for the village.", "tragedy", ["terrible tragedy", "tragedy that was terrible", "very terrible tragedy"],
             "*Tragedy* already means something terrible. Purdue OWL lists *terrible tragedy* among its redundant pairs. The best phrasing is **tragedy**.", 'Redundancy'),
        item("By the time the bell rang, the students [left].", "had left", ["left", "have left", "leave"],
             "Two past events: leaving came first. The earlier event takes the past perfect, **had left** (Purdue OWL, active verb tenses).", 'Tense'),
    ]
    L3 = [
        item("[Opening the file], the error message appeared on the screen.", "When I opened the file", ["Opening the file", "Having opened the file", "To open the file"],
             "An opening phrase must name the person who did the action. *The error message* did not open the file, so the phrase must change; **When I opened the file** adds the doer (Purdue OWL, dangling modifiers).", 'Dangling modifier'),
        item("The quality of the products [have improved since they were launched].", "has improved since they were launched", ["have improved since they were launched", "have improved since it was launched", "has improved since it were launched"],
             "The subject is *quality*, which is singular, so **has improved**. *They* refers to the products (plural), so *they were launched* is right (Purdue OWL, a phrase between subject and verb).", 'Agreement'),
        item("[Due to the fact that] the rain was heavy, the match was stopped.", "Because", ["Due to the fact that", "On account of the reason that", "In light of the fact that"],
             "All four mean the same. The shortest phrase that does the job is **Because**; the others add empty words (Purdue OWL, concision).", 'Concision'),
        item("The manager praised the team for working hard, meeting every deadline and [because they stayed calm].", "staying calm", ["because they stayed calm", "to stay calm", "that they stayed calm"],
             "The list after *for* is made of -ing forms, so the last item must be an -ing form: **staying calm** (Purdue OWL, parallel structure).", 'Parallel structure'),
        item("She is looking forward [to meeting] the new team.", "to meeting", ["to meet", "for meeting", "at meet"],
             "Here *to* is a preposition, not part of an infinitive, so the verb that follows takes its -ing form: **to meeting**. A gerund can follow a preposition (Purdue OWL, gerunds). Applying that to this idiom is my own step `[INFERRED]`.", 'Gerund after a preposition'),
    ]
    return finish({1: L1, 2: L2, 3: L3}, 'V3')


PRACTICE['V3'] = v3


# ============================================================================ V1: reading comprehension (original passages, five questions each)
P_L1 = ("**Passage 1**\n\n> A small town in Karnataka started a mobile library three years ago. A van carries about two thousand books and visits twelve villages each week. "
        "Children borrow most of the books, but many adults now come to the van too, mainly for books on farming and health. The library has one rule: every borrower must return "
        "a book before taking a new one. This keeps the stock moving, and almost no books are lost. The town council pays for the van and the driver. A local school lends two "
        "teachers on Saturdays to help children choose books. Last year the library lent more than forty thousand books. The organisers now want a second van, but they have not "
        "found the money for it yet.\n")
P_L2 = ("**Passage 2**\n\n> When the firm let its staff work from home two days a week, the managers expected a drop in output. Instead, the monthly reports showed a rise of eight percent "
        "in finished projects, and the number of sick days fell. Employees said they saved about ninety minutes a day that they would have spent travelling. However, new staff found "
        "it harder to learn the firm's habits, because much of that learning happens through casual talk in the office. To fix this, the firm now asks new staff to come in every day "
        "for their first three months. Managers also meet teams weekly, so that problems are raised early instead of being left to grow. The firm has not yet decided whether to "
        "allow three days at home; it wants to wait for another six months of results before choosing.\n")
P_L3 = ("**Passage 3**\n\n> Many teachers now argue that frequent short quizzes help students more than one long exam at the end of the year. A short quiz forces a student to recall facts "
        "soon after learning them, and studies of memory suggest that recalling a fact strengthens it far more than reading it again. Opponents reply that quizzes make students "
        "anxious and turn learning into a race for marks. This worry deserves attention, but it rests on a weak assumption: that quizzes must carry heavy marks. If a quiz counts for "
        "little, or nothing, the anxiety largely disappears while the benefit of recall remains. The real question, then, is not whether to use quizzes, but how to weigh them. "
        "A school that treats each quiz as a way to check understanding, rather than a way to rank students, is likely to keep the benefit and lose most of the stress.\n")


def v1():
    def rc(passage, q, right, wrong, why, tag, first=False):
        d = judge(q, right, wrong, why, tag)
        if first:
            d['pre'] = passage
        return d
    L1 = [
        rc(P_L1, "How many villages does the van visit each week?", "Twelve", ["Two", "Forty", "Three"],
           "The passage says the van \"visits twelve villages each week\". The other numbers belong to other facts (two thousand books, forty thousand loans, three years).", 'Fact', True),
        rc(P_L1, "Who borrows most of the books?", "Children", ["Farmers", "Teachers", "Council staff"],
           "\"Children borrow most of the books.\" Adults come too, mainly for farming and health books.", 'Fact'),
        rc(P_L1, "What is the library's one rule?", "A borrower must return a book before taking a new one", ["Each book may be kept for one week only", "Children may borrow only on Saturdays", "No book may be borrowed twice"],
           "The passage states the rule directly: return a book before taking a new one.", 'Fact'),
        rc(P_L1, "Who pays for the van and the driver?", "The town council", ["A local school", "The borrowers", "The organisers"],
           "\"The town council pays for the van and the driver.\" The school only lends two teachers.", 'Fact'),
        rc(P_L1, "What do the organisers want now?", "A second van, for which they have not found the money", ["More teachers on Saturdays", "A rule change about lost books", "A new town council"],
           "The last sentence says they want a second van but have not found the money.", 'Fact'),
    ]
    L2 = [
        rc(P_L2, "Which statement best gives the main idea of the passage?", "Working from home two days a week improved results, and the firm added steps to help new staff.",
           ["The firm has decided to let staff work from home three days a week.", "Working from home made output fall, so the firm ended it.", "New staff are the only people who gain from working at home."],
           "The passage reports better output, then a problem for new staff and the firm's fix. It has *not* decided on three days, and output did not fall.", 'Main idea', True),
        rc(P_L2, "Why must new staff come in every day for their first three months?", "Much of the learning about the firm's habits happens through casual talk in the office.",
           ["They were less productive at home than other staff.", "Managers do not trust new staff.", "They travel less than other staff."],
           "The passage gives this reason directly: casual talk in the office is where the habits are learned.", 'Reason'),
        rc(P_L2, "Which of these is NOT mentioned as a result of working from home?", "Lower office rent", ["Higher output", "Fewer sick days", "Time saved on travel"],
           "Output (up eight percent), sick days (fewer) and travel time (about ninety minutes a day) are all stated. Rent is never mentioned.", 'Not mentioned'),
        rc(P_L2, "In the passage, \"raised\" in \"problems are raised early\" most nearly means", "brought up for discussion", ["lifted physically", "made larger", "grown like crops"],
           "Substitute each option: managers meet teams so that problems are *brought up* early instead of being left to grow. The other meanings do not fit.", 'Word in context'),
        rc(P_L2, "What does the firm plan to do about allowing three days at home?", "Wait for six more months of results before choosing", ["Allow it from next month", "Refuse it for new staff only", "Ask staff to vote now"],
           "The last sentence says it will wait for another six months of results.", 'Detail'),
    ]
    L3 = [
        rc(P_L3, "Which statement best gives the author's main point?", "Frequent quizzes can help learning without much stress if they carry few marks.",
           ["Long exams at the end of the year are better than quizzes.", "Quizzes cannot be used without making students anxious.", "Students should never be ranked."],
           "The author backs quizzes, answers the anxiety worry by lowering the stakes, and says the question is how to weigh them.", 'Main idea', True),
        rc(P_L3, "How does the author treat the opponents' worry about anxiety?", "As a worry worth attention, but one that can be answered",
           ["As a worry with no basis at all", "As proof that quizzes should be dropped", "As a worry the author has not understood"],
           "\"This worry deserves attention, but it rests on a weak assumption\": taken seriously, then answered.", 'Attitude'),
        rc(P_L3, "Which assumption does the author call weak?", "That quizzes must carry heavy marks", ["That recalling a fact strengthens it", "That teachers support quizzes", "That exams come at the end of the year"],
           "The sentence after \"a weak assumption\" names it: \"that quizzes must carry heavy marks\".", 'Detail'),
        rc(P_L3, "Which finding would most weaken the author's argument?", "Students become anxious even about quizzes that carry no marks",
           ["Students remember facts better after a quiz", "Many schools already hold weekly quizzes", "Quizzes take only ten minutes"],
           "The author says anxiety \"largely disappears\" when quizzes carry little or no weight. Finding anxiety even then attacks that claim. The other options do not.", 'Weaken'),
        rc(P_L3, "With which statement would the author most likely agree?", "A school should use quizzes mainly to check understanding.", ["A school should rank students after every quiz.", "A school should replace all lessons with quizzes.", "A school should avoid quizzes altogether."],
           "The last sentence says a school that uses quizzes to check understanding, not to rank, keeps the benefit and loses most of the stress.", 'Inference'),
    ]
    return finish({1: L1, 2: L2, 3: L3}, 'V1')


PRACTICE['V1'] = v1


# ============================================================================ V6: critical reasoning (original arguments)
def v6():
    def cr(arg, question, right, wrong, why, tag):
        stem = f"> {arg}\n\n{question}"
        return judge(stem, right, wrong, why, tag)
    L1 = [
        cr("The canteen raised its prices last month. Since then, fewer staff eat there, and the canteen's income has fallen. The canteen should lower its prices again.",
           "Which sentence is the main conclusion of the argument?", "The canteen should lower its prices again.",
           ["The canteen raised its prices last month.", "Fewer staff eat in the canteen.", "The canteen's income has fallen."],
           "A conclusion is the point the other sentences support. The first three are reasons or facts; the last one says what should be done.", 'Conclusion'),
        cr("All the trains on the Chennai line stop at Katpadi. This train is on the Chennai line.",
           "Which statement must be true?", "This train stops at Katpadi.", ["This train starts at Katpadi.", "Only trains on the Chennai line stop at Katpadi.", "Every train that stops at Katpadi is on the Chennai line."],
           "Every train on the line stops there, and this train is on the line. The other options claim more than the facts say.", 'Inference'),
        cr("In a survey of 200 students, 150 said they use the college library at least once a week.",
           "Which statement must be true?", "At least 150 of the students surveyed use the library at least once a week.",
           ["Most students in the college use the library every day.", "75 percent of all students in the country use their library weekly.", "Fifty of the students never use the library."],
           "150 of the 200 surveyed said so. Nothing is said about other students, about daily use, or about the other 50 (they may use it less than weekly).", 'Inference'),
        cr("A shop plans to stay open until 9 p.m. because it believes evening customers will raise its sales.",
           "Which fact most strengthens the shop's plan?", "Many people in the area finish work after 6 p.m. and buy groceries on their way home.",
           ["The shop's lights are old and use a lot of power.", "Other shops in the area close at 6 p.m.", "The shop owner lives nearby."],
           "A fact that shows customers exist in the evening supports the belief. The other options do not show that anyone would buy.", 'Strengthen'),
        cr("App X is better than App Y, because App X has been downloaded many more times.",
           "Which fact most weakens this argument?", "App X comes pre-installed on most new phones, so many downloads happen automatically.",
           ["App Y was launched one year ago.", "App X is free to download.", "Both apps have a blue icon."],
           "If most downloads are automatic, the count says little about whether people prefer App X. The other options do not touch the reasoning.", 'Weaken'),
    ]
    L2 = [
        cr("A school added a ten-minute walk after lunch. Within a term, afternoon test scores rose. The principal concludes that the walk raised the scores.",
           "Which fact most strengthens the principal's conclusion?", "Afternoon scores in classes of the same school that did not take the walk stayed the same.",
           ["The walk was popular with the teachers.", "The school has a large playground.", "Test scores were also high in the morning."],
           "A comparison group that did not walk and did not improve shows the rise is more likely due to the walk (this is what a good test needs).", 'Strengthen'),
        cr("A school added a ten-minute walk after lunch. Within a term, afternoon test scores rose. The principal concludes that the walk raised the scores.",
           "Which fact most weakens the principal's conclusion?", "In the same term the school also began extra afternoon tutoring for every class.",
           ["The walk takes place on the school grounds.", "Some students walked faster than others.", "The principal supports the walk."],
           "If another change (extra tutoring) started at the same time, it offers a different explanation for the rise.", 'Weaken'),
        cr("The market street should be closed to cars, because it is noisy and crowded with traffic.",
           "The argument depends on which assumption?", "Closing the street to cars would reduce the noise and the crowding.",
           ["The market is the oldest in the city.", "Most shoppers arrive by bus.", "Cars are the main reason people visit the market."],
           "Without the belief that closing the street would ease the noise and crowding, the reason given would not lead to the conclusion.", 'Assumption'),
        cr("Every parcel sent by Express is delivered within two days. Anu's parcel was delivered in four days.",
           "What can be concluded?", "Anu's parcel was not sent by Express.", ["Anu's parcel was lost.", "Express is slower than other services.", "Anu paid too little."],
           "If Express always delivers in two days, a parcel that took four days cannot have been sent by Express.", 'Inference'),
        cr("A café notes that on days when it sells more iced coffee, its sales of salads also rise. The owner decides that iced coffee makes customers buy salads.",
           "Which fact most weakens the owner's decision?", "Both iced coffee and salad sales rise on hot days, when more people visit.",
           ["Iced coffee costs more than salads.", "The café sells soup in winter.", "Salads are made fresh each morning."],
           "A third factor (hot weather) could explain both rises, so one need not cause the other.", 'Weaken'),
    ]
    L3 = [
        cr("The city should build a second bridge, because the existing bridge is crowded every morning.",
           "Which assumption does the argument NEED to be reasonable?", "The crowding would not simply move to the new bridge and stay as bad.",
           ["The existing bridge was built after 1990.", "Every morning commuter wants a new bridge.", "A second bridge would be free to build."],
           "The plan only helps if a new bridge actually eases the crowding. The other options are not needed for that.", 'Assumption'),
        cr("All members of the chess club are good at maths. Priya is good at maths. So Priya is a member of the chess club.",
           "What is the flaw in this argument?", "Being good at maths is not shown to be enough to be a member; others may be good at maths too.",
           ["It assumes Priya plays chess well.", "It uses a survey that is too small.", "It argues in a circle."],
           "The first statement says club members are good at maths, not that everyone good at maths is a member. The conclusion reverses it.", 'Flaw'),
        cr("In seaside towns, ice cream sales and drowning cases both go up in the same months. A columnist says that eating ice cream causes drowning.",
           "What is the flaw in the columnist's reasoning?", "Both may be caused by something else, such as hot weather that brings crowds to the beach.",
           ["It uses too many numbers.", "It assumes people like ice cream.", "It ignores that some towns have no sea."],
           "Two things rising together does not show one causes the other; a common cause explains the pattern more simply.", 'Flaw'),
        cr("A company says its new training programme raises sales: staff who took it sold 12 percent more than they did before.",
           "Which question would be most useful in judging the company's claim?", "Did staff who did not take the training also sell more over the same period?",
           ["How long was each training session?", "Who designed the training programme?", "Do the trainers have degrees?"],
           "If untrained staff also sold more, the rise may have another cause (a busy season), so the training is not shown to matter.", 'Evaluate'),
        cr("In a hostel of 80 students, every student who plays cricket also plays football. Thirty students play football.",
           "Which statement must be true?", "At most 30 students play cricket.", ["Exactly 30 students play cricket.", "At least 30 students play cricket.", "50 students play neither game."],
           "Cricket players are all inside the group of footballers, so they cannot be more than 30. Nothing says how many there are, and some of the other 50 may play other games.", 'Inference'),
    ]
    return finish({1: L1, 2: L2, 3: L3}, 'V6')


PRACTICE['V6'] = v6


# ============================================================================ G2: cloze passages with five numbered blanks (original passages)
def g2():
    def blank(passage, k, right, wrong, why, tag, first=False):
        stem = f"Passage {passage[0]}: choose the word or phrase that best fills blank **({k})**."
        d = judge(stem, right, wrong, why, tag)
        if first:
            d['pre'] = passage[1]
        return d
    p1 = (1, "**Passage 1**\n\n> Meena is a student in Mysuru. She keeps her notebooks **(1)** the shelf above her bed. She wakes up at six **(2)** the morning and studies for two hours before college. Yesterday she **(3)** late for the first class "
             "because the bus broke down. She walked **(4)** the college gate and sat in the last row. After class, she told the teacher about the delay. The teacher was kind, **(5)** she did not mind.\n")
    p2 = (2, "**Passage 2**\n\n> The company opened **(1)** new branch in Coimbatore in 2021. Since then, it **(2)** more than fifty people. Last month the manager announced that a bigger office "
             "**(3)** next year. By the time the new building is ready, the team **(4)** from the old office for three years. **(5)** the cost is high, the board has approved the plan.\n")
    p3 = (3, "**Passage 3**\n\n> The invention of **(1)** printing press changed how people shared **(2)**. Before it, books **(3)** by hand, so only a few people could afford them. By 1500, printers "
             "**(4)** millions of books across Europe. The spread of printed books **(5)** to higher literacy across the continent.\n")
    L1 = [
        blank(p1, 1, "on", ["in", "at", "to"], "Something resting on a surface takes **on**: *I left your keys on the table* (Purdue OWL, prepositions of place).", 'Preposition', True),
        blank(p1, 2, "in", ["on", "at", "by"], "**In** is used with parts of the day, as in *in the afternoon* (Purdue OWL, prepositions of time), so *in the morning*.", 'Preposition'),
        blank(p1, 3, "arrived", ["arrives", "has arrived", "will arrive"], "*Yesterday* is a finished time, so the past simple **arrived** (British Council, present perfect).", 'Tense'),
        blank(p1, 4, "to", ["at", "in", "on"], "Movement towards a place takes **to**: walked to the gate.", 'Preposition'),
        blank(p1, 5, "so", ["but", "because", "unless"], "The teacher was kind, and as a result she did not mind: **so** shows the result.", 'Connector'),
    ]
    L2 = [
        blank(p2, 1, "a", ["an", "the", "no article"], "First mention of one branch among others: **a**. *Branch* begins with a consonant sound (Purdue OWL, articles).", 'Article', True),
        blank(p2, 2, "has hired", ["hired", "had hired", "hires"], "*Since then* with a story that runs up to now takes the present perfect, **has hired** (British Council, present perfect).", 'Tense'),
        blank(p2, 3, "will be opened", ["will open", "is opened", "has opened"], "The office does not open itself: it is opened by the company. A future passive is *will be* plus the past participle: **will be opened** (Purdue OWL, passive verbs; the future form is my extension `[INFERRED]`).", 'Voice'),
        blank(p2, 4, "will have worked", ["works", "has worked", "had worked"], "*By the time the new building is ready* names a future deadline, so the future perfect **will have worked** is used (Purdue OWL, active verb tenses).", 'Tense'),
        blank(p2, 5, "Although", ["Because", "Unless", "So"], "A high cost would normally stop a plan, so the two parts contrast: **Although**.", 'Connector'),
    ]
    L3 = [
        blank(p3, 1, "the", ["a", "an", "no article"], "A specific, well-known invention: **the** printing press (Purdue OWL, articles).", 'Article', True),
        blank(p3, 2, "information", ["informations", "an information", "the informations"], "*Information* is uncountable: no plural and no *an* (Purdue OWL, uncountable nouns).", 'Noun form'),
        blank(p3, 3, "were copied", ["copied", "have copied", "had copying"], "Books do not copy themselves: **were copied** by people, a past passive (Purdue OWL, passive verbs; the past form is my extension `[INFERRED]`).", 'Voice'),
        blank(p3, 4, "had produced", ["have produced", "produce", "producing"], "*By 1500* names a point in the past, and the printing had happened before it, so the past perfect **had produced** (Purdue OWL, active verb tenses).", 'Tense'),
        blank(p3, 5, "led", ["lead", "leading", "leads"], "The passage is in the past tense, so **led**: *led to higher literacy*.", 'Tense'),
    ]
    return finish({1: L1, 2: L2, 3: L3}, 'G2')


PRACTICE['G2'] = g2


# ============================================================================ W1: the essay and the email (writing-skill questions; the writing itself is practised from the prompts in the lesson)
def w1():
    J = judge
    L1 = [
        J("You must write to your manager to ask for two days of leave. Which subject line is best?", "Request for two days' leave, 12 and 13 March",
          ["Hello", "URGENT!!! PLEASE READ", "Leave"], "A meaningful subject line tells the reader what the email is about (Purdue OWL, email etiquette).", 'Subject line'),
        J("You are writing to Mr Rao, a training manager you have not met. Which greeting is best?", "Dear Mr Rao,", ["Hey Rao", "Hi everyone", "Dear friend"],
          "Open a formal email with a greeting such as *Dear Dr. Jones,*, followed by a comma (Purdue OWL, email etiquette; British Council, starting and finishing emails).", 'Greeting'),
        J("Which closing is best for the same email?", "Yours sincerely, Arjun Menon", ["Cheers, Arjun", "Bye for now, Arjun", "See you!! Arjun"],
          "Formal closings listed by the British Council include *Yours sincerely,* followed by the name. The other three are friendly and informal (Purdue OWL: a sign-off phrase and the sender's name).", 'Closing'),
        J("Which sentence suits a formal email?", "I would be grateful if you could confirm the date.", ["Tell me the date asap.", "Gimme the date.", "U need to confirm the date."],
          "Use standard spelling and no text abbreviations such as *u* (Purdue OWL, email etiquette). The first option is also polite.", 'Tone'),
        J("An essay answer should begin with", "a one-sentence thesis that answers the question", ["a long story about your day", "a list of every point you know", "a quotation with no explanation"],
          "Begin with a one or two sentence thesis that restates the question as a statement (Purdue OWL, essays for exams).", 'Opening'),
    ]
    L2 = [
        J("Essay question: \"Is online learning better than classroom learning?\" Which opening sentence is the clearest thesis?",
          "Online learning is more flexible, but classroom learning is better for building habits and friendships.",
          ["Many people have different opinions about learning.", "Learning is important.", "I will now write about learning."],
          "A thesis takes a position that answers the question. The other openings only name the topic or announce what is coming (Purdue OWL, essays for exams).", 'Thesis'),
        J("Which sentence does NOT belong in this paragraph?\n\n(1) Vehicle smoke is a major cause of air pollution. (2) Factories also release harmful gases. (3) The city's new library has a large reading hall. (4) Burning waste in open spaces adds to the problem.",
          "(3)", ["(1)", "(2)", "(4)"], "Sentences 1, 2 and 4 are causes of air pollution. Sentence 3 is about a library, so it breaks the paragraph's single idea.", 'Unity'),
        J("Which is the best topic sentence for a paragraph that lists three causes of stress among students?", "Students face stress from exams, long hours and family expectations.",
          ["Stress.", "Many things happen in life.", "I am a student."], "A topic sentence states the paragraph's one idea and hints at its three parts.", 'Topic sentence'),
        J("Which is the best final sentence for an essay arguing that recycling saves resources?", "Recycling is a small habit that saves resources for the future, and everyone should adopt it.",
          ["That is all I know about recycling.", "Another thing about recycling is plastic bottles.", "Recycling is a topic."],
          "A conclusion returns to the main point and closes it. The others add a new point, apologise, or say nothing.", 'Conclusion'),
        J("The factory reduced its smoke. ___, the air in the town is cleaner.", "As a result", ["However", "For example", "On the other hand"],
          "The cleaner air follows from the reduced smoke, so a word of result is needed: **As a result**.", 'Transition'),
    ]
    L3 = [
        J("Which version is the most concise without losing meaning?", "If it rains, the match will be cancelled.",
          ["In the event that it rains, the match will be cancelled.", "Should it be the case that it rains, the match will be cancelled.", "In the event of the situation where it rains, the match will be cancelled."],
          "All four mean the same, so the shortest is best (Purdue OWL, concision).", 'Concision'),
        J("Put the parts of a formal request email in the best order: A greeting, B reason for writing, C details, D request and thanks, E closing and name.",
          "A, B, C, D, E", ["B, A, C, E, D", "A, C, B, E, D", "E, A, B, C, D"],
          "Greet first, say why you are writing, give the details, make the request and thank the reader, then close with your name.", 'Order'),
        J("Which sentence removes the unclear pronoun in \"The manager told the engineer that he would get a bonus\"?", "The manager said to the engineer, \"You will get a bonus.\"",
          ["The manager told the engineer that he would get a bonus soon.", "The manager and the engineer got a bonus when he said so.", "It was said that he would get a bonus."],
          "In the original, *he* could be the manager or the engineer. Quoting the words ends the doubt (Purdue OWL, using pronouns clearly: refer to a specific noun).", 'Clear pronoun'),
        J("You have 10 minutes for a 190-word essay. Which plan is best?", "2 minutes planning, 6 minutes writing, 2 minutes checking",
          ["9 minutes writing, 1 minute thinking", "Write the conclusion first and then stop", "Spend 5 minutes choosing a title"],
          "Budget your time, plan, write and proofread (Purdue OWL, essays for exams). Six minutes is enough for about 190 words if you have planned.", 'Time'),
        J("Which sentence best supports the claim \"Reading every day improves vocabulary\"?", "A student who reads for thirty minutes a day meets hundreds of new words in a month.",
          ["Everyone knows reading is good.", "Reading is fun and relaxing.", "Many people read."],
          "Support a point with specific evidence, not a general statement (Purdue OWL, essays for exams).", 'Support'),
    ]
    return finish({1: L1, 2: L2, 3: L3}, 'W1')


PRACTICE['W1'] = w1


# ============================================================================ P1: loops and trace tables (programs printed in the official dialect, answers run as Java)
def trace_lines(lo, hi, need=None):
    """gen_trace, but only programs whose printed length is lo..hi lines (and, optionally, which contain a nested loop or a break/continue)."""
    def g(rng):
        q = GC.gen_trace(rng)
        if q is None:
            return None
        text = GC.render_official(q['prog'])
        if not (lo <= len(text) <= hi):
            return None
        joined = '\n'.join(text)
        if need == 'nested' and joined.count('For (') < 2 and 'break' not in joined and 'continue' not in joined and joined.count('While') < 2:
            return None
        q['steps'] = len(text)
        return q
    g.__name__ = 'trace_lines'
    return persist(g)


def p1():
    L1 = [q for t in (1, 2, 3, 4, 5) for q in draw(trace_lines(6, 8), 1, 'P1', 1, t)]
    L2 = [q for t in (1, 2, 3, 4, 5) for q in draw(trace_lines(9, 11), 1, 'P1', 2, t)]
    L3 = [q for t in (1, 2, 3, 4, 5) for q in draw(trace_lines(13, 13, 'nested'), 1, 'P1', 3, t)]
    return finish({1: L1, 2: L2, 3: L3}, 'P1')


PRACTICE['P1'] = p1


# ============================================================================ P3: bitwise operators, P5: arrays (printed programs, answers run as Java)
import gen_cc_code as CC


def p3():
    L1 = [q for t in (1, 2, 3, 4, 5) for q in draw(persist(CC.gen_bitwise), 1, 'P3', 1, t, lvl=1)]
    L2 = [q for t in (1, 2, 3, 4, 5) for q in draw(persist(CC.gen_bitwise), 1, 'P3', 2, t, lvl=2)]
    L3 = [q for t in (1, 2, 3, 4, 5) for q in draw(persist(CC.gen_bitwise), 1, 'P3', 3, t, lvl=3)]
    return finish({1: L1, 2: L2, 3: L3}, 'P3')


PRACTICE['P3'] = p3


def p5():
    def arr(level, tag, kind):
        return draw(persist(CC.gen_array), 1, 'P5', level, tag, kind=kind)
    L1 = arr(1, 1, 'sum') + arr(1, 2, 'max') + arr(1, 3, 'count_gt') + arr(1, 4, 'max') + arr(1, 5, 'count_gt')
    L2 = arr(2, 1, 'even_index') + arr(2, 2, 'reverse') + arr(2, 3, 'prefix') + arr(2, 4, 'even_index') + arr(2, 5, 'prefix')
    L3 = arr(3, 1, 'swap_pairs') + arr(3, 2, 'longest_run') + arr(3, 3, 'product_except') + arr(3, 4, 'longest_run') + arr(3, 5, 'swap_pairs')
    return finish({1: L1, 2: L2, 3: L3}, 'P5')


PRACTICE['P5'] = p5
