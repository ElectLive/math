"""Exact finite controls for TH1--TH3 in bol-theta-fusion-connection.md.

Python 3.11+, standard library only, assertions enabled. This checks rational
symbols, coordinate changes and Fourier exponents. It does not establish
normal convergence, Serre duality, a general pentagon or the new Bol target.
"""

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import factorial
import json
from pathlib import Path


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def inverse(a):
    n = len(a)
    out = [[F(x) for x in row] + unit for row, unit in zip(a, eye(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if out[i][j])
        out[j], out[pivot] = out[pivot], out[j]
        c = out[j][j]
        out[j] = [x / c for x in out[j]]
        for i in range(n):
            if i != j:
                c = out[i][j]
                out[i] = [x - c * y for x, y in zip(out[i], out[j])]
    return [row[n:] for row in out]


def leaves(tree):
    if isinstance(tree, int):
        return [tree]
    return leaves(tree[0]) + leaves(tree[1])


def tree_matrix(tree):
    n = len(leaves(tree))
    columns = [[F(1)] * n]
    def walk(node):
        if isinstance(node, int):
            return
        column = [F(0)] * n
        for i in leaves(node[0]):
            column[i] = F(1)
        for i in leaves(node[1]):
            column[i] = F(-1)
        columns.append(column)
        walk(node[0])
        walk(node[1])
    walk(tree)
    return transpose(columns)


def signed_and_zero_checks():
    signed_cases = 0
    for p in (3, 5, 7):
        for k, l in product(range(-5, 6), repeat=2):
            if not k or not l:
                continue
            t = [[F(1), F(1)], [F(1), F(-1)]]
            g = [[F(k, p), F(0)], [F(0), F(l, p)]]
            out = mm(mm(transpose(t), g), t)
            assert out == [[F(k + l, p), F(k - l, p)],
                           [F(k - l, p), F(k + l, p)]]
            ti = inverse(t)
            assert inverse(out) == mm(mm(ti, inverse(g)), transpose(ti))
            if k + l == 0:
                assert inverse(out) == [[F(0), F(p, 2 * k)],
                                        [F(p, 2 * k), F(0)]]
            signed_cases += 1

    # All five trees of the pentagon, with total and intermediate zero degrees.
    trees = [(((0, 1), 2), 3), ((0, (1, 2)), 3),
             (0, ((1, 2), 3)), (0, (1, (2, 3))), ((0, 1), (2, 3))]
    matrices = [tree_matrix(t) for t in trees]
    g = [[F(0)] * 4 for _ in range(4)]
    for i, k in enumerate((1, -1, 2, -2)):
        g[i][i] = F(k, 3)
    forms = [mm(mm(transpose(t), g), t) for t in matrices]
    assert all(q[0][0] == 0 for q in forms)
    accumulated = eye(4)
    for i in range(5):
        j = (i + 1) % 5
        change = mm(inverse(matrices[j]), matrices[i])
        assert mm(mm(transpose(change), forms[j]), change) == forms[i]
        assert mm(forms[i], inverse(forms[i])) == eye(4)
        accumulated = mm(change, accumulated)
    assert accumulated == eye(4)

    jet_cases = 0
    for k in (-3, -2, -1, 1, 2, 3):
        for order in range(8):
            # t=(tau-tau_0)/(4*pi*i). The exact solution is
            # u*v^(order+1)+(3/k)*(order+1)*t*v^order.
            forcing = F(3, k) * (order + 1) * factorial(order)
            assert forcing == F(3, k) * factorial(order + 1) != 0
            jet_cases += 1
    return {"signed_two_coordinate_cases": signed_cases,
            "four_input_pentagon_edges": 5,
            "all_five_root_slopes_zero": True,
            "all_five_full_forms_nonsingular": True,
            "finite_jet_nonclosure_controls": jet_cases}


def weyl_parity_checks():
    equations = 0
    residue_columns = 0
    for p in (3, 5, 7):
        for k in range(1, p):
            def w(r, s, j):
                return (-j - 2 * r) % p, (2 * k * s * (j + r)) % p
            for r, s, j in product(range(p), repeat=3):
                target, phase = w(r, s, j)
                # U W U and V W V have the predicted sandwich characters.
                assert (-k * j + phase - k * target) % p == (phase + 2 * k * r) % p
                vt, vp = w(r, s, (j + 1) % p)
                assert (vt + 1) % p == target and vp == (phase + 2 * k * s) % p
                # Ad_U W_rs=W_(r,s+1); Ad_V W_rs=W_(r-1,s).
                ut, up = w(r, (s + 1) % p, j)
                assert ut == target and up == (k * j + phase - k * target) % p
                vt, vp = w(r, s, (j - 1) % p)
                wt, wp = w((r - 1) % p, s, j)
                assert wt == (vt + 1) % p and wp == vp
                equations += 4
            for j in range(p):
                sums = [[0] * p for _ in range(p)]
                for r, s in product(range(p), repeat=2):
                    target, phase = w(r, s, j)
                    sums[target][phase] += 1
                # Reduce modulo 1+zeta+...+zeta^(p-1)=0 exactly.
                for target, coeffs in enumerate(sums):
                    reduced = [c - coeffs[-1] for c in coeffs[:-1]]
                    expected = [p if target == j else 0] + [0] * (p - 2)
                    assert reduced == expected
                residue_columns += 1
    return {"exact_weyl_sandwich_and_transport_equations": equations,
            "exact_residue_identity_columns": residue_columns,
            "identity": "sum_(r,s) W_(r,s)=p*I"}


def main():
    assert __debug__, "Run with assertions enabled"
    heat_cases = 0
    # Remove the common scalar 1/(4*pi*i); allow signed nonzero slopes.
    for k, l in product(range(-5, 6), repeat=2):
        if not k or not l or not k + l:
            continue
        a, b, c = F(1, k), F(1, l), F(1, k + l)
        symbol = (a - c, -2 * c, b - c)
        relative = (F(l, k * (k + l)), F(-2, k + l),
                    F(k, l * (k + l)))
        assert symbol == relative and any(symbol)
        heat_cases += 1

    isogeny_cases = 0
    for p in (3, 5, 7):
        for k, l in product(range(1, 8), repeat=2):
            total = k + l
            # x=u+l*v, y=u-k*v. Compute inverse derivative coefficients.
            uu = F(p, k) * F(k, total) ** 2 + F(p, l) * F(l, total) ** 2
            uv = 2 * (F(p, k) * F(k, total) * F(1, total)
                      - F(p, l) * F(l, total) * F(1, total))
            vv = (F(p, k) + F(p, l)) * F(1, total) ** 2
            assert (uu, uv, vv) == (F(p, total), F(0), F(p, k * l * total))
            # Direct quadratic-form and cross-holonomy cancellation.
            assert F(k, p) * l - F(l, p) * k == 0
            assert F(k, p) * l * l + F(l, p) * k * k == F(k * l * total, p)
            isogeny_cases += 1

    theta_exponents = 0
    for p in (3, 5, 7):
        for k in range(1, 8):
            for a, j, n in product(range(k), range(p), range(-3, 4)):
                r = F(a + k * n) - F(k * j, p)
                next_j, next_n = (j - 1) % p, n + int(j == 0)
                next_r = F(a + k * next_n) - F(k * next_j, p)
                assert next_r == r + F(k, p)
                assert F(p, k) * r * r + 2 * r == (
                    F(p, k) * next_r * next_r - F(k, p))
                theta_exponents += 1

    # All solutions of n^2+m^2=1 are inside this finite window.
    # Thus the chosen low coefficient has no omitted-tail contribution.
    defect = F(0)
    contributing_pairs = []
    for n, m in product(range(-3, 4), repeat=2):
        exponent = F(3, 2) * (n * n + m * m)
        if exponent == F(3, 2) and n + m == 1:
            defect += exponent - F((n + m) ** 2, 1) / (2 * F(2, 3))
            contributing_pairs.append([n, m])
    assert contributing_pairs == [[0, 1], [1, 0]]
    assert defect == F(3, 2)

    report = {
        "status": "PASS",
        "arithmetic": "Exact rational arithmetic; no floating-point theta evaluation",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "rational_heat_symbol_cases": heat_cases,
        "positive_isogeny_cases": isogeny_cases,
        "vector_theta_exponent_checks": theta_exponents,
        "signed_and_zero_channels": signed_and_zero_checks(),
        "mixed_kernel_weyl_residue": weyl_parity_checks(),
        "p3_k1_l1_defect": {
            "input_component": "sum_n q^(3*n^2/2)*w^n, squared",
            "monomial": "q^(3/2)*w",
            "operator": "H_(2/3)/(2*pi*i)",
            "contributing_pairs": contributing_pairs,
            "exact_coefficient": str(defect),
        },
        "limits": [
            "Finite algebraic controls; universal proofs belong to TH1--TH5",
            "No numerical convergence or Serre-duality certification",
            "Signed coordinate transport retains every relative coordinate and descent data",
            "No dimension-reducing signed-degree horizontal sewing",
            "No Felder dynamical fusion or Bol-specific analytic identity",
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
