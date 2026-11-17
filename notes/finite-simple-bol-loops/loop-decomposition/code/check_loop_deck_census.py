#!/usr/bin/env python3
"""Exact diagnostics for deletion-deck associative-subloop census formulas.

Standalone checker.  No imports from the graph-loop implementation.
RREF enumeration checks linear claims directly; a generated-subloop search
checks the entire associative-subloop census in the smallest actual loops.
Finite checks support the separate general proofs and do not replace them.
"""
from __future__ import annotations

from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, product
from math import comb
import json


def gaussian(n, d, p):
    if d < 0 or d > n:
        return 0
    num = den = 1
    for j in range(d):
        num *= p ** (n-j) - 1
        den *= p ** (d-j) - 1
    return num // den


def full_support(c, d, p):
    return sum((-1)**j * comb(c, j) * gaussian(c-j, d, p)
               for j in range(c+1))


@lru_cache(None)
def subspaces(n, p):
    answer = []
    for d in range(n+1):
        for pivots in combinations(range(n), d):
            free = [(r, c) for r, a in enumerate(pivots)
                    for c in range(a+1, n) if c not in pivots]
            for values in product(range(p), repeat=len(free)):
                rows = [[int(c == a) for c in range(n)] for a in pivots]
                for (r, c), value in zip(free, values):
                    rows[r][c] = value
                answer.append(tuple(map(tuple, rows)))
    assert len(set(answer)) == len(answer)
    assert len(answer) == sum(gaussian(n, d, p) for d in range(n+1))
    return tuple(answer)


def graphs(n):
    possible = tuple(combinations(range(n), 2))
    for mask in range(1 << len(possible)):
        yield tuple(e for k, e in enumerate(possible) if mask >> k & 1)


def components(n, edges, support):
    remaining = set(support)
    neighbours = [set() for _ in range(n)]
    for i, j in edges:
        neighbours[i].add(j)
        neighbours[j].add(i)
    answer = []
    while remaining:
        todo = [next(iter(remaining))]
        found = set()
        while todo:
            v = todo.pop()
            if v in found:
                continue
            found.add(v)
            todo.extend(neighbours[v] & remaining - found)
        remaining -= found
        answer.append(found)
    return answer


def closed_neighbourhood(n, edges, support):
    answer = set(support)
    for i, j in edges:
        if i in support:
            answer.add(j)
        if j in support:
            answer.add(i)
    return answer


def subsets(n):
    return ({i for i in range(n) if mask >> i & 1}
            for mask in range(1 << n))


def edge_map(x, y, edges, p):
    return tuple((x[i]*y[j] - x[j]*y[i]) % p for i, j in edges)


def add(x, y, p):
    return tuple((a+b) % p for a, b in zip(x, y))


def factor(x, y, edges, p):
    return tuple((x[0]+2*y[0])*v % p
                 for v in edge_map(x[1:], y[1:], edges, p))


def associator(x, y, z, edges, p):
    # Compute directly from the factor set, rather than assume its closed form.
    a = factor(x, y, edges, p)
    b = factor(add(x, y, p), z, edges, p)
    c = factor(y, z, edges, p)
    d = factor(x, add(y, z, p), edges, p)
    return tuple((aa+bb-cc-dd) % p for aa, bb, cc, dd in zip(a, b, c, d))


def component_polynomial(n, edges):
    return Counter((len(s), len(components(n, edges, s))) for s in subsets(n))


def isotropic_formula(n, edges, p):
    qpoly = component_polynomial(n, edges)
    return Counter({d: sum(mult*(p-1)**(s-c)*full_support(c, d, p)
                           for (s, c), mult in qpoly.items())
                    for d in range(n+1)})


def associative_formula(n, edges, p):
    qpoly = component_polynomial(n, edges)
    return Counter({r: gaussian(n, r, p)
                    + sum(mult*(p-1)**(s-c)*full_support(c+1, r, p)
                          for (s, c), mult in qpoly.items())
                    for r in range(n+2)})


def census_formula(n, edges, p):
    a = associative_formula(n, edges, p)
    e = len(edges)
    return Counter({k: sum(a[r]*gaussian(e, k-r, p)*p**(r*(e-(k-r)))
                           for r in range(n+2) if 0 <= k-r <= e)
                    for k in range(n+e+2)})


def check_linear_counts():
    stats = Counter()
    for p in (2, 3):
        for n in range(5):
            for edges in graphs(n):
                direct = Counter()
                for h in subspaces(n, p):
                    stats['isotropic_subspaces_examined'] += 1
                    if not any(any(edge_map(x, y, edges, p))
                               for x, y in combinations(h, 2)):
                        direct[len(h)] += 1
                assert direct == isotropic_formula(n, edges, p), (p, n, edges)
                stats['isotropic_graph_field_cases'] += 1
    for p, max_n in ((2, 4), (5, 3)):
        for n in range(max_n+1):
            for edges in graphs(n):
                direct = Counter()
                for u in subspaces(n+1, p):
                    stats['associative_projected_spaces_examined'] += 1
                    if not any(any(associator(x, y, z, edges, p))
                               for x, y, z in product(u, repeat=3)):
                        direct[len(u)] += 1
                expected = associative_formula(n, edges, p)
                assert direct == expected, (p, n, edges, direct, expected)
                for d in range(n+1):
                    neighbourhood = 0
                    for s in subsets(n):
                        c = len(components(n, edges, s))
                        if c < d:
                            continue
                        untouched = n-len(closed_neighbourhood(n, edges, s))
                        neighbourhood += ((p-1)**(len(s)-c)*full_support(c, d, p)
                                          * p**(untouched+c-d))
                    assert neighbourhood == expected[d+1]-gaussian(n, d+1, p)
                stats['associative_graph_field_cases'] += 1
    return stats


def dominating_polynomial(n, edges):
    return Counter((len(s)-len(components(n, edges, s)),
                    len(components(n, edges, s)))
                   for s in subsets(n)
                   if len(closed_neighbourhood(n, edges, s)) == n)


def transform_dominating_polynomial(n, edges):
    answer = Counter()
    for support in subsets(n):
        term = Counter({(0, 0): 1})
        for comp in components(n, edges, support):
            next_term = Counter()
            for (k, d), mult in term.items():
                next_term[k+len(comp)-1, d+1] += mult
                next_term[k, d] += (-1)**len(comp)*mult
            term = next_term
        answer.update(term)
    assert all(value >= 0 for value in answer.values())
    return +answer


def delete_vertex(n, edges, v):
    index = {u: k for k, u in enumerate(x for x in range(n) if x != v)}
    return tuple((index[a], index[b]) for a, b in edges if v not in (a, b))


def check_deck_polynomials():
    stats = Counter()
    for n in range(6):
        for edges in graphs(n):
            a = dominating_polynomial(n, edges)
            transformed = transform_dominating_polynomial(n, edges)
            assert a == transformed, (n, edges, a, transformed)
            near_rhs = Counter()
            for s in subsets(n):
                c = len(components(n, edges, s))
                untouched = n-len(closed_neighbourhood(n, edges, s))
                if untouched == 0:
                    near_rhs[len(s)-c, c] += n-len(s)
                elif untouched == 1:
                    near_rhs[len(s)-c, c] += 1
            card_sum = Counter()
            for v in range(n):
                card_sum.update(dominating_polynomial(n-1, delete_vertex(n, edges, v)))
            assert card_sum == near_rhs
            if n >= 3:
                cards = [delete_vertex(n, edges, v) for v in range(n)]
                recovered_e = sum(map(len, cards)) // (n-2)
                assert recovered_e == len(edges)
                isolated = any(len(card) == recovered_e for card in cards)
                card_c = [len(components(n-1, card, set(range(n-1)))) for card in cards]
                recovered_c = min(card_c)+int(isolated)
                assert recovered_c == len(components(n, edges, set(range(n))))
                q_from_cards = Counter()
                for card in cards:
                    q_from_cards.update(component_polynomial(n-1, card))
                q_recovered = Counter()
                for (s, c), mult in q_from_cards.items():
                    assert mult % (n-s) == 0
                    q_recovered[s, c] = mult // (n-s)
                q_recovered[n, recovered_c] = 1
                assert q_recovered == component_polynomial(n, edges)
                stats['reconstructed_Q_cases'] += 1
            stats['domination_transform_cases'] += 1
    return stats


def loop_table(n, edges, p):
    e = len(edges)
    elements = tuple(product(range(p), repeat=n+1+e))
    lookup = {x: k for k, x in enumerate(elements)}
    table = []
    for x in elements:
        row = []
        for y in elements:
            central = factor(x[:n+1], y[:n+1], edges, p)
            xy = add(x[:n+1], y[:n+1], p)+tuple(
                (x[n+1+j]+y[n+1+j]+central[j]) % p for j in range(e))
            row.append(lookup[xy])
        table.append(tuple(row))
    return tuple(table)


def all_subloops(table):
    order = len(table)

    def closure(seed):
        reached = set(seed)
        frontier = list(seed)
        while frontier:
            x = frontier.pop()
            for y in tuple(reached):
                for z in (table[x][y], table[y][x]):
                    if z not in reached:
                        reached.add(z)
                        frontier.append(z)
        return frozenset(reached)

    discovered = {frozenset({0})}
    queue = deque(discovered)
    while queue:
        h = queue.popleft()
        for x in range(order):
            if x in h:
                continue
            k = closure(h | {x})
            if k not in discovered:
                discovered.add(k)
                queue.append(k)
    return discovered


def check_actual_subloops():
    records = []
    cases = [(0, ()), (1, ()), (2, ()), (2, ((0, 1),)),
             (3, ((0, 1),))]
    for n, edges in cases:
        p = 2
        table = loop_table(n, edges, p)
        spaces = all_subloops(table)
        census = Counter()
        for h in spaces:
            if all(table[table[x][y]][z] == table[x][table[y][z]]
                   for x, y, z in product(h, repeat=3)):
                k = len(h).bit_length()-1
                assert 2**k == len(h)
                census[k] += 1
        assert census == census_formula(n, edges, p), (n, edges, census)
        records.append({'n': n, 'edges': edges, 'loop_order': len(table),
                        'all_subloops': len(spaces), 'associative_census': dict(census)})
    return records


def check_census_collision():
    """Equal full associative census, unequal maximal-associative census."""
    n = 5
    first = ((0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 3))
    second = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 3))
    expected_q = Counter({(0, 0): 1, (1, 1): 5, (2, 1): 6, (2, 2): 4,
                          (3, 1): 6, (3, 2): 4, (4, 1): 4, (4, 2): 1,
                          (5, 1): 1})
    for edges in (first, second):
        assert component_polynomial(n, edges) == expected_q
    degrees = [sorted(sum(v in edge for edge in edges) for v in range(n))
               for edges in (first, second)]
    assert degrees == [[1, 2, 3, 3, 3], [2, 2, 2, 2, 4]]
    for p in (2, 5, 7):
        assert census_formula(n, first, p) == census_formula(n, second, p)
        a_first = dominating_polynomial(n, first)
        a_second = dominating_polynomial(n, second)
        counts = [Counter({d: sum(mult*(p-1)**k for (k, dd), mult in a.items()
                                  if dd == d)
                           for d in range(n+1)}) for a in (a_first, a_second)]
        assert counts[0] == Counter({1: p**4-p**2, 2: (p+1)**2})
        assert counts[1] == Counter({1: p**4, 2: (p+1)**2})
    # A separate direct enumeration checks actual quotient spaces for p=2.
    direct_counts = []
    for edges in (first, second):
        direct = Counter()
        for u in subspaces(n+1, 2):
            if not any(any(associator(x, y, z, edges, 2))
                       for x, y, z in product(u, repeat=3)):
                direct[len(u)] += 1
        assert direct == associative_formula(n, edges, 2)
        direct_counts.append(direct)
    assert direct_counts[0] == direct_counts[1]
    return {'n': n, 'first_edges': first, 'second_edges': second,
            'degree_sequences': degrees,
            'subspaces_directly_checked': 2*len(subspaces(n+1, 2)),
            'projected_associative_census_p2': dict(direct_counts[0])}


if __name__ == '__main__':
    result = {'linear': dict(check_linear_counts()),
              'polynomials': dict(check_deck_polynomials()),
              'actual_loops': check_actual_subloops(),
              'census_collision': check_census_collision()}
    print(json.dumps(result, indent=2, sort_keys=True))
