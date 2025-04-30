"""
Session 4 - Topic 2
===================
Slice Operations: Copy vs View  (ASCII-only Deep Dive)
"""

# 1. Why Slices Matter
"""
Copy slices allocate new memory;
View slices alias the same memory (zero-copy).
"""

# 2. Lists: slice always copies
lst = list(range(10))
sub = lst[2:5]
sub[0] = 99
print("List original :", lst)
print("List slice    :", sub)

# 3. Bytearray copy vs memoryview view
data = bytearray(b"abcdefghij")
slice_copy = data[2:6]
slice_copy[0] = ord(b'Z')
print("\nBytearray after copy mutate:", data)

view = memoryview(data)
view_slice = view[2:6]
view_slice[0] = ord(b'Y')
print("Bytearray after view mutate:", data)
view_slice.release()
view.release()

print("""
ASCII diagram:
[bytearray] <-> memoryview slice shares same bytes (mutations reflect)
""")

# 4. array.array slicing
import array
arr = array.array('I', range(6))
mv = memoryview(arr)
half = mv[3:]          # view of last 3 items (no cast needed)
half[0] = 777
print("array after mv view edit:", arr)
half.release()
mv.release()

# 5. NumPy slice view vs copy
try:
    import numpy as np
    big = np.arange(10, dtype='int32')
    view_np = big[2:8]
    view_np[:] = -1
    print("\nNumPy after view mutate   :", big)
    copy_np = big[2:8].copy()
    copy_np[:] = 42
    print("NumPy after .copy() mutate:", big)
except ImportError:
    print("\nNumPy not installed; skipping demo.")

# 6. Timing copy vs view (scaled-down)
import time
N = 1_000_000
big_list = list(range(N))
t0 = time.time()
_ = big_list[::2]
t_copy = time.time() - t0

big_byte = bytearray(b"x" * N)
t0 = time.time()
mv_half = memoryview(big_byte)[::2]
t_view = time.time() - t0
mv_half.release()

print("\nTiming (rough):")
print(" List slice copy :", round(t_copy, 4), "sec")
print(" memoryview view :", round(t_view, 4), "sec")

# 7. Pitfalls
"""
- Mutating through a view changes the original data.
- Resizing the source (e.g., bytearray append) invalidates existing views.
- Always call .release() on a memoryview when done (esp. with mmap).
"""
