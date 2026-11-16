#!/usr/bin/env python3
"""Fixed field, Fourier-minor and line-orbit controls; Python 3.11+."""
from itertools import product

from verify_odd_heisenberg_control import (
    ZERO, ONE, ZETA, ZETA_POWERS, add, neg, field_mul, field_pow,
    basis_vector, rho, sigma,
)

assert __debug__


def sub(a, b):
    return add(a, neg(b))


def total(items):
    result = ZERO
    for item in items:
        result = add(result, item)
    return result


def determinant(matrix):
    # Three-dimensional determinant over E; no division is needed.
    a, b, c = matrix
    return add(add(field_mul(a[0], sub(field_mul(b[1], c[2]), field_mul(b[2], c[1]))),
                   neg(field_mul(a[1], sub(field_mul(b[0], c[2]), field_mul(b[2], c[0]))))),
               field_mul(a[2], sub(field_mul(b[0], c[1]), field_mul(b[1], c[0]))))


def field_and_fourier():
    residues = (1, 2, 4)
    nonresidues = (3, 5, 6)
    s = total(ZETA_POWERS[j] for j in residues)
    t = total(ZETA_POWERS[j] for j in nonresidues)
    assert add(s, t) == neg(ONE)
    assert field_mul(s, t) == neg(ONE)
    assert total((s, s, s)) == ZERO
    minor = [[ZETA_POWERS[i*j % 7] for j in residues] for i in nonresidues]
    assert determinant(minor) == s != ZERO
    for v in range(7):
        rows = [(v+i) % 7 for i in nonresidues]
        cols = [(v+j) % 7 for j in residues]
        shifted = [[ZETA_POWERS[i*j % 7] for j in cols] for i in rows]
        assert determinant(shifted) == field_mul(ZETA_POWERS[3*v*v % 7], s)
        coeffs = [field_mul(s, ZETA_POWERS[-v*j % 7]) for j in residues]
        for i in rows:
            expression = add(ZETA_POWERS[i*v % 7],
                             total(field_mul(ZETA_POWERS[i*(v+j) % 7], c)
                                   for j, c in zip(residues, coeffs)))
            assert expression == ZERO
        multiplier = add(ZETA_POWERS[v*v % 7],
                         total(field_mul(ZETA_POWERS[v*(v+j) % 7], c)
                               for j, c in zip(residues, coeffs)))
        assert multiplier == ZETA_POWERS[v*v % 7]
    print('Fourier: Gaussian periods, nonzero minors and all 7 shifted kernels verified')


def line_orbits():
    elements = list(product(range(3), repeat=6))
    fixed = [x for x in elements if field_pow(x, 27) == x]
    assert len(fixed) == 27
    unseen = set(elements) - {ZERO}
    lines = set()
    while unseen:
        representative = next(iter(unseen))
        line = frozenset(field_mul(representative, x) for x in fixed)
        assert len(line) == 27 and ZERO in line
        lines.add(line)
        unseen.difference_update(line)
    assert len(lines) == 28
    xi = sub(ZETA, ZETA_POWERS[6])
    assert field_pow(xi, 27) == neg(xi) and xi != ZERO
    bad = {frozenset(field_mul(field_mul(xi, ZETA_POWERS[j]), x) for x in fixed)
           for j in range(7)}
    assert len(bad) == 7 and bad <= lines
    allowed = lines - bad
    assert len(allowed) == 21
    remaining = set(allowed)
    lengths = []
    while remaining:
        line = next(iter(remaining))
        orbit = set()
        while line not in orbit:
            orbit.add(line)
            line = frozenset(field_pow(x, 9) for x in line)
        assert orbit <= allowed
        remaining.difference_update(orbit)
        lengths.append(len(orbit))
    assert sorted(lengths) == [1, 1, 1, 3, 3, 3, 3, 3, 3]
    print('lines: 28 total, 7 bad, 21 allowed, Frobenius² orbit sizes 1,1,1,3,3,3,3,3,3')


def phi(v, k, r):
    out = [ZERO] * 7
    for j in range(7):
        out[r*j % 7] = field_pow(v[j], 3**k)
    return out


def automorphism_controls():
    generators = [(1, 0, 0, 0), (0, 1, 0, 0),
                  (0, 0, 1, 0), (0, 0, 0, 1)]
    for k, r in ((0, 1), (2, 4), (4, 2)):
        assert r*r % 7 == pow(3, k, 7)
        images = [(r, 0, 0, 0), (0, r, 0, 0),
                  (0, 0, r*r % 7, 0), (0, 0, 0, 1)]
        for i in range(42):
            v = basis_vector(i)
            assert phi(sigma(v), k, r) == sigma(phi(v, k, r))
            for g, target in zip(generators, images):
                assert phi(rho(v, g), k, r) == rho(phi(v, k, r), target)
    print('automorphisms: all three basis-level action and sigma identities verified')


if __name__ == '__main__':
    field_and_fourier()
    line_orbits()
    automorphism_controls()
