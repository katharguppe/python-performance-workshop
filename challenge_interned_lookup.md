# 🧠 Challenge: Interned Dictionary Lookup Optimization

Welcome to your first hardcore performance challenge in Python!

---

## 🎯 Objective

You are given 10,000 randomly generated string keys.

Your task:
1. Create two dictionaries:
   - One using `sys.intern()` for keys
   - One without interning
2. Perform lookups in both
3. Benchmark the time difference using `time.time()`
4. Calculate and print:

```python
lookup_time_difference = plain_lookup_time - interned_lookup_time
```

---

## 🚦 Rules
- You **must** use `sys.intern()` in the first dictionary.
- You **must** time both lookups using `time.time()`.
- Complete and run your code within **2 minutes**.
- Use the provided starter code below.

---

## 🧪 Starter Code (Scaffolded)

```python
import random, string, sys, time

# DO NOT MODIFY THIS
random.seed(42)
keys = ["user_" + random.choice(string.ascii_letters) for _ in range(10000)]

# ✅ Your task begins here

# 1. Create an interned dictionary and time the lookup
start = time.time()

# TODO: Create interned dictionary using sys.intern()
# TODO: Perform lookup in loop

interned_lookup_time = time.time() - start

# 2. Create a plain dictionary and time the lookup
start = time.time()

# TODO: Create plain dictionary
# TODO: Perform lookup in loop

plain_lookup_time = time.time() - start

# 3. Calculate the difference
lookup_time_difference = plain_lookup_time - interned_lookup_time
print("lookup_time_difference =", lookup_time_difference)
```

---

## ✅ Submission Guidelines

Please submit:
- 📸 A screenshot of your code and the `lookup_time_difference`
- 📄 Optionally, a link to your GitHub/Gist or notebook
- 🕒 Mention your total time taken

**Send via**:  
- Email  
- WhatsApp  
- Classroom LMS  
- GitHub PR (if forking the repo)

---

## 🏆 Scoring

| Time Taken | Points |
|------------|--------|
| ≤ 2 mins   | 2      |
| ≤ 3 mins   | 1      |
| > 3 mins   | 0      |

---

## 🔁 Repeatable

You may attempt this challenge multiple times — but only your **best attempt** counts.

Good luck, and may the `lookup_time_difference` be large!
