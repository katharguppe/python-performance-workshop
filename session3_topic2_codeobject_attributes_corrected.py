"""
Session 3 - Topic 2
===================
__code__, __closure__, and co_* Attributes (DEEP Dive)
"""

# ---------------------------------------------------
# 1. Code Object Overview
# ---------------------------------------------------
"""
A PyCodeObject stores bytecode + metadata:
  * co_code        – raw bytecode
  * co_argcount    – positional arg count
  * co_consts      – literal pool
  * co_names       – global / attr names
  * co_varnames    – local variable names
  * co_freevars    – names captured from outer scope
  * co_cellvars    – locals captured by inner funcs
  * co_stacksize   – VM stack depth needed
  * many more …
All exposed via function.__code__.
"""
# ---------------------------------------------------
# 2. Example function to inspect
# ---------------------------------------------------
def outer(a, b):
    x = a + b
    y = 42
    def inner(z):
        return x * z + y
    return inner

inner_fn = outer(2, 3)

# ---------------------------------------------------
# 3. Dump code attributes
# ---------------------------------------------------
import dis, types, sys

def dump_code(fn):
    code = fn.__code__
    keys = ["co_argcount","co_posonlyargcount","co_kwonlyargcount",
            "co_nlocals","co_stacksize","co_consts","co_names",
            "co_varnames","co_cellvars","co_freevars"]
    print("\nAttributes for", fn.__name__)
    for k in keys:
        print(f" {k:<18}: {getattr(code, k)}")
    print(" Disassembly:")
    dis.dis(fn)

dump_code(inner_fn)

# ---------------------------------------------------
# 4. Free vs cell vars demo
# ---------------------------------------------------
print("\nouter.co_cellvars:", outer.__code__.co_cellvars)
print("inner.co_freevars :", inner_fn.__code__.co_freevars)

# ---------------------------------------------------
# 5. Modify a constant inside the code object SAFELY
# ---------------------------------------------------
orig = inner_fn.__code__
consts = list(orig.co_consts)
if 42 in consts:
    consts[consts.index(42)] = 99
new_consts = tuple(consts)

# Preferred path for 3.8+
if hasattr(orig, "replace"):                         # Py 3.8+
    patched_code = orig.replace(co_consts=new_consts)
else:                                                # Very old versions
    patched_code = types.CodeType(
        orig.co_argcount,
        orig.co_posonlyargcount if sys.version_info >= (3, 8) else 0,
        orig.co_kwonlyargcount,
        orig.co_nlocals,
        orig.co_stacksize,
        orig.co_flags,
        orig.co_code,
        new_consts,
        orig.co_names,
        orig.co_varnames,
        orig.co_filename,
        orig.co_name,
        orig.co_firstlineno,
        orig.co_lnotab,
        orig.co_freevars,
        orig.co_cellvars,
    )

patched_inner = types.FunctionType(
    patched_code, globals(), "patched_inner", closure=inner_fn.__closure__
)
print("\npatched_inner(10) =", patched_inner(10))  # Uses 99 now

# ---------------------------------------------------
# END OF TOPIC 2
# ---------------------------------------------------
