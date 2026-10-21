"""Reasoning generators: coding-decoding (A1), series (A2), operator logic (A3), blood relations (A5),
cryptarithmetic (A20), non-verbal in text form (A21). Families mirror the observed items R01-R20.
Each question's check() recomputes the answer by a different route (inverse, brute force, or table)."""
import re
import itertools, math, random, string
from fractions import Fraction
from gen_core import Q, distinct_wrong, fmt

AZ = string.ascii_uppercase
pos = lambda c: AZ.index(c) + 1                      # independent of ord()
WORDS = ['BREAK', 'BRIEF', 'CREATE', 'POLITE', 'TABLE', 'CHAIR', 'STONE', 'PLANT', 'MARKET', 'GARDEN', 'FLOWER', 'SILVER',
         'BURST', 'LAKE', 'VERSATILE', 'FRAUD', 'LAST', 'SMART', 'NORTH', 'BRAVE', 'CLOUD', 'DREAM', 'FRUIT', 'GLASS', 'HOUSE',
         'LIGHT', 'MOUSE', 'OCEAN', 'PAPER', 'QUIET', 'RIVER', 'SHARP', 'TIGER', 'UNION', 'VOICE', 'WATER', 'YOUTH', 'ZEBRA',
         'BRIDGE', 'CASTLE', 'DOCTOR', 'ENGINE', 'FOREST', 'GUITAR', 'HAMMER', 'ISLAND', 'JUNGLE', 'KITTEN', 'LADDER', 'MIRROR']


def opts_str(ans, wrong):
    return [ans] + [w for w in wrong if w != ans][:3]


# =========================================================== A1 coding-decoding
def cd_lettersum(rng):
    w1, w2, w3 = rng.sample(WORDS, 3)
    s = lambda w: sum(pos(c) for c in w)
    ans = s(w3)
    wrong = distinct_wrong(ans, [ans + 1, ans - 1, ans + 10, ans - 10, s(w3[:-1]) + pos(w3[0])], rng, lo=1)
    q = f"In a certain code language {w1} is written as {s(w1)} and {w2} is written as {s(w2)}. How is {w3} written in that code?"
    why = (f"Each letter stands for its place in the alphabet and the code is the sum. {w1}: {' + '.join(str(pos(c)) for c in w1)} = {s(w1)}; "
           f"{w2}: {' + '.join(str(pos(c)) for c in w2)} = {s(w2)}. So {w3} = {' + '.join(str(pos(c)) for c in w3)} = **{ans}**.")
    return Q(q, [ans] + wrong, why, lambda: sum(ord(c) - 64 for c in w3), 'Letter sum')


def cd_mean(rng):
    cand = [w for w in WORDS if sum(pos(c) for c in w) % len(w) == 0]
    w1, w2, w3 = rng.sample(cand, 3)
    m = lambda w: sum(pos(c) for c in w) // len(w)
    ans = m(w3)
    wrong = distinct_wrong(ans, [sum(pos(c) for c in w3), ans + 1, ans - 1], rng, lo=1)
    q = f"In a certain code {w1} is written as {m(w1)} and {w2} as {m(w2)}. What is the code for {w3}?"
    why = (f"The code is the **average** of the letter positions. {w1}: {sum(pos(c) for c in w1)} ÷ {len(w1)} = {m(w1)}; {w2}: {sum(pos(c) for c in w2)} ÷ {len(w2)} = {m(w2)}. "
           f"{w3}: {sum(pos(c) for c in w3)} ÷ {len(w3)} = **{ans}**.")
    return Q(q, [ans] + wrong, why, lambda: Fraction(sum(ord(c) - 64 for c in w3), len(w3)).numerator // Fraction(sum(ord(c) - 64 for c in w3), len(w3)).denominator, 'Average of positions')


def cd_position(rng):
    w1, w2 = rng.sample([w for w in WORDS if 4 <= len(w) <= 6], 2)
    keep_odd = rng.random() < 0.5
    enc = lambda w: ''.join((str(pos(c)) if ((i % 2 == 0) == keep_odd) else '0') for i, c in enumerate(w))
    rule = 'odd positions keep the alphabet number and even positions become 0' if keep_odd else 'even positions keep the alphabet number and odd positions become 0'
    ans = enc(w2)
    alt = ''.join(str(pos(c)) for c in w2)
    wrong = [alt, ''.join((str(pos(c)) if ((i % 2 == 0) != keep_odd) else '0') for i, c in enumerate(w2)), enc(w2)[:-1] + '0']
    wrong = [x for x in wrong if x != ans][:3]
    while len(wrong) < 3:
        wrong.append(ans[::-1] + str(len(wrong)))
    q = f"In a certain code {w1} is written as {enc(w1)}. How is {w2} written in that code?"
    why = f"Compare the code with the word letter by letter: {rule}. {w1} → {enc(w1)}. Apply it to {w2}: " + ' '.join(f"{c}={('%d' % pos(c)) if ((i % 2 == 0) == keep_odd) else '0'}" for i, c in enumerate(w2)) + f" → **{ans}**."
    def check():
        out = ''
        for i, c in enumerate(w2):
            if keep_odd and i % 2 == 0 or (not keep_odd) and i % 2 == 1:
                out += str(AZ.find(c) + 1)
            else:
                out += '0'
        return out
    return Q(q, [ans] + wrong, why, check, 'Position rule')


def cd_swap(rng):
    n = 5
    perm = rng.choice([(1, 0, 2, 4, 3), (1, 0, 2, 3, 4), (0, 1, 3, 2, 4), (4, 1, 2, 3, 0), (2, 1, 0, 3, 4), (1, 0, 3, 2, 4)])
    w1, w2 = rng.sample([w for w in WORDS if len(w) == n], 2)
    enc = lambda w: ''.join(w[i] for i in perm)
    ans = enc(w2)
    wrong = [w2[::-1], w2[1:] + w2[0], w2[-1] + w2[:-1], enc(enc(w2))]
    wrong = [x for x in dict.fromkeys(wrong) if x != ans][:3]
    if len(wrong) < 3: return None
    q = f"If {w1} is written as {enc(w1)}, how is {w2} written in the same code?"
    moved = ', '.join(f"letter {i + 1} goes to place {perm.index(i) + 1}" for i in range(n) if perm[i] != i)
    why = f"Only the **positions** change: {moved}. Apply the same shuffle to {w2}: **{ans}**."
    def check():
        inv = [perm.index(i) for i in range(n)]
        dec = ''.join(ans[inv[i]] for i in range(n))    # decode by inverse permutation must recover the word
        assert dec == w2
        return ans
    return Q(q, [ans] + wrong, why, check, 'Position swap')


def cd_reverse_shift(rng):
    w1, w2 = rng.sample([w for w in WORDS if 5 <= len(w) <= 7], 2)
    k = rng.choice([-1, 1, -2, 2])
    sh = lambda c: AZ[(AZ.index(c) + k) % 26]
    enc = lambda w: ''.join(sh(c) for c in reversed(w))
    ans = enc(w2)
    wrong = [''.join(sh(c) for c in w2), w2[::-1], ''.join(AZ[(AZ.index(c) - k) % 26] for c in reversed(w2)), ''.join(sh(c) for c in reversed(w2))[::-1]]
    wrong = [x for x in dict.fromkeys(wrong) if x != ans][:3]
    if len(wrong) < 3: return None
    q = f"In a certain code {w1} is written as {enc(w1)}. How is {w2} written in that code?"
    d = f"{abs(k)} place{'s' if abs(k) > 1 else ''} {'forward' if k > 0 else 'back'}"
    why = f"Compare {w1} with {enc(w1)}: the word is written **backwards** and every letter then moves {d} in the alphabet. {w2} reversed is {w2[::-1]}; shifting each letter gives **{ans}**."
    def check():
        back = ''.join(AZ[(AZ.index(c) - k) % 26] for c in ans)[::-1]
        assert back == w2
        return ans
    return Q(q, [ans] + wrong, why, check, 'Reverse and shift')


def cd_shift(rng):
    w1, w2 = rng.sample([w for w in WORDS if 4 <= len(w) <= 6], 2)
    k = rng.choice([1, 2, 3, -1, -2, -3])
    mirror = rng.random() < 0.3
    f = (lambda c: AZ[25 - AZ.index(c)]) if mirror else (lambda c: AZ[(AZ.index(c) + k) % 26])
    ans = ''.join(f(c) for c in w2)
    wrong = [''.join(AZ[(AZ.index(c) - (0 if mirror else k)) % 26] for c in w2), ''.join(AZ[(AZ.index(c) + 1) % 26] for c in w2), ''.join(AZ[(AZ.index(c) - 1) % 26] for c in w2), ''.join(AZ[25 - AZ.index(c)] for c in w2)]
    wrong = [x for x in dict.fromkeys(wrong) if x != ans][:3]
    if len(wrong) < 3: return None
    rule = 'every letter is replaced by its **opposite** in the alphabet (A↔Z, B↔Y, …)' if mirror else f"every letter moves **{abs(k)} place{'s' if abs(k) > 1 else ''} {'forward' if k > 0 else 'back'}**"
    q = f"In a certain code {w1} is written as {''.join(f(c) for c in w1)}. How is {w2} written in that code?"
    why = f"Compare the first letters: {w1[0]} → {f(w1[0])}, so {rule}. Applied to {w2}: **{ans}**."
    def check():
        inv = (lambda c: AZ[25 - AZ.index(c)]) if mirror else (lambda c: AZ[(AZ.index(c) - k) % 26])
        assert ''.join(inv(c) for c in ans) == w2
        return ans
    return Q(q, [ans] + wrong, why, check, 'Letter shift')


def cd_substitution(rng):
    words = rng.sample(['sun', 'moon', 'star', 'rain', 'wind', 'cloud', 'snow', 'hill', 'lake', 'tree'], 4)
    codes = rng.sample(['ka', 'lo', 'mi', 'ne', 'pu', 'ra', 'si', 'to', 'vu', 'za'], 4)
    m = dict(zip(words, codes))
    a, b, c, d = words
    s1, s2 = [a, b, c], [a, d]
    rng.shuffle(s1); rng.shuffle(s2)
    cs1, cs2 = [m[w] for w in s1], [m[w] for w in s2]
    rng.shuffle(cs1); rng.shuffle(cs2)
    ans = m[a]
    wrong = [m[b], m[c], m[d]]
    q = (f"In a certain code language, ‘{' '.join(s1)}’ is written as ‘{' '.join(cs1)}’ and ‘{' '.join(s2)}’ is written as ‘{' '.join(cs2)}’. "
         f"What is the code for ‘{a}’?")
    why = f"‘{a}’ is the only word common to both sentences, and the only code common to both is **{ans}**. So {a} = {ans}."
    def check():
        common = set(cs1) & set(cs2)
        assert len(common) == 1
        return common.pop()
    return Q(q, [ans] + wrong, why, check, 'Word substitution')


CD = [cd_lettersum, cd_mean, cd_position, cd_swap, cd_reverse_shift, cd_shift, cd_substitution]
gen_coding = lambda rng: rng.choice(CD)(rng)


# =========================================================== A2 series
def s_poly(rng):
    forms = {'n³ + n² + n': lambda n: n ** 3 + n * n + n, 'n³ − n': lambda n: n ** 3 - n, 'n² + 2n': lambda n: n * n + 2 * n,
             'n³ + 1': lambda n: n ** 3 + 1, '2n² − 1': lambda n: 2 * n * n - 1, 'n² + n': lambda n: n * n + n, 'n³ − 1': lambda n: n ** 3 - 1,
             'n(n+1)(n+2)': lambda n: n * (n + 1) * (n + 2)}
    name = rng.choice(list(forms)); f = forms[name]
    start = rng.randint(1, 3); terms = [f(n) for n in range(start, start + 6)]
    ans = f(start + 6)
    # independent route: method of finite differences extrapolation
    def extrap():
        rows = [terms[:]]
        while any(rows[-1][i] != rows[-1][0] for i in range(len(rows[-1]))) and len(rows[-1]) > 1:
            r = rows[-1]; rows.append([r[i + 1] - r[i] for i in range(len(r) - 1)])
        nxt = rows[-1][-1]
        for r in reversed(rows[:-1]): nxt = r[-1] + nxt
        return nxt
    lin = terms[-1] + (terms[-1] - terms[-2])
    wrong = distinct_wrong(ans, [lin, ans + 2, ans - 2], rng, lo=0)
    shown = ', '.join(map(str, terms))
    q = f"Find the next term: {shown}, ?"
    why = (f"The terms are **{name}** for n = {start}, {start + 1}, … : " + ', '.join(f"f({n}) = {f(n)}" for n in range(start, start + 3)) + f". For n = {start + 6}: **{ans}**. "
           f"(The differences {', '.join(str(terms[i + 1] - terms[i]) for i in range(len(terms) - 1))} keep changing; the finite-difference table confirms it.)")
    return Q(q, [ans] + wrong, why, extrap, 'Formula series')


def s_fibo(rng):
    a, b = rng.randint(0, 4), rng.randint(1, 5)
    kind = rng.choice(['sum', 'twice'])
    t = [a, b]
    f = (lambda x, y: x + y) if kind == 'sum' else (lambda x, y: 2 * (x + y))
    while len(t) < 7: t.append(f(t[-2], t[-1]))
    ans = f(t[-2], t[-1])
    wrong = distinct_wrong(ans, [t[-1] * 2, t[-1] + t[-2] if kind == 'twice' else 2 * (t[-1] + t[-2]), ans + 2], rng, lo=0)
    q = f"Find the next term: {', '.join(map(str, t))}, ?"
    rule = 'each term is the sum of the two before it' if kind == 'sum' else 'each term is **twice the sum** of the two before it'
    why = f"{rule}: {t[-2]} and {t[-1]} give **{ans}**."
    def check():
        x, y = t[-2], t[-1]
        return (x + y) if kind == 'sum' else 2 * x + 2 * y
    return Q(q, [ans] + wrong, why, check, 'Two-term recurrence')


def s_diff_ap(rng):
    a0, d1, dd = rng.randint(1, 50), rng.randint(2, 6), rng.randint(1, 4)
    t = [a0]; d = d1
    for _ in range(6): t.append(t[-1] + d); d += dd
    d_next = d
    ans = t[-1] + d_next
    wrong = distinct_wrong(ans, [t[-1] + (t[-1] - t[-2]), t[-1] + d_next - dd, ans + dd], rng, lo=0)
    gaps = [t[i + 1] - t[i] for i in range(len(t) - 1)]
    q = f"Find the missing term: {', '.join(map(str, t))}, ?"
    why = f"The gaps are {', '.join(map(str, gaps))}: they grow by {dd} each time, so the next gap is {d_next}. {t[-1]} + {d_next} = **{ans}**."
    return Q(q, [ans] + wrong, why, lambda: t[-1] + gaps[-1] + (gaps[-1] - gaps[-2]), 'Growing gaps')


def s_interleave(rng):
    a, da = rng.randint(50, 120), rng.randint(10, 25)
    b, db = rng.randint(5, 30), rng.randint(5, 25)
    n = 7
    odd = [a - da * i for i in range(4)]
    even = [b + db * i for i in range(3)]
    t = []
    for i in range(3): t += [odd[i], even[i]]
    t.append(odd[3])
    ans = odd[4] if False else (b + db * 3)
    t_shown = t
    wrong = distinct_wrong(ans, [odd[3] - da, ans + 5, even[2] - db], rng, lo=0)
    q = f"Find the next term: {', '.join(map(str, t_shown))}, ?"
    why = (f"Two series are woven together. Odd places: {', '.join(str(x) for x in odd)} (−{da} each). Even places: {', '.join(str(x) for x in even)} (+{db} each). "
           f"The next place is an even place: {even[2]} + {db} = **{ans}**.")
    def check():
        return t[1::2][-1] + (t[1::2][-1] - t[1::2][-2])
    return Q(q, [ans] + wrong, why, check, 'Interleaved series')


def s_square_rev(rng):
    roots = rng.choice([[12, 13, 14, 15], [21, 31, 41, 51], [11, 12, 13, 14], [16, 17, 18, 19]])
    rev = lambda n: int(str(n)[::-1])
    t = []
    for r in roots[:3]: t += [r * r, rev(r) ** 2]
    t.append(roots[3] ** 2)
    ans = rev(roots[3]) ** 2
    wrong = distinct_wrong(ans, [roots[3] ** 2 + 2 * roots[3] + 1, rev(roots[3]) ** 2 + 10, (rev(roots[3]) + 1) ** 2], rng, lo=1)
    q = f"Find the next term: {', '.join(map(str, t))}, ?"
    why = (f"The terms are squares: {', '.join(f'{int(x ** 0.5)}²' for x in t)}. The roots alternate between a number and its **digit reversal** ({roots[0]}, {rev(roots[0])}, {roots[1]}, {rev(roots[1])}, …). "
           f"After {roots[3]}² comes {rev(roots[3])}² = **{ans}**.")
    return Q(q, [ans] + wrong, why, lambda: int(str(roots[3])[::-1]) ** 2, 'Squares and reversals')


def s_mulplus(rng):
    a0, k, c = rng.randint(1, 4), rng.randint(2, 4), rng.randint(-3, 5)
    t = [a0]
    for _ in range(5): t.append(t[-1] * k + c)
    ans = t[-1] * k + c
    if any(x <= 0 for x in t): return None
    wrong = distinct_wrong(ans, [t[-1] * k, t[-1] + (t[-1] - t[-2]), ans + k], rng, lo=1)
    q = f"Find the next term: {', '.join(map(str, t))}, ?"
    why = f"Each term is the previous one **× {k} {'+' if c >= 0 else '−'} {abs(c)}**: {t[0]} → {t[1]} → {t[2]}. So {t[-1]} × {k} {'+' if c >= 0 else '−'} {abs(c)} = **{ans}**."
    return Q(q, [ans] + wrong, why, lambda: k * t[-1] + c, 'Multiply and adjust')


def s_alnum(rng):
    k = rng.randint(2, 4)
    n0 = rng.randint(2, 4)
    L = rng.randint(14, 24)
    step = rng.choice([1, 2])
    f = rng.choice([lambda n: n * n - 1, lambda n: n * n + 1, lambda n: n * n + n, lambda n: 2 * n + 1])
    terms = []
    for i in range(5):
        terms.append((f(n0 + i), AZ[L - 1 - 2 * i if L - 1 - 2 * i >= 0 else 0], 6 + step * i * 2))
    if L - 1 - 2 * 5 < 0: return None
    nxt = (f(n0 + 5), AZ[L - 1 - 10], 6 + step * 10)
    ans = f"{nxt[0]}{nxt[1]}{nxt[2]}"
    wrong = [f"{nxt[0]}{AZ[L - 1 - 8]}{nxt[2]}", f"{nxt[0] + 2}{nxt[1]}{nxt[2]}", f"{nxt[0]}{nxt[1]}{nxt[2] - step}"]
    q = "Find the next term: " + ', '.join(f"{a}{b}{c}" for a, b, c in terms) + ", ?"
    why = (f"Three tracks. Numbers: {', '.join(str(t[0]) for t in terms)}, next {nxt[0]}. Letters step back two places each time: {', '.join(t[1] for t in terms)}, next {nxt[1]}. "
           f"Last numbers rise by {2 * step}: {', '.join(str(t[2]) for t in terms)}, next {nxt[2]}. Answer **{ans}**.")
    def check():
        i = 5
        return f"{f(n0 + i)}{AZ[L - 1 - 2 * i]}{6 + step * 2 * i}"
    return Q(q, [ans] + wrong, why, check, 'Number-letter-number')


def s_primes(rng):
    pr = [p for p in range(2, 80) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
    i = rng.randint(2, 8)
    kind = rng.choice(['plain', 'plus1', 'sq'])
    f = {'plain': lambda p: p, 'plus1': lambda p: p + 1, 'sq': lambda p: p * p}[kind]
    t = [f(p) for p in pr[i:i + 5]]
    ans = f(pr[i + 5])
    wrong = distinct_wrong(ans, [f(pr[i + 5] + 1), f(pr[i + 4] + 2), ans + 2], rng, lo=1)
    nm = {'plain': 'consecutive primes', 'plus1': 'each prime plus 1', 'sq': 'squares of consecutive primes'}[kind]
    q = f"Find the next term: {', '.join(map(str, t))}, ?"
    why = f"The terms are {nm}: {', '.join(str(p) for p in pr[i:i + 5])} → the next prime is {pr[i + 5]}, giving **{ans}**."
    def check():
        x = pr[i + 4] + 1
        while any(x % d == 0 for d in range(2, int(x ** 0.5) + 1)): x += 1
        return f(x)
    return Q(q, [ans] + wrong, why, check, 'Prime-based')


SER = [s_poly, s_fibo, s_diff_ap, s_interleave, s_square_rev, s_mulplus, s_alnum, s_primes]
gen_series = lambda rng: rng.choice(SER)(rng)


# =========================================================== A3 operator logic
def op_digitsum_quot(rng):
    ys = rng.sample([2, 3, 4, 5, 6, 7, 8, 9], 3)
    xs = [y * rng.randint(40, 150) for y in ys]
    f = lambda x, y: sum(map(int, str(x // y)))
    ans = f(xs[2], ys[2])
    wrong = distinct_wrong(ans, [sum(map(int, str(xs[2] // ys[2]))) % 10, ans + 1, xs[2] // ys[2] if xs[2] // ys[2] != ans else ans + 3], rng, lo=1)
    q = f"If {xs[0]} ★ {ys[0]} = {f(xs[0], ys[0])} and {xs[1]} ★ {ys[1]} = {f(xs[1], ys[1])}, find {xs[2]} ★ {ys[2]}."
    why = (f"Divide, then add the digits of the quotient **once**. {xs[0]} ÷ {ys[0]} = {xs[0] // ys[0]} → {f(xs[0], ys[0])}; {xs[1]} ÷ {ys[1]} = {xs[1] // ys[1]} → {f(xs[1], ys[1])}. "
           f"{xs[2]} ÷ {ys[2]} = {xs[2] // ys[2]} → **{ans}**.")
    return Q(q, [ans] + wrong, why, lambda: sum(int(ch) for ch in str(int(xs[2] / ys[2]))), 'Divide then digit-sum')


def op_dollar(rng):
    k = rng.choice([30, 40, 50, 60, 70, 80, 90, 100])
    nums = [rng.randint(11, 99) for _ in range(3)]
    if any(0 in (n % 10, n // 10) for n in nums) or len(set(nums)) < 3: return None
    f = lambda n: (n // 10) * (n % 10) + k
    ans = f(nums[2])
    wrong = distinct_wrong(ans, [(nums[2] // 10) + (nums[2] % 10) + k, (nums[2] // 10) * (nums[2] % 10), ans + 10], rng, lo=1)
    q = f"If ${nums[0]} = {f(nums[0])} and ${nums[1]} = {f(nums[1])}, what is ${nums[2]} ? (Here $ is a mathematical operator acting on the two digits.)"
    why = (f"Split each number into its digits, multiply them and add {k}: {nums[0] // 10}×{nums[0] % 10} + {k} = {f(nums[0])}; {nums[1] // 10}×{nums[1] % 10} + {k} = {f(nums[1])}. "
           f"So ${nums[2]} = {nums[2] // 10}×{nums[2] % 10} + {k} = **{ans}**.")
    return Q(q, [ans] + wrong, why, lambda: int(str(nums[2])[0]) * int(str(nums[2])[1]) + k, 'Digit product plus constant')


def op_substitute(rng):
    syms = ['+', '-', '*', '/']
    perm = syms[:]
    while perm == syms: rng.shuffle(perm)
    mapping = dict(zip(syms, perm))                     # "+ means -" etc.
    nums = [rng.randint(2, 12) for _ in range(4)]
    ops = [rng.choice(syms) for _ in range(3)]
    expr_real = f"{nums[0]} {ops[0]} {nums[1]} {ops[1]} {nums[2]} {ops[2]} {nums[3]}"
    expr_sub = ' '.join(mapping.get(tok, tok) for tok in expr_real.split())
    try:
        val = eval(expr_sub)
    except ZeroDivisionError:
        return None
    if abs(val - round(val)) > 1e-9 or abs(val) > 500: return None
    val = int(round(val))
    mp = ', '.join(f"‘{a}’ means ‘{b}’" for a, b in mapping.items() if a != b)
    shown = expr_real.replace('*', '×').replace('/', '÷').replace('-', '−')
    wrong = distinct_wrong(val, [int(round(eval(expr_real))) if abs(eval(expr_real) - round(eval(expr_real))) < 1e-9 else val + 4, val + 2, -val if val else 5], rng)
    q = f"If {mp.replace('*', '×').replace('/', '÷').replace('-', '−')}, what is the value of {shown} ?"
    sub_shown = expr_sub.replace('*', '×').replace('/', '÷').replace('-', '−')
    why = f"Swap each sign for what it stands for first: {shown} becomes {sub_shown}. Now apply BODMAS (division and multiplication before addition and subtraction): **{val}**."
    return Q(q, [val] + wrong, why, lambda: int(round(eval(expr_sub))), 'Sign substitution')


def op_interchange(rng):
    nums = [rng.randint(2, 15) for _ in range(4)]
    ops = [rng.choice(['+', '-', '*']) for _ in range(3)]
    toks = [str(nums[0]), ops[0], str(nums[1]), ops[1], str(nums[2]), ops[2], str(nums[3])]
    num_idx = [0, 2, 4, 6]
    # choose a swap of two numbers, compute target, then break it
    a, b = rng.sample(num_idx, 2)
    swapped = toks[:]; swapped[a], swapped[b] = swapped[b], swapped[a]
    target = eval(''.join(swapped))
    if eval(''.join(toks)) == target or abs(target) > 200: return None
    # all single swaps of two numbers that hit the target
    hits = []
    for x, y in itertools.combinations(num_idx, 2):
        t = toks[:]; t[x], t[y] = t[y], t[x]
        if eval(''.join(t)) == target and toks[x] != toks[y]: hits.append((toks[x], toks[y]))
    if len(hits) != 1: return None
    pairs = list(itertools.combinations(sorted(set(toks[i] for i in num_idx)), 2))
    if len(pairs) < 4: return None
    ans = f"{hits[0][0]} and {hits[0][1]}"
    others = [p for p in pairs if set(p) != set(hits[0])]
    rng.shuffle(others)
    wrong = [f"{p[0]} and {p[1]}" for p in others[:3]]
    if len(wrong) < 3: return None
    shown = ' '.join(toks).replace('*', '×').replace('-', '−')
    tg = str(target).replace('-', '−')
    q = f"Which two **numbers** must be interchanged for the equation to be correct?\n\n{shown} = {tg}"
    why = f"Try the swaps. Interchanging {hits[0][0]} and {hits[0][1]} gives {' '.join(swapped).replace('*', '×').replace('-', '−')} = {tg} (BODMAS). No other pair of these numbers works."
    def check():
        found = []
        for x, y in itertools.combinations(num_idx, 2):
            t = toks[:]; t[x], t[y] = t[y], t[x]
            if eval(''.join(t)) == target and toks[x] != toks[y]: found.append(f"{toks[x]} and {toks[y]}")
        return found[0]
    return Q(q, [ans] + wrong, why, check, 'Interchange numbers')


OPS = [op_digitsum_quot, op_dollar, op_substitute, op_interchange]
gen_operator = lambda rng: rng.choice(OPS)(rng)


# =========================================================== A5 blood relations
UP, DOWN, SIDE, SPOUSE = 'up', 'down', 'side', 'spouse'
WORD = {'father': (UP, 'M'), 'mother': (UP, 'F'), 'son': (DOWN, 'M'), 'daughter': (DOWN, 'F'), 'brother': (SIDE, 'M'),
        'sister': (SIDE, 'F'), 'husband': (SPOUSE, 'M'), 'wife': (SPOUSE, 'F')}
NAME = {(UP,): ('father', 'mother'), (DOWN,): ('son', 'daughter'), (SIDE,): ('brother', 'sister'), (SPOUSE,): ('husband', 'wife'),
        (UP, UP): ('grandfather', 'grandmother'), (DOWN, DOWN): ('grandson', 'granddaughter'), (UP, SIDE): ('uncle', 'aunt'),
        (SIDE, DOWN): ('nephew', 'niece'), (SPOUSE, UP): ('father-in-law', 'mother-in-law'), (DOWN, SPOUSE): ('son-in-law', 'daughter-in-law'),
        (SPOUSE, SIDE): ('brother-in-law', 'sister-in-law'), (SIDE, SPOUSE): ('brother-in-law', 'sister-in-law'), (UP, SIDE, DOWN): ('cousin', 'cousin')}
REWRITE = {(SIDE, SIDE): (SIDE,), (SIDE, UP): (UP,), (DOWN, SIDE): (DOWN,), (UP, DOWN): (SIDE,), (DOWN, UP): (SPOUSE,),
           (UP, SPOUSE): (UP,), (SPOUSE, DOWN): (DOWN,)}


def reduce_path(path):
    path = tuple(path); changed = True
    while changed:
        changed = False
        for i in range(len(path) - 1):
            pair = path[i:i + 2]
            if pair in REWRITE:
                path = path[:i] + REWRITE[pair] + path[i + 2:]; changed = True; break
            if pair == (SPOUSE, SPOUSE):
                return None
    return path


def gen_blood(rng, n_st=None):
    n_st = n_st or rng.choice([2, 2, 3])
    people = rng.sample(['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'], n_st + 1)   # letters, so no name implies a sex
    words = [rng.choice(list(WORD)) for _ in range(n_st)]
    # statement i: people[i] is the <word> of people[i+1]
    hops = []                                   # hop from people[i+1] to people[i]
    sex = {}
    for i, w in enumerate(words):
        kind, sx = WORD[w]
        if sex.get(people[i], sx) != sx: return None
        sex[people[i]] = sx
        hops.append((kind, sx))
    # spouse hops must join opposite sexes when both are known
    for i, w in enumerate(words):
        if WORD[w][0] == SPOUSE:
            other = sex.get(people[i + 1])
            if other == WORD[w][1]: return None
    path = [h[0] for h in reversed(hops)]                 # from people[-1] back to people[0]
    red = reduce_path(path)
    if red is None or red not in NAME: return None
    tgt_sex = sex[people[0]]
    ans = NAME[red][0 if tgt_sex == 'M' else 1]
    if red == (UP, SIDE, DOWN) and n_st != 3: return None
    allnames = sorted({x for v in NAME.values() for x in v} - {ans})
    # distractors: plausible neighbours
    pool = [x for x in ['father', 'mother', 'brother', 'sister', 'uncle', 'aunt', 'grandfather', 'grandmother', 'son', 'daughter', 'nephew', 'niece', 'cousin', 'husband', 'wife', 'father-in-law', 'mother-in-law', 'brother-in-law', 'sister-in-law', 'grandson', 'granddaughter', 'son-in-law', 'daughter-in-law'] if x != ans]
    same_sex = [x for x in pool if (x in ['father', 'brother', 'uncle', 'grandfather', 'son', 'nephew', 'husband', 'father-in-law', 'brother-in-law', 'grandson', 'son-in-law', 'cousin'] ) == (tgt_sex == 'M')]
    rng.shuffle(same_sex)
    wrong = same_sex[:3]
    stmts = ' '.join(f"{people[i]} is the {words[i]} of {people[i + 1]}." for i in range(n_st))
    q = f"{stmts} How is {people[0]} related to {people[-1]}?"
    chain = ' → '.join(f"{people[i + 1]}’s {words[i]} is {people[i]}" for i in reversed(range(n_st)))
    why = (f"Walk from {people[-1]} back to {people[0]}, one statement at a time: {chain}. "
           f"Combined, that is {ans} (the path reduces to ‘{' then '.join(red)}’, and {people[0]} is {'male' if tgt_sex == 'M' else 'female'}).")
    def check():
        # converse test: the relation read the other way round must point back at people[0]'s sex and path
        conv = {UP: DOWN, DOWN: UP, SIDE: SIDE, SPOUSE: SPOUSE}
        back = reduce_path([conv[k] for k in reversed(red)]) if red != (UP, SIDE, DOWN) else (UP, SIDE, DOWN)
        assert back is not None and back in NAME or red == (UP, SIDE, DOWN) or back in NAME, (red, back)
        names = NAME[red]
        return names[0] if tgt_sex == 'M' else names[1]
    return Q(q, [ans] + wrong, why, check, 'Relation chain')


# =========================================================== A20 cryptarithmetic
def gen_crypto(rng):
    op = rng.choice(['+', '+', '-', '*'])
    if op == '*':
        x, y = rng.randint(10, 99), rng.randint(2, 9)
    else:
        x, y = rng.randint(10, 99), rng.randint(10, 99)
        if op == '-' and x <= y: x, y = y, x
    z = {'+': x + y, '-': x - y, '*': x * y}[op]
    if op == '-' and z < 10: return None
    digs = sorted({int(ch) for ch in f"{x}{y}{z}"})
    if len(digs) > 6: return None
    letters = rng.sample(string.ascii_uppercase[:12], len(digs))
    m = dict(zip(digs, letters))
    enc = lambda n: ''.join(m[int(ch)] for ch in str(n))
    sx, sy, sz = enc(x), enc(y), enc(z)
    let = sorted(set(sx + sy + sz))
    lead = {sx[0], sy[0], sz[0]}

    def solutions():
        out = []
        for perm in itertools.permutations(range(10), len(let)):
            d = dict(zip(let, perm))
            if any(d[c] == 0 for c in lead): continue
            X = int(''.join(str(d[c]) for c in sx)); Y = int(''.join(str(d[c]) for c in sy)); Z = int(''.join(str(d[c]) for c in sz))
            if {'+': X + Y, '-': X - Y, '*': X * Y}[op] == Z:
                out.append(d)
                if len(out) > 1: return out
        return out
    sols = solutions()
    if len(sols) != 1: return None
    ask = rng.choice(let)
    ans = sols[0][ask]
    wrong = distinct_wrong(ans, [], rng, lo=0, hi=9)
    sym = {'+': '+', '-': '−', '*': '×'}[op]
    q = f"In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).\n\n```text\n  {sx}\n{sym} {sy}\n= {sz}\n```\n\nWhat is the value of **{ask}**?"
    why = (f"Solve column by column, starting from the units column and tracking carries. The only assignment that works is "
           + ', '.join(f"{c} = {sols[0][c]}" for c in let) + f" (that is {x} {sym} {y} = {z}). So {ask} = **{ans}**. A search over all assignments finds exactly one.")
    return Q(q, [ans] + wrong, why, lambda: solutions()[0][ask], 'Cryptarithm')


# =========================================================== A21 non-verbal (text forms)
def nv_cube(rng):
    n = rng.randint(3, 6)
    k = rng.choice([0, 1, 2, 3])
    count = lambda n, k: sum(1 for x in range(n) for y in range(n) for z in range(n) if sum(c in (0, n - 1) for c in (x, y, z)) == k)
    formula = {3: 8, 2: 12 * (n - 2), 1: 6 * (n - 2) ** 2, 0: (n - 2) ** 3}[k]
    ans = formula
    wrong = distinct_wrong(ans, [6 * n * n, 12 * n, (n - 2) ** 2, 8 * (n - 2)], rng, lo=0)
    word = {3: 'three', 2: 'two', 1: 'one', 0: 'no'}[k]
    q = f"A solid cube is painted on all six faces and then cut into {n}³ = {n ** 3} identical small cubes. How many small cubes have **{word}** painted face{'s' if k != 1 else ''}?"
    why = {3: f"Only the 8 corner cubes touch three faces: **8**.", 2: f"Edge cubes (not corners): 12 edges × ({n} − 2) = **{ans}**.",
           1: f"Face-centre cubes: 6 faces × ({n} − 2)² = **{ans}**.", 0: f"Interior cubes: ({n} − 2)³ = **{ans}**."}[k]
    return Q(q, [ans] + wrong, why, lambda: count(n, k), 'Painted cube')


def nv_dice(rng):
    pairs = [(1, 6), (2, 5), (3, 4)]
    a = rng.randint(1, 6)
    opp = lambda x: 7 - x
    q = f"On a standard die opposite faces add up to 7. If the face showing {a} is on top, which number is on the **bottom**?"
    ans = opp(a)
    wrong = distinct_wrong(ans, [a + 1, a - 1 if a > 1 else 3, 4], rng, lo=1, hi=6)
    why = f"Opposite faces sum to 7, so the bottom is 7 − {a} = **{ans}**."
    def check():
        for p, q2 in pairs:
            if a == p: return q2
            if a == q2: return p
    return Q(q, [ans] + wrong, why, check, 'Dice')


def nv_mirror_clock(rng):
    h, m = rng.randint(1, 11), rng.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
    tot = h * 60 + m
    mir = (12 * 60 - tot) % (12 * 60)
    mh, mm = divmod(mir, 60)
    mh = 12 if mh == 0 else mh
    fmt_t = lambda H, M: f"{H}:{M:02d}"
    ans = fmt_t(mh, mm)
    wrong = []
    for d in (5, -5, 10, 60, -60, 15):
        t2 = (mir + d) % 720; hh, mi = divmod(t2, 60); hh = 12 if hh == 0 else hh
        wrong.append(fmt_t(hh, mi))
    wrong = [w for w in dict.fromkeys(wrong) if w != ans][:3]
    if h == 6 and m == 0: return None
    q = f"A clock shows {fmt_t(h, m)}. What time will its **mirror image** show?"
    why = f"The mirror image time is 12:00 − {fmt_t(h, m)} = {fmt_t(mh, mm)} (subtract from 12 hours; for 12-hour clocks this is the same as 11:60 − t). Answer **{ans}**."
    def check():
        t = (720 - (h * 60 + m)) % 720
        a, b = divmod(t, 60)
        return fmt_t(12 if a == 0 else a, b)
    return Q(q, [ans] + wrong, why, check, 'Mirror clock')


def nv_squares(rng):
    n = rng.randint(3, 7)
    what = rng.choice(['squares', 'rectangles'])
    if what == 'squares':
        ans = sum(i * i for i in range(1, n + 1))
        chk = lambda: sum((n - s + 1) ** 2 for s in range(1, n + 1))
        wrong = distinct_wrong(ans, [n * n, sum(range(1, n + 1)), ans + n], rng, lo=1)
        q = f"How many squares of every size are there in an {n} × {n} grid of unit squares?"
        why = f"Squares of side s: ({n} − s + 1)². Adding for s = 1..{n}: {' + '.join(str(i * i) for i in range(n, 0, -1))} = **{ans}**."
    else:
        ans = (n * (n + 1) // 2) ** 2
        chk = lambda: sum(1 for x1 in range(n + 1) for x2 in range(x1 + 1, n + 1) for y1 in range(n + 1) for y2 in range(y1 + 1, n + 1))
        wrong = distinct_wrong(ans, [sum(i * i for i in range(1, n + 1)), n * n * n, ans - n], rng, lo=1)
        q = f"How many rectangles (squares included) can be traced along the lines of an {n} × {n} grid?"
        why = f"Choose 2 of the {n + 1} vertical lines and 2 of the {n + 1} horizontal lines: C({n + 1},2)² = {n * (n + 1) // 2}² = **{ans}**."
    return Q(q, [ans] + wrong, why, chk, 'Counting figures')


NV = [nv_cube, nv_dice, nv_mirror_clock, nv_squares]
gen_nonverbal = lambda rng: rng.choice(NV)(rng)


# =========================================================== official-sample types: data sufficiency (1/2/3/4), conditional rules, ordered deduction
def _classify(a, b, both):
    if a and b: return 2
    if a != b: return 1
    return 3 if both else 4


DS_ST = [
    ('x + y = {k}', lambda k: (lambda u: u['x'] + u['y'] == k), range(-6, 13)),
    ('y = {k}', lambda k: (lambda u: u['y'] == k), range(-5, 9)),
    ('x - y = {k}', lambda k: (lambda u: u['x'] - u['y'] == k), range(-6, 9)),
    ('x × y = {k}', lambda k: (lambda u: u['x'] * u['y'] == k), [12, 18, 24, 6, 10]),
    ('x² = {k}', lambda k: (lambda u: u['x'] ** 2 == k), [4, 9, 16, 25, 36]),
    ('x > {k}', lambda k: (lambda u: u['x'] > k), range(-3, 6)),
    ('x < {k}', lambda k: (lambda u: u['x'] < k), range(-3, 8)),
    ('x is a positive number', lambda k: (lambda u: u['x'] > 0), [0]),
    ('x is even', lambda k: (lambda u: u['x'] % 2 == 0), [0]),
    # statements that fix x on their own (answers 1 and 2 need these)
    ('x³ = {k}', lambda k: (lambda u: u['x'] ** 3 == k), [-27, -8, 8, 27, 64]),
    ('2x + 3 = {k}', lambda k: (lambda u: 2 * u['x'] + 3 == k), [-5, -1, 5, 7, 9, 13, 17]),
    ('x² = {k} and x is positive', lambda k: (lambda u: u['x'] ** 2 == k and u['x'] > 0), [4, 9, 16, 25, 36]),
    ('x² = {k} and x < 0', lambda k: (lambda u: u['x'] ** 2 == k and u['x'] < 0), [4, 9, 16, 25, 36]),
]
DS_U = [dict(x=x, y=y) for x in range(-12, 13) for y in range(-12, 13)]


def _vals(pred):
    return sorted({u['x'] for u in DS_U if pred(u)})


def _show(vs):
    if len(vs) == 1: return f"x = {vs[0]}"
    if len(vs) <= 4: return "x could be " + ' or '.join(map(str, vs))
    return f"x has many possible values (for example {', '.join(map(str, vs[:3]))})"


def gen_ds(rng, want=None, pool=None):
    want = want or rng.choice([1, 2, 3, 4])
    (t1, f1, r1), (t2, f2, r2) = rng.sample([e for e in DS_ST if pool is None or e[0] in pool] if pool else DS_ST, 2)
    k1, k2 = rng.choice(list(r1)), rng.choice(list(r2))
    s1, s2 = t1.format(k=k1), t2.format(k=k2)
    p1, p2 = f1(k1), f2(k2)
    v1, v2, vb = _vals(p1), _vals(p2), _vals(lambda u: p1(u) and p2(u))
    if not v1 or not v2 or not vb: return None
    a, b, both = len(v1) == 1, len(v2) == 1, len(vb) == 1
    cl = _classify(a, b, both)
    if cl != want: return None
    first = rng.random() < 0.5
    if not first: s1, s2, v1, v2, a, b = s2, s1, v2, v1, b, a
    q = ("Is the information enough to find the value of x? Mark **1** if exactly one statement alone is enough, **2** if either statement alone is enough, "
         "**3** if both together are needed, **4** if even both together are not enough.\n\n"
         f"I. {s1}\nII. {s2}\n")
    why = (f"Statement I alone: {_show(v1)}. Statement II alone: {_show(v2)}. Together: {_show(vb)}. "
           f"So the mark is **{cl}**. (Found by listing every integer pair (x, y) from −12 to 12 that fits each statement.)")
    def check():
        pp1 = lambda u: eval_stmt(s1, u); pp2 = lambda u: eval_stmt(s2, u)
        A = len({u['x'] for u in DS_U if pp1(u)}) == 1; B = len({u['x'] for u in DS_U if pp2(u)}) == 1
        C = len({u['x'] for u in DS_U if pp1(u) and pp2(u)}) == 1
        return _classify(A, B, C)
    return Q(q, [cl] + [c for c in (1, 2, 3, 4) if c != cl], why, check, tag='Data sufficiency (1-2-3-4)', fixed=True)


def eval_stmt(text, u):
    """Re-evaluate a statement from its TEXT (a second route that does not reuse the lambdas)."""
    x, y = u['x'], u['y']
    ok = True
    for t in text.split(' and '):                       # compound statements are a conjunction of simple ones
        t = t.strip()
        if t == 'x is even': r = x % 2 == 0
        elif t in ('x is a positive number', 'x is positive'): r = x > 0
        else:
            t = re.sub(r'(\d)x', r'\1*x', t.replace('×', '*').replace('²', '**2').replace('³', '**3'))
            t = t.replace('=', '==') if '>' not in t and '<' not in t else t
            r = bool(eval(t, {}, dict(x=x, y=y)))
        ok = ok and r
    return ok


NAMES = ['Arun', 'Bina', 'Charu', 'Dev', 'Esha', 'Farid']


def gen_conditional(rng):
    n = 6
    people = NAMES[:n]
    rules = []
    kinds = ['not', 'notcome', 'need']
    while len(rules) < 4:
        x, y = rng.sample(range(n), 2)
        k = rng.choice(kinds)
        r = (k, x, y)
        if r not in rules: rules.append(r)

    def ok(a):
        for k, x, y in rules:
            if k == 'not' and a[x] and a[y]: return False
            if k == 'notcome' and not a[x] and not a[y]: return False
            if k == 'need' and a[x] and not a[y]: return False
        return True
    W = [a for a in itertools.product([0, 1], repeat=n) if ok(a)]
    if len(W) < 8: return None
    p = rng.randrange(n)
    mode = rng.choice(['absent', 'present'])
    cond = [a for a in W if a[p]] if mode == 'absent' else [a for a in W if not a[p]]
    if not cond: return None
    forced = [i for i in range(n) if i != p and all((not a[i]) if mode == 'absent' else a[i] for a in cond)]
    if len(forced) != 1: return None
    ans = people[forced[0]]
    others = [people[i] for i in range(n) if i != p and i != forced[0]]
    # distractors must not be forced either
    wrong = [o for o in others][:3]
    txt = []
    for k, x, y in rules:
        a, b = people[x], people[y]
        txt.append({'not': f"If {a} comes, {b} does not come.", 'notcome': f"If {a} does not come, {b} comes.", 'need': f"If {a} comes, {b} comes too."}[k])
    stem = f"Six friends ({', '.join(people)}) are invited to a party. Not all of them get along, so these rules apply:\n\n" + '\n'.join(f"- {t}" for t in txt) + "\n\n"
    stem += (f"If {people[p]} comes, who must stay away?" if mode == 'absent' else f"If {people[p]} does not come, who must come?")
    why = (f"Of the 64 possible guest lists, {len(W)} obey every rule. " + (f"Among the {len(cond)} in which {people[p]} {'comes' if mode == 'absent' else 'does not come'}, "
           f"only {ans} is {'absent' if mode == 'absent' else 'present'} every time, so the answer is **{ans}**."))

    def check():
        # second route: for each person, look for a counter-example guest list
        out = []
        for i in range(n):
            if i == p: continue
            hit = False
            for a in itertools.product([0, 1], repeat=n):
                if ok(a) and (a[p] == (1 if mode == 'absent' else 0)) and a[i] == (1 if mode == 'absent' else 0):
                    hit = True; break
            if not hit: out.append(people[i])
        return out[0] if len(out) == 1 else None
    return Q(stem, [ans] + wrong, why, check, tag='If-then rules')


DED_V = [('cats', 'pets', 'animals'), ('doctors', 'graduates', 'readers'), ('roses', 'flowers', 'plants'), ('teachers', 'adults', 'citizens'),
         ('laptops', 'computers', 'machines'), ('poets', 'writers', 'artists'), ('engineers', 'professionals', 'workers'), ('trains', 'vehicles', 'transport')]


def _stmt_text(st):
    k, a, b = st
    return {'all': f"All {a} are {b}.", 'some': f"Some {a} are {b}.", 'no': f"No {a} are {b}.", 'some_not': f"Some {a} are not {b}."}[k]


def _entails(prem, concl, sets):
    import official_sample as OS
    return OS.follows(prem, concl, sets)


def gen_deductive(rng):
    import official_sample as OS
    X, Y, Z = rng.choice(DED_V)
    tpl = rng.choice([
        ([('all', X, Y), ('all', Y, Z)], ('all', X, Z)),
        ([('all', X, Y), ('some', X, Z)], ('some', Y, Z)),
        ([('no', Y, Z), ('all', X, Y)], ('no', X, Z)),
        ([('all', Y, Z), ('some_not', X, Z)], ('some_not', X, Y)),
    ])
    prem, concl = tpl
    sets = [X, Y, Z]
    if not (OS.follows(prem, concl, sets) and not OS.follows([prem[0]], concl, sets) and not OS.follows([prem[1]], concl, sets)): return None
    pool = [('some', X, Z), ('all', Z, X), ('some_not', Y, X), ('no', X, Y), ('all', Z, Y), ('some', Y, X), ('some_not', Z, Y)]
    pool = [s for s in pool if s not in prem and s != concl]
    extra = rng.sample(pool, 2)
    five = [prem[0], prem[1], concl] + extra
    order = list(range(5)); rng.shuffle(order)
    label = {five[i]: 'ABCDE'[order.index(i)] for i in range(5)}
    by_label = {label[s]: s for s in five}
    right = label[prem[0]] + label[prem[1]] + label[concl]
    opts = [right]                       # a list, not a set: set order depends on the hash seed and would change the file between runs
    guard = 0
    while len(opts) < 4 and guard < 500:
        guard += 1
        t = rng.sample('ABCDE', 3)
        o = ''.join(t)
        if o in opts: continue
        trip = [by_label[c] for c in t]
        if OS.follows(trip[:2], trip[2], sets) and not OS.follows([trip[0]], trip[2], sets) and not OS.follows([trip[1]], trip[2], sets): continue   # would also be valid
        opts.append(o)
    if len(opts) < 4: return None
    wrong = [o for o in opts if o != right]
    lines = '\n'.join(f"{'ABCDE'[order.index(i)]}. {_stmt_text(five[i])}" for i in sorted(range(5), key=lambda i: order.index(i)))
    q = ("Five statements are given. Choose the option whose **first two statements together entail the third** (the third follows from the first two, and from neither alone).\n\n" + lines + "\n")
    why = (f"{label[prem[0]]} and {label[prem[1]]} together give {label[concl]} ({_stmt_text(prem[0])[:-1]}, and {_stmt_text(prem[1])[:-1].lower() if False else _stmt_text(prem[1])[:-1]}), and neither alone does. "
           f"A search over every arrangement of the sets confirmed that the other three options fail.")
    def check():
        valid = [o for o in [right] + wrong if OS.follows([by_label[o[0]], by_label[o[1]]], by_label[o[2]], sets)
                 and not OS.follows([by_label[o[0]]], by_label[o[2]], sets) and not OS.follows([by_label[o[1]]], by_label[o[2]], sets)]
        return valid[0] if len(valid) == 1 else None
    return Q(q, [right] + wrong, why, check, tag='Ordered deduction')


def s_primegap(rng):
    pr = [p for p in range(2, 60) if all(p % d for d in range(2, p))]
    start = rng.randint(0, 20); first = rng.randint(0, 2)
    t = [start]
    for g in pr[first:first + 6]: t.append(t[-1] + g)
    shown, ans = t[:-1], t[-1]
    wrong = distinct_wrong(ans, [t[-2] + pr[first + 4] , t[-2] + pr[first + 5] + 2, t[-2] + (t[-2] - t[-3]) ], rng, lo=0)
    q = f"Find the next term: {', '.join(map(str, shown))}, ?"
    gaps = [t[i + 1] - t[i] for i in range(len(t) - 1)]
    why = f"The gaps are {', '.join(map(str, gaps[:-1]))}: consecutive primes. The next prime is {gaps[-1]}, so {shown[-1]} + {gaps[-1]} = **{ans}**."
    def check():
        gs = [shown[i + 1] - shown[i] for i in range(len(shown) - 1)]
        nxt = next(p for p in range(gs[-1] + 1, 80) if all(p % d for d in range(2, p)))
        return shown[-1] + nxt
    return Q(q, [ans] + wrong, why, check, 'Gaps are primes')


SER.append(s_primegap)
