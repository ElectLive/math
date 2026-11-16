#!/usr/bin/env python3
"""Finite checks for bol-section-mixing.md, using Python's standard library.

Run from any directory with Python 3.11 or later. No arguments or files are
required. Output is one deterministic JSON object. All matrix and probability
checks are exact; no floating-point spectral calculation is used.

The cases here use prime fields F_3, F_5, and F_7. The manuscript proves the
general prime-power theorem; this bounded check does not implement extension
fields. Matrices are built from the ORIGINAL loop multiplication and actual
left translations, independently of the Fourier block formulas.
"""

from __future__ import annotations

import itertools
import json
import random
from fractions import Fraction


SEED = 20261116
CASES = ((3, 2, 1), (3, 2, 2), (5, 2, 1), (5, 4, 1), (7, 3, 1), (7, 6, 1))
SAMPLED_TRIPLES = 512


class Loop:
    def __init__(self, q: int, m: int, d: int) -> None:
        assert q in (3, 5, 7) and d >= 1 and m >= 2 and (q - 1) % m == 0
        self.q, self.m, self.d = q, m, d
        self.eta = next(
            z for z in range(2, q)
            if pow(z, m, q) == 1
            and all(pow(z, j, q) != 1 for j in range(1, m))
        )
        self.powers = tuple(pow(self.eta, j, q) for j in range(m))
        self.xs = tuple(itertools.product(range(q), repeat=d))
        self.zero = (0,) * (2 * d)
        self.identity = (self.zero, 0, 0)
        self.h = tuple(
            (u + (0,) * d, t, 0) for u in self.xs for t in range(m)
        )

    def gamma(self, u: tuple[int, ...], v: tuple[int, ...]) -> int:
        d = self.d
        return sum(u[i] * v[d + i] - u[d + i] * v[i] for i in range(d)) % self.q

    def mul(self, left: tuple, right: tuple) -> tuple:
        u, t, s = left
        v, a, h = right
        scale = self.powers[t]
        return (
            tuple((x + scale * y) % self.q for x, y in zip(u, v)),
            (t + a) % self.m,
            (s + h - self.gamma(u, v)) % self.q,
        )

    def inverse(self, z: tuple) -> tuple:
        u, t, s = z
        return (
            tuple(-self.powers[-t % self.m] * x % self.q for x in u),
            -t % self.m,
            -s % self.q,
        )

    def element(self, rng: random.Random) -> tuple:
        return (
            tuple(rng.randrange(self.q) for _ in range(2 * self.d)),
            rng.randrange(self.m),
            rng.randrange(self.q),
        )

    def all_elements(self) -> list[tuple]:
        return [
            (u, a, s)
            for u in itertools.product(range(self.q), repeat=2 * self.d)
            for a in range(self.m)
            for s in range(self.q)
        ]

    def correction(self, h: tuple, k: tuple) -> tuple[int, ...]:
        u, t, _ = h
        v, a, _ = k
        return tuple(
            ((1 - self.powers[a]) * u[i] + (self.powers[t] - 1) * v[i]) % self.q
            for i in range(self.d)
        )

    def shear(self, c: tuple[int, ...], z: tuple) -> tuple:
        u, a, s = z
        return (u, a, (s + sum(c[i] * u[self.d + i] for i in range(self.d))) % self.q)


def bol_identity(loop: Loop, a: tuple, b: tuple, c: tuple) -> bool:
    mul = loop.mul
    return mul(a, mul(b, mul(a, c))) == mul(mul(a, mul(b, a)), c)


def check_correction(loop: Loop, h: tuple, k: tuple, l: tuple, z: tuple) -> None:
    mul = loop.mul
    c_hk = loop.correction(h, k)
    assert mul(h, mul(k, z)) == mul(mul(h, k), loop.shear(c_hk, z))
    scale = loop.powers[l[1]]
    scaled = tuple(scale * x % loop.q for x in c_hk)
    assert loop.shear(c_hk, mul(l, z)) == mul(l, loop.shear(scaled, z))
    lhs = tuple(
        (x + y) % loop.q for x, y in zip(loop.correction(mul(h, k), l), scaled)
    )
    rhs = tuple(
        (x + y) % loop.q
        for x, y in zip(loop.correction(h, mul(k, l)), loop.correction(k, l))
    )
    assert lhs == rhs


def verify_law(loop: Loop, rng: random.Random, exhaustive: bool) -> dict:
    q, m, d = loop.q, loop.m, loop.d
    e_x = (1,) + (0,) * (2 * d - 1)
    e_y = (0,) * d + (1,) + (0,) * (d - 1)
    a, b, c = (loop.zero, 1, 0), (e_x, 0, 0), (e_y, 0, 0)
    lhs = loop.mul(loop.mul(a, b), loop.mul(c, a))
    rhs = loop.mul(loop.mul(a, loop.mul(b, c)), a)
    assert lhs[:2] == rhs[:2] and lhs[2] == -loop.eta % q and rhs[2] == -1 % q
    assert lhs != rhs

    if exhaustive:
        elements = loop.all_elements()
        index = {z: i for i, z in enumerate(elements)}
        n = len(elements)
        table = [[index[loop.mul(x, y)] for y in elements] for x in elements]
        expected = set(range(n))
        assert all(set(row) == expected for row in table)
        assert all({table[i][j] for i in range(n)} == expected for j in range(n))
        e = index[loop.identity]
        assert table[e] == list(range(n)) and all(table[i][e] == i for i in range(n))
        for i, row_i in enumerate(table):
            inv = index[loop.inverse(elements[i])]
            for j, row_j in enumerate(table):
                assert table[inv][row_i[j]] == j
                left_outer = table[row_i[row_j[i]]]
                for k in range(n):
                    assert row_i[row_j[row_i[k]]] == left_outer[k]
        for h, k in itertools.product(loop.h, repeat=2):
            for z in elements:
                assert loop.mul(h, loop.mul(k, z)) == loop.mul(
                    loop.mul(h, k), loop.shear(loop.correction(h, k), z)
                )
        for h, k, l in itertools.product(loop.h, repeat=3):
            check_correction(loop, h, k, l, c)
        return {
            "scope": "exhaustive Latin, identity, inverse, left Bol, and correction",
            "loop_order": n,
            "bol_triples": n ** 3,
            "correction_pairs_times_states": len(loop.h) ** 2 * n,
            "coherence_triples": len(loop.h) ** 3,
            "proper_witness_central_coordinates": [lhs[2], rhs[2]],
        }

    for _ in range(SAMPLED_TRIPLES):
        x, y, z = (loop.element(rng) for _ in range(3))
        assert bol_identity(loop, x, y, z)
        assert loop.mul(loop.identity, x) == x == loop.mul(x, loop.identity)
        assert loop.mul(loop.inverse(x), loop.mul(x, y)) == y
        assert loop.mul(x, loop.mul(loop.inverse(x), y)) == y
        h, k, l = (loop.h[rng.randrange(len(loop.h))] for _ in range(3))
        check_correction(loop, h, k, l, z)
    return {
        "scope": "deterministic sampled Bol, identity, inverse, and correction",
        "loop_order": m * q ** (2 * d + 1),
        "sampled_triples": SAMPLED_TRIPLES,
        "proper_witness_central_coordinates": [lhs[2], rhs[2]],
    }


def expected_tv(q: int, m: int, step: int) -> Fraction:
    value = Fraction(q - 1, q * m ** (step - 1))
    return value if step % 2 else value * Fraction(q - m + 1, q)


def tv_from_counts(counts: list[int], denominator: int) -> Fraction:
    n = len(counts)
    assert sum(counts) == denominator
    return Fraction(sum(abs(n * c - denominator) for c in counts), 2 * n * denominator)


def verify_component(loop: Loop) -> dict:
    q, m, d = loop.q, loop.m, loop.d
    # r=e_1, in original (x,y,a,s) coordinates, not in transformed coordinates.
    r = (1,) + (0,) * (d - 1)
    states = [
        (x + tuple(loop.powers[a] * y % q for y in r), a, s)
        for a in range(m) for x in loop.xs for s in range(q)
    ]
    index = {z: i for i, z in enumerate(states)}
    n, degree = len(states), len(loop.h)
    assert n == m * q ** (d + 1) and degree == m * q ** d
    adjacency: list[list[int]] = []
    for z in states:
        targets = [index[loop.mul(h, z)] for h in loop.h]
        assert len(set(targets)) == degree
        adjacency.append(sorted(targets))
    rows = [set(row) for row in adjacency]
    assert all(i in rows[i] for i in range(n))
    assert all(i in rows[j] for i, row in enumerate(adjacency) for j in row)

    # K^2 and K^3 are formed by counting actual paths through the adjacency list.
    square = []
    for row in adjacency:
        counts = [0] * n
        for intermediate in row:
            for target in adjacency[intermediate]:
                counts[target] += 1
        square.append(counts)
    c_edge = q ** (2 * d)
    c_all = (m * m - 1) * q ** (2 * d - 1)
    for i, row in enumerate(square):
        cube = [0] * n
        for intermediate, count in enumerate(row):
            if count:
                for target in adjacency[intermediate]:
                    cube[target] += count
        assert all(value == c_all + c_edge * (j in rows[i]) for j, value in enumerate(cube))
        assert tv_from_counts([int(j in rows[i]) for j in range(n)], degree) == expected_tv(q, m, 1)
        assert tv_from_counts(row, degree * degree) == expected_tv(q, m, 2)

    # The integer cubic identity, symmetry, row sums, and traces determine the
    # allowed eigenvalues and their multiplicities without diagonalization.
    plus = (q - 1) * m * (m + 1) // 2
    minus = (q - 1) * m * (m - 1) // 2
    zero = n - 1 - plus - minus
    assert zero >= 0
    trace_p = Fraction(n, degree)
    trace_p2 = Fraction(sum(square[i][i] for i in range(n)), degree * degree)
    assert trace_p == 1 + Fraction(plus - minus, m)
    assert trace_p2 == 1 + Fraction(plus + minus, m * m)

    counts = [0] * n
    counts[0] = 1
    denominator = 1
    distances = []
    for step in range(1, 7):
        next_counts = [0] * n
        for source, count in enumerate(counts):
            if count:
                for target in adjacency[source]:
                    next_counts[target] += count
        counts = next_counts
        denominator *= degree
        distance = tv_from_counts(counts, denominator)
        assert distance == expected_tv(q, m, step)
        distances.append(str(distance))
    if m == q - 1:
        assert Fraction(distances[1]) == Fraction(2, q * q)

    # The exceptional r=0, fixed-s component is uniform after one step.
    exceptional = [(x + (0,) * d, a, 0) for a in range(m) for x in loop.xs]
    exceptional_set = set(exceptional)
    assert len(exceptional_set) == degree
    for z in exceptional:
        assert {loop.mul(h, z) for h in loop.h} == exceptional_set

    return {
        "component_order": n,
        "degree": degree,
        "integer_cubic_coefficients": {"K": c_edge, "all_ones": c_all},
        "cubic_identity_entries_checked": n * n,
        "all_start_rows_tv_steps_1_2": n,
        "point_start_tv_steps_1_to_6": distances,
        "spectral_multiplicities_from_identity_and_traces": {
            "1": 1, "+1/m": plus, "-1/m": minus, "0": zero,
        },
        "exceptional_component_one_step_uniform": True,
    }


def main() -> None:
    rng = random.Random(SEED)
    results = []
    for q, m, d in CASES:
        loop = Loop(q, m, d)
        results.append({
            "parameters": {"Q": q, "m": m, "d": d, "eta": loop.eta},
            "law": verify_law(loop, rng, exhaustive=(q, m, d) == (3, 2, 1)),
            "walk": verify_component(loop),
        })
    print(json.dumps({
        "status": "pass",
        "arithmetic": "exact integers and fractions; prime fields only",
        "seed": SEED,
        "cases": results,
        "limits": "Finite checks support, but do not prove, the manuscript's quantified theorems.",
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()

