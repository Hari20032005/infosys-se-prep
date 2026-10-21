---
title: Reading Time and Space Complexity off a Snippet
code: P8
section: Pseudocode
weightage_pct: 0.7% of marks
est_questions: 0.25
tier: 4
difficulty: Medium
est_study_hours: 0.8
confidence: Low
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-library/topics/T32-B9-snippet-complexity.md
---

# P8 — Reading Time and Space Complexity off a Snippet

*Adapted from `accenture-prep-final/accenture-prep-library/topics/T32-B9-snippet-complexity.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.3 questions and 0.5 marks** on this topic (about 0.7% of the 75 scored marks). It sits in **Pseudocode**: 5 questions, 10 marks, 10 minutes. **Tier 4**, 0.8 hours to reach reliable recall, confidence **Low**.

**No Infosys question on this topic was recovered.** It rests on syllabus lists or first-hand naming only (C1), so its share is an allocation, not an observation.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.38 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

No question on this topic was recovered. Listed by: C1.

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



1. **Snippet → complexity.** A 4–8 line loop structure, and you name O(n), O(n²) or O(log n).

**1. Correct: (b) 15**  
Variable trace:

| i | sum after line 4 |
|---:|---:|
| 1 | 1 |
| 2 | 3 |
| 3 | 6 |
| 4 | 10 |
| 5 | 15 |

- **(a) 10**: Adds only 1+2+3+4, stopping one iteration early.
- **(c) 20**: Initializes `sum = 5` before the loop.
- **(d) 25**: Uses n² instead of summing 1 to n.

---

---

2. **Nested versus sequential.** Whether two loops multiply or add.

**2. Correct: (b) O(n)**  
Trace/growth:

| n | Loop iterations |
|---:|---:|
| 4 | 4 |
| 8 | 8 |
| 16 | 16 |

- **(a) O(1)**: Ignores the loop bound n.
- **(c) O(log n)**: Thinks `i` doubles or halves; here `i` increments by 1.
- **(d) O(n²)**: Assumes every FOR implies a nested loop.

---

---

3. **A counter that doubles or halves.** The O(log n) signature.

**3. Correct: (a) 7**  
Variable trace:

| Iteration | i at check | i < 100? | count after | i after |
|---:|---:|---|---:|---:|
| 1 | 1 | true | 1 | 2 |
| 2 | 2 | true | 2 | 4 |
| 3 | 4 | true | 3 | 8 |
| 4 | 8 | true | 4 | 16 |
| 5 | 16 | true | 5 | 32 |
| 6 | 32 | true | 6 | 64 |
| 7 | 64 | true | 7 | 128 |
| 8 | 128 | false | 7 | 128 |

- **(c) 6**: Uses floor(log₂ 100) only and omits one valid iteration.
- **(b) 8**: Counts the final failing check `i = 128` as an iteration.
- **(d) 50**: Assumes the loop runs n/2 times because n = 100.

---

---

4. **Space complexity.** Whether a snippet uses O(1) or O(n) auxiliary space, including recursion stack depth.

**4. Correct: (b) 12**  
Variable trace:

| i | j values | count after inner loop |
|---:|---|---:|
| 1 | 1, 2, 3 | 3 |
| 2 | 1, 2, 3 | 6 |
| 3 | 1, 2, 3 | 9 |
| 4 | 1, 2, 3 | 12 |

- **(a) 7**: Adds outer and inner counts: 4 + 3.
- **(c) 16**: Uses 4 × 4 and ignores the inner limit 3.
- **(d) 20**: Uses 4 × 5 or 5 × 4.

---

---

5. **Simplification.** What O(3n² + 5n + 7) reduces to.

## 3. Concept notes

### The counting rule

Time complexity is driven by the number of times the innermost statement runs as a function of `n`. Find the statement executed most often, count its executions, then drop constants and lower-order terms.

### Pattern-recognition table

| Snippet shape | Time complexity |
|---|---|
| Single statement | O(1) |
| Single loop to n | O(n) |
| Two sequential loops (each to n) | O(n) |
| Two nested loops, both to n | O(n^2) |
| Nested loop, inner bound = outer variable | O(n^2) |
| Loop with `i *= 2` or `i /= 2` | O(log n) |
| Loop with `i * i < n` | O(√n) |
| Nested loops, inner runs constant times | O(n) |
| Loop calling an O(n) operation inside | O(n^2) |
| Recursion halving, one call | O(log n) |
| Recursion halving, two calls | O(n) |
| Recursion decrementing by one, one call | O(n) |
| Recursion decrementing by one, two calls | O(2^n) |

### Detailed patterns with snippets

| Shape | Pseudocode snippet | Time | One-line justification |
|---|---|---|---|
| Single statement | `x = a + b` | O(1) | Executes once. |
| Single loop to n | `for i = 1 to n:`<br>`  x = x + 1` | O(n) | Body runs n times. |
| Two sequential loops | `for i = 1 to n:`<br>`  x = x + 1`<br>`for j = 1 to n:`<br>`  y = y + 1` | O(n) | n + n = 2n; drop constant. |
| Two nested loops, both to n | `for i = 1 to n:`<br>`  for j = 1 to n:`<br>`    x = x + 1` | O(n^2) | n × n. |
| Nested, inner bound = outer variable | `for i = 1 to n:`<br>`  for j = 1 to i:`<br>`    x = x + 1` | O(n^2) | Sum 1+2+...+n = n(n+1)/2 → O(n^2). |
| Loop with `i *= 2` or `i /= 2` | `i = 1`<br>`while i < n:`<br>`  i = i * 2` | O(log n) | i doubles each step; ~log₂n steps. |
| Loop with `i * i < n` | `i = 1`<br>`while i * i < n:`<br>`  i = i + 1` | O(√n) | Stops when i² ≥ n, so i ~ √n. |
| Nested loops, inner constant | `for i = 1 to n:`<br>`  for j = 1 to 5:`<br>`    x = x + 1` | O(n) | Outer n × inner 5 = 5n; drop constant. |
| Loop calling O(n) operation | `for i = 1 to n:`<br>`  sum_array(A, n)` | O(n^2) | n iterations × O(n) each. |
| Recursion halving, one call | `f(n):`<br>`  if n <= 1: return`<br>`  f(n/2)` | O(log n) | n halves each call. |
| Recursion halving, two calls | `f(n):`<br>`  if n <= 1: return`<br>`  f(n/2)`<br>`  f(n/2)` | O(n) | T(n)=2T(n/2)+O(1) → O(n). |
| Recursion decrementing by one, one call | `f(n):`<br>`  if n == 0: return`<br>`  f(n-1)` | O(n) | n calls. |
| Recursion decrementing by one, two calls | `f(n):`<br>`  if n == 0: return`<br>`  f(n-1)`<br>`  f(n-1)` | O(2^n) | T(n)=2T(n-1)+O(1) → O(2^n). |

### Why sequential adds but nested multiplies

| Structure | Operation | Example |
|---|---|---|
| Sequential loops | Add | O(n) then O(n^2) → O(n + n^2) = O(n^2) |
| Nested loops | Multiply | Outer n × inner n = n^2 |

Sequential loops run one after another, so their counts add. Nested loops run the inner loop fully for every outer iteration, so their counts multiply.

### Dropping constants and lower-order terms

| Expression | Simplified | Reason |
|---|---|---|
| O(3n^2 + 5n + 7) | O(n^2) | Drop coefficient 3, drop 5n and 7 |
| O(n/2) | O(n) | Drop 1/2 |
| O(2n + log n) | O(n) | n grows faster than log n |
| O(n^2 + n log n) | O(n^2) | n^2 grows faster than n log n |
| O(5) | O(1) | Constant |

### Space complexity

Auxiliary space = extra memory beyond the input.

| Structure | Auxiliary space | Example |
|---|---|---|
| Fixed number of variables | O(1) | `sum = 0; for i = 1 to n: sum = sum + A[i]` |
| Array of size n | O(n) | `B = new array of size n` |
| Recursion depth d | O(d) | `f(n): if n == 0 return; f(n-1)` → depth n → O(n) |

A loop using only `i`, `j`, `sum`, `temp` is O(1) space regardless of n. The input array is not auxiliary. Recursion costs O(depth) stack space even with no explicit array. Recursion of depth n is O(n) space. Recursion halving the input has depth log n, so O(log n) space. Two recursive calls do not multiply space; only maximum depth matters.

### Worked examples

**Snippet A**
```
sum = 0
for i = 1 to n:
    for j = 1 to n:
        sum = sum + i * j
print sum
```
Time: O(n^2). Space: O(1).  
Outer loop runs n times; inner loop runs n times per outer iteration, so innermost statement runs n² times. Only `sum`, `i`, `j` are used; no array or recursion.

**Snippet B**
```
i = 1
while i < n:
    j = 1
    while j <= n:
        x = x + 1
        j = j + 1
    i = i * 2
```
Time: O(n log n). Space: O(1).  
Outer loop doubles `i`, so it runs log n times. Inner loop runs n times per outer iteration, giving n log n total. Fixed variables only.

**Snippet C**
```
function find(A, n, key):
    if n == 0:
        return false
    if A[n-1] == key:
        return true
    return find(A, n-1, key)
```
Time: O(n). Space: O(n).  
Each call reduces n by 1; worst case n calls. Recursion depth is n, so stack space is O(n). The input array `A` is not auxiliary, but the stack is.

### Exam shortcut

- Count nesting depth of loops whose bound depends on n. Each level multiplies by n.
- If a loop multiplies or divides its counter (`i *= 2`, `i /= 2`), that level contributes log n instead of n.
- If the inner bound is the outer variable, two levels still give O(n^2).
- If the inner loop runs a constant number of times, it does not add a factor of n.
- If a loop calls an O(n) operation, multiply: n × n = n^2.
- Recursion: halving → log n depth; decrementing by 1 → n depth. Two calls multiply time by 2 per level; space is still max depth.

## 4. Must-memorise block

| Shape | Complexity |
|---|---|
| Single statement | O(1) |
| Single loop to n | O(n) |
| Two sequential loops to n | O(n) |
| Two nested loops to n | O(n^2) |
| Nested, inner to outer | O(n^2) |
| `i *= 2` or `i /= 2` | O(log n) |
| `i * i < n` | O(√n) |
| Nested, inner constant | O(n) |
| Loop with O(n) inside | O(n^2) |
| Recursion halving, 1 call | O(log n) |
| Recursion halving, 2 calls | O(n) |
| Recursion n−1, 1 call | O(n) |
| Recursion n−1, 2 calls | O(2^n) |

**Add vs multiply**
- Sequential: add. Larger term dominates. O(n) + O(n^2) = O(n^2).
- Nested: multiply. Outer n × inner n = n^2.

**Simplification**
- Drop constants: O(3n^2) = O(n^2), O(n/2) = O(n).
- Drop lower-order terms: O(n^2 + 5n + 7) = O(n^2).
- O(n + log n) = O(n), O(n^2 + n log n) = O(n^2).

**Space rules**
- Fixed variables → O(1) auxiliary space.
- Array of size n → O(n).
- Recursion → O(max depth) stack space.
- Depth n → O(n) space. Depth log n → O(log n) space.
- Two recursive calls do not multiply space; only max depth matters.

## 5. Worked examples

### Example 1 — Single loop

```
1. SET sum = 0
2. FOR i = 1 TO n
3.    SET sum = sum + i
4. PRINT sum
```

Trace for `n = 4`:

| Line | i | sum | Output |
|---|---:|---:|---:|
| 1 | — | 0 | — |
| 2 | 1 | 0 | — |
| 3 | 1 | 1 | — |
| 2 | 2 | 1 | — |
| 3 | 2 | 3 | — |
| 2 | 3 | 3 | — |
| 3 | 3 | 6 | — |
| 2 | 4 | 6 | — |
| 3 | 4 | 10 | — |
| 2 | 5 | 10 | — |
| 4 | 5 | 10 | 10 |

**Final: Time O(n), Space O(1).**

### Example 2 — Two sequential loops

```
1. SET count = 0
2. FOR i = 1 TO n
3.    SET count = count + 1
4. FOR j = 1 TO n
5.    SET count = count + 1
6. PRINT count
```

Trace for `n = 3`:

| Line | i | j | count | Output |
|---|---:|---:|---:|---:|
| 1 | — | — | 0 | — |
| 2 | 1 | — | 0 | — |
| 3 | 1 | — | 1 | — |
| 2 | 2 | — | 1 | — |
| 3 | 2 | — | 2 | — |
| 2 | 3 | — | 2 | — |
| 3 | 3 | — | 3 | — |
| 2 | 4 | — | 3 | — |
| 4 | 4 | 1 | 3 | — |
| 5 | 4 | 1 | 4 | — |
| 4 | 4 | 2 | 4 | — |
| 5 | 4 | 2 | 5 | — |
| 4 | 4 | 3 | 5 | — |
| 5 | 4 | 3 | 6 | — |
| 4 | 4 | 4 | 6 | — |
| 6 | 4 | 4 | 6 | 6 |

**Final: Time O(n), Space O(1).**

### Example 3 — Nested loops

```
1. SET c = 0
2. FOR i = 1 TO n
3.    FOR j = 1 TO n
4.       SET c = c + 1
5. PRINT c
```

Trace for `n = 3`:

| Line | i | j | c | Output |
|---|---:|---:|---:|---:|
| 1 | — | — | 0 | — |
| 2 | 1 | — | 0 | — |
| 3 | 1 | 1 | 0 | — |
| 4 | 1 | 1 | 1 | — |
| 3 | 1 | 2 | 1 | — |
| 4 | 1 | 2 | 2 | — |
| 3 | 1 | 3 | 2 | — |
| 4 | 1 | 3 | 3 | — |
| 3 | 1 | 4 | 3 | — |
| 2 | 2 | — | 3 | — |
| 3 | 2 | 1 | 3 | — |
| 4 | 2 | 1 | 4 | — |
| 3 | 2 | 2 | 4 | — |
| 4 | 2 | 2 | 5 | — |
| 3 | 2 | 3 | 5 | — |
| 4 | 2 | 3 | 6 | — |
| 3 | 2 | 4 | 6 | — |
| 2 | 3 | — | 6 | — |
| 3 | 3 | 1 | 6 | — |
| 4 | 3 | 1 | 7 | — |
| 3 | 3 | 2 | 7 | — |
| 4 | 3 | 2 | 8 | — |
| 3 | 3 | 3 | 8 | — |
| 4 | 3 | 3 | 9 | — |
| 3 | 3 | 4 | 9 | — |
| 2 | 4 | — | 9 | — |
| 5 | 4 | 4 | 9 | 9 |

**Final: Time O(n²), Space O(1).**

### Example 4 — Triangular nested loop

```
1. SET s = 0
2. FOR i = 1 TO n
3.    FOR j = i TO n
4.       SET s = s + 1
5. PRINT s
```

Trace for `n = 4`:

| Line | i | j | s | Output |
|---|---:|---:|---:|---:|
| 1 | — | — | 0 | — |
| 2 | 1 | — | 0 | — |
| 3 | 1 | 1 | 0 | — |
| 4 | 1 | 1 | 1 | — |
| 3 | 1 | 2 | 1 | — |
| 4 | 1 | 2 | 2 | — |
| 3 | 1 | 3 | 2 | — |
| 4 | 1 | 3 | 3 | — |
| 3 | 1 | 4 | 3 | — |
| 4 | 1 | 4 | 4 | — |
| 3 | 1 | 5 | 4 | — |
| 2 | 2 | — | 4 | — |
| 3 | 2 | 2 | 4 | — |
| 4 | 2 | 2 | 5 | — |
| 3 | 2 | 3 | 5 | — |
| 4 | 2 | 3 | 6 | — |
| 3 | 2 | 4 | 6 | — |
| 4 | 2 | 4 | 7 | — |
| 3 | 2 | 5 | 7 | — |
| 2 | 3 | — | 7 | — |
| 3 | 3 | 3 | 7 | — |
| 4 | 3 | 3 | 8 | — |
| 3 | 3 | 4 | 8 | — |
| 4 | 3 | 4 | 9 | — |
| 3 | 3 | 5 | 9 | — |
| 2 | 4 | — | 9 | — |
| 3 | 4 | 4 | 9 | — |
| 4 | 4 | 4 | 10 | — |
| 3 | 4 | 5 | 10 | — |
| 2 | 5 | — | 10 | — |
| 5 | 5 | 5 | 10 | 10 |

**Final: Time O(n²), Space O(1).**  
Iterations = `4 + 3 + 2 + 1 = 10 = n(n+1)/2`.

### Example 5 — While loop with doubling

```
1. SET i = 1
2. SET k = 0
3. WHILE i < n
4.    SET k = k + 1
5.    SET i = i * 2
6. PRINT k
```

Trace for `n = 16`:

| Line | i | k | Output |
|---|---:|---:|---:|
| 1 | 1 | — | — |
| 2 | 1 | 0 | — |
| 3 | 1 | 0 | — |
| 4 | 1 | 1 | — |
| 5 | 2 | 1 | — |
| 3 | 2 | 1 | — |
| 4 | 2 | 2 | — |
| 5 | 4 | 2 | — |
| 3 | 4 | 2 | — |
| 4 | 4 | 3 | — |
| 5 | 8 | 3 | — |
| 3 | 8 | 3 | — |
| 4 | 8 | 4 | — |
| 5 | 16 | 4 |

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid |
|---|---|---|
| **Adding nested loops instead of multiplying** | Two loops "feel" like two passes | Nested loops **multiply** (O(n²)); sequential loops **add** (O(n), larger dominates). Ask: is the second loop *inside* the first? |
| **Calling a triangular loop O(n log n)** | The inner loop clearly runs fewer than n times | `1+2+…+n = n(n+1)/2`, which is **still O(n²)**. Halving a constant never changes the class |
| **Missing a logarithmic loop** | `i = i * 2` looks like ordinary iteration | A counter that **multiplies or divides** its own value is O(log n). Ask: how many times can I double before exceeding n? |
| **Keeping constants and lower-order terms** | `3n² + 5n + 7` looks precise | Big-O drops constants and lower-order terms: **O(n²)**. The answer options will include the unsimplified form |
| **Ignoring an O(n) operation inside a loop** | A single line looks like O(1) | A string concatenation, a list `insert(0,…)`, or a nested search inside a loop multiplies the cost. Read what the body actually does |
| **Saying recursion is O(1) space** | There is no array, so it looks free | **A recursion of depth n costs O(n) stack space.** Depth is the space |
| **Confusing the loop counter's range with n** | `for i from 1 to 100` inside a function looks like a loop over n | A **fixed** bound is O(1) regardless of how large the constant is |
| **Assuming worst case is what is asked** | Best/average/worst are often not stated | If the question says "complexity" without qualifying, give the **worst case** unless the snippet clearly always behaves the same way |

## 7. Practice questions

**1. [Easy]** *(B9 — single loop)*  
What is printed?

```
1 SET n = 5
2 SET sum = 0
3 FOR i = 1 TO n
4     sum = sum + i
5 END FOR
6 PRINT sum
```

(a) 10
(b) 15
(c) 20
(d) 25

---

**2. [Easy]** *(B9 — single loop time)*  
What is the time complexity?

```
1 SET sum = 0
2 FOR i = 1 TO n
3     sum = sum + i
4 END FOR
5 PRINT sum
```

(a) O(1)
(b) O(n)
(c) O(log n)
(d) O(n²)

---

**3. [Easy]** *(B9 — loop variable doubling)*  
What is printed?

```
1 SET n = 100
2 SET count = 0
3 SET i = 1
4 WHILE i < n
5     count = count + 1
6     i = i * 2
7 END WHILE
8 PRINT count
```

(a) 7
(b) 8
(c) 6
(d) 50

---

**4. [Medium]** *(B9 — nested loops)*  
What is printed?

```
1 SET count = 0
2 FOR i = 1 TO 4
3     FOR j = 1 TO 3
4         count = count + 1
5     END FOR
6 END FOR
7 PRINT count
```

(a) 7
(b) 12
(c) 16
(d) 20

---

**5. [Medium]** *(B9 — triangular nested loop)*  
What is printed?

```
1 SET n = 5
2 SET count = 0
3 FOR i = 1 TO n
4     FOR j = i TO n
5         count = count + 1
6     END FOR
7 END FOR
8 PRINT count
```

(a) 20
(b) 10
(c) 15
(d) 25

---

**5. Correct: (c) 15**  
Variable trace:

| i | j range | Increments | count after |
|---:|---|---:|---:|
| 1 | 1 to 5 | 5 | 5 |
| 2 | 2 to 5 | 4 | 9 |
| 3 | 3 to 5 | 3 | 12 |
| 4 | 4 to 5 | 2 | 14 |
| 5 | 5 to 5 | 1 | 15 |

- **(b) 10**: Sums j = i+1 to n, giving 1+2+3+4.
- **(a) 20**: Uses n(n−1) or 5 × 4.
- **(d) 25**: Treats both loops as 1 to n.

---

---

**6. [Medium]** *(B9 — sequential loops)*  
What is the time complexity?

```
1 SET sum = 0
2 FOR i = 1 TO n
3     sum = sum + i
4 END FOR
5 FOR j = 1 TO n
6     sum = sum + j
7 END FOR
8 PRINT sum
```

(a) O(n)
(b) O(1)
(c) O(log n)
(d) O(n²)

---

**6. Correct: (a) O(n)**  
Trace/growth:

| n | First loop | Second loop | Total |
|---:|---:|---:|---:|
| 3 | 3 | 3 | 6 |
| 4 | 4 | 4 | 8 |
| 5 | 5 | 5 | 10 |

- **(b) O(1)**: Ignores both loops.
- **(c) O(log n)**: Confuses linear increment with halving/doubling.
- **(d) O(n²)**: Treats sequential loops as nested.

---

---

**7. [Medium]** *(B9 — recursion halving)*  
What is printed?

```
1 FUNCTION f(n)
2     IF n <= 1
3         RETURN 0
4     END IF
5     RETURN 1 + f(n / 2)   // integer division
6 END FUNCTION
7 PRINT f(16)
```

(a) 4
(b) 5
(c) 3
(d) 8

---

**7. Correct: (a) 4**  
Variable trace:

| Call | n check | Return |
|---|---|---|
| f(16) | 16 > 1 | 1 + f(8) |
| f(8) | 8 > 1 | 1 + f(4) |
| f(4) | 4 > 1 | 1 + f(2) |
| f(2) | 2 > 1 | 1 + f(1) |
| f(1) | 1 ≤ 1 | 0 |

Unwind:

| Return | Value |
|---|---:|
| f(2) | 1 + 0 = 1 |
| f(4) | 1 + 1 = 2 |
| f(8) | 1 + 2 = 3 |
| f(16) | 1 + 3 = 4 |

- **(c) 3**: Returns only log₂(16) − 1 or stops before reaching the base case.
- **(b) 5**: Counts total function calls including f(1), but the return value excludes the base contribution.
- **(d) 8**: Returns n/2 instead of counting halving steps.

---

---

**8. [Medium]** *(B9 — recursion two calls)*  
What is printed?

```
1 FUNCTION g(n)
2     IF n <= 1
3         RETURN 1
4     END IF
5     RETURN g(n - 1) + g(n - 2)
6 END FUNCTION
7 PRINT g(5)
```

(a) 5
(b) 16
(c) 13
(d) 8

---

**8. Correct: (d) 8**  
Variable trace:

| n | Expansion | Value |
|---:|---|---:|
| 0 | base | 1 |
| 1 | base | 1 |
| 2 | g(1) + g(0) | 2 |
| 3 | g(2) + g(1) | 3 |
| 4 | g(3) + g(2) | 5 |
| 5 | g(4) + g(3) | 8 |

- **(a) 5**: Evaluates g(4) instead of g(5).
- **(c) 13**: Computes g(6), an off-by-one in the recurrence index.
- **(b) 16**: Assumes two calls double every level: 2⁴ = 16, ignoring overlapping subproblem values.

---

---

**9. [Hard]** *(B9 — nested loop with condition)*  
What is printed?

```
1 SET n = 5
2 SET count = 0
3 FOR i = 1 TO n
4     FOR j = 1 TO n
5         IF (i + j) % 3 == 0
6             count = count + 1
7         END IF
8     END FOR
9 END FOR
10 PRINT count
```

(a) 12
(b) 8
(c) 10
(d) 9

---

**9. Correct: (d) 9**  
Variable trace:

| i | j with (i+j) % 3 == 0 | count after row |
|---:|---|---:|
| 1 | 2, 5 | 2 |
| 2 | 1, 4 | 4 |
| 3 | 3 | 5 |
| 4 | 2, 5 | 7 |
| 5 | 1, 4 | 9 |

- **(b) 8**: Misses one valid pair, commonly (3, 3).
- **(c) 10**: Counts one invalid pair or assumes every row has two valid j values.
- **(a) 12**: Treats four rows as having three valid j values, but row counts are 2, 2, 1, 2, 2.

---

---

**10. [Hard]** *(B9 — recursive time complexity)*  
What is the time complexity in terms of n?

```
1 FUNCTION h(n)
2     IF n <= 1
3         RETURN 1
4     END IF
5     RETURN h(n - 1) + h(n - 1)
6 END FUNCTION
```

(a) O(n)
(b) O(n²)
(c) O(2ⁿ)
(d) O(n log n)

**Rule:** Sequential loops add: O(n) + O(n) = O(n). Nested loops multiply: O(n) × O(n) = O(n²). One halving recursive call → O(log n); one decrementing recursive call → O(n); two decrementing recursive calls → O(2ⁿ). Recursion depth n costs O(n) stack space.

---

**10. Correct: (c) O(2ⁿ)**  
Growth trace:

| n | Number of calls | Pattern |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 3 | 2¹ + 1 |
| 3 | 7 | 2² + 3 |
| 4 | 15 | 2³ + 7 |
| 5 | 31 | 2⁴ + 15 |

- **(a) O(n)**: Replaces two identical recursive calls with one call.
- **(d) O(n log n)**: Confuses this with a halving divide-and-conquer recurrence.
- **(b) O(n²)**: Sees two calls and assumes nested-loop quadratic growth.

---
## 8. Resources

| Resource | Type | Link | Free/Paid | Time | Why this one |
|---|---|---|---|---|---|
| GfG — Complete guide on complexity analysis | Article | https://www.geeksforgeeks.org/dsa/complete-guide-on-complexity-analysis/ | Free | 30 min | The derivation rules applied directly to loop shapes |
| GfG — Time complexities of all sorting algorithms | Article | https://www.geeksforgeeks.org/competitive-programming/time-complexities-of-all-sorting-algorithms/ | Free | 15 min | Pairs with D5 |
| PrepInsta — Accenture pseudocode | Practice set | https://prepinsta.com/accenture/pseudo-code/general-pseudo-code/ | Free | 25 min | Some items ask for snippet complexity directly |
| `question-banks/QB-T32-B9-snippet-complexity.md` | Question bank | (this library) | Free | 20 min | 20 original questions, all snippet-based |

*All external links verified resolving 2026-09-16.*

## 9. Self-check

- [ ] I can name the complexity of any single, nested, sequential or triangular loop on sight
- [ ] **I recognise a doubling or halving counter as O(log n)**
- [ ] I know sequential loops add and nested loops multiply
- [ ] I can simplify O(3n² + 5n + 7) to O(n²) and explain why
- [ ] I can state the space complexity of a loop using a fixed number of variables
- [ ] **I know a recursion of depth n costs O(n) stack space even with no array**
- [ ] I scored 8/10 or better on the practice questions

## 10. Sources

**Teaching content (§3–§9)** is adapted from `accenture-prep-final/accenture-prep-library/topics/T32-B9-snippet-complexity.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions none in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `P8`). Confidence **Low**. Nothing in this file is a published Infosys syllabus.
