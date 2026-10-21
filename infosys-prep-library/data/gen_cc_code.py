"""Bitwise-operator and array questions for the Core Course (lessons P3 and P5).

Each question prints a short program in the official dialect (numbered lines). Three routes agree on the answer:
  route 1: Python evaluates the same expression (or runs a Python mirror of the program);
  route 2 (the check()): an independent method (an explicit-precedence parser for bitwise questions, a different formulation for arrays);
  route 3: verify_core_course.py translates the PRINTED lines to Java and runs them (q['jcode'] holds those lines)."""
import re

from gen_core import Q, distinct_wrong

PREC = {'*': 5, '+': 4, '<<': 3, '>>': 3, '&': 2, '^': 1, '|': 0}          # Java: higher binds tighter
APPLY = {'*': lambda x, y: x * y, '+': lambda x, y: x + y, '<<': lambda x, y: x << y, '>>': lambda x, y: x >> y,
         '&': lambda x, y: x & y, '^': lambda x, y: x ^ y, '|': lambda x, y: x | y}


def numbered(lines):
    return [f"{i}) {l}" for i, l in enumerate(lines, 1)]


def eval_by_precedence(tokens):
    """Route 2: shunting-yard with the precedence table above. tokens: ints and operator strings, left to right."""
    out, ops = [], []

    def pop():
        op = ops.pop(); y = out.pop(); x = out.pop(); out.append(APPLY[op](x, y))
    for t in tokens:
        if isinstance(t, int):
            out.append(t)
        else:
            while ops and PREC[ops[-1]] >= PREC[t]:
                pop()
            ops.append(t)
    while ops:
        pop()
    return out[0]


def eval_left_to_right(tokens):
    acc = tokens[0]
    for i in range(1, len(tokens), 2):
        acc = APPLY[tokens[i]](acc, tokens[i + 1])
    return acc


def gen_bitwise(rng, lvl=1):
    names = ['a', 'b', 'c']
    vals = {n: rng.randint(2, 31) for n in names}
    n_ops = {1: 1, 2: 2, 3: rng.choice([3, 3, 4])}[lvl]
    pool = {1: ['&', '|', '^', '<<', '>>'], 2: ['&', '|', '^', '+', '<<'], 3: ['&', '|', '^', '+', '<<', '>>', '*']}[lvl]
    ops = [rng.choice(pool) for _ in range(n_ops)]
    if lvl >= 2 and len({PREC[o] for o in ops}) < 2:
        return None                                          # want at least two different precedence levels
    operands, shown = [], []
    for i in range(n_ops + 1):
        if i > 0 and ops[i - 1] in ('<<', '>>'):
            v = rng.randint(1, 3); operands.append(v); shown.append(str(v))
        elif rng.random() < 0.25:
            v = rng.randint(1, 15); operands.append(v); shown.append(str(v))
        else:
            n = rng.choice(names); operands.append(vals[n]); shown.append(n)
    expr = ' '.join(x for pair in zip(shown, ops + ['']) for x in pair).strip()
    tokens = []
    for i, v in enumerate(operands):
        tokens.append(v)
        if i < n_ops: tokens.append(ops[i])
    ans = eval(' '.join(str(t) for t in tokens))               # route 1: Python (same precedence as Java for these operators)
    naive = eval_left_to_right(tokens)
    if ans > 4000 or (lvl >= 2 and (naive == ans or ans == 0)):
        return None
    wrong = distinct_wrong(ans, [naive, ans ^ 1, ans + 2, ans - 2, ans * 2 if ans * 2 < 4000 else ans + 5], rng, lo=0)
    lines = ["Integer a, b, c", f"Set a = {vals['a']}, b = {vals['b']}, c = {vals['c']}"]
    if lvl == 3:
        lines += [f"Set a = {expr}", "Print a"]
    else:
        lines += [f"Print {expr}"]
    code = numbered(lines)
    q = ("What does this program print? (`&` is bitwise AND, `|` is bitwise OR, `^` is bitwise XOR, `<<` and `>>` shift the bits left and right. "
         "Arithmetic is done before shifts, shifts before `&`, `&` before `^`, and `^` before `|`.)\n\n```text\n" + '\n'.join(code) + "\n```\n")
    bits = lambda n: format(n, 'b')
    if lvl == 1:
        why = f"{operands[0]} is {bits(operands[0])} in binary and {operands[1]} is {bits(operands[1])}. Applying {ops[0]} bit by bit gives {bits(ans)}, which is **{ans}**."
    else:
        why = (f"Work out the operator that binds tightest first (order: `*` and `+`, then `<<` `>>`, then `&`, then `^`, then `|`). "
               f"With the values filled in the expression is `{' '.join(str(t) for t in tokens)}`, and the result is **{ans}**. "
               f"(Reading it left to right would wrongly give {naive}.)")
    qd = Q(q, [ans] + wrong, why, lambda: eval_by_precedence(tokens), tag='Bitwise operators')
    qd['jcode'] = code
    qd['steps'] = n_ops + (1 if lvl == 3 else 0)
    return qd


# ======================================================================= arrays
def _data(rng, n, lo=1, hi=9):
    return [rng.randint(lo, hi) for _ in range(n)]


VARS = {'sum': 'i, s', 'max': 'i, m', 'count_gt': 'i, c', 'even_index': 'i, s', 'reverse': 'i', 'prefix': 'i', 'swap_pairs': 'i, t',
        'longest_run': 'i, cur, best', 'product_except': 'i, total'}


def _decl(n, a, kind):
    return [f"Integer a[{n}], {VARS[kind]}", "Set " + ', '.join(f"a[{k}] = {v}" for k, v in enumerate(a))]


ARR_Q = "What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)\n\n```text\n%s\n```\n"


def _arr(rng, lines, expect, check, why, level, steps, tag):
    code = numbered(lines)
    out = ' '.join(map(str, expect))
    cands = []
    if len(expect) == 1:
        cands = [expect[0] + 1, expect[0] - 1, expect[0] + 2, expect[0] * 2]
    else:
        cands = [' '.join(map(str, expect[::-1])), ' '.join(map(str, expect[1:] + expect[:1])), ' '.join(map(str, [expect[0] + 1] + expect[1:])), ' '.join(map(str, expect[:-1] + [expect[-1] + 1]))]
    wrong = []
    for c in cands:
        c = str(c)
        if c != out and c not in wrong:
            wrong.append(c)
    if len(wrong) < 3:
        return None
    qd = Q(ARR_Q % '\n'.join(code), [out] + wrong[:3], why, check, tag)
    qd['jcode'] = code
    qd['steps'] = steps
    return qd


def gen_array(rng, kind):
    n = rng.choice([5, 6]) if kind not in ('longest_run', 'product_except') else (7 if kind == 'longest_run' else 4)
    if kind == 'product_except':
        a = [rng.randint(2, 5) for _ in range(n)]
    elif kind == 'longest_run':
        a = [rng.randint(1, 6) for _ in range(n)]
    else:
        a = _data(rng, n)
    d = _decl(n, a, kind)
    last = n - 1
    if kind == 'sum':
        lines = d + ["Set s = 0", f"For (each i from 0 to {last})", "  s = s + a[i]", "End-for", "Print s"]
        exp = [sum(a)]
        return _arr(rng, lines, exp, lambda: sum(a), f"Add every element: {' + '.join(map(str, a))} = **{sum(a)}**.", 1, 2, 'Array sum')
    if kind == 'max':
        lines = d + ["Set m = a[0]", f"For (each i from 1 to {last})", "  If (a[i] > m) then", "    m = a[i]", "  End-if", "End-for", "Print m"]
        return _arr(rng, lines, [max(a)], lambda: sorted(a)[-1], f"Keep the largest seen so far while walking along {a}: **{max(a)}**.", 1, 3, 'Array maximum')
    if kind == 'count_gt':
        k = rng.randint(3, 6)
        lines = d + ["Set c = 0", f"For (each i from 0 to {last})", f"  If (a[i] > {k}) then", "    c++", "  End-if", "End-for", "Print c"]
        return _arr(rng, lines, [sum(1 for x in a if x > k)], lambda: len([x for x in a if x > k]), f"Count the elements greater than {k} in {a}: **{sum(1 for x in a if x > k)}**.", 1, 3, 'Array count')
    if kind == 'even_index':
        lines = d + ["Set s = 0", f"For (each i from 0 to {last} step 2)", "  s = s + a[i]", "End-for", "Print s"]
        e = [a[i] for i in range(0, n, 2)]
        return _arr(rng, lines, [sum(e)], lambda: sum(a[0::2]), f"`step 2` visits positions 0, 2, 4…: {e} adds to **{sum(e)}**.", 2, 3, 'Array every second')
    if kind == 'reverse':
        lines = d + [f"For (each i from {last} to 0 step -1)", "  Print a[i]", "End-for"]
        return _arr(rng, lines, a[::-1], lambda: ' '.join(map(str, list(reversed(a)))), f"The loop counts down from index {last} to 0, so the array is printed backwards: **{' '.join(map(str, a[::-1]))}**.", 2, 3, 'Array backwards')
    if kind == 'prefix':
        lines = d + [f"For (each i from 1 to {last})", "  a[i] = a[i] + a[i - 1]", "End-for", "Print a[%d]" % last]
        return _arr(rng, lines, [sum(a)], lambda: sum(a), f"Each element becomes the running total, so the last one is the sum of all: {' + '.join(map(str, a))} = **{sum(a)}**.", 2, 4, 'Running totals')
    if kind == 'swap_pairs':
        lines = d + [f"For (each i from 0 to {n - 2} step 2)", "  t = a[i]", "  a[i] = a[i + 1]", "  a[i + 1] = t", "End-for", f"For (each i from 0 to {last})", "  Print a[i]", "End-for"]
        b = a[:]
        for i in range(0, n - 1, 2): b[i], b[i + 1] = b[i + 1], b[i]
        return _arr(rng, lines, b, lambda: ' '.join(map(str, [a[i ^ 1] if (i ^ 1) < n else a[i] for i in range(n)])),
                    f"Each neighbouring pair swaps places: {a} becomes **{' '.join(map(str, b))}**.", 3, 5, 'Swapping pairs')
    if kind == 'longest_run':
        lines = d + ["Set cur = 1", "Set best = 1", f"For (each i from 1 to {last})", "  If (a[i] > a[i - 1]) then", "    cur++", "    If (cur > best) then", "      best = cur", "    End-if", "  Else", "    cur = 1", "  End-if", "End-for", "Print best"]
        best = cur = 1
        for i in range(1, n):
            cur = cur + 1 if a[i] > a[i - 1] else 1
            best = max(best, cur)
        import itertools
        alt = max(len(list(g)) for k, g in itertools.groupby(range(1, n), key=lambda i: a[i] > a[i - 1]) if k) + 1 if any(a[i] > a[i - 1] for i in range(1, n)) else 1
        return _arr(rng, lines, [best], lambda: alt, f"`cur` counts how long the strictly rising run is and `best` remembers the longest. For {a} the longest rising run has **{best}** elements.", 3, 6, 'Longest rising run')
    if kind == 'product_except':
        lines = d + ["Set total = 1", f"For (each i from 0 to {last})", "  total = total * a[i]", "End-for", f"For (each i from 0 to {last})", "  Print total / a[i]", "End-for"]
        tot = 1
        for x in a: tot *= x
        res = [tot // x for x in a]
        import math
        return _arr(rng, lines, res, lambda: ' '.join(str(math.prod(a[:j] + a[j + 1:])) for j in range(n)),
                    f"The product of all four is {tot}. Dividing by each element leaves the product of the others: **{' '.join(map(str, res))}**.", 3, 6, 'Product of the others')
    raise ValueError(kind)
