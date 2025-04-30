"""
Session 4 - Topic 1
===================
Buffer Protocol, memoryview, and array.array  (ASCII‑only Deep Dive)
"""

# ----------------------------------------------------
# 1. WHY Buffer Protocol?
# ----------------------------------------------------
"""
Goal: Allow two Python objects to share the **same** block of memory
without copying.  Any object that exposes a raw, contiguous (or strided)
byte buffer can provide it to consumers (e.g. memoryview, NumPy, PIL).

Key CPython API concept:  PyObject_GetBuffer(obj, Py_buffer* view, flags)
  => fills a C struct "Py_buffer" with
     * buf   : void* pointer to memory
     * len   : total bytes
     * itemsize, format, ndim, shape, strides, readonly ...
"""

# ----------------------------------------------------
# 2. array.array produces a real buffer
# ----------------------------------------------------
import array, sys, struct

arr = array.array('I', range(5))   # unsigned int 32‑bit
print("array contents          :", arr)
print("itemsize (bytes)        :", arr.itemsize)
print("buffer nbytes           :", len(arr) * arr.itemsize)

# raw bytes via tobytes()
print("raw bytes               :", arr.tobytes())

# ----------------------------------------------------
# 3. memoryview: zero‑copy window onto any buffer
# ----------------------------------------------------
mv = memoryview(arr)         # no copy!
print("\nmemoryview obj         :", mv)
print("length (items)         :", len(mv))
print("first three items      :", mv[:3].tolist())

# Modify through the view
mv[0] = 999
print("array mutated via view :", arr)

# ----------------------------------------------------
# 4. ASCII Diagram of sharing
# ----------------------------------------------------
print("""\nASCII diagram:
[ array.array buffer ] <--- shared bytes ---> [ memoryview ]
  999  1  2  3  4
Both objects refer to SAME memory; no copy occurs.
""")

# ----------------------------------------------------
# 5. Inspect Py_buffer fields via memoryview attributes
# ----------------------------------------------------
print("Format code            :", mv.format)     # 'I'
print("Itemsize               :", mv.itemsize)
print("Number of dimensions   :", mv.ndim)
print("Contiguous (C order)   :", mv.contiguous)

# ----------------------------------------------------
# 6. Creating bytes/bytearray views (immutable vs mutable)
# ----------------------------------------------------
data = bytearray(b"abcdef")
view = memoryview(data)
ro_view = memoryview(data).cast('B', shape=[6])   # byte‑level

print("\nOriginal bytearray    :", data)
view[1:3] = b"ZZ"        # in‑place
print("After mutation         :", data)

immutable = bytes(data)
try:
    memoryview(immutable)[0] = 65
except TypeError as e:
    print("Attempt to modify bytes view ->", e)

# ----------------------------------------------------
# 7. Buffer protocol with struct – treat as C array
# ----------------------------------------------------
print("\nInterpreting arr buffer via struct iter:")
buffer_bytes = arr.tobytes()
for offset in range(0, len(buffer_bytes), 4):
    val, = struct.unpack_from('I', buffer_bytes, offset)
    print(" index", offset//4, "=", val)

# ----------------------------------------------------
# 8. When NOT to use memoryview
# ----------------------------------------------------
"""
* When the producer object may resize, invalidating pointers (e.g. list).
* When you truly need a *copy* that is safe from source mutation.
* Over networks or multi‑process boundaries without proper locking.
"""

# ---------------- End of Topic 1 ---------------------
