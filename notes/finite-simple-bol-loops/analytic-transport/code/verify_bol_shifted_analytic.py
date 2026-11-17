#!/usr/bin/env python3
"""Exact finite controls for bol-shifted-analytic-fusion.md.

No numerical ODE integration is used.  Analytic convergence and estimates are
proved in SA1--SA5; this script checks finite marked operators, zero/dual
channels, the compact dynamical twist, and the cubic comparison formulas.
Python standard library only.  All phases are recorded as exponents modulo 3;
when added they use the exact ring Q[w]/(w^2+w+1).
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


def mul(p, q):
    """Monomial product: right factor acts first."""
    return tuple((p[j][0], (e + p[j][1]) % 3) for j, e in q)


def inv(p):
    ans = [None] * len(p)
    for i, (j, e) in enumerate(p):
        ans[j] = (i, -e % 3)
    return tuple(ans)


def ident(n):
    return tuple((i, 0) for i in range(n))


def cycle_phases(p):
    seen, counts = set(), Counter()
    for start in range(len(p)):
        if start in seen:
            continue
        j, length, phase = start, 0, 0
        while j not in seen:
            seen.add(j)
            j, e = p[j]
            length += 1
            phase += e
        assert j == start
        counts[length, phase % 3] += 1
    return [[length, phase, count]
            for (length, phase), count in sorted(counts.items())]


def phase(e):
    return ((Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(1)),
            (Fraction(-1), Fraction(-1)))[e % 3]


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def scale(k, x):
    return (k * x[0], k * x[1])


def dot(x, y):
    return sum(a * b for a, b in zip(x, y)) % 3


def rigid_charge_control():
    charges = list(itertools.product(range(3), repeat=3))
    index = {q: i for i, q in enumerate(charges)}

    def sigma(q):
        a, b, c = q
        return ((a - b + c) % 3, (b - c) % 3, c)

    def sigma_inv(q):
        a, b, c = q
        return ((a + b) % 3, (b + c) % 3, c)

    f, fp, z = (1, 2, 1), (1, 2, 0), (0, 1, 1)
    pure = tuple((index[sigma(q)], 0) for q in charges)
    h = inv(pure)
    graph = lambda f0: tuple((index[sigma(q)], dot(sigma(q), f0))
                            for q in charges)
    g, gp = graph(f), graph(fp)
    dz = tuple((i, dot(q, z)) for i, q in enumerate(charges))
    assert mul(mul(dz, g), inv(dz)) == gp
    assert cycle_phases(g) == cycle_phases(gp)
    assert mul(g, h) == tuple((i, dot(q, f))
                              for i, q in enumerate(charges))
    assert mul(h, g) == tuple((i, dot(sigma(q), f))
                              for i, q in enumerate(charges))
    assert all(sigma_inv(sigma(q)) == q for q in charges)

    # Exact rational coefficient proxy for the algebraic inverse. The actual
    # positive analytic c1,c2 and their lower separation are proved in SA2.
    c1, c2 = Fraction(1), Fraction(2)
    sf = [phase(dot(q, f)) for q in charges]
    sfp = [phase(dot(q, fp)) for q in charges]

    def measurement(s):
        return [add(scale(c1, s[i]), scale(c2, s[index[sigma(q)]]))
                for i, q in enumerate(charges)]

    def recover(m):
        # (c1 I+c2 S)^-1=(c1^2 I-c1 c2 S+c2^2 S^2)/(c1^3+c2^3).
        ans = []
        for i, q in enumerate(charges):
            j, k = index[sigma(q)], index[sigma(sigma(q))]
            v = add(add(scale(c1*c1, m[i]), scale(-c1*c2, m[j])),
                    scale(c2*c2, m[k]))
            ans.append(scale(1/(c1**3+c2**3), v))
        return ans

    mf, mfp = measurement(sf), measurement(sfp)
    assert recover(mf) == sf
    assert recover(mfp) == sfp
    differing = [q for i, q in enumerate(charges) if mf[i] != mfp[i]]
    assert len(differing) == 18

    # Entire-response marking ablation follows from simultaneous conjugacy.
    # Verify every word through length 8, not just GH or one spectrum.
    hp = mul(mul(dz, h), inv(dz))
    word_checks = 0
    for n in range(9):
        for word in itertools.product(range(2), repeat=n):
            old, new = ident(27), ident(27)
            for letter in word:
                old = mul((g, h)[letter], old)
                new = mul((gp, hp)[letter], new)
            assert mul(mul(dz, old), inv(dz)) == new
            # D_z is block scalar: each diagonal block trace is preserved.
            for i in range(27):
                assert ((old[i][1] if old[i][0] == i else None)
                        == (new[i][1] if new[i][0] == i else None))
            word_checks += 1
    q = (1, 1, 1)
    assert (dot(q, f), dot(sigma(q), f)) == (1, 2)
    assert (dot(q, fp), dot(sigma(q), fp)) == (0, 1)
    return {
        "charge_count": len(charges),
        "graph_cycle_phase_polynomials": cycle_phases(g),
        "same_graph_spectra_by_exact_conjugation": True,
        "changed_marked_mixed_response_channels": len(differing),
        "exact_inverse_coefficient_proxy": [1, 2],
        "simultaneous_marking_ablation_words": word_checks,
        "source_charge_111_phases": [1, 2],
        "isotope_charge_111_phases": [0, 1],
    }


def permutation_compose(p, q):
    return tuple(p[j] for j in q)


def permutation_inverse(p):
    q = [0] * len(p)
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def permutation_cycles(p):
    return [[length, count] for length, phase0, count in
            cycle_phases(tuple((j, 0) for j in p)) if phase0 == 0]


def fixed(p):
    return sum(i == j for i, j in enumerate(p))


def cubic_control(p, exhaustive_bol=False):
    points = list(itertools.product(range(p), repeat=3))
    index = {x: i for i, x in enumerate(points)}
    n = len(points)
    ji = tuple(index[tuple(-a % p for a in x)] for x in points)
    outputs = []
    all_translation_cycles = []
    associator_maps = []

    def product(k, x, y):
        c, a, b = x
        d, u, v = y
        return ((c+d+b*u*(a+u)+k*(a*v-b*u)) % p,
                (a+u) % p, (b+v) % p)

    for k in (0, 1):
        translations = [tuple(index[product(k, x, y)] for y in points)
                        for x in points]
        all_translation_cycles.append([permutation_cycles(h)
                                       for h in translations])
        selected = translations[index[(0, 1, 0)]]
        hi = permutation_inverse(selected)
        assert permutation_cycles(selected) == [[p, p*p]]

        # Sparse exact commutator [J,(h+h^-1)/2].
        squared = Fraction(0)
        for col in range(n):
            values = defaultdict(Fraction)
            values[ji[selected[col]]] += Fraction(1, 2)
            values[ji[hi[col]]] += Fraction(1, 2)
            values[selected[ji[col]]] -= Fraction(1, 2)
            values[hi[ji[col]]] -= Fraction(1, 2)
            squared += sum(value*value for value in values.values())
        expected = 0 if k == 0 else p*p*(p-1)
        assert squared == expected

        traces = []
        for r, s in ((selected, selected), (selected, hi),
                     (hi, selected), (hi, hi)):
            traces.append(fixed(permutation_compose(
                ji, permutation_compose(r, permutation_compose(ji, s)))))
        assert traces == ([n, 0, 0, n] if k == 0 else [p*p, 0, 0, p*p])

        # Exact association-defect formula on every pair and test point for p=3.
        if exhaustive_bol:
            defect_record = []
            bol_checks = 0
            for x in points:
                for y in points:
                    xy = product(k, x, y)
                    inv_lxy = permutation_inverse(translations[index[xy]])
                    defect = permutation_compose(
                        inv_lxy, permutation_compose(translations[index[x]],
                                                    translations[index[y]]))
                    delta = (x[1]*y[2]-x[2]*y[1]) % p
                    expected_defect = tuple(index[((d-delta*u) % p, u, v)]
                                            for d, u, v in points)
                    assert defect == expected_defect
                    defect_record.append(defect)
                    for z in points:
                        assert product(k, x, product(k, y, product(k, x, z))) == \
                               product(k, product(k, x, product(k, y, x)), z)
                        bol_checks += 1
            associator_maps.append(defect_record)
            x, y = (0, 1, 0), (0, 0, 1)
            assert product(k, product(k, x, y), x) != \
                   product(k, x, product(k, y, x))
        else:
            bol_checks = 0

        outputs.append({
            "k": k,
            "selected_translation_cycles": permutation_cycles(selected),
            "inversion_cycles": permutation_cycles(ji),
            "commutator_HS_squared": int(squared),
            "normalized_HS_squared": str(squared/n),
            "four_mixed_permutation_traces": traces,
            "exhaustive_Bol_equations": bol_checks,
        })

    assert all_translation_cycles[0] == all_translation_cycles[1]
    if exhaustive_bol:
        assert associator_maps[0] == associator_maps[1]

    # Independent associative additive-group comparison, not a renamed Q_0.
    hgroup = tuple(index[(d, (u+1) % p, v)] for d, u, v in points)
    assert permutation_compose(ji, permutation_compose(hgroup, ji)) == \
           permutation_inverse(hgroup)
    return {
        "p": p,
        "order": n,
        "all_individual_translation_cycles_equal": True,
        "all_associator_defects_equal_at_p3": exhaustive_bol,
        "associative_additive_control_commutes_with_symmetric_translation": True,
        "proper_Bol_controls": outputs,
    }


def vec_add(x, y):
    return tuple((a+b) % 3 for a, b in zip(x, y))


def vec_sub(x, y):
    return tuple((a-b) % 3 for a, b in zip(x, y))


def vec_scale(c, x):
    return tuple(c*a % 3 for a in x)


def inverse_f(lam, v):
    # The bilinear form has C=((0,2),(1,0)), so the map x -> F_lam(x, .)
    # is C^T+lam I in column coordinates. Its determinant is lam^2+1.
    a = lam % 3
    det_inverse = pow((a*a+1) % 3, -1, 3)
    return ((det_inverse*(a*v[0]-v[1])) % 3,
            (det_inverse*(-2*v[0]+a*v[1])) % 3)


def dynamical_controls():
    w = list(itertools.product(range(3), repeat=2))
    checks, zero_checks = 0, 0
    inverse_checks = 0
    for lam, v in itertools.product(range(3), w):
        u = inverse_f(lam, v)
        # Evaluate the actual bilinear form u^T(C+lam I)y on y=e_0,e_1.
        assert ((lam*u[0]+u[1]) % 3, (2*u[0]+lam*u[1]) % 3) == v
        inverse_checks += 1
    for lam, nu, xi in itertools.product(range(3), repeat=3):
        for x, y, z in itertools.product(w, repeat=3):
            # DD8 left: J_(X tensor Y,Z)(lam)(J_XY(lam-xi) tensor I).
            s_xy = inverse_f(lam-xi-nu, vec_scale(nu, y))
            s_z = inverse_f(lam-xi, vec_scale(xi, z))
            left = (vec_sub(vec_sub(x, s_xy), s_z),
                    vec_sub(y, s_z), z)
            # DD8 right: J_(X,Y tensor Z)(lam)(I tensor J_YZ(lam)).
            ynew = vec_sub(y, s_z)
            s_yz = inverse_f(lam-nu-xi,
                             vec_add(vec_scale(nu, ynew), vec_scale(xi, z)))
            right = (vec_sub(x, s_yz), ynew, z)
            assert left == right
            checks += 1
            if nu == 0 or xi == 0 or (nu+xi) % 3 == 0:
                zero_checks += 1

    # A noncentral first-axis collective residue is genuinely changed by J.
    lam, nu, s = 0, 1, (1, 0)
    changed = 0
    for x, y in itertools.product(w, repeat=2):
        jxy = (vec_sub(x, inverse_f(lam-nu, vec_scale(nu, y))), y)
        after_axis = (vec_sub(jxy[0], s), vec_sub(jxy[1], s))
        conjugated = (vec_add(after_axis[0],
                              inverse_f(lam-nu, vec_scale(nu, after_axis[1]))),
                       after_axis[1])
        ordinary = (vec_sub(x, s), vec_sub(y, s))
        changed += conjugated != ordinary
    assert changed == 81
    return {"completion_inverse_checks": inverse_checks,
            "shifted_threefold_equations": checks,
            "equations_with_zero_or_zero_sum_later_charge": zero_checks,
            "noncentral_collective_symbol_changed_basis_states": changed}


def tensor_and_dual_controls():
    # Genuine CH charge (1,1)->2 intertwiner in the smallest W=F_3 control.
    pairs = list(itertools.product(range(3), repeat=2))
    idx = {x: i for i, x in enumerate(pairs)}
    cf = tuple((idx[((2*(x+y)) % 3, (x-y) % 3)], 0) for x, y in pairs)
    equations = 0
    for s, t, z in itertools.product(range(3), repeat=3):
        def charged(charge):
            return tuple(((x-s) % 3,
                          charge*(z+x*t-2*s*t) % 3) for x in range(3))

        rho = charged(1)
        tensor = tuple((idx[(rho[x][0], rho[y][0])],
                        (rho[x][1]+rho[y][1]) % 3) for x, y in pairs)
        out2 = charged(2)
        output = tuple((idx[(out2[u][0], v)], out2[u][1]) for u, v in pairs)
        assert mul(cf, tensor) == mul(output, cf)
        equations += 9

        # Full zero sector is dimension 9, not its scalar invariant line.
        dual = tuple((j, -e % 3) for j, e in rho)
        zero = tuple((idx[(dual[x][0], rho[y][0])],
                      (dual[x][1]+rho[y][1]) % 3) for x, y in pairs)
        for (x, y), (dest, exponent) in zip(pairs, zero):
            xp, yp = pairs[dest]
            assert (xp == yp) == (x == y)
            if x == y:
                assert exponent == 0
        # Coevaluation is the full sum of diagonal basis states.
        assert {zero[idx[(x, x)]][0] for x in range(3)} == \
               {idx[(x, x)] for x in range(3)}

    # Augmentation preserves a unit but is collective rather than primitive.
    omega, one = phase(1), phase(0)
    collective = add(phase(2), scale(-1, one))
    primitive = scale(2, add(omega, scale(-1, one)))
    assert collective != primitive
    return {"regular_charge_intertwiner_equations": equations,
            "true_dual_tensor_dimension": 9,
            "dual_evaluation_checks": 27*9,
            "augmented_collective_symbol_is_not_primitive": True}


def rational_estimate_controls():
    # Analytic L<11/10 and exp(2rL)<500/489 are proved in the manuscript.
    r, l_bound, exp_bound = Fraction(1, 100), Fraction(11, 10), Fraction(500, 489)
    finite_amplitude_error = r*l_bound**3*exp_bound
    gap_bracket = Fraction(2, 15)-Fraction(8, 3)*finite_amplitude_error
    assert finite_amplitude_error < Fraction(14, 1000)
    assert gap_bracket > Fraction(9, 100)
    delta = Fraction(1, 2000000)
    phase_error = 3*(finite_amplitude_error+3*delta/r**2)
    assert phase_error < Fraction(87, 1000)
    w = r**4
    k_bound = Fraction(17, 50)
    third_exp_bound = Fraction(128, 125)
    assert 1/(1-2*r*l_bound-2*w*k_bound) < third_exp_bound
    third_perturbation = 2*w*k_bound*third_exp_bound
    assert third_perturbation < Fraction(7, 1000000000)
    third_phase_error = 3*(finite_amplitude_error +
                          4*third_perturbation/r**2 + 4*delta/r**2)
    assert third_phase_error < Fraction(103, 1000)
    return {"amplitude": str(r),
            "measurement_error": str(delta),
            "upper_phase_error_less_than": "87/1000",
            "normalized_transport_gap_greater_than": "9/1000000",
            "noncentral_third_amplitude": str(w),
            "third_residue_phase_error_less_than": "103/1000",
            "no_numerical_ODE_integration": True}


def main():
    if not __debug__:
        raise RuntimeError("Exact checks require assertions; run Python without -O.")
    result = {
        "schema": 1,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "exact integers, finite fields, Fractions, monomial phase exponents",
        "rigid_marked_charge_control": rigid_charge_control(),
        "collective_tensor_and_true_dual": tensor_and_dual_controls(),
        "dynamical_twist": dynamical_controls(),
        "cubic_controls": [cubic_control(3, True), cubic_control(5)],
        "analytic_constant_rational_controls": rational_estimate_controls(),
        "limits": [
            "The universal analytic proofs are SA1-SA5, not these finite tests.",
            "The large rigid W-space is not enumerated; its exact charge register is tested.",
            "The proper cubic controls are known nonsimple loops, not new simple-loop classifications.",
            "No independent mathematical review is asserted by this executable.",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
