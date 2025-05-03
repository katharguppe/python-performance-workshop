from cython.parallel import prange

def parallel_sum(double[:] arr):
    cdef int i
    cdef double total = 0.0
    with nogil:
        for i in prange(len(arr)):
            total += arr[i]
    return total