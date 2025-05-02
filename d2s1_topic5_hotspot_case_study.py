"""
Day 2 – Session 1  •  Topic 5
=============================
Hotspot Case Study: Ackermann vs Memoized Ackermann  (ASCII-only)
"""

import cProfile, pstats, io, tracemalloc, functools, sys

# ------------------------------------------------------------
# 1. Naive Ackermann (CPU + memory monster)
# ------------------------------------------------------------
sys.setrecursionlimit(10000)  # allow deep recursion demo

def ack(m, n):
    return n + 1 if m == 0 else (
        ack(m - 1, 1) if n == 0 else ack(m - 1, ack(m, n - 1))
    )

# ------------------------------------------------------------
# 2. Memoized Ackermann
# ------------------------------------------------------------
@functools.lru_cache(maxsize=None)
def ack_mem(m, n):
    return n + 1 if m == 0 else (
        ack_mem(m - 1, 1) if n == 0 else ack_mem(m - 1, ack_mem(m, n - 1))
    )

# ------------------------------------------------------------
# 3. Profiling helper
# ------------------------------------------------------------
def profile(fn, *args):
    pr = cProfile.Profile()
    pr.enable()
    result = fn(*args)
    pr.disable()
    s = io.StringIO()
    pstats.Stats(pr, stream=s).strip_dirs().sort_stats("cumtime").print_stats(10)
    return result, s.getvalue()

# ------------------------------------------------------------
# 4. Run naive vs memoized + tracemalloc diff
# ------------------------------------------------------------
print("Profiling naive ack(3,6)...")
tracemalloc.start()
snap1 = tracemalloc.take_snapshot()
_, naive_stats = profile(ack, 3, 6)
snap2 = tracemalloc.take_snapshot()
top_mem_naive = snap2.compare_to(snap1, 'lineno')[:3]

print("Profiling memoized ack_mem(3,6)...")
snap3 = tracemalloc.take_snapshot()
_, memo_stats = profile(ack_mem, 3, 6)
snap4 = tracemalloc.take_snapshot()
top_mem_memo = snap4.compare_to(snap3, 'lineno')[:3]

# ------------------------------------------------------------
# 5. Display
# ------------------------------------------------------------
print("\n=== Naive cProfile top 10 ===")
print(naive_stats)

print("=== Memoized cProfile top 10 ===")
print(memo_stats)

print("=== Naive memory diff (top 3) ===")
for stat in top_mem_naive:
    print(stat)

print("\n=== Memoized memory diff (top 3) ===")
for stat in top_mem_memo:
    print(stat)

# ------------------------------------------------------------
# 6. ASCII flamegraph representation (collapsed)
# ------------------------------------------------------------
print(r"""
ASCII flamegraph summary (naive):
 ack (700k calls) █████████████████████████
  ack             ███████████████████
   ...
Memoized collapses to:
 ack_mem (subcalls hit cache) ██
""")

# ------------------------------------------------------------
# 7. Conclusion
# ------------------------------------------------------------
print("""
Takeaways:
 - CPU time and memory allocations drop by orders of magnitude after memoization.
 - cProfile + tracemalloc combo highlights both compute and heap hotspots.
 - For recursive pure functions, caching is the first optimization to try.
""")

# End of Topic 5
