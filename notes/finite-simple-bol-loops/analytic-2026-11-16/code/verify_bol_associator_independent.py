#!/usr/bin/env python3
"""Independent exact checks of actual reciprocal Bol defect operators.

Uses F3[X]/Phi_(7^A) at A=1,2 and the original reciprocal multiplication.
No authored implementation is imported. Random tests are finite evidence,
not a proof of the all-parameter identities.
"""

from itertools import product
import json
import random


SEED = 2026111609


class Field:
    def __init__(self, level):
        self.order_root = 7**level
        self.step = self.order_root // 7
        self.degree = 6*self.step
        self.zero = (0,)*self.degree
        self.one = (1,)+(0,)*(self.degree-1)
        assert pow(3, self.degree, self.order_root) == 1
        for prime in (2, 3, 7):
            if self.degree % prime == 0:
                assert pow(3, self.degree//prime, self.order_root) != 1
        self.trace_basis = []
        for exponent in range(self.degree):
            polynomial = [0]*self.order_root
            term = exponent
            for _ in range(self.degree):
                polynomial[term] += 1
                term = 3*term % self.order_root
            value = self.reduce(polynomial)
            assert all(a == 0 for a in value[1:])
            self.trace_basis.append(value[0])

    def reduce(self, polynomial):
        polynomial = list(polynomial)
        assert len(polynomial) == self.order_root
        for residue in range(self.step):
            top = polynomial[6*self.step+residue]
            for j in range(6):
                polynomial[j*self.step+residue] -= top
        return tuple(x % 3 for x in polynomial[:self.degree])

    def add(self, a, b):
        return tuple((x+y) % 3 for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple((x-y) % 3 for x, y in zip(a, b))

    def scale(self, a, integer):
        return tuple(integer*x % 3 for x in a)

    def mul(self, a, b):
        c = [0]*self.order_root
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        c[(i+j) % self.order_root] += x*y
        return self.reduce(c)

    def root_mul(self, a, exponent):
        c = [0]*self.order_root
        for i, x in enumerate(a):
            c[(i+exponent) % self.order_root] = x
        return self.reduce(c)

    def trace(self, a):
        return sum(x*y for x, y in zip(a, self.trace_basis)) % 3

    def random(self, rng):
        return tuple(rng.randrange(3) for _ in range(self.degree))


class Loop:
    def __init__(self, level):
        self.field = Field(level)
        self.modulus = 7**level
        self.eta = next(x for x in range(self.modulus)
                        if x % 7 == 2 and (x*x+x+1) % self.modulus == 0)
        self.zero_u = (self.field.zero, self.field.zero, 0, 0)
        self.zero_c = (0, 0)
        self.identity = (self.zero_u, self.zero_c)

    def add_c(self, a, b):
        return ((a[0]+b[0]) % 3, (a[1]+b[1]) % self.modulus)

    def neg_c(self, a):
        return (-a[0] % 3, -a[1] % self.modulus)

    def sub_c(self, a, b):
        return self.add_c(a, self.neg_c(b))

    def add_u(self, a, b):
        f = self.field
        return (f.add(a[0], b[0]), f.add(a[1], b[1]),
                (a[2]+b[2]) % self.modulus, (a[3]+b[3]) % self.modulus)

    def neg_u(self, a):
        f = self.field
        return (f.scale(a[0], -1), f.scale(a[1], -1),
                -a[2] % self.modulus, -a[3] % self.modulus)

    def sub_u(self, a, b):
        return self.add_u(a, self.neg_u(b))

    def half_u(self, a):
        f = self.field
        half = pow(2, -1, self.modulus)
        return (f.scale(a[0], 2), f.scale(a[1], 2),
                half*a[2] % self.modulus, half*a[3] % self.modulus)

    def bimap(self, a, b):
        f = self.field
        value = f.sub(f.mul(a[0], b[1]), f.mul(a[1], b[0]))
        return (f.trace(value), (a[2]*b[3]-a[3]*b[2]) % self.modulus)

    def action(self, c, a):
        scalar = pow(self.eta, c[0], self.modulus)
        f = self.field
        return (f.root_mul(a[0], c[1]), f.root_mul(a[1], c[1]),
                scalar*a[2] % self.modulus, scalar*a[3] % self.modulus)

    def mul(self, x, y):
        u, c = x
        v, d = y
        return (self.add_u(u, self.action(c, v)),
                self.sub_c(self.add_c(c, d), self.bimap(u, v)))

    def ldiv(self, x, target):
        u, c = x
        z, e = target
        v = self.action(self.neg_c(c), self.sub_u(z, u))
        d = self.add_c(self.sub_c(e, c), self.bimap(u, v))
        result = (v, d)
        assert self.mul(x, result) == target
        return result

    def defect_actual(self, x, y, state):
        return self.ldiv(self.mul(x, y), self.mul(x, self.mul(y, state)))

    def hg(self, h, g, state):
        z, e = state
        return (self.action(g, z), self.add_c(e, self.bimap(h, z)))

    def defect_formula(self, x, y, state):
        u, c = x
        v, d = y
        g = self.bimap(u, v)
        h = self.sub_u(self.action(g, self.add_u(u, self.action(c, v))),
                       self.add_u(self.action(d, u), v))
        return self.hg(h, g, state)

    def random(self, rng):
        f = self.field
        return ((f.random(rng), f.random(rng), rng.randrange(self.modulus), rng.randrange(self.modulus)),
                (rng.randrange(3), rng.randrange(self.modulus)))


def test_level(level, samples, rng):
    loop = Loop(level)
    tested = 0
    for _ in range(samples):
        x, y, z, r = [loop.random(rng) for _ in range(4)]
        assert loop.mul(loop.identity, x) == loop.mul(x, loop.identity) == x
        assert loop.mul(x, loop.mul(y, loop.mul(x, z))) == loop.mul(loop.mul(x, loop.mul(y, x)), z)
        actual = loop.defect_actual(x, y, z)
        assert actual == loop.defect_formula(x, y, z)
        assert loop.defect_actual(y, loop.mul(x, y), actual) == z
        h, g = x
        h1, g1 = y
        composed = loop.hg(h, g, loop.hg(h1, g1, z))
        expected = loop.hg(loop.add_u(h1, loop.action(g1, h)), loop.add_c(g, g1), z)
        assert composed == expected
        u, c = x
        w, e = z
        # Equality before applying chi checks every right-nucleus character.
        phase_actual = loop.sub_c(c, loop.bimap(u, w))
        phase_weyl = loop.sub_c(c, loop.bimap(loop.action(loop.neg_c(c), u),
                               loop.add_u(loop.action(c, w), loop.half_u(u))))
        assert phase_actual == phase_weyl
        half_c = (2*c[0] % 3, pow(2, -1, loop.modulus)*c[1] % loop.modulus)
        left = (loop.zero_u, half_c)
        middle = (loop.action(loop.neg_c(half_c), u), loop.zero_c)
        assert loop.mul(left, loop.mul(middle, loop.mul(left, z))) == loop.mul(x, z)
        n = (loop.zero_u, r[1])
        assert loop.mul(x, loop.mul(z, n)) == loop.mul(loop.mul(x, z), n)
        tested += 1
    return {'level': level, 'central_modulus': loop.modulus, 'field_degree': loop.field.degree,
            'eta': loop.eta, 'samples': tested,
            'checked': ['actual Bol identity', 'actual left division', 'defect formula',
                        'Bol inverse defect law', 'H composition', 'Weyl phase for all characters',
                        'Bol palindrome', 'right-nucleus equivariance']}


if __name__ == '__main__':
    rng = random.Random(SEED)
    print(json.dumps({'seed': SEED, 'results': [test_level(1, 96, rng), test_level(2, 32, rng)]}, indent=2))

