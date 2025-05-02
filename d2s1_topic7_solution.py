"""
Day 2 – Session 1  •  Challenge Solution
========================================
Provides memoized Fibonacci + proof of speed/mem gains.
"""

import cProfile, pstats, io, tracemalloc, functools, time

# Naive for reference
def fib_rec(n):
    return n if n < 2 else fib_rec(n-1) + fib_rec(n-2)

@functools.lru_cache(maxsize=None)
def fib_fast(n):
    return n if n < 2 else fib_fast(n-1) + fib_fast(n-2)

def profile(fn, n):
    pr = cProfile.Profile()
    pr.enable()
    tracemalloc.start()
    t0 = time.perf_counter()
    res = fn(n)
    elapsed = time.perf_counter() - t0
    snap = tracemalloc.take_snapshot()
    pr.disable()
    buf = io.StringIO()
    pstats.Stats(pr, stream=buf).strip_dirs().sort_stats("cumtime").print_stats(5)
    return res, elapsed, buf.getvalue(), snap

N = 35
print("=== Naive fib_rec ===")
res1, t1, stats1, snap1 = profile(fib_rec, N)
print(stats1)

print("=== Memoized fib_fast ===")
res2, t2, stats2, snap2 = profile(fib_fast, N)
print(stats2)

print("Result equal :", res1 == res2)
print("Speedup      :", round(t1 / t2, 1), "x")

diff = snap2.compare_to(snap1, "lineno")[:3]
print("Top memory diff (memo vs naive):")
for stat in diff:
    print(stat)
