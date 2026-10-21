## 2. Exactly what gets asked

Light coding is rare and small. One 2025 interview asked for a **palindrome program** and the choice between Java and Python (B5) `[REPORTED]`; another asked for a **SQL query returning the top rows of a student table** (B6, an undated account, `[REPORTED]`); the Jun 2025 DSE interview (a different, higher role) included a **second-highest salary** query and a 45-minute coding test, which is the upgrade-path format, not the Systems Engineer interview. Joins and SQL fundamentals were asked in B4.

| Sub-pattern | How it appears | Observed |
|---|---|---|
| A short program on a whiteboard or laptop | Palindrome | B5 |
| “Java or Python, and why?” | Language choice | B5 |
| A SQL query | Top-N rows; second-highest salary | B6, DSE account |
| SQL concept | Joins and their types | B4 |

The SE interview does **not** look like a coding round. The aim is to see that you can write 5–10 lines cleanly and explain them.

## 3. Concept notes

### 3.1 The template for any small program

1. Restate the problem and one example in your own words.
2. Say the idea in one sentence (“compare characters from both ends”).
3. Write it with clear names; handle the empty or one-character case.
4. Trace it on the example, aloud.
5. State the time and space cost (“O(n) time, O(1) space”).

### 3.2 Why Java

Say it plainly: you write Java for structured programs and DSA, and use Python for ML and quick scripts. Both of your deployed projects have Python backends, so this is true.

### 3.3 SQL in three lines

`SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT`. An `INNER JOIN` keeps matched rows; a `LEFT JOIN` keeps every row of the left table; `HAVING` filters groups, `WHERE` filters rows.

### 3.4 Second-highest: name the trap

“Second-highest **row**” and “second-highest **value**” differ when salaries tie. The `MAX … WHERE salary < (SELECT MAX …)` form and `DENSE_RANK() = 2` both return the second-highest **distinct** value.

## 4. Must-memorise block

| Task | Idea |
|---|---|
| Palindrome | two pointers from both ends |
| Reverse a number | `rev = rev * 10 + n % 10; n /= 10` |
| Prime | test divisors up to √n |
| Fibonacci | keep the last two values |
| Anagram | sort both and compare |
| Missing number 1..n | n(n+1)/2 minus the sum |
| Duplicates | `LinkedHashSet` |

## 5. Worked examples

Every program below was compiled with `javac` and run; the output is the real output.

{{WORKED}}

### SQL, executed

{{SQL}}

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Comparing `String`s with `==` | Compares references | Use `.equals` |
| Integer overflow in factorial | `int` overflows at 13! | Use `long`, and say so |
| Prime loop to n | Slow | Stop at √n |
| Off-by-one in loops | `<` vs `<=` | Trace the last iteration |
| “Second highest” with duplicates | Row vs distinct value | State which one you mean |
| Silent code | The panel cannot follow | Think aloud |
| `Arrays.sort` on the array you still need | Mutates it | Copy first |

## 8. Resources

- **https://docs.oracle.com/javase/tutorial/** — the official Java tutorial; use it for syntax, not for practice problems.
- **https://www.w3schools.com/sql/** — quick SQL reference, including joins.
- **https://www.geeksforgeeks.org/java-programming-examples/** — a list of short Java programs like the ones above.

## 9. Self-check

1. Can you write a palindrome check for both a string and a number, from memory?
2. Can you explain the difference between `INNER JOIN` and `LEFT JOIN` with an example?
3. Which second-highest query works with duplicate salaries?
4. Why is the loop for primes `i * i <= n` and not `i < n`?
5. What do you say when asked “Java or Python?”
