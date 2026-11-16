#!/usr/bin/env python3
"""Verify finite SD scalar bounds; this does not verify group theory."""

rows = [
    (5616,11232,752,5),
    (20160,241920,6644,11),
    (372000,744000,14751,7),
    (6048,12096,792,5),
    (62400,249600,6793,7),
    (126000,756000,14920,11),
]
for n,a,B,r in rows:
    assert B**100 >= a**71
    assert n % r and B*B >= a and 2*B < n
    K = 2*r-1
    M = max(K,24)
    F,E = [1,B],[1,B-1]
    for k in range(2,M+1):
        F.append(B*F[-1]+(k-1)*a*F[-2])
        E.append((B-1)*E[-1]+(k-1)*a*E[-2])
    assert all(F[k]-E[k]<n**(k-1) for k in range(3,M+1))
    assert K*F[K-1]<n**(K-1)
    assert 50*(2*B)**24<n**24
    assert 2*B*26<=n*25
print('passed')
