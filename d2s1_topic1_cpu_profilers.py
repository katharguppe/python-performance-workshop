"""
Day 2  Session 1    Topic 1
==============================
CPU Profilers and FlameGraph Basics  (ASCII only, deep dive)
"""

import cProfile
import pstats
import io
import time
import sys
import array

# Sample functions
def slow_factorial(n):
    return 1 if n == 0 else n * slow_factorial(n - 1)

def fast_factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

# cProfile example
pr = cProfile.Profile()
pr.enable()
slow_factorial(15)
fast_factorial(15)
pr.disable()

s = io.StringIO()
pstats.Stats(pr, stream=s).strip_dirs().sort_stats("cumulative").print_stats(10)
print(s.getvalue())

# Line profiler example (optional)
try:
    from line_profiler import LineProfiler

    def busy():
        total = 0
        for i in range(10000):
            total += i * i
        return total

    lp = LineProfiler(busy)
    lp.enable_by_count()
    busy()
    lp.disable()
    print("line_profiler stats:")
    lp.print_stats()
except ImportError:
    print("line_profiler not installed\n")

# Flame graph tools usage example
print(r"""
py-spy usage (external):
  py-spy record -o flame.svg -- python your_script.py
perf usage (Linux):
  perf record -g -- python your_script.py
  perf script | flamegraph.pl > flame.svg
ASCII flamegraph sample:
 slow_factorial ######
  builtin_mul   @@
""")