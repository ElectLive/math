#!/usr/bin/env python3
"""Check finite arithmetic in the alternating-socle SD candidate.

This uses exact integers; it does not validate the group theory or folder assumptions.
"""

from math import factorial, isqrt


def prime(p):
    return p >= 2 and all(p % j for j in range(2, isqrt(p) + 1))


def main():
    involutions = [1, 1]
    for m in range(2, 16):
        involutions.append(involutions[-1] + (m - 1) * involutions[-2])
    for m in (14, 15):
        assert 2 * m**3 * involutions[m] <= factorial(m)
    assert factorial(14) // 2 >= 2 * 14**6
    for m in range(7, 14):
        n = factorial(m) // 2
        a, b = 2 * n, involutions[m]
        r = next(p for p in range(m + 1, 2 * m) if prime(p))
        cutoff = 2 * r - 1
        limit = max(cutoff, 24)
        f, g = [1, b], [1, b - 1]
        for k in range(2, limit + 1):
            f.append(b * f[-1] + (k - 1) * a * f[-2])
            g.append((b - 1) * g[-1] + (k - 1) * a * g[-2])
        assert all(f[k] - g[k] < n ** (k - 1) for k in range(3, limit + 1)), m
        assert cutoff * f[cutoff - 1] < n ** (cutoff - 1), m
        assert b * b >= a and 2 * b < n, m
        assert 50 * (2 * b)**24 < n**24, m
        assert 52 * b <= 25 * n, m
    print("alternating-socle arithmetic checks passed")


if __name__ == "__main__":
    main()
