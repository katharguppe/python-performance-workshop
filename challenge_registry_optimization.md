# 🧠 Challenge: Optimize a Registry to Fit in 300 KB

Welcome to your next hardcore performance challenge in Python internals.

---

## 🎯 Objective

Design and implement a high-performance object registry that stores 100,000 unique entries (e.g., users, sensors, log entries) **within 300 KB of memory**.

You must:
- Use `__slots__` to reduce memory overhead
- Avoid `__dict__` and `__weakref__` unless necessary
- Eliminate circular references
- Use `gc`, `sys`, or `tracemalloc` to measure memory usage
- Bonus: Use `weakref` if needed to reduce retention

---

## 🛠️ Requirements

- Each object must store:
  - An integer ID
  - A name (max 10 characters)
  - A timestamp (use int or float)

- Total memory used by all objects (plus storage structure) must be **≤ 300 KB**

---

## 📏 What You'll Submit

1. Your registry class (using `__slots__`)
2. Code to generate and store 100,000 items
3. Output of your memory measurement using `sys.getsizeof()` or `tracemalloc`
4. A printout of the final memory used in kilobytes

---

## 🧪 Starter Code (Scaffold)

```python
import sys
import tracemalloc
from time import time

# TODO: Define your optimized class here using __slots__
class Entry:
    pass

# Simulate registry
registry = []

tracemalloc.start()

# TODO: Fill registry with 100,000 entries
for i in range(100000):
    # Example data
    obj = Entry()  # Add proper init
    registry.append(obj)

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')

total_mem = sum(stat.size for stat in top_stats)
print(f"Total memory used: {total_mem / 1024:.2f} KB")

# ✅ Your memory must be under 300 KB!
```

---

## 🏆 Scoring Criteria

| Criteria | Points |
|----------|--------|
| Memory ≤ 300 KB | 3 |
| Uses `__slots__` correctly | 1 |
| Measures memory with `tracemalloc` or `sys` | 1 |
| Bonus: Uses `weakref` where applicable | +1 |

---

## 📬 Submission

Please submit:
- Your code (.py or notebook)
- Screenshot showing memory output
- Optional: link to your GitHub or Gist

---

Good luck optimizing like a true Pythonist 🐍💪
