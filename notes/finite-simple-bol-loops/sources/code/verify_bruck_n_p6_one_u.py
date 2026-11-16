#!/usr/bin/env python3
"""Derive the P6/U F20 cross-map restrictions for the b=1 obstruction.

Imports the fixed-component equation solver and module/action models from
verify_bruck_n_quadratic_support.py and verify_bruck_one_m_noncentral.py.
This checks a finite representation-theoretic lemma, not existence or
nonexistence of a Bruck envelope. Run with Python 3.11+ and assertions enabled.
"""
from pathlib import Path
import contextlib
import io
import runpy

assert __debug__
HERE = Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    components = runpy.run_path(str(HERE / 'verify_bruck_n_quadratic_support.py'))
    model = runpy.run_path(str(HERE / 'verify_bruck_one_m_noncentral.py'))

add, rank = components['add'], components['rank']
nullspace, nact, mv = model['nullspace'], model['nact'], model['mv']
generators = (model['p'], model['qgen'])

def solutions(indices, rows):
    """Nullspace of the selected coordinates of the full equations."""
    pivots = {}
    for row in rows:
        add(pivots, sum(((row >> source) & 1) << j
                        for j, source in enumerate(indices)))
    result = []
    for i in range(len(indices)):
        if i in pivots:
            continue
        vector = 1 << i
        for j in sorted(pivots):
            if (pivots[j] & vector).bit_count() & 1:
                vector |= 1 << j
        result.append(sum(((vector >> j) & 1) << source
                          for j, source in enumerate(indices)))
    return result

def intertwiners(codomain_action, dimension):
    """Solve Hom_F20(N, codomain) using the 5- and 4-cycle generators."""
    equations = []
    for g in generators:
        for i in range(4):
            image = nact(1 << i, g[0])
            for bit in range(dimension):
                row = 0
                for j in range(4):
                    if image >> j & 1:
                        row ^= 1 << (dimension * j + bit)
                for j in range(dimension):
                    if codomain_action(1 << j, g) >> bit & 1:
                        row ^= 1 << (dimension * i + j)
                equations.append(row)
    return [tuple((h >> (dimension * i)) & ((1 << dimension) - 1)
                  for i in range(4)) for h in nullspace(equations, 4 * dimension)]

data = components['component']('P6')
base, mon, feature = data['base'], data['mon'], data['feat']
rows = data['allrows'] + data['extra']
cross = solutions(data['groups']['XU0'], rows)
top, = solutions(data['groups']['U0'], rows)
assert len(cross) == 2

def quadratic(coefficients, vector):
    value, features = 0, feature(vector)
    for i in range(len(mon)):
        if features >> i & 1:
            value ^= (coefficients >> (4 * i)) & 15
    return value

def polar(coefficients, x, y):
    return (quadratic(coefficients, x) ^ quadratic(coefficients, y)
            ^ quadratic(coefficients, x ^ y))

X_maps = intertwiners(lambda v, g: data['baseact'](v, g[1]), 6)
assert len(X_maps) == 1 and rank(X_maps[0]) == 4
X = X_maps[0]

def U_action(v, g):
    if g == generators[1]:
        return model['uact'](v, g[0])
    return nact(v & 15, g[0]) | (nact(v >> 4, g[0]) << 4)

U_maps = intertwiners(U_action, 8)
assert len(U_maps) == 2

def epsilon(v):
    return ((v & 15) ^ (v >> 4)) * 17

Soc = tuple(epsilon(x) for x in next(B for B in U_maps
                                    if rank(epsilon(x) for x in B) == 4))
D = next(B for B in U_maps if rank(list(B) + list(Soc)) == 8)
assert rank(Soc) == 4 and rank(D) == 4
fixed = model['u1']
assert fixed.bit_count() % 2 == 1
assert all(data['baseact'](fixed, g[1]) == fixed for g in model['F'])
assert rank(list(X) + [fixed]) == 5
assert all(quadratic(top, mv(D, s) << base)
           == ((mv(D, s) & 15) ^ (mv(D, s) >> 4)) for s in range(16))
assert all(quadratic(top, mv(Soc, s) << base) == 0 for s in range(16))

def fixed_restriction(co, embedding):
    return tuple(polar(co, fixed, u << base) for u in embedding)

def bilinear_restriction(co, left, right):
    return tuple(polar(co, x, u << base) for x in left for u in right)

# The nonzero intertwiner ι is determined by the reviewed top projection.
iota = tuple((u & 15) ^ (u >> 4) for u in D)
assert rank(iota) == 4
space = [cross[0], cross[1], cross[0] ^ cross[1]]
zero4, zero16 = (0,) * 4, (0,) * 16
beta0 = next(c for c in space
             if fixed_restriction(c, D) == iota
             and fixed_restriction(c, Soc) == zero4)
beta1 = next(c for c in space
             if fixed_restriction(c, D) == zero4
             and fixed_restriction(c, Soc) == iota)
assert beta0 != beta1 and rank([beta0, beta1]) == 2
assert bilinear_restriction(beta0, X, D) == zero16
assert bilinear_restriction(beta0, X, Soc) == zero16
assert bilinear_restriction(beta1, X, Soc) == zero16
assert bilinear_restriction(beta1, X, D) != zero16
# Polar radical of soc(U) when the β1 coefficient is zero: test on all
# basis vectors of P6 and U. The top map has zero polar.
for x in (1, 2, 4, 8, 16, 32):
    for u in (1, 2, 4, 8, 16, 32, 64, 128):
        assert polar(beta0, x, epsilon(u) << base) == 0
for u in (1, 2, 4, 8, 16, 32, 64, 128):
    for v in (1, 2, 4, 8, 16, 32, 64, 128):
        assert polar(top, u << base, v << base) == 0
print('P6 one-U cross-map restrictions passed')
