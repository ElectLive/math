#!/usr/bin/env python3
"""Independent finite checks of supplied Bol fusion/intertwiner candidates.

Written by /root/independent_review. Imports no authored research checker.
Exact arithmetic only. It tests finite interfaces; it is not a uniform proof.
"""

from collections import Counter
import hashlib
import json
import random


class Field:
    """F_3[X]/Phi_(7^A), independently represented by coefficient tuples."""

    def __init__(self, A):
        self.A = A
        self.m = 7 ** A
        self.step = 7 ** (A - 1)
        self.degree = 6 * self.step
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)
        self.x = (0, 1) + (0,) * (self.degree - 2)
        assert self.pow(self.x, self.m) == self.one
        assert self.pow(self.x, self.m // 7) != self.one
        self.q = 3 ** self.degree
        powers = [self.one]
        for _ in range(1, self.m):
            powers.append(self.mul(powers[-1], self.x))
        self.trace_weights = []
        for i in range(self.degree):
            out = self.zero
            for j in range(self.degree):
                out = self.add(out, powers[(i * pow(3, j, self.m)) % self.m])
            assert all(x == 0 for x in out[1:])
            self.trace_weights.append(out[0])

    def add(self, a, b):
        return tuple((x + y) % 3 for x, y in zip(a, b))

    def neg(self, a):
        return tuple((-x) % 3 for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def scale(self, a, s):
        return tuple((s * x) % 3 for x in a)

    def mul(self, a, b):
        t = [0] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        t[i + j] += x * y
        for r in range(len(t) - 1, self.degree - 1, -1):
            c = t[r] % 3
            if c:
                for j in range(6):
                    t[r - self.degree + j * self.step] -= c
        return tuple(x % 3 for x in t[:self.degree])

    def pow(self, a, n):
        out = self.one
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n //= 2
        return out

    def tr(self, a):
        return sum(x * y for x, y in zip(a, self.trace_weights)) % 3

    def rand(self, rng):
        return tuple(rng.randrange(3) for _ in range(self.degree))


class Model:
    """Actual admissible n=2,k=1 reciprocal loop at level A."""

    def __init__(self, A):
        self.f = Field(A)
        self.m = 7 ** A
        self.eta = {1: 2, 2: 30}[A]
        self.lambdas = tuple(self.f.pow(self.f.x, i) for i in range(self.m))
        self.zero = ((self.f.zero, self.f.zero), (0, 0))
        assert pow(self.eta, 3, self.m) == 1
        assert self.eta % 7 == 2

    def randu(self, rng):
        return ((self.f.rand(rng), self.f.rand(rng)),
                (rng.randrange(self.m), rng.randrange(self.m)))

    def randz(self, rng):
        return (rng.randrange(3), rng.randrange(self.m))

    def addu(self, u, v):
        return (tuple(self.f.add(x, y) for x, y in zip(u[0], v[0])),
                tuple((x + y) % self.m for x, y in zip(u[1], v[1])))

    def negu(self, u):
        return (tuple(self.f.neg(x) for x in u[0]),
                tuple((-x) % self.m for x in u[1]))

    def subu(self, u, v):
        return self.addu(u, self.negu(v))

    def addz(self, c, d):
        return ((c[0] + d[0]) % 3, (c[1] + d[1]) % self.m)

    def negz(self, c):
        return ((-c[0]) % 3, (-c[1]) % self.m)

    def R(self, c, u):
        lam = self.lambdas[c[1] % self.m]
        eta = pow(self.eta, c[0] % 3, self.m)
        return (tuple(self.f.mul(lam, x) for x in u[0]),
                tuple(eta * x % self.m for x in u[1]))

    def b(self, u, v):
        field = self.f.sub(self.f.mul(u[0][0], v[0][1]),
                           self.f.mul(u[0][1], v[0][0]))
        ring = (u[1][0] * v[1][1] - u[1][1] * v[1][0]) % self.m
        return (self.f.tr(field), ring)

    def law(self, x, y):
        a, c = x
        u, e = y
        return (self.addu(a, self.R(c, u)),
                self.addz(self.addz(c, e), self.negz(self.b(a, u))))

    def ldivide(self, x, y):
        a, c = x
        X, e = y
        u = self.R(self.negz(c), self.subu(X, a))
        return (u, self.addz(self.addz(e, self.negz(c)), self.b(a, u)))

    def defect(self, x, y, z):
        return self.ldivide(self.law(x, y), self.law(x, self.law(y, z)))

    def hg(self, x, y):
        a, c = x
        v, d = y
        g = self.b(a, v)
        h = self.subu(self.addu(self.subu(self.R(g, a), self.R(d, a)),
                              self.R(self.addz(c, g), v)), v)
        return h, g

    def phase(self, chi, z):
        return (self.m * chi[0] * z[0] + 3 * chi[1] * z[1]) % (3 * self.m)

    def pi(self, chi, x, u):
        a, c = x
        return (self.addu(a, self.R(c, u)),
                self.phase(chi, self.addz(c, self.negz(self.b(a, u)))))

    def J(self, chi, h, g, u):
        return self.R(g, u), self.phase(chi, self.b(h, u))

    def K(self, u, kw, kv):
        return (tuple(self.f.scale(x, kw) for x in u[0]),
                tuple(kv * x % self.m for x in u[1]))

    def F(self, u, v, kw, kv):
        t = self.subu(v, u)
        return self.addu(u, self.K(t, kw, kv)), t


def checks(A, samples):
    M = Model(A)
    rng = random.Random(2026111602 + A)
    counts = Counter()
    chars = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, M.m - 1)]
    if A == 2:
        chars += [(0, 7), (1, 7), (2, 42)]
    for _ in range(samples):
        x = M.randu(rng), M.randz(rng)
        y = M.randu(rng), M.randz(rng)
        z = M.randu(rng), M.randz(rng)
        a, c = x
        h, g = M.hg(x, y)
        actual = M.defect(x, y, z)
        formula = M.R(g, z[0]), M.addz(z[1], M.b(h, z[0]))
        assert actual == formula
        assert M.law(x, M.law(y, M.law(x, z))) == M.law(M.law(x, M.law(y, x)), z)
        counts['actual_loop_defect_and_bol'] += 1
        for chi in chars:
            psi = chars[rng.randrange(len(chars))]
            sigma = M.addz(chi, psi)
            u, v = M.randu(rng), M.randu(rng)
            kw, kv = rng.randrange(3), rng.randrange(M.m)
            r, t = M.F(u, v, kw, kv)
            u1, q1 = M.pi(chi, x, u)
            v1, q2 = M.pi(psi, x, v)
            target = (M.addu(a, M.R(c, r)), M.R(c, t))
            residual = (M.phase(psi, M.b(a, t)) -
                        M.phase(sigma, M.b(a, M.K(t, kw, kv)))) % (3 * M.m)
            targetphase = (M.phase(sigma, M.addz(c, M.negz(M.b(a, r)))) - residual) % (3 * M.m)
            assert M.F(u1, v1, kw, kv) == target
            assert (q1 + q2) % (3 * M.m) == targetphase
            u2, s1 = M.J(chi, h, g, u)
            v2, s2 = M.J(psi, h, g, v)
            residual_h = (M.phase(psi, M.b(h, t)) -
                          M.phase(sigma, M.b(h, M.K(t, kw, kv)))) % (3 * M.m)
            assert M.F(u2, v2, kw, kv) == (M.R(g, r), M.R(g, t))
            assert (s1 + s2) % (3 * M.m) == (M.phase(sigma, M.b(h, r)) + residual_h) % (3 * M.m)
            counts['residual_fusion_translation_and_correction'] += 1
            if sigma[0] * kw % 3 == psi[0] and sigma[1] * kv % M.m == psi[1]:
                assert residual == residual_h == 0
                counts['decoupled_fusion'] += 1

    # Exact division and fusion at deliberately chosen exceptional characters.
    for chi, psi in [((1, 1), (2, M.m - 1)), ((0, 0), (0, 0)),
                     ((1, 0), (1, 0)), ((0, 1), (0, 1))]:
        sigma = M.addz(chi, psi)
        kw_solutions = [x for x in range(3) if sigma[0] * x % 3 == psi[0]]
        kv_solutions = [x for x in range(M.m) if sigma[1] * x % M.m == psi[1]]
        if chi == (1, 1) and psi == (2, M.m - 1):
            assert not kw_solutions and not kv_solutions
        else:
            assert kw_solutions and kv_solutions
        counts['exceptional_fusion_solvability'] += 1

    # Full-defect orbit intertwiners: sparse kernel transport, including
    # nonzero phases before the compatibility test and nontrivial dilations.
    for chi, psi in [((1, 1), (2, 2)), ((1, 0), (0, 1)),
                     ((0, 0), (0, 0)), ((1, 1), (1, 1))]:
        w = M.randu(rng)
        s = (tuple(M.f.scale(a, psi[0]) for a in w[0]),
             tuple(psi[1] * a % M.m for a in w[1]))
        t = (tuple(M.f.scale(a, chi[0]) for a in w[0]),
             tuple(chi[1] * a % M.m for a in w[1]))
        orbit = {(M.R((a, z), s), M.R((a, z), t))
                 for a in range(3) for z in range(M.m)}
        for __ in range(5):
            h, g = M.randu(rng), M.randz(rng)
            mapped = set()
            for u, v in orbit:
                u1, phiu = M.J(chi, h, g, u)
                v1, psiv = M.J(psi, h, g, v)
                assert (phiu - psiv) % (3 * M.m) == 0
                mapped.add((u1, v1))
            assert mapped == orbit
            counts['full_defect_orbit_intertwiner'] += 1

    return dict(sorted(counts.items()))


if __name__ == '__main__':
    print(json.dumps({'seed_base': 2026111602,
                      'levels': {str(A): checks(A, n) for A, n in [(1, 12), (2, 3)]},
                      'imports_authored_checkers': False,
                      'arithmetic': 'exact F3 polynomial quotients and integer phases'},
                     indent=2, sort_keys=True))

