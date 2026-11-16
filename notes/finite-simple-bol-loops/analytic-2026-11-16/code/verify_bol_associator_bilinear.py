#!/usr/bin/env python3
"""Authored exact checks for the intrinsic associator spectral proof.

No other verifier is imported.  Finite enumeration supports, but does not
replace, the all-parameter alternating-sum and ring-conductor proofs.
"""

from fractions import Fraction
from itertools import product
from math import gcd
import json


def rank_mod(matrix, p=3):
    a = [row[:] for row in matrix]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][col], -1, p)
        a[rank] = [x * inverse % p for x in a[rank]]
        for i in range(len(a)):
            if i != rank:
                factor = a[i][col]
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def cross(a):
    x, y, z = a
    return [[0, -z % 3, y], [z, 0, -x % 3], [-y % 3, x, 0]]


def cyclotomic_reduction(counts, prime, level):
    """Exact reduction modulo Phi_(prime^level), without approximate roots."""
    m = prime**level
    step = m // prime
    out = counts[:]
    for residue in range(step):
        top = out[(prime - 1) * step + residue]
        for j in range(prime - 1):
            out[j * step + residue] -= top
    return out[: (prime - 1) * step]


def check_value(counts, denominator, expected, prime, level):
    reduced = cyclotomic_reduction(counts, prime, level)
    assert not any(reduced[1:]), (prime, level, reduced, expected)
    assert Fraction(reduced[0], denominator) == expected


def check_alternating_sums():
    vectors = list(product(range(3), repeat=3))
    checks = 0
    compatible = 0
    incompatible = 0
    for alpha in vectors:
        b = cross(alpha)
        rank = rank_mod(b)
        phase = [[sum(u[i] * b[i][j] * v[j]
                      for i in range(3) for j in range(3)) % 3
                  for v in vectors] for u in vectors]
        for w in vectors:
            membership = rank_mod([row + [wi] for row, wi in zip(b, w)]) == rank
            compatible += membership
            incompatible += not membership
            dot = [sum(x * y for x, y in zip(u, w)) % 3 for u in vectors]
            for a, aa in product(range(3), repeat=2):
                counts = [0] * 3
                for i in range(27):
                    for j in range(27):
                        counts[(phase[i][j] + a * dot[i] + aa * dot[j]) % 3] += 1
                expected = Fraction(1, 3**rank) if membership or (a == aa == 0) else Fraction(0)
                check_value(counts, 27**2, expected, 3, 1)
                checks += 1
    return {"all_cross_pencil_labels": 27, "all_linear_vectors": 27,
            "all_scalar_coefficient_pairs": 9, "exact_sums": checks,
            "compatible_label_vector_pairs": compatible,
            "incompatible_label_vector_pairs": incompatible,
            "terms_per_sum": 729}


def circular_convolution(a, b):
    m = len(a)
    out = [0] * m
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[(i + j) % m] += x * y
    return out


def scalar_pair_histogram(m, quadratic, linear_x, linear_y):
    counts = [0] * m
    for x in range(m):
        for y in range(m):
            counts[(quadratic * x * y + linear_x * x + linear_y * y) % m] += 1
    return counts


def plane_average_histogram(m, eta, sigma, rho, z, acting=0):
    """Enumerate actual four-variable phase through independent coordinate pairs."""
    counts = [0] * m
    z0, z1 = z
    for c, d in product(range(3), repeat=2):
        a = (pow(eta, acting, m) - pow(eta, d, m)) % m
        aa = (pow(eta, (c + acting) % 3, m) - 1) % m
        assert a == 0 or gcd(a, m) == 1
        assert aa == 0 or gcd(aa, m) == 1
        first = scalar_pair_histogram(m, sigma, rho * a * z1, -rho * aa * z0)
        second = scalar_pair_histogram(m, -sigma, -rho * a * z0, rho * aa * z1)
        actual = circular_convolution(first, second)
        counts = [x + y for x, y in zip(counts, actual)]
    assert sum(counts) == 9 * m**4
    return counts


def check_ring_planes():
    result = []
    for level in (1, 2):
        m = 7**level
        eta = 2 if level == 1 else 30
        labels = range(7) if level == 1 else (0, 1, 7, 14, 35)
        central = range(7) if level == 1 else (0, 1, 7, 14, 42)
        vectors = [(0, 0), (1, 0), (1, 2)] if level == 1 else [(0, 0), (1, 0), (7, 0), (7, 14), (1, 7)]
        checks = 0
        counts_by_bad = [0, 0]
        conductor_counts = {}
        for sigma, rho, z in product(labels, central, vectors):
            divisor = gcd(sigma, m)
            bad = any((rho * x) % divisor for x in z)
            expected = Fraction(divisor**2, m**2) / (9 if bad else 1)
            counts = plane_average_histogram(m, eta, sigma, rho, z)
            check_value(counts, 9 * m**4, expected, 7, level)
            counts_by_bad[bool(bad)] += 1
            conductor = m // divisor
            conductor_counts[conductor] = conductor_counts.get(conductor, 0) + 1
            checks += 1
        # Acting labels do not alter the averaged coefficient. Test each label,
        # including the exact sharp 1/9 eigenmode and imprimitive edge cases.
        for acting in range(3):
            for sigma, rho, z in [(0, 1, (1, 0)), (m // 7, 1, (1, 0)), (m // 7, m // 7, (1, 0))]:
                divisor = gcd(sigma, m)
                bad = any((rho * x) % divisor for x in z)
                expected = Fraction(divisor**2, m**2) / (9 if bad else 1)
                counts = plane_average_histogram(m, eta, sigma, rho, z, acting)
                check_value(counts, 9 * m**4, expected, 7, level)
                checks += 1
        result.append({"modulus": m, "eta": eta, "exact_plane_averages": checks,
                       "compatible_incompatible_cases": counts_by_bad,
                       "conductor_counts": conductor_counts,
                       "represented_terms_per_average": 9 * m**4,
                       "enumerated_scalar_pairs_per_average": 18 * m**2,
                       "sharp_eigenvalue": "1/9"})
    return result


def main():
    print(json.dumps({"status": "passed", "arithmetic": "exact integer cyclotomic reduction and rational arithmetic",
                      "alternating_sums": check_alternating_sums(),
                      "ring_planes": check_ring_planes(),
                      "scope": "Finite bilinear identities and conductor factors; no full reciprocal-loop matrix enumeration."},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

