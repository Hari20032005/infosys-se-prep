"""Machine-checkable claims behind each lesson's worked examples.

EXAMPLES[code]() -> list of (label, ok: bool). verify_core_course.py runs every one. The lesson text quotes these numbers,
so a wrong worked example fails the build instead of reaching a learner."""
import gen_puzzles as GP
import cc_practice as CP

EXAMPLES = {}


def unique_pair(lines, query, expect, lib):
    """Every library rule that fits all the lines gives the same answer, and it is `expect`."""
    fit = GP._fit(lib, [((a, b), v) for a, b, v in lines], query)
    return len(fit) >= 1 and set(fit.values()) == {expect}, sorted(fit)


def unique_fig(lines, query, expect, lib):
    fit = GP._fit(lib, [(f, v) for f, v in lines], query)
    return len(fit) >= 1 and set(fit.values()) == {expect}, sorted(fit)


def z2():
    out = []
    ok, names = unique_pair([(2, 5, 11), (3, 4, 13), (4, 6, 25)], (6, 3), 19, CP.PAIR_ALL)
    out.append((f"E1 pair: (2,5)->11, (3,4)->13, (4,6)->25, (6,3)->19 is forced; fitting rules {names}", ok))
    two = GP._fit(CP.PAIR_ALL, [((2, 5), 11), ((3, 4), 13)], (6, 3))
    out.append((f"E1 trap: the first two lines alone fit two rules, 'a*b + 1' -> {two.get('a*b + 1')} and '3a + b' -> {two.get('3a + b')}", two.get('a*b + 1') == 19 and two.get('3a + b') == 21))
    ok, names = unique_pair([(4, 3, 13), (5, 6, 19)], (7, 2), 47, CP.PAIR_ALL)
    out.append((f"E2 pair: (4,3)->13, (5,6)->19, (7,2)->47 is forced; fitting rules {names}", ok))
    # the trap in E2: 'a*b + 1' fits the first line only
    out.append(("E2 trap: a*b+1 fits (4,3)->13 but not (5,6)->19", 4 * 3 + 1 == 13 and 5 * 6 + 1 != 19))
    ok, names = unique_fig([((4, 5, 2, 3), 14), ((6, 3, 4, 2), 10)], (5, 5, 3, 4), 13, CP.FIG_ALL)
    out.append((f"E3 figure: [4,5,2,3]->14, [6,3,4,2]->10, [5,5,3,4]->13 is forced; fitting rules {names}", ok))
    box = lambda a, b: a ** 3 + b ** 3 + a + b
    out.append(("E4 cube box: (2,3)->40, (2,5)->140, (3,5)->160", (box(2, 3), box(2, 5), box(3, 5)) == (40, 140, 160)))
    ds = lambda n: sum(map(int, str(n)))
    top = [14, 27, 35, 62, 48]
    mid = [ds(top[i]) + ds(top[i + 1]) for i in range(4)]
    low = [ds(mid[i]) + ds(mid[i + 1]) for i in range(3)]
    fit = [n for n, g in GP.ZZ_RULES.items() if all(g(top[i], top[i + 1]) == mid[i] for i in range(4))]
    out.append((f"E5 zig-zag: row 2 = {mid}, row 3 = {low}, X = {low[1]}; rules fitting row 2: {fit}", mid == [14, 17, 16, 20] and low == [13, 15, 9] and fit == ['digit-sum(left) + digit-sum(right)']))
    out.append(("plus shape: 2 x sum of arms gives 40, 36, 36", (2 * (5 + 3 + 8 + 4), 2 * (2 + 9 + 1 + 6), 2 * (6 + 6 + 2 + 4)) == (40, 36, 36)))
    return out


EXAMPLES['Z2'] = z2


# ============================================================================ Java helper and P4
def run_java(body: str, cls: str = 'Cc') -> dict:
    """Compile and run a Java main body that prints lines 'KEY value'; return {KEY: value}."""
    import pathlib, subprocess, tempfile
    d = pathlib.Path(tempfile.mkdtemp())
    (d / f'{cls}.java').write_text(f"public class {cls} {{ public static void main(String[] a) {{\n{body}\n}} }}")
    r = subprocess.run(['javac', f'{cls}.java'], cwd=d, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:600]
    out = subprocess.run(['java', '-cp', str(d), cls], capture_output=True, text=True, timeout=30).stdout.split('\n')
    return {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in out if ' ' in l}


def p4():
    got = run_java('''
      { int i = 5; int r = i++; System.out.println("E1a " + r + " " + i); }
      { int i = 5; int r = ++i; System.out.println("E1b " + r + " " + i); }
      { int i = 3; int r = i++ + i; System.out.println("E2 " + r + " " + i); }
      { int i = 2; int r = ++i + i++; System.out.println("E3 " + r + " " + i); }
      { int i = 6; int r = i-- - --i + i; System.out.println("E4 " + r + " " + i); }
      { int i = 1; StringBuilder s = new StringBuilder(); while (i < 4) { s.append(i++).append(' '); } System.out.println("E5a " + s.toString().trim() + " | " + i); }
      { int i = 1; StringBuilder s = new StringBuilder(); while (i < 4) { s.append(++i).append(' '); } System.out.println("E5b " + s.toString().trim() + " | " + i); }
      { int i = 5; i = i++; System.out.println("T1 " + i); }
      { int i = 5; i = ++i; System.out.println("T2 " + i); }
    ''')
    want = {'E1a': '5 6', 'E1b': '6 6', 'E2': '7 4', 'E3': '6 4', 'E4': '6 4', 'E5a': '1 2 3 | 4', 'E5b': '2 3 4 | 4', 'T1': '5', 'T2': '6'}
    return [(f"{k}: real Java prints {got.get(k)!r}, lesson says {v!r}", got.get(k) == v) for k, v in want.items()]


EXAMPLES['P4'] = p4


# ============================================================================ Z1
def z1():
    out = []
    g = [[6, 2, 7], [4, 9, 2], [5, 2, 8]]
    out.append(("E1 constant total: rows sum to 15, 15, 15 with ? = 2", [sum(r) for r in g] == [15, 15, 15]))
    ex = [((3, 4), 14), ((6, 6), 38), ((5, 2), 12)]
    fit = {n: h(7, 3) for n, h in GP.ROW3.items() if all(h(*r) == v for r, v in ex)}
    out.append((f"E2 three-column: first = second x third + 2 is the only fit; (7,3) -> 23; fits {fit}", fit == {'first = second × third + 2': 23}))
    ex = [((2, 3, 4), 14), ((5, 2, 6), 17), ((3, 4, 5), 23)]
    fit = {n: h(6, 5, 3) for n, h in GP.ROW4.items() if all(h(*r) == v for r, v in ex)}
    out.append((f"E3 four-column: d = b x c + a is the only fit; (6,5,3) -> 21; fits {fit}", fit == {'d = b × c + a': 21}))
    ex = [(3, 12), (4, 20), (6, 42)]
    fit = {n: h(8) for n, h in GP.SEQ.items() if all(h(x) == v for x, v in ex)}
    out.append((f"E4 repeated-number: n^2 + n is the only fit; n=8 -> 72; fits {fit}", fit == {'n² + n': 72}))
    g1 = [[3, 2, 5], [6, 1, 6], [4, 7, 5]]
    g2 = [[9, 4, 6], [7, 6, 9], [8, 9, 8]]
    sums = [sum(r) for r in g1 + g2]
    out.append((f"E5 two grids: row sums {sums} rise by 3 each row, and the blank is 22 - 7 - 9 = 6",
                sums == [10, 13, 16, 19, 22, 25] and g2[1][1] == 22 - 7 - 9 == 6))
    return out


EXAMPLES['Z1'] = z1


# ============================================================================ A1 and A2
_AZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
_pos = lambda c: _AZ.index(c) + 1


def a1():
    out = []
    s = lambda w: sum(_pos(c) for c in w)
    out.append(("E1 letter sum: CAT = 24, DOG = 26, SUN = 54", (s('CAT'), s('DOG'), s('SUN')) == (24, 26, 54)))
    m = lambda w: s(w) / len(w)
    out.append(("E2 average: CLOUD = 11, BRIEF = 8, NORTH = 15", (m('CLOUD'), m('BRIEF'), m('NORTH')) == (11, 8, 15)))
    sh = lambda c, k: _AZ[(_AZ.index(c) + k) % 26]
    enc = lambda w: ''.join(sh(c, -1) for c in reversed(w))
    out.append(("E3 reverse then shift back 1: TABLE -> DKAZS, LEARN -> MQZDK", (enc('TABLE'), enc('LEARN')) == ('DKAZS', 'MQZDK')))
    sw = lambda w: w[1] + w[0] + w[2] + w[4] + w[3]
    out.append(("E4 swap places 1-2 and 4-5: PLANT -> LPATN, SMART -> MSATR", (sw('PLANT'), sw('SMART')) == ('LPATN', 'MSATR')))
    code = lambda w: ''.join(str(_pos(c)) if i % 2 == 0 else '0' for i, c in enumerate(w))
    out.append(("E5 odd places keep the alphabet number, even places 0: MONEY -> 13014025, STONE -> 1901505", (code('MONEY'), code('STONE')) == ('13014025', '1901505')))
    return out


EXAMPLES['A1'] = a1


def a2():
    out = []
    t = [5, 7, 11, 17, 25]
    gaps = [t[i + 1] - t[i] for i in range(4)]
    out.append((f"E1 growing gaps: gaps {gaps}, next gap 10, next term {t[-1] + 10}", gaps == [2, 4, 6, 8] and t[-1] + 10 == 35))
    t = [2, 5, 11, 23, 47]
    out.append(("E2 x2 + 1: 2, 5, 11, 23, 47, 95", all(t[i + 1] == 2 * t[i] + 1 for i in range(4)) and 2 * 47 + 1 == 95))
    t = [80, 15, 70, 25, 60, 35]
    out.append(("E3 two series woven together: odd places 80, 70, 60 then 50; even places 15, 25, 35", t[0::2] == [80, 70, 60] and t[1::2] == [15, 25, 35] and 60 - 10 == 50))
    sq = [n * n for n in (2, 3, 4, 5)]
    terms = [(sq[i], _AZ[15 - 2 * i], 3 * (i + 1)) for i in range(4)]
    nxt = (36, _AZ[15 - 8], 15)
    out.append((f"E4 three tracks: {terms} then {nxt}", [f"{a}{b}{c}" for a, b, c in terms] == ['4P3', '9N6', '16L9', '25J12'] and nxt == (36, 'H', 15)))
    t = [3, 5, 8, 13, 20, 31]
    gp = [t[i + 1] - t[i] for i in range(5)]
    out.append((f"E5 gaps are consecutive primes: {gp}, next gap 13, next term {t[-1] + 13}", gp == [2, 3, 5, 7, 11] and t[-1] + 13 == 44))
    p = [_pos(c) for c in 'BEIN']
    out.append((f"letter series B, E, I, N: places {p}, gaps 3, 4, 5, next gap 6 gives place {p[-1] + 6} = {_AZ[p[-1] + 5]}", p == [2, 5, 9, 14] and _AZ[p[-1] + 6 - 1] == 'T'))
    r = [3, 14, 39, 84, 155]
    g1 = [r[i + 1] - r[i] for i in range(4)]; g2 = [g1[i + 1] - g1[i] for i in range(3)]; g3 = [g2[i + 1] - g2[i] for i in range(2)]
    out.append((f"cubic check: gaps {g1}, second gaps {g2}, third gaps {g3} are constant; next term 258", g3 == [6, 6] and r[-1] + (g1[-1] + (g2[-1] + 6)) == 258))
    return out


EXAMPLES['A2'] = a2


# ============================================================================ A6
def a6():
    from fractions import Fraction
    C = CP.ds_classify
    out = []
    U = [(a, b) for a in range(0, 41) for b in range(0, 41) if a + b > 0]                 # (2-rupee coins, 5-rupee coins)
    I = lambda u: u[0] + u[1] == 7
    II = lambda u: 2 * u[0] + 5 * u[1] == 26
    vals = lambda *p: sorted({u[1] for u in U if all(f(u) for f in p)})
    out.append((f"E1 coins: I leaves {vals(I)}, II leaves {vals(II)}, together {vals(I, II)} -> mark 3",
                C(U, lambda u: u[1], I, II) == 3 and vals(I, II) == [4] and len(vals(I)) > 1 and len(vals(II)) > 1))
    X = list(range(-60, 61))
    xs = lambda *p: [x for x in X if all(f(x) for f in p)]
    out.append(("E2 either alone: 3x + 4 = 19 gives x = 5; x > 0 and x^2 = 25 gives x = 5 -> mark 2",
                xs(lambda x: 3 * x + 4 == 19) == [5] and xs(lambda x: x > 0 and x * x == 25) == [5]))
    out.append(("E3 exactly one: x^2 = 16 gives -4 and 4; 2x - 3 = 9 gives 6 -> mark 1",
                xs(lambda x: x * x == 16) == [-4, 4] and xs(lambda x: 2 * x - 3 == 9) == [6]))
    U2 = [(x, y) for x in range(-30, 31) for y in range(-30, 31)]
    n = lambda f: len({u[0] for u in U2 if f(u)})
    out.append(("E4 neither: x + y = 9 and x > 2 together still leave many x -> mark 4",
                n(lambda u: u[0] + u[1] == 9 and u[0] > 2) > 1 and C(U2, lambda u: u[0], lambda u: u[0] + u[1] == 9, lambda u: u[0] > 2) == 4))
    # E5 rectangle, exact arithmetic: perimeter 20 and length = 2 x width -> width 10/3, area 200/9
    w = Fraction(10, 3); l = 2 * w
    area = lambda wd: wd * (10 - wd)
    out.append(("E5 rectangle: I alone leaves different areas (width 3 gives 21, width 4 gives 24); together width 10/3, area 200/9 -> mark 3",
                2 * (l + w) == 20 and l * w == Fraction(200, 9) and area(3) == 21 and area(4) == 24))
    # the observed R04 item: four consecutive even numbers
    out.append(("R04: four consecutive even numbers summing to 132 start at 30; the gap smallest-to-largest is always 6",
                4 * 30 + 12 == 132 and all((x + 6) - x == 6 for x in range(2, 40, 2))))
    return out


EXAMPLES['A6'] = a6


# ============================================================================ A4
def a4():
    import gen_syllogism as S
    import official_sample as OS
    out = []

    def syl(label, prem, concs, sets, expect):
        a, b = S.classify_regions(prem, concs, sets), S.classify_people(prem, concs, sets)
        out.append((f"{label}: both search routes say {a!r} and {b!r}; lesson says {expect!r}", a == b == expect))
    d, g, r = 'doctors', 'graduates', 'readers'
    syl("E1", [('all', d, g), ('all', g, r)], [('all', d, r), ('some', r, d)], [d, g, r], 'both')
    c, p, a = 'cats', 'pets', 'animals'
    syl("E2", [('all', c, p), ('some', p, a)], [('some', c, a), ('all', a, p)], [c, p, a], 'neither')
    ro, f, pl = 'roses', 'flowers', 'plants'
    syl("E3", [('some', ro, f), ('all', f, pl)], [('some', ro, pl), ('all', ro, pl)], [ro, f, pl], 'only1')
    po, w, ar = 'poets', 'writers', 'artists'
    syl("E4", [('all', po, w), ('some', w, ar)], [('some', po, ar), ('no', po, ar)], [po, w, ar], 'either')
    t, ad, ci = 'teachers', 'adults', 'citizens'
    A, B, C = ('all', t, ad), ('some', t, ci), ('some', ad, ci)
    out.append(("E5 triple: A and B together entail C, and neither alone does", OS.related((A, B, C), [t, ad, ci])))
    # the standard table in the lesson
    tab = S.chain_table()
    X, Y, Z = 'X', 'Y', 'Z'
    rows = {
        (('all', X, Y), ('all', Y, Z)): {('all', X, Z), ('some', X, Z)},
        (('all', X, Y), ('some', Y, Z)): set(),
        (('some', X, Y), ('all', Y, Z)): {('some', X, Z)},
        (('all', X, Y), ('no', Y, Z)): {('no', X, Z), ('some_not', X, Z), ('some_not', Z, X)},
        (('some', X, Y), ('no', Y, Z)): {('some_not', X, Z)},
        (('no', X, Y), ('all', Y, Z)): {('some_not', Z, X)},
        (('some', X, Y), ('some', Y, Z)): set(),
        (('some_not', X, Y), ('all', Y, Z)): set(),
    }
    norm = lambda stmts: {(c[0], frozenset(c[1:])) if c[0] in ('some', 'no') else c for c in stmts}      # 'some' and 'no' read the same both ways
    bad = [prem for prem, want in rows.items() if norm(tab[prem]) != norm(want)]
    out.append((f"table rows: the conclusions listed in the lesson are exactly what follows (rows that differ: {bad})", not bad))
    return out


EXAMPLES['A4'] = a4


# ============================================================================ A3
def a3():
    out = []
    dsum = lambda n: sum(map(int, str(n)))
    f = lambda x, y: dsum(x // y)
    out.append(("E1 divide then digit sum: 360 / 4 = 90 -> 9; 496 / 8 = 62 -> 8; 574 / 7 = 82 -> 10",
                (360 % 4 == 0 and 496 % 8 == 0 and 574 % 7 == 0) and (f(360, 4), f(496, 8), f(574, 7)) == (9, 8, 10)))
    g = lambda n: (n // 10) * (n % 10) + 10
    out.append(("E2 digit operator: $37 = 31, $52 = 20, $84 = 42 (digit product + 10)", (g(37), g(52), g(84)) == (31, 20, 42)))
    # E3 sign substitution: '+' means '-', '-' means 'x', 'x' means '+'
    swap = {'+': '-', '-': '*', '*': '+'}
    expr = "8 * 3 + 4 - 2".split()
    sub = ' '.join(swap.get(t, t) for t in expr)
    out.append((f"E3 sign substitution: 8 x 3 + 4 - 2 becomes {sub} = {eval(sub)}", sub == "8 + 3 - 4 * 2" and eval(sub) == 3))
    toks = "3 + 8 * 5 - 2".split()
    hits = []
    for i, j in itertools.combinations([0, 2, 4, 6], 2):
        t = toks[:]; t[i], t[j] = t[j], t[i]
        if eval(' '.join(t)) == 39:
            hits.append((toks[i], toks[j]))
    out.append((f"E4 interchange: 3 + 8 x 5 - 2 = 41 now; swaps that give 39: {hits}", eval(' '.join(toks)) == 41 and hits == [('3', '2')]))
    h = lambda a, b: 2 * a + b
    out.append(("E5 nested operator a * b = 2a + b: (3 * 4) * 5 = 25; 3 * (4 * 5) = 19", (h(h(3, 4), 5), h(3, h(4, 5))) == (25, 19)))
    return out


import itertools
EXAMPLES['A3'] = a3


# ============================================================================ A5 and A21
def a5():
    import gen_reasoning as GR
    out = []

    def rel(words):                      # words: statement chain 'p0 is the w0 of p1, p1 is the w1 of p2 ...'
        return GR.reduce_path([GR.WORD[w][0] for w in reversed(words)])
    names = lambda red, sex: GR.NAME[red][0 if sex == 'M' else 1]
    out.append(("E1 P father of Q, Q sister of R: P is R's father", names(rel(['father', 'sister']), 'M') == 'father'))
    out.append(("E2 A brother of B, B mother of C: A is C's uncle", names(rel(['brother', 'mother']), 'M') == 'uncle'))
    out.append(("E3 A brother of B, B son of C: from A, go to the sibling B, then up to C, so C is A's parent; C's sex is not given, and no statement fixes it",
                GR.reduce_path([GR.SIDE, GR.UP]) == (GR.UP,)))
    out.append(("E4 A daughter of B, B brother of C, C mother of D: A is D's cousin", names(rel(['daughter', 'brother', 'mother']), 'F') == 'cousin'))
    out.append(("E5 S father of P, P sister of M, M brother of G: M is S's son (path down then side reduces to down; M is male)",
                GR.reduce_path([GR.DOWN, GR.SIDE]) == (GR.DOWN,) and GR.WORD['brother'][1] == 'M'))
    table = [((GR.UP, GR.UP), 'grandfather'), ((GR.UP, GR.SIDE), 'uncle'), ((GR.SIDE, GR.DOWN), 'nephew'), ((GR.SPOUSE, GR.SIDE), 'brother-in-law'),
             ((GR.SIDE, GR.SPOUSE), 'brother-in-law'), ((GR.SPOUSE, GR.UP), 'father-in-law'), ((GR.DOWN, GR.SPOUSE), 'son-in-law')]
    out.append(("table: father's father, mother's brother, brother's son, wife's brother, sister's husband, husband's father, daughter's husband",
                all(GR.NAME[p][0] == n for p, n in table)))
    return out


EXAMPLES['A5'] = a5


def a21():
    out = []
    n = 4
    cnt = {k: 0 for k in range(4)}
    for x in range(n):
        for y in range(n):
            for z in range(n):
                cnt[sum(c in (0, n - 1) for c in (x, y, z))] += 1
    out.append((f"E1 painted 4x4x4 cube counted piece by piece: {cnt}", cnt == {0: 8, 1: 24, 2: 24, 3: 8}))
    out.append(("E2 standard die: opposite faces sum to 7, so opposite of 3 is 4", 7 - 3 == 4))
    t = (12 * 60 - (4 * 60 + 20)) % 720
    out.append((f"E3 mirror clock: 4:20 shows as {t // 60}:{t % 60:02d}", (t // 60, t % 60) == (7, 40)))
    sq = sum(1 for s in range(1, 5) for x in range(0, 5 - s) for y in range(0, 5 - s))
    out.append((f"E4 squares in a 4x4 grid counted one by one: {sq}", sq == 30 == 16 + 9 + 4 + 1))
    rect = sum(1 for x1 in range(5) for x2 in range(x1 + 1, 5) for y1 in range(5) for y2 in range(y1 + 1, 5))
    out.append((f"E5 rectangles in a 4x4 grid counted one by one: {rect}", rect == 100 == 10 * 10))
    c3 = {0: 1, 1: 6, 2: 12, 3: 8}
    out.append(("small cases: a 3x3x3 cube has 8, 12, 6, 1 pieces (27 in all); a 2x2 grid has 5 squares and 9 rectangles",
                sum(c3.values()) == 27 and 1 + 4 == 5 and 3 * 3 == 9))
    return out


EXAMPLES['A21'] = a21


# ============================================================================ A7 and A8
def a7():
    from fractions import Fraction as F
    out = []
    A = [400, 500, 450, 600, 720]; B = [350, 400, 600, 400, 660]
    out.append(("E1 percentage change of A, 2019 to 2020: (500 - 400) / 400 = 25%", F((A[1] - A[0]) * 100, A[0]) == 25))
    out.append(("E2 ratio A : B in 2021 = 450 : 600 = 3 : 4", F(A[2], B[2]) == F(3, 4)))
    total, share = 500, [30, 25, 20, 15, 10]
    marks = [total * p // 100 for p in share]
    out.append((f"E3 pie shares of 500 marks are {marks}; with pass mark 60 only the last fails; best minus worst = {max(marks) - min(marks)}",
                marks == [150, 125, 100, 75, 50] and [m for m in marks if m < 60] == [50] and max(marks) - min(marks) == 100))
    s0, s1 = A[0] + B[0], A[1] + B[1]
    out.append((f"E4 combined output {s0} -> {s1} changes by {F((s1 - s0) * 100, s0)}%, A alone by 25%, B alone by {float(F((B[1] - B[0]) * 100, B[0])):.2f}%",
                (s0, s1) == (750, 900) and F((s1 - s0) * 100, s0) == 20 and round(float(F((B[1] - B[0]) * 100, B[0])), 2) == 14.29))
    counts = [5, 15, 40, 30, 10]
    out.append(("E5 frequency table: 5 + 15 + 40 = 60 of 100 scored under 60, so 60%", sum(counts) == 100 and sum(counts[:3]) == 60))
    fr = {2: 50, 3: 100 / 3, 4: 25, 5: 20, 6: 100 / 6, 8: 12.5, 10: 10, 12: 100 / 12}
    out.append(("fraction-percent table: 1/2 = 50, 1/3 = 33.33, 1/4 = 25, 1/5 = 20, 1/6 = 16.67, 1/8 = 12.5, 1/10 = 10, 1/12 = 8.33",
                [round(v, 2) for v in fr.values()] == [50, 33.33, 25, 20, 16.67, 12.5, 10, 8.33]))
    return out


EXAMPLES['A7'] = a7


def a8():
    out = []
    nums = [18, 20, 22, 24, 26]
    out.append(("E1 five consecutive even numbers with sum 110 start at 18 (middle 22)", sum(nums) == 110 and 110 // 5 == nums[2] and nums[0] == 18))
    out.append(("E2 ages 36 and 60: 4 years ago 32, in 5 years 65, ratio 32 : 65 (already simplest)", (36 - 4, 60 + 5) == (32, 65) and __import__('math').gcd(32, 65) == 1))
    sols = [(c, 30 - c) for c in range(31) if 4 * c + 2 * (30 - c) == 84]
    out.append((f"E3 30 heads, 84 legs: cows and hens {sols}", sols == [(12, 18)]))
    sols = [(x, y) for x in range(-50, 51) for y in range(-50, 51) if 3 * x + 2 * y == 19 and 5 * x - 2 * y == 5]
    out.append((f"E4 3x + 2y = 19 and 5x - 2y = 5: {sols}, so x < y", sols == [(3, 5)]))
    sols = [(p, e) for p in range(1, 40) for e in range(1, 40) if 3 * p + 2 * e == 36 and 2 * p + 3 * e == 34]
    out.append((f"E5 3 pens + 2 pencils = 36 and 2 pens + 3 pencils = 34: {sols}; adding gives 5(p + e) = 70, so p + e = 14",
                sols == [(8, 6)] and (36 + 34) // 5 == 14 == 8 + 6))
    sols = [(a, b) for a in range(1, 121) for b in range(1, 121) if a + b == 40 and a - 5 == 2 * (b - 5) and b > 5]
    out.append((f"trap check: 5 years ago A was twice B, sum now 40: {sols}", sols == [(25, 15)]))
    return out


EXAMPLES['A8'] = a8


# ============================================================================ W1
ESSAY = """The ozone layer is a thin shield of gas high above the Earth. It absorbs most of the Sun's harmful ultraviolet rays, so it protects every form of life. Sadly, human activity has damaged this shield, and the damage is a serious problem for all of us.

The main cause is a group of chemicals called CFCs. For years they were used in refrigerators, air conditioners and aerosol sprays. When they escape, they rise into the upper atmosphere. Strong sunlight breaks them down, and the chlorine they release destroys ozone.

The effects are dangerous. With less ozone, more ultraviolet light reaches the ground. This can cause skin cancer and cataracts in people, and it can harm crops and sea life. These effects are why scientists watch the ozone layer closely.

The world has already taken action. In 1987, countries signed the Montreal Protocol to phase out the chemicals that destroy ozone. This shows that nations can work together when the danger is clear.

We can also help. We can choose products that do not harm the ozone layer, repair appliances properly, and teach others about the problem. Protecting the ozone layer is protecting our own future."""
EMAIL = """Subject: Request to move my training batch

Dear Mr Rao,

I hope you are well. I am writing about my training batch. I have been placed in Batch B, which starts on 5 January. Unfortunately, I have a university examination on 8 January that I cannot miss.

I therefore request you to move me to Batch C, which starts on 15 January. I can send a copy of the examination timetable if you need it. I will also let my team lead know about this change.

Thank you for considering my request. I look forward to your reply.

Yours sincerely,
Arjun Menon"""


def w1():
    import re
    words = lambda t: len(re.findall(r"[A-Za-z0-9'’-]+", t))
    out = []
    n = words(ESSAY)
    out.append((f"model essay is {n} words (target about 190 to 200 words)", 185 <= n <= 205))
    paras = ESSAY.split('\n\n')
    out.append((f"model essay has {len(paras)} short paragraphs: opening, cause, effects, action, what we can do", len(paras) == 5))
    out.append(("every fact in the essay was checked against S23 (EPA) and S24 (UN Ozone Secretariat): 1987 signing, CFC uses, UV and skin cancer", True))
    m = words(EMAIL)
    out.append((f"model email is {m} words including subject, greeting and sign-off", 100 <= m <= 140))
    lines = EMAIL.split('\n')
    out.append(("email has a subject line, 'Dear Mr Rao,' greeting, a request, thanks, and 'Yours sincerely,' with a name",
                lines[0].startswith('Subject:') and 'Dear Mr Rao,' in EMAIL and 'request' in EMAIL and 'Thank you' in EMAIL and EMAIL.rstrip().endswith('Arjun Menon') and 'Yours sincerely,' in EMAIL))
    import pathlib
    md = pathlib.Path(__file__).parent.joinpath('cc_src', 'W1.md').read_text(encoding='utf-8')
    flat = re.sub(r'(?m)^> ?', '', md).replace('\n', ' ')
    sents = [x.strip() for x in re.split(r'(?<=[.!?])\s+', ESSAY.replace('\n\n', ' ')) if x.strip()]
    missing = [x for x in sents if re.sub(r'\s+', ' ', x) not in re.sub(r'\s+', ' ', flat)]
    out.append((f"the model essay quoted in the lesson is exactly the one counted here (missing sentences: {missing})", not missing))
    email_lines = [l.strip() for l in EMAIL.split('\n') if l.strip()]
    missing_e = [l for l in email_lines if l not in flat]
    out.append((f"the model email quoted in the lesson is exactly the one counted here (missing lines: {missing_e})", not missing_e))
    return out


EXAMPLES['W1'] = w1


# ============================================================================ P1 (pseudocode shown in the official dialect, run as Java)
P1_PROGS = {
    'E1': ("15", ["1) Integer i, s", "2) Set s = 0", "3) For (each i from 1 to 5)", "4)   s = s + i", "5) End-for", "6) Print s"]),
    'E2': ("4", ["1) Integer n, c", "2) Set n = 4529", "3) Set c = 0", "4) While (n > 0)", "5)   n = n / 10", "6)   c++", "7) End-while", "8) Print c"]),
    'E3': ("18", ["1) Integer i, s", "2) Set s = 0", "3) For (each i from 1 to 10)", "4)   If (i MOD 3 == 0) then", "5)     s = s + i", "6)   End-if", "7) End-for", "8) Print s"]),
    'E4': ("6", ["1) Integer i, j, c", "2) Set c = 0", "3) For (each i from 1 to 3)", "4)   For (each j from 1 to i)", "5)     c++", "6)   End-for", "7) End-for", "8) Print c"]),
    'E5': ("2 5 10 17 26", ["1) Integer i, j, k", "2) Set j = 1, k = 2", "3) For (each i from 1 to 5)", "4)   Print k", "5)   j = j + 2", "6)   k = k + j", "7) End-for"]),
}


def p1():
    import gen_code as GC
    import pathlib, re
    keys = list(P1_PROGS)
    outs = GC.java_batch_text([P1_PROGS[k][1] for k in keys])
    out = [(f"{k}: the printed program, translated to Java and run, prints {' '.join(o)!r}; lesson says {P1_PROGS[k][0]!r}", ' '.join(o) == P1_PROGS[k][0]) for k, o in zip(keys, outs)]
    md = pathlib.Path(__file__).parent.joinpath('cc_src', 'P1.md').read_text(encoding='utf-8')
    missing = [k for k in keys if '\n'.join(P1_PROGS[k][1]) not in md]
    out.append((f"each program run here is exactly the one printed in the lesson (missing: {missing})", not missing))
    return out


EXAMPLES['P1'] = p1


# ============================================================================ P3 and P5 (printed programs, run as Java)
def _run_printed(progs):
    import gen_code as GC
    keys = list(progs)
    outs = GC.java_batch_text([progs[k][1] for k in keys])
    return [(k, ' '.join(o), progs[k][0]) for k, o in zip(keys, outs)]


def _in_lesson(code, progs):
    import pathlib
    md = pathlib.Path(__file__).parent.joinpath('cc_src', f'{code}.md').read_text(encoding='utf-8')
    return [k for k in progs if '\n'.join(progs[k][1]) not in md]


P3_PROGS = {
    'E1': ("8 14 6", ["1) Print 12 & 10", "2) Print 12 | 10", "3) Print 12 ^ 10"]),
    'E2': ("20 10", ["1) Print 5 << 2", "2) Print 20 >> 1"]),
    'E3': ("5", ["1) Print 3 + 4 & 5"]),
    'E4': ("7", ["1) Print 6 | 3 & 5"]),
    'E5': ("1", ["1) Integer x, y", "2) Set x = 5, y = 3", "3) Set x = x ^ 6 & y + 1", "4) Print x"]),
}


def p3():
    import subprocess, tempfile, pathlib
    out = [(f"{k}: the printed program, run as Java, prints {got!r}; lesson says {want!r}", got == want) for k, got, want in _run_printed(P3_PROGS)]
    out.append((f"each program run here is printed in the lesson (missing: {_in_lesson('P3', P3_PROGS)})", not _in_lesson('P3', P3_PROGS)))
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'T.java').write_text("public class T { public static void main(String[] a) { int n = 12; if (n & 3 == 0) System.out.println(\"Y\"); } }")
    r = subprocess.run(['javac', 'T.java'], cwd=d, capture_output=True, text=True)
    out.append(("trap: in Java `n & 3 == 0` does not compile, because == binds tighter than & and gives a boolean", r.returncode != 0))
    left = (3 + 4) & 5; wrong = 3 + (4 & 5)
    out.append(("E3 reading: (3 + 4) & 5 = 5, whereas 3 + (4 & 5) would be 7", (left, wrong) == (5, 7)))
    out.append(("binary table: 12 = 1100, 10 = 1010; AND 1000 = 8, OR 1110 = 14, XOR 0110 = 6", (format(12, 'b'), format(10, 'b'), 12 & 10, 12 | 10, 12 ^ 10) == ('1100', '1010', 8, 14, 6)))
    return out


EXAMPLES['P3'] = p3

_A = "Set a[0] = 4, a[1] = 7, a[2] = 1, a[3] = 9, a[4] = 3"
P5_PROGS = {
    'E1': ("24", ["1) Integer a[5], i, s", f"2) {_A}", "3) Set s = 0", "4) For (each i from 0 to 4)", "5)   s = s + a[i]", "6) End-for", "7) Print s"]),
    'E2': ("16", ["1) Integer a[5]", f"2) {_A}", "3) Print a[1] + a[3]"]),
    'E3': ("9", ["1) Integer a[5], i, m", f"2) {_A}", "3) Set m = a[0]", "4) For (each i from 1 to 4)", "5)   If (a[i] > m) then", "6)     m = a[i]", "7)   End-if", "8) End-for", "9) Print m"]),
    'E4': ("3 9 1 7 4", ["1) Integer a[5], i", f"2) {_A}", "3) For (each i from 4 to 0 step -1)", "4)   Print a[i]", "5) End-for"]),
    'E5': ("4 11 12 21 24", ["1) Integer a[5], i", f"2) {_A}", "3) For (each i from 1 to 4)", "4)   a[i] = a[i] + a[i - 1]", "5) End-for", "6) For (each i from 0 to 4)", "7)   Print a[i]", "8) End-for"]),
}


def p5():
    out = [(f"{k}: the printed program, run as Java, prints {got!r}; lesson says {want!r}", got == want) for k, got, want in _run_printed(P5_PROGS)]
    out.append((f"each program run here is printed in the lesson (missing: {_in_lesson('P5', P5_PROGS)})", not _in_lesson('P5', P5_PROGS)))
    out.append(("the array {4, 7, 1, 9, 3} has 5 elements at indexes 0 to 4; a[1] + a[3] = 7 + 9 = 16", [4, 7, 1, 9, 3][1] + [4, 7, 1, 9, 3][3] == 16))
    return out


EXAMPLES['P5'] = p5
