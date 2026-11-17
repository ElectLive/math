#!/usr/bin/env python3
"""E6 graph-fixed binary torus calculation; not a finite-group construction.

Bourbaki diagram: 1--3--4--5--6 with node 2 attached to 4.
Coordinates use ordered simple roots 1,...,6; graph swaps 1/6 and 3/5.
"""
from collections import Counter, deque

N = 6
EDGES = ((0, 2), (2, 3), (3, 4), (4, 5), (1, 3))
SIGMA = (5, 1, 4, 3, 2, 0)
A = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
for i, j in EDGES:
    A[i][j] = A[j][i] = -1


def root_reflection(v, i):
    w = list(v)
    w[i] -= sum(A[i][j] * v[j] for j in range(N))
    return tuple(w)


def torus_reflection(v, i):
    if v & (1 << i):
        return v ^ sum((A[j][i] % 2) << j for j in range(N))
    return v


def closure(starts, moves):
    seen = set(starts)
    todo = deque(sorted(seen))
    while todo:
        x = todo.popleft()
        for move in moves:
            y = move(x)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def graph_bits(v):
    return sum(((v >> SIGMA[i]) & 1) << i for i in range(N))


def graph_root(v):
    return tuple(v[SIGMA[i]] for i in range(N))


def fixed_roots(roots, v):
    return sum(sum(r[i] * ((v >> i) & 1) for i in range(N)) % 2 == 0 for r in roots)


def main():
    simple = [tuple(int(i == j) for j in range(N)) for i in range(N)]
    roots = closure(simple, [lambda v, i=i: root_reflection(v, i) for i in range(N)])
    assert len(roots) == 72
    assert all(sum(v[i] * A[i][j] * v[j] for i in range(N) for j in range(N)) == 2
               and tuple(-x for x in v) in roots and graph_root(v) in roots for v in roots)
    graph_roots = {r for r in roots if graph_root(r) == r}
    assert len(graph_roots) == 24
    torus = [v for v in range(1 << N) if graph_bits(v) == v]
    assert len(torus) == 16
    dist = Counter(fixed_roots(graph_roots, v) for v in torus)
    assert dist == {24: 4, 8: 12}
    f4 = {v for v in torus if fixed_roots(graph_roots, v) == 24}
    assert len(f4) == 4 and 0 in f4 and any(f4)
    nonzero_f4 = min(f4 - {0})
    assert fixed_roots(roots, nonzero_f4) in (32, 40)
    print(f"nonidentity F4-type fixed-torus witness: {nonzero_f4}, fixed roots {fixed_roots(roots, nonzero_f4)}")
    c4 = {v for v in torus if fixed_roots(graph_roots, v) == 8}
    assert len(c4) == 12

    words = ((0, 5), (2, 4), (1,), (3,))
    def word(v, indices):
        for i in indices:
            v = torus_reflection(v, i)
        return v
    orbit = closure([min(c4)], [lambda v, w=w: word(v, w) for w in words])
    assert orbit == c4
    pairs = Counter(fixed_roots(roots, u ^ v) for u in c4 for v in c4 if u < v)
    assert pairs == {32: 48, 40: 18}
    assert 2 in c4 and 8 in c4 and 22 in c4
    assert fixed_roots(roots, 2 ^ 8) == 32
    assert fixed_roots(roots, 2 ^ 22) == 40
    print("72 roots, 24 graph-fixed roots, 16 fixed torus points")
    print("12 C4-type candidates form one folded-Weyl orbit")
    print("48 products have 32 fixed roots; 18 have 40; witnesses 2 xor 8 and 2 xor 22")


if __name__ == "__main__":
    main()
