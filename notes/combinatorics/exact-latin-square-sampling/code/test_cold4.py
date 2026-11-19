import unittest
from random import Random

import cold4
from exact_core import is_latin

class ColdWordTests(unittest.TestCase):
    def test_multiple_cuts(self):
        rows = ((0,1,2,3),(1,0,3,2))
        word = (0,1,0,1)
        roots = cold4._packing(rows, 1, word)
        self.assertEqual(roots, ((0,1),(2,3)))
        self.assertEqual(set(cold4._pins(word,1,rows[:1],roots)),
                         {(0,1),(1,0),(2,3),(3,2)})
        self.assertIsNone(cold4._pins(word,1,rows[:1],(roots[0],roots[0])))

    def test_positive_pinning_recipe(self):
        n = 4096
        rows = (tuple(range(n)), tuple(i ^ 1 for i in range(n)))
        word, roots = cold4.canonical_recipe(rows, 1)
        pins = cold4._pins(word, 1, rows[:1], roots)
        self.assertEqual(len(roots), 128)
        self.assertEqual(len(pins), 256)
        self.assertTrue(all(rows[1][i] == j for i, j in pins))

    def test_forward_reverse_same_atom(self):
        for n in range(1, 8):
            got = 0
            for seed in range(20):
                result = cold4.forward(n, Random(seed))
                if result:
                    square, odds = result
                    self.assertTrue(is_latin(square))
                    self.assertEqual(odds, cold4.reverse(square))
                    got += 1
            self.assertGreater(got, 0)

if __name__ == "__main__":
    unittest.main()
