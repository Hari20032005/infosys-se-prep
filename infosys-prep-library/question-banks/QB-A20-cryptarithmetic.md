# QB-A20 — Cryptarithmetic

**Reasoning Ability** · **Tier 4** · 8 questions · topic file: see the `A20` file in `topics/`, `puzzles/`, `pseudocode/` or `interview/`

Generated for this library from the rule families seen in the Infosys pool (`../data/gen_*.py`). Every key was recomputed by a second route; see `../research/04-qa-report.md`.

**How to use this bank.** Attempt every question before opening the key. Answer letters are balanced across a–d and not in a repeating pattern, so guessing the pattern will not help.

---

## Practice questions

**1.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  GA
× G
= AGG
```

What is the value of **G**?
a) 5
b) 3
c) 4
d) 8

**2.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  FC
+ FJ
= JCJ
```

What is the value of **C**?
a) 6
b) 8
c) 0
d) 3

**3.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  EG
+ GE
= IEI
```

What is the value of **I**?
a) 1
b) 3
c) 2
d) 0

**4.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  GB
× H
= BGK
```

What is the value of **K**?
a) 2
b) 8
c) 3
d) 5

**5.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  EE
+ GG
= GGA
```

What is the value of **G**?
a) 2
b) 1
c) 9
d) 3

**6.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  II
× I
= BIA
```

What is the value of **A**?
a) 5
b) 0
c) 3
d) 1

**7.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  CH
+ BB
= CLL
```

What is the value of **H**?
a) 2
b) 8
c) 5
d) 6

**8.** **[Cryptarithm]** In the cryptarithm below each letter stands for a different digit (the first letter of a number is not 0).

```text
  DK
+ DA
= AAL
```

What is the value of **L**?
a) 1
b) 0
c) 6
d) 8

### ANSWER KEY

1. **d** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is A = 6, G = 8 (that is 86 × 8 = 688). So G = **8**. A search over all assignments finds exactly one.
2. **c** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is C = 0, F = 5, J = 1 (that is 50 + 51 = 101). So C = **0**. A search over all assignments finds exactly one.
3. **a** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is E = 2, G = 9, I = 1 (that is 29 + 92 = 121). So I = **1**. A search over all assignments finds exactly one.
4. **c** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is B = 7, G = 8, H = 9, K = 3 (that is 87 × 9 = 783). So K = **3**. A search over all assignments finds exactly one.
5. **b** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is A = 0, E = 9, G = 1 (that is 99 + 11 = 110). So G = **1**. A search over all assignments finds exactly one.
6. **d** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is A = 1, B = 8, I = 9 (that is 99 × 9 = 891). So A = **1**. A search over all assignments finds exactly one.
7. **a** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is B = 8, C = 1, H = 2, L = 0 (that is 12 + 88 = 100). So H = **2**. A search over all assignments finds exactly one.
8. **b** — Solve column by column, starting from the units column and tracking carries. The only assignment that works is A = 1, D = 5, K = 9, L = 0 (that is 59 + 51 = 110). So L = **0**. A search over all assignments finds exactly one.
