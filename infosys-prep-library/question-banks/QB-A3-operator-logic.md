# QB-A3 — Operator logic

**Reasoning Ability** · **Tier 2** · 20 questions · topic file: see the `A3` file in `topics/`, `puzzles/`, `pseudocode/` or `interview/`

Generated for this library from the rule families seen in the Infosys pool (`../data/gen_*.py`). Every key was recomputed by a second route; see `../research/04-qa-report.md`.

**How to use this bank.** Attempt every question before opening the key. Answer letters are balanced across a–d and not in a repeating pattern, so guessing the pattern will not help.

---

## Practice questions

**1.** **[Sign substitution]** If ‘+’ means ‘×’, ‘−’ means ‘÷’, ‘×’ means ‘+’, ‘÷’ means ‘−’, what is the value of 10 + 8 + 3 × 9 ?
a) 45
b) 249
c) 251
d) -249

**2.** **[Divide then digit-sum]** If 405 ★ 5 = 9 and 228 ★ 2 = 6, find 749 ★ 7.
a) 107
b) 8
c) 9
d) 20

**3.** **[Digit product plus constant]** If $26 = 72 and $44 = 76, what is $69 ? (Here $ is a mathematical operator acting on the two digits.)
a) 114
b) 54
c) 75
d) 124

**4.** **[Sign substitution]** If ‘+’ means ‘÷’, ‘−’ means ‘+’, ‘×’ means ‘−’, ‘÷’ means ‘×’, what is the value of 2 × 12 × 4 × 12 ?
a) 26
b) -26
c) 1152
d) -24

**5.** **[Interchange numbers]** Which two **numbers** must be interchanged for the equation to be correct?

2 + 14 + 4 × 3 = 48
a) 14 and 4
b) 14 and 2
c) 2 and 3
d) 2 and 4

**6.** **[Sign substitution]** If ‘−’ means ‘÷’, ‘×’ means ‘−’, ‘÷’ means ‘×’, what is the value of 10 + 2 + 7 ÷ 12 ?
a) 98
b) 100
c) -96
d) 96

**7.** **[Digit product plus constant]** If $34 = 102 and $82 = 106, what is $97 ? (Here $ is a mathematical operator acting on the two digits.)
a) 153
b) 106
c) 63
d) 163

**8.** **[Digit product plus constant]** If $63 = 68 and $57 = 85, what is $64 ? (Here $ is a mathematical operator acting on the two digits.)
a) 84
b) 60
c) 24
d) 74

**9.** **[Interchange numbers]** Which two **numbers** must be interchanged for the equation to be correct?

9 × 11 − 7 × 4 = −19
a) 11 and 4
b) 7 and 9
c) 9 and 4
d) 11 and 7

**10.** **[Divide then digit-sum]** If 658 ★ 7 = 13 and 584 ★ 8 = 10, find 305 ★ 5.
a) 61
b) 8
c) 15
d) 7

**11.** **[Sign substitution]** If ‘+’ means ‘−’, ‘−’ means ‘+’, what is the value of 3 + 7 × 4 × 3 ?
a) 87
b) -79
c) -81
d) 81

**12.** **[Interchange numbers]** Which two **numbers** must be interchanged for the equation to be correct?

12 − 13 × 7 − 4 = −75
a) 4 and 7
b) 13 and 4
c) 12 and 13
d) 12 and 7

**13.** **[Divide then digit-sum]** If 672 ★ 6 = 4 and 966 ★ 7 = 12, find 304 ★ 4.
a) 13
b) 14
c) 3
d) 76

**14.** **[Interchange numbers]** Which two **numbers** must be interchanged for the equation to be correct?

6 + 10 + 4 − 13 = 25
a) 10 and 6
b) 4 and 6
c) 4 and 13
d) 10 and 4

**15.** **[Sign substitution]** If ‘+’ means ‘×’, ‘−’ means ‘÷’, ‘×’ means ‘−’, ‘÷’ means ‘+’, what is the value of 12 ÷ 4 × 4 − 2 ?
a) -14
b) 14
c) 16
d) 10

**16.** **[Sign substitution]** If ‘+’ means ‘×’, ‘−’ means ‘÷’, ‘×’ means ‘−’, ‘÷’ means ‘+’, what is the value of 5 ÷ 9 × 4 + 9 ?
a) -20
b) -22
c) 22
d) -18

**17.** **[Digit product plus constant]** If $48 = 112 and $52 = 90, what is $14 ? (Here $ is a mathematical operator acting on the two digits.)
a) 4
b) 85
c) 84
d) 94

**18.** **[Digit product plus constant]** If $26 = 102 and $47 = 118, what is $87 ? (Here $ is a mathematical operator acting on the two digits.)
a) 105
b) 156
c) 56
d) 146

**19.** **[Sign substitution]** If ‘+’ means ‘÷’, ‘÷’ means ‘+’, what is the value of 12 × 2 − 2 × 10 ?
a) -4
b) 6
c) 5
d) 4

**20.** **[Divide then digit-sum]** If 536 ★ 4 = 8 and 200 ★ 2 = 1, find 1224 ★ 9.
a) 10
b) 18
c) 11
d) 136

### ANSWER KEY

1. **b** — Swap each sign for what it stands for first: 10 + 8 + 3 × 9 becomes 10 × 8 × 3 + 9. Now apply BODMAS (division and multiplication before addition and subtraction): **249**.
2. **b** — Divide, then add the digits of the quotient **once**. 405 ÷ 5 = 81 → 9; 228 ÷ 2 = 114 → 6. 749 ÷ 7 = 107 → **8**.
3. **a** — Split each number into its digits, multiply them and add 60: 2×6 + 60 = 72; 4×4 + 60 = 76. So $69 = 6×9 + 60 = **114**.
4. **b** — Swap each sign for what it stands for first: 2 × 12 × 4 × 12 becomes 2 − 12 − 4 − 12. Now apply BODMAS (division and multiplication before addition and subtraction): **-26**.
5. **a** — Try the swaps. Interchanging 14 and 4 gives 2 + 4 + 14 × 3 = 48 (BODMAS). No other pair of these numbers works.
6. **d** — Swap each sign for what it stands for first: 10 + 2 + 7 ÷ 12 becomes 10 + 2 + 7 × 12. Now apply BODMAS (division and multiplication before addition and subtraction): **96**.
7. **a** — Split each number into its digits, multiply them and add 90: 3×4 + 90 = 102; 8×2 + 90 = 106. So $97 = 9×7 + 90 = **153**.
8. **d** — Split each number into its digits, multiply them and add 50: 6×3 + 50 = 68; 5×7 + 50 = 85. So $64 = 6×4 + 50 = **74**.
9. **c** — Try the swaps. Interchanging 9 and 4 gives 4 × 11 − 7 × 9 = −19 (BODMAS). No other pair of these numbers works.
10. **d** — Divide, then add the digits of the quotient **once**. 658 ÷ 7 = 94 → 13; 584 ÷ 8 = 73 → 10. 305 ÷ 5 = 61 → **7**.
11. **c** — Swap each sign for what it stands for first: 3 + 7 × 4 × 3 becomes 3 − 7 × 4 × 3. Now apply BODMAS (division and multiplication before addition and subtraction): **-81**.
12. **c** — Try the swaps. Interchanging 12 and 13 gives 13 − 12 × 7 − 4 = −75 (BODMAS). No other pair of these numbers works.
13. **a** — Divide, then add the digits of the quotient **once**. 672 ÷ 6 = 112 → 4; 966 ÷ 7 = 138 → 12. 304 ÷ 4 = 76 → **13**.
14. **c** — Try the swaps. Interchanging 4 and 13 gives 6 + 10 + 13 − 4 = 25 (BODMAS). No other pair of these numbers works.
15. **b** — Swap each sign for what it stands for first: 12 ÷ 4 × 4 − 2 becomes 12 + 4 − 4 ÷ 2. Now apply BODMAS (division and multiplication before addition and subtraction): **14**.
16. **b** — Swap each sign for what it stands for first: 5 ÷ 9 × 4 + 9 becomes 5 + 9 − 4 × 9. Now apply BODMAS (division and multiplication before addition and subtraction): **-22**.
17. **c** — Split each number into its digits, multiply them and add 80: 4×8 + 80 = 112; 5×2 + 80 = 90. So $14 = 1×4 + 80 = **84**.
18. **d** — Split each number into its digits, multiply them and add 90: 2×6 + 90 = 102; 4×7 + 90 = 118. So $87 = 8×7 + 90 = **146**.
19. **d** — Swap each sign for what it stands for first: 12 × 2 − 2 × 10 becomes 12 × 2 − 2 × 10. Now apply BODMAS (division and multiplication before addition and subtraction): **4**.
20. **a** — Divide, then add the digits of the quotient **once**. 536 ÷ 4 = 134 → 8; 200 ÷ 2 = 100 → 1. 1224 ÷ 9 = 136 → **10**.
