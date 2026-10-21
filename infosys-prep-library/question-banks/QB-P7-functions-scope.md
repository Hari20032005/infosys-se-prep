# QB-P7 — Functions — Scope and Pass by Value vs Reference

**Pseudocode** · **Tier 4** · 18 questions

Topic file: [`P7-functions-scope.md`](/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library/pseudocode/P7-functions-scope.md)

*Adapted from `accenture-prep-final/accenture-prep-library/question-banks/QB-T35-B5-functions-scope.md`; verified in that library's QA. Questions and answer key are unchanged.*

**How to use this bank.** Attempt every question before opening the key, at the real pace for this section (120 seconds a question). Answer letters are balanced across a–d.

---

**1.** **[Easy]** *(B5 — function definition and return)*

```
FUNCTION ADD(a, b)
    RETURN a + b
END FUNCTION
PRINT ADD(3, 4) * 2
```
(a) 12
(b) 7
(c) 24
(d) 14

**1. (d) 14** — `ADD(3, 4)` returns 7, and `7 * 2 = 14`.

| Call | a | b | RETURN | Printed |
|---|---|---|---|---|
| ADD(3, 4) | 3 | 4 | 7 | 7 * 2 = 14 |

- (b) 7 is the return value before the multiplication.
- (c) 24 wrongly applies the multiply inside the function.
- (a) 12 wrongly uses `3 * 4` in place of addition.

---

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
(a) 5 10
(b) 5 5
(c) 10 10
(d) 10 5

**2. (a) 5 10** — `LOCAL x` creates a separate variable inside `SHOW()`, so the top-level `x` keeps 10.

| Statement | x inside SHOW | x at top level | Printed |
|---|---|---|---|
| x = 10 | — | 10 | — |
| LOCAL x; x = 5 | 5 | 10 | 5 |
| PRINT x (after CALL) | — | 10 | 10 |

- (b) assumes the inner assignment overwrites the global.
- (c) ignores the `LOCAL x` declaration entirely.
- (d) reverses the execution order of the two `PRINT` statements.

---

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

**4. (b) 13** — `SQUARE(2) = 4` and `SQUARE(3) = 9`; the sum is 13.

| Call | n | n * n |
|---|---|---|
| SQUARE(2) | 2 | 4 |
| SQUARE(3) | 3 | 9 |

- (a) 25 is `SQUARE(5)`, not a sum of two calls.
- (d) 36 is `SQUARE(2 + 3)` evaluated as a single squared argument.
- (c) 10 is `4 + 6`, an arithmetic slip.

---

**5.** **[Easy]** *(B5 — parameter passing modes)*

In pseudocode, when a parameter is passed **by value**, which statement is true?

(a) The function receives the caller's variable, so changes are visible to the caller.
(b) The function receives a copy, so changes to the parameter do not affect the caller's variable.
(c) The parameter can be used only as an output, never as an input.
(d) The parameter name inside the function must match the caller's variable name.

**5. (b) The function receives a copy, so changes to the parameter do not affect the caller's variable.** — By-value passing copies the argument into the parameter slot; the caller's original is isolated.

- (a) describes by-reference passing, not by-value.
- (c) is false: by-value parameters can be read as inputs normally.
- (d) is false: parameter names are independent of caller variable names.

---

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
(b) 14 14
(c) 14 7
(d) 7 7

**6. (b) 14 14** — `x` is `REF`, so it aliases `a`; doubling it changes `a` to 14 and returns 14.

| Step | x (alias of a) | a | b |
|---|---|---|---|
| a = 7 | — | 7 | — |
| x = x * 2 | 14 | 14 | — |
| b = RETURN x | — | 14 | 14 |

- (a) treats `REF` as by-value, leaving `a` at 7.
- (c) reverses the printed order of `a` and `b`.
- (d) assumes neither variable is updated.

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
(b) 1 2
(c) 1 1
(d) 2 2

**7. (b) 1 2** — both parameters are by value, so the swap happens on copies and `x`, `y` are unchanged.

| Step | a | b | temp | x | y |
|---|---|---|---|---|---|
| x = 1, y = 2 | — | — | — | 1 | 2 |
| temp = a | 1 | 2 | 1 | 1 | 2 |
| a = b | 2 | 2 | 1 | 1 | 2 |
| b = temp | 2 | 1 | 1 | 1 | 2 |

- (a) is the result only if both parameters were `REF`.
- (c) assumes `x` was changed but not `y`.
- (d) assigns the swapped copy values back to the caller.

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
(b) 10
(c) 105
(d) 110

**8. (d) 110** — arrays are passed by reference, so `arr[2]` (value 10) becomes 110 in the caller.

| Step | arr |
|---|---|
| initial | [5, 10, 15] |
| arr[2] = arr[2] + 100 | [5, 110, 15] |

- (a) 5 is `arr[1]`, an index-offset error.
- (b) 10 is the pre-modification value.
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
(a) 13
(b) 10
(c) 7
(d) 16

**9. (a) 13** — `COUNT(4) = 10` and `COUNT(2) = 3`; the sum is 13.

| Call | n | total after loop |
|---|---|---|
| COUNT(4) | 4 | 1 + 2 + 3 + 4 = 10 |
| COUNT(2) | 2 | 1 + 2 = 3 |

- (b) 10 is only the first call's value.
- (c) 7 is `4 + 3`, summing `n` rather than the series.
- (d) 16 wrongly uses `4 * 4` for the first call.

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
(b) 51 50
(c) 51 100
(d) 101 50

**10. (b) 51 50** — `GLOBAL g` lets `F()` write 50 to the global, and the function returns `50 + 1 = 51`.

| Statement | g (global) | Value printed |
|---|---|---|
| g = 100 | 100 | — |
| GLOBAL g; g = 50 | 50 | — |
| PRINT F() | 50 | 51 |
| PRINT g | 50 | 50 |

- (a) ignores the returned `g + 1`.
- (c) treats `g` as a local copy, leaving the global at 100.
- (d) adds 1 to 100 instead of to the updated value.

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
(b) A B 6
(c) B A 6
(d) B A 5

**11. (d) B A 5** — `DEC(5)` runs first, printing B and returning 4; then `INC(4)` prints A and returns 5.

| Step | Output | Value |
|---|---|---|
| DEC(5) | B | 4 |
| INC(4) | A | 5 |
| PRINT INC(DEC(5)) | — | 5 |

- (a) reverses the nesting order of the two calls.
- (b) reverses the order and miscomputes `5 - 1 + 1`.
- (c) gives the right order but returns 6.

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
(b) 0
(c) -10
(d) 30

**14. (c) -10** — two reference swaps restore the originals, so `x = 10`, `y = 20`, and `10 - 20 = -10`.

| Step | x | y |
|---|---|---|
| initial | 10 | 20 |
| SWAP 1 | 20 | 10 |
| SWAP 2 | 10 | 20 |

- (a) 10 is `x` alone, ignoring the subtraction.
- (b) 0 assumes the swaps left `x` equal to `y`.
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
(a) 12
(b) 6
(c) 21
(d) 20

**15. (a) 12** — the recursion adds 6 + 4 + 2 and stops at `MYST(0) = 0`, giving 12.

| Call | n | Returns |
|---|---|---|
| MYST(0) | 0 | 0 |
| MYST(2) | 2 | 2 + 0 = 2 |
| MYST(4) | 4 | 4 + 2 = 6 |
| MYST(6) | 6 | 6 + 6 = 12 |

- (c) 21 is the sum 1 + 2 + … + 6, ignoring the step of 2.
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
(a) [1, 2, 3]
(b) [2, 3, 4]
(c) [1, 3, 3]
(d) [1, 2, 4]

**17. (c) [1, 3, 3]** — `arr[2]` is passed by reference, so the second element 2 becomes 3 in place.

| Step | arr |
|---|---|
| initial | [1, 2, 3] |
| ADDONE(arr[2]) → arr[2] = 3 | [1, 3, 3] |

- (b) increments every element instead of just `arr[2]`.
- (a) assumes the array is passed by value.
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
