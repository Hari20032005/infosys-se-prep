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
course: core
lesson: 4
---

# Lesson 04. Coding and decoding

*Topic `A1` · about 2.1 of the 75 marks · plan about 0.8 hours.*

## 1. The idea

In a coding-decoding question, a word is turned into a code by a hidden rule. You see one or two examples and have to code a new word.

The code can be a number (the sum of the letters, say) or a new word (every letter moved along). In both cases the first job is the same: turn each letter into its place in the alphabet. A is 1, B is 2, up to Z, which is 26. After that, comparing the word with its code shows the rule.

There are only five or six rules that actually appear. Learn them and the question becomes a checklist.

## 2. What Infosys actually asks

Five coding questions were found in the 2025 reports `[REPORTED]`. They were all variations of the same few ideas:

- the sum of the letters' places (BURST = 80);
- the average of the letters' places (LAST = 13);
- keep the place number for letters in odd positions, and write 0 for the even positions (CHAIR = 301018);
- write the word backwards, then move every letter one place back (CREATE = DSZDQB);
- swap the positions of some letters (BREAK = RBEKA).

The official 2020 sample had no pure coding question, so everything here comes from reports. The Reasoning section is 15 questions in 25 minutes, about 100 seconds each.

## 3. The method

1. **Write down the place numbers** of the letters in the first example, if the code is a number. Do the same for the code if it is letters.
2. **Compare the word with its code.** Is the code a number, or a word of the same length?
3. **If the code is a number:** try the sum, then the average, then "keep some letters, zero for others".
4. **If the code is a word:**
    - letters moved by the same amount? That is a shift;
    - letters in a different order? That is a swap or a reverse;
    - both? Do the reverse first, then the shift.
5. **Test on the second example** (or on every letter) before using the rule.
6. **Apply to the new word**, one letter at a time.

The rule ladder:

| The code is | Try |
|---|---|
| A number about 5 to 15 times the word length | Sum of places |
| A small number, same size as a letter place | Average of places |
| A long string of digits with zeros | Odd or even places |
| Same letters in another order | Swap or reverse |
| Letters, all moved the same amount | Shift |
| Reversed and shifted | Reverse, then shift |
| Words given as whole sentences | Find the one word the sentences share |

## 4. Shortcuts and when they fail

**Look at the first letter.** Compare the first letter of the word with the first letter of the code. If it is exactly 1 or 2 places away, you probably have a shift. *It fails if the word is reversed*, because then the first letter of the code comes from the last letter of the word.

**Last letter first.** If the code is the word reversed, the last letter of the code is the first letter of the word. Check that quickly. *It fails for swaps that do not reverse everything.*

**Anchors for places.** Remember E = 5, J = 10, O = 15, T = 20, Y = 25. Count from the nearest anchor. *It fails on mistakes in counting*, so write the numbers down for long words.

**Words that share a letter.** For sentence codes, the one word that appears in both sentences matches the one code word that appears in both. *It fails if the two sentences share more than one word.* Then you need more information.

## 5. Worked examples

All results below were checked by code.

**Example 1 (sum of places).** CAT is written as 24 and DOG as 26. How is SUN written?

CAT: 3 + 1 + 20 = 24. DOG: 4 + 15 + 7 = 26. So the code is the sum. SUN: 19 + 21 + 14 = **54**.

**Example 2 (average of places).** CLOUD is written as 11 and BRIEF as 8. How is NORTH written?

CLOUD: 3 + 12 + 15 + 21 + 4 = 55. Divide by 5: 11. BRIEF: 2 + 18 + 9 + 5 + 6 = 40, divided by 5 is 8. So the code is the average. NORTH: 14 + 15 + 18 + 20 + 8 = 75, divided by 5 is **15**.

**Example 3 (reverse, then shift).** TABLE is written as DKAZS. How is LEARN written?

Reverse TABLE: ELBAT. Move each letter back one place: E to D, L to K, B to A, A to Z, T to S. That gives DKAZS, the code. For LEARN: reverse it to NRAEL. Move each letter back one place: M, Q, Z, D, K. Answer: **MQZDK**.

**Example 4 (swap positions).** PLANT is written as LPATN. How is SMART written?

Compare PLANT with LPATN. Letters 1 and 2 swapped, letter 3 stayed, and letters 4 and 5 swapped. Apply the same to SMART: M, S, A, T, R. Answer: **MSATR**.

**Example 5 (odd places keep the number).** MONEY is written as 13014025. How is STONE written?

M is 13. Then O is 0. N is 14. E is 0. Y is 25. Putting them together: 13, 0, 14, 0, 25. So letters in odd places keep their place number, and letters in even places become 0. STONE: S is 19, T is 0, O is 15, N is 0, E is 5. Answer: **1901505**.

## 6. Traps

- **Mixing up the order of reverse and shift.** The two steps give different answers in the other order. Check with the example.
- **Skipping the second example.** One example can fit two rules. Always test on a second word.
- **Wrong place numbers.** Write them out for long words and add twice.
- **Averages that do not divide.** If your average is not a whole number, the rule is probably the sum.
- **Wrapping past Z.** A shift can run off the end. Z plus 1 is A.


## 7. Practice questions

Attempt each level before opening the key. Level 3 is harder than anything in the 2020 official sample, on purpose: if you can do Level 3, the real paper will feel easy.

### Level 1: warm-up

*One step: add up the places, shift the letters, or match whole words.*

**1.** **[Letter sum]** In a certain code language PAPER is written as 56 and NORTH is written as 75. How is GUITAR written in that code?  
a) 77  
b) 76  
c) 75  
d) 86  

**2.** **[Letter shift]** In a certain code FRAUD is written as DPYSB. How is HOUSE written in that code?  
a) IPVTF  
b) FMSQC  
c) GNTRD  
d) JQWUG  

**3.** **[Word substitution]** In a certain code language, ‘cloud tree star’ is written as ‘si ra to’ and ‘hill tree’ is written as ‘ka ra’. What is the code for ‘tree’?  
a) ra  
b) to  
c) ka  
d) si  

**4.** **[Letter sum]** In a certain code language RIVER is written as 72 and MIRROR is written as 91. How is LAST written in that code?  
a) 62  
b) 51  
c) 52  
d) 53  

**5.** **[Letter shift]** In a certain code WATER is written as YCVGT. How is BRIEF written in that code?  
a) AQHDE  
b) ZPGCD  
c) DTKGH  
d) CSJFG  

### Level 2: exam level

*Averages, odd-even position codes, and swaps.*

**6.** **[Average of positions]** In a certain code TABLE is written as 8 and LAST as 13. What is the code for FRAUD?  
a) 10  
b) 50  
c) 11  
d) 9  

**7.** **[Position rule]** In a certain code BRAVE is written as 0180220. How is CASTLE written in that code?  
a) 311920125  
b) 30190120  
c) 0102005  
d) 0102000  

**8.** **[Position swap]** If SMART is written as MSATR, how is TABLE written in the same code?  
a) ETABL  
b) ELBAT  
c) ATBEL  
d) ABLET  

**9.** **[Letter sum]** In a certain code language SILVER is written as 85 and NORTH is written as 75. How is YOUTH written in that code?  
a) 99  
b) 88  
c) 90  
d) 89  

**10.** **[Position rule]** In a certain code NORTH is written as 1401808. How is STONE written in that code?  
a) 0200140  
b) 192015145  
c) 1901500  
d) 1901505  

### Level 3: beyond the exam

*Reverse and shift together, and longer words with more to check.*

**11.** **[Reverse and shift]** In a certain code ISLAND is written as FPCNUK. How is WATER written in that code?  
a) RETAW  
b) TGVCY  
c) PCRYU  
d) YCVGT  

**12.** **[Reverse and shift]** In a certain code VOICE is written as FDJPW. How is MARKET written in that code?  
a) NBSLFU  
b) UFLSBN  
c) SDJQZL  
d) TEKRAM  

**13.** **[Position swap]** If BURST is written as UBRTS, how is HOUSE written in the same code?  
a) ESUOH  
b) OUSEH  
c) EHOUS  
d) OHUES  

**14.** **[Reverse and shift]** In a certain code VOICE is written as FDJPW. How is SILVER written in that code?  
a) SFWMJT  
b) QDUKHR  
c) REVLIS  
d) TJMWFS  

**15.** **[Average of positions]** In a certain code CASTLE is written as 10 and ENGINE as 9. What is the code for FRAUD?  
a) 10  
b) 9  
c) 11  
d) 50  

### ANSWER KEY

1. **b** — Each letter stands for its place in the alphabet and the code is the sum. PAPER: 16 + 1 + 16 + 5 + 18 = 56; NORTH: 14 + 15 + 18 + 20 + 8 = 75. So GUITAR = 7 + 21 + 9 + 20 + 1 + 18 = **76**.
2. **b** — Compare the first letters: F → D, so every letter moves **2 places back**. Applied to HOUSE: **FMSQC**.
3. **a** — ‘tree’ is the only word common to both sentences, and the only code common to both is **ra**. So tree = ra.
4. **c** — Each letter stands for its place in the alphabet and the code is the sum. RIVER: 18 + 9 + 22 + 5 + 18 = 72; MIRROR: 13 + 9 + 18 + 18 + 15 + 18 = 91. So LAST = 12 + 1 + 19 + 20 = **52**.
5. **c** — Compare the first letters: W → Y, so every letter moves **2 places forward**. Applied to BRIEF: **DTKGH**.
6. **a** — The code is the **average** of the letter positions. TABLE: 40 ÷ 5 = 8; LAST: 52 ÷ 4 = 13. FRAUD: 50 ÷ 5 = **10**.
7. **c** — Compare the code with the word letter by letter: even positions keep the alphabet number and odd positions become 0. BRAVE → 0180220. Apply it to CASTLE: C=0 A=1 S=0 T=20 L=0 E=5 → **0102005**.
8. **c** — Only the **positions** change: letter 1 goes to place 2, letter 2 goes to place 1, letter 4 goes to place 5, letter 5 goes to place 4. Apply the same shuffle to TABLE: **ATBEL**.
9. **d** — Each letter stands for its place in the alphabet and the code is the sum. SILVER: 19 + 9 + 12 + 22 + 5 + 18 = 85; NORTH: 14 + 15 + 18 + 20 + 8 = 75. So YOUTH = 25 + 15 + 21 + 20 + 8 = **89**.
10. **d** — Compare the code with the word letter by letter: odd positions keep the alphabet number and even positions become 0. NORTH → 1401808. Apply it to STONE: S=19 T=0 O=15 N=0 E=5 → **1901505**.
11. **b** — Compare ISLAND with FPCNUK: the word is written **backwards** and every letter then moves 2 places forward in the alphabet. WATER reversed is RETAW; shifting each letter gives **TGVCY**.
12. **b** — Compare VOICE with FDJPW: the word is written **backwards** and every letter then moves 1 place forward in the alphabet. MARKET reversed is TEKRAM; shifting each letter gives **UFLSBN**.
13. **d** — Only the **positions** change: letter 1 goes to place 2, letter 2 goes to place 1, letter 4 goes to place 5, letter 5 goes to place 4. Apply the same shuffle to HOUSE: **OHUES**.
14. **a** — Compare VOICE with FDJPW: the word is written **backwards** and every letter then moves 1 place forward in the alphabet. SILVER reversed is REVLIS; shifting each letter gives **SFWMJT**.
15. **a** — The code is the **average** of the letter positions. CASTLE: 60 ÷ 6 = 10; ENGINE: 54 ÷ 6 = 9. FRAUD: 50 ÷ 5 = **10**.

## 8. Recap in 60 seconds

- Letters become numbers: A = 1 to Z = 26. Anchors: E 5, J 10, O 15, T 20, Y 25.
- Number codes: sum, then average, then odd or even places.
- Word codes: shift (all letters move the same), swap (order changes), reverse (backwards). Reverse and shift can come together.
- Test the rule on the second example before you use it.
- Sentence codes: the word both sentences share matches the code both share.

## 9. Sources

- `../question-banks/QB-99-OBSERVED-POOL.md`: the five coding items reported in 2025, solved by running code.
- Every code in the five examples is computed and checked in `data/cc_examples.py`. No outside website is cited, because the rules are arithmetic and string handling, not language rules (see `../research/06-method-sources.md`).
