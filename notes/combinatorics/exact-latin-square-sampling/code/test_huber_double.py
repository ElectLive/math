"""Small deterministic checks for rational-only constant-gap doubling."""
import random
import unittest
from huber_double import double_low, uniform_below

class HuberTests(unittest.TestCase):
    def test_zero(self):
        rng = random.Random(7)
        self.assertFalse(any(double_low(lambda: False, rng.getrandbits) for _ in range(100)))

    def test_one_fifth_smoke(self):
        # A seeded smoke check, not a proof of the exact distribution.
        rng = random.Random(771)
        count = sum(double_low(lambda: rng.randrange(5) == 0, rng.getrandbits)
                    for _ in range(10000))
        self.assertTrue(3700 <= count <= 4300)

    def test_uniform_one(self):
        self.assertEqual(uniform_below(1, lambda _: self.fail("unexpected bit read")), 0)

if __name__ == "__main__":
    unittest.main()
