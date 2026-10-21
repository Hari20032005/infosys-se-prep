---
title: Conditionals and Branch Selection in Pseudocode
code: P6
section: Pseudocode
weightage_pct: 1.1% of marks
est_questions: 0.40
tier: 3
difficulty: Medium
est_study_hours: 0.6
confidence: Medium
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-library/topics/T07-B2-conditionals-nested-if.md
---

# P6 — Conditionals and Branch Selection in Pseudocode

*Adapted from `accenture-prep-final/accenture-prep-library/topics/T07-B2-conditionals-nested-if.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.4 questions and 0.8 marks** on this topic (about 1.1% of the 75 scored marks). It sits in **Pseudocode**: 5 questions, 10 marks, 10 minutes. **Tier 3**, 0.6 hours to reach reliable recall, confidence **Medium**.

**2 questions on this topic are in the observed Infosys pool** (O46, O47), from 1 source. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 1.06 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| O46 | 2020-09-22 | Number = 90 tested against 90 < Number < 95: what is displayed? |
| O47 | 2020-09-22 | a=6, b=3, c=2 with a three-way condition, else a=b+1: print a+b+c |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



1. **Trace a 6–12 line snippet ending in `Print a + b + c`.** The universal shape.

**1. (c) 15**  
| Start | a=3 | b=5 | c=7 | sum=15 |
|---|---|---|---|---|
| Guard | a>b | 3>5 false | body skipped | final=15 |
- (b) 25: adds 10 once despite false guard.  
- (a) 45: executes all three +10 updates.  
- (d) 55: overcounts updates by adding extra 10.

---

2. **The dead-guard pattern.** Confirmed in 4 local items. The first condition is false, so nothing changes.

**2. (b) 15**  
| Start | a=2 | b=9 | c=4 | sum=15 |
|---|---|---|---|---|
| Guard | (a+b+c) > (c+b+a) | 15>15 false | body skipped | final=15 |
- (a) 25: adds 10 to one variable despite identity guard false.  
- (c) 45: treats identity guard as true and adds 10 to all three.  
- (d) 55: treats guard true plus an extra update.

---

3. **Outer-true, inner-false.** Confirmed in item 68, where the published answer key was itself wrong. You enter the outer block but the inner guard blocks everything.

**3. (b) 17**  
| Start | a=6 | b=2 | c=9 | sum=17 |
|---|---|---|---|---|
| Outer | a>b | 6>2 true | enter outer |  |
| Inner | c<b | 9<2 false | skip inner body | final=17 |
- (c) 18: increments only a as if inner guard true.  
- (a) 19: increments a and c only.  
- (d) 20: treats inner guard true and increments all three.

---

4. **Reassignment before a later read.** Confirmed in 4 local items. A variable is updated, then a later condition must use the *new* value.

**4. (a) 28**  
| Start | a=4 | b=7 | c=3 |  |
|---|---|---|---|---|
| a<b | true |  |  |  |
| a=a+5 | a=9 | b=7 | c=3 |  |
| a>b | 9>7 true |  |  |  |
| c=c+a | a=9 | b=7 | c=12 | final=28 |
- (b) 14: treats outer a<b false, no changes.  
- (c) 19: updates a but treats inner a>b false, c unchanged.  
- (d) 23: uses old a=4 in c=c+a, giving c=7.

---

5. **The identity comparison.** Confirmed twice: `(a+b+c) > (c+b+a)` is **always false** — both sides are equal and `>` is strict.

**5. (a) 44**  
| Start | a=10 | b=4 | c=6 |  |
|---|---|---|---|---|
| a>b | true |  |  |  |
| b=a+b | a=10 | b=14 | c=6 |  |
| b>a | 14>10 true |  |  |  |
| c=c+b | a=10 | b=14 | c=20 | final=44 |
- (b) 20: treats outer a>b false, no changes.  
- (c) 34: uses old b=4 in c=c+b, giving c=10.  
- (d) 40: treats inner b>a false, executes c=c+a, giving c=16.

---

6. **Truthiness of integers.** A condition like `((r*q)+q)` is true whenever it is non-zero.

> **No pen and paper.** Hold three variables as a mental triple and restate them after every assignment.

## 3. Concept notes

### 3.1 Boolean foundations

In these papers a condition is **any expression that evaluates to a truth value**. The rule is:

| Expression value | Treated as |
|---|---|
| 0 | FALSE |
| any non-zero integer (1, 5, −3, 100) | TRUE |

So a condition like `if ((r * q) + q)` is **not** a comparison — it is a truthiness test.

| r | q | (r·q)+q | Result |
|---|---|---|---|
| 2 | 3 | 9 | TRUE |
| −1 | 5 | 0 | FALSE |
| 0 | 7 | 7 | TRUE |
| 4 | 0 | 0 | FALSE |

The `−1, 5` case is the trap: non-zero is not the same as positive.

**Truth tables**

| A | B | A AND B | A OR B |
|---|---|---|---|
| F | F | F | F |
| F | T | F | T |
| T | F | F | T |
| T | T | T | T |

| A | NOT A |
|---|---|
| T | F |
| F | T |

### 3.2 Relational operators

| Op | Meaning | True when… |
|---|---|---|
| `>` | strictly greater | left > right only |
| `>=` | greater or equal | left > right **or** equal |
| `<` | strictly less | left < right only |
| `<=` | less or equal | left < right **or** equal |
| `==` | equal to | both sides same value |
| `!=` | not equal to | sides differ |
| `=` | assignment (as a statement); in many papers an equality test when it appears inside a condition | check the paper's convention |

**The single most important fact:** `>` is **strictly** greater. If both sides are equal, the result is **FALSE**.

Worked example:

```
a = 4
b = 9
c = 2
if ((a + b + c) > (c + b + a)) then
    print "YES"
else
    print "NO"
end if
```

Both sides are `4 + 9 + 2 = 15`. The test is `15 > 15`, which is **FALSE**. Output: `NO`.

Any comparison of an expression with **itself reordered** is always FALSE for `>` and `<`, and always TRUE for `>=`, `<=`, `==`.

### 3.3 Branch constructs

| Construct | Shape | Used when |
|---|---|---|
| `if` | one condition, body runs or is skipped | single optional action |
| `if-else` | exactly one of two bodies runs | two-way choice |
| `if-else-if` ladder | first TRUE branch runs, **all remaining branches skipped** | mutually exclusive ranges/grades |
| nested `if` | inner condition only tested if outer is TRUE | dependent conditions |
| `switch/case` | jumps to matching `case`, needs `break` to stop | one value, many discrete options |

Generic syntax:

```
if (condition) then
    statements
end if

if (condition) then
    statements
else
    statements
end if

if (c1) then
    s1
else if (c2) then
    s2
else if (c3) then
    s3
else
    s4
end if

if (outer) then
    if (inner) then
        s
    end if
end if
```

**Ladder vs nested:** in a ladder, at most **one** branch executes and the rest are never tested. In a nested `if`, both outer and inner must be TRUE for the innermost body to run, and tests happen top-down.

**Matching `End if`:** `If` and `End if` pair like brackets. The nearest unmatched `If` is closed by the next `End if` (innermost-first). Indentation mirrors this:

```
if (A) then          <- If #1
    if (B) then      <- If #2
        x = 1
    end if           <- closes If #2
    y = 2            <- still inside If #1
end if               <- closes If #1
```

A line indented at the level of `If #1` is **outside** `If #2`, so it runs whenever the outer guard is TRUE — even when the inner guard is FALSE. This is exactly Trap 2 below.

**switch / case**

```
switch (n)
    case 1:
        x = x + 1
        break
    case 2:
        x = x + 2
        break
    default:
        x = 0
end switch
```

| Detail | Behaviour |
|---|---|
| matching | control jumps to the matching `case` label |
| `break` | exits the whole switch |
| no `break` | **fall-through**: execution continues into the next case body and onward |
| `default` | runs when no case matches — and is also reached by fall-through |

Fall-through worked example:

```
x = 0
switch (2)
    case 1: x = x + 1
    case 2: x = x + 2
    case 3: x = x + 3
    default: x = x + 10
end switch
print x
```

| Step | Action | x |
|---|---|---|
| start | x = 0 | 0 |
| match | case 2 | 0 |
| case 2 | x = 0 + 2 | 2 |
| falls into case 3 | x = 2 + 3 | 5 |
| falls into default | x = 5 + 10 | 15 |

Output `15`. **With a `break` after each case, the output would be `2`.** If no case matches and there is no `default`, nothing executes.

### 3.4 Dry-run / trace table technique

One **column per variable**, one **row per executed line**. Add a "Note" column for the condition result. Update a variable's cell only on the line that assigns it; carry the old value forward otherwise.

Snippet:

```
1  a = 3
2  b = 4
3  c = a * b
4  if (c > 10) then
5      a = c - b
6  end if
print a, b, c
```

| Row | Line | Statement | a | b | c | Note |
|---|---|---|---|---|---|---|
| 1 | 1 | `a = 3` | 3 | — | — | |
| 2 | 2 | `b = 4` | 3 | 4 | — | |
| 3 | 3 | `c = a * b` | 3 | 4 | 12 | 3 × 4 |
| 4 | 4 | `if (c > 10)` | 3 | 4 | 12 | 12 > 10 → TRUE, enter body |
| 5 | 5 | `a = c - b` | 8 | 4 | 12 | 12 − 4 |
| 6 | 6 | `end if` | 8 | 4 | 12 | no change |

Output: `8 4 12`.

Rules that make this fast:

- Write the initial values in row 0 **before** reading any condition.
- Only assignment lines change a cell.
- `print` reads the **current** cell values, i.e. the last row.

### 3.5 Short-circuit evaluation

| Chain | Behaviour |
|---|---|
| `A AND B` | if `A` is FALSE, `B` is **not evaluated**; the result is FALSE |
| `A OR B` | if `A` is TRUE, `B` is **not evaluated**; the result is TRUE |
| `A AND B` with A TRUE | `B` **is** evaluated |
| `A OR B` with A FALSE | `B` **is** evaluated |

Why it changes output: the skipped operand never runs, so any **side effect** inside it never happens, and any error inside it never occurs.

```
a = 0
b = 5
if (a != 0 AND b / a > 1) then
    print "A"
else
    print "B"
end if
```

`a != 0` is FALSE, so `b / a` is never evaluated (no division by zero) and the AND is FALSE. Output `B`.

```
count = 0
flag = 0
if (flag != 0 OR count = count + 1) then
    print "X"
end if
```

`flag != 0` is FALSE, so the OR **does** evaluate the second operand and `count` becomes 1.

**Fast eliminator:** if neither operand has a side effect and neither can error, short-circuit cannot change the printed output. Ignore it and evaluate normally.

### 3.6 The four branch-selection traps

#### Trap 1 — FALSE outer guard makes the body dead code

```
x = 5
y = 3
if (x < y) then
    x = x + 10
    y = y * 2
end if
print x, y
```

| Row | Line | Statement | x | y | Note |
|---|---|---|---|---|---|
| 1 | 1 | `x = 5` | 5 | — | |
| 2 | 2 | `y = 3` | 5 | 3 | |
| 3 | 3 | `if (x < y)` | 5 | 3 | 5 < 3 → **FALSE** |
| 4 | 4–5 | body | 5 | 3 | **skipped, never executed** |
| 5 | 6 | `end if` | 5 | 3 | |

Output: `5 3`.

**Rule: evaluate the outermost condition BEFORE tracing the body.** If it is FALSE, the answer is the current variable values. This alone answers many questions in seconds.

#### Trap 2 — outer TRUE but inner FALSE

```
a = 4
b = 9
if (a < b) then
    if (a > b) then
        a = a + b
        b = a - b
    end if
end if
print a, b
```

| Row | Line | Statement | a | b | Note |
|---|---|---|---|---|---|
| 1 | 1 | `a = 4` | 4 | — | |
| 2 | 2 | `b = 9` | 4 | 9 | |
| 3 | 3 | `if (a < b)` | 4 | 9 | 4 < 9 → TRUE, enter outer |
| 4 | 4 | `if (a > b)` | 4 | 9 | 4 > 9 → **FALSE**, skip inner |
| 5 | 7 | `end if` (inner) | 4 | 9 | no change |
| 6 | 8 | `end if` (outer) | 4 | 9 | no change |

Output: `4 9`.

Wrong answer to avoid: if the inner guard were TRUE the body would give `a = 13`, then `b = 13 − 9 = 4`. Candidates who assume "we entered the outer block, so the body runs" answer `13 4`. It is `4 9`.

#### Trap 3 — a variable reassigned before a later condition reads it

```
a = 10
b = 7
if (a > b) then
    a = a - 5
end if
if (a > b) then
    b = a * 2
else
    b = b * 2
end if
print a, b
```

Correct trace (second condition uses the **NEW** `a`):

| Row | Line | Statement | a | b | Note |
|---|---|---|---|---|---|
| 1 | 1 | `a = 10` | 10 | — | |
| 2 | 2 | `b = 7` | 10 | 7 | |
| 3 | 3 | `if (a > b)` | 10 | 7 | 10 > 7 → TRUE |
| 4 | 4 | `a = a - 5` | **5** | 7 | a is now 5 |
| 5 | 6 | `if (a > b)` | 5 | 7 | 5 > 7 → **FALSE** |
| 6 | 9 | `b = b * 2` | 5 | **14** | else-branch taken |

Output: `5 14`.

Stale-value trace (using the original `a = 10` at line 6):

| Row | Line | Statement | a | b | Note |
|---|---|---|---|---|---|
| 5′ | 6 | `if (a > b)` | 10 | 7 | 10 > 7 → TRUE — **WRONG** |
| 6′ | 7 | `b = a * 2` | 10 | 20 | WRONG |

Wrong answer: `10 20`. The branch flips **and** the value is wrong. Whenever a variable is reassigned above, cross out its old value.

#### Trap 4 — the always-false identity comparison

```
x = 6
y = 2
z = 9
if ((x + y + z) > (z + y + x)) then
    print "YES"
else
    print "NO"
end if
```

| Row | Line | Statement | x | y | z | Note |
|---|---|---|---|---|---|---|
| 1 | 1 | `x = 6` | 6 | — | — | |
| 2 | 2 | `y = 2` | 6 | 2 | — | |
| 3 | 3 | `z = 9` | 6 | 2 | 9 | |
| 4 | 4 | `if (...)` | 6 | 2 | 9 | 17 > 17 → **FALSE** |

Output: `NO`. Both sides are the same three variables summed, so `>` is FALSE and `>=`/`<=`/`==` would be TRUE.

### 3.7 Operator precedence inside a condition

Highest binds first:

| Level | Operators |
|---|---|
| 1 (highest) | `( )` |
| 2 | `*` `/` `%` |
| 3 | `+` `-` |
| 4 | `<` `<=` `>` `>=` `==` `!=` |
| 5 | `NOT` |
| 6 | `AND` |
| 7 (lowest) | `OR` |

Arithmetic binds tighter than relational, which binds tighter than logical. So:

- `a + b > c` → `(a + b) > c`
- `a > b AND c > d` → `(a > b) AND (c > d)`
- `NOT a > b` → `NOT (a > b)` — `NOT` sits below relational, above `AND`
- `a OR b AND c` → `a OR (b AND c)`

Use brackets when tracing to remove all doubt.

### 3.8 60-second attack checklist

| # | Step |
|---|---|
| 1 | List every variable and its initial value in a row. |
| 2 | Scan for assignments **above** the first condition and apply them first. |
| 3 | Evaluate the **outermost** condition with current values. FALSE → entire block is dead code → jump to the print. |
| 4 | TRUE → step into the block; check each inner condition separately. |
| 5 | Wherever a variable was reassigned, use the **new** value in every later condition. |
| 6 | For `>` or `<` with visibly equal sides (especially identical expressions reordered), answer FALSE immediately. |
| 7 | For `switch`, check for missing `break` → fall-through; check for `default`. |
| 8 | Apply short-circuit only if the skipped operand has a side effect or can error. |
| 9 | Print the **final** values, in the order the print statement asks for them. |

## 4. Must-memorise block

**Truth tables**

| A | B | A AND B | A OR B |
|---|---|---|---|
| F | F | F | F |
| F | T | F | T |
| T | F | F | T |
| T | T | T | T |

| A | NOT A |
|---|---|
| T | F |
| F | T |

**Truthy / falsy**

| Value | Condition result |
|---|---|
| `0` | FALSE |
| any non-zero integer, including negatives | TRUE |

`if ((r * q) + q)` is TRUE whenever `(r*q)+q ≠ 0`. With `r = −1, q = 5` it is `0` → FALSE.

**Relational operators**

| Op | True when |
|---|---|
| `>` | left **strictly** greater |
| `>=` | greater or equal |
| `<` | left strictly less |
| `<=` | less or equal |
| `==` | equal |
| `!=` | not equal |
| `=` | assignment as a statement; equality test inside a condition in many papers |

**Strict-greater rule:** if both sides are equal, `>` is FALSE and `<` is FALSE.

**Always-false identity pattern:** `(a + b + c) > (c + b + a)` is **always FALSE**, whatever the values. Same expression reordered is never greater than itself. (`>=`, `<=`, `==` are always TRUE.)

**The four traps**

| # | Trap | One-line rule |
|---|---|---|
| 1 | FALSE outer guard | Evaluate the outermost condition first; if FALSE, the whole body is dead code and the output is the current values. |
| 2 | Outer TRUE, inner FALSE | Entering the outer block does not run the inner body; re-test every inner condition. |
| 3 | Reassignment before a later condition | The later condition reads the **new** value, not the original. |
| 4 | Identity comparison | `(x + y + z) > (z + y + x)` is always FALSE. |

**Branch constructs**

| Construct | Key fact |
|---|---|
| `if` | body runs or is skipped entirely |
| `if-else` | exactly one of the two bodies runs |
| `if-else-if` ladder | first TRUE branch runs; every later branch is skipped untested |
| nested `if` | inner guard is evaluated only if the outer guard is TRUE |
| `switch` + `break` | exactly one case body runs |
| `switch` without `break` | fall-through: continues into every subsequent case and into `default` |
| `switch`, no match, no `default` | nothing executes |

**End-if matching:** pair `If`/`End if` like brackets, innermost first. A line indented at the outer level is outside the inner `If` and runs whenever the outer guard is TRUE.

**Short-circuit**

| Chain | Rule |
|---|---|
| `A AND B` | `A` FALSE → `B` not evaluated → FALSE |
| `A OR B` | `A` TRUE → `B` not evaluated → TRUE |

Matters only when the skipped operand has a side effect or can error (e.g. division by zero). Otherwise it cannot change the output.

**Precedence (high → low):** `( )` → `* / %` → `+ -` → `< <= > >= == !=` → `NOT` → `AND` → `OR`. Arithmetic beats relational; relational beats logical.

**60-second attack checklist**

1. Write all initial values.
2. Apply assignments that sit above the first condition.
3. Evaluate the outermost condition. FALSE → dead code → skip to the print.
4. TRUE → test each inner condition separately.
5. Use reassigned values in every later condition.
6. Equal sides with `>` or `<` → FALSE, instantly.

**6. (b) 13**  
| Start | a=5 | b=8 | c=2 |  |
|---|---|---|---|---|
| a<b | true |  |  |  |
| b=b-a | a=5 | b=3 | c=2 |  |
| b<c | 3<2 false |  |  |  |
| c=c+b | a=5 | b=3 | c=5 | final=13 |
- (a) 12: treats inner b<c true, executes a=a+c, giving a=7.  
- (c) 15: treats outer a<b false, no changes.  
- (d) 23: does not update b before inner test; c=c+b uses b=8, giving c=10.

---

7. `switch`: check `break` (fall-through) and `default`.

**7. (a) 28**  
| Start | a=2 | b=6 | c=3 |  |
|---|---|---|---|---|
| a<b | true |  |  |  |
| c=a+b | a=2 | b=6 | c=8 |  |
| a=c+b | a=14 | b=6 | c=8 |  |
| identity | 28>28 false |  |  | final=28 |
- (b) 29: treats identity guard as true, increments a.  
- (c) 11: treats outer a<b false, no changes.  
- (d) 18: skips c=a+b but executes a=c+b using old c=3, giving a=9.

---

8. Ignore short-circuit unless an operand has a side effect or errors.

**8. (a) 12**

| Line | a | b | c | Note |
|---|---|---|---|---|
| 1–3 | 3 | 4 | 5 | |
| 4 | 3 | 4 | 5 | 3 > 4 is FALSE → skip 5–6 |
| 8 | 3 | 4 | 5 | 3 + 4 + 5 = **12** |

- (b) 20: treated `a > b` as TRUE and ran both body lines (b = 7, c = 10).
- (c) 15: ran only line 5 (b = 7) and left c = 5.
- (d) 7: printed the skipped body's `a + b` and ignored c.

---

9. Print final values, in the order asked.

## 5. Worked examples

### Example 1 — dead outer guard

```text
1  a = 4
2  b = 7
3  c = 2
4  if a > b
5      c = a + b
6      if c > 10
7          a = c - b
8      else
9          b = c + a
10 Print a + b + c
```

| Line | a | b | c | Note |
|---:|---:|---:|---:|---|
| 1 | 4 | — | — | `a = 4` |
| 2 | 4 | 7 | — | `b = 7` |
| 3 | 4 | 7 | 2 | `c = 2` |
| 4 | 4 | 7 | 2 | `a > b` → `4 > 7` false; skip 5–9 |
| 10 | 4 | 7 | 2 | `Print a + b + c` |

**Final answer: 13**

### Example 2 — outer guard true, inner guard false

```text
1  a = 6
2  b = 8
3  c = 3
4  if a < b
5      if c > a
6          a = a + c
7          b = b - c
8  Print a + b + c
```

| Line | a | b | c | Note |
|---:|---:|---:|---:|---|
| 1 | 6 | — | — | `a = 6` |
| 2 | 6 | 8 | — | `b = 8` |
| 3 | 6 | 8 | 3 | `c = 3` |
| 4 | 6 | 8 | 3 | `a < b` → `6 < 8` true |
| 5 | 6 | 8 | 3 | `c > a` → `3 > 6` false; skip 6–7 |
| 8 | 6 | 8 | 3 | `Print a + b + c` |

**Final answer: 17**

### Example 3 — reassignment before a later condition

```text
1  a = 3
2  b = 9
3  c = 5
4  if a < b
5      c = a + b
6      if c > b
7          a = c + b
8      else
9          b = c - a
10 Print a + b + c
```

| Line | a | b | c | Note |
|---:|---:|---:|---:|---|
| 1 | 3 | — | — | `a = 3` |
| 2 | 3 | 9 | — | `b = 9` |
| 3 | 3 | 9 | 5 | `c = 5` |
| 4 | 3 | 9 | 5 | `a < b` → `3 < 9` true |
| 5 | 3 | 9 | 12 | `c = a + b` → `3 + 9 = 12` |
| 6 | 3 | 9 | 12 | `c > b` → `12 > 9` true; uses new `c` |
| 7 | 21 | 9 | 12 | `a = c + b` → `12 + 9 = 21` |
| 10 | 21 | 9 | 12 | `Print a + b + c` |

**Final answer: 42**

### Example 4 — identity comparison is always false

```text
1  a = 2
2  b = 4
3  c = 6
4  if (a + b + c) > (c + b + a)
5      a = a + 10
6      b = b + 10
7      c = c + 10
8  if a < b
9      c = a + b + 5
10 Print a + b + c
```

| Line | a | b | c | Note |
|---:|---:|---:|---:|---|
| 1 | 2 | — | — | `a = 2` |
| 2 | 2 | 4 | — | `b = 4` |
| 3 | 2 | 4 | 6 | `c = 6` |
| 4 | 2 | 4 | 6 | `(a+b+c) > (c+b+a)` → `12 > 12` false; skip 5–7 |
| 8 | 2 | 4 | 6 | `a < b` → `2 < 4` true |
| 9 | 2 | 4 | 11 | `c = a + b + 5` → `2 + 4 + 5 = 11` |
| 10 | 2 | 4 | 11 | `Print a + b + c` |

**Final answer: 17**

### Example 5 — nested if/else after outer true

```text
1  a = 10
2  b = 4
3  c = 7
4  if a > b
5      b = a - c
6      if b > c
7          a = a - b
8      else
9          c = b + a
10 Print a + b + c
```

| Line | a | b | c | Note |
|---:|---:|---:|---:|---|
| 1 | 10 | — | — | `a = 10` |
| 2 | 10 | 4 | — | `b = 4` |
| 3 | 10 | 4 | 7 | `c = 7` |
| 4 | 10 | 4 | 7 | `a > b` → `10 > 4` true |
| 5 | 10 | 3 | 7 | `b = a - c` → `10 - 7 = 3` |
| 6 | 10 | 3 | 7 | `b > c` → `3 > 7` false |
| 9 | 10 | 3 | 13 | `c = b + a` → `3 + 10 = 13` |
| 10 | 10 | 3 | 13 | `Print a + b + c` |

**Final answer: 26**

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid |
|---|---|---|
| Dead outer guard | The `if` is false, so every indented line under it is skipped. People still compute the body. | Check the guard first. If false, jump straight to the next line at the same indent or after the block. |
| True outer, false inner | The outer guard runs, so people assume all nested code runs. The inner guard can still skip its body. | Trace each `if` independently. A true outer only exposes the inner test. |
| Reassignment before a later condition | A variable is changed in the body, then used in the next condition. People read the old value. | After every assignment, update the variable value in your trace before evaluating any later condition. |
| Identity comparison `(a+b+c) > (c+b+a)` | Looks like two different sums. Addition is commutative, so both sides are the same number. | Cancel or reorder: `a+b+c` equals `c+b+a`. Strict `>` is false. |
| `else` binds to nearest `if` | Nested `if` without braces or clear indentation makes people attach `else` to the outer `if`. | Match `else` to the closest unmatched `if` at the same indentation level. |
| `>` vs `>=`, `<` vs `<=` | Boundary values decide the branch. People drop the equality case. | Read the operator exactly. Test the boundary value when values are equal. |
| Compound `and` / `or` | People evaluate only one side or misapply short-circuit logic. | `and`: both must be true. `or`: at least one true. Evaluate left-to-right only if needed. |
| Sequential `if`s vs `else if` | Two separate `if`s can both execute; an `else if` chain stops after the first true branch. | Check whether the second condition is a new `if` or an `else if`. |
| Assignment inside branch changes later output | The final `Print` uses the latest values, not the initial values. | Keep a running value table. Do not use original values for the print unless no assignment ran. |

## 7. Practice questions

1. **[Easy]** *(B2 — false guard / dead code)*  
What is the output?
```
1 a = 3
2 b = 5
3 c = 7
4 if a > b then
5   a = a + 10
6   b = b + 10
7   c = c + 10
8 end if
9 Print a + b + c
```
(a) 45
(b) 25
(c) 15
(d) 55

2. **[Easy]** *(B2 — identity comparison trap)*  
What is the output?
```
1 a = 2
2 b = 9
3 c = 4
4 if (a + b + c) > (c + b + a) then
5   a = a + 10
6   b = b + 10
7   c = c + 10
8 end if
9 Print a + b + c
```
(a) 25  
(b) 15  
(c) 45  
(d) 55  

3. **[Medium]** *(B2 — outer true, inner false)*  
What is the output?
```
1 a = 6
2 b = 2
3 c = 9
4 if a > b then
5   if c < b then
6     a = a + 1
7     b = b + 1
8     c = c + 1
9   end if
10 end if
11 Print a + b + c
```
(a) 19
(b) 17
(c) 18
(d) 20

4. **[Medium]** *(B2 — reassignment before later condition)*  
What is the output?
```
1 a = 4
2 b = 7
3 c = 3
4 if a < b then
5   a = a + 5
6   if a > b then
7     c = c + a
8   end if
9 end if
10 Print a + b + c
```
(a) 28
(b) 14
(c) 19
(d) 23

5. **[Medium]** *(B2 — nested if/else after reassignment)*  
What is the output?
```
1 a = 10
2 b = 4
3 c = 6
4 if a > b then
5   b = a + b
6   if b > a then
7     c = c + b
8   else
9     c = c + a
10  end if
11 end if
12 Print a + b + c
```
(a) 44  
(b) 20  
(c) 34  
(d) 40  

6. **[Hard]** *(B2 — inner false, else executes)*  
What is the output?
```
1 a = 5
2 b = 8
3 c = 2
4 if a < b then
5   b = b - a
6   if b < c then
7     a = a + c
8   else
9     c = c + b
10  end if
11 end if
12 Print a + b + c
```
(a) 12  
(b) 13  
(c) 15  
(d) 23  

7. **[Hard]** *(B2 — reassignment plus identity comparison)*  
What is the output?
```
1 a = 2
2 b = 6
3 c = 3
4 if a < b then
5   c = a + b
6   a = c + b
7 end if
8 if (a + b + c) > (c + b + a) then
9   a = a + 1
10 end if
11 Print a + b + c
```
(a) 28
(b) 29
(c) 11
(d) 18

---

**8. [Easy]** *(B2 — dead code under a FALSE guard)*

```
1  a = 3
2  b = 4
3  c = 5
4  IF a > b THEN
5      b = a + b
6      c = b + a
7  END IF
8  Print a + b + c
```

(a) 12  (b) 20  (c) 15  (d) 7

**9. [Medium]** *(B2 — nested guard, inner FALSE)*

```
1  p = 6
2  q = 2
3  r = 9
4  IF p > q THEN
5      IF r < p THEN
6          q = p + r
7          r = q - p
8      END IF
9  END IF
10 Print p + q + r
```

(a) 30  (b) 17  (c) 42  (d) 15

**9. (b) 17**

| Line | p | q | r | Note |
|---|---|---|---|---|
| 1–3 | 6 | 2 | 9 | |
| 4 | 6 | 2 | 9 | 6 > 2 TRUE → enter |
| 5 | 6 | 2 | 9 | 9 < 6 FALSE → skip 6–7 |
| 10 | 6 | 2 | 9 | 6 + 2 + 9 = **17** |

- (a) 30: read `r < p` as TRUE (q = 15, r = 9).
- (c) 42: read the inner guard as TRUE and used `r = q + p` = 21.
- (d) 15: stopped after computing q = p + r and printed only that.

---

**10. [Medium]** *(B2 — reassignment before the guard)*

```
1  a = 5
2  b = 9
3  c = 2
4  a = a + b
5  IF a > 10 THEN
6      c = a - b
7  ELSE
8      c = b - a
9  END IF
10 Print a + b + c
```

(a) 18  (b) 23  (c) 28  (d) 46

**10. (c) 28**

| Line | a | b | c | Note |
|---|---|---|---|---|
| 1–3 | 5 | 9 | 2 | |
| 4 | 14 | 9 | 2 | a = 5 + 9 |
| 5–6 | 14 | 9 | 5 | 14 > 10 TRUE → c = 14 − 9 |
| 10 | 14 | 9 | 5 | 14 + 9 + 5 = **28** |

- (a) 18: used the stale a = 5 in line 5, so the ELSE ran (c = 9 − 5 = 4).
- (b) 23: printed only a + b, dropping c.
- (d) 46: computed c = a + b = 23 instead of a − b.

---

**11. [Medium]** *(B2 — identity comparison guard)*

```
1  a = 7
2  b = 3
3  c = 6
4  IF (a + b + c) > (c + b + a) THEN
5      a = a + b + c
6      b = a - c
7  ELSE
8      c = a + b
9  END IF
10 Print a + b + c
```

(a) 16  (b) 32  (c) 14  (d) 20

**11. (d) 20**

| Line | a | b | c | Note |
|---|---|---|---|---|
| 1–3 | 7 | 3 | 6 | |
| 4 | 7 | 3 | 6 | 16 > 16 is FALSE → ELSE |
| 8 | 7 | 3 | 10 | c = 7 + 3 |
| 10 | 7 | 3 | 10 | 7 + 3 + 10 = **20** |

- (b) 32: read the identity comparison as TRUE (a = 16, b = 10).
- (a) 16: applied neither branch, printing the initial values.
- (c) 14: used c = a − b = 4 in the ELSE branch.

---

**12. [Medium]** *(B2 — always-false conditions)*
A fragment contains `IF (x + y) > (y + x) THEN ...`. Which statement is correct?

(a) The body runs whenever x > y
(b) The body runs whenever x < y
(c) The body always runs
(d) The body never runs, because both sides are the same sum written in a different order

**12. (d)** Both sides are the same sum reordered, so `>` is never satisfied and the body is unreachable.
- (a) Wrong: the condition never tests x against y at all.
- (b) Wrong: same error — the brackets differ, the value does not.
- (c) Wrong: `>` needs a strict difference; equal sides make it FALSE.

---

**13. [Hard]** *(B2 — sequential IFs sharing one variable)*

```
1  p = 10
2  q = 4
3  r = 7
4  IF p > q THEN
5      r = p - q
6  END IF
7  IF r > p THEN
8      p = r + q
9  ELSE
10     q = r + p
11 END IF
12 Print p + q + r
```

(a) 20  (b) 34  (c) 32  (d) 33

**13. (c) 32**

| Line | p | q | r | Note |
|---|---|---|---|---|
| 1–3 | 10 | 4 | 7 | |
| 4–5 | 10 | 4 | 6 | 10 > 4 TRUE → r = 10 − 4 |
| 7 | 10 | 4 | 6 | 6 > 10 FALSE → ELSE |
| 10 | 10 | 16 | 6 | q = 6 + 10 |
| 12 | 10 | 16 | 6 | 10 + 16 + 6 = **32** |

- (b) 34: never updated r (kept 7), so q = 7 + 10 = 17 and the sum uses 7.
- (a) 20: took `r > p` as TRUE → p = r + q = 10, leaving the sum at 20.
- (d) 33: used the stale r = 7 in the final print with the updated q = 16.

---

**14. [Hard]** *(B2 — IF / ELSE IF chain after a false identity guard)*

```
1  a = 8
2  b = 5
3  c = 3
4  IF (a + b + c) > (c + b + a) THEN
5      a = a + 1
6  ELSE IF a > b + c THEN
7      c = a + b
8  ELSE
9      c = b + c
10 END IF
11 Print a + b + c
```

(a) 26  (b) 16  (c) 17  (d) 21

---

**14. (d) 21**

| Line | a | b | c | Note |
|---|---|---|---|---|
| 1–3 | 8 | 5 | 3 | |
| 4 | 8 | 5 | 3 | 16 > 16 FALSE |
| 6 | 8 | 5 | 3 | 8 > 5 + 3 = 8 → FALSE |
| 9 | 8 | 5 | 8 | c = 5 + 3 |
| 11 | 8 | 5 | 8 | 8 + 5 + 8 = **21** |

- (a) 26: took the ELSE IF as TRUE (8 > 8), so c = a + b = 13.
- (c) 17: took the first branch as TRUE, incrementing a to 9.
- (b) 16: ran no branch and printed the initial values.

---
## 8. Resources

| Resource | Type | Link | Free/Paid | Time | Why this one |
|---|---|---|---|---|---|
| PrepInsta — Accenture pseudocode | Practice set | https://prepinsta.com/accenture/pseudo-code/general-pseudo-code/ | Free | 45 min | Largest free volume of output-prediction items in the observed style |
| CodeChef — Accenture interview questions | Practice set | https://www.codechef.com/practice/accenture-interview-questions | Free | 45 min | Company-tagged practice |
| GfG — Bitwise operators | Article | https://www.geeksforgeeks.org/cpp/bitwise-operators-in-c-cpp/ | Free | 20 min | Conditions in this exam usually contain a bitwise operation; read with T11 |
| `question-banks/QB-T07-B2-conditionals-nested-if.md` | Question bank | (this library) | Free | 40 min | 35 original traces weighted to the four observed traps |

*All external links verified resolving 2026-09-16.*

## 9. Self-check

- [ ] **I evaluate the outermost guard before tracing any body**
- [ ] I recognise `(x+y+z) > (z+y+x)` as always false, instantly
- [ ] I know that `>` fails when both sides are equal
- [ ] I know that any non-zero integer is truthy and 0 is falsy
- [ ] I restate all three variables after every assignment line
- [ ] I can match `End if` to its opening `If` by indentation
- [ ] I can trace a 12-line nested snippet in under 60 seconds without writing anything
- [ ] I can spot a dead body and answer from the initial values alone
- [ ] I scored 11/14 or better on the practice questions

## 10. Sources

**Teaching content (§3–§9)** is adapted from `accenture-prep-final/accenture-prep-library/topics/T07-B2-conditionals-nested-if.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions O46, O47 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `P6`). Confidence **Medium**. Nothing in this file is a published Infosys syllabus.
