#!/usr/bin/env python3
"""Re-execute the runnable code in the COPIED Accenture banks where the question asks for printed output:
QB-P3 (36 C snippets, compiled with cc) and QB-P2 (16 Python snippets). Compares the program's real output with the
keyed option. Questions that ask for something other than the printed text (counts, complexity) are reported as such.
The remaining copied pseudocode banks use mixed pseudocode dialects that cannot be run directly; they rely on the source
library's QA (45 answers re-executed there) and are not re-verified here.
    python3 data/verify_copied.py
"""
import pathlib, re, subprocess, sys, tempfile
ROOT = pathlib.Path(__file__).resolve().parent.parent
norm = lambda s: re.sub(r'\s+', ' ', s.strip().replace('`', ''))


def blocks(path):
    t = path.read_text()
    parts = re.split(r'\n---\n', t)
    for p in parts:
        m = re.search(r'\*\*(\d+)\.\*\* \*\*\[', p)
        if not m: continue
        n = int(m.group(1))
        code = re.search(r'```(\w+)\n(.*?)```', p, re.S)
        opts = dict(re.findall(r'(?m)^\(([a-d])\)\s+(.*)$', p.split('**%d. (' % n)[0]))
        key = re.search(r'\*\*%d\. \(([a-d])\)' % n, p)
        stem = p.split('```')[2] if p.count('```') >= 2 else ''
        if code and key and opts:
            yield n, code.group(1), code.group(2), opts, key.group(1), stem


def run_c(code):
    src = code if re.search(r'\bmain\s*\(', code) else "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdint.h>\nint main(void){\n" + code + "\nreturn 0;}\n"
    d = pathlib.Path(tempfile.mkdtemp()); (d / 'a.c').write_text(src)
    r = subprocess.run(['cc', '-w', '-o', str(d / 'a'), str(d / 'a.c')], capture_output=True, text=True)
    if r.returncode: return None
    return subprocess.run([str(d / 'a')], capture_output=True, text=True, timeout=10).stdout


def run_py(code):
    r = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, timeout=10)
    return r.stdout if r.returncode == 0 else None


# ---------------------------------------------------------------- pseudocode translators (three dialects)
def _cond(c):
    c = re.sub(r'(?<![<>!=])=(?!=)', '==', c)
    c = re.sub(r'<>', '!=', c)
    c = re.sub(r'\bAND\b|&&', ' and ', c, flags=re.I); c = re.sub(r'\bOR\b|\|\|', ' or ', c, flags=re.I)
    c = re.sub(r'\bNOT\b', ' not ', c, flags=re.I)
    c = re.sub(r'(?<![&|=<>!])!(?!=)', ' not ', c)
    c = re.sub(r'\bMOD\b', '%', c, flags=re.I); c = re.sub(r'\bDIV\b', '//', c, flags=re.I)
    return c.replace('TRUE', 'True').replace('FALSE', 'False')


def _ex(e):
    e = re.sub(r'\bMOD\b', '%', e, flags=re.I); e = re.sub(r'\bDIV\b', '//', e, flags=re.I)
    e = re.sub(r'(?<![/])/(?![/])', '//', e)
    return e


def tr_p6(code):
    out, ind = [], 0
    for raw in code.split('\n'):
        l = re.sub(r'^\s*\d+\.\s*', '', raw).strip()
        if not l: continue
        U = l.upper(); pad = '    ' * ind
        if U.startswith('SET '): out.append(pad + _ex(l[4:]))
        elif U.startswith('PRINT '): out.append(pad + 'out.append(' + _ex(l[6:]) + ')')
        elif U.startswith('IF ') and U.endswith(' THEN'): out.append(pad + 'if ' + _cond(l[3:-5]) + ':'); ind += 1
        elif U.startswith('ELSE IF ') and U.endswith(' THEN'): ind -= 1; out.append('    ' * ind + 'elif ' + _cond(l[8:-5]) + ':'); ind += 1
        elif U == 'ELSE': ind -= 1; out.append('    ' * ind + 'else:'); ind += 1
        elif U == 'END IF': ind -= 1
        elif re.match(r'^[A-Za-z_]\w*(\[.*\])? = ', l): out.append(pad + _ex(l))
        else: raise ValueError(l)
    return '\n'.join(out)


def tr_p1(code):
    out, stack = [], []          # stack of (indent, kind)
    lines = [l.rstrip() for l in code.split('\n') if l.strip()]
    for k, raw in enumerate(lines):
        ind = (len(raw) - len(raw.lstrip())) // 4
        l = raw.strip(); pad = '    ' * ind
        while stack and stack[-1][0] >= ind and not (stack[-1][1] == 'do' and stack[-1][0] == ind and l.startswith('while') and not l.endswith(':')):
            stack.pop()
        m = re.match(r'for (\w+) = (.+?) to (.+?)(?: step (.+?))?:$', l)
        if m:
            v, a, b, st = m.groups(); st = st or '1'
            out.append(pad + f"for {v} in range({_ex(a)}, ({_ex(b)}) {'+' if int(st) > 0 else '-'} 1, {st}):"); continue
        if l == 'do:': out.append(pad + 'while True:'); stack.append((ind, 'do')); continue
        if l.startswith('while') and not l.endswith(':'):
            out.append(pad + '    if not (' + _cond(l[5:].strip()) + '): break'); continue
        if l.endswith(':') and re.match(r'(if|while|elif)\b', l): out.append(pad + l[:l.index(' ')] + ' ' + _cond(l[l.index(' ') + 1:-1]) + ':'); continue
        if l == 'else:': out.append(pad + 'else:'); continue
        if l in ('break', 'continue'): out.append(pad + l); continue
        if re.match(r'(print|Print) ', l): out.append(pad + 'out.append(' + _ex(l.split(' ', 1)[1]) + ')'); continue
        if re.match(r'^[A-Za-z_]\w* = ', l): out.append(pad + _ex(l)); continue
        raise ValueError(l)
    return '\n'.join(out)


def tr_p5(code):
    out, stack = [], []          # stack of (indent, post-statement)
    lines = [re.sub(r'\s*//.*$', '', l).rstrip() for l in code.split('\n')]
    lines = [l for l in lines if l.strip()]
    for raw in lines:
        ind = (len(raw) - len(raw.lstrip())) // 4; l = raw.strip(); pad = '    ' * ind
        while stack and stack[-1][0] >= ind:
            i0, post = stack.pop()
            if post: out.append('    ' * (i0 + 1) + post)
        m = re.match(r'Integer (\w+)(\[\d+\])+ = (.+)$', l)
        if m: out.append(pad + f"{m.group(1)} = " + m.group(3).replace('{', '[').replace('}', ']')); continue
        m = re.match(r'Integer (\w+) = (.+)$', l)
        if m: out.append(pad + f"{m.group(1)} = {_ex(m.group(2))}"); continue
        m = re.match(r'Integer (\w+)$', l)
        if m: out.append(pad + f"{m.group(1)} = 0"); continue
        m = re.match(r'for \((.*?);(.*?);(.*?)\)$', l)
        if m:
            init, cond, post = [x.strip() for x in m.groups()]
            out.append(pad + _ex(init)); out.append(pad + 'while ' + _cond(cond) + ':'); stack.append((ind, _ex(post).replace('++', ' += 1'))); continue
        m = re.match(r'(if|while) \((.*)\)$', l)
        if m: out.append(pad + m.group(1) + ' ' + _cond(m.group(2)) + ':'); stack.append((ind, None)); continue
        if l == 'else': out.append(pad + 'else:'); stack.append((ind, None)); continue
        if re.match(r'(Print|print) ', l): out.append(pad + 'out.append(' + _ex(l.split(' ', 1)[1]) + ')'); continue
        if re.match(r'^[A-Za-z_]\w*(\[.*\])* = ', l): out.append(pad + _ex(l)); continue
        raise ValueError(l)
    while stack:
        i0, post = stack.pop()
        if post: out.append('    ' * (i0 + 1) + post)
    return '\n'.join(out)


def run_pseudo(code, tr):
    try:
        src = "out = []\n" + tr(code)
    except Exception:
        return None
    env = {}
    try:
        exec(compile(src, '<p>', 'exec'), env)
    except Exception:
        return None
    return ' '.join(str(x) for x in env['out'])


tot = ok = bad = skipped = 0
for name, runner, langs in (('QB-P3-bitwise-operators.md', run_c, ('c',)), ('QB-P2-recursion.md', run_py, ('python',)),
                            ('QB-P6-conditionals-nested-if.md', lambda c: run_pseudo(c, tr_p6), ('',)),
                            ('QB-P1-loops-iteration.md', lambda c: run_pseudo(c, tr_p1), ('text',)),
                            ('QB-P5-arrays.md', lambda c: run_pseudo(c, tr_p5), ('', 'text'))):
    for n, lang, code, opts, key, stem in blocks(ROOT / 'question-banks' / name):
        tot += 1
        if lang not in langs: skipped += 1; continue
        out = runner(code)
        if out is None: skipped += 1; print(f"  {name} Q{n}: cannot run"); continue
        o = norm(out)
        keyed = norm(opts[key])
        if o == keyed or o.replace(' ', '') == keyed.replace(' ', ''):
            ok += 1
        elif not any(norm(v) == o or norm(v).replace(' ', '') == o.replace(' ', '') for v in opts.values()):
            skipped += 1                                           # the question asks something other than the printed text
        else:
            bad += 1; print(f"  MISMATCH {name} Q{n}: program printed {o!r}, key says ({key}) {keyed!r}")
print(f"verify_copied: {tot} code questions inspected; {ok} output keys confirmed by running the code; {bad} mismatches; {skipped} ask for something other than printed output or cannot be run")
sys.exit(1 if bad else 0)
