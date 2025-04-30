"""
Session 4 - Topic 4
===================
CHALLENGE: Reverse a Large Array via memoryview (zero copy)
-----------------------------------------------------------
Goal:
    Implement reverse_inplace(buf) that reverses the order of
    elements in an array.array *without* allocating another
    large buffer.  Use memoryview to swap bytes in-place.

Requirements:
    * Accepts an array.array of any type code (e.g., 'I', 'f').
    * Must not create a second array/bytes object of same size.
    * Runtime O(n), memory O(1).
    * After the call, original buffer order is reversed.

Hints:
    * Create a memoryview with the same format (cast).
    * Use two indices (left, right) and swap items.
    * Call mv.release() when done to free the view.
"""

import array
def reverse_inplace(buf):
    """
    Temporary stub so the script runs without raising an error.
    Does nothing except print a reminder.
    """
    print("reverse_inplace() is still a stub no action taken.")
    # You could also use:  pass


# -------------------------------------------------
# Demo / test helper
if __name__ == "__main__":
    arr = array.array('I', range(10))
    print("Before:", list(arr))
    reverse_inplace(arr)          # expected to reverse contents
    print("After :", list(arr))
