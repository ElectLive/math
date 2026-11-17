#!/usr/bin/env python3
"""Exact small checks for the hyperbolic Weil vacuum packet.

Python 3.11+, standard library only. No floating point, network or files written.
This is verification evidence for finite algebra, not a proof of modularity.
"""
from fractions import Fraction
from itertools import product


def vectors(p, r):
    return list(product(range(p), repeat=r))


def add_scaled(a, u, b, v, p):
    return tuple((a * x + b * y) % p for x, y in zip(u, v))


def matrix_action(g, point, p):
    """J g J on columns, where g=(a,b,c,d)."""
    a, b, c, d = g
    u, v = point
    return add_scaled(d, u, c, v, p), add_scaled(b, u, a, v, p)


def multiply(g, h, p):
    a, b, c, d = g
    e, f, j, k = h
    return ((a*e+b*j) % p, (a*f+b*k) % p,
            (c*e+d*j) % p, (c*f+d*k) % p)


def finite_packet_check(p, r):
    v = vectors(p, r)
    zero = (0,) * r
    m = p ** r
    lines = [(0, 1)] + [(1, t) for t in range(p)]
    supports = [
        {(add_scaled(a, u, 0, u, p), add_scaled(b, u, 0, u, p))
         for u in v}
        for a, b in lines
    ]
    for i, x in enumerate(supports):
        assert len(x) == m
        for j, y in enumerate(supports):
            assert Fraction(len(x & y), m) == (1 if i == j else Fraction(1, m))

    group = [g for g in product(range(p), repeat=4)
             if (g[0]*g[3]-g[1]*g[2]) % p == 1]
    vacuum = {(zero, u) for u in v}
    for g in group:
        image = {matrix_action(g, x, p) for x in vacuum}
        assert image in supports
        assert Fraction(len(vacuum & image), m) == (
            1 if g[2] == 0 else Fraction(1, m))

    s, t = (0, p-1, 1, 0), (1, 1, 0, 1)
    st = multiply(s, t, p)
    sts = multiply(multiply(st, st, p), st, p)
    ss = multiply(s, s, p)
    assert sts == ss
    for point in product(v, repeat=2):
        assert matrix_action(s, matrix_action(t, point, p), p) == matrix_action(st, point, p)
        assert matrix_action(sts, point, p) == tuple(tuple((-a) % p for a in u) for u in point)

    # Gauss sum of Q(u,lambda)=lambda(u)/p is M: count powers of zeta_p.
    counts = [0] * p
    for u, lam in product(v, repeat=2):
        counts[sum(a*b for a, b in zip(u, lam)) % p] += 1
    # zeta_p^(p-1)=-sum_{j=0}^{p-2}zeta_p^j.
    reduced = [counts[j] - counts[-1] for j in range(p-1)]
    assert reduced == [m] + [0] * (p-2)
    print(f"p={p}, r={r}: |D|={m*m}, |SL2(Fp)|={len(group)}, "
          f"vacuum dimension={p+1}; exact Gram, S/T, Gauss and matrix coefficients passed")


def first_coefficient(p, r):
    return 240 * (Fraction(p**4, p**r)-1) / (p**4-1)


def rank_recovery_check():
    for p in (2, 3, 5, 7):
        for r in range(0, 13):
            a1 = first_coefficient(p, r)
            assert 1 + Fraction(p**4-1, 240) * a1 == Fraction(p**4, p**r)
    a72, a36 = first_coefficient(3, 72), first_coefficient(3, 36)
    assert a72 == -3 + Fraction(1, 3**67)
    assert a36 == -3 + Fraction(1, 3**31)
    assert a72 != a36
    print("Rigid-sector modular coefficients: rank72 = -3 + 1/3^67; rank36 = -3 + 1/3^31")


def jordan_recovery_check():
    # Actual paired Jordan blocks; tests the second-difference interface.
    for degree, blocks in ((1, [1, 1, 2, 4]), (2, [1, 3, 3]), (3, [2, 5])):
        last = max(blocks)
        ranks = [2*degree*sum(max(j-k, 0) for j in blocks) for k in range(last+2)]
        recovered = [
            (ranks[j-1]-2*ranks[j]+ranks[j+1]) // (2*degree)
            for j in range(1, last+1)
        ]
        assert recovered == [blocks.count(j) for j in range(1, last+1)]
        for r in ranks:
            a1 = first_coefficient(3, r)
            recovered_power = 1 + Fraction(3**4-1, 240) * a1
            assert recovered_power == Fraction(3**4, 3**r)
    print("Paired Jordan multiplicities recovered from three finite rank packets")


if __name__ == "__main__":
    for p, r in ((2, 1), (3, 1), (3, 2), (5, 1), (5, 2)):
        finite_packet_check(p, r)
    rank_recovery_check()
    jordan_recovery_check()
