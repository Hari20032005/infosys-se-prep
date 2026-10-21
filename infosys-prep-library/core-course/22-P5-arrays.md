---
title: Arrays
code: P5
section: Pseudocode
weightage_pct: 1.8% of marks
est_questions: 0.68
tier: 2
difficulty: Medium
est_study_hours: 0.8
confidence: Medium
last_updated: 2026-09-30
course: core
lesson: 22
---

# Lesson 22. Arrays

*Topic `P5` · about 1.4 of the 75 marks · plan about 0.8 hours.*

## 1. The idea

An array is a row of boxes, each holding one value. Each box has a number called its **index**, and the numbering **starts at 0**. So an array with 5 boxes has indexes 0, 1, 2, 3 and 4. The first box is `a[0]`, and the last is `a[4]`.

Two things you do with an array come up again and again: reading a box (`a[2]`), and walking along all the boxes with a loop (`For (each i from 0 to 4)`), using `a[i]` inside.

An array question is a loop question with a list of numbers attached. The same trace table works. You add one more thing: a note of what is in each box.

Why does counting start at 0? Think of the index as how far a box is from the start. The first box is no steps from the start, so its index is 0. The second box is one step away, so its index is 1. That also explains the rule for the last box: an array of n boxes ends at index n − 1. If you ever feel unsure, count on your fingers from 0 and check the last index.

## 2. What Infosys actually asks

Two array questions were reported, both from one coaching video that said they were asked in 2025 `[REPORTED]`:

- Find the product of all elements, then print each element's "total divided by that element". For the input 2, 3, 4, 5 the output is 60 40 30 24.
- Find the length of the longest run in which each number is bigger than the one before. For 1, 2, 2, 3, 4, 5, 1 the answer is 4.

The official 2020 sample had no array question. Pseudocode is 5 questions worth 10 marks in 10 minutes, about two marks and two minutes each.

## 3. The method

1. **Write the array as a row of boxes** with the indexes above them: `0 1 2 3 4`.
2. **Note where the loop starts and stops.** `from 0 to 4` visits all five boxes. `from 1 to 4` skips the first.
3. **Watch the step.** `step 2` visits every second box. `step -1` counts backwards.
4. **Trace the loop** as in the loop lesson, with a column for each variable.
5. **If the program changes a box, redraw the row.** The new values matter for later turns.
6. **Check your index.** Is the largest index you use still inside the array?
7. **Read the bounds twice.** Many wrong answers come from running the loop one turn too many or too few, so write down the first and last value of `i` before you start.

Words you will meet:

| Word | Meaning |
|---|---|
| `a[i - 1]` | the box just before box i |
| `a[i] = a[i] + a[i - 1]` | box i becomes the running total |
| `step 2` | go up by 2 each turn |
| `step -1` | go down by 1 each turn |

Five patterns come up so often that it pays to recognise them at once:

| If you see | It is probably | What it does |
|---|---|---|
| `s = s + a[i]` inside a loop over all boxes | a sum | adds every element |
| `If (a[i] > m) then m = a[i]` | a maximum | keeps the largest seen so far |
| `If (a[i] > k) then c++` | a count | counts the elements above k |
| `a[i] = a[i] + a[i - 1]` | running totals | each box becomes the total up to that point |
| `t = a[i]`, `a[i] = a[i + 1]`, `a[i + 1] = t` | a swap | exchanges two neighbouring boxes using a spare variable `t` |

Knowing the pattern lets you predict the answer before you trace, and then use the trace to confirm it. If the trace and your prediction disagree, trace again, because one of them has a slip.

## 4. Shortcuts and when they fail

**Total divided by an element.** If you know the total of all the elements, you can get the product of the others by dividing. *It fails for a zero element.*

**Running totals.** If every box becomes itself plus the box before, the last box holds the sum of all the original values. *It fails if the loop stops early.*

**Count the visits.** `from 0 to 4 step 2` visits indexes 0, 2 and 4, which is three boxes. *It fails if the end falls between steps.* List them.

**Check the first and last turn of a loop with `a[i - 1]`.** The loop must start at 1, not 0, or you read a box that does not exist. *It fails only if the question starts at 0 on purpose.* Then the program has a bug, and the question may be about that.

## 5. Worked examples

All the outputs below come from translating the printed program to Java and running it. The array holds 4, 7, 1, 9, 3.

**Example 1 (adding everything).**

```text
1) Integer a[5], i, s
2) Set a[0] = 4, a[1] = 7, a[2] = 1, a[3] = 9, a[4] = 3
3) Set s = 0
4) For (each i from 0 to 4)
5)   s = s + a[i]
6) End-for
7) Print s
```

4 + 7 + 1 + 9 + 3 = **24**.

**Example 2 (reading two boxes).**

```text
1) Integer a[5]
2) Set a[0] = 4, a[1] = 7, a[2] = 1, a[3] = 9, a[4] = 3
3) Print a[1] + a[3]
```

Index 1 holds 7 and index 3 holds 9. Output: **16**. (Index 1 is the **second** box.)

**Example 3 (the biggest).**

```text
1) Integer a[5], i, m
2) Set a[0] = 4, a[1] = 7, a[2] = 1, a[3] = 9, a[4] = 3
3) Set m = a[0]
4) For (each i from 1 to 4)
5)   If (a[i] > m) then
6)     m = a[i]
7)   End-if
8) End-for
9) Print m
```

m starts at 4. It becomes 7, stays 7, becomes 9, stays 9. Output: **9**.

**Example 4 (backwards).**

```text
1) Integer a[5], i
2) Set a[0] = 4, a[1] = 7, a[2] = 1, a[3] = 9, a[4] = 3
3) For (each i from 4 to 0 step -1)
4)   Print a[i]
5) End-for
```

The loop counts 4, 3, 2, 1, 0. Output: **3 9 1 7 4**.

**Example 5 (running totals).**

```text
1) Integer a[5], i
2) Set a[0] = 4, a[1] = 7, a[2] = 1, a[3] = 9, a[4] = 3
3) For (each i from 1 to 4)
4)   a[i] = a[i] + a[i - 1]
5) End-for
6) For (each i from 0 to 4)
7)   Print a[i]
8) End-for
```

Turn by turn the array becomes 4 11 1 9 3, then 4 11 12 9 3, then 4 11 12 21 3, then 4 11 12 21 24. Output: **4 11 12 21 24**.

## 6. Traps

- **Starting the count at 1.** The first box is index 0.
- **Using an index that is too big.** An array of 5 boxes has no `a[5]`.
- **Forgetting that the loop changes the array.** In Example 5 each turn uses the new value of the box before.
- **A `step` that skips the end.** List the indexes the loop actually visits.
- **Printing one line at a time.** If a `Print` is inside the loop, the output is a list, so write the answer as a list in the same order.
- **Forgetting the spare variable in a swap.** Without `t`, the first assignment destroys a value you still need. After `a[i] = a[i + 1]`, the old `a[i]` is gone unless it was saved.


## 7. Practice questions

Attempt each level before opening the key. Level 3 is harder than anything in the 2020 official sample, on purpose: if you can do Level 3, the real paper will feel easy.

### Level 1: warm-up

*Add, find the largest, or count the elements above a number.*

**1.** **[Array sum]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[6], i, s
2) Set a[0] = 3, a[1] = 2, a[2] = 6, a[3] = 6, a[4] = 8, a[5] = 8
3) Set s = 0
4) For (each i from 0 to 5)
5)   s = s + a[i]
6) End-for
7) Print s
```

a) 32  
b) 33  
c) 35  
d) 34  

**2.** **[Array maximum]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[6], i, m
2) Set a[0] = 8, a[1] = 8, a[2] = 4, a[3] = 5, a[4] = 2, a[5] = 1
3) Set m = a[0]
4) For (each i from 1 to 5)
5)   If (a[i] > m) then
6)     m = a[i]
7)   End-if
8) End-for
9) Print m
```

a) 9  
b) 8  
c) 10  
d) 7  

**3.** **[Array count]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[5], i, c
2) Set a[0] = 4, a[1] = 1, a[2] = 9, a[3] = 7, a[4] = 9
3) Set c = 0
4) For (each i from 0 to 4)
5)   If (a[i] > 5) then
6)     c++
7)   End-if
8) End-for
9) Print c
```

a) 4  
b) 2  
c) 3  
d) 5  

**4.** **[Array maximum]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[6], i, m
2) Set a[0] = 7, a[1] = 9, a[2] = 7, a[3] = 1, a[4] = 6, a[5] = 4
3) Set m = a[0]
4) For (each i from 1 to 5)
5)   If (a[i] > m) then
6)     m = a[i]
7)   End-if
8) End-for
9) Print m
```

a) 10  
b) 9  
c) 11  
d) 8  

**5.** **[Array count]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[6], i, c
2) Set a[0] = 1, a[1] = 5, a[2] = 3, a[3] = 1, a[4] = 6, a[5] = 3
3) Set c = 0
4) For (each i from 0 to 5)
5)   If (a[i] > 4) then
6)     c++
7)   End-if
8) End-for
9) Print c
```

a) 1  
b) 4  
c) 3  
d) 2  

### Level 2: exam level

*Every second element, going backwards, and running totals.*

**6.** **[Array every second]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[6], i, s
2) Set a[0] = 3, a[1] = 5, a[2] = 3, a[3] = 3, a[4] = 1, a[5] = 5
3) Set s = 0
4) For (each i from 0 to 5 step 2)
5)   s = s + a[i]
6) End-for
7) Print s
```

a) 7  
b) 9  
c) 8  
d) 6  

**7.** **[Array backwards]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[5], i
2) Set a[0] = 5, a[1] = 8, a[2] = 2, a[3] = 6, a[4] = 1
3) For (each i from 4 to 0 step -1)
4)   Print a[i]
5) End-for
```

a) 1 6 2 8 5  
b) 6 2 8 5 1  
c) 2 6 2 8 5  
d) 5 8 2 6 1  

**8.** **[Running totals]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[5], i
2) Set a[0] = 3, a[1] = 9, a[2] = 3, a[3] = 9, a[4] = 7
3) For (each i from 1 to 4)
4)   a[i] = a[i] + a[i - 1]
5) End-for
6) Print a[4]
```

a) 30  
b) 31  
c) 33  
d) 32  

**9.** **[Array every second]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[5], i, s
2) Set a[0] = 2, a[1] = 4, a[2] = 1, a[3] = 5, a[4] = 8
3) Set s = 0
4) For (each i from 0 to 4 step 2)
5)   s = s + a[i]
6) End-for
7) Print s
```

a) 12  
b) 13  
c) 11  
d) 10  

**10.** **[Running totals]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[6], i
2) Set a[0] = 5, a[1] = 9, a[2] = 1, a[3] = 7, a[4] = 4, a[5] = 4
3) For (each i from 1 to 5)
4)   a[i] = a[i] + a[i - 1]
5) End-for
6) Print a[5]
```

a) 31  
b) 29  
c) 30  
d) 32  

### Level 3: beyond the exam

*Swapping neighbours, the longest rising run, and the product of the others.*

**11.** **[Swapping pairs]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[6], i, t
2) Set a[0] = 2, a[1] = 4, a[2] = 2, a[3] = 5, a[4] = 9, a[5] = 1
3) For (each i from 0 to 4 step 2)
4)   t = a[i]
5)   a[i] = a[i + 1]
6)   a[i + 1] = t
7) End-for
8) For (each i from 0 to 5)
9)   Print a[i]
10) End-for
```

a) 5 2 5 2 1 9  
b) 9 1 2 5 2 4  
c) 2 5 2 1 9 4  
d) 4 2 5 2 1 9  

**12.** **[Longest rising run]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[7], i, cur, best
2) Set a[0] = 5, a[1] = 3, a[2] = 6, a[3] = 1, a[4] = 5, a[5] = 1, a[6] = 2
3) Set cur = 1
4) Set best = 1
5) For (each i from 1 to 6)
6)   If (a[i] > a[i - 1]) then
7)     cur++
8)     If (cur > best) then
9)       best = cur
10)     End-if
11)   Else
12)     cur = 1
13)   End-if
14) End-for
15) Print best
```

a) 2  
b) 3  
c) 4  
d) 1  

**13.** **[Product of the others]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[4], i, total
2) Set a[0] = 5, a[1] = 2, a[2] = 2, a[3] = 4
3) Set total = 1
4) For (each i from 0 to 3)
5)   total = total * a[i]
6) End-for
7) For (each i from 0 to 3)
8)   Print total / a[i]
9) End-for
```

a) 20 40 40 16  
b) 17 40 40 20  
c) 16 40 40 20  
d) 40 40 20 16  

**14.** **[Longest rising run]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[7], i, cur, best
2) Set a[0] = 2, a[1] = 6, a[2] = 1, a[3] = 3, a[4] = 1, a[5] = 6, a[6] = 4
3) Set cur = 1
4) Set best = 1
5) For (each i from 1 to 6)
6)   If (a[i] > a[i - 1]) then
7)     cur++
8)     If (cur > best) then
9)       best = cur
10)     End-if
11)   Else
12)     cur = 1
13)   End-if
14) End-for
15) Print best
```

a) 3  
b) 1  
c) 4  
d) 2  

**15.** **[Swapping pairs]** What is the output of the following pseudocode? (Arrays start at index 0; `/` is whole-number division; values printed one per line are shown here separated by spaces.)  

```text
1) Integer a[5], i, t
2) Set a[0] = 3, a[1] = 1, a[2] = 1, a[3] = 7, a[4] = 4
3) For (each i from 0 to 3 step 2)
4)   t = a[i]
5)   a[i] = a[i + 1]
6)   a[i + 1] = t
7) End-for
8) For (each i from 0 to 4)
9)   Print a[i]
10) End-for
```

a) 1 3 7 1 4  
b) 2 3 7 1 4  
c) 3 7 1 4 1  
d) 4 1 7 3 1  

### ANSWER KEY

1. **b** — Add every element: 3 + 2 + 6 + 6 + 8 + 8 = **33**.
2. **b** — Keep the largest seen so far while walking along [8, 8, 4, 5, 2, 1]: **8**.
3. **c** — Count the elements greater than 5 in [4, 1, 9, 7, 9]: **3**.
4. **b** — Keep the largest seen so far while walking along [7, 9, 7, 1, 6, 4]: **9**.
5. **d** — Count the elements greater than 4 in [1, 5, 3, 1, 6, 3]: **2**.
6. **a** — `step 2` visits positions 0, 2, 4…: [3, 3, 1] adds to **7**.
7. **a** — The loop counts down from index 4 to 0, so the array is printed backwards: **1 6 2 8 5**.
8. **b** — Each element becomes the running total, so the last one is the sum of all: 3 + 9 + 3 + 9 + 7 = **31**.
9. **c** — `step 2` visits positions 0, 2, 4…: [2, 1, 8] adds to **11**.
10. **c** — Each element becomes the running total, so the last one is the sum of all: 5 + 9 + 1 + 7 + 4 + 4 = **30**.
11. **d** — Each neighbouring pair swaps places: [2, 4, 2, 5, 9, 1] becomes **4 2 5 2 1 9**.
12. **a** — `cur` counts how long the strictly rising run is and `best` remembers the longest. For [5, 3, 6, 1, 5, 1, 2] the longest rising run has **2** elements.
13. **c** — The product of all four is 80. Dividing by each element leaves the product of the others: **16 40 40 20**.
14. **d** — `cur` counts how long the strictly rising run is and `best` remembers the longest. For [2, 6, 1, 3, 1, 6, 4] the longest rising run has **2** elements.
15. **a** — Each neighbouring pair swaps places: [3, 1, 1, 7, 4] becomes **1 3 7 1 4**.

## 8. Recap in 60 seconds

- Arrays start at index 0. Five boxes: 0 to 4.
- `For (each i from 0 to n-1)` visits every box.
- `step 2` skips one; `step -1` counts down.
- Redraw the row when the program changes a box.
- Running total: each box becomes itself plus the one before.
- Check the first and last index used.

## 9. Sources

- [The Java Tutorials: Arrays](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html): each item in an array is an element accessed by its numerical index, and numbering begins with 0 (S2 in `../research/06-method-sources.md`).
- `../question-banks/QB-99-OBSERVED-POOL.md`: the two array questions reported in 2025, solved by running code.
- Every output above comes from translating the printed program to Java and running it (`data/cc_examples.py`).
