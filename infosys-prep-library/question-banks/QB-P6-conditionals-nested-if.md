# QB-P6 — Conditionals and Branch Selection in Pseudocode

**Pseudocode** · **Tier 3** · 36 questions

Topic file: [`P6-conditionals-nested-if.md`](/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library/pseudocode/P6-conditionals-nested-if.md)

*Adapted from `accenture-prep-final/accenture-prep-library/question-banks/QB-T07-B2-conditionals-nested-if.md`; verified in that library's QA. Questions and answer key are unchanged.*

**How to use this bank.** Attempt every question before opening the key, at the real pace for this section (120 seconds a question). Answer letters are balanced across a–d.

---

**1.** **[Easy]** *(B2 — truthiness of non-zero integers)*

```
1.  SET x = 0
2.  SET y = 7
3.  IF x THEN
4.      PRINT "A"
5.  END IF
6.  IF y THEN
7.      PRINT "B"
8.  ELSE
9.      PRINT "C"
10. END IF
```

Each `PRINT` writes its own line. What is the output?

(a) B then C
(b) B
(c) C
(d) A

**1. (b) B**

`x` is 0, which is falsy, so line 4 never runs and nothing is printed for the first block. `y` is 7, which is truthy, so the `IF y` branch prints `B` and the `ELSE` is skipped.

| Line | x | y | Decision | Output |
|---|---|---|---|---|
| 1 | 0 | — | — | — |
| 2 | 0 | 7 | — | — |
| 3-5 | 0 | 7 | `IF x` false | — |
| 6 | 0 | 7 | `IF y` true | — |
| 7 | 0 | 7 | — | B |

- (a) Treats `IF x` as true. In this pseudocode a condition is true only when the value is non-zero.
- (c) Prints the `ELSE` arm of the second `IF`, which is unreachable because `y` is non-zero.
- (d) Assumes both the `IF` and the `ELSE` arm of a single `IF` can execute. Only one arm runs.

---

**2.** **[Easy]** *(B2 — dead code under a false guard)*

```
1.  SET a = 4
2.  SET b = 9
3.  SET c = 6
4.  IF a > b THEN
5.      c = c + 1
6.  END IF
7.  PRINT c
```

(a) 5
(b) 9
(c) 6
(d) 7

**2. (c) 6**

The guard `a > b` is `4 > 9`, which is false, so the body `c = c + 1` is dead code. `c` keeps its initial value of 6.

| Line | a | b | c | Decision |
|---|---|---|---|---|
| 1-3 | 4 | 9 | 6 | — |
| 4 | 4 | 9 | 6 | `4 > 9` false |
| 5 | 4 | 9 | 6 | skipped (dead code) |
| 7 | 4 | 9 | 6 | prints 6 |

- (a) Adds 1 to `c` as if the guard were true.
- (b) Prints `b` instead of `c`.
- (d) Subtracts 1 from `c`; the body is a `+1`, not a `-1`, and it does not run anyway.

---

**3.** **[Easy]** *(B2 — ordering in an if / else-if ladder)*

```
1.  SET n = 12
2.  IF n > 10 THEN
3.      PRINT "LARGE"
4.  ELSE IF n > 5 THEN
5.      PRINT "MEDIUM"
6.  ELSE
7.      PRINT "SMALL"
8.  END IF
```

(a) LARGE
(b) MEDIUM
(c) LARGE then MEDIUM
(d) SMALL

**3. (a) LARGE**

The ladder is evaluated top-down and the first true guard wins. `12 > 10` is true, so `LARGE` is printed and the remaining arms are not evaluated.

| Line | n | Guard | Result |
|---|---|---|---|
| 1 | 12 | — | — |
| 2 | 12 | `12 > 10` true | enter |
| 3 | 12 | — | prints LARGE |

- (b) `n > 5` is also true, but the `ELSE IF` is only reached when the first guard fails.
- (d) `SMALL` is the final `ELSE`, reached only when both guards fail.
- (d) Assumes every matching arm executes; an `else-if` ladder stops at the first match.

---

**4.** **[Easy]** *(B2 — truthiness of zero and of negative integers)*

```
1.  SET p = -3
2.  SET q = 0
3.  IF p THEN
4.      PRINT "P"
5.  END IF
6.  IF q THEN
7.      PRINT "Q"
8.  END IF
9.  IF NOT q THEN
10.     PRINT "R"
11. END IF
```

(a) P
(b) P then R
(c) P, Q, R
(d) Q then R

**4. (b) P then R**

`p = -3` is non-zero, so it is truthy and `P` prints. `q = 0` is falsy, so `Q` does not print; `NOT q` is therefore true and `R` prints.

| Line | p | q | Decision | Output |
|---|---|---|---|---|
| 1-2 | -3 | 0 | — | — |
| 3-5 | -3 | 0 | `IF p` true | P |
| 6-8 | -3 | 0 | `IF q` false | — |
| 9-11 | -3 | 0 | `NOT q` true | R |

- (a) Stops after the first block, ignoring the third `IF`.
- (a) Treats `q = 0` as truthy, which is the whole point of the truthiness rule.
- (a) Prints both `Q` and `R`, which is impossible since `IF q` and `IF NOT q` cannot both be true.

---

**5.** **[Medium]** *(B2 — outer guard true, inner guard false)*

```
1.  SET a = 8
2.  SET b = 3
3.  SET c = 5
4.  IF a > b THEN
5.      IF b > c THEN
6.          PRINT "INNER"
7.      ELSE
8.          PRINT "OUTER-ONLY"
9.      END IF
10. ELSE
11.     PRINT "NOTHING"
12. END IF
```

(a) INNER
(b) OUTER-ONLY
(c) NOTHING
(d) No output at all

**5. (b) OUTER-ONLY**

`a > b` is `8 > 3`, true, so the outer body is entered. The inner guard `b > c` is `3 > 5`, false, so the inner `ELSE` runs and prints `OUTER-ONLY`. The outer `ELSE` at line 10-11 is never reached.

| Line | a | b | c | Decision | Output |
|---|---|---|---|---|---|
| 1-3 | 8 | 3 | 5 | — | — |
| 4 | 8 | 3 | 5 | `8 > 3` true | — |
| 5 | 8 | 3 | 5 | `3 > 5` false | — |
| 8 | 8 | 3 | 5 | — | OUTER-ONLY |

- (a) Reads the inner guard as true; `3 > 5` is false.
- (c) Takes the outer `ELSE`, which requires `a > b` to be false.
- (d) The inner `ELSE` always prints something in this block.

---

**6.** **[Medium]** *(B2 — reassignment before a later condition reads the variable)*

```
1.  SET x = 4
2.  SET y = 4
3.  IF x >= y THEN
4.      x = x + 10
5.  END IF
6.  IF x = y THEN
7.      PRINT "EQUAL"
8.  ELSE
9.      PRINT "NOT EQUAL"
10. END IF
11. PRINT x
```

`PRINT` writes one value per line. What is the full output?

(a) EQUAL then 4
(b) NOT EQUAL then 4
(c) NOT EQUAL then 14
(d) EQUAL then 14

**6. (c) NOT EQUAL then 14**

`4 >= 4` is true, so line 4 runs and sets `x` to 14. The later test `x = y` is `14 = 4`, false, so `NOT EQUAL` prints. Line 11 then prints the current `x`, which is 14.

| Line | x | y | Decision | Output |
|---|---|---|---|---|
| 1-2 | 4 | 4 | — | — |
| 3-4 | 14 | 4 | `4 >= 4` true | — |
| 6 | 14 | 4 | `14 = 4` false | — |
| 9 | 14 | 4 | — | NOT EQUAL |
| 11 | 14 | 4 | — | 14 |

- (a) Uses the original `x = 4` at line 6 and again at line 11, forgetting the reassignment.
- (b) Correctly sees `x` became 14 but then treats `14 = 4` as true.
- (d) Uses the stale value of `x` for the print on line 11.

---

**7.** **[Medium]** *(B2 — the always-false identity comparison)*

```
1.  SET a = 2
2.  SET b = 5
3.  SET c = 7
4.  IF (a + b + c) > (c + b + a) THEN
5.      PRINT "TRUE-BRANCH"
6.  ELSE
7.      PRINT "FALSE-BRANCH"
8.  END IF
```

(a) FALSE-BRANCH
(b) TRUE-BRANCH
(c) TRUE-BRANCH then FALSE-BRANCH
(d) No output at all

**7. (a) FALSE-BRANCH**

Both sides sum to the same value: `2 + 5 + 7 = 14` and `7 + 5 + 2 = 14`. Addition is commutative, so `14 > 14` is false, the `ELSE` arm runs and prints `FALSE-BRANCH`.

| Line | a | b | c | LHS | RHS | Decision |
|---|---|---|---|---|---|---|
| 1-3 | 2 | 5 | 7 | — | — | — |
| 4 | 2 | 5 | 7 | 14 | 14 | `14 > 14` false |
| 7 | 2 | 5 | 7 | 14 | 14 | prints FALSE-BRANCH |

- (b) Reads the reversed sum as a different quantity; swapping the order of addition changes nothing.
- (c) Assumes both arms run; a single `IF / ELSE` executes exactly one arm.
- (d) The `ELSE` arm always prints here.

---

**8.** **[Medium]** *(B2 — nested guard plus truthiness of a reassigned integer)*

```
1.  SET a = 0
2.  SET b = 1
3.  IF b THEN
4.      a = 5
5.      IF a THEN
6.          b = 0
7.      END IF
8.  END IF
9.  PRINT a
10. PRINT b
```

(a) 0 then 1
(b) 5 then 1
(c) 0 then 0
(d) 5 then 0

**8. (d) 5 then 0**

`b = 1` is truthy, so `a` is set to 5. `a = 5` is truthy, so `b` is set to 0. The prints then output the final `a` and the final `b`.

| Line | a | b | Decision | Output |
|---|---|---|---|---|
| 1-2 | 0 | 1 | — | — |
| 3 | 0 | 1 | `IF b` true | — |
| 4 | 5 | 1 | — | — |
| 5 | 5 | 1 | `IF a` true | — |
| 6 | 5 | 0 | — | — |
| 9-10 | 5 | 0 | — | 5, 0 |

- (a) Ignores the nested block entirely.
- (b) Executes `a = 5` but not the inner `b = 0`.
- (c) Uses the initial `a = 0`, missing that line 4 overwrote it before the inner guard read it.

---

**9.** **[Medium]** *(B2 — else-if ladder combined with reassignment)*

```
1.  SET m = 10
2.  SET n = 4
3.  IF m > n THEN
4.      m = m - n
5.  ELSE IF m < n THEN
6.      n = n - m
7.  END IF
8.  IF m > n THEN
9.      PRINT "M"
10. ELSE
11.     PRINT "N"
12. END IF
```

(a) N
(b) M then N
(c) No output at all
(d) M

**9. (d) M**

`10 > 4` is true, so `m` becomes 6 and the `ELSE IF` is skipped. After the ladder, `m > n` is `6 > 4`, true, so `M` prints.

| Line | m | n | Decision | Output |
|---|---|---|---|---|
| 1-2 | 10 | 4 | — | — |
| 3-4 | 6 | 4 | `10 > 4` true | — |
| 5-6 | 6 | 4 | `ELSE IF` skipped | — |
| 8 | 6 | 4 | `6 > 4` true | M |

- (a) Takes the final `ELSE`, which requires `m <= n` after the ladder.
- (b) Assumes both branches of the ladder execute.
- (c) Both `IF` statements always produce a print here.

---

**10.** **[Medium]** *(B2 — truthiness of a computed zero)*

```
1.  SET k = 3
2.  SET flag = k - 3
3.  IF flag THEN
4.      PRINT "ON"
5.  ELSE
6.      PRINT "OFF"
7.  END IF
8.  IF k - 3 THEN
9.      PRINT "YES"
10. ELSE
11.     PRINT "NO"
12. END IF
```

(a) ON then NO
(b) ON then YES
(c) OFF then YES
(d) OFF then NO

**10. (d) OFF then NO**

`flag` is `3 - 3 = 0`, which is falsy, so the first block prints `OFF`. The second condition recomputes the same value, `0`, so it is also falsy and prints `NO`.

| Line | k | flag | Decision | Output |
|---|---|---|---|---|
| 1-2 | 3 | 0 | — | — |
| 3-6 | 3 | 0 | `IF flag` false | OFF |
| 8 | 3 | 0 | `3 - 3` is 0, false | — |
| 11 | 3 | 0 | — | NO |

- (b) Treats `0` as true in both blocks.
- (c) Mixes the two arms: the second block must also take its `ELSE`.
- (a) Treats `0` as true in the first block only.

---

**11.** **[Hard]** *(B2 — reassignment feeding an identity comparison)*

```
1.  SET a = 6
2.  SET b = 2
3.  SET c = 4
4.  IF a > b THEN
5.      c = a - b
6.      IF (a + b + c) > (c + b + a) THEN
7.          c = c + 1
8.      ELSE
9.          c = c - 1
10.     END IF
11. END IF
12. PRINT c
```

(a) 2
(b) 3
(c) 4
(d) 5

**11. (b) 3**

`6 > 2` is true, so `c` is set to `6 - 2 = 4`. The identity comparison `(6 + 2 + 4) > (4 + 2 + 6)` is `12 > 12`, false, so the `ELSE` runs and `c` becomes `4 - 1 = 3`.

| Line | a | b | c | LHS | RHS | Decision |
|---|---|---|---|---|---|---|
| 1-3 | 6 | 2 | 4 | — | — | — |
| 4 | 6 | 2 | 4 | — | — | `6 > 2` true |
| 5 | 6 | 2 | 4 | — | — | — |
| 6 | 6 | 2 | 4 | 12 | 12 | false |
| 9 | 6 | 2 | 3 | — | — | — |
| 12 | 6 | 2 | 3 | — | — | prints 3 |

- (d) Takes the `THEN` arm and increments `c` to 5.
- (d) Skips the inner block and leaves `c` at the value set on line 5.
- (a) Subtracts 2 somewhere; only 1 is subtracted.

---

**12.** **[Hard]** *(B2 — inner guard false because a computed value is zero)*

```
1.  SET x = 5
2.  SET y = 5
3.  SET z = 1
4.  IF x >= y THEN
5.      z = x - y
6.      IF z THEN
7.          PRINT "FIRST"
8.      ELSE
9.          PRINT "SECOND"
10.     END IF
11. ELSE
12.     PRINT "THIRD"
13. END IF
```

(a) FIRST
(b) THIRD
(c) No output at all
(d) SECOND

**12. (d) SECOND**

`5 >= 5` is true, so the outer body runs and sets `z = 5 - 5 = 0`. The inner guard `IF z` sees 0, which is falsy, so the inner `ELSE` prints `SECOND`.

| Line | x | y | z | Decision | Output |
|---|---|---|---|---|---|
| 1-3 | 5 | 5 | 1 | — | — |
| 4 | 5 | 5 | 1 | `5 >= 5` true | — |
| 5 | 5 | 5 | 0 | — | — |
| 6 | 5 | 5 | 0 | `IF z` false | — |
| 9 | 5 | 5 | 0 | — | SECOND |

- (a) Treats the inner `IF z` as true even though `z` is 0.
- (b) Takes the outer `ELSE`, which requires `x >= y` to be false.
- (c) The inner `ELSE` always prints in this block.

---

**13.** **[Hard]** *(B2 — dead code plus identity comparison plus equality test)*

```
1.  SET a = 3
2.  SET b = 8
3.  SET c = 3
4.  IF a > b THEN
5.      a = 100
6.  END IF
7.  IF (a + b + c) > (c + b + a) THEN
8.      b = 0
9.  END IF
10. IF a = c THEN
11.     PRINT "SAME"
12. ELSE
13.     PRINT "DIFFERENT"
14. END IF
15. PRINT a
```

(a) DIFFERENT then 3
(b) SAME then 100
(c) SAME then 3
(d) DIFFERENT then 100

**13. (c) SAME then 3**

`3 > 8` is false, so line 5 never runs and `a` stays 3. The identity comparison is `14 > 14`, false, so line 8 never runs and `b` stays 8. Finally `a = c` is `3 = 3`, true, so `SAME` prints and line 15 prints `a = 3`.

| Line | a | b | c | Decision | Output |
|---|---|---|---|---|---|
| 1-3 | 3 | 8 | 3 | — | — |
| 4-5 | 3 | 8 | 3 | `3 > 8` false, dead code | — |
| 7-8 | 3 | 8 | 3 | `14 > 14` false | — |
| 10-11 | 3 | 8 | 3 | `3 = 3` true | SAME |
| 15 | 3 | 8 | 3 | — | 3 |

- (a) Executes the dead `a = 100` and the dead `b = 0`.
- (b) Executes `a = 100` but correctly skips the identity-comparison body.
- (d) Correctly keeps `a = 3` but takes the `ELSE` arm at line 12.

---

**14.** **[Hard]** *(B2 — else-if chain inside a truthy outer guard)*

```
1.  SET p = 2
2.  SET q = 0
3.  SET r = 9
4.  IF p THEN
5.      q = p - 2
6.      IF q THEN
7.          r = 1
8.      ELSE IF p > 1 THEN
9.          r = 2
10.     ELSE
11.         r = 3
12.     END IF
13. END IF
14. PRINT q
15. PRINT r
```

(a) 0 then 9
(b) 0 then 1
(c) 2 then 2
(d) 0 then 2

**14. (d) 0 then 2**

`p = 2` is truthy, so the outer body runs and `q` becomes `2 - 2 = 0`. The inner `IF q` sees 0 and is false, so control moves to `ELSE IF p > 1`, i.e. `2 > 1`, true, setting `r = 2`. The prints show `q = 0` and `r = 2`.

| Line | p | q | r | Decision | Output |
|---|---|---|---|---|---|
| 1-3 | 2 | 0 | 9 | — | — |
| 4-5 | 2 | 0 | 9 | `IF p` true | — |
| 6 | 2 | 0 | 9 | `IF q` false | — |
| 8-9 | 2 | 0 | 2 | `2 > 1` true | — |
| 14-15 | 2 | 0 | 2 | — | 0, 2 |

- (a) Takes the first inner branch `r = 1`, which requires `q` to be truthy.
- (c) Prints `q`'s pre-assignment value of 2 instead of the value after line 5.
- (b) Prints `r`'s initial value of 9, taking no inner branch at all.

---

**15.** **[Hard]** *(B2 — equality branch of the identity comparison)*

```
1.  SET a = 1
2.  SET b = 2
3.  SET c = 3
4.  IF a + b + c > c + b + a THEN
5.      PRINT "GREATER"
6.  ELSE IF a + b + c = c + b + a THEN
7.      PRINT "EQUAL"
8.  ELSE
9.      PRINT "LESS"
10. END IF
11. c = a + b
12. IF c THEN
13.     PRINT c
14. END IF
```

(a) LESS then 3
(b) EQUAL then 1
(c) GREATER then 3
(d) EQUAL then 3

**15. (d) EQUAL then 3**

The first test `6 > 6` is false. The `ELSE IF` tests `6 = 6`, which is true, so `EQUAL` prints. Then `c` is set to `1 + 2 = 3`, which is non-zero, so the final `IF` prints `3`.

| Line | a | b | c | Decision | Output |
|---|---|---|---|---|---|
| 1-3 | 1 | 2 | 3 | — | — |
| 4 | 1 | 2 | 3 | `6 > 6` false | — |
| 6-7 | 1 | 2 | 3 | `6 = 6` true | EQUAL |
| 11 | 1 | 2 | 3 | — | — |
| 12-13 | 1 | 2 | 3 | `IF c` true | 3 |

- (a) Reads the reversed sum as strictly larger; the two sides are equal.
- (b) Correctly prints `EQUAL` but prints `c` from before line 11.
- (c) Takes the `ELSE` arm instead of the `ELSE IF`.

---

**16.** **[Hard]** *(B2 — sequential guards where an earlier write changes a later test)*

```
1.  SET x = 7
2.  SET y = 12
3.  IF x > 5 THEN
4.      x = x + 8
5.  END IF
6.  IF x > y THEN
7.      y = x
8.  ELSE
9.      x = x + 1
10. END IF
11. IF x > y THEN
12.     PRINT "X WINS"
13. ELSE IF x = y THEN
14.     PRINT "TIE"
15. ELSE
16.     PRINT "Y WINS"
17. END IF
```

(a) X WINS
(b) TIE
(c) Y WINS
(d) No output at all

**16. (b) TIE**

`x > 5` is `7 > 5`, true, so `x` becomes 15. Then `15 > 12` is true, so `y` becomes `x`, i.e. 15. The last ladder tests `x > y` as `15 > 15`, false, then `x = y` as `15 = 15`, true, printing `TIE`.

| Line | x | y | Decision | Output |
|---|---|---|---|---|
| 1-2 | 7 | 12 | — | — |
| 3-4 | 15 | 12 | `7 > 5` true | — |
| 6-7 | 15 | 15 | `15 > 12` true | — |
| 11 | 15 | 15 | `15 > 15` false | — |
| 13-14 | 15 | 15 | `15 = 15` true | TIE |

- (a) Takes the `THEN` arm of the last ladder without noticing `y` was set equal to `x`.
- (c) Takes the final `ELSE`, which requires `x < y`.
- (d) The last ladder always prints one of its three arms.

---

**17.** **[Hard]** *(B2 — switching to an else-if branch when the first guard is false)*

```
1.  SET a = 4
2.  SET b = 4
3.  SET c = 4
4.  IF a > b THEN
5.      c = 1
6.      IF a > c THEN
7.          c = 2
8.      END IF
9.  ELSE IF a = b THEN
10.     c = 10
11.     IF c > b THEN
12.         c = 20
13.     END IF
14. ELSE
15.     c = 30
16. END IF
17. PRINT c
```

(a) 20
(b) 10
(c) 2
(d) 30

**17. (a) 20**

`a > b` is `4 > 4`, false, so lines 5-8 are skipped entirely. The `ELSE IF a = b` is `4 = 4`, true, so `c` becomes 10. Then `c > b` is `10 > 4`, true, so `c` becomes 20.

| Line | a | b | c | Decision | Output |
|---|---|---|---|---|---|
| 1-3 | 4 | 4 | 4 | — | — |
| 4-8 | 4 | 4 | 4 | `4 > 4` false, dead code | — |
| 9-10 | 4 | 4 | 10 | `4 = 4` true | — |
| 11-12 | 4 | 4 | 20 | `10 > 4` true | — |
| 17 | 4 | 4 | 20 | — | 20 |

- (c) Enters the outer `THEN` and applies the nested `c = 2`.
- (b) Stops after `c = 10`, ignoring the nested `IF c > b`.
- (d) Takes the final `ELSE`, which requires `a = b` to be false.

---

**18.** **[Hard]** *(B2 — identity comparison first, truthiness second)*

```
1.  SET a = 5
2.  SET b = 5
3.  SET c = 0
4.  IF (a + b) > (b + a) THEN
5.      c = -1
6.  ELSE IF a >= b THEN
7.      c = 2
8.      IF c - 2 THEN
9.          c = 3
10.     END IF
11. ELSE
12.     c = 4
13. END IF
14. PRINT c
```

(a) 3
(b) 2
(c) 4
(d) -1

---

**18. (a) 2**

`(5 + 5) > (5 + 5)` is `10 > 10`, false. The `ELSE IF a >= b` is `5 >= 5`, true, so `c` becomes 2. The inner guard is `c - 2` = 0, falsy, so line 9 is skipped and `c` stays 2.

| Line | a | b | c | Decision | Output |
|---|---|---|---|---|---|
| 1-3 | 5 | 5 | 0 | — | — |
| 4 | 5 | 5 | 0 | `10 > 10` false | — |
| 6-7 | 5 | 5 | 2 | `5 >= 5` true | — |
| 8 | 5 | 5 | 2 | `c - 2` is 0, false | — |
| 14 | 5 | 5 | 2 | — | 2 |

- (b) Reads `c - 2` as true and executes `c = 3`, but 0 is falsy.
- (c) Takes the outer `ELSE`; `a >= b` is true, so the `ELSE` is unreachable.
- (d) Takes the first `THEN` arm even though the two sums are equal.

---

**19.** **[Easy]** *(B2 — truthiness of non-zero integers)*

In pseudocode, a condition is true when its value is non-zero. What is printed?

```
x = 0
y = -7
if (x) then
    print "A"
else
    if (y) then
        print "B"
    else
        print "C"
    end if
end if
```

(a) A
(b) Nothing is printed
(c) C
(d) B

**19. (d) B**
`x = 0` is falsy so the outer `if` fails; `y = -7` is non-zero so it is truthy and "B" prints.

| Variable | Value | Truthy? |
|---|---|---|
| x | 0 | No |
| y | -7 | Yes |

- (a) Assumes 0 is truthy — in pseudocode only non-zero is true.
- (c) Reached only if both `x` and `y` were falsy; `y = -7` is non-zero.
- (b) Something is always printed here because the `else` chain is exhaustive.

---

**20.** **[Easy]** *(B2 — false guard makes the body dead code)*

What is printed?

```
a = 5
b = 3
c = 8
if (a > b + c) then
    print "YES"
    print a + b + c
else
    print "NO"
end if
```

(a) YES then 16
(b) YES then 8
(c) NO
(d) Nothing is printed

**20. (c) NO**
`b + c = 11`, and `5 > 11` is false, so the whole `if` body is dead code and only "NO" prints.

| Variable | Value |
|---|---|
| a | 5 |
| b | 3 |
| c | 8 |
| b + c | 11 |

- (a) Assumes the guard passes and prints the sum 16.
- (b) Prints "YES" and misreads the sum as 8.
- (d) The `else` branch always prints "NO".

---

**21.** **[Easy]** *(B2 — outer-true-inner-false)*

What is printed?

```
p = 10
q = 4
r = 6
if (p > q) then
    if (p > r + q) then
        print "INNER"
    else
        print "OUTER"
    end if
else
    print "NONE"
end if
```

(a) INNER
(b) INNER then OUTER
(c) NONE
(d) OUTER

**21. (d) OUTER**
`p > q` is `10 > 4` true, so the inner `if` runs; `p > r + q` is `10 > 10` false, so "OUTER" prints.

| Variable | Value |
|---|---|
| p | 10 |
| q | 4 |
| r | 6 |
| r + q | 10 |

- (a) Treats `10 > 10` as true; it is false.
- (c) Reached only if `p > q` failed, but `10 > 4` is true.
- (b) Only one branch of a nested `if` executes.

---

**22.** **[Easy]** *(B2 — variable reassigned before a later condition reads it)*

What is printed?

```
m = 2
n = 9
m = m + 8
if (m > n) then
    print "BIG"
else
    print "SMALL"
end if
```

(a) BIG
(b) SMALL
(c) BIG then SMALL
(d) Nothing is printed

**22. (a) BIG**
`m` is reassigned to `2 + 8 = 10` before the test; `10 > 9` is true, so "BIG" prints.

| Variable | Value |
|---|---|
| m (initial) | 2 |
| n | 9 |
| m (after `m + 8`) | 10 |

- (b) Uses the stale `m = 2` and concludes `2 > 9` is false.
- (c) Only one branch executes.
- (d) The `else` branch always prints "SMALL".

---

**23.** **[Medium]** *(B2 — always-false identity comparison)*

What is printed?

```
a = 4
b = 7
c = 2
if (a + b + c) > (c + b + a) then
    print "LEFT"
else
    print "RIGHT"
end if
```

(a) LEFT
(b) LEFT then RIGHT
(c) RIGHT
(d) Nothing is printed

**23. (c) RIGHT**
`a + b + c` and `c + b + a` are the same sum, so the comparison is false and "RIGHT" prints.

| Expression | Value |
|---|---|
| a + b + c | 13 |
| c + b + a | 13 |

- (a) Assumes reordering changes the sum; addition is commutative.
- (b) Only one branch executes.
- (d) The `else` branch always prints "RIGHT".

---

**24.** **[Medium]** *(B2 — false guard makes the body dead code)*

What is printed?

```
x = 12
y = 5
z = 5
if (x < y) then
    z = z + 100
    print z
end if
print z
```

(a) 105
(b) 5
(c) 105 then 5
(d) 5 then 105

**24. (b) 5**
`12 < 5` is false, so `z = z + 100` never runs; `z` stays 5 and the final `print z` outputs 5.

| Variable | Value |
|---|---|
| x | 12 |
| y | 5 |
| z (initial) | 5 |
| z (final) | 5 |

- (a) Assumes the guard passes and prints 105.
- (c) Prints the dead-code value first.
- (d) Reverses the order of the two prints.

---

**25.** **[Medium]** *(B2 — outer-true-inner-false)*

What is printed?

```
a = 3
b = 3
c = 3
if (a >= b) then
    if (a > b) then
        print "STRICT"
    else
        print "EQUAL"
    end if
else
    print "LESS"
end if
```

(a) EQUAL
(b) STRICT
(c) LESS
(d) Nothing is printed

**25. (a) EQUAL**
`a >= b` is `3 >= 3` true, so the inner `if` runs; `a > b` is `3 > 3` false, so "EQUAL" prints.

| Variable | Value |
|---|---|
| a | 3 |
| b | 3 |
| c | 3 |

- (b) Treats `3 > 3` as true; it is false.
- (c) Reached only if `a >= b` failed, but it is true.
- (d) The inner `else` always prints "EQUAL".

---

**26.** **[Medium]** *(B2 — variable reassigned before a later condition reads it)*

What is printed?

```
k = 1
j = 1
k = k + j
j = k + j
if (k > j) then
    print "K"
else
    print "J"
end if
```

(a) K
(b) J
(c) K then J
(d) Nothing is printed

**26. (b) J**
`k = 1 + 1 = 2`, then `j = 2 + 1 = 3`; `2 > 3` is false, so "J" prints.

| Variable | Value |
|---|---|
| k (initial) | 1 |
| j (initial) | 1 |
| k (after `k + j`) | 2 |
| j (after `k + j`) | 3 |

- (a) Compares `k` against the stale `j = 1`.
- (c) Only one branch executes.
- (d) The `else` branch always prints "J".

---

**27.** **[Medium]** *(B2 — truthiness of non-zero integers)*

What is printed?

```
t = 3 - 3
u = 3 - 4
if (t) then
    print "T"
else
    if (u) then
        print "U"
    else
        print "V"
    end if
end if
```

(a) T
(b) V
(c) U
(d) Nothing is printed

**27. (c) U**
`t = 3 - 3 = 0`, which is falsy, so the outer `if (t)` fails and control passes to the `else`. `u = 3 - 4 = -1`, which is **non-zero and therefore truthy**, so the inner `if (u)` succeeds and **`U`** is printed.

| Variable | Value | Truthy? |
|---|---|---|
| `t` | 0 | No — 0 is the only falsy integer |
| `u` | −1 | **Yes** — truthiness means non-zero, not positive |

- (a) `T` requires `t` to be truthy, but `t` is exactly 0.
- (b) `V` is the inner `else`, reached only if `u` were also 0.
- (d) Something is always printed — every branch of this chain ends in a `print`.

---

**28.** **[Medium]** *(B2 — always-false identity comparison)*

What is printed?

```
a = 9
b = 1
c = 6
if (a + b + c) > (c + b + a) then
    print "GREATER"
else
    if (a + b + c) < (c + b + a) then
        print "LESSER"
    else
        print "EQUAL"
    end if
end if
```

(a) GREATER
(b) LESSER
(c) EQUAL
(d) Nothing is printed

**28. (c) EQUAL**
Both sums are 16, so `>` is false and `<` is false; the innermost `else` prints "EQUAL".

| Expression | Value |
|---|---|
| a + b + c | 16 |
| c + b + a | 16 |

- (a) Assumes reordering makes the left sum larger.
- (b) Assumes reordering makes the left sum smaller.
- (d) The final `else` always prints "EQUAL".

---

**29.** **[Hard]** *(B2 — false guard makes the body dead code)*

What is printed?

```
a = 6
b = 2
c = 3
if (a * b < c) then
    a = a + 1
    b = b + 1
    c = c + 1
end if
print a + b + c
```

(a) 14
(b) 11
(c) 12
(d) 9

**29. (b) 11**
`a * b = 12`, and `12 < 3` is false, so the body is dead code; `a + b + c = 6 + 2 + 3 = 11`.

| Variable | Value |
|---|---|
| a | 6 |
| b | 2 |
| c | 3 |
| a * b | 12 |

- (a) Assumes the guard passes and adds 1 to each variable.
- (c) Adds 1 to only one variable.
- (d) Miscalculates the sum as 9.

---

**30.** **[Hard]** *(B2 — outer-true-inner-false)*

What is printed?

```
x = 8
y = 8
z = 20
if (x + y <= z) then
    if (x + y < z) then
        print "UNDER"
    else
        print "EXACT"
    end if
else
    print "OVER"
end if
```

(a) UNDER
(b) Nothing is printed
(c) OVER
(d) EXACT

**30. (a) UNDER**
`x + y = 16` and `z = 20`. The outer guard `16 <= 20` is **true**, so the inner `if` is evaluated. The inner guard `16 < 20` is **also true**, so **`UNDER`** is printed.

| Expression | Value | Guard | Result |
|---|---|---|---|
| `x + y` | 16 | `16 <= 20` | true — enter |
| `x + y` | 16 | `16 < 20` | true — print `UNDER` |

- (b) Nothing printed: impossible — every path through this chain reaches a `print`.
- (c) `OVER` is the outer `else`, reached only if `x + y > z`.
- (d) `EXACT` is the inner `else`, reached only when `x + y == z` — that is, when the `<=` holds but the `<` does not. Here 16 is strictly less than 20, so the inner `if` succeeds.

---

**31.** **[Hard]** *(B2 — variable reassigned before a later condition reads it)*

What is printed?

```
a = 5
b = 2
c = 0
c = a - b
b = c - b
if (b > c) then
    print "B"
else
    if (b == c) then
        print "SAME"
    else
        print "C"
    end if
end if
```

(a) B
(b) SAME
(c) C
(d) Nothing is printed

**31. (c) C**
`c = 5 - 2 = 3`, then `b = 3 - 2 = 1`; `1 > 3` is false and `1 == 3` is false, so "C" prints.

| Variable | Value |
|---|---|
| a | 5 |
| b (initial) | 2 |
| c (after `a - b`) | 3 |
| b (after `c - b`) | 1 |

- (a) Compares `b` against the stale `c = 0`.
- (b) Assumes `b` and `c` end equal; they are 1 and 3.
- (d) The `else` chain always prints something.

---

**32.** **[Hard]** *(B2 — always-false identity comparison)*

What is printed?

```
a = 2
b = 5
c = 8
if (a + b + c) > (c + b + a) then
    print "X"
else
    if (a + b + c) == (c + b + a) then
        print "Y"
    else
        print "Z"
    end if
end if
```

(a) X
(b) Nothing is printed
(c) Z
(d) Y

**32. (d) Y**
Both sums are 15, so `>` is false; the inner test `==` is true, so "Y" prints.

| Expression | Value |
|---|---|
| a + b + c | 15 |
| c + b + a | 15 |

- (a) Assumes reordering makes the left sum larger.
- (c) Reached only if the sums were unequal; they are equal.
- (b) The `else` chain always prints something.

---

**33.** **[Hard]** *(B2 — truthiness of non-zero integers)*

What is printed?

```
a = 4
b = 4
c = 0
if (a - b) then
    print "P"
else
    if (a - b + c) then
        print "Q"
    else
        if (c) then
            print "R"
        else
            print "S"
        end if
    end if
end if
```

(a) P
(b) Q
(c) R
(d) S

**33. (d) S**
`a - b = 0` is falsy, so "P" is skipped; `a - b + c = 0` is falsy, so "Q" is skipped; `c = 0` is falsy, so "S" prints.

| Expression | Value | Truthy? |
|---|---|---|
| a - b | 0 | No |
| a - b + c | 0 | No |
| c | 0 | No |

- (a) Assumes `a - b = 0` is truthy.
- (b) Assumes `a - b + c` is non-zero; it is 0.
- (c) Assumes `c` is non-zero; it is 0.

---

**34.** **[Hard]** *(B2 — false guard makes the body dead code)*

What is printed?

```
a = 7
b = 7
c = 7
if (a > b) then
    c = c * 2
else
    if (b > c) then
        c = c * 3
    else
        c = c + 1
    end if
end if
print c
```

(a) 14
(b) 8
(c) 21
(d) 7

**34. (b) 8**
`a > b` is `7 > 7` false, so the first body is skipped; `b > c` is `7 > 7` false, so `c = c + 1 = 8`.

| Variable | Value |
|---|---|
| a | 7 |
| b | 7 |
| c (initial) | 7 |
| c (final) | 8 |

- (a) Assumes `a > b` is true and doubles `c`.
- (c) Assumes `b > c` is true and triples `c`.
- (d) Forgets the `c = c + 1` assignment.

---

**35.** **[Hard]** *(B2 — outer-true-inner-false)*

What is printed?

```
p = 15
q = 5
r = 5
if (p > q) then
    if (q > r) then
        print "FIRST"
    else
        if (p > q + r) then
            print "SECOND"
        else
            print "THIRD"
        end if
    end if
else
    print "FOURTH"
end if
```

(a) FIRST
(b) THIRD
(c) SECOND
(d) FOURTH

**35. (c) SECOND**
`p > q` is `15 > 5` true, so the inner `if` runs; `q > r` is `5 > 5` false, so the nested `if` runs; `p > q + r` is `15 > 10` true, so "SECOND" prints.

| Expression | Value |
|---|---|
| p | 15 |
| q | 5 |
| r | 5 |
| q + r | 10 |

- (a) Treats `5 > 5` as true.
- (b) Treats `15 > 10` as false.
- (d) Reached only if `p > q` failed, but it is true.

---

**36.** **[Hard]** *(B2 — variable reassigned before a later condition reads it)*

What is printed?

```
a = 10
b = 4
c = 6
a = b + c
b = a - b
if (a > b) then
    if (b > c) then
        print "ONE"
    else
        print "TWO"
    end if
else
    print "THREE"
end if
```

(a) TWO
(b) ONE
(c) THREE
(d) Nothing is printed

---

---

**36. (a) TWO**
`a = 4 + 6 = 10`, then `b = 10 - 4 = 6`; `10 > 6` is true, so the inner `if` runs; `6 > 6` is false, so "TWO" prints.

| Variable | Value |
|---|---|
| a (initial) | 10 |
| b (initial) | 4 |
| c | 6 |
| a (after `b + c`) | 10 |
| b (after `a - b`) | 6 |

- (b) Treats `6 > 6` as true.
- (c) Reached only if `a > b` failed, but `10 > 6` is true.
- (d) The inner `else` always prints "TWO".

---
