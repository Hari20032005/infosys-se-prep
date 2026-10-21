---
title: Coding and decoding
code: A1
section: Reasoning Ability
weightage_pct: 2.8% of marks
est_questions: 2.07
tier: 1
difficulty: Medium
est_study_hours: 0.8
confidence: High
last_updated: 2026-09-30
adapted_from: L&T/lt-prep-library/topics/L4-coding-and-decoding.md
---
<!-- Drafted by DeepSeek V4.1 Flash via ds.py; reviewed by Claude 2026-09-21. Answer
     letters rebalanced by data/shuffle.py (correctness-preserving: option text is
     swapped and the key letter repointed). Numeric keys re-checked by
     data/verify_keys.py. -->

# A1 — Coding and decoding

*Adapted from `L&T/lt-prep-library/topics/L4-coding-and-decoding.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **2.1 questions and 2.1 marks** on this topic (about 2.8% of the 75 scored marks). It sits in **Reasoning Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 1**, 0.8 hours to reach reliable recall, confidence **High**.

**6 questions on this topic are in the observed Infosys pool** (R01, R05, R06, R14, R15), from 2 sources. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 2.59 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| R01 | 2026-09-22 | In a certain code LAST is written as 13 and TABLE as 8. How is FRAUD written? |
| R05 | 2025-09-29 | In a certain code BURST is written as 80 and LAKE as 29. How is VERSATILE written? |
| R05b | 2025-09-25 | BURST = 80, LAKE = 29, VERSATILE = ? |
| R06 | 2025-09-29 | In a certain code CHAIR is written as 301018. How is TABLE written? |
| R14 | 2025-09-25 | CREATE is written as DSZDQB. How is POLITE written? |
| R15 | 2025-10-09 | If BREAK is written as RBEKA, how is BRIEF written? |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



| Sub-pattern | How it appears | Roughly how often |
|---|---|---|
| Letter-shift (Caesar) coding | One or two words given in coded form; find the code for a new word | ~30% |
| Position-number coding | Letters replaced by 1-26 values, then concatenated or summed | ~20% |
| Substitution / word-code | Invented words mapped to real words; identify what one word means | ~20% |
| Reverse-alphabet (Atbash) | A↔Z, B↔Y; effectively 27 minus the position | ~10% |
| Symbol coding | Real words mapped to symbols; find the symbol for a word | ~8% |
| Conditional coding | Rule differs by vowel/consonant or by odd/even position | ~7% |
| Mixed / two-step | Reverse then shift, or shift then reverse, or shift by increasing steps | ~5% |

The share column is inferred from the shape of Indian campus placement papers generally, not from an observed L&T paper. The absolute count is small, so any one of these could dominate your three questions.

## 3. Concept notes

### 3.1 The alphabet grid and the reverse rule

Every coding question is faster if the alphabet's numeric positions are reflex, not calculation.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

**Reverse-alphabet position = 27 − forward position.** Example: R is 18, so its reverse is 27 − 18 = 9 = I. Every pair sums to 27: A↔Z, B↔Y, ..., M↔N.

Anchor points that remove counting: **EJOTY = 5, 10, 15, 20, 25** and **CFILORUX = 3, 6, 9, 12, 15, 18, 21, 24**. From E=5 you can reach F, G, H, I in two steps; from J=10 the same for the teens.

Vowels are **A, E, I, O, U** (5). Everything else (21 letters) is a consonant. Y is treated as a consonant in these papers.

### 3.2 Shift coding (the Caesar pattern)

**Rule: every letter moves a fixed number of places, in the same direction.** Word CAT coded as DBU means +1. To decode, reverse the direction.

Direction vocabulary: "forward/right" = toward Z; "backward/left" = toward A. Wrapping is allowed and normal: Z + 1 = A, A − 1 = Z.

Verify a shift on **two** letters before you commit. A single letter can be explained by several rules at once - for example, C→G could be +4, or it could be a reverse-alphabet substitution. Two letters in the same word almost never coincide by accident.

Variable-shift variants exist: +1, +2, +3, ... across successive letters (progressive shift), or +1 for odd positions and −1 for even positions. Both are still positional, so read the position, then apply.

### 3.3 Reverse-alphabet (Atbash) coding

**Rule: replace each letter with the letter equidistant from the other end.** A→Z, B→Y, C→X, ..., M→N, N→M. A word and its code have the same length, and the first letter usually lands far away from the original.

Because it is exactly 27 minus the position, you can compute it in your head: F is 6, 27 − 6 = 21 = U, so F→U. Atbash never wraps ambiguously - it is a mirror, not a rotation.

### 3.4 Position-number coding

Three distinct flavours, and you must tell them apart in the first five seconds.

| Flavour | What is done | Example |
|---|---|---|
| Concatenation | Write each letter's position, no separators | CAT → 3120 |
| Sum | Add all positions into one number | CAT → 3+1+20 = 24 |
| Difference | Subtract consecutive positions | CAT → 3−1=2, 1−20=−19 (rare) |

For concatenation, the number of digits tells you the word length, because A-I contribute 1 digit and J-Z contribute 2. A 6-digit code is not necessarily a 6-letter word. **Count the digits first.** 3120 = 3, 1, 20 = three letters. 1291514 = 12, 9, 15, 14 = four letters.

For the sum flavour, you only need the total, so use EJOTY anchors rather than full counting.

### 3.5 Substitution / word-code coding

A sentence is given in an invented language, with the English meaning alongside it. The rule set:

1. **Same word → same code, every time.** If 'ka' appears in two sentences, the real word common to both sentences is 'ka'.
2. **Different words → different codes.** No two real words share a code.
3. **Order is usually scrambled** - never match by position, match by co-occurrence.

Method: find the word that appears in exactly two sentences, note which real word also appears in exactly those two sentences, and pin them together. Delete that pair and repeat. Example: 'pit na ka' = 'you are good' and 'na ta pit' = 'are you smart' → 'na' and 'are' are the only items shared → na = are. Remove, and 'ka pit' = 'you good', so 'ta' = smart.

### 3.6 Symbol coding

Same logic as substitution coding but with symbols instead of invented words: '@', '#', '%'. Longer sentences give more constraints. If a symbol appears only in one sentence, the word it maps to is one of that sentence's words - look for the shortest sentence that contains it to narrow down.

### 3.7 Conditional coding

The rule branches on the letter's class or position.

| Condition | Rule |
|---|---|
| Vowel at that position | Apply rule A |
| Consonant at that position | Apply rule B |
| Odd position in the word | Apply rule A |
| Even position in the word | Apply rule B |

Example: "vowels move one step forward, consonants one step back" applied to BAND gives A E M C (B→A, A→E, N→M, D→C). Read the word left to right, decide each letter's class, then transform. Do not transform first and check later.

### 3.8 Two-step and mixed coding

The word is manipulated twice. Common orders:

- **Reverse then shift:** COLD → DLOC → (shift +2) → FNQE.
- **Shift then reverse:** COLD → (shift +2) → EQNF → reverse → FNQE. Note these two often coincide - test with the given example rather than guessing.

Some papers add a third layer (substitute, then reverse, then shift). Given the one-minute budget, if a question needs three layers, mark and move on.

## 4. Must-memorise block

- **A=1, B=2, ... Z=26.** Reverse value = **27 − forward value**.
- **EJOTY = 5, 10, 15, 20, 25.**
- **CFILORUX = 3, 6, 9, 12, 15, 18, 21, 24.**
- Reverse pairs: **AZ, BY, CX, DW, EV, FU, GT, HS, IR, JQ, KP, LO, MN** (all sum to 27).
- Wrap rules: **Z + 1 = A** and **A − 1 = Z**.
- Vowels: **A E I O U** (5). Consonants: 21. Y counts as a consonant.
- Decoding = applying the inverse operation. If coding is +3, decoding is −3.
- Concatenation code: split by position values - 1 digit for A-I, 2 digits for J-Z.
- Sum code: total of the letter positions only.
- Substitution: **shared code = shared word**. Order is never reliable.
- Progressive shift on an n-letter word uses +1, +2, ..., +n.
- Same-length words usually indicate a per-letter rule (shift or Atbash), not a numeric rule.

## 5. Worked examples

**Example 1.** If RAIN is coded as SBJO, how is SNOW coded?

Fast method: R→S is +1, A→B is +1. Fixed shift +1. Apply: S→T, N→O, O→P, W→X. **Answer: TOPX.**
Slow method: writing out the alphabet and counting from A each time loses 30-40 seconds. Use EJOTY: N is 14, so N+1 is 15 = O.

**Example 2.** If FRIEND is coded as UIRVMW, how is SAFE coded?

Fast method: F=6, its code is U=21, and 27 − 6 = 21. Confirmed by R=18 → I=9, and 27 − 18 = 9. This is Atbash. Apply: S=19 → 27−19=8 = H; A=1 → 26 = Z; F=6 → 21 = U; E=5 → 22 = V. **Answer: HZUV.**
Slow method: building the full reverse alphabet A–Z in the margin. You only need the subtraction, which is one step.

**Example 3.** If LION is coded as 1291514, how is TIGER coded?

Fast method: 1291514 must split as 12, 9, 15, 14 - four values matching L, I, O, N (the 9 must be a single digit because 12 and 15 are already taken and 91 is impossible). So it is concatenated positions. TIGER = T=20, I=9, G=7, E=5, R=18 → **2097518**.
Slow method: assuming one digit per letter. That fails immediately on L=12. Check the first digit pair first - if it exceeds 26, your split is wrong.

**Example 4.** In a code language, 'ram is good' is written 'pa ta ka'; 'good boy' is written 'ka na'; 'boy is smart' is written 'na ta ha'. What is the code for 'smart'?

Fast method: find shared items. Sentences 2 and 3 share only the word 'boy', and share only the code 'na'. So na = boy. Sentence 2 then gives ka = good. Sentence 1 then gives ta = is. Sentence 3 becomes na ta ha = boy is smart, so **ha = smart**.
Slow method: guessing word-by-word from sentence 1. Order is scrambled, so this produces contradictory assignments and wastes a minute.

**Example 5.** In a code, letters are first written in reverse order and then each is moved two places forward. If COLD is coded as FNQE, how is WARM coded?

Fast method: verify on COLD - reverse gives DLOC, then +2 gives F, N, Q, E. Matches. Apply to WARM: reverse gives MRAW, then +2 gives O, T, C, Y. **Answer: OTCY.**
Slow method: trying "shift then reverse" first. It happens to give the same result here, but on some words the two orders differ, so verify against the given example rather than assuming.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Locking onto a shift after one letter | Many rules explain a single letter-to-letter change | Verify on a second letter in the same word before applying |
| Forgetting the wrap | Z+1 is A, not a number past 26 | Say "wrap" out loud whenever you pass A or Z |
| Reading the shift direction backwards | "Forward" means toward Z, not toward A | Check the first pair against the given example before solving |
| Splitting a concatenated number wrongly | 121 vs 1,2,1 changes everything | Split greedily: take 2 digits when the pair is 10-26 and the word length demands it |
| Matching substitution codes by position | The invented sentence is deliberately reordered | Match by co-occurrence only; ignore order entirely |
| Trying to decode an unresolvable word | Some words in substitution sets genuinely cannot be pinned down | If two words share the same two possible codes and no sentence separates them, the answer is "cannot be determined" |
| Using A=0 | Zero-indexing silently shifts every answer by one | A=1, always |
| Applying the rule to the wrong word | "Code for X" vs "decode Y" | Circle the target word before you start transforming |

## 7. Practice questions

**1.** If TEACHER is coded as VGCEJGT, how is CHILD coded?
a) EJKMF b) EJKNF c) EJKMF d) DKJMF

**2.** If MONKEY is coded as NLMPVB, how is TIGER coded?
a) SRTVI b) GQTVI c) GRTWI d) GRTVI

**3.** If CAT is coded as 3120, how is DOG coded?
a) 4517 b) 4175 c) 4157 d) 4156

**4.** In a code language, 'pit na ka' means 'you are good', 'na ta pit' means 'are you smart', and 'ka pit' means 'you good'. Which word means 'smart'?
a) pit b) na c) ta d) ka

**5.** In a code, letters at odd positions move one step forward and letters at even positions move one step backward. How is MIND coded?
a) MHOC b) NHOC c) NHOB d) NJOC

**6.** If ROSE is coded as 6821 and CHAIR as 73456, how is SEARCH coded?
a) 214763 b) 214673 c) 216473 d) 124673

**7.** If FRIEND is coded as GTLISJ, how is CANDLE coded?
a) DCQHQK b) DCQHQJ c) DCQHPK d) ECQHQK

**8.** In a code, 'come home' is written '#@', 'home sweet' is written '@%', and 'sweet lime' is written '%$'. What is the code for 'lime'?
a) $ b) @ c) % d) #

**9.** Each vowel in a word is replaced by the next letter of the alphabet and each consonant by the previous letter. How is BAND coded?
a) AEND b) BEMC c) AEMC d) AEMB

**10.** If CAT is coded as 24 by adding letter positions, how is DOG coded by the same rule?
a) 24 b) 30 c) 28 d) 26

**11.** In a code language, 'ki ma ta' means 'eat healthy food', 'ta ni ba' means 'food is tasty', and 'ba ki' means 'healthy is'. What does 'ta' mean?
a) is b) food c) healthy d) tasty

**12.** In a code, letters of a word are first written in reverse order and then each letter is moved two places forward. If BEAT is coded as UBFC, how is MICE coded?
a) FDJM b) EFJN c) FDKN d) FDJN

### ANSWER KEY

1. **a)** TEACHER → VGCEJGT is +2 on each letter. C+2=E, H+2=J, I+2=K, L+2=N, D+2=F → EJKMF.
2. **d)** M=13→N=14, 27−13=14, so this is Atbash. T=20→7=G, I=9→18=R, G=7→20=T, E=5→22=V, R=18→9=I → GRTVI.
3. **c)** CAT = C, A, T = 3, 1, 20 concatenated. DOG = 4, 15, 7 → 4157.
4. **c)** 'na' and 'are' are the only items common to the first two sentences. Stripping 'na' leaves 'ka pit' = 'you good', so the remaining word in sentence 2, 'ta', is 'smart'.
5. **b)** M (odd) +1 = N; I (even) −1 = H; N (odd) +1 = O; D (even) −1 = C → NHOC.
6. **b)** ROSE → R6, O8, S2, E1; CHAIR → C7, H3, A4, I5, R6. R=6 agrees in both. SEARCH = 2, 1, 4, 6, 7, 3 → 214673.
7. **a)** FRIEND uses progressive shift +1, +2, +3, +4, +5, +6. CANDLE: C+1=D, A+2=C, N+3=Q, D+4=H, L+5=Q, E+6=K → DCQHQK.
8. **a)** 'sweet' is the only word common to 'home sweet' (@%) and 'sweet lime' (%$), so sweet = %; lime is the other symbol in the second pair, $.
9. **c)** B (consonant) → A, A (vowel) → E, N (consonant) → M, D (consonant) → C → AEMC.
10. **d)** D+O+G = 4+15+7 = 26.
11. **b)** 'ta' appears in sentence 1 ('eat healthy food') and sentence 2 ('food is tasty'); the only real word common to both is 'food'.
12. **d)** BEAT reversed = TAEB, +2 = UBFC, which confirms the order. MICE reversed = ECIM, +2 = FDJN.

## 8. Resources

- **Verbal Reasoning Questions and Answers** — https://www.indiabix.com/verbal-reasoning/questions-and-answers/ — index of question sets - open a sub-topic for the actual questions.
- **Coding Decoding - Solved Questions and Answers** — https://www.geeksforgeeks.org/coding-decoding/ — index of question sets - open a sub-topic for the actual questions.
- **Atbash - Wikipedia** — https://en.wikipedia.org/wiki/Atbash — reference article.
- **ASCII Table - ASCII codes, hex, decimal, binary, html** — https://www.rapidtables.com/code/text/ascii-table.html — page content not classified - read it before relying on it.

## 9. Self-check

Answer yes or no to each. Six yes answers means you can stop.

1. Can you state the reverse-alphabet position of any letter R without counting, using 27 − position?
2. Can you recall EJOTY and CFILORUX and use them to reach a nearby letter in two steps?
3. For a concatenated number code, can you split it correctly on the first try, including two-digit values for J-Z?
4. In substitution coding, do you automatically match by shared code rather than by word order?
5. Do you verify a proposed shift on a second letter before committing to the answer?
6. Can you identify whether a code was produced by a shift, an Atbash mirror, or a numeric rule within five seconds of reading it?

## 10. Sources

**Teaching content (§3–§9)** is adapted from `L&T/lt-prep-library/topics/L4-coding-and-decoding.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions R01, R05, R06, R14, R15 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A1`). Confidence **High**. Nothing in this file is a published Infosys syllabus.
