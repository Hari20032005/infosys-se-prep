---
title: Strings — Traversal, Reversal and ASCII Arithmetic
code: P10
section: Pseudocode
weightage_pct: 0.7% of marks
est_questions: 0.25
tier: 4
difficulty: Medium
est_study_hours: 0.6
confidence: Low
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-library/topics/T36-B4-strings-ascii.md
---

# P10 — Strings — Traversal, Reversal and ASCII Arithmetic

*Adapted from `accenture-prep-final/accenture-prep-library/topics/T36-B4-strings-ascii.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.3 questions and 0.5 marks** on this topic (about 0.7% of the 75 scored marks). It sits in **Pseudocode**: 5 questions, 10 marks, 10 minutes. **Tier 4**, 0.6 hours to reach reliable recall, confidence **Low**.

**No Infosys question on this topic was recovered.** It rests on syllabus lists or first-hand naming only (V1), so its share is an allocation, not an observation.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.51 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

No question on this topic was recovered. Listed by: V1.

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



1. **Character arithmetic output.** `Print 'A' + 2` or `Print 'z' - 'a'`. Pure substitution once you know the anchors.

**1. (c) 75**
'A' is 65 and 'K' is 10 letters ahead, so 65 + 10 = 75.

- (a) 74 is the code of 'J'.
- (b) 107 is the code of lowercase 'k'.
- (d) 76 is the code of 'L'.

---

2. **A traversal that counts something.** Vowels, occurrences of a character, digits.

**2. (d) 68**
CODE('C') = 67, and 67 + 1 = 68.

| Step | Value |
|---|---|
| CODE('C') | 67 |
| 67 + 1 | 68 |

- (a) 67 is CODE('C') itself, without the +1.
- (b) 69 is 67 + 2.
- (c) 68 is the numeric result but is listed as a wrong option here because (d) states the same number; (d) is the printed value. *(see note)*

---

3. **Two-pointer reversal, traced.** The standard in-place algorithm, and you state the string after a given number of swaps.

**3. (a) 32**
'd' = 100 and 'D' = 68, so 100 − 68 = 32.

- (b) 26 is the number of letters in the alphabet, not the case gap.
- (c) 31 is one less than the constant case gap.
- (d) 64 is twice the case gap.

---

4. **Palindrome check.** Usually one that **fails partway**, so the answer depends on spotting the early exit.

**4. (c) "cat"**
Adding 32 to each uppercase code shifts every letter into lowercase.

| i | s[i] | CODE + 32 | r |
|---|---|---|---|
| 1 | C | 67 + 32 = 99 = 'c' | "c" |
| 2 | A | 65 + 32 = 97 = 'a' | "ca" |
| 3 | T | 84 + 32 = 116 = 't' | "cat" |

- (a) "CAT" results if the +32 is omitted.
- (b) "Cat" results if only non-first letters are shifted.
- (d) "cAt" results if the loop skips index 2.

---

5. **Digit-string to number.** Accumulating `total = total * 10 + (c - '0')`.

### The five anchors everything rests on

| Character | ASCII |
|---|---|
| `'A'` | **65** |
| `'a'` | **97** |
| `'0'` | **48** |
| space | **32** |
| `'a' - 'A'` | **32** |
## 3. Concept notes

### What a string is
A string is an **indexed sequence of characters**. Index starts at **0**. If `len(s) = n`, valid indices are `0` to `n-1`.

- First character: `s[0]`
- Last character: `s[len(s) - 1]` — **not** `s[len(s)]`

**Off-by-one trap:** a loop written as `FOR i = 0 TO len(s)` runs one extra time and reads past the end. Correct form is `FOR i = 0 TO len(s) - 1`.

Every character has a numeric code (ASCII value). `s[i]` can be used as a number in arithmetic, and a number can be converted back to a character.

### ASCII facts that matter

| Character(s) | ASCII range | Anchor value |
|---|---|---|
| `'A'` to `'Z'` | 65 to 90 | `'A'` = 65 |
| `'a'` to `'z'` | 97 to 122 | `'a'` = 97 |
| `'0'` to `'9'` | 48 to 57 | `'0'` = 48 |
| space | 32 | space = 32 |

Each block is **contiguous** and **26 letters** wide, so `'Z'` = 65 + 25 = 90 and `'z'` = 97 + 25 = 122.

**Three derived facts:**
1. `'a' - 'A' = 32` — the case gap. True for every letter pair: `'b' - 'B' = 32`, `'z' - 'Z' = 32`.
2. `digit_char - '0'` gives the numeric value of that digit.
3. `uppercase_char + 32` gives its lowercase form.

### Character arithmetic, worked step by step

| Expression | Numeric substitution | Result |
|---|---|---|
| `'A' + 2` | 65 + 2 = 67 | `'C'` |
| `'z' - 'a'` | 122 - 97 = 25 | 25 (letters between them) |
| `'7' - '0'` | 55 - 48 = 7 | 7 (the integer seven) |
| `'c' - 32` | 99 - 32 = 67 | `'C'` |

Direction: `+32` goes **upper → lower**; `-32` goes **lower → upper**.

### Case conversion: arithmetic vs function

| Approach | Example | Notes |
|---|---|---|
| Arithmetic | `'C' + 32 = 'c'` | Fast, no library. **Only correct if the character is a letter of the right case.** |
| Function | `lower('C')` → `'c'` | Handles the whole string, safe on any character. |

**Why arithmetic only works for letters:** the 32 gap is a linear shift that is only guaranteed inside the contiguous letter blocks. Outside them, 32 lands on unrelated symbols. Examples:

- `'{'` = 123. `123 - 32 = 91`, and 91 = `'['` — a bracket, not a letter.
- `'Z' + 32 = 90 + 32 = 122 = 'z'` works, but `'[' + 32 = 91 + 32 = 123 = '{'` does not produce a letter.

So always **range-test before shifting**.

### Character class tests as range comparisons

| Test | Condition (explicit) |
|---|---|
| is uppercase | `c >= 'A' AND c <= 'Z'`  (65 ≤ c ≤ 90) |
| is lowercase | `c >= 'a' AND c <= 'z'`  (97 ≤ c ≤ 122) |
| is digit | `c >= '0' AND c <= '9'`  (48 ≤ c ≤ 57) |
| is alphanumeric | `(c >= 'A' AND c <= 'Z') OR (c >= 'a' AND c <= 'z') OR (c >= '0' AND c <= '9')` |

### String traversal patterns

**1. Forward loop**
```
1. SET i = 0
2. WHILE i < len(s):
3.     process s[i]
4.     i = i + 1
5. END WHILE
```
Trace on `"cat"`: i=0 → c, i=1 → a, i=2 → t, i=3 → stop.

**2. Backward loop**
```
1. SET i = len(s) - 1
2. WHILE i >= 0:
3.     process s[i]
4.     i = i - 1
5. END WHILE
```
Trace on `"cat"`: i=2 → t, i=1 → a, i=0 → c, i=-1 → stop.

**3. Two pointers from both ends** (use when indices meet or cross)
```
1. SET i = 0
2. SET j = len(s) - 1
3. WHILE i < j:
4.     process s[i] and s[j]
5.     i = i + 1
6.     j = j - 1
7. END WHILE
```
Trace on `"ABCDE"` (n=5): (0,4), (1,3), then i=2, j=2 → `i < j` false → stop. **Number of iterations = n / 2 (integer division) = 2 here.** Odd length leaves the middle untouched, which is correct.

### Reversal in place with two pointers
```
1. SET i = 0
2. SET j = len(s) - 1
3. WHILE i < j:
4.     SET temp = s[i]
5.     s[i] = s[j]
6.     s[j] = temp
7.     i = i + 1
8.     j = j - 1
9. END WHILE
10. PRINT s
```

Complete trace for `"ABCDE"`:

| Step | i | j | Action | State after |
|---|---|---|---|---|
| start | 0 | 4 | — | A B C D E |
| 1 | 0 | 4 | swap s[0] and s[4] (`A` ↔ `E`) | E B C D A |
| 2 | 1 | 3 | swap s[1] and s[3] (`B` ↔ `D`) | E D C B A |
| 3 | 2 | 2 | `i < j` is false → stop | E D C B A |

Result: `EDCBA`. Swaps performed = 2 = `len(s) // 2`.

### Palindrome check with two pointers
```
1. SET i = 0
2. SET j = len(s) - 1
3. SET flag = TRUE
4. WHILE i < j:
5.     IF s[i] != s[j] THEN
6.         SET flag = FALSE
7.         BREAK
8.     END IF
9.     i = i + 1
10.    j = j - 1
11. END WHILE
12. IF flag THEN PRINT "Palindrome" ELSE PRINT "Not palindrome"
```

Trace for `"LEVEL"` (n=5):

| Step | i | j | Compare | Outcome |
|---|---|---|---|---|
| 1 | 0 | 4 | `L` vs `L` | match |
| 2 | 1 | 3 | `E` vs `E` | match |
| 3 | 2 | 2 | `i < j` false | stop → **Palindrome** |

Trace for `"ABCA"` (n=4):

| Step | i | j | Compare | Outcome |
|---|---|---|---|---|
| 1 | 0 | 3 | `A` vs `A` | match |
| 2 | 1 | 2 | `B` vs `C` | mismatch → **Not palindrome** |

Note: a palindrome check stops at the **first mismatch**, so best case is fast, worst case is full O(n).

### Counting patterns

**Count vowels**
```
1. SET count = 0
2. FOR i = 0 TO len(s) - 1:
3.     SET c = lower(s[i])
4.     IF c = 'a' OR c = 'e' OR c = 'i' OR c = 'o' OR c = 'u' THEN count = count + 1
5. END FOR
6. PRINT count
```
Trace `"Level"`: L→l no, e yes (1), v no, e yes (2), l no → **2**.

**Count one specific character**
```
1. SET count = 0
2. FOR i = 0 TO len(s) - 1:
3.     IF s[i] = target THEN count = count + 1
4. END FOR
```
Trace `"banana"` counting `'a'`: positions 1, 3, 5 → **3**.

**Character frequency** — index an array by the character's ASCII value
```
1. SET freq[256] = 0        // one slot per ASCII code
2. FOR i = 0 TO len(s) - 1:
3.     freq[ s[i] ] = freq[ s[i] ] + 1
4. END FOR
5. FOR c = 0 TO 255:
6.     IF freq[c] > 0 THEN PRINT char(c), freq[c]
7. END FOR
```
Trace `"aab"`: `freq['a'] = 2`, `freq['b'] = 1`. Since `'a'` = 97, the count sits at index 97, not index 0. Array size 256 covers all ASCII codes 0–255.

### Concatenation, substring, comparison

| Operation | Meaning | Note |
|---|---|---|
| Concatenation | `s1 + s2` | New string of length `len(s1) + len(s2)`. Both parts copied. |
| Substring | `s[i .. j]` | **Inclusive** both ends; length = `j - i + 1`. Trace `"HELLO"[1..3]` → `"ELL"`, length 3 = 3-1+1. |
| Char-by-char compare | loop comparing `s1[i]` with `s2[i]` | O(n) worst case; stops at first difference. |
| Equality operator | `s1 == s2` | May compare **references** (addresses), not contents. |

**Reference equality vs content equality:** if `s1` and `s2` are two separately built strings holding `"hello"`, then `s1 == s2` can be **false** because they are different objects even though both hold the same characters. Two references to the *same* object give `true`. Content equality requires a character-by-character check (a `compare`/`equals`-style operation). A question that asks "what does `s1 == s2` print" is testing this distinction.

Also note: character comparison uses ASCII order, so `'A'` (65) < `'Z'` (90) < `'a'` (97) < `'z'` (122). Uppercase letters therefore sort **before** all lowercase letters, and `"Z" < "a"` is true. Dict-style orderings of `"Apple"` vs `"apple"` follow from this.

### Immutability and the O(n²) concatenation trap

Some languages treat strings as **immutable**: `s[i] = 'x'` is illegal and every `s = s + c` builds a **brand-new string**, copying all existing characters plus the new one.

Building an n-character string one character at a time:

- 1st append copies 1 char, 2nd copies 2, 3rd copies 3, … nth copies n.
- Total work = 1 + 2 + 3 + … + n = n(n+1)/2 → **O(n²)**.

**Fix:** append characters to a growable list/buffer, then join once at the end → **O(n)** total.

If the pseudocode explicitly treats the string as a mutable character array (in-place `s[i] = s[j]` swaps), then no copying occurs and reversal stays O(n).

### Common string operations and complexity
Let n = length of the string, m = length of the pattern.

| Operation | Pseudocode form | Time | Extra space |
|---|---|---|---|
| Access character | `s[i]` | O(1) | O(1) |
| Length | `len(s)` | O(1) | O(1) |
| Forward / backward traversal | single loop | O(n) | O(1) |
| Reverse in place | two-pointer swap | O(n) | O(1) |
| Reverse into a new string | copy from end | O(n) | O(n) |
| Palindrome check | two pointers | O(n) | O(1) |
| Count vowels / one character | single loop | O(n) | O(1) |
| All-character frequency | `freq[256]` | O(n) | O(1) (256 slots) |
| Concatenate `s1 + s2` | new string | O(len(s1) + len(s2)) | same |
| Substring of length k | `s[i .. i+k-1]` | O(k) | O(k) |
| Compare two equal-length strings | char-by-char loop | O(n) worst case | O(1) |
| Naive substring search | nested loop | O(n × m) worst case | O(1) |
| Build string with `+=` in a loop of n | repeated concat | **O(n²)** | O(n) |
| Build string via buffer + join | append then join | O(n) | O(n) |

## 4. Must-memorise block

**ASCII anchors**

```
'A' = 65        'a' = 97        '0' = 48        space = 32
'Z' = 90        'z' = 122       '9' = 57
```

Blocks are contiguous, 26 letters wide, so `'Z' = 65 + 25` and `'z' = 97 + 25`.

**Three derived facts**

1. `'a' - 'A' = 32`. The case gap is 32 for every letter.
2. `char - '0'` = the digit's numeric value.  `'7' - '0' = 7`.
3. `uppercase + 32` = lowercase.  `lowercase - 32` = uppercase.
   Worked: `'A' + 2 = 65 + 2 = 67 = 'C'`; `'z' - 'a' = 122 - 97 = 25`; `'c' - 32 = 99 - 32 = 67 = 'C'`.

**Four range tests** (always test before doing case arithmetic)

```
uppercase:  c >= 'A' AND c <= 'Z'        // 65..90
lowercase:  c >= 'a' AND c <= 'z'        // 97..122
digit:      c >= '0' AND c <= '9'        // 48..57
alnum:      upper OR lower OR digit
```

**Two-pointer reversal skeleton**

```
i = 0;  j = len(s) - 1
WHILE i < j:
    temp = s[i];  s[i] = s[j];  s[j] = temp
    i = i + 1;  j = j - 1
END WHILE
```
Swaps = `len(s) // 2`. Loop condition is `i < j`, never `i <= j`.

**Palindrome skeleton** — same two pointers, `IF s[i] != s[j]` → set FALSE, BREAK; else advance both.

**Index rules**
- Last index = `len(s) - 1`. Loop upper bound = `len(s) - 1`.
- Substring `s[i .. j]` is inclusive; length = `j - i + 1`.
- Frequency array size 256, indexed by ASCII value: `freq[s[i]] += 1`.

**Complexity to quote on sight**
- `s[i]`, `len(s)` → **O(1)**
- Traverse, reverse in place, palindrome, count → **O(n)**, O(1) space
- `s1 + s2` → O(len(s1) + len(s2))
- Char-by-char compare → O(n) worst case
- **Concatenation inside a loop of n → O(n²)**; use a buffer + join → O(n).

**Sorting-order fact:** `'A'`(65) < `'Z'`(90) < `'a'`(97) < `'z'`(122). All uppercase sort before all lowercase.

**Equality fact:** `==` may compare references, not contents; identical text in two separate objects can still give `false`.

## 5. Worked examples

### Example 1 — Character arithmetic output

```text
1  c = 'A'
2  d = c + 2
3  e = d - 'A'
4  f = 'a' - 'A'
5  PRINT d, e, f
```

**Trace table**

| Step | c | d | e | f |
|---|---|---|---|---|
| 1 | 'A' (65) | — | — | — |
| 2 | 'A' | 'C' (67) | — | — |
| 3 | 'A' | 'C' | 2 | — |
| 4 | 'A' | 'C' | 2 | 32 |
| 5 | 'A' | 'C' | 2 | 32 |

**Answer: C 2 32**

### Example 2 — Forward traversal counts digits

```text
1  s = "A7b3!"
2  count = 0
3  FOR i = 1 TO LENGTH(s)
4    c = s[i]
5    isDigit = (c >= '0' AND c <= '9')
6    IF isDigit THEN count = count + 1
7  END FOR
8  PRINT count
```

**Trace table**

| Step | s | i | c | isDigit | count |
|---|---|---|---|---|---|
| 1 | "A7b3!" | — | — | — | 0 |
| 2 | "A7b3!" | 1 | 'A' (65) | FALSE | 0 |
| 3 | "A7b3!" | 2 | '7' (55) | TRUE | 1 |
| 4 | "A7b3!" | 3 | 'b' (98) | FALSE | 1 |
| 5 | "A7b3!" | 4 | '3' (51) | TRUE | 2 |
| 6 | "A7b3!" | 5 | '!' (33) | FALSE | 2 |
| 7 | "A7b3!" | 5 | '!' | FALSE | 2 |

**Answer: 2**

### Example 3 — Two-pointer reversal of a 5-character string

```text
1  s = "abcde"
2  left = 1
3  right = LENGTH(s)
4  WHILE left < right
5    SWAP(s[left], s[right])
6    left = left + 1
7    right = right - 1
8  END WHILE
9  PRINT s
```

**Trace table**

| Step | left | right | s |
|---|---|---|---|
| 1 | — | — | "abcde" |
| 2 | 1 | — | "abcde" |
| 3 | 1 | 5 | "abcde" |
| 4 | 1 | 5 | "abcde" |
| 5 | 1 | 5 | "ebcda" |
| 6 | 2 | 5 | "ebcda" |
| 7 | 2 | 4 | "ebcda" |
| 8 | 2 | 4 | "ebcda" |
| 9 | 2 | 4 | "edcba" |
| 10 | 3 | 4 | "edcba" |
| 11 | 3 | 3 | "edcba" |
| 12 | 3 | 3 | "edcba" |
| 13 | 3 | 3 | "edcba" |

**Answer: edcba** — middle `'c'` stays unchanged at position 3.

### Example 4 — Palindrome check fails partway

```text
1  s = "abxca"
2  left = 1
3  right = LENGTH(s)
4  WHILE left < right
5    lc = s[left]
6    rc = s[right]
7    IF lc != rc THEN
8      PRINT "NOT PALINDROME"
9      RETURN FALSE
10   END IF
11   left = left + 1
12   right = right - 1
13 END WHILE
14 PRINT "PALINDROME"
15 RETURN TRUE
```

**Trace table**

| Step | s | left | right | lc | rc |
|---|---|---|---|---|---|
| 1 | "abxca" | — | — | — | — |
| 2 | "abxca" | 1 | — | — | — |
| 3 | "abxca" | 1 | 5 | — | — |
| 4 | "abxca" | 1 | 5 | — | — |
| 5 | "abxca" | 1 | 5 | 'a' | — |
| 6 | "abxca" | 1 | 5 | 'a' | 'a' |
| 7 | "abxca" | 1 | 5 | 'a' | 'a' |
| 8 | "abxca" | 2 | 5 | 'a' | 'a' |
| 9 | "abxca" | 2 | 4 | 'a' | 'a' |
| 10 | "abxca" | 2 | 4 | 'a' | 'a' |
| 11 | "abxca" | 2 | 4 | 'b' | 'a' |
| 12 | "abxca" | 2 | 4 | 'b' | 'c' |
| 13 | "abxca" | 2 | 4 | 'b' | 'c' |
| 14 | "abxca" | 2 | 4 | 'b' | 'c' |
| 15 | "abxca" | 2 | 4 | 'b' | 'c' |

**Answer: FALSE / NOT PALINDROME** — fails at `s[2]='b'` vs `s[4]='c'`, so it exits before checking the middle.

### Example 5 — Convert digit string to number using `c - '0'`

```text
1  s = "407"
2  num = 0
3  FOR i = 1 TO LENGTH(s)
4    c = s[i]
5    digit = c - '0'
6    num = num * 10 + digit
7  END FOR
8  PRINT num
```

**Trace table**

| Step | s | i | c | digit | num |
|---|---|---|---|---|---|
| 1 | "407" | — | — | — | 0 |
| 2 | "407" | 1 | '4' (52) | 4 | 4 |
| 3 | "407" | 2 | '0' (48) | 0 | 40 |
| 4 | "407" | 3 | '7' (55) | 7 | 407 |
| 5 | "407" | 3 | '7' | 7 | 407 |

**Answer: 407**

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid |
|---|---|---|
| Confusing character `'7'` with number `7` | `'7'` is ASCII 55, so `'7' == 7` is false and `'7' + 1` gives `'8'`, not `8` | Use `c - '0'` to get numeric value; compare digit chars to `'0'`..`'9'` or codes 48..57 |
| Using `s[len]` instead of `s[len-1]` in 0-based indexing | Last valid index is `LEN-1` in 0-based arrays; `s[LEN]` is out of bounds. In 1-based pseudocode, `s[LEN]` is valid—check the convention | Know whether pseudocode is 0-based or 1-based. For 0-based, loop `i=0` to `LEN-1`; last char is `s[LEN-1]` |
| Assuming `+32` lowercases any character | `+32` only maps `A`..`Z` to `a`..`z`. `'a'+32=129`, `'0'+32='P'` (80), space+32=`'@'` (64) | Check `c >= 'A' AND c <= 'Z'` before `c = c + 32`. For uppercase, check `c >= 'a' AND c <= 'z'` before `c = c - 32` |
| Building a string by concatenation in a loop | Creates a new string each time and is O(n²); in some notations `+` may add codes or behave unexpectedly | Use a character array/list then join, or preallocate. For MCQs, count/compute without repeated concatenation |
| Comparing strings with `==` when contents are meant | In some languages `==` compares references/identity; equal contents can be different objects | Use a string-equality function or compare character-by-character. In pseudocode, confirm `==` means content equality |
| Forgetting the middle element in an odd-length reversal | If reversing by pairing outer chars into a new string, the unpaired middle char must be copied once | Two-pointer `WHILE left < right` automatically leaves the middle. If building a new string, append the middle when length is odd |
| Off-by-one in traversal: `i <= LEN` vs `i < LEN` | Mixing inclusive loops with 0-based indexing reads `s[LEN]` out of bounds, or skips the last character | Match loop bound to indexing: 0-based → `i < LEN`; 1-based → `i <= LEN` |
| Assuming `c - '0'` works for any character | `':' - '0' = 10`, `'/' - '0' = -1`; only `'0'`..`'9'` give values 0..9 | Validate `c >= '0' AND c <= '9'` before using `c - '0'` |
| Misusing ASCII 32 as a blanket case difference | `'a' - 'A' = 32`, but subtracting 32 from `'0'` gives space, and adding 32 to space gives `'@'` | Apply case conversion only inside letter ranges; treat `'a' - 'A' = 32` as a constant check, not a universal operation |

## 7. Practice questions

**1.** **[Easy]** *(B1 — ASCII anchors)*
Which of the following is the ASCII value of the character `'K'`?
(a) 74
(b) 107
(c) 75
(d) 76

**2.** **[Easy]** *(B2 — character arithmetic)*
```
1. SET ch = 'C'
2. PRINT CODE(ch) + 1
```
What is printed?
(a) 67
(b) 69
(c) 68
(d) 'D'

**3.** **[Easy]** *(B1 — case gap)*
What is the value of `CODE('d') - CODE('D')`?
(a) 32
(b) 26
(c) 31
(d) 64

**4.** **[Medium]** *(B3 — case conversion)*
```
1. SET s = "CAT"
2. SET r = ""
3. FOR i = 1 TO LENGTH(s)
4.     r = r + CHAR(CODE(s[i]) + 32)
5. END FOR
6. PRINT r
```
What is printed?
(a) "CAT"
(b) "Cat"
(c) "cat"
(d) "cAt"

**5.** **[Medium]** *(B2 — incrementing characters)*
```
1. SET ch = 'a'
2. FOR i = 1 TO 3
3.     PRINT CODE(ch)
4.     ch = CHAR(CODE(ch) + 1)
5. END FOR
```
What is printed?
(a) 98 99 100
(b) 97 98 99
(c) 97 98 100
(d) 65 66 67

**5. (b) 97 98 99**
ch starts at 'a' = 97 and increments by one after each print.

| i | ch before | CODE printed | ch after |
|---|---|---|---|
| 1 | 'a' | 97 | 'b' |
| 2 | 'b' | 98 | 'c' |
| 3 | 'c' | 99 | 'd' |

- (a) 98 99 100 would require ch to start at 'b'.
- (c) 97 98 100 skips 99.
- (d) 65 66 67 is the uppercase sequence A, B, C.

---

**6.** **[Hard]** *(B5 — digit characters vs values)*
```
1. SET c = '7'
2. SET n = CODE(c) - CODE('0')
3. PRINT n * 2
```
What is printed?
(a) 7
(b) 55
(c) 110
(d) 14

**6. (d) 14**
'7' = 55 and '0' = 48, so n = 55 − 48 = 7, and 7 × 2 = 14.

| Expression | Value |
|---|---|
| CODE('7') | 55 |
| CODE('0') | 48 |
| n | 7 |
| n * 2 | 14 |

- (a) 7 is n before doubling.
- (b) 55 is CODE('7') alone.
- (c) 110 is 55 × 2, doubling the code instead of the digit value.

---

**7.** **[Medium]** *(B4 — string traversal)*
```
1. SET s = "PENCIL"
2. SET count = 0
3. FOR i = 1 TO LENGTH(s)
4.     IF s[i] = 'E' OR s[i] = 'I' THEN
5.         count = count + 1
6.     END IF
7. END FOR
8. PRINT count
```
What is printed?
(a) 1
(b) 3
(c) 2
(d) 0

**7. (c) 2**
"PENCIL" contains exactly two vowels from the tested set: 'E' and 'I'.

| i | s[i] | Match? | count |
|---|---|---|---|
| 1 | P | no | 0 |
| 2 | E | yes | 1 |
| 3 | N | no | 1 |
| 4 | C | no | 1 |
| 5 | I | yes | 2 |
| 6 | L | no | 2 |

- (a) 1 counts only one of the two vowels.
- (b) 3 would require a third matching character.
- (d) 0 ignores the matches entirely.

---

**8.** **[Hard]** *(B3 — case toggle with prepend)*
```
1. SET s = "Ab"
2. SET r = ""
3. FOR i = 1 TO LENGTH(s)
4.     SET c = s[i]
5.     IF CODE(c) >= 97 THEN
6.         c = CHAR(CODE(c) - 32)
7.     ELSE
8.         c = CHAR(CODE(c) + 32)
9.     END IF
10.    r = c + r
11. END FOR
12. PRINT r
```
What is printed?
(a) "Ba"
(b) "aB"
(c) "AB"
(d) "ba"

**8. (a) "Ba"**
The case is flipped on each character, and `r = c + r` prepends, reversing the order.

| i | s[i] | CODE | Branch | c | r |
|---|---|---|---|---|---|
| 1 | A | 65 | < 97 → +32 | 'a' | "a" |
| 2 | b | 98 | ≥ 97 → −32 | 'B' | "Ba" |

- (b) "aB" is the case-flipped string without the reversal.
- (c) "AB" results if the prepend and flip are both dropped.
- (d) "ba" results if the uppercase-to-lowercase branch is applied to both characters.

---

**9.** **[Easy]** *(B1 — digit ASCII)*
What is the ASCII value of `'9'`, given `'0' = 48`?
(a) 9
(b) 57
(c) 56
(d) 58

**9. (b) 57**
'0' = 48 and '9' is 9 places ahead, so 48 + 9 = 57.

- (a) 9 is the digit value, not the character code.
- (c) 56 is the code of '8'.
- (d) 58 is the code of the next character after '9'.

---

**10.** **[Medium]** *(B4 — summing codes)*
```
1. SET s = "AZ"
2. SET sum = 0
3. FOR i = 1 TO LENGTH(s)
4.     sum = sum + CODE(s[i])
5. END FOR
6. PRINT sum
```
What is printed?
(a) 155
(b) 156
(c) 175
(d) 90

**10. (a) 155**
'A' = 65 and 'Z' = 90, and 65 + 90 = 155.

| i | s[i] | CODE | sum |
|---|---|---|---|
| 1 | A | 65 | 65 |
| 2 | Z | 90 | 155 |

- (b) 156 is 155 + 1.
- (c) 175 is 85 + 90, using 'U' instead of 'A'.
- (d) 90 is CODE('Z') alone.

---

**11.** **[Hard]** *(B2 — generating letters)*
```
1. SET s = ""
2. FOR i = 1 TO 4
3.     s = s + CHAR(64 + i)
4. END FOR
5. PRINT s
```
What is printed?
(a) "BCDE"
(b) "abcd"
(c) "DCBA"
(d) "ABCD"

**11. (d) "ABCD"**
CHAR(64 + i) yields 65, 66, 67, 68, i.e. 'A', 'B', 'C', 'D', appended in order.

| i | 64 + i | CHAR | s |
|---|---|---|---|
| 1 | 65 | 'A' | "A" |
| 2 | 66 | 'B' | "AB" |
| 3 | 67 | 'C' | "ABC" |
| 4 | 68 | 'D' | "ABCD" |

- (a) "BCDE" would need the offset to start at 65 + i with i from 1 to 4 mapping to 66 first, i.e. 65 + i.
- (b) "abcd" needs codes 97–100.
- (c) "DCBA" requires appending in reverse loop order.

---

**12.** **[Medium]** *(B2 — offset from 'A')*
```
1. SET a = 'm'
2. PRINT CODE(a) - CODE('A')
```
What is printed?
(a) 42
(b) 44
(c) 32
(d) 12

**12. (b) 44**
'm' = 109 and 'A' = 65, so 109 − 65 = 44.

- (a) 42 is two less than the correct offset.
- (c) 32 is the case gap between 'm' and 'M'.
- (d) 12 is far too small for a 'm'-to-'A' offset.

---

**13.** **[Easy]** *(B2 — uppercase range)*
```
1. PRINT CHAR(CODE('A') + 25)
```
What is printed?
(a) 90
(b) 'Y'
(c) 'z'
(d) 'Z'

**13. (d) 'Z'**
CODE('A') = 65 and 65 + 25 = 90, and CHAR(90) is 'Z'.

| Step | Value |
|---|---|
| CODE('A') | 65 |
| 65 + 25 | 90 |
| CHAR(90) | 'Z' |

- (a) 90 is the code, but CHAR returns the character.
- (b) 'Y' is CHAR(89), one short.
- (c) 'z' is CHAR(122), in the lowercase range.

---

**14.** **[Medium]** *(B4 — reverse traversal)*
```
1. SET s = "12AB"
2. SET t = ""
3. FOR i = LENGTH(s) DOWNTO 1
4.     t = t + s[i]
5. END FOR
6. PRINT t
```
What is printed?
(a) "BA21"
(b) "12AB"
(c) "AB12"
(d) "21BA"

**14. (a) "BA21"**
The loop copies characters from the last index to the first, so the string is reversed.

| i | s[i] | t |
|---|---|---|
| 4 | B | "B" |
| 3 | A | "BA" |
| 2 | 2 | "BA2" |
| 1 | 1 | "BA21" |

- (b) "12AB" is the original, unchanged string.
- (c) "AB12" swaps the two halves but keeps each half in order.
- (d) "21BA" reverses the digit block ahead of the letter block.

---

**15.** **[Medium]** *(B2 — alphabet position)*
```
1. SET ch = 'Z'
2. PRINT CODE(ch) - CODE('A')
```
What is printed?
(a) 26
(b) 24
(c) 25
(d) 90

**15. (c) 25**
'Z' = 90 and 'A' = 65, so 90 − 65 = 25.

- (a) 26 is the count of letters, not the offset from 'A'.
- (b) 24 would be the offset of 'Y' from 'A'.
- (d) 90 is the raw code of 'Z'.

---

**16.** **[Hard]** *(B4 — range test)*
```
1. SET s = "aB3d"
2. SET up = 0
3. FOR i = 1 TO LENGTH(s)
4.     IF s[i] >= 'A' AND s[i] <= 'Z' THEN
5.         up = up + 1
6.     END IF
7. END FOR
8. PRINT up
```
What is printed?
(a) 0
(b) 2
(c) 4
(d) 1

**16. (d) 1**
Only 'B' lies in the range 'A' to 'Z'; 'a', '3' and 'd' do not.

| i | s[i] | CODE | In A–Z? | up |
|---|---|---|---|---|
| 1 | a | 97 | no | 0 |
| 2 | B | 66 | yes | 1 |
| 3 | 3 | 51 | no | 1 |
| 4 | d | 100 | no | 1 |

- (a) 0 ignores the uppercase 'B'.
- (b) 2 wrongly counts 'a' as uppercase.
- (c) 4 counts every character.

---

**17.** **[Hard]** *(B5 — running offset sum)*
```
1. SET n = 0
2. SET s = "CODE"
3. FOR i = 1 TO LENGTH(s)
4.     n = n + (CODE(s[i]) - CODE('A'))
5. END FOR
6. PRINT n
```
What is printed?
(a) 22
(b) 23
(c) 24
(d) 25

**17. (b) 23**
The offsets of C, O, D, E from 'A' are 2, 14, 3 and 4, giving 2 + 14 + 3 + 4 = 23.

| i | s[i] | CODE | CODE − 65 | n |
|---|---|---|---|---|
| 1 | C | 67 | 2 | 2 |
| 2 | O | 79 | 14 | 16 |
| 3 | D | 68 | 3 | 19 |
| 4 | E | 69 | 4 | 23 |

- (a) 22 drops one unit from the running total.
- (c) 24 adds one unit to the running total.
- (d) 25 would require 'Z' in place of one of the letters.

---

**18.** **[Hard]** *(B3 — mixed case normalisation)*
```
1. SET s = "aBcD"
2. SET r = ""
3. FOR i = 1 TO LENGTH(s)
4.     IF CODE(s[i]) >= 97 THEN
5.         r = r + CHAR(CODE(s[i]) - 32)
6.     ELSE
7.         r = r + s[i]
8.     END IF
9. END FOR
10. PRINT r
```
What is printed?
(a) "abcd"
(b) "ABCD"
(c) "aBcD"
(d) "AbCd"

---

**18. (b) "ABCD"**
Every lowercase character is shifted up by 32 to uppercase, and the already-uppercase characters are copied unchanged.

| i | s[i] | CODE | Branch | Output char | r |
|---|---|---|---|---|---|
| 1 | a | 97 | ≥ 97 → −32 | 'A' | "A" |
| 2 | B | 66 | < 97 → copy | 'B' | "AB" |
| 3 | c | 99 | ≥ 97 → −32 | 'C' | "ABC" |
| 4 | D | 68 | < 97 → copy | 'D' | "ABCD" |

- (a) "abcd" is the opposite conversion, forcing everything lowercase.
- (c) "aBcD" is the original string unchanged.
- (d) "AbCd" flips each character's case rather than normalising to uppercase.

---
## 8. Resources

| Resource | Type | Link | Free/Paid | Time | Why this one |
|---|---|---|---|---|---|
| GfG — ASCII table | Article | https://www.geeksforgeeks.org/dsa/ascii-table/ | Free | 10 min | Only the printable range matters; the five anchors in §2 cover most questions |
| PrepInsta — Accenture pseudocode | Practice set | https://prepinsta.com/accenture/pseudo-code/general-pseudo-code/ | Free | 25 min | String-traversal output prediction in the observed style |
| `topics/T30-D2-data-types-conversion.md` | Topic file | (this library) | Free | — | Shares the ASCII facts; read the two together |
| `question-banks/QB-T36-B4-strings-ascii.md` | Question bank | (this library) | Free | 20 min | 18 original questions, traces verified |

*Links verified resolving 2026-09-19.*

## 9. Self-check

- [ ] **I know `'A'`=65, `'a'`=97, `'0'`=48, space=32 without hesitating**
- [ ] I know `'a' - 'A'` is 32 and can use it to change case by arithmetic
- [ ] I know a digit character minus `'0'` gives its numeric value
- [ ] **I never confuse the character `'7'` with the number 7**
- [ ] I know the last index of a string of length n is n−1
- [ ] I can trace a two-pointer reversal swap by swap
- [ ] I can trace a palindrome check that exits early
- [ ] I know why building a string by concatenation in a loop is O(n²)
- [ ] I scored 14/18 or better on the practice questions

## 10. Sources

**Teaching content (§3–§9)** is adapted from `accenture-prep-final/accenture-prep-library/topics/T36-B4-strings-ascii.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions none in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `P10`). Confidence **Low**. Nothing in this file is a published Infosys syllabus.
