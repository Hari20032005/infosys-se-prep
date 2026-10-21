---
title: Loops and Iteration Counting
code: P1
section: Pseudocode
weightage_pct: 3.6% of marks
est_questions: 1.34
tier: 1
difficulty: Easy
est_study_hours: 1.0
confidence: High
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-library/topics/T25-B1-loops-iteration.md
---

# P1 — Loops and Iteration Counting

*Adapted from `accenture-prep-final/accenture-prep-library/topics/T25-B1-loops-iteration.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **1.3 questions and 2.7 marks** on this topic (about 3.6% of the 75 scored marks). It sits in **Pseudocode**: 5 questions, 10 marks, 10 minutes. **Tier 1**, 1.0 hours to reach reliable recall, confidence **High**.

**9 questions on this topic are in the observed Infosys pool** (P01, P02, P04, P05, P06, P08, P09, O48, O50), from 3 sources. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 2.68 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| O48 | 2020-09-22 | Loop i = 1..5 printing k, then j = j+1, k = k+j: which series? |
| O50 | 2020-09-22 | For i from 1 to 1, for j from i to 1: print k+1 with k = 6 |
| P01 | 2026-09-22 | for w = 0 to 5: if (w mod 2 == 0 and w / 2 == 0) display w |
| P02 | 2026-09-22 | x = 27 mod 7; for i = 0 to x: display i |
| P04 | 2025-09-25 | Integer x = 0. do { ++x; display x; x--; } while (x >= -1) |
| P05 | 2025-09-25 | n = 26, i = 0. while (n mod 8 != 0) { n = n + 5; i = i + 1 }. n = n + i. print n |
| P06 | 2024-12-18 | x = 3, y = 2, result = 0. for i = 1 to y: result = result + x * i. print result |
| P08 | 2024-12-18 | n = 123, sum = 0. while n > 0: sum = sum + n mod 10; n = n / 10. print sum |
| P09 | 2024-12-18 | n = 6, sum = 0. for i = 1 to n: if i mod 2 == 0 then sum = sum + i*i else sum = sum + i. print sum |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



1. **Iteration counting.** Whether `from a to b` is inclusive. Confirmed: it is, so `from 3 to 4` is 2 passes.

**1. Correct: (a) 7**  
Trace table:

| Iteration | c | x before | x = x XOR c | x after |
|---:|---:|---:|---:|---:|
| 1 | 3 | 0 | 0 XOR 3 | 3 |
| 2 | 4 | 3 | 3 XOR 4 | 7 |

The loop `for(each c from 3 to 4)` is inclusive, so it runs exactly 2 times. Output is 7.

- (c) 1: Mistaking `XOR` for `AND`, or computing only `3 AND 4`.
- (b) 3: Stopping after the first iteration.
- (d) 12: Multiplying `3 * 4` instead of applying bitwise XOR.

---

2. **Accumulation across passes.** A variable built up over iterations, where you must carry the value forward.

**2. Correct: (b) 14**  
Trace table:

| i | count before | count after |
|---:|---:|---:|
| 2 | 0 | 2 |
| 3 | 2 | 5 |
| 4 | 5 | 9 |
| 5 | 9 | 14 |

Inclusive range `2 to 5` runs `5 - 2 + 1 = 4` times. Output is 14.

- (a) 9: Using exclusive upper bound `2 to 4`, giving `2 + 3 + 4 = 9`.
- (c) 15: Using `1 to 5`, giving `1 + 2 + 3 + 4 + 5 = 15`.
- (d) 20: Using wrong bounds or extra terms.

---

3. **An expression that changes per pass.** Confirmed: a bitwise mask whose result is not constant.

**3. Correct: (b) 3**  
Trace table:

| k | body runs? |
|---:|---|
| 7 | yes |
| 8 | yes |
| 9 | yes |

Inclusive range `7 to 9` runs `9 - 7 + 1 = 3` times.

- (a) 2: Treating the upper bound as exclusive, counting only 7 and 8.
- (c) 4: Counting an extra value, such as 6 through 9.
- (d) 0: Assuming the loop is empty.

---

4. **Nested loops.** Total iterations as a product, or a triangular inner bound.

**4. Correct: (d) 30**  
Trace table:

| i | j | i * j | s before | s after |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 0 | 2 |
| 1 | 3 | 3 | 2 | 5 |
| 2 | 2 | 4 | 5 | 9 |
| 2 | 3 | 6 | 9 | 15 |
| 3 | 2 | 6 | 15 | 21 |
| 3 | 3 | 9 | 21 | 30 |

Output is 30.

- (a) 18: Omitting one outer or inner iteration, producing a partial sum.
- (b) 24: Dropping a `6` term from the sum.
- (c) 36: Adding an extra `6` term or including `j = 4`.

---

5. **`do-while` minimum execution.** That it always runs at least once.

## 3. Concept notes

### 3.1 The three loop forms

**`for` loop** — counter-driven, bounds fixed in the header.

```
for i from a to b step s
    statements
end for
```

**`while` loop** — condition-driven, tested before the body.

```
while condition
    statements
end while
```

**`do-while` loop** — condition tested after the body.

```
do
    statements
while condition
```

| Form | Condition tested | Minimum executions | Counter updated by | Runs zero times? |
|---|---|---|---|---|
| `for` | Before each iteration (top) | 0 | The loop header | Yes, if the start is already past the end |
| `while` | Before each iteration (top) | 0 | You, inside the body | Yes |
| `do-while` | After each iteration (bottom) | **1** | You, inside the body | **Never** |

The do-while trap: the body executes once **before** the condition is ever evaluated. A `do-while` whose condition is false from the start still runs one time. Reading it as "same as while" loses every such question.

### 3.2 Counting iterations — the highest-value skill

Three rules, applied mechanically:

| Form written as | Iterations | Values taken |
|---|---|---|
| `for i from a to b` (inclusive) | `b - a + 1` | a, a+1, …, b |
| `for i = a; i < b; i++` (exclusive) | `b - a` | a, a+1, …, b-1 |
| `for i from a to b step s`, `s > 0` | `floor((b - a) / s) + 1` | a, a+s, a+2s, … ≤ b |
| `while i <= b` … `i = i + s`, starting at a | `floor((b - a) / s) + 1` | same as above |
| `while i < b` … `i = i + s`, starting at a | `ceil((b - a) / s)` | same as above |

Guard: if `b < a` with a positive step, the count is **0** — the formula does not apply. For a descending `step -s`, use `floor((a - b) / s) + 1`.

**Worked examples**

| Loop | Iterations | Values |
|---|---|---|
| `for i from 3 to 4` | `4-3+1 = 2` | 3, 4 |
| `for i from 0 to 4` | `4-0+1 = 5` | 0, 1, 2, 3, 4 |
| `for i from 1 to 10 step 2` | `floor(9/2)+1 = 4+1 = 5` | 1, 3, 5, 7, 9 |
| `for i from 2 to 10 step 3` | `floor(8/3)+1 = 2+1 = 3` | 2, 5, 8 |
| `for i = 0; i < 5; i++` | `5-0 = 5` | 0, 1, 2, 3, 4 |
| `for i = 1; i <= 5; i++` | `5-1+1 = 5` | 1, 2, 3, 4, 5 |
| `for i = 1; i < 5; i++` | `5-1 = 4` | 1, 2, 3, 4 |
| `for i from 1 to n` | `n` | 1 … n |
| `for i from 0 to n-1` | `n` | 0 … n-1 |
| `for i from 0 to n` | `n+1` | 0 … n |
| `for i from 10 to 1 step 1` | `0` | none |
| `for i from 10 to 1 step -1` | `10` | 10 … 1 |

Compare `for i from 1 to n` with `for i from 0 to n-1` — both run exactly `n` times. Compare `for i from 1 to n` with `for i from 0 to n` — the second runs `n+1` times. This single shift is the most common wrong answer.

### 3.3 Off-by-one and the fencepost problem

Fencepost rule: **n posts need n−1 gaps.** Wherever a loop counts the *boundaries* between items, it runs one fewer time than the number of items; wherever it counts the *items*, it runs one time per item.

| Question | Wrong answer | Correct answer | Why |
|---|---|---|---|
| `for i from 1 to 10` — how many times? | 9 | 10 | Inclusive both ends |
| Last index of an n-element array indexed from 0 | n | n-1 | Fencepost |
| `for i = 0; i <= n; i++` — how many times? | n | n+1 | `<=` adds one |
| Pairs among n items | n | n-1 | Pairs = gaps |
| `while i < n` starting at `i = 0` | n+1 | n | `<` drops the last value |

### 3.4 Nested loops

**Independent bounds → multiply.** `for i from 1 to 3` containing `for j from 1 to 5` = `3 × 5 = 15` total inner-body executions.

**Inner bound depends on the outer variable → add, do not multiply.** Sum the inner counts over each outer value.

```
count = 0
for i from 1 to 4
    for j from 1 to i
        count = count + 1
```

| Outer `i` | Inner `j` values | Inner iterations |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 1, 2 | 2 |
| 3 | 1, 2, 3 | 3 |
| 4 | 1, 2, 3, 4 | 4 |
| **Total** | | **10** |

`1 + 2 + 3 + 4 = 10 = 4×5/2`. General case: `for i from 1 to n / for j from 1 to i` runs `n(n+1)/2` times. The mirror form `for j from i to n` also gives `n(n+1)/2` (4+3+2+1 = 10).

### 3.5 `break` and `continue`

| Statement | Effect | Effect on the iteration count |
|---|---|---|
| `break` | Leaves the **innermost** loop immediately | Remaining iterations never happen — count is truncated |
| `continue` | Skips the rest of the body, jumps to the next iteration | The iteration still **counts**; only body work is skipped |

Two traps:
1. In a `for` loop, `continue` still executes the header's increment. In a `while` loop, if the `continue` sits **above** the counter update, the counter never advances → infinite loop.
2. `break` inside nested loops exits one level only; the outer loop resumes normally.

Worked `break`:

```
sum = 0
for i from 1 to 100
    sum = sum + i
    if sum > 20 then break
```

| i | sum after adding | `sum > 20`? |
|---|---|---|
| 1 | 1 | no |
| 2 | 3 | no |
| 3 | 6 | no |
| 4 | 10 | no |
| 5 | 15 | no |
| 6 | 21 | **yes → break** |

Body executed 6 times, output 21 — not 100 iterations and not 5050.

### 3.6 Infinite loops

| Cause | Example |
|---|---|
| Counter never updated | `i = 0` / `while i < 5` / `print i` — no `i = i + 1` |
| Update in the wrong direction | `while i < 5` … `i = i - 1` |
| Update outside the loop body | Increment written after `end while` |
| Condition can never be hit | `while i != 10` … `i = i + 2`, starting `i = 1` (takes odd values forever) |
| Condition is literally true | `while true` with no reachable `break` |
| Counter reset inside the body | `while i < 5` … `i = 0` at the top of each pass |

An infinite loop is not always a `while true`: any loop whose exit condition the updates cannot reach is infinite.

### 3.7 Loop invariants (informal)

A loop invariant is a statement that is **true before the loop starts and stays true after every iteration**. It is the standard way to reason about what a loop has computed when it stops.

Example — the sum loop below has the invariant: *"at the top of each pass, `sum` equals the total of all integers from 1 to `i - 1`."* Check it before pass 1 (`sum = 0`, `i = 1`, nothing added — true), check it after each pass, and the invariant plus the exit condition `i > 5` proves the final `sum` is `1+2+3+4+5`.

In MCQs you rarely write invariants down, but recognising one tells you quickly whether a loop computes `n(n+1)/2`, `n²`, or a running product.

### 3.8 Fully worked trace table

```
sum = 0
i = 1
while i <= 5
    sum = sum + i
    i = i + 1
end while
print sum
```

| Pass | `i` before check | `i <= 5`? | `sum` before | `sum = sum + i` | `i = i + 1` | `sum` after | `i` after |
|---|---|---|---|---|---|---|---|
| 1 | 1 | true | 0 | 0 + 1 = 1 | 1 + 1 = 2 | 1 | 2 |
| 2 | 2 | true | 1 | 1 + 2 = 3 | 2 + 1 = 3 | 3 | 3 |
| 3 | 3 | true | 3 | 3 + 3 = 6 | 3 + 1 = 4 | 6 | 4 |
| 4 | 4 | true | 6 | 6 + 4 = 10 | 4 + 1 = 5 | 10 | 5 |
| 5 | 5 | true | 10 | 10 + 5 = 15 | 5 + 1 = 6 | 15 | 6 |
| — | 6 | **false** | 15 | — | — | 15 | 6 |

**Output: 15.** Iterations: 5. Cross-check with the formula: `sum 1..5 = 5×6/2 = 15`. ✔

Note the exit row: the condition is evaluated a 6th time, is false, and **nothing inside the body runs**. The final value of `i` is 6, not 5 — exam options frequently offer both.

### 3.9 Exam pattern: a variable modified inside the loop

When the loop counter or the tested variable is changed inside the body, the arithmetic progression is broken. Always trace value by value.

**Example A — counter jumped by 3.**

```
i = 1
total = 0
while i <= 20
    total = total + i
    i = i + 3
```

Values added: 1, 4, 7, 10, 13, 16, 19 (next would be 22 > 20, stop). Count = 7, total = 1+4+7+10+13+16+19 = **70**. Cross-check: `floor((19-1)/3)+1 = 7`; arithmetic series sum `= 7 × (1+19)/2 = 70`. ✔

**Example B — the tested variable doubles (not a fixed step).**

```
x = 1
count = 0
while x < 50
    x = x * 2
    count = count + 1
```

| Pass | `x` before | `x < 50`? | `x` after | `count` after |
|---|---|---|---|---|
| 1 | 1 | true | 2 | 1 |
| 2 | 2 | true | 4 | 2 |
| 3 | 4 | true | 8 | 3 |
| 4 | 8 | true | 16 | 4 |
| 5 | 16 | true | 32 | 5 |
| 6 | 32 | true | 64 | 6 |
| — | 64 | **false** | 64 | 6 |

**Output: 6.** The step size is not constant, so `b - a + 1` and the step formula do **not** apply — only a trace, or the log rule below.

**Example C — the tested variable is overwritten mid-loop.**

```
i = 1
while i <= 10
    print i
    if i = 3 then i = 8
    i = i + 1
```

Prints 1, 2, 3, then jumps to 8, prints 8, 9, 10 → **6 values printed** (1, 2, 3, 8, 9, 10), not 10. The jump skips 4, 5, 6, 7 entirely.

### 3.10 Summation shortcuts

| Quantity | Formula | Check |
|---|---|---|
| `1 + 2 + … + n` | `n(n+1)/2` | n=5 → 15 |
| `1 + 2 + … + n` (triangular nested loop count) | `n(n+1)/2` | n=4 → 10 |
| First n even numbers `2+4+…+2n` | `n(n+1)` | n=4 → 20 |
| First n odd numbers `1+3+…+(2n-1)` | `n²` | n=5 → 25 |
| `1 + 2 + … + (n-1)` | `n(n-1)/2` | n=5 → 10, i.e. pairs among n items |

**Halving / doubling loops (log base 2).**

| Form | Iterations |
|---|---|
| `while n > 1` … `n = floor(n / 2)` | `floor(log2 n)` |
| `while n > 0` … `n = floor(n / 2)` | `floor(log2 n) + 1` |
| `x = 1; while x < n` … `x = x * 2` (n > 1) | `floor(log2 n) + 1` |

| n | `while n > 1: n = n/2` | `while n > 0: n = n/2` | `x = 1; while x < n: x = x*2` |
|---|---|---|---|
| 8 | 3 (8→4→2→1) | 4 | 4 |
| 10 | 3 (10→5→2→1) | 4 | 4 |
| 50 | — | — | 6 |
| 100 | 6 (100→50→25→12→6→3→1) | 7 | 7 |

Use these to answer in seconds what a trace would take a minute to do — but only after confirming the loop is a pure halving/doubling pattern with no extra modification.

---

## 4. Must-memorise block

**Three loop forms — minimum executions**

| Form | Syntax | Tested | Min runs |
|---|---|---|---|
| `for` | `for i from a to b step s … end for` | top | 0 |
| `while` | `while cond … end while` | top | 0 |
| `do-while` | `do … while cond` | bottom | **1 — always at least once** |

**Do-while trap:** the body runs *before* the first condition test. A `do-while` with an already-false condition still executes exactly once. `while` with the same condition executes zero times.

**Three iteration-count formulas**

| Rule | Formula | Worked number |
|---|---|---|
| Inclusive `for i from a to b` | `b - a + 1` | `from 3 to 4` → `4-3+1 = 2` |
| Exclusive `for i = a; i < b; i++` | `b - a` | `i = 1; i < 5` → `5-1 = 4` |
| Stepped `for i from a to b step s` | `floor((b-a)/s) + 1` | `from 1 to 10 step 2` → `floor(9/2)+1 = 5` |

Anchors: `from 3 to 4` = 2 · `from 0 to 4` = 5 · `from 1 to 10 step 2` = 5 · `from 1 to n` = n · `from 0 to n-1` = n · `from 0 to n` = n+1.
If `b < a` with a positive step → **0 iterations**.

**Summation shortcuts**

| Quantity | Formula |
|---|---|
| `1 + 2 + … + n` | `n(n+1)/2` |
| `1 + 2 + … + (n-1)` | `n(n-1)/2` |
| First n even numbers | `n(n+1)` |
| First n odd numbers | `n²` |
| Halving `while n > 1: n = n/2` | `floor(log2 n)` |
| Halving `while n > 0: n = n/2` | `floor(log2 n) + 1` |
| Doubling `x = 1; while x < n: x = x*2` (n > 1) | `floor(log2 n) + 1` |

**Nested loops:** independent bounds → **multiply** (`3 × 5 = 15`). Inner bound depends on the outer variable → **add the inner counts** (`1+2+3+4 = 10 = n(n+1)/2` for n=4).

**`break` vs `continue`:** `break` ends the innermost loop and cuts the remaining iterations. `continue` skips only the rest of the body — the iteration still counts. In a `while` loop, `continue` placed above the counter update causes an infinite loop.

**Infinite loop causes:** no update · wrong-direction update · update outside the body · an unreachable exit value (`while i != 10` with `i = i + 2` from 1) · `while true` with no reachable `break` · counter reset inside the body.

**Off-by-one checklist:** inclusive `to b` adds 1 · `<=` adds 1 versus `<` · n-element array indexed from 0 ends at `n-1` · n posts have `n-1` gaps · `for i from 1 to n` and `for i from 0 to n-1` are both n iterations, but `for i from 0 to n` is n+1.

**Trace discipline:** on exit, the condition is evaluated one final time and fails — record the final counter value, which is usually one past the last value used in the body.

## 5. Worked examples

### Example 1 — Inclusive `for(each)` with bitwise XOR

1. `total ← 0`
2. `for(each c from 3 to 4)`
3. `    total ← total + (c BITXOR 1)`
4. `end for`
5. `print total`

| Line | c | total | Output/Notes |
|---:|---:|---:|---|
| 1 | — | 0 | total initialized |
| 2 | 3 | 0 | enter iteration 1 |
| 3 | 3 | 2 | `3 BITXOR 1 = 2`; total = 0 + 2 |
| 4 | 3 | 2 | end iteration 1; next c = 4 |
| 2 | 4 | 2 | enter iteration 2 |
| 3 | 4 | 7 | `4 BITXOR 1 = 5`; total = 2 + 5 |
| 4 | 4 | 7 | end iteration 2; loop ends |
| 5 | 4 | 7 | print 7 |

**Final answer: 7**

### Example 2 — Exclusive upper bound with `while i < 5`

1. `sum ← 0`
2. `i ← 1`
3. `while i < 5`
4. `    sum ← sum + i`
5. `    i ← i + 1`

**5. Correct: (a) 3**  
Trace table:

| c | c AND 3 | x before | x after |
|---:|---:|---:|---:|
| 3 | 3 | 0 | 3 |
| 4 | 0 | 3 | 3 |

`for(each c from 3 to 4)` is inclusive and runs 2 times. Output is 3.

- (b) 0: Treating both `c AND 3` values as 0.
- (c) 4: Using `c AND 4` instead of `c AND 3`.
- (d) 7: Adding `3 + 4` instead of applying bitwise AND.

---

6. `end while`

**6. Correct: (b) 9**  
Trace table:

| i | s before | s after | i after |
|---:|---:|---:|---:|
| 1 | 0 | 1 | 3 |
| 3 | 1 | 4 | 5 |
| 5 | 4 | 9 | 7 |

Loop stops when `i = 7`, because `7 <= 5` is false. Output is 9.

- (a) 6: Incrementing `i` by 1, giving `1 + 2 + 3 = 6`.
- (c) 12: Running an extra iteration or adding a term twice.
- (d) 15: Adding `1 + 2 + 3 + 4 + 5`.

---

7. `print sum`

| Line | sum | i | Output/Notes |
|---:|---:|---:|---|
| 1 | 0 | — | sum initialized |
| 2 | 0 | 1 | i initialized |
| 3 | 0 | 1 | `1 < 5` true |
| 4 | 1 | 1 | sum = 0 + 1 |
| 5 | 1 | 2 | i = 1 + 1 |
| 6 | 1 | 2 | end iteration 1 |
| 3 | 1 | 2 | `2 < 5` true |
| 4 | 3 | 2 | sum = 1 + 2 |
| 5 | 3 | 3 | i = 2 + 1 |
| 6 | 3 | 3 | end iteration 2 |
| 3 | 3 | 3 | `3 < 5` true |
| 4 | 6 | 3 | sum = 3 + 3 |
| 5 | 6 | 4 | i = 3 + 1 |
| 6 | 6 | 4 | end iteration 3 |
| 3 | 6 | 4 | `4 < 5` true |
| 4 | 10 | 4 | sum = 6 + 4 |
| 5 | 10 | 5 | i = 4 + 1 |
| 6 | 10 | 5 | end iteration 4 |
| 3 | 10 | 5 | `5 < 5` false |
| 7 | 10 | 5 | print 10 |

**Final answer: 10**

### Example 3 — Nested inclusive loops

1. `count ← 0`
2. `for(each i from 1 to 2)`
3. `    for(each j from 1 to 2)`
4. `        count ← count + (i * j)`
5. `    end for`
6. `end for`
7. `print count`

| Line | i | j | count | Output/Notes |
|---:|---:|---:|---:|---|
| 1 | — | — | 0 | count initialized |
| 2 | 1 | — | 0 | enter outer iteration 1 |
| 3 | 1 | 1 | 0 | enter inner iteration 1 |
| 4 | 1 | 1 | 1 | `i * j = 1`; count = 0 + 1 |
| 5 | 1 | 1 | 1 | end inner iteration 1; next j = 2 |
| 3 | 1 | 2 | 1 | enter inner iteration 2 |
| 4 | 1 | 2 | 3 | `i * j = 2`; count = 1 + 2 |
| 5 | 1 | 2 | 3 | end inner iteration 2; inner loop ends |
| 6 | 1 | 2 | 3 | end outer iteration 1; next i = 2 |
| 2 | 2 | 2 | 3 | enter outer iteration 2 |
| 3 | 2 | 1 | 3 | enter inner iteration 1 |
| 4 | 2 | 1 | 5 | `i * j = 2`; count = 3 + 2 |
| 5 | 2 | 1 | 5 | end inner iteration 1; next j = 2 |
| 3 | 2 | 2 | 5 | enter inner iteration 2 |
| 4 | 2 | 2 | 9 | `i * j = 4`; count = 5 + 4 |
| 5 | 2 | 2 | 9 | end inner iteration 2; inner loop ends |
| 6 | 2 | 2 | 9 | end outer iteration 2; outer loop ends |
| 7 | 2 | 2 | 9 | print 9 |

**Final answer: 9**

### Example 4 — Variable modified inside changes later iterations

1. `x ← 0`
2. `i ← 1`
3. `while i <= 5`
4. `    x ← x + i`
5. `    i ← i + 2`
6. `end while`
7. `print x`

| Line | x | i | Output/Notes |
|---:|---:|---:|---|
| 1 | 0 | — | x initialized |
| 2 | 0 | 1 | i initialized |
| 3 | 0 | 1 | `1 <= 5` true |
| 4 | 1 | 1 | x = 0 + 1 |
| 5 | 1 | 3 | i = 1 + 2 |
| 6 | 1 | 3 | end iteration 1 |
| 3 | 1 | 3 | `3 <= 5` true |
| 4 | 4 | 3 | x = 1 + 3 |
| 5 | 4 | 5 | i = 3 + 2 |
| 6 | 4 | 5 | end iteration 2 |
| 3 | 4 | 5 | `5 <= 5` true |
| 4 | 9 | 5 | x = 4 + 5 |
| 5 | 9 | 7 | i = 5 + 2 |
| 6 | 9 | 7 | end iteration 3 |
| 3 | 9 | 7 | `7 <= 5` false |
| 7 | 9 | 7 | print 9 |

**Final answer: 9**

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid |
|---|---|---|
| Assuming `for(each c from 3 to 4)` excludes 4. | People import the C-style habit `for(i=0; i<n; i++)`, where the upper bound is not executed. | Treat `from A to B` as inclusive unless the pseudocode explicitly writes `< B` or `exclusive`. For `3 to 4`, values are 3 and 4. |
| Counting iterations by the final loop variable instead of distinct values. | For `3 to 4`, final `c` is 4, but iterations = 2. | For step 1 inclusive, iterations = end − start + 1. Verify by listing values. |
| Modifying a `for(each)` loop variable inside the body. | In many for-each loops, the next iteration resets the loop variable to the next range value, so the body change is overwritten. | If modification must affect later iterations, use a `while` loop or confirm the exact for-loop semantics. Do not assume the change carries forward. |
| Forgetting that `while` re-tests the condition after every body update. | The variable updated at the bottom changes whether the next iteration runs. | Trace the condition line every time. Update the variable in the table before the next condition row. |
| Using multiplication for nested loop body count when the inner bound depends on the outer variable. | Total inner executions are the sum of inner counts, not necessarily outer_count × inner_count. | Compute inner iterations per outer value and add them. |
| Mixing `<` and `<=` in the loop condition. | `i < 5` stops at 4; `i <= 5` includes 5. One character changes the output. | Write actual values before tracing: `1,2,3,4` versus `1,2,3,4,5`. |
| Treating `BITXOR` or `BITAND` as decimal arithmetic or using wrong precedence. | Bitwise operations work on binary bits; e.g. `3 BITXOR 1 = 2`, not 4. | Parenthesize bitwise expressions and compute in binary before substituting. |
| Relying on a loop variable after the loop ends. | A for-loop variable may be one past the last value, or undefined, depending on the pseudocode definition. | Only use variables after the loop if the pseudocode explicitly shows the final assignment. |
| Skipping trace rows for `end for`, `end while`, and condition retests. | Those rows are where the next value or termination decision is set, so skipped rows cause wrong iteration counts. | Include one row per executed line, especially condition and end-of-loop lines. |

## 7. Practice questions

1. **[Easy]** *(B1 — loops and iteration counting)*  
   What is the output?
   ```pseudocode
   1. Set x = 0
   2. for(each c from 3 to 4)
   3.    x = x XOR c
   4. end for
   5. print x
   ```
   (a) 3
   (b) 7
   (c) 1
   (d) 12

2. **[Easy]** *(B1 — loops and iteration counting)*  
   What is the output?
   ```pseudocode
   1. Set count = 0
   2. for(i from 2 to 5)
   3.    count = count + i
   4. end for
   5. print count
   ```
   (a) 15
   (b) 14
   (c) 9
   (d) 20

3. **[Easy]** *(B1 — loops and iteration counting)*  
   How many times does the loop body execute?
   ```pseudocode
   for(each k from 7 to 9)
       print k
   end for
   ```
   (a) 2
   (b) 3
   (c) 4
   (d) 0

4. **[Medium]** *(B1 — loops and iteration counting)*  
   What is the output?
   ```pseudocode
   1. Set s = 0
   2. for(i from 1 to 3)
   3.    for(j from 2 to 3)
   4.       s = s + (i * j)
   5.    end for
   6. end for
   7. print s
   ```
   (a) 18
   (b) 24
   (c) 30
   (d) 36

5. **[Medium]** *(B1 — loops and iteration counting)*  
   What is the output?
   ```pseudocode
   1. Set x = 0
   2. for(each c from 3 to 4)
   3.    x = x + (c AND 3)
   4. end for
   5. print x
   ```
   (a) 7
   (b) 0
   (c) 4
   (d) 3

6. **[Medium]** *(B1 — loops and iteration counting)*  
   What is the output?
   ```pseudocode
   1. Set i = 1
   2. Set s = 0
   3. while i <= 5
   4.    s = s + i
   5.    i = i + 2
   6. end while
   7. print s
   ```
   (a) 6  
   (b) 9  
   (c) 12  
   (d) 15

7. **[Medium]** *(B1 — loops and iteration counting)*  
   What is the output?
   ```pseudocode
   1. Set t = 0
   2. for(i from 1 to 3)
   3.    for(j from 1 to i - 1)
   4.       t = t + j
   5.    end for
   6. end for
   7. print t
   ```
   (a) 3
   (b) 6
   (c) 4
   (d) 10

**7. Correct: (c) 4**  
Trace table:

| i | j range | j | t before | t after |
|---:|---|---:|---:|---:|
| 1 | 1 to 0 | none | 0 | 0 |
| 2 | 1 to 1 | 1 | 0 | 1 |
| 3 | 1 to 2 | 1 | 1 | 2 |
| 3 | 1 to 2 | 2 | 2 | 4 |

Output is 4.

- (a) 3: Using an exclusive lower bound or missing the `j = 2` addition.
- (b) 6: Using `j from 1 to i`, which adds `1 + 2 + 3` for `i = 3`.
- (d) 10: Using a fixed inner range and miscalculating the total.

---

8. **[Medium]** *(B1 — loops and iteration counting)*  
   A loop is:
   ```pseudocode
   for(i from 4 to 10)
       for(j from 1 to 3)
           print i, j
       end for
   end for
   ```
   How many times is `print i, j` executed?
   (a) 18
   (b) 30
   (c) 21
   (d) 24

**8. Correct: (c) 21**  
Trace/count table:

| i | inner j values | inner executions |
|---:|---|---:|
| 4 | 1, 2, 3 | 3 |
| 5 | 1, 2, 3 | 3 |
| 6 | 1, 2, 3 | 3 |
| 7 | 1, 2, 3 | 3 |
| 8 | 1, 2, 3 | 3 |
| 9 | 1, 2, 3 | 3 |
| 10 | 1, 2, 3 | 3 |

Outer loop runs `10 - 4 + 1 = 7` times. Inner loop runs 3 times each. Total = `7 * 3 = 21`.

- (a) 18: Using outer range `4 to 9`, giving `6 * 3`.
- (d) 24: Using outer range `4 to 11`, giving `8 * 3`.
- (b) 30: Using 10 outer iterations and 3 inner iterations.

---

9. **[Medium]** *(B1 — loops and iteration counting)*  
   What is the output?
   ```pseudocode
   1. Set r = 1
   2. for(c from 2 to 4)
   3.    r = r XOR c
   4. end for
   5. print r
   ```
   (a) 4
   (b) 3
   (c) 0
   (d) 7

**9. Correct: (a) 4**  
Trace table:

| c | r before | r XOR c | r after |
|---:|---:|---:|---:|
| 2 | 1 | 1 XOR 2 = 3 | 3 |
| 3 | 3 | 3 XOR 3 = 0 | 0 |
| 4 | 0 | 0 XOR 4 = 4 | 4 |

Output is 4.

- (c) 0: Stopping at `c = 3`, where `3 XOR 3 = 0`.
- (b) 3: Computing only the first iteration.
- (d) 7: Adding XOR results as `3 + 0 + 4`.

---

10. **[Hard]** *(B1 — loops and iteration counting)*  
    What is the output?
    ```pseudocode
    1. Set n = 0
    2. Set i = 1
    3. while i <= 4
    4.    Set j = i
    5.    while j <= 4
    6.       n = n + (i XOR j)
    7.       j = j + 1
    8.    end while
    9.    i = i + 1
    10. end while
    11. print n
    ```
    (a) 20
    (b) 24
    (c) 32
    (d) 28

**10. Correct: (b) 24**  
Trace table:

| i | j | i XOR j | n after |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 |
| 1 | 2 | 3 | 3 |
| 1 | 3 | 2 | 5 |
| 1 | 4 | 5 | 10 |
| 2 | 2 | 0 | 10 |
| 2 | 3 | 1 | 11 |
| 2 | 4 | 6 | 17 |
| 3 | 3 | 0 | 17 |
| 3 | 4 | 7 | 24 |
| 4 | 4 | 0 | 24 |

Output is 24.

- (a) 20: Omitting one XOR term or stopping before `i = 4`.
- (d) 28: Adding an extra term, such as an additional 4.
- (c) 32: Including extra iterations or miscalculating XOR.

---

11. **[Hard]** *(B1 — loops and iteration counting)*  
    What is the output?
    ```pseudocode
    1. Set a = 5
    2. Set b = 0
    3. while a > 0
    4.    b = b + (a AND 3)
    5.    a = a - 2
    6. end while
    7. print b
    ```
    (a) 3
    (b) 5
    (c) 4
    (d) 7

**11. Correct: (b) 5**  
Trace table:

| a | a AND 3 | b before | b after | a after |
|---:|---:|---:|---:|---:|
| 5 | 1 | 0 | 1 | 3 |
| 3 | 3 | 1 | 4 | 1 |
| 1 | 1 | 4 | 5 | -1 |

Loop stops when `a = -1`, because `-1 > 0` is false. Output is 5.

- (a) 3: Missing the iteration for `a = 1` or `a = 5`.
- (c) 4: Miscomputing one bitwise AND value.
- (d) 7: Treating AND as addition or using OR instead of AND.

---

12. **[Hard]** *(B1 — loops and iteration counting)*  
    What is the output?
    ```pseudocode
    1. Set total = 0
    2. for(i from 1 to 3)
    3.    Set k = 0
    4.    while k < i
    5.       total = total + (i OR k)
    6.       k = k + 1
    7.    end while
    8. end for
    9. print total
    ```
    (a) 12
    (b) 9
    (c) 18
    (d) 15

**Rule:** In pseudocode, `for i from A to B` is inclusive: it executes `B - A + 1` times if `B >= A`, and 0 times if `B < A`. `for i from A to B - 1` and `while i < B` exclude `B`. In a counted `for`, the loop variable is assigned the next value from the range each iteration; changing it inside the body does not change the iteration count. In a `while`/`repeat`, assignments inside the body can change later iterations. Bitwise `AND`, `OR`, and `XOR` operate on binary representations.

**12. Correct: (d) 15**  
Trace table:

| i | k | i OR k | total after |
|---:|---:|---:|---:|
| 1 | 0 | 1 | 1 |
| 2 | 0 | 2 | 3 |
| 2 | 1 | 3 | 6 |
| 3 | 0 | 3 | 9 |
| 3 | 1 | 3 | 12 |
| 3 | 2 | 3 | 15 |

Output is 15.

- (b) 9: Stopping after `i = 2`.
- (a) 12: Missing the final `k = 2` addition for `i = 3`.
- (c) 18: Adding an extra inner iteration or miscalculating OR.

---
## 8. Resources

| Resource | Type | Link | Free/Paid | Time | Why this one |
|---|---|---|---|---|---|
| PrepInsta — Accenture pseudocode | Practice set | https://prepinsta.com/accenture/pseudo-code/general-pseudo-code/ | Free | 40 min | Loop-based output prediction in the observed style |
| CodeChef — Accenture interview questions | Practice set | https://www.codechef.com/practice/accenture-interview-questions | Free | 40 min | Company-tagged practice |
| GfG — Complexity analysis guide | Article | https://www.geeksforgeeks.org/dsa/complete-guide-on-complexity-analysis/ | Free | 20 min | Iteration counting is the foundation of B9; read them together |
| `question-banks/QB-T25-B1-loops-iteration.md` | Question bank | (this library) | Free | 30 min | 20 original questions |

*All external links verified resolving 2026-09-16.*

## 9. Self-check

- [ ] **I know `for i from a to b` is inclusive and runs b−a+1 times**
- [ ] I know `for i = a; i < b; i++` runs b−a times
- [ ] I can compute iterations for a loop with a step other than 1
- [ ] I can compute total iterations for a nested and for a triangular loop
- [ ] I know a `do-while` always executes at least once
- [ ] I recompute every expression inside the body on each pass rather than assuming it is constant
- [ ] I can apply the sum shortcuts n(n+1)/2 and n² for the first n odd numbers
- [ ] I scored 9/12 or better on the practice questions

## 10. Sources

**Teaching content (§3–§9)** is adapted from `accenture-prep-final/accenture-prep-library/topics/T25-B1-loops-iteration.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions P01, P02, P04, P05, P06, P08, P09, O48, O50 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `P1`). Confidence **High**. Nothing in this file is a published Infosys syllabus.
