#!/usr/bin/env python3
"""Exact finite arithmetic for the linear extension/vector-parabolic orientation.

Python 3.11+, standard library, assertions enabled, no file I/O.
The manuscript owns the analytic tail, group normalizers and fiber proof.
No subgroup census or loop existence assertion is made here.
"""
from math import gcd, isqrt, prod

assert __debug__, 'Run with assertions enabled'


def gl(d, q):
    return prod(q**d-q**i for i in range(d))


def prime_power(q):
    for p in range(2, q+1):
        if any(p % d == 0 for d in range(2, isqrt(p)+1)):
            continue
        z, f = 1, 0
        while z < q:
            z *= p
            f += 1
        if z == q:
            return p, f
    return None


def divide(a, b):
    assert a % b == 0
    return a // b


def weighted_capacity(m, q, p, f):
    ambient = gl(m, q)
    if p == 2:
        result = sum(divide(ambient, q**(r*(2*m-3*r))*gl(r, q)*gl(m-2*r, q))
                     * q**(m-r) for r in range(m//2+1))
    else:
        result = sum(divide(ambient, gl(r, q)*gl(m-r, q))*q**r
                     for r in range(m+1))
    if f % 2 == 0:
        s = isqrt(q)
        assert s*s == q
        result += divide(ambient, gl(m, s))*s**m
    return result


bounds = {2:385, 3:26, 4:11, 5:8, 6:6, 7:3, 8:3,
          9:2, 10:2, 11:2, 12:2, 13:2}
expected = {(2,2),(2,3),(2,4),(2,5),(2,9),(3,2),(3,3),(3,4),(4,2)}
found = set()
for a, bound in bounds.items():
    # Monotonicity then proves the stated analytic inequality above this bound.
    assert bound*(bound+1)**(a-2) > 192*a
    for q in range(2, bound+1):
        field = prime_power(q)
        if field is None:
            continue
        p, f = field
        n, m = 2*a, 2*a-1
        socle = divide(divide(gl(n, q), q-1), gcd(n, q-1))
        normalizer_upper = divide(4*f*gl(a, q*q), q-1)
        capacity = weighted_capacity(m, q, p, f)
        if socle <= normalizer_upper*capacity:
            found.add((a, q))
assert found == expected, (found, expected)
assert 2**13 > 384*14
print('b=2 analytic-bound finite residual: nine pairs')

# Use the original Y-intersection index for seven residuals, without outer loss.
for a, q, p, f in ((2,3,3,1),(2,4,2,2),(2,5,5,1),(2,9,3,2),
                   (3,3,3,1),(3,4,2,2),(4,2,2,1)):
    m = 2*a-1
    y_order = divide(q**m*gl(m, q), q-1)
    j_order = divide(2*gl(a, q*q), (q-1)*(q**(2*a)-1))
    capacity = weighted_capacity(m, q, p, f)
    assert y_order > j_order*capacity, (a, q)
print('seven refined actual-intersection inequalities pass')

# The only small b>=3 boundary in the analytic proof is n=6,b=3,q=2.
socle = gl(6, 2)
normalizer_upper = 6*gl(2, 8)
capacity = weighted_capacity(5, 2, 2, 1)
assert capacity == 59552
assert socle > normalizer_upper*capacity
assert divide(socle, normalizer_upper) == 952320
print('n=6,b=3,q=2: capacity 59552 < required degree 952320')
print('PASS: remaining (a,q)=(2,2),(3,2) use the written A8/affine proofs')
