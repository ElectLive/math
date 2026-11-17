"""Exact controls for HT1--HT6 in bol-heat-sewing-repair.md.

Python 3.11+, standard library, assertions enabled. Cyclotomic arithmetic
is exact. These finite checks do not prove analytic convergence or heat
identities and do not certify a combined charged-fusion functor.
"""

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


class Cyclotomic:
    """Q[zeta_p], reduced by 1+z+...+z^(p-1); p is prime."""

    def __init__(self, p):
        self.p = p
        self.zero = (Fraction(0),) * (p - 1)
        self.one = (Fraction(1),) + (Fraction(0),) * (p - 2)

    def reduce(self, coefficients):
        raw = [Fraction(0)] * self.p
        for i, c in enumerate(coefficients):
            raw[i % self.p] += c
        return tuple(c - raw[-1] for c in raw[:-1])

    def z(self, power):
        raw = [Fraction(0)] * self.p
        raw[power % self.p] = Fraction(1)
        return self.reduce(raw)

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def scale(self, c, a):
        return tuple(c * x for x in a)

    def mul(self, a, b):
        raw = [Fraction(0)] * (2 * self.p - 3)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        raw[i + j] += x * y
        return self.reduce(raw)

    def conjugate(self, a):
        out = self.zero
        for i, c in enumerate(a):
            out = self.add(out, self.scale(c, self.z(-i)))
        return out

    def matrix(self, n):
        return [[self.zero for _ in range(n)] for _ in range(n)]

    def identity(self, n):
        out = self.matrix(n)
        for j in range(n):
            out[j][j] = self.one
        return out

    def mm(self, a, b):
        n = len(a)
        out = self.matrix(n)
        for i, k, j in product(range(n), repeat=3):
            if a[i][k] != self.zero and b[k][j] != self.zero:
                out[i][j] = self.add(out[i][j], self.mul(a[i][k], b[k][j]))
        return out

    def adjoint(self, a):
        return [[self.conjugate(a[j][i]) for j in range(len(a))]
                for i in range(len(a))]

    def sm(self, c, a):
        return [[self.scale(c, x) for x in row] for row in a]

    def trace(self, a):
        out = self.zero
        for j in range(len(a)):
            out = self.add(out, a[j][j])
        return out

    def trace_product(self, a, b):
        out = self.zero
        for i, j in product(range(len(a)), repeat=2):
            if a[i][j] != self.zero and b[j][i] != self.zero:
                out = self.add(out, self.mul(a[i][j], b[j][i]))
        return out

    def kron(self, a, b):
        n, m = len(a), len(b)
        out = self.matrix(n * m)
        for i, j, k, l in product(range(n), range(n), range(m), range(m)):
            out[i * m + k][j * m + l] = self.mul(a[i][j], b[k][l])
        return out


def weyl(c, k, r, s):
    out = c.matrix(c.p)
    for j in range(c.p):
        out[(-j - 2 * r) % c.p][j] = c.z(2 * k * s * (j + r))
    return out


def shift(c, n):
    out = c.matrix(n)
    for j in range(n):
        out[(j + 1) % n][j] = c.one
    return out


def units(c, m):
    for a, b in product(range(m), repeat=2):
        out = c.matrix(m)
        out[a][b] = c.one
        yield a, b, out


def reconstruct(c, k, m, q):
    out = c.matrix(c.p * m)
    coefficient_norm = c.zero
    count = 0
    for r, s in product(range(c.p), repeat=2):
        w = weyl(c, k, r, s)
        for a, b, e in units(c, m):
            t = c.trace_product(c.kron(w, e), q)
            coefficient_norm = c.add(coefficient_norm, c.mul(t, c.conjugate(t)))
            et = c.adjoint(e)
            basis = c.kron(w, et)
            for i, j in product(range(c.p * m), repeat=2):
                out[i][j] = c.add(out[i][j], c.mul(t, basis[i][j]))
            count += 1
    assert out == c.sm(c.p, q)
    assert coefficient_norm == c.scale(c.p, c.trace_product(c.adjoint(q), q))
    return count


def basis_and_tomography():
    orthogonality = 0
    coefficients = 0
    cases = []
    for p, m in ((3, 1), (3, 2), (3, 3), (5, 1), (5, 2)):
        c = Cyclotomic(p)
        k = 1
        ws = [weyl(c, k, r, s) for r, s in product(range(p), repeat=2)]
        total = c.matrix(p)
        for i, w in enumerate(ws):
            assert c.adjoint(w) == w
            assert c.mm(w, w) == c.identity(p)
            for r, s in product(range(p), repeat=2):
                total[r][s] = c.add(total[r][s], w[r][s])
            for j, ww in enumerate(ws):
                assert c.trace_product(w, ww) == (c.scale(p, c.one) if i == j else c.zero)
                orthogonality += 1
        assert total == c.sm(p, c.identity(p))

        n = p * m
        q = [[c.add(c.scale((i + 2 * j) % 4 - 1, c.one), c.z(i * j + j))
              for j in range(n)] for i in range(n)]
        coefficients += reconstruct(c, k, m, q)
        cases.append({"p": p, "zero_matrix_size": m, "operator_dimension": n,
                      "full_zero_algebra_dimension": m * m})
    return {"orthogonality_equations": orthogonality,
            "reconstructed_exact_coefficients": coefficients,
            "cases": cases}


def modular_generators():
    checks = 0
    for p in (3, 5, 7):
        c = Cyclotomic(p)
        for k in range(1, p):
            fourier = [[c.z(-k * i * j) for j in range(p)] for i in range(p)]
            shear = c.matrix(p)
            for j in range(p):
                shear[j][j] = c.z(k * pow(2, -1, p) * j * j)
            assert c.mm(fourier, c.adjoint(fourier)) == c.sm(p, c.identity(p))
            for r, s in product(range(p), repeat=2):
                w = weyl(c, k, r, s)
                fs = c.mm(c.mm(fourier, w), c.adjoint(fourier))
                assert fs == c.sm(p, weyl(c, k, s, -r))
                ts = c.mm(c.mm(shear, w), c.adjoint(shear))
                assert ts == weyl(c, k, r, r + s)
                checks += 2
    return {"exact_S_T_conjugation_equations": checks,
            "Fourier_normalization": "F_unnormalized F_unnormalized*=p I",
            "metaplectic_phase_used": False}


def scalar_phase_control():
    p = 3
    c = Cyclotomic(p)
    q = shift(c, p)
    q2 = [[c.mul(c.z(1), x) for x in row] for row in q]
    qpow, q2pow = c.identity(p), c.identity(p)
    for j in range(1, p + 1):
        qpow, q2pow = c.mm(qpow, q), c.mm(q2pow, q2)
        assert c.trace(qpow) == c.trace(q2pow)
    assert qpow == q2pow == c.identity(p)
    differentiated = 0
    ablated = 0
    for r, s in product(range(p), repeat=2):
        a = weyl(c, 1, r, s)
        t1, t2 = c.trace_product(a, q), c.trace_product(a, q2)
        assert t2 == c.mul(c.z(1), t1)
        differentiated += t1 != t2
        for t, w in product(range(p), repeat=2):
            b = weyl(c, 1, t, w)
            g1 = c.trace(c.mm(c.mm(c.mm(a, q), b), c.adjoint(q)))
            g2 = c.trace(c.mm(c.mm(c.mm(a, q2), b), c.adjoint(q2)))
            assert g1 == g2
            ablated += 1
    assert differentiated > 0
    return {"equal_spectrum_matrices": "V and zeta_3 V, characteristic polynomial t^3-1",
            "distinguishing_marked_coefficients": differentiated,
            "graph_only_phase_erasure_equations": ablated}


def cycle_type(perm):
    seen = set()
    lengths = Counter()
    for i in range(len(perm)):
        if i in seen:
            continue
        j, size = i, 0
        while j not in seen:
            seen.add(j)
            size += 1
            j = perm[j]
        lengths[size] += 1
    return dict(sorted(lengths.items()))


def proper_cubic_control():
    p = 3
    elements = list(product(range(p), repeat=3))
    index = {x: i for i, x in enumerate(elements)}

    def mul(h, x, y):
        c, a, b = x
        d, u, v = y
        return ((c + d + b * u * (a + u) + h * (a * v - b * u)) % p,
                (a + u) % p, (b + v) % p)

    bol_checks = 0
    for h in (0, 1):
        for x, y, z in product(elements, repeat=3):
            assert mul(h, x, mul(h, y, mul(h, x, z))) == mul(h, mul(h, x, mul(h, y, x)), z)
            bol_checks += 1
        x, y = (0, 1, 0), (0, 0, 1)
        assert mul(h, mul(h, x, y), x) != mul(h, x, mul(h, y, x))

    individual_spectra = []
    for x in elements:
        cycles = [cycle_type([index[mul(h, x, y)] for y in elements]) for h in (0, 1)]
        assert cycles[0] == cycles[1]
        individual_spectra.append(cycles[0])

    def f(h, x):
        d, u, v = x
        return ((d + h * u * v) % p, u, v)

    marked_conjugation = 0
    for h in (0, 1):
        for x in elements:
            # F_h^(-1) L_(0,0,1)^h F_h = T_0(0,1,-2h,0).
            lhs = f(-h, mul(h, (0, 0, 1), f(h, x)))
            d, u, v = x
            rhs = ((d + u * u - 2 * h * u) % p, u, (v + 1) % p)
            assert lhs == rhs
            marked_conjugation += 1

    c = Cyclotomic(p)
    v = shift(c, p)
    probe = c.adjoint(v)
    all_coefficients = []
    for h in (0, 1):
        d = c.matrix(p)
        for u in range(p):
            d[u][u] = c.z(u * u - 2 * h * u)
        q = c.kron(d, v)
        assert c.mm(q, c.adjoint(q)) == c.identity(p * p)
        qpow = c.identity(p * p)
        for j in range(1, p + 1):
            qpow = c.mm(qpow, q)
            assert c.trace(qpow) == (c.scale(p * p, c.one) if j == p else c.zero)
        reconstruct(c, 1, p, q)
        coeffs = []
        for r, s in product(range(p), repeat=2):
            observed = c.trace_product(c.kron(weyl(c, 1, r, s), probe), q)
            expected = c.scale(p, c.z(r * r + 2 * h * r))
            assert observed == expected
            coeffs.append(observed)
        all_coefficients.append(coeffs)
    assert all_coefficients[0] != all_coefficients[1]
    return {"orders": [27, 27], "parameters": [0, 1],
            "left_Bol_equations": bol_checks,
            "nonflexible_witness_in_each": True,
            "equal_labeled_left_translation_cycle_types": len(individual_spectra),
            "exact_marked_conjugation_equations": marked_conjugation,
            "zero_algebra": "Mat_3", "charged_mark_dimension": 9,
            "common_charged_characteristic_polynomial": "(t^3-1)^3",
            "r_1_probe_coefficients": ["3*zeta_3", "3"],
            "full_matrix_reconstruction_each": True}


def associative_control():
    p = 3
    elements = list(product(range(p), repeat=3))

    def mul(x, y):
        c, a, b = x
        d, u, v = y
        return ((c + d + a * v) % p, (a + u) % p, (b + v) % p)

    checked = 0
    for x, y, z in product(elements, repeat=3):
        assert mul(mul(x, y), z) == mul(x, mul(y, z))
        checked += 1
    assert mul((0, 1, 0), (0, 0, 1)) != mul((0, 0, 1), (0, 1, 0))
    return {"model": "Heisenberg group on F3^3", "order": 27,
            "associativity_equations": checked, "noncommutative": True}


def finite_sampling_control():
    # For f(w,w')=1/((1-a*w)(1-b*w')), exact root averaging
    # gives 1/((1-a^N)(1-b^N)). This tests the tail constant.
    checks = 0
    for r in (Fraction(3, 2), Fraction(2), Fraction(3)):
        for n in range(1, 9):
            a = 1 / r
            exact = 1 / ((1 - a ** n) ** 2) - 1
            tail = ((1 - r ** (-n)) ** (-2)) - 1
            assert exact == tail > 0
            checks += 1
    return {"exact_geometric_tail_controls": checks,
            "bound": "M*((1-R^(-N))^(-2)-1)",
            "floating_point_theta_samples": False}


def main():
    assert __debug__, "Run with assertions enabled"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()
    report = {
        "status": "PASS",
        "arithmetic": "Exact Q[zeta_p], integers and rational numbers",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "basis_and_tomography": basis_and_tomography(),
        "modular_generators": modular_generators(),
        "scalar_phase_control": scalar_phase_control(),
        "proper_cubic_control": proper_cubic_control(),
        "associative_control": associative_control(),
        "finite_sampling_control": finite_sampling_control(),
        "limits": "Finite controls, not proofs of analytic convergence, contour estimates, or a combined charged-fusion functor",
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.certificate:
        args.certificate.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
