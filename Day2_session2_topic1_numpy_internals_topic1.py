
# ASCII-only NumPy internals deep dive
import numpy as np
from numpy.lib.stride_tricks import as_strided
import os, tracemalloc

a = np.arange(12, dtype='float64').reshape(3,4)
print("a shape", a.shape, "strides", a.strides)
b = np.arange(4)
print("Broadcast a+b:\n", a+b)
# Broadcasting strides demo
bview = as_strided(b, shape=(3,4), strides=(0, b.strides[0]))
print("broadcasted strides", bview.strides)
