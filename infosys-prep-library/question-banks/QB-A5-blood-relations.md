# QB-A5 — Blood relations

**Reasoning Ability** · **Tier 2** · 20 questions · topic file: see the `A5` file in `topics/`, `puzzles/`, `pseudocode/` or `interview/`

Generated for this library from the rule families seen in the Infosys pool (`../data/gen_*.py`). Every key was recomputed by a second route; see `../research/04-qa-report.md`.

**How to use this bank.** Attempt every question before opening the key. Answer letters are balanced across a–d and not in a repeating pattern, so guessing the pattern will not help.

---

## Practice questions

**1.** **[Relation chain]** R is the daughter of U. U is the sister of Q. Q is the daughter of P. How is R related to P?
a) granddaughter
b) mother-in-law
c) wife
d) sister-in-law

**2.** **[Relation chain]** P is the mother of R. R is the wife of W. How is P related to W?
a) daughter
b) wife
c) mother-in-law
d) mother

**3.** **[Relation chain]** T is the daughter of W. W is the son of S. How is T related to S?
a) niece
b) aunt
c) granddaughter
d) wife

**4.** **[Relation chain]** P is the wife of Q. Q is the father of S. How is P related to S?
a) aunt
b) grandmother
c) niece
d) mother

**5.** **[Relation chain]** W is the wife of T. T is the father of S. How is W related to S?
a) mother
b) wife
c) sister
d) aunt

**6.** **[Relation chain]** V is the brother of S. S is the daughter of U. How is V related to U?
a) son
b) uncle
c) son-in-law
d) brother-in-law

**7.** **[Relation chain]** T is the brother of R. R is the brother of Q. Q is the mother of U. How is T related to U?
a) son
b) nephew
c) grandfather
d) uncle

**8.** **[Relation chain]** R is the wife of T. T is the son of S. How is R related to S?
a) aunt
b) daughter-in-law
c) grandmother
d) granddaughter

**9.** **[Relation chain]** W is the brother of T. T is the daughter of P. How is W related to P?
a) uncle
b) son
c) husband
d) grandfather

**10.** **[Relation chain]** P is the father of Q. Q is the brother of U. How is P related to U?
a) brother
b) nephew
c) father
d) father-in-law

**11.** **[Relation chain]** R is the husband of W. W is the sister of P. How is R related to P?
a) brother-in-law
b) brother
c) father
d) cousin

**12.** **[Relation chain]** W is the wife of T. T is the brother of S. How is W related to S?
a) niece
b) mother
c) sister-in-law
d) granddaughter

**13.** **[Relation chain]** V is the son of T. T is the brother of Q. How is V related to Q?
a) brother-in-law
b) nephew
c) uncle
d) father-in-law

**14.** **[Relation chain]** P is the wife of W. W is the son of U. How is P related to U?
a) granddaughter
b) mother
c) wife
d) daughter-in-law

**15.** **[Relation chain]** Q is the husband of W. W is the sister of T. How is Q related to T?
a) uncle
b) grandfather
c) brother-in-law
d) son-in-law

**16.** **[Relation chain]** U is the son of R. R is the mother of W. W is the husband of P. How is U related to P?
a) father
b) son
c) grandson
d) brother-in-law

**17.** **[Relation chain]** U is the brother of P. P is the son of T. How is U related to T?
a) son
b) cousin
c) grandfather
d) nephew

**18.** **[Relation chain]** V is the son of T. T is the son of S. How is V related to S?
a) brother
b) son-in-law
c) husband
d) grandson

**19.** **[Relation chain]** V is the brother of S. S is the son of R. How is V related to R?
a) uncle
b) son
c) brother
d) grandfather

**20.** **[Relation chain]** W is the sister of Q. Q is the sister of U. U is the son of T. How is W related to T?
a) niece
b) daughter
c) daughter-in-law
d) mother-in-law

### ANSWER KEY

1. **a** — Walk from P back to R, one statement at a time: P’s daughter is Q → Q’s sister is U → U’s daughter is R. Combined, that is granddaughter (the path reduces to ‘down then down’, and R is female).
2. **c** — Walk from W back to P, one statement at a time: W’s wife is R → R’s mother is P. Combined, that is mother-in-law (the path reduces to ‘spouse then up’, and P is female).
3. **c** — Walk from S back to T, one statement at a time: S’s son is W → W’s daughter is T. Combined, that is granddaughter (the path reduces to ‘down then down’, and T is female).
4. **d** — Walk from S back to P, one statement at a time: S’s father is Q → Q’s wife is P. Combined, that is mother (the path reduces to ‘up’, and P is female).
5. **a** — Walk from S back to W, one statement at a time: S’s father is T → T’s wife is W. Combined, that is mother (the path reduces to ‘up’, and W is female).
6. **a** — Walk from U back to V, one statement at a time: U’s daughter is S → S’s brother is V. Combined, that is son (the path reduces to ‘down’, and V is male).
7. **d** — Walk from U back to T, one statement at a time: U’s mother is Q → Q’s brother is R → R’s brother is T. Combined, that is uncle (the path reduces to ‘up then side’, and T is male).
8. **b** — Walk from S back to R, one statement at a time: S’s son is T → T’s wife is R. Combined, that is daughter-in-law (the path reduces to ‘down then spouse’, and R is female).
9. **b** — Walk from P back to W, one statement at a time: P’s daughter is T → T’s brother is W. Combined, that is son (the path reduces to ‘down’, and W is male).
10. **c** — Walk from U back to P, one statement at a time: U’s brother is Q → Q’s father is P. Combined, that is father (the path reduces to ‘up’, and P is male).
11. **a** — Walk from P back to R, one statement at a time: P’s sister is W → W’s husband is R. Combined, that is brother-in-law (the path reduces to ‘side then spouse’, and R is male).
12. **c** — Walk from S back to W, one statement at a time: S’s brother is T → T’s wife is W. Combined, that is sister-in-law (the path reduces to ‘side then spouse’, and W is female).
13. **b** — Walk from Q back to V, one statement at a time: Q’s brother is T → T’s son is V. Combined, that is nephew (the path reduces to ‘side then down’, and V is male).
14. **d** — Walk from U back to P, one statement at a time: U’s son is W → W’s wife is P. Combined, that is daughter-in-law (the path reduces to ‘down then spouse’, and P is female).
15. **c** — Walk from T back to Q, one statement at a time: T’s sister is W → W’s husband is Q. Combined, that is brother-in-law (the path reduces to ‘side then spouse’, and Q is male).
16. **d** — Walk from P back to U, one statement at a time: P’s husband is W → W’s mother is R → R’s son is U. Combined, that is brother-in-law (the path reduces to ‘spouse then side’, and U is male).
17. **a** — Walk from T back to U, one statement at a time: T’s son is P → P’s brother is U. Combined, that is son (the path reduces to ‘down’, and U is male).
18. **d** — Walk from S back to V, one statement at a time: S’s son is T → T’s son is V. Combined, that is grandson (the path reduces to ‘down then down’, and V is male).
19. **b** — Walk from R back to V, one statement at a time: R’s son is S → S’s brother is V. Combined, that is son (the path reduces to ‘down’, and V is male).
20. **b** — Walk from T back to W, one statement at a time: T’s son is U → U’s sister is Q → Q’s sister is W. Combined, that is daughter (the path reduces to ‘down’, and W is female).
