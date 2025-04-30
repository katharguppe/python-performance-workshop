"""
Session 4 - Topic 1 (Use Cases)  ASCII‑only
------------------------------------------
Now includes safe release of memoryview before mmap closes.
"""

import array, struct, os, mmap, tempfile, sys

# Case 1: Reverse in-place with memoryview
def reverse_inplace(data):
    mv = memoryview(data)
    left, right = 0, len(mv) - 1
    while left < right:
        mv[left], mv[right] = mv[right], mv[left]
        left += 1
        right -= 1
    mv.release()

ba = bytearray(b"abcdefghijklmnopqrstuvwxyz")
reverse_inplace(ba)
print("Reverse in-place :", ba[:10], "...")

# Case 2: Binary header parse
header = bytearray(os.urandom(16))
mv_head = memoryview(header)
magic, major, minor = struct.unpack_from(">IHH", mv_head, 0)
mv_head.release()
print("Parsed header magic:", magic)

# Case 3: mmap editing without copy
tmp = tempfile.TemporaryFile()
tmp.write(b"abcdefghij")
tmp.flush()

mm = mmap.mmap(tmp.fileno(), 0, access=mmap.ACCESS_WRITE)
mv_map = memoryview(mm)
mv_map[0:4] = b"ZZZZ"
print("After mmap edit  :", mm[:10])
mv_map.release()
mm.close()
tmp.close()

# Case 4: Zero-copy NumPy bridge
try:
    import numpy as np
    arr = array.array('f', [1.0, 2.0, 3.0, 4.0])
    np_view = np.asarray(arr, dtype='float32')
    np_view *= 10
    print("After NumPy scale:", arr)
except ImportError:
    print("NumPy not installed; skipping NumPy demo.")

# Case 5: Packet assembly
def build_packet(parts):
    buf = bytearray(sum(len(p) for p in parts))
    mv = memoryview(buf)
    offset = 0
    for part in parts:
        mv[offset:offset+len(part)] = part
        offset += len(part)
    mv.release()
    return buf

pkt = build_packet([b"HEAD", b"DATA", b"TAIL"])
print("Assembled packet :", pkt)
