---
title: Recursion — Trace, Base Case, Accumulation
code: P2
section: Pseudocode
weightage_pct: 1.1% of marks
est_questions: 0.43
tier: 4
difficulty: Easy
est_study_hours: 1.0
confidence: Medium
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-library/topics/T31-B6-recursion.md
---

# P2 — Recursion — Trace, Base Case, Accumulation

*Adapted from `accenture-prep-final/accenture-prep-library/topics/T31-B6-recursion.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.4 questions and 0.9 marks** on this topic (about 1.1% of the 75 scored marks). It sits in **Pseudocode**: 5 questions, 10 marks, 10 minutes. **Tier 4**, 1.0 hours to reach reliable recall, confidence **Medium**.

**3 questions on this topic are in the observed Infosys pool** (P07, P10, P11), from 1 source. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.69 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| P07 | 2024-12-18 | Standard recursive factorial; output for n = 5? |
| P10 | 2024-12-18 | function calc(a, b): if b == 0 return 1 else return a * calc(a, b - 1). Output of calc(6, 3)? |
| P11 | 2024-12-18 | function f(x, y): if y == 0 return x else return f(x + y, y - 1). Output of f(7, 2)? |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



1. **"What does this recursive function compute?"** Confirmed local item. You identify the accumulation, not trace it.

**Q1. Correct: (b) 10**

Variable trace table:

| Call | Computation | Value |
|---|---:|---:|
| F(0) | base | 0 |
| F(1) | 1 + F(0) | 1 |
| F(2) | 2 + F(1) | 3 |
| F(3) | 3 + F(2) | 6 |
| F(4) | 4 + F(3) | 10 |

- (a) 24: uses `n * F(n - 1)` and computes factorial.
- (c) 4: returns only the top-level `n`, ignoring recursive additions.
- (d) 0: returns the base-case value without adding `1+2+3+4`.

---

2. **The plus-versus-times trap.** `n + f(n-1)` is a sum; `n * f(n-1)` is a factorial.

**Q2. Correct: (a)**

Check table for the correct edit:

| Check | F(0) | F(1) | F(2) |
|---|---:|---:|---:|
| Correct: base `1`, multiply | 1 | 1 * 1 = 1 | 2 * 1 = 2 |
| Only multiply | 0 | 1 * 0 = 0 | 2 * 0 = 0 |
| Only base `1` | 1 | 1 + 1 = 2 | 2 + 2 = 4 |

- (b) With `F(0)=0`, multiplying gives `F(1)=0`, so it is not `1!`.
- (c) Changing only the base leaves the `+` accumulation, so it is not factorial.
- (d) `(n - 1) * F(n)` calls `F(n)` with the same `n`, so it does not progress to a base case.

---

3. **Call-stack tracing.** What is returned at each level for a small input.

**Q3. Correct: (d) 4**

Variable trace table:

| Call | n | Return expression | Value |
|---|---:|---|---:|
| F(0) | 0 | base | 0 |
| F(1) | 1 | 1 + F(0) | 1 |
| F(2) | 2 | 2 + F(1) | 3 |
| F(3) | 3 | 3 + F(2) | 6 |

Calls made: `F(3)`, `F(2)`, `F(1)`, `F(0)` = 4.

- (a) 3: counts only non-base calls or omits the initial call.
- (b) 5: counts an extra call, such as `F(-1)` or treats `PRINT` as a call.
- (c) 6: counts more than the actual recursive calls, often by counting statements.

---

4. **Base-case reasoning.** What happens when it is missing, or which input terminates immediately.

**Q4. Correct: (c) 9**

Variable trace table:

| Call | Computation | Value |
|---|---:|---:|
| F(-1) | base | 0 |
| F(1) | 1 + F(-1) | 1 |
| F(3) | 3 + F(1) | 4 |
| F(5) | 5 + F(3) | 9 |

- (b) 15: sums all integers `1..5` instead of stepping by 2.
- (d) 8: computes `5 + 3` and drops the final `+1`.
- (a) 5: returns only the first `n`.

---

5. **Call counting.** How many calls a naive fibonacci makes for a small n.

## 3. Concept notes

### What recursion is
A function that calls itself. Each call must work on a smaller/simpler input until a stopping condition is reached.

### Two mandatory parts

| Part | Role | If missing |
|---|---|---|
| Base case | Returns a value without calling itself; stops recursion | Infinite recursion → stack overflow |
| Recursive case | Calls the function on a smaller/simpler input | Function never progresses toward a result |

### Call stack: factorial(4)

```
FACTORIAL(4) CALL STACK

WINDING (push)                          UNWINDING (pop)
----------                              ----------

factorial(4) needs 3                    factorial(0) returns 1
+----------------+                      +----------------+  value = 1
| factorial(4)   |                      | factorial(0)   |
+----------------+                      +----------------+

factorial(3) needs 2                    factorial(1) = 1 * 1 = 1
+----------------+                      +----------------+  value = 1
| factorial(3)   |                      | factorial(1)   |
+----------------+                      +----------------+
| factorial(4)   |
+----------------+

factorial(2) needs 1                    factorial(2) = 2 * 1 = 2
+----------------+                      +----------------+  value = 2
| factorial(2)   |                      | factorial(2)   |
+----------------+                      +----------------+
| factorial(3)   |
+----------------+
| factorial(4)   |
+----------------+

factorial(1) needs 0                    factorial(3) = 3 * 2 = 6
+----------------+                      +----------------+  value = 6
| factorial(1)   |                      | factorial(3)   |
+----------------+                      +----------------+
| factorial(2)   |
+----------------+
| factorial(3)   |
+----------------+
| factorial(4)   |
+----------------+

factorial(0) base case                  factorial(4) = 4 * 6 = 24
+----------------+                      +----------------+  value = 24
| factorial(0)   |                      | factorial(4)   |
+----------------+                      +----------------+
| factorial(1)   |
+----------------+
| factorial(2)   |
+----------------+
| factorial(3)   |
+----------------+
| factorial(4)   |
+----------------+
```

| Stack level | Computation | Returned value |
|---|---|---|
| factorial(0) | base case | 1 |
| factorial(1) | 1 * factorial(0) = 1 * 1 | 1 |
| factorial(2) | 2 * factorial(1) = 2 * 1 | 2 |
| factorial(3) | 3 * factorial(2) = 3 * 2 | 6 |
| factorial(4) | 4 * factorial(3) = 4 * 6 | 24 |

### Winding and unwinding phases
- **Winding (down):** each call pushes a stack frame and reduces the input. Statements **before** the recursive call run here.
- **Unwinding (up):** frames pop and return values combine. Statements **after** the recursive call run here.

```pseudocode
function f(n):
    if n == 0:
        return
    print "down", n      // BEFORE recursive call
    f(n-1)
    print "up", n        // AFTER recursive call

f(3)
```

Output:
```
down 3
down 2
down 1
up 1
up 2
up 3
```

| Call | Runs before f(n-1) | Runs after f(n-1) returns |
|---|---|---|
| f(3) | print down 3 | print up 3 |
| f(2) | print down 2 | print up 2 |
| f(1) | print down 1 | print up 1 |
| f(0) | base case, return | — |

Before-call prints descend `3,2,1`. After-call prints ascend `1,2,3`.

### Direct vs indirect recursion

| Type | Definition | Example |
|---|---|---|
| Direct | Function calls itself directly | `factorial(n)` calls `factorial(n-1)` |
| Indirect (mutual) | A calls B; B calls A | `isEven(n)` calls `isOdd(n-1)`; `isOdd(n)` calls `isEven(n-1)` |

### Tail recursion
A recursive call is the last operation in the function; no work is pending after it returns. Some compilers/interpreters reuse the current stack frame instead of pushing a new one (tail-call optimisation), making stack space O(1) instead of O(n).

Non-tail factorial:
```pseudocode
factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)   // multiplication pending AFTER call
```

Tail factorial:
```pseudocode
factorial(n, acc):
    if n == 0: return acc
    return factorial(n-1, acc*n)  // call is last operation
```

### Worked traces

##

## 1. factorial(5) = 120

```pseudocode
factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)
```

| Step | Call | Expands to | Value returned |
|---|---|---|---|
| 1 | factorial(5) | 5 * factorial(4) | 5 * 24 = 120 |
| 2 | factorial(4) | 4 * factorial(3) | 4 * 6 = 24 |
| 3 | factorial(3) | 3 * factorial(2) | 3 * 2 = 6 |
| 4 | factorial(2) | 2 * factorial(1) | 2 * 1 = 2 |
| 5 | factorial(1) | 1 * factorial(0) | 1 * 1 = 1 |
| 6 | factorial(0) | base case | 1 |

Final answer: **120**.

##

## 2. fibonacci(5) = 5, call tree and call count

```pseudocode
fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)
```

Call tree:
```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) = 1
│   │   │   └── fib(0) = 0
│   │   └── fib(1) = 1
│   └── fib(2)
│       ├── fib(1) = 1
│       └── fib(0) = 0
└── fib(3)
    ├── fib(2)
    │   ├── fib(1) = 1
    │   └── fib(0) = 0
    └── fib(1) = 1
```

| n | Number of calls C(n) |
|---|---|
| 0 | 1 |
| 1 | 1 |
| 2 | 1 + C(1) + C(0) = 3 |
| 3 | 1 + 3 + 1 = 5 |
| 4 | 1 + 5 + 3 = 9 |
| 5 | 1 + 9 + 5 = 15 |

Total calls including top-level fib(5): **15**.  
Final answer: fib(5) = **5**.

##

## 3. Sum of first n natural numbers: n + f(n-1), n = 5 → 15

```pseudocode
sum(n):
    if n == 0: return 0
    return n + sum(n-1)
```

| Step | Call | Expands to | Value returned |
|---|---|---|---|
| 1 | sum(5) | 5 + sum(4) | 5 + 10 = 15 |
| 2 | sum(4) | 4 + sum(3) | 4 + 6 = 10 |
| 3 | sum(3) | 3 + sum(2) | 3 + 3 = 6 |
| 4 | sum(2) | 2 + sum(1) | 2 + 1 = 3 |
| 5 | sum(1) | 1 + sum(0) | 1 + 0 = 1 |
| 6 | sum(0) | base case | 0 |

Final answer: **15**.

##

## 4. Reverse a string

```pseudocode
reverse(s):
    if length(s) <= 1: return s
    return reverse(s[1..end]) + s[0]
```

Trace for `"CAT"`:

| Step | Call | Expands to | Value returned |
|---|---|---|---|
| 1 | reverse("CAT") | reverse("AT") + "C" | "TA" + "C" = "TAC" |
| 2 | reverse("AT") | reverse("T") + "A" | "T" + "A" = "TA" |
| 3 | reverse("T") | base case | "T" |

Final answer: **"TAC"**.

##

## 5. power(2,5) = 32

```pseudocode
power(x, n):
    if n == 0: return 1
    return x * power(x, n-1)
```

| Step | Call | Expands to | Value returned |
|---|---|---|---|
| 1 | power(2,5) | 2 * power(2,4) | 2 * 16 = 32 |
| 2 | power(2,4) | 2 * power(2,3) | 2 * 8 = 16 |
| 3 | power(2,3) | 2 * power(2,2) | 2 * 4 = 8 |
| 4 | power(2,2) | 2 * power(2,1) | 2 * 2 = 4 |
| 5 | power(2,1) | 2 * power(2,0) | 2 * 1 = 2 |
| 6 | power(2,0) | base case | 1 |

Final answer: **32**.

##

## 6. GCD via Euclid: gcd(48,18) = 6

```pseudocode
gcd(a, b):
    if b == 0: return a
    return gcd(b, a mod b)
```

| Step | Call | a mod b | Next call | Return |
|---|---|---|---|---|
| 1 | gcd(48,18) | 48 mod 18 = 12 | gcd(18,12) | 6 |
| 2 | gcd(18,12) | 18 mod 12 = 6 | gcd(12,6) | 6 |
| 3 | gcd(12,6) | 12 mod 6 = 0 | gcd(6,0) | 6 |
| 4 | gcd(6,0) | base case b == 0 | — | 6 |

Final answer: **6**.

### Recursion with + vs *: the sum-vs-factorial trap

`number + func(number-1)` computes a **SUM**, not a factorial. The operator is plus.

| Pattern | Base case | What it computes | n = 5 |
|---|---|---|---|
| `n + f(n-1)` | `f(0)=0` | Sum 1+2+...+n | 15 |
| `n * f(n-1)` | `f(0)=1` | Factorial n! | 120 |

`f(5)` with plus: 5+4+3+2+1+0 = **15**, not 120.  
`f(5)` with multiply: 5×4×3×2×1 = **120**.

### Recursion vs iteration

| Aspect | Recursion | Iteration |
|---|---|---|
| Memory | Uses call stack; O(n) frames for depth n | Usually O(1) extra memory |
| Speed | Function-call overhead; often slower | Generally faster |
| Readability | Clean for trees, divide & conquer | Clean for simple repetition |
| Stack risk | Stack overflow for deep recursion | No stack overflow from loop depth |
| Termination | Explicit base case | Loop condition |
| Examples | factorial, fib, tree traversal | factorial, fib, array loops |

### Time complexity of naive fibonacci and memoisation
Naive `fib(n)` recomputes the same subproblems. Number of calls grows exponentially: **O(2^n)**. For fib(5) it is 15 calls; for fib(30) it is millions.

Memoisation stores each `fib(k)` the first time it is computed. Later calls read the stored value. Each k from 0 to n is computed once.

| Version | Time | Space |
|---|---|---|
| Naive recursion | O(2^n) | O(n) stack |
| Memoised recursion | O(n) | O(n) table + O(n) stack |
| Iterative | O(n) | O(1) |

### Exam shortcut without tracing every level

| Question asks | Shortcut |
|---|---|
| Factorial n! | Multiply n down to 1; 5! = 120 |
| Sum 1..n with `n + f(n-1)` | n(n+1)/2; n=5 → 15 |
| Power x^n | Multiply x n times; 2^5 = 32 |
| Fibonacci n | Use fib table: 0,1,1,2,3,5,8,13,21 |
| Number of fib calls | C(n)=1+C(n-1)+C(n-2); C(0)=C(1)=1 |
| Print order | Before recursive call → descending; after → ascending |
| GCD | Apply a mod b until b = 0; last non-zero remainder is answer |
| String reverse | Last character moves to front, recurse on rest |
| + vs * | Plus → sum; star → product/factorial |

## 4. Must-memorise block

| Item | Recall |
|---|---|
| Two mandatory parts | Base case (stops recursion) + recursive case (calls itself on smaller input) |
| Missing base case | Infinite recursion → stack overflow |
| Call-stack order rule | Work BEFORE recursive call runs on the way down (winding); work AFTER recursive call runs on the way up (unwinding) |
| Direct recursion | A calls A |
| Indirect recursion | A calls B, B calls A |
| Tail recursion | Recursive call is last operation → can reuse stack frame → O(1) stack |
| Naive fib time | O(2^n) |
| Memoised fib time | O(n) |
| fib(5) call count | 15 calls |

**Factorials**

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| n! | 1 | 1 | 2 | 6 | 24 | 120 | 720 |

**Fibonacci** (F(0)=0, F(1)=1)

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| fib(n) | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 |

**Sum-vs-product trap**

| Pattern | Base case | Computes | n = 5 |
|---|---|---|---|
| `n + f(n-1)` | `f(0)=0` | Sum 1+2+...+n | 15 |
| `n * f(n-1)` | `f(0)=1` | Factorial n! | 120 |

**Call-stack order rule**

| Phase | Direction | What runs | Example output |
|---|---|---|---|
| Winding | Down | Statements before recursive call | 5,4,3,2,1 |
| Unwinding | Up | Statements after recursive call | 1,2,3,4,5 |

**Recursion vs iteration**

| | Recursion | Iteration |
|---|---|---|
| Memory | O(n) stack | O(1) extra |
| Speed | Slower (call overhead) | Faster |
| Risk | Stack overflow | No stack overflow |
| Use | Trees, divide & conquer | Simple loops |

## 5. Worked examples

### Example 1 — `number + func(number - 1)` computes a sum

```text
1  FUNCTION f(n)
2    IF n == 1 THEN
3      RETURN 1
4    ELSE
5      RETURN n + f(n - 1)
6    END IF
7  END FUNCTION
8  PRINT f(4)
```

| Step | Line | n | Computation / Return | Call stack (top last) |
|---:|---:|---:|---|---|
| 1 | 2 | 4 | `4 == 1` false | `f(4)` |
| 2 | 5 (call) | 4 | call `f(3)`; pending `4 + f(3)` | `f(4) → f(3)` |
| 3 | 2 | 3 | `3 == 1` false | `f(4) → f(3)` |
| 4 | 5 (call) | 3 | call `f(2)`; pending `3 + f(2)` | `f(4) → f(3) → f(2)` |
| 5 | 2 | 2 | `2 == 1` false | `f(4) → f(3) → f(2)` |
| 6 | 5 (call) | 2 | call `f(1)`; pending `2 + f(1)` | `f(4) → f(3) → f(2) → f(1)` |
| 7 | 2 | 1 | `1 == 1` true | `f(4) → f(3) → f(2) → f(1)` |
| 8 | 3 (return) | 1 | return `1` | `f(4) → f(3) → f(2) → f(1)` |
| 9 | 5 (return) | 2 | return `2 + 1 = 3` | `f(4) → f(3) → f(2)` |
| 10 | 5 (return) | 3 | return `3 + 3 = 6` | `f(4) → f(3)` |
| 11 | 5 (return) | 4 | return `4 + 6 = 10` | `f(4)` |
| 12 | 8 | — | print `10` | — |

**Answer: `f(4) = 10`. The `+` computes the sum `4 + 3 + 2 + 1 = 10`; if line 5 used `*`, it would be `4 * 3 * 2 * 1 = 24`.**

### Example 2 — same shape, but `*` computes factorial

```text
1  FUNCTION fact(n)
2    IF n <= 1 THEN
3      RETURN 1
4    ELSE
5      RETURN n * fact(n - 1)
6    END IF
7  END FUNCTION
8  PRINT fact(4)
```

| Step | Line | n | Computation / Return | Call stack (top last) |
|---:|---:|---:|---|---|
| 1 | 2 | 4 | `4 <= 1` false | `fact(4)` |
| 2 | 5 (call) | 4 | call `fact(3)`; pending `4 * fact(3)` | `fact(4) → fact(3)` |
| 3 | 2 | 3 | `3 <= 1` false | `fact(4) → fact(3)` |
| 4 | 5 (call) | 3 | call `fact(2)`; pending `3 * fact(2)` | `fact(4) → fact(3) → fact(2)` |
| 5 | 2 | 2 | `2 <= 1` false | `fact(4) → fact(3) → fact(2)` |
| 6 | 5 (call) | 2 | call `fact(1)`; pending `2 * fact(1)` | `fact(4) → fact(3) → fact(2) → fact(1)` |
| 7 | 2 | 1 | `1 <= 1` true | `fact(4) → fact(3) → fact(2) → fact(1)` |
| 8 | 3 (return) | 1 | return `1` | `fact(4) → fact(3) → fact(2) → fact(1)` |
| 9 | 5 (return) | 2 | return `2 * 1 = 2` | `fact(4) → fact(3) → fact(2)` |
| 10 | 5 (return) | 3 | return `3 * 2 = 6` | `fact(4) → fact(3)` |
| 11 | 5 (return) | 4 | return `4 * 6 = 24` | `fact(4)` |
| 12 | 8 | — | print `24` | — |

**Answer: `fact(4) = 24`. The `*` computes `4 * 3 * 2 * 1 = 24`.**

### Example 3 — counting calls, not summing values

```text
1  FUNCTION countCalls(n)
2    IF n == 0 THEN
3      RETURN 1
4    ELSE
5      RETURN 1 + countCalls(n - 1)
6    END IF
7  END FUNCTION
8  PRINT countCalls(4)
```

| Step | Line | n | Computation / Return | Call stack (top last) |
|---:|---:|---:|---|---|
| 1 | 2 | 4 | `4 == 0` false | `countCalls(4)` |
| 2 | 5 (call) | 4 | call `countCalls(3)`; pending `1 + countCalls(3)` | `countCalls(4) → countCalls(3)` |
| 3 | 2 | 3 | `3 == 0` false | `countCalls(4) → countCalls(3)` |
| 4 | 5 (call) | 3 | call `countCalls(2)`; pending `1 + countCalls(2)` | `countCalls(4) → countCalls(3) → countCalls(2)` |
| 5 | 2 | 2 | `2 == 0` false | `countCalls(4) → countCalls(3) → countCalls(2)` |
| 6 | 5 (call) | 2 | call `countCalls(1)`; pending `1 + countCalls(1)` | `countCalls(4) → countCalls(3) → countCalls(2) → countCalls(1)` |
| 7 | 2 | 1 | `1 == 0` false | `countCalls(4) → countCalls(3) → countCalls(2) → countCalls(1)` |
| 8 | 5 (call) | 1 | call `countCalls(0)`; pending `1 + countCalls(0)` | `countCalls(4) → countCalls(3) → countCalls(2) → countCalls(1) → countCalls(0)` |
| 9 | 2 | 0 | `0 == 0` true | `countCalls(4) → countCalls(3) → countCalls(2) → countCalls(1) → countCalls(0)` |
| 10 | 3 (return) | 0 | return `1` | `countCalls(4) → countCalls(3) → countCalls(2) → countCalls(1) → countCalls(0)` |
| 11 | 5 (return) | 1 | return `1 + 1 = 2` | `countCalls(4) → countCalls(3) → countCalls(2) → countCalls(1)` |
| 12 | 5 (return) | 2 | return `1 + 2 = 3` | `countCalls(4) → countCalls(3) → countCalls(2)` |
| 13 | 5 (return) | 3 | return `1 + 3 = 4` | `countCalls(4) → countCalls(3)` |
| 14 | 5 (return) | 4 | return `1 + 4 = 5` | `countCalls(4)` |
| 15 | 8 | — | print `5` | — |

**Answer: `countCalls(4) = 5`. It counts 5 calls total including the initial call and the base call `countCalls(0)`; non-base recursive calls are 4.**

### Example 4 — two recursive calls: Fibonacci-style trace

```text
1  FUNCTION fib(n)
2    IF n <= 1 THEN
3      RETURN n
4    ELSE
5      RETURN fib(n - 1) + fib(n - 2)
6    END IF
7  END FUNCTION
8  PRINT fib(4)
```

| Step | Call | Line | n | Computation / Return | Call stack (top last) |
|---:|---|---:|---:|---|---|
| 1 | A | 2 | 4 | `4 <= 1` false | `fib(4)` |
| 2 | A | 5 (call) | 4 | call `fib(3)`; pending `fib(3) + fib(2)` | `fib(4) → fib(3)` |
| 3 | B | 2 | 3 | `3 <= 1` false | `fib(4) → fib(3)` |
| 4 | B | 5 (call) | 3 | call `fib(2)`; pending `fib(2) + fib(1)` | `fib(4) → fib(3) → fib(2)` |
| 5 | C | 2 | 2 | `2 <= 1` false | `fib(4) → fib(3) → fib(2)` |
| 6 | C | 5 (call) | 2 | call `fib(1)`; pending `fib(1) + fib(0)` | `fib(4) → fib(3) → fib(2) → fib(1)` |
| 7 | D | 2 | 1 | `1 <= 1` true | `fib(4) → fib(3) → fib(2) → fib(1)` |
| 8 | D | 3 (return) | 1 | return `1` | `fib(4) → fib(3) → fib(2)` |
| 9 | C | 5 (call) | 2 | call `fib(0)`; pending `1 + fib(0)` | `fib(4) → fib(3) → fib(2) → fib(0)` |
| 10 | E | 2 | 0 | `0 <= 1` true | `fib(4) → fib(3) → fib(2) → fib(0)` |
| 11 | E | 3 (return) | 0 | return `0` | `fib(4) → fib(3) → fib(2)` |
| 12 | C | 5 (return) | 2 | return `1 + 0 = 1` | `fib(4) → fib(3)` |
| 13 | B | 5 (call) | 3 | call `fib(1)`; pending `1 + fib(1)` | `fib(4) → fib(3) → fib(1)` |
| 14 | F | 2 | 1 | `1 <= 1` true | `fib(4) → fib(3) → fib(1)` |
| 15 | F | 3 (return) | 1 | return `1` | `fib(4) → fib(3)` |
| 16 | B | 5 (return) | 3 | return `1 + 1 = 2` | `fib(4)` |
| 17 | A | 5 (call) | 4 | call `fib(2)`; pending `2 + fib(2)` | `fib(4) → fib(2)` |
| 18 | G | 2 | 2 | `2 <= 1` false | `fib(4) → fib(2)` |
| 19 | G | 5 (call) | 2 | call `fib(1)`; pending `fib(1) + fib(0)` | `fib(4) → fib(2) → fib(1)` |
| 20 | H | 2 | 1 | `1 <= 1` true | `fib(4) → fib(2) → fib(1)` |
| 21 | H | 3 (return) | 1 | return `1` | `fib(4) → fib(2)` |
| 22 | G | 5 (call) | 2 | call `fib(0)`; pending `1 + fib(0)` | `fib(4) → fib(2) → fib(0)` |
| 23 | I | 2 | 0 | `0 <= 1` true | `fib(4) → fib(2) → fib(0)` |
| 24 | I | 3 (return) | 0 | return `0` | `fib(4) → fib(2)` |
| 25 | G | 5 (return) | 2 | return `1 + 0 = 1` | `fib(4)` |
| 26 | A | 5 (return) | 4 | return `2 + 1 = 3` | — |
| 27 | — | 8 | — | print `3` | — |

**Answer: `fib(4) = 3`. Naive recursion makes 9 total calls; the returned value is `2 + 1 = 3`.**

### Example 5 — off-by-one base case

```text
1  FUNCTION s(n)
2    IF n == 1 THEN
3      RETURN 0
4    ELSE
5      RETURN n + s(n - 1)
6    END IF
7  END FUNCTION
8  PRINT s(4)
```

| Step | Line | n | Computation / Return | Call stack (top last) |
|---:|---:|---:|---|---|
| 1 | 2 | 4 | `4 == 1` false | `s(4)` |
| 2 | 5 (call) | 4 | call `s(3)`; pending `4 + s(3)` | `s(4) → s(3)` |
| 3 | 2 | 3 | `3 == 1` false | `s(4) → s(3)` |
| 4 | 5 (call) | 3 | call `s(2)`; pending `3 + s(2)` | `s(4) → s(3) → s(2)` |
| 5 | 2 | 2 | `2 == 1` false | `s(4) → s(3) → s(2)` |
| 6 | 5 (call) | 2 | call `s(1)`; pending `2 + s(1)` | `s(4) → s(3) → s(2) → s(1)` |
| 7 | 2 | 1 | `1 == 1` true | `s(4) → s(3) → s(2) → s(1)` |
| 8 | 3 (return) | 1 | return `0` | `s(4) → s(3) → s(2) → s(1)` |
| 9 | 5 (return) | 2 | return `2 + 0 = 2` | `s(4) → s(3) → s(2)` |
| 10 | 5 (return) | 3 | return `3 + 2 = 5` | `s(4) → s(3)` |
| 11 | 5 (return) | 4 | return `4 + 5 = 9` | `s(4)` |
| 12 | 8 | — | print `9` | — |

**Answer: `s(4) = 9`. The base `s(1) = 0` omits 1, so the sum is `4 + 3 + 2 + 0 = 9` instead of 10.**

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid |
|---|---|---|
| `+` in recursive call mistaken for factorial | `n * f(n-1)` is the familiar factorial shape; `n + f(n-1)` looks similar and candidates answer product | Read the operator literally. Test `n = 4`: plus gives `4 + 3 + 2 + 1 = 10`; times gives `4 * 3 * 2 * 1 = 24` |
| Base case `n == 0` vs `n == 1` | Off-by-one changes the sum or product by one term | Substitute the base into the smallest call. For sum `1..n`, use `n == 1 return 1`; for factorial, use `n <= 1 return 1` |
| Missing or unreachable base case | Recursion never stops or skips the base, causing infinite recursion or stack overflow | Check every recursive path reaches the base. For example, `n - 2` with base `n == 0` misses odd `n` |
| Counting calls vs computing values | `1 + f(n-1)` looks like a sum, but the `1` may count calls rather than add data | Identify what each literal represents. Separate the returned value from any side-effect counter |
| Wrong evaluation order in two-call recursion | `f(n-1) + f(n-2)` fully finishes the left branch before starting the right branch | Trace depth-first, left to right. Do not interleave the two recursive calls |
| Confusing total calls with recursion depth | `fib(4)` has depth 4 but 9 total function calls | Track stack depth separately from total invocations. Count every call, including repeated subproblems |
| Ignoring zero and negative inputs | Base `n <= 1` handles `0`; base `n == 1` does not, so `n = 0` can loop or fail | Test `n = 0` if the function allows it. Read the base condition exactly as written |
| Product with base returning `0` | A factorial-style recursion with `n == 0 return 0` collapses the whole product to `0` | Factorial base returns `1`. Sum base may return `0`; match the base to the operation |
| `PRINT` inside the recursive function vs final `PRINT` | Intermediate values may be printed on every call, so the visible output is not only the final return value | Separate side effects from return values. Identify what the final line actually prints |

## 7. Practice questions

1. **[Easy]** *(B6 — plus vs multiply)*  
What is printed?

```text
1  FUNCTION F(n)
2      IF n == 0 THEN
3          RETURN 0
4      END IF
5      RETURN n + F(n - 1)
6  END FUNCTION
7  PRINT F(4)
```

(a) 24
(b) 10
(c) 4
(d) 0

2. **[Easy]** *(B6 — base case edit)*  
Given the function below, which edit makes `F(n)` return `n!` for `n >= 0`?

```text
1  FUNCTION F(n)
2      IF n == 0 THEN
3          RETURN 0
4      END IF
5      RETURN n + F(n - 1)
6  END FUNCTION
```

(a) Change line 3 to `RETURN 1` and line 5 to `RETURN n * F(n - 1)`.
(b) Change only line 5 to `RETURN n * F(n - 1)`.
(c) Change only line 3 to `RETURN 1`.
(d) Change line 5 to `RETURN (n - 1) * F(n)`.

3. **[Easy]** *(B6 — counting calls)*  
How many total calls to `F` occur while evaluating `PRINT F(3)`, including the initial call?

```text
1  FUNCTION F(n)
2      IF n == 0 THEN
3          RETURN 0
4      END IF
5      RETURN n + F(n - 1)
6  END FUNCTION
7  PRINT F(3)
```

(a) 3
(b) 5
(c) 6
(d) 4

4. **[Medium]** *(B6 — step size)*  
What is printed?

```text
1  FUNCTION F(n)
2      IF n <= 0 THEN
3          RETURN 0
4      END IF
5      RETURN n + F(n - 2)
6  END FUNCTION
7  PRINT F(5)
```

(a) 5
(b) 15
(c) 9
(d) 8

5. **[Medium]** *(B6 — factorial trap)*  
What is printed?

```text
1  FUNCTION F(n)
2      IF n == 0 THEN
3          RETURN 1
4      END IF
5      RETURN n * F(n - 1)
6  END FUNCTION
7  PRINT F(5)
```

(a) 15
(b) 120
(c) 720
(d) 5

**Q5. Correct: (b) 120**

Variable trace table:

| Call | Computation | Value |
|---|---:|---:|
| F(0) | base | 1 |
| F(1) | 1 * F(0) | 1 |
| F(2) | 2 * F(1) | 2 |
| F(3) | 3 * F(2) | 6 |
| F(4) | 4 * F(3) | 24 |
| F(5) | 5 * F(4) | 120 |

- (a) 15: uses `+` instead of `*`, giving `1+2+3+4+5`.
- (c) 720: computes `6!` or multiplies one extra term.
- (d) 5: returns only `n` and ignores the recursive product.

---

6. **[Medium]** *(B6 — even sum)*  
What is printed?

```text
1  FUNCTION G(n)
2      IF n == 0 THEN
3          RETURN 0
4      END IF
5      RETURN n + G(n - 2)
6  END FUNCTION
7  PRINT G(6)
```

(a) 12
(b) 20
(c) 21
(d) 6

**Q6. Correct: (a) 12**

Variable trace table:

| Call | Computation | Value |
|---|---:|---:|
| G(0) | base | 0 |
| G(2) | 2 + G(0) | 2 |
| G(4) | 4 + G(2) | 6 |
| G(6) | 6 + G(4) | 12 |

- (b) 20: adds an extra even term, such as `8`, or uses a wrong upper bound.
- (c) 21: sums `1+2+3+4+5+6`.
- (d) 6: returns only the first `n`.

---

7. **[Medium]** *(B6 — two recursive calls)*  
What is printed?

```text
1  FUNCTION H(n)
2      IF n <= 1 THEN
3          RETURN 1
4      END IF
5      RETURN H(n - 1) + H(n - 2)
6  END FUNCTION
7  PRINT H(5)
```

(a) 8
(b) 13
(c) 5
(d) 16

**Q7. Correct: (a) 8**

Variable trace table:

| Call | Computation | Value |
|---|---:|---:|
| H(0) | base | 1 |
| H(1) | base | 1 |
| H(2) | H(1) + H(0) | 2 |
| H(3) | H(2) + H(1) | 3 |
| H(4) | H(3) + H(2) | 5 |
| H(5) | H(4) + H(3) | 8 |

- (c) 5: reports `H(4)` instead of `H(5)`.
- (b) 13: computes one extra Fibonacci step, such as `H(6)`.
- (d) 16: adds or doubles without correctly applying the base values.

---

8. **[Medium]** *(B6 — print order)*  
What is printed?

```text
1  FUNCTION P(n)
2      IF n == 0 THEN
3          RETURN 0
4      END IF
5      PRINT n
6      RETURN P(n - 1)
7  END FUNCTION
8  P(3)
```

(a) 3 2 1 0
(b) 1 2 3
(c) 0 1 2 3
(d) 3 2 1

**Q8. Correct: (d) 3 2 1**

Variable trace table:

| Call | Action | Output / Return |
|---|---|---|
| P(3) | n=3, `PRINT 3`, call P(2) | output 3 |
| P(2) | n=2, `PRINT 2`, call P(1) | output 2 |
| P(1) | n=1, `PRINT 1`, call P(0) | output 1 |
| P(0) | n=0, base | return 0 |

- (b) 1 2 3: prints after the recursive call instead of before it.
- (c) 0 1 2 3: prints at the base case too and reverses the order.
- (a) 3 2 1 0: prints `0` before checking the base case.

---

9. **[Hard]** *(B6 — precedence and recursion)*  
Assume multiplication is evaluated before addition. What is printed?

```text
1  FUNCTION F(n)
2      IF n == 0 THEN
3          RETURN 1
4      END IF
5      RETURN n + F(n - 1) * 2
6  END FUNCTION
7  PRINT F(3)
```

(a) 7
(b) 30
(c) 19
(d) 26

**Q9. Correct: (c) 19**

Variable trace table:

| Call | Computation | Value |
|---|---:|---:|
| F(0) | base | 1 |
| F(1) | 1 + F(0) * 2 = 1 + 2 | 3 |
| F(2) | 2 + F(1) * 2 = 2 + 6 | 8 |
| F(3) | 3 + F(2) * 2 = 3 + 16 | 19 |

- (b) 30: evaluates `(n + F(n - 1)) * 2` left-to-right.
- (a) 7: ignores `* 2` and uses a pure sum with base `1`.
- (d) 26: evaluates as `n * F(n - 1) + 2`.

---

10. **[Hard]** *(B6 — digit recursion)*  
`DIV` is integer division. What is printed?

```text
1  FUNCTION Q(n)
2      IF n == 0 THEN
3          RETURN 0
4      END IF
5      RETURN (n MOD 10) + Q(n DIV 10)
6  END FUNCTION
7  PRINT Q(1234)
```

(a) 1234
(b) 10
(c) 4
(d) 24

**Q10. Correct: (b) 10**

Variable trace table:

| Call | Computation | Value |
|---|---:|---:|
| Q(0) | base | 0 |
| Q(1) | 1 + Q(0) | 1 |
| Q(12) | 2 + Q(1) | 3 |
| Q(123) | 3 + Q(12) | 6 |
| Q(1234) | 4 + Q(123) | 10 |

- (a) 1234: ignores `MOD` and `DIV`, returning the original number.
- (c) 4: returns only the last digit.
- (d) 24: multiplies digits `1*2*3*4` instead of adding them.

---

11. **[Hard]** *(B6 — call counting in branching recursion)*  
How many total calls to `F` occur while evaluating `PRINT F(4)`, including the initial call?

```text
1  FUNCTION F(n)
2      IF n <= 1 THEN
3          RETURN n
4      END IF
5      RETURN F(n - 1) + F(n - 2)
6  END FUNCTION
7  PRINT F(4)
```

(a) 15
(b) 8
(c) 5
(d) 9

**Q11. Correct: (d) 9**

Variable trace table / call table:

| Order | Call | Invoked from | Recursive calls made |
|---:|---|---|---|
| 1 | F(4) | initial | F(3), F(2) |
| 2 | F(3) | F(4) | F(2), F(1) |
| 3 | F(2) | F(3) | F(1), F(0) |
| 4 | F(1) | F(2) | none, base |
| 5 | F(0) | F(2) | none, base |
| 6 | F(1) | F(3) | none, base |
| 7 | F(2) | F(4) | F(1), F(0) |
| 8 | F(1) | F(2) | none, base |
| 9 | F(0) | F(2) | none, base |

Total calls = 9.

- (b) 8: omits the initial call or misses one base call.
- (a) 15: counts extra branches or treats the recursion tree as larger than it is.
- (c) 5: counts distinct values `F(4)`, `F(3)`, `F(2)`, `F(1)`, `F(0)` instead of actual calls.

---

12. **[Medium]** *(B6 — call stack)*  
When tracing `F(n) = n + F(n - 1)` down to base case `F(0)`, in what order are the additions actually evaluated?

(a) During the forward call phase, as `n + (n-1) + ... + 0`.
(b) The stack discards pending additions when it reaches `F(0)`.
(c) After the base case, from `F(0)` upward to `F(n)`.
(d) Only the first addition `n + F(n-1)` is evaluated; the rest are skipped.

**Rule:** Trace recursion down to the base case, then evaluate upward. The return expression decides the operation: `n + F(n-1)` sums; `n * F(n-1)` multiplies/factorials. Counting calls is separate from computing the returned value.

**Q12. Correct: (c)**

- (a) Additions do not happen during the forward call phase; calls are still being pushed.
- (b) The first addition cannot complete without the recursive return value.
- (b) The stack keeps pending frames with their stored `n` values until the calls return.

---
## 8. Resources

| Resource | Type | Link | Free/Paid | Time | Why this one |
|---|---|---|---|---|---|
| PrepInsta — Accenture pseudocode | Practice set | https://prepinsta.com/accenture/pseudo-code/general-pseudo-code/ | Free | 40 min | Recursion output-prediction items |
| CodeChef — Accenture interview questions | Practice set | https://www.codechef.com/practice/accenture-interview-questions | Free | 40 min | Company-tagged practice |
| GfG — Complexity analysis guide | Article | https://www.geeksforgeeks.org/dsa/complete-guide-on-complexity-analysis/ | Free | 20 min | For the O(2ⁿ) naive-fibonacci result |
| `question-banks/QB-T31-B6-recursion.md` | Question bank | (this library) | Free | 30 min | 20 original questions |

*All external links verified resolving 2026-09-16.*

## 9. Self-check

- [ ] **I read the operator before deciding what a recursion computes — `+` is a sum, `*` is a factorial**
- [ ] I can name the two mandatory parts of any recursion
- [ ] I can say what happens when the base case is missing
- [ ] I can trace `factorial(5)` and `fibonacci(5)` by hand and get 120 and 5
- [ ] I know the factorials up to 6! and the fibonacci numbers up to F(8)
- [ ] I can explain why work before the recursive call happens on the way down and work after it on the way up
- [ ] I know naive fibonacci is O(2ⁿ) and that memoisation fixes it
- [ ] I can compare recursion and iteration on memory and stack risk
- [ ] I scored 9/12 or better on the practice questions

## 10. Sources

**Teaching content (§3–§9)** is adapted from `accenture-prep-final/accenture-prep-library/topics/T31-B6-recursion.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions P07, P10, P11 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `P2`). Confidence **Medium**. Nothing in this file is a published Infosys syllabus.
