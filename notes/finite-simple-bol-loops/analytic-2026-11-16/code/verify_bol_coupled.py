#!/usr/bin/env python3
"""Exact h=1,2 checks for the coupled constant-rank pencils.

All field operations are exact. NumPy is used only to build the F_729
addition/multiplication tables and store small integer matrices.  There is
no numerical rank calculation and no floating-point field arithmetic.
"""

from __future__ import annotations

import itertools
import json
import random
from functools import lru_cache

import numpy as np


P = 3
Q = 729
DEG = 6


def base_tables():
    powers = np.array([3**j for j in range(DEG)], dtype=np.int32)
    digits = np.array(
        [[(a // (3**j)) % 3 for j in range(DEG)] for a in range(Q)],
        dtype=np.int16,
    )
    add = np.sum(
        ((digits[:, None, :] + digits[None, :, :]) % 3) * powers,
        axis=2,
        dtype=np.int32,
    ).astype(np.uint16)
    coeff = np.zeros((Q, Q, 2 * DEG - 1), dtype=np.int16)
    for i in range(DEG):
        for j in range(DEG):
            coeff[:, :, i + j] += digits[:, i, None] * digits[None, :, j]
    coeff %= 3
    # lambda^6 = -(1+lambda+...+lambda^5), the seventh cyclotomic polynomial.
    for j in range(2 * DEG - 2, DEG - 1, -1):
        top = coeff[:, :, j].copy()
        for i in range(DEG):
            coeff[:, :, j - DEG + i] = (coeff[:, :, j - DEG + i] - top) % 3
        coeff[:, :, j] = 0
    mul = np.sum(coeff[:, :, :DEG] * powers, axis=2, dtype=np.int32).astype(
        np.uint16
    )
    neg = mul[2, :].copy()
    inverse = np.zeros(Q, dtype=np.uint16)
    for a in range(1, Q):
        hits = np.flatnonzero(mul[a] == 1)
        assert len(hits) == 1
        inverse[a] = hits[0]
    return add, mul, neg, inverse, digits


ADD, MUL, NEG, INV, DIGITS = base_tables()


def eadd(a, b):
    return int(ADD[a, b])


def emul(a, b):
    return int(MUL[a, b])


def eneg(a):
    return int(NEG[a])


def epow(a, exponent):
    answer = 1
    while exponent:
        if exponent & 1:
            answer = emul(answer, a)
        a = emul(a, a)
        exponent >>= 1
    return answer


def eabsolute_trace(a):
    answer = 0
    for _ in range(DEG):
        answer = eadd(answer, a)
        a = epow(a, 3)
    assert answer in (0, 1, 2)
    return answer


class Extension:
    """E[T]/(T^d - sum(reduction[i] T^i)), packed in radix |E|."""

    def __init__(self, degree, reduction=None):
        self.degree = degree
        self.reduction = tuple(reduction or ())
        self.order = Q**degree
        self.basis = tuple(Q**i for i in range(degree))
        if degree == 1:
            self.trace_basis = (1,)
        else:
            self.trace_basis = tuple(self.trace_frobenius(b) for b in self.basis)

    @lru_cache(maxsize=None)
    def unpack(self, value):
        return tuple((value // (Q**i)) % Q for i in range(self.degree))

    def pack(self, coeff):
        return sum(int(a) * Q**i for i, a in enumerate(coeff))

    def add(self, a, b):
        if self.degree == 1:
            return eadd(a, b)
        return self.pack([eadd(x, y) for x, y in zip(self.unpack(a), self.unpack(b))])

    def neg(self, a):
        return self.pack([eneg(x) for x in self.unpack(a)])

    def mul(self, a, b):
        if self.degree == 1 or (a < Q and b < Q):
            return emul(a, b)
        aa, bb = self.unpack(a), self.unpack(b)
        if a < Q:
            return self.pack([emul(a, x) for x in bb])
        if b < Q:
            return self.pack([emul(x, b) for x in aa])
        d = self.degree
        c = [0] * (2 * d - 1)
        for i, x in enumerate(aa):
            if x:
                for j, y in enumerate(bb):
                    if y:
                        c[i + j] = eadd(c[i + j], emul(x, y))
        for j in range(2 * d - 2, d - 1, -1):
            top = c[j]
            if top:
                for i, factor in enumerate(self.reduction):
                    if factor:
                        c[j - d + i] = eadd(c[j - d + i], emul(top, factor))
            c[j] = 0
        return self.pack(c[:d])

    def power(self, a, exponent):
        answer = 1
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, a)
            a = self.mul(a, a)
            exponent >>= 1
        return answer

    def trace_frobenius(self, a):
        answer = 0
        for _ in range(self.degree):
            answer = self.add(answer, a)
            a = self.power(a, Q)
        assert answer < Q, (self.degree, a, answer)
        return answer

    def trace(self, a):
        answer = 0
        for coefficient, basis_trace in zip(self.unpack(a), self.trace_basis):
            answer = eadd(answer, emul(coefficient, basis_trace))
        return answer

    def prime_coordinates(self, a):
        return [int(d) for coefficient in self.unpack(a) for d in DIGITS[coefficient]]


def erank(matrix):
    a = np.array(matrix, dtype=np.uint16, copy=True)
    nrows, ncols = a.shape
    rank = 0
    for col in range(ncols):
        hits = np.flatnonzero(a[rank:, col])
        if not len(hits):
            continue
        pivot = rank + int(hits[0])
        a[[rank, pivot]] = a[[pivot, rank]]
        a[rank] = MUL[INV[a[rank, col]], a[rank]]
        for row in range(nrows):
            if row != rank and a[row, col]:
                a[row] = ADD[a[row], NEG[MUL[a[row, col], a[rank]]]]
        rank += 1
        if rank == min(nrows, ncols):
            break
    return rank


def prank(matrix):
    a = np.array(matrix, dtype=np.int16, copy=True) % 3
    nrows, ncols = a.shape
    rank = 0
    for col in range(ncols):
        hits = np.flatnonzero(a[rank:, col])
        if not len(hits):
            continue
        pivot = rank + int(hits[0])
        a[[rank, pivot]] = a[[pivot, rank]]
        a[rank] = (a[rank] * int(a[rank, col])) % 3
        for row in range(nrows):
            if row != rank and a[row, col]:
                a[row] = (a[row] - int(a[row, col]) * a[rank]) % 3
        rank += 1
        if rank == min(nrows, ncols):
            break
    return rank


def parameter_basis(field, count):
    # Alternate extension coordinates, avoiding a needlessly subfield-only
    # sample when h=2. All entries are distinct prime-field basis vectors.
    basis = [field.basis[j] * 3**i for i in range(DEG) for j in range(field.degree)]
    assert count <= len(basis)
    return basis[:count]


def linear_combination(field, coefficients, basis):
    value = 0
    for scalar, vector in zip(coefficients, basis):
        value = field.add(value, field.mul(scalar, vector))
    return value


def good_matrix(field, t):
    h = field.degree
    z = (t, field.power(t, 3), field.power(t, 9))
    block = np.zeros((3 * h, 3 * h), dtype=np.uint16)
    for i, j, index, sign in ((0, 1, 2, 1), (0, 2, 1, 2), (1, 2, 0, 1)):
        for a, ea in enumerate(field.basis):
            for b, eb in enumerate(field.basis):
                value = field.trace(field.mul(z[index], field.mul(ea, eb)))
                value = emul(sign, value)
                block[i * h + a, j * h + b] = value
                block[j * h + b, i * h + a] = eneg(value)
    answer = np.zeros((6 * h, 6 * h), dtype=np.uint16)
    answer[: 3 * h, : 3 * h] = block
    answer[3 * h :, 3 * h :] = block
    return answer


def aligned_matrix(field, coefficients, m):
    k, degree = len(coefficients), field.degree
    answer = np.zeros((k + 1 + 2 * degree, k + 1 + 2 * degree), dtype=np.uint16)
    for j, scalar in enumerate(coefficients):
        answer[0, j + 1] = scalar
        answer[j + 1, 0] = eneg(scalar)
    start = k + 1
    for i, ei in enumerate(field.basis):
        for j, ej in enumerate(field.basis):
            value = field.trace(field.mul(m, field.mul(ei, ej)))
            answer[start + i, start + degree + j] = value
            answer[start + degree + j, start + i] = eneg(value)
    return answer


def matrix_combination(coefficients, matrices):
    answer = np.zeros_like(matrices[0])
    for scalar, matrix in zip(coefficients, matrices):
        answer = ADD[answer, MUL[scalar, matrix]]
    return answer


def is_alternating(matrix):
    return bool(np.all(np.diag(matrix) == 0) and np.all(ADD[matrix, matrix.T] == 0))


def verify_h(h, L, M, samples=256):
    k, n = 2 * h + 1, 6 * h
    basis_L = parameter_basis(L, k)
    basis_M = parameter_basis(M, k)
    good_basis = [good_matrix(L, t) for t in basis_L]
    coordinate_basis = [tuple(int(i == j) for i in range(k)) for j in range(k)]
    aligned_basis = [
        aligned_matrix(M, nu, m) for nu, m in zip(coordinate_basis, basis_M)
    ]
    assert all(is_alternating(b) for b in good_basis + aligned_basis)
    common_good = n - erank(np.vstack(good_basis))
    common_aligned = n - erank(np.vstack(aligned_basis))
    assert common_good == common_aligned == 0
    parameters = list(itertools.product(range(3), repeat=k))
    t_values = [linear_combination(L, nu, basis_L) for nu in parameters]
    m_values = [linear_combination(M, nu, basis_M) for nu in parameters]
    assert len(set(t_values)) == len(set(m_values)) == 3**k
    z_values = [(t, L.power(t, 3), L.power(t, 9)) for t in t_values]
    rank_histogram = {}
    good_matrices = []
    common_image_vector = np.zeros(n, dtype=np.uint16)
    common_image_vector[0] = 1
    for nu, t, m in zip(parameters, t_values, m_values):
        good = good_matrix(L, t)
        aligned = aligned_matrix(M, nu, m)
        assert np.array_equal(good, matrix_combination(nu, good_basis))
        assert np.array_equal(aligned, matrix_combination(nu, aligned_basis))
        rank_good, rank_aligned = erank(good), erank(aligned)
        expected = 0 if not any(nu) else 4 * h
        assert rank_good == rank_aligned == expected
        good_matrices.append(good)
        rank_histogram[str(expected)] = rank_histogram.get(str(expected), 0) + 1
        if any(nu):
            assert erank(np.column_stack((aligned, common_image_vector))) == expected

    # Random coefficients in L^3 plus constructed polynomials having a
    # 2-dimensional root space. For each polynomial enumerate every t in A.
    rng = random.Random(2026111600 + h)
    polynomials = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    # The span of the first two independent parameter basis vectors is a
    # 2-dimensional F_3-root space. Solve a*t+b*t^3+t^9=0 at both vectors.
    t1, t2 = basis_L[:2]
    t13, t23 = L.power(t1, 3), L.power(t2, 3)
    t19, t29 = L.power(t1, 9), L.power(t2, 9)
    determinant = L.add(L.mul(t1, t23), L.neg(L.mul(t2, t13)))
    assert determinant
    inverse_det = L.power(determinant, L.order - 2)
    aa = L.mul(
        L.add(L.neg(L.mul(t19, t23)), L.mul(t29, t13)), inverse_det
    )
    bb = L.mul(
        L.add(L.neg(L.mul(t1, t29)), L.mul(t2, t19)), inverse_det
    )
    polynomials.append((aa, bb, 1))
    for _ in range(samples):
        coefficients = tuple(rng.randrange(L.order) for _ in range(3))
        if not any(coefficients):
            coefficients = (1, 0, 0)
        polynomials.append(coefficients)
    root_count_histogram = {}
    image_membership_checks = 0
    for polynomial_index, coefficients in enumerate(polynomials):
        roots = []
        # Convert the L-valued Fourier coefficient to the ordinary E-dual
        # coordinates of our matrices using the perfect trace pairing.
        covector = np.zeros(n, dtype=np.uint16)
        for i, coefficient in enumerate(coefficients):
            for j, basis_element in enumerate(L.basis):
                covector[i * h + j] = L.trace(L.mul(coefficient, basis_element))
        assert np.any(covector)
        for nu, z, good in zip(parameters, z_values, good_matrices):
            value = 0
            for coefficient, coordinate in zip(coefficients, z):
                value = L.add(value, L.mul(coefficient, coordinate))
            if not value:
                roots.append(nu)
            if polynomial_index < 12:
                # t=0 is a separate stratum: its image is {0}, not the
                # vacuous hyperplane cut out by z(0)=0.
                expected_membership = bool(any(nu) and value == 0)
                rank_base = 4 * h if any(nu) else 0
                actual_membership = erank(np.column_stack((good, covector))) == rank_base
                assert actual_membership == expected_membership
                image_membership_checks += 1
        count = len(roots)
        assert count in (1, 3, 9), (h, coefficients, count)
        # Independent rank computation of the F_3-linear restriction A -> L.
        columns = []
        for t in basis_L:
            value = 0
            for coefficient, exponent in zip(coefficients, (1, 3, 9)):
                value = L.add(value, L.mul(coefficient, L.power(t, exponent)))
            columns.append(L.prime_coordinates(value))
        nullity = k - prank(np.array(columns).T)
        assert count == 3**nullity and nullity <= 2
        root_count_histogram[str(count)] = root_count_histogram.get(str(count), 0) + 1
    assert root_count_histogram.get("9", 0) >= 1
    return {
        "h": h,
        "parameter_dimension_F3": k,
        "ambient_dimension_E": n,
        "parameter_basis_L_packed": basis_L,
        "parameter_basis_M_packed": basis_M,
        "all_parameter_forms_checked": len(parameters),
        "identical_scalar_rank_histogram": rank_histogram,
        "common_radical_dimensions_E": {"good": common_good, "aligned": common_aligned},
        "aligned_e0_in_every_nonzero_scalar_image": True,
        "sampled_nonzero_linearized_polynomials": len(polynomials),
        "all_parameter_values_checked_per_polynomial": len(parameters),
        "root_count_histogram": root_count_histogram,
        "maximum_parameter_kernel_dimension_F3": 2,
        "direct_scalar_image_membership_checks": image_membership_checks,
    }


def main():
    lam = 3
    assert epow(lam, 7) == 1 and lam != 1
    assert all(epow(a, Q) == a for a in range(Q))
    assert eabsolute_trace(lam) == 2
    nonsquare = next(a for a in range(2, Q) if epow(a, (Q - 1) // 2) == 2)
    E = Extension(1)
    quadratic = Extension(2, (nonsquare, 0))
    cubic = Extension(3, (lam, 1, 0))
    assert quadratic.trace_basis == (2, 0)
    assert cubic.trace_basis == (0, 0, 2)
    rng = random.Random(20261116)
    for field in (quadratic, cubic):
        for _ in range(64):
            a = rng.randrange(1, field.order)
            assert field.power(a, field.order - 1) == 1
            assert field.trace(a) == field.trace_frobenius(a)
        trace_gram = [
            [field.trace(field.mul(a, b)) for b in field.basis]
            for a in field.basis
        ]
        assert erank(trace_gram) == field.degree
    result = {
        "arithmetic": "exact polynomial arithmetic in characteristic 3",
        "base_field": {
            "order": Q,
            "modulus": "X^6+X^5+X^4+X^3+X^2+X+1",
            "irreducibility_certificate": "ord_7(3)=6",
            "lambda_packed": lam,
            "lambda_absolute_trace": 2,
        },
        "extensions": {
            "L_for_h2": {
                "degree_over_E": 2,
                "relation": f"T^2={nonsquare}",
                "nonsquare_E_packed": nonsquare,
                "nonsquare_power_364": epow(nonsquare, 364),
                "trace_basis": quadratic.trace_basis,
            },
            "M_for_h2": {
                "degree_over_E": 3,
                "relation": "T^3=T+lambda",
                "irreducibility_certificate": "Tr_(E/F3)(lambda)=2 != 0",
                "trace_basis": cubic.trace_basis,
            },
        },
        "cases": [verify_h(1, E, E), verify_h(2, quadratic, cubic)],
        "scope": {
            "ranks": "Exhaustive over all parameters for h=1,2.",
            "kernel_bound": "Exhaustive over each parameter space for 260 sampled/constructed polynomials per h; the all-coefficient claim follows separately from the degree-9 root bound.",
            "not_checked": "The external Bol roundtrip factor 18/49 and the weighted-Gram normalization are not encoded in this verifier.",
        },
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

