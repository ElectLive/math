"""Exact finite Gaussian-sewing checks; standard library, assertions enabled.

This validates finite Grassmann identities and bordered determinants.  It does
not validate a continuum sewing limit, modularity, or inherited Bol inputs.
"""

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


def add(*polys):
    out = {}
    for poly in polys:
        for mask, value in poly.items():
            out[mask] = out.get(mask, F(0)) + value
    return {mask: value for mask, value in out.items() if value}


def scale(poly, value):
    return {mask: value * coeff for mask, coeff in poly.items() if value * coeff}


def mul(a, b):
    out = {}
    for x, cx in a.items():
        for y, cy in b.items():
            if x & y:
                continue
            inversions = sum((y & ((1 << i) - 1)).bit_count()
                             for i in range(x.bit_length()) if (x >> i) & 1)
            z = x | y
            value = cx * cy * (-1 if inversions % 2 else 1)
            out[z] = out.get(z, F(0)) + value
    return {mask: value for mask, value in out.items() if value}


def var(i):
    return {1 << i: F(1)}


def exp(poly):
    assert not poly.get(0, 0)
    answer, term, k = {0: F(1)}, {0: F(1)}, 0
    while term:
        k += 1
        term = scale(mul(term, poly), F(1, k))
        answer = add(answer, term)
    return answer


def integrate_pairs(poly, pairs):
    # Variables psi_i,barpsi_i have consecutive indices 2i,2i+1.
    # The convention makes integral exp(-barpsi A psi) = det(A).
    mask = sum((1 << (2 * i)) | (1 << (2 * i + 1)) for i in pairs)
    return {key ^ mask: coeff for key, coeff in poly.items()
            if key & mask == mask}


def determinant(a):
    n = len(a)
    assert all(len(row) == n for row in a)
    a = [[F(x) for x in row] for row in a]
    result = F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            result = -result
        value = a[j][j]
        result *= value
        for i in range(j + 1, n):
            factor = a[i][j] / value
            a[i] = [x - factor * y for x, y in zip(a[i], a[j])]
    return result


def inverse(a):
    n = len(a)
    out = [[F(x) for x in row] + [F(i == j) for j in range(n)]
           for i, row in enumerate(a)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if out[i][j])
        out[j], out[pivot] = out[pivot], out[j]
        value = out[j][j]
        out[j] = [x / value for x in out[j]]
        for i in range(n):
            if i != j:
                value = out[i][j]
                out[i] = [x - value * y for x, y in zip(out[i], out[j])]
    return [row[n:] for row in out]


def mm(a, b):
    return [[sum(F(x) * y for x, y in zip(row, column))
             for column in zip(*b)] for row in a]


def plus(a, b):
    return [[x + y for x, y in zip(row, other)] for row, other in zip(a, b)]


def source_gaussian(a):
    n = len(a)
    action = {}
    for i, j in product(range(n), repeat=2):
        action = add(action, scale(mul(var(2 * i + 1), var(2 * j)), -F(a[i][j])))
    for i in range(n):
        bar_eta, eta = var(2 * n + 2 * i), var(2 * n + 2 * i + 1)
        action = add(action, mul(bar_eta, var(2 * i)), mul(var(2 * i + 1), eta))
    return integrate_pairs(exp(action), range(n))


def invertible_formula(a):
    n, action = len(a), {}
    ainv = inverse(a)
    for i, j in product(range(n), repeat=2):
        action = add(action, scale(mul(var(2 * n + 2 * i),
                                       var(2 * n + 2 * j + 1)), ainv[i][j]))
    return scale(exp(action), determinant(a))


def finite_gaussian_checks():
    matrices = [[[2]], [[1, 2], [3, 5]], [[0, 1], [1, 2]],
                [[1, 1, 0], [0, 2, 1], [1, 0, 1]]]
    for a in matrices:
        assert determinant(a)
        assert source_gaussian(a) == invertible_formula(a)

    singular_examples = 0
    for a in (0, 1, 2, -3):
        actual = source_gaussian([[a, 0], [0, 0]])
        p1, p2 = mul(var(4), var(5)), mul(var(6), var(7))
        expected = add(scale(p2, F(a)), mul(p1, p2))
        assert actual == expected
        assert not actual.get(0, 0)
        singular_examples += 1

    # A non-diagonal singular matrix has no source-free term either.
    assert not source_gaussian([[1, 2], [2, 4]]).get(0, 0)
    # Two internal pairs, with an individually singular first pivot block.
    # Partial coefficient extraction never divides by that block.
    a = [[0, 1], [1, 2]]
    action = {}
    for i, j in product(range(2), repeat=2):
        action = add(action, scale(mul(var(2 * i + 1), var(2 * j)), -F(a[i][j])))
    for i in range(2):
        action = add(action, mul(var(4 + 2 * i), var(2 * i)),
                     mul(var(2 * i + 1), var(5 + 2 * i)))
    integrand = exp(action)
    simultaneous = integrate_pairs(integrand, (0, 1))
    first_then_second = integrate_pairs(integrate_pairs(integrand, (0,)), (1,))
    second_then_first = integrate_pairs(integrate_pairs(integrand, (1,)), (0,))
    assert simultaneous == first_then_second == second_then_first
    assert simultaneous == invertible_formula(a)
    return {"invertible_source_formulas": len(matrices),
            "diagonal_singular_examples": singular_examples,
            "nondiagonal_singular_examples": 1,
            "singular_pivot_sewing_orders": 3,
            "singular_example": "Z_diag(a,0)=a*bareta2*eta2+bareta1*eta1*bareta2*eta2"}


def schur_checks():
    n = 2
    a = [[1, 2], [3, 5]]
    b = [[2, 0], [1, -1]]
    c = [[0, 1], [2, 3]]
    d = [[1, 0], [2, 1]]
    action = {}
    for i, j in product(range(n), repeat=2):
        action = add(action,
                     scale(mul(var(2 * i + 1), var(2 * j)), -F(a[i][j])),
                     scale(mul(var(2 * i + 1), var(2 * n + 2 * j + 1)), F(b[i][j])),
                     scale(mul(var(2 * n + 2 * i), var(2 * j)), F(c[i][j])),
                     scale(mul(var(2 * n + 2 * i), var(2 * n + 2 * j + 1)), F(d[i][j])))
    effective = plus(d, mm(mm(c, inverse(a)), b))
    expected_action = {}
    for i, j in product(range(n), repeat=2):
        expected_action = add(expected_action,
                              scale(mul(var(2 * n + 2 * i), var(2 * n + 2 * j + 1)),
                                    effective[i][j]))
    assert integrate_pairs(exp(action), range(n)) == scale(exp(expected_action), determinant(a))
    return {"nontrivial_schur_source_identity": True,
            "effective_matrix": [[str(x) for x in row] for row in effective]}


def bordered(m, u, v, h):
    n = len(m)
    return [list(m[i]) + list(u[i]) for i in range(n)] + [list(v[i]) + [0] * h for i in range(h)]


def border_checks():
    checks = 0
    for n, h in ((1, 0), (1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)):
        m = [[F((i + 2) * (j + 1) + int(i == j)) for j in range(n)] for i in range(n)]
        u = [[F((i + 1) ** j) for j in range(h)] for i in range(n)]
        v = [[F((j + 2) ** i) for j in range(n)] for i in range(h)]
        a = [[F(i + j + 1) for j in range(h)] for i in range(n)]
        b = [[F(i - j + 2) for j in range(n)] for i in range(h)]
        value = determinant(bordered(m, u, v, h))
        if n < h:
            assert value == 0
        correction = [[sum(a[i][k] * v[k][j] + u[i][k] * b[k][j] for k in range(h))
                       for j in range(n)] for i in range(n)]
        assert determinant(bordered(plus(m, correction), u, v, h)) == value
        for r in (F(2), F(-3)):
            scaled = [[r * x for x in row] for row in m]
            assert determinant(bordered(scaled, u, v, h)) == r ** (n - h) * value
            checks += 1
        if h == 2:
            change = [[1, 2], [0, 1]]
            assert determinant(bordered(m, mm(u, inverse(change)), mm(change, v), h)) == value
            checks += 1
    return {"border_covariance_checks": checks,
            "checks": ["zero-mode saturation", "M->M+A V+U B", "weight n-h", "zero-basis transport"]}


def main():
    assert __debug__, "Run with assertions enabled"
    quartic = mul(mul(var(0), var(1)), mul(var(2), var(3)))
    non_gaussian = add({0: F(1)}, scale(quartic, F(2)))
    assert all(mask.bit_count() in (0, 4) for mask in non_gaussian)
    assert non_gaussian != exp({})
    report = {"status": "PASS",
              "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "arithmetic": "exact rational exterior algebra and determinants",
              "finite_gaussian": finite_gaussian_checks(),
              "schur_complement": schur_checks(),
              "bordered_zero_modes": border_checks(),
              "quartic_escape": "nonzero fourth coefficient with zero second coefficients",
              "limits": ["No continuum convergence check", "No numerical theta or modularity check",
                         "No new interacting theory", "No inherited Bol input reverified"]}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
