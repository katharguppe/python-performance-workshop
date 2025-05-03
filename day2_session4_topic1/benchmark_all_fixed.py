# python setup.py build_ext --inplace
# python benchmark_all_fixed.py
# benchmark_all_fixed.py
#
# Purpose: Benchmark multiple Cython vs Python functions after precompilation via setup.py
# Assumes all .pyx files and setup.py are in the same directory
# Run with:
#   python benchmark_all_fixed.py

import timeit
import numpy as np

# Import precompiled Cython modules
import sum_cython
import distance_cython
import array_sum_cython
import parallel_sum_cython

# -------------------------------
# Pure Python Versions
# -------------------------------

def sum_python(a, b):
    return [a[i] + b[i] for i in range(len(a))]

def distance_python(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def fast_array_sum_python(arr):
    total = 0.0
    rows = len(arr)
    cols = len(arr[0])
    for i in range(rows):
        for j in range(cols):
            total += arr[i][j]
    return total

def parallel_sum_python(arr):
    total = 0.0
    for val in arr:
        total += val
    return total

# -------------------------------
# Benchmarking Helper
# -------------------------------

def benchmark(name, func_py, func_cy, args_func, number=10):
    raw_args = args_func()  # These are array.array by default

    # For Python version: convert arrays back to lists
    py_args = [list(arg) if isinstance(arg, array.array) else arg for arg in raw_args]

    # Run once to catch errors early
    py_result = func_py(*py_args)
    cy_result = func_cy(*raw_args)

    # Optional type check
    try:
        assert type(py_result) == type(cy_result), f"Return types differ in {name}"
    except AssertionError as e:
        print(e)

    # Benchmarking
    t_py = timeit.timeit(lambda: func_py(*py_args), number=number)
    t_cy = timeit.timeit(lambda: func_cy(*raw_args), number=number)

    print(f"{name}:")
    print(f"  Python: {t_py:.6f}s")
    print(f"  Cython: {t_cy:.6f}s")
    print(f"  Speedup: {t_py / t_cy:.2f}x\n")

# -------------------------------
# Generate Test Data
# -------------------------------

import array

import array

def get_sum_data():
    size = 1_000_000
    a = list(range(size))
    b = list(range(size))
    return (a, b)

def get_distance_data():
    return ((1.0, 2.0), (3.0, 4.0))

def get_array_sum_data():
    return (np.random.rand(1000, 1000), )

def get_parallel_sum_data():
    return (np.random.rand(10_000_000), )

# -------------------------------
# Run Benchmarks
# -------------------------------

if __name__ == "__main__":
    print("🚀 Starting benchmarks...\n")

    benchmark("4.1 List Sum", sum_python, sum_cython.sum_cython, get_sum_data)
    benchmark("4.2 Distance Calculation", distance_python, distance_cython.calculate_distance, get_distance_data)
    benchmark("5.1 Fast Array Sum", fast_array_sum_python, array_sum_cython.fast_array_sum, get_array_sum_data)
    benchmark("5.2 Parallel Sum", parallel_sum_python, parallel_sum_cython.parallel_sum, get_parallel_sum_data)