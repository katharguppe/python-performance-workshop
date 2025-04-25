# Python Performance Workshop 🔥

Welcome to the **Advanced Python Internals and Performance Workshop** — a 3-day deep-dive into the internals of Python, memory models, object identity, performance tuning, and C-level integrations.

This is **not your typical beginner workshop** — it's crafted for hardcore Python developers who want to master how Python *really* works under the hood.

---

## 🚀 Session 1.1: Object Identity, Interning, and Memory

This session covers:
- Difference between `is`, `==`, and `id()`
- Python interning mechanism for strings and integers
- Memory impact and optimization through reuse
- Performance benchmarking using `timeit`
- Live challenge: Optimize dictionary lookups with `sys.intern`

📘 Notebook: [`Session_1.1_Object_Identity_and_Interning.ipynb`](./Session_1.1_Object_Identity_and_Interning.ipynb)

---

## 🧠 Challenge: Interned Key Lookup Optimization

Participants must:
- Compare dictionary lookup times with and without interning
- Use `sys.intern()` for optimization
- Benchmark execution time
- Submit difference in lookup time

🎯 Target: Complete in under **2 minutes**  
🏆 Reward: **2 points** for all correct and on-time submissions

---

## 📥 How to Submit

This challenge may be hosted on a competitive platform like HackerRank, or you can submit:
1. Your final `lookup_time_difference` result
2. Screenshot of your code or link to a public Gist
3. Time taken to complete

---

## 📅 More Coming Soon

This repo will include:
- Notebooks for all 3 days
- Final integration project
- Extra challenges on async I/O, Cython, and memory profiling

Stay tuned and fork the repo to follow along!

---

Made with ❤️ by Dr. Srinivas K. S.
