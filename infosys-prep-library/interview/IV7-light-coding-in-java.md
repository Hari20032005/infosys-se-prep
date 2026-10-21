---
title: Light coding in Java
code: IV7
section: Interview
weightage_pct: interview stage
est_questions: 1
tier: 3
difficulty: Medium
est_study_hours: 0.7
confidence: Low
last_updated: 2026-09-30
---

# IV7 — Light coding in Java

## 1. Why this topic matters here

This is interview material, not test material. **1 question on this theme** were reported across **1 first-hand interview account** (B5), so it is **Tier 3** for the interview stage, 0.7 hours to prepare. Interviews are face to face on campus, 15–40 minutes, technical and HR usually in one conversation (`../research/03-pattern-synthesis.md` §6). The questions are at textbook level; the teaching body below is sized to answer them aloud, not to pass a written exam.

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

**Example 1 — Palindrome (string and number).** Reverse and compare. For a number, rebuild the reverse with `% 10` and `/ 10`.

```java
public class Main {
    static boolean isPalString(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) { if (s.charAt(i++) != s.charAt(j--)) return false; }
        return true;
    }
    static boolean isPalNumber(int n) {
        int rev = 0, t = n;
        while (t > 0) { rev = rev * 10 + t % 10; t /= 10; }
        return rev == n;
    }
    public static void main(String[] a) {
        System.out.println(isPalString("madam"));
        System.out.println(isPalString("hello"));
        System.out.println(isPalNumber(121));
        System.out.println(isPalNumber(123));
    }
}
```

Output (run):

```text
true
false
true
false
```

**Example 2 — Reverse a string and reverse each word.** Use `StringBuilder.reverse()`, or swap characters from both ends.

```java
public class Main {
    public static void main(String[] a) {
        String s = "Infosys Limited";
        System.out.println(new StringBuilder(s).reverse());
        StringBuilder out = new StringBuilder();
        for (String w : s.split(" ")) out.append(new StringBuilder(w).reverse()).append(' ');
        System.out.println(out.toString().trim());
    }
}
```

Output (run):

```text
detimiL sysofnI
sysofnI detimiL
```

**Example 3 — Factorial (loop and recursion).** The loop version is O(n) time and O(1) space; the recursive version uses O(n) stack.

```java
public class Main {
    static long fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }
    public static void main(String[] a) {
        long f = 1;
        for (int i = 2; i <= 5; i++) f *= i;
        System.out.println(f);
        System.out.println(fact(10));
    }
}
```

Output (run):

```text
120
3628800
```

**Example 4 — Fibonacci series.** Keep the last two terms; do not recurse for the series.

```java
public class Main {
    public static void main(String[] a) {
        int x = 0, y = 1;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10; i++) { sb.append(x).append(i < 9 ? ", " : ""); int z = x + y; x = y; y = z; }
        System.out.println(sb);
    }
}
```

Output (run):

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

**Example 5 — Prime check and primes up to 30.** Test divisors only up to the square root.

```java
public class Main {
    static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; (long) i * i <= n; i++) if (n % i == 0) return false;
        return true;
    }
    public static void main(String[] a) {
        System.out.println(isPrime(97) + " " + isPrime(91));
        StringBuilder sb = new StringBuilder();
        for (int i = 2; i <= 30; i++) if (isPrime(i)) sb.append(i).append(' ');
        System.out.println(sb.toString().trim());
    }
}
```

Output (run):

```text
true false
2 3 5 7 11 13 17 19 23 29
```

**Example 6 — Swap two numbers without a temporary variable.** Add and subtract, or use XOR. Mention the overflow risk of the addition form.

```java
public class Main {
    public static void main(String[] a) {
        int x = 7, y = 12;
        x = x + y; y = x - y; x = x - y;
        System.out.println(x + " " + y);
        x ^= y; y ^= x; x ^= y;
        System.out.println(x + " " + y);
    }
}
```

Output (run):

```text
12 7
7 12
```

**Example 7 — Count vowels and consonants.** Lower-case first; count only letters.

```java
public class Main {
    public static void main(String[] a) {
        String s = "Infosys Limited".toLowerCase();
        int v = 0, c = 0;
        for (char ch : s.toCharArray()) {
            if (ch < 'a' || ch > 'z') continue;
            if ("aeiou".indexOf(ch) >= 0) v++; else c++;
        }
        System.out.println("vowels=" + v + " consonants=" + c);
    }
}
```

Output (run):

```text
vowels=5 consonants=9
```

**Example 8 — Anagram check.** Two words are anagrams if their sorted letters are equal.

```java
import java.util.Arrays;
public class Main {
    static boolean anagram(String p, String q) {
        char[] x = p.toLowerCase().toCharArray(), y = q.toLowerCase().toCharArray();
        Arrays.sort(x); Arrays.sort(y);
        return Arrays.equals(x, y);
    }
    public static void main(String[] a) {
        System.out.println(anagram("listen", "silent"));
        System.out.println(anagram("apple", "paple"));
        System.out.println(anagram("abc", "abd"));
    }
}
```

Output (run):

```text
true
true
false
```

**Example 9 — Largest and second-largest in an array.** One pass with two variables; ignore duplicates of the maximum.

```java
public class Main {
    public static void main(String[] a) {
        int[] arr = {12, 45, 7, 45, 33, 28};
        int max = Integer.MIN_VALUE, second = Integer.MIN_VALUE;
        for (int v : arr) {
            if (v > max) { second = max; max = v; }
            else if (v > second && v != max) second = v;
        }
        System.out.println(max + " " + second);
    }
}
```

Output (run):

```text
45 33
```

**Example 10 — Remove duplicates from an array.** A `LinkedHashSet` keeps first-seen order.

```java
import java.util.*;
public class Main {
    public static void main(String[] a) {
        int[] arr = {4, 2, 4, 7, 2, 9, 7};
        Set<Integer> s = new LinkedHashSet<>();
        for (int v : arr) s.add(v);
        System.out.println(s);
    }
}
```

Output (run):

```text
[4, 2, 7, 9]
```

**Example 11 — Armstrong number.** Sum of each digit raised to the number of digits equals the number: 153 = 1³ + 5³ + 3³.

```java
public class Main {
    static boolean armstrong(int n) {
        int digits = String.valueOf(n).length(), sum = 0, t = n;
        while (t > 0) { sum += (int) Math.pow(t % 10, digits); t /= 10; }
        return sum == n;
    }
    public static void main(String[] a) {
        System.out.println(armstrong(153) + " " + armstrong(154));
    }
}
```

Output (run):

```text
true false
```

**Example 12 — FizzBuzz 1 to 15.** Test the multiple of 15 first.

```java
public class Main {
    public static void main(String[] a) {
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= 15; i++) {
            String t = i % 15 == 0 ? "FizzBuzz" : i % 3 == 0 ? "Fizz" : i % 5 == 0 ? "Buzz" : String.valueOf(i);
            sb.append(t).append(i < 15 ? " " : "");
        }
        System.out.println(sb);
    }
}
```

Output (run):

```text
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
```


### SQL, executed

The tables, used by all six queries (run in SQLite):

```sql
CREATE TABLE emp (id INTEGER PRIMARY KEY, name TEXT, dept_id INTEGER, salary INTEGER);
CREATE TABLE dept (id INTEGER PRIMARY KEY, dname TEXT);
INSERT INTO dept VALUES (1, 'Testing'), (2, 'Development'), (3, 'HR');
INSERT INTO emp VALUES (1, 'Asha', 2, 50000), (2, 'Bala', 2, 65000), (3, 'Chitra', 1, 65000), (4, 'Dev', 1, 45000),
                       (5, 'Esha', NULL, 38000), (6, 'Farid', 2, 72000);
```

**Top 3 earners (MySQL/SQLite style; SQL Server writes `SELECT TOP 3 …`).**

```sql
SELECT name, salary FROM emp ORDER BY salary DESC LIMIT 3;
```

| name | salary |
|---|---|
| Farid | 72000 |
| Bala | 65000 |
| Chitra | 65000 |

**Second-highest salary without a window function.**

```sql
SELECT MAX(salary) AS second_highest FROM emp WHERE salary < (SELECT MAX(salary) FROM emp);
```

| second_highest |
|---|
| 65000 |

**Second-highest **distinct** salary with DENSE_RANK.**

```sql
SELECT salary FROM (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS r FROM emp) WHERE r = 2 GROUP BY salary;
```

| salary |
|---|
| 65000 |

**INNER JOIN: employees with their department.**

```sql
SELECT e.name, d.dname FROM emp e INNER JOIN dept d ON e.dept_id = d.id ORDER BY e.id;
```

| name | dname |
|---|---|
| Asha | Development |
| Bala | Development |
| Chitra | Testing |
| Dev | Testing |
| Farid | Development |

**LEFT JOIN: every employee, even without a department.**

```sql
SELECT e.name, d.dname FROM emp e LEFT JOIN dept d ON e.dept_id = d.id ORDER BY e.id;
```

| name | dname |
|---|---|
| Asha | Development |
| Bala | Development |
| Chitra | Testing |
| Dev | Testing |
| Esha | NULL |
| Farid | Development |

**GROUP BY with HAVING: departments with more than one employee.**

```sql
SELECT d.dname, COUNT(*) AS n FROM emp e JOIN dept d ON e.dept_id = d.id GROUP BY d.dname HAVING COUNT(*) > 1 ORDER BY d.dname;
```

| dname | n |
|---|---|
| Development | 3 |
| Testing | 2 |

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

## 7. Practice questions

Eight short programs. Write each in Java from memory, then open the solution. The expected output was produced by running the solution.

**1.** Reverse the number 12345.

<details><summary>Expected output and solution</summary>

Expected output:

```text
54321
```

```java
public class Main { public static void main(String[] a) { int n = 12345, r = 0; while (n > 0) { r = r * 10 + n % 10; n /= 10; } System.out.println(r); } }
```
</details>

**2.** Find the sum of the digits of 9875.

<details><summary>Expected output and solution</summary>

Expected output:

```text
29
```

```java
public class Main { public static void main(String[] a) { int n = 9875, s = 0; while (n > 0) { s += n % 10; n /= 10; } System.out.println(s); } }
```
</details>

**3.** Find the GCD of 84 and 36 with Euclid's algorithm.

<details><summary>Expected output and solution</summary>

Expected output:

```text
12
```

```java
public class Main { static int g(int a, int b) { return b == 0 ? a : g(b, a % b); } public static void main(String[] a) { System.out.println(g(84, 36)); } }
```
</details>

**4.** Count the words in "the quick brown fox".

<details><summary>Expected output and solution</summary>

Expected output:

```text
4
```

```java
public class Main { public static void main(String[] a) { System.out.println("the quick brown fox".trim().split("\\s+").length); } }
```
</details>

**5.** Are "Listen" and "Silent" anagrams, ignoring case?

<details><summary>Expected output and solution</summary>

Expected output:

```text
true
```

```java
import java.util.*; public class Main { public static void main(String[] a) { char[] x = "Listen".toLowerCase().toCharArray(), y = "Silent".toLowerCase().toCharArray(); Arrays.sort(x); Arrays.sort(y); System.out.println(Arrays.equals(x, y)); } }
```
</details>

**6.** Sort {5, 2, 9, 1, 7} in ascending order and print it.

<details><summary>Expected output and solution</summary>

Expected output:

```text
[1, 2, 5, 7, 9]
```

```java
import java.util.*; public class Main { public static void main(String[] a) { int[] v = {5, 2, 9, 1, 7}; Arrays.sort(v); System.out.println(Arrays.toString(v)); } }
```
</details>

**7.** The array {1, 2, 4, 5, 6} should hold 1 to 6. Find the missing number.

<details><summary>Expected output and solution</summary>

Expected output:

```text
3
```

```java
public class Main { public static void main(String[] a) { int[] v = {1, 2, 4, 5, 6}; int n = 6, exp = n * (n + 1) / 2, s = 0; for (int x : v) s += x; System.out.println(exp - s); } }
```
</details>

**8.** Print a right-angled triangle of stars with height 4.

<details><summary>Expected output and solution</summary>

Expected output:

```text
*
**
***
****
```

```java
public class Main { public static void main(String[] a) { for (int i = 1; i <= 4; i++) System.out.println("*".repeat(i)); } }
```
</details>


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

## 10. Sources

Written for this library. **Evidence:** first-hand interview accounts B1–B6 (`../data/reviews-online.csv`), questions I01 … I25 in `../data/questions-observed.csv`, and the format notes in `00-INTERVIEW-FORMAT.md`. Project facts are taken from your own verified file `HARIHARAN_INTERVIEW_CONTEXT.md` (27 Sep 2026), not from the web. Confidence **Low**; the interview data is five accounts.
