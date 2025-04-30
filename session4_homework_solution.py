"""
Session 4 - Homework Solution
=============================
Memory-efficient 2-D matrix using a single contiguous buffer.
"""

import array, ctypes

class MemoryMatrix:
    def __init__(self, rows, cols, typecode='d', fill=0):
        if rows <= 0 or cols <= 0:
            raise ValueError("rows and cols must be positive")
        self.rows = rows
        self.cols = cols
        self.typecode = typecode
        self._buf = array.array(typecode, [fill]) * (rows * cols)

    def _idx(self, r, c):
        if not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError
        return r * self.cols + c

    def __getitem__(self, key):
        r, c = key
        return self._buf[self._idx(r, c)]

    def __setitem__(self, key, value):
        r, c = key
        self._buf[self._idx(r, c)] = value

    def row_view(self, r):
        start = r * self.cols
        end   = start + self.cols
        mv = memoryview(self._buf)[start:end]   # already in correct format
        return mv

    def col_view(self, c):
        step = self.cols
        mv = memoryview(self._buf)[c::step]
        return mv

    def tolist(self):
        v = memoryview(self._buf)
        out = []
        for r in range(self.rows):
            start = r * self.cols
            end   = start + self.cols
            out.append(list(v[start:end]))
        v.release()
        return out

    def __iter__(self):
        for r in range(self.rows):
            yield self.row_view(r)

    def __repr__(self):
        return f"MemoryMatrix({self.rows}x{self.cols}, type={self.typecode})"


# Demo tests
if __name__ == "__main__":
    m = MemoryMatrix(3, 4, typecode='I', fill=0)
    m[1, 2] = 99
    print("m[1,2] :", m[1, 2])
    print("Row 1  :", list(m.row_view(1)))
    print("Col 2  :", list(m.col_view(2)))
    print("tolist :", m.tolist())
