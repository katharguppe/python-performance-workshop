# sum_cython.pyx

def sum_cython(list a, list b):
    cdef int i, n = len(a), val
    result = [0] * n
    for i in range(n):
        result[i] = a[i] + b[i]
    return result