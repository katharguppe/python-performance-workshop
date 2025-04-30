"""
Session 4 - Topic 3
===================
Object Identity vs Equality for Buffer Objects (ASCII only)
"""

# -------------------------------------------------
# 1. Quick Refresher
# -------------------------------------------------
"""
identity : `is`   -> two variables reference the *same* object (id equal)
equality : `==`   -> objects compare equal in value/content
"""

# -------------------------------------------------
# 2. Bytearray and memoryview slices
# -------------------------------------------------
ba = bytearray(b"ABCDEF")
mv1 = memoryview(ba)
mv2 = mv1[0:3]     # view of first 3 bytes
mv3 = memoryview(ba)  # second independent view

print("mv1 is mv2     :", mv1 is mv2)  # False (distinct view objects)
print("mv2 == mv3[:3] :", mv2 == mv3[:3])  # True (same bytes)
print("mv2.obj is ba  :", mv2.obj is ba)   # True (share memory)

# ASCII map
print("""
ASCII diagram:
bytearray ba  ->  [A][B][C][D][E][F]
mv2 (0:3)     ->  ^^^^^^^^^
mv3           ->  ^^^^^^^^^^^^^^^^^^^
All share SAME underlying buffer, but mv1/mv2/mv3 are distinct Python objs.
""")

# modify through view
mv2[0] = ord(b'Z')
print("After mv2 mutate ba :", ba)

mv1.release(); mv2.release(); mv3.release()

# -------------------------------------------------
# 3. Immutable bytes copies
# -------------------------------------------------
b1 = bytes(b"hello")
b2 = b1[:]          # slice copy (identical value)
print("\nbytes equality     :", b1 == b2)   # True
print("bytes identity      :", b1 is b2)    # Implementation-dependent

# Python may intern small immutable literals but never rely on that.

# -------------------------------------------------
# 4. array.array view identity demo
# -------------------------------------------------
import array
arr = array.array('i', range(5))
view_a = memoryview(arr)
view_b = view_a[1:]
print("\narray view share   :", view_b.obj is arr)  # True
view_a.release(); view_b.release()

# -------------------------------------------------
# 5. NumPy base attribute (if installed)
# -------------------------------------------------
try:
    import numpy as np
    x = np.arange(8)
    y = x[2:6]        # view
    print("\nNumPy value equal :", np.array_equal(y, x[2:6]))
    print("NumPy identity     :", y is x)             # False
    print("Share memory       :", y.base is x)        # True
except ImportError:
    print("\nNumPy not installed; skipping NumPy demo.")

# -------------------------------------------------
# 6. Equality pitfalls with memoryview
# -------------------------------------------------
data1 = bytearray(b"XXXX")
data2 = bytearray(b"XXXX")
mv_a = memoryview(data1)
mv_b = memoryview(data2)
print("\nEqual content, separate memory:", mv_a == mv_b)  # True
print("Identity check obj attr        :", mv_a.obj is mv_b.obj)  # False
mv_a.release(); mv_b.release()

# -------------------------------------------------
# 7. When Identity Matters
# -------------------------------------------------
"""
Use `is` or `.obj` to confirm two views alias the same buffer
when you plan to mutate through one of them.

For immutables (bytes), identity rarely matters;
value equality is enough.
"""

# End of Topic 3
