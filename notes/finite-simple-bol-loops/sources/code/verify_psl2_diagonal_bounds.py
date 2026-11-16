#!/usr/bin/env python3
"""Exact finite inequalities for manuscripts/sd-psl2-all-factors.md.

Deterministic integer arithmetic only. This does not establish the counting
lemma, group formulas, infinite bounds or folder reduction.
"""
from math import gcd, isqrt

def prime(x):
    return x >= 2 and all(x % z for z in range(2, isqrt(x)+1))

qs = []
for p in range(2, 32):
    if prime(p):
        q, f = p, 1
        while q < 32:
            if q >= 7:
                qs.append((q, f))
            q, f = q*p, f+1
assert sorted(q for q,f in qs) == [7,8,9,11,13,16,17,19,23,25,27,29,31]
for q, f in qs:
    d = gcd(2, q-1)
    n = q*(q*q-1)//d
    a = d*f*n
    b = q*q-(2-d)+1 + (isqrt(q)*(q+1) if f%2 == 0 else 0)
    if f%2 == 0:
        assert isqrt(q)**2 == q
    r = next(x for x in range(q+2, 2*q+2) if prime(x))
    K = 2*r-1
    F, E = [1,b], [1,b-1]
    for k in range(2, max(K,24)+1):
        F.append(b*F[-1] + (k-1)*a*F[-2])
        E.append((b-1)*E[-1] + (k-1)*a*E[-2])
    assert all(F[k]-E[k] < n**(k-1) for k in range(3,max(K,24)+1)), (q,f)
    assert K*F[K-1] < n**(K-1), (q,f)
assert 50*2**24 < 3**24
print('passed')
