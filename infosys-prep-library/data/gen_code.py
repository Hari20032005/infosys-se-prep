"""Pseudocode trace generators (P1 loops, P4 increments) in the style seen in the observed pool.

A program is a small AST. Three independent evaluators must agree before a question is kept:
  1. translate to Python source and exec it
  2. walk the AST with a tiny interpreter
  3. (batch, in build_topics.py) translate to Java, compile with javac, run, compare
All generated programs keep every value non-negative so Python's floor division and Java's
truncating division cannot disagree.
"""
import itertools, random, subprocess, tempfile, pathlib, re, os
from gen_core import Q, distinct_wrong

# ------------------------------------------------------------------ AST
# stmt := ('set', v, expr) | ('print', expr) | ('for', v, lo, hi, step, body) | ('while', cond, body)
#       | ('dowhile', body, cond) | ('if', cond, then, else) | ('inc', v, '++'|'--') | ('break',) | ('continue',)
# expr/cond are strings over variables, integers, + - * / (integer division) mod, == != < <= > >=, and, or

def to_py_expr(e):
    e = re.sub(r'\bmod\b', '%', e)
    e = re.sub(r'(?<![/])/(?![/])', '//', e)
    return e.replace(' and ', ' and ').replace(' or ', ' or ')


def to_java_expr(e):
    e = re.sub(r'\bmod\b', '%', e)
    return e.replace(' and ', ' && ').replace(' or ', ' || ')


def to_text_expr(e):
    return e


def render(prog, ind=0, dialect='infosys'):
    pad = '    ' * ind
    out = []
    for s in prog:
        k = s[0]
        if k == 'set': out.append(f"{pad}{s[1]} = {s[2]}")
        elif k == 'decl': out.append(f"{pad}Set integer {s[1]} = {s[2]}")
        elif k == 'print': out.append(f"{pad}Print {s[1]}")
        elif k == 'inc': out.append(f"{pad}{s[1]}{s[2]}")
        elif k == 'break': out.append(f"{pad}break")
        elif k == 'continue': out.append(f"{pad}continue")
        elif k == 'for':
            step = f" step {s[4]}" if s[4] != 1 else ''
            out.append(f"{pad}for (each {s[1]} from {s[2]} to {s[3]}{step})")
            out += render(s[5], ind + 1)
        elif k == 'while':
            out.append(f"{pad}while ({s[1]})"); out += render(s[2], ind + 1)
        elif k == 'dowhile':
            out.append(f"{pad}do"); out += render(s[1], ind + 1); out.append(f"{pad}while ({s[2]})")
        elif k == 'if':
            out.append(f"{pad}if ({s[1]})"); out += render(s[2], ind + 1)
            if s[3]:
                out.append(f"{pad}else"); out += render(s[3], ind + 1)
    return out


def render_official(prog):
    """Render in the dialect of Infosys's own sample paper: numbered lines, `Integer ...` declarations, `Set`,
    `For (each i from a to b)`, `While (cond)`, `If (cond) then`, `End-for` / `End-while` / `End-if`, `MOD`."""
    decl = sorted(vars_of(prog))
    lines = ([f"Integer {', '.join(decl)}"] if decl else [])

    def body(pr, ind):
        out = []
        pad = '  ' * ind
        for st in pr:
            k = st[0]
            e = lambda x: re.sub(r'\bmod\b', 'MOD', x)
            if k == 'decl': out.append(f"{pad}Set {st[1]} = {e(st[2])}")
            elif k == 'set': out.append(f"{pad}{st[1]} = {e(st[2])}")
            elif k == 'print': out.append(f"{pad}Print {e(st[1])}")
            elif k == 'inc': out.append(f"{pad}{st[1]}{st[2]}")
            elif k in ('break', 'continue'): out.append(f"{pad}{k}")
            elif k == 'for':
                step = f" step {st[4]}" if st[4] != 1 else ''
                out.append(f"{pad}For (each {st[1]} from {e(st[2])} to {e(st[3])}{step})"); out += body(st[5], ind + 1); out.append(f"{pad}End-for")
            elif k == 'while':
                out.append(f"{pad}While ({e(st[1])})"); out += body(st[2], ind + 1); out.append(f"{pad}End-while")
            elif k == 'dowhile':
                out.append(f"{pad}Do"); out += body(st[1], ind + 1); out.append(f"{pad}While ({e(st[2])})")
            elif k == 'if':
                out.append(f"{pad}If ({e(st[1])}) then"); out += body(st[2], ind + 1)
                if st[3]:
                    out.append(f"{pad}Else"); out += body(st[3], ind + 1)
                out.append(f"{pad}End-if")
        return out
    lines += body(prog, 0)
    return [f"{i}) {l}" for i, l in enumerate(lines, 1)]


def to_py(prog, ind=0, snap=False, depth=0):
    pad = '    ' * ind
    out = []
    for s in prog:
        k = s[0]
        if k in ('set', 'decl'): out.append(f"{pad}{s[1]} = {to_py_expr(s[2])}")
        elif k == 'print': out.append(f"{pad}out.append({to_py_expr(s[1])})")
        elif k == 'inc': out.append(f"{pad}{s[1]} {'+' if s[2] == '++' else '-'}= 1")
        elif k == 'break': out.append(f"{pad}break")
        elif k == 'continue': out.append(f"{pad}continue")
        elif k == 'for':
            lo, hi, st = to_py_expr(s[2]), to_py_expr(s[3]), s[4]
            out.append(f"{pad}for {s[1]} in range({lo}, ({hi}) + 1, {st}):" if st > 0 else f"{pad}for {s[1]} in range({lo}, ({hi}) - 1, {st}):")
            out += to_py(s[5], ind + 1, snap, depth + 1) or [pad + '    pass']
            if snap and depth == 0: out.append(f"{pad}    SNAP()")
        elif k == 'while':
            out.append(f"{pad}while {to_py_expr(s[1])}:"); out += to_py(s[2], ind + 1, snap, depth + 1) or [pad + '    pass']
            if snap and depth == 0: out.append(f"{pad}    SNAP()")
            out.append(f"{pad}    guard += 1"); out.append(f"{pad}    assert guard < 10000")
        elif k == 'dowhile':
            out.append(f"{pad}while True:"); out += to_py(s[1], ind + 1, snap, depth + 1)
            if snap and depth == 0: out.append(f"{pad}    SNAP()")
            out.append(f"{pad}    guard += 1"); out.append(f"{pad}    assert guard < 10000")
            out.append(f"{pad}    if not ({to_py_expr(s[2])}): break")
        elif k == 'if':
            out.append(f"{pad}if {to_py_expr(s[1])}:"); out += to_py(s[2], ind + 1, snap, depth) or [pad + '    pass']
            if s[3]:
                out.append(f"{pad}else:"); out += to_py(s[3], ind + 1, snap, depth)
    return out


def trace_table(prog, limit=7):
    """Markdown table of the variables at the end of each outermost loop pass (first `limit` passes)."""
    names = sorted(v for v in vars_of(prog))
    src = "out = []\nguard = 0\nrows = []\ndef SNAP():\n    rows.append([globals().get(n) for n in NAMES])\n" + '\n'.join(to_py(prog, snap=True))
    env = {'NAMES': names}
    exec(src, env)
    rows = env['rows']
    if not rows: return ''
    shown = rows[:limit]
    tbl = '| pass | ' + ' | '.join(names) + ' |\n|---|' + '---|' * len(names) + '\n' + '\n'.join(
        f"| {i + 1} | " + ' | '.join('-' if x is None else str(x) for x in r) + ' |' for i, r in enumerate(shown))
    return tbl + (f"\n\n(… {len(rows) - limit} more passes)" if len(rows) > limit else '')


def run_py(prog):
    src = "out = []\nguard = 0\n" + '\n'.join(to_py(prog))
    env = {}
    exec(src, env)
    return [str(x) for x in env['out']]


class _Break(Exception): pass
class _Continue(Exception): pass


def _ev(e, env):
    e = re.sub(r'\bmod\b', '%', e)
    e = re.sub(r'(?<![/])/(?![/])', '//', e)
    return eval(e, {}, env)


def run_ast(prog, env=None, out=None, guard=None):
    env = {} if env is None else env
    out = [] if out is None else out
    guard = guard if guard is not None else [0]
    def step():
        guard[0] += 1
        assert guard[0] < 10000
    for s in prog:
        k = s[0]
        if k in ('set', 'decl'): env[s[1]] = _ev(s[2], env)
        elif k == 'print': out.append(str(_ev(s[1], env)))
        elif k == 'inc': env[s[1]] += 1 if s[2] == '++' else -1
        elif k == 'break': raise _Break()
        elif k == 'continue': raise _Continue()
        elif k == 'if':
            run_ast((s[2] if _ev(s[1], env) else s[3]) or [], env, out, guard)
        elif k == 'for':
            i = _ev(s[2], env); hi = _ev(s[3], env)
            while (i <= hi if s[4] > 0 else i >= hi):
                env[s[1]] = i
                try: run_ast(s[5], env, out, guard)
                except _Break: break
                except _Continue: pass
                i += s[4]
                step()
        elif k == 'while':
            while _ev(s[1], env):
                try: run_ast(s[2], env, out, guard)
                except _Break: break
                except _Continue: pass
                step()
        elif k == 'dowhile':
            while True:
                try: run_ast(s[1], env, out, guard)
                except _Break: break
                except _Continue: pass
                step()
                if not _ev(s[2], env): break
    return out


def to_java_body(prog, ind=2):
    pad = '    ' * ind
    out = []
    for s in prog:
        k = s[0]
        if k == 'decl': out.append(f"{pad}int {s[1]} = {to_java_expr(s[2])};")
        elif k == 'set': out.append(f"{pad}{s[1]} = {to_java_expr(s[2])};")
        elif k == 'print': out.append(f"{pad}out.append({to_java_expr(s[1])}).append('\\n');")
        elif k == 'inc': out.append(f"{pad}{s[1]}{s[2]};")
        elif k == 'break': out.append(f"{pad}break;")
        elif k == 'continue': out.append(f"{pad}continue;")
        elif k == 'for':
            cmp_ = '<=' if s[4] > 0 else '>='
            out.append(f"{pad}for ({s[1]} = {to_java_expr(s[2])}; {s[1]} {cmp_} {to_java_expr(s[3])}; {s[1]} += {s[4]}) {{")
            out += to_java_body(s[5], ind + 1); out.append(f"{pad}}}")
        elif k == 'while':
            out.append(f"{pad}while ({to_java_expr(s[1])}) {{"); out += to_java_body(s[2], ind + 1); out.append(f"{pad}}}")
        elif k == 'dowhile':
            out.append(f"{pad}do {{"); out += to_java_body(s[1], ind + 1); out.append(f"{pad}}} while ({to_java_expr(s[2])});")
        elif k == 'if':
            out.append(f"{pad}if ({to_java_expr(s[1])}) {{"); out += to_java_body(s[2], ind + 1); out.append(f"{pad}}}")
            if s[3]:
                out.append(f"{pad}else {{"); out += to_java_body(s[3], ind + 1); out.append(f"{pad}}}")
    return out


def vars_of(prog, acc=None):
    acc = set() if acc is None else acc
    for s in prog:
        if s[0] in ('set', 'decl', 'inc'): acc.add(s[1])
        if s[0] == 'for': acc.add(s[1]); vars_of(s[5], acc)
        if s[0] == 'while': vars_of(s[2], acc)
        if s[0] == 'dowhile': vars_of(s[1], acc)
        if s[0] == 'if': vars_of(s[2], acc); vars_of(s[3] or [], acc)
    return acc


def java_batch(progs):
    """Compile and run every program in ONE Java class; return list of output lists."""
    methods = []
    for n, p in enumerate(progs):
        declared = {s[1] for s in p if s[0] == 'decl'}
        free = sorted(vars_of(p) - declared)
        pre = [f"        int {v} = 0;" for v in free]
        body = to_java_body(p, 2)
        methods.append(f"    static void q{n}(StringBuilder out) {{\n" + '\n'.join(pre + body) + "\n    }")
    main = ["    public static void main(String[] a) {", "        StringBuilder out = new StringBuilder();"]
    for n in range(len(progs)):
        main += [f"        q{n}(out); out.append(\"#\\n\");"]
    main += ["        System.out.print(out);", "    }"]
    src = "public class Batch {\n" + '\n'.join(methods) + '\n' + '\n'.join(main) + "\n}\n"
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'Batch.java').write_text(src)
    r = subprocess.run(['javac', 'Batch.java'], cwd=d, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:1500]
    r = subprocess.run(['java', '-cp', str(d), 'Batch'], capture_output=True, text=True, timeout=60)
    assert r.returncode == 0, r.stderr[:500]
    chunks = r.stdout.split('#\n')[:-1]
    return [c.split('\n')[:-1] for c in chunks]


def text_to_java_body(code_lines):
    """Translate the PRINTED official-dialect text (not the internal program) to Java, so the words a student actually
    reads are what gets executed. Indentation tells a `Do ... While (c)` footer apart from a `While (c)` header."""
    names, body, stack = [], [], []
    for raw in code_lines:
        raw = re.sub(r'^\s*\d+\)\s?', '', raw)
        ind = len(raw) - len(raw.lstrip())
        t = raw.strip()
        t = re.sub(r'\bMOD\b', '%', t).replace(' and ', ' && ').replace(' or ', ' || ')
        if t.startswith('Integer '):
            names += [x.strip() for x in t[8:].split(',')]
        elif t.startswith('Set '):
            body += [part.strip() + ';' for part in t[4:].split(',')]       # `Set j = 1, k = 2` sets two variables
        elif t.startswith('Print '):
            body.append(f'out.append(String.valueOf({t[6:]})).append("\\n");')
        elif t.startswith('For (each '):
            m = re.match(r'For \(each (\w+) from (.+?) to (.+?)(?: step (-?\d+))?\)$', t)
            v_, lo, hi, st = m.group(1), m.group(2), m.group(3), int(m.group(4) or 1)
            body.append(f"for ({v_} = {lo}; {v_} {'<=' if st > 0 else '>='} {hi}; {v_} += {st}) {{"); stack.append(('for', ind))
        elif t == 'Do':
            body.append('do {'); stack.append(('do', ind))
        elif t.startswith('While ('):
            cond = t[len('While '):]
            if stack and stack[-1] == ('do', ind):
                stack.pop(); body.append('} while ' + cond + ';')
            else:
                body.append('while ' + cond + ' {'); stack.append(('while', ind))
        elif t.startswith('If ('):
            body.append('if ' + re.sub(r' then$', '', t[3:]) + ' {'); stack.append(('if', ind))
        elif t == 'Else':
            body.append('} else {')
        elif t in ('End-for', 'End-while', 'End-if'):
            body.append('}'); stack.pop()
        elif t in ('break', 'continue'):
            body.append(t + ';')
        else:
            body.append(t + ';')                  # `x = expr`, `x++`
    assert not stack, 'unbalanced blocks in rendered pseudocode'
    return names, body


def java_batch_text(codes):
    """Like java_batch, but each program is the rendered text (list of lines)."""
    methods = []
    for n, lines in enumerate(codes):
        names, body = text_to_java_body(lines)
        pre = []
        for v_ in names:
            m = re.match(r'(\w+)\[(\d+)\]$', v_)                      # `Integer a[6]` declares an array of 6
            pre.append(f"        int[] {m.group(1)} = new int[{m.group(2)}];" if m else f"        int {v_} = 0;")
        methods.append(f"    static void q{n}(StringBuilder out) {{\n" + '\n'.join(pre + ['        ' + b for b in body]) + "\n    }")
    main = ["    public static void main(String[] a) {", "        StringBuilder out = new StringBuilder();"]
    for n in range(len(codes)):
        main += [f"        q{n}(out); out.append(\"#\\n\");"]
    main += ["        System.out.print(out);", "    }"]
    src = "public class BatchText {\n" + '\n'.join(methods) + '\n' + '\n'.join(main) + "\n}\n"
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'BatchText.java').write_text(src)
    r = subprocess.run(['javac', 'BatchText.java'], cwd=d, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:1500]
    r = subprocess.run(['java', '-cp', str(d), 'BatchText'], capture_output=True, text=True, timeout=60)
    assert r.returncode == 0, r.stderr[:500]
    chunks = r.stdout.split('#\n')[:-1]
    return [c.split('\n')[:-1] for c in chunks]


# ------------------------------------------------------------------ program templates
def v(rng, pool='ijk'): return rng.choice(pool)


def prog_accumulate(rng):
    n = rng.randint(6, 14); m = rng.choice([2, 3, 4, 5]); r = rng.randint(0, m - 1); k = rng.choice([1, 2, 3])
    body = [('if', f"i mod {m} == {r}", [('set', 's', f"s + i * {k}")], None)]
    return [('decl', 's', '0'), ('decl', 'n', str(n)), ('for', 'i', '1', 'n', 1, body), ('print', 's')]


def prog_until_divisible(rng):
    m = rng.choice([4, 5, 6, 7, 8, 9]); inc = rng.choice([2, 3, 4, 5, 6, 7]); n0 = rng.randint(10, 60)
    if inc % m == 0: return None
    prog = [('decl', 'n', str(n0)), ('decl', 'i', '0'), ('while', f"n mod {m} != 0", [('set', 'n', f"n + {inc}"), ('inc', 'i', '++')]),
            ('set', 'n', 'n + i'), ('print', 'n')]
    return prog


def prog_digits(rng):
    n = rng.randint(100, 99999); kind = rng.choice(['sum', 'rev', 'count_even', 'product'])
    if kind == 'sum':
        body = [('set', 's', 's + n mod 10'), ('set', 'n', 'n / 10')]; init = [('decl', 's', '0')]; out = 's'
    elif kind == 'rev':
        body = [('set', 'r', 'r * 10 + n mod 10'), ('set', 'n', 'n / 10')]; init = [('decl', 'r', '0')]; out = 'r'
    elif kind == 'count_even':
        body = [('if', 'n mod 10 mod 2 == 0', [('inc', 'c', '++')], None), ('set', 'n', 'n / 10')]; init = [('decl', 'c', '0')]; out = 'c'
    else:
        if '0' in str(n): return None
        body = [('set', 'p', 'p * (n mod 10)'), ('set', 'n', 'n / 10')]; init = [('decl', 'p', '1')]; out = 'p'
    return [('decl', 'n', str(n))] + init + [('while', 'n > 0', body), ('print', out)]


def prog_nested(rng):
    a, b, m = rng.randint(3, 6), rng.randint(3, 7), rng.choice([2, 3, 4])
    lo = rng.choice(['1', 'i'])
    inner = [('if', f"(i + j) mod {m} == 0", [('inc', 'c', '++')], None)]
    return [('decl', 'c', '0'), ('decl', 'j', '0'), ('for', 'i', '1', str(a), 1, [('for', 'j', lo, str(b), 1, inner)]), ('print', 'c')]


def prog_seq_print(rng):
    a, b, st = rng.randint(1, 6), rng.randint(9, 20), rng.choice([1, 2, 3])
    cond = rng.choice(['i mod 2 == 0', 'i mod 3 != 0', 'i > 5', 'i mod 2 == 1 and i > 3'])
    return [('for', 'i', str(a), str(b), st, [('if', cond, [('print', 'i * 2')], None)])]


def prog_dowhile(rng):
    x0 = rng.randint(1, 5); lim = rng.randint(12, 40); k = rng.choice([2, 3])
    body = [('set', 'x', f"x * {k}"), ('print', 'x')]
    return [('decl', 'x', str(x0)), ('dowhile', body, f"x < {lim}")]


def prog_break_continue(rng):
    n = rng.randint(8, 16); cut = rng.randint(4, n - 2); skip = rng.choice([2, 3])
    body = [('if', f"i mod {skip} == 0", [('continue',)], None), ('if', f"i > {cut}", [('break',)], None), ('set', 's', 's + i')]
    return [('decl', 's', '0'), ('for', 'i', '1', str(n), 1, body), ('print', 's'), ('print', 'i')]


def prog_gcd(rng):
    a, b = rng.randint(12, 90), rng.randint(12, 90)
    if a == b: return None
    body = [('if', 'a > b', [('set', 'a', 'a - b')], [('set', 'b', 'b - a')])]
    return [('decl', 'a', str(a)), ('decl', 'b', str(b)), ('while', 'a != b', body), ('print', 'a')]


def prog_halve(rng):
    n = rng.randint(20, 900)
    return [('decl', 'n', str(n)), ('decl', 'c', '0'), ('while', 'n > 1', [('set', 'n', 'n / 2'), ('inc', 'c', '++')]), ('print', 'c')]


def prog_downfor(rng):
    hi = rng.randint(15, 40); st = -rng.choice([2, 3, 4]); lo = rng.randint(1, 8)
    return [('decl', 's', '0'), ('for', 'i', str(hi), str(lo), st, [('set', 's', 's + i')]), ('print', 's')]


TEMPLATES = [prog_accumulate, prog_until_divisible, prog_digits, prog_nested, prog_seq_print, prog_dowhile, prog_break_continue, prog_gcd, prog_halve, prog_downfor]

_MUT = [(r'<=', '<'), (r'<', '<='), (r'>=', '>'), (r'>', '>='), (r'mod 2 == 0', 'mod 2 == 1'), (r'\+ (\d+)', lambda m: f"+ {int(m.group(1)) + 1}")]


def mutate(prog, rng):
    """One small edit that a careless solver would effectively make (off-by-one bound, swapped test, +1)."""
    import copy, json
    txt = json.dumps(prog)
    cands = []
    for pat, rep in _MUT:
        if re.search(pat, txt):
            cands.append((pat, rep))
    rng.shuffle(cands)
    for pat, rep in cands:
        new = re.sub(pat, rep, txt, count=1)
        try:
            return json.loads(new)
        except Exception:
            continue
    return None


def _untuple(x):
    return tuple(_untuple(y) for y in x) if isinstance(x, list) else x


def gen_trace(rng):
    prog = rng.choice(TEMPLATES)(rng)
    if prog is None: return None
    try:
        out = run_py(prog); out2 = run_ast(prog)
    except AssertionError:
        return None
    if out != out2 or not out or len(out) > 9: return None
    ans = ' '.join(out)
    # distractors from mutated programs
    wrong = []
    for _ in range(12):
        mp = mutate(prog, rng)
        if not mp: continue
        try:
            mo = ' '.join(run_py(_untuple(mp)))
        except Exception:
            continue
        if mo and mo != ans and mo not in wrong and len(mo.split()) <= 9: wrong.append(mo)
    for d in (1, -1, 2, 10):
        if len(wrong) >= 3: break
        try:
            alt = str(int(out[-1]) + d)
            if alt != ans and alt not in wrong: wrong.append(alt)
        except ValueError:
            pass
    if len(wrong) < 3: return None
    code = '\n'.join(render_official(prog))
    multi = len(out) > 1
    q = (f"What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)\n\n```text\n{code}\n```\n")
    tt = trace_table(prog)
    why = (f"Trace it, recording the variables at the end of each pass:\n\n{tt}\n\n" if tt else "Trace it. ") + (
        f"The program prints {', '.join(out)} in that order" if multi else f"The program prints {out[0]}") + f". Output: **{ans}**."
    
    qd = Q(q, [ans] + wrong[:3], why, lambda: ' '.join(run_ast(prog)), 'Trace')
    qd['prog'] = prog
    return qd


# ------------------------------------------------------------------ P4: increment operators
def _terms(rng, n=None):
    n = n or rng.choice([2, 2, 3])
    t = [rng.choice(['i++', '++i', 'i--', '--i', 'i']) for _ in range(n)]
    return t


def eval_terms(terms, ops, i0):
    i, total = i0, 0
    vals = []
    for t in terms:
        if t == 'i': v_ = i
        elif t == 'i++': v_ = i; i += 1
        elif t == '++i': i += 1; v_ = i
        elif t == 'i--': v_ = i; i -= 1
        elif t == '--i': i -= 1; v_ = i
        vals.append(v_)
    total = vals[0]
    for op, v_ in zip(ops, vals[1:]):
        total = total + v_ if op == '+' else total - v_
    return total, i


def eval_terms_alt(terms, ops, i0):
    """Second implementation: rewrite each term into a (pre-delta, read, post-delta) triple."""
    i = i0
    acc = None
    for n, t in enumerate(terms):
        pre = 1 if t == '++i' else -1 if t == '--i' else 0
        post = 1 if t == 'i++' else -1 if t == 'i--' else 0
        i += pre
        val = i
        i += post
        if post: val = i - post
        acc = val if acc is None else (acc + val if ops[n - 1] == '+' else acc - val)
    return acc, i


def gen_incr(rng, n_terms=None, asks=None):
    terms = _terms(rng, n_terms)
    if len(set(terms)) == 1 and terms[0] == 'i': return None
    ops = [rng.choice(['+', '+', '-']) for _ in terms[1:]]
    i0 = rng.randint(2, 7)
    expr = ''.join(f" {o} {t}" if n else t for n, (o, t) in enumerate(zip([''] + ops, terms)))
    expr = terms[0] + ''.join(f" {o} {t}" for o, t in zip(ops, terms[1:]))
    res, fin = eval_terms(terms, ops, i0)
    res2, fin2 = eval_terms_alt(terms, ops, i0)
    if (res, fin) != (res2, fin2): return None
    ask = rng.choice(list(asks) if asks else ['result', 'i', 'both'])
    # distractors: wrong evaluation orders
    def wrong_eval(mode):
        i = i0; vals = []
        for t in terms:
            if mode == 'all-pre':                     # treat every term as prefix
                d = 1 if '++' in t else -1 if '--' in t else 0
                i += d; vals.append(i)
            elif mode == 'all-post':
                vals.append(i); i += 1 if '++' in t else -1 if '--' in t else 0
            elif mode == 'ignore':
                vals.append(i)
        tot = vals[0]
        for o, x in zip(ops, vals[1:]): tot = tot + x if o == '+' else tot - x
        return tot, i
    wr = [wrong_eval(m) for m in ('all-pre', 'all-post', 'ignore')]
    code = f"int i = {i0};\nint result = {expr};\nprint(result, i);"
    if ask == 'result':
        ans = str(res); cands = [str(w[0]) for w in wr] + [str(res + 1), str(res - 1), str(res + 2)]
        q = f"What is the value of `result` after this code runs? Java-style left-to-right evaluation.\n\n```text\n{code}\n```\n"
        why = f"`i` starts at {i0}. Evaluate left to right: " + explain_terms(terms, ops, i0) + f" → result = **{res}**, and `i` ends at {fin}."
    elif ask == 'i':
        ans = str(fin); cands = [str(w[1]) for w in wr] + [str(fin + 1), str(fin - 1), str(i0)]
        q = f"What is the final value of `i` after this code runs?\n\n```text\n{code}\n```\n"
        why = f"Each `++`/`--` changes `i` once, wherever it sits: {sum(1 for t in terms if '++' in t) - sum(1 for t in terms if '--' in t):+d} in total, so `i` ends at {i0} {sum(1 for t in terms if '++' in t) - sum(1 for t in terms if '--' in t):+d} = **{fin}**. (result is {res}.)"
    else:
        ans = f"{res} {fin}"; cands = [f"{w[0]} {w[1]}" for w in wr] + [f"{res} {i0}", f"{res + 1} {fin}", f"{fin} {res}"]
        q = f"What does `print(result, i)` output?\n\n```text\n{code}\n```\n"
        why = f"Left to right: " + explain_terms(terms, ops, i0) + f". result = {res}, i = {fin} → **{ans}**."
    wrong = []
    for c in cands:
        if c != ans and c not in wrong: wrong.append(c)
    if len(wrong) < 3: return None
    qd = Q(q, [ans] + wrong[:3], why, lambda: {'result': str(eval_terms_alt(terms, ops, i0)[0]), 'i': str(eval_terms_alt(terms, ops, i0)[1]),
                                               'both': f"{eval_terms_alt(terms, ops, i0)[0]} {eval_terms_alt(terms, ops, i0)[1]}"}[ask], 'Increment operators')
    qd['meta'] = (terms, ops, i0, ask)
    return qd


def explain_terms(terms, ops, i0):
    i = i0; parts = []
    for t in terms:
        if t == 'i': parts.append(f"`i` reads {i}")
        elif t == 'i++': parts.append(f"`i++` reads {i} then i becomes {i + 1}"); i += 1
        elif t == '++i': i += 1; parts.append(f"`++i` makes i {i} then reads {i}")
        elif t == 'i--': parts.append(f"`i--` reads {i} then i becomes {i - 1}"); i -= 1
        elif t == '--i': i -= 1; parts.append(f"`--i` makes i {i} then reads {i}")
    return '; '.join(parts)


def java_incr_check(questions_meta):
    """questions_meta: list of (terms, ops, i0). Real Java run of every expression."""
    body = []
    for n, (terms, ops, i0) in enumerate(questions_meta):
        expr = terms[0] + ''.join(f" {o} {t}" for o, t in zip(ops, terms[1:]))
        body.append(f"        {{ int i = {i0}; int result = {expr}; System.out.println(result + \" \" + i); }}")
    src = "public class Inc {\n    public static void main(String[] a) {\n" + '\n'.join(body) + "\n    }\n}\n"
    d = pathlib.Path(tempfile.mkdtemp()); (d / 'Inc.java').write_text(src)
    r = subprocess.run(['javac', 'Inc.java'], cwd=d, capture_output=True, text=True); assert r.returncode == 0, r.stderr[:800]
    r = subprocess.run(['java', '-cp', str(d), 'Inc'], capture_output=True, text=True); assert r.returncode == 0
    return r.stdout.strip().split('\n')
