"""
Session 4 - Topic 5
===================
SOLUTION: Reverse Large Array via memoryview (zero copy)
"""

import array, sys

def reverse_inplace(buf):
    """Reverse array.array contents in-place using memoryview."""
    mv = memoryview(buf)
    itemsize = buf.itemsize
    # Cast to bytes so each index moves by itemsize
    byte_mv = mv.cast('B')
    left = 0
    right = len(buf) - 1
    while left < right:
        # swap items byte by byte
        for i in range(itemsize):
            li = left * itemsize + i
            ri = right * itemsize + i
            byte_mv[li], byte_mv[ri] = byte_mv[ri], byte_mv[li]
        left += 1
        right -= 1
    byte_mv.release()
    mv.release()

# Quick validation
if __name__ == "__main__":
    arr = array.array('I', range(10))
    print("Before:", list(arr))
    reverse_inplace(arr)
    print("After :", list(arr))
