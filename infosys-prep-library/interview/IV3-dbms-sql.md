---
title: DBMS and SQL — Joins, GROUP BY, Keys, Indexes, NULLs
code: IV3
section: Interview
weightage_pct: interview stage
est_questions: 1
tier: 3
difficulty: Medium
est_study_hours: 1.0
confidence: Low
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-library/topics/T08-D6-dbms-sql.md
---

# IV3 — DBMS and SQL — Joins, GROUP BY, Keys, Indexes, NULLs

*Adapted from `accenture-prep-final/accenture-prep-library/topics/T08-D6-dbms-sql.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

This is interview material, not test material. **1 question on this theme** were reported across **1 first-hand interview account** (B4), so it is **Tier 3** for the interview stage, 1.0 hours to prepare. Interviews are face to face on campus, 15–40 minutes, technical and HR usually in one conversation (`../research/03-pattern-synthesis.md` §6). The questions are at textbook level; the teaching body below is sized to answer them aloud, not to pass a written exam.

## 2. Exactly what gets asked

### What Infosys interviewers asked

| ID | Account | Date | Question |
|---|---|---|---|
| I16 | B4 | 2025-01-20 | What are joins and what are their types? |

> The pattern notes below come from the library this file was adapted from; their frequency remarks describe that source, not Infosys.



1. **Small-table join with a row count.** Two tiny tables are shown and you state how many rows the join returns. LEFT JOIN with NULL filling is the confirmed local pattern.

1. **(c) `UPDATE employees SET salary = salary * 1.10 WHERE dept_id = 10;`** — Correct: `SET` changes values and `WHERE` restricts which rows are updated.  
   - (b) `HAVING` is not valid in an `UPDATE` statement.  
   - (a) `UPDATE` syntax requires `SET` before `WHERE`.  
   - (d) `10%` is not a valid numeric salary expression.

---

2. **WHERE versus HAVING.** The most examined SQL distinction anywhere.

2. **(a) `WHERE email IS NULL`** — Correct: `NULL` must be tested with `IS NULL`, not equality.  
   - (b) `= NULL` evaluates to unknown, so no rows match.  
   - (c) `<> NULL` also evaluates to unknown.  
   - (d) `''` is an empty string, not a `NULL` value.

---

3. **Index optimisation.** Confirmed asked twice. Which column to index for a given query, and when an index will *not* help — notably a leading-wildcard `LIKE '%x'`.

3. **(c) `student_id` generated unique and not changing** — Correct: a primary key should be unique, non-null, and stable.  
   - (a) Names can duplicate.  
   - (b) Email can change or be missing.  
   - (d) Phone numbers can change and duplicate.

---

4. **NULL behaviour.** Confirmed local item. Why `= NULL` never matches, and how aggregates treat NULLs.

4. **(c) `WHERE name LIKE 'A%'`** — Correct: `A%` means starts with `A`, followed by any characters.  
   - (b) `%A` means ends with `A`.  
   - (d) `_A%` means second character is `A`.  
   - (a) `= 'A*'` matches the literal string `A*`.

---

5. **Key selection.** Confirmed local item. Which column is the appropriate primary key, and primary key versus unique.

5. **(b) 6** — Correct: 3 matching mark rows plus 1 row each for students 3, 4, and 5.  
   - (c) Counts only the matching mark rows.  
   - (a) Counts only the student rows.  
   - (d) Counts nonexistent extra rows.

---

6. **Trigger purpose.** Confirmed local item: automatically logging a deletion.

6. **(d) `WHERE` filters rows before grouping; `HAVING` filters groups after grouping.** — Correct: this is the standard logical order.  
   - (a) Reverses the two clauses.  
   - (c) `HAVING` appears after `GROUP BY`.  
   - (b) `HAVING` can be used with `GROUP BY`.

---

7. **Concurrency and ACID.** Confirmed local item on SQL concurrency — dirty reads, lost updates, isolation levels.

7. **(a) A B-tree index on `email`** — Correct: B-tree supports fast equality searches on high-cardinality columns.  
   - (b) `gender` has low selectivity and does not help find email.  
   - (c) A primary-key index helps only if `email` is the primary key.  
   - (d) `@` has no effect on whether an index works.

---

8. **Aggregate and GROUP BY rules**, including `COUNT(*)` versus `COUNT(column)`.

## 3. Concept notes

**DBMS**: Software layer between users/applications and stored data. Stores, retrieves, updates data; enforces schema, constraints, concurrency control, recovery, security.

**DBMS vs RDBMS**: RDBMS is a DBMS that organizes data as relations (tables) with rows/columns and supports relational operators, SQL, keys, and referential integrity. Every RDBMS is a DBMS; not every DBMS is an RDBMS (e.g., hierarchical, network, XML, key-value stores).

**File system limitations fixed by DBMS**:

| Problem | File system | DBMS |
|---|---|---|
| Concurrent access | No locking/atomicity; lost updates, inconsistent reads | Transactions, locks, isolation levels |
| Redundancy | Duplicate data across files; wasted space, inconsistency | Normalized schema, centralized data, constraints |
| Integrity | Application-enforced; weak | Domain, entity, referential integrity; triggers |
| Security | OS file permissions only | Users, roles, privileges at table/column/row level, views, auditing |
| Backup/recovery | Manual; no point-in-time recovery | Automated backup, transaction log, rollback/roll-forward |

**Vocabulary**:

| Term | Definition | Synonym |
|---|---|---|
| Table | Set of rows with same columns | Relation |
| Row | Single record in a table | Tuple |
| Column | Attribute/field of a table | Attribute |
| Domain | Set of permitted atomic values for a column | - |
| Cardinality | Number of rows in a relation | - |
| Degree | Number of columns in a relation | - |

**Keys**:

Super key: any attribute set that uniquely identifies each row. Example: `Student(StudentID, Email, Name)`. `{StudentID}`, `{Email}`, `{StudentID, Email}`, `{StudentID, Name}` are super keys.

Candidate key: minimal super key; no proper subset is a super key. Example: `{StudentID}`, `{Email}`.

Primary key: candidate key chosen to identify rows; cannot be NULL; only one per table. Example: `StudentID`.

Alternate key: candidate key not chosen as primary. Example: `Email`.

Composite key: key with two or more attributes. Example: `Enrollment(StudentID, CourseID)` primary key `{StudentID, CourseID}`.

Foreign key: column(s) in one table referencing primary/unique key of another. Example: `Enrollment.StudentID -> Student.StudentID`. Allows NULL if column nullable.

Unique key: constraint enforcing distinct values in column(s). Example: `UNIQUE(Email)`. Allows NULL (multiple in most DBMS; SQL Server allows one).

Surrogate key: system-generated artificial identifier with no business meaning. Example: `id INT AUTO_INCREMENT`.

| Key | Rule | NULL allowed | Max per table | Example |
|---|---|---|---|---|
| Super key | Uniquely identifies each row | Yes (if a subset is unique) | Many | `{StudentID}`, `{Email}`, `{StudentID,Name}` |
| Candidate key | Minimal super key | No (as enforced key) | Many | `{StudentID}`, `{Email}` |
| Primary key | Chosen candidate key | No | 1 | `StudentID` |
| Alternate key | Candidate key not primary | No | Many | `Email` |
| Composite key | >=2 attributes | No if primary | Many | `{StudentID, CourseID}` |
| Foreign key | References PK/unique of another table | Yes if nullable | Many | `Enrollment.StudentID -> Student.StudentID` |
| Unique key | Enforces distinct values | Yes (multiple NULLs in most DBMS; one in SQL Server) | Many | `Email` |
| Surrogate key | System-generated artificial id | No | Usually 1 | `id INT AUTO_INCREMENT` |

**PRIMARY KEY vs UNIQUE**:
- PRIMARY KEY: one per table; NOT NULL; creates unique index; can be composite.
- UNIQUE: multiple per table; allows NULL (except SQL Server permits only one NULL); creates unique index; can be composite.
- Both enforce uniqueness.

**Referential integrity**: Every non-NULL foreign key value must match an existing primary/unique key value in the referenced table. Prevents orphan rows.

**ON DELETE actions**:

| Action | Behavior |
|---|---|
| CASCADE | Delete child rows when parent row is deleted. |
| SET NULL | Set foreign key in child rows to NULL (FK column must be nullable). |
| RESTRICT | Block parent deletion if any child row references it. (NO ACTION similar; timing may differ by DBMS.) |

**Normalisation**:

Partial dependency: A non-prime attribute A is partially dependent on candidate key K if a proper subset X ⊂ K exists such that X → A.

Transitive dependency: A non-prime attribute A is transitively dependent on key K if K → Y and Y → A, where Y is not a superkey.

| NF | Rule (one sentence) | Anomaly removed | Before → After |
|---|---|---|---|
| 1NF | Every column holds only atomic values; no repeating groups or arrays. | Multi-valued attribute redundancy/ambiguity. | `Student(SID, Name, Phones='9876,5432')` → `Student(SID, Name)`, `StudentPhone(SID, Phone)` |
| 2NF | In 1NF and no non-prime attribute is partially dependent on any candidate key (no proper subset of a composite key determines a non-prime attribute). | Partial dependency redundancy and update anomaly. | `Enrollment(SID, CID, SName, CName)` PK`{SID,CID}`; `SName` depends on `SID` → `Student(SID,SName)`, `Course(CID,CName)`, `Enrollment(SID,CID)` |
| 3NF | In 2NF and no non-prime attribute is transitively dependent on any candidate key (for every FD X→A, X is a superkey or A is prime). | Transitive dependency redundancy and update anomaly. | `Student(SID, DeptID, DeptName)` with `SID→DeptID→DeptName` → `Student(SID,DeptID)`, `Department(DeptID,DeptName)` |
| BCNF | In 3NF and for every non-trivial FD X→Y, X is a superkey. | Anomaly from a non-superkey determining a prime attribute. | `TeacherCourse(StudentID, Course, Teacher)` with `{StudentID,Course}→Teacher` and `Teacher→Course` → `TeacherCourse(Teacher,Course)`, `StudentTeacher(StudentID,Teacher)` |

Denormalisation: Intentionally reintroducing redundancy by merging tables or duplicating columns. Purpose: reduce joins and improve read performance in reporting/OLAP or read-heavy systems. Cost: update anomalies, more storage, more complex integrity enforcement.

**ACID**:

| Property | Definition | Violation example |
|---|---|---|
| Atomicity | Transaction executes all operations or none. | Bank transfer debits account A but crash occurs before crediting B; money vanishes. |
| Consistency | Transaction moves DB from one valid state to another, preserving all constraints. | Insert child row with non-existent foreign key; orphan record remains. |
| Isolation | Concurrent transactions do not see each other's intermediate states. | Dirty read: T2 reads T1's uncommitted update; T1 rolls back; T2 used invalid data. |
| Durability | Committed changes survive system failure. | Power failure immediately after COMMIT; update lost because log not flushed. |

**Transactions**:
A transaction is a sequence of operations treated as one logical unit.
COMMIT: makes all changes since last COMMIT/ROLLBACK permanent.
ROLLBACK: undoes all changes since last COMMIT (or to a SAVEPOINT).
SAVEPOINT: names an intermediate point within a transaction; ROLLBACK TO SAVEPOINT undoes only changes after that point.

**Concurrency problems**:

| Problem | Description |
|---|---|
| Dirty read | T1 modifies a row; T2 reads uncommitted value; T1 rolls back. T2 has invalid data. |
| Non-repeatable read | T1 reads a row; T2 updates/deletes and commits; T1 re-reads same row and sees different/missing value. |
| Phantom read | T1 runs a query; T2 inserts/deletes rows satisfying the query and commits; T1 re-runs query and sees new/missing rows. |
| Lost update | T1 and T2 read same value; both write based on it; one write overwrites the other. |

**Isolation levels**:

| Isolation level | Dirty read | Non-repeatable read | Phantom read | Lost update |
|---|---|---|---|---|
| READ UNCOMMITTED | Possible | Possible | Possible | Possible |
| READ COMMITTED | Prevented | Possible | Possible | Possible |
| REPEATABLE READ | Prevented | Prevented | Possible (prevented in MySQL InnoDB via next-key locks) | Prevented (in most locking DBMS) |
| SERIALIZABLE | Prevented | Prevented | Prevented | Prevented |### SQL sub-languages

| Sub-language | Purpose | Statements | Transaction behaviour |
|---|---|---|---|
| **DDL** (Data Definition) | Define/alter structure | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME`, `COMMENT` | Auto-commit in MySQL/Oracle; `TRUNCATE`/`DROP` are rollback-able in PostgreSQL and SQL Server |
| **DML** (Data Manipulation) | Change/read data | `INSERT`, `UPDATE`, `DELETE`, `MERGE` (upsert), `SELECT`* | Transactional; needs `COMMIT` |
| **DCL** (Data Control) | Permissions | `GRANT`, `REVOKE` | Auto-commit in most engines |
| **TCL** (Transaction Control) | Transaction boundaries | `COMMIT`, `ROLLBACK`, `SAVEPOINT`, `RELEASE SAVEPOINT`, `SET TRANSACTION` | — |

\*`SELECT` is often split out as **DQL**. `TRUNCATE` is DDL (drops and recreates the segment, resets identity, cannot take a `WHERE`), `DELETE` is DML (row-by-row, `WHERE`, fires triggers, rollback-able).

### JOINs

Base tables used in every example below.

**students**

| id | name |
|---|---|
| 1 | Asha |
| 2 | Bhanu |
| 3 | Chetan |
| 4 | Divya |

**enrolments**

| student_id | course |
|---|---|
| 1 | SQL |
| 1 | Java |
| 3 | SQL |
| 5 | Python |

All queries join on `students.id = enrolments.student_id`. Row order is never guaranteed unless `ORDER BY` is used.

#### INNER JOIN

Returns only row pairs where the join predicate is TRUE. Non-matching rows on **both** sides are dropped.

`SELECT name, course FROM students INNER JOIN enrolments ON students.id = enrolments.student_id;`

| name | course |
|---|---|
| Asha | SQL |
| Asha | Java |
| Chetan | SQL |

3 rows. Bhanu (id 2) and Divya (id 4) have no enrolment; enrolment row `(5, Python)` has no student.

#### LEFT JOIN / LEFT OUTER JOIN

Keeps **every** row of the left table. If no right row matches, the right columns are filled with **NULL** — one output row per unmatched left row (not zero, not a blank string, not 0).

`SELECT name, course FROM students LEFT JOIN enrolments ON students.id = enrolments.student_id;`

| name | course |
|---|---|
| Asha | SQL |
| Asha | Java |
| Bhanu | **NULL** |
| Chetan | SQL |
| Divya | **NULL** |

5 rows. `OUTER` is optional noise — `LEFT JOIN` = `LEFT OUTER JOIN`.

Trap: a filter on the right table in `WHERE` silently converts a LEFT JOIN into an INNER JOIN, because `NULL = 'SQL'` is UNKNOWN, not TRUE.

- `ON students.id = enrolments.student_id AND course = 'SQL'` → keeps Bhanu and Divya with NULL course (5 rows: Asha/SQL, Bhanu/NULL, Chetan/SQL, Divya/NULL — 4 rows, since Asha only has one SQL row).
- `ON students.id = enrolments.student_id WHERE course = 'SQL'` → returns only Asha and Chetan; Bhanu and Divya are eliminated.

#### RIGHT JOIN / RIGHT OUTER JOIN

Mirror of LEFT JOIN: keeps every row of the right table, NULL-fills the left columns.

`SELECT name, course FROM students RIGHT JOIN enrolments ON students.id = enrolments.student_id;`

| name | course |
|---|---|
| Asha | SQL |
| Asha | Java |
| Chetan | SQL |
| **NULL** | Python |

4 rows.

#### FULL OUTER JOIN

Union of LEFT and RIGHT: all matched rows, plus unmatched rows from both sides, each NULL-filled on the missing side.

`SELECT name, course FROM students FULL OUTER JOIN enrolments ON students.id = enrolments.student_id;`

| name | course |
|---|---|
| Asha | SQL |
| Asha | Java |
| Bhanu | NULL |
| Chetan | SQL |
| Divya | NULL |
| NULL | Python |

6 rows = 3 matched + 2 left-only + 1 right-only. MySQL has no `FULL OUTER JOIN` — emulate with `LEFT JOIN UNION RIGHT JOIN`.

#### CROSS JOIN

Cartesian product: every row of the left table paired with every row of the right table. **No `ON` clause.** Result size = rows(left) × rows(right) = 4 × 4 = **16 rows**.

`SELECT students.id, name, student_id, course FROM students CROSS JOIN enrolments;`

| id | name | student_id | course |
|---|---|---|---|
| 1 | Asha | 1 | SQL |
| 1 | Asha | 1 | Java |
| 1 | Asha | 3 | SQL |
| 1 | Asha | 5 | Python |
| 2 | Bhanu | 1 | SQL |
| 2 | Bhanu | 1 | Java |
| 2 | Bhanu | 3 | SQL |
| 2 | Bhanu | 5 | Python |
| 3 | Chetan | 1 | SQL |
| 3 | Chetan | 1 | Java |
| 3 | Chetan | 3 | SQL |
| 3 | Chetan | 5 | Python |
| 4 | Divya | 1 | SQL |
| 4 | Divya | 1 | Java |
| 4 | Divya | 3 | SQL |
| 4 | Divya | 5 | Python |

An accidental `FROM a, b` with no `WHERE` is a CROSS JOIN — a classic cause of row explosion.

#### SELF JOIN

A table joined to itself, using two different aliases. Needed whenever a row references another row of the same table (hierarchy, "same city as", comparison).

**employees**

| id | name | mgr_id |
|---|---|---|
| 1 | Asha | NULL |
| 2 | Bhanu | 1 |
| 3 | Chetan | 1 |
| 4 | Divya | 2 |

`SELECT e.name AS emp, m.name AS mgr FROM employees e LEFT JOIN employees m ON e.mgr_id = m.id;`

| emp | mgr |
|---|---|
| Asha | NULL |
| Bhanu | Asha |
| Chetan | Asha |
| Divya | Bhanu |

A self JOIN is an ordinary INNER/LEFT/RIGHT/CROSS join whose two inputs happen to be the same table; the aliases are mandatory.

### WHERE vs HAVING

`WHERE` filters **rows before grouping**. `HAVING` filters **groups after aggregation**. `WHERE` runs on raw table rows, so it cannot contain an aggregate. `HAVING` runs after `GROUP BY`, so it can.

**sales**

| id | dept | amount |
|---|---|---|
| 1 | A | 100 |
| 2 | A | 200 |
| 3 | B | 50 |
| 4 | B | 60 |
| 5 | B | 70 |
| 6 | C | 500 |

`SELECT dept, COUNT(*) FROM sales WHERE amount >= 60 GROUP BY dept HAVING COUNT(*) >= 2;`

| dept | COUNT(*) |
|---|---|
| A | 2 |
| B | 2 |

Row 3 (amount 50) is removed by `WHERE` first, so B has only 2 rows left; C survives `WHERE` but is dropped by `HAVING` (count 1).

| | WHERE | HAVING |
|---|---|---|
| Runs | Before `GROUP BY` | After `GROUP BY` |
| Operates on | Individual rows | Groups |
| Aggregates allowed | No (`WHERE COUNT(*) > 2` is an error) | Yes |
| Column aliases | Not allowed | Standard SQL: not allowed; MySQL allows it |
| Needs GROUP BY | No | No (turns the whole result into one group) |
| Filters on | Base columns | Base columns, aggregates, grouped expressions |

### Logical order of execution of a SELECT statement

| Step | Clause | What happens |
|---|---|---|
| 1 | `FROM` | Load source tables |
| 2 | `ON` | Evaluate join predicate |
| 3 | `JOIN` | Build the joined row set (INNER/LEFT/…/CROSS) |
| 4 | `WHERE` | Discard rows whose predicate is not TRUE |
| 5 | `GROUP BY` | Collapse rows into groups |
| 6 | `HAVING` | Discard groups whose predicate is not TRUE |
| 7 | `SELECT` | Compute the output expressions **and their aliases** |
| 8 | `DISTINCT` | Remove duplicate output rows |
| 9 | `ORDER BY` | Sort the final rows |
| 10 | `LIMIT` / `OFFSET` | Truncate the result |

Consequences:

- **A SELECT alias cannot be used in `WHERE`.** `WHERE` (step 4) executes before `SELECT` (step 7) — the alias does not exist yet. `SELECT price * qty AS total FROM items WHERE total > 100;` fails; write `WHERE price * qty > 100`.
- **A SELECT alias *can* be used in `ORDER BY`**, because `ORDER BY` (step 9) runs after `SELECT` (step 7). This is the only clause where the SQL standard guarantees alias visibility.
- A SELECT alias cannot be used in `HAVING` in standard SQL (step 6 precedes step 7). MySQL permits it; PostgreSQL permits it in `GROUP BY` and `ORDER BY` only; Oracle and SQL Server permit it only in `ORDER BY`.
- `WHERE` also runs before `GROUP BY`, so `WHERE` can never reference an aggregate — use `HAVING`.
- `LIMIT` runs last, so it can reference an `ORDER BY` column but nothing else is recomputed after truncation.

### GROUP BY and aggregate functions

Rules:

1. Every expression in the `SELECT` list that is **not** inside an aggregate must appear in `GROUP BY` (standard SQL; MySQL enforces this only with `ONLY_FULL_GROUP_BY` enabled).
2. `GROUP BY` may take multiple columns or expressions — grouping is by the combination.
3. All NULLs in the grouping column form **one** group (NULLs are treated as equal for grouping and for `DISTINCT`).
4. `WHERE` cannot contain aggregates; `HAVING` can, and may reference aggregates not present in `SELECT`.
5. Without `GROUP BY`, an aggregate query returns exactly one row — even if the table is empty (`COUNT` → 0, everything else → NULL).

Aggregates: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` (plus `COUNT(DISTINCT …)`, `STRING_AGG`/`GROUP_CONCAT` for text).

**t**

| id | dept | bonus |
|---|---|---|
| 1 | A | 100 |
| 2 | A | NULL |
| 3 | B | 200 |
| 4 | B | 200 |
| 5 | NULL | NULL |

| Expression | Result | Rule |
|---|---|---|
| `COUNT(*)` | 5 | Counts **rows**, NULLs included |
| `COUNT(bonus)` | 3 | Counts **non-NULL values** only |
| `COUNT(DISTINCT bonus)` | 2 | Counts distinct non-NULL values (100, 200) |
| `COUNT(dept)` | 4 | Excludes the NULL dept |
| `COUNT(DISTINCT dept)` | 2 | A, B — NULL excluded |
| `SUM(bonus)` | 500 | NULLs ignored |
| `AVG(bonus)` | 166.67 | 500 / 3, **not** 500 / 5 — the denominator is the non-NULL count |
| `MIN(bonus)` / `MAX(bonus)` | 100 / 200 | NULLs ignored |

`SELECT dept, COUNT(*) FROM t GROUP BY dept;` → `A:2`, `B:2`, `NULL:1`.

If a column is entirely NULL: `SUM`/`AVG`/`MIN`/`MAX` return NULL, `COUNT(col)` returns 0. `COUNT(*)` never returns NULL.

`COUNT(*)` is not "slower than COUNT(1)" in modern optimisers — both count rows.

### NULL handling

NULL is a marker for **unknown or absent**, not a value. Consequences:

- `NULL = NULL` evaluates to UNKNOWN, not TRUE; therefore `WHERE col = NULL` returns **zero rows**. Same for `<> NULL`, `IN (NULL)`, `NOT IN (…, NULL)`.
- Use `IS NULL` / `IS NOT NULL`. `IS NULL` is a predicate, not a function.
- `NOT IN (1, 2, NULL)` returns **no rows** for any value, because `x <> NULL` is UNKNOWN and `NOT UNKNOWN` is UNKNOWN. `NOT EXISTS` has no such trap — prefer it.
- Arithmetic with NULL yields NULL: `100 + NULL = NULL`. `CONCAT('a', NULL)` yields NULL in MySQL and SQL Server and in standard `||`; Oracle treats the empty string as NULL and `||` treats NULL as empty.
- Any comparison with NULL, except `IS [NOT] NULL` and `<=>` (MySQL null-safe equality), yields UNKNOWN.

| Function | Behaviour | Example | Result |
|---|---|---|---|
| `COALESCE(a, b, c, …)` | First non-NULL argument (standard SQL, any number of args) | `COALESCE(NULL, 5, 9)` | 5 |
| `NULLIF(a, b)` | NULL if `a = b`, else `a` | `NULLIF(10, 10)` / `NULLIF(10, 3)` | NULL / 10 |
| `IFNULL(a, b)` | MySQL/SQLite 2-argument `COALESCE` | `IFNULL(NULL, 7)` | 7 |
| `ISNULL(a, b)` | SQL Server 2-argument function — **not** the `IS NULL` predicate | `ISNULL(NULL, 7)` | 7 |

**Three-valued logic** (TRUE / FALSE / UNKNOWN, where UNKNOWN is produced by any comparison involving NULL):

| `AND` | TRUE | FALSE | UNKNOWN |
|---|---|---|---|
| **TRUE** | TRUE | FALSE | UNKNOWN |
| **FALSE** | FALSE | FALSE | FALSE |
| **UNKNOWN** | UNKNOWN | FALSE | UNKNOWN |

| `OR` | TRUE | FALSE | UNKNOWN |
|---|---|---|---|
| **TRUE** | TRUE | TRUE | TRUE |
| **FALSE** | TRUE | FALSE | UNKNOWN |
| **UNKNOWN** | TRUE | UNKNOWN | UNKNOWN |

`NOT UNKNOWN = UNKNOWN`. `WHERE` and `HAVING` keep a row **only** when the predicate is TRUE; FALSE and UNKNOWN are both discarded. A `CHECK` constraint, by contrast, passes when the condition is TRUE **or UNKNOWN**. In a `UNIQUE` column, most engines (PostgreSQL, MySQL, Oracle) allow many NULLs because NULLs are not equal; SQL Server allows only one per unique constraint. Aggregates, `GROUP BY` and `DISTINCT` all skip or collapse NULLs as shown above.

### LIKE, IN, BETWEEN, EXISTS, subqueries

**LIKE** — pattern matching. `%` = zero or more characters; `_` = exactly one character.

| Pattern | Matches | Does not match |
|---|---|---|
| `'A%'` | `Asha`, `A`, `Alok` | `Ravi` |
| `'%a'` | `Asha`, `Divya` | `Ravi` |
| `'_sha'` | `Asha` | `Ash` |
| `'%sh%'` | `Asha` | `Ravi` |
| `'A_ha'` | `Asha` | `Aisha` |

Escape a literal wildcard with `ESCAPE`: `LIKE '50\%%' ESCAPE '\'`. Case sensitivity follows the column collation, not the operator. `NOT LIKE` is not NULL-safe.

**IN** — shorthand for a chain of `OR` equalities: `x IN (1,2,3)` ≡ `x = 1 OR x = 2 OR x = 3`. `NOT IN` is the NULL trap described above.

**BETWEEN a AND b** — inclusive on both ends, equivalent to `x >= a AND x <= b`. `BETWEEN 10 AND 5` is always empty (bounds are not swapped). It works on dates and strings too.

**EXISTS** — returns TRUE/FALSE based on whether the subquery returns at least one row; the select list is irrelevant, so `EXISTS (SELECT 1 FROM …)` is idiomatic. It short-circuits on the first row, and `NOT EXISTS` is NULL-safe.

| | Non-correlated subquery | Correlated subquery |
|---|---|---|
| References outer query | No | Yes |
| Executed | Once, independently — can be run standalone | Once per candidate outer row |
| Typical use | `WHERE id IN (SELECT …)`, `WHERE salary > (SELECT AVG(salary) FROM emp)` | `WHERE EXISTS (SELECT 1 FROM … WHERE inner.dept = outer.dept)` |
| Cost | One extra execution | Potentially O(outer rows) unless the optimiser rewrites it as a join |

A scalar subquery must return exactly one column and at most one row, and can be used anywhere a value is allowed. A subquery in `FROM` is a derived table and **must** have an alias.

### Indexes

An index is a separate, sorted data structure that maps key values to row locations. The default structure is a **B-tree** (balanced tree, all leaves at the same depth), which makes equality and range lookups O(log n) instead of a full O(n) scan. Hash indexes support equality only. A B-tree's entries are sorted by the **leading** column first.

| | Clustered index | Non-clustered index |
|---|---|---|
| Stores the table rows | Yes — the leaf level **is** the data | No — leaves hold a row locator |
| Physical row order | Determined by the key | Unaffected |
| Count per table | Exactly one (or zero) | Many |
| Row locator | — | Clustering key value, or RID on a heap (SQL Server) |
| Example | InnoDB primary key; `PRIMARY KEY` clustered by default | Every `CREATE INDEX` |

InnoDB: the primary key *is* the clustered index, so secondary indexes store the primary-key value as their pointer — a lookup via a secondary index costs two B-tree traversals. If no primary key exists, InnoDB promotes the first `UNIQUE NOT NULL` index, else creates a hidden 6-byte row id.

**An index helps when**

- The column appears in `WHERE` with `=`, `<`, `>`, `BETWEEN`, or a prefix `LIKE 'abc%'`.
- The column is a join key.
- The column drives `ORDER BY` / `GROUP BY` that matches the index order — avoiding a sort.
- The column has high selectivity (many distinct values relative to rows).

**An index hurts when**

- The table is write-heavy: every `INSERT`, `UPDATE` of an indexed column, and `DELETE` must maintain every index.
- Storage grows, and the optimiser has more access paths to evaluate.
- The column is low-cardinality (e.g. a status flag with three values) — a scan is cheaper than the extra lookups.
- The optimiser estimates the predicate matches so many rows that a table scan wins anyway.

**Why `LIKE '%x'` cannot use an index:** a B-tree is sorted by the string's *prefix*. With a leading wildcard there is no known prefix, so no range of the tree can be isolated — the engine must read every entry (index scan or full table scan). `LIKE 'x%'` gives a prefix and becomes a range seek. The same logic explains why wrapping the column in a function kills index use: `WHERE YEAR(order_date) = 2024` cannot seek, but `WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01'` can. Such predicates are called non-sargable.

**Composite index / leftmost-prefix rule:** an index on `(a, b)` serves `WHERE a = ?` and `WHERE a = ? AND b = ?`, but **not** `WHERE b = ?` alone. Column order in the index definition matters more than the columns chosen.

**Covering index:** an index that contains every column the query needs (key columns plus non-key `INCLUDE`d columns in SQL Server, or all referenced columns in the key elsewhere). The engine answers from the index alone — an index-only scan — with no lookup into the table or clustered index. This is the standard fix for a hot query that reads few columns from a wide table. Note that Oracle B-tree indexes store no entry for a row whose indexed columns are all NULL, so `IS NULL` on such a column cannot use that index.

### Views, stored procedures, triggers

**View** — a named, stored `SELECT` that behaves like a read-only virtual table. It holds no data of its own (unless explicitly materialised), so it always reflects the underlying tables, and it is used to encapsulate a complex join, expose only certain columns or rows, and give a stable interface over a renamed schema. A plain view is updatable only when it maps simply to one base table with no aggregates, `DISTINCT`, `GROUP BY`, or `UNION`; complex views are read-only, and a `WITH CHECK OPTION` clause prevents inserts or updates that would not satisfy the view's `WHERE`.

**Stored procedure** — a named, precompiled block of SQL plus control flow (`IF`, loops, variables, exception handling) stored in the database and executed with `CALL` (MySQL/PostgreSQL) or `EXEC` (SQL Server). It accepts `IN`/`OUT` parameters, reduces round trips and repeated parsing, and centralises business logic; the trade-offs are database-vendor lock-in and logic that is harder to version than application code. Stored procedures do **not** run inside a SELECT statement, unlike functions, which are the correct tool when a computed value is needed inside a query.

**Trigger** — a block of code attached to a table that fires automatically in response to `INSERT`, `UPDATE`, or `DELETE`. It can run `BEFORE` or `AFTER` the statement, per row or per statement, and typically has access to `OLD` and `NEW` row values. The canonical use is **audit logging**: an `AFTER UPDATE` or `AFTER DELETE` trigger writes the changed row, the old and new values, the user, and a timestamp into an audit table, which cannot be bypassed by an application path that forgets to log. Other uses are maintaining derived or denormalised columns, cascading changes, and enforcing constraints that a `CHECK` cannot express. Risks: triggers fire invisibly (so a single `DELETE` can cascade into unexpected side effects), they add per-row overhead on every write, and they can recurse if a trigger writes to its own table.

## 4. Must-memorise block

**Data types**

| Type | Notes |
|---|---|
| `INT` / `INTEGER`, `SMALLINT`, `BIGINT` | Exact whole numbers |
| `DECIMAL(p,s)` / `NUMERIC(p,s)` | Exact fixed-point — the only correct choice for money |
| `FLOAT` / `REAL` / `DOUBLE` | Approximate binary floating point — never use for currency |
| `CHAR(n)` | Fixed length, space-padded |
| `VARCHAR(n)` / `TEXT` / `CLOB` | Variable-length character data |
| `DATE`, `TIME`, `TIMESTAMP` / `DATETIME` | `TIMESTAMP` may carry time zone; `DATETIME` does not |
| `BOOLEAN` | TRUE / FALSE / UNKNOWN |
| `BLOB` | Binary large object |

**Normal forms**

| Form | Requirement |
|---|---|
| 1NF | Atomic values only; no repeating groups; each row identifiable by a key |
| 2NF | 1NF + no non-key attribute depends on **part** of a composite candidate key |
| 3NF | 2NF + no transitive dependency (non-key attribute depending on another non-key attribute) |
| BCNF | For every functional dependency `X → Y`, `X` is a superkey (stricter than 3NF; removes anomalies from overlapping candidate keys) |
| 4NF | BCNF + no non-trivial multivalued dependencies |

Goal of normalisation: eliminate insert/update/delete anomalies. **Denormalisation** deliberately reintroduces redundancy to avoid joins on read-heavy workloads.

**ACID**

| Property | Meaning |
|---|---|
| Atomicity | A transaction's statements all apply or none do |
| Consistency | A transaction moves the database from one valid state to another; constraints hold at commit |
| Isolation | Concurrent transactions do not see each other's uncommitted work |
| Durability | Committed changes survive a crash (write-ahead / redo log) |

Isolation levels vs phenomena: `READ UNCOMMITTED` allows dirty reads; `READ COMMITTED` allows non-repeatable reads and phantoms; `REPEATABLE READ` allows phantoms in the standard (InnoDB's `REPEATABLE READ` blocks them with next-key locks); `SERIALIZABLE` prevents all three. Higher isolation = more locking = less concurrency.

**Join types**

| Join | Keeps |
|---|---|
| `INNER` | Matched pairs only |
| `LEFT [OUTER]` | All left rows; unmatched right columns = NULL |
| `RIGHT [OUTER]` | All right rows; unmatched left columns = NULL |
| `FULL [OUTER]` | All rows from both sides, NULL-filled where unmatched |
| `CROSS` | Cartesian product, rows × rows, no `ON` clause |
| `SELF` | Same table joined to itself under two aliases |

`A LEFT JOIN B ON … WHERE b.col = x` behaves as an INNER JOIN; put the condition in `ON` to preserve unmatched left rows.

**WHERE vs HAVING**

- `WHERE` filters rows before grouping; cannot use aggregates.
- `HAVING` filters groups after grouping; can use aggregates.
- Aliases: never in `WHERE`; `ORDER BY` always; MySQL also allows them in `GROUP BY` and `HAVING`.

**Logical execution order**

`FROM → ON → JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT`

Alias available in `ORDER BY` because `SELECT` precedes it; unavailable in `WHERE`/`HAVING` because it follows them.

**COUNT variants**

| Expression | Counts |
|---|---|
| `COUNT(*)` | Every row, NULLs included |
| `COUNT(col)` | Non-NULL values of `col` |
| `COUNT(DISTINCT col)` | Distinct non-NULL values of `col` |

`AVG(col)` divides by the non-NULL count. `SUM`/`AVG`/`MIN`/`MAX` return NULL over an all-NULL (or empty) input; `COUNT` returns 0.

**NULL rules**

- NULL is unknown/absent, not a value; `= NULL`, `<> NULL` and `NOT IN (…, NULL)` never return rows.
- Use `IS NULL` / `IS NOT NULL`; `COALESCE` for the first non-NULL; `NULLIF(a,b)` to turn a sentinel into NULL; `IFNULL`/`ISNULL` are 2-argument vendor equivalents.
- Aggregates (except `COUNT(*)`) ignore NULLs; `GROUP BY` and `DISTINCT` treat all NULLs as one group.
- Any arithmetic or comparison with NULL yields NULL/UNKNOWN; `WHERE` keeps only TRUE rows; `CHECK` passes on TRUE or UNKNOWN.
- `NOT EXISTS` is NULL-safe where `NOT IN` is not.

**Index rules of thumb**

- Index the columns used in `WHERE`, `JOIN`, `ORDER BY` and `GROUP BY`.
- Composite index follows the leftmost-prefix rule: `(a,b)` serves `a` and `a,b`, not `b`.
- One clustered index per table (InnoDB: the primary key); many non-clustered indexes allowed.
- Every index adds write cost on `INSERT`/`UPDATE`/`DELETE` plus storage — do not index everything.
- Low-selectivity columns rarely benefit from a standalone index.
- `LIKE '%x'` and functions wrapping the column are non-sargable and force a scan; `LIKE 'x%'` and range predicates can seek.
- A covering index containing every referenced column enables an index-only scan with no table lookup.

## 5. Worked examples

### Example 1 — LEFT JOIN row count with NULL marks

Students:

| student_id | name |
|---:|---|
| 1 | Asha |
| 2 | Bina |
| 3 | Chetan |
| 4 | Dev |

Marks:

| student_id | subject | score |
|---:|---|---:|
| 1 | Math | 80 |
| 1 | Physics | 75 |
| 2 | Math | NULL |
| 4 | Math | 90 |

Query:

```sql
SELECT s.student_id, s.name, m.subject, m.score
FROM students s
LEFT JOIN marks m ON s.student_id = m.student_id
ORDER BY s.student_id, m.subject;
```

Step-by-step:

- Matching join rows: student 1 has 2 marks, student 2 has 1 mark, student 4 has 1 mark.
- Matching total = 2 + 1 + 1 = 4.
- Unmatched left rows: student 3 has no marks. LEFT JOIN produces 1 row with `m.subject = NULL`, `m.score = NULL`.
- Total result rows = 4 + 1 = 5.
- Student 2's `score` is NULL, but the join condition is on `student_id`, so it is still a matching row. It does not create an extra nonmatching row.

Result:

| student_id | name | subject | score |
|---:|---|---|---:|
| 1 | Asha | Math | 80 |
| 1 | Asha | Physics | 75 |
| 2 | Bina | Math | NULL |
| 3 | Chetan | NULL | NULL |
| 4 | Dev | Math | 90 |

`COUNT(*)` over this result = 5. `COUNT(m.score)` = 3, because two rows have NULL score.

**Final answer: 5 rows.**

---

### Example 2 — GROUP BY, WHERE vs HAVING, character count

Employees:

| emp_id | dept | hire_year | commission | name |
|---:|---|---:|---:|---|
| 1 | Sales | 2020 | 1000 | anna |
| 2 | Sales | 2019 | NULL | alan |
| 3 | Sales | 2021 | 500 | bella |
| 4 | IT | 2020 | NULL | aarav |
| 5 | IT | 2021 | 200 | diya |
| 6 | HR | 2022 | NULL | ravi |

Query:

```sql
SELECT dept,
       COUNT(*) AS emp_count,
       COUNT(commission) AS comm_count,
       SUM(CHAR_LENGTH(name) - CHAR_LENGTH(REPLACE(name, 'a', ''))) AS a_count
FROM employees
WHERE hire_year >= 2020
GROUP BY dept
HAVING COUNT(*) >= 2
ORDER BY dept;
```

Step-by-step:

- `WHERE hire_year >= 2020` keeps emp_id 1, 3, 4, 5, 6. Excludes emp_id 2.
- Sales group: rows 1 and 3.
  - `COUNT(*)` = 2.
  - `COUNT(commission)` = 2, because 1000 and 500 are non-NULL.
  - `a_count`: `anna` = 4 − 2 = 2; `bella` = 5 − 4 = 1. Sum = 3.
- IT group: rows 4 and 5.
  - `COUNT(*)` = 2.
  - `COUNT(commission)` = 1, because row 4 commission is NULL.
  - `a_count`: `aarav` = 5 − 2 = 3; `diya` = 4 − 3 = 1. Sum = 4.
- HR group: row 6.
  - `COUNT(*)` = 1.
  - `HAVING COUNT(*) >= 2` removes HR.

Result:

| dept | emp_count | comm_count | a_count |
|---|---|---:|---:|
| IT | 2 | 1 | 4 |
| Sales | 2 | 2 | 3 |

`WHERE` filtered rows before grouping. `HAVING` filtered groups after aggregation.

**Final answer: IT (2, 1, 4) and Sales (2, 2, 3).**

---

### Example 3 — NULL handling in aggregates and predicates

Scores:

| score |
|---:|
| 80 |
| NULL |
| 75 |
| NULL |
| 90 |

Query:

```sql
SELECT COUNT(*) AS rows,
       COUNT(score) AS non_null_scores,
       SUM(score) AS total,
       AVG(score) AS avg_score,
       AVG(COALESCE(score, 0)) AS avg_with_zero
FROM marks;
```

Step-by-step:

- `COUNT(*)`: counts all 5 rows.
- `COUNT(score)`: skips the 2 NULLs, so 3.
- `SUM(score)`: 80 + 75 + 90 = 245.
- `AVG(score)`: 245 / 3 = 81.6667.
- `AVG(COALESCE(score, 0))`: (80 + 0 + 75 + 0 + 90) / 5 = 245 / 5 = 49.0000.

Predicates:

- `WHERE score <> 80` returns 75 and 90 only. NULL rows are not returned because `NULL <> 80` is UNKNOWN, not TRUE.
- `WHERE score IS NULL` returns the two NULL rows.

**Final answer: rows = 5, non_null_scores = 3, total = 245, avg_score = 81.6667, avg_with_zero = 49.0000.**

---

### Example 4 — Index optimisation on email, LIKE, primary-key choice

Table `users`:

| user_id | email | created_at |
|---:|---|---|
| 1 | a@b.com | 2024-01-01 |
| 2 | c@d.com | 2024-01-02 |

Assume `user_id` is the primary key and there is no index on `email`.

Query comparison:

| Query | Index use |
|---|---|
| `WHERE email = 'a@b.com'` | B-tree index on `email` can be used. Create `UNIQUE INDEX ux_users_email ON users(email);` if uniqueness is required. |
| `WHERE email LIKE 'a%@b.com'` | Leading literal `a` allows a B-tree range scan on `email`, then residual filtering. |
| `WHERE email LIKE '%@b.com'` | Leading `%` prevents a normal B-tree seek. Likely full scan unless an index-only scan is cheaper or a trigram/full-text index exists. |
| `WHERE LOWER(email) = 'a@b.com'` | Function on the column is not sargable. A normal `email` index is not used. Use case-insensitive collation, store lowercased email, or create a function-based index on `LOWER(email)`. |

Primary-key choice:

- `users`: email is unique but can change and is longer than an integer. Use `user_id` as a surrogate primary key and add `UNIQUE(email)`.
- `enrollments(student_id, course_id, grade)` with rule “a student can take a course once”: use composite primary key `(student_id, course_id)`. It enforces the rule and gives a useful join index. If a surrogate `enrollment_id` is added, still add `UNIQUE(student_id, course_id)`.

**Final answer: create a B-tree/UNIQUE index on email for equality and prefix LIKE; `LIKE '%@b.com'` and `LOWER(email)=` do not use a normal email index. For users choose `user_id` PK + `UNIQUE(email)`; for the enrollment table choose composite PK `(student_id, course_id)`.**

---

### Example 5 — UPDATE, trigger logging delete, concurrency

Tables:

```sql
employees(emp_id INT PRIMARY KEY, name VARCHAR(50), salary INT)
employee_delete_log(log_id INT AUTO_INCREMENT PRIMARY KEY,
                    emp_id INT, name VARCHAR(50), deleted_at DATETIME)
```

Trigger:

```sql
CREATE TRIGGER trg_employee_after_delete
AFTER DELETE ON employees
FOR EACH ROW
INSERT INTO employee_delete_log (emp_id, name, deleted_at)
VALUES (OLD.emp_id, OLD.name, CURRENT_TIMESTAMP);
```

Questions:

- (a) `DELETE FROM employees WHERE emp_id = 7;` succeeds. What log row appears?
- (b) If the transaction rolls back, what happens to the log row?
- (c) Initial salary for `emp_id = 5` is 5000. T1 and T2 each run `UPDATE employees SET salary = salary + 100 WHERE emp_id = 5;` and commit. Final salary?
- (d) If both run `UPDATE employees SET salary = 6000 WHERE emp_id = 5;` and commit, final salary?
- (e) Which isolation level can see the uncommitted log row?

Step-by-step:

- (a) `AFTER DELETE` trigger fires once per deleted row. It inserts `OLD.emp_id = 7`, `OLD.name` = deleted employee's name, and current timestamp.
- (b) In a transactional engine with a transactional log table, the trigger insert is part of the same transaction. `ROLLBACK` undoes both the delete and the log insert. If the log table is non-transactional, the insert may persist; this is engine-dependent.
- (c) Row-level locking: T2 waits for T1. T1 writes 5100. T2 then reads 5100 and writes 5200. Final = 5000 + 100 + 100 = 5200.
- (d) Both write the absolute value 6000. T1 commits 6000; T2 then sets 6000 again. Final = 6000, not 6200.
- (e) `READ UNCOMMITTED` permits dirty reads. `READ COMMITTED`, `REPEATABLE READ`, and `SERIALIZABLE` prevent reading uncommitted data under normal locking/consistent reads.

**Final answer: (a) one log row for emp_id = 7 with OLD values; (b) rolls back with the DELETE in transactional tables; (c) 5200; (d) 6000; (e) READ UNCOMMITTED.**

---

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid |
|---|---|---|
| LEFT JOIN then `WHERE right_table.col = ...` | The `WHERE` removes NULL-extended rows, making the result behave like an INNER JOIN. | Put right-table conditions in the `ON` clause when unmatched left rows must remain. Use `WHERE` only for left-table or intended row filters. |
| `COUNT(*)` vs `COUNT(column)` | `COUNT(*)` counts rows; `COUNT(column)` skips NULLs. They differ whenever the column has NULLs. | Decide whether NULL rows should count. Use `COUNT(*)`, `COUNT(column)`, or `COUNT(COALESCE(column, ...))` deliberately. |
| `= NULL`, `<> NULL`, `NOT IN (..., NULL)` | `= NULL` yields UNKNOWN, not TRUE. `NOT IN` with a NULL in the list/subquery is never TRUE for nonmatching values, often returning no rows. | Use `IS NULL` / `IS NOT NULL`. Replace `NOT IN` with `NOT EXISTS` or remove NULLs from the list. |
| WHERE vs HAVING | `WHERE` runs before grouping and cannot filter on aggregates; `HAVING` runs after grouping. Putting an aggregate in `WHERE` is an error. | Row conditions go in `WHERE`; group/aggregate conditions go in `HAVING`. |
| Selecting nonaggregated columns not in GROUP BY | Some engines allow it and return arbitrary row values from the group; standard SQL rejects it. | Include every nonaggregated selected column in `GROUP BY`, or wrap it in an aggregate. |
| Index on email and `LIKE`/functions | `LIKE '%@x.com'` has a leading wildcard; `LOWER(email)=` wraps the column in a function. Normal B-tree indexes cannot seek on these. | Use prefix patterns (`LIKE 'a%'`), store normalized case, use case-insensitive collation, or create an expression/trigram index. |
| Primary key vs unique key, email as PK | PK is NOT NULL and only one per table; unique allows NULLs (often multiple). Email can change and is long. | Use a surrogate PK (`user_id`) plus `UNIQUE(email)`. For many-to-many tables, use a composite PK on the two FK columns. |
| Trigger timing and rollback | `AFTER DELETE` is per row and uses `OLD`, but its insert is part of the same transaction in transactional engines. People expect the log to survive a rollback. | Know engine/table type. If audit must survive rollback, write to a non-transactional/external log; otherwise expect rollback to undo it. |
| UPDATE concurrency and lost updates | Two sessions doing read-modify-write or absolute `SET x = 6000` can overwrite each other; `SET x = x + 100` is atomic at row level under row locking. | Use atomic increments; rely on row locks; use appropriate isolation/optimistic locking for read-modify-write logic. |

## 7. Practice questions

1. **[Easy]** *(D6 — SQL UPDATE)* Which statement increases salary by 10% for every employee in department 10?
   (a) `UPDATE employees WHERE dept_id = 10 SET salary = salary * 1.10;`
   (b) `UPDATE employees SET salary = salary * 1.10 HAVING dept_id = 10;`
   (c) `UPDATE employees SET salary = salary * 1.10 WHERE dept_id = 10;`
   (d) `UPDATE employees SET salary = 10% WHERE dept_id = 10;`

2. **[Easy]** *(D6 — NULL handling)* Which condition correctly finds rows where `email` has no value?
   (a) `WHERE email IS NULL`
   (b) `WHERE email = NULL`
   (c) `WHERE email <> NULL`
   (d) `WHERE email = ''`

3. **[Easy]** *(D6 — primary-key choice)* For a Student table, which is the best primary key?
   (a) `student_name`
   (b) `email`
   (c) `student_id` generated unique and not changing
   (d) `phone_number`

4. **[Easy]** *(D6 — LIKE)* Which query returns names that start with `A`?
   (a) `WHERE name = 'A*'`
   (b) `WHERE name LIKE '%A'`
   (c) `WHERE name LIKE 'A%'`
   (d) `WHERE name LIKE '_A%'`

5. **[Medium]** *(D6 — LEFT JOIN)* `students` has 5 rows. `marks` has 3 rows: student_id 1 has two marks, student_id 2 has one mark, no other student has marks. How many rows does `SELECT * FROM students s LEFT JOIN marks m ON s.student_id = m.student_id` return?
   (a) 5
   (b) 6
   (c) 3
   (d) 8

6. **[Medium]** *(D6 — WHERE vs HAVING)* Which statement is correct about `WHERE` and `HAVING`?
   (a) `WHERE` filters groups after grouping; `HAVING` filters rows before grouping.
   (b) `HAVING` can only be used without `GROUP BY`.
   (c) Both must appear before `GROUP BY`.
   (d) `WHERE` filters rows before grouping; `HAVING` filters groups after grouping.

7. **[Medium]** *(D6 — index optimisation)* A users table is queried with `WHERE email = 'a@b.com'`. Which index is most directly useful?
   (a) A B-tree index on `email`
   (b) A bitmap index on `gender`
   (c) An index on the primary key only
   (d) No index, because email contains `@`

8. **[Medium]** *(D6 — counting character occurrences)* Which expression counts occurrences of lowercase `a` in an ASCII text column `c`?
   (a) `REPLACE(c, 'a', '') - LENGTH(c)`
   (b) `LENGTH(c) - LENGTH(REPLACE(c, '', 'a'))`
   (c) `LENGTH(c) - LENGTH(REPLACE(c, 'a', ''))`
   (d) `COUNT(c) - COUNT(REPLACE(c, 'a', ''))`

8. **(c) `LENGTH(d) - LENGTH(REPLACE(c, 'a', ''))`** — Correct: removing `a` reduces length by the number of `a` occurrences.  
   - (b) Replaces empty string, not `a`.  
   - (d) `COUNT` counts rows, not characters.  
   - (a) Subtracts lengths in the wrong order and is not meaningful.

---

9. **[Medium]** *(D6 — SQL concurrency)* Two transactions read the same row, both add 10, and both write back. The second write overwrites the first, so one increment is lost. What is this problem called?
   (a) Deadlock
   (b) Phantom read
   (c) Dirty read
   (d) Lost update

9. **(d) Lost update** — Correct: one transaction's update overwrites another's, losing an increment.  
   - (c) Dirty read reads uncommitted data.  
   - (b) Phantom read sees new rows in a repeated range query.  
   - (a) Deadlock is a cycle of transactions waiting on locks.

---

10. **[Medium]** *(D6 — triggers)* You need to insert an audit row automatically whenever an employee row is deleted. Which trigger is appropriate?
    (a) `BEFORE INSERT ON employee FOR EACH ROW`
    (b) `INSTEAD OF UPDATE ON employee FOR EACH ROW`
    (c) `AFTER SELECT ON employee FOR EACH ROW`
    (d) `AFTER DELETE ON employee FOR EACH ROW`

10. **(d) `AFTER DELETE ON employee FOR EACH ROW`** — Correct: it fires after each deleted employee row, suitable for audit logging.  
    - (a) Fires on inserts, not deletes.  
    - (c) `SELECT` triggers are not standard.  
    - (b) Fires on updates, not deletes.

---

11. **[Medium]** *(D6 — GROUP BY)* Which query is valid in standard SQL?
    (a) `SELECT dept_id, COUNT(*) FROM employee GROUP BY dept_id;`
    (b) `SELECT emp_name, dept_id, COUNT(*) FROM employee GROUP BY dept_id;`
    (c) `SELECT dept_id, COUNT(*) FROM employee GROUP BY emp_name;`
    (d) `SELECT COUNT(*) FROM employee GROUP BY COUNT(*);`

11. **(a) `SELECT dept_id, COUNT(*) FROM employee GROUP BY dept_id;`** — Correct: `dept_id` is grouped and `COUNT(*)` is aggregated.  
    - (b) `emp_name` is neither grouped nor aggregated.  
    - (c) `dept_id` is not grouped or aggregated.  
    - (d) `GROUP BY COUNT(*)` is invalid.

---

12. **[Medium]** *(D6 — keys)* `Enrollment(student_id, course_id, grade)`. Which primary key best prevents a student from enrolling twice in the same course?
    (a) `PRIMARY KEY(student_id)`
    (b) `PRIMARY KEY(student_id, course_id)`
    (c) `PRIMARY KEY(grade)`
    (d) `PRIMARY KEY(course_id)`

12. **(b) `PRIMARY KEY(student_id, course_id)`** — Correct: the pair must be unique, so duplicate enrollment is blocked.  
    - (a) Allows only one course per student.  
    - (d) Allows only one student per course.  
    - (c) Grade is not a unique enrollment identifier.

---

13. **[Medium]** *(D6 — index optimisation)* Query: `SELECT * FROM employees WHERE department_id = 5 ORDER BY hire_date DESC;` Which index best supports this?
    (a) Index on `hire_date`
    (b) Composite index on `(department_id, hire_date)`
    (c) Index on `department_id`
    (d) Composite index on `(hire_date, department_id)`

13. **(b) Composite index on `(department_id, hire_date)`** — Correct: equality on `department_id` plus ordering by `hire_date` matches the index order.  
    - (c) Filters department but may still sort.  
    - (a) Helps ordering but not the department filter.  
    - (d) Wrong leading column for the equality predicate.

---

14. **[Hard]** *(D6 — composite index leftmost prefix)* Index `idx_ln_fn(last_name, first_name)` exists. Which query cannot use the index efficiently for the `first_name` filter alone?
    (a) `WHERE last_name = 'Kumar'`
    (b) `WHERE last_name LIKE 'K%'`
    (c) `WHERE last_name = 'Kumar' AND first_name = 'Ravi'`
    (d) `WHERE first_name = 'Ravi'`

14. **(d) `WHERE first_name = 'Ravi'`** — Correct: a composite index needs the leftmost column, `last_name`, to use `first_name` efficiently alone.  
    - (a) Uses the leftmost column `last_name`.  
    - (c) Uses both index columns.  
    - (b) Uses `last_name` as a range on the leftmost column.

---

15. **[Hard]** *(D6 — NULL handling in aggregates)* Table `t` has salary values `100`, `NULL`, `200`. What does `SELECT COUNT(*), COUNT(salary), AVG(salary) FROM t` return?
    (a) `3, 3, 150`
    (b) `3, 2, 150`
    (c) `2, 2, 150`
    (d) `3, 2, NULL`

15. **(b) `3, 2, 150`** — Correct: `COUNT(*)` counts all 3 rows, `COUNT(salary)` ignores `NULL`, and `AVG(salary)` averages 100 and 200.  
    - (a) Wrongly counts the `NULL` salary.  
    - (c) Wrongly excludes the `NULL` row from `COUNT(*)`.  
    - (d) Wrongly returns `NULL` for the average.

---

16. **[Hard]** *(D6 — LEFT JOIN with WHERE)* `SELECT * FROM students s LEFT JOIN marks m ON s.student_id = m.student_id WHERE m.score > 50;` What happens to students with no marks?
    (a) They are excluded because `WHERE` on the right table filters out NULL-extended rows.
    (b) The join becomes a `RIGHT JOIN`.
    (c) They appear twice.
    (d) They appear with `NULL` score.

---

16. **(a) They are excluded because `WHERE` on the right table filters out NULL-extended rows.** — Correct: `m.score > 50` is unknown for unmatched rows, so they are removed.  
    - (d) That would happen without the `WHERE` condition.  
    - (c) A left join does not duplicate unmatched students here.  
    - (b) The join type does not change to `RIGHT JOIN`.

---
## 8. Resources

| Resource | Type | Link | Free/Paid | Time | Why this one |
|---|---|---|---|---|---|
| GfG — SQL joins | Article | https://www.geeksforgeeks.org/dbms/sql-join-set-1-inner-left-right-and-full-joins/ | Free | 25 min | Worked join examples with visible result rows — exactly the exam's format |
| GfG — SQL tutorial | Tutorial series | https://www.geeksforgeeks.org/dbms/sql-tutorial/ | Free | 60 min | Complete coverage; use the clauses, aggregates and NULL sections |
| GfG — Normal forms in DBMS | Article | https://www.geeksforgeeks.org/dbms/normal-forms-in-dbms/ | Free | 25 min | 1NF to BCNF with the dependency definitions the exam uses |
| CodeChef — SQL case studies, topic-wise | Practice set | https://www.codechef.com/practice/sql-case-studies-topic-wise | Free | 90 min | **Recommended by a selected candidate** who used it to clear the SQL round |
| `question-banks/QB-T08-D6-dbms-sql.md` | Question bank | (this library) | Free | 45 min | 40 original questions with small-table join row counts |

*All external links verified resolving 2026-09-16.*

## 9. Self-check

- [ ] I can define super, candidate, primary, alternate, composite, foreign and unique keys
- [ ] I can state how PRIMARY KEY differs from UNIQUE on NULLs and on count per table
- [ ] I can state the rule for 1NF, 2NF, 3NF and BCNF and name the anomaly each removes
- [ ] I can define partial and transitive dependency
- [ ] I can state the four ACID properties with an example of violating each
- [ ] Given two small tables, I can write the exact result rows of an INNER and a LEFT JOIN
- [ ] **I can explain WHERE versus HAVING using the logical order of execution**
- [ ] I can recite the logical execution order of a SELECT statement
- [ ] I can explain why `= NULL` never matches anything
- [ ] I can state the difference between `COUNT(*)`, `COUNT(col)` and `COUNT(DISTINCT col)`
- [ ] I can say when an index helps, when it hurts, and why `LIKE '%x'` cannot use one
- [ ] I scored 13/16 or better on the practice questions

## 10. Sources

**Teaching content (§3–§9)** is adapted from `accenture-prep-final/accenture-prep-library/topics/T08-D6-dbms-sql.md`, verified in that library's QA. **Infosys evidence:** first-hand interview accounts in `../data/reviews-online.csv` and `../data/questions-observed.csv` (rows `I01`–`I25`); interview format in `../research/03-pattern-synthesis.md` §6.
