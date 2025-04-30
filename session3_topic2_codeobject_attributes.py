"""
Session 3 - Topic 2
===================
__code__, __closure__, and co_* Attributes (DEEP Dive)
"""

# ===================================================
# 1. What is a Code Object?
# ===================================================
"""
Every Python function owns an immutable PyCodeObject exposed as
function.__code__.  It stores:

* Raw bytecode           -> co_code
* Argument counts        -> co_argcount, co_kwonlyargcount, co_posonlyargcount
* Local variable names    co_varnames
* Literals / constants    co_consts
* Referenced names        co_names
* Free/cell vars          co_freevars, co_cellvars
* Stack requirements      co_stacksize
* Metadata (filename, firstlineno, flags, etc.)
"""
# ===================================================
# 2. Example Function for Inspection
# ===================================================
def outer(a, b):
    x = a + b          # cell variable
    y = 42             # cell variable

    def inner(z):
        return x * z + y   # captures x and y
    return inner

inner_fn = outer(2, 3)

# ===================================================
# 3. ASCII Diagram
# ===================================================
"""
outer.__code__.co_cellvars -> ('x','y')
          |
          v
inner.__code__.co_freevars -> ('x','y')
inner.__closure__          -> tuple(cell(x), cell(y))
"""

# ===================================================
# 4. Dump Code Attributes
# ===================================================
import dis, types

def dump_code(fn):
    code = fn.__code__
    attrs = ["co_argcount","co_posonlyargcount","co_kwonlyargcount",
             "co_nlocals","co_stacksize","co_consts","co_names",
             "co_varnames","co_cellvars","co_freevars"]
    print(f"\nCode attributes for {fn.__name__}:")
    for a in attrs:
        print(f" {a:<18}: {getattr(code, a)}")
    print(" Disassembly:")
    dis.dis(fn)

dump_code(inner_fn)

# ===================================================
# 5. Free vs Cell Variables
# ===================================================
print("\nouter.co_cellvars :", outer.__code__.co_cellvars)
print("inner.co_freevars  :", inner_fn.__code__.co_freevars)

# ===================================================
# 6. Modifying a Code Object (Advanced Demo)
# ===================================================
orig = inner_fn.__code__
consts = list(orig.co_consts)
if 42 in consts:
    consts[consts.index(42)] = 99  # change literal 42 -> 99

new_code = types.CodeType(
    orig.co_argcount,
    orig.co_posonlyargcount,
    orig.co_kwonlyargcount,
    orig.co_nlocals,
    orig.co_stacksize,
    orig.co_flags,
    orig.co_code,
    tuple(consts),
    orig.co_names,
    orig.co_varnames,
    orig.co_filename,
    orig.co_name,
    orig.co_firstlineno,
    orig.co_lnotab,
    orig.co_freevars,
    orig.co_cellvars
)

patched_inner = types.FunctionType(new_code, globals(), "patched_inner", closure=inner_fn.__closure__)
print("\npatched_inner(10) =", patched_inner(10))  # uses 99 instead of 42

# ===================================================
# 7. When NOT to Hack Code Objects
# ===================================================
"""
* Highly CPython‑specific; breaks on PyPy, MicroPython, future versions.
* Can introduce hard‑to‑debug crashes.
* Security risk if untrusted code is injected.
Only for controlled tooling or research.
"""

# ===========================
# END OF TOPIC 2
# ===========================
