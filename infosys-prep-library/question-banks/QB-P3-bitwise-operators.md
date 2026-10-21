# QB-P3 — Bitwise Operators and Operator Precedence

**Pseudocode** · **Tier 2** · 36 questions

Topic file: [`P3-bitwise-operators.md`](/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library/pseudocode/P3-bitwise-operators.md)

*Adapted from `accenture-prep-final/accenture-prep-library/question-banks/QB-T11-B7-bitwise-operators.md`; verified in that library's QA. Questions and answer key are unchanged.*

**How to use this bank.** Attempt every question before opening the key, at the real pace for this section (120 seconds a question). Answer letters are balanced across a–d.

---

**1.** **[Easy]** *(B7 — precedence: `+` binds tighter than `&`)*

```c
int r = 2 + 3 & 6;
printf("%d", r);
```

(a) 4
(b) 0
(c) 5
(d) 6

**1. (a) 4**
`+` has higher precedence than `&`, so the expression evaluates as `(2 + 3) & 6`, i.e. `5 & 6`. In binary `101 & 110 = 100`, which is 4.

- (b) 0 — comes from evaluating `3 & 6 = 2` and then treating `2 + 2` loosely, or from a shifted bit position; the correct grouping is `(2+3) & 6`.
- (c) 5 — this is the value of `2 + 3` itself, produced by ignoring the `& 6` entirely.
- (d) 6 — the result of the left-to-right misread `2 + (3 & 6) = 2 + 2` rounded off, or simply taking the larger operand.

---

**2.** **[Easy]** *(B7 — XOR is self-inverse)*

```c
int x = 13;
x = x ^ 9;
x = x ^ 9;
printf("%d", x);
```

(a) 0
(b) 4
(c) 26
(d) 13

**2. (d) 13**

| step | expression | value |
|---|---|---|
| start | `x` | 13 |
| after `x = x ^ 9` | `13 ^ 9` | 4 |
| after `x = x ^ 9` | `4 ^ 9` | 13 |

XOR is self-inverse: `p ^ q ^ q == p`, so applying the same mask twice restores the original value.

- (a) 0 — assumes the two XORs cancel the variable to zero rather than restoring it.
- (b) 4 — stops after the first XOR and forgets the second one.
- (c) 26 — wrongly treats the second XOR as an addition (`13 + 9 + 4` style reasoning).

---

**3.** **[Easy]** *(B7 — `n & 1` as odd test inside a branch)*

```c
int n = 11;
if (n & 1)
    printf("A");
else
    printf("B");
printf("%d", n >> 1);
```

(a) B5
(b) A5
(c) A6
(d) B6

**3. (b) A5**
`11 & 1` is 1 (11 is odd), so the `if` branch runs and `"A"` is printed. Then `11 >> 1` is `1011 >> 1 = 101 = 5`.

| step | value |
|---|---|
| `n & 1` | 1 → prints `A` |
| `n >> 1` | 5 |

- (a) B5 — assumes `11 & 1` is 0, i.e. confuses the parity of 11.
- (c) A6 — assumes `>> 1` rounds up instead of dropping the low bit.
- (d) B6 — makes both of the above mistakes.

---

**4.** **[Easy]** *(B7 — left and right shifts on small integers)*

```c
int a = 5;
int b = a << 2;
int c = b >> 1;
printf("%d %d", b, c);
```

(a) 40 20
(b) 10 20
(c) 20 5
(d) 20 10

**4. (d) 20 10**
`a << 2` multiplies by 4: `5 << 2 = 20`. Then `20 >> 1` halves it: `20 >> 1 = 10`. Note `c` is computed from `b`, not from the original `a`.

- (b) 10 20 — swaps the two results, as if `c` were computed first.
- (c) 20 5 — computes `c` from the original `a` (`5 >> 1 = 2` rounded up) instead of from `b`.
- (a) 40 20 — doubles instead of quadrupling in the first shift.

---

**5.** **[Medium]** *(B7 — `&` versus `&&`)*

```c
int a = 12, b = 8;
printf("%d %d", a & b, a && b);
```

(a) 1 8
(b) 8 1
(c) 0 1
(d) 8 8

**5. (b) 8 1**
`&` is bitwise AND: `12 = 1100`, `8 = 1000`, so `1100 & 1000 = 1000 = 8`. `&&` is the logical AND, which yields 1 for two non-zero operands.

- (a) 1 8 — swaps the meanings of `&` and `&&`.
- (d) 8 8 — treats `&&` as bitwise too, which would give 8.
- (c) 0 1 — treats `&` as if it were `^` or assumes the bits do not overlap.

---

**6.** **[Medium]** *(B7 — precedence chain `&` > `^` > `|`)*

```c
int r = 1 | 2 ^ 3 & 4;
printf("%d", r);
```

(a) 0
(b) 4
(c) 3
(d) 7

**6. (c) 3**
Precedence is `&` then `^` then `|`. `3 & 4 = 0`; `2 ^ 0 = 2`; `1 | 2 = 3`.

- (a) 0 — evaluates strictly left to right: `1 | 2 = 3`, `3 ^ 3 = 0`, `0 & 4 = 0`.
- (b) 4 — evaluates strictly right to left, ending with `1 | (2 ^ (3 & 4))` mis-simplified to 4.
- (d) 7 — collapses the whole thing into a logical OR of non-zero operands.

---

**7.** **[Medium]** *(B7 — `n & (n - 1)`)*

```c
int n = 100;
printf("%d", n & (n - 1));
```

(a) 0
(b) 4
(c) 96
(d) 100

**7. (c) 96**
`100 = 1100100` and `99 = 1100011`. AND-ing them gives `1100000 = 96`. In general `n & (n-1)` clears the lowest set bit; since 100 has more than one set bit, the result is non-zero and is not 0.

- (a) 0 — assumes `n & (n-1)` is always zero, confusing it with the power-of-two test returning true.
- (b) 4 — the isolated lowest set bit; that would be `n & -n`, not `n & (n-1)`.
- (d) 100 — assumes AND with a nearby number changes nothing.

---

**8.** **[Medium]** *(B7 — XOR swap)*

```c
int a = 7, b = 5;
a ^= b;
b ^= a;
a ^= b;
printf("%d %d", a, b);
```

(a) 2 2
(b) 7 5
(c) 2 7
(d) 5 7

**8. (d) 5 7**
The three-step XOR sequence swaps the variables. `a ^= b` gives `7^5 = 2`; `b ^= a` gives `5^2 = 7`; `a ^= b` gives `2^7 = 5`.

| step | a | b |
|---|---|---|
| start | 7 | 5 |
| `a ^= b` | 2 | 5 |
| `b ^= a` | 2 | 7 |
| `a ^= b` | 5 | 7 |

- (b) 7 5 — the "no swap happened" answer, obtained by assuming the XORs cancel out.
- (c) 2 7 — this is the state after only two of the three statements.
- (a) 2 2 — assumes the final statement re-XORs against the same value rather than the updated one.

---

**9.** **[Medium]** *(B7 — `==` binds tighter than `&` in a guard)*

```c
int n = 12;
if (n & 3 == 0)
    printf("Y");
else
    printf("X");
```

(a) X
(b) No output
(c) XY
(d) Y

**9. (a) X**
Inside `if`, `==` has higher precedence than `&`, so the condition is `n & (3 == 0)`, i.e. `12 & 0`, which is 0 (false). The `else` branch runs and prints `X`. (The source key said (d) Y; compiling and running the code prints X, so the key here is (a).)

- (d) Y — this is what you get if you (incorrectly) group it as `(n & 3) == 0`; `12 & 3 = 0`, which is true, so the `if` branch would print Y.
- (c) XY — no code path prints both.
- (b) No output — the `else` branch always prints something.

---

**10.** **[Medium]** *(B7 — `+` binds tighter than `<<`)*

```c
printf("%d", 1 << 2 + 3);
```

(a) 32
(b) 13
(c) 64
(d) 7

**10. (a) 32**
`+` binds tighter than `<<`, so the shift count is `2 + 3 = 5`: `1 << 5 = 32`.

- (d) 7 — evaluates left to right as `(1 << 2) + 3 = 4 + 3`.
- (b) 13 — evaluates as `(1 << 2) + 3 + 6` style miscalculation, or adds 2 and 3 into the base.
- (c) 64 — uses a shift count of 6, off by one.

---

**11.** **[Hard]** *(B7 — clearing the lowest set bit in a loop)*

```c
int n = 45, c = 0;
while (n) {
    n &= n - 1;
    c++;
}
printf("%d", c);
```

(a) 5
(b) 4
(c) 6
(d) 3

**11. (b) 4**
`n &= n - 1` clears the lowest set bit each pass, so the loop runs exactly once per set bit. `45 = 101101` has four 1-bits.

| iter | n before | n in binary | n & (n-1) | c |
|---|---|---|---|---|
| 1 | 45 | 101101 | 44 | 1 |
| 2 | 44 | 101100 | 40 | 2 |
| 3 | 40 | 101000 | 32 | 3 |
| 4 | 32 | 100000 | 0 | 4 |
| 5 | 0 | — | loop ends | 4 |

- (a) 5 — counts the number of binary digits or the value 45's index, not the set bits.
- (c) 6 — counts all six bit positions of `101101`, including the zeros.
- (d) 3 — drops the leading 1-bit of 45.

---

**12.** **[Hard]** *(B7 — mixed `&`, `^`, `|` precedence)*

```c
int a = 5, b = 6;
printf("%d", a & b ^ a | b);
```

(a) 7
(b) 5
(c) 3
(d) 11

**12. (a) 7**
Precedence is `&` > `^` > `|`. `5 & 6 = 4`; `4 ^ 5 = 1`; `1 | 6 = 7`.

- (c) 3 — evaluates left to right: `5 & 6 = 4`, `4 ^ 5 = 1`, then misapplies the last step as `1 | 2`.
- (b) 5 — takes `a` itself as the result.
- (d) 11 — evaluates as `a & (b ^ c) | b = 5 & 3 | 6` style grouping, ignoring standard precedence.

---

**13.** **[Hard]** *(B7 — power-of-two test used as a branch guard)*

```c
int n = 30;
if ((n & (n - 1)) == 0)
    printf("P2");
else if (n & 1)
    printf("ODD");
else
    printf("OTHER");
```

(a) P2
(b) OTHER
(c) ODD
(d) No output

**13. (b) OTHER**
`n & (n-1)` for `n = 30` is `11110 & 11101 = 11100 = 28`, which is not 0, so 30 is not a power of two. The `else if` then tests `30 & 1`, which is 0 because 30 is even, so the final `else` runs.

- (a) P2 — reached by wrongly concluding 30 is a power of two.
- (c) ODD — reached by believing `30 & 1` is 1.
- (d) No output — an `else` branch always matches here.

---

**14.** **[Hard]** *(B7 — compound assignment with shifts and masks)*

```c
int a = 1;
a <<= 3;
a |= 1 << 1;
a &= ~(1 << 2);
printf("%d", a);
```

(a) 2
(b) 10
(c) 14
(d) 8

**14. (b) 10**
`a = 1`; `a <<= 3` gives 8; `a |= 1 << 1` gives `8 | 2 = 10`; `a &= ~(1 << 2)` clears bit 2, but 10 is `1010` and bit 2 (value 4) is already 0, so `a` stays 10.

| step | a (binary) | a |
|---|---|---|
| `a = 1` | 0001 | 1 |
| `a <<= 3` | 1000 | 8 |
| `a |= 1 << 1` | 1010 | 10 |
| `a &= ~(1 << 2)` | 1010 | 10 |

- (a) 2 — subtracts rather than clears the bit, or stops after the `|=` step.
- (d) 8 — ignores the `|= 1 << 1` statement entirely.
- (c) 14 — treats `&= ~(1 << 2)` as `|= (1 << 2)`, setting bit 2 to give `1110`.

---

**15.** **[Hard]** *(B7 — mask extraction with `&` and `>>`)*

```c
int v = 0xAB;
int mask = 0xF0;
printf("%d", (v & mask) >> 4);
```

(a) 160
(b) 11
(c) 15
(d) 10

**15. (d) 10**
`0xAB = 1010 1011`. AND with `0xF0 = 1111 0000` keeps the high nibble: `1010 0000 = 160`. Shifting right by 4 gives `1010 = 10`.

- (b) 11 — reads the low nibble `1011` instead of the high nibble.
- (c) 15 — assumes the mask keeps all four high bits set to 1.
- (a) 160 — forgets the `>> 4`.

---

**16.** **[Hard]** *(B7 — bitwise inside a logical guard)*

```c
int a = 4, b = 2;
if (a & b || a & 1)
    printf("T");
else
    printf("F");
```

(a) T
(b) Compile error
(c) 0
(d) F

**16. (d) F**
`&` binds tighter than `||`, so the condition is `(a & d) || (a & 1)`. `4 & 2 = 0` and `4 & 1 = 0`, so the whole condition is false and `F` is printed.

- (a) T — assumes `a & b` or `a & 1` is non-zero.
- (c) 0 — `if` prints strings here, never a number.
- (b) Compile error — the expression is valid C; `&` simply binds tighter than `||`.

---

**17.** **[Hard]** *(B7 — shifts on `unsigned char` and truncation)*

```c
unsigned char v = 0x5A;
v = (v >> 4) | (v << 4);
printf("%u", v);
```

(a) 90
(b) 170
(c) 165
(d) 15

**17. (c) 165**
`0x5A = 0101 1010`. `v >> 4 = 5`. `v << 4` promotes to `int` and gives `0x5A0`, i.e. 1440. `5 | 1440 = 1445`. Assigning 1445 back to an `unsigned char` keeps the low 8 bits: `1445 mod 256 = 165` (`0xA5`).

- (a) 90 — this is `0x5A` itself; it comes from seeing the OR as cancelling out, which it does not.
- (b) 170 — shifts only one way (a single nibble swap with the wrong nibble retained).
- (d) 15 — assumes the result is masked down to a nibble.

---

**18.** **[Hard]** *(B7 — XOR combined with a shift)*

```c
int n = 9;
printf("%d", (n >> 1) ^ n);
```

(a) 5
(b) 13
(c) 8
(d) 12

---

**18. (b) 13**
`9 >> 1 = 4`. Then `9 ^ 4`: `1001 ^ 0100 = 1101 = 13`. The expression `n ^ (n >> 1)` is the binary-to-Gray-code conversion.

- (a) 5 — computes `9 >> 1 = 4` and then adds 1.
- (c) 8 — clears the low bit of 9 or halts after the shift.
- (d) 12 — computes `9 | (9 >> 1) = 1001 | 0100 = 1101` incorrectly as 12, or uses AND instead of XOR.

---

**19.** **[Easy]** *(B7 — AND evaluation)*

What is the value of the expression below (integers are small, positive, and fit in a byte)?

```c
printf("%d", 6 & 3);
```

(a) 7
(b) 0
(c) 1
(d) 2

**19. (d) 2**
`6` is `110` and `3` is `011`; AND keeps only the columns set in both, giving `010` = 2.

- (a) 7 is the OR (`6 | 3` = `111`), not the AND.
- (c) 1 comes from counting the number of `1` bits common to both instead of evaluating the bit columns.
- (b) 0 wrongly assumes the two numbers share no set bit at all.

---

**20.** **[Easy]** *(B7 — OR evaluation)*

```c
int a = 5, b = 2;
printf("%d", a | b);
```

(a) 3
(b) 5
(c) 2
(d) 7

**20. (d) 7**
`5` is `101` and `2` is `010`; OR sets a bit if it is set in either operand, giving `111` = 7.

- (a) 3 is the XOR (`5 ^ 2` = `111 ^ 010` = `101`... no; `5 ^ 2` = `101 ^ 010` = `111` = 7 as well; 3 comes from adding the two operands' set-bit counts).
- (b) 5 mistakenly keeps only the left operand.
- (c) 2 mistakenly keeps only the right operand.

---

**21.** **[Easy]** *(B7 — XOR self-inverse)*

```c
int a = 9;
printf("%d", a ^ a);
```

(a) 81
(b) 9
(c) 0
(d) 1

**21. (c) 0**
XOR of any value with itself is 0 because every bit position matches itself.

- (b) 9 results from treating `^` as a no-op.
- (a) 81 results from treating `^` as exponentiation (9²).
- (d) 1 results from confusing bitwise XOR with the relational "not equal".

---

**22.** **[Easy]** *(B7 — left shift)*

```c
printf("%d", 1 << 4);
```

(a) 8
(b) 4
(c) 16
(d) 32

**22. (c) 16**
`1 << 4` shifts the single set bit four positions left: `00000001` → `00010000` = 2⁴ = 16.

- (a) 8 is `1 << 3`.
- (b) 4 is `1 << 2`.
- (d) 32 is `1 << 5`.

---

**23.** **[Medium]** *(B7 — precedence: + binds tighter than &)*

```c
printf("%d", 3 + 4 & 5);
```

(a) 7
(b) 4
(c) 5
(d) 1

**23. (c) 5**
`+` has higher precedence than `&`, so the expression is `(3 + 4) & 5` = `7 & 5` = `111 & 101` = `101` = 5.

- (a) 7 comes from evaluating `3 + (4 & 5)` = `3 + 4` = 7.
- (b) 4 comes from evaluating only `4 & 5` = `100` = 4 and ignoring the `3 +`.
- (d) 1 comes from treating `&` as the logical AND, where both `7` and `5` are non-zero.

---

**24.** **[Medium]** *(B7 — odd test inside a branch guard)*

```c
int n = 12;
if (n & 1)
    printf("odd");
else
    printf("even");
```

(a) Nothing is printed
(b) odd
(c) even
(d) Compile error: `&` cannot be used as a condition

**24. (c) even**
`12 & 1` = `1100 & 0001` = `0`, which is false, so the `else` branch runs and prints `even`.

- (b) odd assumes `n & 1` is true whenever `n` is non-zero, rather than testing bit 0.
- (a) is wrong because the `else` branch always executes when the condition is false.
- (d) is wrong because an integer expression is a valid condition in C; `&` is a normal operator.

---

**25.** **[Medium]** *(B7 — power-of-two test n & (n-1))*

```c
int n = 64;
if (n > 0 && (n & (n - 1)) == 0)
    printf("yes");
else
    printf("no");
```

(a) no
(b) Nothing is printed
(c) yes
(d) Compile error: `n & (n - 1)` is not a valid condition

**25. (c) yes**
For `n = 64`, `n - 1` is 63; `64 & 63` = `1000000 & 0111111` = `0`, so the guard is true and `yes` is printed. The trick is that a power of two has exactly one set bit, and subtracting 1 turns all lower bits on.

- (a) no would be correct only if `n & (n - 1)` were non-zero, which happens for non-powers-of-two such as 6 or 10.
- (b) is wrong because both branches print something.
- (d) is wrong because `(n & (n - 1)) == 0` is a valid logical expression.

---

**26.** **[Medium]** *(B7 — bitwise NOT)*

Assuming a 32-bit `int` and two's-complement representation:

```c
printf("%d", ~5);
```

(a) -5
(b) 4294967290
(c) 250
(d) -6

**26. (d) -6**
On a 32-bit two's-complement `int`, `~5` flips all 32 bits, giving the value `-(5 + 1)` = -6. In general `~x == -x - 1`.

- (a) -5 ignores the `-1` in the identity `~x = -x - 1`.
- (c) 250 is `~5` truncated to 8 bits (`11111010` = 250); the argument is an `int`, so no truncation occurs.
- (b) 4294967290 is the value that would be printed with `%u`; with `%d` the signed value -6 is printed.

---

**27.** **[Medium]** *(B7 — shift associativity)*

```c
printf("%d", 8 << 1 >> 2);
```

(a) 16
(b) 8
(c) 4
(d) 2

**27. (c) 4**
`<<` and `>>` have the same precedence, so evaluation is left to right: `(8 << 1) >> 2` = `16 >> 2` = 4.

- (a) 16 stops after the left shift.
- (b) 8 comes from grouping right to left: `8 << (1 >> 2)` = `8 << 0` = 8.
- (d) 2 comes from dropping the left shift and computing `8 >> 2`.

---

**28.** **[Medium]** *(B7 — AND vs OR vs XOR)*

```c
int x = 12, y = 10;
printf("%d", x & y);
```

(a) 6
(b) 8
(c) 14
(d) 22

**28. (b) 8**
`12` is `1100` and `10` is `1010`; AND keeps only bit 3, giving `1000` = 8.

- (a) 6 is the XOR `12 ^ 10` = `0110`.
- (c) 14 is the OR `12 | 10` = `1110`.
- (d) 22 is the sum `12 + 10`, which no bitwise operator produces.

---

**29.** **[Hard]** *(B7 — precedence: == binds tighter than &)*

```c
int n = 5;
printf("%d", n & 1 == 0);
```

(a) `0`, because `==` binds tighter than `&`, so the expression is `n & (1 == 0)`
(b) `5`, because `&` combines `n` with the result of the comparison
(c) Compile error: `==` cannot appear after `&`
(d) `1`, because `n` is odd and `5 & 1` is `1`

**29. (a) 0**
`==` has higher precedence than `&`, so `n & 1 == 0` parses as `n & (1 == 0)` = `n & 0` = `0` for every `n`. The intended test must be written `(n & 1) == 0`.

- (d) 1 is what `(n & 1) == 0` would give — but with `n = 5` that expression is `0`, not the expression actually written; the misreading is treating the code as if the parentheses were present.
- (b) 5 assumes `&` combines `n` with the truth value `1` before the comparison.
- (c) is wrong; the expression is syntactically valid C, it just does not do what it looks like.

---

**30.** **[Hard]** *(B7 — XOR swap)*

```c
int a = 5, b = 3;
a = a ^ b;
b = a ^ b;
a = a ^ b;
printf("%d %d", a, b);
```

(a) 3 5
(b) 5 3
(c) 6 3
(d) 3 6

**30. (a) 3 5**

| Step | Statement | a | b |
|---|---|---|---|
| init | `a = 5, b = 3` | 5 | 3 |
| 1 | `a = a ^ b` = `5 ^ 3` = 6 | 6 | 3 |
| 2 | `b = a ^ b` = `6 ^ 3` = 5 | 6 | 5 |
| 3 | `a = a ^ b` = `6 ^ 5` = 3 | 3 | 5 |

The three XORs exchange the two values without a temporary.

- (b) 5 3 is the original, unswapped order — the effect of a swap is invisible only if you skip the updates.
- (c) 6 3 is the state after only the first two statements.
- (d) 3 6 mixes the final value of `a` with the intermediate value of `b` from step 1.

---

**31.** **[Hard]** *(B7 — & vs &&)*

```c
printf("%d %d", 5 & 2, 5 && 2);
```

(a) 0 1
(b) 1 1
(c) 0 0
(d) 1 0

**31. (a) 0 1**
`5 & 2` = `101 & 010` = `000` = 0. `5 && 2` = 1 because both operands are non-zero, and `&&` yields only 0 or 1.

- (c) 0 0 wrongly assumes `&&` returns a bitwise combination of the operands.
- (b) 1 1 wrongly assumes `&` behaves like the logical AND.
- (d) 1 0 reverses the two results.

---

**32.** **[Hard]** *(B7 — precedence: ^ binds tighter than |)*

```c
printf("%d", 1 | 2 ^ 3);
```

(a) 1
(b) 9
(c) 0
(d) 3

**32. (a) 1**
`^` has higher precedence than `|`, so `1 | 2 ^ 3` = `1 | (2 ^ 3)` = `1 | (010 ^ 011)` = `1 | 001` = `1 | 1` = 1.

- (d) 3 comes from computing only `1 | 2` = 3 and ignoring `^ 3`.
- (b) 9 comes from reading `^` as exponentiation: 2³ = 8, then `1 | 8` = 9.
- (c) 0 comes from evaluating strictly left to right: `(1 | 2) ^ 3` = `3 ^ 3` = 0.

---

**33.** **[Hard]** *(B7 — counting set bits with a branch loop)*

```c
int n = 29, count = 0;
while (n) {
    count += n & 1;
    n >>= 1;
}
printf("%d", count);
```

(a) 3
(b) 4
(c) 5
(d) 29

**33. (b) 4**

| `n` | `n & 1` | `count` | `n` after `n >>= 1` |
|---|---|---|---|
| 11101 (29) | 1 | 1 | 1110 (14) |
| 1110 (14) | 0 | 1 | 111 (7) |
| 111 (7) | 1 | 2 | 11 (3) |
| 11 (3) | 1 | 3 | 1 (1) |
| 1 (1) | 1 | 4 | 0 |

`29` = `11101` has four `1` bits, so the loop counts to 4.

- (a) 3 is the count for 14 or 7, i.e. the value after one or two iterations too many.
- (c) 5 is the count for a value with five set bits, such as 31 or 47.
- (d) 29 is the original number, not the number of set bits.

---

**34.** **[Hard]** *(B7 — precedence: << binds tighter than &)*

```c
printf("%d", 1 << 3 & 3);
```

(a) 0
(b) 3
(c) 8
(d) Compile error: `<<` and `&` cannot appear in the same expression

**34. (a) 0**
`<<` has higher precedence than `&`, so the expression is `(1 << 3) & 3` = `8 & 3` = `1000 & 0011` = `0000` = 0.

- (c) 8 comes from assuming `&` is evaluated first: `1 << (3 & 3)` = `1 << 3` = 8.
- (b) 3 is the value of the right operand `3 & 3` alone.
- (d) is wrong; mixing `<<` and `&` is legal C — it is only a readability warning, not a compile error.

---

**35.** **[Hard]** *(B7 — shift combined with XOR)*

```c
int x = 6;
printf("%d", x ^ (x >> 1));
```

(a) 3
(b) 5
(c) 6
(d) 7

**35. (b) 5**
`x >> 1` = `6 >> 1` = 3. Then `6 ^ 3` = `110 ^ 011` = `101` = 5.

- (a) 3 is just the value of `x >> 1`; the XOR with `x` was skipped.
- (c) 6 is `x` itself, as if XOR-ing with the shifted value changed nothing.
- (d) 7 is the OR `6 | 3` = `111`, not the XOR.

---

**36.** **[Hard]** *(B7 — grouping with parentheses and ~)*

```c
printf("%d", (6 | 3) & ~4);
```

(a) 3
(b) 7
(c) 4
(d) 2

---

---

**36. (a) 3**
`6 | 3` = `110 | 011` = `111` = 7. `~4` = -5, whose low bits are `...1011`. `7 & ~4` = `0111 & 1011` = `0011` = 3. Equivalent to "clear bit 2 of 7".

- (b) 7 stops after the OR and never applies the mask.
- (c) 4 treats `~4` as `4` (ignoring the NOT) and answers with the masked-out bit.
- (d) 2 comes from dropping the OR: `6 & ~4` = `0110 & 1011` = `0010` = 2.

---
