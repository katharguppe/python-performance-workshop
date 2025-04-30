"""
Session 3 - Topic 1
===================
Closures and Cell Objects (DEEP Dive with Visuals)  — ASCII‑safe version
"""

# ===================================================
# 1. What is a Closure in Python?
# ===================================================
"""
A closure is a function that:
1. Is defined inside another function (a *nested function*), AND
2. Remembers and has access to variables from the outer function’s scope
   even AFTER the outer function has finished execution.

This is implemented via special internal objects called "cell" objects.

Closures enable lexical scoping and persistent state without globals.
"""

# ===================================================
# 2. Closure Illustration (ASCII)
# ===================================================

"""
Consider:

    def outer():
        x = 10
        def inner():
            return x
        return inner

This creates a closure!

When `inner` is returned, it retains a reference to `x`
inside a "cell object".

ASCII Diagram:
   +--------------------+
   |   outer() scope    |
   |  x = 10 (captured) |
   +--------------------+
            |
            v   (cell reference)
   +-----------------------+
   |   inner() function    |
   |  __closure__ -> cell  |
   +-----------------------+
"""

# ===================================================
# 3. Demonstration Code
# ===================================================

def make_multiplier(factor):
    """Return a closure that multiplies by *factor*."""
    def multiply(n):
        return n * factor  # <- factor is a free variable captured in a cell
    return multiply

times3 = make_multiplier(3)
print("times3(10) =", times3(10))  # Expected: 30

# ===================================================
# 4. Inspecting the Closure Internals
# ===================================================

print("\nInspecting Closure Internals:")
print("Function name:", times3.__name__)
print("__closure__ attribute:", times3.__closure__)
print("Cell contents:", [cell.cell_contents for cell in times3.__closure__])

# ===================================================
# 5. Cell Objects Explained
# ===================================================
"""
Each element of function.__closure__ is a <cell> object.
It contains a reference to a captured variable.
"""

for idx, cell in enumerate(times3.__closure__):
    print(f"Cell {idx}: {cell}  ->  content={cell.cell_contents}  type={type(cell)}")

# ===================================================
# 6. Common Closure Trap
# ===================================================
"""
Trap: Loop variables are late‑bound!

for i in range(3):
    funcs.append(lambda: i)

All captured lambdas will print 2.
Fix by binding a default argument:  lambda i=i: i
"""

def buggy_build_funcs():
    funcs = []
    for i in range(3):
        funcs.append(lambda: i)  # Wrong
    return funcs

def fixed_build_funcs():
    funcs = []
    for i in range(3):
        funcs.append(lambda i=i: i)  # Correct
    return funcs

buggy = buggy_build_funcs()
fixed = fixed_build_funcs()
print("\nBuggy closures results:", [f() for f in buggy])   # [2, 2, 2]
print("Fixed closures results:", [f() for f in fixed])     # [0, 1, 2]

# ===================================================
# 7. Practical Uses of Closures
# ===================================================
"""
- Factory functions (configurable behavior without classes)
- Decorators that keep local state
- Simple memoization or caching
- Callback registrations without exposing globals
"""

# ===========================
# END OF TOPIC 1
# ===========================
