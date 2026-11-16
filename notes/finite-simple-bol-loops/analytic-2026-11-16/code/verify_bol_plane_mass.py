#!/usr/bin/env python3
"""Exact new checks for the sharp plane-mass bound and its attainment.

Every two-dimensional
subspace of F_3^3 and F_3^5 is enumerated using unique RREF bases.
"""

import itertools
import json
from fractions import Fraction

import numpy as np

from verify_bol_coupled import (
    Extension,
    Q,
    erank,
    good_matrix,
    linear_combination,
    parameter_basis,
)


# An exact numerator a+b*sqrt(21), always with denominator 18 per factor.
WEIGHT_NUMERATORS = ((4, 0), (7, 1), (7, -1))


def quadratic_mul(x, y):
    a, b = x
    c, d = y
    return a * c + 21 * b * d, a * d + b * c


def quadratic_power(x, n):
    result = (1, 0)
    for _ in range(n):
        result = quadratic_mul(result, x)
    return result


def weight_numerator(vector):
    result = (1, 0)
    for entry in vector:
        result = quadratic_mul(result, WEIGHT_NUMERATORS[entry])
    return result


def plane_vectors(rows):
    return [
        tuple((s * x + t * y) % 3 for x, y in zip(*rows))
        for s, t in itertools.product(range(3), repeat=2)
    ]


def plane_mass_numerator(rows):
    real = radical = 0
    for vector in plane_vectors(rows):
        a, b = weight_numerator(vector)
        real += a
        radical += b
    # Negation preserves the plane and conjugates sqrt(21), so the mass
    # of every linear subspace is rational for this particular weight.
    assert radical == 0
    return real


def rref_planes(k):
    for pivots in itertools.combinations(range(k), 2):
        free_positions = [
            (i, j)
            for i, pivot in enumerate(pivots)
            for j in range(pivot + 1, k)
            if j not in pivots
        ]
        for values in itertools.product(range(3), repeat=len(free_positions)):
            rows = [[0] * k for _ in range(2)]
            for i, pivot in enumerate(pivots):
                rows[i][pivot] = 1
            for (i, j), value in zip(free_positions, values):
                rows[i][j] = value
            yield rows


def verify_plane_maximum(k):
    expected_pair = tuple(
        sum(quadratic_power(w, k - 1)[i] for w in WEIGHT_NUMERATORS)
        for i in range(2)
    )
    assert expected_pair[1] == 0
    expected_numerator = 18 * expected_pair[0]
    maximum = -1
    count = maxima = 0
    seen = set()
    for rows in rref_planes(k):
        key = tuple(sorted(plane_vectors(rows)))
        assert len(set(key)) == 9 and key not in seen
        seen.add(key)
        mass = plane_mass_numerator(rows)
        assert mass <= expected_numerator
        count += 1
        if mass > maximum:
            maximum, maxima = mass, 1
        elif mass == maximum:
            maxima += 1
    expected_count = ((3**k - 1) * (3**k - 3)) // ((9 - 1) * (9 - 3))
    assert count == expected_count and maximum == expected_numerator
    target_rows = [[1] * (k - 1) + [0], [0] * (k - 1) + [1]]
    assert plane_mass_numerator(target_rows) == maximum
    return {
        "parameter_dimension": k,
        "all_two_planes_checked": count,
        "maximizing_planes": maxima,
        "exact_maximum_weight": str(Fraction(maximum, 18**k)),
        "maximum_equals_sum_w_to_k_minus_1": True,
        "target_plane": "{(s,...,s,t):s,t in F_3}",
        "target_plane_attains_maximum": True,
    }


def verify_root_plane(h, field):
    k, n = 2 * h + 1, 6 * h
    basis = parameter_basis(field, k)
    va = tuple([1] * (k - 1) + [0])
    vb = tuple([0] * (k - 1) + [1])
    a = linear_combination(field, va, basis)
    b = linear_combination(field, vb, basis)
    a2 = field.power(a, 2)
    u = field.add(field.power(b, 3), field.neg(field.mul(a2, b)))
    assert a and b and u
    u2 = field.power(u, 2)
    coefficients = (
        field.mul(a2, u2),
        field.neg(field.add(field.power(a, 6), u2)),
        1,
    )
    target = set(plane_vectors((va, vb)))
    roots = set()
    image_parameters = set()
    covector = np.zeros(n, dtype=np.uint16)
    for i, coefficient in enumerate(coefficients):
        for j, basis_element in enumerate(field.basis):
            covector[i * h + j] = field.trace(field.mul(coefficient, basis_element))
    assert np.any(covector)
    for nu in itertools.product(range(3), repeat=k):
        t = linear_combination(field, nu, basis)
        value = 0
        for coefficient, exponent in zip(coefficients, (1, 3, 9)):
            value = field.add(value, field.mul(coefficient, field.power(t, exponent)))
        if value == 0:
            roots.add(nu)
        scalar_form = good_matrix(field, t)
        rank_base = 4 * h if any(nu) else 0
        if erank(np.column_stack((scalar_form, covector))) == rank_base:
            image_parameters.add(nu)
    zero = (0,) * k
    assert roots == target
    assert image_parameters == target - {zero}
    mass_numerator = plane_mass_numerator((va, vb))
    good_mass = Fraction(mass_numerator - 4**k, 18**k)
    aligned_mass = Fraction(18**k - 4**k, 18**k)
    return {
        "h": h,
        "parameter_dimension": k,
        "all_parameters_checked": 3**k,
        "a_packed": a,
        "b_packed": b,
        "u_packed": u,
        "polynomial_coefficients_X_X3_X9_packed": coefficients,
        "root_parameter_set_is_exact_target_plane": True,
        "direct_scalar_image_parameters_are_exact_plane_minus_zero": True,
        "nonzero_scalar_image_parameter_count": len(image_parameters),
        "exact_good_image_weight": str(good_mass),
        "exact_aligned_image_weight": str(aligned_mass),
        "exact_squared_norm_ratio_if_shared_gram_prefactor": str(good_mass / aligned_mass),
    }


def main():
    assert Q == 729
    E = Extension(1)
    quadratic = Extension(2, (14, 0))
    results = {
        "arithmetic": "Exact F_729 extension arithmetic and exact Q(sqrt(21)) weights.",
        "plane_enumeration": [verify_plane_maximum(3), verify_plane_maximum(5)],
        "root_polynomial_attainment": [verify_root_plane(1, E), verify_root_plane(2, quadratic)],
        "scope": "The weight maximum is exhaustive for k=3,5; the general inequality and the general root-polynomial construction have separate proofs. The external Bol Gram prefactor 18/49 is not checked here.",
    }
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()

