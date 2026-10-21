"""IV7: light coding in Java and SQL, as asked in Infosys interviews (palindrome, a second-highest query, joins).
Every program is compiled and run here; the output shown in the library is the real output."""
import pathlib, re, sqlite3, subprocess, tempfile

WORKED = [
("Palindrome (string and number)", "Reverse and compare. For a number, rebuild the reverse with `% 10` and `/ 10`.",
"""public class Main {
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
}"""),
("Reverse a string and reverse each word", "Use `StringBuilder.reverse()`, or swap characters from both ends.",
"""public class Main {
    public static void main(String[] a) {
        String s = "Infosys Limited";
        System.out.println(new StringBuilder(s).reverse());
        StringBuilder out = new StringBuilder();
        for (String w : s.split(" ")) out.append(new StringBuilder(w).reverse()).append(' ');
        System.out.println(out.toString().trim());
    }
}"""),
("Factorial (loop and recursion)", "The loop version is O(n) time and O(1) space; the recursive version uses O(n) stack.",
"""public class Main {
    static long fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }
    public static void main(String[] a) {
        long f = 1;
        for (int i = 2; i <= 5; i++) f *= i;
        System.out.println(f);
        System.out.println(fact(10));
    }
}"""),
("Fibonacci series", "Keep the last two terms; do not recurse for the series.",
"""public class Main {
    public static void main(String[] a) {
        int x = 0, y = 1;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10; i++) { sb.append(x).append(i < 9 ? ", " : ""); int z = x + y; x = y; y = z; }
        System.out.println(sb);
    }
}"""),
("Prime check and primes up to 30", "Test divisors only up to the square root.",
"""public class Main {
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
}"""),
("Swap two numbers without a temporary variable", "Add and subtract, or use XOR. Mention the overflow risk of the addition form.",
"""public class Main {
    public static void main(String[] a) {
        int x = 7, y = 12;
        x = x + y; y = x - y; x = x - y;
        System.out.println(x + " " + y);
        x ^= y; y ^= x; x ^= y;
        System.out.println(x + " " + y);
    }
}"""),
("Count vowels and consonants", "Lower-case first; count only letters.",
"""public class Main {
    public static void main(String[] a) {
        String s = "Infosys Limited".toLowerCase();
        int v = 0, c = 0;
        for (char ch : s.toCharArray()) {
            if (ch < 'a' || ch > 'z') continue;
            if ("aeiou".indexOf(ch) >= 0) v++; else c++;
        }
        System.out.println("vowels=" + v + " consonants=" + c);
    }
}"""),
("Anagram check", "Two words are anagrams if their sorted letters are equal.",
"""import java.util.Arrays;
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
}"""),
("Largest and second-largest in an array", "One pass with two variables; ignore duplicates of the maximum.",
"""public class Main {
    public static void main(String[] a) {
        int[] arr = {12, 45, 7, 45, 33, 28};
        int max = Integer.MIN_VALUE, second = Integer.MIN_VALUE;
        for (int v : arr) {
            if (v > max) { second = max; max = v; }
            else if (v > second && v != max) second = v;
        }
        System.out.println(max + " " + second);
    }
}"""),
("Remove duplicates from an array", "A `LinkedHashSet` keeps first-seen order.",
"""import java.util.*;
public class Main {
    public static void main(String[] a) {
        int[] arr = {4, 2, 4, 7, 2, 9, 7};
        Set<Integer> s = new LinkedHashSet<>();
        for (int v : arr) s.add(v);
        System.out.println(s);
    }
}"""),
("Armstrong number", "Sum of each digit raised to the number of digits equals the number: 153 = 1³ + 5³ + 3³.",
"""public class Main {
    static boolean armstrong(int n) {
        int digits = String.valueOf(n).length(), sum = 0, t = n;
        while (t > 0) { sum += (int) Math.pow(t % 10, digits); t /= 10; }
        return sum == n;
    }
    public static void main(String[] a) {
        System.out.println(armstrong(153) + " " + armstrong(154));
    }
}"""),
("FizzBuzz 1 to 15", "Test the multiple of 15 first.",
"""public class Main {
    public static void main(String[] a) {
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= 15; i++) {
            String t = i % 15 == 0 ? "FizzBuzz" : i % 3 == 0 ? "Fizz" : i % 5 == 0 ? "Buzz" : String.valueOf(i);
            sb.append(t).append(i < 15 ? " " : "");
        }
        System.out.println(sb);
    }
}"""),
]

EXERCISES = [
("Reverse the number 12345.", """public class Main { public static void main(String[] a) { int n = 12345, r = 0; while (n > 0) { r = r * 10 + n % 10; n /= 10; } System.out.println(r); } }"""),
("Find the sum of the digits of 9875.", """public class Main { public static void main(String[] a) { int n = 9875, s = 0; while (n > 0) { s += n % 10; n /= 10; } System.out.println(s); } }"""),
("Find the GCD of 84 and 36 with Euclid's algorithm.", """public class Main { static int g(int a, int b) { return b == 0 ? a : g(b, a % b); } public static void main(String[] a) { System.out.println(g(84, 36)); } }"""),
("Count the words in \"the quick brown fox\".", """public class Main { public static void main(String[] a) { System.out.println("the quick brown fox".trim().split("\\\\s+").length); } }"""),
("Are \"Listen\" and \"Silent\" anagrams, ignoring case?", """import java.util.*; public class Main { public static void main(String[] a) { char[] x = "Listen".toLowerCase().toCharArray(), y = "Silent".toLowerCase().toCharArray(); Arrays.sort(x); Arrays.sort(y); System.out.println(Arrays.equals(x, y)); } }"""),
("Sort {5, 2, 9, 1, 7} in ascending order and print it.", """import java.util.*; public class Main { public static void main(String[] a) { int[] v = {5, 2, 9, 1, 7}; Arrays.sort(v); System.out.println(Arrays.toString(v)); } }"""),
("The array {1, 2, 4, 5, 6} should hold 1 to 6. Find the missing number.", """public class Main { public static void main(String[] a) { int[] v = {1, 2, 4, 5, 6}; int n = 6, exp = n * (n + 1) / 2, s = 0; for (int x : v) s += x; System.out.println(exp - s); } }"""),
("Print a right-angled triangle of stars with height 4.", """public class Main { public static void main(String[] a) { for (int i = 1; i <= 4; i++) System.out.println("*".repeat(i)); } }"""),
]


def run_java(code):
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'Main.java').write_text(code)
    r = subprocess.run(['javac', 'Main.java'], cwd=d, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:800]
    r = subprocess.run(['java', '-cp', str(d), 'Main'], capture_output=True, text=True, timeout=30)
    assert r.returncode == 0, r.stderr[:400]
    return r.stdout.rstrip('\n')


def fmt_code(code):
    return code


SQL_SETUP = """
CREATE TABLE emp (id INTEGER PRIMARY KEY, name TEXT, dept_id INTEGER, salary INTEGER);
CREATE TABLE dept (id INTEGER PRIMARY KEY, dname TEXT);
INSERT INTO dept VALUES (1, 'Testing'), (2, 'Development'), (3, 'HR');
INSERT INTO emp VALUES (1, 'Asha', 2, 50000), (2, 'Bala', 2, 65000), (3, 'Chitra', 1, 65000), (4, 'Dev', 1, 45000),
                       (5, 'Esha', NULL, 38000), (6, 'Farid', 2, 72000);
"""
SQL_QUERIES = [
    ("Top 3 earners (MySQL/SQLite style; SQL Server writes `SELECT TOP 3 …`)", "SELECT name, salary FROM emp ORDER BY salary DESC LIMIT 3"),
    ("Second-highest salary without a window function", "SELECT MAX(salary) AS second_highest FROM emp WHERE salary < (SELECT MAX(salary) FROM emp)"),
    ("Second-highest **distinct** salary with DENSE_RANK", "SELECT salary FROM (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS r FROM emp) WHERE r = 2 GROUP BY salary"),
    ("INNER JOIN: employees with their department", "SELECT e.name, d.dname FROM emp e INNER JOIN dept d ON e.dept_id = d.id ORDER BY e.id"),
    ("LEFT JOIN: every employee, even without a department", "SELECT e.name, d.dname FROM emp e LEFT JOIN dept d ON e.dept_id = d.id ORDER BY e.id"),
    ("GROUP BY with HAVING: departments with more than one employee", "SELECT d.dname, COUNT(*) AS n FROM emp e JOIN dept d ON e.dept_id = d.id GROUP BY d.dname HAVING COUNT(*) > 1 ORDER BY d.dname"),
]


def run_sql():
    con = sqlite3.connect(':memory:')
    con.executescript(SQL_SETUP)
    out = []
    for title, q in SQL_QUERIES:
        cur = con.execute(q)
        cols = [c[0] for c in cur.description]
        rows = cur.fetchall()
        out.append((title, q, cols, rows))
    return out


def md_table(cols, rows):
    t = '| ' + ' | '.join(cols) + ' |\n|' + '---|' * len(cols) + '\n'
    return t + '\n'.join('| ' + ' | '.join('NULL' if v is None else str(v) for v in r) + ' |' for r in rows)


def worked_md():
    parts = []
    for i, (title, note, code) in enumerate(WORKED, 1):
        out = run_java(code)
        parts.append(f"**Example {i} — {title}.** {note}\n\n```java\n{code}\n```\n\nOutput (run):\n\n```text\n{out}\n```\n")
    return '\n'.join(parts)


def sql_md():
    parts = ["The tables, used by all six queries (run in SQLite):\n", "```sql\n" + SQL_SETUP.strip() + "\n```\n"]
    for title, q, cols, rows in run_sql():
        parts.append(f"**{title}.**\n\n```sql\n{q};\n```\n\n{md_table(cols, rows)}\n")
    return '\n'.join(parts)


def exercises_md():
    lines = ["Write each in Java from memory, then open the solution. The expected output was produced by running the solution.\n"]
    for i, (stmt, code) in enumerate(EXERCISES, 1):
        out = run_java(code)
        lines.append(f"**{i}.** {stmt}\n\n<details><summary>Expected output and solution</summary>\n\nExpected output:\n\n```text\n{out}\n```\n\n```java\n{code}\n```\n</details>\n")
    return '\n'.join(lines)


def exercise_outputs():
    return [run_java(code) for _, code in EXERCISES]
