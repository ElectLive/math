"""Exact small controls for the DD finite dynamical fusion construction.

Python 3.11+, standard library only; run with assertions enabled.
The control uses p=3, W=F3^2, Z=F3, b_lambda=lambda I, and
C=((0,2),(1,0)). It tests physical zero sectors as well as nonzero ones.
It does not construct the huge loop, prove an elliptic connection, or
replace the universal proofs in bol-dynamical-fusion-construction.md.
"""

import argparse
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


P = 3
HALF = 2
ZERO = (0, 0)
W = list(product(range(P), repeat=2))
I = ((1, 0), (0, 1))
C = ((0, 2), (1, 0))


def add(x, y):
    return tuple((a + b) % P for a, b in zip(x, y))


def scale(a, x):
    return tuple(a * b % P for b in x)


def dot(x, y):
    return sum(a * b for a, b in zip(x, y)) % P


def mv(a, x):
    return tuple(dot(row, x) for row in a)


def transpose(a):
    return tuple(zip(*a))


def inverse(a):
    determinant = (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % P
    k = pow(determinant, -1, P)
    return ((k * a[1][1] % P, -k * a[0][1] % P),
            (-k * a[1][0] % P, k * a[0][0] % P))


FORMS = {lam: tuple(tuple((C[i][j] + lam * I[i][j]) % P
                         for j in range(2)) for i in range(2))
         for lam in range(P)}
# F(x)(y)=x^t FORMS y: the column coordinate of F(x) is FORMS^t x.
MAPS = {lam: transpose(FORMS[lam]) for lam in range(P)}
INVERSES = {lam: inverse(MAPS[lam]) for lam in range(P)}


def form(lam, x, y):
    return dot(x, mv(FORMS[lam], y))


def group_multiply(g, h):
    x, y, z = g
    xx, yy, zz = h
    return (add(x, xx), add(y, yy),
            (z + zz + HALF * (dot(x, yy) - dot(xx, y))) % P)


def projective_action(lam, g, t):
    x, y, z = g
    return (add(t, scale(-1, x)),
            (lam * z + form(lam, t, y) - HALF * form(lam, x, y)) % P)


def physical_action(mu, g, t):
    x, y, z = g
    return (add(t, scale(-1, x)),
            mu * (z + dot(t, y) - HALF * dot(x, y)) % P)


def projective_and_phi_checks():
    group = list(product(W, W, range(P)))
    basis_tests = [ZERO, (1, 0), (0, 1)]
    checked = 0
    for lam, g, h in product(range(P), group, group):
        gh = group_multiply(g, h)
        omega = HALF * (dot(g[0], mv(C, h[1]))
                        - dot(h[0], mv(C, g[1]))) % P
        for t in basis_tests:
            ht, hp = projective_action(lam, h, t)
            gt, gp = projective_action(lam, g, ht)
            target, phase = projective_action(lam, gh, t)
            assert gt == target and (hp + gp - phase) % P == omega
            checked += 1

    def phi(lam, mu, x, t):
        s = scale(-1, mv(INVERSES[(lam - mu) % P], scale(mu, x)))
        return add(s, t), add(x, t)

    generators = [((1, 0), ZERO, 0), ((0, 1), ZERO, 0),
                  (ZERO, (1, 0), 0), (ZERO, (0, 1), 0), (ZERO, ZERO, 1)]
    intertwiners = 0
    for lam, mu, x, t, g in product(range(P), range(P), W, W, generators):
        gt, phase_left = projective_action(lam, g, t)
        target_left = phi(lam, mu, x, gt)
        s, xx = phi(lam, mu, x, t)
        target_s, phase_s = projective_action((lam - mu) % P, g, s)
        target_x, phase_x = physical_action(mu, g, xx)
        assert target_left == (target_s, target_x)
        assert phase_left == (phase_s + phase_x) % P
        intertwiners += 1
    return {"projective_composition_affine_basis_checks": checked,
            "expectation_intertwiner_generator_checks": intertwiners,
            "scope": "All group pairs; affine basis tests cover dependence on t"}


# A module is ('H',mu) or ('char',xi,eta). Character modules have central
# weight zero and explicitly exercise the nontrivial neutral Weyl channels.
def charge(module):
    return module[1] if module[0] == "H" else 0


def second_weight(module, state):
    return scale(module[1], state) if module[0] == "H" else module[2]


def fuse_step(lam, modules, states, left, right):
    states = list(states)
    nu = sum(charge(modules[i]) for i in right) % P
    weight = ZERO
    for i in right:
        weight = add(weight, second_weight(modules[i], states[i]))
    s = scale(-1, mv(INVERSES[(lam - nu) % P], weight))
    phase = 0
    for i in left:
        if modules[i][0] == "H":
            states[i] = add(states[i], s)
        else:
            phase -= dot(modules[i][1], s)
    return tuple(states), phase % P


def indices(tree):
    if isinstance(tree, int):
        return [tree]
    return indices(tree[0]) + indices(tree[1])


def tree_map(tree, lam, modules, states):
    if isinstance(tree, int):
        return states, 0
    left, right = tree
    right_ids = indices(right)
    nu = sum(charge(modules[i]) for i in right_ids) % P
    states, a = tree_map(left, (lam - nu) % P, modules, states)
    states, b = tree_map(right, lam, modules, states)
    states, c = fuse_step(lam, modules, states, indices(left), right_ids)
    return states, (a + b + c) % P


def twist_and_pentagon_checks():
    left, right = ((0, 1), 2), (0, (1, 2))
    triples = 0
    for lam, weights in product(range(P), product(range(P), repeat=3)):
        modules = tuple(("H", mu) for mu in weights)
        for states in product(W, repeat=3):
            assert tree_map(left, lam, modules, states) == tree_map(
                right, lam, modules, states)
            triples += 1

    neutral = 0
    for lam, xi, eta, position, x, y in product(range(P), W, W, range(3), W, W):
        modules, states = [("H", 1), ("H", 2)], [x, y]
        modules.insert(position, ("char", xi, eta))
        states.insert(position, None)
        assert tree_map(left, lam, modules, tuple(states)) == tree_map(
            right, lam, modules, tuple(states))
        neutral += 1

    trees = [(((0, 1), 2), 3), ((0, (1, 2)), 3),
             (0, ((1, 2), 3)), (0, (1, (2, 3))), ((0, 1), (2, 3))]
    pentagons = 0
    for lam, weights in product(range(P), product(range(P), repeat=4)):
        modules = tuple(("H", mu) for mu in weights)
        for j in range(8):
            vector = tuple(int(i == j) for i in range(8))
            states = tuple(vector[2 * i:2 * i + 2] for i in range(4))
            outputs = [tree_map(t, lam, modules, states) for t in trees]
            assert all(out == outputs[0] for out in outputs)
            pentagons += 1

    parameter_outputs = [fuse_step(lam, (("H", 1), ("H", 1)),
                                   (ZERO, (1, 0)), [0], [1])[0][0]
                         for lam in range(P)]
    assert len(set(parameter_outputs)) == 3
    duality = 0
    def evaluation(lam, mu, x, y):
        values, phase = fuse_step(lam, (("H", -mu % P), ("H", mu)),
                                  (x, y), [0], [1])
        assert phase == 0
        return values[0] == values[1]
    def coevaluation(lam, mu):
        out = []
        for t in W:
            values, phase = fuse_step(lam, (("H", mu), ("H", -mu % P)),
                                      (t, t), [0], [1])
            assert phase == 0
            # Invert the controlled translation; the right coordinate stays t.
            out.append((add(scale(2, t), scale(-1, values[0])), t))
        return out
    for lam, mu, t in product(range(P), range(P), W):
        first = [u for u, v in coevaluation((lam - mu) % P, mu)
                 if evaluation(lam, mu, v, t)]
        second = [v for u, v in coevaluation(lam, mu)
                  if evaluation((lam + mu) % P, mu, t, u)]
        assert first == second == [t]
        duality += 2
    return {"all_H_charge_triple_basis_states": triples,
            "mixed_full_neutral_character_checks": neutral,
            "all_five_fourfold_trees_linear_basis_checks": pentagons,
            "shifted_true_dual_triangle_basis_checks": duality,
            "parameter_dependent_first_coordinates": parameter_outputs,
            "scope": "Fourfold maps linear in coordinates; all eight basis vectors tested"}


def fourier_product_checks():
    labels = list(product(W, repeat=2))
    multiplication, associativity, reconstruction = 0, 0, 0
    for lam in range(P):
        phases = {(a, b): dot(a[0], mv(INVERSES[lam], b[1]))
                  for a, b in product(labels, repeat=2)}
        multiplication += len(phases)
        def plus(a, b):
            return add(a[0], b[0]), add(a[1], b[1])
        for a, b, c in product(labels, repeat=3):
            assert (phases[a, b] + phases[plus(a, b), c]
                    - phases[b, c] - phases[a, plus(b, c)]) % P == 0
            associativity += 1
        central = [a for a in labels if all(phases[a, b] == phases[b, a]
                                           for b in labels)]
        assert central == [(ZERO, ZERO)]
        recovered_inverse = tuple(tuple(phases[(e, ZERO), (ZERO, f)]
                                         for f in I) for e in I)
        assert recovered_inverse == INVERSES[lam]
        recovered_map = inverse(recovered_inverse)
        assert recovered_map == MAPS[lam]
        assert tuple(tuple((recovered_map[i][j] - MAPS[0][i][j]) % P
                           for j in range(2)) for i in range(2)) == tuple(
                               tuple(lam * I[i][j] % P for j in range(2))
                               for i in range(2))
        reconstruction += 1
    return {"Fourier_product_phase_pairs": multiplication,
            "exact_associative_triples": associativity,
            "reconstructed_parameter_forms": reconstruction,
            "fiber_algebra_dimension": len(labels),
            "fiber_center_dimension": 1,
            "identity_twist_center_dimension": len(labels),
            "scope": "All fibers Mat_9; Fourier marks reconstruct b_lambda"}


def auxiliary_bundle_checks():
    # DD17 is a permutation on these Schrödinger delta bases. Testing
    # bijectivity checks the full expectation map, not only each Phi_x.
    schrodinger_bases = 0
    for lam, mu in product(range(P), repeat=2):
        outputs = []
        for t, x in product(W, repeat=2):
            s = scale(-1, mv(INVERSES[(lam - mu) % P], scale(mu, x)))
            outputs.append((add(s, t), add(x, t)))
            schrodinger_bases += 1
        assert len(set(outputs)) == len(W) ** 2

    # A neutral character has Phi(delta_t)=psi(-xi(t)) delta_(t+s),
    # s=-F_lambda^-1 eta. The phase is a unit and the coordinate map
    # is a permutation, including every nontrivial neutral character.
    character_bases = 0
    for lam, xi, eta in product(range(P), W, W):
        s = scale(-1, mv(INVERSES[lam], eta))
        outputs = [(add(t, s), -dot(xi, t) % P) for t in W]
        assert len({v for v, phase in outputs}) == len(W)
        character_bases += len(outputs)

    # Include every residue of the physical commutator c and of the
    # auxiliary multiplier d, and three integer lifts per physical
    # charge. These are finite sign/coherence controls, not a numerical
    # verification of the analytic Chern formula proved in DD5a.
    carries, true_duals = 0, 0
    for c, d, lam, mu, nu, a, b in product(
            range(P), range(P), range(P), range(P), range(P),
            range(-1, 2), range(-1, 2)):
        lifts = {r: (-r * c - d) % P for r in range(P)}
        k, ell = (-mu * c) % P + P * a, (-nu * c) % P + P * b
        def carry(r, charge_value, degree):
            numerator = lifts[r] - lifts[(r - charge_value) % P] - degree
            assert numerator % P == 0
            return numerator // P
        n1 = carry(lam, nu, ell)
        n2 = carry((lam - nu) % P, mu, k)
        nt = carry(lam, (mu + nu) % P, k + ell)
        assert n1 + n2 == nt
        # This integer equality is simultaneously the exponent and
        # slope equality for both terms of the full Chern one-form.
        assert lifts[lam] == lifts[(lam - mu - nu) % P] + k + ell + P * nt
        carries += 1
        if nu == 0 and b == 0:
            assert (carry(lam, mu, k)
                    + carry((lam - mu) % P, -mu % P, -k)) == 0
            true_duals += 1
    return {"unitary_total_expectation_H_basis_images": schrodinger_bases,
            "unitary_total_expectation_neutral_character_basis_images": character_bases,
            "integer_lift_and_shifted_carry_checks": carries,
            "true_dual_zero_carry_checks": true_duals,
            "scope": "Unitarity and degree/carry controls; full Chern horizontality is proved in DD5a"}


def rigid_completion_checks():
    r = [[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]]
    s = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
    def mm(a, b):
        return [[dot(row, col) for col in zip(*b)] for row in a]
    assert mm(transpose(r), s) == mm(s, r)
    assert mm(s, s) == [[int(i == j) for j in range(4)] for i in range(4)]
    orbit = []
    value = 1
    while value not in orbit:
        orbit.append(value)
        value = 3 * value % 19
    assert value == 1 and len(orbit) == 18 and 18 > 4
    return {"rigid_field_degree": 18, "matrix_degree_bound": 4,
            "order19_Frobenius_orbit": orbit,
            "compatible_symmetric_S": s,
            "scope": "Nonvanishing follows symbolically from DD6; no F_(3^18) enumeration"}


def main():
    assert __debug__, "Run with assertions enabled"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()
    result = {"status": "PASS", "arithmetic": "Exact F3, integers and root-of-unity exponents",
              "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "projective_and_expectation": projective_and_phi_checks(),
              "shifted_fusion": twist_and_pentagon_checks(),
              "Fourier_algebras": fourier_product_checks(),
              "auxiliary_bundle_action": auxiliary_bundle_checks(),
              "rigid_completion": rigid_completion_checks(),
              "limits": ["Finite dynamical parameter, no continuous q-connection",
                         "Auxiliary projective modules are not the physical linear modules",
                         "No new isotope separator or analytic rigidity is certified",
                         "No huge loop or field extension is enumerated"]}
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.certificate:
        args.certificate.write_text(output)
        print(json.dumps({"status": "PASS", "certificate": str(args.certificate),
                          "script_sha256": result["script_sha256"]}, indent=2))
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
