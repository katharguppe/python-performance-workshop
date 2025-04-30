"""
Session 4 - Homework (Patched Stub v2)
======================================
This stub version runs without external errors.
TODO markers remain for student implementation.
"""

import array   # bytearray is built-in, no import needed

# ---------------- MemoryMatrix skeleton ----------------
class MemoryMatrix:
    def __init__(self, rows, cols, typecode='d', fill=0):
        self.rows = rows
        self.cols = cols
        self.typecode = typecode
        self._buf = array.array(typecode, [fill]) * (rows * cols)

    def __getitem__(self, key):
        print("TODO: __getitem__ not implemented")
        return None

    def __setitem__(self, key, value):
        print("TODO: __setitem__ not implemented")

    def row_view(self, r):
        print("TODO: row_view not implemented")
        return memoryview(self._buf)[0:0]

    def col_view(self, c):
        print("TODO: col_view not implemented")
        return memoryview(self._buf)[0:0]

    def tolist(self):
        print("TODO: tolist not implemented")
        return []

    def __iter__(self):
        print("TODO: __iter__ not implemented")
        return iter([])

    def __repr__(self):
        return f"MemoryMatrix({self.rows}x{self.cols})"


# ---------------- Placeholder functions ----------------
def sum_even_bytes(buf):
    print("TODO: sum_even_bytes not implemented")
    return 0

def negate_ints_inplace(arr):
    print("TODO: negate_ints_inplace not implemented")

def alias_detect(view_a, view_b):
    print("TODO: alias_detect not implemented")
    return False


# ---------------- Demo tests --------------------------
if __name__ == "__main__":
    data = bytes(range(10))
    print("Sum even bytes (stub):", sum_even_bytes(data))

    ints = array.array('i', [1, -2, 3])
    negate_ints_inplace(ints)
    print("After negate stub    :", list(ints))

    buf = bytearray(b"hello")
    v1 = memoryview(buf)
    v2 = v1[1:]
    print("Alias detect (stub)  :", alias_detect(v1, v2))

    m = MemoryMatrix(3, 4)
    print("Matrix stub repr     :", m)
    print("Matrix tolist stub   :", m.tolist())
