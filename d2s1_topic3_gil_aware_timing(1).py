"""
Day 2 – Session 1  •  Topic 3
=============================
GIL-Aware Timing & Concurrency Trade‑offs  (ASCII-only deep dive)
"""

import time, threading, multiprocessing, sys, math

# ------------------------------------------------------------
# 1. CPU-bound workload
# ------------------------------------------------------------
def cpu_task(n):
    """Artificially heavy: compute many sqrt operations."""
    total = 0.0
    for i in range(1, n):
        total += math.sqrt(i)
    return total

N = 300_000  # adjust for quick demo

# ------------------------------------------------------------
# 2. Single-thread baseline
# ------------------------------------------------------------
t0 = time.time()
cpu_task(N)
baseline = time.time() - t0
print("Single-thread :", round(baseline, 3), "sec")

# ------------------------------------------------------------
# 3. Multi-thread attempt (GIL blocks real parallelism)
# ------------------------------------------------------------
def threaded_run(workers=4):
    threads = [threading.Thread(target=cpu_task, args=(N,)) for _ in range(workers)]
    for th in threads: th.start()
    for th in threads: th.join()

t0 = time.time()
threaded_run()
threaded_time = time.time() - t0
print("4 threads      :", round(threaded_time, 3), "sec (GIL)")

# ------------------------------------------------------------
# 4. Multi-processing (circumvents GIL)
# ------------------------------------------------------------
def mp_worker(_):
    cpu_task(N)

def multiproc_run(workers=4):
    with multiprocessing.Pool(workers) as pool:
        pool.map(mp_worker, range(workers))

t0 = time.time()
multiproc_run()
mp_time = time.time() - t0
print("4 processes    :", round(mp_time, 3), "sec (no shared GIL)")

# ------------------------------------------------------------
# 5. sys.setswitchinterval demo
# ------------------------------------------------------------
orig_si = sys.getswitchinterval()
sys.setswitchinterval(0.001)   # more context switches
t0 = time.time()
threaded_run()
print("Threads, switch=1ms:", round(time.time() - t0, 3), "sec")
sys.setswitchinterval(orig_si)

# ------------------------------------------------------------
# ASCII diagram of GIL timeline
# ------------------------------------------------------------
print(r"""
ASCII timeline (2 threads):

t=0   [Thread‑A RUN ▓▓▓]  GIL held
      [Thread‑B WAIT ..]

t=0.005 context switch -> GIL to Thread‑B
      [Thread‑A WAIT ..]
      [Thread‑B RUN ▓▓▓]

CPU-bound threads simply alternate; they never run truly in parallel.
""")

# ------------------------------------------------------------
# 6. Best Practices
# ------------------------------------------------------------
"""
* Use multiprocessing or native extensions (NumPy, Cython) for CPU work.
* Use threading for I/O-bound latency hiding.
* Adjust sys.setswitchinterval only for experiments; default 5 ms stable.
* For true parallel CPU inside single CPython process, explore subinterpreters (3.12+ preview) or PyPy STM.
"""

# End of Topic 3
