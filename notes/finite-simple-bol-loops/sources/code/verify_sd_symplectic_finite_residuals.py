#!/usr/bin/env python3
"""Check the arithmetic in sd-symplectic-finite-residuals.md, not its sources."""
from math import isqrt

for q, f in [(5, 1), (7, 1), (8, 3), (9, 2), (16, 4), (32, 5)]:
    even = q % 2 == 0
    n = q**4 * (q**2 - 1) * (q**4 - 1) // (1 if even else 2)
    a = 2 * f * n
    if even:
        if f % 2:
            c = q**2 * (q**2 + 1) * (q - 1)
        else:
            s = isqrt(q)
            assert s * s == q
            c = s**4 * (s**2 - 1) * (s**4 - 1)
        assert n % c == 0
        b = q**6 + q**4 - q**2 + n // c
    else:
        b = 1 + q**4 * (q**2 + 2)
        if f == 2:
            assert (2 * n) % 51840 == 0
            b += (2 * n) // 51840
    assert n >= 2**20
    assert b**3 + 3 * a * b < n**2
    print(f"PSp4({q}): n={n}, a={a}, b={b}")

n = a = 1451520
centralizers = (23040, 4608, 1536, 384)
assert all(n % c == 0 for c in centralizers)
classes = tuple(n // c for c in centralizers)
assert classes == (63, 315, 945, 3780)
b = 1 + sum(classes)
assert b == 5104 and n >= 2**20
assert b**3 + 3 * a * b == 155189039104
assert n**2 == 2106910310400
assert b**3 + 3 * a * b < n**2
print(f"PSp6(2): n={n}, a={a}, b={b}, classes={classes}")
print("symplectic finite residual checks passed")
