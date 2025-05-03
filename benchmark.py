# benchmark.py
import timeit
import numpy as np

# Import both implementations
from fib_cython import fib_cython  # Compiled Cython version
from performance_benchmark import fib_python  # Pure Python version

def benchmark():
    n = 1000000  # Input size (adjust based on your hardware)
    
    # Verify correctness (optional but recommended)
    assert fib_cython(n) == fib_python(n), "Results do not match!"
    
    # Time both implementations
    python_time = timeit.timeit(lambda: fib_python(n), number=100)
    cython_time = timeit.timeit(lambda: fib_cython(n), number=100)
    
    print(f"Python version: {python_time:.4f}s")
    print(f"Cython version: {cython_time:.4f}s")
    print(f"Speedup: {python_time / cython_time:.2f}x")

if __name__ == "__main__":
    benchmark()