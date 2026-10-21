---
title: Functions — Scope and Pass by Value vs Reference
code: P7
section: Pseudocode
weightage_pct: 0.9% of marks
est_questions: 0.35
tier: 4
difficulty: Medium
est_study_hours: 0.6
confidence: Medium
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-library/topics/T35-B5-functions-scope.md
---

# P7 — Functions — Scope and Pass by Value vs Reference

*Adapted from `accenture-prep-final/accenture-prep-library/topics/T35-B5-functions-scope.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.4 questions and 0.7 marks** on this topic (about 0.9% of the 75 scored marks). It sits in **Pseudocode**: 5 questions, 10 marks, 10 minutes. **Tier 4**, 0.6 hours to reach reliable recall, confidence **Medium**.

**1 question on this topic are in the observed Infosys pool** (O49), from 1 source. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.94 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| O49 | 2020-09-22 | Function with while(b): temp = a MOD b ... called with a=10, b=6 |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



1. **"Does this swap work?"** The archetype. A swap function under pass-by-value, and you must see that the caller's variables are unchanged.

**1. (a) 14** — `ADD(3, 4)` returns 7, and `7 * 2 = 14`.

| Call | a | b | RETURN | Printed |
|---|---|---|---|---|
| ADD(3, 4) | 3 | 4 | 7 | 7 * 2 = 14 |

- (b) 7 is the return value before the multiplication.
- (c) 24 wrongly applies the multiply inside the function.
- (d) 12 wrongly uses `3 * 4` in place of addition.

---

2. **Predict the output across a call boundary.** Confirmed shape in items 68–79: a function takes three integers, mutates them, and prints.

**2. (c) 5 10** — `LOCAL x` creates a separate variable inside `SHOW()`, so the top-level `x` keeps 10.

| Statement | x inside SHOW | x at top level | Printed |
|---|---|---|---|
| x = 10 | — | 10 | — |
| LOCAL x; x = 5 | 5 | 10 | 5 |
| PRINT x (after CALL) | — | 10 | 10 |

- (a) assumes the inner assignment overwrites the global.
- (b) ignores the `LOCAL x` declaration entirely.
- (d) reverses the execution order of the two `PRINT` statements.

---

3. **Scope and shadowing.** A local with the same name as a global; which value does each `print` see.

**3. (c) 3 13** — `n` is a value copy, so `a` stays 3 while the function returns 13.

| Step | n (local) | a | b |
|---|---|---|---|
| a = 3 | — | 3 | — |
| CALL CHANGE(3) | 3 → 13 | 3 | — |
| b = 13 | — | 3 | 13 |

- (a) reverses the printed order of `a` and `b`.
- (b) assumes by-value assignment modified `a`.
- (d) ignores the return value assigned to `b`.

---

4. **Array or object parameters.** The one genuinely subtle case — **mutating an element is visible to the caller, reassigning the whole parameter is not.**

**4. (b) 13** — `SQUARE(2) = 4` and `SQUARE(3) = 9`; the sum is 13.

| Call | n | n * n |
|---|---|---|
| SQUARE(2) | 2 | 4 |
| SQUARE(3) | 3 | 9 |

- (a) 25 is `SQUARE(5)`, not a sum of two calls.
- (d) 36 is `SQUARE(2 + 3)` evaluated as a single squared argument.
- (c) 10 is `4 + 6`, an arithmetic slip.

---

5. **Return semantics.** What a function returns when the `return` is inside a conditional that never fires.
## 3. Concept notes

**Function vs procedure.** A *function* is a named block that computes and **hands back a value** to the caller (`RETURN x`). A *procedure* is the same block that returns **nothing** (`RETURN` with no value, or falls off the end). In pseudocode MCQs both are written with `FUNCTION name(params)` … `END FUNCTION`.

**Signature, parameters, arguments.**
- **Signature** = the function's name plus its parameter list: `FUNCTION add(p, q)`.
- **Parameters** = the names inside the signature (`p`, `q`) — placeholders that exist only while the function runs.
- **Arguments** = the actual expressions supplied at the call site: in `add(3, m+1)`, the arguments are `3` and `m+1`.

**Call mechanics, step by step.**
1. The caller's **arguments are evaluated** left to right (`m+1` is computed now, not later).
2. A **new stack frame** (activation record) is pushed: it holds this call's parameters, its local variables, and the return address.
3. **Parameters are bound** to the argument values (by value) or to the caller's variables (by reference).
4. **The body runs.** Every local name lives in this frame only.
5. **The return value is handed back** to the call site (or nothing, for a procedure).

**5. (a) The function receives a copy, so changes to the parameter do not affect the caller's variable.** — By-value passing copies the argument into the parameter slot; the caller's original is isolated.

- (b) describes by-reference passing, not by-value.
- (c) is false: by-value parameters can be read as inputs normally.
- (d) is false: parameter names are independent of caller variable names.

---

6. **The frame is destroyed** and control resumes after the call.

Step 6 is *why* locals are local: a local variable's storage **ceases to exist** when the frame is popped. Nothing outside that frame can name it. This also explains why two recursive calls each have their own copy of a parameter — each call got its own frame (see the recursion topic).

**Pass by value.** The parameter receives a **copy** of the argument's value. Writing to the parameter changes only the copy inside the frame.

```
FUNCTION swap(x, y)
    temp = x
    x = y
    y = temp
    RETURN
END FUNCTION

a = 5
b = 9
swap(a, b)
PRINT a, " ", b
```

Trace:

| Step | Frame state | Caller state |
|---|---|---|
| evaluate arguments | — | a = 5, b = 9 |
| bind | x = 5, y = 9 | a = 5, b = 9 |
| temp = x | x = 5, y = 9, temp = 5 | a = 5, b = 9 |
| x = y | x = 9, y = 9, temp = 5 | a = 5, b = 9 |
| y = temp | x = 9, y = 5, temp = 5 | a = 5, b = 9 |
| frame destroyed | — | a = 5, b = 9 |

Output: `5 9`. **After a pass-by-value call the caller's `a` and `b` are UNCHANGED.** This is the single most examined fact in this topic — the swap silently did nothing useful.

**Pass by reference.** The parameter is an **alias** for the caller's variable — same storage, second name. Writing the parameter writes the caller's variable.

```
PROCEDURE swap(REF x, REF y)
    temp = x
    x = y
    y = temp
    RETURN
END PROCEDURE

a = 5
b = 9
swap(a, b)
PRINT a, " ", b
```

Trace:

| Step | Frame state | Caller state |
|---|---|---|
| bind | x → a, y → b (aliases) | a = 5, b = 9 |
| temp = x | temp = 5 | a = 5, b = 9 |
| x = y | — | a = 9, b = 9 |
| y = temp | — | a = 9, b = 5 |
| frame destroyed | — | a = 9, b = 5 |

Output: `9 5`. The swap worked, because `x` and `a` were never two different things.

**Comparison.**

| | Pass by value | Pass by reference |
|---|---|---|
| What is copied | the argument's value | nothing — parameter aliases the caller's variable |
| Caller sees writes to the parameter? | No | Yes |
| Cost for large data | copy of the whole value (expensive) | cost of a reference only |
| Typical | C, Java (primitives), Python (name binding) | C++ `int&`, Pascal `var`, C# `ref`/`out` |

**The middle case: an object, array or list passed "by value".** The *value* being copied is a **reference** (a pointer to the heap data), not the data itself. Result:
- Mutating the **contents** the parameter points at → **visible** to the caller.
- **Reassigning** the parameter to a new object/array → **not visible**; only the local copy of the reference changed.

*Example A — mutate an element (visible):*

```
FUNCTION bump(arr)
    arr[0] = arr[0] + 1
    RETURN
END FUNCTION

nums = [10, 20, 30]
bump(nums)
PRINT nums[0]
```

| Step | Inside frame | Caller `nums` |
|---|---|---|
| bind | arr → same list object as nums | [10, 20, 30] |
| arr[0] = arr[0] + 1 | arr → [11, 20, 30] | [11, 20, 30] |
| frame destroyed | — | [11, 20, 30] |

Output: `11`.

*Example B — reassign the whole array (not visible):*

```
FUNCTION reset(arr)
    arr = [0, 0, 0]
    RETURN
END FUNCTION

nums = [10, 20, 30]
reset(nums)
PRINT nums[0]
```

| Step | Inside frame | Caller `nums` |
|---|---|---|
| bind | arr → same list object as nums | [10, 20, 30] |
| arr = [0, 0, 0] | arr → new list [0, 0, 0] | [10, 20, 30] |
| frame destroyed | — | [10, 20, 30] |

Output: `10`. **Mutate yes, reassign no.**

**Scope kinds.**

| Kind | Where it lives | Visible from |
|---|---|---|
| Local | a variable declared inside a function body | that function only |
| Parameter | the signature's names | that call's body only |
| Global | declared at top level | the whole program, all functions |
| Block | declared inside `{ }`, `IF`, or a loop body | that block only |

**Shadowing worked example.** When a local has the same name as a global, the **innermost declaration wins** inside its scope. Here `local g` is declared explicitly:

```
g = 100
FUNCTION f()
    local g
    g = 7
    PRINT g
    RETURN
END FUNCTION

PRINT g
f()
PRINT g
```

| Statement | Which `g` | Value printed |
|---|---|---|
| `PRINT g` (top level) | global | 100 |
| `PRINT g` (inside f) | local, shadowing | 7 |
| `PRINT g` (top level) | global | 100 |

Output: `100`, `7`, `100`.

Watch the wording: if instead the function contains `global g` (or the pseudocode says every assignment to an undeclared name hits the global), the local never exists and the output is `100`, `7`, `7`. Read the declaration lines before answering.

**Lifetime vs scope.** *Scope* is **where the name can be written** — a compile-time, textual notion. *Lifetime* is **when the storage exists at runtime** — for an ordinary local, from frame push to frame pop. They usually coincide, but not always: a **static / persistent local** is scoped to the function but its lifetime is the whole program. It is initialised **once**, and it **survives frame destruction**.

```
FUNCTION counter()
    static n = 0
    n = n + 1
    RETURN n
END FUNCTION

PRINT counter()
PRINT counter()
PRINT counter()
```

Output: `1`, `2`, `3`. Without `static` — plain `n = 0` — it would print `1`, `1`, `1`, because the frame is destroyed each time.

**Why a function should not depend on globals.** A function that reads or writes a global can no longer be reasoned about from its signature alone: the same arguments can produce different results depending on program history, and hidden edits make bugs appear far from their cause. Passing what it needs in as parameters (and returning what it produces) keeps the function's behaviour fully determined by its call, which is also what makes recursion and testing tractable.

**Recursion and the call stack (three lines).**
- Each recursive call pushes its **own frame**, so each call has its own private copy of every parameter and local.
- The frames stack up until the **base case** is reached, then unwrap in **reverse order** of calls.
- No base case → frames are never popped → stack overflow. (Full treatment in the recursion topic.)

**Common traps.**

| Trap | What the MCQ does | Correct reading |
|---|---|---|
| Shadowing | local and global share a name | innermost declaration wins |
| Forgetting to return | function computes but no `RETURN`, caller prints the result variable | returns `0`/`NULL`/nothing — not the computed value |
| Return inside a loop | `RETURN` in the first iteration | loop exits immediately on the first hit |
| Modifying a parameter, expecting the caller to see it | swap-style function under pass by value | caller's variable is unchanged |
| Reassigning an array/object parameter | `arr = [...]` inside the function | caller still sees the old data |
| Mutating array/object contents | `arr[i] = ...` inside the function | caller **does** see the change |
| Static local mistaken for ordinary local | `static n = 0` inside a function | keeps its value across calls; printed values increase |

## 4. Must-memorise block

| Fact | Rule |
|---|---|
| Pass-by-value swap | Caller's variables are **UNCHANGED** after the call. Only the frame's parameters swapped. |
| Pass-by-reference swap | Caller's variables **do** change, because the parameters are aliases. |
| Reference copied by value | **Mutate the contents → caller sees it. Reassign the parameter → caller does NOT.** |
| Frame destruction | Popping the frame is what destroys locals and makes them local. |
| Static / persistent local | Initialised **once**; survives frame destruction; ordinary local re-initialises every call. |
| Return value | Handed back at the call site; a procedure returns nothing. |

**Scope resolution order** (search from the innermost outward, stop at the first match):
1. Block scope (innermost block containing the use)
2. Local variables of the enclosing function
3. Parameters of the enclosing function
4. Global variables
5. Not found → error / undefined

**Shadowing rule:** when two visible declarations share a name, the **innermost** one is used for every reference inside its scope; the outer one is invisible there and unchanged by writes to the inner one.

**Fast checks before answering:**
- Is the parameter list marked `REF` / `var` / `&`? → reference, caller changes.
- No marker, argument is a primitive? → copy, caller unchanged.
- No marker, argument is an array/object? → mutated contents visible, reassignment not.
- Name appears both outside and inside a function? → resolve innermost first.
- `static` in the declaration? → value persists across calls.
- `RETURN` before the loop ends? → only the first iteration happened.

## 5. Worked examples

### Example 1 — Swap under pass-by-value (caller unchanged)

```
1  FUNCTION Swap(BY VALUE x, BY VALUE y)
2      temp = x
3      x = y
4      y = temp
5  END FUNCTION
6
7  a = 10
8  b = 20
9  CALL Swap(a, b)
10 PRINT a, b
```

| Step | a (caller) | b (caller) | x (callee) | y (callee) |
|---|---|---|---|---|
| Before call | 10 | 20 | — | — |
| On entry | 10 | 20 | 10 | 20 |
| After line 2 | 10 | 20 | 10 | 20 |
| After line 3 | 10 | 20 | 20 | 20 |
| After line 4 | 10 | 20 | 20 | 10 |
| After return | 10 | 20 | — | — |

**Prints: 10 20** — caller variables are unchanged because parameters receive copies.

### Example 2 — Same swap under pass-by-reference (caller changed)

```
1  FUNCTION Swap(BY REFERENCE x, BY REFERENCE y)
2      temp = x
3      x = y
4      y = temp
5  END FUNCTION
6
7  a = 10
8  b = 20
9  CALL Swap(a, b)
10 PRINT a, b
```

| Step | a (caller) | b (caller) | x (callee alias) | y (callee alias) |
|---|---|---|---|---|
| Before call | 10 | 20 | — | — |
| On entry | 10 | 20 | 10 | 20 |
| After line 2 | 10 | 20 | 10 | 20 |
| After line 3 | 20 | 20 | 20 | 20 |
| After line 4 | 20 | 10 | 20 | 10 |
| After return | 20 | 10 | — | — |

**Prints: 20 10** — `x` and `y` are aliases for `a` and `b`, so assignments inside the function modify the caller.

### Example 3 — Array by value: mutating an element IS visible to caller

```
1  FUNCTION ChangeFirst(BY VALUE arr)
2      arr[0] = 99
3  END FUNCTION
4
5  A = [1, 2, 3]
6  CALL ChangeFirst(A)
7  PRINT A[0], A[1], A[2]
```

| Step | A (caller) | arr (callee) |
|---|---|---|
| Before call | [1, 2, 3] | — |
| On entry | [1, 2, 3] | points to same array |
| After line 2 | [99, 2, 3] | [99, 2, 3] |
| After return | [99, 2, 3] | — |

**Prints: 99 2 3** — pass-by-value copies the array reference, so element mutation affects the shared underlying array.

### Example 4 — Same array: REASSIGNING the parameter is NOT visible

```
1  FUNCTION Reassign(BY VALUE arr)
2      arr = [7, 8, 9]
3  END FUNCTION
4
5  A = [1, 2, 3]
6  CALL Reassign(A)
7  PRINT A[0], A[1], A[2]
```

| Step | A (caller) | arr (callee) |
|---|---|---|
| Before call | [1, 2, 3] | — |
| On entry | [1, 2, 3] | points to same array |
| After line 2 | [1, 2, 3] | points to new [7, 8, 9] |
| After return | [1, 2, 3] | — |

**Prints: 1 2 3** — reassigning the parameter rebinds only the local copy; the caller's array is unchanged.

### Example 5 — Global shadowed by local, prints before, inside and after

```
1  GLOBAL G = 5
2
3  FUNCTION Show()
4      LOCAL G = 10
5      PRINT G
6  END FUNCTION
7
8  PRINT G
9  CALL Show()
10 PRINT G
```

| Step | Global G (caller scope) | Local G (callee scope) |
|---|---|---|
| Before call (line 8) | 5 | not in scope |
| Inside function (line 5) | 5 (shadowed) | 10 |
| After return (line 10) | 5 | out of scope |

**Prints: 5, 10, 5** — line 8 prints global `G`; line 5 prints local `G`; line 10 prints global `G` again.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid |
|---|---|---|
| Expecting a value-swap to work | People assume assignments to parameters affect the caller; pass-by-value copies values into separate parameter slots. | Check the parameter mode. If `BY VALUE`, caller variables remain unchanged after the call. |
| Assuming arrays always behave like primitives | Arrays passed by value often copy the reference, so element mutation is visible, but reassigning the parameter is not. | Distinguish `arr[i] = x` (mutates shared element) from `arr = new` (rebinds local copy). Trace the reference. |
| Shadowing | A local variable with the same name as a global hides the global inside the function; prints inside show the local, prints outside show the global. | Use distinct names or explicitly track scope. In trace tables, keep separate columns for global and local variables. |
| Forgetting the return | A function that computes a value but does not return it leaves the caller's variable unchanged. | Always check for a `RETURN` statement and ensure the caller assigns the result: `x = f(...)`, not just `f(...)`. |
| Reading a local after the function returns | Locals are destroyed when the function exits; referring to them outside is a scope error or yields undefined/garbage. | Only access variables in the scope where they are declared. After return, use the returned value or caller variables. |
| Assuming parameter order does not matter | Parameters bind by position, not by name; swapping arguments silently changes behavior. | Match argument order to the parameter list. Write the call in the same order as the function signature. |
| Confusing pass-by-reference with pass-by-value for objects | Some pseudocode passes objects/arrays by reference by default, but primitives by value; mixing them up leads to wrong predictions. | Read the function header for `BY VALUE` / `BY REFERENCE` or any `&` marker. If absent, apply the exam's stated convention. |
| Ignoring that reassigning a by-reference parameter may break the alias | If a parameter is by reference and you assign it to a new object/array, the caller's variable may still point to the original depending on language rules. | Trace carefully. By-reference aliasing usually means direct assignment changes the caller, but reassigning to a new object may rebind only the local unless the convention says otherwise. |

## 7. Practice questions

**1.** **[Easy]** *(B5 — function definition and return)*

```
FUNCTION ADD(a, b)
    RETURN a + b
END FUNCTION
PRINT ADD(3, 4) * 2
```
(a) 14
(b) 7
(c) 24
(d) 12

**2.** **[Easy]** *(B5 — local vs global scope)*

```
x = 10
FUNCTION SHOW()
    LOCAL x
    x = 5
    PRINT x
END FUNCTION
CALL SHOW()
PRINT x
```
(a) 5 5
(b) 10 10
(c) 5 10
(d) 10 5

**3.** **[Easy]** *(B5 — pass by value)*

```
FUNCTION CHANGE(n)
    n = n + 10
    RETURN n
END FUNCTION
a = 3
b = CHANGE(a)
PRINT a, b
```
(a) 13 3
(b) 13 13
(c) 3 13
(d) 3 3

**4.** **[Easy]** *(B5 — return values in expressions)*

```
FUNCTION SQUARE(n)
    RETURN n * n
END FUNCTION
PRINT SQUARE(2) + SQUARE(3)
```
(a) 25
(b) 13
(c) 10
(d) 36

**5.** **[Easy]** *(B5 — parameter passing modes)*

In pseudocode, when a parameter is passed **by value**, which statement is true?

(a) The function receives a copy, so changes to the parameter do not affect the caller's variable.
(b) The function receives the caller's variable, so changes are visible to the caller.
(c) The parameter can be used only as an output, never as an input.
(d) The parameter name inside the function must match the caller's variable name.

**6.** **[Medium]** *(B5 — REF parameters)*

```
FUNCTION DOUBLE(REF x)
    x = x * 2
    RETURN x
END FUNCTION
a = 7
b = DOUBLE(a)
PRINT a, b
```
(a) 7 14
(b) 7 7
(c) 14 7
(d) 14 14

**6. (d) 14 14** — `x` is `REF`, so it aliases `a`; doubling it changes `a` to 14 and returns 14.

| Step | x (alias of a) | a | b |
|---|---|---|---|
| a = 7 | — | 7 | — |
| x = x * 2 | 14 | 14 | — |
| b = RETURN x | — | 14 | 14 |

- (a) treats `REF` as by-value, leaving `a` at 7.
- (c) reverses the printed order of `a` and `b`.
- (b) assumes neither variable is updated.

---

**7.** **[Medium]** *(B5 — swap with by-value parameters)*

```
FUNCTION SWAP(a, b)
    temp = a
    a = b
    b = temp
END FUNCTION
x = 1
y = 2
CALL SWAP(x, y)
PRINT x, y
```
(a) 2 1
(b) 1 1
(c) 2 2
(d) 1 2

**7. (d) 1 2** — both parameters are by value, so the swap happens on copies and `x`, `y` are unchanged.

| Step | a | b | temp | x | y |
|---|---|---|---|---|---|
| x = 1, y = 2 | — | — | — | 1 | 2 |
| temp = a | 1 | 2 | 1 | 1 | 2 |
| a = b | 2 | 2 | 1 | 1 | 2 |
| b = temp | 2 | 1 | 1 | 1 | 2 |

- (a) is the result only if both parameters were `REF`.
- (b) assumes `x` was changed but not `y`.
- (c) assigns the swapped copy values back to the caller.

---

**8.** **[Medium]** *(B5 — arrays and reference passing)*

```
// Arrays are passed by reference
FUNCTION MODIFY(arr)
    arr[2] = arr[2] + 100
END FUNCTION
nums = [5, 10, 15]
CALL MODIFY(nums)
PRINT nums[2]
```
(a) 5
(b) 110
(c) 105
(d) 10

**8. (b) 110** — arrays are passed by reference, so `arr[2]` (value 10) becomes 110 in the caller.

| Step | arr |
|---|---|
| initial | [5, 10, 15] |
| arr[2] = arr[2] + 100 | [5, 110, 15] |

- (a) 5 is `arr[1]`, an index-offset error.
- (d) 10 is the pre-modification value.
- (c) 105 wrongly adds 100 to `arr[1]` (5).

---

**9.** **[Medium]** *(B5 — loops inside functions)*

```
FUNCTION COUNT(n)
    total = 0
    FOR i = 1 TO n
        total = total + i
    NEXT i
    RETURN total
END FUNCTION
PRINT COUNT(4) + COUNT(2)
```
(a) 16
(b) 10
(c) 7
(d) 13

**9. (d) 13** — `COUNT(4) = 10` and `COUNT(2) = 3`; the sum is 13.

| Call | n | total after loop |
|---|---|---|
| COUNT(4) | 4 | 1 + 2 + 3 + 4 = 10 |
| COUNT(2) | 2 | 1 + 2 = 3 |

- (b) 10 is only the first call's value.
- (c) 7 is `4 + 3`, summing `n` rather than the series.
- (a) 16 wrongly uses `4 * 4` for the first call.

---

**10.** **[Medium]** *(B5 — GLOBAL declaration)*

```
g = 100
FUNCTION F()
    GLOBAL g
    g = 50
    RETURN g + 1
END FUNCTION
PRINT F()
PRINT g
```
(a) 50 50
(b) 101 50
(c) 51 100
(d) 51 50

**10. (d) 51 50** — `GLOBAL g` lets `F()` write 50 to the global, and the function returns `50 + 1 = 51`.

| Statement | g (global) | Value printed |
|---|---|---|
| g = 100 | 100 | — |
| GLOBAL g; g = 50 | 50 | — |
| PRINT F() | 50 | 51 |
| PRINT g | 50 | 50 |

- (a) ignores the returned `g + 1`.
- (c) treats `g` as a local copy, leaving the global at 100.
- (b) adds 1 to 100 instead of to the updated value.

---

**11.** **[Medium]** *(B5 — order of evaluation in nested calls)*

```
FUNCTION INC(x)
    PRINT "A"
    RETURN x + 1
END FUNCTION
FUNCTION DEC(x)
    PRINT "B"
    RETURN x - 1
END FUNCTION
PRINT INC(DEC(5))
```
(a) A B 5
(b) B A 5
(c) A B 6
(d) B A 6

**11. (b) B A 5** — `DEC(5)` runs first, printing B and returning 4; then `INC(4)` prints A and returns 5.

| Step | Output | Value |
|---|---|---|
| DEC(5) | B | 4 |
| INC(4) | A | 5 |
| PRINT INC(DEC(5)) | — | 5 |

- (a) reverses the nesting order of the two calls.
- (c) reverses the order and miscomputes `5 - 1 + 1`.
- (d) gives the right order but returns 6.

---

**12.** **[Medium]** *(B5 — recursion and return values)*

```
FUNCTION FACT(n)
    IF n <= 1 THEN
        RETURN 1
    END IF
    RETURN n * FACT(n - 1)
END FUNCTION
PRINT FACT(4)
```
(a) 10
(b) 12
(c) 4
(d) 24

**12. (d) 24** — 4 × 3 × 2 × 1 = 24, with the base case `n <= 1` returning 1.

| Call | n | Returns |
|---|---|---|
| FACT(1) | 1 | 1 |
| FACT(2) | 2 | 2 |
| FACT(3) | 3 | 6 |
| FACT(4) | 4 | 24 |

- (a) 10 is the sum 1 + 2 + 3 + 4, not the product.
- (b) 12 stops the recursion one level early.
- (c) 4 is the argument, not the result.

---

**13.** **[Hard]** *(B5 — mixing by-value and by-reference parameters)*

```
FUNCTION TEST(REF a, b)
    a = a + 1
    b = b + 1
    RETURN a + b
END FUNCTION
x = 5
y = 5
z = TEST(x, y)
PRINT x, y, z
```
(a) 6 5 12
(b) 5 5 10
(c) 6 6 12
(d) 5 6 11

**13. (a) 6 5 12** — `a` is `REF` so `x` becomes 6; `b` is by value so `y` stays 5, and the function returns `6 + 6 = 12`.

| Step | a (alias of x) | b (copy) | x | y | Return |
|---|---|---|---|---|---|
| x = 5, y = 5 | — | — | 5 | 5 | — |
| a = a + 1 | 6 | 5 | 6 | 5 | — |
| b = b + 1 | 6 | 6 | 6 | 5 | — |
| RETURN a + b | — | — | 6 | 5 | 12 |

- (b) treats both parameters as by value.
- (c) treats both parameters as by reference, changing `y` to 6.
- (d) swaps the passing modes between the two parameters.

---

**14.** **[Hard]** *(B5 — repeated reference swaps)*

```
FUNCTION SWAP(REF a, REF b)
    t = a
    a = b
    b = t
END FUNCTION
x = 10
y = 20
CALL SWAP(x, y)
CALL SWAP(x, y)
PRINT x - y
```
(a) 10
(b) -10
(c) 0
(d) 30

**14. (b) -10** — two reference swaps restore the originals, so `x = 10`, `y = 20`, and `10 - 20 = -10`.

| Step | x | y |
|---|---|---|
| initial | 10 | 20 |
| SWAP 1 | 20 | 10 |
| SWAP 2 | 10 | 20 |

- (a) 10 is `x` alone, ignoring the subtraction.
- (c) 0 assumes the swaps left `x` equal to `y`.
- (d) 30 is `x + y` instead of the difference.

---

**15.** **[Hard]** *(B5 — recursion with a non-unit step)*

```
FUNCTION MYST(n)
    IF n = 0 THEN
        RETURN 0
    END IF
    RETURN n + MYST(n - 2)
END FUNCTION
PRINT MYST(6)
```
(a) 21
(b) 6
(c) 12
(d) 20

**15. (c) 12** — the recursion adds 6 + 4 + 2 and stops at `MYST(0) = 0`, giving 12.

| Call | n | Returns |
|---|---|---|
| MYST(0) | 0 | 0 |
| MYST(2) | 2 | 2 + 0 = 2 |
| MYST(4) | 4 | 4 + 2 = 6 |
| MYST(6) | 6 | 6 + 6 = 12 |

- (a) 21 is the sum 1 + 2 + … + 6, ignoring the step of 2.
- (b) 6 is only the first addend.
- (d) 20 is 6 + 4 + 2 with an extra 8 accumulated.

---

**16.** **[Hard]** *(B5 — parameter shadowing names)*

```
FUNCTION CALC(base, REF extra)
    base = base + extra
    extra = extra + 1
    RETURN base
END FUNCTION
a = 2
b = 3
PRINT CALC(a, b)
PRINT a, b
```
(a) 5 then 2 3
(b) 8 then 3 4
(c) 5 then 2 4
(d) 5 then 3 4

**16. (c) 5 then 2 4** — `base` is a copy (`a` stays 2) while `extra` aliases `b`, which becomes 4; the function returns 5.

| Step | base | extra (alias of b) | a | b | Return |
|---|---|---|---|---|---|
| a = 2, b = 3 | — | — | 2 | 3 | — |
| base = base + extra | 5 | 3 | 2 | 3 | — |
| extra = extra + 1 | 5 | 4 | 2 | 4 | — |
| RETURN base | — | — | 2 | 4 | 5 |

- (a) ignores the `extra = extra + 1` update to `b`.
- (b) treats `base` as a reference and adds 3 twice.
- (d) treats `base` as a reference, changing `a` to 5.

---

**17.** **[Hard]** *(B5 — passing an array element by reference)*

```
FUNCTION ADDONE(REF v)
    v = v + 1
END FUNCTION
arr = [1, 2, 3]
CALL ADDONE(arr[2])
PRINT arr
```
(a) [1, 3, 3]
(b) [2, 3, 4]
(c) [1, 2, 3]
(d) [1, 2, 4]

**17. (a) [1, 3, 3]** — `arr[2]` is passed by reference, so the second element 2 becomes 3 in place.

| Step | arr |
|---|---|
| initial | [1, 2, 3] |
| ADDONE(arr[2]) → arr[2] = 3 | [1, 3, 3] |

- (b) increments every element instead of just `arr[2]`.
- (c) assumes the array is passed by value.
- (d) targets `arr[3]` (value 3) instead of `arr[2]`.

---

**18.** **[Hard]** *(B5 — print order inside recursion)*

```
FUNCTION F(n)
    IF n <= 0 THEN
        RETURN 1
    END IF
    PRINT n
    RETURN F(n - 1) + n
END FUNCTION
PRINT F(3)
```
(a) 3 2 1 7
(b) 1 2 3 7
(c) 3 2 1 6
(d) 7 3 2 1

---

**18. (a) 3 2 1 7** — each call prints `n` before recursing, so 3, 2, 1 are printed in that order, and the final result is 7.

| Call | Prints | Return |
|---|---|---|
| F(0) | — | 1 |
| F(1) | 1 | 1 + 1 = 2 |
| F(2) | 2 | 2 + 2 = 4 |
| F(3) | 3 | 4 + 3 = 7 |

- (b) prints in ascending order, which would need the `PRINT` after the recursive call.
- (c) returns 6, dropping the base-case 1.
- (d) prints the result before the descending values.

---
## 8. Resources

| Resource | Type | Link | Free/Paid | Time | Why this one |
|---|---|---|---|---|---|
| GfG — Parameter passing techniques | Article | https://www.geeksforgeeks.org/java/parameter-passing-techniques-in-java-with-examples/ | Free | 20 min | The swap example worked both ways, which is exactly the exam's archetype |
| GfG — Functions in programming | Article | https://www.geeksforgeeks.org/dsa/functions-in-programming/ | Free | 15 min | Call mechanics and the stack frame, language-agnostic |
| PrepInsta — Accenture pseudocode | Practice set | https://prepinsta.com/accenture/pseudo-code/general-pseudo-code/ | Free | 25 min | Function-based output prediction in the observed style |
| `topics/T31-B6-recursion.md` | Topic file | (this library) | Free | — | The call stack explained at length; read §3 there alongside this |
| `question-banks/QB-T35-B5-functions-scope.md` | Question bank | (this library) | Free | 20 min | 18 original questions, traces verified |

*Links verified resolving 2026-09-19.*

## 9. Self-check

- [ ] **I know a pass-by-value swap leaves the caller's variables unchanged**
- [ ] I can explain why, in terms of the stack frame
- [ ] I know pass-by-reference makes the same swap work
- [ ] **I know that for an array parameter, mutating an element IS visible but reassigning the parameter is NOT**
- [ ] I can trace a snippet where a local shadows a global
- [ ] I know the difference between scope and lifetime
- [ ] I can say what a function returns when its only `return` sits inside a branch that does not run
- [ ] I scored 14/18 or better on the practice questions

## 10. Sources

**Teaching content (§3–§9)** is adapted from `accenture-prep-final/accenture-prep-library/topics/T35-B5-functions-scope.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions O49 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `P7`). Confidence **Medium**. Nothing in this file is a published Infosys syllabus.
