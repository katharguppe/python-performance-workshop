"""
Day 2  Session 1  •  Topic 2
=============================
Memory Profilers & Allocation Tracing  (ASCII-only, deep dive)
"""

# ----------------------------------------------------------
# 1. tracemalloc snapshot diff
# ----------------------------------------------------------
import tracemalloc, sys, random

def waste_memory():
    """Create a bunch of lists to simulate leak."""
    junk = []
    for _ in range(1000):
        junk.append(bytearray(random.randint(1000, 2000)))
    return junk

tracemalloc.start()

snap1 = tracemalloc.take_snapshot()
_ = waste_memory()
snap2 = tracemalloc.take_snapshot()

top_stats = snap2.compare_to(snap1, 'lineno')[:5]
print("Top 5 memory changes (tracemalloc diff):")
for stat in top_stats:
    print(stat)

# ----------------------------------------------------------
# 2. memory_profiler live RSS (if installed)
# ----------------------------------------------------------
try:
    from memory_profiler import memory_usage

    def task():
        waste_memory()
        return "done"

    mem_before = memory_usage()[0]
    memory_usage(task, interval=0.1)
    mem_after = memory_usage()[0]
    print("\nmemory_profiler RSS diff:", mem_after - mem_before, "MiB")
except ImportError:
    print("\nmemory_profiler not installed; skipping RSS demo")

# ----------------------------------------------------------
# 3. objgraph growth detection (if installed)
# ----------------------------------------------------------
try:
    import objgraph, gc
    gc.collect()
    print("\nobjgraph top growth:")
    objgraph.show_growth(limit=5)
except ImportError:
    print("\nobjgraph not installed; skipping growth demo")

# ----------------------------------------------------------
# 4. ASCII Heap Timeline
# ----------------------------------------------------------
print(r"""
ASCII heap timeline (bytes):

time -->   leak grows
          ^snap1      ^snap2
Use tracemalloc to reveal source lines.
""")

# ----------------------------------------------------------
# 5. Best-practice tips
# ----------------------------------------------------------
"""
* Enable tracemalloc in entry point:  tracemalloc.start(25)  (# frames)
* Always compare snapshots instead of single absolute numbers.
* For RSS, run on Linux with --disable-gc to isolate GC noise if needed.
* Release large objects (del / context manager) before final snapshot.
"""

# End Topic 2
