#!/usr/bin/env python3
"""Exact central cubic Bol-family checks; Python 3.11+, standard library only.

Default: exhaustive p=3. Optional: --primes 3 5, with cubic-time Bol checks.
No enormous-loop table is constructed. This script validates formulas and
small instances, not any global classification or moonshine conjecture.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from itertools import product
import json
import random


def compose(f, g):
    return tuple(f[i] for i in g)


def inverse(f):
    out = [0] * len(f)
    for i, j in enumerate(f):
        out[j] = i
    return tuple(out)


def cycle_type(f):
    unseen = set(range(len(f)))
    result = Counter()
    while unseen:
        i = next(iter(unseen))
        length = 0
        while i in unseen:
            unseen.remove(i)
            length += 1
            i = f[i]
        result[length] += 1
    return tuple(sorted(result.items()))


def generated_group(generators):
    identity = tuple(range(len(generators[0])))
    found = {identity}
    queue = deque([identity])
    while queue:
        g = queue.popleft()
        for s in generators:
            h = compose(s, g)
            if h not in found:
                found.add(h)
                queue.append(h)
    return found


def oscillator_coefficients(cycles, degree):
    """Coefficients after removing q^(-N/24), exact finite Euler product."""
    out = [1] + [0] * degree
    for j, count in cycles:
        for d in range(j, degree + 1, j):
            for _ in range(count):
                for n in range(d, degree + 1):
                    out[n] += out[n - d]
    return out


def verify(p):
    assert p >= 3 and p % 2 and all(p % d for d in range(2, int(p**0.5) + 1))
    elements = list(product(range(p), repeat=3))
    labels = {x: i for i, x in enumerate(elements)}
    n = len(elements)
    identity = tuple(range(n))
    zero = labels[(0, 0, 0)]
    e1, e2, central = (labels[x] for x in [(0, 1, 0), (0, 0, 1), (1, 0, 0)])

    def mul_tuple(x, y, k):
        c, a, b = x
        d, u, v = y
        return ((c + d + b * u * (a + u) + k * (a * v - b * u)) % p,
                (a + u) % p, (b + v) % p)

    def inv_tuple(x):
        return tuple(-a % p for a in x)

    negative = tuple(labels[inv_tuple(x)] for x in elements)
    all_reports = []
    group_zero = None
    defects_zero = None
    translations_zero = None
    table_zero = tuple(tuple(labels[mul_tuple(x, y, 0)] for y in elements)
                       for x in elements)

    for k in (0, 1):
        table = tuple(tuple(labels[mul_tuple(x, y, k)] for y in elements)
                      for x in elements)
        left = table
        left_inverse = tuple(inverse(l) for l in left)
        assert table[zero] == identity
        assert all(table[x][zero] == x for x in range(n))
        assert all(len(set(row)) == n for row in table)
        assert all(len({table[x][y] for x in range(n)}) == n for y in range(n))
        assert all(table[x][negative[x]] == table[negative[x]][x] == zero
                   for x in range(n))

        for x, y, z in product(range(n), repeat=3):
            assert table[x][table[y][table[x][z]]] == table[table[x][table[y][x]]][z]
        assert table[table[e1][e2]][e1] != table[e1][table[e2][e1]]

        aip_failures = 0
        defect_histogram = Counter()
        aip_histogram = Counter()
        marked_defects = {}
        for x, y in product(range(n), repeat=2):
            _, a, b = elements[x]
            _, u, v = elements[y]
            delta = (a * v - b * u) % p
            xy = table[x][y]
            dxy = compose(left_inverse[xy], compose(left[x], left[y]))
            expected = tuple(labels[((d - delta * s) % p, s, t)]
                             for d, s, t in elements)
            assert dxy == expected
            marked_defects[x, y] = dxy
            dtype = cycle_type(dxy)
            assert dtype == (((1, n),) if not delta else ((1, p*p), (p, p*(p-1))))
            defect_histogram[str(dtype)] += 1
            # Independent finite control of the odd-Bol two-word collapse.
            assert len(cycle_type(compose(left[x], left[y]))) == 1
            if delta:
                assert len(dtype) == 2

            target = table[negative[x]][negative[y]]
            aip_failures += target != negative[xy]
            exy = compose(left_inverse[negative[xy]], left[target])
            expected_e = tuple(labels[((d + 2*k*delta) % p, s, t)]
                               for d, s, t in elements)
            assert exy == expected_e
            etype = cycle_type(exy)
            assert etype == (((1, n),) if not k*delta else ((p, p*p),))
            aip_histogram[str(etype)] += 1

        expected_nonzero = p*p*(p*p-1)*(p*p-p)
        assert aip_failures == (expected_nonzero if k else 0)

        # Principal isotope of Q_0 with identity t=(0,-k,0).
        t = labels[(0, -k % p, 0)]
        right_t = tuple(table_zero[x][t] for x in range(n))
        divide_t = inverse(right_t)
        phi = tuple(labels[((c-k*a*b) % p, (a-k) % p, b)] for c, a, b in elements)
        for x, y in product(range(n), repeat=2):
            assert phi[table[x][y]] == table_zero[divide_t[phi[x]]][phi[y]]

        # The generated group is exactly the p^4 maps in (S9).
        group = generated_group([left[e1], left[e2], left[central]])
        explicit = set()
        for a, b, B, C in product(range(p), repeat=4):
            explicit.add(tuple(labels[((d+b*u*u+B*u+k*a*v+C) % p,
                                       (u+a) % p, (v+b) % p)]
                               for d, u, v in elements))
        assert group == explicit
        assert len(group) == p**4
        assert set(left).issubset(group)
        assert sum(g[zero] == zero for g in group) == p
        fk = tuple(labels[((d+k*u*v) % p, u, v)] for d, u, v in elements)
        if k == 0:
            group_zero = group
            defects_zero = marked_defects
            translations_zero = tuple(cycle_type(l) for l in left)
        else:
            assert group == {compose(fk, compose(g, inverse(fk))) for g in group_zero}
            assert marked_defects == defects_zero
            assert tuple(cycle_type(l) for l in left) == translations_zero

        # Power law includes the essential integer-division convention at p=3.
        for x, (c, a, b) in enumerate(elements):
            power = identity
            for exponent in range(1, p*p+1):
                power = compose(left[x], power)
                xpow = ((exponent*c + b*a*a*((exponent**3-exponent)//3)) % p,
                        exponent*a % p, exponent*b % p)
                assert power == left[labels[xpow]]

        # Arbitrary deterministic random relabeling conjugates every marked word.
        rng = random.Random(323_000+p*10+k)
        shuffle = list(range(n))
        rng.shuffle(shuffle)
        shuffle = tuple(shuffle)
        unshuffle = inverse(shuffle)
        relabeled = [[None]*n for _ in range(n)]
        for x, y in product(range(n), repeat=2):
            relabeled[shuffle[x]][shuffle[y]] = shuffle[table[x][y]]
        relabeled = tuple(tuple(row) for row in relabeled)
        for x, y in product(range(n), repeat=2):
            rx, ry = shuffle[x], shuffle[y]
            rd = compose(inverse(relabeled[relabeled[rx][ry]]),
                         compose(relabeled[rx], relabeled[ry]))
            assert rd == compose(shuffle, compose(marked_defects[x,y], unshuffle))
            assert cycle_type(rd) == cycle_type(marked_defects[x,y])
            reinv_xy = shuffle[negative[table[x][y]]]
            reinv_x_reinv_y = relabeled[shuffle[negative[x]]][shuffle[negative[y]]]
            re = compose(inverse(relabeled[reinv_xy]), relabeled[reinv_x_reinv_y])
            e = compose(left_inverse[negative[table[x][y]]],
                        left[table[negative[x]][negative[y]]])
            assert re == compose(shuffle, compose(e, unshuffle))

        all_reports.append({
            "k": k, "order": n, "left_bol_triples": n**3,
            "proper_witness": [elements[e1], elements[e2], elements[e1]],
            "aip_failing_pairs": aip_failures,
            "left_multiplication_group_order": len(group),
            "identity_stabilizer_order": p,
            "defect_cycle_histogram": dict(defect_histogram),
            "aip_probe_cycle_histogram": dict(aip_histogram),
            "translation_cycle_histogram": dict(Counter(str(cycle_type(l)) for l in left)),
            "principal_isotope_pairs": n*n,
            "random_relabeling_pairs": n*n,
            "two_translation_uniform_cycle_pairs": n*n,
        })

    cycles_d = ((1,p*p),(p,p*(p-1)))
    cycles_e = ((p,p*p),)
    coefficients_d = oscillator_coefficients(cycles_d, 6)
    coefficients_e = oscillator_coefficients(cycles_e, 6)
    coefficients_i = oscillator_coefficients(((1,p**3),), 6)
    assert coefficients_d[1] == p*p
    assert coefficients_e[1] == 0 and coefficients_e[p] == p*p
    assert coefficients_i[1] == p**3
    return {"p": p, "members": all_reports,
            "oscillator_coefficients_q0_through_q6": {
                "identity": coefficients_i, "nonzero_associator_defect": coefficients_d,
                "nonzero_aip_probe": coefficients_e}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", type=int, nargs="+", choices=[3, 5], default=[3])
    args = parser.parse_args()
    print(json.dumps({"status": "PASS", "checks": [verify(p) for p in args.primes]},
                     indent=2))
