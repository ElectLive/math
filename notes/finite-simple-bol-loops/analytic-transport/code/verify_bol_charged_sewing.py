"""Exact charged Heisenberg, degree-carry, and local-current controls.

Python 3.11+, standard library only; run with assertions enabled.
The rigid B_i matrices are exactly equations (1)--(2) at source
2a25b81e3efe5bdd8a3923e27c94aef16a559094, odd-rigid-center-nongloop.md.
No huge loop, field extension, or induced set is enumerated. This is a
manual finite certificate, not CI, formal verification, or an analytic
convergence proof. All new universal proofs belong to their manuscripts.
"""

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path


P = 3
HALF = 2
ROOTS = ((1, 0), (0, 1), (-1, -1))
B_RIGID = [
    [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 2, 0, 0]],
    [[0, 0, 0, 2], [0, 1, 1, 0], [0, 1, 0, 0], [2, 0, 0, 0]],
    [[0, 2, 1, 1], [1, 1, 0, 2], [2, 2, 0, 0], [0, 1, 0, 0]],
]


def vectors(d):
    return list(product(range(P), repeat=d))


def add(a, b):
    return tuple((x + y) % P for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x % P for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b)) % P


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return list(map(list, zip(*a)))


def mv(a, x):
    return tuple(dot(row, x) for row in a)


def mm(a, b):
    return [[dot(row, col) for col in zip(*b)] for row in a]


def madd(a, b, c=1):
    return [[(x + c * y) % P for x, y in zip(row, other)]
            for row, other in zip(a, b)]


def rank(rows):
    a = [list(row) for row in rows]
    if not a:
        return 0
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inverse = pow(a[r][j], -1, P)
        a[r] = [inverse * x % P for x in a[r]]
        for i in range(len(a)):
            if i != r:
                coefficient = a[i][j]
                a[i] = [(x - coefficient * y) % P for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def inverse(a):
    n = len(a)
    out = [row[:] + unit for row, unit in zip(a, eye(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if out[i][j])
        out[j], out[pivot] = out[pivot], out[j]
        c = pow(out[j][j], -1, P)
        out[j] = [c * x % P for x in out[j]]
        for i in range(n):
            if i != j:
                c = out[i][j]
                out[i] = [(x - c * y) % P for x, y in zip(out[i], out[j])]
    return [row[n:] for row in out]


def scalar_form(forms, ell):
    n = len(forms[0])
    return [[sum(c * b[i][j] for c, b in zip(ell, forms)) % P
             for j in range(n)] for i in range(n)]


def bvalue(forms, x, y):
    return tuple(dot(x, mv(b, y)) for b in forms)


def group_multiply(forms, g, h):
    x, y, z = g
    xx, yy, zz = h
    bracket = add(bvalue(forms, x, yy), scale(-1, bvalue(forms, xx, y)))
    return add(x, xx), add(y, yy), add(add(z, zz), scale(HALF, bracket))


def schrodinger_basis_action(forms, ell, g, t):
    """rho(g) delta_t = zeta^phase delta_(t-x), with CH2 convention."""
    x, y, z = g
    phase = dot(ell, add(z, add(bvalue(forms, t, y),
                               scale(-HALF, bvalue(forms, x, y)))))
    return add(t, scale(-1, x)), phase


def representation_and_fusion_checks():
    forms = [[[1]]]
    ws, zs = vectors(1), vectors(1)
    group = list(product(ws, ws, zs))
    products = 0
    for ell in zs:
        for g in group:
            for h in group:
                gh = group_multiply(forms, g, h)
                for t in ws:
                    ht, hp = schrodinger_basis_action(forms, ell, h, t)
                    gt, gp = schrodinger_basis_action(forms, ell, g, ht)
                    target, phase = schrodinger_basis_action(forms, ell, gh, t)
                    assert target == gt and phase == (gp + hp) % P
                    products += 1

    # A two-dimensional pencil with every nonzero scalar form invertible.
    # L_ell is the transpose scalar matrix, since L_ell(x)(y)=x^t B_ell y.
    forms = [eye(2), [[0, 2], [1, 0]]]
    charges, ws = vectors(2), vectors(2)
    linear = {ell: transpose(scalar_form(forms, ell)) for ell in charges}
    assert all(rank(linear[ell]) == 2 for ell in charges if any(ell))
    zero_w, zero_z = (0, 0), (0, 0)
    generators = [(e, zero_w, zero_z) for e in eye(2)]
    generators += [(zero_w, e, zero_z) for e in eye(2)]
    generators += [(zero_w, zero_w, e) for e in eye(2)]
    fusion_checks, pairs = 0, 0
    for ell in charges:
        for mu in charges:
            gamma = add(ell, mu)
            if not any(gamma):
                continue
            pairs += 1
            inv = inverse(linear[gamma])
            for x in ws:
                for y in ws:
                    u = mv(inv, add(mv(linear[ell], x), mv(linear[mu], y)))
                    v = add(x, scale(-1, y))
                    assert add(u, mv(mm(inv, linear[mu]), v)) == x
                    assert add(u, scale(-1, mv(mm(inv, linear[ell]), v))) == y
                    for g in generators:
                        xx, phase_x = schrodinger_basis_action(forms, ell, g, x)
                        yy, phase_y = schrodinger_basis_action(forms, mu, g, y)
                        uu, phase_u = schrodinger_basis_action(forms, gamma, g, u)
                        transformed = mv(inv, add(mv(linear[ell], xx),
                                                   mv(linear[mu], yy)))
                        assert transformed == uu and add(xx, scale(-1, yy)) == v
                        assert (phase_x + phase_y) % P == phase_u
                        fusion_checks += 1

    f_moves, triples = 0, 0
    for ell, mu, nu in product(charges, repeat=3):
        if not all(any(charge) for charge in (ell, mu, nu)):
            continue
        e, f, d = add(ell, mu), add(mu, nu), add(add(ell, mu), nu)
        if not all(any(charge) for charge in (e, f, d)):
            continue
        triples += 1
        a, b, c = linear[ell], linear[mu], linear[nu]
        ei, fi, di = inverse(linear[e]), inverse(linear[f]), inverse(linear[d])
        for unit in eye(4):
            v, w = tuple(unit[:2]), tuple(unit[2:])
            z = scale(-1, mv(mm(di, linear[e]), w))
            inner = add(z, w)
            x = add(inner, mv(mm(ei, b), v))
            y = add(inner, scale(-1, mv(mm(ei, a), v)))
            vv = add(y, scale(-1, z))
            ww = add(x, scale(-1, mv(fi, add(mv(b, y), mv(c, z)))))
            formula_v = add(w, scale(-1, mv(mm(ei, a), v)))
            formula_w = add(mv(madd(eye(2), mm(mm(fi, c), mm(ei, a)), -1), v),
                            mv(mm(fi, c), w))
            assert (vv, ww) == (formula_v, formula_w)
            assert add(ww, scale(-1, mv(mm(fi, c), vv))) == v
            assert add(vv, mv(mm(ei, a), v)) == w
            assert mv(di, add(add(mv(a, x), mv(b, y)), mv(c, z))) == zero_w
            f_moves += 1
    return {"exact_monomial_representation_checks": products,
            "regular_sum_charge_pairs": pairs,
            "charged_fusion_generator_basis_checks": fusion_checks,
            "regular_tree_triples": triples,
            "F_move_and_inverse_basis_checks": f_moves,
            "scope": "Finite intertwiner equations; universal pentagon proved in CH2"}


def omega(x, y):
    d = len(x) // 2
    return (dot(x[:d], y[d:]) - dot(y[:d], x[d:])) % P


def zero_algebra_checks():
    cases = [(1, (1, 0), (0, 2), "one_degree_nondegenerate"),
             (2, (1, 0, 0, 0), (0, 0, 2, 0), "two_degrees_nondegenerate"),
             (2, (1, 0, 0, 0), (0, 1, 0, 0), "two_degrees_isotropic"),
             (2, (1, 0, 0, 0), (2, 0, 0, 0), "two_degrees_dependent"),
             (2, (0, 0, 0, 0), (0, 0, 0, 0), "two_degrees_identity")]
    report = []
    for d, u, v, name in cases:
        ambient = vectors(2 * d)
        perp = [x for x in ambient if omega(u, x) == omega(v, x) == 0]
        center = [x for x in perp if all(omega(x, y) == 0 for y in perp)]
        s = rank([u, v])
        t = int(omega(u, v) != 0)
        radical_dimension, matrix_exponent = s - 2 * t, d - s + t
        assert len(perp) == P ** (2 * d - s)
        assert len(center) == P ** radical_dimension
        assert len(perp) == len(center) * (P ** matrix_exponent) ** 2
        assert any(omega(x, y) for x in perp for y in perp) == (matrix_exponent > 0)
        # Direct exact character trace for every Weyl basis vector.
        forms, ell = [eye(d)], (1,)
        for x in ambient:
            total = [0, 0]
            g = (x[:d], x[d:], (0,))
            for basis in vectors(d):
                target, phase = schrodinger_basis_action(forms, ell, g, basis)
                if target == basis:
                    for j, coefficient in enumerate(ROOTS[phase]):
                        total[j] += coefficient
            assert total == ([P ** d, 0] if not any(x) else [0, 0])
        report.append({"case": name, "irreducible_dimension": P ** d,
                       "common_zero_dimension": len(perp),
                       "scalar_blocks": len(center),
                       "matrix_block_size": P ** matrix_exponent})
    return report


def carry_checks():
    charges, c = vectors(3), (1, 0, 1)
    section = {ell: -dot(ell, c) % P for ell in charges}
    def carry(ell, mu):
        value = section[ell] + section[mu] - section[add(ell, mu)]
        assert value % P == 0 and value // P in (0, 1)
        return value // P
    pairs = {(ell, mu): carry(ell, mu) for ell in charges for mu in charges}
    for ell, mu, nu in product(charges, repeat=3):
        assert (pairs[ell, mu] + pairs[add(ell, mu), nu]
                == pairs[mu, nu] + pairs[ell, add(mu, nu)])
    cyclic = 0
    for ell in charges:
        accum, total = (0, 0, 0), 0
        for _ in range(P):
            total += carry(accum, ell)
            accum = add(accum, ell)
        assert not any(accum) and total == section[ell]
        cyclic += int(total != 0)

    # Actual charged automorphy consistency, c=-1, with normalized k=ell.
    forms, us = [[[1]]], [(1,), (2,)]
    automorphy = 0
    for ell_value in (1, 2):
        ell = (ell_value,)
        u, v = ((1,), (0,), (0,)), ((0,), (2,), (0,))
        for k in range(-6, 7):
            if k % P != ell_value:
                continue
            for basis in vectors(1):
                vb, vp = schrodinger_basis_action(forms, ell, v, basis)
                uvb, uvp = schrodinger_basis_action(forms, ell, u, vb)
                ub, up = schrodinger_basis_action(forms, ell, u, basis)
                vub, vup = schrodinger_basis_action(forms, ell, v, ub)
                assert uvb == vub and (vp + uvp - up - vup + k) % P == 0
                automorphy += 1
            assert Fraction(P * k, P).denominator == 1
    return {"finite_charge_count": len(charges),
            "exact_carry_pairs": len(pairs),
            "exact_triple_cocycle_checks": len(charges) ** 3,
            "nonsplit_cyclic_charge_restrictions": cyclic,
            "exact_projective_automorphy_basis_checks": automorphy,
            "normalized_dual_labels": [1, 2],
            "normalized_dual_output_label": 3,
            "true_dual_labels": [1, -1],
            "true_dual_output_label": 0,
            "rank3_normalized_bundle_degrees": [1, 2],
            "rank9_normalized_bundle_degrees": [3, 6],
            "scope": "Geometric degree labels, not conformal weights"}


def poly_add(a, b, scale_b=1):
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = (out.get(monomial, 0) + scale_b * coefficient) % P
    return {m: c for m, c in out.items() if c}


def poly_multiply(a, b):
    out = {}
    for x, c in a.items():
        for y, d in b.items():
            monomial = tuple(i + j for i, j in zip(x, y))
            out[monomial] = (out.get(monomial, 0) + c * d) % P
    return {m: c for m, c in out.items() if c}


def poly_det(matrix):
    n, out = len(matrix), {}
    for perm in permutations(range(n)):
        sign = (-1) ** sum(perm[i] > perm[j]
                           for i in range(n) for j in range(i + 1, n))
        term = {(0, 0, 0): 1}
        for i in range(n):
            term = poly_multiply(term, matrix[i][perm[i]])
        out = poly_add(out, term, sign)
    return out


def rigid_matrix_and_gauge_checks():
    variables = [{tuple(int(i == j) for i in range(3)): 1} for j in range(3)]
    def linear(coefficients):
        out = {}
        for c, variable in zip(coefficients, variables):
            out = poly_add(out, variable, c)
        return out
    b_poly = [[linear([b[i][j] for b in B_RIGID]) for j in range(4)]
              for i in range(4)]
    q = {(0, 2, 0): 1, (0, 1, 1): 2, (0, 0, 2): 2, (1, 0, 1): 1}
    c_coefficients = [
        [(0, 0, 0), (0, 0, 0), (-1, 0, 1), (0, -1, 1)],
        [(0, 0, 0), (0, 0, 0), (0, 1, 0), (0, 0, -1)],
        [(1, 0, -1), (0, 1, -1), (0, -1, -1), (0, 0, -1)],
        [(0, -1, 0), (0, 0, 1), (0, 0, 1), (0, 0, 0)],
    ]
    assert poly_det(b_poly) == poly_multiply(q, q)
    for i in range(4):
        for j in range(4):
            minor = [[b_poly[r][s] for s in range(4) if s != i]
                     for r in range(4) if r != j]
            adj = poly_add({}, poly_det(minor), (-1) ** (i + j))
            assert adj == poly_multiply(q, linear(c_coefficients[i][j]))
    charges = vectors(3)
    ranks = {ell: rank(scalar_form(B_RIGID, ell)) for ell in charges}
    assert Counter(ranks.values()) == {0: 1, 2: 8, 4: 18}

    r = [[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]]
    for i, b in enumerate(B_RIGID):
        expected = b if i == 0 else madd(b, B_RIGID[i - 1])
        assert mm(mm(transpose(r), b), inverse(r)) == expected
    t = [[1, 0, 0], [1, 1, 0], [0, 1, 1]]
    sigma = [[1, 0, 0], [0, 2, 0], [0, 1, 1]]
    powers = [eye(3)]
    for _ in range(9):
        powers.append(mm(powers[-1], t))
    assert powers[3] == powers[9] == eye(3)
    f = (1, 2, 1)
    base = [(0, 0, 0)]
    for j in range(9):
        base.append(add(base[-1], mv(powers[j], f)))
    assert base[3] == (0, 0, 1) and not any(base[9])
    gauge_checks, fusion_phases = 0, 0
    for shift in range(P):
        z = (0, shift, shift)
        shifted_generator = add(f, (0, 0, -shift % P))
        shifted = [(0, 0, 0)]
        for j in range(9):
            shifted.append(add(shifted[-1], mv(powers[j], shifted_generator)))
        for j in range(9):
            inv_t = inverse(powers[j])
            assert shifted[j] == add(base[j], add(z, scale(-1, mv(powers[j], z))))
            assert mv(sigma, shifted[j]) == mv(inv_t, shifted[j])
            for ell in charges:
                out = mv(transpose(inv_t), ell)
                phase_difference = dot(out, add(shifted[j], scale(-1, base[j])))
                assert phase_difference == (dot(out, z) - dot(ell, z)) % P
                gauge_checks += 1
        for ell in charges:
            for mu in charges:
                assert (dot(ell, z) + dot(mu, z)) % P == dot(add(ell, mu), z)
                fusion_phases += 1
    return {"matrix_source": "2a25b81e3efe5bdd8a3923e27c94aef16a559094 equations(1)-(2)",
            "exact_polynomial_determinant_identity": "det B=(y^2-yz-z^2+xz)^2",
            "exact_polynomial_adjugate_entries": 16,
            "full_b_rank_histogram": dict(sorted(Counter(ranks.values()).items())),
            "large_field_trace_rank_histogram": {0: 1, 36: 8, 72: 18},
            "graph_transport_gauge_phase_checks": gauge_checks,
            "charge_junction_gauge_checks": fusion_phases,
            "fixed_raw_epsilon2_boundary_phases": [1, 0, 2],
            "limit": "Graph-only closed networks erase shifts; separately fixed marks do not"}


def cubic_associative_quotient():
    elements = vectors(3)
    lookup = {x: i for i, x in enumerate(elements)}
    reports = []
    for k in (0, 1):
        def multiply(x, y):
            c, a, b = x
            d, u, v = y
            return ((c + d + b * u * (a + u) + k * (a * v - b * u)) % P,
                    (a + u) % P, (b + v) % P)
        table = [[lookup[multiply(x, y)] for y in elements] for x in elements]
        parent = list(range(27))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            parent[y] = x
            return True
        associative_triples = 0
        for x, y, z in product(range(27), repeat=3):
            union(table[table[x][y]][z], table[x][table[y][z]])
            associative_triples += 1
        rounds, contexts = 0, 0
        while True:
            changed = False
            rounds += 1
            for x, y in product(range(27), repeat=2):
                if find(x) == find(y):
                    for z in range(27):
                        changed |= union(table[z][x], table[z][y])
                        changed |= union(table[x][z], table[y][z])
                        contexts += 2
            if not changed:
                break
        classes = {}
        for i, x in enumerate(elements):
            classes.setdefault(find(i), set()).add(x)
        expected = [{(c, a, b) for c in range(P)} for a, b in vectors(2)]
        assert {frozenset(x) for x in classes.values()} == set(map(frozenset, expected))
        x, y, z = (0, 1, 0), (0, 0, 1), (0, 1, 0)
        left, right = multiply(multiply(x, y), z), multiply(x, multiply(y, z))
        assert left == (2, 2, 1) and right == (1, 2, 1)
        for xx, yy in product(elements, repeat=2):
            assert multiply(xx, yy)[1:] == add(xx[1:], yy[1:])
        reports.append({"parameter_k": k, "associative_triples": associative_triples,
                        "left_right_context_checks": contexts, "closure_rounds": rounds,
                        "congruence_classes": len(classes), "each_class_size": 3,
                        "quotient": "additive F3^2", "left_witness": left,
                        "right_witness": right})
    return reports


def main():
    assert __debug__, "Run with assertions enabled"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()
    report = {"status": "PASS", "arithmetic": "Exact F3, Z[zeta_3], polynomials and rationals",
              "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "charged_representations": representation_and_fusion_checks(),
              "zero_algebras": zero_algebra_checks(),
              "geometric_degree_carry": carry_checks(),
              "rigid_matrix_and_gauge": rigid_matrix_and_gauge_checks(),
              "cubic_associative_quotient": cubic_associative_quotient(),
              "limits": ["No huge multiplication table or induced set",
                         "No independent review of inherited proper-loop interfaces",
                         "No CI, formal verification, or analytic convergence proof",
                         "Geometric degree is not conformal weight",
                         "No nonabelian fusion-compatible analytic connection is certified"]}
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.certificate:
        args.certificate.write_text(encoded)
        print(json.dumps({"status": "PASS", "script_sha256": report["script_sha256"],
                          "certificate": str(args.certificate),
                          "fusion_checks": report["charged_representations"][
                              "charged_fusion_generator_basis_checks"],
                          "carry_triples": 19683,
                          "associative_quotient_classes_each": 9}, indent=2))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
