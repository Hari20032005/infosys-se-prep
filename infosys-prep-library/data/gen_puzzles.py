"""Numerical-puzzle generators (sections Z1 and Z2, and the Numerical Puzzle part of the mock).

The rule families below are the ones seen in the observed pool (questions Z01-Z15 in
questions-observed.csv). Each instance is checked for UNIQUENESS against a library of
competing rules: every rule that reproduces all the worked examples must give the same
answer for the query, otherwise the instance is discarded and redrawn.
"""
import itertools, math, random
from gen_core import Q, distinct_wrong, fmt

def disp(rule):
    """Rule name as shown to learners: a real multiplication sign and superscripts, because '**a*b**' breaks Markdown bold."""
    return rule.replace('*', '×').replace('^2', '²').replace('^3', '³')


dp = lambda n: (n // 10) * (n % 10)          # product of the two digits
ds = lambda n: sum(map(int, str(n)))         # digit sum

# ---------------------------------------------------------------- pair rules  (a, b) -> v
PAIR = {}
for k in (1, 2, 3, 4, 5, 10):
    PAIR[f'a*b + {k}'] = (lambda k: lambda a, b: a * b + k)(k)
    PAIR[f'a*b - {k}'] = (lambda k: lambda a, b: a * b - k)(k)
for k in (2, 3, 4, 5):
    PAIR[f'({k})(a+b)'] = (lambda k: lambda a, b: k * (a + b))(k)
    PAIR[f'{k}a + b'] = (lambda k: lambda a, b: k * a + b)(k)
    PAIR[f'a + {k}b'] = (lambda k: lambda a, b: a + k * b)(k)
    PAIR[f'{k}a - b'] = (lambda k: lambda a, b: k * a - b)(k)
    PAIR[f'{k}(a-b)'] = (lambda k: lambda a, b: k * (a - b))(k)
PAIR.update({
    'a^2 - b^2': lambda a, b: a * a - b * b,
    'a^2 + b^2': lambda a, b: a * a + b * b,
    'a^2 + b': lambda a, b: a * a + b,
    'a^2 - b': lambda a, b: a * a - b,
    'a + b^2': lambda a, b: a + b * b,
    'a*b + a + b': lambda a, b: a * b + a + b,
    'a*b - a - b': lambda a, b: a * b - a - b,
    'a*b + (a-b)': lambda a, b: a * b + (a - b),
    'a*(b+1)': lambda a, b: a * (b + 1),
    '(a+b)^2': lambda a, b: (a + b) ** 2,
    '(a+b)(a-b)+b': lambda a, b: (a + b) * (a - b) + b,
    'a*b': lambda a, b: a * b,
})
DIGIT = {   # two-digit inputs
    'digit-product(a) - digit-product(b)': lambda a, b: dp(a) - dp(b),
    'digit-product(a) + digit-product(b)': lambda a, b: dp(a) + dp(b),
    'digit-sum(a + b)': lambda a, b: ds(a + b),
    'digit-sum(a) * digit-sum(b)': lambda a, b: ds(a) * ds(b),
    'digit-sum(a) + digit-sum(b)': lambda a, b: ds(a) + ds(b),
}
# rules shown to learners in worked explanations (plain English)
PAIR_TEXT = {name: name for name in list(PAIR) + list(DIGIT)}


def sole(d):
    vals = set(d.values())
    assert len(vals) == 1, d
    return vals.pop()


def _fit(rules, examples, query):
    """Answers given by every library rule that reproduces all examples."""
    out = {}
    for name, f in rules.items():
        try:
            if all(f(*inp) == v for inp, v in examples):
                out[name] = f(*query)
        except Exception:
            pass
    return out


def gen_pair(rng, digit=False, names=None, span=None, lib=None):
    lib = lib or (DIGIT if digit else PAIR)
    name = rng.choice(list(names) if names else list(lib))
    f = lib[name]
    lo, hi = span or ((11, 99) if digit else (2, 20))
    pts = [(rng.randint(lo, hi), rng.randint(lo, hi)) for _ in range(4)]
    if len({p for p in pts}) < 4 or any(a == b for a, b in pts):
        return None
    vals = [f(*p) for p in pts]
    if any(v < 0 or v > 999 for v in vals) or len(set(vals)) < 4:
        return None
    ex, qpt = list(zip(pts[:3], vals[:3])), pts[3]
    ans = vals[3]
    fit = _fit(lib, ex, qpt)
    if set(fit.values()) != {ans}:
        return None                                   # another library rule fits the examples but disagrees
    # distractors: rules that fit the first two examples but not the third
    near = _fit(lib, ex[:2], qpt)
    cands = [v for n, v in near.items() if v != ans and v >= 0]
    rng.shuffle(cands)
    wrong = distinct_wrong(ans, cands, rng, lo=0)
    lines = '\n'.join(f"({a}, {b}) → {v}" for (a, b), v in ex)
    q = f"Find the missing number, using the same rule in every line:\n\n```text\n{lines}\n({qpt[0]}, {qpt[1]}) → ?\n```\n"
    why = (f"Test rules on the first line, then confirm on the second. The rule that fits all three lines is **{disp(name)}**: "
           + '; '.join(f"({a}, {b}) → {v}" for (a, b), v in ex) + f". Applied to ({qpt[0]}, {qpt[1]}) it gives **{ans}**. "
           f"({len(lib)} candidate rules were tried; only this one fits.)")
    qd = Q(q, [ans] + wrong, why, lambda: sole(fit), tag='Pair rule')
    qd['rule'] = name
    return qd


# ---------------------------------------------------------------- figure rules: four outer numbers -> centre
FIG = {
    'a*b - c*d': lambda a, b, c, d: a * b - c * d,
    'a*b + c*d': lambda a, b, c, d: a * b + c * d,
    'a*d - b*c': lambda a, b, c, d: a * d - b * c,
    'a*d + b*c': lambda a, b, c, d: a * d + b * c,
    '(a+b)(c+d) / 2': lambda a, b, c, d: (a + b) * (c + d) // 2 if (a + b) * (c + d) % 2 == 0 else -1,
    'a + b + c + d + 4': lambda a, b, c, d: a + b + c + d + 4,
    'a*c + b*d': lambda a, b, c, d: a * c + b * d,
    'a*c - b*d': lambda a, b, c, d: a * c - b * d,
    'a + b*c - d': lambda a, b, c, d: a + b * c - d,
    'a*b + c - d': lambda a, b, c, d: a * b + c - d,
    '(a+c)*(b-d)': lambda a, b, c, d: (a + c) * (b - d),
    '2(a+b+c+d)': lambda a, b, c, d: 2 * (a + b + c + d),
    'a^2 + b^2 - c - d': lambda a, b, c, d: a * a + b * b - c - d,
}


def gen_figure(rng, names=None, top=15, lib=None):
    lib = lib or FIG
    name = rng.choice(list(names) if names else list(lib))
    f = lib[name]
    figs = [tuple(rng.randint(2, top) for _ in range(4)) for _ in range(4)]
    if len(set(figs)) < 4:
        return None
    vals = [f(*x) for x in figs]
    if any(v <= 0 or v > 400 for v in vals) or len(set(vals)) < 4:
        return None
    ex, qf = list(zip(figs[:3], vals[:3])), figs[3]
    ans = vals[3]
    fit = _fit(lib, ex, qf)
    if set(fit.values()) != {ans}:
        return None
    near = _fit(lib, ex[:2], qf)
    cands = [v for v in near.values() if v != ans and v > 0]
    rng.shuffle(cands)
    wrong = distinct_wrong(ans, cands, rng, lo=1)
    lines = '\n'.join(f"outer {list(x)} → centre {v}" for x, v in ex)
    q = (f"Each figure has four outer numbers in the order (a, b, c, d) and one centre number. Find the missing centre number:\n\n"
         f"```text\n{lines}\nouter {list(qf)} → centre ?\n```\n")
    why = (f"The rule that fits all three figures is **centre = {disp(name)}**. "
           + '; '.join(f"{list(x)} → {v}" for x, v in ex) + f". For {list(qf)} it gives **{ans}**.")
    qd = Q(q, [ans] + wrong, why, lambda: sole(fit), tag='Figure rule')
    qd['rule'] = name
    return qd


# ---------------------------------------------------------------- row rules on 3 or 4 columns
ROW3 = {   # first = g(second, third): "find the first number"
    'first = second × third': lambda b, c: b * c,
    'first = second × third + 2': lambda b, c: b * c + 2,
    'first = second² − third': lambda b, c: b * b - c,
    'first = second² + third': lambda b, c: b * b + c,
    'first = second + third²': lambda b, c: b + c * c,
    'first = (second + third) × 2': lambda b, c: (b + c) * 2,
    'first = (second + third) × third': lambda b, c: (b + c) * c,
    'first = second × (third + 1)': lambda b, c: b * (c + 1),
}


def gen_row3(rng, names=None):
    name = rng.choice(list(names) if names else list(ROW3))
    g = ROW3[name]
    rows = [(rng.randint(2, 9), rng.randint(2, 9)) for _ in range(4)]
    if len(set(rows)) < 4:
        return None
    vals = [g(*r) for r in rows]
    if len(set(vals)) < 4 or any(v > 150 for v in vals):
        return None
    ex, qr = list(zip(rows[:3], vals[:3])), rows[3]
    ans = vals[3]
    fit = {n: h(*qr) for n, h in ROW3.items() if all(h(*r) == v for r, v in ex)}
    if set(fit.values()) != {ans}:
        return None
    near = {n: h(*qr) for n, h in ROW3.items() if all(h(*r) == v for r, v in ex[:2])}
    cands = [v for v in near.values() if v != ans and v > 0]
    wrong = distinct_wrong(ans, cands, rng, lo=1)
    lines = '\n'.join(f"{v:>4}  {b}  {c}" for (b, c), v in ex) + f"\n   ?  {qr[0]}  {qr[1]}"
    q = f"Find the missing number in the last row, using the rule the first three rows follow:\n\n```text\n{lines}\n```\n"
    why = f"The rule is **{name}**: " + '; '.join(f"{v} from {b} and {c}" for (b, c), v in ex) + f". Last row: **{ans}**."
    qd = Q(q, [ans] + wrong, why, lambda: sole(fit), tag='Three-column rows')
    qd['rule'] = name
    return qd


ROW4 = {   # (a, b, c) -> d   rows of four numbers
    'd = b × c + a': lambda a, b, c: b * c + a,
    'd = a + b + c': lambda a, b, c: a + b + c,
    'd = a × b − c': lambda a, b, c: a * b - c,
    'd = a × b + c': lambda a, b, c: a * b + c,
    'd = a × c − b': lambda a, b, c: a * c - b,
    'd = (a + b) × c': lambda a, b, c: (a + b) * c,
    'd = a × b × c': lambda a, b, c: a * b * c,
    'd = a² + b × c': lambda a, b, c: a * a + b * c,
    'd = b² − a × c': lambda a, b, c: b * b - a * c,
}


def gen_row4(rng, names=None):
    name = rng.choice(list(names) if names else list(ROW4))
    g = ROW4[name]
    rows = [tuple(rng.randint(2, 9) for _ in range(3)) for _ in range(4)]
    if len(set(rows)) < 4:
        return None
    vals = [g(*r) for r in rows]
    if len(set(vals)) < 4 or any(v <= 0 or v > 250 for v in vals):
        return None
    ex, qr = list(zip(rows[:3], vals[:3])), rows[3]
    ans = vals[3]
    fit = {n: h(*qr) for n, h in ROW4.items() if all(h(*r) == v for r, v in ex)}
    if set(fit.values()) != {ans}:
        return None
    near = {n: h(*qr) for n, h in ROW4.items() if all(h(*r) == v for r, v in ex[:2])}
    cands = [v for v in near.values() if v != ans and v > 0]
    wrong = distinct_wrong(ans, cands, rng, lo=1)
    lines = '\n'.join(f"{a}  {b}  {c}  {v:>4}" for (a, b, c), v in ex) + f"\n{qr[0]}  {qr[1]}  {qr[2]}     ?"
    q = f"Find the missing number:\n\n```text\n{lines}\n```\n"
    why = f"For a row (a, b, c, d) the rule is **{name}**: " + '; '.join(f"{a},{b},{c} → {v}" for (a, b, c), v in ex) + f". The last row gives **{ans}**."
    qd = Q(q, [ans] + wrong, why, lambda: sole(fit), tag='Four-column rows')
    qd['rule'] = name
    return qd


# ---------------------------------------------------------------- (n, n, f(n))  tables, e.g. 4 4 10 / 5 5 15
SEQ = {
    'n(n+1)/2': lambda n: n * (n + 1) // 2,
    'n² + n': lambda n: n * n + n,
    'n² − 1': lambda n: n * n - 1,
    'n² + 1': lambda n: n * n + 1,
    'n³': lambda n: n ** 3,
    '2n + 2': lambda n: 2 * n + 2,
    'n(n−1)/2': lambda n: n * (n - 1) // 2,
    'n² + 2n': lambda n: n * n + 2 * n,
}


def gen_seqtable(rng, names=None):
    name = rng.choice(list(names) if names else list(SEQ))
    f = SEQ[name]
    ns = sorted(rng.sample(range(3, 13), 4))
    vals = [f(n) for n in ns]
    if len(set(vals)) < 4:
        return None
    ex, qn = list(zip(ns[:3], vals[:3])), ns[3]
    ans = vals[3]
    fit = {n: h(qn) for n, h in SEQ.items() if all(h(x) == v for x, v in ex)}
    if set(fit.values()) != {ans}:
        return None
    near = {n: h(qn) for n, h in SEQ.items() if all(h(x) == v for x, v in ex[:2])}
    cands = [v for v in near.values() if v != ans]
    wrong = distinct_wrong(ans, cands, rng, lo=1)
    lines = '\n'.join(f"{n}  {n}  {v}" for n, v in ex) + f"\n{qn}  {qn}  ?"
    q = f"Find the missing number:\n\n```text\n{lines}\n```\n"
    why = f"Only the repeated number matters: the third number is **{name}**. " + '; '.join(f"n={n} → {v}" for n, v in ex) + f". For n = {qn}: **{ans}**."
    qd = Q(q, [ans] + wrong, why, lambda: sole(fit), tag='Repeated-number table')
    qd['rule'] = name
    return qd


# ---------------------------------------------------------------- grids with a constant row or column sum
def gen_sumgrid(rng, shapes=None):
    rows, cols = rng.choice(list(shapes) if shapes else [(3, 3), (3, 4), (4, 4)])
    by_row = rng.random() < 0.5
    S = rng.randint(10, 24) if by_row else rng.randint(10, 24)
    if by_row:
        grid = [[rng.randint(1, 9) for _ in range(cols - 1)] for _ in range(rows)]
        for r in grid: r.append(S - sum(r))
    else:
        grid = [[0] * cols for _ in range(rows)]
        for c in range(cols):
            col = [rng.randint(1, 9) for _ in range(rows - 1)]
            col.append(S - sum(col))
            for r in range(rows): grid[r][c] = col[r]
    if any(x < 1 or x > 15 for row in grid for x in row):
        return None
    r0, c0 = rows - 1, cols - 1
    ans = grid[r0][c0]
    if by_row:
        known = rows - 1
    shown = [[str(x) for x in row] for row in grid]
    shown[r0][c0] = '?'
    txt = '\n'.join('  '.join(f'{x:>2}' for x in row) for row in shown)
    wrong = distinct_wrong(ans, [S - ans, sum(grid[r0][:-1]) , ans + 2], rng, lo=0)
    axis = 'row' if by_row else 'column'

    def check():
        if by_row:
            return S - sum(grid[r0][:-1])
        return S - sum(grid[r][c0] for r in range(rows - 1))
    q = f"Every {axis} of this grid adds up to the same number. Find the missing number:\n\n```text\n{txt}\n```\n"
    if by_row:
        why = f"The complete rows add up to {S} (e.g. {' + '.join(map(str, grid[0]))} = {S}). The last row has {' + '.join(map(str, grid[r0][:-1]))} = {sum(grid[r0][:-1])}, so the missing number is {S} − {sum(grid[r0][:-1])} = **{ans}**."
    else:
        col_known = [grid[r][c0] for r in range(rows - 1)]
        why = f"Each column adds up to {S}. The last column has {' + '.join(map(str, col_known))} = {sum(col_known)}, so the missing number is {S} − {sum(col_known)} = **{ans}**."
    return Q(q, [ans] + wrong, why, check, tag='Sum grid')


# ---------------------------------------------------------------- Kakuro-style: distinct digits, row and column sums
def _solve_kakuro(rowsums, colsums, given, n=3):
    """All fillings of an n x n grid with digits 1-9, distinct within every row and column."""
    cells = [(r, c) for r in range(n) for c in range(n) if (r, c) not in given]
    sols = []
    grid = [[given.get((r, c), 0) for c in range(n)] for r in range(n)]

    def ok(r, c):
        row = [x for x in grid[r] if x]
        col = [grid[i][c] for i in range(n) if grid[i][c]]
        if len(set(row)) != len(row) or len(set(col)) != len(col):
            return False
        if sum(row) > rowsums[r] or sum(col) > colsums[c]:
            return False
        if len(row) == n and sum(row) != rowsums[r]:
            return False
        if len(col) == n and sum(col) != colsums[c]:
            return False
        return True

    def rec(i):
        if i == len(cells):
            if all(sum(grid[r]) == rowsums[r] for r in range(n)) and all(sum(grid[r][c] for r in range(n)) == colsums[c] for c in range(n)):
                sols.append([row[:] for row in grid])
            return
        r, c = cells[i]
        for v in range(1, 10):
            grid[r][c] = v
            if ok(r, c):
                rec(i + 1)
        grid[r][c] = 0
    rec(0)
    return sols


def gen_kakuro(rng, givens=(3, 4)):
    n = 3
    sol = [rng.sample(range(1, 10), n) for _ in range(n)]
    if any(len({sol[r][c] for r in range(n)}) < n for c in range(n)):
        return None
    rowsums = [sum(r) for r in sol]
    colsums = [sum(sol[r][c] for r in range(n)) for c in range(n)]
    cells = [(r, c) for r in range(n) for c in range(n)]
    rng.shuffle(cells)
    k = rng.choice(list(givens))
    given = {cell: sol[cell[0]][cell[1]] for cell in cells[:k]}
    sols = _solve_kakuro(rowsums, colsums, given, n)
    if len(sols) != 1:
        return None
    blank = cells[k]
    ans = sol[blank[0]][blank[1]]
    shown = [[str(sol[r][c]) if (r, c) in given else '.' for c in range(n)] for r in range(n)]
    shown[blank[0]][blank[1]] = '?'
    hdr = '      ' + '  '.join(f'{s:>2}' for s in colsums)
    body = '\n'.join(f'{rowsums[r]:>3} | ' + '  '.join(f'{x:>2}' for x in shown[r]) for r in range(n))
    wrong = distinct_wrong(ans, [], rng, lo=1, hi=9)
    q = (f"Fill the grid with digits 1–9 so that **no digit repeats in any row or column**, each row adds up to the number on its left and each column to the number above it. "
         f"A dot is another empty cell. What number replaces ‘?’ ?\n\n```text\n{hdr}\n    +{'-' * (4 * n)}\n{body}\n```\n")
    why = (f"Work from the row or column with the fewest unknowns. The only grid that satisfies every sum with no repeats has row {blank[0] + 1} = "
           f"{sol[blank[0]]}, so ‘?’ = **{ans}**. (Checked by trying every filling: exactly one exists.)")
    return Q(q, [ans] + wrong, why, lambda: _solve_kakuro(rowsums, colsums, given, n)[0][blank[0]][blank[1]], tag='Distinct-digit sum grid')


# ---------------------------------------------------------------- digit-based grids: pairs of 2-digit numbers
def gen_digitpair(rng):
    return gen_pair(rng, digit=True)


FAMILIES = {
    'pair': gen_pair, 'digitpair': gen_digitpair, 'figure': gen_figure, 'row3': gen_row3,
    'row4': gen_row4, 'seqtable': gen_seqtable, 'sumgrid': gen_sumgrid, 'kakuro': gen_kakuro,
}


# ---------------------------------------------------------------- official-sample types (Infosys sample paper, 2020)
def gen_gridsums(rng):
    """Two 3x3 grids. Row sums of grid 1 rise by a constant d and keep rising into grid 2 (official type)."""
    d = rng.choice([2, 3, 4, 5])
    s0 = rng.randint(10, 20)
    sums1 = [s0, s0 + d, s0 + 2 * d]
    sums2 = [s0 + 3 * d, s0 + 4 * d, s0 + 5 * d]

    def row(total):
        a, b = rng.randint(1, 9), rng.randint(1, 9)
        c = total - a - b
        return [a, b, c] if 1 <= c <= 15 else None
    g1 = [row(t) for t in sums1]
    g2 = [row(t) for t in sums2]
    if None in g1 or None in g2: return None
    r, c = 0, 2
    ans = g2[r][c]
    shown2 = [[str(x) for x in rw] for rw in g2]; shown2[r][c] = '?'
    t1 = '\n'.join('  '.join(f'{x:>2}' for x in rw) for rw in g1)
    t2 = '\n'.join('  '.join(f'{x:>2}' for x in rw) for rw in shown2)
    wrong = distinct_wrong(ans, [sums2[0] - g2[0][0], sums1[0] - g2[0][0] - g2[0][1], ans + d, ans - d], rng, lo=1)
    q = (f"Two 3x3 grids relate in the same way. Find the missing number in the second grid.\n\n```text\nGrid 1          Grid 2\n"
         + '\n'.join(f"{a}      {b}" for a, b in zip(t1.split('\n'), t2.split('\n'))) + "\n```\n")
    why = (f"Add each row of grid 1: {', '.join(map(str, sums1))}. The totals rise by {d} each row, and the series carries on into grid 2: {', '.join(map(str, sums2))}. "
           f"The first row of grid 2 must total {sums2[0]}, so ? = {sums2[0]} − {g2[0][0]} − {g2[0][1]} = **{ans}**.")
    return Q(q, [ans] + wrong, why, lambda: (s0 + 3 * d) - g2[0][0] - g2[0][1], tag='Row sums as a series')


def gen_cubebox(rng, ks=(2, 3), top=9):
    """Circles: top (a, a^k), bottom (b, b^k); the box holds a^k + b^k + (a + b) (official type)."""
    k = rng.choice(list(ks))
    pairs = []
    while len(pairs) < 3:
        a, b = rng.randint(2, top), rng.randint(2, top)
        if a != b and (a, b) not in pairs: pairs.append((a, b))
    box = lambda a, b: a ** k + b ** k + a + b
    (a1, b1), (a2, b2), (a3, b3) = pairs
    ans = box(a3, b3)
    wrong = distinct_wrong(ans, [a3 ** k + b3 ** k, box(a3, b3) - (a3 + b3) + a3 * b3, ans + 2, a3 ** k + b3 ** k + abs(a3 - b3)], rng, lo=1)
    sup = {2: 'square', 3: 'cube'}[k]
    q = (f"Each set shows four circles and a box. The right-hand circle of each pair holds the {sup} of the left-hand one. "
         f"Find the value in the last box.\n\n```text\nset 1:  top {a1}, {a1 ** k}   bottom {b1}, {b1 ** k}   box {box(a1, b1)}\n"
         f"set 2:  top {a2}, {a2 ** k}   bottom {b2}, {b2 ** k}   box {box(a2, b2)}\nset 3:  top {a3}, {a3 ** k}   bottom {b3}, {b3 ** k}   box ?\n```\n")
    why = (f"Box = {sup} of the first + {sup} of the second + the two small numbers added: {a1 ** k} + {b1 ** k} + {a1 + b1} = {box(a1, b1)}; "
           f"{a2 ** k} + {b2 ** k} + {a2 + b2} = {box(a2, b2)}. Set 3: {a3 ** k} + {b3 ** k} + {a3 + b3} = **{ans}**.")
    qd = Q(q, [ans] + wrong, why, lambda: a3 ** k + b3 ** k + a3 + b3 if box(a1, b1) == a1 ** k + b1 ** k + a1 + b1 else None, tag='Powers in a box')
    qd['rule'] = f'a^{k} + b^{k} + a + b'
    return qd


ZZ_RULES = {
    'digit-sum(left) + digit-sum(right)': lambda a, b: ds(a) + ds(b),
    'left + right': lambda a, b: a + b,
    '|left - right|': lambda a, b: abs(a - b),
    'digit-sum(left + right)': lambda a, b: ds(a + b),
    'left + digit-sum(right)': lambda a, b: a + ds(b),
}


def gen_zigzag(rng, names=None):
    """Row 1 of five numbers; each number in row 2 is a function of the two numbers above it; row 3 likewise (official type)."""
    name = rng.choice(list(names) if names else list(ZZ_RULES)); f = ZZ_RULES[name]
    top = rng.choice([[16, 25, 36, 49, 64], [11, 22, 33, 44, 55], [12, 21, 34, 43, 56]]) if rng.random() < 0.5 else sorted(rng.sample(range(11, 90), 5))
    mid = [f(top[i], top[i + 1]) for i in range(4)]
    low = [f(mid[i], mid[i + 1]) for i in range(3)]
    if min(mid + low) < 1: return None
    hide = rng.choice([0, 1, 2]); ans = low[hide]
    lows = [str(v) for v in low]; lows[hide] = 'X'
    fit = {n: g for n, g in ZZ_RULES.items() if all(g(top[i], top[i + 1]) == mid[i] for i in range(4)) and
           all(g(mid[i], mid[i + 1]) == low[i] for i in range(3) if i != hide)}
    if len({g(mid[hide], mid[hide + 1]) for g in fit.values()}) != 1: return None
    wrong = distinct_wrong(ans, [mid[hide] + mid[hide + 1], abs(mid[hide] - mid[hide + 1]), ds(mid[hide] + mid[hide + 1])], rng, lo=1)
    q = (f"Each number in a lower row comes from the two numbers above it, by one rule used throughout. Find X.\n\n```text\n"
         f"{'   '.join(f'{v:>3}' for v in top)}\n   {'   '.join(f'{v:>3}' for v in mid)}\n      {'   '.join(f'{v:>3}' for v in lows)}\n```\n")
    why = (f"The rule is **{name}**. Row 2: " + '; '.join(f"({top[i]}, {top[i + 1]}) → {mid[i]}" for i in range(2)) + f"… Row 3: (" +
           f"{mid[hide]}, {mid[hide + 1]}) → **{ans}**.")
    qd = Q(q, [ans] + wrong, why, lambda: next(iter({g(mid[hide], mid[hide + 1]) for g in fit.values()})), tag='Zig-zag rows')
    qd['rule'] = name
    return qd


FAMILIES.update({'gridsums': gen_gridsums, 'cubebox': gen_cubebox, 'zigzag': gen_zigzag})


def gen_mixed(rng, families=None):
    fams = families or ['pair', 'pair', 'digitpair', 'figure', 'row3', 'row4', 'seqtable', 'sumgrid', 'kakuro']
    return FAMILIES[rng.choice(fams)](rng)
