#!/usr/bin/env python3
"""Exact arithmetic only; group-theoretic hypotheses are not checked here."""
from fractions import Fraction
from math import gcd, isqrt


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


values = []
for p in range(2, 1024):
    if prime(p):
        q, f = p, 1
        while q < 1024:
            values.append((q, f))
            q, f = q * p, f + 1
assert len(values) == len(set(q for q, f in values))
expected = {2: [5, 7, 8, 9, 16, 32], 3: [2], 4: []}
below = {2: [3, 4], 3: [], 4: []}
for r in (2, 3, 4):
    bad, small = [], []
    for q, f in sorted(values):
        if (r == 3 and q >= 7) or (r == 4 and q >= 3):
            continue
        if r == 2 and q == 2:  # PSp_4(2) is not simple.
            continue
        g = gcd(2, q - 1)
        num = q ** (r * r)
        for i in range(1, r + 1):
            num *= q ** (2 * i) - 1
        assert num % g == 0
        n = num // g
        t = 2 * f if r == 2 else g * f
        if q == 2:
            bound = Fraction(76 * t, 5)
        elif q == 3:
            bound = Fraction(54 * t, 5)
        elif q % 2:
            bound = Fraction(t * (q + 12), q)
        else:
            bound = Fraction(t * (q + 5), q)
        C = min(Fraction(100), bound)
        Q = q ** r
        threshold = t**3 * Q**3 * C * (C + Fraction(3, Q))**2
        if n < 2**20:
            small.append(q)
        elif n <= threshold:
            bad.append(q)
    assert bad == expected[r], (r, bad)
    assert small == below[r], (r, small)
for r, q in ((2, 1024), (3, 7), (4, 3), (5, 2)):
    E = 2 * r * (r - 1)
    assert q ** (2 * E - 3) > (24 * 1030**2)**2
assert 8**12 > 24 * 27 * 1030**2
print('refined symplectic screen passed')
