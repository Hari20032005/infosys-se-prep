# QB-P8 — Reading Time and Space Complexity off a Snippet

**Pseudocode** · **Tier 4** · 18 questions

Topic file: [`P8-snippet-complexity.md`](/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library/pseudocode/P8-snippet-complexity.md)

*Adapted from `accenture-prep-final/accenture-prep-library/question-banks/QB-T32-B9-snippet-complexity.md`; verified in that library's QA. Questions and answer key are unchanged.*

**How to use this bank.** Attempt every question before opening the key, at the real pace for this section (120 seconds a question). Answer letters are balanced across a–d.

---

**1.** **[Easy]** *(B9 — sequential loops)*
```text
sum = 0
for i = 1 to n:
    sum = sum + i
for j = 1 to n:
    sum = sum + j
```
What is the time complexity?
(a) O(1)
(b) O(log n)
(c) O(n^2)
(d) O(n)

**1. (d) O(n)**
The two loops are sequential, so their costs add: O(n) + O(n) = O(n).
- (b) O(log n): wrong because each loop increments by 1, not by doubling or halving.
- (c) O(n^2): wrong because the loops are not nested.
- (a) O(1): wrong because the work depends linearly on n.

Trace:
| n | first loop iterations | second loop iterations | total |
|---|---:|---:|---:|
| 4 | 4 | 4 | 8 |
| 8 | 8 | 8 | 16 |

---

**2.** **[Easy]** *(B9 — nested vs sequential loops)*
```text
for i = 1 to n:
    for j = 1 to m:
        x = x + 1
```
What is the time complexity?
(a) O(n × m)
(b) O(n + m)
(c) O(n^2)
(d) O(m^2)

**2. (a) O(n × m)**
The outer loop runs n times, and for each outer iteration the inner loop runs m times, giving n × m operations.
- (b) O(n + m): wrong because nested loops multiply, not add.
- (c) O(n^2): wrong because the inner bound is m, not necessarily n.
- (d) O(m^2): wrong because the outer loop contributes n repetitions.

Trace:
| n | m | inner increments |
|---:|---:|---:|
| 3 | 4 | 12 |
| 5 | 2 | 10 |

---

**3.** **[Easy]** *(B9 — constant time)*
```text
a = 5
b = a * 2
c = a + b
```
n is an input variable not used by this block. What is the time complexity?
(a) O(log n)
(b) O(n)
(c) O(n^2)
(d) O(1)

**3. (d) O(1)**
The block has a fixed number of assignments and arithmetic operations, independent of n.
- (a) O(log n): wrong because n is not used at all.
- (b) O(n): wrong because there is no loop over n.
- (c) O(n^2): wrong because there is no nested loop.

Trace:
| n | operations |
|---:|---:|
| any | 3 assignments |
| any | constant |

---

**4.** **[Easy]** *(B9 — single loop count)*
```text
count = 0
for i = 1 to n:
    count = count + 1
```
What is the time complexity?
(a) O(n)
(b) O(log n)
(c) O(n^2)
(d) O(1)

**4. (a) O(n)**
The for loop runs n times and each iteration does constant work.
- (d) O(1): wrong because the loop count grows with n.
- (b) O(log n): wrong because i increments by 1, not by doubling.
- (c) O(n^2): wrong because there is only one loop.

Trace:
| n | iterations | count after |
|---:|---:|---:|
| 4 | 4 | 4 |
| 8 | 8 | 8 |

---

**5.** **[Medium]** *(B9 — halving counter)*
```text
i = n
while i > 1:
    i = i // 2
```
How many iterations does the while loop perform in Big-O terms?
(a) O(n)
(b) O(1)
(c) O(log n)
(d) O(n log n)

**5. (c) O(log n)**
Each iteration halves i, so the number of iterations is about log₂ n.
- (b) O(1): wrong because i changes and the loop can run many times.
- (a) O(n): wrong because halving skips most values.
- (d) O(n log n): wrong because there is no outer O(n) loop.

Trace:
| n | i values | iterations |
|---:|---|---:|
| 16 | 16, 8, 4, 2, 1 | 4 |
| 8 | 8, 4, 2, 1 | 3 |

---

**6.** **[Medium]** *(B9 — doubling counter)*
```text
i = 1
while i < n:
    i = i * 2
```
What is the time complexity?
(a) O(n)
(b) O(log n)
(c) O(n log n)
(d) O(sqrt n)

**6. (b) O(log n)**
i doubles each iteration, so it reaches n in about log₂ n steps.
- (a) O(n): wrong because doubling is faster than incrementing by 1.
- (c) O(n log n): wrong because there is no extra linear loop.
- (d) O(sqrt n): wrong because doubling, not squaring, controls the loop.

Trace:
| n | i values before exit | iterations |
|---:|---|---:|
| 16 | 1, 2, 4, 8, 16 | 4 |
| 8 | 1, 2, 4, 8 | 3 |

---

**7.** **[Medium]** *(B9 — triangular loop)*
```text
for i = 1 to n:
    for j = 1 to i:
        x = x + 1
```
What is the total time complexity?
(a) O(n)
(b) O(n log n)
(c) O(n^3)
(d) O(n^2)

**7. (d) O(n^2)**
Inner loop runs i times for each i, so total work is 1 + 2 + … + n = n(n+1)/2 = O(n^2).
- (a) O(n): wrong because the inner loop grows with i.
- (b) O(n log n): wrong because the inner loop is linear in i.
- (c) O(n^3): wrong because there are only two nested loops.

Trace:
| n | inner iterations by i | total |
|---:|---|---:|
| 4 | 1 + 2 + 3 + 4 | 10 |
| 5 | 1 + 2 + 3 + 4 + 5 | 15 |

---

**8.** **[Medium]** *(B9 — sequential loops with different orders)*
```text
for i = 1 to n:
    a = a + i

for j = 1 to n:
    for k = 1 to n:
        b = b + j + k
```
What is the overall time complexity?
(a) O(n)
(b) O(n^2)
(c) O(n log n)
(d) O(n^3)

**8. (b) O(n^2)**
The first block is O(n); the second block is O(n^2). The larger term dominates, so the total is O(n^2).
- (a) O(n): wrong because the double nested loop is quadratic.
- (d) O(n^3): wrong because the second block has only two nested loops.
- (c) O(n log n): wrong because neither block has logarithmic behavior.

Trace:
| n | first block | second block | total |
|---:|---:|---:|---:|
| 4 | 4 | 16 | 20 |
| 5 | 5 | 25 | 30 |

---

**9.** **[Medium]** *(B9 — nested loop with changing start)*
```text
for i = 1 to n:
    for j = i to n:
        x = x + 1
```
How many times is x incremented?
(a) O(n^3)
(b) O(n)
(c) O(n log n)
(d) O(n^2)

**9. (d) O(n^2)**
For i = 1, inner runs n times; for i = 2, n−1 times; …; for i = n, 1 time. Total is n(n+1)/2 = O(n^2).
- (b) O(n): wrong because the inner loop contributes many iterations.
- (c) O(n log n): wrong because j increments by 1, not by doubling.
- (a) O(n^3): wrong because there are only two nested loops.

Trace:
| n | inner counts by i | total |
|---:|---|---:|
| 4 | 4 + 3 + 2 + 1 | 10 |
| 5 | 5 + 4 + 3 + 2 + 1 | 15 |

---

**10.** **[Medium]** *(B9 — recursion stack depth)*
```text
F(n) {
    if n <= 1:
        return 1
    return F(n - 1) + 1
}
```
What is the space complexity due to the recursion stack?
(a) O(1)
(b) O(log n)
(c) O(n)
(d) O(2^n)

**10. (c) O(n)**
The recursion calls F(n−1), then F(n−2), …, so the maximum stack depth is n.
- (a) O(1): wrong because recursive calls remain on the stack.
- (b) O(log n): wrong because n decreases by 1, not by halving.
- (d) O(2^n): wrong because each call makes only one recursive call.

Trace:
| n | stack depth |
|---:|---:|
| 4 | F(4), F(3), F(2), F(1) = 4 |
| 5 | F(5), F(4), F(3), F(2), F(1) = 5 |

---

**11.** **[Hard]** *(B9 — outer linear, inner logarithmic)*
```text
for i = 1 to n:
    j = 1
    while j < n:
        j = j * 2
```
What is the time complexity?
(a) O(n log n)
(b) O(log n)
(c) O(n)
(d) O(n^2)

**11. (a) O(n log n)**
The outer loop runs n times. For each i, the inner while doubles j until it reaches n, so it runs O(log n) times. Total is O(n log n).
- (c) O(n): wrong because the inner while adds a logarithmic factor per i.
- (b) O(log n): wrong because the outer loop is linear.
- (d) O(n^2): wrong because the inner loop is logarithmic, not linear.

Trace:
| n | outer iterations | inner j values | total |
|---:|---:|---|---:|
| 8 | 8 | 1, 2, 4 | 24 |
| 16 | 16 | 1, 2, 4, 8 | 64 |

---

**12.** **[Hard]** *(B9 — nested halving and logarithmic inner)*
```text
i = n
while i > 0:
    j = 1
    while j < i:
        j = j * 2
    i = i // 2
```
What is the time complexity?
(a) O(n)
(b) O(log n)
(c) O((log n)^2)
(d) O(n log n)

**12. (c) O((log n)^2)**
Outer i halves: n, n/2, n/4, …. For each i, the inner while doubles j up to i, taking O(log i). Summed over O(log n) outer levels, this is O((log n)^2).
- (a) O(n): wrong because i shrinks logarithmically.
- (b) O(log n): wrong because there is an inner logarithmic loop for each outer level.
- (d) O(n log n): wrong because there is no linear n-sized loop.

Trace:
| n | outer i values | inner iterations for each i | total |
|---:|---|---:|---:|
| 16 | 16, 8, 4, 2, 1 | 4 + 3 + 2 + 1 + 0 | 10 |
| 32 | 32, 16, 8, 4, 2, 1 | 5 + 4 + 3 + 2 + 1 + 0 | 15 |

---

**13.** **[Hard]** *(B9 — break inside nested loop)*
```text
for i = 1 to n:
    for j = 1 to n:
        if j == i:
            break
        x = x + 1
```
What is the total time complexity in the worst case?
(a) O(n)
(b) O(n^2)
(c) O(n log n)
(d) O(n^3)

**13. (b) O(n^2)**
For each i, the inner loop runs until j == i. That is about i iterations per outer iteration, so total is 1 + 2 + … + n = O(n^2).
- (a) O(n): wrong because the break does not make the inner loop constant-time for every i.
- (c) O(n log n): wrong because j increments by 1, not by doubling.
- (d) O(n^3): wrong because there are only two nested loops.

Trace:
| n | x increments by i | total |
|---:|---|---:|
| 4 | 0 + 1 + 2 + 3 | 6 |
| 5 | 0 + 1 + 2 + 3 + 4 | 10 |

---

**14.** **[Hard]** *(B9 — branching recursion time)*
```text
G(n) {
    if n <= 1:
        return 1
    return G(n - 1) + G(n - 1)
}
```
What is the time complexity of G(n)?
(a) O(n)
(b) O(n^2)
(c) O(2^n)
(d) O(n log n)

**14. (c) O(2^n)**
Each call makes two recursive calls of size n−1, producing a binary recursion tree of depth n. Total calls are about 2^n.
- (a) O(n): wrong because it ignores the second recursive call at each level.
- (b) O(n^2): wrong because this is not a two-nested-loop pattern.
- (d) O(n log n): wrong because n decreases by 1 and branching doubles the work.

Trace:
| n | calls T(n) = 2T(n−1) + 1 |
|---:|---:|
| 1 | 1 |
| 2 | 3 |
| 3 | 7 |
| 4 | 15 |

---

**15.** **[Hard]** *(B9 — outer linear, inner doubling from 1 to n)*
```text
for i = 1 to n:
    for j = 1; j < n; j = j * 2:
        x = x + 1
```
What is the time complexity?
(a) O(log n)
(b) O(n log n)
(c) O(n)
(d) O(n^2)

**15. (b) O(n log n)**
The outer loop runs n times. The inner loop doubles j from 1 until it reaches n, so it runs O(log n) times per outer iteration.
- (a) O(log n): wrong because it ignores the outer n loop.
- (c) O(n): wrong because it ignores the inner logarithmic loop.
- (d) O(n^2): wrong because j doubles, so the inner loop does not run n times.

Trace:
| n | outer iterations | inner j values | total |
|---:|---:|---|---:|
| 8 | 8 | 1, 2, 4 | 24 |
| 16 | 16 | 1, 2, 4, 8 | 64 |

---

**16.** **[Hard]** *(B9 — geometric inner bound)*
```text
for i = 1; i <= n; i = i * 2:
    for j = 1; j <= i; j = j + 1:
        x = x + 1
```
What is the time complexity?
(a) O(log n)
(b) O(n)
(c) O(n^2)
(d) O(n log n)

**16. (b) O(n)**
i takes values 1, 2, 4, 8, …, up to n. The inner loop runs i times, so total work is 1 + 2 + 4 + … ≤ 2n, which is O(n).
- (a) O(log n): wrong because it counts only the outer loop.
- (d) O(n log n): wrong because the inner loop is not n for every i.
- (c) O(n^2): wrong because the sum of powers of 2 up to n is linear, not quadratic.

Trace:
| n | i values | inner iterations | total |
|---:|---|---:|---:|
| 8 | 1, 2, 4, 8 | 1 + 2 + 4 + 8 | 15 |
| 16 | 1, 2, 4, 8, 16 | 1 + 2 + 4 + 8 + 16 | 31 |

---

**17.** **[Hard]** *(B9 — recursion space for factorial)*
```text
fact(n) {
    if n == 0:
        return 1
    return n * fact(n - 1)
}
```
What is the space complexity of this recursive function, including the recursion stack?
(a) O(n)
(b) O(1)
(c) O(log n)
(d) O(n^2)

**17. (a) O(n)**
The recursive calls are fact(n), fact(n−1), …, fact(0). The maximum stack depth is about n + 1, so space is O(n).
- (b) O(1): wrong because recursive stack frames are not constant in number.
- (c) O(log n): wrong because n decreases by 1, not by halving.
- (d) O(n^2): wrong because the stack depth is linear, not quadratic.

Trace:
| n | stack frames |
|---:|---:|
| 4 | fact(4), fact(3), fact(2), fact(1), fact(0) = 5 |
| 5 | fact(5), fact(4), fact(3), fact(2), fact(1), fact(0) = 6 |

---

**18.** **[Hard]** *(B9 — recursion stack vs call tree)*
```text
A(n) {
    if n == 0:
        return 1
    return A(n - 1) + A(n - 1)
}
```
What is the space complexity of A(n) including the recursion stack?
(a) O(n)
(b) O(1)
(c) O(2^n)
(d) O(log n)

---

---

**18. (a) O(n)**
The time complexity is exponential, but the space complexity is determined by the maximum recursion depth, which is n + 1. So space is O(n).
- (b) O(1): wrong because recursion stack frames are stored.
- (c) O(2^n): wrong because this confuses the number of calls with the maximum stack depth.
- (d) O(log n): wrong because n decreases by 1, not by halving.

Trace:
| n | maximum simultaneous stack frames |
|---:|---:|
| 4 | A(4), A(3), A(2), A(1), A(0) = 5 |
| 5 | A(5), A(4), A(3), A(2), A(1), A(0) = 6 |

---
