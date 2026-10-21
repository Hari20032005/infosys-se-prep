#!/usr/bin/env python3
"""Assemble every NEW topic file and every generated question bank.

For each new topic:  frontmatter + H1 + generated section 1 + hand-written sections from data/src/<code>.md
+ generated section 7 (12 inline practice questions with an ANSWER KEY) + generated section 10.
Inline questions and the standalone bank for a topic come from ONE generator run, sliced, so they never repeat.

    python3 data/build_topics.py
"""
import random
import pathlib, random, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gen_core, gen_puzzles as GP, gen_reasoning as GR, gen_quant as GQ, gen_code as GC, gen_oop, bank_verbal as BV
from lib_common import *
import copy_reused as CR

SRC = ROOT / 'data' / 'src'
FILES = {}          # code -> relative path, written to data/filemap.json
BANKS = {}          # code -> [relative bank paths]
LOG = []


def letters(ks): return ''.join(ks)


# ---------------------------------------------------------------- generator specs
def puzzle_mix(fams): return lambda rng: GP.gen_mixed(rng, fams)


SPEC = {
    # code: (dir, filename, generator fn or list factory, inline n, bank n, bank title, seed)
    'Z1':  ('puzzles', 'Z1-number-grids-and-matrices', puzzle_mix(['row3', 'row4', 'seqtable', 'sumgrid', 'kakuro', 'row4', 'row3', 'gridsums', 'gridsums']), 12, 30, 'Number grids and matrices'),
    'Z2':  ('puzzles', 'Z2-pair-and-figure-rules', puzzle_mix(['pair', 'pair', 'digitpair', 'figure', 'figure', 'cubebox', 'zigzag', 'zigzag']), 12, 30, 'Pair and figure rules'),
    'A3':  ('topics', 'A3-operator-logic', GR.gen_operator, 12, 20, 'Operator logic'),
    'A5':  ('topics', 'A5-blood-relations', GR.gen_blood, 12, 20, 'Blood relations'),
    'A7':  ('topics', 'A7-data-interpretation', GQ.gen_di, 12, 24, 'Data interpretation'),
    'A8':  ('topics', 'A8-linear-equations-and-ages', GQ.gen_linear, 12, 30, 'Linear equations and ages'),
    'A10': ('topics', 'A10-number-system', GQ.gen_numsys, 8, 12, 'Number system'),
    'A11': ('topics', 'A11-mensuration', GQ.gen_mensuration, 12, 20, 'Mensuration'),
    'A16': ('topics', 'A16-time-and-work', GQ.gen_timework, 8, 12, 'Time and work'),
    'A18': ('topics', 'A18-permutations-combinations-probability', GQ.gen_pc, 8, 12, 'Permutations, combinations and probability'),
    'A20': ('topics', 'A20-cryptarithmetic', GR.gen_crypto, 8, 8, 'Cryptarithmetic'),
    'A21': ('topics', 'A21-non-verbal-reasoning', GR.gen_nonverbal, 8, 10, 'Non-verbal reasoning (text forms)'),
    'P4':  ('pseudocode', 'P4-increment-operators-and-dialect', GC.gen_incr, 12, 24, 'Increment operators'),
}
# extra banks for files that were COPIED (they keep their own inline practice; these add Infosys-shaped volume)
EXTRA = {
    'A1': ('QB-A1-coding-decoding', GR.gen_coding, 30, 'Coding and decoding'),
    'A2': ('QB-A2-number-and-letter-series', GR.gen_series, 30, 'Number and letter series'),
    'P1': ('QB-P1-infosys-dialect-traces', GC.gen_trace, 24, 'Loop and trace questions in the Infosys dialect'),
    'A6': ('QB-A6-data-sufficiency-1234', GR.gen_ds, 24, 'Data sufficiency in the official 1-2-3-4 format'),
    'A19': ('QB-A19-if-then-rules', GR.gen_conditional, 20, 'If-then attendance puzzles'),
    'A4': ('QB-A4-ordered-deduction', GR.gen_deductive, 16, 'Deductive reasoning: which statements entail which'),
    'A9': ('QB-A9-replacement-mixtures', GQ.gen_mixture_replace, 16, 'Replacement mixtures (milk and water)'),
}


def section10_new(code):
    t = TOP[code]
    ids = ', '.join(t['qids']) if t['qids'] else 'none'
    return (f"## 10. Sources\n\nThis file was written for this library. **Infosys evidence:** observed questions {ids} in `../data/questions-observed.csv`; "
            f"section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `{code}`). "
            f"Confidence **{t['conf']}**. Practice questions in §7 and the bank were generated and checked by execution (brute force, simulation or inverse); "
            f"see `../research/04-qa-report.md`. Nothing here is a published Infosys syllabus.\n")


def sec7(code, qs, bank_path=None, label='Practice questions', seed=None):
    qmd, kmd, used = render_questions(qs, seed or (code + '-inline'))
    link = f"\nMore questions: [`{bank_path.name}`](../question-banks/{bank_path.name}).\n" if bank_path else ''
    return f"## 7. {label}\n{link}\n{qmd}\n### ANSWER KEY\n\n{kmd}\n", used


def assemble(code, path, qs_inline, bank_path, extra_head='', label='Practice questions'):
    t = TOP[code]
    src = (SRC / f"{code}.md").read_text(encoding='utf-8')
    # split hand-written sections so section 7 goes between 6 and 8
    parts = re.split(r'(?m)^(?=## \d+\. )', src)
    parts = [p for p in parts if p.strip()]
    by = {int(re.match(r'## (\d+)\.', p).group(1)): p.rstrip('\n') + '\n' for p in parts}
    need = {2, 3, 4, 5, 6, 8, 9}
    assert need <= set(by), f"{code}: missing sections {need - set(by)}"
    s7, used = sec7(code, qs_inline, bank_path, label, seed=f"{code}-inline")
    body = [CR.section1(code).rstrip('\n') + '\n']
    for n in (2, 3, 4, 5, 6):
        body.append(by[n])
    body.append(s7)
    body.append(by[8]); body.append(by[9])
    body.append(section10_new(code))
    text = frontmatter(code, t['label']) + f"\n# {code} — {t['label']}\n\n" + '\n'.join(body)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')
    return used


def build_generated(code):
    d, name, gen, n_in, n_bank, btitle = SPEC[code]
    seed = 1000 + sum(ord(c) for c in code)
    qs = gen_core.run(gen, seed, n_in + n_bank)
    inline, bank = qs[:n_in], qs[n_in:]
    bank_path = ROOT / 'question-banks' / f"QB-{code}-{name.split('-', 1)[1]}.md"
    used_a = assemble(code, ROOT / d / f"{name}.md", inline, bank_path)
    used_b = write_bank(bank_path, code, btitle, bank,
                        f"Generated for this library from the rule families seen in the Infosys pool (`../data/gen_*.py`). Every key was recomputed by a second route; see `../research/04-qa-report.md`.",
                        seed=f"{code}-bank")
    FILES[code] = f"{d}/{name}.md"; BANKS.setdefault(code, []).append(str(bank_path.relative_to(ROOT)))
    LOG.append((code, len(inline), len(bank)))
    return inline, bank


def build_extra(code):
    fname, gen, n, title = EXTRA[code]
    seed = 5000 + sum(ord(c) for c in code)
    if code == 'A6':                            # fixed 1-2-3-4 scale: balance the four answers by construction
        qs = [q for w in (1, 2, 3, 4) for q in gen_core.run(gen, seed + w, n // 4, want=w)]
        for salt in range(200):                 # seeded shuffle; reject a guessable repeating key
            random.Random(seed * 7 + salt).shuffle(qs)
            seq = ''.join(q['opts'][0] for q in qs)
            if not any(seq == (seq[:p_] * (n // p_ + 1))[:n] for p_ in range(1, 7)):
                break
        else:
            raise RuntimeError('no non-cyclic order for A6')
    else:
        qs = gen_core.run(gen, seed, n)
    path = ROOT / 'question-banks' / f"{fname}.md"
    write_bank(path, code, title, qs,
               f"Generated for this library in the style of the observed Infosys items (`../data/gen_*.py`); an additional bank for the copied topic file. Every key was recomputed by a second route.",
               seed=f"{code}-extra")
    BANKS.setdefault(code, []).append(str(path.relative_to(ROOT)))
    LOG.append((f"{code}+", 0, len(qs)))
    return qs


def build_hand():
    """V5, V6, G2, P9 and W1: hand-written items."""
    # ---- V5 para-jumbles
    inl, bank = BV.jumble_questions(range(0, 10)), BV.jumble_questions(range(10, 18))
    bp = ROOT / 'question-banks' / 'QB-V5-para-jumbles.md'
    assemble('V5', ROOT / 'topics' / 'V5-para-jumbles.md', inl, bp)
    write_bank(bp, 'V5', 'Para-jumbles', bank, "Hand-written for this library. Each set is a chain in which every sentence points back to the one before it, so exactly one order works.", seed='V5-bank')
    FILES['V5'] = 'topics/V5-para-jumbles.md'; BANKS['V5'] = [str(bp.relative_to(ROOT))]; LOG.append(('V5', 10, 8))
    # ---- V2 extra: identify the correct sentence (official format)
    cq = BV.choose_questions()
    cp = ROOT / 'question-banks' / 'QB-V2-identify-the-correct-sentence.md'
    write_bank(cp, 'V2', 'Identify the correct sentence', cq, "The official sample paper has an error-identification set in this format: four versions of a sentence, one correct. Hand-written for this library.", seed='V2-extra')
    BANKS.setdefault('V2', []).append(str(cp.relative_to(ROOT))); LOG.append(('V2+', 0, len(cq)))
    # ---- V6 critical reasoning
    inl, bank = BV.cr_questions(range(0, 8)), BV.cr_questions(range(8, 14))
    bp = ROOT / 'question-banks' / 'QB-V6-critical-reasoning.md'
    assemble('V6', ROOT / 'topics' / 'V6-critical-reasoning.md', inl, bp)
    write_bank(bp, 'V6', 'Critical reasoning', bank, "Hand-written for this library; each key states why the other options fail.", seed='V6-bank')
    FILES['V6'] = 'topics/V6-critical-reasoning.md'; BANKS['V6'] = [str(bp.relative_to(ROOT))]; LOG.append(('V6', 8, 6))
    # ---- G2 grammar (inline sentence-level + cloze bank)
    bp = ROOT / 'question-banks' / 'QB-G2-cloze-passages.md'
    assemble('G2', ROOT / 'topics' / 'G2-grammar-tense-articles-prepositions.md', BV.G2_INLINE, bp)
    write_bank(bp, 'G2', 'Cloze passages (five blanks each)', BV.cloze_questions(range(0, 5)),
               "Five passages of five blanks each, the shape of the English Grammar section (5 questions, 10 minutes). Hand-written for this library.", seed='G2-bank')
    FILES['G2'] = 'topics/G2-grammar-tense-articles-prepositions.md'; BANKS['G2'] = [str(bp.relative_to(ROOT))]; LOG.append(('G2', 12, 25))
    # ---- P9 OOP
    oq = gen_oop.oop_questions()
    bp = ROOT / 'question-banks' / 'QB-P9-oop-in-pseudocode.md'
    assemble('P9', ROOT / 'pseudocode' / 'P9-oop-in-pseudocode.md', oq[:6], bp)
    write_bank(bp, 'P9', 'OOP tracing', oq[6:], "Every key is the real output of the Java snippet, produced by compiling and running it (`data/gen_oop.py`).", seed='P9-bank')
    FILES['P9'] = 'pseudocode/P9-oop-in-pseudocode.md'; BANKS['P9'] = [str(bp.relative_to(ROOT))]; LOG.append(('P9', 6, 6))
    # ---- W1 writing: prompts instead of MCQs
    build_w1()


W1_PROMPTS = [
    ("Ozone layer depletion", "essay", "Define the layer → CFC cause → effects on health and crops → Montreal Protocol and recovery → a personal step."),
    ("The future of remote work", "essay", "Define remote work → benefits (commute, balance, talent) → challenges (isolation, communication) → hybrid model → conclusion."),
    ("Plastic pollution", "essay", "Scale of the problem → causes (single-use, weak collection) → effects (drains, rivers, animals) → solutions (reuse, recycling, rules)."),
    ("Artificial intelligence in everyday life", "essay", "Where we meet it (phones, maps, recommendations) → benefits → risks (jobs, privacy, errors) → responsible use."),
    ("Importance of a healthy lifestyle", "essay", "Definition → diet, exercise, sleep → effects on study and work → habits to start today."),
    ("Social media: boon or bane", "essay", "What it offers → risks (time, comparison, misinformation) → balanced use → conclusion."),
    ("Renewable energy for India", "essay", "Need → solar, wind, hydro → challenges (storage, cost) → government role → outlook."),
    ("Email to your manager: you need a day off next Friday", "email", "Subject → purpose in line 1 → date and reason → how work will be covered → polite close."),
    ("Email to a vendor: the delivered laptops are faulty", "email", "Subject with order number → what arrived → what is wrong → what you want (replacement by a date) → close."),
    ("Email to your professor: request an extension for a project", "email", "Subject → purpose → reason in one sentence → revised date → thanks."),
    ("Email to HR confirming your joining date", "email", "Subject → thank for the offer → confirm the date and location → list documents you will bring → close."),
    ("Cyber safety for students", "essay", "Risks → simple rules (passwords, links, updates) → role of the college → conclusion."),
    ("Teamwork in the workplace", "essay", "Definition → benefits → obstacles → how to build a good team → conclusion."),
    ("Email to a colleague: reschedule a meeting", "email", "Subject → purpose → two alternative slots → apology → close."),
    ("Cashless payments and digital India", "essay", "Growth of UPI → benefits → risks (fraud, digital divide) → what to do → outlook."),
]


def build_w1():
    code = 'W1'
    bp = ROOT / 'question-banks' / 'QB-W1-writing-prompts.md'
    lines = ['## 7. Practice prompts', '', f"More prompts: [`{bp.name}`](../question-banks/{bp.name}).", '',
             'Set a timer for **10 minutes** for each. Write first, then compare with the outline.', '']
    for i, (t, kind, outline) in enumerate(W1_PROMPTS[:8], 1):
        lines.append(f"{i}. **[{kind.capitalize()}]** {t}")
    lines += ['', '### Model outlines', '']
    for i, (t, kind, outline) in enumerate(W1_PROMPTS[:8], 1):
        lines.append(f"- **{i}. {t}.** {outline}")
    s7 = '\n'.join(lines) + '\n'
    t = TOP[code]
    src = (SRC / 'W1.md').read_text(encoding='utf-8')
    parts = [p for p in re.split(r'(?m)^(?=## \d+\. )', src) if p.strip()]
    by = {int(re.match(r'## (\d+)\.', p).group(1)): p.rstrip('\n') + '\n' for p in parts}
    body = [CR.section1(code).rstrip('\n') + '\n'] + [by[n] for n in (2, 3, 4, 5, 6)] + [s7, by[8], by[9], section10_new(code)]
    text = frontmatter(code, t['label']) + f"\n# {code} — {t['label']}\n\n" + '\n'.join(body)
    (ROOT / 'topics' / 'W1-english-writing.md').write_text(text, encoding='utf-8')
    bl = [f"# QB-W1 — Writing prompts", '', f"**English Writing** · **Tier 1** · {len(W1_PROMPTS)} prompts", '',
          'The test gives one essay or email in 10 minutes. Use each prompt as a timed drill, then compare your structure with the outline.', '',
          '---', '', '## Prompts', '']
    for i, (tt, kind, outline) in enumerate(W1_PROMPTS, 1):
        bl += [f"**{i}.** **[{kind.capitalize()}]** {tt}", f"*Outline:* {outline}", '']
    bl += ['### Self-marking checklist', '', '- On topic, with a clear introduction and conclusion', '- Three points, each in its own sentence or two',
           '- Present tense unless describing history', '- No contractions in an email', '- Re-read once: agreement, articles, spelling', '- About 190 words in 10 minutes.']
    bp.write_text('\n'.join(bl) + '\n', encoding='utf-8')
    FILES['W1'] = 'topics/W1-english-writing.md'; BANKS['W1'] = [str(bp.relative_to(ROOT))]; LOG.append(('W1', 8, len(W1_PROMPTS)))


def main():
    for code in SPEC:
        build_generated(code)
    for code in EXTRA:
        build_extra(code)
    build_hand()
    # real-Java cross-check of every P4 increment question
    # (done in verify_generated.py, which regenerates the same questions and runs javac/java)
    import json
    fm = json.loads((ROOT / 'data' / 'filemap.json').read_text())
    fm.update({k: v for k, v in FILES.items()})
    fm['_banks'] = BANKS
    (ROOT / 'data' / 'filemap.json').write_text(json.dumps(fm, indent=2) + '\n')
    print(f"built {len(FILES)} new topic files; {sum(len(v) for v in BANKS.values())} generated/hand banks")
    print(f"generated questions: {gen_core.STATS['generated']} (each with an independent check())")
    for row in LOG: print('  ', row)


if __name__ == '__main__':
    main()
