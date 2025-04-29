"""
Session 2 - Topic 3
===================
Optimization Implications - DEEP DIVE
"""

# =====================================
# 1. Why Optimization Implications Matter
# =====================================
"""
- Python is an interpreted language. Execution speed depends not just on algorithm but *how* you write the code.
- Different constructs (generator, list comp, global vs local) emit different bytecode.
- Some cause heavier GC load, others cause deeper call stacks.
- Understanding these differences is key to tuning critical paths.
"""

# =====================================
# 2. Generator vs List Comprehension
# =====================================
"""
Generators are lazy — they produce values one by one.
List comprehensions build entire lists in memory immediately.

Memory vs speed tradeoff:
- Small data: list may be faster.
- Huge data: generator wins (no RAM bloat).

Bytecode for both shows critical differences.
"""

import dis
import timeit

# Example functions
def list_comp():
    return [i*i for i in range(10000)]

def generator_expr():
    return sum(i*i for i in range(10000))

print("\nDisassembly of List Comprehension:")
dis.dis(list_comp)

print("\nDisassembly of Generator Expression:")
dis.dis(generator_expr)

# Timing comparison
print("\nTiming Comparison (500 runs each):")
lc_time = timeit.timeit(list_comp, number=500)
gen_time = timeit.timeit(generator_expr, number=500)

print(f"List Comprehension: {lc_time:.5f} sec")
print(f"Generator Expression: {gen_time:.5f} sec")

# =====================================
# 3. Global vs Local Variable Access
# =====================================
"""
Python accesses:
- Locals: via LOAD_FAST (array lookup, O(1))
- Globals: via LOAD_GLOBAL (dictionary lookup, slower)

You should favor locals inside hot loops.
"""

global_var = 42

def access_global():
    return global_var + 1

def access_local():
    local_var = 42
    return local_var + 1

print("\nDisassembly of Global vs Local Access:")
print("Global Access:")
dis.dis(access_global)
print("\nLocal Access:")
dis.dis(access_local)

# Timing
print("\nTiming (1 million calls):")
g_time = timeit.timeit(access_global, number=1_000_000)
l_time = timeit.timeit(access_local, number=1_000_000)

print(f"Global Variable Access: {g_time:.5f} sec")
print(f"Local Variable Access: {l_time:.5f} sec")

# =====================================
# 4. Function Call Overhead
# =====================================
"""
Each function call:
- Allocates a new PyFrameObject
- Pushes/pops stack frames
- Adds slight latency (~0.2 - 0.5 microseconds per call)

In deeply nested recursion or tight loops, this adds up.
Iteration often beats recursion unless tail call optimized (which Python doesn't do!).
"""

# Recursive Sum
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n-1)

# Iterative Sum
def iterative_sum(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

print("\nTiming Recursive vs Iterative Sum (n=500):")
rec_time = timeit.timeit('recursive_sum(500)', globals=globals(), number=1000)
iter_time = timeit.timeit('iterative_sum(500)', globals=globals(), number=1000)

print(f"Recursive Sum: {rec_time:.5f} sec")
print(f"Iterative Sum: {iter_time:.5f} sec")

# =====================================
# 5. Object Creation Cost
# =====================================
"""
Object construction matters.

- Tuples are slightly cheaper than lists.
- Attribute lookup is slower than dictionary direct lookup.
"""

def build_list():
    return [i for i in range(10)]

def build_tuple():
    return tuple(i for i in range(10))

print("\nTiming List vs Tuple Creation:")
list_time = timeit.timeit(build_list, number=1_000_000)
tuple_time = timeit.timeit(build_tuple, number=1_000_000)

print(f"List Creation: {list_time:.5f} sec")
print(f"Tuple Creation: {tuple_time:.5f} sec")

# Attribute Lookup
class Dummy:
    def __init__(self):
        self.x = 42

dummy = Dummy()

def attr_lookup():
    return dummy.x

def dict_lookup():
    return {'x':42}['x']

print("\nTiming Attribute vs Dictionary Lookup:")
attr_time = timeit.timeit(attr_lookup, number=1_000_000)
dict_time = timeit.timeit(dict_lookup, number=1_000_000)

print(f"Attribute Lookup: {attr_time:.5f} sec")
print(f"Dictionary Lookup: {dict_time:.5f} sec")

# =====================================
# 6. Micro-Benchmarks the Right Way
# =====================================
"""
Proper benchmarking tips:
- Use timeit — it avoids common timing traps.
- Warm up the function before timing (avoid cold start anomalies).
- Repeat multiple times to observe variance.
- Ignore results unless >10% improvement in real-world cases.
"""

# =====================================
# 7. When NOT to Optimize
# =====================================
"""
DO NOT:
- Optimize readability-critical code unless profiling shows major gain.
- Fight Python's dynamic nature: heavy C-like micro-optimizations usually harm clarity without huge speed gain.
- Focus on single function benchmarks in isolation — system effects matter.

ALWAYS:
- Profile first (cProfile, timeit, tracemalloc).
- Optimize data structures before algorithm internals.
- Optimize ONLY your real bottlenecks.
"""

# ===========================
# END OF TOPIC 3
# ===========================
