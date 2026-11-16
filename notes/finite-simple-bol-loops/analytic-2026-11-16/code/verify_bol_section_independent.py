#!/usr/bin/env python3
"""Independent read-only checks for the Bol-section review.

Constructs original-coordinate left-translation matrices/path counts. This
script was independently written by /root/independent_review, not copied from
the authored research verifiers. Proofs remain the mathematical basis.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
import json
import numpy as np


def finite_case(q, m, eta, d):
    xs = list(product(range(q), repeat=d))
    r = (1,) + (0,) * (d - 1)
    states = [(x, a, s) for x in xs for a in range(m) for s in range(q)]
    index = {z: i for i, z in enumerate(states)}
    n, degree = len(states), m * q**d
    matrix = np.zeros((n, n), dtype=np.int64)
    for i, (x, a, s) in enumerate(states):
        y = tuple(pow(eta, a, q) * v % q for v in r)
        for t in range(m):
            scalar = pow(eta, t, q)
            for u in xs:
                target = (tuple((ui + scalar * xi) % q for ui, xi in zip(u, x)),
                          (a + t) % m,
                          (s - sum(ui * yi for ui, yi in zip(u, y))) % q)
                matrix[i, index[target]] += 1
    assert np.array_equal(matrix, matrix.T)
    assert np.all(matrix.sum(axis=0) == degree)
    assert np.array_equal(matrix @ matrix @ matrix,
                          q**(2*d) * matrix +
                          (m*m - 1) * q**(2*d-1) * np.ones_like(matrix))
    row = np.zeros(n, dtype=np.int64)
    row[0] = 1
    distances = []
    for step in range(1, 7):
        row = row @ matrix
        den = degree**step
        actual = sum(Fraction(abs(int(v)*n - den), 2*den*n) for v in row)
        expected = Fraction(q-1, q*m**(step-1))
        if step % 2 == 0:
            expected *= Fraction(q-m+1, q)
        assert actual == expected
        distances.append(str(actual))
    return dict(q=q, m=m, eta=eta, d=d, states=n, degree=degree,
                total_variation=distances, integer_cubic=True)


def ring_paths(n, units, d=1):
    xs = list(product(range(n), repeat=d))
    first = [(x, b, -x[0] % n) for b in units for x in xs]
    counts = Counter()
    for x, b, s in first:
        for a in units:
            for u in xs:
                target = (tuple((u[i]+a*x[i]) % n for i in range(d)),
                          a*b % n, (s-u[0]*b) % n)
                counts[target] += 1
    degree = len(units)*n**d
    size = len(units)*n**(d+1)
    den = degree**2
    numerator = sum(abs(v*size-den) for v in counts.values())
    numerator += (size-len(counts))*den
    return Fraction(numerator, 2*den*size), den


def arithmetic_cases():
    all_unit, teich = [], []
    for p, depth, d in [(3,1,1), (3,2,1), (3,2,2), (3,3,1), (5,2,1)]:
        n = p**depth
        units = [u for u in range(n) if gcd(u,n) == 1]
        actual, paths = ring_paths(n, units, d)
        expected = Fraction(2*p, p**3-1)*(1-Fraction(1,p**(3*depth)))
        assert actual == expected
        all_unit.append(dict(p=p, depth=depth, d=d, paths=paths, tv2=str(actual)))
    for n, m, eta in [(9,2,8), (25,4,7), (49,3,30), (49,6,19)]:
        units = sorted({pow(eta,j,n) for j in range(m)})
        assert len(units) == m
        actual, paths = ring_paths(n,units)
        assert actual == Fraction((n-1)*(n-m+1),m*n*n)
        teich.append(dict(n=n, m=m, eta=eta, paths=paths, tv2=str(actual)))
    return dict(all_units=all_unit, teichmuller=teich)


def conductor_matrix():
    n = 9
    units = [a for a in range(n) if gcd(a,n) == 1]
    states = [(x,b,s) for x in range(n) for b in units for s in range(n)]
    index = {z:i for i,z in enumerate(states)}
    matrix = np.zeros((len(states),len(states)),dtype=np.int64)
    for i,(x,b,s) in enumerate(states):
        for a in units:
            for u in range(n):
                matrix[i,index[((u+a*x)%n,a*b%n,(s-u*b)%n)]] += 1
    assert np.array_equal(matrix,matrix.T)
    powers = {1:matrix}
    for j in range(2,7):
        powers[j] = powers[j-1] @ matrix
    # Degree54, so even the sum of absolute row bounds in this polynomial
    # is below 10^11. All integer arithmetic is safe in int64.
    polynomial = (powers[6]-54*powers[5]-810*powers[4]+43740*powers[3]
                  +59049*powers[2]-3188646*matrix)
    assert not np.any(polynomial)
    multiplicities = {54:1,27:6,-27:2,9:126,-9:90,0:261}
    for j in range(1,7):
        assert int(np.trace(powers[j])) == sum(k**j*v for k,v in multiplicities.items())
    return dict(ring="Z/9", states=len(states), degree=54,
                annihilating_polynomial="K(K-54I)(K^2-729I)(K^2-81I)=0",
                moments=6, multiplicities=multiplicities)


if __name__ == "__main__":
    print(json.dumps(dict(
        finite=[finite_case(*a) for a in [(3,2,2,1),(3,2,2,2),
                 (5,2,4,1),(5,4,2,1),(7,3,2,1),(7,6,3,1)]],
        arithmetic=arithmetic_cases(), conductor=conductor_matrix(),
        status="PASS"),sort_keys=True,separators=(",",":")))

