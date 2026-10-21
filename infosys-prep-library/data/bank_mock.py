"""Hand-written and search-verified items for MOCK-01.
  * syllogisms: a conclusion FOLLOWS only if it is true in every model of the premises (exhaustive search,
    with the usual exam convention that every named class is non-empty);
  * seating: constraints are added until brute force over all arrangements leaves exactly one;
  * pseudocode: keys come from executing the same logic in Python;
  * verbal: authored, one best answer by design (see each `why`).
"""
import itertools, random
from gen_core import Q
from bank_verbal import T


# ---------------------------------------------------------------- syllogism model checker
def _models(sets, n=6):
    k = len(sets)
    for bits in itertools.product(range(2 ** k), repeat=n):          # each element: membership bitmask
        yield bits


def holds(stmt, bits, idx):
    kind, a, b = stmt
    ia, ib = idx[a], idx[b]
    A = [i for i, m in enumerate(bits) if m >> ia & 1]
    B = [i for i, m in enumerate(bits) if m >> ib & 1]
    if kind == 'all':  return all(i in B for i in A)
    if kind == 'some': return any(i in B for i in A)
    if kind == 'no':   return not any(i in B for i in A)
    if kind == 'some_not': return any(i not in B for i in A)
    raise ValueError(kind)


def follows(premises, conclusion, sets, n=5):
    idx = {s: i for i, s in enumerate(sets)}
    found = False
    for bits in _models(sets, n):
        if not all(any(m >> idx[s] & 1 for m in bits) for s in sets):   # every class non-empty
            continue
        if all(holds(p, bits, idx) for p in premises):
            found = True
            if not holds(conclusion, bits, idx):
                return False
    return found


def syllogism(stem, premises, concs, sets, why):
    res = [follows(premises, c[1], sets) for c in concs]
    names = ['Only conclusion I follows', 'Only conclusion II follows', 'Both conclusions follow', 'Neither conclusion follows']
    correct = names[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[tuple(res)]]
    wrong = [n for n in names if n != correct]
    text = stem + '\n\n' + '\n'.join(f"{'I' if i == 0 else 'II'}. {c[0]}" for i, c in enumerate(concs))
    return T(text, correct, wrong, why + f" (Checked against every model of the premises: I {'follows' if res[0] else 'does not'}, II {'follows' if res[1] else 'does not'}.)", 'Syllogism')


SYL = [
    syllogism("Statements: All engines are machines. Some machines are toys.\nConclusions:",
              [('all', 'engine', 'machine'), ('some', 'machine', 'toy')],
              [("Some engines are toys.", ('some', 'engine', 'toy')), ("Some toys are machines.", ('some', 'toy', 'machine'))],
              ['engine', 'machine', 'toy'],
              "The machines that are toys may all be non-engines, so I does not follow. ‘Some machines are toys’ turns round to ‘Some toys are machines’, so II follows."),
    syllogism("Statements: All doctors are graduates. All graduates are readers.\nConclusions:",
              [('all', 'doctor', 'graduate'), ('all', 'graduate', 'reader')],
              [("All doctors are readers.", ('all', 'doctor', 'reader')), ("Some readers are doctors.", ('some', 'reader', 'doctor'))],
              ['doctor', 'graduate', 'reader'],
              "Two ‘all’ statements chain: doctors ⊂ graduates ⊂ readers, so I follows. ‘All doctors are readers’ also gives ‘Some readers are doctors’ by conversion, so II follows."),
]


# ---------------------------------------------------------------- seating puzzle with a unique solution
def seating(seed):
    rng = random.Random(seed)
    people = list('ABCDE')
    for _ in range(2000):
        target = people[:]
        rng.shuffle(target)
        pos = {p: i for i, p in enumerate(target)}
        pool = []
        for x, y in itertools.permutations(people, 2):
            if pos[x] + 1 == pos[y]:
                pool.append((f"{x} sits immediately to the left of {y}.", lambda t, x=x, y=y: t.index(x) + 1 == t.index(y)))
            if abs(pos[x] - pos[y]) == 1:
                pool.append((f"{x} and {y} sit next to each other.", lambda t, x=x, y=y: abs(t.index(x) - t.index(y)) == 1))
            if abs(pos[x] - pos[y]) >= 2:
                pool.append((f"{x} does not sit next to {y}.", lambda t, x=x, y=y: abs(t.index(x) - t.index(y)) != 1))
        for x in people:
            if pos[x] in (0, 4):
                pool.append((f"{x} sits at one of the two ends.", lambda t, x=x: t.index(x) in (0, 4)))
            if pos[x] == 2:
                pool.append((f"{x} sits exactly in the middle.", lambda t, x=x: t.index(x) == 2))
        rng.shuffle(pool)
        chosen, cons = [], []
        perms = list(itertools.permutations(people))
        alive = perms
        for txt, f in pool:
            if len(chosen) >= 5: break
            if not f(target): continue
            new = [p for p in alive if f(p)]
            if len(new) < len(alive):
                chosen.append(txt); cons.append(f); alive = new
            if len(alive) == 1: break
        if len(alive) == 1 and 4 <= len(chosen) <= 5:
            return chosen, list(alive[0]), cons
    raise RuntimeError('no unique seating found')


def seating_questions(seed=7):
    cons_txt, sol, cons = seating(seed)
    setup = ("Five friends A, B, C, D and E sit in a row facing north. " + ' '.join(cons_txt))
    left_end, second_right = sol[0], sol[3]
    def check_unique():
        return sum(1 for p in itertools.permutations('ABCDE') if all(f(list(p)) for f in cons))
    assert check_unique() == 1
    qs = []
    others = list('ABCDE')
    def mk(ask, ans, why):
        wrong = [p for p in others if p != ans][:3]
        return T(f"{setup}\n\n{ask}", ans, wrong, why, 'Seating',)
    row = ' '.join(sol)
    qs.append(mk("Who sits at the extreme left end of the row?", left_end, f"Applying the clues leaves exactly one arrangement (left to right: {row}). The extreme left is {left_end}. (Checked by trying all 120 arrangements: exactly one satisfies every clue.)"))
    qs.append(mk("Who sits second from the right end?", second_right, f"The only arrangement that satisfies every clue is {row}, so the person second from the right is {second_right}."))
    return qs


# ---------------------------------------------------------------- pseudocode (keys by execution)
def pseudo_recursion():
    def f(x, y): return x if y == 0 else f(x * 2, y - 1)
    ans = f(3, 4)
    wrong = [f(3, 3), f(3, 5), 3 + 4 * 2]
    code = "Function f(x, y)\n    if (y == 0)\n        return x\n    return f(x * 2, y - 1)\n\nPrint f(3, 4)"
    return T(f"What is the output of the following pseudocode?\n\n```text\n{code}\n```\n", str(ans), [str(w) for w in wrong],
             f"Each call doubles x and lowers y: f(3,4) → f(6,3) → f(12,2) → f(24,1) → f(48,0) = **{ans}**.", 'Recursion')


def pseudo_bitwise():
    a, b = 12, 10
    ans = (a & b) + (a | b) + (a ^ b)
    wrong = [(a & b) + (a | b), (a | b) + (a ^ b), (a & b) * 2 + (a ^ b) + 2, a + b + (a ^ b)]
    wrong = list(dict.fromkeys(w for w in wrong if w != ans))[:3]
    assert len(wrong) == 3
    code = f"Set integer a = {a}\nSet integer b = {b}\nPrint (a & b) + (a | b) + (a ^ b)"
    return T(f"What is the output of the following pseudocode? (`&` is bitwise AND, `|` OR, `^` XOR.)\n\n```text\n{code}\n```\n", str(ans), [str(w) for w in wrong],
             f"{a} = 1100 and {b} = 1010 in binary. AND = 1000 = {a & b}; OR = 1110 = {a | b}; XOR = 0110 = {a ^ b}. Sum = {a & b} + {a | b} + {a ^ b} = **{ans}**.", 'Bitwise')


# ---------------------------------------------------------------- verbal (authored)
RC_PASSAGE = ("In many crowded cities, open land is scarce and expensive. Some residents have responded by turning rooftops into small farms. "
              "Using containers filled with soil or simple water-based systems, they grow vegetables such as tomatoes, spinach and chillies. "
              "The practice lowers the household's food bills and gives families fresher produce. It also keeps buildings cooler, because plants absorb heat that would otherwise warm the roof. "
              "However, rooftop farming is not without problems. A roof must be strong enough to carry the weight of wet soil, and water must be carried up several floors. "
              "Pests can also spread between nearby roofs. City governments in several countries now offer training and small grants, hoping that more people will take up the idea. "
              "Supporters argue that, even if rooftop farms cannot feed a whole city, they make urban life greener and more self-reliant.")

RC = [
    T("According to the passage, rooftop farms help keep buildings cooler because", "plants absorb heat that would otherwise warm the roof.",
      ["they reflect sunlight with white paint.", "they block the rain from reaching the roof.", "the soil is always wet."],
      "The passage says so directly: ‘plants absorb heat that would otherwise warm the roof’.", 'Reading comprehension',
      pre=f"**Passage.** Read the passage and answer the five questions.\n\n> {RC_PASSAGE}\n"),
    T("Which of the following is **not** mentioned as a problem of rooftop farming?", "The high price of seeds.",
      ["The weight of wet soil on the roof.", "Carrying water up several floors.", "Pests spreading between roofs."],
      "The roof's strength, carrying water and pests are all named; seed prices are not mentioned.", 'Reading comprehension'),
    T("The word ‘self-reliant’ in the last sentence most nearly means", "able to depend on oneself.",
      ["dependent on others.", "extremely wealthy.", "growing quickly."],
      "‘Self-reliant’ = relying on oneself.", 'Reading comprehension'),
    T("The author's attitude towards rooftop farming is best described as", "cautiously positive.",
      ["strongly opposed.", "completely indifferent.", "wildly enthusiastic."],
      "The passage lists benefits, names real problems and reports supporters' limited claim (‘even if … cannot feed a whole city’): a cautiously positive view.", 'Reading comprehension'),
    T("Why do city governments offer training and small grants?", "To encourage more people to take up rooftop farming.",
      ["To raise the price of vegetables.", "To stop people using their roofs.", "To reduce the weight on roofs."],
      "The passage states: ‘hoping that more people will take up the idea’.", 'Reading comprehension'),
]

ERR = [
    T("Find the part of the sentence that has an error.\n\nNeither of the two candidates (a) / were able to answer (b) / all the questions correctly. (c) / No error (d)", "(b)", ["(a)", "(c)", "(d)"],
      "*Neither* takes a singular verb: ‘was able to answer’.", 'Spotting errors'),
    T("Find the part of the sentence that has an error.\n\nShe has been working (a) / in this company (b) / since five years. (c) / No error (d)", "(c)", ["(a)", "(b)", "(d)"],
      "*Since* needs a point in time; a length of time takes *for*: ‘for five years’.", 'Spotting errors'),
    T("Find the part of the sentence that has an error.\n\nThe furniture in the new office (a) / are made of (b) / teak wood. (c) / No error (d)", "(b)", ["(a)", "(c)", "(d)"],
      "*Furniture* is uncountable and singular: ‘is made of’.", 'Spotting errors'),
    T("Find the part of the sentence that has an error.\n\nEach of the students (a) / must submit (b) / his or her assignment by Friday. (c) / No error (d)", "(d)", ["(a)", "(b)", "(c)"],
      "*Each* is singular, ‘must submit’ is correct, and ‘his or her’ agrees with it. There is no error.", 'Spotting errors'),
]

SC = [
    T("The manager was so ___ with the quality of the work that he gave the team a bonus.", "impressed", ["disappointed", "unaware", "anxious"],
      "A bonus is a reward, so the feeling is positive: *impressed*.", 'Sentence completion'),
    T("Despite the heavy rain, the match ___ as planned.", "went ahead", ["was cancelled", "gets cancelled", "has gone ahead"],
      "*Despite* signals contrast with the rain, and the past tense fits: *went ahead*.", 'Sentence completion'),
    T("She is ___ of the two sisters.", "the taller", ["taller", "tallest", "the tallest"],
      "Two people: the comparative with *the* — *the taller of the two*.", 'Sentence completion'),
]

VOC = [
    T("Choose the word closest in meaning to **meticulous**.", "painstaking", ["careless", "hasty", "generous"], "*Meticulous* means very careful about details: *painstaking*.", 'Synonym'),
    T("Choose the word closest in meaning to **abundant**.", "plentiful", ["scarce", "fragile", "rare"], "*Abundant* = existing in large quantities: *plentiful*.", 'Synonym'),
    T("Choose the word opposite in meaning to **transparent**.", "opaque", ["clear", "thin", "bright"], "*Transparent* lets light through; its opposite is *opaque*.", 'Antonym'),
    T("Choose the meaning of the idiom ‘to burn the midnight oil’.", "to work late into the night", ["to waste fuel", "to start a fire", "to be very angry"], "It means studying or working far into the night.", 'Idiom'),
]

CLOZE6 = ("Every year, thousands of students (1) ___ for jobs through campus drives. A good preparation plan begins (2) ___ understanding the test pattern. "
          "Students who practise under timed conditions (3) ___ more confident on the day. They also learn (4) ___ manage their time across sections. "
          "(5) ___ , regular revision keeps the basics fresh.")
CLOZE_MOCK = [
    T("Blank (1):", "apply", ["applies", "applied", "applying"], "*Thousands of students* is plural and the sentence is general: **apply**.", 'Cloze',
      pre=f"**Passage.** Choose the best word for each numbered blank.\n\n> {CLOZE6}\n"),
    T("Blank (2):", "with", ["at", "by", "on"], "The phrase is *begins with*.", 'Cloze'),
    T("Blank (3):", "feel", ["feels", "felt", "feeling"], "*Students who practise … feel*: plural subject, general present.", 'Cloze'),
    T("Blank (4):", "to", ["for", "of", "at"], "*Learn to manage*: the infinitive.", 'Cloze'),
    T("Blank (5):", "Finally", ["Although", "Because", "Unless"], "The sentence adds a last point in the list; *Finally* fits, the others break the grammar.", 'Cloze'),
]

DS = T("Is x a single number? What is the value of x?\n\nI. x + y = 10 and y = 4.\nII. x² = 36.",
       "Statement I alone is sufficient", ["Statement II alone is sufficient", "Both statements together are needed", "Neither statement is sufficient"],
       "I gives x = 10 − 4 = 6. II gives x = 6 or x = −6, which is not one value. So **I alone is sufficient**.", 'Data sufficiency')

ESSAY_PROMPT = "Write an essay of about 190 words on **‘Social media and students’**, or a formal email to your principal requesting permission to hold a technical workshop. Time: 10 minutes."
