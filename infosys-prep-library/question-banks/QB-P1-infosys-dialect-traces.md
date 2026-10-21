# QB-P1 — Loop and trace questions in the Infosys dialect

**Pseudocode** · **Tier 1** · 24 questions · topic file: see the `P1` file in `topics/`, `puzzles/`, `pseudocode/` or `interview/`

Generated for this library in the style of the observed Infosys items (`../data/gen_*.py`); an additional bank for the copied topic file. Every key was recomputed by a second route.

**How to use this bank.** Attempt every question before opening the key. Answer letters are balanced across a–d and not in a repeating pattern, so guessing the pattern will not help.

---

## Practice questions

**1.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer c, n
2) Set n = 388
3) Set c = 0
4) While (n > 1)
5)   n = n / 2
6)   c++
7) End-while
8) Print c
```

a) 9
b) 8
c) 10
d) 7

**2.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i, n, s
2) Set s = 0
3) Set n = 13
4) For (each i from 1 to n)
5)   If (i MOD 4 == 1) then
6)     s = s + i * 1
7)   End-if
8) End-for
9) Print s
```

a) 27
b) 30
c) 29
d) 28

**3.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 33 to 8 step -4)
4)   s = s + i
5) End-for
6) Print s
```

a) 148
b) 147
c) 149
d) 146

**4.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer c, i, j
2) Set c = 0
3) Set j = 0
4) For (each i from 1 to 3)
5)   For (each j from 1 to 3)
6)     If ((i + j) MOD 2 == 0) then
7)       c++
8)     End-if
9)   End-for
10) End-for
11) Print c
```

a) 7
b) 6
c) 5
d) 4

**5.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer c, n
2) Set n = 151
3) Set c = 0
4) While (n > 1)
5)   n = n / 2
6)   c++
7) End-while
8) Print c
```

a) 6
b) 9
c) 8
d) 7

**6.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i, n
2) Set n = 35
3) Set i = 0
4) While (n MOD 7 != 0)
5)   n = n + 3
6)   i++
7) End-while
8) n = n + i
9) Print n
```

a) 35
b) 37
c) 34
d) 36

**7.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer c, i, j
2) Set c = 0
3) Set j = 0
4) For (each i from 1 to 5)
5)   For (each j from 1 to 7)
6)     If ((i + j) MOD 2 == 0) then
7)       c++
8)     End-if
9)   End-for
10) End-for
11) Print c
```

a) 20
b) 19
c) 17
d) 18

**8.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer c, i, j
2) Set c = 0
3) Set j = 0
4) For (each i from 1 to 3)
5)   For (each j from 1 to 7)
6)     If ((i + j) MOD 2 == 0) then
7)       c++
8)     End-if
9)   End-for
10) End-for
11) Print c
```

a) 13
b) 12
c) 11
d) 10

**9.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer x
2) Set x = 1
3) Do
4)   x = x * 2
5)   Print x
6) While (x < 38)
```

a) 2 4 8 16 32 64
b) 65
c) 66
d) 63

**10.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer c, n
2) Set n = 549
3) Set c = 0
4) While (n > 1)
5)   n = n / 2
6)   c++
7) End-while
8) Print c
```

a) 10
b) 8
c) 9
d) 11

**11.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 37 to 5 step -3)
4)   s = s + i
5) End-for
6) Print s
```

a) 244
b) 242
c) 243
d) 241

**12.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i, n
2) Set n = 34
3) Set i = 0
4) While (n MOD 7 != 0)
5)   n = n + 3
6)   i++
7) End-while
8) n = n + i
9) Print n
```

a) 44
b) 55
c) 53
d) 54

**13.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer a, b
2) Set a = 58
3) Set b = 77
4) While (a != b)
5)   If (a > b) then
6)     a = a - b
7)   Else
8)     b = b - a
9)   End-if
10) End-while
11) Print a
```

a) 1
b) 2
c) 3
d) 0

**14.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i, n, s
2) Set s = 0
3) Set n = 9
4) For (each i from 1 to n)
5)   If (i MOD 2 == 0) then
6)     s = s + i * 3
7)   End-if
8) End-for
9) Print s
```

a) 75
b) 59
c) 60
d) 61

**15.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer c, i, j
2) Set c = 0
3) Set j = 0
4) For (each i from 1 to 4)
5)   For (each j from i to 4)
6)     If ((i + j) MOD 3 == 0) then
7)       c++
8)     End-if
9)   End-for
10) End-for
11) Print c
```

a) 3
b) 4
c) 5
d) 2

**16.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer c, n
2) Set n = 212
3) Set c = 0
4) While (n > 1)
5)   n = n / 2
6)   c++
7) End-while
8) Print c
```

a) 9
b) 7
c) 8
d) 6

**17.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 20 to 5 step -3)
4)   s = s + i
5) End-for
6) Print s
```

a) 75
b) 77
c) 76
d) 74

**18.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 1 to 9)
4)   If (i MOD 3 == 0) then
5)     continue
6)   End-if
7)   If (i > 6) then
8)     break
9)   End-if
10)   s = s + i
11) End-for
12) Print s
13) Print i
```

a) 6
b) 9
c) 8
d) 12 7

**19.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i, n, s
2) Set s = 0
3) Set n = 6
4) For (each i from 1 to n)
5)   If (i MOD 5 == 0) then
6)     s = s + i * 1
7)   End-if
8) End-for
9) Print s
```

a) 7
b) 4
c) 5
d) 6

**20.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i
2) For (each i from 4 to 15 step 2)
3)   If (i MOD 2 == 0) then
4)     Print i * 2
5)   End-if
6) End-for
```

a) 29
b) 27
c) 30
d) 8 12 16 20 24 28

**21.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer a, b
2) Set a = 73
3) Set b = 46
4) While (a != b)
5)   If (a > b) then
6)     a = a - b
7)   Else
8)     b = b - a
9)   End-if
10) End-while
11) Print a
```

a) 2
b) 3
c) 1
d) 0

**22.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 1 to 8)
4)   If (i MOD 2 == 0) then
5)     continue
6)   End-if
7)   If (i > 4) then
8)     break
9)   End-if
10)   s = s + i
11) End-for
12) Print s
13) Print i
```

a) 4
b) 4 5
c) 6
d) 6 6

**23.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer i, s
2) Set s = 0
3) For (each i from 29 to 7 step -2)
4)   s = s + i
5) End-for
6) Print s
```

a) 216
b) 218
c) 217
d) 215

**24.** **[Trace]** What is the output of the following pseudocode? (All variables are integers; `/` is integer division; `MOD` is the remainder.)

```text
1) Integer c, n
2) Set n = 808
3) Set c = 0
4) While (n > 1)
5)   n = n / 2
6)   c++
7) End-while
8) Print c
```

a) 10
b) 9
c) 11
d) 8

### ANSWER KEY

1. **b** — Trace it, recording the variables at the end of each pass:

| pass | c | n |
|---|---|---|
| 1 | 1 | 194 |
| 2 | 2 | 97 |
| 3 | 3 | 48 |
| 4 | 4 | 24 |
| 5 | 5 | 12 |
| 6 | 6 | 6 |
| 7 | 7 | 3 |

(… 1 more passes)

The program prints 8. Output: **8**.
2. **d** — Trace it, recording the variables at the end of each pass:

| pass | i | n | s |
|---|---|---|---|
| 1 | 1 | 13 | 1 |
| 2 | 2 | 13 | 1 |
| 3 | 3 | 13 | 1 |
| 4 | 4 | 13 | 1 |
| 5 | 5 | 13 | 6 |
| 6 | 6 | 13 | 6 |
| 7 | 7 | 13 | 6 |

(… 6 more passes)

The program prints 28. Output: **28**.
3. **b** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 33 | 33 |
| 2 | 29 | 62 |
| 3 | 25 | 87 |
| 4 | 21 | 108 |
| 5 | 17 | 125 |
| 6 | 13 | 138 |
| 7 | 9 | 147 |

The program prints 147. Output: **147**.
4. **c** — Trace it, recording the variables at the end of each pass:

| pass | c | i | j |
|---|---|---|---|
| 1 | 2 | 1 | 3 |
| 2 | 3 | 2 | 3 |
| 3 | 5 | 3 | 3 |

The program prints 5. Output: **5**.
5. **d** — Trace it, recording the variables at the end of each pass:

| pass | c | n |
|---|---|---|
| 1 | 1 | 75 |
| 2 | 2 | 37 |
| 3 | 3 | 18 |
| 4 | 4 | 9 |
| 5 | 5 | 4 |
| 6 | 6 | 2 |
| 7 | 7 | 1 |

The program prints 7. Output: **7**.
6. **a** — Trace it. The program prints 35. Output: **35**.
7. **d** — Trace it, recording the variables at the end of each pass:

| pass | c | i | j |
|---|---|---|---|
| 1 | 4 | 1 | 7 |
| 2 | 7 | 2 | 7 |
| 3 | 11 | 3 | 7 |
| 4 | 14 | 4 | 7 |
| 5 | 18 | 5 | 7 |

The program prints 18. Output: **18**.
8. **c** — Trace it, recording the variables at the end of each pass:

| pass | c | i | j |
|---|---|---|---|
| 1 | 4 | 1 | 7 |
| 2 | 7 | 2 | 7 |
| 3 | 11 | 3 | 7 |

The program prints 11. Output: **11**.
9. **a** — Trace it, recording the variables at the end of each pass:

| pass | x |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 6 | 64 |

The program prints 2, 4, 8, 16, 32, 64 in that order. Output: **2 4 8 16 32 64**.
10. **c** — Trace it, recording the variables at the end of each pass:

| pass | c | n |
|---|---|---|
| 1 | 1 | 274 |
| 2 | 2 | 137 |
| 3 | 3 | 68 |
| 4 | 4 | 34 |
| 5 | 5 | 17 |
| 6 | 6 | 8 |
| 7 | 7 | 4 |

(… 2 more passes)

The program prints 9. Output: **9**.
11. **b** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 37 | 37 |
| 2 | 34 | 71 |
| 3 | 31 | 102 |
| 4 | 28 | 130 |
| 5 | 25 | 155 |
| 6 | 22 | 177 |
| 7 | 19 | 196 |

(… 4 more passes)

The program prints 242. Output: **242**.
12. **d** — Trace it, recording the variables at the end of each pass:

| pass | i | n |
|---|---|---|
| 1 | 1 | 37 |
| 2 | 2 | 40 |
| 3 | 3 | 43 |
| 4 | 4 | 46 |
| 5 | 5 | 49 |

The program prints 54. Output: **54**.
13. **a** — Trace it, recording the variables at the end of each pass:

| pass | a | b |
|---|---|---|
| 1 | 58 | 19 |
| 2 | 39 | 19 |
| 3 | 20 | 19 |
| 4 | 1 | 19 |
| 5 | 1 | 18 |
| 6 | 1 | 17 |
| 7 | 1 | 16 |

(… 15 more passes)

The program prints 1. Output: **1**.
14. **c** — Trace it, recording the variables at the end of each pass:

| pass | i | n | s |
|---|---|---|---|
| 1 | 1 | 9 | 0 |
| 2 | 2 | 9 | 6 |
| 3 | 3 | 9 | 6 |
| 4 | 4 | 9 | 18 |
| 5 | 5 | 9 | 18 |
| 6 | 6 | 9 | 36 |
| 7 | 7 | 9 | 36 |

(… 2 more passes)

The program prints 60. Output: **60**.
15. **a** — Trace it, recording the variables at the end of each pass:

| pass | c | i | j |
|---|---|---|---|
| 1 | 1 | 1 | 4 |
| 2 | 2 | 2 | 4 |
| 3 | 3 | 3 | 4 |
| 4 | 3 | 4 | 4 |

The program prints 3. Output: **3**.
16. **b** — Trace it, recording the variables at the end of each pass:

| pass | c | n |
|---|---|---|
| 1 | 1 | 106 |
| 2 | 2 | 53 |
| 3 | 3 | 26 |
| 4 | 4 | 13 |
| 5 | 5 | 6 |
| 6 | 6 | 3 |
| 7 | 7 | 1 |

The program prints 7. Output: **7**.
17. **a** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 20 | 20 |
| 2 | 17 | 37 |
| 3 | 14 | 51 |
| 4 | 11 | 62 |
| 5 | 8 | 70 |
| 6 | 5 | 75 |

The program prints 75. Output: **75**.
18. **d** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 4 | 7 |
| 4 | 5 | 12 |

The program prints 12, 7 in that order. Output: **12 7**.
19. **c** — Trace it, recording the variables at the end of each pass:

| pass | i | n | s |
|---|---|---|---|
| 1 | 1 | 6 | 0 |
| 2 | 2 | 6 | 0 |
| 3 | 3 | 6 | 0 |
| 4 | 4 | 6 | 0 |
| 5 | 5 | 6 | 5 |
| 6 | 6 | 6 | 5 |

The program prints 5. Output: **5**.
20. **d** — Trace it, recording the variables at the end of each pass:

| pass | i |
|---|---|
| 1 | 4 |
| 2 | 6 |
| 3 | 8 |
| 4 | 10 |
| 5 | 12 |
| 6 | 14 |

The program prints 8, 12, 16, 20, 24, 28 in that order. Output: **8 12 16 20 24 28**.
21. **c** — Trace it, recording the variables at the end of each pass:

| pass | a | b |
|---|---|---|
| 1 | 27 | 46 |
| 2 | 27 | 19 |
| 3 | 8 | 19 |
| 4 | 8 | 11 |
| 5 | 8 | 3 |
| 6 | 5 | 3 |
| 7 | 2 | 3 |

(… 2 more passes)

The program prints 1. Output: **1**.
22. **b** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 3 | 4 |

The program prints 4, 5 in that order. Output: **4 5**.
23. **a** — Trace it, recording the variables at the end of each pass:

| pass | i | s |
|---|---|---|
| 1 | 29 | 29 |
| 2 | 27 | 56 |
| 3 | 25 | 81 |
| 4 | 23 | 104 |
| 5 | 21 | 125 |
| 6 | 19 | 144 |
| 7 | 17 | 161 |

(… 5 more passes)

The program prints 216. Output: **216**.
24. **b** — Trace it, recording the variables at the end of each pass:

| pass | c | n |
|---|---|---|
| 1 | 1 | 404 |
| 2 | 2 | 202 |
| 3 | 3 | 101 |
| 4 | 4 | 50 |
| 5 | 5 | 25 |
| 6 | 6 | 12 |
| 7 | 7 | 6 |

(… 2 more passes)

The program prints 9. Output: **9**.
