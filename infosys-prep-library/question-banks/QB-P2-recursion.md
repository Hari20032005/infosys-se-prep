# QB-P2 — Recursion — Trace, Base Case, Accumulation

**Pseudocode** · **Tier 4** · 18 questions

Topic file: [`P2-recursion.md`](/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library/pseudocode/P2-recursion.md)

*Adapted from `accenture-prep-final/accenture-prep-library/question-banks/QB-T31-B6-recursion.md`; verified in that library's QA. Questions and answer key are unchanged.*

**How to use this bank.** Attempt every question before opening the key, at the real pace for this section (120 seconds a question). Answer letters are balanced across a–d.

---

**1.** **[Easy]** *(B1 — base case)*
A recursive function is written with no base case. What is the most likely result when it is called?

(a) It returns 0 automatically.
(b) It keeps calling itself until the call stack overflows.
(c) It terminates after a single pass.
(d) The compiler rewrites it as a loop.

**1. (b) It keeps calling itself until the call stack overflows.**
With no base case there is no terminating condition, so each call pushes a new frame until the stack limit is hit (Python raises `RecursionError`).

- (a) Nothing in a recursive function returns 0 automatically; the return value comes only from executed `return` statements.
- (c) There is no mechanism that stops after one pass; each call immediately calls itself again.
- (d) Python does not convert recursion into iteration; that is a feature of some compilers for other languages, not of the interpreter here.

---

**2.** **[Easy]** *(B2 — plus-versus-times trap)*
```python
def f(n):
    if n == 0:
        return 0
    return n + f(n - 1)
```
What does `f(4)` return?

(a) 24
(b) 10
(c) 4
(d) 0

**2. (b) 10**
The recursion adds `n` on the way back up, so the result is the sum 4 + 3 + 2 + 1 + 0 = 10.

| Call | Returns |
|---|---|
| f(0) | 0 |
| f(1) | 1 + 0 = 1 |
| f(2) | 2 + 1 = 3 |
| f(3) | 3 + 3 = 6 |
| f(4) | 4 + 6 = 10 |

- (a) 24 is the factorial 4!, produced by `n * f(n - 1)` instead of `n + f(n - 1)`. This is the plus-versus-times trap.
- (c) 4 is just the argument, as if only one term were added.
- (d) 0 is the base-case value only; it ignores all the additions performed while unwinding.

---

**3.** **[Easy]** *(B3 — call-stack trace)*
```python
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
```
What is the value of `fact(5)`?

(a) 15
(b) 24
(c) 120
(d) 720

**3. (c) 120**
`fact(5)` computes 5 × 4 × 3 × 2 × `fact(1)` = 5 × 4 × 3 × 2 × 1 = 120.

| Call | Returns |
|---|---|
| fact(1) | 1 |
| fact(2) | 2 × 1 = 2 |
| fact(3) | 3 × 2 = 6 |
| fact(4) | 4 × 6 = 24 |
| fact(5) | 5 × 24 = 120 |

- (a) 15 is 1 + 2 + 3 + 4 + 5, the sum, not the product.
- (b) 24 is `fact(4)`; the final multiplication by 5 is missed.
- (d) 720 is `fact(6)`, one level too deep.

---

**4.** **[Easy]** *(B4 — call counting)*
```python
def f(n):
    if n == 0:
        return
    f(n - 1)
```
Including the initial call `f(3)`, how many times is `f` called in total?

(a) 3
(b) 4
(c) 2
(d) 5

**4. (b) 4**
The calls are f(3), f(2), f(1), f(0); f(0) hits the base case and stops.

- (a) 3 counts only the non-base calls f(3), f(2), f(1).
- (c) 2 stops at f(2) and ignores the deeper frames.
- (d) 5 adds an extra call after the base case, which never happens.

---

**5.** **[Medium]** *(B5 — naive fibonacci)*
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```
Including the initial call, how many times is `fib` called in total while evaluating `fib(5)`?

(a) 15
(b) 9
(c) 12
(d) 25

**5. (a) 15**
Let C(n) be the number of calls for fib(n): C(0) = C(1) = 1, C(n) = 1 + C(n-1) + C(n-2). This gives C(2) = 3, C(3) = 5, C(4) = 9, C(5) = 15.

- (b) 9 is C(4), the count for fib(4), not fib(5).
- (c) 12 counts only part of the tree, typically forgetting the repeated fib(2) subtrees.
- (d) 25 is 5²; the call count grows like the fib numbers themselves (roughly 2·fib(n+1) − 1), not like n².

---

**6.** **[Medium]** *(B2 — accumulation trace)*
```python
def g(n):
    if n == 0:
        return 0
    return g(n - 1) + n * n
```
What is `g(4)`?

(a) 16
(b) 30
(c) 25
(d) 100

**6. (b) 30**
The recursion adds n² on the way back up: 1² + 2² + 3² + 4² = 1 + 4 + 9 + 16 = 30.

| f(0) | f(1) | f(2) | f(3) | f(4) |
|---|---|---|---|---|
| 0 | 0 + 1 = 1 | 1 + 4 = 5 | 5 + 9 = 14 | 14 + 16 = 30 |

- (a) 16 is only the last term n² for n = 4.
- (d) 100 is (1 + 2 + 3 + 4)² = 10², the square of the sum, not the sum of squares.
- (c) 25 is 5² and matches no partial sum here.

---

**7.** **[Medium]** *(B3 — call-stack trace)*
```python
def f(n):
    if n == 0:
        return 0
    return f(n // 10) + n % 10
```
What does `f(9876)` return?

(a) 9876
(b) 15
(c) 24
(d) 30

**7. (d) 30**
The function sums the decimal digits of n; 9 + 8 + 7 + 6 = 30.

| Call | Returns |
|---|---|
| f(0) | 0 |
| f(9) | 0 + 9 = 9 |
| f(98) | 9 + 8 = 17 |
| f(987) | 17 + 7 = 24 |
| f(9876) | 24 + 6 = 30 |

- (a) 9876 is the original argument returned unchanged.
- (c) 24 is `f(987)`; the last digit 6 is never added.
- (b) 15 is unrelated; it comes from summing the wrong digits.

---

**8.** **[Medium]** *(B3 — head versus tail recursion)*
```python
def f(n):
    if n == 0:
        return
    print(n, end=" ")
    f(n - 1)
    print(n, end=" ")
f(3)
```
What is printed?

(a) 1 2 3 3 2 1
(b) 3 2 1
(c) 3 2 1 1 2 3
(d) 1 2 3

**8. (c) 3 2 1 1 2 3**
The first print happens before the recursive call, so it descends 3, 2, 1; the second print happens after the call returns, so it ascends 1, 2, 3.

- (a) 1 2 3 3 2 1 is the reverse order; it would occur if the prints were swapped.
- (b) 3 2 1 stops after the descending prints and ignores the print after the recursive call.
- (d) 1 2 3 is only the ascending half of the output.

---

**9.** **[Medium]** *(B6 — recursion versus iteration)*
Which statement about recursion and iteration is TRUE?

(a) Every iterative loop can be replaced by a recursive function, and recursion always uses less memory than the loop.
(b) A recursive solution often uses more memory than an iterative one because every pending call keeps a stack frame alive.
(c) A recursive function cannot be written without at least two base cases.
(d) Recursion is always faster than iteration because the compiler optimises recursive calls.

**9. (b) A recursive solution often uses more memory than an iterative one because every pending call keeps a stack frame alive.**
Each unfinished call holds its own frame with parameters and locals, so recursion needs O(depth) extra space, while a simple loop needs O(1).

- (a) The first half is true (loops and recursion are equivalent in power), but recursion does not always use less memory — it usually uses more.
- (d) Recursion carries call overhead and is generally slower than the equivalent loop in Python.
- (c) One base case is enough for many functions (factorial, sum, and so on); two are not required.

---

**10.** **[Medium]** *(B1 — base case)*
```python
def f(n):
    if n == 1:
        return 1
    return n + f(n - 2)
```
What happens when `f(6)` is called?

(a) It recurses indefinitely and ends with a recursion/stack-overflow error.
(b) It returns 21.
(c) It returns 12.
(d) It returns 6.

**10. (a) It recurses indefinitely and ends with a recursion/stack-overflow error.**
`n` decreases by 2 each time, so from 6 the values are 6, 4, 2, 0, −2, −4, … and the value 1 required by the base case is never reached.

- (c) 12 is what you get if you wrongly assume `f(0)` returns 0 and stop there.
- (b) 21 is what you get if you wrongly assume `f(1)` is eventually reached and the series continues to 1.
- (d) 6 is just the input, ignoring the recursive additions.

---

**11.** **[Hard]** *(B2 — plus-versus-times trap)*
```python
def f(n):
    if n == 0:
        return 1
    return n + f(n - 1)
```
What is `f(4)`?

(a) 10
(b) 24
(c) 11
(d) 4

**11. (c) 11**
The base case returns 1, so the sum picks up an extra 1: 4 + 3 + 2 + 1 + 1 = 11.

| f(0) | f(1) | f(2) | f(3) | f(4) |
|---|---|---|---|---|
| 1 | 1 + 1 = 2 | 2 + 2 = 4 | 3 + 4 = 7 | 4 + 7 = 11 |

- (a) 10 assumes the base case returns 0, which is the usual sum 1..4.
- (b) 24 is 4!, produced by multiplication rather than addition.
- (d) 4 is just the argument.

---

**12.** **[Hard]** *(B5 — naive fibonacci)*
Using the naive fibonacci below, how many of the calls made while evaluating `fib(5)` are base-case calls (calls where `n <= 1`)?
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

(a) 8
(b) 7
(c) 5
(d) 15

**12. (a) 8**
The base-case calls are the leaves of the call tree. For fib(5) the leaves are fib(1) five times and fib(0) three times, giving 8 leaves out of 15 total calls.

- (c) 5 is the number of fib(1) calls only, ignoring fib(0) calls.
- (b) 7 is the number of internal (non-base) calls — 15 total minus 8 leaves.
- (d) 15 is the total number of calls, including all internal ones.

---

**13.** **[Hard]** *(B7 — accumulator parameter)*
```python
def f(n, acc):
    if n <= 1:
        return acc
    return f(n - 1, acc * n)
```
What does `f(4, 2)` return?

(a) 24
(b) 12
(c) 8
(d) 48

**13. (d) 48**
`acc` starts at 2 and is multiplied by each value of n from 4 down to 2: 2 × 4 × 3 × 2 = 48, then `f(1, 48)` returns `acc`.

| Call | n | acc |
|---|---|---|
| f(4, 2) | 4 | 2 |
| f(3, 8) | 3 | 2 × 4 = 8 |
| f(2, 24) | 2 | 8 × 3 = 24 |
| f(1, 48) | 1 | 24 × 2 = 48 → returns 48 |

- (a) 24 is the accumulator value at the call `f(2, 24)`; the multiplication by 2 still has to happen.
- (b) 12 is 4 × 3, stopping one step early.
- (c) 8 is the accumulator after the first multiplication only.

---

**14.** **[Hard]** *(B3 — call-stack trace)*
```python
def f(n):
    if n == 0:
        return 0
    return f(n // 2) + 1
```
What is `f(10)`?

(a) 3
(b) 5
(c) 10
(d) 4

**14. (d) 4**
The function counts how many times n must be halved (integer division) to reach 0: 10 → 5 → 2 → 1 → 0, which is 4 steps.

| f(0) | f(1) | f(2) | f(5) | f(10) |
|---|---|---|---|---|
| 0 | 0 + 1 = 1 | 1 + 1 = 2 | 2 + 1 = 3 | 3 + 1 = 4 |

- (a) 3 is the value of `f(5)`, one halving short.
- (b) 5 is 10 / 2, treating the result as a division rather than a count of steps.
- (c) 10 is the argument itself.

---

**15.** **[Hard]** *(B4 — call counting)*
```python
def f(n):
    if n == 0:
        return 1
    return f(n - 1) + f(n - 1)
```
Including the initial call, how many calls are made in total when `f(4)` is evaluated?

(a) 16
(b) 15
(c) 31
(d) 8

**15. (c) 31**
Each call spawns two more until n = 0, so the number of calls satisfies T(0) = 1, T(n) = 2·T(n−1) + 1. T(1) = 3, T(2) = 7, T(3) = 15, T(4) = 31.

- (a) 16 is 2⁴, the number of base-case calls at depth 4, not the total.
- (b) 15 is T(3), the count for `f(3)`.
- (d) 8 is the depth of the recursion, not the number of calls.

---

**16.** **[Hard]** *(B3 — call-stack trace)*
```python
def f(n):
    if n == 0:
        return 0
    return 2 * f(n - 1) + 1
```
What is `f(4)`?

(a) 15
(b) 31
(c) 16
(d) 8

**16. (a) 15**
Unwinding gives f(1) = 1, f(2) = 3, f(3) = 7, f(4) = 15; in general f(n) = 2ⁿ − 1.

| f(0) | f(1) | f(2) | f(3) | f(4) |
|---|---|---|---|---|
| 0 | 2×0 + 1 = 1 | 2×1 + 1 = 3 | 2×3 + 1 = 7 | 2×7 + 1 = 15 |

- (b) 31 is f(5), one level too deep.
- (c) 16 is 2⁴, the doubling alone ignoring the repeated `+ 1`.
- (d) 8 is the recursion depth.

---

**17.** **[Hard]** *(B1 — base case and branching)*
```python
def paths(r, c):
    if r == 0 or c == 0:
        return 1
    return paths(r - 1, c) + paths(r, c - 1)
```
What is `paths(2, 2)`?

(a) 2
(b) 4
(c) 8
(d) 6

**17. (d) 6**
Every path from (2,2) to an edge uses two "up" and two "left" moves in some order, giving C(4,2) = 6 paths; the recursion returns exactly that.

| Call | Value |
|---|---|
| paths(1,1) | paths(0,1) + paths(1,0) = 1 + 1 = 2 |
| paths(1,2) | paths(0,2) + paths(1,1) = 1 + 2 = 3 |
| paths(2,1) | paths(1,1) + paths(2,0) = 2 + 1 = 3 |
| paths(2,2) | paths(1,2) + paths(2,1) = 3 + 3 = 6 |

- (b) 4 is 2 × 2, the number of cells, not the number of paths.
- (c) 8 is 2³, which counts paths on a larger grid or double-counts routes.
- (a) 2 is the number of moves in one direction only.

---

**18.** **[Hard]** *(B2 — plus-versus-times trap)*
```python
def f(n):
    if n == 0:
        return 0
    return n * f(n - 1)
```
What is `f(5)`?

(a) 0
(b) 5
(c) 120
(d) 1

---

---

**18. (a) 0**
The base case returns 0, and everything is multiplied by that value on the way back up: 5 × 4 × 3 × 2 × 1 × 0 = 0. A product recursion needs a base case of 1, not 0.

- (c) 120 is 5!, the result you get only if the base case returns 1.
- (b) 5 is just the argument.
- (d) 1 is the value the base case should return, not the value this code produces.

---
