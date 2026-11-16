#!/usr/bin/env python3
"""Check the common J/V6 witness for the projective-only reduction.

Uses the P/F-normalizer and reviewed module helpers pinned in the accompanying
manuscript. This finite witness does not itself prove the envelope reduction.
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
apply, hom, rank = z['apply'], z['hom'], z['rank']
evalword, perms, P, Q = z['evalword'], z['perms'], z['P'], z['Q']
c6, d6 = z['C'], z['D']
add = d['add']
c5, d5 = (1, 0, 2, 3, 4), (0, 2, 3, 4, 1)

def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))

def actn(v, p):
    out = 0
    for i in range(4):
        if v >> i & 1:
            out ^= (1 << p[0]) ^ (1 << p[i + 1])
    return (out >> 1) & 15

# Verify that the paired point actions are two faithful models of the same S5.
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
np, nq = evalword(N, perms[P]), evalword(N, perms[Q])
assert apply(N[0], 2) ^ 2 == 1
assert apply(N[0], 1) == 1

# Odd t swaps the two N coordinates of U, applying the N action on each.
def t_u(v):
    return (apply(N[0], v >> 4) | (apply(N[0], v & 15) << 4))
assert t_u(1) ^ 1 == 17  # (1,1) in the two four-bit coordinates


def coord(basis, v):
    for i in range(1 << len(basis)):
        if apply(basis, i) == v:
            return i
    raise ValueError('vector outside [P,X]')

for name in ('J', 'V6'):
    X = d['getq'](name)
    px, qx = evalword(X, perms[P]), evalword(X, perms[Q])
    space = {}
    for i in range(len(X[0])):
        add(space, px[i] ^ (1 << i))
    basis = tuple(space.values())
    assert basis == (3, 10, 23, 6)
    S = tuple(tuple(coord(basis, apply(A, v)) for v in basis)
              for A in (px, qx))
    intertwiners = hom(S, (np, nq))
    assert len(intertwiners) == 1 and rank(intertwiners[0]) == 4
    phi = intertwiners[0]
    assert apply(phi, coord(basis, 17)) == 1
    assert apply(px, 4) == 4
    assert apply(X[0], 21) == 21
    if name == 'V6':
        assert apply(X[0], 32) ^ 32 == 21
    else:
        assert all(apply(X[0], v) ^ v != 21 for v in range(32))
    print(name, 'S basis', basis, 'phi', phi,
          'v=17, l=4, phi(v)=1, t fixes v+l=21')
print('V6: (1+t)32=21; N: (1+t)2=1; U: (1+t)(1,0)=(1,1).')
print('Paired S5 order 120; common witness verified.')
