def fib_python(n):
    """Pure Python implementation of Fibonacci sequence"""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result