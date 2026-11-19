"""Exact constant-gap doubling, for an iid p-coin with p<=1/5.

Huber (2016), arXiv:1308.1562 §2, with threshold 32 at the first
level, doubled thereafter. Only rational comparisons and fair bits.
No target probability or approximation to that probability is needed.
"""
from fractions import Fraction


def uniform_below(n, randbits):
    if n < 1:
        raise ValueError("positive denominator required")
    if n == 1:
        return 0
    bits = (n - 1).bit_length()
    while True:
        u = randbits(bits)
        if u < n:
            return u


def _coin(num, den, randbits):
    return uniform_below(den, randbits) < num


def double_low(pcoin, randbits):
    """Return a bool whose mean is exactly twice the input-coin bias.

    pcoin(), randbits(k) must give mutually independent fresh random bits
    from their stipulated distributions; pcoin's bias must be <=1/5.
    """
    C, eps = Fraction(2), Fraction(1, 2)
    k, i = 32, 1
    while True:
        while 0 < i < k:
            if pcoin():
                i -= 1
            else:
                # Add G−1 for G geometric((C−1)/C), supported on 1,2,...
                num, den = C.numerator - C.denominator, C.numerator
                while not _coin(num, den, randbits):
                    i += 1
        if i == 0:
            return True
        mult = 1 + eps / 2
        # Identical to Bern(mult**(-i)), avoiding a huge power.
        for _ in range(i):
            if not _coin(mult.denominator, mult.numerator, randbits):
                return False
        C *= mult
        eps /= 2
        k *= 2
