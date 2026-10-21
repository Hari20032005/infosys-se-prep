# QB-P10 — Strings — Traversal, Reversal and ASCII Arithmetic

**Pseudocode** · **Tier 4** · 18 questions

Topic file: [`P10-strings-ascii.md`](/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library/pseudocode/P10-strings-ascii.md)

*Adapted from `accenture-prep-final/accenture-prep-library/question-banks/QB-T36-B4-strings-ascii.md`; verified in that library's QA. Questions and answer key are unchanged.*

**How to use this bank.** Attempt every question before opening the key, at the real pace for this section (120 seconds a question). Answer letters are balanced across a–d.

---

**1.** **[Easy]** *(B1 — ASCII anchors)*
Which of the following is the ASCII value of the character `'K'`?
(a) 74
(b) 107
(c) 75
(d) 76

**1. (c) 75**
'A' is 65 and 'K' is 10 letters ahead, so 65 + 10 = 75.

- (a) 74 is the code of 'J'.
- (b) 107 is the code of lowercase 'k'.
- (d) 76 is the code of 'L'.

---

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

**2. (c) 68**
CODE('C') = 67, and 67 + 1 = 68.

| Step | Value |
|---|---|
| CODE('C') | 67 |
| 67 + 1 | 68 |

- (a) 67 is CODE('C') itself, without the +1.
- (b) 69 is 67 + 2.
- (d) `'D'` is the character whose code is 68, but the statement prints `CODE(ch) + 1`, which is the number itself, not the character it stands for.

---

**3.** **[Easy]** *(B1 — case gap)*
What is the value of `CODE('d') - CODE('D')`?
(a) 32
(b) 26
(c) 31
(d) 64

**3. (a) 32**
'd' = 100 and 'D' = 68, so 100 − 68 = 32.

- (b) 26 is the number of letters in the alphabet, not the case gap.
- (c) 31 is one less than the constant case gap.
- (d) 64 is twice the case gap.

---

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
