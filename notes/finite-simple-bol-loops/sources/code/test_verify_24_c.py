"""Regression for the wreath solver's packed hit-table output."""

import ctypes
import unittest

from verify_24_c import compile_c_lib


class TestHitTableCopy(unittest.TestCase):
    def test_two_small_tables_are_packed_with_their_correct_stride(self):
        lib = compile_c_lib()
        lib.copy_hit_tables.argtypes = [
            ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8),
            ctypes.c_int, ctypes.c_int,
        ]
        lib.copy_hit_tables.restype = None
        n = 4
        cyclic = [(x + y) % n for x in range(n) for y in range(n)]
        klein = [x ^ y for x in range(n) for y in range(n)]
        stored = (ctypes.c_uint8 * (2 * 24 * 24))()
        stored[:n * n] = cyclic
        stored[24 * 24:24 * 24 + n * n] = klein
        packed = (ctypes.c_uint8 * (2 * n * n))()

        lib.copy_hit_tables(packed, stored, n, 2)

        self.assertEqual(list(packed[:n * n]), cyclic)
        self.assertEqual(list(packed[n * n:]), klein)


if __name__ == "__main__":
    unittest.main()
