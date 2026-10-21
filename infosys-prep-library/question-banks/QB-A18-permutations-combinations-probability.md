# QB-A18 — Permutations, combinations and probability

**Technical Ability** · **Tier 4** · 12 questions · topic file: see the `A18` file in `topics/`, `puzzles/`, `pseudocode/` or `interview/`

Generated for this library from the rule families seen in the Infosys pool (`../data/gen_*.py`). Every key was recomputed by a second route; see `../research/04-qa-report.md`.

**How to use this bank.** Attempt every question before opening the key. Answer letters are balanced across a–d and not in a repeating pattern, so guessing the pattern will not help.

---

## Practice questions

**1.** **[Arrangements]** In how many distinct ways can the letters of the word BOOKS be arranged?
a) 30
b) 60
c) 56
d) 120

**2.** **[Vowels in odd places]** How many arrangements of the letters of the word BLOCKAGE (all letters different) can be made if the vowels occupy only odd places?
a) 40320
b) 480
c) 720
d) 2880

**3.** **[Selections]** In how many ways can a committee of 2 be chosen from 11 people?
a) 61
b) 11
c) 110
d) 55

**4.** **[Arrangements]** In how many distinct ways can the letters of the word TOMATO be arranged?
a) 180
b) 90
c) 360
d) 720

**5.** **[Coin tosses]** A fair coin is tossed 5 times. What is the probability of getting exactly 2 heads?
a) 5/16
b) 5/8
c) 1/32
d) 2/5

**6.** **[Cards]** A card is drawn at random from a standard pack of 52. What is the probability that it is a king or a heart?
a) 17/52
b) 4/13
c) 1/52
d) 29/52

**7.** **[Complement]** A bag has 5 red, 2 blue and 1 green balls. One ball is drawn at random. What is the probability that it is **not** green?
a) 7/8
b) 1
c) 5/8
d) 1/8

**8.** **[Selections]** In how many ways can a committee of 3 be chosen from 9 people?
a) 504
b) 168
c) 84
d) 36

**9.** **[Onto placements]** 5 different chocolates are placed in 3 different boxes, each box able to hold all 5. In how many ways can this be done if no box is left empty?
a) 243
b) 21
c) 36
d) 150

**10.** **[Selections with a condition]** In how many ways can a team of 3 be chosen from 12 people if one particular person must be in the team?
a) 165
b) 220
c) 55
d) 110

**11.** **[Single draw]** A bag has 3 red, 5 blue and 6 green balls. One ball is drawn at random. What is the probability that it is red?
a) 11/14
b) 3/14
c) 3/5
d) 3/11

**12.** **[Selections with a condition]** In how many ways can a team of 3 be chosen from 10 people if one particular person must be in the team?
a) 120
b) 72
c) 36
d) 84

### ANSWER KEY

1. **b** — 5! = 120, divided by the factorials of the repeats (O ×2): 120 ÷ 2 = **60**.
2. **d** — 3 vowels go into the 4 odd places in P(4,3) = 24 ways; the 5 consonants fill the rest in 120 ways. Total **2880**.
3. **d** — Order does not matter: C(11,2) = 11!/(2!·9!) = **55**.
4. **a** — 6! = 720, divided by the factorials of the repeats (O ×2, T ×2): 720 ÷ 4 = **180**.
5. **a** — C(5,2) = 10 favourable sequences out of 2^5 = 32: **5/16**.
6. **b** — Kings 4 + hearts 13 − the king of hearts counted twice = 16 cards. 16/52 = **4/13**.
7. **a** — 1 − 1/8 = 7/8 = **7/8**.
8. **c** — Order does not matter: C(9,3) = 9!/(3!·6!) = **84**.
9. **d** — Inclusion–exclusion: +C(3,0)·(3)^5 −C(3,1)·(2)^5 +C(3,2)·(1)^5 = **150**. Listing all 243 placements and keeping those that use every box also gives 150.
10. **c** — That person is fixed, so choose the other 2 from the remaining 11: C(11,2) = **55**.
11. **b** — 3 favourable out of 14: **3/14**.
12. **c** — That person is fixed, so choose the other 2 from the remaining 9: C(9,2) = **36**.
