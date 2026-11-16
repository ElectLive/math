#!/usr/bin/env python3
"""Enumerate U_3(4) and involutions in PGU_3(4) times x -> x^4.

GF(16) = F2[x]/(x^4+x+1); matrices act on column vectors and
preserve h(v,w)=sum v_i w_i^4. No external inputs or libraries.
"""
from itertools import product
from collections import Counter


def multiply(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 16:
            a ^= 0b10011
    return out


M = [[multiply(a, b) for b in range(16)] for a in range(16)]
def power(a, n):
    x = 1
    while n:
        if n & 1:
            x = M[x][a]
        a = M[a][a]
        n >>= 1
    return x

bar = [power(a, 4) for a in range(16)]
assert all(power(a, 16) == a for a in range(16))
assert all(power(a, 15) == 1 for a in range(1, 16))
scalars = tuple(a for a in range(1, 16) if M[a][bar[a]] == 1)
assert len(scalars) == 5

def herm(v, w):
    return M[v[0]][bar[w[0]]] ^ M[v[1]][bar[w[1]]] ^ M[v[2]][bar[w[2]]]

def scalar_matrix_product(A):
    # A is stored as columns; find whether A * bar(A) is scalar.
    rows = tuple(zip(*A))
    diag = None
    for i in range(3):
        for j in range(3):
            x = M[rows[i][0]][bar[A[j][0]]] ^ M[rows[i][1]][bar[A[j][1]]] ^ M[rows[i][2]][bar[A[j][2]]]
            if i == j:
                if diag is None:
                    diag = x
                elif x != diag:
                    return None
            elif x:
                return None
    return diag

def projective(A):
    return min(tuple(M[a][x] for col in A for x in col) for a in scalars)

vectors = list(product(range(16), repeat=3))
unit = [v for v in vectors if herm(v, v) == 1]
assert len(unit) == 1040
orth = {v: [w for w in unit if herm(v, w) == 0] for v in unit}
assert all(len(v) == 60 for v in orth.values())
# For any v,w orthonormal the last column is selected by intersecting
# their explicitly enumerated orthogonal norm-one vectors.
ortho_sets = {v: set(vs) for v, vs in orth.items()}
classes = set()
outer = set()
scalar_counts = Counter()
linear = 0
fixed_linear = 0
for v in unit:
    for w in orth[v]:
        zlist = ortho_sets[v] & ortho_sets[w]
        assert len(zlist) == 5
        for z in zlist:
            A = (v, w, z)
            linear += 1
            if all(bar[x] == x for col in A for x in col):
                fixed_linear += 1
            key = projective(A)
            classes.add(key)
            scalar = scalar_matrix_product(A)
            if scalar is not None:
                assert scalar in scalars
                scalar_counts[scalar] += 1
                outer.add(key)
assert fixed_linear == 60
assert linear == 312000
assert len(classes) == 62400 and len(classes) * len(scalars) == linear
assert len(outer) == 1040 and sum(scalar_counts.values()) == 5 * len(outer)
# Square scalars lie both in F4 and in the norm-one group, so are 1.
assert scalar_counts == {1: 5200}
print('norm-one vectors', len(unit), 'orthogonal norm-one vectors', 60)
print('unitary matrices', linear, 'scalar center', len(scalars), 'projective matrices', len(classes))
print('F4-entry unitary matrices', fixed_linear, 'quotient', len(classes) // fixed_linear)
print('semilinear involutions', len(outer), 'linear lifts by square scalar', sorted(scalar_counts.items()))
