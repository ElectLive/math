#!/usr/bin/env python3
"""Construct and check the 10D fixed-free indecomposable two-M module.

Uses the reviewed one-M extension enumerator with its source pin recorded in
bruck-s5-two-m-support.md. Python 3.11+; no external data or output files.
"""
assert __debug__, "Run with assertions enabled"

import contextlib
import io
from pathlib import Path
import runpy
import sys

path = Path(__file__).resolve().parent / 'enumerate_bruck_s5_principal_modules.py'
old = sys.argv
sys.argv = [str(path)]
try:
    with contextlib.redirect_stdout(io.StringIO()):
        z = runpy.run_path(str(path))
finally:
    sys.argv = old
apply, mul, inv = z['apply'], z['mul'], z['inv']
getq, coh, block, hom = z['getq'], z['coh'], z['block'], z['hom_basis']
M = getq('M')
classes, dim = coh(*M, 0, 1)
# The helper constructs distinct cohomology classes; the two selected
# coordinates are independent and the fourth is their sum.
assert dim == 8 and len(set(classes)) == 4 and classes[0] == 0
assert classes[1] ^ classes[2] == classes[3]

def transpose(a):
    return tuple(sum(((a[j] >> i) & 1) << j for j in range(len(a)))
                 for i in range(len(a)))

def dual(a):
    return transpose(inv(a))

def extension(v):
    mask = (1 << dim) - 1
    return tuple(dual(block(M[i], 0, 1, (v >> (i * dim)) & mask))
                 for i in range(2))

e1, e2 = extension(classes[1]), extension(classes[2])
identity = tuple(1 << i for i in range(10))
Q = []
for g in range(2):
    a, b = e1[g], e2[g]
    # In the dual extension the last four coordinates form the M socle,
    # and the first two are the regular-sign quotient.
    assert all(a[i] == b[i] and (a[i] & 3) == 0 for i in range(2, 6))
    cols = [((a[i + 2] >> 2) & 15) for i in range(4)]
    cols += [((a[i + 2] >> 2) & 15) << 4 for i in range(4)]
    for i in range(2):
        assert (a[i] & 3) == (b[i] & 3) == (2 if i == 0 else 1)
        cols.append(((a[i] >> 2) & 15) | (((b[i] >> 2) & 15) << 4)
                    | ((a[i] & 3) << 8))
    Q.append(tuple(cols))
Q = tuple(Q)
assert Q == ((7, 12, 10, 8, 112, 192, 160, 128, 652, 386),
             (2, 4, 8, 1, 32, 64, 128, 16, 512, 256))

# Check the representation against the faithful six-point S5 model, including
# all group relations and injectivity of the generated matrix action.
C, D = z['C'], z['Dp']
def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))
i6 = tuple(range(6))
seen = {i6: identity}
queue = [i6]
for p in queue:
    for pp, A in ((C, Q[0]), (D, Q[1])):
        target, matrix = compose(p, pp), mul(seen[p], A)
        if target not in seen:
            seen[target] = matrix
            queue.append(target)
        else:
            assert seen[target] == matrix
assert len(seen) == len(set(seen.values())) == 120

# Both four-dimensional restrictions are irreducible; the top quotient swaps
# its two basis vectors, hence is the regular sign module R.
for shift in (0, 4):
    for x in range(1, 16):
        orbit, todo = {x << shift}, [x << shift]
        for v in todo:
            for A in Q:
                y = apply(A, v)
                if y not in orbit:
                    orbit.add(y)
                    todo.append(y)
        assert len(orbit) == 15
fixed = [v for v in range(1024) if all(apply(g, v) == v for g in Q)]
assert fixed == [0]
r = len({apply(Q[0], v) ^ v for v in range(1024)}).bit_length() - 1
assert r == 5

endom = hom(Q, Q)
assert len(endom) == 2
zero = tuple(0 for _ in range(10))
for mask in range(1 << len(endom)):
    a = zero
    for j, e in enumerate(endom):
        if mask >> j & 1:
            a = tuple(x ^ y for x, y in zip(a, e))
    assert mul(a, a) != a or a in (zero, identity)
print('Ext(R,M): 4 classes; chosen coordinates independent.')
print('Faithful S5 matrices: 120; socle M^2 and top regular sign checked.')
print('Fixed space dimension 0; transposition rank 5; End dimension 2.')
print('All four endomorphisms checked: no nontrivial idempotent.')
