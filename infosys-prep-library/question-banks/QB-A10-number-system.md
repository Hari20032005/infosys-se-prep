# QB-A10 — Number system

**Technical Ability** · **Tier 4** · 12 questions · topic file: see the `A10` file in `topics/`, `puzzles/`, `pseudocode/` or `interview/`

Generated for this library from the rule families seen in the Infosys pool (`../data/gen_*.py`). Every key was recomputed by a second route; see `../research/04-qa-report.md`.

**How to use this bank.** Attempt every question before opening the key. Answer letters are balanced across a–d and not in a repeating pattern, so guessing the pattern will not help.

---

## Practice questions

**1.** **[Divisibility]** Which of these numbers is divisible by 6?
a) 57560
b) 62853
c) 9151
d) 21492

**2.** **[Remainder of a power]** What is the remainder when 9^16 is divided by 11?
a) 9
b) 1
c) 5
d) 10

**3.** **[Divisibility]** Which of these numbers is divisible by 9?
a) 30397
b) 86823
c) 47450
d) 26444

**4.** **[Last digit]** What is the last digit of 16^25?
a) 1
b) 8
c) 6
d) 0

**5.** **[LCM]** Find the LCM of 91 and 74.
a) 6732
b) 1
c) 6825
d) 6734

**6.** **[Last digit]** What is the last digit of 14^47?
a) 4
b) 6
c) 0
d) 8

**7.** **[LCM]** Find the LCM of 99 and 53.
a) 5346
b) 5247
c) 5249
d) 1

**8.** **[Number of factors]** How many positive factors does 180 have?
a) 4
b) 20
c) 18
d) 5

**9.** **[Last digit]** What is the last digit of 17^82?
a) 7
b) 4
c) 9
d) 1

**10.** **[Last digit]** What is the last digit of 11^43?
a) 1
b) 2
c) 6
d) 3

**11.** **[Remainder of a power]** What is the remainder when 25^19 is divided by 4?
a) 3
b) 2
c) 0
d) 1

**12.** **[Divisibility]** Which of these numbers is divisible by 8?
a) 30058
b) 49280
c) 70171
d) 70549

### ANSWER KEY

1. **d** — Use the test: even and digit sum divisible by 3. Only 21492 passes (check: 21492 ÷ 6 = 3582).
2. **a** — Reduce the base first: 9 ≡ 9 (mod 11). Repeated multiplication mod 11 gives remainder **9**.
3. **b** — Use the test: digit sum divisible by 9. Only 86823 passes (check: 86823 ÷ 9 = 9647).
4. **c** — Only the last digit of the base matters: 6. Its powers end in the repeating cycle 6 (length 1). 25 mod 1 = 0, so the last digit is **6**.
5. **d** — LCM = 91 × 74 ÷ HCF = 6734 ÷ 1 = **6734**.
6. **a** — Only the last digit of the base matters: 4. Its powers end in the repeating cycle 4, 6 (length 2). 47 mod 2 = 1, so the last digit is **4**.
7. **b** — LCM = 99 × 53 ÷ HCF = 5247 ÷ 1 = **5247**.
8. **c** — 180 = 2^2 × 3^2 × 5. Number of factors = (2+1) × (2+1) × (1+1) = **18**.
9. **c** — Only the last digit of the base matters: 7. Its powers end in the repeating cycle 7, 9, 3, 1 (length 4). 82 mod 4 = 2, so the last digit is **9**.
10. **a** — Only the last digit of the base matters: 1. Its powers end in the repeating cycle 1 (length 1). 43 mod 1 = 0, so the last digit is **1**.
11. **d** — Reduce the base first: 25 ≡ 1 (mod 4). Repeated multiplication mod 4 gives remainder **1**.
12. **b** — Use the test: last three digits divisible by 8. Only 49280 passes (check: 49280 ÷ 8 = 6160).
