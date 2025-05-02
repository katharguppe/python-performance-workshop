"""
Day 2 – Session 1  •  Challenge
================================
Task: Refactor recursive Fibonacci into a memoized DP version
and prove >= 20x speedup and >= 50x fewer allocations
using cProfile + tracemalloc.

File: d2s1_challenge.py
"""

import cProfile, pstats, io, tracemalloc, functools

# Naive recursive Fibonacci
def fib_rec(n):
    return n if n < 2 else fib_rec(n-1) + fib_rec(n-2)

# --- TODO student implementation ---------------
def fib_fast(n):
    """
    Memoized or bottom-up DP Fibonacci.
    Must return same result as fib_rec(n).
    """
    raise NotImplementedError("implement fib_fast")

# --- Profiler helper (provided) ---------------
def run_profile(fn, n):
    pr = cProfile.Profile()
    pr.enable()
    tracemalloc.start()
    fn(n)
    snap = tracemalloc.take_snapshot()
    pr.disable()
    stats_io = io.StringIO()
    pstats.Stats(pr, stream=stats_io).strip_dirs().sort_stats("cumtime").print_stats(5)
    return stats_io.getvalue(), snap

if __name__ == "__main__":
    N = 30
    print("Profiling naive fib_rec...")
    rec_stats, rec_snap = run_profile(fib_rec, N)
    print(rec_stats)

    print("Profiling student fib_fast...")
    try:
        fast_stats, fast_snap = run_profile(fib_fast, N)
        print(fast_stats)
        # student should add snapshot comparison and print improvement numbers
    except NotImplementedError:
        print("fib_fast not implemented yet")
