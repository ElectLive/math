"""Finite, exhaustive support/mass tests; no statistical acceptance tolerances."""
import itertools
import random
import unittest
from fractions import Fraction
from math import factorial, prod

import exact_core as e


class BitTape:
    def __init__(self, draws):
        self.draws = iter(draws)
    def getrandbits(self, bits):
        draw = next(self.draws)
        assert 0 <= draw < 1 << bits
        return draw


class ExactCoreTests(unittest.TestCase):
    def test_bits_avoid_modulo_bias(self):
        self.assertEqual(e.randbelow(1, BitTape([])), 0)
        self.assertEqual(e.randbelow(3, BitTape([3, 2])), 2)
        self.assertFalse(e.coin(0, 1, BitTape([])))
        self.assertTrue(e.coin(1, 1, BitTape([])))

    def test_all_zero_one_boards_through_three(self):
        for n in range(4):
            for b in itertools.product(range(1 << n), repeat=n):
                rows = [r for r in itertools.permutations(range(n))
                        if all(q & (1 << x) for q, x in zip(b, r))]
                self.assertEqual(e.permanent(b), len(rows))
                self.assertEqual(list(e.matchings(b)), rows)
                self.assertEqual([e.unrank_matching(b, i) for i in range(len(rows))], rows)
                if not rows:
                    with self.assertRaises(ValueError):
                        e.sample_matching(b)

    def test_reduced_table_and_labels(self):
        counts = (1, 1, 1, 4, 56, 9408, 16942080)
        for n, known in enumerate(counts, 1):
            s = e.ReducedSpace(n)
            self.assertEqual(s.reduced_count, known)
            self.assertEqual(s.labeled_count, known*factorial(n)*factorial(n-1))
            for i in {0,s.reduced_count//2,s.reduced_count-1}:
                L = s.unrank_reduced(i)
                self.assertTrue(e.is_latin(L))
                self.assertEqual(L[0], tuple(range(n)))
                self.assertEqual(tuple(row[0] for row in L), tuple(range(n)))

    def test_unranking_bijection_all_labeled_through_four(self):
        for n in range(1,5):
            s = e.ReducedSpace(n)
            targets = set(e.iter_latin(n))
            byrank = {s.unrank(i) for i in range(s.labeled_count)}
            self.assertEqual(byrank, targets)
            self.assertEqual(len(byrank), s.labeled_count)
            for i in range(s.labeled_count):
                self.assertEqual(s.sample(BitTape([i])), s.unrank(i))

    def test_all_small_rejection_atoms(self):
        for n in range(1,5):
            bound = prod(e.row_envelope(n,d) for d in range(1,n+1))
            for sq in e.iter_latin(n):
                board, p = e.full_board(n), Fraction(1)
                for i,row in enumerate(sq):
                    m = e.permanent(board)
                    cap = e.row_envelope(n,n-i)
                    self.assertLessEqual(m,cap)
                    p *= Fraction(m,cap)*Fraction(1,m)
                    board = e.delete_matching(board,row)
                self.assertEqual(p,Fraction(1,bound))

    def test_generated_rejection_and_validation(self):
        for n in range(1,8):
            self.assertTrue(e.is_latin(e.sample_latin(n,random.Random(92+n),method="rejection")))
        for bad in (-1,0,2.5,True):
            with self.assertRaises(ValueError): e.sample_latin(bad)
        for bad in ((-1,), (2,), (1,4)):
            with self.assertRaises(ValueError): e.permanent(bad)
        for row in ((0,0),(4,1),(-1,1),(0,)):
            with self.assertRaises(ValueError): e.delete_matching((3,3),row)
        self.assertFalse(e.is_latin(((False,),)))
        self.assertFalse(e.is_latin(((0,1),(0,1))))


if __name__ == "__main__":
    unittest.main()
