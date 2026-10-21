# QB-P5 — Arrays — 1D and 2D Traversal and Indexing

**Pseudocode** · **Tier 2** · 36 questions

Topic file: [`P5-arrays.md`](/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library/pseudocode/P5-arrays.md)

*Adapted from `accenture-prep-final/accenture-prep-library/question-banks/QB-T15-B3-arrays-1d-2d.md`; verified in that library's QA. Questions and answer key are unchanged.*

**How to use this bank.** Attempt every question before opening the key, at the real pace for this section (120 seconds a question). Answer letters are balanced across a–d.

---

**1.** **[Easy]** *(B3 — 2D indexing, element access)*

```
Integer arr[2][2] = {{3, 5}, {7, 9}}    // all indices zero-based
Print arr[1][0] + arr[0][1]
```

(a) 12
(b) 10
(c) 14
(d) 16

**1. (a) 12**
Row 1 column 0 holds 7; row 0 column 1 holds 5; 7 + 5 = 12.

| i | j | arr[i][j] |
|---|---|---|
| 1 | 0 | 7 |
| 0 | 1 | 5 |

- (b) 10 reads `arr[0][0] + arr[1][0]` (3 + 7) or mixes up row/column order.
- (c) 14 comes from `arr[1][0] + arr[1][1]` (7 + 9), summing across the second row instead.
- (d) 16 comes from `arr[0][1] + arr[1][1]` (5 + 9) or from `arr[1][1] + arr[0][0]` plus an extra 2.

---

**2.** **[Easy]** *(B3 — 1D traversal, loop bounds)*

```
Integer a[5] = {1, 2, 3, 4, 5}
Integer sum = 0
for (i = 0; i <= 4; i = i + 1)
    sum = sum + a[i]
Print sum
```

(a) 10
(b) 12
(c) 15
(d) 20

**2. (c) 15**
`i` runs 0, 1, 2, 3, 4, so all five elements are added: 1 + 2 + 3 + 4 + 5 = 15.

| i | a[i] | sum |
|---|---|---|
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 6 |
| 3 | 4 | 10 |
| 4 | 5 | 15 |

- (a) 10 is the sum for `i < 4` (stops at index 3), a classic off-by-one.
- (b) 12 has no consistent loop range for this array.
- (d) 20 wrongly assumes the loop runs past index 4 and re-adds elements.

---

**3.** **[Easy]** *(B3 — 2D element summation)*

```
Integer arr[2][2] = {{6, 4}, {2, 8}}
Print arr[0][0] + arr[0][1] + arr[1][0] + arr[1][1]
```

(a) 16
(b) 18
(c) 20
(d) 22

**3. (c) 20**
6 + 4 + 2 + 8 = 20; each element is read exactly once.

| Expression | Value |
|---|---|
| arr[0][0] | 6 |
| arr[0][1] | 4 |
| arr[1][0] | 2 |
| arr[1][1] | 8 |

- (a) 16 omits the 4 at `arr[0][1]`.
- (b) 18 omits the 2 at `arr[1][0]`.
- (d) 22 has no valid combination of these four values.

---

**4.** **[Easy]** *(B3 — valid index range in 2D)*

```
Integer arr[2][3] = {{1, 2, 3}, {4, 5, 6}}
```

Which expression evaluates to the value `6`?

(a) `arr[2][1]`
(b) `arr[2][3]`
(c) `arr[1][2]`
(d) `arr[1][3]`

**4. (c) `arr[1][2]`**
Row index 1, column index 2 → second row, third column → the value 6.

- (b) `arr[2][3]` is doubly out of bounds: valid rows are 0–1 and valid columns are 0–2.
- (a) `arr[2][1]` is out of bounds on the row index.
- (d) `arr[1][3]` is out of bounds on the column index (columns stop at 2).

---

**5.** **[Medium]** *(B3 — bitwise AND in a nested loop)*

```
Integer arr[2][2] = {{1, 2}, {3, 4}}
Integer sum = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if ((arr[i][j] & 1) == 0)
            sum = sum + arr[i][j]
Print sum
```

(a) 10
(b) 6
(c) 4
(d) 3

**5. (b) 6**
The condition keeps only even elements: 2 and 4; 2 + 4 = 6.

| i | j | arr[i][j] | arr & 1 | sum |
|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 2 | 0 | 2 |
| 1 | 0 | 3 | 1 | 2 |
| 1 | 1 | 4 | 0 | 6 |

- (a) 10 sums all four elements and ignores the condition.
- (d) 3 sums the odd elements 1 + 3, i.e. the condition inverted.
- (c) 4 treats the traversal as ending after the single value 4 instead of accumulating.

---

**6.** **[Medium]** *(B3 — bitwise AND with a mask)*

```
Integer arr[2][2] = {{5, 2}, {3, 6}}
Integer s = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if ((arr[i][j] & 3) == 2)
            s = s + arr[i][j]
Print s
```

(a) 8
(b) 6
(c) 11
(d) 16

**6. (a) 8**
`x & 3` keeps the low two bits. 5 & 3 = 1, 2 & 3 = 2, 3 & 3 = 3, 6 & 3 = 2, so only 2 and 6 qualify: 2 + 6 = 8.

| i | j | arr[i][j] | arr & 3 | s |
|---|---|---|---|---|
| 0 | 0 | 5 | 1 | 0 |
| 0 | 1 | 2 | 2 | 2 |
| 1 | 0 | 3 | 3 | 2 |
| 1 | 1 | 6 | 2 | 8 |

- (b) 6 adds only the last qualifying element, forgetting the earlier 2.
- (c) 11 sums 5 + 6, treating the mask as a parity test.
- (d) 16 is 2 + 5 + 3 + 6, the sum of all elements with the condition ignored.

---

**7.** **[Medium]** *(B3 — 1D start index off-by-one)*

```
Integer a[5] = {4, 8, 12, 16, 20}
Integer s = 0
for (i = 1; i <= 4; i = i + 1)
    s = s + a[i]
Print s
```

(a) 40
(b) 60
(c) 56
(d) 24

**7. (c) 56**
The loop starts at index 1 and includes index 4, so it skips `a[0] = 4`: 8 + 12 + 16 + 20 = 56.

| i | a[i] | s |
|---|---|---|
| 1 | 8 | 8 |
| 2 | 12 | 20 |
| 3 | 16 | 36 |
| 4 | 20 | 56 |

- (b) 60 adds `a[0]`, i.e. starts the loop at 0.
- (a) 40 is 4 + 8 + 12 + 16, which stops one index too early.
- (d) 24 is 4 + 8 + 12, both starting at 0 and stopping early.

---

**8.** **[Medium]** *(B3 — column traversal in 2D)*

```
Integer arr[2][2] = {{2, 7}, {9, 4}}
Integer s = 0
for (i = 0; i < 2; i = i + 1)
    s = s + arr[i][1]
Print s
```

(a) 9
(b) 13
(c) 11
(d) 6

**8. (c) 11**
`arr[i][1]` fixes column 1 and walks the rows: 7 + 4 = 11.

| i | arr[i][1] | s |
|---|---|---|
| 0 | 7 | 7 |
| 1 | 4 | 11 |

- (a) 9 is 2 + 7, summing column 0 instead of column 1.
- (b) 13 is 9 + 4, summing the second row.
- (d) 6 is 2 + 4, summing the main diagonal.

---

**9.** **[Medium]** *(B3 — right shift inside a condition)*

```
Integer arr[2][2] = {{4, 5}, {6, 2}}
Integer s = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if ((arr[i][j] >> 1) == 2)
            s = s + 1
Print s
```

(a) 1
(b) 4
(c) 3
(d) 2

**9. (d) 2**
`x >> 1` is floor(x / 2). 4 >> 1 = 2 and 5 >> 1 = 2 qualify; 6 >> 1 = 3 and 2 >> 1 = 1 do not. Counter reaches 2.

| i | j | arr[i][j] | >> 1 | s |
|---|---|---|---|---|
| 0 | 0 | 4 | 2 | 1 |
| 0 | 1 | 5 | 2 | 2 |
| 1 | 0 | 6 | 3 | 2 |
| 1 | 1 | 2 | 1 | 2 |

- (a) 1 counts only 4 and wrongly rejects 5 >> 1 = 2.
- (c) 3 also accepts 6 >> 1, which is 3, not 2.
- (b) 4 ignores the condition entirely and counts every element.

---

**10.** **[Medium]** *(B3 — 1D traversal with a stride)*

```
Integer a[6] = {3, 6, 9, 12, 15, 18}
Integer s = 0
for (i = 0; i < 6; i = i + 2)
    s = s + a[i]
Print s
```

(a) 36
(b) 63
(c) 27
(d) 33

**10. (c) 27**
`i` takes the values 0, 2, 4: 3 + 9 + 15 = 27.

| i | a[i] | s |
|---|---|---|
| 0 | 3 | 3 |
| 2 | 9 | 12 |
| 4 | 15 | 27 |

- (a) 36 is 6 + 12 + 18, the odd-index elements, i.e. the stride starting at 1.
- (b) 63 is the sum of all six elements (3 + 6 + 9 + 12 + 15 + 18).
- (d) 33 is 3 + 6 + 9 + 15, an inconsistent subset.

---

**11.** **[Hard]** *(B3 — XOR on loop indices)*

```
Integer arr[2][2] = {{1, 3}, {5, 7}}
Integer s = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if ((i ^ j) == 1)
            s = s + arr[i][j]
Print s
```

(a) 6
(b) 10
(c) 4
(d) 8

**11. (d) 8**
`i ^ j == 1` for the two index pairs (0,1) and (1,0) only. These read 3 and 5: 3 + 5 = 8.

| i | j | i ^ j | arr[i][j] | s |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 3 | 3 |
| 1 | 0 | 1 | 5 | 8 |
| 1 | 1 | 0 | 7 | 8 |

- (a) 6 is 1 + 5, misreading the XOR test as `i == 0`.
- (b) 10 is 3 + 7, summing the second column.
- (c) 4 is 1 + 3, summing the first row.

---

**12.** **[Hard]** *(B3 — in-place modification then sum)*

```
Integer a[5] = {2, 4, 6, 8, 10}
Integer s = 0
for (i = 0; i < 5; i = i + 1)
    a[i] = a[i] / 2
    s = s + a[i]
Print s
```

(a) 5
(b) 30
(c) 10
(d) 15

**12. (d) 15**
Each element is halved before being added, so the array becomes {1, 2, 3, 4, 5} and the running sum is 15.

| i | a[i] before | a[i] after | s |
|---|---|---|---|
| 0 | 2 | 1 | 1 |
| 1 | 4 | 2 | 3 |
| 2 | 6 | 3 | 6 |
| 3 | 8 | 4 | 10 |
| 4 | 10 | 5 | 15 |

- (b) 30 sums the original values, ignoring the division.
- (c) 10 is the sum after the loop runs only up to `i < 4`.
- (a) 5 is the final value of `a[4]` alone, not the accumulated sum.

---

**13.** **[Hard]** *(B3 — mutation plus diagonal condition)*

```
Integer arr[2][2] = {{1, 2}, {3, 4}}
Integer s = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        arr[i][j] = arr[i][j] * 2
        if (i == j)
            s = s + arr[i][j]
Print s
```

(a) 10
(b) 4
(c) 20
(d) 6

**13. (a) 10**
Every element is doubled to {{2, 4}, {6, 8}}, but only the diagonal positions satisfy `i == j`: 2 + 8 = 10.

| i | j | arr[i][j] after ×2 | i == j | s |
|---|---|---|---|---|
| 0 | 0 | 2 | true | 2 |
| 0 | 1 | 4 | false | 2 |
| 1 | 0 | 6 | false | 2 |
| 1 | 1 | 8 | true | 10 |

- (b) 4 is 1 + 3, the diagonal before doubling.
- (c) 20 is 2 + 4 + 6 + 8, the sum of all elements after doubling.
- (d) 6 is 2 + 4, the first row after doubling instead of the diagonal.

---

**14.** **[Hard]** *(B3 — combined bitwise condition over 1D)*

```
Integer a[6] = {1, 2, 3, 4, 5, 6}
Integer s = 0
for (i = 0; i < 6; i = i + 1)
    if (((a[i] & 1) == 0) && ((i & 1) == 1))
        s = s + a[i]
Print s
```

(a) 12
(b) 9
(c) 6
(d) 21

**14. (a) 12**
Both parts must hold: the value must be even and the index must be odd. That happens at indices 1, 3, 5 with values 2, 4, 6: total 12.

| i | a[i] | a[i]&1 | i&1 | qualifies | s |
|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | no | 0 |
| 1 | 2 | 0 | 1 | yes | 2 |
| 2 | 3 | 1 | 0 | no | 2 |
| 3 | 4 | 0 | 1 | yes | 6 |
| 4 | 5 | 1 | 0 | no | 6 |
| 5 | 6 | 0 | 1 | yes | 12 |

- (c) 6 is 2 + 4, dropping the final qualifying element.
- (b) 9 is 1 + 3 + 5, summing the odd values instead of the even ones at odd indices.
- (d) 21 sums all six elements, ignoring the condition.

---

**15.** **[Hard]** *(B3 — OR with index, then mask)*

```
Integer arr[2][2] = {{3, 6}, {9, 12}}
Integer s = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if (((arr[i][j] | i) & 4) == 4)
            s = s + arr[i][j]
Print s
```

(a) 21
(b) 6
(c) 18
(d) 30

**15. (c) 18**
The mask `& 4` tests bit 2 (value 4). 3 | 0 = 3 → 3 & 4 = 0; 6 | 0 = 6 → 6 & 4 = 4 (pass); 9 | 1 = 9 → 9 & 4 = 0; 12 | 1 = 13 → 13 & 4 = 4 (pass). Total 6 + 12 = 18.

| i | j | arr[i][j] | arr \| i | & 4 | s |
|---|---|---|---|---|---|
| 0 | 0 | 3 | 3 | 0 | 0 |
| 0 | 1 | 6 | 6 | 4 | 6 |
| 1 | 0 | 9 | 9 | 0 | 6 |
| 1 | 1 | 12 | 13 | 4 | 18 |

- (b) 6 stops after the first qualifying element.
- (a) 21 is 9 + 12, the second row, or 3 + 6 + 12.
- (d) 30 is 3 + 6 + 9 + 12, the sum of all elements with the condition ignored.

---

**16.** **[Hard]** *(B3 — conditional index swap)*

```
Integer arr[2][2] = {{4, 1}, {6, 3}}
Integer s = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if (i < j)
            s = s + arr[i][j]
        else
            s = s + arr[j][i]
Print s
```

(a) 14
(b) 9
(c) 11
(d) 7

**16. (b) 9**
When `i < j` the code adds `arr[i][j]`, otherwise `arr[j][i]`. The four contributions are 4, 1, 1, 3 → 9.

| i | j | i < j | read | value | s |
|---|---|---|---|---|---|
| 0 | 0 | false | arr[0][0] | 4 | 4 |
| 0 | 1 | true | arr[0][1] | 1 | 5 |
| 1 | 0 | false | arr[0][1] | 1 | 6 |
| 1 | 1 | false | arr[1][1] | 3 | 9 |

- (a) 14 is 4 + 1 + 6 + 3, the sum of all four elements with the branch ignored.
- (d) 7 is 1 + 6, the anti-diagonal only.
- (c) 11 is 4 + 1 + 6, stopping before the final iteration.

---

**17.** **[Hard]** *(B3 — 1D loop start offset)*

```
Integer a[5] = {7, 14, 21, 28, 35}
Integer s = 0
for (i = 1; i < 5; i = i + 1)
    s = s + a[i]
Print s
```

(a) 105
(b) 98
(c) 70
(d) 84

**17. (b) 98**
The loop starts at index 1, so `a[0] = 7` is skipped: 14 + 21 + 28 + 35 = 98.

| i | a[i] | s |
|---|---|---|
| 1 | 14 | 14 |
| 2 | 21 | 35 |
| 3 | 28 | 63 |
| 4 | 35 | 98 |

- (a) 105 is 7 + 14 + 21 + 28 + 35, i.e. starting the loop at index 0.
- (c) 70 is 7 + 14 + 21 + 28, an early stop at index 3.
- (d) 84 is 21 + 28 + 35, i.e. starting the loop at index 2.

---

**18.** **[Hard]** *(B3 — bitwise AND with row index, swapped read)*

```
Integer arr[2][2] = {{6, 9}, {10, 15}}
Integer s = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if ((arr[i][j] & i) == 0)
            s = s + arr[j][i]
Print s
```

(a) 40
(b) 25
(c) 24
(d) 31

---

**18. (b) 25**
`arr[i][j] & i` is zero only when `i` is 0 (any value) or when the element has bit 0 clear. 6 & 0 = 0, 9 & 0 = 0, 10 & 1 = 0 pass; 15 & 1 = 1 fails. The code adds `arr[j][i]`: 6 + 10 + 9 = 25.

| i | j | arr[i][j] | arr[i][j] & i | added | s |
|---|---|---|---|---|---|
| 0 | 0 | 6 | 0 | arr[0][0] = 6 | 6 |
| 0 | 1 | 9 | 0 | arr[1][0] = 10 | 16 |
| 1 | 0 | 10 | 0 | arr[0][1] = 9 | 25 |
| 1 | 1 | 15 | 1 | — | 25 |

- (a) 40 is 6 + 9 + 10 + 15, the sum of all elements with the condition ignored.
- (c) 24 is 9 + 15, treating the test as odd-value detection (`x & 1`).
- (d) 31 is 6 + 10 + 15, the complement of the correct set.

---

**19.** **[Easy]** *(B3 — 1D array traversal with a step)*

```text
Integer arr[5] = {2, 4, 6, 8, 10}
Integer sum = 0
for (i = 0; i <= 4; i = i + 2)
    sum = sum + arr[i]
Print sum
```

What is printed?

(a) 12
(b) 30
(c) 20
(d) 18

---

**19. (d) 18**

The step is 2, so `i` takes the values 0, 2 and 4; the summed elements are `arr[0]=2`, `arr[2]=6`, `arr[4]=10`.

| i | arr[i] | sum |
|---|---|---|
| 0 | 2 | 2 |
| 2 | 6 | 8 |
| 4 | 10 | 18 |

- (a) Uses only the first two iterations (2 + 6 = 8) or adds `arr[1]` instead.
- (c) Adds exactly five terms of 4, ignoring the step 2.
- (b) Adds every element (2+4+6+8+10 = 30), i.e. treats the increment as 1.

---

**20.** **[Easy]** *(B3 — 1D indexing with an offset)*

```text
Integer arr[6] = {5, 10, 15, 20, 25, 30}
Print arr[3] + arr[0]
```

Indexing is zero-based. What is printed?

(a) 20
(b) 35
(c) 25
(d) 15

---

**20. (c) 25**

Zero-based indexing means `arr[0]=5`, `arr[1]=10`, `arr[2]=15`, `arr[3]=20`, so 20 + 5 = 25.

- (a) Counts from 1 and reads `arr[3]` as the third element (15), then adds 5.
- (b) Counts from 1 and reads `arr[3]` as 20 + 15.
- (d) Returns `arr[2]` (15) instead of `arr[3]`.

---

**21.** **[Easy]** *(B3 — 2D indexing, row then column)*

```text
Integer arr[2][2] = {{3, 5}, {7, 9}}
Print arr[1][0] + arr[0][1]
```

Both dimensions are zero-based. What is printed?

(a) 16
(b) 10
(c) 14
(d) 12

---

**21. (d) 12**

`arr[1][0]` is row 1, column 0 of the initialiser, i.e. 7; `arr[0][1]` is 5. 7 + 5 = 12.

- (b) Swaps the two subscripts and picks `arr[0][1]=5` with `arr[1][1]=9`, then mis-adds.
- (c) Adds the first row (3 + 5 = 8) plus something, or picks 7 + 7.
- (a) Adds 7 + 9 (column 1 entirely) rather than the two requested cells.

---

**22.** **[Easy]** *(B3 — loop iteration count on a 1D array)*

```text
Integer arr[7] = {1, 2, 3, 4, 5, 6, 7}
Integer count = 0
for (i = 0; i < 7; i = i + 3)
    count = count + 1
Print count
```

What is printed?

(a) 3
(b) 4
(c) 2
(d) 7

---

**22. (a) 3**

The loop starts at `i = 0` and adds 3 each time: 0, 3, 6 are all less than 7, and 9 is not.

| i | i < 7 | count |
|---|---|---|
| 0 | true | 1 |
| 3 | true | 2 |
| 6 | true | 3 |
| 9 | false | 3 |

- (c) Divides 7 by 3 and truncates, ignoring that i = 0 counts as one iteration.
- (b) Counts i = 0, 3, 6, 9 and wrongly accepts i = 9.
- (d) Assumes the loop touches every element (increment 1).

---

**23.** **[Medium]** *(B3 — full 2D traversal)*

```text
Integer arr[2][2] = {{4, 6}, {8, 10}}
Integer sum = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        sum = sum + arr[i][j]
Print sum
```

What is printed?

(a) 28
(b) 24
(c) 18
(d) 14

---

**23. (a) 28**

The nested loops visit all four cells: 4 + 6 + 8 + 10 = 28.

| i | j | arr[i][j] | sum |
|---|---|---|---|
| 0 | 0 | 4 | 4 |
| 0 | 1 | 6 | 10 |
| 1 | 0 | 8 | 18 |
| 1 | 1 | 10 | 28 |

- (c) Sums only the first row plus the first column (4+6+8 = 18).
- (b) Drops the last element (4+6+8 = 18) or sums 4+10+10.
- (d) Adds only the first row (4 + 6 = 10) and part of the second.

---

**24.** **[Medium]** *(B3 — bitwise AND in the condition)*

```text
Integer arr[2][2] = {{3, 6}, {5, 4}}
Integer sum = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if ((arr[i][j] & 1) == 0)
            sum = sum + arr[i][j]
Print sum
```

What is printed?

(a) 8
(b) 10
(c) 14
(d) 18

---

**24. (b) 10**

`arr[i][j] & 1` is 0 only for even values, so only 6 and 4 are added.

| i | j | val | val & 1 | sum |
|---|---|---|---|---|
| 0 | 0 | 3 | 1 | 0 |
| 0 | 1 | 6 | 0 | 6 |
| 1 | 0 | 5 | 1 | 6 |
| 1 | 1 | 4 | 0 | 10 |

- (a) Adds 3 + 5 = 8, i.e. keeps the odd values instead of the even ones.
- (c) Adds 3 + 5 + 6 (mis-evaluates `3 & 1` as 0).
- (d) Sums everything (28) or sums everything except 4.

---

**25.** **[Medium]** *(B3 — XOR accumulation over a 1D array)*

```text
Integer arr[4] = {7, 3, 5, 6}
Integer r = 0
for (i = 0; i < 4; i = i + 1)
    r = r XOR arr[i]
Print r
```

What is printed?

(a) 7
(b) 5
(c) 6
(d) 1

---

**25. (a) 7**

XOR is applied left to right and the order does not change the result: 7 ^ 3 ^ 5 ^ 6 = 7.

| i | arr[i] | r |
|---|---|---|
| 0 | 7 | 7 |
| 1 | 3 | 4 |
| 2 | 5 | 1 |
| 3 | 6 | 7 |

- (d) Stops one step early and reports the running value 1.
- (b) Returns the value 5 because it treats XOR as addition of bits modulo something else.
- (c) Returns the raw last element 6 instead of accumulating.

---

**26.** **[Medium]** *(B3 — diagonal access arr[i][i])*

```text
Integer arr[2][2] = {{2, 9}, {4, 7}}
Integer sum = 0
for (i = 0; i < 2; i = i + 1)
    sum = sum + arr[i][i]
Print sum
```

What is printed?

(a) 6
(b) 9
(c) 11
(d) 13

---

**26. (b) 9**

`arr[i][i]` picks the main diagonal: `arr[0][0]=2` and `arr[1][1]=7`, giving 9.

| i | arr[i][i] | sum |
|---|---|---|
| 0 | 2 | 2 |
| 1 | 7 | 9 |

- (a) Adds `arr[0][0]` and `arr[0][1]` (2 + 9 = 11) — wrong order of subscripts.
- (c) Adds 2 + 9 (first row) instead of the diagonal.
- (d) Adds 9 + 4 (the anti-diagonal) instead of the main diagonal.

---

**27.** **[Medium]** *(B3 — off-by-one loop bound)*

```text
Integer arr[5] = {10, 20, 30, 40, 50}
Integer sum = 0
for (i = 0; i <= 5; i = i + 1)
    sum = sum + arr[i]
```

The array is declared with size 5 and indices run from 0 to 4. What happens when this code runs?

(a) The loop body executes 4 times because `i <= 5` is never reached.
(b) The loop body executes 5 times and sums every element of the array.
(c) The loop body executes 6 times and `arr[5]` automatically holds the value 0, so the sum is 150.
(d) The loop body executes 6 times; the last iteration reads `arr[5]`, which is outside the declared bounds.

---

**27. (d) The loop body executes 6 times; the last iteration reads `arr[5]`, which is outside the declared bounds.**

`i` runs 0, 1, 2, 3, 4, 5 — six values. Valid indices are 0 to 4, so the sixth access is out of range.

| i | i <= 5 | access |
|---|---|---|
| 0–4 | true | arr[0] … arr[4] — valid |
| 5 | true | arr[5] — out of bounds |
| 6 | false | loop ends |

- (b) Ignores that `<=` allows `i = 5`, so the loop runs six times, not five.
- (c) Invents a guarantee that out-of-range memory holds 0; nothing in the declaration says that.
- (a) Reverses the loop logic — `i = 0` satisfies `i <= 5` immediately.

---

**28.** **[Medium]** *(B3 — bitwise OR in the condition)*

```text
Integer arr[2][2] = {{1, 2}, {4, 8}}
Integer sum = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if ((arr[i][j] OR 4) == 4)
            sum = sum + arr[i][j]
Print sum
```

What is printed?

(a) 4
(b) 7
(c) 6
(d) 15

---

**28. (a) 4**

`x OR 4 == 4` is true only when `x` has no bits outside the bit pattern of 4 (binary 100). Among 1, 2, 4, 8 only 4 qualifies.

| i | j | val | val OR 4 | sum |
|---|---|---|---|---|
| 0 | 0 | 1 | 5 | 0 |
| 0 | 1 | 2 | 6 | 0 |
| 1 | 0 | 4 | 4 | 4 |
| 1 | 1 | 8 | 12 | 4 |

- (d) Adds every element (1+2+4+8 = 15), ignoring the condition.
- (b) Adds 1 + 2 + 4 = 7.
- (c) Treats the condition as always true except for one value.

---

**29.** **[Hard]** *(B3 — bitmask test `& 4` selecting elements)*

```text
Integer arr[2][2] = {{6, 9}, {12, 3}}
Integer sum = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if ((arr[i][j] & 4) == 4)
            sum = sum + arr[i][j]
Print sum
```

What is printed?

(a) 12
(b) 27
(c) 15
(d) 18

---

**29. (d) 18**

The mask `& 4` tests bit 2 (value 4). 6 (110) and 12 (1100) both have it set; 9 (1001) and 3 (0011) do not.

| i | j | val | val & 4 | sum |
|---|---|---|---|---|
| 0 | 0 | 6 | 4 | 6 |
| 0 | 1 | 9 | 0 | 6 |
| 1 | 0 | 12 | 4 | 18 |
| 1 | 1 | 3 | 0 | 18 |

- (a) Adds only 12, missing the 6.
- (c) Adds 6 + 9 = 15.
- (b) Adds everything (6+9+12+3 = 30) minus a rounding, i.e. drops the condition.

---

**30.** **[Hard]** *(B3 — swapped indices arr[j][i] behind a condition)*

```text
Integer arr[2][2] = {{2, 5}, {8, 3}}
Integer sum = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if (i > j)
            sum = sum + arr[j][i]
Print sum
```

What is printed?

(a) 8
(b) 5
(c) 13
(d) 0

---

**30. (b) 5**

`i > j` holds only for `(i=1, j=0)`, and the element read is `arr[j][i] = arr[0][1] = 5`.

| i | j | i > j | arr[j][i] | sum |
|---|---|---|---|---|
| 0 | 0 | false | — | 0 |
| 0 | 1 | false | — | 0 |
| 1 | 0 | true | arr[0][1] = 5 | 5 |
| 1 | 1 | false | — | 5 |

- (a) Uses the subscripts in the written order `arr[1][0] = 8` instead of `arr[0][1]`.
- (c) Adds both 8 and 5 (13) by accepting `(i=0, j=1)` as well.
- (d) Concludes the condition never fires because rows and columns look symmetric.

---

**31.** **[Hard]** *(B3 — shift operators applied to 2D elements)*

```text
Integer arr[2][2] = {{3, 4}, {5, 6}}
Integer sum = 0
for (i = 0; i < 2; i = i + 1)
    sum = sum + (arr[i][0] << 1)
    sum = sum + (arr[i][1] >> 1)
Print sum
```

What is printed?

(a) 18
(b) 21
(c) 16
(d) 24

---

**31. (b) 21**

Left shift by 1 doubles; right shift by 1 halves (integer division). Row 0 gives 3×2 + 4/2 = 8; row 1 gives 5×2 + 6/2 = 13.

| i | arr[i][0] << 1 | arr[i][1] >> 1 | sum |
|---|---|---|---|
| 0 | 6 | 2 | 8 |
| 1 | 10 | 3 | 21 |

- (a) Shifts in the wrong direction on one side, e.g. 3/2 + 4*2 = 9.
- (d) Applies `<< 1` to both columns: 6 + 8 + 10 + 12 = 36, minus a term.
- (c) Uses `>> 1` for both columns: 1 + 2 + 2 + 3 = 8 with something similar.

---

**32.** **[Hard]** *(B3 — odd/even branch mixing array values with indices)*

```text
Integer arr[2][2] = {{7, 2}, {3, 6}}
Integer sum = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if ((arr[i][j] & 1) == 1)
            sum = sum + arr[i][j]
        else
            sum = sum + i + j
Print sum
```

What is printed?

(a) 13
(b) 18
(c) 11
(d) 16

---

**32. (a) 13**

Odd values contribute themselves; even values contribute `i + j`.

| i | j | val | odd? | added | sum |
|---|---|---|---|---|---|
| 0 | 0 | 7 | yes | 7 | 7 |
| 0 | 1 | 2 | no | 0+1 = 1 | 8 |
| 1 | 0 | 3 | yes | 3 | 11 |
| 1 | 1 | 6 | no | 1+1 = 2 | 13 |

- (b) Adds the even values themselves (2 + 6 = 8) instead of `i + j`, giving 18.
- (c) Ignores the two `i + j` contributions (7 + 3 = 10, or 7+3+1 = 11).
- (d) Adds `i + j` for every even cell but also counts 6 as odd.

---

**33.** **[Hard]** *(B3 — in-place update of a 1D array, then re-traversal)*

```text
Integer arr[4] = {2, 4, 6, 8}
for (i = 0; i < 4; i = i + 1)
    arr[i] = arr[i] / 2
Integer sum = 0
for (i = 0; i < 4; i = i + 1)
    sum = sum + arr[i] * 3
Print sum
```

What is printed?

(a) 20
(b) 60
(c) 15
(d) 30

---

**33. (d) 30**

The first loop halves each element in place, giving {1, 2, 3, 4}. The second loop adds `arr[i] * 3` each time: 3 + 6 + 9 + 12 = 30.

| i | arr[i] after halving | arr[i] * 3 | sum |
|---|---|---|---|
| 0 | 1 | 3 | 3 |
| 1 | 2 | 6 | 9 |
| 2 | 3 | 9 | 18 |
| 3 | 4 | 12 | 30 |

- (a) Multiplies the total by 3 after summing (10 * 3 would be 30, so 20 means one element was halved twice).
- (c) Sums the halved array without the `* 3`: 1+2+3+4 = 10, close to but not 15.
- (b) Multiplies the *original* array by 3 and sums: 6+12+18+24 = 60, ignoring the in-place update.

---

**34.** **[Hard]** *(B3 — rectangular array, different bounds per dimension)*

```text
Integer arr[3][2] = {{1, 2}, {3, 4}, {5, 6}}
Integer sum = 0
for (i = 0; i < 3; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        if (j == 0)
            sum = sum + arr[i][j] * 2
        else
            sum = sum - arr[i][j]
Print sum
```

What is printed?

(a) 12
(b) 6
(c) 21
(d) 0

---

**34. (b) 6**

Row 0 contributes +1×2 and −2; row 1 contributes +3×2 and −4; row 2 contributes +5×2 and −6.

| i | j | val | operation | sum |
|---|---|---|---|---|
| 0 | 0 | 1 | +2 | 2 |
| 0 | 1 | 2 | −2 | 0 |
| 1 | 0 | 3 | +6 | 6 |
| 1 | 1 | 4 | −4 | 2 |
| 2 | 0 | 5 | +10 | 12 |
| 2 | 1 | 6 | −6 | 6 |

- (a) Uses 12 as the final figure by skipping the last subtraction.
- (c) Adds both columns instead of subtracting the second: 18 + 12 = 30, so 21 means an arithmetic slip.
- (d) Subtracts from an initial value of 0 for the first row only (2 − 2 = 0) and stops.

---

**35.** **[Hard]** *(B3 — reverse column traversal with an index condition)*

```text
Integer arr[2][2] = {{11, 4}, {9, 2}}
Integer sum = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 1; j >= 0; j = j - 1)
        if ((i + j) == 1)
            sum = sum + arr[i][j]
Print sum
```

What is printed?

(a) 15
(b) 11
(c) 20
(d) 13

---

**35. (d) 13**

The condition `i + j == 1` is satisfied by `(0,1)` and `(1,0)`, reading `arr[0][1] = 4` and `arr[1][0] = 9`.

| i | j | i + j | element | sum |
|---|---|---|---|---|
| 0 | 1 | 1 | arr[0][1] = 4 | 4 |
| 0 | 0 | 0 | skipped | 4 |
| 1 | 1 | 2 | skipped | 4 |
| 1 | 0 | 1 | arr[1][0] = 9 | 13 |

- (a) Adds 11 + 4 (row 0) and stops.
- (b) Adds only 11, the first element of row 0.
- (c) Adds all four elements (11+4+9+2 = 26 is wrong too, so 20 means partial traversal ignoring the bound `j >= 0`).

---

**36.** **[Hard]** *(B3 — XOR of 2D elements with a 1D array indexed by the outer loop)*

```text
Integer arr[2][2] = {{5, 10}, {15, 20}}
Integer b[3] = {4, 6, 8}
Integer sum = 0
for (i = 0; i < 2; i = i + 1)
    for (j = 0; j < 2; j = j + 1)
        sum = sum + (arr[i][j] XOR b[i])
Print sum
```

What is printed?

(a) 48
(b) 36
(c) 42
(d) 26

---

---

**36. (c) 42**

`b[i]` depends only on the outer index, so each row uses one fixed XOR mask: row 0 uses 4, row 1 uses 6.

| i | j | arr[i][j] | b[i] | XOR | sum |
|---|---|---|---|---|---|
| 0 | 0 | 5 | 4 | 1 | 1 |
| 0 | 1 | 10 | 4 | 14 | 15 |
| 1 | 0 | 15 | 6 | 9 | 24 |
| 1 | 1 | 20 | 6 | 18 | 42 |

- (b) Uses `b[j]` instead of `b[i]` for the second column (10 ^ 6 = 12), giving a smaller total.
- (a) Uses `b[0] = 4` for both rows: 1 + 14 + 11 + 16 = 42, so 48 reflects an incorrect XOR.
- (d) Adds the array elements without XOR (5 + 10 + 15 + 20 = 50) or subtracts instead of XORing.

---
