"""P9: object-oriented tracing questions. Every key is the real output of the Java snippet, produced by
javac/java at build time. The distractors are hand-chosen wrong traces (see the `wrong` lists)."""
import pathlib, subprocess, tempfile
from gen_core import Q

# (code shown to the learner, main-body statements, wrong outputs, why)
SNIPPETS = [
    ("class A { void show() { System.out.print(\"A\"); } }\nclass B extends A { void show() { System.out.print(\"B\"); } }",
     "A obj = new B(); obj.show();", ["A", "AB", "BA"],
     "The real class is B and `show` is an instance method, so B's version runs."),
    ("class A { void show() { System.out.print(\"A\"); } }\nclass B extends A { void show() { super.show(); System.out.print(\"B\"); } }",
     "A obj = new B(); obj.show();", ["B", "BA", "A"],
     "B's `show` runs; its first statement `super.show()` prints A, then it prints B."),
    ("class A { A() { System.out.print(\"A\"); } }\nclass B extends A { B() { System.out.print(\"B\"); } }",
     "new B();", ["B", "BA", "AA"],
     "A constructor starts by calling the parent constructor, so A prints first."),
    ("class A { int x = 10; }\nclass B extends A { int x = 20; }",
     "A a = new B(); System.out.print(a.x);", ["20", "30", "0"],
     "Fields are not overridden: the reference type A decides, so `a.x` is A's 10."),
    ("class A { int x = 10; }\nclass B extends A { int x = 20; }",
     "A a = new B(); System.out.print(((B) a).x);", ["10", "30", "20 10"],
     "The cast makes the compiler read B's field: 20."),
    ("class A { static void hi() { System.out.print(\"A\"); } }\nclass B extends A { static void hi() { System.out.print(\"B\"); } }",
     "A a = new B(); a.hi();", ["B", "AB", "BA"],
     "Static methods are bound at compile time by the reference type A, so A's `hi` runs."),
    ("class T { void f(int x) { System.out.print(\"int \"); }\n        void f(double x) { System.out.print(\"double \"); } }",
     "T t = new T(); t.f(5); t.f(5.0);", ["double double ", "int int ", "double int "],
     "`5` is an int literal and `5.0` a double literal; the overload matching each exactly runs."),
    ("class Animal { void sound() { System.out.print(\"... \"); } }\nclass Dog extends Animal { void sound() { System.out.print(\"Woof \"); } }\nclass Cat extends Animal { void sound() { System.out.print(\"Meow \"); } }",
     "Animal[] z = { new Dog(), new Cat(), new Animal() };\nfor (Animal a : z) a.sound();", ["... ... ... ", "Woof Woof Woof ", "Woof Meow Meow "],
     "Each object answers with its own class's `sound`: Dog, Cat, then the base Animal."),
    ("class C { static int n = 0; C() { n++; } }",
     "new C(); new C(); new C(); System.out.print(C.n);", ["0", "1", "2"],
     "`n` is shared by all objects and the constructor adds 1 each time: 3."),
    ("class A { A(int v) { System.out.print(v + \" \"); } }\nclass B extends A { B(int v) { super(v * 2); System.out.print(v); } }",
     "new B(4);", ["4 8", "8", "4"],
     "`super(v * 2)` runs first and prints 8 and a space; then B prints 4."),
    ("class A { private void p() { System.out.print(\"A.p \"); }\n          void call() { p(); } }\nclass B extends A { void p() { System.out.print(\"B.p \"); } }",
     "new B().call();", ["B.p ", "A.p B.p ", "B.p A.p "],
     "A private method is not overridden. `call` belongs to A and invokes A's own `p`."),
    ("class A { void hello() { System.out.print(\"A\"); } }\nclass B extends A { void hello() { System.out.print(\"B\"); } void only() { System.out.print(\"only\"); } }",
     "A a = new B(); a.hello(); ((B) a).only();", ["Aonly", "BA", "B only"],
     "`hello` dispatches to B, and the cast allows calling B's own `only`: B then only."),
]


def java_outputs():
    d = pathlib.Path(tempfile.mkdtemp())
    mains = []
    src_parts = []
    for n, (code, body, _, _) in enumerate(SNIPPETS):
        # rename classes per snippet to avoid clashes: wrap each snippet in its own file
        name = f"S{n}"
        src = code + f"\nclass {name} {{ public static void main(String[] args) {{\n{body}\n}} }}\n"
        (d / f"{name}.java").write_text(src)
        mains.append(name)
    outs = []
    for name in mains:
        r = subprocess.run(['javac', f'{name}.java'], cwd=d, capture_output=True, text=True)
        assert r.returncode == 0, (name, r.stderr[:600])
        r = subprocess.run(['java', '-cp', str(d), name], capture_output=True, text=True)
        assert r.returncode == 0, (name, r.stderr[:300])
        outs.append(r.stdout)
    return outs


def oop_questions():
    outs = java_outputs()
    qs = []
    for (code, body, wrong, why), out in zip(SNIPPETS, outs):
        if out in wrong:
            raise AssertionError(f"a distractor equals the real output: {out!r}")
        shown = out.strip() if out.strip() else out
        opts = [out] + wrong
        qtxt = f"What is the output?\n\n```java\n{code}\n\n// main:\n{body}\n```\n"
        assert len({fmt_out(o) for o in opts}) == 4, (opts,)
        qs.append(Q(qtxt, [fmt_out(o) for o in opts], why + f" (Output: `{out.strip()}`, produced by running the code.)", (lambda o=out: fmt_out(o)), 'OOP trace'))
    return qs


def fmt_out(o):
    return o.strip().replace('  ', ' ') or '(nothing)'
