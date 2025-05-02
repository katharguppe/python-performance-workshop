"""
Day 2 Session 2 • Topic 1
============================
NumPy Internals & Broadcasting (ASCII-only, gory deep dive)
"""

# ----------------------------------------------------------------
# SECTION 1: PyArrayObject – Low-level ndarray structure
# ----------------------------------------------------------------
"""
CPythons C-struct for ndarray:
--------------------------------
struct PyArrayObject {
    char *data;              // pointer to data
    int nd;                  // number of dimensions
    npy_intp *dimensions;    // shape
    npy_intp *strides;       // step size in bytes per dim
    int flags;               // C_CONTIGUOUS, WRITEABLE, ALIGNED
    ...
};

Understanding these fields helps debug performance issues from misaligned or broadcasted arrays.
"""

import numpy as np
print("=== PyArrayObject Fields (via NumPy interface) ===")
arr = np.arange(12, dtype=np.float64).reshape(3, 4)
print("shape   :", arr.shape)
print("dtype   :", arr.dtype)
print("ndim    :", arr.ndim)
print("strides :", arr.strides)  # bytes to move to next element along each axis
print("flags   :", arr.flags)

# ----------------------------------------------------------------
# SECTION 2: Broadcasting Rules – Explained
# ----------------------------------------------------------------
"""
Broadcasting Algorithm:
------------------------
Align shapes from the right:
   A.shape:        (3, 4)
   B.shape:            (4)
=> Broadcast shape: (3, 4)

RULES:
- Two dims are compatible if:
  1. equal, OR
  2. one of them is 1

- A dim of size 1 will be 'virtually repeated' (stride = 0)

ASCII DIAGRAM:
--------------
  A.shape = (3, 4)
  B.shape =     (4)
→ result.shape = (3, 4)
"""

b = np.arange(4)
print("\n=== Broadcasting A + B ===")
print(arr + b)

# Stride demo via as_strided
from numpy.lib.stride_tricks import as_strided
bv = as_strided(b, shape=(3, 4), strides=(0, b.strides[0]))
print("Broadcasted stride pattern:", bv.strides)

# ----------------------------------------------------------------
# SECTION 3: Memory-mapped arrays & ALIGNED flags
# ----------------------------------------------------------------
print("\n=== Memory-Mapped Array ===")
mmap = np.memmap("memmap_temp.dat", dtype='int32', shape=(4, 4), mode='w+')
mmap[:] = np.arange(16).reshape(4, 4)
print("Memmap shape       :", mmap.shape)
print("C_CONTIGUOUS       :", mmap.flags.c_contiguous)
print("ALIGNED            :", mmap.flags.aligned)
mmap.flush()

# ----------------------------------------------------------------
# SECTION 4: Pitfall – broadcasting that causes huge allocations
# ----------------------------------------------------------------
print("\n=== Hidden Allocation Danger ===")
x = np.ones((10000, 1000))
y = np.ones((1000,))  # implicitly broadcasted

# OK: x * y (broadcast y as row)
x @ y[:1000]  # dot product

# BAD: y[:, None] + x.T → allocates huge (1000, 10000) intermediate
try:
    bad = y[:, None] + x.T
    print("bad shape :", bad.shape)
except MemoryError:
    print("MemoryError caught")

# ----------------------------------------------------------------
# SECTION 5: Sliding Window View (no copies)
# ----------------------------------------------------------------
"""
Use case: extract all 3x3 blocks from a 5x5 image

ASCII WINDOW:
[ 0  1  2 ]
[ 5  6  7 ]
[10 11 12 ]

as_strided creates a view with offset jumps:
shape: (rows - 2, cols - 2, 3, 3)
strides: (row_stride, col_stride, row_stride, col_stride)
"""

def sliding_window_view(arr, size):
    from numpy.lib.stride_tricks import as_strided
    s0, s1 = arr.strides
    m, n = arr.shape
    return as_strided(arr,
                      shape=(m - size + 1, n - size + 1, size, size),
                      strides=(s0, s1, s0, s1))

img = np.arange(25).reshape(5, 5)
patches = sliding_window_view(img, 3)
print("\n=== First 3x3 patch ===\n", patches[0, 0])
print("Window shape:", patches.shape)

# ----------------------------------------------------------------
# CLEANUP
# ----------------------------------------------------------------
import os
#os.remove("memmap_temp.dat")
