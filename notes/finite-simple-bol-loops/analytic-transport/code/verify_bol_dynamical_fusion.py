"""Exact controls for the charged-fusion principal-symbol obstruction.

Python 3.11+, standard library only; run with assertions enabled.
This exhausts support permutations for a nine-point Heisenberg control,
not a simple proper Bol loop, and does not validate analytic convergence.
Universal statements and scope are in bol-fusion-symbol-obstruction.md.
"""

import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
import json
from math import factorial, isqrt
from pathlib import Path


def rational_rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    pivot_row = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        coefficient = a[pivot_row][j]
        a[pivot_row] = [x / coefficient for x in a[pivot_row]]
        for i in range(len(a)):
            if i != pivot_row and a[i][j]:
                coefficient = a[i][j]
                a[i] = [x - coefficient * y
                        for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def separate_basis(n):
    grid = list(product(range(n), repeat=2))
    return [[int(x == i) for x, y in grid] for i in range(n - 1)] + [
        [int(y == i) for x, y in grid] for i in range(n - 1)]


def push_function(values, permutation):
    result = [0] * len(values)
    for source, target in enumerate(permutation):
        result[target] = values[source]
    return result


def is_separate(values, n):
    return all(values[i * n + j] - values[i * n]
               - values[j] + values[0] == 0
               for i in range(1, n) for j in range(1, n))


def permutation_control():
    n = 3
    grid = list(product(range(n), repeat=2))
    lookup = {point: i for i, point in enumerate(grid)}
    functions = separate_basis(n)
    source_shift = [lookup[((x + 1) % n, (y + 1) % n)] for x, y in grid]
    target_shift = [lookup[((u + 1) % n, v)] for u, v in grid]
    predicted = set()
    for sigma, tau in product(list(permutations(range(n))), repeat=2):
        predicted.add(tuple(lookup[(sigma[x], tau[y])] for x, y in grid))
        predicted.add(tuple(lookup[(sigma[y], tau[x])] for x, y in grid))
    assert len(predicted) == 2 * factorial(n) ** 2

    normalizers = set()
    equivariant = set()
    examined = 0
    for perm in permutations(range(n * n)):
        examined += 1
        if all(is_separate(push_function(f, perm), n) for f in functions):
            normalizers.add(perm)
        if all(perm[source_shift[k]] == target_shift[perm[k]]
               for k in range(n * n)):
            equivariant.add(perm)
    assert examined == factorial(9)
    assert normalizers == predicted
    assert len(equivariant) == factorial(n) * n ** n
    assert not normalizers.intersection(equivariant)

    # Actual canonical regular fusion for lambda=mu=1, gamma=2.
    fusion = tuple(lookup[((2 * x + 2 * y) % 3, (x - y) % 3)]
                   for x, y in grid)
    assert fusion in equivariant and fusion not in normalizers
    input_after_fusion = [push_function(f, fusion) for f in functions]
    # Traceless basis: multiply by 3 to keep integer entries.
    trace_input = [[3 * x - 1 for x in f] for f in input_after_fusion]
    trace_output = [[3 * x - 1 for x in f] for f in functions]
    assert rational_rank(trace_input) == rational_rank(trace_output) == 4
    assert rational_rank(trace_input + trace_output) == 8
    assert rational_rank([[1] * 9] + input_after_fusion + functions) == 9
    return {
        "support_permutations_examined": examined,
        "separate_symbol_normalizers": len(normalizers),
        "predicted_grid_normalizers": len(predicted),
        "first_axis_equivariant_supports": len(equivariant),
        "intersection": 0,
        "canonical_fusion_is_equivariant": True,
        "canonical_fusion_normalizes_separate_symbols": False,
        "separate_traceless_dimensions": [4, 4],
        "joint_traceless_span_dimension": 8,
        "joint_unital_span_dimension": 9,
    }


def charged_intertwiner_control():
    p, half = 3, 2
    grid = list(product(range(p), repeat=2))
    checked, pairs = 0, 0
    for ell, mu in product(range(p), repeat=2):
        gamma = (ell + mu) % p
        if gamma == 0:
            continue
        pairs += 1
        inverse = pow(gamma, -1, p)
        for x, y in grid:
            u = inverse * (ell * x + mu * y) % p
            v = (x - y) % p
            assert (u + inverse * mu * v) % p == x
            assert (u - inverse * ell * v) % p == y
            for t, s, z in product(range(p), repeat=3):
                xx, yy = (x - t) % p, (y - t) % p
                left_u = inverse * (ell * xx + mu * yy) % p
                left_v = (xx - yy) % p
                phase_input = (
                    ell * (z + x * s - half * t * s)
                    + mu * (z + y * s - half * t * s)) % p
                phase_output = gamma * (z + u * s - half * t * s) % p
                assert left_u == (u - t) % p and left_v == v
                assert phase_input == phase_output
                checked += 1
    return {"regular_sum_pairs_including_degenerate_inputs": pairs,
            "exact_delta_basis_intertwiner_equations": checked}


def parameter_span_control():
    reports = []
    for p in (3, 5, 7, 11):
        def nonzero_line(a, b):
            return {(t * a % p, t * b % p) for t in range(1, p)}
        fixed_lines = [(1, 0), (0, 1), (1, -1 % p)]
        directions = fixed_lines + [(a, (1 - a) % p) for a in range(2, p)]
        supports = [nonzero_line(*direction) for direction in directions]
        for i, x in enumerate(supports):
            for y in supports[i + 1:]:
                assert x.isdisjoint(y)
        covered = set().union(*supports)
        assert covered == set(product(range(p), repeat=2)) - {(0, 0)}
        one_split = set().union(*supports[:4])
        assert len(one_split) + 1 == 4 * p - 3
        reports.append({"prime": p, "projective_directions": len(directions),
                        "one_regular_split_unital_span": len(one_split) + 1,
                        "all_regular_splits_unital_span": len(covered) + 1,
                        "all_regular_splits_traceless_span": len(covered)})
    return reports


def joint_zero_control():
    p = 3
    vectors = list(product(range(p), repeat=4))
    first = (1, 0, 1, 0)
    second = (0, 1, 0, 1)
    reports = []
    for ell, mu in ((1, 1), (1, 2)):
        def omega(x, y):
            return (ell * (x[0] * y[1] - y[0] * x[1])
                    + mu * (x[2] * y[3] - y[2] * x[3])) % p
        fixed = [x for x in vectors
                 if omega(first, x) == omega(second, x) == 0]
        center = [x for x in fixed if all(omega(x, y) == 0 for y in fixed)]
        separate = [x for x in vectors
                    if all(omega(e, x) == 0 for e in (
                        (1, 0, 0, 0), (0, 1, 0, 0),
                        (0, 0, 1, 0), (0, 0, 0, 1)))]
        assert len(separate) == 1 and len(fixed) == 9
        expected_center = 1 if (ell + mu) % p else 9
        assert len(center) == expected_center
        block_size = isqrt(len(fixed) // len(center))
        assert len(center) * block_size ** 2 == len(fixed)
        reports.append({"charges": [ell, mu],
                        "separately_fixed_tensor_dimension": len(separate),
                        "joint_fixed_dimension": len(fixed),
                        "center_dimension": len(center),
                        "matrix_block_size": block_size,
                        "dimension_growth_factor": len(fixed) // len(separate)})
    return reports


def main():
    assert __debug__, "Run with assertions enabled"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()
    report = {
        "status": "PASS",
        "arithmetic": "Exact integers, rationals and finite fields",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "grid_symbol_control": permutation_control(),
        "charged_intertwiner_control": charged_intertwiner_control(),
        "parameter_span_control": parameter_span_control(),
        "joint_zero_control": joint_zero_control(),
        "limits": [
            "Local Heisenberg controls, not an enumerated simple proper Bol loop",
            "Full separate principal-symbol hypothesis is essential",
            "No test of arbitrary shared-q or restricted trace systems",
            "No analytic convergence, flatness or pentagon certified here",
            "No independent review of inherited classification interfaces",
        ],
    }
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.certificate:
        args.certificate.write_text(encoded)
        print(json.dumps({"status": report["status"],
                          "script_sha256": report["script_sha256"],
                          "certificate": str(args.certificate),
                          "permutations": 362880,
                          "normalizers": 72,
                          "equivariant_supports": 162,
                          "intersection": 0}, indent=2))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
