#!/usr/bin/env python3
"""Check the refined screen on the residuals of the earlier classical screen.

This verifies finite rational arithmetic only, not source theorems or the
completeness of the inherited parameter grids and tail arguments.
"""
from fractions import Fraction
from math import gcd, isqrt, prod

LINEAR = {4: (3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 25, 27, 29, 49),
          5: (2, 3, 4), 6: (2,), 7: ()}
UNITARY = {4: (3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 31),
           5: (2, 3, 4), 6: (2,), 7: ()}
EXPECTED_LINEAR = {(4, 3), (4, 4), (4, 5), (4, 9)}
EXPECTED_UNITARY = {(4, 3), (4, 4), (4, 5), (4, 7), (4, 8),
                    (5, 2), (5, 4), (6, 2)}


def is_prime(p):
    return p >= 2 and all(p % i for i in range(2, isqrt(p) + 1))


def prime_power_exponent(q):
    candidates = []
    for p in range(2, q + 1):
        if not is_prime(p):
            continue
        remaining, f = q, 0
        while remaining % p == 0:
            remaining //= p
            f += 1
        if f and remaining == 1:
            assert p ** f == q
            candidates.append(f)
    assert len(candidates) == 1, f"{q} is not a prime power"
    return candidates[0]


def sufficient(d, q, unitary):
    f = prime_power_exponent(q)
    g = gcd(d, q + 1 if unitary else q - 1)
    t, r = 2 * f * g, d - 1
    numerator = q ** (d * (d - 1) // 2) * prod(
        q ** i - ((-1) ** i if unitary else 1) for i in range(2, d + 1))
    assert numerator % g == 0
    n = numerator // g
    assert n >= 2 ** 20
    C = min(Fraction(100), t * (Fraction(413, 50) if unitary else Fraction(5, 2)))
    if not unitary:
        C = min(C, Fraction(t * (q + 5), q * g))
    elif q > 2:
        C = min(C, Fraction(t * (q + 8), q * g))
    return Fraction(n) > t ** 3 * q ** (3 * r) * C * (C + Fraction(3, q ** r)) ** 2


def failures(grid, unitary):
    return {(d, q) for d, qs in grid.items() for q in qs if not sufficient(d, q, unitary)}


assert failures(LINEAR, False) == EXPECTED_LINEAR
assert failures(UNITARY, True) == EXPECTED_UNITARY
print('refined linear and unitary residual arithmetic passed')
