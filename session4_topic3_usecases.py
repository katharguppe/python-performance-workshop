"""
Session 4 - Topic 3 (Use Cases)
===============================
Identity vs Equality for Buffers – Two practical scenarios (ASCII only)
"""

import array, mmap, tempfile, os

# ---------------------------------------------------------
# Case 1: Prevent double-write when two memoryviews alias
# WHY:
#   In a function that writes to both "dst" and "src", you must be sure
#   they do not reference the same underlying buffer or you risk data corruption.
# ---------------------------------------------------------
def safe_copy(src_view, dst_view):
    """Copy data only if src and dst do NOT alias the same memory."""
    if src_view.obj is dst_view.obj:
        raise ValueError("Source and destination share memory! abort copy.")
    dst_view[:] = src_view

buf1 = bytearray(b"AAAAAAA")
buf2 = bytearray(b"BBBBBBB")
mv_src = memoryview(buf1)
mv_dst = memoryview(buf2)
safe_copy(mv_src, mv_dst)
print("safe_copy worked  :", buf2)

try:
    mv_alias = memoryview(buf1)[2:]   # slice still refers to buf1
    safe_copy(mv_src, mv_alias)
except ValueError as e:
    print("Alias detected   :", e)
mv_src.release(); mv_dst.release(); mv_alias.release()

# ---------------------------------------------------------
# Case 2: Cache deduplication for large read‑only bytes
# WHY:
#   Avoid keeping multiple identical immutable blobs in RAM.
#   Compare value equality first; if equal, reuse existing object.
# ---------------------------------------------------------
class BlobCache:
    def __init__(self):
        self._store = []
    def add_blob(self, blob):
        for existing in self._store:
            if blob == existing:      # same content
                print("Reusing existing blob object")
                return existing       # may or may not be same identity
        self._store.append(blob)
        print("Storing new blob")
        return blob

cache = BlobCache()
b1 = bytes(os.urandom(8))
b2 = b1[:]      # equal content, new identity
cache.add_blob(b1)
cache.add_blob(b2)  # detects equality, avoids duplicate

# End of use‑cases
