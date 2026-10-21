"""Infosys's own sample test (PDF author "Infosys Ltd", created 22 Sep 2020, hosted at
https://infytq.onwingspan.com/public-assets/InfosysCampusRecruitmentSampleTest-SystemsEngineer.pdf).

The PDF carries a CONFIDENTIAL watermark although it sits at a public asset path, so this library does NOT
reproduce its text. Each item below is a short paraphrased gist with the section and question number, so you can
open the PDF beside it. Every answer was derived here, and where a computer can decide it, it is decided by
execution (brute force over the real constraints, simulation, or a model search). Verbal items are judgement.
Run: python3 data/official_sample.py   (exits 1 if any executable check fails)
"""
import itertools, math, sys
from fractions import Fraction

ITEMS = []     # dicts: qid, section, sub, taxon, gist, answer, method, how ('executed' | 'judgement' | 'unsolved')


def item(qid, section, sub, taxon, gist, answer, method, how, check=None):
    ITEMS.append(dict(qid=qid, section=section, sub=sub, taxon=taxon, gist=gist, answer=answer, method=method, how=how, check=check))


# ======================================================================== Section 1: Reasoning
# --- Data interpretation: a thief, three computers, three tools, three months
def _thief():
    comps, tools, perips = ['Tejas', 'Prithvi', 'Vayu'], ['screwdriver', 'pliers', 'wire cutter'], ['printer', 'keyboard', 'monitor']
    months = ['January', 'February', 'March']
    sols = []
    for mc in itertools.permutations(comps):                 # computer attacked in each month
        for mt in itertools.permutations(tools):             # tool used in each month
            for cp in itertools.permutations(perips):        # peripheral taken from each computer (comps order)
                lost = dict(zip(comps, cp)); tool_of = dict(zip(mc, mt)); month_of = {c: m for m, c in zip(months, mc)}
                if mc[0] != 'Prithvi' or mt[0] == 'wire cutter': continue
                if not (lost['Vayu'] == 'keyboard' and tool_of['Vayu'] == 'pliers'): continue
                if not any(lost[c] == 'monitor' and tool_of[c] == 'wire cutter' for c in comps): continue
                if mc[2] != 'Tejas': continue
                sols.append((tool_of, lost, month_of))
    return sols


_s = _thief()
assert len(_s) == 1, len(_s)
_tool, _lost, _month = _s[0]
item('O01', 'reasoning', 'data interpretation (logic set)', 'A19', 'Thief, three computers, three tools: which tool was used on Tejas?', _tool['Tejas'], 'Enumerate all assignments; exactly one satisfies every clue', 'executed', lambda: _tool['Tejas'] == 'wire cutter')
item('O02', 'reasoning', 'data interpretation (logic set)', 'A19', 'Same set: in which month was the keyboard taken?', _month['Vayu'], 'Same unique assignment', 'executed', lambda: _month['Vayu'] == 'February')
item('O03', 'reasoning', 'data interpretation (logic set)', 'A19', 'Same set: which peripheral did Prithvi lose?', _lost['Prithvi'], 'Same unique assignment', 'executed', lambda: _lost['Prithvi'] == 'printer')
item('O04', 'reasoning', 'data interpretation (logic set)', 'A19', 'Same set: in which month was the wire cutter used? (fill in)', _month['Tejas'], 'Same unique assignment', 'executed', lambda: _month['Tejas'] == 'March')
item('O05', 'reasoning', 'data interpretation (logic set)', 'A19', 'Same set: which computer lost its monitor?', next(c for c in _lost if _lost[c] == 'monitor'), 'Same unique assignment', 'executed', lambda: _lost['Tejas'] == 'monitor')


# --- Data sufficiency (the official 1/2/3/4 answer scheme)
def classify(a, b, both):
    """1 = exactly one statement alone suffices; 2 = either alone; 3 = both together only; 4 = neither, even together."""
    if a and b: return 2
    if a != b: return 1
    return 3 if both else 4


def suff(universe, target, st):
    vals = {target(u) for u in universe if st(u)}
    return len(vals) == 1


# DS2: three consecutive integers X, Y, Z in some order, which is the highest?
U2 = [dict(zip('XYZ', p)) for n in range(1, 4) for p in itertools.permutations([n, n + 1, n + 2])]
hi = lambda u: max(u, key=u.get)
s2a = suff(U2, hi, lambda u: u['X'] + u['Y'] == 2 * u['Z'])
s2b = suff(U2, hi, lambda u: u['X'] > u['Y'])
s2ab = suff(U2, hi, lambda u: u['X'] + u['Y'] == 2 * u['Z'] and u['X'] > u['Y'])
# DS3: Rs 4 in 50 paisa and 1 rupee coins: how many 50 paisa coins?
U3 = [dict(a=a, b=b) for a in range(0, 9) for b in range(0, 5) if a * 50 + b * 100 == 400]
s3a = suff(U3, lambda u: u['a'], lambda u: u['a'] < u['b'])
s3b = suff(U3, lambda u: u['a'], lambda u: u['a'] + u['b'] == 5)
# DS4: alloy: two cost vectors that satisfy BOTH statements but give different copper costs
def alloy_ok(c, a, t):
    return Fraction(8 * 30 + 6 * c + 3 * a + t, 18) == 150 and a == c
ex4 = [(250, 250, 2460 - 9 * 250), (260, 260, 2460 - 9 * 260)]
assert all(alloy_ok(*e) for e in ex4) and ex4[0][0] != ex4[1][0]
# DS5: is the mean 2000?  two data sets satisfying BOTH statements, one with mean 2000 and one without
d5a = [880, 1999, 1999, 2390, 2390, 2342]
d5b = [880, 1000, 1500, 2100, 2200, 2390]
def st5(d): return min(d) == 880 and max(d) == 2390 and sum(1 for x in d if x > 2000) == len(d) // 2 and sum(1 for x in d if x < 2000) == len(d) // 2
assert st5(d5a) and st5(d5b) and Fraction(sum(d5a), 6) == 2000 and Fraction(sum(d5b), 6) != 2000
item('O06', 'reasoning', 'data sufficiency', 'A6', 'How many litres of juice can 375 trees give (oranges per tree; one cup per orange)?', '4 (cannot be determined)', 'A cup is not a volume in litres, so no statement fixes the answer', 'judgement')
item('O07', 'reasoning', 'data sufficiency', 'A6', 'Three consecutive integers X, Y, Z in no fixed order: which is highest?', '3 (both together)', 'Enumerated every assignment of three consecutive integers: I alone and II alone each leave two candidates; together only X', 'executed',
     lambda: classify(s2a, s2b, s2ab) == 3)
item('O08', 'reasoning', 'data sufficiency', 'A6', 'Rs 4 in 50-paisa and one-rupee coins: how many 50-paisa coins?', '1 (one statement alone: the second)', 'Enumerated (a, b): "fewer 50p than Re 1 coins" leaves two cases; "five coins in total" leaves one', 'executed',
     lambda: classify(s3a, s3b, suff(U3, lambda u: u['a'], lambda u: u['a'] < u['b'] and u['a'] + u['b'] == 5)) == 1)
item('O09', 'reasoning', 'data sufficiency', 'A6', 'Alloy in ratio 8:6:3:1, zinc Rs 30/kg: cost of copper per kg?', '4 (neither, even together)', 'Two different cost vectors satisfy both statements but give copper at Rs 250 and Rs 260', 'executed', lambda: all(alloy_ok(*e) for e in ex4) and ex4[0][0] != ex4[1][0])
item('O10', 'reasoning', 'data sufficiency', 'A6', 'Is 2000 the average GRE score? (range given; half above, half below 2000)', '4 (neither, even together)', 'Two data sets fit both statements, one with mean 2000 and one without; "half above" describes the median, not the mean', 'executed', lambda: st5(d5a) and st5(d5b) and Fraction(sum(d5a), 6) == 2000 and Fraction(sum(d5b), 6) != 2000)


# --- Deductive reasoning: choose logically related statements.  Model search: a triple is "logically related" when
#     one statement follows from the other two and needs BOTH of them.
def follows(premises, concl, sets, singles=(), n=5):
    idx = {s: i for i, s in enumerate(sets)}
    found = False
    for bits in itertools.product(range(2 ** len(sets)), repeat=n):
        if not all(any(m >> idx[s] & 1 for m in bits) for s in sets): continue
        if any(sum(m >> idx[s] & 1 for m in bits) != 1 for s in singles): continue
        if all(_h(p, bits, idx) for p in premises):
            found = True
            if not _h(concl, bits, idx): return False
    return found


def _h(stmt, bits, idx):
    k, a, b = stmt
    A = [i for i, m in enumerate(bits) if m >> idx[a] & 1]; B = [i for i, m in enumerate(bits) if m >> idx[b] & 1]
    return {'all': lambda: all(i in B for i in A), 'some': lambda: any(i in B for i in A), 'no': lambda: not any(i in B for i in A),
            'some_not': lambda: any(i not in B for i in A)}[k]()


def related(triple, sets, singles=()):
    """Ordered reading: the first two statements entail the third, and neither premise alone is enough."""
    p1, p2, concl = triple
    return follows([p1, p2], concl, sets, singles) and not follows([p1], concl, sets, singles) and not follows([p2], concl, sets, singles)


S3 = {'A': ('some_not', 'book', 'novel'), 'B': ('all', 'novel', 'fiction'), 'C': ('some', 'novel', 'fiction'), 'D': ('all', 'fiction', 'novel'), 'E': ('some_not', 'book', 'fiction')}
S4 = {'A': ('some', 'painter', 'farmer'), 'B': ('all', 'raman', 'farmer'), 'C': ('all', 'painter', 'choreo'), 'D': ('all', 'raman', 'painter'), 'E': ('some', 'farmer', 'choreo')}
S5 = {'A': ('some_not', 'fish', 'carn'), 'B': ('all', 'fish', 'swimmer'), 'C': ('all', 'fish', 'carn'), 'D': ('some_not', 'swimmer', 'carn'), 'E': ('some', 'swimmer', 'carn')}
opts3 = {'a': 'ADE', 'b': 'ABC', 'c': 'CED', 'd': 'DBA'}
opts4 = {'a': 'BAD', 'b': 'CDE', 'c': 'ACE', 'd': 'DAB'}
opts5 = {'a': 'DCB', 'b': 'EDA', 'c': 'BEC', 'd': None}
r3 = {k: related([S3[c] for c in v], ['book', 'novel', 'fiction']) for k, v in opts3.items()}
r4 = {k: related([S4[c] for c in v], ['painter', 'farmer', 'choreo', 'raman'], singles=('raman',)) for k, v in opts4.items()}
r5 = {k: related([S5[c] for c in v], ['fish', 'swimmer', 'carn']) for k, v in opts5.items() if v}
item('O11', 'reasoning', 'deductive reasoning (choose three)', 'A4', 'Nurses, demand, efficient: choose the three related statements (multi-select)', 'not solved', 'Multi-select with no stated rule for which triple counts; the official key is not published, so no answer is asserted', 'unsolved')
item('O12', 'reasoning', 'deductive reasoning (choose three)', 'A4', 'Rohan, jesters, magicians, criminals: choose the three related statements (multi-select)', 'not solved', 'Same: multi-select, key not published', 'unsolved')
item('O13', 'reasoning', 'deductive reasoning (combination)', 'A4', 'Books, novels, fiction: which triple is logically related?', 'a (ADE)', '"Only novels are fiction" plus "some books are not novels" give "some books are not fiction" (first two entail the third); only ADE passes', 'executed', lambda: [k for k, v in r3.items() if v] == ['a'])
item('O14', 'reasoning', 'deductive reasoning (combination)', 'A4', 'Painters, farmers, choreographers: which triple is logically related?', 'c (ACE)', '"All painters are choreographers" plus "some painters are farmers" give "some farmers are choreographers"; only ACE', 'executed', lambda: [k for k, v in r4.items() if v] == ['c'])
item('O15', 'reasoning', 'deductive reasoning (combination)', 'A4', 'Fishes, swimmers, carnivorous: which triple is logically related?', 'd (none of the above)', 'On the reading that the first two statements must entail the third, none of DCB, EDA, BEC works (B and C entail E, but BEC puts E second). On an unordered reading BEC would be the answer; the official key is not published', 'executed', lambda: [k for k, v in r5.items() if v] == [])

# ======================================================================== Section 2: Technical Ability
# --- LET + LEE = ALL with E = 5
sol = []
for L, T, A in itertools.permutations([d for d in range(10) if d != 5], 3):
    if L == 0 or A == 0: continue
    if 100 * L + 10 * 5 + T + 100 * L + 10 * 5 + 5 == 100 * A + 10 * L + L: sol.append((L, T, A))
assert len(sol) == 1, sol
L_, T_, A_ = sol[0]
val = A_ + L_ + L_
opts = {'a': L_, 'b': 10 * L_ + 5, 'c': 5, 'd': A_, 'e': 10 * T_ + L_}
match = [k for k, v in opts.items() if v == val]
item('O16', 'technical', 'cryptarithmetic', 'A20', 'LET + LEE = ALL with E = 5: find A + L + L', f"{'/'.join(match)} (value {val}; L={L_}, T={T_}, A={A_})", 'Brute force over all digit assignments: exactly one solution', 'executed', lambda: len(match) == 1)
cnt = sum(1 for p in itertools.product(range(3), repeat=5) if len(set(p)) == 3)
item('O17', 'technical', 'counting (onto assignments)', 'A18', '5 distinct chocolates into 3 distinct containers, none empty: ways?', f'b ({cnt})', '3^5 - 3·2^5 + 3 = 150, confirmed by listing all 243 assignments', 'executed', lambda: cnt == 150 == 3 ** 5 - 3 * 2 ** 5 + 3)
vow = set('EOA')
arr = sum(1 for p in itertools.permutations('KEYBOARD') if all(i % 2 == 0 for i, ch in enumerate(p) if ch in vow))
item('O18', 'technical', 'counting (arrangements)', 'A18', 'Arrangements of KEYBOARD with the vowels only in odd places?', f'a ({arr})', 'P(4,3) × 5! = 24 × 120, confirmed by listing all 40,320 arrangements', 'executed', lambda: arr == 2880 == math.perm(4, 3) * math.factorial(5))
seq = [0, 2, 5, 10, 17, 28, 41]
item('O19', 'technical', 'number series', 'A2', 'Missing term in 0, 2, 5, 10, 17, _, 41', '28', 'Gaps are the consecutive primes 2, 3, 5, 7, 11, 13', 'executed', lambda: [seq[i + 1] - seq[i] for i in range(6)] == [2, 3, 5, 7, 11, 13])
x = Fraction(24)
item('O20', 'technical', 'mixtures (replacement)', 'A9', '8 L drawn from a can of milk and replaced by water, four times in all; milk : total = 16 : 81. Original quantity?', 'c (24 litres)', '(1 - 8/x)^4 = 16/81 gives 1 - 8/x = 2/3, so x = 24', 'executed', lambda: (1 - Fraction(8) / x) ** 4 == Fraction(16, 81))

# --- Logical reasoning: who comes to Jon Snow's wedding (conditional rules), brute force over 2^7
names = ['Petyr', 'Qhorin', 'Ramsay', 'Sansa', 'Theon', 'Umar', 'Varys']
def ok(a):
    P, Q, R, S, T, U, V = a
    return (not P or not U) and (not S or not T) and (T or not R) and (R or (P and Q))
W = [a for a in itertools.product([0, 1], repeat=7) if ok(a)]
always_absent_given_Q = [names[i] for i in range(7) if all(not a[i] for a in W if a[1])]
givenR = [a for a in W if not a[2]]
givenU = [a for a in W if a[5]]
q2 = {'a: Petyr and Theon do not come': all(not a[0] and not a[4] for a in givenR), 'b: Umar does not come': all(not a[5] for a in givenR),
      'c: Theon comes': all(a[4] for a in givenR), 'd: Sansa does not come and Qhorin comes': all((not a[3]) and a[1] for a in givenR)}
q3 = {'a: Theon comes': any(a[4] for a in givenU) and not all(a[4] for a in givenU)}
q3_must_not = {'a: Theon comes': all(not a[4] for a in givenU), 'b: Varys comes': all(not a[6] for a in givenU), 'c: Ramsay does not come': all(a[2] for a in givenU), 'd: Qhorin does not come': all(a[1] for a in givenU)}
groups = {'a': {'Theon', 'Umar', 'Petyr', 'Qhorin'}, 'b': {'Varys', 'Ramsay', 'Umar'}, 'c': {'Sansa', 'Qhorin', 'Theon', 'Ramsay'}, 'd': {'Ramsay', 'Umar', 'Sansa'}}
okg = {k: ok(tuple(1 if n in g else 0 for n in names)) for k, g in groups.items()}
free = [names[i] for i in range(7) if all(ok(tuple(1 if j == i else a[j] for j in range(7))) for a in W)]
item('O21', 'technical', 'logical reasoning (conditional rules)', 'A19', 'Wedding guests with if-then rules: if Qhorin comes, who must stay away?', 'e (nobody is forced to stay away)', 'Checked all 128 attendance patterns against the four rules', 'executed', lambda: always_absent_given_Q == [])
item('O22', 'technical', 'logical reasoning (conditional rules)', 'A19', 'If Ramsay does not come, what must be true?', 'b (Umar does not come)', 'No Ramsay forces Petyr and Qhorin to come, and Petyr coming rules Umar out; checked all 128 patterns', 'executed', lambda: [k for k, v in q2.items() if v] == ['b: Umar does not come'])
item('O23', 'technical', 'logical reasoning (conditional rules)', 'A19', 'If Umar comes, which statement must NOT be true?', 'c (Ramsay does not come)', 'If Umar comes, Petyr cannot, so Ramsay must come; checked all 128 patterns', 'executed', lambda: [k for k, v in q3_must_not.items() if v] == ['c: Ramsay does not come'])
item('O24', 'technical', 'logical reasoning (conditional rules)', 'A19', 'Which listed group could be exactly the attendees?', 'e (none of the listed groups works)', 'Each listed group breaks at least one rule', 'executed', lambda: not any(okg.values()))
item('O25', 'technical', 'logical reasoning (conditional rules)', 'A19', 'Who can attend regardless of who else attends?', 'Varys (and also Qhorin)', 'Adding them never breaks a rule, because neither appears on the "if" side of any rule', 'executed', lambda: free == ['Qhorin', 'Varys'])

# ======================================================================== Section 3: Verbal (judgement)
V = [
 ('O26', 'critical reasoning', 'V6', 'Computer chips from Japan and US missile accuracy: which statement strengthens the argument?', 'a', 'It ties missile accuracy to computer quality, the link the argument needs'),
 ('O27', 'critical reasoning', 'V6', 'Ethanol blending and "Jetrol": which statement weakens the argument?', 'a', 'A fuel that pollutes three times more removes the claimed benefit'),
 ('O28', 'critical reasoning', 'V6', 'Health of income groups (heights, infant deaths): what can be inferred?', 'c', 'Nutrition is one factor and is not without significance; the others overreach'),
 ('O29', 'English corrective usage', 'G1', 'Fill the blank after "raises transaction costs and ___ in the economy"', 'a (inefficiencies)', 'The only noun that fits "transaction costs and ..."'),
 ('O30', 'English corrective usage', 'G1', 'Fill the blank: majority of emotional and physical problems ___ the stresses of life', 'c (have their origins in)', 'Plural subject, "origins in"'),
 ('O31', 'English corrective usage', 'G1', 'Fill the blank: music retailing relies on walk-ins and ___', 'a (impulse purchase)', 'Walk-in customers buy on impulse'),
 ('O32', 'English corrective usage', 'G1', 'Fill the blank: what has happened since is a ___ of fortune', 'b (startling reversal)', '"Reversal of fortune" is the fixed phrase'),
 ('O33', 'English error correction', 'V3', 'Skeptics emphasise conditions that fluctuate "and also has ..." : best replacement', 'b (and have a significant psychological component)', 'Plural subject "conditions" needs "have"'),
 ('O34', 'English error correction', 'V3', 'Dutch Health Council found "none of the evidence ... were harmful": best replacement', 'c (no evidence ... was harmful)', 'Singular uncountable "evidence" takes "was"'),
 ('O35', 'English error correction', 'V3', 'Fear of an enemy "is definitely to be an instinctive quality": best replacement', 'c (is certainly an instinctive quality)', 'Removes the awkward "definitely to be"'),
 ('O36', 'English error correction', 'V3', 'Globalization "too uses ... relationships as well for creating": best replacement', 'b (social and political relationships to create)', 'Plural noun and "to create"; removes the redundancy'),
 ('O37', 'English error identification', 'V2', 'Passionate efforts "on their own have the ability ...": which sentence is correct?', '1', 'Plural subject, plural pronoun, plural verb, "legendary"'),
 ('O38', 'English error identification', 'V2', 'Another relief for airlines and shipping: which sentence is correct?', '3', '"in relation to" and "hospitality" are right; the others have "An other", "have", "hospitability"'),
 ('O39', 'English error identification', 'V2', 'Power sector gains if the coal scheme works: which sentence is correct?', '2', '"can gain ... scheme ... works" agrees in number and tense'),
 ('O40', 'English error identification', 'V2', 'Earning endorsements is a primary challenge: which sentence is correct?', '3', '"is one of the primary challenges that we face every day"'),
 ('O41', 'reading comprehension', 'V1', 'Shakespeare\'s comedies: what is noted about the techniques?', 'b (consistently employed in his comedies)', 'The passage says they stay consistent across the comedies'),
 ('O42', 'reading comprehension', 'V1', 'What is the content of Shakespeare\'s comedies?', 'a (love and marriage)', 'Stated directly'),
 ('O43', 'reading comprehension', 'V1', 'Which statement is understood from the passage?', 'b (techniques consistently evident in all his comedies)', 'Matches the passage; the others misstate it'),
 ('O44', 'reading comprehension', 'V1', 'Where is the lower class made fun of (Dogberry and Verges)?', 'd (Much Ado About Nothing)', 'Named in the passage'),
 ('O45', 'reading comprehension', 'V1', 'Why are the comedies treasured?', 'd (the intuitive use of the techniques)', 'The closing sentence'),
]
for qid, sub, taxon, gist, ans, why in V:
    item(qid, 'verbal', sub, taxon, gist, ans, why, 'judgement')

# ======================================================================== Section 4: Pseudocode (executed)
def p1():
    n = 90
    return 'b (not within the range)' if not (n > 90 and n < 95) else 'a'
def p2():
    a, b, c = 6, 3, 2
    if b > a and a > c and c > b: b = a + 1
    else: a = b + 1
    return a + b + c
def p3():
    j = k = 1; out = []
    for i in range(1, 6): out.append(k); j += 1; k += j
    return ' '.join(map(str, out))
def p4():
    a, b = 10, 6
    while b: a, b = b, a % b
    return a
def p5():
    k = 6; out = []
    for i in range(1, 2):
        for j in range(i, 2): out.append(k + 1)
    return out[0]
item('O46', 'pseudocode', 'if / else', 'P6', 'Number = 90 tested against 90 < Number < 95: what is displayed?', p1(), 'The condition 90 > 90 is false, so the else branch runs', 'executed', lambda: p1().startswith('b'))
item('O47', 'pseudocode', 'if / else', 'P6', 'a=6, b=3, c=2 with a three-way condition, else a=b+1: print a+b+c', str(p2()), 'Condition is false, so a = 4; 4 + 3 + 2 = 9', 'executed', lambda: p2() == 9)
item('O48', 'pseudocode', 'loop (series)', 'P1', 'Loop i = 1..5 printing k, then j = j+1, k = k+j: which series?', 'a (' + p3() + ')', 'Trace j and k each pass: triangular numbers', 'executed', lambda: p3() == '1 3 6 10 15')
item('O49', 'pseudocode', 'while loop (Euclid)', 'P7', 'Function with while(b): temp = a MOD b ... called with a=10, b=6', 'a (' + str(p4()) + ')', 'This is Euclid\'s algorithm: gcd(10, 6) = 2', 'executed', lambda: p4() == 2)
item('O50', 'pseudocode', 'nested loop', 'P1', 'For i from 1 to 1, for j from i to 1: print k+1 with k = 6', 'c (' + str(p5()) + ')', 'The body runs once: 6 + 1 = 7', 'executed', lambda: p5() == 7)

# ======================================================================== Section 5: Puzzles (figures read from the PDF images)
g1 = [[4, 2, 6], [5, 2, 8], [6, 1, 11]]
rs = [sum(r) for r in g1]
q_ans1 = rs[2] + 3 * 1                           # next row sums continue +3: 21, 24, 27
g2_rows = [rs[2] + 3, rs[2] + 6, rs[2] + 9]
miss = g2_rows[0] - (7 + 5)
item('O51', 'puzzle', 'grid (row sums continue a series)', 'Z1', '3x3 grids: first grid\'s row sums are 12, 15, 18; fill the missing cell of the second (3 marks)', f'c ({miss})',
     'Row sums rise by 3 and carry on into the second grid: 21, 24, 27, so 7 + 5 + ? = 21', 'executed', lambda: rs == [12, 15, 18] and miss == 9 and [sum([8, 8, 8]), sum([9, 10, 8])] == g2_rows[1:])
f = lambda t, l, r, b: 2 * (t + l + r + b)
item('O52', 'puzzle', 'plus-shaped figure (centre from arms)', 'Z2', 'Plus figures: arms 7,4,6,8 give 50 and 1,12,20,7 give 80; find the centre for 13,11,9,14 (2 marks)', f'b ({f(13, 11, 9, 14)})',
     'Centre = 2 × (sum of the four arms)', 'executed', lambda: f(7, 4, 6, 8) == 50 and f(1, 12, 20, 7) == 80 and f(13, 11, 9, 14) == 94)
bx = lambda a, b: a ** 3 + b ** 3 + a + b
item('O53', 'puzzle', 'circles (cubes and a box)', 'Z2', 'Circles 4→64 and 3→27 give 98; 6→216 and 2→8 give 232; third pair 9→729 and A→125 (2 marks)', f'A = 5 (a) and B = {bx(9, 5)} (c)',
     'Each box = cube + cube + sum of the two small numbers: 64+27+7 = 98; 216+8+8 = 232; so A = 5 and B = 729+125+14', 'executed', lambda: bx(4, 3) == 98 and bx(6, 2) == 232 and 5 ** 3 == 125 and bx(9, 5) == 868)
dsum = lambda n: sum(map(int, str(n)))
mid = [dsum(a) + dsum(b) for a, b in zip([16, 25, 36, 49], [25, 36, 49, 64])]
low = [dsum(a) + dsum(b) for a, b in zip([14, 16, 22], [16, 22, 23])]
item('O54', 'puzzle', 'zig-zag rows (digit sums of neighbours)', 'Z2', 'Rows 16,25,36,49,64 → 14,16,22,23 → 12,X,9: find X (3 marks)', f'{low[1]}',
     'Each number is the digit-sum of its upper-left neighbour plus the digit-sum of its upper-right neighbour', 'executed', lambda: mid == [14, 16, 22, 23] and low[0] == 12 and low[2] == 9 and low[1] == 11)


def verify():
    bad, n_exec, n_judg, n_uns = [], 0, 0, 0
    for it in ITEMS:
        if it['how'] == 'executed':
            n_exec += 1
            try:
                if not it['check']():
                    bad.append(it['qid'])
            except Exception as e:
                bad.append(f"{it['qid']} ({e})")
        elif it['how'] == 'judgement': n_judg += 1
        else: n_uns += 1
    return bad, n_exec, n_judg, n_uns


if __name__ == '__main__':
    bad, e, j, u = verify()
    print(f"official sample: {len(ITEMS)} items | {e} decided by execution, {j} by judgement (verbal, units), {u} not solved (multi-select, no key) | failed checks: {bad or 'none'}")
    print('Q21 absent given Qhorin:', always_absent_given_Q, '| Q22:', {k: v for k, v in q2.items()}, '| Q23 must-not:', {k: v for k, v in q3_must_not.items()}, '| Q24 groups ok:', okg, '| Q25 free:', free)
    print('deductive (ordered reading):', r3, r4, r5)
    print('LET+LEE=ALL', sol, 'A+L+L =', val, 'options', opts, '->', match)
    sys.exit(1 if bad else 0)
