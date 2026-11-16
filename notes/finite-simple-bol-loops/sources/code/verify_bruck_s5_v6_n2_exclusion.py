#!/usr/bin/env python3
"""Verify all F20 stabilizers collide for the V6 plus N squared module.

Imports the principal-stabilizer helper and its reviewed dependencies; Python
3.11+ required. This verifies module-level transversality, not a loop census.
"""
assert __debug__, "Run with assertions enabled"

import contextlib
import io
from pathlib import Path
import runpy
import sys

code = Path(__file__).resolve().parent
old = sys.argv
sys.argv = [str(code / 'verify_bruck_s5_principal_stabilizer_fixed.py')]
try:
    with contextlib.redirect_stdout(io.StringIO()):
        z = runpy.run_path(sys.argv[0])
finally:
    sys.argv = old

d = z['d']
apply, rank, hom = z['apply'], z['rank'], z['hom']
evalword, perms = z['evalword'], z['perms']
P, Q, kernel = z['P'], z['Q'], z['kernel']
add, X = d['add'], d['getq']('V6')
c6, d6 = z['C'], z['D']
c5, d5 = (1, 0, 2, 3, 4), (0, 2, 3, 4, 1)

def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))

def actn(v, p):
    out = 0
    for i in range(4):
        if v >> i & 1:
            out ^= (1 << p[0]) ^ (1 << p[i + 1])
    return (out >> 1) & 15

# Check that the 6-point and natural 5-point generators define the same
# faithful S5, independently of the precomputed module words.
i6, i5 = tuple(range(6)), tuple(range(5))
pairs = {i6: i5}
queue = [i6]
for x in queue:
    for a, b in ((c6, c5), (d6, d5)):
        q6, q5 = compose(x, a), compose(pairs[x], b)
        if q6 not in pairs:
            pairs[q6] = q5
            queue.append(q6)
        else:
            assert pairs[q6] == q5
assert len(pairs) == len(set(pairs.values())) == 120

N = tuple(tuple(actn(1 << i, p) for i in range(4)) for p in (c5, d5))
# Two independent copies of N, without the swap used for the projective U.
N2 = tuple(tuple(list(g) + [a << 4 for a in g]) for g in N)
V = tuple(tuple(list(X[j]) + [a << 6 for a in N2[j]]) for j in range(2))
n = 14
pv, qv = evalword(V, perms[P]), evalword(V, perms[Q])
k = kernel(tuple(pv[i] ^ (1 << i) for i in range(n)))
assert len(k) == 2

# Principal nontrivial F20 constituent S=[P,V6].
px = evalword(X, perms[P])
bb = {}
for i in range(6):
    add(bb, px[i] ^ (1 << i))
basis = tuple(bb.values())
assert len(basis) == 4

def coord(b, v):
    for i in range(1 << len(b)):
        if apply(b, i) == v:
            return i
    raise ValueError('vector outside constituent')

def restrict(A, b):
    return tuple(coord(b, apply(A, x)) for x in b)

def span(b):
    return {apply(b, i) for i in range(1 << len(b))}

S = (restrict(evalword(X, perms[P]), basis),
     restrict(evalword(X, perms[Q]), basis))
h = hom(S, (pv, qv))
assert len(h) == 3
image_t = tuple(V[0][i] ^ (1 << i) for i in range(n))
assert rank(image_t) == 5
displacements = span(image_t)
intersections, subspaces = [], set()
for mask in range(1, 8):
    f = tuple(0 for _ in range(4))
    for j, vector in enumerate(h):
        if mask >> j & 1:
            f = tuple(x ^ y for x, y in zip(f, vector))
    assert rank(f) == 4
    simple = span(f)
    assert all(apply(g, v) in simple for g in (pv, qv) for v in f)
    # Every nonzero vector generates the whole F20 constituent.
    for x in simple - {0}:
        orbit, todo = {x}, [x]
        for v in todo:
            for g in (pv, qv):
                y = apply(g, v)
                if y not in orbit:
                    orbit.add(y)
                    todo.append(y)
        assert rank(tuple(orbit)) == 4
    W = tuple(k) + f
    assert rank(W) == 6
    ws = span(W)
    assert all(apply(g, v) in ws for g in (pv, qv) for v in W)
    assert frozenset(ws) not in subspaces
    subspaces.add(frozenset(ws))
    intersection = ws & displacements
    intersections.append(len(intersection).bit_length() - 1)
    print('line', mask, 'W dimension', 6, 'intersection dimension',
          intersections[-1], 'witness', min(intersection - {0}))
assert len(subspaces) == 7
assert intersections == [3, 1, 1, 1, 1, 1, 1]
print('Paired S5 order 120; seven distinct F20-stable W; all collide.')
