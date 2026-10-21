---
title: Arrays — 1D and 2D Traversal and Indexing
code: P5
section: Pseudocode
weightage_pct: 1.8% of marks
est_questions: 0.68
tier: 2
difficulty: Medium
est_study_hours: 0.8
confidence: Medium
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-library/topics/T15-B3-arrays-1d-2d.md
---

# P5 — Arrays — 1D and 2D Traversal and Indexing

*Adapted from `accenture-prep-final/accenture-prep-library/topics/T15-B3-arrays-1d-2d.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.7 questions and 1.4 marks** on this topic (about 1.8% of the 75 scored marks). It sits in **Pseudocode**: 5 questions, 10 marks, 10 minutes. **Tier 2**, 0.8 hours to reach reliable recall, confidence **Medium**.

**2 questions on this topic are in the observed Infosys pool** (P12, P15), from 1 source. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** its ROI alone would place it lower, but this section has its own cut-off and this topic is needed to reach 60% of the section's marks. Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| P12 | 2026-09-18 | total = product of all elements; result[i] = total / a[i]. Input 2, 3, 4, 5. Output? |
| P15 | 2026-09-18 | cur = 1, best = 1. for i = 1 to n-1: if a[i] > a[i-1] then cur++ ; best = max(best, cur) else cur = 1. Output for [1, 2, 2, 3, 4, 5, 1]? |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



1. **2D initialiser to element access.** Given `Integer arr[2][2] = {{0, 1}, {4, 1}}`, know immediately that `arr[0][0]=0`, `arr[0][1]=1`, `arr[1][0]=4`, `arr[1][1]=1`. Confirmed in 4 items.

**1. Correct: (d) `arr[1]` gives 3**

- (b) `arr[2] = 9` — off by one; index 2 is the *third* element.
- (c) `arr[0] = 7` — first element, not second.
- (a) `arr[5]` — out of range; a size-5 array has valid indices 0–4.

---

2. **Bitwise on array elements inside a guard.** `If((3 & arr[1][1]) < (arr[1][0] + 1))`.

**2. Correct: (c) 6**

| i | j | arr[i][j] | s |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 4 | 5 |
| 1 | 1 | 1 | 6 |

- (a) 5 — `s` initialised to `arr[0][1]`, so `arr[0][0] = 0` never added.
- (b) 7 — `arr[1][1] = 1` added one extra time after the loops.
- (d) 10 — `arr[1][0] = 4` counted twice and `arr[0][0] = 0` skipped.

---

3. **In-place modification then re-read.** `arr[0][0] = (arr[0][0] ^ 2) + arr[0][0]` — the element appears on both sides.

**3. Correct: (b) 5**

| Step | Value |
|---|---|
| `3 & arr[1][1]` = `3 & 1` | 1 |
| `arr[1][0] + 1` = `4 + 1` | 5 |
| `1 < 5` | True → line 4 |
| `t = arr[0][1] + arr[1][0]` = `1 + 4` | 5 |

- (a) 1 — comparison read reversed, so the Else branch runs: `0 + 1`.
- (c) 4 — `t` set to `arr[1][0]` alone.
- (d) 6 — sum of all four elements instead of just the two.

---

4. **Print a sum of two elements.** The standard ending.

**4. Correct: (c) 10**

| Step | Value |
|---|---|
| `arr[0][0] = (0 ^ 2) + 0` | 2 |
| `arr[0][1] = 1 + 2` | 3 |
| `arr[1][0]`, `arr[1][1]` unchanged | 4, 1 |
| `2 + 3 + 4 + 1` | 10 |

- (a) 8 — line 3 uses the *original* `arr[0][0] = 0`, so `arr[0][1]` stays 1.
- (d) 12 — `arr[0][0]` counted twice in the Print.
- (b) 6 — `^` read as exponentiation, giving `arr[0][0] = 0` and `arr[0][1] = 1`.

---

5. **1D indexing and the off-by-one.** Which index is the "second element" of a zero-indexed array (index 1). Confirmed in the array-initialisation item.

### The two grids that actually appeared

| `{{0,1},{4,1}}` | col 0 | col 1 |
|---|---|---|
| **row 0** | 0 | 1 |
| **row 1** | 4 | 1 |

| `{{1,2},{2,4}}` | col 0 | col 1 |
|---|---|---|
| **row 0** | 1 | 2 |
| **row 1** | 2 | 4 |

Memorise the *shape* of that mapping, not these two grids.

## 3. Concept notes

**Convention used below:** every array in this section is **zero-indexed** unless stated otherwise. Loop bounds are inclusive. Statements are given in generic pseudocode (`DECLARE`, `FOR`, `WHILE`, `IF`, `OUTPUT`).

### 3.1 What an array is

An array is a **fixed-size, ordered collection of elements of the same type**. Each element is reached by its **index** (its position number).

- Fixed size: the length is set at declaration and does not change.
- Ordered: element order is part of the structure.
- Same type: all elements are the same data type.
- **Contiguous memory:** the elements sit in consecutive memory cells, one after another, with no gaps.

Because the block is contiguous, the machine can compute the address of any element directly:

```
address(arr[i]) = base_address + i * element_size_in_bytes
```

This is the same formula every time, so it costs the same work for `i = 0` and for `i = 999999`. That is why indexing is **O(1)** — constant time. The computer does not scan; it multiplies and adds.

| Operation on a 1D array | Cost | Why |
|---|---|---|
| Read `arr[i]` | O(1) | address arithmetic |
| Write `arr[i] = x` | O(1) | address arithmetic |
| Find an element by value (linear search) | O(n) | must inspect up to n cells |
| Find max / min | O(n) | every element must be read |
| Sum | O(n) | every element must be read |
| Insert at front / middle | O(n) | must shift elements |
| Delete at front / middle | O(n) | must shift elements |

### 3.2 Zero-based vs one-based indexing

| | Zero-based | One-based |
|---|---|---|
| First element index | 0 | 1 |
| Second element index | 1 | 2 |
| k-th element index | k − 1 | k |
| Last element index | n − 1 | n |
| Valid index range | 0 to n − 1 | 1 to n |
| Number of valid indices | n | n |

**The exam trap.** For a zero-indexed array:

| Phrase in the question | Index |
|---|---|
| first element | 0 |
| **second element** | **1** |
| third element | 2 |
| last element | n − 1 |
| element at position n | does not exist |

Candidates lose marks by answering index 2 for "second element". The second element is **index 1** because counting starts at 0.

**Length vs last index.** If an array has `n` elements, its last index is `n − 1`. So `last index = length − 1` and `number of elements = last index + 1`.

**Out of bounds.** A reference is out of bounds if the index is outside the valid range.

| Base | Out of bounds when | Typical result |
|---|---|---|
| zero-based | `i < 0` or `i > n − 1` | runtime error, or undefined/garbage value |
| one-based | `i < 1` or `i > n` | runtime error, or undefined/garbage value |

The most common off-by-one bug: writing `FOR i = 0 TO n` instead of `FOR i = 0 TO n-1`. The first version runs n + 1 times and reads `arr[n]`, which is out of bounds.

### 3.3 Declaring and initialising 1D arrays in pseudocode

```
DECLARE arr[5]                      // 5 elements, valid indices 0..4
arr = [10, 20, 30, 40, 50]

DECLARE nums[5] = [1, 2, 3, 4, 5]   // declare and initialise together

DECLARE n = 4
DECLARE flags[n]                    // length taken from a variable
```

Filling an array by reading input, and printing it:

```
DECLARE a[5]
FOR i = 0 TO 4
    READ a[i]
END FOR

FOR i = 0 TO 4
    OUTPUT a[i]
END FOR
```

Setting every element to the same value:

```
FOR i = 0 TO n-1
    a[i] = 0
END FOR
```

Note: `DECLARE arr[5]` gives **5** cells, not 6. The 5 is a **count**, not the largest index. The largest index is 4.

### 3.4 Traversal patterns (1D)

| Pattern | Pseudocode | Iterations |
|---|---|---|
| Forward | `FOR i = 0 TO n-1` | n |
| Backward | `FOR i = n-1 DOWNTO 0` | n |
| Every other element | `FOR i = 0 TO n-1 STEP 2` | ceil(n/2) |
| Every third element | `FOR i = 0 TO n-1 STEP 3` | ceil(n/3) |
| Skip first, rest | `FOR i = 1 TO n-1` | n − 1 |
| All but last | `FOR i = 0 TO n-2` | n − 1 |

Forward:

```
FOR i = 0 TO n-1
    OUTPUT a[i]
END FOR
```

Backward — often asked, required for reverse printing:

```
FOR i = n-1 DOWNTO 0
    OUTPUT a[i]
END FOR
```

Every other element (indices 0, 2, 4, …):

```
FOR i = 0 TO n-1 STEP 2
    OUTPUT a[i]
END FOR
```

Count check for the every-other loop: `ceil(n/2)`. For n = 5 the indices are 0, 2, 4 → 3 iterations = ceil(5/2) = 3. For n = 4 the indices are 0, 2 → 2 iterations = ceil(4/2) = 2.

### 3.5 2D arrays: the mental model

A 2D array is a **grid of rows and columns**. Think of a table or a spreadsheet. Every cell is identified by two numbers: its row and its column.

```
DECLARE grid[R][C]     // R rows, C columns
grid[row][column]
```

- The **first** index selects the **row**.
- The **second** index selects the **column**.
- Total number of cells = R × C.
- Valid row indices: 0 to R − 1. Valid column indices: 0 to C − 1.

Some exam papers declare `arr[C][R]` instead; always check which dimension the paper treats as rows. Unless the question says otherwise, assume `arr[rows][cols]`.

#### Reading an initialiser into a grid

The initialiser is written as a list of row lists, **outer braces = the whole grid, inner braces = one row, left to right**.

**Example A:** `arr[2][2] = {{0,1},{4,1}}`

Row 0 = `{0,1}`, Row 1 = `{4,1}`.

| | col 0 | col 1 |
|---|---|---|
| **row 0** | 0 | 1 |
| **row 1** | 4 | 1 |

So:

| Cell | Value |
|---|---|
| `arr[0][0]` | 0 |
| `arr[0][1]` | 1 |
| `arr[1][0]` | 4 |
| `arr[1][1]` | 1 |

**Example B:** `arr[2][2] = {{1,2},{2,4}}`

Row 0 = `{1,2}`, Row 1 = `{2,4}`.

| | col 0 | col 1 |
|---|---|---|
| **row 0** | 1 | 2 |
| **row 1** | 2 | 4 |

So:

| Cell | Value |
|---|---|
| `arr[0][0]` | 1 |
| `arr[0][1]` | 2 |
| `arr[1][0]` | 2 |
| `arr[1][1]` | 4 |

**Reading rule to memorise.** The first number inside an inner brace is column 0 of that row; the second is column 1; and so on. The first inner brace is row 0.

A non-square example: `arr[2][3] = {{5,6,7},{8,9,10}}`

| | col 0 | col 1 | col 2 |
|---|---|---|---|
| **row 0** | 5 | 6 | 7 |
| **row 1** | 8 | 9 | 10 |

Total cells = 2 × 3 = 6. `arr[1][2] = 10`.

### 3.6 Row-major vs column-major storage

Memory is one-dimensional; a 2D array is flattened into it in one of two orders.

- **Row-major:** store row 0 completely, then row 1, then row 2, … (used by C, C++, Java, Python).
- **Column-major:** store column 0 completely, then column 1, then column 2, … (used by Fortran, MATLAB, R).

Let `R` = number of rows, `C` = number of columns, `w` = element size in bytes, `base` = address of `arr[0][0]`, and indices zero-based.

| Order | Address of `arr[i][j]` | Linear element number (0-based) |
|---|---|---|
| Row-major | `base + (i * C + j) * w` | `i * C + j` |
| Column-major | `base + (j * R + i) * w` | `j * R + i` |

**Worked example.** `R = 3`, `C = 4`, `w = 4` bytes, `base = 1000`. Find the address of `arr[2][1]`.

Row-major:

```
linear index = i * C + j = 2 * 4 + 1 = 9
address      = 1000 + 9 * 4 = 1000 + 36 = 1036
```

Column-major:

```
linear index = j * R + i = 1 * 3 + 2 = 5
address      = 1000 + 5 * 4 = 1000 + 20 = 1020
```

| | Linear index | Byte offset | Address |
|---|---|---|---|
| Row-major | 9 | 36 | 1036 |
| Column-major | 5 | 20 | 1020 |

Sanity checks: for `arr[0][0]` both formulas give the base address 1000. For the last cell `arr[2][3]` in row-major: `2*4 + 3 = 11`, address `1000 + 44 = 1044`; the array has 12 cells (0…11), so 11 is indeed the last linear index.

If indices are **one-based**, subtract 1 from each index first, or use `base + ((i-1) * C + (j-1)) * w` for row-major.

### 3.7 Nested-loop traversal of a 2D array

```
FOR i = 0 TO R-1
    FOR j = 0 TO C-1
        OUTPUT arr[i][j]
    END FOR
END FOR
```

| Loop | Runs | Body of inner loop runs |
|---|---|---|
| Outer `i` | R times | — |
| Inner `j` | C times per outer pass | R × C times |
| Statement `OUTPUT arr[i][j]` | — | R × C times |

**Total iteration count of the inner body = R × C.** For a 3 × 4 array that is 12. For a 2 × 2 array that is 4.

| Traversal shape | Iteration count |
|---|---|
| 1D, `0 TO n-1` | n |
| 1D, `0 TO n-1 STEP 2` | ceil(n/2) |
| 2D rectangular R × C | R × C |
| 2D triangular, inner `j = 0 TO i` | R(R+1)/2 |
| 3D, R × C × D | R × C × D |

Traversal orders:

| Order | Pseudocode |
|---|---|
| Row by row (row-major order) | outer loop over rows, inner loop over columns |
| Column by column | outer loop over columns, inner loop over rows |
| Reverse rows | `FOR i = R-1 DOWNTO 0` |

Row-by-row traversal of `{{0,1},{4,1}}` visits 0, 1, 4, 1 in that order. Column-by-column traversal visits 0, 4, 1, 1.

### 3.8 Common operations

All snippets assume zero-based indexing and `n` elements (1D) or `R × C` (2D).

#### Sum

```
sum = 0
FOR i = 0 TO n-1
    sum = sum + a[i]
END FOR
```

Trace on `a = [4, 1, 7]`:

| i | a[i] | sum after |
|---|---|---|
| 0 | 4 | 4 |
| 1 | 1 | 5 |
| 2 | 7 | 12 |

Result 12.

#### Max

```
max = a[0]
FOR i = 1 TO n-1
    IF a[i] > max THEN
        max = a[i]
    END IF
END FOR
```

Trace on `a = [3, 9, 2]`:

| i | a[i] | max after |
|---|---|---|
| — | — | 3 (initial) |
| 1 | 9 | 9 |
| 2 | 2 | 9 |

Result 9. The loop starts at `i = 1` because `a[0]` is already the seed. Starting the loop at 0 also works.

#### Min

```
min = a[0]
FOR i = 1 TO n-1
    IF a[i] < min THEN
        min = a[i]
    END IF
END FOR
```

Trace on `a = [3, 9, 2]`: min starts at 3 → i=1: 9 is not < 3 → i=2: 2 < 3 → min = 2. Result 2.

#### Reverse in place

```
left = 0
right = n-1
WHILE left < right
    temp = a[left]
    a[left] = a[right]
    a[right] = temp
    left = left + 1
    right = right - 1
END WHILE
```

Trace on `a = [1, 2, 3, 4]`:

| Step | left | right | Array after swap |
|---|---|---|---|
| start | 0 | 3 | [1, 2, 3, 4] |
| swap | 0 | 3 | [4, 2, 3, 1] |
| swap | 1 | 2 | [4, 3, 2, 1] |
| stop | 2 | 1 | left < right is false |

Result `[4, 3, 2, 1]`. Number of swaps = floor(n/2). For n = 5, middle element (index 2) is never touched.

#### Swap two elements

```
temp = a[i]
a[i] = a[j]
a[j] = temp
```

Trace on `a = [5, 6, 7]` with `i = 0`, `j = 2`:

| Statement | Array |
|---|---|
| start | [5, 6, 7] |
| `temp = a[0]` | [5, 6, 7], temp = 5 |
| `a[0] = a[2]` | [7, 6, 7] |
| `a[2] = temp` | [7, 6, 5] |

The order of the three statements matters. Writing `a[i] = a[j]` before saving `a[i]` destroys the value. If `i == j`, the swap is a no-op and is still correct with a temp variable (XOR-swap without a temp fails when `i == j`).

#### Count occurrences

```
count = 0
FOR i = 0 TO n-1
    IF a[i] = key THEN
        count = count + 1
    END IF
END FOR
```

Trace on `a = [2, 3, 2, 5, 2]`, `key = 2`:

| i | a[i] | Match? | count after |
|---|---|---|---|
| 0 | 2 | yes | 1 |
| 1 | 3 | no | 1 |
| 2 | 2 | yes | 2 |
| 3 | 5 | no | 2 |
| 4 | 2 | yes | 3 |

Result 3. Iterations always = n (no early exit).

#### Linear search

```
found = -1
FOR i = 0 TO n-1
    IF a[i] = key THEN
        found = i
        BREAK
    END IF
END FOR
```

Trace on `a = [9, 4, 7, 4]`:

| key | Scanned | Result |
|---|---|---|
| 4 | a[0]=9 no, a[1]=4 yes → break | 1 (first match) |
| 7 | a[0] no, a[1] no, a[2] yes → break | 2 |
| 6 | all four compared, none match | −1 |

Best case 1 comparison, worst case n comparisons, so O(n). Without `BREAK`, the loop returns the **last** match instead of the first.

### 3.9 In-place modification trap

"In place" means updating the same array without a copy. If an element is written early and then read again later in the same pass, the read sees the **new** value, not the original. This changes the answer.

```
FOR i = 1 TO n-1
    a[i] = a[i] + a[i-1]
END FOR
```

Trace on `a = [1, 2, 3, 4]`:

| i | a[i-1] read | a[i] before | a[i] after | Array |
|---|---|---|---|---|
| 1 | 1 | 2 | 3 | [1, 3, 3, 4] |
| 2 | 3 (already updated) | 3 | 6 | [1, 3, 6, 4] |
| 3 | 6 (already updated) | 4 | 10 | [1, 3, 6, 10] |

Result `[1, 3, 6, 10]` — running totals. If instead the original values were used (`a[i] + original_a[i-1]`), the result would be `[1, 3, 5, 7]`. Same code shape, different answer, purely because of the read-after-write.

Contrast with the safe direction:

```
FOR i = 0 TO n-2
    a[i] = a[i] + a[i+1]
END FOR
```

Here `a[i+1]` has not been updated yet when it is read (the loop moves forward and writes to i, reads from i+1). Trace on `[1, 2, 3, 4]`:

| i | a[i] | a[i+1] | a[i] after | Array |
|---|---|---|---|---|
| 0 | 1 | 2 | 3 | [3, 2, 3, 4] |
| 1 | 2 | 3 | 5 | [3, 5, 3, 4] |
| 2 | 3 | 4 | 7 | [3, 5, 7, 4] |

Result `[3, 5, 7, 4]`, computed from original neighbours.

**Rule of thumb for the exam:** when tracing an in-place loop, write the array after **every single iteration**. A loop that reads a lower index (`a[i-1]`) while running forwards reads already-modified data; a loop that reads a higher index (`a[i+1]`) while running forwards reads original data.

Also watch for compound traps: overwriting with 0 or −1 before a later comparison, e.g. setting `a[i] = 0` in one loop and later counting how many elements equal 0.

### 3.10 Jagged arrays (brief)

A jagged (ragged) array is an array of arrays whose rows have **different lengths**.

```
DECLARE jag[3][]
jag[0] = [1, 2]
jag[1] = [3, 4, 5, 6]
jag[2] = [7]
```

| Row | Length | Elements |
|---|---|---|
| 0 | 2 | 1, 2 |
| 1 | 4 | 3, 4, 5, 6 |
| 2 | 1 | 7 |

Traversal must use each row's own length, not a fixed column count:

```
FOR i = 0 TO rows-1
    FOR j = 0 TO length(jag[i]) - 1
        OUTPUT jag[i][j]
    END FOR
END FOR
```

| | Rectangular 2D array | Jagged array |
|---|---|---|
| Row lengths | all equal | may differ |
| Bounds | row 0..R-1, col 0..C-1 | row 0..R-1, col 0..len(row)-1 |
| Address formula | single formula works | no single formula |
| Total cells | R × C | sum of row lengths |
| Contiguity | one contiguous block | rows may be scattered |

### 3.11 Array vs linked list

| Property | Array | Linked list |
|---|---|---|
| Size | fixed at creation | grows and shrinks at runtime |
| Memory layout | contiguous block | nodes scattered, joined by pointers |
| Access by index | O(1) | O(n) |
| Insert at front | O(n) — shift all | O(1) |
| Insert at end | O(1) if space remains | O(1) with a tail pointer, else O(n) |
| Insert in middle | O(n) — shift | O(1) after reaching the position, O(n) to reach it |
| Delete | O(n) — shift | O(1) after reaching the position |
| Memory overhead | none | one pointer per node |
| Cache performance | good (contiguous) | poor (scattered) |
| Binary search possible | yes, if sorted | no (no O(1) index) |
| Random access | yes | no |

## 4. Must-memorise block

### Index range and traps

| Fact | Value |
|---|---|
| Zero-based valid range | 0 to n − 1 |
| One-based valid range | 1 to n |
| Number of elements | last index + 1 |
| Last index | length − 1 |
| Out of bounds (zero-based) | `i < 0` or `i > n − 1` |
| Out of bounds (one-based) | `i < 1` or `i > n` |
| `FOR i = 0 TO n` on an n-element array | runs n + 1 times, reads `arr[n]` → out of bounds |

**Trap table — "which index is that?" (zero-based array):**

| Asked for | Index |
|---|---|
| first element | 0 |
| **second element** | **1** |
| third element | 2 |
| last element | n − 1 |
| element before last | n − 2 |

### 2D initialiser → grid, example A

`arr[2][2] = {{0,1},{4,1}}`

| | col 0 | col 1 |
|---|---|---|
| **row 0** | 0 | 1 |
| **row 1** | 4 | 1 |

`arr[0][0] = 0` · `arr[0][1] = 1` · `arr[1][0] = 4` · `arr[1][1] = 1`

### 2D initialiser → grid, example B

`arr[2][2] = {{1,2},{2,4}}`

| | col 0 | col 1 |
|---|---|---|
| **row 0** | 1 | 2 |
| **row 1** | 2 | 4 |

`arr[0][0] = 1` · `arr[0][1] = 2` · `arr[1][0] = 2` · `arr[1][1] = 4`

### Address formulas

| Order | Address of `arr[i][j]` | Linear index (0-based) |
|---|---|---|
| Row-major | `base + (i*C + j) * w` | `i*C + j` |
| Column-major | `base + (j*R + i) * w` | `j*R + i` |

R = rows, C = columns, w = element size in bytes, zero-based indices. For one-based indices, subtract 1 from i and j first.

### Nested traversal iteration count

| Loop form | Inner-body iterations |
|---|---|
| `FOR i = 0 TO n-1` | n |
| `FOR i = 0 TO n-1 STEP 2` | ceil(n/2) |
| `FOR i = 0 TO R-1 / FOR j = 0 TO C-1` | R × C |
| `FOR i = 0 TO R-1 / FOR j = 0 TO i` | R(R+1)/2 |

### One-line recall list

- Contiguous memory → `base + i*w` → **O(1) indexing**.
- Zero-based: 0 … n−1. One-based: 1 … n.
- Second element of a zero-indexed array is index **1**, not 2.
- `DECLARE a[5]` = 5 cells, indices 0–4.
- `arr[row][col]`; first initialiser brace = row 0; first value in a row = column 0.
- Row-major = row by row; column-major = column by column.
- Nested R × C traversal = R × C iterations.
- Reverse in place = floor(n/2) swaps; middle element of an odd-length array never moves.
- Linear search returns the **first** match only if it breaks; without `BREAK` it returns the **last**.
- In-place trap: a value written earlier in the same pass is read back as the new value. Trace the array after every iteration.

## 5. Worked examples

Convention used throughout: indexing is **zero-based**, `arr[row][column]`, `For i = 0 to 1` executes i = 0 and i = 1 (bounds inclusive), integers divide with truncation, and `^` is bitwise XOR, `&` bitwise AND, `>>` right shift.

### Example 1 — Bitwise condition guarding a 2D element update

```
1  Integer arr[2][2] = {{0,1},{4,1}}
2  If ((3 & arr[1][1]) < (arr[1][0] + 1))
3     arr[0][0] = (arr[0][0] ^ 2) + arr[0][0]
4  End If
5  Print arr[0][0] + arr[1][0]
```

| Line | arr[0][0] | arr[0][1] | arr[1][0] | arr[1][1] | Condition / value |
|---|---|---|---|---|---|
| 1 | 0 | 1 | 4 | 1 | array initialised |
| 2 | 0 | 1 | 4 | 1 | 3 & 1 = 1; 4 + 1 = 5; 1 < 5 → **True** |
| 3 | 2 | 1 | 4 | 1 | arr[0][0] = (0 ^ 2) + 0 = 2 + 0 = 2 |
| 4 | 2 | 1 | 4 | 1 | if-block ends (no operation) |
| 5 | 2 | 1 | 4 | 1 | Print 2 + 4 = 6 |

**Answer: 6**

### Example 2 — Nested loops over a 2D array, diagonal weighted double

```
1  Integer arr[2][2] = {{3,5},{7,2}}
2  Integer i, j, s
3  s = 0
4  For i = 0 to 1
5    For j = 0 to 1
6      If (i == j)
7        s = s + arr[i][j] * 2
8      Else
9        s = s + arr[i][j]
10     End If
11   End For
12 End For
13 Print s
```

| Line | i | j | arr[0][0] | arr[0][1] | arr[1][0] | arr[1][1] | s | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | – | – | 3 | 5 | 7 | 2 | – | array initialised |
| 2 | – | – | 3 | 5 | 7 | 2 | – | i, j declared |
| 3 | – | – | 3 | 5 | 7 | 2 | 0 | s = 0 |
| 4 | 0 | – | 3 | 5 | 7 | 2 | 0 | outer loop begins |
| 5 | 0 | 0 | 3 | 5 | 7 | 2 | 0 | inner loop begins |
| 6 | 0 | 0 | 3 | 5 | 7 | 2 | 0 | 0 == 0 → True |
| 7 | 0 | 0 | 3 | 5 | 7 | 2 | 6 | s = 0 + arr[0][0] * 2 = 0 + 6 |
| 8 | 0 | 0 | 3 | 5 | 7 | 2 | 6 | Else skipped (not executed) |
| 10 | 0 | 0 | 3 | 5 | 7 | 2 | 6 | if-block ends |
| 11 | 0 | 1 | 3 | 5 | 7 | 2 | 6 | End For: j → 1 |
| 5 | 0 | 1 | 3 | 5 | 7 | 2 | 6 | inner loop body |
| 6 | 0 | 1 | 3 | 5 | 7 | 2 | 6 | 0 == 1 → False |
| 8 | 0 | 1 | 3 | 5 | 7 | 2 | 6 | – |
| 9 | 0 | 1 | 3 | 5 | 7 | 2 | 11 | s = 6 + arr[0][1] = 6 + 5 |
| 10 | 0 | 1 | 3 | 5 | 7 | 2 | 11 | if-block ends |
| 11 | 0 | 2 | 3 | 5 | 7 | 2 | 11 | j → 2, exceeds bound; inner loop ends |
| 12 | 1 | – | 3 | 5 | 7 | 2 | 11 | i → 1 |
| 4 | 1 | – | 3 | 5 | 7 | 2 | 11 | outer loop body |
| 5 | 1 | 0 | 3 | 5 | 7 | 2 | 11 | inner loop begins |
| 6 | 1 | 0 | 3 | 5 | 7 | 2 | 11 | 1 == 0 → False |
| 8 | 1 | 0 | 3 | 5 | 7 | 2 | 11 | – |
| 9 | 1 | 0 | 3 | 5 | 7 | 2 | 18 | s = 11 + arr[1][0] = 11 + 7 |
| 10 | 1 | 0 | 3 | 5 | 7 | 2 | 18 | if-block ends |
| 11 | 1 | 1 | 3 | 5 | 7 | 2 | 18 | j → 1 |
| 5 | 1 | 1 | 3 | 5 | 7 | 2 | 18 | inner loop body |
| 6 | 1 | 1 | 3 | 5 | 7 | 2 | 18 | 1 == 1 → True |
| 7 | 1 | 1 | 3 | 5 | 7 | 2 | 22 | s = 18 + arr[1][1] * 2 = 18 + 4 |
| 8 | 1 | 1 | 3 | 5 | 7 | 2 | 22 | Else skipped (not executed) |
| 10 | 1 | 1 | 3 | 5 | 7 | 2 | 22 | if-block ends |
| 11 | 1 | 2 | 3 | 5 | 7 | 2 | 22 | j → 2; inner loop ends |
| 12 | 2 | – | 3 | 5 | 7 | 2 | 22 | i → 2; outer loop ends |
| 13 | 2 | – | 3 | 5 | 7 | 2 | 22 | Print 22 |

**Answer: 22**

### Example 3 — 1D array rewritten in place with XOR

```
1  Integer arr[3] = {5, 2, 7}
2  Integer i
3  For i = 0 to 2
4     arr[i] = (arr[i] ^ 3) + i
5  End For
6  Print arr[0] + arr[2]
```

| Line | i | arr[0] | arr[1] | arr[2] | Value computed |
|---|---|---|---|---|---|
| 1 | – | 5 | 2 | 7 | array initialised |
| 2 | – | 5 | 2 | 7 | i declared |
| 3 | 0 | 5 | 2 | 7 | i = 0 |
| 4 | 0 | 6 | 2 | 7 | arr[0] = (5 ^ 3) + 0 = 6 + 0 = 6 |
| 5 | 1 | 6 | 2 | 7 | End For: i → 1 |
| 3 | 1 | 6 | 2 | 7 | loop body |
| 4 | 1 | 6 | 2 | 7 | arr[1] = (2 ^ 3) + 1 = 1 + 1 = 2 |
| 5 | 2 | 6 | 2 | 7 | i → 2 |
| 3 | 2 | 6 | 2 | 7 | loop body |
| 4 | 2 | 6 | 2 | 6 | arr[2] = (7 ^ 3) + 2 = 4 + 2 = 6 |
| 5 | 3 | 6 | 2 | 6 | i → 3, exceeds bound; loop ends |
| 6 | 3 | 6 | 2 | 6 | Print 6 + 6 = 12 |

**Answer: 12**

### Example 4 — Column sum with `>>`, then a bitwise branch

```
1  Integer arr[2][2] = {{3,6},{1,2}}
2  Integer j, t
3  t = 0
4  For j = 0 to 1
5     t = t + (arr[j][1] >> 1)
6  End For
7  If (t > arr[0][0])
8     t = t ^ arr[1][0]
9  Else
10    t = t + arr[1][1]
11 End If
12 Print t
```

| Line | j | arr[0][0] | arr[0][1] | arr[1][0] | arr[1][1] | t | Note |
|---|---|---|---|---|---|---|---|
| 1 | – | 3 | 6 | 1 | 2 | – | array initialised |
| 2 | – | 3 | 6 | 1 | 2 | – | j, t declared |
| 3 | – | 3 | 6 | 1 | 2 | 0 | t = 0 |
| 4 | 0 | 3 | 6 | 1 | 2 | 0 | j = 0 |
| 5 | 0 | 3 | 6 | 1 | 2 | 3 | t = 0 + (6 >> 1) = 0 + 3 |
| 6 | 1 | 3 | 6 | 1 | 2 | 3 | End For: j → 1 |
| 4 | 1 | 3 | 6 | 1 | 2 | 3 | loop body |
| 5 | 1 | 3 | 6 | 1 | 2 | 4 | t = 3 + (2 >> 1) = 3 + 1 |
| 6 | 2 | 3 | 6 | 1 | 2 | 4 | j → 2, exceeds bound; loop ends |
| 7 | 2 | 3 | 6 | 1 | 2 | 4 | 4 > 3 → True |
| 8 | 2 | 3 | 6 | 1 | 2 | 5 | t = 4 ^ 1 = 5 |
| 11 | 2 | 3 | 6 | 1 | 2 | 5 | if-block ends (lines 9, 10 skipped) |
| 12 | 2 | 3 | 6 | 1 | 2 | 5 | Print 5 |

**Answer: 5**

### Example 5 — Halving the main diagonal inside a row-sum loop

```
1  Integer arr[2][2] = {{2,4},{6,8}}
2  Integer i, s
3  s = 0
4  For i = 0 to 1
5     arr[i][i] = arr[i][i] / 2
6     s = s + arr[i][0] + arr[i][1]
7  End For
8  Print s
```

| Line | i | arr[0][0] | arr[0][1] | arr[1][0] | arr[1][1] | s | Note |
|---|---|---|---|---|---|---|---|
| 1 | – | 2 | 4 | 6 | 8 | – | array initialised |
| 2 | – | 2 | 4 | 6 | 8 | – | i, s declared |
| 3 | – | 2 | 4 | 6 | 8 | 0 | s = 0 |
| 4 | 0 | 2 | 4 | 6 | 8 | 0 | i = 0 |
| 5 | 0 | 1 | 4 | 6 | 8 | 0 | arr[0][0] = 2 / 2 = 1 |
| 6 | 0 | 1 | 4 | 6 | 8 | 5 | s = 0 + arr[0][0] + arr[0][1] = 0 + 1 + 4 |
| 7 | 1 | 1 | 4 | 6 | 8 | 5 | End For: i → 1 |
| 4 | 1 | 1 | 4 | 6 | 8 | 5 | loop body |
| 5 | 1 | 1 | 4 | 6 | 4 | 5 | arr[1][1] = 8 / 2 = 4 |
| 6 | 1 | 1 | 4 | 6 | 4 | 15 | s = 5 + arr[1][0] + arr[1][1] = 5 + 6 + 4 |
| 7 | 2 | 1 | 4 | 6 | 4 | 15 | i → 2, exceeds bound; loop ends |
| 8 | 2 | 1 | 4 | 6 | 4 | 15 | Print 15 |

**Answer: 15**

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid |
|---|---|---|
| Assuming 1-based indexing | School maths notation starts at 1; pseudocode here starts at 0, so `arr[2][2]` has valid indices 0 and 1 only | Read the declaration first: `arr[R][C]` means rows 0..R−1 and columns 0..C−1; index 2 in a 2×2 is out of bounds |
| Writing `arr[j][i]` instead of `arr[i][j]` | Both are syntactically valid and both in range for a square array, so nothing errors — the answer is just silently wrong | Chant "row first, column second". In nested loops the outer counter is always the row |
| Treating `&` as `&&` (or `\|` as `\|\|`) | `2 && 4` is 1, but `2 & 4` is 0; the two give opposite-looking results on the same inputs | `&&`/`\|\|` return only 0 or 1 as a truth value; `&`/`\|`/`^` combine the individual bits of the numbers |
| Re-using an array element assuming it still holds its initial value | Line 5 may have overwritten `arr[i][i]`; later lines and the final `Print` see the new value | Trace with the element columns in the table, not from memory of the declaration line |
| Ignoring integer-division truncation | `5 / 2` is 2, not 2.5; a half-integer answer anywhere means a wrong final print | Do every `/` with integer values and drop the fraction immediately, before adding anything to it |
| Reading `For i = 0 to n` as "n iterations" | The `to` bound is inclusive, so it runs n + 1 times | Count the loop rows explicitly in the trace rather than multiplying in your head |
| Evaluating mixed bitwise/arithmetic expressions strictly left to right | `^` binds looser than `+` and `*`, so `arr[0][0] ^ 2 + arr[0][0]` is not `(arr[0][0] ^ 2) + arr[0][0]` | Where brackets are given, use them; where they are not, apply precedence: `* / + -` first, then `<< >>`, then `< >`, then `== !=`, then `&`, then `^`, then `\|` |
| Assuming `arr[i][i]` or a diagonal covers the whole array | A diagonal touches only `min(R, C)` cells, but the `Print` may sum all elements | Separate "cells touched by the loop" from "cells read by the Print" and list them explicitly |

## 7. Practice questions

**1. [Easy]** *(B3 — 1D indexing and the second-element trap)*

In pseudocode, `Integer arr[5] = {7, 3, 9, 2, 5}` uses zero-based indexing. Which statement correctly extracts the **second** element of `arr`?

(a) `arr[5]` gives 5
(b) `arr[2]` gives 9
(c) `arr[0]` gives 7
(d) `arr[1]` gives 3

**2. [Medium]** *(B3 — 2D nested traversal)*

```
1  Integer arr[2][2] = {{0,1},{4,1}}
2  Integer i, j, s
3  s = 0
4  For(i = 0; i < 2; i = i + 1)
5      For(j = 0; j < 2; j = j + 1)
6          s = s + arr[i][j]
7      End For
8  End For
9  Print s
```

(a) 5
(b) 7
(c) 6
(d) 10

**3. [Medium]** *(B3 — bitwise condition on array elements)*

```
1  Integer arr[2][2] = {{0,1},{4,1}}
2  Integer t
3  If((3 & arr[1][1]) < (arr[1][0] + 1))
4      t = arr[0][1] + arr[1][0]
5  Else
6      t = arr[0][0] + arr[1][1]
7  End If
8  Print t
```

(a) 1
(b) 5
(c) 4
(d) 6

**4. [Medium]** *(B3 — assignment with XOR then a sum Print)*

```
1  Integer arr[2][2] = {{0,1},{4,1}}
2  arr[0][0] = (arr[0][0] ^ 2) + arr[0][0]
3  arr[0][1] = arr[0][1] + arr[0][0]
4  Print arr[0][0] + arr[0][1] + arr[1][0] + arr[1][1]
```

(a) 8
(b) 6
(c) 10
(d) 12

**5. [Hard]** *(B3 — while loop over a 2D diagonal)*

```
1  Integer arr[2][2] = {{0,1},{4,1}}
2  Integer i = 0
3  While(i < 2)
4      arr[i][i] = arr[i][i] + arr[i][1 - i]
5      i = i + 1
6  End While
7  Print arr[0][0] + arr[1][1]
```

(a) 2
(b) 5
(c) 6
(d) 1

**5. Correct: (c) 6**

| i | Body | arr[0][0] | arr[1][1] |
|---|---|---|---|
| 0 | `arr[0][0] = 0 + arr[0][1] = 0 + 1` | 1 | 1 |
| 1 | `arr[1][1] = 1 + arr[1][0] = 1 + 4` | 1 | 5 |
| Print | `1 + 5` | | 6 |

- (a) 2 — loop runs only for `i = 0`; `arr[1][1]` stays 1, so `1 + 1`.
- (b) 5 — first iteration skipped; `0 + (1 + 4)`.
- (d) 1 — loop never executes; original diagonal `0 + 1`.

---

**6. [Hard]** *(B3 — 1D in-place reversal, then index read)*

```
1  Integer arr[6] = {1, 2, 3, 4, 5, 6}
2  Integer i, t
3  For(i = 0; i < 3; i = i + 1)
4      t = arr[i]
5      arr[i] = arr[5 - i]
6      arr[5 - i] = t
7  End For
8  Print arr[1] + arr[4]
```

(a) 6
(b) 7
(c) 3
(d) 5

---

**6. Correct: (b) 7**

| i | Swap | arr after iteration |
|---|---|---|
| 0 | `arr[0] ↔ arr[5]` | {6, 2, 3, 4, 5, 1} |
| 1 | `arr[1] ↔ arr[4]` | {6, 5, 3, 4, 2, 1} |
| 2 | `arr[2] ↔ arr[3]` | {6, 5, 4, 3, 2, 1} |
| Print | `arr[1] + arr[4] = 5 + 2` | 7 |

- (a) 6 — Print reads `arr[1] + arr[5]` = `5 + 1`.
- (d) 5 — swap treated as a no-op; original `arr[1] + arr[4]` = `2 + 3`.
- (c) 3 — Print reads `arr[4] + arr[5]` = `2 + 1`.

---

7. For `Integer A[5] = {8, 3, 7, 1, 9}`, which expression gives the second element?  
**[Easy]** *(B3 — 1D indexing)*  
(a) `A[0]`  
(b) `A[1]`  
(c) `A[2]`  
(d) `A[5]`

**7. (b) `A[1]`**  
- (a) `A[0]` is the first element, `8`.  
- (c) `A[2]` is the third element, `7`.  
- (d) `A[5]` is out of bounds; valid indices are `0` to `4`.

---

8. What is printed?  
**[Medium]** *(B3 — 2D indexing + bitwise condition)*  
```
7. Integer arr[2][2] = {{0,1},{4,1}}
8. Integer sum = 0
9. If((3 & arr[1][1]) < (arr[1][0] + 1))
10.     arr[0][0] = (arr[0][0] ^ 2) + arr[0][0]
11. End If
12. sum = arr[0][0] + arr[0][1]
13. Print sum
```
(a) 1
(b) 5
(c) 3
(d) 2

**8. (c) 3**  
| Variable | Value |
|---|---|
| `arr[1][1]` | 1 |
| `3 & arr[1][1]` | 1 |
| `arr[1][0] + 1` | 5 |
| `arr[0][0]` after line 4 | `(0 ^ 2) + 0 = 2` |
| `sum` | `2 + 1 = 3` |
- (a) 1: assumes condition is false, so no update.  
- (d) 2: prints only `arr[0][0]`.  
- (b) 5: adds `arr[0][1] + arr[1][0] = 1 + 4`.

---

9. What is printed?  
**[Medium]** *(B3 — nested 2D traversal)*  
```
7. Integer M[3][2] = {{2,5},{4,1},{6,3}}
8. Integer s = 0
9. For i = 0 to 2
10.     For j = 0 to 1
11.         s = s + M[i][j]
12.     End For
13. End For
14. Print s
```
(a) 18
(b) 12
(c) 21
(d) 27

**9. (c) 21**  
| `i` | `j` | `M[i][j]` | `s` |
|---|---|---|---|
| 0 | 0 | 2 | 2 |
| 0 | 1 | 5 | 7 |
| 1 | 0 | 4 | 11 |
| 1 | 1 | 1 | 12 |
| 2 | 0 | 6 | 18 |
| 2 | 1 | 3 | 21 |
- (b) 12: stops after row `i = 1`.  
- (a) 18: omits the last element `M[2][1] = 3`.  
- (d) 27: double-counts the first row `{2,5}`.

---

10. What is printed?  
**[Medium]** *(B3 — 1D traversal with condition)*  
```
7. Integer A[5] = {3, 1, 4, 2, 0}
8. Integer x = 0
9. For i = 0 to 4
10.     If(A[i] > i)
11.         x = x + A[i]
12.     End If
13. End For
14. Print x
```
(a) 4  
(b) 7  
(c) 8  
(d) 10

**10. (b) 7**  
| `i` | `A[i]` | `A[i] > i` | `x` |
|---|---|---|---|
| 0 | 3 | true | 3 |
| 1 | 1 | false | 3 |
| 2 | 4 | true | 7 |
| 3 | 2 | false | 7 |
| 4 | 0 | false | 7 |
- (a) 4: adds only `A[2]`, misses `A[0]`.  
- (c) 8: uses `>=` instead of `>`, so also adds `A[1] = 1`.  
- (d) 10: sums all positive values, ignoring `A[i] > i`.

---

11. What is printed?  
**[Hard]** *(B3 — 2D assignment + bitwise)*  
```
7. Integer arr[2][2] = {{0,1},{4,1}}
8. Integer a = arr[1][1]
9. If((arr[0][1] + a) > (arr[1][0] - 1))
10.     arr[1][1] = (arr[1][0] & 3) + arr[0][0]
11. Else
12.     arr[0][0] = (arr[0][0] ^ 3) + 1
13. End If
14. arr[0][0] = arr[0][0] + arr[1][1]
15. Print arr[0][0] + arr[1][0]
```
(a) 4
(b) 8
(c) 5
(d) 9

**11. (d) 9**  
| Step | Value |
|---|---|
| `a` | 1 |
| Condition | `(1+1) > (4-1)` → `2 > 3` false |
| Line 6 | `arr[0][0] = (0 ^ 3) + 1 = 4` |
| Line 8 | `arr[0][0] = 4 + arr[1][1] = 4 + 1 = 5` |
| Print | `5 + arr[1][0] = 5 + 4 = 9` |
- (a) 4: takes true branch and prints `0 + 4`.  
- (c) 5: stops before adding `arr[1][0]`.  
- (b) 8: omits line 8, so prints `4 + 4`.

---

12. What is printed?  
**[Hard]** *(B3 — nested traversal + parity)*  
```
7. Integer A[2][3] = {{1,2,3},{4,5,6}}
8. Integer s = 0
9. For i = 0 to 1
10.     For j = 0 to 2
11.         If((A[i][j] & 1) == 0)
12.             s = s + A[i][j]
13.         Else
14.             s = s + (j + 1)
15.         End If
16.    End For
17. End For
18. Print s
```
(a) 12
(b) 21
(c) 18
(d) 15

---

**12. (c) 18**  
| `i,j` | `A[i][j]` | Branch | `s` |
|---|---|---|---|
| 0,0 | 1 | odd: `+(0+1)` | 1 |
| 0,1 | 2 | even: `+2` | 3 |
| 0,2 | 3 | odd: `+(2+1)` | 6 |
| 1,0 | 4 | even: `+4` | 10 |
| 1,1 | 5 | odd: `+(1+1)` | 12 |
| 1,2 | 6 | even: `+6` | 18 |
- (a) 12: sums only even values.  
- (b) 15: adds `j` for odd values, not `j + 1`.  
- (d) 21: sums all values, ignoring the condition.

---
## 8. Resources

| Resource | Type | Link | Free/Paid | Time | Why this one |
|---|---|---|---|---|---|
| PrepInsta — Accenture pseudocode | Practice set | https://prepinsta.com/accenture/pseudo-code/general-pseudo-code/ | Free | 45 min | Includes array-based output prediction |
| CodeChef — Accenture interview questions | Practice set | https://www.codechef.com/practice/accenture-interview-questions | Free | 45 min | Company-tagged practice |
| GfG — Bitwise operators | Article | https://www.geeksforgeeks.org/cpp/bitwise-operators-in-c-cpp/ | Free | 20 min | Every observed array item contains a bitwise operation |
| `question-banks/QB-T15-B3-arrays-1d-2d.md` | Question bank | (this library) | Free | 40 min | 35 original questions, 2D-with-bitwise heavy |

*All external links verified resolving 2026-09-16.*

## 9. Self-check

- [ ] **Given any `{{a,b},{c,d}}` initialiser I can state all four element values in under 5 seconds**
- [ ] I know the valid index range of an n-element array is 0 to n−1
- [ ] I know the "second element" of a zero-indexed array is at index 1
- [ ] I can evaluate a bitwise expression on array elements inside a guard
- [ ] I correctly handle an element that is assigned from its own current value
- [ ] I can compute the total iterations of a nested 2D traversal
- [ ] I can apply the row-major address formula
- [ ] I scored 9/12 or better on the practice questions

## 10. Sources

**Teaching content (§3–§9)** is adapted from `accenture-prep-final/accenture-prep-library/topics/T15-B3-arrays-1d-2d.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions P12, P15 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `P5`). Confidence **Medium**. Nothing in this file is a published Infosys syllabus.
