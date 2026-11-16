#!/usr/bin/env python3
"""P6⊕U, N² Frattini: exhaustive F20 elementary-shadow check.

Imports the reviewed component solver and its P6 model, plus the reviewed
one-M F20/action model. This finite check is not an envelope construction or
a proof of the actual central-lift obstruction. Run with assertions enabled.
"""
from pathlib import Path
import contextlib
import io
import itertools
import runpy
from functools import lru_cache

assert __debug__
HERE = Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    components = runpy.run_path(str(HERE / 'verify_bruck_n_quadratic_support.py'))
    model = runpy.run_path(str(HERE / 'verify_bruck_one_m_noncentral.py'))
add, rank = components['add'], components['rank']
nullspace, nact, mv = model['nullspace'], model['nact'], model['mv']

def solutions(indices, rows):
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

def span(basis):
    result = [0]
    for v in basis:
        result += [x ^ v for x in result]
    return result

def intertwiners(action, dimension):
    equations = []
    for g in (model['p'], model['qgen']):
        for i in range(4):
            image = nact(1 << i, g[0])
            for bit in range(dimension):
                row = 0
                for j in range(4):
                    if image >> j & 1:
                        row ^= 1 << (dimension*j+bit)
                for j in range(dimension):
                    if action(1 << j, g) >> bit & 1:
                        row ^= 1 << (dimension*i+j)
                equations.append(row)
    return [tuple((h >> (dimension*i)) & ((1 << dimension)-1)
                  for i in range(4)) for h in nullspace(equations, 4*dimension)]

d = components['component']('P6')
base, mon, feature = d['base'], d['mon'], d['feat']
full_rows, zero_rows = d['allrows'], d['allrows'] + d['extra']
full_basis, zero_basis = [], []
for name in ('X', 'U0', 'XU0'):
    full_basis.extend(solutions(d['groups'][name], full_rows))
    zero_basis.extend(solutions(d['groups'][name], zero_rows))
assert len(full_basis) == 5 and len(zero_basis) == 3
full, zero = span(full_basis), span(zero_basis)
assert len(set(full)) == 32 and len(set(zero)) == 8 and set(zero) <= set(full)

@lru_cache(None)
def q(co, v):
    value, features = 0, feature(v)
    for i in range(len(mon)):
        if features >> i & 1:
            value ^= (co >> (4*i)) & 15
    return value

Xmaps = intertwiners(lambda v, g: d['baseact'](v, g[1]), 6)
assert len(Xmaps) == 1 and rank(Xmaps[0]) == 4
X = Xmaps[0]
gens = (model['p'], model['qgen'])
def U_action(v, g):
    if g == gens[1]:
        return model['uact'](v, g[0])
    return nact(v & 15, g[0]) | (nact(v >> 4, g[0]) << 4)
Umaps = intertwiners(U_action, 8)
assert len(Umaps) == 2
def epsilon(v):
    return ((v & 15) ^ (v >> 4))*17
Soc = tuple(epsilon(x) for x in next(B for B in Umaps
                                    if rank(epsilon(x) for x in B) == 4))
D = next(B for B in Umaps if rank(list(B)+list(Soc)) == 8)
assert rank(Soc) == rank(D) == 4

def embed(mask, s):
    return ((mv(X, s) if mask & 1 else 0)
            ^ ((mv(D, s) if mask & 2 else 0) << base)
            ^ ((mv(Soc, s) if mask & 4 else 0) << base))

f1, f2 = model['u1'], model['u2']
assert f1 ^ f2 == 63 and f1.bit_count() % 2 == f2.bit_count() % 2 == 1
assert all(d['baseact'](v, g[1]) == v for v in (f1, f2) for g in model['F'])
assert rank(list(X)+[f1, f2]) == 6
planes = set()
for u, v in itertools.combinations(range(1, 8), 2):
    planes.add(tuple(sorted((u, v, u ^ v))))
assert len(planes) == 7

# Derive the intended component span directly from evaluated maps, not labels.
top, = solutions(d['groups']['U0'], zero_rows)
cross = solutions(d['groups']['XU0'], zero_rows)
assert len(cross) == 2
aug_top = next(co for co in cross if all(
    q(co, x | (u << base)) == ((x.bit_count() & 1)*((u & 15) ^ (u >> 4)))
    for x in range(64) for u in range(256)))
assert all(q(top, u << base) == ((u & 15) ^ (u >> 4)) for u in range(256))
expected_space = {0, top, aug_top, top ^ aug_top}
assert len(expected_space) == 4 and expected_space <= set(zero)

for fixed_basis in ((f1,), (f2,), (f1, f2)):
    survivors = []
    for q0 in zero:
        if not q0:
            continue
        for q1 in full:
            if q1 in (0, q0):
                continue  # coordinate components must be independent
            for plane in sorted(planes):
                u, v = plane[:2]
                basis = ([embed(u, 1 << i) for i in range(4)]
                         + [embed(v, 1 << i) for i in range(4)]
                         + list(fixed_basis))
                # Basis and pair sums test the full quadratic and polar on W.
                samples = basis + [x ^ y for x, y in itertools.combinations(basis, 2)]
                if all(q(q0, x) == q(q1, x) == 0 for x in samples):
                    survivors.append((q0, q1, plane))
    assert len(survivors) == 6
    assert all(plane == (1, 4, 5) for _, _, plane in survivors)
    assert all({0, q0, q1, q0 ^ q1} == expected_space
               for q0, q1, _ in survivors)
print('P6 N² one-U elementary-shadow enumeration passed')
