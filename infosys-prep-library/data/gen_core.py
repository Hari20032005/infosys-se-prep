"""Generator plumbing. Every generated question carries a `check` callable that recomputes the
answer by a DIFFERENT route from the one that produced it (brute force, simulation, or an
inverse); `run()` asserts the two agree at build time and counts them for the QA report."""
import random

STATS = {'generated': 0, 'checked': 0}


def Q(q, opts, why, check, tag=None, fixed=False):
    """opts[0] is the correct option. check() must return the correct option string independently.
    fixed=True: the options are printed in sorted order (the official 1/2/3/4 data-sufficiency scale) instead of being shuffled."""
    return dict(q=q, opts=[str(o) for o in opts], why=why, check=check, tag=tag, fixed=fixed)


def run(gen, seed, n, **kw):
    """Generate n questions with unique stems, asserting each independent check."""
    rng = random.Random(seed)
    out, seen, guard = [], set(), 0
    while len(out) < n:
        guard += 1
        assert guard < n * 400, f"{gen.__name__}: cannot produce {n} distinct questions"
        q = gen(rng, **kw)
        if q is None or q['q'] in seen:
            continue
        if len(set(q['opts'])) != 4:
            continue
        got = str(q['check']())
        assert got == q['opts'][0], f"{gen.__name__}: check {got!r} != key {q['opts'][0]!r} for\n{q['q']}"
        STATS['generated'] += 1
        STATS['checked'] += 1
        seen.add(q['q'])
        out.append(q)
    return out


def distinct_wrong(answer, candidates, rng, lo=None, hi=None, need=3):
    """Pick `need` distinct wrong numeric options: candidates first, then nearby offsets."""
    wrong = []
    for c in candidates:
        if c != answer and c not in wrong and (lo is None or c >= lo) and (hi is None or c <= hi):
            wrong.append(c)
    off = [1, -1, 2, -2, 10, -10, 3, -3, 5, -5, 4, -4, 6, 8, 12]
    rng.shuffle(off)
    for o in off:
        if len(wrong) >= need + 4:
            break
        c = answer + o
        if c != answer and c not in wrong and (lo is None or c >= lo) and (hi is None or c <= hi):
            wrong.append(c)
    head = wrong[:need]
    return head


def fmt(x):
    if isinstance(x, float) and abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return str(x)
