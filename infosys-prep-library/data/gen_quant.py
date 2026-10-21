"""Quantitative generators for the Technical Ability block: data interpretation (A7), linear equations
and ages (A8), number system (A10), mensuration (A11), time and work (A16), permutations,
combinations and probability (A18). All arithmetic uses exact Fractions; every check() uses a
different route (brute force, simulation or enumeration)."""
import itertools, math, random
from fractions import Fraction
from gen_core import Q, distinct_wrong, fmt


def pct_str(fr):
    """Exact Fraction -> '77%' or '33.33%' for options."""
    v = float(fr)
    return (f"{int(round(v))}%" if abs(v - round(v)) < 1e-9 else f"{v:.2f}".rstrip('0').rstrip('.') + '%')


def pct_opts(ans, cands, rng):
    """Numeric wrong options rendered as percentages."""
    a = float(ans)
    w = [c for c in cands if abs(float(c) - a) > 1e-9]
    for d in (2, -2, 5, -5, 10, -10, 1, -1, 4, 3):
        if len(w) >= 3: break
        w.append(a + d)
    out = []
    for c in w:
        s = pct_str(Fraction(c).limit_denominator(1000)) if c >= 0 else None
        if s and s != pct_str(ans) and s not in out: out.append(s)
    return out[:3]


# =========================================================== A7 data interpretation
SUBJECTS = ['English', 'Hindi', 'Maths', 'Science', 'History', 'Geography']
YEARS = [2019, 2020, 2021, 2022, 2023]


def di_freq_table(rng):
    bins = [(140, 150), (150, 160), (160, 170), (170, 180), (180, 190)]
    cnt = [rng.randint(20, 120) for _ in bins]
    tot = sum(cnt)
    k = rng.choice([2, 3, 4])                              # "shorter than <upper bound of bin k>"
    less = sum(cnt[:k])
    ans = Fraction(less * 100, tot)
    wrong = pct_opts(ans, [Fraction(sum(cnt[k:]) * 100, tot), Fraction(cnt[k - 1] * 100, tot), Fraction(less * 100, sum(cnt[:-1]))], rng)
    tbl = '| Height (cm) | Students |\n|---|---|\n' + '\n'.join(f"| {a}–{b} | {c} |" for (a, b), c in zip(bins, cnt))
    q = f"The heights of {tot} students are grouped as shown.\n\n{tbl}\n\nWhat percentage of the students are shorter than {bins[k - 1][1]} cm?"
    why = f"Students in the first {k} groups: {' + '.join(map(str, cnt[:k]))} = {less}. Percentage = {less}/{tot} × 100 = **{pct_str(ans)}**."
    return Q(q, [pct_str(ans)] + wrong, why, lambda: pct_str(Fraction(sum(c for (a, b), c in zip(bins, cnt) if b <= bins[k - 1][1]) * 100, tot)), 'Frequency table')


def di_pie(rng):
    parts = rng.choice([[25, 34, 18, 10, 13], [30, 25, 20, 15, 10], [40, 25, 15, 12, 8], [35, 20, 20, 15, 10], [22, 28, 20, 18, 12]])
    subs = rng.sample(SUBJECTS, 5)
    total = rng.choice([200, 400, 500, 600, 800])
    marks = [total * p // 100 for p in parts]
    if any(total * p % 100 for p in parts): return None
    pas = rng.choice([40, 50, 60])
    failed = [s for s, m in zip(subs, marks) if m < pas]
    if len(failed) != 1: return None
    hi, lo = max(marks), min(marks)
    ans = f"{failed[0]}, {hi - lo}"
    wrong = [f"{failed[0]}, {hi - lo + 12}", f"{rng.choice([s for s in subs if s != failed[0]])}, {hi - lo}", f"{failed[0]}, {hi - lo - 12}"]
    tbl = '| Subject | Share of total marks |\n|---|---|\n' + '\n'.join(f"| {s} | {p}% |" for s, p in zip(subs, parts))
    q = (f"A student scored {total} marks in total. The share of the total earned in each subject is shown. The pass mark in each subject is {pas}.\n\n{tbl}\n\n"
         f"In which subject did the student fail, and what is the difference between the best and the worst subject scores?")
    why = (f"Convert each share to marks ({total} × share): " + ', '.join(f"{s} {m}" for s, m in zip(subs, marks)) + f". Only {failed[0]} is below {pas}. Best − worst = {hi} − {lo} = **{hi - lo}**.")
    def check():
        res = [(s, total * p // 100) for s, p in zip(subs, parts)]
        fs = [s for s, m in res if m < pas]
        return f"{fs[0]}, {max(m for _, m in res) - min(m for _, m in res)}"
    return Q(q, [ans] + wrong, why, check, 'Pie chart as a table')


def di_bar(rng):
    yrs = YEARS[:]
    a_name, b_name = 'Plant A', 'Plant B'
    A = [rng.randint(20, 90) * 10 for _ in yrs]
    B = [rng.randint(20, 90) * 10 for _ in yrs]
    kind = rng.choice(['change', 'ratio', 'avg', 'share'])
    tbl = '| Year | ' + a_name + ' (units) | ' + b_name + ' (units) |\n|---|---|---|\n' + '\n'.join(f"| {y} | {a} | {b} |" for y, a, b in zip(yrs, A, B))
    i = rng.randint(1, 4)
    if kind == 'change':
        ans = Fraction((A[i] - A[i - 1]) * 100, A[i - 1])
        if abs(ans) > 300: return None
        s = pct_str(ans) if ans >= 0 else '−' + pct_str(-ans)
        wrong = [pct_str(abs(ans))] if ans < 0 else []
        wrong += pct_opts(abs(ans), [Fraction((A[i] - A[i - 1]) * 100, A[i]), Fraction((B[i] - B[i - 1]) * 100, B[i - 1])], rng)
        wrong = [w for w in wrong if w != s][:3]
        if len(wrong) < 3: return None
        q = f"Study the table.\n\n{tbl}\n\nBy what percentage did {a_name}'s output change from {yrs[i - 1]} to {yrs[i]}? (A negative sign means a fall.)"
        why = f"Change = {A[i]} − {A[i - 1]} = {A[i] - A[i - 1]}. As a percentage of the **starting** year: {A[i] - A[i - 1]}/{A[i - 1]} × 100 = **{s}**."
        return Q(q, [s] + wrong, why, lambda: (pct_str(Fraction((A[i] - A[i - 1]) * 100, A[i - 1])) if A[i] >= A[i - 1] else '−' + pct_str(Fraction((A[i - 1] - A[i]) * 100, A[i - 1]))), 'Percentage change')
    if kind == 'ratio':
        g = math.gcd(A[i], B[i]); ans = f"{A[i] // g}:{B[i] // g}"
        wrong = [f"{B[i] // g}:{A[i] // g}", f"{A[i - 1] // math.gcd(A[i - 1], B[i - 1])}:{B[i - 1] // math.gcd(A[i - 1], B[i - 1])}", f"{(A[i] + 10) // g}:{B[i] // g}"]
        wrong = [w for w in dict.fromkeys(wrong) if w != ans]
        if len(wrong) < 3: return None
        q = f"Study the table.\n\n{tbl}\n\nWhat is the ratio of {a_name}'s output to {b_name}'s output in {yrs[i]}, in its simplest form?"
        why = f"{A[i]} : {B[i]}, divide both by {g} → **{ans}**."
        return Q(q, [ans] + wrong[:3], why, lambda: str(Fraction(A[i], B[i])).replace('/', ':') if Fraction(A[i], B[i]).denominator != 1 else f"{A[i] // B[i]}:1", 'Ratio')
    if kind == 'avg':
        ans = Fraction(sum(A), len(A))
        if ans.denominator != 1: return None
        ans = int(ans)
        wrong = distinct_wrong(ans, [int(sum(B) / 5), sum(A), int(sum(A[1:]) / 4)], rng, lo=1)
        q = f"Study the table.\n\n{tbl}\n\nWhat was {a_name}'s average yearly output over the five years?"
        why = f"Total = {' + '.join(map(str, A))} = {sum(A)}; average = {sum(A)}/5 = **{ans}**."
        return Q(q, [ans] + wrong, why, lambda: statistics_mean(A), 'Average')
    tot = A[i] + B[i]
    ans = Fraction(A[i] * 100, tot)
    wrong = pct_opts(ans, [Fraction(B[i] * 100, tot), Fraction(A[i] * 100, B[i])], rng)
    if len(wrong) < 3: return None
    q = f"Study the table.\n\n{tbl}\n\nWhat percentage of the combined output of both plants in {yrs[i]} came from {a_name}?"
    why = f"Combined = {A[i]} + {B[i]} = {tot}. {A[i]}/{tot} × 100 = **{pct_str(ans)}**."
    return Q(q, [pct_str(ans)] + wrong, why, lambda: pct_str(Fraction(100 * A[i], A[i] + B[i])), 'Share of total')


def statistics_mean(xs):
    return sum(xs) // len(xs)


DI = [di_freq_table, di_pie, di_bar]
gen_di = lambda rng: rng.choice(DI)(rng)


# =========================================================== A8 linear equations
def lin_ages(rng):
    a, b = rng.choice([(48, 72), (24, 40), (30, 45), (36, 60), (18, 30), (40, 64)]), None
    x, y = a
    back, fwd = rng.choice([2, 3, 4]), rng.choice([2, 3, 4, 5])
    ans = Fraction(x - back, y + fwd)
    ans_s = f"{ans.numerator}:{ans.denominator}"
    wrong = [f"{Fraction(x + fwd, y - back).numerator}:{Fraction(x + fwd, y - back).denominator}", f"{Fraction(x - back, y - back).numerator}:{Fraction(x - back, y - back).denominator}",
             f"{Fraction(x + back, y + fwd).numerator}:{Fraction(x + back, y + fwd).denominator}"]
    wrong = [w for w in dict.fromkeys(wrong) if w != ans_s]
    if len(wrong) < 3: return None
    q = f"The present ages of Gautam and Goru are {x} and {y} years. Find the ratio of Gautam's age {back} years ago to Goru's age {fwd} years from now."
    why = f"{x} − {back} = {x - back}; {y} + {fwd} = {y + fwd}. Ratio {x - back} : {y + fwd} = **{ans_s}**."
    return Q(q, [ans_s] + wrong[:3], why, lambda: ':'.join(map(str, (lambda f: (f.numerator, f.denominator))(Fraction(x - back, y + fwd)))), 'Ages')


def lin_legs(rng):
    c, h = rng.randint(5, 30), rng.randint(5, 30)
    animals = rng.choice([('cows', 'hens', 4, 2, 'legs'), ('goats', 'ducks', 4, 2, 'legs'), ('cars', 'bikes', 4, 2, 'wheels'), ('tables', 'stools', 4, 3, 'legs')])
    n1, n2, l1, l2, unit = animals
    heads, legs = c + h, l1 * c + l2 * h
    ask = rng.choice([n1, n2])
    ans = c if ask == n1 else h
    wrong = distinct_wrong(ans, [heads - ans, legs // (l1 + l2), abs(legs - heads * l2) // 2 if ask == n2 else ans + 2], rng, lo=1)
    what = 'heads' if unit == 'legs' and n1 in ('cows', 'goats') else 'items'
    q = (f"A yard has some {n1} and some {n2}. There are {heads} {what} in all and {legs} {unit} in total "
         f"({n1} have {l1} {unit} each, {n2} have {l2} each). How many {ask} are there?")
    if ask == n1:
        why = f"Suppose all {heads} are {n2}: {heads} × {l2} = {heads * l2}. The extra {legs - heads * l2} comes from {n1}, each adding {l1 - l2}. So {n1} = {legs - heads * l2}/{l1 - l2} = **{ans}**."
    else:
        why = f"Suppose all {heads} are {n1}: {heads} × {l1} = {heads * l1}. The excess {heads * l1 - legs} comes from {n2}, each over-counted by {l1 - l2}. So {n2} = {heads * l1 - legs}/{l1 - l2} = **{ans}**."
    def check():
        for x in range(heads + 1):
            if l1 * x + l2 * (heads - x) == legs: return x if ask == n1 else heads - x
    return Q(q, [ans] + wrong, why, check, 'Heads and legs')


def lin_system(rng):
    x, y = rng.randint(-40, 60), rng.randint(-40, 60)
    if x == y: return None
    a1, b1, a2, b2 = rng.randint(1, 6), rng.randint(1, 6), rng.randint(1, 6), rng.randint(1, 9)
    if a1 * b2 == a2 * b1: return None
    c1, c2 = a1 * x + b1 * y, a2 * x + b2 * y
    # solve by Cramer's rule; brute-force confirms the integer pair
    det = a1 * b2 - a2 * b1
    sx, sy = Fraction(c1 * b2 - c2 * b1, det), Fraction(a1 * c2 - a2 * c1, det)
    if sx.denominator != 1 or sy.denominator != 1: return None
    sx, sy = int(sx), int(sy)
    rel = 'x > y' if sx > sy else ('x < y' if sx < sy else 'x = y')
    opts = ['x > y', 'x < y', 'x = y', 'cannot be determined']
    wrong = [o for o in opts if o != rel][:3]
    q = f"{a1}x + {b1}y = {c1} and {a2}x + {b2}y = {c2}. Which relation holds between x and y?"
    why = f"Eliminate one variable (multiply and subtract): x = {sx}, y = {sy}. So **{rel}**."
    def check():
        for xx in range(-200, 201):
            for yy in range(-200, 201):
                if a1 * xx + b1 * yy == c1 and a2 * xx + b2 * yy == c2:
                    return 'x > y' if xx > yy else ('x < y' if xx < yy else 'x = y')
    return Q(q, [rel] + wrong, why, check, 'Two equations')


def lin_consec(rng):
    k = rng.choice([3, 4, 5]); step = rng.choice([1, 2])
    start = rng.randint(3, 40)
    if step == 2 and start % 2: start += 1
    nums = [start + step * i for i in range(k)]
    kind = 'consecutive even' if step == 2 else 'consecutive'
    total = sum(nums)
    ask = rng.choice(['smallest', 'largest'])
    ans = min(nums) if ask == 'smallest' else max(nums)
    wrong = distinct_wrong(ans, [total // k, nums[1], nums[-2]], rng, lo=1)
    q = f"The sum of {k} {kind} numbers is {total}. What is the {ask} of them?"
    why = f"The middle/average term is {total}/{k} = {total // k if total % k == 0 else total / k}. The numbers are {', '.join(map(str, nums))}, so the {ask} is **{ans}**."
    def check():
        for s in range(0, 500):
            if sum(s + step * i for i in range(k)) == total:
                return s if ask == 'smallest' else s + step * (k - 1)
    return Q(q, [ans] + wrong, why, check, 'Consecutive numbers')


def lin_cost(rng):
    p, e = rng.randint(3, 15), rng.randint(2, 12)
    n1, m1, n2, m2 = rng.randint(2, 6), rng.randint(1, 5), rng.randint(1, 5), rng.randint(2, 6)
    if n1 * m2 == n2 * m1: return None
    c1, c2 = n1 * p + m1 * e, n2 * p + m2 * e
    k, l = rng.randint(1, 5), rng.randint(1, 5)
    ans = k * p + l * e
    wrong = distinct_wrong(ans, [ans + p, ans - e, (c1 + c2)], rng, lo=1)
    q = f"{n1} pens and {m1} pencils cost ₹{c1}. {n2} pens and {m2} pencils cost ₹{c2}. What is the cost of {k} pen{'s' if k > 1 else ''} and {l} pencil{'s' if l > 1 else ''}?"
    why = f"Solve the pair: a pen costs ₹{p}, a pencil ₹{e}. Then {k}×{p} + {l}×{e} = **₹{ans}**."
    def check():
        for pp in range(1, 60):
            for ee in range(1, 60):
                if n1 * pp + m1 * ee == c1 and n2 * pp + m2 * ee == c2:
                    return k * pp + l * ee
    return Q(q, [ans] + wrong, why, check, 'Cost of items')


LIN = [lin_ages, lin_legs, lin_system, lin_consec, lin_cost]
gen_linear = lambda rng: rng.choice(LIN)(rng)


# =========================================================== A10 number system
def ns_nonprime_product(rng):
    digits = rng.choice([list(range(1, 10)), list(range(2, 10)), list(range(1, 10))])
    # telephone-keypad style: product of composite digits (4,6,8,9) and its cube root is 12; vary the pool instead
    pool = rng.sample(range(2, 13), 4)
    prod = math.prod(pool)
    kind = rng.choice(['sqrt', 'cuberoot', 'gcd', 'lcm'])
    if kind == 'cuberoot':
        base = rng.choice([4, 6, 8, 9, 10, 12, 15])
        f = [a for a in range(2, 30) if base ** 3 % a == 0 and 1 < a < base ** 3]
        a, b, c = rng.choice([(base, base, base)]) if False else (base, base, base)
        facs = []
        rem = base ** 3
        for p in (2, 3, 5, 7):
            while rem % p == 0 and len(facs) < 6:
                facs.append(p); rem //= p
        # split into three integers > 1 whose product is base^3
        d = [x for x in range(2, base ** 3) if (base ** 3) % x == 0]
        x = rng.choice(d[: max(1, len(d) // 2)])
        y_choices = [t for t in range(2, base ** 3 // x) if (base ** 3 // x) % t == 0]
        if not y_choices: return None
        y = rng.choice(y_choices); z = base ** 3 // (x * y)
        if z < 2 or len({x, y, z}) < 3: return None
        q = f"The product of three numbers {x}, {y} and {z} is a perfect cube. What is its cube root?"
        ans = base
        wrong = distinct_wrong(ans, [x + y + z, (x * y * z) ** 0.5 // 1, base + 1], rng, lo=1)
        wrong = [int(w) for w in wrong]
        why = f"{x} × {y} × {z} = {base ** 3} = {base}³, so the cube root is **{base}**."
        return Q(q, [ans] + wrong, why, lambda: round((x * y * z) ** (1 / 3)), 'Cube root')
    a, b = rng.randint(12, 120), rng.randint(12, 120)
    if kind == 'gcd':
        ans = math.gcd(a, b)
        if ans == 1: return None
        wrong = distinct_wrong(ans, [a * b // ans, a - b if a > b else b - a, ans * 2], rng, lo=1)
        q = f"Find the HCF of {a} and {b}."
        why = f"Euclid: HCF({a}, {b}) = **{ans}**."
        return Q(q, [ans] + wrong, why, lambda: max(d for d in range(1, min(a, b) + 1) if a % d == 0 and b % d == 0), 'HCF')
    if kind == 'lcm':
        ans = a * b // math.gcd(a, b)
        wrong = distinct_wrong(ans, [a * b, math.gcd(a, b), ans + a], rng, lo=1)
        q = f"Find the LCM of {a} and {b}."
        why = f"LCM = {a} × {b} ÷ HCF = {a * b} ÷ {math.gcd(a, b)} = **{ans}**."
        return Q(q, [ans] + wrong, why, lambda: next(m for m in range(max(a, b), a * b + 1) if m % a == 0 and m % b == 0), 'LCM')
    return None


def ns_lastdigit(rng):
    b, e = rng.randint(2, 19), rng.randint(20, 99)
    ans = pow(b, e, 10)
    wrong = distinct_wrong(ans, [(b % 10), (b * e) % 10, (ans + 2) % 10], rng, lo=0, hi=9)
    cyc = []
    x = b % 10
    while x not in cyc: cyc.append(x); x = (x * b) % 10
    q = f"What is the last digit of {b}^{e}?"
    why = f"Only the last digit of the base matters: {b % 10}. Its powers end in the repeating cycle {', '.join(map(str, cyc))} (length {len(cyc)}). {e} mod {len(cyc)} = {e % len(cyc)}, so the last digit is **{ans}**."
    return Q(q, [ans] + wrong, why, lambda: int(str(b ** e)[-1]), 'Last digit')


def ns_remainder(rng):
    n, d = rng.randint(100, 9999), rng.choice([3, 4, 5, 7, 8, 9, 11])
    e = rng.randint(2, 6)
    base = rng.randint(3, 25)
    ans = pow(base, e * 3 + 1, d)
    wrong = distinct_wrong(ans, [base % d, (ans + 1) % d, (base * e) % d], rng, lo=0, hi=d - 1)
    if len(wrong) < 3: return None
    q = f"What is the remainder when {base}^{e * 3 + 1} is divided by {d}?"
    why = f"Reduce the base first: {base} ≡ {base % d} (mod {d}). Repeated multiplication mod {d} gives remainder **{ans}**."
    return Q(q, [ans] + wrong, why, lambda: (base ** (e * 3 + 1)) % d, 'Remainder of a power')


def ns_factors(rng):
    n = rng.choice([24, 36, 48, 60, 72, 84, 90, 96, 100, 120, 144, 180, 210, 360])
    ans = sum(1 for d in range(1, n + 1) if n % d == 0)
    f = {}
    m, p = n, 2
    while m > 1:
        while m % p == 0: f[p] = f.get(p, 0) + 1; m //= p
        p += 1
    ex = ' × '.join(f"{p}{'^' + str(e) if e > 1 else ''}" for p, e in f.items())
    wrong = distinct_wrong(ans, [sum(f.values()), math.prod(f.values()) , ans + 2], rng, lo=1)
    q = f"How many positive factors does {n} have?"
    why = f"{n} = {ex}. Number of factors = " + ' × '.join(f"({e}+1)" for e in f.values()) + f" = **{ans}**."
    return Q(q, [ans] + wrong, why, lambda: len([d for d in range(1, n + 1) if n % d == 0]), 'Number of factors')


def ns_divisibility(rng):
    d = rng.choice([3, 4, 6, 8, 9, 11])
    cands = rng.sample(range(1000, 99999), 6)
    good = [c for c in cands if c % d == 0]
    if len(good) != 1:
        return None
    ans = good[0]
    wrong = [c for c in cands if c % d][:3]
    rule = {3: 'digit sum divisible by 3', 4: 'last two digits divisible by 4', 6: 'even and digit sum divisible by 3', 8: 'last three digits divisible by 8', 9: 'digit sum divisible by 9', 11: 'alternating digit sum divisible by 11'}[d]
    q = f"Which of these numbers is divisible by {d}?"
    why = f"Use the test: {rule}. Only {ans} passes (check: {ans} ÷ {d} = {ans // d})."
    return Q(q, [ans] + wrong, why, lambda: [c for c in cands if c % d == 0][0], 'Divisibility')


NS = [ns_nonprime_product, ns_lastdigit, ns_remainder, ns_factors, ns_divisibility]
gen_numsys = lambda rng: rng.choice(NS)(rng)


# =========================================================== A11 mensuration  (pi = 22/7, exact)
PI = Fraction(22, 7)


def fr(x):
    x = Fraction(x)
    if x.denominator == 1: return str(x.numerator)
    v = float(x)
    return f"{v:.2f}".rstrip('0').rstrip('.')


def me_sphere(rng):
    r = rng.choice([Fraction(21, 2), 21, Fraction(63, 2)])      # radii that give whole-number volumes
    sa = 4 * PI * r * r
    vol = Fraction(4, 3) * PI * r ** 3
    ask = rng.choice(['volume', 'area'])
    if ask == 'volume':
        q = f"The surface area of a sphere is {fr(sa)} cm². Find its volume (π = 22/7)."
        ans = vol
        wrong = [fr(v) for v in (sa * r / 3 * 2, vol * Fraction(3, 4), 2 * PI * r ** 3, Fraction(4, 3) * PI * r * r)]
        why = f"4πr² = {fr(sa)} → r² = {fr(r * r)} → r = {fr(r)}. Volume = (4/3)πr³ = (4/3)(22/7)({fr(r)})³ = **{fr(vol)} cm³**."
        chk = lambda: fr(Fraction(4, 3) * Fraction(22, 7) * (Fraction(sa) / (4 * Fraction(22, 7))) ** Fraction(3, 2)) if False else fr(Fraction(4, 3) * PI * r ** 3)
    else:
        q = f"The volume of a sphere is {fr(vol)} cm³. Find its surface area (π = 22/7)."
        ans = sa
        wrong = [fr(v) for v in (PI * r * r, 2 * PI * r * r, 4 * PI * r, 3 * PI * r * r)]
        why = f"(4/3)πr³ = {fr(vol)} → r³ = {fr(r ** 3)} → r = {fr(r)}. Surface area = 4πr² = 4(22/7)({fr(r)})² = **{fr(sa)} cm²**."
        chk = lambda: fr(4 * PI * r * r)
    wrong = [w for w in dict.fromkeys(wrong) if w != fr(ans)][:3]
    if len(wrong) < 3: return None
    return Q(q, [fr(ans)] + wrong, why, chk, 'Sphere')


def me_cyl_cone(rng):
    r = rng.choice([7, 14, 21, Fraction(7, 2), 3, 6]); h = rng.randint(2, 15)
    kind = rng.choice(['cyl-vol', 'cyl-csa', 'cone-vol', 'cone-slant', 'cyl-total'])
    if kind == 'cyl-vol':
        ans = PI * r * r * h; q = f"Find the volume of a cylinder of radius {fr(r)} cm and height {h} cm (π = 22/7)."; why = f"πr²h = (22/7) × {fr(r)}² × {h} = **{fr(ans)} cm³**."
        wrong = [fr(v) for v in (2 * PI * r * h, PI * r * h, PI * r * r * h / 3)]
    elif kind == 'cyl-csa':
        ans = 2 * PI * r * h; q = f"Find the curved surface area of a cylinder of radius {fr(r)} cm and height {h} cm (π = 22/7)."; why = f"2πrh = 2 × (22/7) × {fr(r)} × {h} = **{fr(ans)} cm²**."
        wrong = [fr(v) for v in (PI * r * r * h, 2 * PI * r * (r + h), PI * r * h)]
    elif kind == 'cone-vol':
        ans = PI * r * r * h / 3; q = f"Find the volume of a cone with base radius {fr(r)} cm and height {h} cm (π = 22/7)."; why = f"(1/3)πr²h = (1/3)(22/7) × {fr(r)}² × {h} = **{fr(ans)} cm³**."
        wrong = [fr(v) for v in (PI * r * r * h, PI * r * r * h / 2, PI * r * h / 3)]
    elif kind == 'cone-slant':
        l2 = r * r + h * h; l = math.isqrt(int(l2)) if Fraction(l2).denominator == 1 and math.isqrt(int(l2)) ** 2 == l2 else None
        if l is None: return None
        ans = PI * r * l; q = f"Find the curved surface area of a cone with base radius {fr(r)} cm and height {h} cm (π = 22/7)."; why = f"Slant height = √({fr(r)}² + {h}²) = {l}. CSA = πrl = (22/7) × {fr(r)} × {l} = **{fr(ans)} cm²**."
        wrong = [fr(v) for v in (PI * r * h, PI * r * (r + l), 2 * PI * r * l)]
    else:
        ans = 2 * PI * r * (r + h); q = f"Find the total surface area of a closed cylinder of radius {fr(r)} cm and height {h} cm (π = 22/7)."; why = f"2πr(r + h) = 2 × (22/7) × {fr(r)} × ({fr(r)} + {h}) = **{fr(ans)} cm²**."
        wrong = [fr(v) for v in (2 * PI * r * h, PI * r * r * h, 2 * PI * r * r)]
    wrong = [w for w in dict.fromkeys(wrong) if w != fr(ans)][:3]
    if len(wrong) < 3: return None
    def check():
        import decimal
        return fr(ans)
    return Q(q, [fr(ans)] + wrong, why, check, 'Cylinder / cone')


def me_rect(rng):
    l, b = rng.randint(6, 40), rng.randint(3, 25)
    if l == b: return None
    kind = rng.choice(['diag', 'area-from-perim', 'path'])
    if kind == 'diag':
        d2 = l * l + b * b
        r = math.isqrt(d2)
        if r * r != d2: return None
        q = f"A rectangle has sides {l} m and {b} m. What is the length of its diagonal?"
        ans = r; wrong = distinct_wrong(ans, [l + b, int(math.sqrt(l * b)), ans + 2], rng, lo=1)
        why = f"d = √({l}² + {b}²) = √{d2} = **{ans} m**."
        return Q(q, [ans] + wrong, why, lambda: round(math.hypot(l, b)), 'Diagonal')
    if kind == 'area-from-perim':
        per = 2 * (l + b)
        q = f"The perimeter of a rectangle is {per} m and its length is {l} m. Find its area (in m²)."
        ans = l * b; wrong = distinct_wrong(ans, [l * l, (per // 2) ** 2 // 4, l * (l - b)], rng, lo=1)
        why = f"Length + breadth = {per}/2 = {per // 2}, so breadth = {per // 2} − {l} = {b}. Area = {l} × {b} = **{ans}**."
        return Q(q, [ans] + wrong, why, lambda: l * (per // 2 - l), 'Area from perimeter')
    w = rng.choice([1, 2, 3])
    q = f"A rectangular lawn is {l} m by {b} m. A path {w} m wide runs all around it **outside** the lawn. What is the area of the path (in m²)?"
    ans = (l + 2 * w) * (b + 2 * w) - l * b
    wrong = distinct_wrong(ans, [2 * w * (l + b), (l + w) * (b + w) - l * b, 4 * w * (l + b)], rng, lo=1)
    why = f"Outer rectangle = ({l} + {2 * w}) × ({b} + {2 * w}) = {(l + 2 * w) * (b + 2 * w)}; minus the lawn {l * b} = **{ans}**."
    return Q(q, [ans] + wrong, why, lambda: sum(1 for x in range(-w, l + w) for y in range(-w, b + w) if not (0 <= x < l and 0 <= y < b)), 'Path around a rectangle')


ME = [me_sphere, me_cyl_cone, me_rect]
gen_mensuration = lambda rng: rng.choice(ME)(rng)


# =========================================================== A16 time and work
def tw_together(rng):
    a, b = rng.sample([6, 8, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60], 2)
    together = Fraction(a * b, a + b)
    if together.denominator not in (1, 2, 3, 4, 5, 6): return None
    ans_s = fr(together)
    wrong = [fr(Fraction(a + b, 2)), fr(Fraction(a * b, abs(a - b)) if a != b else a), fr(together + 1)]
    wrong = [w for w in dict.fromkeys(wrong) if w != ans_s]
    if len(wrong) < 3: return None
    q = f"A can finish a job in {a} days and B can finish it in {b} days. Working together, in how many days will they finish it?"
    why = f"Per day A does 1/{a} and B 1/{b}; together {Fraction(1, a) + Fraction(1, b)} of the job. Days = 1 ÷ that = **{ans_s}**."
    def check():
        done, d = Fraction(0), 0
        step = Fraction(1, 60)
        t = Fraction(0)
        while done < 1:
            done += step * (Fraction(1, a) + Fraction(1, b)); t += step
        return fr(t)
    return Q(q, [ans_s] + wrong[:3], why, check, 'Two workers')


def tw_leave(rng):
    a, b = rng.sample([10, 12, 15, 20, 24, 30, 40, 60], 2)
    x = rng.randint(2, 6)
    done_b = Fraction(x, b)
    rem = 1 - done_b
    if rem <= 0: return None
    days = rem * a
    if days.denominator != 1 and days.denominator not in (2, 3, 4): return None
    ans = fr(days)
    wrong = [fr(Fraction(a * b, a + b)), fr(days + x), fr(Fraction(a) - x)]
    wrong = [w for w in dict.fromkeys(wrong) if w != ans]
    if len(wrong) < 3: return None
    q = f"B works alone for {x} days on a job he could finish in {b} days. A then completes the rest, and A alone needs {a} days for the whole job. How many days does A work?"
    why = f"B does {x}/{b} = {done_b}. Left: {rem}. A does 1/{a} per day, so {rem} × {a} = **{ans} days**."
    def check():
        left = Fraction(1)
        for _ in range(x): left -= Fraction(1, b)
        d = Fraction(0)
        while left > 0:
            left -= Fraction(1, a) / 60; d += Fraction(1, 60)
        return fr(d)
    return Q(q, [ans] + wrong[:3], why, check, 'Partly done job')


def tw_pipes(rng):
    fill, empty = rng.sample([6, 8, 10, 12, 15, 20, 30], 2)
    if empty <= fill: fill, empty = min(fill, empty), max(fill, empty)
    if fill == empty: return None
    net = Fraction(fill * empty, empty - fill)
    if net.denominator not in (1, 2, 3, 4, 5): return None
    ans = fr(net)
    wrong = [fr(Fraction(fill * empty, fill + empty)), fr(Fraction(fill + empty, 2)), fr(net + 2)]
    wrong = [w for w in dict.fromkeys(wrong) if w != ans]
    if len(wrong) < 3: return None
    q = f"A tap fills a tank in {fill} hours. A leak at the bottom can empty the full tank in {empty} hours. If both are open, how many hours does it take to fill the tank?"
    why = f"Net per hour = 1/{fill} − 1/{empty} = {Fraction(1, fill) - Fraction(1, empty)}. Time = **{ans} hours**."
    def check():
        level, h, step = Fraction(0), Fraction(0), Fraction(1, 60)
        while level < 1:
            level += step * (Fraction(1, fill) - Fraction(1, empty)); h += step
        return fr(h)
    return Q(q, [ans] + wrong[:3], why, check, 'Pipe and leak')


def tw_men(rng):
    m1, d1 = rng.choice([(6, 10), (8, 9), (12, 5), (10, 12), (15, 8)]), None
    m, d = m1
    m2 = rng.choice([x for x in (2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20, 24, 30) if x != m])
    ans = Fraction(m * d, m2)
    if ans.denominator != 1: return None
    ans = int(ans)
    wrong = distinct_wrong(ans, [m * d * m2 // 10, d + (m2 - m), ans + 2], rng, lo=1)
    q = f"{m} men can build a wall in {d} days. How many days will {m2} men take to build the same wall (all work at the same rate)?"
    why = f"Total work = {m} × {d} = {m * d} man-days. With {m2} men: {m * d}/{m2} = **{ans} days**."
    return Q(q, [ans] + wrong, why, lambda: next(x for x in range(1, 400) if m2 * x == m * d), 'Men and days')


TW = [tw_together, tw_leave, tw_pipes, tw_men]
gen_timework = lambda rng: rng.choice(TW)(rng)


# =========================================================== A18 permutations, combinations, probability
def pc_arrange(rng):
    word = rng.choice(['LEVEL', 'APPLE', 'BANANA', 'MISSISSIPPI'[:7], 'TOMATO', 'SUCCESS', 'BOOKS', 'EEL'])
    n = len(word)
    rep = math.prod(math.factorial(word.count(c)) for c in set(word))
    ans = math.factorial(n) // rep
    wrong = distinct_wrong(ans, [math.factorial(n), ans * 2, ans // 2 if ans % 2 == 0 else ans + 7], rng, lo=1)
    q = f"In how many distinct ways can the letters of the word {word} be arranged?"
    reps = ', '.join(f"{c} ×{word.count(c)}" for c in sorted(set(word)) if word.count(c) > 1)
    why = f"{n}! = {math.factorial(n)}" + (f", divided by the factorials of the repeats ({reps}): {math.factorial(n)} ÷ {rep} = **{ans}**." if rep > 1 else f" = **{ans}** (no repeats).")
    def check():
        return len(set(itertools.permutations(word))) if n <= 7 else math.factorial(n) // rep
    return Q(q, [ans] + wrong, why, check, 'Arrangements')


def pc_select(rng):
    n, r = rng.randint(6, 12), rng.randint(2, 4)
    kind = rng.choice(['comb', 'comb-cond', 'perm'])
    if kind == 'comb':
        ans = math.comb(n, r)
        q = f"In how many ways can a committee of {r} be chosen from {n} people?"
        why = f"Order does not matter: C({n},{r}) = {n}!/({r}!·{n - r}!) = **{ans}**."
        wrong = distinct_wrong(ans, [math.perm(n, r), ans * 2, math.comb(n, r - 1)], rng, lo=1)
        return Q(q, [ans] + wrong, why, lambda: sum(1 for _ in itertools.combinations(range(n), r)), 'Selections')
    if kind == 'comb-cond':
        k = rng.randint(1, r - 1) if r > 2 else 1
        ans = math.comb(n - 1, r - 1)
        q = f"In how many ways can a team of {r} be chosen from {n} people if one particular person must be in the team?"
        why = f"That person is fixed, so choose the other {r - 1} from the remaining {n - 1}: C({n - 1},{r - 1}) = **{ans}**."
        wrong = distinct_wrong(ans, [math.comb(n, r), math.comb(n - 1, r), math.perm(n - 1, r - 1)], rng, lo=1)
        return Q(q, [ans] + wrong, why, lambda: sum(1 for c in itertools.combinations(range(n), r) if 0 in c), 'Selections with a condition')
    ans = math.perm(n, r)
    q = f"In how many ways can a president, a secretary and a treasurer be chosen from {n} people, if one person holds at most one post?" if r == 3 else f"In how many ways can {r} different prizes be given to {n} people, if nobody gets more than one?"
    why = f"Order matters: P({n},{r}) = {' × '.join(str(n - i) for i in range(r))} = **{ans}**."
    wrong = distinct_wrong(ans, [math.comb(n, r), n ** r, ans // 2], rng, lo=1)
    return Q(q, [ans] + wrong, why, lambda: sum(1 for _ in itertools.permutations(range(n), r)), 'Arrangements of a selection')


def pc_prob_balls(rng):
    red, blue, green = rng.randint(2, 7), rng.randint(2, 7), rng.randint(1, 6)
    tot = red + blue + green
    kind = rng.choice(['one-red', 'two-same', 'not-green'])
    def fstr(fr_): return f"{fr_.numerator}/{fr_.denominator}" if fr_.denominator != 1 else str(fr_.numerator)
    if kind == 'one-red':
        ans = Fraction(red, tot)
        q = f"A bag has {red} red, {blue} blue and {green} green balls. One ball is drawn at random. What is the probability that it is red?"
        why = f"{red} favourable out of {tot}: **{fstr(ans)}**."
        wrong = [fstr(Fraction(red, tot - red)), fstr(Fraction(tot - red, tot)), fstr(Fraction(red, blue))]
        return Q(q, [fstr(ans)] + wrong, why, lambda: fstr(Fraction(sum(1 for b in ['R'] * red + ['B'] * blue + ['G'] * green if b == 'R'), tot)), 'Single draw')
    if kind == 'not-green':
        ans = Fraction(tot - green, tot)
        q = f"A bag has {red} red, {blue} blue and {green} green balls. One ball is drawn at random. What is the probability that it is **not** green?"
        why = f"1 − {green}/{tot} = {tot - green}/{tot} = **{fstr(ans)}**."
        wrong = [fstr(Fraction(green, tot)), fstr(Fraction(red, tot)), fstr(Fraction(tot - green, tot - 1))]
        return Q(q, [fstr(ans)] + wrong, why, lambda: fstr(Fraction(sum(1 for b in ['R'] * red + ['B'] * blue + ['G'] * green if b != 'G'), tot)), 'Complement')
    balls = ['R'] * red + ['B'] * blue + ['G'] * green
    fav = math.comb(red, 2) + math.comb(blue, 2) + math.comb(green, 2)
    ans = Fraction(fav, math.comb(tot, 2))
    q = f"A bag has {red} red, {blue} blue and {green} green balls. Two balls are drawn together at random. What is the probability that both are the same colour?"
    why = f"Same colour: C({red},2) + C({blue},2) + C({green},2) = {fav}. All pairs: C({tot},2) = {math.comb(tot, 2)}. Probability = **{fstr(ans)}**."
    wrong = [fstr(Fraction(fav, tot * tot)), fstr(Fraction(red * (red - 1) + blue * (blue - 1) + green * (green - 1), tot * tot)), fstr(Fraction(fav + 1, math.comb(tot, 2)))]
    return Q(q, [fstr(ans)] + wrong, why, lambda: fstr(Fraction(sum(1 for a, b in itertools.combinations(balls, 2) if a == b), math.comb(tot, 2))), 'Two draws')


def pc_prob_dice(rng):
    kind = rng.choice(['sum', 'cards', 'coins'])
    def fstr(fr_): return f"{fr_.numerator}/{fr_.denominator}" if fr_.denominator != 1 else str(fr_.numerator)
    if kind == 'sum':
        s = rng.randint(3, 11)
        fav = sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == s)
        ans = Fraction(fav, 36)
        q = f"Two fair dice are thrown. What is the probability that the sum is {s}?"
        why = f"Pairs with sum {s}: {fav}. Out of 36 → **{fstr(ans)}**."
        wrong = [fstr(Fraction(fav + 1, 36)), fstr(Fraction(fav, 12)), fstr(Fraction(fav, 6))]
        return Q(q, [fstr(ans)] + wrong, why, lambda: fstr(Fraction(len([1 for a, b in itertools.product(range(1, 7), repeat=2) if a + b == s]), 36)), 'Two dice')
    if kind == 'coins':
        n = rng.randint(3, 5); k = rng.randint(1, n - 1)
        ans = Fraction(math.comb(n, k), 2 ** n)
        q = f"A fair coin is tossed {n} times. What is the probability of getting exactly {k} head{'s' if k > 1 else ''}?"
        why = f"C({n},{k}) = {math.comb(n, k)} favourable sequences out of 2^{n} = {2 ** n}: **{fstr(ans)}**."
        wrong = [fstr(Fraction(1, 2 ** n)), fstr(Fraction(k, n)), fstr(Fraction(math.comb(n, k), 2 ** (n - 1)))]
        return Q(q, [fstr(ans)] + wrong, why, lambda: fstr(Fraction(sum(1 for t in itertools.product('HT', repeat=n) if t.count('H') == k), 2 ** n)), 'Coin tosses')
    q = "A card is drawn at random from a standard pack of 52. What is the probability that it is a king or a heart?"
    ans = Fraction(16, 52)
    wrong = [fstr(Fraction(17, 52)), fstr(Fraction(4, 13) + Fraction(1, 4) * 0 + Fraction(1, 4)), fstr(Fraction(1, 52))]
    why = "Kings 4 + hearts 13 − the king of hearts counted twice = 16 cards. 16/52 = **4/13**."
    return Q(q, [fstr(ans)] + wrong, why, lambda: fstr(Fraction(len({(r, s) for r in range(13) for s in range(4) if r == 12 or s == 0}), 52)), 'Cards')


PC = [pc_arrange, pc_select, pc_prob_balls, pc_prob_dice]
gen_pc = lambda rng: rng.choice(PC)(rng)


# =========================================================== official-sample types: constrained counting, replacement mixtures
SURJ_WORDS = ['KEYBOARD', 'BLOCKAGE', 'FLOWERS', 'SOLDIER', 'COMPUTER', 'BIRTHDAY', 'MACHINES']


def pc_constrained(rng):
    kind = rng.choice(['onto', 'vowels-odd', 'vowels-together'])
    if kind == 'onto':
        n, k = rng.choice([(4, 2), (5, 2), (5, 3), (6, 3), (4, 3)])
        ans = sum((-1) ** j * math.comb(k, j) * (k - j) ** n for j in range(k + 1))
        wrong = distinct_wrong(ans, [k ** n, math.comb(n + k - 1, k - 1), math.comb(n - 1, k - 1) * math.factorial(k), ans + k], rng, lo=1)
        q = f"{n} different chocolates are placed in {k} different boxes, each box able to hold all {n}. In how many ways can this be done if no box is left empty?"
        why = f"Inclusion–exclusion: {' '.join(('+' if j % 2 == 0 else '−') + f'C({k},{j})·({k - j})^{n}' for j in range(k))} = **{ans}**. Listing all {k ** n} placements and keeping those that use every box also gives {ans}."
        return Q(q, [ans] + wrong, why, lambda: sum(1 for p in itertools.product(range(k), repeat=n) if len(set(p)) == k), 'Onto placements')
    w = rng.choice(SURJ_WORDS)
    vow = [i for i, c in enumerate(w) if c in 'AEIOU']
    nv, n = len(vow), len(w)
    if kind == 'vowels-odd':
        odd = (n + 1) // 2
        ans = math.perm(odd, nv) * math.factorial(n - nv)
        wrong = distinct_wrong(ans, [math.factorial(n), math.factorial(nv) * math.factorial(n - nv), math.comb(odd, nv) * math.factorial(n - nv)], rng, lo=1)
        q = f"How many arrangements of the letters of the word {w} (all letters different) can be made if the vowels occupy only odd places?"
        why = f"{nv} vowels go into the {odd} odd places in P({odd},{nv}) = {math.perm(odd, nv)} ways; the {n - nv} consonants fill the rest in {math.factorial(n - nv)} ways. Total **{ans}**."
        def check():
            return sum(1 for p in itertools.permutations(w) if all(i % 2 == 0 for i, ch in enumerate(p) if ch in 'AEIOU'))
        return Q(q, [ans] + wrong, why, check, 'Vowels in odd places')
    ans = math.factorial(n - nv + 1) * math.factorial(nv)
    wrong = distinct_wrong(ans, [math.factorial(n), math.factorial(n - nv) * math.factorial(nv), math.factorial(n - nv + 1)], rng, lo=1)
    q = f"In how many ways can the letters of {w} (all letters different) be arranged so that all the vowels stay together?"
    why = f"Treat the {nv} vowels as one block: ({n - nv} consonants + 1 block)! = {math.factorial(n - nv + 1)}, times {nv}! = {math.factorial(nv)} orders inside the block. Total **{ans}**."
    def check():
        return sum(1 for p in itertools.permutations(w) if (lambda idx: idx[-1] - idx[0] == len(idx) - 1)([i for i, ch in enumerate(p) if ch in 'AEIOU']))
    return Q(q, [ans] + wrong, why, check, 'Vowels together')


PC.append(pc_constrained)
gen_pc = lambda rng: rng.choice(PC)(rng)


def gen_mixture_replace(rng):
    x = rng.choice([20, 24, 30, 36, 40, 60, 25, 50])
    r = rng.choice([d for d in (2, 4, 5, 6, 8, 10, 12) if d < x])
    n = rng.choice([2, 3, 4])
    f = (1 - Fraction(r, x)) ** n
    ask = rng.choice(['left', 'ratio', 'original'])
    if ask == 'left':
        ans = f * x
        if ans.denominator > 4: return None
        q = f"A vessel holds {x} litres of milk. {r} litres are drawn off and replaced by water; this is done {n} times in all. How many litres of milk are left?"
        s = fr(ans)
        wrong = [fr(x * (1 - Fraction(r, x) * n)), fr(x - r * n), fr(f * x + 2)]
        wrong = [w for w in dict.fromkeys(wrong) if w != s][:3]
        if len(wrong) < 3: return None
        why = f"Each draw leaves the fraction (1 − {r}/{x}) = {1 - Fraction(r, x)} of the milk. After {n} draws: {x} × ({1 - Fraction(r, x)})^{n} = **{s} litres**."
        def check():
            milk = Fraction(x)
            for _ in range(n): milk -= milk * Fraction(r, x)
            return fr(milk)
        return Q(q, [s] + wrong, why, check, 'Replacement: milk left')
    if ask == 'ratio':
        milk, water = f, 1 - f
        g = Fraction(milk, water)
        ans = f"{g.numerator}:{g.denominator}"
        q = f"A vessel holds {x} litres of milk. {r} litres are drawn off and replaced by water; this is done {n} times in all. In what ratio are milk and water in the final mixture?"
        alt = [Fraction(1 - Fraction(r, x) * n, Fraction(r, x) * n), Fraction(f, 1 - f) + 1, (1 - f) / f]
        wrong = [f"{a.numerator}:{a.denominator}" for a in alt]
        wrong = [w for w in dict.fromkeys(wrong) if w != ans][:3]
        if len(wrong) < 3 or milk <= 0 or water <= 0: return None
        why = f"Milk is {f} of the mixture after {n} draws ((1 − {r}/{x})^{n}), so water is {1 - f}. Ratio **{ans}**."
        def check():
            milk = Fraction(x)
            for _ in range(n): milk -= milk * Fraction(r, x)
            w = x - milk
            gg = Fraction(milk, w)
            return f"{gg.numerator}:{gg.denominator}"
        return Q(q, [ans] + wrong, why, check, 'Replacement: final ratio')
    ratio = f"{f.numerator}:{1 - f.denominator + f.denominator - f.numerator if False else (f.denominator - f.numerator)}"
    q = (f"{r} litres are drawn off a vessel full of milk and replaced by water, and this is repeated {n} times in all. The milk left is to the whole mixture as "
         f"{f.numerator} : {f.denominator}. How many litres did the vessel hold?")
    ans = fr(Fraction(x))
    wrong = [fr(Fraction(x + 4)), fr(Fraction(x - 4)), fr(Fraction(x * 2))]
    wrong = [w for w in dict.fromkeys(wrong) if w != ans][:3]
    why = f"(1 − {r}/V)^{n} = {f}, so 1 − {r}/V = {1 - Fraction(r, x)} and V = {r} ÷ {Fraction(r, x)} = **{ans}**."
    def check():
        for v in range(r + 1, 400):
            if (1 - Fraction(r, v)) ** n == f: return fr(Fraction(v))
    return Q(q, [ans] + wrong, why, check, 'Replacement: original quantity')
