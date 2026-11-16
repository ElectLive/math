#!/usr/bin/env python3
"""Exact finite R-screen arithmetic; no group-theory source is executed."""
from math import gcd, isqrt

LIMIT = 1030**2


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def powers_below(limit):
    values = []
    for p in range(2, limit):
        if prime(p):
            q, f = p, 1
            while q < limit:
                values.append((q, f))
                q, f = q*p, f+1
    assert len(values) == len({q for q, _ in values})
    return sorted(values)


def rank_linear(d, q, f, unitary=False):
    g = gcd(d, q+1 if unitary else q-1)
    n = q**(d*(d-1)//2)
    for i in range(2,d+1):
        n *= q**i - ((-1)**i if unitary else 1)
    assert n % g == 0
    return n//g, 2*f*g


def rank_symplectic(r, q, f):
    g = gcd(2,q-1)
    n = q**(r*r)
    for i in range(1,r+1):
        n *= q**(2*i)-1
    assert n % g == 0
    return n//g, 2*f if r == 2 else g*f


def fails(n,t,q,r):
    return n >= 2**20 and n <= LIMIT*t**3*q**(3*r)

linear_expected = {
    4:[3,4,5,7,8,9,11,13,16,17,19,25,27,29,49],
    5:[2,3,4], 6:[2], 7:[]
}
for d in range(4,8):
    actual = []
    for q,f in powers_below(256):
        n,t = rank_linear(d,q,f)
        if fails(n,t,q,d-1):
            actual.append(q)
    assert actual == linear_expected[d], (d, actual)
assert 2**42 > LIMIT*32*8**4
assert 256**6 > LIMIT*32*4**4*8**3

unitary_expected = {
    4:[3,4,5,7,8,9,11,13,16,17,19,23,25,27,31],
    5:[2,3,4], 6:[2], 7:[]
}
for d in range(4,8):
    actual = []
    for q,f in powers_below(128):
        n,t = rank_linear(d,q,f,unitary=True)
        if fails(n,t,q,d-1):
            actual.append(q)
    assert actual == unitary_expected[d], (d, actual)
assert 2**42 > LIMIT*12*8**4
assert 128**6 > LIMIT*12*4**4*7**3

symplectic_expected = {
    2:[5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53,59,61,64,81,125,128,256],
    3:[2,3], 4:[]
}
for r in (2,3,4):
    actual = []
    for q,f in powers_below(1024):
        if (r == 3 and q >= 7) or (r == 4 and q >= 3):
            continue
        n,t = rank_symplectic(r,q,f)
        if fails(n,t,q,r):
            actual.append(q)
    assert actual == symplectic_expected[r], (r, actual)
# The tail bound does not cover (r,q)=(4,2), so check it exactly.
n,t = rank_symplectic(4,2,1)
assert n >= 2**20 and n > LIMIT*t**3*2**12
# Conservative endpoint bounds use log2(q) <= the displayed integer.
assert 2**40 > LIMIT*24
assert 3**24 > LIMIT*24*2**3
assert 7**12 > LIMIT*24*3**3
assert 1024**4 > LIMIT*24*10**3
print('classical R-screen arithmetic passed')
