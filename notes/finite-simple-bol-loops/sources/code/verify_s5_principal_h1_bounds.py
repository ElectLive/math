#!/usr/bin/env python3
"""Cayley-cocycle dimensions used for a candidate one-M module bound.

The representations are M, J and V6 from the S5 radical manuscripts. We
construct dual matrices explicitly and check every Cayley edge for cocycle
consistency. This finite check does not prove the surrounding module reduction.
"""
C = (1, 0, 3, 2, 5, 4)
D = (0, 2, 3, 4, 1, 5)


def action_j(v, p):
    value = 0
    for i in range(5):
        if v >> i & 1:
            value ^= 1 << p[i]
    if value >> 5:
        value ^= 63
    return value


def action_m(v, p):
    value = 0
    for i in range(4):
        if v >> i & 1:
            value ^= (1 << p[0]) ^ (1 << p[i + 1])
    if value >> 5 & 1:
        value ^= 63
    return (value >> 1) & 15


def apply(matrix, v):
    result = 0
    for i, column in enumerate(matrix):
        if v >> i & 1:
            result ^= column
    return result


def multiply(a, b):
    return tuple(apply(a, col) for col in b)


def inverse(matrix):
    n = len(matrix)
    pivots = {}
    for i, col in enumerate(matrix):
        v, witness = col, 1 << i
        while v:
            bit = v.bit_length() - 1
            if bit in pivots:
                v ^= pivots[bit][0]
                witness ^= pivots[bit][1]
            else:
                pivots[bit] = (v, witness)
                break
    assert len(pivots) == n
    result = []
    for i in range(n):
        v, witness = 1 << i, 0
        while v:
            bit = v.bit_length() - 1
            v ^= pivots[bit][0]
            witness ^= pivots[bit][1]
        result.append(witness)
    return tuple(result)


def dual(matrix):
    inverse_matrix = inverse(matrix)
    n = len(matrix)
    return tuple(sum(((inverse_matrix[i] >> j) & 1) << i for i in range(n))
                 for j in range(n))


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


def h1(first, second, expected_order):
    n = len(first)
    identity = tuple(1 << i for i in range(n))
    generators = (first, second)
    # Each entry is the n-bit coefficient column of one unknown generator bit.
    seen = {identity: (0,) * (2 * n)}
    queue = [identity]
    rows = []
    for g in queue:
        old = seen[g]
        for j, h in enumerate(generators):
            target = multiply(g, h)
            candidate = tuple(old[i] ^ (g[i - j * n] if j * n <= i < (j + 1) * n else 0)
                              for i in range(2 * n))
            if target not in seen:
                seen[target] = candidate
                queue.append(target)
            else:
                differences = tuple(x ^ y for x, y in zip(candidate, seen[target]))
                rows.extend(sum(((v >> bit) & 1) << i for i, v in enumerate(differences))
                            for bit in range(n))
    assert len(seen) == expected_order
    principal = [(first[i] ^ (1 << i)) | ((second[i] ^ (1 << i)) << n)
                 for i in range(n)]
    assert all((row & v).bit_count() % 2 == 0 for row in rows for v in principal)
    constraint_rank = rank(rows)
    principal_rank = rank(principal)
    return constraint_rank, principal_rank, 2 * n - constraint_rank - principal_rank


def power(a, n):
    result = tuple(1 << i for i in range(len(a)))
    for _ in range(n):
        result = multiply(result, a)
    return result


expected = {'M': ((3, 4, 1), (2, 4, 2)),
            'J': ((4, 4, 2), (4, 4, 2)),
            'V6': ((6, 5, 1), (6, 4, 2))}
for name in ('M', 'J', 'V6'):
    if name == 'M':
        c = tuple(action_m(1 << i, C) for i in range(4))
        d = tuple(action_m(1 << i, D) for i in range(4))
    elif name == 'J':
        c = tuple(action_j(1 << i, C) for i in range(5))
        d = tuple(action_j(1 << i, D) for i in range(5))
    else:
        c = tuple([action_j(1 << i, C) for i in range(5)] + [32 ^ 21])
        d = tuple([action_j(1 << i, D) for i in range(5)] + [32 ^ 1])
    c, d = dual(c), dual(d)
    # Nagy Lemma 3.1: d^2 and [c,d] generate A5.
    comm = multiply(multiply(multiply(inverse(c), inverse(d)), c), d)
    s5 = h1(c, d, 120)
    a5 = h1(power(d, 2), comm, 60)
    assert (s5, a5) == expected[name]
    print(name, 'S5 (constraint, principal, H1):', s5,
          'A5 (constraint, principal, H1):', a5)
