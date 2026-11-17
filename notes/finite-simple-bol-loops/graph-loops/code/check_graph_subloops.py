#!/usr/bin/env python3
"""Independent finite checks for graph-derived isotropic/subloop theorems.

The direct side enumerates vector subspaces by reduced row echelon bases and
checks the alternating edge map.  The comparison side uses dominating vertex
sets and connected components.  Neither imports another graph-loop checker.

Default scope: all labelled simple graphs on at most four vertices over F2 and
F3; binary square-zero hyperplanes on the same graphs; proper-Bol universal
right alternativity on all graphs on at most three vertices over F2,F3,F5.
These are exact finite checks, not substitutes for the general proofs.
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product
import json
from typing import Iterable

Vector = tuple[int, ...]
Basis = tuple[Vector, ...]
Graph = tuple[tuple[int, int], ...]


def rref(rows: Iterable[Vector], p: int, n: int) -> Basis:
    a = [list(row) for row in rows if any(c % p for c in row)]
    a = [[c % p for c in row] for row in a]
    pivot_row = 0
    for col in range(n):
        pivot = next((r for r in range(pivot_row, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inv = pow(a[pivot_row][col], -1, p)
        a[pivot_row] = [(inv * c) % p for c in a[pivot_row]]
        for r in range(len(a)):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [(c - factor * d) % p
                        for c, d in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return tuple(tuple(row) for row in a[:pivot_row])


def all_subspaces(n: int, p: int) -> tuple[Basis, ...]:
    result: list[Basis] = []
    for dim in range(n + 1):
        for pivots in combinations(range(n), dim):
            free = [(r, c) for r, pivot in enumerate(pivots)
                    for c in range(pivot + 1, n) if c not in pivots]
            for values in product(range(p), repeat=len(free)):
                rows = [[0] * n for _ in pivots]
                for r, pivot in enumerate(pivots):
                    rows[r][pivot] = 1
                for (r, c), value in zip(free, values):
                    rows[r][c] = value
                result.append(tuple(tuple(row) for row in rows))
    assert len(result) == len(set(result))
    # Independent Gaussian-binomial count checks the RREF enumeration size.
    expected = 0
    for d in range(n + 1):
        numerator = denominator = 1
        for j in range(d):
            numerator *= p ** (n - j) - 1
            denominator *= p ** (d - j) - 1
        expected += numerator // denominator
    assert len(result) == expected
    return tuple(result)


def all_graphs(n: int) -> Iterable[Graph]:
    possible = tuple(combinations(range(n), 2))
    for mask in range(1 << len(possible)):
        yield tuple(edge for k, edge in enumerate(possible) if mask >> k & 1)


def edge_map(x: Vector, y: Vector, edges: Graph, p: int) -> Vector:
    return tuple((x[i] * y[j] - x[j] * y[i]) % p for i, j in edges)


def direct_maximal_isotropic(n: int, p: int, edges: Graph,
                             subspaces: tuple[Basis, ...]) -> set[Basis]:
    result = set()
    for basis in subspaces:
        if any(any(edge_map(x, y, edges, p))
               for x, y in combinations(basis, 2)):
            continue
        # H^perp is the simultaneous kernel of v -> B(h,v), h in the basis.
        equations = []
        for h in basis:
            for i, j in edges:
                row = [0] * n
                row[i] = -h[j] % p
                row[j] = h[i] % p
                equations.append(tuple(row))
        perp_dimension = n - len(rref(equations, p, n))
        # A larger isotropic space exists iff H^perp contains a vector outside H.
        if perp_dimension == len(basis):
            result.add(basis)
    return result


def support_components(n: int, edges: Graph, support: set[int]) -> list[set[int]]:
    adjacency = {v: set() for v in support}
    for i, j in edges:
        if i in support and j in support:
            adjacency[i].add(j)
            adjacency[j].add(i)
    remaining = set(support)
    components = []
    while remaining:
        todo = [min(remaining)]
        found = set()
        while todo:
            v = todo.pop()
            if v in found:
                continue
            found.add(v)
            todo.extend(adjacency[v] - found)
        remaining -= found
        components.append(found)
    return components


def dominates(n: int, edges: Graph, support: set[int]) -> bool:
    closed = set(support)
    for i, j in edges:
        if i in support:
            closed.add(j)
        if j in support:
            closed.add(i)
    return len(closed) == n


def component_prediction(n: int, p: int, edges: Graph) -> tuple[set[Basis], Counter]:
    predicted: set[Basis] = set()
    count_formula = Counter()
    for mask in range(1 << n):
        support = {i for i in range(n) if mask >> i & 1}
        if not dominates(n, edges, support):
            continue
        components = support_components(n, edges, support)
        count_formula[len(components)] += (p - 1) ** (len(support) - len(components))
        free_vertices = [(row, v) for row, comp in enumerate(components)
                         for v in sorted(comp) if v != min(comp)]
        for values in product(range(1, p), repeat=len(free_vertices)):
            rows = [[0] * n for _ in components]
            for row, comp in enumerate(components):
                rows[row][min(comp)] = 1
            for (row, vertex), value in zip(free_vertices, values):
                rows[row][vertex] = value
            predicted.add(rref((tuple(row) for row in rows), p, n))
    assert Counter(map(len, predicted)) == count_formula
    return predicted, count_formula


def binary_square(t: int, x: Vector, edges: Graph) -> Vector:
    return tuple(t * x[i] * x[j] for i, j in edges)


def check_square_zero_hyperplanes(n: int, edges: Graph) -> int:
    vectors = tuple(product(range(2), repeat=n + 1))
    actual = set()
    for functional in vectors[1:]:
        if all(not any(binary_square(a[0], a[1:], edges))
               for a in vectors
               if sum(c * x for c, x in zip(functional, a)) % 2 == 0):
            actual.add(functional)
    if not edges:
        predicted = set(vectors[1:])
    else:
        predicted = {(1,) + (0,) * n}
        for v in range(n):
            if all(v in edge for edge in edges):
                predicted.add((0,) + tuple(int(i == v) for i in range(n)))
        if len(edges) == 1:
            i, j = edges[0]
            predicted.add((1,) + tuple(int(k in (i, j)) for k in range(n)))
    assert actual == predicted, (n, edges, actual, predicted)
    return len(actual)


def add(x: Vector, y: Vector, p: int) -> Vector:
    return tuple((a + b) % p for a, b in zip(x, y))


def bol_factor(x: Vector, y: Vector, edges: Graph, p: int) -> Vector:
    # Independent exact factor-set evaluation, not the simplified associator.
    coefficient = (x[0] + 2 * y[0]) % p
    return tuple(coefficient * c % p for c in edge_map(x[1:], y[1:], edges, p))


def direct_right_alt_discrepancy(x: Vector, y: Vector, edges: Graph, p: int) -> Vector:
    # Central coordinates of (xy)y minus x(yy).
    terms = (bol_factor(x, y, edges, p),
             bol_factor(add(x, y, p), y, edges, p),
             bol_factor(y, y, edges, p),
             bol_factor(x, add(y, y, p), edges, p))
    return tuple((a + b - c - d) % p for a, b, c, d in zip(*terms))


def check_right_alt_set(n: int, p: int, edges: Graph) -> tuple[int, int]:
    vectors = tuple(product(range(p), repeat=n + 1))
    actual = set()
    evaluated = 0
    for y in vectors:
        valid = True
        for x in vectors:
            discrepancy = direct_right_alt_discrepancy(x, y, edges, p)
            evaluated += 1
            expected_discrepancy = tuple((-3 * y[0] * c) % p
                                         for c in edge_map(x[1:], y[1:], edges, p))
            assert discrepancy == expected_discrepancy
            if any(discrepancy):
                valid = False
                break
        if valid:
            actual.add(y)
    incident = {v for edge in edges for v in edge}
    predicted = {y for y in vectors
                 if p == 3 or y[0] == 0 or all(y[v + 1] == 0 for v in incident)}
    assert actual == predicted, (n, p, edges, actual, predicted)
    return len(actual), evaluated



def check_six_vertex_loss() -> dict:
    """Same dominating-component polynomial, different triangle intersections."""
    n = 6
    first = ((0, 1), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (2, 3))
    second = ((0, 1), (0, 2), (0, 4), (0, 5), (1, 4), (1, 5), (2, 3))
    expected = Counter({(0, 2): 3, (0, 3): 2, (1, 1): 1, (1, 2): 8,
                        (1, 3): 1, (2, 1): 4, (2, 2): 7, (3, 1): 6,
                        (3, 2): 2, (4, 1): 4, (5, 1): 1})
    polynomials = []
    triangle_intersections = []
    degree_sequences = []
    subspaces = all_subspaces(n, 2)
    maximal_counts = []
    for edges in (first, second):
        coefficient = Counter()
        for mask in range(1 << n):
            support = {i for i in range(n) if mask >> i & 1}
            if dominates(n, edges, support):
                d = len(support_components(n, edges, support))
                coefficient[len(support) - d, d] += 1
        assert coefficient == expected
        polynomials.append(coefficient)
        triangles = [set(vertices) for vertices in combinations(range(n), 3)
                     if all(tuple(sorted(pair)) in edges
                            for pair in combinations(vertices, 2))]
        triangle_intersections.append(sorted(len(a & b)
                                             for a, b in combinations(triangles, 2)))
        degree_sequences.append(sorted(Counter(v for edge in edges for v in edge).values()))
        actual = direct_maximal_isotropic(n, 2, edges, subspaces)
        predicted, _ = component_prediction(n, 2, edges)
        assert actual == predicted
        counts = Counter(map(len, actual))
        assert counts == Counter({1: 16, 2: 20, 3: 3})
        maximal_counts.append(dict(sorted(counts.items())))
        # Check the stated factored polynomial at several integer arguments.
        for q in (2, 3, 5, 7):
            evaluated = Counter()
            for (k, d), c in coefficient.items():
                evaluated[d] += c * (q - 1) ** k
            assert evaluated == Counter({1: q ** 4 * (q - 1),
                                         2: q ** 2 * (2 * q + 1), 3: q + 1})
    assert polynomials[0] == polynomials[1]
    assert degree_sequences[0] == degree_sequences[1]
    assert triangle_intersections == [[1], [2]]
    return {'vertices': n, 'edges_each': len(first),
            'common_degree_sequence': degree_sequences[0],
            'triangle_pair_intersections': triangle_intersections,
            'binary_maximal_isotropic_dimensions': maximal_counts,
            'rref_subspaces_checked_each': len(subspaces)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-n', type=int, default=4)
    parser.add_argument('--right-alt-max-n', type=int, default=3)
    args = parser.parse_args()
    if not 0 <= args.max_n <= 5 or not 0 <= args.right_alt_max_n <= 3:
        parser.error('max-n must be 0..5 and right-alt-max-n must be 0..3')
    summary = {
        'maximal_isotropic_graph_field_cases': 0,
        'enumerated_subspace_cases': 0,
        'verified_maximal_isotropic_spaces': 0,
        'square_zero_hyperplane_graph_cases': 0,
        'right_alternative_graph_field_cases': 0,
        'right_alternative_discrepancy_evaluations': 0,
    }
    for n in range(args.max_n + 1):
        for p in (2, 3):
            subspaces = all_subspaces(n, p)
            for edges in all_graphs(n):
                actual = direct_maximal_isotropic(n, p, edges, subspaces)
                predicted, counts = component_prediction(n, p, edges)
                assert actual == predicted, (n, p, edges, actual, predicted)
                assert Counter(map(len, actual)) == counts
                summary['maximal_isotropic_graph_field_cases'] += 1
                summary['enumerated_subspace_cases'] += len(subspaces)
                summary['verified_maximal_isotropic_spaces'] += len(actual)
        for edges in all_graphs(n):
            check_square_zero_hyperplanes(n, edges)
            summary['square_zero_hyperplane_graph_cases'] += 1
    for n in range(args.right_alt_max_n + 1):
        for p in (2, 3, 5):
            for edges in all_graphs(n):
                _, evaluations = check_right_alt_set(n, p, edges)
                summary['right_alternative_graph_field_cases'] += 1
                summary['right_alternative_discrepancy_evaluations'] += evaluations
    summary['six_vertex_invariant_loss'] = check_six_vertex_loss()
    summary['status'] = 'PASS'
    summary['scope'] = {'isotropic_fields': [2, 3], 'isotropic_max_n': args.max_n,
                        'right_alternative_fields': [2, 3, 5],
                        'right_alternative_max_n': args.right_alt_max_n}
    print(json.dumps(summary, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
