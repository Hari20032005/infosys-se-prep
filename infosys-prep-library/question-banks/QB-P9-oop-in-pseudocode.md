# QB-P9 — OOP tracing

**Pseudocode** · **Tier 4** · 6 questions · topic file: see the `P9` file in `topics/`, `puzzles/`, `pseudocode/` or `interview/`

Every key is the real output of the Java snippet, produced by compiling and running it (`data/gen_oop.py`).

**How to use this bank.** Attempt every question before opening the key. Answer letters are balanced across a–d and not in a repeating pattern, so guessing the pattern will not help.

---

## Practice questions

**1.** **[OOP trace]** What is the output?

```java
class T { void f(int x) { System.out.print("int "); }
        void f(double x) { System.out.print("double "); } }

// main:
T t = new T(); t.f(5); t.f(5.0);
```

a) double double
b) int double
c) double int
d) int int

**2.** **[OOP trace]** What is the output?

```java
class Animal { void sound() { System.out.print("... "); } }
class Dog extends Animal { void sound() { System.out.print("Woof "); } }
class Cat extends Animal { void sound() { System.out.print("Meow "); } }

// main:
Animal[] z = { new Dog(), new Cat(), new Animal() };
for (Animal a : z) a.sound();
```

a) Woof Meow ...
b) Woof Meow Meow
c) ... ... ...
d) Woof Woof Woof

**3.** **[OOP trace]** What is the output?

```java
class C { static int n = 0; C() { n++; } }

// main:
new C(); new C(); new C(); System.out.print(C.n);
```

a) 1
b) 3
c) 2
d) 0

**4.** **[OOP trace]** What is the output?

```java
class A { A(int v) { System.out.print(v + " "); } }
class B extends A { B(int v) { super(v * 2); System.out.print(v); } }

// main:
new B(4);
```

a) 4 8
b) 4
c) 8 4
d) 8

**5.** **[OOP trace]** What is the output?

```java
class A { private void p() { System.out.print("A.p "); }
          void call() { p(); } }
class B extends A { void p() { System.out.print("B.p "); } }

// main:
new B().call();
```

a) A.p B.p
b) B.p A.p
c) B.p
d) A.p

**6.** **[OOP trace]** What is the output?

```java
class A { void hello() { System.out.print("A"); } }
class B extends A { void hello() { System.out.print("B"); } void only() { System.out.print("only"); } }

// main:
A a = new B(); a.hello(); ((B) a).only();
```

a) Bonly
b) Aonly
c) BA
d) B only

### ANSWER KEY

1. **b** — `5` is an int literal and `5.0` a double literal; the overload matching each exactly runs. (Output: `int double`, produced by running the code.)
2. **a** — Each object answers with its own class's `sound`: Dog, Cat, then the base Animal. (Output: `Woof Meow ...`, produced by running the code.)
3. **b** — `n` is shared by all objects and the constructor adds 1 each time: 3. (Output: `3`, produced by running the code.)
4. **c** — `super(v * 2)` runs first and prints 8 and a space; then B prints 4. (Output: `8 4`, produced by running the code.)
5. **d** — A private method is not overridden. `call` belongs to A and invokes A's own `p`. (Output: `A.p`, produced by running the code.)
6. **a** — `hello` dispatches to B, and the cast allows calling B's own `only`: B then only. (Output: `Bonly`, produced by running the code.)
