# array_sum_cython.pyx

def fast_array_sum(double[:, ::1] array not None):
    cdef int i, j
    cdef double total = 0.0
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            total += array[i, j]
    return total