#!/usr/bin/env python3
"""Exact diagnostics for loop-defect-graphs.md; Python 3.11+, stdlib only.

The component oracle closes the associativity relations as a loop congruence;
the graph side independently constructs actual translation permutations. The
rank-spectrum checks evaluate factor-set coboundaries on a basis, rather than
testing the rank-condition derivation in the manuscript. No imported checker.
"""

from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
from itertools import product, permutations
import json


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def join(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        self.parent[max(x, y)] = min(x, y)
        return True

    def blocks(self):
        out = {}
        for x in range(len(self.parent)):
            out.setdefault(self.find(x), set()).add(x)
        return frozenset(frozenset(b) for b in out.values())


def divisions(table):
    n = len(table)
    assert table[0] == list(range(n))
    assert [row[0] for row in table] == list(range(n))
    left = [[0] * n for _ in range(n)]
    right = [[0] * n for _ in range(n)]
    for a in range(n):
        assert sorted(table[a]) == list(range(n))
        assert sorted(table[b][a] for b in range(n)) == list(range(n))
        for b in range(n):
            left[a][table[a][b]] = b
            right[b][table[a][b]] = a
    return left, right


def associativity_congruence(table, left, right):
    """Least congruence identifying all differently bracketed triple products."""
    n = len(table)
    uf = UnionFind(n)
    for x, y, z in product(range(n), repeat=3):
        uf.join(table[table[x][y]][z], table[x][table[y][z]])
    changed = True
    rounds = 0
    while changed:
        changed = False
        rounds += 1
        blocks = uf.blocks()
        for block in blocks:
            x = min(block)
            for y in block:
                for z in range(n):
                    for operation in (table, left, right):
                        changed |= uf.join(operation[x][z], operation[y][z])
                        changed |= uf.join(operation[z][x], operation[z][y])
    return uf.blocks(), rounds


def translated_defects(table, inverse_left):
    """Build P from actual L_z^-1 (L_xy^-1 L_x L_y) L_z, with multiplicities."""
    n = len(table)
    defects = Counter()
    for x, y in product(range(n), repeat=2):
        inverse_xy = inverse_left[table[x][y]]
        defects[tuple(inverse_xy[table[x][table[y][a]]] for a in range(n))] += 1
    local_counts = [[0] * n for _ in range(n)]
    for defect, multiplicity in defects.items():
        for a, b in enumerate(defect):
            local_counts[a][b] += multiplicity
    counts = [[0] * n for _ in range(n)]
    components = UnionFind(n)
    for defect, multiplicity in defects.items():
        for z in range(n):
            lz, iz = table[z], inverse_left[z]
            for a in range(n):
                b = iz[defect[lz[a]]]
                counts[a][b] += multiplicity
                components.join(a, b)
    den = n ** 3
    assert all(sum(row) == den for row in counts)
    assert all(sum(counts[a][b] for a in range(n)) == den for b in range(n))
    return counts, components.blocks(), len(defects), local_counts


def quotient_table(table, blocks):
    blocks = sorted(blocks, key=min)
    block_index = {x: i for i, block in enumerate(blocks) for x in block}
    quotient = [[None] * len(blocks) for _ in blocks]
    for i, first in enumerate(blocks):
        for j, second in enumerate(blocks):
            images = {block_index[table[x][y]] for x in first for y in second}
            assert len(images) == 1
            quotient[i][j] = images.pop()
    for i, j, k in product(range(len(blocks)), repeat=3):
        assert quotient[quotient[i][j]][k] == quotient[i][quotient[j][k]]
    return quotient


def check_components(name, table, bol=True):
    left, right = divisions(table)
    counts, actual, number_defects, local_counts = translated_defects(table, left)
    expected, rounds = associativity_congruence(table, left, right)
    assert actual == expected
    assert len({len(block) for block in actual}) == 1
    quotient_table(table, actual)
    symmetric = all(counts[a][b] == counts[b][a]
                    for a, b in product(range(len(table)), repeat=2))
    if bol:
        assert symmetric
    return {
        'name': name, 'order': len(table), 'distinct_left_defects': number_defects,
        'component_count': len(actual), 'component_size': len(next(iter(actual))),
        'congruence_closure_rounds': rounds, 'symmetric': symmetric,
        'local_isolate_count': sum(local_counts[a][a] == len(table)**2
                                   for a in range(len(table))),
        'local_matrix_sha256': sha256(json.dumps(local_counts, separators=(',', ':')).encode()).hexdigest(),
        'matrix_sha256': sha256(json.dumps(counts, separators=(',', ':')).encode()).hexdigest(),
    }, counts


def graph_table(p, n, edges, kind='bruck', twist=False):
    e = len(edges)
    elements = list(product(range(p), repeat=1 + n + e))
    index = {x: i for i, x in enumerate(elements)}

    def multiply(x, y):
        a, u, s = x[0], x[1:1+n], x[1+n:]
        b, v, t = y[0], y[1:1+n], y[1+n:]
        beta = [(u[i] * v[j] - u[j] * v[i]) % p for i, j in edges]
        if kind == 'bruck':
            correction = [((a + 2*b) * val) % p for val in beta]
        else:
            assert p == 2
            correction = [(a * val + b * u[i] * u[j]) % 2
                          for val, (i, j) in zip(beta, edges)]
        if twist:
            assert p == 2 and n == 2 and e == 1
            correction[0] ^= (a*b + u[0]*v[0] + u[1]*v[1]
                              + a*v[0] + a*v[1] + u[0]*v[1]) % 2
        return ((a+b) % p, *((u[i]+v[i]) % p for i in range(n)),
                *((s[i]+t[i]+correction[i]) % p for i in range(e)))

    return elements, [[index[multiply(x, y)] for y in elements] for x in elements]


def group_table(elements, multiplication):
    index = {x: i for i, x in enumerate(elements)}
    return [[index[multiplication(x, y)] for y in elements] for x in elements]


def moufang_and_associator_collision():
    elements, first = graph_table(2, 2, [(0, 1)], 'cubic')
    _, second = graph_table(2, 2, [(0, 1)], 'cubic', twist=True)
    for table in (first, second):
        divisions(table)
        for x, y, z in product(range(16), repeat=3):
            assert table[table[x][y]][table[z][x]] == table[x][table[table[y][z]][x]]
    for x, y, z in product(range(16), repeat=3):
        a1, b1 = first[first[x][y]][z], first[x][first[y][z]]
        a2, b2 = second[second[x][y]][z], second[x][second[y][z]]
        assert a1 ^ b1 == a2 ^ b2
    squares = [sum(table[x][x] == 0 for x in range(16)) for table in (first, second)]
    assert squares == [14, 2]
    check1, matrix1 = check_components('binary_cubic_single_edge', first)
    check2, matrix2 = check_components('binary_cubic_bilinear_twist', second)
    assert matrix1 == matrix2
    assert check1['local_matrix_sha256'] == check2['local_matrix_sha256']
    assert all(Fraction(matrix1[a][a], 16**3) == Fraction(43, 64) for a in range(16))
    return {'square_one_counts': squares, 'identical_associator_values': True,
            'identical_translated_defect_matrices': True,
            'checks': [check1, check2]}


def star_triangle_collision():
    stars = [(0, 1), (0, 2), (0, 3)]
    triangles = [(0, 1), (0, 2), (1, 2)]
    checks = []
    matrices = []
    for name, edges in [('star_K1_3', stars), ('triangle_and_isolate', triangles)]:
        _, table = graph_table(2, 4, edges)
        result, counts = check_components(name, table)
        assert result['component_count'] == 32 and result['component_size'] == 8
        assert result['local_isolate_count'] == (16 if name == 'star_K1_3' else 32)
        for a, b in product(range(256), repeat=2):
            expected = Fraction(65, 128) if a == b else (
                Fraction(9, 128) if a // 8 == b // 8 else Fraction(0))
            assert Fraction(counts[a][b], 256**3) == expected
        checks.append(result)
        matrices.append(counts)
    assert matrices[0] == matrices[1]
    return {'checks': checks, 'matrices_identical_in_coordinate_order': True,
            'two_color_recovered_central_factor_ranks': [0, 1],
            'block_diagonal_weight': '65/128', 'block_off_diagonal_weight': '9/128'}


def scalar_spectrum_checks():
    out = []
    for kind, p, r in [('bruck', p, r) for p in (2, 3, 5)
                       for r in (0, 2, 4) if not (p == 5 and r == 4)] + [
                           ('cubic', 2, r) for r in (0, 2, 4)]:
        points = list(product(range(p), repeat=r+1))
        basis = [tuple(int(i == j) for i in range(r+1)) for j in range(r+1)]

        def add(x, y):
            return tuple((a+b) % p for a, b in zip(x, y))

        def factor(x, y):
            beta = sum(x[i]*y[i+1]-x[i+1]*y[i] for i in range(1, r+1, 2)) % p
            if kind == 'bruck':
                return (x[0]+2*y[0])*beta % p
            return (x[0]*beta+y[0]*sum(x[i]*x[i+1] for i in range(1, r+1, 2))) % p

        count = 0
        for x, y in product(points, repeat=2):
            if all((factor(x, y)+factor(add(x, y), z)
                    -factor(y, z)-factor(x, add(y, z))) % p == 0 for z in basis):
                count += 1
        actual = Fraction(count, len(points)**2)
        predicted = (Fraction(1, 4)+Fraction(3, 4)*Fraction(1, 2**r)
                     if kind == 'bruck' and p == 2 else
                     Fraction(1, p**3)+(1-Fraction(1, p**3))*Fraction(1, p**r))
        assert actual == predicted
        out.append({'kind': kind, 'p': p, 'scalar_rank': r,
                    'quotient_pairs': len(points)**2, 'eigenvalue': str(actual)})
    return out


def generated_subloop(table, left, right, generators):
    current = {0, *generators}
    changed = True
    while changed:
        enlarged = current | {operation[x][y] for x in current for y in current
                              for operation in (table, left, right)}
        changed = enlarged != current
        current = enlarged
    return frozenset(current)


def all_subloops(table):
    left, right = divisions(table)
    found = {frozenset({0})}
    queue = deque(found)
    while queue:
        sub = queue.popleft()
        for x in range(len(table)):
            if x not in sub:
                bigger = generated_subloop(table, left, right, sub | {x})
                if bigger not in found:
                    found.add(bigger)
                    queue.append(bigger)
    return found


def subgroup_incidence_collision(p=3):
    elements = list(product(range(p*p), range(p)))
    idx = {x: i for i, x in enumerate(elements)}
    abelian = group_table(elements, lambda x, y: ((x[0]+y[0]) % (p*p), (x[1]+y[1]) % p))
    modular = group_table(elements, lambda x, y: ((x[0]+pow(1+p, x[1], p*p)*y[0]) % (p*p),
                                                (x[1]+y[1]) % p))
    for table in (abelian, modular):
        divisions(table)
        assert all(table[table[x][y]][z] == table[x][table[y][z]]
                   for x, y, z in product(range(p**3), repeat=3))
    assert abelian[idx[(1, 0)]][idx[(0, 1)]] == abelian[idx[(0, 1)]][idx[(1, 0)]]
    assert modular[idx[(1, 0)]][idx[(0, 1)]] != modular[idx[(0, 1)]][idx[(1, 0)]]
    transport = {idx[(p*i, j)]: idx[(p*i, j)] for i, j in product(range(p), repeat=2)}
    for j in range(p):
        generator = idx[(1, j)]
        x = y = 0
        for _ in range(p*p):
            if x in transport:
                assert transport[x] == y
            transport[x] = y
            x, y = modular[x][generator], abelian[y][generator]
    assert len(transport) == p**3 and len(set(transport.values())) == p**3
    subs_a, subs_b = all_subloops(abelian), all_subloops(modular)
    assert {frozenset(transport[x] for x in sub) for sub in subs_b} == subs_a
    for x in range(p**3):
        powers_b, powers_a = {0}, {0}
        b = a = 0
        for _ in range(p*p):
            b, a = modular[b][x], abelian[a][transport[x]]
            powers_b.add(b)
            powers_a.add(a)
        assert {transport[b] for b in powers_b} == powers_a
    return {'p': p, 'order': p**3, 'subgroup_count': len(subs_a),
            'subgroup_order_counts': dict(sorted(Counter(map(len, subs_a)).items())),
            'explicit_incidence_and_power_graph_isomorphism': True,
            'groups_nonisomorphic_by_commutativity': True}


def main():
    nonbol = [[0, 1, 2, 3, 4], [1, 0, 3, 4, 2], [2, 3, 4, 0, 1],
              [3, 4, 1, 2, 0], [4, 2, 0, 1, 3]]
    perms = list(permutations(range(3)))
    s3 = group_table(perms, lambda x, y: tuple(x[y[i]] for i in range(3)))
    central3 = graph_table(3, 2, [(0, 1)])[1]
    bruck2 = graph_table(2, 2, [(0, 1)])[1]
    examples = [check_components('nonbol_order5', nonbol, False)[0],
                check_components('symmetric_group_S3', s3)[0],
                check_components('ternary_single_edge', central3)[0],
                check_components('proper_bruck_single_edge_F2', bruck2)[0]]
    result = {'component_theorem_examples': examples,
              'same_associator_moufang_collision': moufang_and_associator_collision(),
              'graph_family_collision': star_triangle_collision(),
              'scalar_spectrum': scalar_spectrum_checks(),
              'subgroup_incidence_collision': subgroup_incidence_collision(),
              'status': 'all checks passed'}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
