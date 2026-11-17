#!/usr/bin/env python3
"""Exact small checks for bol-cocycle-packets.md; Python standard library only.

No huge simple loop, classification interface, or modular transformation is
verified here. The symbolic proofs retain their explicitly pinned dependencies.
"""
from collections import Counter
from itertools import product


def rank_mod(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    r = 0
    for j in range(len(a[0])):
        pivot = next((k for k in range(r, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = pow(a[r][j], -1, p)
        a[r] = [x * scale % p for x in a[r]]
        for k in range(len(a)):
            if k != r:
                scale = a[k][j]
                a[k] = [(x - scale * y) % p for x, y in zip(a[k], a[r])]
        r += 1
    return r


def dot(x, y, p=3):
    return sum(a * b for a, b in zip(x, y)) % p


def rigid_check():
    b0 = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 2, 0, 0]]
    b1 = [[0, 0, 0, 2], [0, 1, 1, 0], [0, 1, 0, 0], [2, 0, 0, 0]]
    b2 = [[0, 2, 1, 1], [1, 1, 0, 2], [2, 2, 0, 0], [0, 1, 0, 0]]
    assert b1 == list(map(list, zip(*b1)))
    f, fp, nf, n2f = (1, 2, 1), (1, 2, 0), (0, 1, 2), (0, 0, 1)
    phase = (1, 0, 1)
    fibers = []
    ranks = []
    for g in (f, fp):
        fiber = [ell for ell in product(range(3), repeat=3)
                 if tuple(dot(ell, v) for v in (g, nf, n2f)) == phase]
        assert len(fiber) == 1
        ell = fiber[0]
        fibers.append(ell)
        b = [[sum(c * m[i][j] for c, m in zip(ell, (b0, b1, b2))) % 3
              for j in range(4)] for i in range(4)]
        a = [[(b[i][j] - b[j][i]) % 3 for j in range(4)] for i in range(4)]
        ranks.append(rank_mod(a, 3))
    assert fibers == [(1, 1, 1), (2, 1, 1)]
    assert ranks == [4, 2]
    rank_histogram = Counter()
    for x, y, z in product(range(3), repeat=3):
        b = [[(x*b0[i][j]+y*b1[i][j]+z*b2[i][j]) % 3
              for j in range(4)] for i in range(4)]
        a = [[(b[i][j]-b[j][i]) % 3 for j in range(4)] for i in range(4)]
        rank_histogram[18*rank_mod(a, 3)] += 1
    assert rank_histogram == {0: 3, 36: 12, 72: 12}
    for c in range(3):
        a = [[(b2[i][j] + c*b0[i][j] - b2[j][i] - c*b0[j][i]) % 3
              for j in range(4)] for i in range(4)]
        assert rank_mod(a, 3) == (2 if c == 2 else 4)
        if c == 2:
            for v in ((1, 1, 1, 0), (0, 0, 1, 1)):
                assert all(dot(row, v) == 0 for row in a)
    print("rigid phase fibers:", fibers, "; E-ranks:", ranks,
          "; F3 trace ranks:", [18*r for r in ranks],
          "; unphased histogram:", dict(rank_histogram))


def small_loop_check():
    q, m, alpha = 3, 2, 2
    elems = list(product(range(q), range(q), range(m), range(q)))
    index = {x: i for i, x in enumerate(elems)}

    def multiply(x, y):
        u1, u2, t, s = x
        v1, v2, r, h = y
        scale = pow(alpha, t, q)
        return ((u1 + scale*v1) % q, (u2 + scale*v2) % q,
                (t+r) % m, (s+h-u1*v2+u2*v1) % q)

    n = len(elems)
    table = [[index[multiply(x, y)] for y in elems] for x in elems]
    identity = index[(0, 0, 0, 0)]
    assert table[identity] == list(range(n))
    assert [row[identity] for row in table] == list(range(n))
    assert all(len(set(row)) == n for row in table)
    assert all(len({row[j] for row in table}) == n for j in range(n))
    for x, y, z in product(range(n), repeat=3):
        assert table[x][table[y][table[x][z]]] == table[table[x][table[y][x]]][z]
    x, y, z = [index[a] for a in ((0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0))]
    lhs, rhs = table[table[x][y]][table[z][x]], table[table[x][table[y][z]]][x]
    assert lhs != rhs
    assert (elems[lhs][-1], elems[rhs][-1]) == (1, 2)

    inv_left = []
    for row in table:
        inverse = [None]*n
        for i, j in enumerate(row):
            inverse[j] = i
        inv_left.append(inverse)
    histogram = Counter()
    for x, y in product(range(n), repeat=2):
        xy = table[x][y]
        defect = [inv_left[xy][table[x][table[y][z]]] for z in range(n)]
        u1, u2, t, s = elems[x]
        v1, v2, r, h = elems[y]
        c1 = ((1-pow(alpha, r, q))*u1 + (pow(alpha, t, q)-1)*v1) % q
        c2 = ((1-pow(alpha, r, q))*u2 + (pow(alpha, t, q)-1)*v2) % q
        for z, (w1, w2, k, ell) in enumerate(elems):
            expected = (w1, w2, k, (ell+c1*w2-c2*w1) % q)
            assert elems[defect[z]] == expected
        seen = set()
        cycle_counts = Counter()
        for z in range(n):
            if z not in seen:
                length, u = 0, z
                while u not in seen:
                    seen.add(u)
                    length += 1
                    u = defect[u]
                cycle_counts[length] += 1
        histogram[tuple(sorted(cycle_counts.items()))] += 1
    assert histogram == {((1, 54),): 972, ((1, 18), (3, 12)): 1944}
    print("order-54 control: all", n**3, "left Bol triples checked; Moufang witness:",
          elems[lhs], elems[rhs], "; defect cycle histogram:", dict(histogram))


def jordan_check():
    for p, degree in ((3, 3), (5, 2), (7, 1)):
        for ns in product(range(3), repeat=p):
            ranks = [2*degree*sum(n*max(ell-k, 0) for ell, n in enumerate(ns, 1))
                     for k in range(p+2)]
            recovered = tuple((ranks[k-1]-2*ranks[k]+ranks[k+1])//(2*degree)
                              for k in range(1, p+1))
            assert recovered == ns
    print("paired-Jordan second differences recovered all sampled multiplicity vectors")


def root_graph_check():
    """F4=F2[w]/(w^2+w+1), coordinates 0,1,w,w+1 encoded 0..3."""
    def mul(x, y):
        out = 0
        while y:
            if y & 1:
                out ^= x
            y >>= 1
            x <<= 1
            if x & 4:
                x ^= 7
        return out

    def frob(x, j):
        return mul(x, x) if j else x

    maps = [tuple(mul(a, x) ^ mul(b, mul(x, x)) for x in range(4))
            for a, b in product(range(4), repeat=2) if a or b]
    assert len(set(maps)) == 15

    def rank(values):
        return {1: 0, 2: 1, 4: 2}[len(set(values))]

    def profile(phi):
        return {(s, t): rank([mul(s, phi[x]) ^ phi[mul(t, x)] for x in range(4)])
                for s, t in product(range(4), repeat=2)}

    def transport(phi, c, d, j):
        # In F4 the nontrivial Frobenius is its own inverse.
        return tuple(mul(c, frob(phi[mul(d, frob(x, j))], j)) for x in range(4))

    for phi, c, d, j in product(maps, range(1, 4), range(1, 4), range(2)):
        psi = transport(phi, c, d, j)
        rp, rs = profile(phi), profile(psi)
        assert rank(phi) == rank(psi)
        assert all(rp[s, t] == rs[frob(s, j), frob(t, j)]
                   for s, t in product(range(4), repeat=2))
    remaining = set(maps)
    sizes = []
    while remaining:
        phi = min(remaining)
        orbit = {transport(phi, c, d, j)
                 for c, d, j in product(range(1, 4), range(1, 4), range(2))}
        sizes.append(len(orbit))
        remaining -= orbit
    assert sorted(sizes) == [3, 3, 9]
    ident = tuple(range(4))
    square = tuple(mul(x, x) for x in range(4))
    trace = tuple(x ^ mul(x, x) for x in range(4))
    assert (rank(ident), rank(square), rank(trace)) == (2, 2, 1)
    assert (profile(ident)[2, 2], profile(square)[2, 2]) == (0, 2)
    print("root-graph F4: all 15 maps, all 270 parameter transports checked; orbit sizes:",
          sorted(sizes), "; three classes separated by marked rank packet")


if __name__ == "__main__":
    rigid_check()
    small_loop_check()
    jordan_check()
    root_graph_check()
