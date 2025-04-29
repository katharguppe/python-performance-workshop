"""
Session 2 - Topic 2
===================
Frame Objects and Function Calling Internals - DEEP DIVE
"""

# =====================================
# 1. Why Frame Objects Exist
# =====================================
"""
- A frame object (PyFrameObject) represents an *execution context*.
- Every active function call has its own frame.
- Frames maintain:
    - Local variables
    - Global variables
    - Builtins
    - Instruction pointer (bytecode offset)
    - Call back-link to previous frame
- Essential for:
    - Recursive calls
    - Debugging
    - Exception tracing (tracebacks follow frame chain)
"""

# =====================================
# 2. Inspecting Live Frames with inspect Module
# =====================================
"""
Python’s inspect module gives a pure Python API to peek into frame internals.
"""

import inspect

def first():
    second()

def second():
    third()

def third():
    frame = inspect.currentframe()
    print("\nCurrent Frame:")
    print("Function name:", frame.f_code.co_name)
    print("Locals:", frame.f_locals)
    print("Bytecode offset (f_lasti):", frame.f_lasti)
    
    back = frame.f_back
    print("\nCaller Frame:")
    print("Function name:", back.f_code.co_name)
    
    back2 = back.f_back
    print("\nGrandcaller Frame:")
    print("Function name:", back2.f_code.co_name)

first()

# =====================================
# 3. Understanding Frame Chains
# =====================================
"""
Each call creates a new frame.
- f_back links to the caller.
- Walking f_back repeatedly gives entire call stack.
- Frame chain ends at top-level interpreter frame (e.g., __main__).
"""

def walk_frame_chain():
    frame = inspect.currentframe()
    depth = 0
    while frame:
        print(f"Depth {depth}: Function {frame.f_code.co_name}")
        frame = frame.f_back
        depth += 1

print("\nWalking current frame chain:")
walk_frame_chain()

# =====================================
# 4. How Function Calls Work Internally
# =====================================
"""
Inside CPython:
    - When you call a function:
        1. Arguments are evaluated (pushed on stack).
        2. A new frame is created with new locals array.
        3. Execution switches to the new frame.
        4. On return, frame is destroyed, and control returns to previous frame.
    
Major opcodes involved:
    - CALL_FUNCTION
    - LOAD_GLOBAL
    - RETURN_VALUE
"""

import dis

def add(x, y):
    return x + y

print("\nDisassembly of simple add function:")
dis.dis(add)

# Look for LOAD_FAST, BINARY_ADD, RETURN_VALUE opcodes.

# =====================================
# 5. Fast Locals Optimization
# =====================================
"""
Optimization:
- Instead of using a dictionary for locals, Python uses a *fixed array* internally.
- LOAD_FAST and STORE_FAST opcodes directly index into this array.
- Result: variable access becomes O(1) indexed lookup instead of hash table search.

Evidence:
- Functions without dynamic locals are much faster than exec() or eval() scopes.
"""

def fast_example(a, b):
    return a * b

print("\nDisassembly of fast locals example:")
dis.dis(fast_example)

# Look for LOAD_FAST / STORE_FAST — direct slot access.

# =====================================
# 6. Inline Caches and Specialization
# =====================================
"""
Python 3.11+ introduced Adaptive Specialization (PEP 659):
- Opcodes mutate at runtime after a few executions to a specialized version.
- Reduces attribute lookup cost, call overhead.

Example:
- LOAD_ATTR --> LOAD_ATTR_ADAPTIVE --> LOAD_ATTR_SLOT / LOAD_ATTR_INSTANCE_VALUE

You can observe specialization stats via sys._get_specialization_stats().
"""

import sys

def attr_demo():
    class Obj:
        def __init__(self):
            self.val = 10
    o = Obj()
    return o.val

attr_demo()
print("\nSpecialization stats (may require Python 3.11+):")
try:
    print(sys._get_specialization_stats())
except AttributeError:
    print("Specialization stats not available (needs Python 3.11+)")

# =====================================
# 7. When Frame Knowledge Helps or Hurts
# =====================================
"""
Helps:
- Debugging deeply recursive calls.
- Custom tracers, profilers, debuggers (e.g., coverage tools).
- Detecting memory leaks (lingering frame references).

Hurts:
- Over-optimizing trivial code paths.
- Misusing inspect to peek into frames instead of clean design.
- Keeping frame references alive → memory leaks (common GC bug).
"""

# ===========================
# END OF TOPIC 2
# ===========================

