"""
Session 3 - Topic 3
===================
Free vs Cell Variables & Inner-Function Traps (ASCII-safe)
"""

# 1. Terminology
"""
- Local variable  : defined and used inside the same function.
- Cell variable   : local in outer function captured by inner function.
                    Appears in outer.__code__.co_cellvars
- Free variable   : referenced in a function but defined in an outer scope.
                    Appears in inner.__code__.co_freevars
"""

# 2. Basic Example
def outer():
    x = 10
    def inner():
        return x
    return inner

fn = outer()
print("inner() ->", fn())
print("outer.co_cellvars :", outer.__code__.co_cellvars)
print("inner.co_freevars :", fn.__code__.co_freevars)

print("""\nASCII diagram:
[outer]  x=10  -> cell
   |
   +-- returns inner() which uses x (free var)
""")

# 3. Trap 1 - Late binding in loops
def loop_trap():
    funcs = []
    for i in range(3):
        funcs.append(lambda: i)  # late-binding
    return funcs

wrong = loop_trap()
print("Late-binding trap:", [f() for f in wrong])  # [2, 2, 2]

def loop_fixed():
    funcs = []
    for i in range(3):
        funcs.append(lambda i=i: i)
    return funcs

right = loop_fixed()
print("Fixed closures   :", [f() for f in right])  # [0, 1, 2]

# 4. Trap 2 - UnboundLocalError via accidental rebind
def unsafe():
    x = 5
    def inner():
        # Uncomment next line to see UnboundLocalError
        # print(x)
        nonlocal x
        x += 1
        return x
    return inner

print("UnboundLocalError demo line is commented to keep file runnable.")

# 5. Using 'nonlocal' correctly
def counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc

c = counter()
print("counter:", c(), c(), c())  # 1 2 3
print("Cell content now:", c.__closure__[0].cell_contents)

# 6. Bytecode peek
import dis
print("\nBytecode for inc():")
dis.dis(counter().__code__)

# 7. Nested closure example
def grand():
    g = "grand"
    def parent():
        p = "parent"
        def child():
            return g, p
        return child
    return parent

child_fn = grand()()
print("\nNested closure returns:", child_fn())
print("grand.cellvars :", grand.__code__.co_cellvars)
print("parent.cellvars:", grand().__code__.co_cellvars)
print("child.freevars :", child_fn.__code__.co_freevars)

print("""\nNested diagram:
grand() -> cell[g]
  parent() captures g -> cell[p]
    child() captures g + p as free vars
""")

# End of Topic 3
