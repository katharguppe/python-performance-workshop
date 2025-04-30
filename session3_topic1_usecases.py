"""
Session 3 - Topic 1 (Use‑Cases)
===============================
Four practical closure use‑cases in one file:
1. Factory functions
2. Decorator with local state
3. Memoization / caching
4. Callback registration
"""

# ---------------------------------------------------
# 1. Factory Function (configurable behavior)
# ---------------------------------------------------
def power_factory(exp):
    """Return a function that raises numbers to *exp* power."""
    def power(n):
        return n ** exp
    return power

square = power_factory(2)
cube   = power_factory(3)
print("Factory Function -> square(5):", square(5))  # 25
print("Factory Function -> cube(5):",   cube(5))    # 125)

# ---------------------------------------------------
# 2. Decorator that keeps local state
# ---------------------------------------------------
def call_counter(func):
    """Decorator that counts calls to *func*."""
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"[{func.__name__}] call #{count}")
        return func(*args, **kwargs)
    return wrapper

@call_counter
def greet(name):
    print("Hello,", name)

greet("Alice")
greet("Bob")

# ---------------------------------------------------
# 3. Memoization / caching with closure
# ---------------------------------------------------
def memoize(fn):
    cache = {}
    def memoized(x):
        if x not in cache:
            cache[x] = fn(x)
        return cache[x]
    return memoized

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print("Memoized fib(10):", fib(10))  # 55

# ---------------------------------------------------
# 4. Callback registration emitter
# ---------------------------------------------------
def make_event_emitter():
    listeners = []
    def on(fn):
        listeners.append(fn)
        return fn
    def emit(value):
        for fn in listeners:
            fn(value)
    return on, emit

on_data, emit_data = make_event_emitter()

@on_data
def printer(msg):
    print("Printer got:", msg)

def logger(msg):
    print("Log:", msg)
on_data(logger)

emit_data("Hello!")
