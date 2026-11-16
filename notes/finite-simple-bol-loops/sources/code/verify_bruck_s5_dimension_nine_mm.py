#!/usr/bin/env python3
"""Two H1 tensor calculations and the d=9 MM transversal obstruction.

The two-generator presentation is Nagy, arXiv:0709.4544v1, Lemma 3.1.
All vector and matrix arithmetic is over F2. No group extensions are enumerated.
"""
from itertools import product

C = (1, 0, 3, 2, 5, 4)
D = (0, 2, 3, 4, 1, 5)
IDENTITY = tuple(range(6))


def perm_mul(a, b):
    return tuple(a[b[i]] for i in range(6))


def perm_inv(a):
    return tuple(a.index(i) for i in range(6))


def perm_power(a, n):
    out = IDENTITY
    for _ in range(n):
        out = perm_mul(out, a)
    return out


def action_m(v, p):
    bits = 0
    for i in range(4):
        if v >> i & 1:
            bits ^= (1 << p[0]) ^ (1 << p[i + 1])
    if bits >> 5 & 1:
        bits ^= 63
    return (bits >> 1) & 15


def action_j(v, p):
    bits = 0
    for i in range(5):
        if v >> i & 1:
            bits ^= 1 << p[i]
    if bits >> 5:
        bits ^= 63
    return bits


def action_e(v, p, kind):
    if kind == 'split':
        return action_m(v & 15, p) | (v & 16)
    if kind == 'J':
        return action_j(v, p)
    bits = 0
    for i in range(5):
        if v >> i & 1:
            bits ^= (1 << p[i]) ^ (1 << p[5])
    return bits & 31


def linear(cols, v):
    out = 0
    for i, col in enumerate(cols):
        if v >> i & 1:
            out ^= col
    return out


def matrix_mul(a, b):
    return tuple(linear(a, col) for col in b)


def rank(vectors):
    pivots = {}
    for value in vectors:
        while value:
            bit = value.bit_length() - 1
            if bit in pivots:
                value ^= pivots[bit]
            else:
                pivots[bit] = value
                break
    return len(pivots)


def check_h1(kind):
    other_dim = 4 if kind == 'MM' else 5
    dim = 4 * other_dim
    other_action = action_m if kind == 'MM' else action_j

    def tensor_matrix(p):
        cols = []
        for i in range(4):
            a = action_m(1 << i, p)
            for j in range(other_dim):
                b = other_action(1 << j, p)
                cols.append(sum(1 << (other_dim * x + y)
                                for x in range(4) for y in range(other_dim)
                                if a >> x & 1 and b >> y & 1))
        return tuple(cols)

    ident = tuple(1 << i for i in range(dim))
    c, d = tensor_matrix(C), tensor_matrix(D)
    group, queue = {ident}, [ident]
    for a in queue:
        for b in (c, d):
            element = matrix_mul(a, b)
            if element not in group:
                group.add(element)
                queue.append(element)
    assert len(group) == 120
    inverses = {a: next(b for b in group if matrix_mul(a, b) == ident)
                for a in group}

    def multiply(a, b):
        p, v = a
        q, w = b
        return matrix_mul(p, q), v ^ linear(p, w)

    def inverse(a):
        p, v = a
        q = inverses[p]
        return q, linear(q, v)

    identity = (ident, 0)

    def power(a, n):
        out = identity
        for _ in range(n):
            out = multiply(out, a)
        return out

    def residues(x, y):
        a, b = (c, x), (d, y)
        comm = multiply(multiply(multiply(inverse(a), inverse(b)), a), b)
        values = [power(a, 2), power(b, 4), power(multiply(a, b), 5),
                  power(comm, 3)]
        assert all(matrix == ident for matrix, _ in values)
        return sum(value << (dim * i) for i, (_, value) in enumerate(values))

    constraints = [residues(1 << i, 0) for i in range(dim)]
    constraints += [residues(0, 1 << i) for i in range(dim)]
    principal = [(linear(c, 1 << i) ^ (1 << i)) |
                 ((linear(d, 1 << i) ^ (1 << i)) << dim)
                 for i in range(dim)]
    mask = (1 << dim) - 1
    assert all(residues(v & mask, v >> dim) == 0 for v in principal)
    residue_rank, principal_rank = rank(constraints), rank(principal)
    assert (residue_rank, principal_rank) == ((17, 15) if kind == 'MM' else (21, 19))
    assert 2 * dim - residue_rank == principal_rank
    print(kind, 'relator rank', residue_rank, 'Z1 dimension', 2 * dim - residue_rank,
          'B1 dimension', principal_rank, 'H1 dimension 0')


for name in ('MM', 'MJ'):
    check_h1(name)

# Construct the actual C5 normalizer in the 6-point S5 action.
group, queue = {IDENTITY}, [IDENTITY]
for a in queue:
    for b in (C, D):
        element = perm_mul(a, b)
        if element not in group:
            group.add(element)
            queue.append(element)
assert len(group) == 120
p = perm_mul(C, D)
assert perm_power(p, 5) == IDENTITY and p != IDENTITY
h = next(a for a in sorted(group)
         if perm_power(a, 4) == IDENTITY and perm_power(a, 2) != IDENTITY
         and perm_mul(perm_mul(a, p), perm_inv(a)) in
         {perm_power(p, i) for i in range(1, 5)})
assert len({perm_power(p, i) for i in range(5)}) == 5

for kind in ('split', 'J', 'dual'):
    module_u = {v ^ action_e(v, p, kind) for v in range(32)}
    assert len(module_u) == 16
    maps = []
    for cols in product(module_u, repeat=4):
        if any(action_e(cols[i], a, kind) != linear(cols, action_m(1 << i, a))
               for i in range(4) for a in (p, h)):
            continue
        mapping = [linear(cols, v) for v in range(16)]
        if len(set(mapping)) == 16:
            maps.append(mapping)
    assert len(maps) == 1
    phi = maps[0]
    image = {v ^ (action_m(v & 15, C) | (action_e(v >> 4, C, kind) << 4))
             for v in range(512)}
    assert len(image) == 16
    for mode in ('Eonly', 'diagonal'):
        W = {(v if mode == 'diagonal' else 0) | (phi[v] << 4)
             for v in range(16)}
        assert len(W) == 16
        count = len(W & image)
        assert count == (2 if kind == 'dual' else 4)
        print(kind, mode, '|W ∩ (1+t)V| =', count)
