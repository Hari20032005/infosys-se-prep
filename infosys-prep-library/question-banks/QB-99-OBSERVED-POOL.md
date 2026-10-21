# QB-99 — Observed Question Pool

**Every question in this file was reported by a source as asked in the Infosys Systems Engineer test.** Nothing here is authored except where a line says so. Items whose data the source lost are listed at the bottom with the reason, not quietly dropped.

**Every numeric and trace answer was re-derived by running `data/verify_observed.py`:**

```bash
python3 data/verify_observed.py
```

**Size and honesty.** 60 unique questions from 8 videos and one first-hand account, plus 25 first-hand interview questions. **All but one of the question sources are coaching videos relaying candidate recall.** That makes each item `[REPORTED]` at best: a coach saying "this was asked" is not the same as a dated paper. Where two channels independently presented the same item it is `[LIKELY]`. Use the pool to calibrate style and difficulty, then get volume from the topic question banks.

| Section | Unique items | Oldest source | Newest source |
|---|---|---|---|
| Reasoning Ability | 20 | 2024-11-04 | 2026-09-22 |
| Technical Ability (mathematical) | 8 | 2025-09-25 | 2026-09-22 |
| Pseudocode | 15 | 2024-12-18 | 2026-09-22 |
| Numerical Puzzle | 15 | 2024-11-04 | 2026-09-22 |
| Verbal Ability | 1 | 2026-09-22 | 2026-09-22 |
| English Writing | 1 | 2025-05-12 | 2025-05-12 |
| **Total** | **60** | | |

**How to use it.** Cover the answer, set a timer at the real per-question pace (Reasoning 100 s, Technical 3.5 min, Pseudocode 2 min, Puzzle 2.5 min), and only then open the working.

---

## 1. Reasoning Ability — 20 items

### R01. Coding-decoding (letter-value average)

> In a certain code LAST is written as 13 and TABLE as 8. How is FRAUD written?

<details><summary>Answer and working</summary>

**Answer: 10**

Take the mean of the letters' alphabet positions. LAST = (12+1+19+20)/4 = 52/4 = 13. TABLE = (20+1+2+12+5)/5 = 40/5 = 8. FRAUD = (6+18+1+21+4)/5 = 50/5 = **10**.

**Pattern to remember:** when a word maps to a small number, try the letter sum first, then sum ÷ length.

**Source:** OnlineStudy4u video, 2026-09-22 — "PYQ … one or two years old" · `[REPORTED]` · verified by execution
</details>

---

### R02. Number series

> Find the missing term: 3, 14, 39, 84, 155, ?, 399

<details><summary>Answer and working</summary>

**Answer: 258**

Differences are 11, 25, 45, 71; second differences 14, 20, 26 rise by 6. Faster: the terms are n³ + n² + n → 3, 14, 39, 84, 155, **258**, 399 (216 + 36 + 6 = 258; 343 + 49 + 7 = 399 checks the last term).

**Source:** OnlineStudy4u video, 2026-09-22 — "PYQ … one or two years old" · `[REPORTED]` · verified by execution
</details>

---

### R03. Alphanumeric series

> Find the next term: H47F, I48G, K50I, ?

<details><summary>Answer and working</summary>

**Answer: N53L**

Three independent tracks, each with gaps +1, +2, next +3. Letters H→I→K→**N**; numbers 47→48→50→**53**; letters F→G→I→**L**. Answer **N53L**.

**Source:** OnlineStudy4u video, 2026-09-22 — "PYQ … one or two years old" · `[REPORTED]` · verified by execution
</details>

---

### R04. Data sufficiency

> What is the smallest of four consecutive even numbers? I. Their sum is 132. II. The difference between the smallest and the largest is 6.

<details><summary>Answer and working</summary>

**Answer: I alone is sufficient (smallest = 30); II is always true for any four consecutive evens**

Statement I: x + (x+2) + (x+4) + (x+6) = 132 → 4x = 120 → x = **30**. Sufficient. Statement II: the gap between the smallest and largest of **any** four consecutive even numbers is 6, so it carries no information. **I alone is sufficient.**

**Source:** OnlineStudy4u video, 2026-09-22 — "PYQ … one or two years old" · `[REPORTED]` · verified by execution
</details>

---

### R05. Coding-decoding (letter-sum)

> In a certain code BURST is written as 80 and LAKE as 29. How is VERSATILE written?

<details><summary>Answer and working</summary>

**Answer: 111**

Sum of alphabet positions. BURST = 2+21+18+19+20 = 80. LAKE = 12+1+11+5 = 29. VERSATILE = 22+5+18+19+1+20+9+12+5 = **111**.

**Speed tip:** memorise E=5, J=10, O=15, T=20, Y=25 ("EJOTY") and count from the nearest anchor.

**Source:** Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination" · also presented independently by YT-2YHL (2025-09-25) · `[LIKELY]` · verified by execution

*Note:* Also presented by OnlineStudy4u (YT-2YHL 2025-09-25, YT-U7HK 2026-09-18); same channel counted once
</details>

---

### R06. Coding-decoding (position rule)

> In a certain code CHAIR is written as 301018. How is TABLE written?

<details><summary>Answer and working</summary>

**Answer: 200205**

Odd positions keep their alphabet number, even positions become 0. CHAIR → C=3, 0, A=1, 0, R=18 → 301018. TABLE → T=20, 0, B=2, 0, E=5 → **200205**.

**Source:** Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination" · `[REPORTED]` · verified by execution
</details>

---

### R07. Number series

> Find the next term: 0, 1, 2, 6, 16, 44, 120, ?

<details><summary>Answer and working</summary>

**Answer: 328**

Each term is twice the sum of the previous two: 2(1+0)=2, 2(2+1)=6, 2(6+2)=16, 2(16+6)=44, 2(44+16)=120, 2(120+44)=**328**.

**Source:** Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination" · `[REPORTED]` · verified by execution
</details>

---

### R08. Number series

> Find the next term: 144, 441, 169, 961, 196, ?

<details><summary>Answer and working</summary>

**Answer: 1681**

Squares with reversed roots: 12², 21², 13², 31², 14², then **41² = 1681**. The source's option letter was inaudible; 1681 is the only value the rule allows.

**Source:** Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination" · `[REPORTED]` · verified by execution

*Note:* Stated option value inaudible; 41^2 = 1681
</details>

---

### R09. Operator logic

> If 264 * 2 = 6 and 870 * 3 = 11, what is 735 * 5?

<details><summary>Answer and working</summary>

**Answer: 12**

Divide, then add the digits of the quotient **once**. 264÷2 = 132 → 1+3+2 = 6. 870÷3 = 290 → 2+9+0 = 11 (note: not reduced again to 2). 735÷5 = 147 → 1+4+7 = **12**.

**Source:** Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination" · `[REPORTED]` · verified by execution
</details>

---

### R10. Syllogism

> Statements: All shoes are legs. Some legs are pairs. Some pairs are hands. Conclusions: I. Some hands are shoes. II. Some pairs are shoes.

*Options as recovered:* I only / II only / both / neither

<details><summary>Answer and working</summary>

**Answer: Neither follows**

Draw a counter-model: shoes inside legs; pairs overlapping legs only outside shoes; hands overlapping pairs only outside legs. All three statements hold and neither conclusion does. Two chained "some" statements never force a definite link. **Neither follows.**

**Source:** Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination" · `[REPORTED]` · verified by execution
</details>

---

### R11. Alphanumeric series

> Find the next term: 3Y6, 8W8, 15U10, 24S12, 35Q14, ?

<details><summary>Answer and working</summary>

**Answer: 48O16**

Three tracks. Numbers 3, 8, 15, 24, 35 are 2²−1 … 6²−1, so next is 7²−1 = 48. Letters Y, W, U, S, Q step back 2 → **O**. Last numbers 6, 8, 10, 12, 14 → 16. Answer **48O16** (the source read the option as "48 O").

**Source:** Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination" · `[REPORTED]` · verified by execution
</details>

---

### R12. Operator logic

> If $59 = 135, $48 = 122 and $96 = 144, then $136 = ?

*Options as recovered:* 168 / ... 

<details><summary>Answer and working</summary>

**Answer: 168**

Subtract the digit product: 135 − 5×9 = 90; 122 − 4×8 = 90; 144 − 9×6 = 90. So $ab = a×b + 90. The offered answer 168 comes from 13×6 + 90. **168.**

**Flag:** reading 136 as 1, 3, 6 gives 1×3×6 + 90 = 108. The question is ambiguous as recalled; 168 is the option the source offered.

**Source:** OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated · `[REPORTED]` · verified by execution
</details>

---

### R13. Blood relation (coded)

> 'x + y' means x is the sister of y, 'x - y' means x is the father of y, 'x * y' means x is the brother of y. Which expression means M is the son of S?

*Options as recovered:* only option B recoverable: S - P + M * G

<details><summary>Answer and working</summary>

**Answer: S - P + M * G**

Decode each symbol. S − P: S is P's father. P + M: P is M's sister, so M is P's sibling and therefore also S's child. M × G: M is G's **brother**, which fixes M as male. So M is S's son → **S − P + M × G**.

Only this option was audible in the source. Distractors to practise against: P × M − S (P is M's brother, M is S's father — wrong direction); S + P − M (S is a sister); M − S + P (M is S's father).

**Source:** OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated · `[REPORTED]` · verified by execution
</details>

---

### R14. Coding-decoding (reverse + shift)

> CREATE is written as DSZDQB. How is POLITE written?

*Options as recovered:* option B: DSHKNO

<details><summary>Answer and working</summary>

**Answer: DSHKNO**

Reverse the word, then shift every letter back by one. CREATE → ETAERC → DSZDQB. POLITE → ETILOP → E−1 = D, T−1 = S, I−1 = H, L−1 = K, O−1 = N, P−1 = O → **DSHKNO**.

The transcript heard the code as "DSJDQB"; only DSZDQB (A−1 wraps to Z) is consistent with the answer the source gave.

**Source:** OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated · `[REPORTED]` · verified by execution
</details>

---

### R15. Coding-decoding (swap)

> If BREAK is written as RBEKA, how is BRIEF written?

<details><summary>Answer and working</summary>

**Answer: RBIFE**

Positions 1-2 swap, 3 stays, 4-5 swap. BREAK → R B E K A. BRIEF → **R B I F E**.

Reported from shift 1 of the early-October 2025 SE exam.

**Source:** OnlineStudy4u video, 2025-10-09 — candidates' recall of the early-October 2025 SE slots · `[REPORTED]` · verified by execution

*Note:* "asked in the shift one" of the early-Oct 2025 SE exam
</details>

---

### R16. Number series

> Find the next term: 13, 17, 19, 23, 29, ?

*Options as recovered:* 31 / 32 / 33 / ...

<details><summary>Answer and working</summary>

**Answer: 31**

Consecutive primes: 13, 17, 19, 23, 29, **31**.

**Source:** OnlineStudy4u video, 2025-10-09 — candidates' recall of the early-October 2025 SE slots · `[REPORTED]` · verified by execution
</details>

---

### R17. Alphanumeric series

> Replace ?: 1D, ?, 5H, 7J, 9L

*Options as recovered:* 3F / 3G / none

<details><summary>Answer and working</summary>

**Answer: 3F**

Numbers are odd 1, 3, 5, 7, 9; letters D, F, H, J, L step +2. Missing term **3F**.

**Source:** Tekno UF video, 2024-11-04 — candidate reports from the 3 Nov 2024 exam · `[REPORTED]` · verified by execution

*Note:* Exam of 3 Nov 2024 (older cycle)
</details>

---

### R18. Alphanumeric series

> Replace ?: 12M, ?, 14Q, 15S

*Options as recovered:* 13F / 13O / 13N / 13H

<details><summary>Answer and working</summary>

**Answer: 13O**

Numbers 12, 13, 14, 15; letters M, O, Q, S step +2. Missing term **13O**.

**Source:** Tekno UF video, 2024-11-04 — candidate reports from the 3 Nov 2024 exam · `[REPORTED]` · verified by execution
</details>

---

### R19. Number series

> Find the next term: 100, 20, 80, 50, 60, 80, ?

<details><summary>Answer and working</summary>

**Answer: 40**

Two series interleaved. Odd places: 100, 80, 60, **40** (−20). Even places: 20, 50, 80 (+30). The 7th term is in the odd series: **40**.

**Source:** Tekno UF video, 2024-11-04 — candidate reports from the 3 Nov 2024 exam · `[REPORTED]` · verified by execution
</details>

---

### R20. Number series

> Find the missing term: 91, 94, 100, 109, ?, 136

*Options as recovered:* ... / 121

<details><summary>Answer and working</summary>

**Answer: 121**

Differences 3, 6, 9, 12, 15. 109 + 12 = **121**, and 121 + 15 = 136 confirms it.

**Source:** OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated · `[REPORTED]` · verified by execution

*Note:* Re-used in YT-U7HK
</details>

---

## 2. Technical Ability (mathematical) — 8 items

### Q01. Linear equations / quantity comparison

> If 2x + 3y = 7 and 5x + 8y = 2, which relation between x and y holds?

*Options as recovered:* x>y / x<y / x=y / cannot be determined

<details><summary>Answer and working</summary>

**Answer: x > y (x = 50, y = -31)**

Eliminate x: 5×(2x + 3y = 7) → 10x + 15y = 35; 2×(5x + 8y = 2) → 10x + 16y = 4. Subtract: y = −31. Then 2x = 7 + 93 → x = 50. **x > y.**

**Source:** OnlineStudy4u video, 2026-09-22 — "PYQ … one or two years old" · `[REPORTED]` · verified by execution
</details>

---

### Q02. Ages / ratio

> The present ages of A and B are 48 and 72. Find the ratio of A's age 3 years ago to B's age 3 years from now.

<details><summary>Answer and working</summary>

**Answer: 3:5**

Three years ago: 45. Three years hence: 75. 45 : 75 = **3 : 5**.

**Source:** Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination" · also presented independently by YT-2YHL (2025-09-25) · `[LIKELY]` · verified by execution
</details>

---

### Q03. Data interpretation (table)

> Heights of 400 students: 140-150 cm: 150; 150-160: 88; 160-170: 70; 170-180: 50; 180-190: 42. What percentage are shorter than 170 cm?

*Options as recovered:* includes 77%

<details><summary>Answer and working</summary>

**Answer: 77%**

Shorter than 170 cm = the first three classes: 150 + 88 + 70 = 308. 308/400 = **77%**. Check the table sums to 400 (150+88+70+50+42 = 400) — if it did not, the recall would be suspect.

**Source:** Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination" · also presented independently by YT-2YHL (2025-09-25) · `[LIKELY]` · verified by execution

*Note:* Source: "this year more DI questions are getting asked"
</details>

---

### Q04. Averages

> The sum of 15 observations is 2100. Every observation is doubled and then reduced by 10. By how much does the average increase?

<details><summary>Answer and working</summary>

**Answer: 130**

Old mean = 2100/15 = 140. Doubling and subtracting 10 applies the same to the mean: 2×140 − 10 = 270. Increase = **130**.

**Rule:** a linear change to every data point (ax + b) changes the mean the same way. It does not need the individual values.

**Source:** Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination" · `[REPORTED]` · verified by execution
</details>

---

### Q05. Linear equations (heads and legs)

> A farm has cows and hens: 45 heads and 130 legs in total. How many cows?

<details><summary>Answer and working</summary>

**Answer: 20**

Assume all 45 are hens: 90 legs. The extra 40 legs come from cows, 2 extra each → **20 cows**.

**Source:** Placement Walaa video, 2025-09-29 — "asked in recent Infosys examination" · `[REPORTED]` · verified by execution
</details>

---

### Q06. Number system (primes, cube root)

> What is the cube root of the product of the non-prime numbers on a telephone keypad?

*Options as recovered:* ... / 12

<details><summary>Answer and working</summary>

**Answer: 12 (reading "non-prime" as the composites 4, 6, 8, 9)**

The keypad digits are 0–9. The primes are 2, 3, 5, 7. "Non-prime" is intended as the **composites** 4, 6, 8, 9: 4×6×8×9 = 1728 = 12³. Cube root **12**.

**Trap worth knowing:** 0 and 1 are also non-prime. Including 0 makes the product 0. On the real test, pick the reading that produces an offered option.

**Source:** OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated · `[REPORTED]` · verified by execution
</details>

---

### Q07. Data interpretation (pie)

> A student's total is 400 marks, split English 25%, Hindi 34%, Maths 18%, Science 10%, History 13%. Pass mark per subject is 50. In which subject did he fail, and what is the gap between his best and worst subject?

*Options as recovered:* Science, 88 / Science, 96 / ...

<details><summary>Answer and working</summary>

**Answer: Science; 96**

Convert percentages of 400: English 100, Hindi 136, Maths 72, Science **40**, History 52. Only Science is below 50 → failed in Science. Best − worst = 136 − 40 = **96**.

**Source defect:** the stem says marks are "out of 100", but Hindi comes to 136. The recall is internally inconsistent; the answer stands on the chart data.

**Source:** OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated · `[REPORTED]` · verified by execution
</details>

---

### Q08. Mensuration (sphere)

> The surface area of a sphere is 154 cm^2. Find its volume (pi = 22/7).

<details><summary>Answer and working</summary>

**Answer: 179.67 cm^3 (539/3)**

4πr² = 154 → r² = 154 × 7/88 = 12.25 → r = 3.5. V = (4/3) × (22/7) × 3.5³ = 539/3 ≈ **179.67 cm³**. The source said "around 180".

**Source:** OnlineStudy4u video, 2025-10-09 — candidates' recall of the early-October 2025 SE slots · `[REPORTED]` · verified by execution
</details>

---

## 3. Pseudocode — 15 items

### P01. Loop + integer division

> for w = 0 to 5: if (w mod 2 == 0 and w / 2 == 0) display w

<details><summary>Answer and working</summary>

**Answer: 0**

w runs 0..5. Integer division: w/2 == 0 only for w = 0 and 1. Of those, only 0 is even. Output **0**.

**Source:** OnlineStudy4u video, 2026-09-22 — "PYQ … one or two years old" · `[REPORTED]` · verified by execution

*Note:* 2 marks per pseudocode item (source)
</details>

---

### P02. Modulus + loop

> x = 27 mod 7; for i = 0 to x: display i

<details><summary>Answer and working</summary>

**Answer: 0 1 2 3 4 5 6**

27 mod 7 = 6. The loop displays **0 1 2 3 4 5 6**.

**Source:** OnlineStudy4u video, 2026-09-22 — "PYQ … one or two years old" · `[REPORTED]` · verified by execution
</details>

---

### P03. Bitwise precedence

> Integer p = 1, q = 1. p = p ^ 1 & 1 + q ^ 1 & 1. Print p + q.

<details><summary>Answer and working</summary>

**Answer: 1**

In C and Java, `+` binds tighter than `&`, which binds tighter than `^`: p = 1 ^ (1 & (1+1)) ^ (1 & 1) = 1 ^ 0 ^ 1 = 0. Reading strictly left to right also gives p = 0. Either way p + q = 0 + 1 = **1**.

**Know the order:** arithmetic > shifts > relational > `&` > `^` > `|` > `&&` > `||`.

**Source:** OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated · `[REPORTED]` · verified by execution

*Note:* Operator symbols reconstructed from ASR ("J" = ^); answer is robust to both readings
</details>

---

### P04. Do-while

> Integer x = 0. do { ++x; display x; x--; } while (x >= -1)

<details><summary>Answer and working</summary>

**Answer: infinite loop printing 1**

x starts at 0. Each pass: ++x makes 1, display 1, x-- returns it to 0. The test 0 ≥ −1 is always true. **Infinite loop printing 1.**

**Source:** OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated · `[REPORTED]` · verified by execution
</details>

---

### P05. While + mod

> n = 26, i = 0. while (n mod 8 != 0) { n = n + 5; i = i + 1 }. n = n + i. print n

*Options as recovered:* 0 / 11 / 22 / 62

<details><summary>Answer and working</summary>

**Answer: 62**

Add 5 until n is divisible by 8: 26→31→36→41→46→51→56 (six additions, i = 6). Then n + i = 56 + 6 = **62**.

**Source:** OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated · `[REPORTED]` · verified by execution
</details>

---

### P06. For loop accumulate

> x = 3, y = 2, result = 0. for i = 1 to y: result = result + x * i. print result

<details><summary>Answer and working</summary>

**Answer: 9**

result = 3×1 + 3×2 = **9**.

**Source:** Code Bashers video, 2024-12-18 — "latest pseudo code questions asked in SE hiring" · `[REPORTED]` · verified by execution

*Note:* Older cycle (Dec 2024)
</details>

---

### P07. Recursion (factorial)

> Standard recursive factorial; output for n = 5?

<details><summary>Answer and working</summary>

**Answer: 120**

5! = 5×4×3×2×1 = **120**.

**Source:** Code Bashers video, 2024-12-18 — "latest pseudo code questions asked in SE hiring" · `[REPORTED]` · verified by execution

*Note:* Code shown on screen only; reconstructed as textbook factorial
</details>

---

### P08. Digit sum

> n = 123, sum = 0. while n > 0: sum = sum + n mod 10; n = n / 10. print sum

<details><summary>Answer and working</summary>

**Answer: 6**

Digit sum of 123 with integer division: 3 + 2 + 1 = **6**.

**Source:** Code Bashers video, 2024-12-18 — "latest pseudo code questions asked in SE hiring" · `[REPORTED]` · verified by execution
</details>

---

### P09. Branch in loop

> n = 6, sum = 0. for i = 1 to n: if i mod 2 == 0 then sum = sum + i*i else sum = sum + i. print sum

<details><summary>Answer and working</summary>

**Answer: 65**

Odd i add i: 1 + 3 + 5 = 9. Even i add i²: 4 + 16 + 36 = 56. Total **65**.

**Source:** Code Bashers video, 2024-12-18 — "latest pseudo code questions asked in SE hiring" · `[REPORTED]` · verified by execution
</details>

---

### P10. Recursion (power)

> function calc(a, b): if b == 0 return 1 else return a * calc(a, b - 1). Output of calc(6, 3)?

<details><summary>Answer and working</summary>

**Answer: 216**

calc(a, b) = a^b: 6³ = **216**.

**Source:** Code Bashers video, 2024-12-18 — "latest pseudo code questions asked in SE hiring" · `[REPORTED]` · verified by execution
</details>

---

### P11. Recursion (accumulating argument)

> function f(x, y): if y == 0 return x else return f(x + y, y - 1). Output of f(7, 2)?

<details><summary>Answer and working</summary>

**Answer: 10**

f(7,2) → f(9,1) → f(10,0) → **10**.

**Source:** Code Bashers video, 2024-12-18 — "latest pseudo code questions asked in SE hiring" · `[REPORTED]` · verified by execution
</details>

---

### P12. Arrays (product except self)

> total = product of all elements; result[i] = total / a[i]. Input 2, 3, 4, 5. Output?

*Options as recovered:* 60 40 30 24 / 60 40 20 ...

<details><summary>Answer and working</summary>

**Answer: 60 40 30 24**

Product of all = 2×3×4×5 = 120. Divide by each element: 60, 40, 30, 24. Output **60 40 30 24**.

**Source:** OnlineStudy4u video, 2026-09-18 — "PYQ … 4th/11th/16th October 2025" · `[REPORTED]` · verified by execution

*Note:* Presenter: "these pseudo code questions were asked in 2025"
</details>

---

### P13. Pre/post increment (fill the blank)

> i = 5. Which statement makes both result and i equal 6 when the function returns?

*Options as recovered:* options inaudible

<details><summary>Answer and working</summary>

**Answer: result = ++i**

`result = ++i` increments first, then assigns: i = 6, result = 6. `result = i++` gives result 5, i 6. `result = i + 1` leaves i at 5. `result = --i + 2` gives 6 but leaves i at 4. **result = ++i.**

Only the answer was audible in the source; the other three options here are authored.

**Source:** OnlineStudy4u video, 2026-09-18 — "PYQ … 4th/11th/16th October 2025" · `[REPORTED]` · verified by execution
</details>

---

### P14. Pre/post increment (fill the blank)

> i = 2. Choose result = ___ so that result prints 7.

*Options as recovered:* combinations of i++ and ++i

<details><summary>Answer and working</summary>

**Answer: ++i + ++i (3 + 4)**

Java evaluates operands left to right. i = 2: `++i` → 3 (i = 3), then `++i` → 4 (i = 4). 3 + 4 = **7**. The other combinations: `i++ + i++` = 2 + 3 = 5; `i++ + ++i` = 2 + 4 = 6; `++i + i++` = 3 + 3 = 6.

**Warning:** in C this expression is undefined behaviour. Infosys pseudocode assumes the Java-style left-to-right reading.

**Source:** OnlineStudy4u video, 2026-09-18 — "PYQ … 4th/11th/16th October 2025" · `[REPORTED]` · verified by execution
</details>

---

### P15. Arrays (longest increasing run)

> cur = 1, best = 1. for i = 1 to n-1: if a[i] > a[i-1] then cur++ ; best = max(best, cur) else cur = 1. Output for [1, 2, 2, 3, 4, 5, 1]?

*Options as recovered:* options inaudible

<details><summary>Answer and working</summary>

**Answer: 4**

The function tracks the longest **strictly** increasing run. [1, 2, 2, 3, 4, 5, 1]: 1→2 (run 2), 2→2 resets (not >), 2→3→4→5 (run 4), 5→1 resets. Answer **4**.

**The trap:** 1, 2, 2, 3, 4, 5 looks like a run of 6, but the repeated 2 breaks it.

**Source:** OnlineStudy4u video, 2026-09-18 — "PYQ … 4th/11th/16th October 2025" · `[REPORTED]` · verified by execution

*Note:* Presenter: "one of the very trickier question which was asked"
</details>

---

## 4. Numerical Puzzle — 15 items

### Z01. 4x4 grid (row sum)

> Grid rows: 1 5 6 3 / 9 1 2 3 / 1 1 6 7 / 4 1 2 ?

<details><summary>Answer and working</summary>

**Answer: 8**

Every complete row sums to 15 (1+5+6+3, 9+1+2+3, 1+1+6+7). Last row: 4 + 1 + 2 + ? = 15 → **8**.

**Source:** OnlineStudy4u video, 2026-09-22 — "PYQ … one or two years old" · `[REPORTED]` · verified by execution

*Note:* Source: "this is for two marks"
</details>

---

### Z02. Row rule

> Rows: 7 6 42 36 / 8 4 32 16 / 10 12 120 ?

<details><summary>Answer and working</summary>

**Answer: 144**

Each row is a, b, a×b, b². 7, 6, 42, 36; 8, 4, 32, 16; 10, 12, 120, **144**.

**Source:** OnlineStudy4u video, 2026-09-22 — "PYQ … one or two years old" · `[REPORTED]` · verified by execution
</details>

---

### Z03. Figure (outer -> centre)

> Figure 1: 3, 7, 5, 1 -> 16. Figure 2: 9, 8, 34, 2 -> 4. Figure 3: 15, 12, 21, 8 -> ?

*Options as recovered:* ... / 12

<details><summary>Answer and working</summary>

**Answer: 12**

Centre = (first × second) − (third × fourth). 3×7 − 5×1 = 16; 9×8 − 34×2 = 4; 15×12 − 21×8 = 180 − 168 = **12**.

**Source:** OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated · `[REPORTED]` · verified by execution

*Note:* Re-used in YT-U7HK
</details>

---

### Z04. Diagonal pairs

> Opposite pairs 36 & 12 -> 48, 8 & 32 -> 40, 16 & 25 -> 41, 39 & 7 -> ?

*Options as recovered:* ... / 46

<details><summary>Answer and working</summary>

**Answer: 46**

Each value is the sum of its opposite pair: 36+12 = 48, 8+32 = 40, 16+25 = 41, 39+7 = **46**.

**Source:** OnlineStudy4u video, 2025-09-25 — "Infosys PYQ", undated · `[REPORTED]` · verified by execution

*Note:* Re-used in YT-U7HK
</details>

---

### Z05. Figure (two products)

> Figure 1: (11, 4) and (2, 2) -> 48. Figure 2: (7, 7) and (5, 6) -> 79. Figure 3: (8, 8) and (12, 9) -> ?

*Options as recovered:* ... / 172

<details><summary>Answer and working</summary>

**Answer: 172**

Centre = product of one pair + product of the other. 11×4 + 2×2 = 48; 7×7 + 5×6 = 79; 8×8 + 12×9 = 64 + 108 = **172**.

**Source:** OnlineStudy4u video, 2026-09-18 — "PYQ … 4th/11th/16th October 2025" · `[REPORTED]` · verified by execution

*Note:* Also YT-2YHL (same channel)
</details>

---

### Z06. Pair rule

> (5, 11) -> 58, (12, 8) -> 99, (16, 7) -> ?

*Options as recovered:* 115

<details><summary>Answer and working</summary>

**Answer: 115**

a × b + 3: 5×11+3 = 58; 12×8+3 = 99; 16×7+3 = **115**.

**Source:** OnlineStudy4u video, 2025-10-09 — candidates' recall of the early-October 2025 SE slots · `[REPORTED]` · verified by execution

*Note:* Early-Oct 2025 SE slot
</details>

---

### Z07. 4x4 grid (row rule)

> Rows: 8 3 6 26 / 4 9 12 112 / 5 7 2 19 / 9 6 4 ?

<details><summary>Answer and working</summary>

**Answer: 33**

Fourth = second × third + first. 3×6+8 = 26; 9×12+4 = 112; 7×2+5 = 19; 6×4+9 = **33**.

Reported as a 4×4 matrix puzzle from the early-October 2025 slots.

**Source:** OnlineStudy4u video, 2025-10-09 — candidates' recall of the early-October 2025 SE slots · `[REPORTED]` · verified by execution

*Note:* Early-Oct 2025 SE slot; "4x4 matrix puzzles were asked"
</details>

---

### Z08. Pair rule (difference of squares)

> (15, 10) -> 125, (18, 11) -> 203, (21, 16) -> ?

<details><summary>Answer and working</summary>

**Answer: 185**

Difference of squares: 15² − 10² = 225 − 100 = 125; 18² − 11² = 203; 21² − 16² = 441 − 256 = **185**.

Students called this the hardest puzzle of the slot. The middle value was inaudible in the source and is filled in by the same rule.

**Source:** OnlineStudy4u video, 2025-10-09 — candidates' recall of the early-October 2025 SE slots · `[REPORTED]` · verified by execution
</details>

---

### Z09. 3x3 grid (row product)

> Rows: 20 4 5 / 48 6 8 / ? 8 4

<details><summary>Answer and working</summary>

**Answer: 32**

First = second × third: 4×5 = 20, 6×8 = 48, 8×4 = **32**.

**Source:** OnlineStudy4u video, 2025-10-09 — candidates' recall of the early-October 2025 SE slots · `[REPORTED]` · verified by execution

*Note:* "This is from the shift two"
</details>

---

### Z10. Grid of 2-digit pairs

> Top row 35 32 51, bottom row 43 46 61, middle row ? 30 11

<details><summary>Answer and working</summary>

**Answer: 27**

Multiply the digits of the top number and the bottom number, then add. 32 & 46: 3×2 + 4×6 = 30 ✓. 51 & 61: 5×1 + 6×1 = 11 ✓. 35 & 43: 3×5 + 4×3 = **27**.

**Source:** OnlineStudy4u video, 2025-09-27 — "Infosys previous-year puzzles" · `[REPORTED]` · verified by execution
</details>

---

### Z11. Triangular numbers

> 4 4 10, 5 5 15, 6 6 21, 8 8 36, 9 9 ?

<details><summary>Answer and working</summary>

**Answer: 45**

Third = n(n+1)/2 (triangular numbers): 10, 15, 21, 36, then 9×10/2 = **45**.

**Source:** OnlineStudy4u video, 2025-09-27 — "Infosys previous-year puzzles" · `[REPORTED]` · verified by execution

*Note:* Source: "most repeated and common pattern"
</details>

---

### Z12. Boxes (products)

> Box 1: (2,2)->4, (3,3)->9, (5,4)->20. Box 2: (4,2)->8, (4,3)->12, (?,4)->28

*Options as recovered:* ... B: 7

<details><summary>Answer and working</summary>

**Answer: 7**

Every entry is the product of its pair. (?, 4) → 28 → **7**.

**Source:** OnlineStudy4u video, 2025-09-27 — "Infosys previous-year puzzles" · `[REPORTED]` · verified by execution
</details>

---

### Z13. Pair rule (digit products)

> (58, 75) -> 5, (96, 38) -> 30, (62, 23) -> ?

<details><summary>Answer and working</summary>

**Answer: 6**

Digit product of the first minus digit product of the second: 5×8 − 7×5 = 5; 9×6 − 3×8 = 30; 6×2 − 2×3 = **6**.

**Source:** OnlineStudy4u video, 2025-09-27 — "Infosys previous-year puzzles" · `[REPORTED]` · verified by execution
</details>

---

### Z14. Pair rule (digit sum of sum)

> (43, 17) -> 6, (63, 27) -> 9, (44, 56) -> ?

*Options as recovered:* A: 1

<details><summary>Answer and working</summary>

**Answer: 1**

Add the pair, then take the digit sum: 43+17 = 60 → 6; 63+27 = 90 → 9; 44+56 = 100 → **1**.

**Source:** OnlineStudy4u video, 2025-09-27 — "Infosys previous-year puzzles" · `[REPORTED]` · verified by execution

*Note:* Presenter flagged a misprint in the options
</details>

---

### Z15. Pair rule (product)

> (11, 32) -> 352, (12, 33) -> 396, (13, 34) -> ?

*Options as recovered:* four options by last digit

<details><summary>Answer and working</summary>

**Answer: 442**

Plain product: 11×32 = 352, 12×33 = 396, 13×34 = **442**.

**Source:** Tekno UF video, 2024-11-04 — candidate reports from the 3 Nov 2024 exam · `[REPORTED]` · verified by execution

*Note:* Exam of 3 Nov 2024 (older cycle)
</details>

---

## 5. Verbal Ability — 1 items

### V01. Spotting errors

> Spot the error: The IRC has already expressed / it's concern over the increasingly / draconian nature of legislation in the UK. / No error

*Options as recovered:* 3 parts + no error

<details><summary>Answer and working</summary>

**Answer: part 2: it's -> its**

"It's" means "it is". The possessive is **its**. Error in part 2: *expressed **its** concern over …*

**Source:** OnlineStudy4u video, 2026-09-22 — "PYQ … one or two years old" · `[REPORTED]` · verified by grammar rule

*Note:* Sentence reconstructed from ASR
</details>

---

## 6. English Writing — 1 items

### W01. English writing test

> Write an essay on ozone layer depletion.

<details><summary>How to approach it</summary>

Ten minutes, about 190–200 words, four paragraphs: define the problem (the ozone layer absorbs UV-B; CFCs and halons break O₃ down, most visibly as the Antarctic ozone hole); effects (skin cancer, cataracts, crop and marine damage); response (the 1987 Montreal Protocol phased out CFCs, and the layer is recovering); one-line conclusion. Grammar and coherence are marked, not originality. Full method in `topics/W1-english-writing.md`.

**Source:** First-hand Naukri Code360 account, on-campus SE test of 12 May 2025 · `[REPORTED]` · verified by n/a

*Note:* First-hand, on-campus SE test of 12 May 2025
</details>

---

## 7. Interview questions — first-hand, 2024-25

These come from five first-hand accounts (B1–B5 in `data/reviews-online.csv`). Model answers are in `interview/`.

| ID | Account | Date | Type | Question |
|---|---|---|---|---|
| I01 | B1 | 2025-05-12 | technical | Define SDLC. |
| I02 | B1 | 2025-05-12 | technical | Difference between Waterfall and Agile. |
| I03 | B1 | 2025-05-12 | technical | Define OOP and explain its four pillars. |
| I04 | B1 | 2025-05-12 | technical | Explain the access specifiers in Java. |
| I05 | B2 | 2025-01-10 | HR/behavioural | How do you handle rejections? |
| I06 | B2 | 2025-01-10 | HR/behavioural | How do you manage time and prioritise tasks? |
| I07 | B2 | 2025-01-10 | HR/behavioural | Explain your final-year project in detail. |
| I08 | B2 | 2025-01-10 | HR/behavioural | Why has your CGPA been declining? |
| I09 | B2 | 2025-01-10 | technical | What is the SDLC? |
| I10 | B2 | 2025-01-10 | technical | Who is a Scrum Master? |
| I11 | B2 | 2025-01-10 | technical | What is sprint planning? |
| I12 | B3 | 2025-12-04 | technical | Difference between method overloading and method overriding, with examples. |
| I13 | B3 | 2025-12-04 | technical | Explain the SDLC and different SDLC models. |
| I14 | B4 | 2025-01-20 | HR/behavioural | Introduce yourself and say why you want to join Infosys. |
| I15 | B4 | 2025-01-20 | technical | What is SDLC and why is it needed? |
| I16 | B4 | 2025-01-20 | technical | What are joins and what are their types? |
| I17 | B5 | 2025-01 | HR/behavioural | Explain your capstone project. |
| I18 | B5 | 2025-01 | technical | Write a program to check a palindrome. |
| I19 | B5 | 2025-01 | technical | Java or Python, and why? |
| I20 | B5 | 2025-01 | HR/behavioural | What do you do beyond academics? |
| I21 | B5 | 2025-01 | HR/behavioural | Are you willing to relocate? |
| I22 | B5 | 2025-01 | HR/behavioural | Why a job rather than higher studies? |
| I23 | B5 | 2025-01 | HR/behavioural | How do you handle stressful situations? |
| I24 | B5 | 2025-01 | HR/behavioural | What is your opinion of generative AI? |
| I25 | B5 | 2025-01 | HR/behavioural | How do you use AI in daily life? |

**What recurs:** SDLC in four of five accounts, OOP in three, projects in three. Behavioural questions (rejection, stress, time management, relocation) replace a separate behavioural test.

## 8. Repeat rate

- **Independent repeats:** 3 of 60 unique questions (5.0%) were presented by two different channels: R05, Q02, Q03. Both channels may share one upstream PYQ file, so treat this as corroboration that the item circulates, not as a measured exam repeat.
- **Cross-slot repeats cannot be measured.** No source ties one question to two different slots or dates.
- **Same-channel reuse** (OnlineStudy4u showing the same slide in 2025 and 2026) is not counted.

## 9. Verification record

| Check | Result |
|---|---|
| `verify_observed.py` | every reasoning, quant, pseudocode and puzzle answer recomputed; **0 mismatches** after two verifier bugs were fixed (see `research/04-qa-report.md`) |
| Source answers that differ from ours | R08 (option letter inaudible), R12 (ambiguous reading, flagged), Q07 (stem defective, flagged) |
| Pseudocode in Java | all 15 observed pseudocode items (P01–P15) re-run as real Java by `data/verify_generated.py` |

## 10. Discarded items — 16, with reasons

| ID | Source | Item | Why discarded |
|---|---|---|---|
| X01 | YT-2MBO | interchange-two-numbers equation | operators lost in ASR; cannot re-pose |
| X02 | YT-2MBO | histogram DI (pass % at 60% of 50) | chart values never spoken |
| X03 | YT-2MBO | DS probability (red/green/blue) | value in statement II not spoken |
| X04 | YT-2YHL/YT-U7HK | figure puzzle "5, ?, 68, 73" -> 52 | layout unrecoverable |
| X05 | YT-5XTG | "100 in between" shift-one puzzle | stub; data inaudible |
| X06 | YT-5XTG | shift-two "412 - 39? = 40" puzzle | stated arithmetic (412 - 398 = 14) does not produce 40; transcription defective |
| X07 | YT-6UFT | grid 5 3 7 / 2 4 1 / 1 3 ? -> 75 | cell layout lost |
| X08 | YT-6UFT | 3 and 2 -> 11 pattern | presenter never states a working rule |
| X09 | YT-6UFT | triangle figure -> 15 | stub |
| X10 | YT-6UFT | ring 6 15 23 48 / 30 45 41 36 | presenter: "if 46 is in the options take 46, otherwise 50" - no determinable rule |
| X11 | YT-6UFT | 50 16 32 / 49 33 16 / ? grid | presenter calls it a "junk question"; rule incomplete |
| X12 | YT-KC2G | series 8705, 263, 11, 951, 15123 | digit grouping unrecoverable |
| X13 | YT-KC2G | series 28456 ... 777 | stub |
| X14 | YT-KC2G | quiz series 5821, 55117 | stub |
| X15 | YT-KC2G | quiz question shown on screen | content never spoken |
| X16 | YT-U7HK | puzzle "question four" | stub |

All of these are auto-caption losses: the question was on screen and the presenter never read the data aloud. They still count as evidence of section content (grid puzzles, data sufficiency, DI) in `data/analyze.py`, but not as study material.
