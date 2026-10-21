# QB-P4 — Increment operators

**Pseudocode** · **Tier 2** · 24 questions · topic file: see the `P4` file in `topics/`, `puzzles/`, `pseudocode/` or `interview/`

Generated for this library from the rule families seen in the Infosys pool (`../data/gen_*.py`). Every key was recomputed by a second route; see `../research/04-qa-report.md`.

**How to use this bank.** Attempt every question before opening the key. Answer letters are balanced across a–d and not in a repeating pattern, so guessing the pattern will not help.

---

## Practice questions

**1.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 4;
int result = --i - i;
print(result, i);
```

a) 2
b) 0
c) -1
d) 1

**2.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 4;
int result = i-- + i++;
print(result, i);
```

a) 6
b) 8
c) 7
d) 9

**3.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 3;
int result = i++ + i-- + i;
print(result, i);
```

a) 11 3
b) 3 10
c) 10 3
d) 9 3

**4.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 2;
int result = i++ - i++;
print(result, i);
```

a) -1 4
b) -1 2
c) 0 2
d) 0 4

**5.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 4;
int result = i-- + --i;
print(result, i);
```

a) 6 2
b) 5 2
c) 8 4
d) 7 2

**6.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 6;
int result = i - i++;
print(result, i);
```

a) -1 7
b) 0 7
c) 0 6
d) 1 7

**7.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 3;
int result = --i + i++;
print(result, i);
```

a) 3 4
b) 6 3
c) 5 3
d) 4 3

**8.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 4;
int result = i-- - ++i - i--;
print(result, i);
```

a) -2
b) -4
c) -3
d) -5

**9.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 7;
int result = i++ - i--;
print(result, i);
```

a) 0
b) 1
c) -2
d) -1

**10.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 6;
int result = i++ - --i + i--;
print(result, i);
```

a) 6 5
b) 7 5
c) 6 6
d) 5 5

**11.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 6;
int result = i-- + i++ + ++i;
print(result, i);
```

a) 18
b) 20
c) 17
d) 19

**12.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 4;
int result = i-- - --i;
print(result, i);
```

a) 1 2
b) 0 4
c) 2 2
d) 2 4

**13.** **[Increment operators]** What is the final value of `i` after this code runs?

```text
int i = 3;
int result = --i + i--;
print(result, i);
```

a) 1
b) 0
c) 3
d) 2

**14.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 7;
int result = i - i--;
print(result, i);
```

a) 1 6
b) 0 6
c) 0 7
d) 6 0

**15.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 6;
int result = ++i - i++;
print(result, i);
```

a) 1 8
b) 0 6
c) 0 8
d) -1 8

**16.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 5;
int result = i-- + i-- - i--;
print(result, i);
```

a) 6 5
b) 5 2
c) 6 2
d) 5 5

**17.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 2;
int result = ++i + i++ + i++;
print(result, i);
```

a) 9 5
b) 6 2
c) 12 5
d) 10 5

**18.** **[Increment operators]** What is the final value of `i` after this code runs?

```text
int i = 7;
int result = i++ + ++i;
print(result, i);
```

a) 10
b) 9
c) 8
d) 7

**19.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 4;
int result = --i - ++i;
print(result, i);
```

a) 1 4
b) 0 4
c) 4 -1
d) -1 4

**20.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 7;
int result = i-- - --i;
print(result, i);
```

a) 0 7
b) 2 5
c) 2 7
d) 1 5

**21.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 7;
int result = i-- - --i;
print(result, i);
```

a) 1
b) 0
c) 3
d) 2

**22.** **[Increment operators]** What is the value of `result` after this code runs? Java-style left-to-right evaluation.

```text
int i = 3;
int result = --i - i;
print(result, i);
```

a) 0
b) 2
c) -1
d) 1

**23.** **[Increment operators]** What is the final value of `i` after this code runs?

```text
int i = 4;
int result = i-- + i-- - i;
print(result, i);
```

a) 4
b) 1
c) 3
d) 2

**24.** **[Increment operators]** What does `print(result, i)` output?

```text
int i = 4;
int result = i++ - --i;
print(result, i);
```

a) 1 4
b) -1 4
c) 0 4
d) 4 0

### ANSWER KEY

1. **b** — `i` starts at 4. Evaluate left to right: `--i` makes i 3 then reads 3; `i` reads 3 → result = **0**, and `i` ends at 3.
2. **c** — `i` starts at 4. Evaluate left to right: `i--` reads 4 then i becomes 3; `i++` reads 3 then i becomes 4 → result = **7**, and `i` ends at 4.
3. **c** — Left to right: `i++` reads 3 then i becomes 4; `i--` reads 4 then i becomes 3; `i` reads 3. result = 10, i = 3 → **10 3**.
4. **a** — Left to right: `i++` reads 2 then i becomes 3; `i++` reads 3 then i becomes 4. result = -1, i = 4 → **-1 4**.
5. **a** — Left to right: `i--` reads 4 then i becomes 3; `--i` makes i 2 then reads 2. result = 6, i = 2 → **6 2**.
6. **b** — Left to right: `i` reads 6; `i++` reads 6 then i becomes 7. result = 0, i = 7 → **0 7**.
7. **d** — Left to right: `--i` makes i 2 then reads 2; `i++` reads 2 then i becomes 3. result = 4, i = 3 → **4 3**.
8. **b** — `i` starts at 4. Evaluate left to right: `i--` reads 4 then i becomes 3; `++i` makes i 4 then reads 4; `i--` reads 4 then i becomes 3 → result = **-4**, and `i` ends at 3.
9. **d** — `i` starts at 7. Evaluate left to right: `i++` reads 7 then i becomes 8; `i--` reads 8 then i becomes 7 → result = **-1**, and `i` ends at 7.
10. **a** — Left to right: `i++` reads 6 then i becomes 7; `--i` makes i 6 then reads 6; `i--` reads 6 then i becomes 5. result = 6, i = 5 → **6 5**.
11. **a** — `i` starts at 6. Evaluate left to right: `i--` reads 6 then i becomes 5; `i++` reads 5 then i becomes 6; `++i` makes i 7 then reads 7 → result = **18**, and `i` ends at 7.
12. **c** — Left to right: `i--` reads 4 then i becomes 3; `--i` makes i 2 then reads 2. result = 2, i = 2 → **2 2**.
13. **a** — Each `++`/`--` changes `i` once, wherever it sits: -2 in total, so `i` ends at 3 -2 = **1**. (result is 4.)
14. **b** — Left to right: `i` reads 7; `i--` reads 7 then i becomes 6. result = 0, i = 6 → **0 6**.
15. **c** — Left to right: `++i` makes i 7 then reads 7; `i++` reads 7 then i becomes 8. result = 0, i = 8 → **0 8**.
16. **c** — Left to right: `i--` reads 5 then i becomes 4; `i--` reads 4 then i becomes 3; `i--` reads 3 then i becomes 2. result = 6, i = 2 → **6 2**.
17. **d** — Left to right: `++i` makes i 3 then reads 3; `i++` reads 3 then i becomes 4; `i++` reads 4 then i becomes 5. result = 10, i = 5 → **10 5**.
18. **b** — Each `++`/`--` changes `i` once, wherever it sits: +2 in total, so `i` ends at 7 +2 = **9**. (result is 16.)
19. **d** — Left to right: `--i` makes i 3 then reads 3; `++i` makes i 4 then reads 4. result = -1, i = 4 → **-1 4**.
20. **b** — Left to right: `i--` reads 7 then i becomes 6; `--i` makes i 5 then reads 5. result = 2, i = 5 → **2 5**.
21. **d** — `i` starts at 7. Evaluate left to right: `i--` reads 7 then i becomes 6; `--i` makes i 5 then reads 5 → result = **2**, and `i` ends at 5.
22. **a** — `i` starts at 3. Evaluate left to right: `--i` makes i 2 then reads 2; `i` reads 2 → result = **0**, and `i` ends at 2.
23. **d** — Each `++`/`--` changes `i` once, wherever it sits: -2 in total, so `i` ends at 4 -2 = **2**. (result is 5.)
24. **c** — Left to right: `i++` reads 4 then i becomes 5; `--i` makes i 4 then reads 4. result = 0, i = 4 → **0 4**.
