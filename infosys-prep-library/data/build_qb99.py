"""Generates question-banks/QB-99-OBSERVED-POOL.md from questions-observed.csv plus the worked
explanations below. Question text and answers come from the CSV only, so the pool cannot drift
from the data that verify_observed.py checks."""
import csv
from collections import Counter

SRC = {
 'YT-5XTG': 'OnlineStudy4u video, 2025-10-09 — candidates\' recall of the early-October 2025 SE slots',
 'YT-2NTB': 'Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination"',
 'YT-2YHL': 'OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated',
 'YT-U7HK': 'OnlineStudy4u video, 2026-09-18 — "PYQ … 4th/11th/16th October 2025"',
 'YT-2MBO': 'OnlineStudy4u video, 2026-09-22 — "PYQ … one or two years old"',
 'YT-6UFT': 'OnlineStudy4u video, 2025-09-27 — "Infosys previous-year puzzles"',
 'YT-HZGK': 'Code Bashers video, 2024-12-18 — "latest pseudo code questions asked in SE hiring"',
 'YT-KC2G': 'Tekno UF video, 2024-11-04 — candidate reports from the 3 Nov 2024 exam',
 'B1': 'First-hand Naukri Code360 account, on-campus SE test of 12 May 2025',
}

W = {
'R01': "Take the mean of the letters' alphabet positions. LAST = (12+1+19+20)/4 = 52/4 = 13. TABLE = (20+1+2+12+5)/5 = 40/5 = 8. FRAUD = (6+18+1+21+4)/5 = 50/5 = **10**.\n\n**Pattern to remember:** when a word maps to a small number, try the letter sum first, then sum ÷ length.",
'R02': "Differences are 11, 25, 45, 71; second differences 14, 20, 26 rise by 6. Faster: the terms are n³ + n² + n → 3, 14, 39, 84, 155, **258**, 399 (216 + 36 + 6 = 258; 343 + 49 + 7 = 399 checks the last term).",
'R03': "Three independent tracks, each with gaps +1, +2, next +3. Letters H→I→K→**N**; numbers 47→48→50→**53**; letters F→G→I→**L**. Answer **N53L**.",
'R04': "Statement I: x + (x+2) + (x+4) + (x+6) = 132 → 4x = 120 → x = **30**. Sufficient. Statement II: the gap between the smallest and largest of **any** four consecutive even numbers is 6, so it carries no information. **I alone is sufficient.**",
'R05': "Sum of alphabet positions. BURST = 2+21+18+19+20 = 80. LAKE = 12+1+11+5 = 29. VERSATILE = 22+5+18+19+1+20+9+12+5 = **111**.\n\n**Speed tip:** memorise E=5, J=10, O=15, T=20, Y=25 (\"EJOTY\") and count from the nearest anchor.",
'R06': "Odd positions keep their alphabet number, even positions become 0. CHAIR → C=3, 0, A=1, 0, R=18 → 301018. TABLE → T=20, 0, B=2, 0, E=5 → **200205**.",
'R07': "Each term is twice the sum of the previous two: 2(1+0)=2, 2(2+1)=6, 2(6+2)=16, 2(16+6)=44, 2(44+16)=120, 2(120+44)=**328**.",
'R08': "Squares with reversed roots: 12², 21², 13², 31², 14², then **41² = 1681**. The source's option letter was inaudible; 1681 is the only value the rule allows.",
'R09': "Divide, then add the digits of the quotient **once**. 264÷2 = 132 → 1+3+2 = 6. 870÷3 = 290 → 2+9+0 = 11 (note: not reduced again to 2). 735÷5 = 147 → 1+4+7 = **12**.",
'R10': "Draw a counter-model: shoes inside legs; pairs overlapping legs only outside shoes; hands overlapping pairs only outside legs. All three statements hold and neither conclusion does. Two chained \"some\" statements never force a definite link. **Neither follows.**",
'R11': "Three tracks. Numbers 3, 8, 15, 24, 35 are 2²−1 … 6²−1, so next is 7²−1 = 48. Letters Y, W, U, S, Q step back 2 → **O**. Last numbers 6, 8, 10, 12, 14 → 16. Answer **48O16** (the source read the option as \"48 O\").",
'R12': "Subtract the digit product: 135 − 5×9 = 90; 122 − 4×8 = 90; 144 − 9×6 = 90. So $ab = a×b + 90. The offered answer 168 comes from 13×6 + 90. **168.**\n\n**Flag:** reading 136 as 1, 3, 6 gives 1×3×6 + 90 = 108. The question is ambiguous as recalled; 168 is the option the source offered.",
'R13': "Decode each symbol. S − P: S is P's father. P + M: P is M's sister, so M is P's sibling and therefore also S's child. M × G: M is G's **brother**, which fixes M as male. So M is S's son → **S − P + M × G**.\n\nOnly this option was audible in the source. Distractors to practise against: P × M − S (P is M's brother, M is S's father — wrong direction); S + P − M (S is a sister); M − S + P (M is S's father).",
'R14': "Reverse the word, then shift every letter back by one. CREATE → ETAERC → DSZDQB. POLITE → ETILOP → E−1 = D, T−1 = S, I−1 = H, L−1 = K, O−1 = N, P−1 = O → **DSHKNO**.\n\nThe transcript heard the code as \"DSJDQB\"; only DSZDQB (A−1 wraps to Z) is consistent with the answer the source gave.",
'R15': "Positions 1-2 swap, 3 stays, 4-5 swap. BREAK → R B E K A. BRIEF → **R B I F E**.\n\nReported from shift 1 of the early-October 2025 SE exam.",
'R16': "Consecutive primes: 13, 17, 19, 23, 29, **31**.",
'R17': "Numbers are odd 1, 3, 5, 7, 9; letters D, F, H, J, L step +2. Missing term **3F**.",
'R18': "Numbers 12, 13, 14, 15; letters M, O, Q, S step +2. Missing term **13O**.",
'R19': "Two series interleaved. Odd places: 100, 80, 60, **40** (−20). Even places: 20, 50, 80 (+30). The 7th term is in the odd series: **40**.",
'R20': "Differences 3, 6, 9, 12, 15. 109 + 12 = **121**, and 121 + 15 = 136 confirms it.",
'Q01': "Eliminate x: 5×(2x + 3y = 7) → 10x + 15y = 35; 2×(5x + 8y = 2) → 10x + 16y = 4. Subtract: y = −31. Then 2x = 7 + 93 → x = 50. **x > y.**",
'Q02': "Three years ago: 45. Three years hence: 75. 45 : 75 = **3 : 5**.",
'Q03': "Shorter than 170 cm = the first three classes: 150 + 88 + 70 = 308. 308/400 = **77%**. Check the table sums to 400 (150+88+70+50+42 = 400) — if it did not, the recall would be suspect.",
'Q04': "Old mean = 2100/15 = 140. Doubling and subtracting 10 applies the same to the mean: 2×140 − 10 = 270. Increase = **130**.\n\n**Rule:** a linear change to every data point (ax + b) changes the mean the same way. It does not need the individual values.",
'Q05': "Assume all 45 are hens: 90 legs. The extra 40 legs come from cows, 2 extra each → **20 cows**.",
'Q06': "The keypad digits are 0–9. The primes are 2, 3, 5, 7. \"Non-prime\" is intended as the **composites** 4, 6, 8, 9: 4×6×8×9 = 1728 = 12³. Cube root **12**.\n\n**Trap worth knowing:** 0 and 1 are also non-prime. Including 0 makes the product 0. On the real test, pick the reading that produces an offered option.",
'Q07': "Convert percentages of 400: English 100, Hindi 136, Maths 72, Science **40**, History 52. Only Science is below 50 → failed in Science. Best − worst = 136 − 40 = **96**.\n\n**Source defect:** the stem says marks are \"out of 100\", but Hindi comes to 136. The recall is internally inconsistent; the answer stands on the chart data.",
'Q08': "4πr² = 154 → r² = 154 × 7/88 = 12.25 → r = 3.5. V = (4/3) × (22/7) × 3.5³ = 539/3 ≈ **179.67 cm³**. The source said \"around 180\".",
'P01': "w runs 0..5. Integer division: w/2 == 0 only for w = 0 and 1. Of those, only 0 is even. Output **0**.",
'P02': "27 mod 7 = 6. The loop displays **0 1 2 3 4 5 6**.",
'P03': "In C and Java, `+` binds tighter than `&`, which binds tighter than `^`: p = 1 ^ (1 & (1+1)) ^ (1 & 1) = 1 ^ 0 ^ 1 = 0. Reading strictly left to right also gives p = 0. Either way p + q = 0 + 1 = **1**.\n\n**Know the order:** arithmetic > shifts > relational > `&` > `^` > `|` > `&&` > `||`.",
'P04': "x starts at 0. Each pass: ++x makes 1, display 1, x-- returns it to 0. The test 0 ≥ −1 is always true. **Infinite loop printing 1.**",
'P05': "Add 5 until n is divisible by 8: 26→31→36→41→46→51→56 (six additions, i = 6). Then n + i = 56 + 6 = **62**.",
'P06': "result = 3×1 + 3×2 = **9**.",
'P07': "5! = 5×4×3×2×1 = **120**.",
'P08': "Digit sum of 123 with integer division: 3 + 2 + 1 = **6**.",
'P09': "Odd i add i: 1 + 3 + 5 = 9. Even i add i²: 4 + 16 + 36 = 56. Total **65**.",
'P10': "calc(a, b) = a^b: 6³ = **216**.",
'P11': "f(7,2) → f(9,1) → f(10,0) → **10**.",
'P12': "Product of all = 2×3×4×5 = 120. Divide by each element: 60, 40, 30, 24. Output **60 40 30 24**.",
'P13': "`result = ++i` increments first, then assigns: i = 6, result = 6. `result = i++` gives result 5, i 6. `result = i + 1` leaves i at 5. `result = --i + 2` gives 6 but leaves i at 4. **result = ++i.**\n\nOnly the answer was audible in the source; the other three options here are authored.",
'P14': "Java evaluates operands left to right. i = 2: `++i` → 3 (i = 3), then `++i` → 4 (i = 4). 3 + 4 = **7**. The other combinations: `i++ + i++` = 2 + 3 = 5; `i++ + ++i` = 2 + 4 = 6; `++i + i++` = 3 + 3 = 6.\n\n**Warning:** in C this expression is undefined behaviour. Infosys pseudocode assumes the Java-style left-to-right reading.",
'P15': "The function tracks the longest **strictly** increasing run. [1, 2, 2, 3, 4, 5, 1]: 1→2 (run 2), 2→2 resets (not >), 2→3→4→5 (run 4), 5→1 resets. Answer **4**.\n\n**The trap:** 1, 2, 2, 3, 4, 5 looks like a run of 6, but the repeated 2 breaks it.",
'Z01': "Every complete row sums to 15 (1+5+6+3, 9+1+2+3, 1+1+6+7). Last row: 4 + 1 + 2 + ? = 15 → **8**.",
'Z02': "Each row is a, b, a×b, b². 7, 6, 42, 36; 8, 4, 32, 16; 10, 12, 120, **144**.",
'Z03': "Centre = (first × second) − (third × fourth). 3×7 − 5×1 = 16; 9×8 − 34×2 = 4; 15×12 − 21×8 = 180 − 168 = **12**.",
'Z04': "Each value is the sum of its opposite pair: 36+12 = 48, 8+32 = 40, 16+25 = 41, 39+7 = **46**.",
'Z05': "Centre = product of one pair + product of the other. 11×4 + 2×2 = 48; 7×7 + 5×6 = 79; 8×8 + 12×9 = 64 + 108 = **172**.",
'Z06': "a × b + 3: 5×11+3 = 58; 12×8+3 = 99; 16×7+3 = **115**.",
'Z07': "Fourth = second × third + first. 3×6+8 = 26; 9×12+4 = 112; 7×2+5 = 19; 6×4+9 = **33**.\n\nReported as a 4×4 matrix puzzle from the early-October 2025 slots.",
'Z08': "Difference of squares: 15² − 10² = 225 − 100 = 125; 18² − 11² = 203; 21² − 16² = 441 − 256 = **185**.\n\nStudents called this the hardest puzzle of the slot. The middle value was inaudible in the source and is filled in by the same rule.",
'Z09': "First = second × third: 4×5 = 20, 6×8 = 48, 8×4 = **32**.",
'Z10': "Multiply the digits of the top number and the bottom number, then add. 32 & 46: 3×2 + 4×6 = 30 ✓. 51 & 61: 5×1 + 6×1 = 11 ✓. 35 & 43: 3×5 + 4×3 = **27**.",
'Z11': "Third = n(n+1)/2 (triangular numbers): 10, 15, 21, 36, then 9×10/2 = **45**.",
'Z12': "Every entry is the product of its pair. (?, 4) → 28 → **7**.",
'Z13': "Digit product of the first minus digit product of the second: 5×8 − 7×5 = 5; 9×6 − 3×8 = 30; 6×2 − 2×3 = **6**.",
'Z14': "Add the pair, then take the digit sum: 43+17 = 60 → 6; 63+27 = 90 → 9; 44+56 = 100 → **1**.",
'Z15': "Plain product: 11×32 = 352, 12×33 = 396, 13×34 = **442**.",
'V01': "\"It's\" means \"it is\". The possessive is **its**. Error in part 2: *expressed **its** concern over …*",
}

def main():
    rows = [r for r in csv.DictReader(open('questions-observed.csv')) if r['source'] != 'OFF-2020']
    exam = [r for r in rows if r['section'] not in ('interview',) and not r['duplicate_of']]
    dups = [r for r in rows if r['duplicate_of']]
    disc = list(csv.DictReader(open('questions-discarded.csv')))
    iv = [r for r in rows if r['section'] == 'interview']
    order = [('reasoning', 'Reasoning Ability'), ('quant', 'Technical Ability (mathematical)'),
             ('pseudocode', 'Pseudocode'), ('puzzle', 'Numerical Puzzle'), ('verbal', 'Verbal Ability'),
             ('essay', 'English Writing')]
    by = Counter(r['section'] for r in exam)
    L = []
    L.append('# QB-99 — Observed Question Pool\n')
    L.append('**Every question in this file was reported by a source as asked in the Infosys Systems Engineer test.** Nothing here is authored except where a line says so. Items whose data the source lost are listed at the bottom with the reason, not quietly dropped.\n')
    L.append('**Every numeric and trace answer was re-derived by running `data/verify_observed.py`:**\n\n```bash\npython3 data/verify_observed.py\n```\n')
    L.append(f'**Size and honesty.** {len(exam)} unique questions from 8 videos and one first-hand account, plus {len(iv)} first-hand interview questions. **All but one of the question sources are coaching videos relaying candidate recall.** That makes each item `[REPORTED]` at best: a coach saying "this was asked" is not the same as a dated paper. Where two channels independently presented the same item it is `[LIKELY]`. Use the pool to calibrate style and difficulty, then get volume from the topic question banks.\n')
    L.append('| Section | Unique items | Oldest source | Newest source |\n|---|---|---|---|')
    for key, name in order:
        rs = [r for r in exam if r['section'] == key]
        if rs:
            L.append(f"| {name} | {len(rs)} | {min(r['source_date'] for r in rs)} | {max(r['source_date'] for r in rs)} |")
    L.append(f"| **Total** | **{len(exam)}** | | |\n")
    L.append('**How to use it.** Cover the answer, set a timer at the real per-question pace (Reasoning 100 s, Technical 3.5 min, Pseudocode 2 min, Puzzle 2.5 min), and only then open the working.\n\n---\n')
    n = 0
    for key, name in order:
        rs = [r for r in exam if r['section'] == key]
        if not rs: continue
        L.append(f'## {order.index((key, name)) + 1}. {name} — {len(rs)} items\n')
        for r in rs:
            n += 1
            L.append(f"### {r['qid']}. {r['subsection'][0].upper() + r['subsection'][1:]}\n")
            L.append(f"> {r['question_text']}\n")
            if r['options'] and r['options'] not in ('4 options', 'standard DS options'):
                L.append(f"*Options as recovered:* {r['options']}\n")
            tag = r['confidence']
            if r['qid'] in ('W01',):
                L.append('<details><summary>How to approach it</summary>\n\nTen minutes, about 190–200 words, four paragraphs: define the problem (the ozone layer absorbs UV-B; CFCs and halons break O₃ down, most visibly as the Antarctic ozone hole); effects (skin cancer, cataracts, crop and marine damage); response (the 1987 Montreal Protocol phased out CFCs, and the layer is recovering); one-line conclusion. Grammar and coherence are marked, not originality. Full method in `topics/W1-english-writing.md`.\n')
            else:
                L.append(f"<details><summary>Answer and working</summary>\n\n**Answer: {r['verified_answer']}**\n\n{W[r['qid']]}\n")
            dup = [d for d in dups if d['duplicate_of'] == r['qid']]
            extra = f" · also presented independently by {dup[0]['source']} ({dup[0]['source_date']})" if dup else ''
            note = f"\n\n*Note:* {r['notes']}" if r['notes'] and r['qid'] not in ('R12', 'R13', 'R14', 'Q06', 'Q07', 'P13', 'P14', 'Z08') else ''
            L.append(f"**Source:** {SRC.get(r['source'], r['source'])}{extra} · `[{tag}]` · verified by {'execution' if 'verify' in r['verification_method'] else r['verification_method']}{note}\n</details>\n\n---\n")
    L.append('## 7. Interview questions — first-hand, 2024-25\n')
    L.append('These come from five first-hand accounts (B1–B5 in `data/reviews-online.csv`). Model answers are in `interview/`.\n')
    L.append('| ID | Account | Date | Type | Question |\n|---|---|---|---|---|')
    for r in iv:
        L.append(f"| {r['qid']} | {r['source']} | {r['source_date']} | {r['subsection']} | {r['question_text']} |")
    L.append('\n**What recurs:** SDLC in four of five accounts, OOP in three, projects in three. Behavioural questions (rejection, stress, time management, relocation) replace a separate behavioural test.\n')
    L.append('## 8. Repeat rate\n')
    L.append(f'- **Independent repeats:** {len(dups)} of {len(exam)} unique questions ({100*len(dups)/len(exam):.1f}%) were presented by two different channels: '
             + ', '.join(f"{d['duplicate_of']}" for d in dups) + '. Both channels may share one upstream PYQ file, so treat this as corroboration that the item circulates, not as a measured exam repeat.')
    L.append('- **Cross-slot repeats cannot be measured.** No source ties one question to two different slots or dates.')
    L.append('- **Same-channel reuse** (OnlineStudy4u showing the same slide in 2025 and 2026) is not counted.\n')
    L.append('## 9. Verification record\n')
    L.append('| Check | Result |\n|---|---|')
    L.append('| `verify_observed.py` | every reasoning, quant, pseudocode and puzzle answer recomputed; **0 mismatches** after two verifier bugs were fixed (see `research/04-qa-report.md`) |')
    L.append('| Source answers that differ from ours | R08 (option letter inaudible), R12 (ambiguous reading, flagged), Q07 (stem defective, flagged) |')
    L.append('| Pseudocode in Java | all 15 observed pseudocode items (P01–P15) re-run as real Java by `data/verify_generated.py` |\n')
    L.append(f'## 10. Discarded items — {len(disc)}, with reasons\n')
    L.append('| ID | Source | Item | Why discarded |\n|---|---|---|---|')
    for d in disc:
        L.append(f"| {d['disc_id']} | {d['source']} | {d['item']} | {d['reason']} |")
    L.append('\nAll of these are auto-caption losses: the question was on screen and the presenter never read the data aloud. They still count as evidence of section content (grid puzzles, data sufficiency, DI) in `data/analyze.py`, but not as study material.')
    open('../question-banks/QB-99-OBSERVED-POOL.md', 'w').write('\n'.join(L) + '\n')
    print(f'QB-99: {n} items written, {len(iv)} interview, {len(disc)} discarded')

if __name__ == '__main__':
    main()
