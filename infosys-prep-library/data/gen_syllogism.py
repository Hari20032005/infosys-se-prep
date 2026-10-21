"""Syllogism questions ("Statements ... Conclusions I and II ... which follows?") for the Core Course.

A statement is ('all' | 'some' | 'no' | 'some_not', A, B) over three classes X, Y, Z.
Convention (the usual exam one, and the one the library's syllogism checkers use): every named class has at least one member.

Two independent ways to decide whether a conclusion follows:
  route 1 (used to build the question, because it is fast): a search over worlds described by WHICH of the 8 Venn regions are occupied (255 worlds);
  route 2 (the check, run once per accepted question): official_sample.follows, a search over worlds of 5 individuals (32,768 worlds).
They share no code, so a bug in one would show up as a disagreement."""
import itertools

import official_sample as OS
from gen_core import Q

LABELS = {'only1': 'Only conclusion I follows', 'only2': 'Only conclusion II follows', 'both': 'Both I and II follow',
          'neither': 'Neither I nor II follows', 'either': 'Either I or II follows'}
TEXT = {'all': 'All {a} are {b}.', 'some': 'Some {a} are {b}.', 'no': 'No {a} are {b}.', 'some_not': 'Some {a} are not {b}.'}
VOCAB = [('doctors', 'graduates', 'readers'), ('roses', 'flowers', 'plants'), ('teachers', 'adults', 'citizens'), ('laptops', 'computers', 'machines'),
         ('poets', 'writers', 'artists'), ('engineers', 'professionals', 'workers'), ('trains', 'vehicles', 'transport'), ('cats', 'pets', 'animals'),
         ('pens', 'tools', 'objects'), ('mangoes', 'fruits', 'foods')]


def stmt_text(st):
    k, a, b = st
    return TEXT[k].format(a=a, b=b)


# ---------------------------------------------------------------- route 2: occupied Venn regions
def _holds(st, regions, idx):
    k, a, b = st
    A = [r for r in regions if r >> idx[a] & 1]
    B = lambda r: r >> idx[b] & 1
    return {'all': lambda: all(B(r) for r in A), 'some': lambda: any(B(r) for r in A),
            'no': lambda: not any(B(r) for r in A), 'some_not': lambda: any(not B(r) for r in A)}[k]()


def region_worlds(sets):
    idx = {s: i for i, s in enumerate(sets)}
    for mask in range(1, 2 ** 8):
        regions = [r for r in range(8) if mask >> r & 1]
        if all(any(r >> idx[s] & 1 for r in regions) for s in sets):          # every class has a member
            yield regions, idx


def classify_regions(premises, concs, sets):
    """-> 'only1' | 'only2' | 'both' | 'neither' | 'either', or None if the premises cannot all be true."""
    worlds = [(r, i) for r, i in region_worlds(sets) if all(_holds(p, r, i) for p in premises)]
    if not worlds:
        return None
    f = [all(_holds(c, r, i) for r, i in worlds) for c in concs]
    if f[0] and f[1]: return 'both'
    if f[0]: return 'only1'
    if f[1]: return 'only2'
    if all(_holds(concs[0], r, i) or _holds(concs[1], r, i) for r, i in worlds): return 'either'
    return 'neither'


# ---------------------------------------------------------------- route 1: five-individual worlds (official_sample.follows)
def classify_people(premises, concs, sets):
    f = [OS.follows(premises, c, sets) for c in concs]
    if f[0] and f[1]: return 'both'
    if f[0]: return 'only1'
    if f[1]: return 'only2'
    # "either": in every world satisfying the premises, I or II is true  <=>  neither (not I and not II) is possible
    neg = {'all': 'some_not', 'some': 'no', 'no': 'some', 'some_not': 'all'}
    n1, n2 = (neg[concs[0][0]], concs[0][1], concs[0][2]), (neg[concs[1][0]], concs[1][1], concs[1][2])
    both_false = _possible(premises + [n1, n2], sets)
    return 'neither' if both_false else 'either'


def _possible(statements, sets, n=5):
    idx = {s: i for i, s in enumerate(sets)}
    for bits in itertools.product(range(2 ** len(sets)), repeat=n):
        if not all(any(m >> idx[s] & 1 for m in bits) for s in sets):
            continue
        if all(OS._h(st, bits, idx) for st in statements):
            return True
    return False


# ---------------------------------------------------------------- the generator
def gen_syllogism(rng, want=None, forms=('all', 'some', 'no', 'some_not')):
    X, Y, Z = rng.choice(VOCAB)
    k1, k2 = rng.choice(forms), rng.choice(forms)
    p1 = (k1, X, Y) if rng.random() < 0.5 else (k1, Y, X)
    p2 = (k2, Y, Z) if rng.random() < 0.5 else (k2, Z, Y)
    cands = [(k, a, b) for k in ('all', 'some', 'no', 'some_not') for a, b in ((X, Z), (Z, X))]
    c1, c2 = rng.sample(cands, 2)
    sets = [X, Y, Z]
    ans = classify_regions([p1, p2], [c1, c2], sets)
    if ans is None or (want and ans != want):
        return None
    labels = list(LABELS)
    wrong = [l for l in labels if l != ans]
    rng.shuffle(wrong)
    q = (f"Statements:\n\nStatement 1: {stmt_text(p1)}\nStatement 2: {stmt_text(p2)}\n\nConclusions:\n\nI. {stmt_text(c1)}\nII. {stmt_text(c2)}\n\n"
         "Which option is correct? (Treat every group named as having at least one member.)")
    why = (f"Tried every possible arrangement of the three groups that makes both statements true. Conclusion I {'holds in all of them' if ans in ('only1', 'both') else 'fails in at least one'}; "
           f"conclusion II {'holds in all of them' if ans in ('only2', 'both') else 'fails in at least one'}. "
           + ("Whichever arrangement you pick, one of the two conclusions is true, but neither is true in every arrangement, so **either I or II** follows. " if ans == 'either' else "")
           + f"Result: **{LABELS[ans].lower()}**.")
    qd = Q(q, [LABELS[ans]] + [LABELS[w] for w in wrong[:3]], why, lambda: LABELS[classify_people([p1, p2], [c1, c2], sets)], tag='Syllogism')
    qd['syl'] = (p1, p2, c1, c2, sets)
    return qd


# ---------------------------------------------------------------- table of what follows from a chain of two premises (for the lesson)
def chain_table():
    """For premises relating X-Y and Y-Z, which statements about X and Z follow. Returns {(p1, p2): [conclusions]}."""
    X, Y, Z = 'X', 'Y', 'Z'
    sets = [X, Y, Z]
    out = {}
    concl = [(k, a, b) for k in ('all', 'some', 'no', 'some_not') for a, b in ((X, Z), (Z, X))]
    for k1, k2 in itertools.product(('all', 'some', 'no', 'some_not'), repeat=2):
        for p1 in ((k1, X, Y), (k1, Y, X)):
            for p2 in ((k2, Y, Z), (k2, Z, Y)):
                if classify_regions([p1, p2], [concl[0], concl[0]], sets) is None:
                    continue
                out[(p1, p2)] = [c for c in concl if all(_holds(c, r, i) for r, i in region_worlds(sets)
                                                         if all(_holds(p, r, i) for p in (p1, p2)))]
    return out
