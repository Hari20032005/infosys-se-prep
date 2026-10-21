---
title: Number and letter series
code: A2
section: Reasoning Ability
weightage_pct: 3.7% of marks
est_questions: 2.75
tier: 1
difficulty: Easy
est_study_hours: 1.0
confidence: High
last_updated: 2026-09-30
course: core
lesson: 3
---

# Lesson 03. Number and letter series

*Topic `A2` · about 2.8 of the 75 marks · plan about 1.0 hours.*

## 1. The idea

A series is a list of numbers (or letters) that follows a pattern. You are given most of the list and asked for the next term, or for one that is missing.

The pattern is always made of small, familiar moves: add the same amount, multiply by the same amount, add a growing amount, add up the last two terms, use squares or primes. There are only about a dozen of these. Once you know them, you stop guessing and start checking.

Letters work the same way. Replace each letter by its place in the alphabet (A is 1, B is 2, and so on up to Z, which is 26), and a letter series becomes a number series.

## 2. What Infosys actually asks

Series questions were the most common reasoning item in the 2025 reports. Ten were found in the pool `[REPORTED]`, and one more was in the official 2020 sample, where the gaps in the series were the prime numbers 2, 3, 5, 7, 11, 13 `[CONFIRMED — official sample 2020]`.

The kinds that appeared:

- a polynomial pattern, such as cubes plus squares plus the number;
- each term equal to twice the sum of the two before it;
- squares in which every second one is written backwards (144, 441, 169, 961);
- three tracks in one term, such as `3Y6, 8W8, 15U10`, where the number, the letter and the last number each follow their own rule;
- two series woven together, in odd and even places;
- consecutive prime numbers;
- a number and a letter together, such as `1D, ?, 5H, 7J`.

The Reasoning section has 15 questions in 25 minutes, about 100 seconds each. A series should take less than that.

## 3. The method

1. **Write the gaps.** Subtract each term from the next. Do this first, every time.
2. **Read the gaps.**
    - All the same? Then it is a constant gap. Add it again.
    - Growing by a steady amount? Take the gaps of the gaps. If those are steady, carry them forward.
    - Odd numbers, squares or primes? Then the gaps follow that list.
    - Gaps that are rising fast, or gaps of different sizes with no pattern? Go to step 3.
3. **Check the ratios.** Divide each term by the one before. A steady ratio means multiply. A steady ratio plus a small adjustment means "× k + c".
4. **Check the landmarks.** Do the terms look like squares (1, 4, 9, 16, 25, 36, 49, 64), cubes (1, 8, 27, 64, 125) or primes?
5. **Split the places.** If the gaps jump up and down, take the odd places and the even places as two separate series.
6. **Letters:** change them to numbers first, then go back to step 1.
7. **Combined terms:** treat every part of the term (the number, the letter, the last number) as its own series.
8. **Check the rule on every term**, not only the first two.

Quick signals:

| What you see | Try |
|---|---|
| Same gap every time | Add the gap |
| Gaps grow by 2, or 3, or 1 | Second gaps (gaps of gaps) |
| Terms near squares or cubes | n² ± n, n³ ± n |
| Ratio about 2 or 3 | × k + c |
| Gaps jump up and down | Odd and even places |
| Gaps are 2, 3, 5, 7, 11 | Prime gaps |

## 4. Shortcuts and when they fail

**Gaps of gaps.** If the second row of gaps is steady, you can extend the table with simple additions. If the second row is not steady, take a third row. A steady third row means a cubic pattern. *It fails when the pattern is not polynomial*, as with × 2 + 1, where the gaps themselves double. Use ratios then.

**Landmark numbers.** Memorise squares up to 15 and cubes up to 10. Most "strange" series sit on top of them. *It fails when the series is a sum of different landmarks.* Then use the gaps.

**The alphabet anchors.** Remember E = 5, J = 10, O = 15, T = 20, Y = 25. From an anchor you can count to any letter in a few steps. *It fails if the series wraps past Z.* Subtract 26 when that happens.

**Split the places.** If the gaps zig-zag, separate the odd and even places. Each half is usually an easy series. *It fails if the two halves depend on each other.* That is rare in the Infosys items found.

## 5. Worked examples

All the numbers below were checked by code.

**Example 1 (growing gaps).** 5, 7, 11, 17, 25, ?

The gaps are 2, 4, 6, 8. They grow by 2, so the next gap is 10. Answer: 25 + 10 = **35**.

**Example 2 (multiply and add).** 2, 5, 11, 23, 47, ?

The gaps are 3, 6, 12, 24. They double, which is a sign of multiplying. Try × 2 + 1: 2 × 2 + 1 = 5, 5 × 2 + 1 = 11, and so on. It fits every term. Answer: 47 × 2 + 1 = **95**.

**Example 3 (two series woven together).** 80, 15, 70, 25, 60, 35, ?

The gaps are −65, +55, −45, +35, −25, so they zig-zag. Split the places. Odd places: 80, 70, 60 (down by 10). Even places: 15, 25, 35 (up by 10). The next term is an odd place, so it is 60 − 10 = **50**.

**Example 4 (three tracks).** 4P3, 9N6, 16L9, 25J12, ?

Take each part on its own. The numbers 4, 9, 16, 25 are squares of 2, 3, 4, 5, so the next is 36. The letters P, N, L, J move back two places each time, so the next is H. The last numbers 3, 6, 9, 12 grow by 3, so the next is 15. Answer: **36H15**.

**Example 5 (prime gaps, as in the official sample).** 3, 5, 8, 13, 20, 31, ?

The gaps are 2, 3, 5, 7, 11. These are consecutive primes, and the next prime is 13. Answer: 31 + 13 = **44**.

## 6. Traps

- **Looking at two terms only.** Two terms fit many patterns. Check at least four.
- **Forgetting to split.** A zig-zag in the gaps nearly always means two series.
- **Letter wrap-around.** After Z comes A again, but most questions avoid it. If your answer goes past Z, recheck.
- **Missing the combined term.** With `3Y6, 8W8`, three things change at once. Take them one at a time.
- **Stopping at "gap of gaps is steady".** Carry it forward properly: add the next gap-of-gap to the last gap, then add that to the last term.


## 7. Practice questions

Attempt each level before opening the key. Level 3 is harder than anything in the 2020 official sample, on purpose: if you can do Level 3, the real paper will feel easy.

### Level 1: warm-up

*One idea: a steady gap, a steady ratio, primes, or the sum of two terms.*

**1.** **[Constant gap]** Find the next term: 21, 24, 27, 30, 33, 36, ?  
a) 39  
b) 45  
c) 36  
d) 42  

**2.** **[Constant ratio]** Find the next term: 2, 4, 8, 16, 32, 64, ?  
a) 96  
b) 128  
c) 133  
d) 130  

**3.** **[Prime-based]** Find the next term: 17, 19, 23, 29, 31, ?  
a) 39  
b) 37  
c) 33  
d) 38  

**4.** **[Two-term recurrence]** Find the next term: 1, 5, 12, 34, 92, 252, 688, ?  
a) 1880  
b) 1376  
c) 1882  
d) 940  

**5.** **[Growing gaps]** Find the missing term: 8, 10, 15, 23, 34, 48, 65, ?  
a) 82  
b) 85  
c) 89  
d) 88  

### Level 2: exam level

*Two ideas: letters turned into numbers, polynomial patterns, prime gaps, multiply and adjust, and woven series.*

**6.** **[Letter series]** Find the next letter: C, D, F, I, M, ?  
a) R  
b) T  
c) S  
d) Q  

**7.** **[Formula series]** Find the next term: 26, 63, 124, 215, 342, 511, ?  
a) 730  
b) 680  
c) 728  
d) 726  

**8.** **[Gaps are primes]** Find the next term: 18, 23, 30, 41, 54, 71, ?  
a) 92  
b) 90  
c) 95  
d) 88  

**9.** **[Multiply and adjust]** Find the next term: 2, 9, 37, 149, 597, 2389, ?  
a) 9556  
b) 9561  
c) 4181  
d) 9557  

**10.** **[Interleaved series]** Find the next term: 111, 5, 97, 26, 83, 47, 69, ?  
a) 73  
b) 26  
c) 55  
d) 68  

### Level 3: beyond the exam

*Three or four tracks at once, or squares written backwards.*

**11.** **[Number-letter-number]** Find the next term: 6R6, 12P10, 20N14, 30L18, 42J22, ?  
a) 56J26  
b) 56H24  
c) 56H26  
d) 58H26  

**12.** **[Number-letter-number]** Find the next term: 17V6, 26T10, 37R14, 50P18, 65N22, ?  
a) 84L26  
b) 82L24  
c) 82N26  
d) 82L26  

**13.** **[Squares and reversals]** Find the next term: 441, 144, 961, 169, 1681, 196, 2601, ?  
a) 2704  
b) 256  
c) 225  
d) 235  

**14.** **[Squares and reversals]** Find the next term: 144, 441, 169, 961, 196, 1681, 225, ?  
a) 256  
b) 2704  
c) 2601  
d) 2611  

**15.** **[Interleaved series]** Find the next term: 115, 10, 93, 30, 71, 50, 49, ?  
a) 70  
b) 30  
c) 27  
d) 75  

### ANSWER KEY

1. **a** — The gap is the same every time (3): 24 − 21 = 3. So the next term is 36 + 3 = **39**.
2. **b** — Each term is the one before **× 2**: 2 × 2 = 4. So the next term is 64 × 2 = **128**.
3. **b** — The terms are consecutive primes: 17, 19, 23, 29, 31 → the next prime is 37, giving **37**.
4. **a** — each term is **twice the sum** of the two before it: 252 and 688 give **1880**.
5. **b** — The gaps are 2, 5, 8, 11, 14, 17: they grow by 3 each time, so the next gap is 20. 65 + 20 = **85**.
6. **a** — Turn the letters into places in the alphabet: 3, 4, 6, 9, 13. The gaps are 1, 2, 3, 4, growing by 1, so the next gap is 5. 13 + 5 = 18, which is **R**.
7. **c** — The terms are **n³ − 1** for n = 3, 4, … : f(3) = 26, f(4) = 63, f(5) = 124. For n = 9: **728**. (The differences 37, 61, 91, 127, 169 keep changing; the finite-difference table confirms it.)
8. **b** — The gaps are 5, 7, 11, 13, 17: consecutive primes. The next prime is 19, so 71 + 19 = **90**.
9. **d** — Each term is the previous one **× 4 + 1**: 2 → 9 → 37. So 2389 × 4 + 1 = **9557**.
10. **d** — Two series are woven together. Odd places: 111, 97, 83, 69 (−14 each). Even places: 5, 26, 47 (+21 each). The next place is an even place: 47 + 21 = **68**.
11. **c** — Three tracks. Numbers: 6, 12, 20, 30, 42, next 56. Letters step back two places each time: R, P, N, L, J, next H. Last numbers rise by 4: 6, 10, 14, 18, 22, next 26. Answer **56H26**.
12. **d** — Three tracks. Numbers: 17, 26, 37, 50, 65, next 82. Letters step back two places each time: V, T, R, P, N, next L. Last numbers rise by 4: 6, 10, 14, 18, 22, next 26. Answer **82L26**.
13. **c** — The terms are squares: 21², 12², 31², 13², 41², 14², 51². The roots alternate between a number and its **digit reversal** (21, 12, 31, 13, …). After 51² comes 15² = **225**.
14. **c** — The terms are squares: 12², 21², 13², 31², 14², 41², 15². The roots alternate between a number and its **digit reversal** (12, 21, 13, 31, …). After 15² comes 51² = **2601**.
15. **a** — Two series are woven together. Odd places: 115, 93, 71, 49 (−22 each). Even places: 10, 30, 50 (+20 each). The next place is an even place: 50 + 20 = **70**.

## 8. Recap in 60 seconds

- Write the **gaps** first. Always.
- Steady gap: add. Growing gap: gaps of gaps. Ratio: multiply. Zig-zag gaps: split odd and even places.
- Letters become numbers (A = 1 to Z = 26). Remember E, J, O, T, Y.
- A term made of parts: solve each part as its own series.
- Check your rule on **every** term before answering.
- Learn your squares to 15 and cubes to 10.

## 9. Sources

- Infosys's own 2020 sample paper, section 2 (a series whose gaps are the primes). See `../research/05-source-credibility.md`.
- `../question-banks/QB-99-OBSERVED-POOL.md`: the ten series items reported in 2025, solved by running code.
- Every term and every gap in the examples is checked in `data/cc_examples.py`. No outside website is cited, because series are arithmetic (see `../research/06-method-sources.md`).
