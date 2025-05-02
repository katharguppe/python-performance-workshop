"""
Day 2 – Session 1  •  Topic 4
=============================
12‑Point Best‑Practice Checklist for Profiling & Optimization  (ASCII)
"""

# ------------------------------------------------------------
# 0. Purpose
# ------------------------------------------------------------
"""
This file is NOT for speed – it is a living checklist you can import
or `python -m` to print the rules and run a micro‑benchmark variance demo.
All text is ASCII‑only.
"""

RULES = [
    "1. ALWAYS measure before you optimize (no guess‑work).",
    "2. Warm up the code path; ignore first‑run JIT/heavy import cost.",
    "3. Run at least 5‑10 repeats, report median and MAD (median abs dev).",
    "4. Separate I/O cost from CPU cost; measure them independently.",
    "5. Use time.perf_counter() or timeit – never time.time() on modern OS.",
    "6. For memory, compare tracemalloc snapshots, not single totals.",
    "7. Disable GC (gc.disable()) inside tight loops to isolate alloc cost.",
    "8. Only micro‑optimize after algorithm/data‑structure choices are done.",
    "9. Watch variance: if stddev >10%, results are not stable – find cause.",
    "10. Document environment: Python version, OS, CPU governor, cores.",
    "11. Keep benchmark data in version control (JSON/CSV).",
    "12. Roll back optimizations that harm readability with <5% gain.",
]

def print_rules():
    print("Best‑Practice Rules:")
    for line in RULES:
        print("  " + line)

# ------------------------------------------------------------
# 1. Variance demo with bootstrap sampling
# ------------------------------------------------------------
import time, statistics, random

def micro_sleep():
    # jitter: simulate noisy workload 0.5‑1.0 ms
    time.sleep(random.uniform(0.0005, 0.001))

def run_variance(repeats=20):
    durations = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        micro_sleep()
        durations.append((time.perf_counter() - t0) * 1e6)  # microsec
    median = statistics.median(durations)
    mad = statistics.median([abs(x - median) for x in durations])
    print("\nTiming variance demo (microseconds):")
    print("  median =", round(median, 3),
          "  MAD =", round(mad, 3))
    # ASCII sparkline
    print("  " + "".join("*" if d < median else "+" for d in durations))

# ------------------------------------------------------------
# 2. Macro vs Micro benchmark illustration (ASCII diagram)
# ------------------------------------------------------------
def ascii_macro_micro():
    print(r"""
Macro benchmark
  ┌───────────────────────────────────────────┐
  │ Whole app: HTTP request -> DB -> render   │
  └───────────────────────────────────────────┘

Micro benchmark
  ┌───┐      ┌───┐
  │fnA│ 20µs │fnB│ 5µs
  └───┘      └───┘

Optimize fnA/fnB ONLY if they sit in the hot path of macro benchmark.
""")

# ------------------------------------------------------------
# CLI usage
# ------------------------------------------------------------
if __name__ == "__main__":
    print_rules()
    ascii_macro_micro()
    run_variance()
