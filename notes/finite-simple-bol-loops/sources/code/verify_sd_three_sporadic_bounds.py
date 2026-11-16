#!/usr/bin/env python3
"""Exact arithmetic only; source tables and group theory are not checked here."""
from math import isqrt

rows = [
    ('M11', 7920, 7920, 587, 7),
    ('M22', 443520, 887040, 16713, 13),
    ('J1', 175560, 175560, 5292, 13),
]
for name, n, a, B, r in rows:
    assert r > 2 and all(r % d for d in range(2, isqrt(r) + 1))
    assert n % r
    assert (B - 1)**100 < a**71 <= B**100
    assert a <= B*B and 2*B < n
    N, K = 25, 2*r - 1
    assert 2*N*(2*B)**(N-1) < n**(N-1)
    assert 2*B*(N+1) <= n*N
    F, E = [1, B], [1, B-1]
    for k in range(2, max(K, N-1)+1):
        F.append(B*F[-1]+(k-1)*a*F[-2])
        E.append((B-1)*E[-1]+(k-1)*a*E[-2])
    assert all(F[k]-E[k] < n**(k-1) for k in range(3, len(F)))
    assert K*F[K-1] < n**(K-1)
    print(f'{name}: passed; B={B}, r={r}, N={N}, K={K}')
