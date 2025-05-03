# distutils: language = c++

def fib_cython(int n):
    """Cython implementation of Fibonacci sequence with explicit typing"""
    cdef int a = 0, b = 1, temp
    result = []
    while a < n:
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result