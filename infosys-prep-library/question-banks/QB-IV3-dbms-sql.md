# QB-IV3 — DBMS and SQL — Joins, GROUP BY, Keys, Indexes, NULLs

**Interview** · **Tier 3** · 36 questions

Topic file: [`IV3-dbms-sql.md`](/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library/interview/IV3-dbms-sql.md)

*Adapted from `accenture-prep-final/accenture-prep-library/question-banks/QB-T08-D6-dbms-sql.md`; verified in that library's QA. Questions and answer key are unchanged.*

**How to use this bank.** Attempt every question before opening the key, at the real pace for this section (120 seconds a question). Answer letters are balanced across a–d.

---

**1.** **[Easy]** *(D6 — joins: inner join row count)*

```sql
SELECT COUNT(*) FROM EMP INNER JOIN DEPT ON EMP.dept_id = DEPT.dept_id;
```

| EMP.emp_id | EMP.name | EMP.dept_id |
|---|---|---|
| 1 | A | 10 |
| 2 | B | 20 |
| 3 | C | 10 |
| 4 | D | NULL |
| 5 | E | 30 |

| DEPT.dept_id | DEPT.dept_name |
|---|---|
| 10 | Sales |
| 20 | HR |
| 40 | Legal |

How many rows does the query return?

(a) 3
(b) 5
(c) 4
(d) 2

---

**1. (a) 3**

The inner join keeps only rows where `EMP.dept_id` matches a `DEPT.dept_id`: emp 1 (10), emp 2 (20), emp 3 (10). Emp 4 has `dept_id = NULL` (never equal to anything) and emp 5 has 30, which has no DEPT match.

| EMP.emp_id | EMP.dept_id | Match in DEPT? |
|---|---|---|
| 1 | 10 | Yes |
| 2 | 20 | Yes |
| 3 | 10 | Yes |
| 4 | NULL | No (UNKNOWN) |
| 5 | 30 | No |

- (b) Counts all 5 EMP rows — that is a LEFT JOIN from EMP, not an inner join.
- (c) Counts emp 4 as a match by treating NULL as equal to NULL.
- (d) Forgets that both emp 1 and emp 3 match dept 10.

---

**2.** **[Easy]** *(D6 — COUNT variants and NULL)*

```sql
SELECT COUNT(*), COUNT(c), COUNT(DISTINCT c) FROM T;
```

| T.c |
|---|
| 5 |
| NULL |
| 7 |
| NULL |
| 5 |

What three values does the query return, in order?

(a) 5, 5, 2
(b) 5, 3, 3
(c) 5, 3, 2
(d) 5, 4, 2

---

**2. (c) 5, 3, 2**

`COUNT(*)` counts rows (5). `COUNT(d)` skips NULLs, leaving 5, 7, 5 (3). `COUNT(DISTINCT d)` skips NULLs and de-duplicates, leaving 5 and 7 (2).

| Value | Count(*) | Count(d) | Count(DISTINCT d) |
|---|---|---|---|
| 5 | counted | counted | counted |
| NULL | counted | skipped | skipped |
| 7 | counted | counted | counted |
| NULL | counted | skipped | skipped |
| 5 | counted | counted | counted (duplicate) |
| **Total** | **5** | **3** | **2** |

- (a) Assumes `COUNT(d)` counts NULLs — it does not.
- (b) Assumes `COUNT(DISTINCT d)` counts NULL as a distinct value.
- (d) Assumes `COUNT(d)` treats one of the NULLs as a real value.

---

**3.** **[Easy]** *(D6 — keys: foreign key enforcement)*

```sql
CREATE TABLE Customer (cust_id INT PRIMARY KEY, name VARCHAR(30));
CREATE TABLE Orders (
  order_id INT PRIMARY KEY,
  cust_id  INT REFERENCES Customer(cust_id),
  amount   INT
);
INSERT INTO Orders VALUES (101, 999, 500);   -- 999 does not exist in Customer
```

What is the result of the INSERT?

(a) The row is inserted and cust_id is set to NULL automatically.
(b) The row is inserted, and a new Customer row with cust_id 999 is created automatically.
(c) The row is inserted because cust_id is not the primary key of Orders.
(d) The statement fails with a foreign-key constraint violation.

---

**3. (d) The statement fails with a foreign-key constraint violation**

`cust_id` is a foreign key referencing `Customer(cust_id)`. A non-NULL value with no matching parent row violates the constraint and the INSERT is rejected.

- (a) NULL substitution is never done automatically; it applies only if the column were omitted and were nullable.
- (b) No cascade insert exists in standard SQL; a foreign key never creates the parent row.
- (c) The constraint applies to the foreign key itself and has nothing to do with which column is the primary key.

---

**4.** **[Easy]** *(D6 — ACID)*

A transaction debits ₹500 from account A and then credits ₹500 to account B. The credit step fails, and the debit is undone, so either both changes take effect or neither does.

Which ACID property does this describe?

(a) Durability
(b) Consistency
(c) Isolation
(d) Atomicity

---

**4. (d) Atomicity**

Atomicity means a transaction is all-or-nothing: the debit is rolled back because the credit failed.

- (b) Consistency is about the database moving from one valid state to another, not about undoing partial work.
- (c) Isolation is about concurrent transactions not interfering with each other.
- (a) Durability is about committed changes surviving a crash.

---

**5.** **[Easy]** *(D6 — keys: primary key properties)*

Which statement about a PRIMARY KEY in a relational table is TRUE?

(a) A table can have more than one primary key.
(b) A table can have at most one primary key, and none of its columns may be NULL.
(c) A primary key column may store NULL values.
(d) A primary key must always consist of exactly one column.

---

**5. (b) A table can have at most one primary key, and none of its columns may be NULL**

A primary key is unique and NOT NULL by definition, and each table may define only one.

- (a) A table may have several UNIQUE constraints, but only one PRIMARY KEY.
- (c) NULL values are forbidden in every column of the primary key.
- (d) A primary key may be composite, e.g. `(order_id, product_id)`.

---

**6.** **[Easy]** *(D6 — joins: inner join result rows)*

```sql
SELECT a FROM T1 INNER JOIN T2 ON T1.a = T2.b;
```

| T1.a |
|---|
| 1 |
| 2 |
| 3 |

| T2.b |
|---|
| 2 |
| 3 |
| 4 |

Which values are returned?

(a) 1, 2, 3
(b) 2, 3, 4
(c) 2, 3
(d) 1, 2, 3, 4

---

**6. (c) 2, 3**

Only rows satisfying `T1.a = T2.b` survive.

| T1.a | Match in T2.b? | Emitted |
|---|---|---|
| 1 | No | — |
| 2 | Yes | 2 |
| 3 | Yes | 3 |

- (a) Returns all of T1 — that is a LEFT JOIN result.
- (b) Returns all of T2 — that is a RIGHT JOIN result.
- (d) Returns the union of both columns, which is not what a join does.

---

**7.** **[Medium]** *(D6 — WHERE vs HAVING)*

```sql
SELECT dept_id, COUNT(*) AS c
FROM Emp
GROUP BY dept_id
HAVING COUNT(*) > 3;
```

Which statement is correct?

(a) HAVING and WHERE are interchangeable here; `WHERE COUNT(*) > 3` returns the same rows.
(b) HAVING can only be used together with the COUNT function.
(c) HAVING filters rows before they are grouped, so it cannot reference aggregates.
(d) HAVING filters groups after aggregation; WHERE runs before grouping and therefore cannot reference aggregates.

---

**7. (d) HAVING filters groups after aggregation; WHERE runs before grouping and therefore cannot reference aggregates**

Logical processing is FROM → WHERE → GROUP BY → HAVING → SELECT. WHERE sees individual rows, so aggregate functions are not available there.

- (a) WHERE cannot contain an aggregate; the query would be rejected.
- (b) HAVING accepts any aggregate (`SUM`, `AVG`, `MAX`, …), not only COUNT.
- (c) Reverses the order: HAVING runs after grouping, not before.

---

**8.** **[Medium]** *(D6 — logical execution order)*

Which sequence gives the logical order in which SQL clauses are processed (not the order in which they are written)?

(a) SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
(b) WHERE → FROM → GROUP BY → SELECT → HAVING → ORDER BY
(c) FROM → GROUP BY → WHERE → HAVING → ORDER BY → SELECT
(d) FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

---

**8. (d) FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY**

This is the standard logical order; `SELECT` is evaluated late, which is why column aliases defined in SELECT cannot be referenced in WHERE.

- (a) Starts with SELECT, the written order rather than the logical order.
- (c) Places WHERE after GROUP BY and ORDER BY before SELECT.
- (b) Puts WHERE before FROM and HAVING after SELECT.

---

**9.** **[Medium]** *(D6 — index usage)*

A B-tree index exists on `Customer(name)`. Which WHERE clause **cannot** use that index to narrow the search?

(a) WHERE name = 'Ravi'
(b) WHERE name LIKE 'Rav%'
(c) WHERE name LIKE '%avi'
(d) WHERE name BETWEEN 'A' AND 'M'

---

**9. (c) WHERE name LIKE '%avi'**

A leading wildcard makes the pattern a leading-substring match, so the B-tree ordering on `name` cannot be used to seek. The engine must scan the column.

- (a) Equality on the indexed column is the ideal index seek.
- (b) A prefix pattern `'Rav%'` can be turned into a range seek on the index.
- (d) BETWEEN is a range predicate on the leading column, which a B-tree supports.

---

**10.** **[Medium]** *(D6 — composite index / leftmost prefix)*

A composite B-tree index exists on `Emp(dept_id, salary)`, in that column order. Which WHERE clause can use the index efficiently?

(a) WHERE salary = 50000
(b) WHERE salary > 50000
(c) WHERE dept_id = 10 AND salary > 50000
(d) WHERE dept_id + 0 = 10

---

**10. (c) WHERE dept_id = 10 AND salary > 50000**

The leftmost indexed column `dept_id` has an equality predicate and the next column `salary` has a range predicate, which is exactly the pattern a composite B-tree handles.

- (b) `salary` alone is not a leftmost prefix, so the index cannot be used for a seek.
- (a) Same problem: the leading column `dept_id` is absent.
- (d) `dept_id + 0` is an expression on the column, so the index cannot be matched (this is also not generally sargable).

---

**11.** **[Medium]** *(D6 — LEFT JOIN with COUNT(column))*

```sql
SELECT d.dept_name, COUNT(e.emp_id) AS n
FROM DEPT d LEFT JOIN EMP e ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
```

| DEPT.dept_id | DEPT.dept_name |
|---|---|
| 10 | Sales |
| 20 | HR |
| 30 | Legal |

| EMP.emp_id | EMP.dept_id |
|---|---|
| 1 | 10 |
| 2 | 10 |
| 3 | 20 |
| 4 | NULL |

What value of `n` is returned for `'Legal'`?

(a) 0
(b) NULL
(c) 1
(d) The row for Legal is not returned at all.

---

**11. (a) 0**

`COUNT(e.emp_id)` counts non-NULL values of the right table's column. Legal has no employees, so the LEFT JOIN produces a NULL-extended row and the count is 0.

| dept_name | Joined emp_id | COUNT(e.emp_id) |
|---|---|---|
| HR | 3 | 1 |
| Legal | NULL | 0 |
| Sales | 1, 2 | 2 |

- (c) That is Sales, not Legal.
- (b) NULL would be the result of `SUM(e.emp_id)` on an empty group, not of COUNT.
- (d) The LEFT JOIN guarantees every DEPT row appears.

---

**12.** **[Medium]** *(D6 — join fan-out from duplicate keys)*

```sql
SELECT COUNT(*) FROM T1 JOIN T2 ON T1.A = T2.B;
```

| T1.A |
|---|
| 1 |
| 2 |
| 3 |

| T2.B | T2.X |
|---|---|
| 1 | p |
| 1 | q |
| 2 | r |

What does the query return?

(a) 2
(b) 4
(c) 3
(d) 6

---

**12. (c) 3**

A is joined to B on `A = B`. Value 1 matches two B rows (fan-out), value 2 matches one, and value 3 matches none.

| T1.A | Matching T2 rows | Output rows |
|---|---|---|
| 1 | (1,'p'), (1,'q') | 2 |
| 2 | (2,'r') | 1 |
| 3 | none | 0 |
| **Total** | | **3** |

- (a) Counts the matched A values (1 and 2) instead of the produced rows.
- (b) Adds a row for A = 3, which has no match.
- (d) Multiplies row counts as if this were a cross join.

---

**13.** **[Medium]** *(D6 — GROUP BY on multiple columns)*

```sql
SELECT region, product, SUM(amount) AS total
FROM Sales
GROUP BY region, product;
```

| region | product | amount |
|---|---|---|
| East | P1 | 100 |
| East | P1 | 200 |
| East | P2 | 50 |
| West | P1 | 300 |
| West | P1 | 100 |

How many rows are returned, and what is `total` for the group (West, P1)?

(a) 5 rows; total for (West, P1) = 400
(b) 3 rows; total for (West, P1) = 400
(c) 3 rows; total for (West, P1) = 300
(d) 4 rows; total for (West, P1) = 400

---

**13. (b) 3 rows; total for (West, P1) = 400**

One group per distinct (region, product) pair.

| Group | Rows | SUM(amount) |
|---|---|---|
| East, P1 | 100, 200 | 300 |
| East, P2 | 50 | 50 |
| West, P1 | 300, 100 | 400 |

- (a) 5 rows is the ungrouped row count.
- (c) Uses only the first West/P1 amount (300) and ignores 100.
- (d) Splits the (East, P1) group into two rows.

---

**14.** **[Medium]** *(D6 — NULL in comparisons)*

```sql
SELECT COUNT(*) FROM T WHERE x <> 5;
```

| T.x |
|---|
| 1 |
| 2 |
| NULL |

What does the query return?

(a) 0
(b) 2
(c) 1
(d) 3

---

**14. (b) 2**

`NULL <> 5` evaluates to UNKNOWN, not TRUE, so the NULL row is not returned by WHERE.

| T.x | x <> 5 | Returned? |
|---|---|---|
| 1 | TRUE | Yes |
| 2 | TRUE | Yes |
| NULL | UNKNOWN | No |
| **Total** | | **2** |

- (a) Assumes every row fails, which would happen only if all rows were NULL.
- (c) Counts only one of the two numeric rows.
- (d) Counts the NULL row as if UNKNOWN were TRUE.

---

**15.** **[Medium]** *(D6 — normal forms)*

```
OrderLine(order_id, product_id, product_name, qty)
Primary key: (order_id, product_id)
Dependency: product_id -> product_name
```

`product_name` depends on `product_id` alone, which is only part of the composite primary key. This is a partial dependency. Removing this partial dependency brings the table to which normal form?

(a) 2NF
(b) BCNF
(c) 1NF
(d) 3NF

---

**15. (a) 2NF**

A relation is in 2NF when every non-key attribute depends on the whole primary key. Storing `product_name` keyed by only part of the composite key is a partial dependency, and removing it achieves 2NF.

- (c) 1NF concerns only atomic column values, which is a different issue that this table does not raise.
- (b) BCNF is a stricter form than 3NF and is not reached by removing only a partial dependency.
- (d) 3NF additionally requires that no non-key attribute is transitively dependent on the key; that is a later step.

---

**16.** **[Hard]** *(D6 — LEFT JOIN converted to inner join by WHERE)*

```sql
SELECT d.dept_name, e.emp_id
FROM DEPT d LEFT JOIN EMP e ON d.dept_id = e.dept_id
WHERE e.salary > 50000;
```

| DEPT.dept_id | DEPT.dept_name |
|---|---|
| 10 | Sales |
| 20 | HR |
| 30 | Legal |
| 40 | Marketing |

| EMP.emp_id | EMP.dept_id | EMP.salary |
|---|---|---|
| 1 | 10 | 60000 |
| 2 | 10 | 40000 |
| 3 | 20 | 90000 |
| 4 | 30 | 30000 |

How many rows does the query return?

(a) 3 rows
(b) 0 rows
(c) 1 row
(d) 2 rows

---

**16. (d) 2 rows**

The LEFT JOIN produces five rows, including a NULL-extended row for Marketing. The WHERE predicate on `e.salary` makes that row UNKNOWN, so it is discarded and the query behaves like an inner join.

| dept_name | emp_id | salary | salary > 50000? |
|---|---|---|---|
| Sales | 1 | 60000 | TRUE |
| Sales | 2 | 40000 | FALSE |
| HR | 3 | 90000 | TRUE |
| Legal | 4 | 30000 | FALSE |
| Marketing | NULL | NULL | UNKNOWN |
| **Kept** | | | **2** |

- (a) Counts the Sales/1, Sales/2 and HR/3 matches without applying the WHERE predicate.
- (c) Keeps only one of the two rows above the salary threshold.
- (b) Assumes the predicate removes every row, which would happen only if no employee earned above 50000.

---

**17.** **[Hard]** *(D6 — GROUP BY and NULL groups)*

```sql
SELECT dept_id, COUNT(*) AS n FROM Emp GROUP BY dept_id;
```

| Emp.emp_id | Emp.dept_id |
|---|---|
| 1 | 10 |
| 2 | 10 |
| 3 | 20 |
| 4 | NULL |
| 5 | 20 |

Which statement describes the result?

(a) 3 rows; the row with dept_id = NULL has n = 2
(b) 2 rows; the rows with NULL dept_id are dropped from the result
(c) 3 rows; one row has dept_id = NULL and n = 1
(d) 5 rows; one row per employee

---

**17. (c) 3 rows; one row has dept_id = NULL and n = 1**

GROUP BY treats all NULLs in the grouping column as one group, but the group key itself is displayed as NULL.

| Group key | Rows | COUNT(*) |
|---|---|---|
| 10 | emp 1, 2 | 2 |
| 20 | emp 3, 5 | 2 |
| NULL | emp 4 | 1 |

- (b) Misapplies the rule that `WHERE dept_id IS NOT NULL` would exclude them; GROUP BY still forms the NULL group.
- (a) Assigns both of the dept 20 rows to the NULL group.
- (d) Confuses GROUP BY with a plain SELECT, which would indeed return 5 rows.

---

**18.** **[Hard]** *(D6 — NOT IN with a NULL in the subquery)*

```sql
SELECT COUNT(*) FROM A WHERE x NOT IN (SELECT y FROM B);
```

| A.x |
|---|
| 1 |
| 2 |
| 3 |

| B.y |
|---|
| 1 |
| NULL |

What does the query return?

(a) 1
(b) 0
(c) 2
(d) 3

---

**18. (b) 0**

The subquery returns the set {1, NULL}. `x NOT IN (1, NULL)` expands to `x <> 1 AND x <> NULL`. The second term is UNKNOWN for every row, so the whole condition is never TRUE.

| A.x | x <> 1 | x <> NULL | AND | Returned? |
|---|---|---|---|---|
| 1 | FALSE | UNKNOWN | FALSE | No |
| 2 | TRUE | UNKNOWN | UNKNOWN | No |
| 3 | TRUE | UNKNOWN | UNKNOWN | No |
| **Total** | | | | **0** |

- (a) Counts x = 2 only, ignoring the UNKNOWN propagated by the NULL.
- (c) Counts x = 2 and x = 3, treating `x <> NULL` as TRUE.
- (d) Treats the condition as a plain not-equal test over all three rows.

---

**19.** **[Easy]** *(D6 — Aggregates and NULLs)*

```sql
Emp
EmpID | Dept | Bonus
1     | 'A'  | 100
2     | 'A'  | NULL
3     | 'B'  | 200
4     | 'B'  | NULL
5     | NULL | NULL
```

```sql
SELECT COUNT(*), COUNT(Bonus), COUNT(DISTINCT Dept) FROM Emp;
```

The three values returned are:

(a) 5, 3, 3
(b) 5, 2, 2
(c) 4, 2, 2
(d) 5, 2, 3

---

**19. (b) 5, 2, 2**
`COUNT(*)` counts rows regardless of NULLs (5); `COUNT(Bonus)` skips NULLs (100 and 200 only); `COUNT(DISTINCT Dept)` counts distinct non-NULL values ('A', 'B').
- (a) Assumes `COUNT(Bonus)` and `COUNT(DISTINCT Dept)` both count NULLs as a value — aggregate functions ignore NULL except `COUNT(*)`.
- (c) Drops one row from `COUNT(*)` by wrongly treating the NULL `Dept` row as absent from the table.
- (d) Counts NULL as a distinct value of `Dept`.

---

**20.** **[Easy]** *(D6 — Key types)*

Which statement about keys is correct?

(a) A PRIMARY KEY column may contain NULL values as long as the non-NULL values are unique.
(b) A FOREIGN KEY value must always match an existing value in the referenced table.
(c) A super key is any set of attributes that uniquely identifies a tuple; a candidate key is a minimal super key.
(d) A table can have at most one candidate key.

---

**20. (c) A super key is any set of attributes that uniquely identifies a tuple; a candidate key is a minimal super key.**
This is the standard definition: candidate keys are exactly the minimal super keys, and one of them is chosen as the primary key.
- (a) A PRIMARY KEY implies NOT NULL; NULLs are never permitted in it.
- (b) A FOREIGN KEY may be NULL, and may only reference a UNIQUE or PRIMARY KEY column; "must always match" is too strong.
- (d) A table can have several candidate keys; only the chosen one becomes the primary key.

---

**21.** **[Medium]** *(D6 — Inner join result)*

```sql
Students                          Depts
SID | Name   | DeptID             DeptID | DName
1   | 'Amit' | 10                 10     | 'CSE'
2   | 'Bina' | 20                 20     | 'ECE'
3   | 'Chand'| 10                 30     | 'MECH'
4   | 'Dev'  | 20
```

```sql
SELECT s.Name, d.DName
FROM Students s INNER JOIN Depts d ON s.DeptID = d.DeptID
ORDER BY s.Name;
```

The result is:

(a) 4 rows: `Amit|CSE`, `Bina|ECE`, `Chand|CSE`, `Dev|ECE`
(b) 5 rows, including `Dev | MECH`
(c) 3 rows: `Amit|CSE`, `Bina|ECE`, `Chand|CSE`
(d) 4 rows: `Amit|CSE`, `Bina|ECE`, `Chand|CSE`, `Dev|NULL`

---

**21. (a) 4 rows: `Amit|CSE`, `Bina|ECE`, `Chand|CSE`, `Dev|ECE`**
An inner join keeps only rows where `Students.DeptID = Depts.DeptID`; all four students have a matching department, giving 4 rows.
- (b) `MECH` (DeptID 30) has no matching student, so it cannot appear in the result.
- (c) `Dev` has DeptID 20, which does match `ECE`; dropping that row is wrong.
- (d) `Dev` matches `ECE`; an inner join never produces a NULL on the right side.

---

**22.** **[Medium]** *(D6 — Outer joins and COUNT)*

```sql
Orders                            Customers
OrderID | CustID | Amount         CustID | City
101     | 1      | 500            1      | 'Pune'
102     | 2      | 300            2      | 'Delhi'
103     | 1      | 700            3      | 'Kochi'
104     | 4      | 200
```

```sql
SELECT COUNT(*), COUNT(c.City)
FROM Orders o LEFT JOIN Customers c ON o.CustID = c.CustID;
```

The two values returned are:

(a) 3 and 3
(b) 4 and 3
(c) 7 and 3
(d) 4 and 4

---

**22. (b) 4 and 3**
A LEFT JOIN keeps all 4 order rows (OrderID 104 has no matching customer). `COUNT(*)` counts rows, so 4; `COUNT(c.City)` ignores the NULL produced for the unmatched row, so 3.
- (a) `COUNT(*)` is wrongly treated as the count of matched rows only, discarding the unmatched left row.
- (d) `COUNT(c.City)` is assumed to count NULLs as values.
- (c) 7 is the row count of a full outer join (matched rows + unmatched right row), not of a left join.

---

**23.** **[Easy]** *(D6 — WHERE vs HAVING)*

Which statement about `WHERE` and `HAVING` is correct?

(a) `WHERE` filters individual rows before grouping; `HAVING` filters groups after aggregation.
(b) `WHERE` and `HAVING` are fully interchangeable; using either one always produces the same result.
(c) `HAVING` may only be used together with `GROUP BY`, and it must always reference an aggregate function.
(d) `WHERE` filters groups after aggregation; `HAVING` filters individual rows before grouping.

---

**23. (a) `WHERE` filters individual rows before grouping; `HAVING` filters groups after aggregation.**
`WHERE` runs before `GROUP BY` and cannot contain aggregates; `HAVING` runs after grouping and is where aggregate conditions belong.
- (d) Reverses the two clauses.
- (b) They apply at different stages; an aggregate condition in `WHERE` is a syntax error.
- (c) Standard SQL permits `HAVING` without `GROUP BY` (the whole table is one group), and `HAVING` may reference grouping columns rather than aggregates.

---

**24.** **[Medium]** *(D6 — Logical execution order)*

Which sequence correctly describes the logical order in which a SQL query is processed?

(a) `FROM` → `WHERE` → `GROUP BY` → `SELECT` → `HAVING` → `ORDER BY`
(b) `SELECT` → `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `ORDER BY`
(c) `FROM` → `GROUP BY` → `WHERE` → `HAVING` → `SELECT` → `ORDER BY`
(d) `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`

---

**24. (d) `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`**
Rows are produced by `FROM`, filtered by `WHERE`, grouped, filtered again by `HAVING`, then projected by `SELECT` and finally sorted.
- (b) Puts `SELECT` first; column aliases defined in `SELECT` are not available to `WHERE`.
- (c) Applies `GROUP BY` before `WHERE`, which would aggregate rows that should have been discarded first.
- (a) Applies `SELECT` before `HAVING`, which would evaluate `HAVING` against ungrouped projections.

---

**25.** **[Medium]** *(D6 — GROUP BY with HAVING)*

```sql
Sales
Region  | Product | Qty
'East'  | 'X'     | 10
'East'  | 'Y'     | 20
'West'  | 'X'     | 5
'West'  | 'X'     | 15
'North' | 'Y'     | 7
```

```sql
SELECT Region, COUNT(*)
FROM Sales
GROUP BY Region
HAVING COUNT(*) > 1;
```

The result is:

(a) 3 rows: `East|2`, `West|2`, `North|1`
(b) 2 rows: `East|2`, `West|2`
(c) 1 row: `West|2`
(d) 2 rows: `East|2`, `North|1`

---

**25. (b) 2 rows: `East|2`, `West|2`**
`East` and `West` each have 2 rows and pass `COUNT(*) > 1`; `North` has only 1 row and is removed by `HAVING`.
- (a) Shows the pre-`HAVING` result; the `North` group must be filtered out.
- (c) `East` has 2 rows too, so it also survives the filter.
- (d) `North` has 1 row, so it cannot appear in the output.

---

**26.** **[Easy]** *(D6 — ACID properties)*

Which ACID property guarantees that once a transaction has committed, its changes survive a subsequent system crash?

(a) Atomicity
(b) Durability
(c) Consistency
(d) Isolation

---

**26. (b) Durability**
Durability is the guarantee that committed changes are persisted (typically via the write-ahead log) and survive crashes.
- (a) Atomicity covers all-or-nothing execution of a transaction, not persistence after commit.
- (c) Consistency covers moving the database from one valid state to another, respecting constraints.
- (d) Isolation covers the non-interference of concurrent transactions.

---

**27.** **[Medium]** *(D6 — Index usage)*

Table `Users` has a B-tree index on the column `email`. Which query is LEAST likely to be able to use that index?

(a) `SELECT * FROM Users WHERE LOWER(email) = 'a@b.com';`
(b) `SELECT * FROM Users WHERE email LIKE 'abc%';`
(c) `SELECT * FROM Users WHERE email = 'a@b.com';`
(d) `SELECT * FROM Users WHERE email BETWEEN 'a' AND 'b';`

---

**27. (a) `SELECT * FROM Users WHERE LOWER(email) = 'a@b.com';`**
Wrapping the indexed column in a function (`LOWER(email)`) makes the predicate non-sargable, so a plain index on `email` cannot be used (a function-based index would be required).
- (c) An equality predicate on the indexed column is the ideal index lookup.
- (b) A prefix pattern `LIKE 'abc%'` can be answered by an index range scan.
- (d) `BETWEEN` is a range predicate, which a B-tree index handles directly.

---

**28.** **[Hard]** *(D6 — Normal forms)*

Relation `R(A, B, C, D)` has the functional dependencies:

```
AB → C
AB → D
C  → A
D  → B
```

The highest normal form satisfied by `R` is:

(a) 3NF but not BCNF
(b) 1NF only
(c) 2NF but not 3NF
(d) BCNF

---

**28. (a) 3NF but not BCNF**
Key closures: `AB⁺ = ABCD`, `BC⁺ = ABCD` (C→A), `AD⁺ = ABCD` (D→B), `CD⁺ = ABCD`. All four attributes are prime, so no partial or transitive dependency on a non-prime attribute exists → 3NF holds. But `C → A` has a determinant `C` that is not a superkey (`C⁺ = {C, A}`), so BCNF fails.
- (b) 1NF is trivially satisfied and is far weaker than what `R` achieves.
- (c) A 2NF violation requires a non-prime attribute dependent on part of a key; every attribute here is prime.
- (d) BCNF requires every determinant to be a superkey, which `C → A` violates.

---

**29.** **[Medium]** *(D6 — Self join)*

```sql
Emp
EmpID | Name     | MgrID
1     | 'Anil'   | NULL
2     | 'Bela'   | 1
3     | 'Chetan' | 1
4     | 'Divya'  | 2
```

```sql
SELECT e.Name AS Emp, m.Name AS Mgr
FROM Emp e JOIN Emp m ON e.MgrID = m.EmpID;
```

The result is:

(a) 4 rows: `Anil|NULL`, `Bela|Anil`, `Chetan|Anil`, `Divya|Bela`
(b) 6 rows
(c) 3 rows: `Bela|Anil`, `Chetan|Anil`, `Divya|Chetan`
(d) 3 rows: `Bela|Anil`, `Chetan|Anil`, `Divya|Bela`

---

**29. (d) 3 rows: `Bela|Anil`, `Chetan|Anil`, `Divya|Bela`**
The join matches `MgrID` to `EmpID`: Bela→Anil, Chetan→Anil, Divya→Bela. Anil's `MgrID` is NULL, so no row is produced for him.
- (a) An inner join cannot output `Anil|NULL`; the NULL `MgrID` fails the equality test.
- (b) 6 rows would require a cross join (4×4 = 16) or a full outer join, not an inner join.
- (c) Divya's `MgrID` is 2 (Bela), not 3 (Chetan).

---

**30.** **[Medium]** *(D6 — NULL in predicates)*

```sql
T
x
1
2
NULL
```

```sql
SELECT COUNT(*) FROM T WHERE x <> 2;
```

The value returned is:

(a) 1
(b) 0
(c) 2
(d) 3

---

**30. (a) 1**
`x <> 2` is TRUE only for `x = 1`. The comparison with NULL yields UNKNOWN, and `WHERE` keeps only rows where the condition is TRUE, so the NULL row is excluded.
- (d) Counts all rows in the table, ignoring the filter entirely.
- (b) Assumes NULL is treated as equal to 2, or that the comparison removes every row.
- (c) Rightly drops the NULL row but also keeps `x = 2`, which fails `x <> 2`.

---

**31.** **[Easy]** *(D6 — Primary key constraints)*

Which statement about a `PRIMARY KEY` constraint is correct?

(a) When it is declared on multiple columns, each individual column must also be unique on its own.
(b) It permits a single NULL value in the key column, provided all other values are distinct.
(c) It enforces uniqueness across the key columns and does not permit NULL values.
(d) A table may declare more than one `PRIMARY KEY` constraint as long as the column sets differ.

---

**31. (c) It enforces uniqueness across the key columns and does not permit NULL values.**
A PRIMARY KEY is a UNIQUE + NOT NULL constraint, enforced over the whole key (composite or not).
- (b) Not even one NULL is allowed in a PRIMARY KEY column.
- (a) A composite primary key requires only the *combination* to be unique; individual columns may repeat.
- (d) Only one PRIMARY KEY constraint is permitted per table.

---

**32.** **[Medium]** *(D6 — Joins with DISTINCT aggregates)*

```sql
Students                          Enroll
StudentID | Name                  StudentID | CourseID
1         | 'A'                   1         | 10
2         | 'B'                   1         | 20
3         | 'C'                   2         | 10
4         | 'D'                   3         | 30
```

```sql
SELECT COUNT(DISTINCT e.StudentID)
FROM Students s JOIN Enroll e ON s.StudentID = e.StudentID;
```

The value returned is:

(a) 4
(b) 1
(c) 3
(d) 2

---

**32. (c) 3**
The join produces 4 rows (student 1 twice), but `DISTINCT` collapses them to StudentIDs 1, 2 and 3.
- (a) 4 is the raw join row count before `DISTINCT` is applied.
- (b) 1 is only the number of students with more than one enrollment (student 1).
- (d) 2 is the number of students with exactly one enrollment (students 2 and 3), not the distinct count.

---

**33.** **[Hard]** *(D6 — Cross join row counting)*

```sql
A                     B
id                    id
1                     1
2                     2
3                     3
                      4
```

```sql
SELECT COUNT(*) FROM A CROSS JOIN B WHERE A.id <> B.id;
```

The value returned is:

(a) 12
(b) 7
(c) 8
(d) 9

---

**33. (d) 9**
The cross join produces 3 × 4 = 12 pairs; the predicate removes the 3 pairs where the ids are equal.

| A.id | matching B.id values (≠) | pairs |
|------|--------------------------|-------|
| 1 | 2, 3, 4 | 3 |
| 2 | 1, 3, 4 | 3 |
| 3 | 1, 2, 4 | 3 |
| **Total** | | **9** |

- (a) 12 is the unfiltered cross-join size, before the `WHERE` clause applies.
- (c) 8 drops one pair too many, typically by mishandling the id 4 row that appears only in `B`.
- (b) 7 undercounts; every one of the 12 pairs has a well-defined comparison result.

---

**34.** **[Medium]** *(D6 — Aggregates with WHERE and HAVING)*

```sql
Emp2
Dept | Salary
'IT' | 1000
'IT' | 2000
'HR' | 1500
'HR' | NULL
'HR' | 2500
```

```sql
SELECT Dept, AVG(Salary)
FROM Emp2
WHERE Salary IS NOT NULL
GROUP BY Dept
HAVING AVG(Salary) > 1500;
```

The result is:

(a) 0 rows
(b) 1 row: `HR | 1666.67`
(c) 2 rows: `IT | 1500` and `HR | 2000`
(d) 1 row: `HR | 2000`

---

**34. (d) 1 row: `HR | 2000`**
`WHERE Salary IS NOT NULL` leaves `IT: 1000, 2000` and `HR: 1500, 2500`. Group averages are 1500 (IT) and 2000 (HR); `HAVING AVG(Salary) > 1500` keeps only HR.
- (a) HR's average (2000) does exceed 1500, so at least one row survives.
- (c) IT's average is exactly 1500, which fails the strict `>` comparison.
- (b) 1666.67 would be the HR average if the NULL were counted as 0 ((1500+0+2500)/3); `WHERE` has already removed that row.

---

**35.** **[Easy]** *(D6 — Clustered vs non-clustered indexes)*

Which statement about clustered and non-clustered indexes is correct?

(a) A table can have several clustered indexes but only one non-clustered index.
(b) A clustered index determines the physical order of the table's rows, and a table can have at most one.
(c) A non-clustered index stores the complete table row at its leaf level, so no table lookup is ever needed.
(d) A non-clustered index can only serve equality predicates, never range predicates.

---

**35. (b) A clustered index determines the physical order of the table's rows, and a table can have at most one.**
Because the table's own storage order can only be one thing, only one clustered index is possible; non-clustered indexes are separate structures holding key values plus row locators.
- (a) Reverses the rule: at most one clustered index, many non-clustered ones.
- (c) A non-clustered index stores indexed column values plus a row locator (or included columns), not the whole row for every column — a lookup is usually still needed.
- (d) Non-clustered indexes are ordered structures and serve range predicates as well as equality.

---

**36.** **[Hard]** *(D6 — AVG and NULL handling)*

```sql
Scores
Student | Marks
'A'     | 80
'B'     | NULL
'C'     | 90
'D'     | NULL
```

```sql
SELECT COUNT(*), COUNT(Marks), AVG(Marks) FROM Scores;
```

The three values returned are:

(a) 4, 2, 85
(b) 4, 4, 42.5
(c) 4, 2, 42.5
(d) 2, 2, 85

---

---

**36. (a) 4, 2, 85**
`COUNT(*)` counts all 4 rows; `COUNT(Marks)` counts the 2 non-NULL marks; `AVG(Marks)` ignores NULLs and computes (80 + 90) / 2 = 85.
- (b) Treats NULLs as counted values and divides the sum by 4 as if NULL contributed 0.
- (c) Divides the sum of 170 by 4, producing 42.5 — the classic "NULL as zero" error.
- (d) Uses `COUNT(Marks)` semantics (2) for `COUNT(*)`, which counts rows, not non-NULL values.

---
