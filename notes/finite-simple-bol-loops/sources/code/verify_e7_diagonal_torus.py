#!/usr/bin/env python3
"""Check E7 root-datum 2-torsion orbits, not finite-group realization.

Bourbaki E7 diagram: 1--3--4--5--6--7 with 2 attached to 4.
All vectors use the seven simple roots in that order. Only stdlib is used.
"""
from collections import deque

N = 7
EDGES = ((0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 3))
CARTAN = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
for i, j in EDGES:
    CARTAN[i][j] = CARTAN[j][i] = -1


def reflect_root(root, i):
    v = list(root)
    v[i] -= sum(CARTAN[i][j] * root[j] for j in range(N))
    return tuple(v)


def root_norm(root):
    return sum(root[i] * CARTAN[i][j] * root[j]
               for i in range(N) for j in range(N))


def reflect_torus(bits, i):
    if not (bits & (1 << i)):
        return bits
    return bits ^ sum((CARTAN[j][i] % 2) << j for j in range(N))


def closure(seed, reflections):
    seen = {seed}
    todo = deque([seed])
    while todo:
        v = todo.popleft()
        for i in range(N):
            w = reflections(v, i)
            if w not in seen:
                seen.add(w)
                todo.append(w)
    return seen


def main():
    simple = [tuple(int(i == j) for j in range(N)) for i in range(N)]
    roots = set().union(*(closure(v, reflect_root) for v in simple))
    assert len(roots) == 126
    assert all(root_norm(v) == 2 and tuple(-x for x in v) in roots for v in roots)
    assert all(reflect_root(v, i) in roots for v in roots for i in range(N))

    left = set(range(1 << N))
    orbits = []
    while left:
        orbit = closure(min(left), reflect_torus)
        assert orbit <= left
        left -= orbit
        orbits.append(orbit)
    assert len(orbits) == 4 and set().union(*orbits) == set(range(128))
    by_size = {len(orbit): orbit for orbit in orbits}
    assert sorted(by_size) == [1, 28, 36, 63]

    def fixed_roots(bits):
        return sum(sum(root[i] * ((bits >> i) & 1) for i in range(N)) % 2 == 0
                   for root in roots)

    # The sc cocharacter lattice is the coroot lattice. Evaluate its 2-torsion
    # on the adjoint root lattice by the Cartan matrix, modulo two.
    def cartan_image(bits):
        return sum((sum(CARTAN[i][j] * ((bits >> j) & 1)
                        for j in range(N)) % 2) << i for i in range(N))

    images = [cartan_image(v) for v in range(128)]
    assert sum(value == 0 for value in images) == 2
    assert set(images) == by_size[1] | by_size[63]
    assert all(images.count(v) == 2 for v in set(images))
    print("Cartan mod 2: kernel 2, image identity plus the 63-orbit")

    expected = {1: 126, 63: 62, 36: 56, 28: 72}
    for size, count in expected.items():
        assert {fixed_roots(v) for v in by_size[size]} == {count}
    for size in (36, 28):
        for v in by_size[size]:
            assert all((v ^ w) in by_size[63] for w in by_size[size] if w != v)
        v, w = sorted(by_size[size])[:2]
        print(f"orbit {size}: witness {v} xor {w} = {v ^ w}; all distinct pairs in 63-orbit")
    print("126 norm-two roots; orbit sizes 1, 63, 36, 28; fixed-root counts 126, 62, 56, 72")


if __name__ == "__main__":
    main()
