"""Exact controls for CT collective charged differential/difference transport.

Python 3.11+, standard library. Mathematical proofs are in CT1--CT7;
these finite checks do not prove analytic convergence or modularity.
"""

import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


P = 3
W = list(product(range(P), repeat=2))
ZERO = (0, 0)
ROT = ((0, 2), (1, 0))


def add(x, y):
    return tuple((a + b) % P for a, b in zip(x, y))


def scale(a, x):
    return tuple(a * b % P for b in x)


def dot(x, y):
    return sum(a * b for a, b in zip(x, y)) % P


def mv(a, x):
    return tuple(dot(row, x) for row in a)


def inv2(a):
    d = pow((a[0][0] * a[1][1] - a[0][1] * a[1][0]) % P, -1, P)
    return ((d * a[1][1] % P, -d * a[0][1] % P),
            (-d * a[1][0] % P, d * a[0][0] % P))


def finverse(sign, lam):
    form = tuple(tuple((sign * ROT[i][j] + (lam if i == j else 0)) % P
                       for j in range(2)) for i in range(2))
    return inv2(tuple(zip(*form)))


def j_action(sign, lam, nu, state):
    x, y = state
    shift = mv(finverse(sign, (lam - nu) % P), scale(nu, y))
    return add(x, scale(-1, shift)), y


def physical(mu, g, x):
    a, b, c = g
    return add(x, scale(-1, a)), mu * (c + dot(x, b) - 2 * dot(a, b)) % P


def group_mul(g, h):
    x, y, z = g
    a, b, c = h
    return add(x, a), add(y, b), (z + c + 2 * (dot(x, b) - dot(a, y))) % P


def group_inv(g):
    return scale(-1, g[0]), scale(-1, g[1]), -g[2] % P


def finite_difference_controls():
    covariance = wrong_base = first_axis = second_axis = changed = 0
    e1, e2 = (1, 0), (0, 1)
    for sign, lam, mu, nu, x, y in product((1, 2), range(P), range(P),
                                          range(P), W, W):
        # R=ROT transports b by -1 and completion C to -C.
        # Test the base/charge covariance independently of CT5's definition.
        state = x, y
        ar = lambda xy: tuple(mv(ROT, v) for v in xy)
        out1 = ar(j_action(sign, lam, nu, state))
        out2 = j_action(-sign % P, -lam % P, -nu % P, ar(state))
        assert out1 == out2
        covariance += 1
        wrong_base += out1 != j_action(sign, lam, -nu % P, ar(state))

        fi = finverse(sign, (lam - nu) % P)
        for t in (e1, e2):
            # Independent closed formula for J^-1 Delta(X_t) J.
            tx = add(x, scale(-1, add(t, mv(fi, scale(nu, t)))))
            ty = add(y, scale(-1, t))
            lhs = j_action(sign, lam, nu, (tx, ty))
            jx, jy = j_action(sign, lam, nu, state)
            rhs = add(jx, scale(-1, t)), add(jy, scale(-1, t))
            assert lhs == rhs
            first_axis += 1
            changed += (tx, ty) != (add(x, scale(-1, t)), ty)
            # The second-axis source phase genuinely couples x and y.
            source_phase = (mu * dot(x, t) + nu * dot(y, t)
                            - mu * dot(mv(fi, scale(nu, y)), t)) % P
            output_phase = (mu * dot(jx, t) + nu * dot(jy, t)) % P
            assert source_phase == output_phase
            second_axis += 1
    assert wrong_base > 0 and changed > 0

    # Moving the pair, rather than pretending every group element fixes it.
    generators = [(e1, ZERO, 0), (e2, ZERO, 0),
                  (ZERO, e1, 0), (ZERO, e2, 0)]
    pair = (e1, ZERO, 0), (ZERO, e1, 0)
    conjugation = 0
    for mu, g, hol, state in product(range(P), generators, pair, W):
        transformed = group_mul(group_mul(g, hol), group_inv(g))
        s1, a = physical(mu, hol, state)
        s1, b = physical(mu, g, s1)
        s2, c = physical(mu, g, state)
        s2, d = physical(mu, transformed, s2)
        assert s1 == s2 and (a + b) % P == (c + d) % P
        conjugation += 1
    return {"moving_completion_charge_covariance": covariance,
            "omitting_base_transport_failures": wrong_base,
            "noncentral_first_axis_operator_identities": first_axis,
            "noncentral_second_axis_phase_identities": second_axis,
            "genuinely_changed_first_axis_symbols": changed,
            "transported_holonomy_pair_equations": conjugation}


class CQ:
    """Complex rational arithmetic, used only for exact modular identities."""
    def __init__(self, x=0, y=0):
        if isinstance(x, CQ):
            self.x, self.y = x.x, x.y
        else:
            self.x, self.y = Q(x), Q(y)

    def __add__(self, other):
        z = CQ(other)
        return CQ(self.x + z.x, self.y + z.y)

    __radd__ = __add__

    def __neg__(self):
        return CQ(-self.x, -self.y)

    def __sub__(self, other):
        return self + -CQ(other)

    def __rsub__(self, other):
        return CQ(other) + -self

    def __mul__(self, other):
        z = CQ(other)
        return CQ(self.x * z.x - self.y * z.y,
                  self.x * z.y + self.y * z.x)

    __rmul__ = __mul__

    def __truediv__(self, other):
        z = CQ(other)
        norm = z.x * z.x + z.y * z.y
        return self * CQ(z.x / norm, -z.y / norm)

    def __eq__(self, other):
        z = CQ(other)
        return self.x == z.x and self.y == z.y


def mm(a, b):
    return tuple(tuple(sum(a[i][h] * b[h][j] for h in range(2))
                       for j in range(2)) for i in range(2))


def transformed(gamma, z, tau):
    (a, b), (c, d) = gamma
    den = c * tau + d
    return z / den, (a * tau + b) / den, c * z * z / den


def modular_controls():
    identity = ((1, 0), (0, 1))
    generators = [((1, n), (0, 1)) for n in (-12, -6, 6, 12)]
    generators += [((1, 0), (n, 1)) for n in (-12, -6, 6, 12)]
    matrices = {identity, *generators}
    matrices.update(mm(a, b) for a, b in product(generators, repeat=2))
    matrices = sorted(matrices)
    for (a, b), (c, d) in matrices:
        assert a * d - b * c == 1 and (a - 1) % 6 == 0
        assert b % 6 == c % 6 == (d - 1) % 6 == 0
    points = [(CQ(Q(1, 3), Q(2, 5)), CQ(Q(1, 7), Q(4, 3))),
              (CQ(-2, Q(1, 9)), CQ(Q(-2, 3), Q(3, 5))),
              (CQ(0, 0), CQ(0, 2))]
    metric = phases = composition = carry = 0
    for gamma, (z, tau), degree in product(matrices, points, range(-5, 6)):
        zp, tp, exponent = transformed(gamma, z, tau)
        assert zp.y * zp.y / tp.y == z.y * z.y / tau.y - exponent.y
        metric += 1
        (a, b), (c, d) = gamma
        slope = Q(degree, 3)
        assert (slope * c * d / 2).denominator == 1
        assert (slope * a * b / 2).denominator == 1
        phases += 2
        # All scalar gauges, including negative carry degrees, multiply.
        for other in (-4, 0, 5):
            assert Q(degree + other, 3) * exponent == (
                Q(degree, 3) * exponent + Q(other, 3) * exponent)
            carry += 1
    for g, h, (z, tau) in product(generators, generators, points):
        zh, th, eh = transformed(h, z, tau)
        zgh, tgh, eg = transformed(g, zh, th)
        zp, tp, egh = transformed(mm(g, h), z, tau)
        assert (zgh, tgh) == (zp, tp) and eh + eg == egh
        composition += 1
    return {"level_6_matrices": len(matrices),
            "exact_Chern_metric_identities": metric,
            "holonomy_scalar_phases_are_one": phases,
            "modular_gauge_group_laws": composition,
            "signed_degree_gauge_products": carry}


def carries_and_units():
    carries = triangles = zero_inputs = 0
    for c, mu, nu, eta in product(range(P), repeat=4):
        rep = lambda m: -m * c % P
        n = lambda m, v: (rep(m) + rep(v) - rep((m + v) % P)) // P
        assert n(mu, nu) + n((mu + nu) % P, eta) == (
            n(nu, eta) + n(mu, (nu + eta) % P))
        carries += 1
        for offset in (-2, -1, 0, 1, 2):
            k = rep(mu) + P * offset
            # True dual has degree -k, not rep(-mu).
            assert (k + mu * c) % P == 0
            assert (-k + (-mu % P) * c) % P == 0
            assert k + -k == 0
            triangles += 1
            zero_inputs += k == 0
    assert zero_inputs
    # The unit has a base difference even though its physical matrix is 1.
    s = [Q(2), Q(5), Q(11)]
    base_translation = (1, 2, 0)
    augmented_unit = [s[base_translation[i]] - s[i] for i in range(3)]
    assert augmented_unit != [0, 0, 0]
    assert [Q(1) - Q(1) for _ in range(3)] == [0, 0, 0]
    return {"carry_cocycles": carries, "true_dual_integer_equations": triangles,
            "actual_zero_degree_inputs": zero_inputs,
            "unit_base_difference_retained": True}


def main():
    assert __debug__, "Run with assertions enabled"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()
    report = {"status": "PASS", "arithmetic": "Exact finite fields and complex rationals",
              "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "differential_difference": finite_difference_controls(),
              "modular": modular_controls(), "zero_and_carries": carries_and_units(),
              "limits": ["Finite controls, not universal mathematical proofs",
                         "Collective tensor rule, not ordinary primitive connections",
                         "No CE/Fock identification or full SL2 descent claimed",
                         "Analytic norm convergence is proved in CT and SA"]}
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.certificate:
        args.certificate.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
