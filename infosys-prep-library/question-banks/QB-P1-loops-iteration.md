# QB-P1 — Loops and Iteration Counting

**Pseudocode** · **Tier 1** · 18 questions

Topic file: [`P1-loops-iteration.md`](/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library/pseudocode/P1-loops-iteration.md)

*Adapted from `accenture-prep-final/accenture-prep-library/question-banks/QB-T25-B1-loops-iteration.md`; verified in that library's QA. Questions and answer key are unchanged.*

**How to use this bank.** Attempt every question before opening the key, at the real pace for this section (120 seconds a question). Answer letters are balanced across a–d.

---

**1.** **[Easy]** *(B1 — running sum, inclusive bounds)*

```text
sum = 0
for i = 1 to 5:
    sum = sum + i
print sum
```

The loop bounds `1 to 5` are inclusive on both ends. What is printed?

(a) 10
(b) 15
(c) 20
(d) 5

**1. (b) 15**
The bound `1 to 5` includes both endpoints, so the body runs 5 times, adding 1+2+3+4+5 = 15.

| i | sum after body |
|---|---|
| 1 | 1 |
| 2 | 3 |
| 3 | 6 |
| 4 | 10 |
| 5 | 15 |

- (a) 10 — assumes the range ends at 4 (1+2+3+4), i.e. an exclusive upper bound.
- (c) 20 — double-counts, e.g. multiplying 5 × 4 or adding 1..5 twice partially.
- (d) 5 — reads the iteration count as the sum.

---

**2.** **[Easy]** *(B1 — do-while minimum execution)*

```text
i = 100
do:
    print i
    i = i + 1
while i < 5
```

How many times does the `print` statement execute?

(a) 0
(b) 1
(c) 10
(d) 5

**2. (b) 1**
A `do-while` tests its condition *after* the body, so the body always executes at least once. Here `i` becomes 101, the test `101 < 5` fails, and the loop stops — one execution.

| step | i before | printed | i after | i < 5 ? |
|---|---|---|---|---|
| 1 | 100 | 100 | 101 | false |

- (a) 0 — treats it as a `while` loop that checks before running.
- (d) 5 — assumes the loop runs until `i` reaches the condition value.
- (c) 10 — arbitrary; the condition is never satisfied and no further passes occur.

---

**3.** **[Easy]** *(B1 — inclusive from-a-to-b count)*

```text
count = 0
for i = 5 to 15:
    count = count + 1
print count
```

What is printed?

(a) 9
(b) 10
(c) 11
(d) 15

**3. (c) 11**
Inclusive counting uses `last − first + 1` = 15 − 5 + 1 = 11.

| i values | count |
|---|---|
| 5,6,7,8,9,10,11,12,13,14,15 | 11 |

- (b) 10 — uses `last − first`, forgetting to add 1 for the inclusive endpoint.
- (a) 9 — uses `last − first − 1`.
- (d) 15 — reports the upper bound value instead of the number of iterations.

---

**4.** **[Easy]** *(B1 — while loop, final value)*

```text
x = 0
while x < 10:
    x = x + 3
print x
```

What is printed?

(a) 9
(b) 12
(c) 10
(d) 13

**4. (b) 12**
`x` takes the values 0, 3, 6, 9 inside the loop; the test `9 < 10` is still true, so the body runs once more and `x` becomes 12. The next test `12 < 10` fails.

| pass | x at test | x after body |
|---|---|---|
| 1 | 0 | 3 |
| 2 | 3 | 6 |
| 3 | 6 | 9 |
| 4 | 9 | 12 (loop ends) |

- (a) 9 — stops at the last value that satisfied the condition instead of the value produced by the final pass.
- (c) 10 — assumes the loop exits exactly at the bound.
- (d) 13 — assumes a fifth pass, but `12 < 10` is false so the body never runs again.

---

**5.** **[Medium]** *(B1 — nested triangular loop count)*

```text
count = 0
for i = 1 to 5:
    for j = 1 to i:
        count = count + 1
print count
```

How many times does the innermost statement execute?

(a) 25
(b) 5
(c) 10
(d) 15

**5. (d) 15**
The inner loop runs `i` times for `i = 1..5`, giving 1+2+3+4+5 = 15.

| i | inner passes |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |

- (a) 25 — uses 5 × 5, ignoring that the inner bound depends on `i`.
- (c) 10 — computes 1+2+3+4, dropping the last outer pass.
- (b) 5 — counts outer iterations only.

---

**6.** **[Medium]** *(B1 — nested loop, expression changes per pass)*

```text
total = 0
for i = 1 to 4:
    for j = 1 to i:
        total = total + j
print total
```

What is printed?

(a) 20
(b) 16
(c) 24
(d) 10

**6. (a) 20**
Each outer pass adds 1+2+...+i, so the total is 1+3+6+10 = 20.

| i | j values | added | total |
|---|---|---|---|
| 1 | 1 | 1 | 1 |
| 2 | 1,2 | 3 | 4 |
| 3 | 1,2,3 | 6 | 10 |
| 4 | 1,2,3,4 | 10 | 20 |

- (d) 10 — reports only the final outer pass's contribution.
- (b) 16 — adds `i` per pass instead of the inner sum of `j`.
- (c) 24 — mistakes the accumulation for a product or sums 1..4 twice with an extra term.

---

**7.** **[Medium]** *(B1 — halving loop, iteration counting)*

```text
n = 20
steps = 0
while n > 1:
    n = n / 2        // integer division, remainder discarded
    steps = steps + 1
print steps
```

What is printed?

(a) 5
(b) 4
(c) 3
(d) 6

**7. (b) 4**
Integer division halves `n` each pass: 20→10→5→2→1. Four halvings occur before `n > 1` becomes false.

| steps | n before | n after |
|---|---|---|
| 1 | 20 | 10 |
| 2 | 10 | 5 |
| 3 | 5 | 2 |
| 4 | 2 | 1 (stop) |

- (a) 5 — assumes `n = 1` triggers one more pass, but the test is `n > 1`.
- (c) 3 — stops when `n` first becomes odd, applying an even-division rule that does not exist.
- (d) 6 — roughly uses log₂(20) rounding up twice.

---

**8.** **[Medium]** *(B1 — descending loop with step)*

```text
count = 0
for i = 10 to 2 step -2:
    count = count + 1
print count
```

What is printed?

(a) 4
(b) 6
(c) 5
(d) 9

**8. (c) 5**
Starting at 10 and subtracting 2 gives 10, 8, 6, 4, 2 — the next value 0 is below the lower bound 2, so the loop stops after 5 iterations.

| i values | count |
|---|---|
| 10, 8, 6, 4, 2 | 5 |

- (a) 4 — stops at 4, treating the lower bound as exclusive.
- (b) 6 — includes 0, ignoring the declared end bound of 2.
- (d) 9 — uses the span 10→2 divided by 1 rather than by the step 2.

---

**9.** **[Medium]** *(B1 — do-while with changing body expression)*

```text
i = 1
s = 0
do:
    s = s + i * i
    i = i + 1
while i <= 3
print s
```

What is printed?

(a) 13
(b) 14
(c) 9
(d) 18

**9. (b) 14**
A `do-while` runs the body before testing, so it processes i = 1, 2, 3 and adds 1+4+9 = 14. The test after the third pass sees i = 4, which fails.

| i before | i*i | s | i after | i <= 3 ? |
|---|---|---|---|---|
| 1 | 1 | 1 | 2 | true |
| 2 | 4 | 5 | 3 | true |
| 3 | 9 | 14 | 4 | false |

- (a) 13 — drops the last added square (9 → 8) or starts the sum at i = 0.
- (c) 9 — adds only the final term.
- (d) 18 — treats `i * i` as `2 * i` and sums 2+4+6+6.

---

**10.** **[Medium]** *(B1 — loop with skip condition)*

```text
count = 0
for i = 1 to 10:
    if i mod 3 = 0:
        continue
    count = count + 1
print count
```

What is printed?

(a) 10
(b) 3
(c) 7
(d) 4

**10. (c) 7**
`continue` skips the rest of the body for that pass, so the multiples of 3 (3, 6, 9) are not counted. 10 − 3 = 7.

| i | i mod 3 = 0 ? | count |
|---|---|---|
| 1,2 | no | 2 |
| 3 | yes (skip) | 2 |
| 4,5 | no | 4 |
| 6 | yes (skip) | 4 |
| 7,8 | no | 6 |
| 9 | yes (skip) | 6 |
| 10 | no | 7 |

- (a) 10 — treats `continue` as a no-op.
- (b) 3 — counts the skipped iterations instead of the kept ones.
- (d) 4 — skips only multiples of 6 or stops after the first skip.

---

**11.** **[Hard]** *(B1 — nested loop with inner bound dependent on outer)*

```text
total = 0
for i = 1 to 3:
    for j = i to 3:
        total = total + i * j
print total
```

What is printed?

(a) 25
(b) 30
(c) 24
(d) 36

**11. (a) 25**
The inner loop starts at `j = i`, so it contributes `i² + i(i+1) + ... + 3i`. Totals are 6, 10 and 9.

| i | j values | i*j values | subtotal |
|---|---|---|---|
| 1 | 1,2,3 | 1,2,3 | 6 |
| 2 | 2,3 | 4,6 | 10 |
| 3 | 3 | 9 | 9 |

Total = 6 + 10 + 9 = 25.

- (c) 24 — assumes `j` starts at 1 for every `i` and adjusts by one term.
- (b) 30 — uses `j = i to 4`, adding an out-of-range term.
- (d) 36 — assumes a full 3 × 3 grid with `i*j` summed (that gives 36 only if `j` runs 1..3 for every `i`; here the lower bound is `i`).

---

**12.** **[Hard]** *(B1 — multiplicative increment, iteration counting)*

```text
n = 1
iterations = 0
while n <= 100:
    n = n * 3
    iterations = iterations + 1
print iterations
```

What is printed?

(a) 5
(b) 4
(c) 6
(d) 3

**12. (a) 5**
`n` triples each pass: 1, 3, 9, 27, 81 all satisfy `n <= 100` at the test, and the fifth pass pushes `n` to 243.

| iterations | n before | n after |
|---|---|---|
| 1 | 1 | 3 |
| 2 | 3 | 9 |
| 3 | 9 | 27 |
| 4 | 27 | 81 |
| 5 | 81 | 243 (stop) |

- (b) 4 — stops when `n` reaches 81, i.e. tests after the multiply instead of before.
- (c) 6 — assumes 243 still passes the test.
- (d) 3 — uses base-10 division intuition rather than tripling.

---

**13.** **[Hard]** *(B1 — inclusive range with a compound divisibility test)*

```text
count = 0
for i = 1 to 20:
    if i mod 4 = 0 or i mod 6 = 0:
        count = count + 1
print count
```

What is printed?

(a) 7
(b) 6
(c) 5
(d) 8

**13. (a) 7**
Multiples of 4 up to 20 are 4, 8, 12, 16, 20 (5 values); multiples of 6 are 6, 12, 18 (3 values). The overlap 12 is counted once, so 5 + 3 − 1 = 7.

| category | values | count |
|---|---|---|
| divisible by 4 | 4, 8, 12, 16, 20 | 5 |
| divisible by 6 | 6, 12, 18 | 3 |
| both (LCM 12) | 12 | 1 |
| union | — | 7 |

- (d) 8 — adds 5 + 3 without removing the double-counted 12.
- (b) 6 — misses 20 or 18 from the range.
- (c) 5 — counts only multiples of 4.

---

**14.** **[Hard]** *(B1 — do-while minimum execution plus counting)*

```text
x = 50
count = 0
do:
    x = x - 7
    count = count + 1
while x > 0
print count
```

What is printed?

(a) 7
(b) 9
(c) 6
(d) 8

**14. (d) 8**
`x` decreases by 7 each pass: after 7 passes `x = 1`, which still satisfies `1 > 0`, so an eighth pass runs and leaves `x = −6`.

| count | x after body | x > 0 ? |
|---|---|---|
| 6 | 8 | true |
| 7 | 1 | true |
| 8 | −6 | false |

- (a) 7 — stops at `x = 1` instead of testing the condition again.
- (c) 6 — treats the loop as `while x >= 7`, i.e. stops at 8.
- (b) 9 — adds a pass because it assumes the loop stops at `x = 0`.

---

**15.** **[Hard]** *(B1 — decreasing triangular loop, body value changes per pass)*

```text
s = 0
for i = 1 to 4:
    for j = 1 to 5 - i:
        s = s + i
print s
```

What is printed?

(a) 15
(b) 10
(c) 20
(d) 24

**15. (c) 20**
The inner loop runs `5 − i` times for `i = 1..4`, and `i` is added each time: 4×1 + 3×2 + 2×3 + 1×4 = 4+6+6+4 = 20.

| i | inner passes (5−i) | added | s |
|---|---|---|---|
| 1 | 4 | 4 | 4 |
| 2 | 3 | 6 | 10 |
| 3 | 2 | 6 | 16 |
| 4 | 1 | 4 | 20 |

- (a) 15 — adds 1 per pass instead of `i`.
- (b) 10 — counts the iterations (4+3+2+1) rather than the accumulated value.
- (d) 24 — uses `5 × i` style bounds, giving 4+8+8+4.

---

**16.** **[Hard]** *(B1 — accumulator with an expression that changes every pass)*

```text
n = 5
result = 0
power = 1
while n > 0:
    result = result + power
    power = power * 2
    n = n - 1
print result
```

What is printed?

(a) 15
(b) 32
(c) 30
(d) 31

**16. (d) 31**
`power` doubles each pass, so the body adds 1, 2, 4, 8, 16 before `n` reaches 0.

| pass | power added | result | n after |
|---|---|---|---|
| 1 | 1 | 1 | 4 |
| 2 | 2 | 3 | 3 |
| 3 | 4 | 7 | 2 |
| 4 | 8 | 15 | 1 |
| 5 | 16 | 31 | 0 (stop) |

- (b) 32 — includes a sixth power term (32) that is never added.
- (c) 30 — starts the doubling from 2 or drops the first addend.
- (a) 15 — stops after four passes, missing the final +16.

---

**17.** **[Hard]** *(B1 — triple nested loop with a condition on indices)*

```text
total = 0
for i = 1 to 3:
    for j = 1 to 3:
        for k = 1 to 3:
            if i = j or j = k:
                total = total + 1
print total
```

What is printed?

(a) 15
(b) 18
(c) 27
(d) 12

**17. (a) 15**
There are 27 triples. Those with `i = j` number 3 × 3 = 9, those with `j = k` number 3 × 3 = 9, and the triple with `i = j = k` (3 of them) is in both sets, so the union is 9 + 9 − 3 = 15.

| condition | triples | count |
|---|---|---|
| i = j (k free) | 3 j-values × 3 k | 9 |
| j = k (i free) | 3 j-values × 3 i | 9 |
| both i=j=k | (1,1,1),(2,2,2),(3,3,3) | 3 |
| union | — | 15 |

- (d) 12 — subtracts 6 instead of 3 for the overlap.
- (b) 18 — adds 9 + 9 and ignores the overlap entirely.
- (c) 27 — counts every triple, treating the `if` as always true.

---

**18.** **[Hard]** *(B1 — descending inclusive range with step, accumulating)*

```text
count = 0
for i = 20 to 5 step -3:
    count = count + i
print count
```

What is printed?

(a) 78
(b) 72
(c) 70
(d) 75

---

**18. (d) 75**
`i` takes the values 20, 17, 14, 11, 8, 5 (six passes, since 5 is exactly reached), and these sum to 75.

| i | running total |
|---|---|
| 20 | 20 |
| 17 | 37 |
| 14 | 51 |
| 11 | 62 |
| 8 | 70 |
| 5 | 75 |

- (a) 78 — includes an extra value (2 below the lower bound) in the sum.
- (b) 72 — omits the final term 5.
- (c) 70 — adds the first five terms only, stopping at 8.

---
