"""Exact finite certificates for translation-class fusion and fermionic traces.

Python 3.11+, standard library; run with assertions enabled. The 363-class
example replaces F_(3^18) by F_3 to test the local bimap arithmetic. Its
induction test uses Z semidirect C_9, not a claim to construct the huge loop.
The two 801-class controls are class-two groups, not selected simple Bol loops.
General functoriality and modularity are proved in the companion manuscripts.
"""

from collections import Counter
from itertools import product
from math import comb
import json


P = 3


def add(x, y):
    return tuple((a + b) % P for a, b in zip(x, y))


def neg(x):
    return tuple(-a % P for a in x)


def scale(a, x):
    return tuple(a * b % P for b in x)


def vectors(n):
    return list(product(range(P), repeat=n))


def rank(rows):
    a = [list(x) for x in rows]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c] % P), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        a[r] = [v * pow(a[r][c], -1, P) % P for v in a[r]]
        for i in range(len(a)):
            if i != r:
                t = a[i][c]
                a[i] = [(u - t * v) % P for u, v in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def combination(forms, ell):
    d = len(forms[0])
    return [[sum(ell[k] * forms[k][i][j] for k in range(len(forms))) % P
             for j in range(d)] for i in range(d)]


def pairing(forms, x, y):
    return tuple(sum(x[i] * b[i][j] * y[j]
                     for i in range(len(x)) for j in range(len(y))) % P
                 for b in forms)


def span(generators, dim):
    ans = {(0,) * dim}
    for v in generators:
        ans = {add(w, scale(t, v)) for w in ans for t in range(P)}
    return ans


def seed(forms):
    """Construct actual conjugacy classes via central commutator cosets."""
    d, s = len(forms[0]), len(forms)
    ws, zs = vectors(d), vectors(s)
    basis = [tuple(int(i == j) for i in range(d)) for j in range(d)]
    images, representatives, classes = {}, {}, []
    for w in ws:
        image = span([pairing(forms, w, u) for u in basis], s)
        images[w] = image
        for z in zs:
            representatives[w, z] = min(add(z, t) for t in image)
        classes.extend((w, z) for z in sorted({representatives[w, z] for z in zs}))
    index = {c: i for i, c in enumerate(classes)}
    radicals = {}
    ranks = {}
    for ell in zs:
        radicals[ell] = {w for w in ws
                         if all(sum(a * b for a, b in zip(ell, z)) % P == 0
                                for z in images[w])}
        ranks[ell] = rank(combination(forms, ell))
        assert len(radicals[ell]) == P ** (d - ranks[ell])
    assert len(classes) == sum(map(len, radicals.values()))

    def central(z):
        return tuple(index[w, representatives[w, add(t, z)]] for w, t in classes)

    return dict(forms=forms, d=d, s=s, ws=ws, zs=zs, images=images,
                reps=representatives, classes=classes, index=index,
                radicals=radicals, ranks=ranks, central=central)


def compose(g, h):
    return tuple(g[h[i]] for i in range(len(g)))


def inverse(g):
    h = [0] * len(g)
    for i, j in enumerate(g):
        h[j] = i
    return tuple(h)


def cycles(g):
    remaining = set(range(len(g)))
    counts = Counter()
    while remaining:
        i = next(iter(remaining))
        j, size = i, 0
        while j in remaining:
            remaining.remove(j)
            size += 1
            j = g[j]
        assert j == i
        counts[size] += 1
    return dict(sorted(counts.items()))


def fixed(g):
    return sum(i == j for i, j in enumerate(g))


def reconstruction_checks(data):
    """Check higher fusion and subspace inversion against enumerated orbits."""
    s = data['s']
    subspaces = {frozenset({(0,) * s})}
    for v in data['zs']:
        subspaces |= {frozenset(span(list(j) + [v], s)) for j in tuple(subspaces)}
    expected = Counter(frozenset(j) for j in data['images'].values())
    h = {}
    for j in subspaces:
        annihilator = [ell for ell in data['zs']
                       if all(sum(a * b for a, b in zip(ell, z)) % P == 0 for z in j)]
        common = set(data['ws'])
        for ell in annihilator:
            common &= data['radicals'][ell]
        assert len(common) == sum(image <= j for image in data['images'].values())
        h[j] = len(common)
    recovered = {}
    dimensions = {j: rank(list(j)) for j in subspaces}
    for j in subspaces:
        value = 0
        for k in subspaces:
            if k <= j:
                delta = dimensions[j] - dimensions[k]
                value += (-1) ** delta * P ** (delta * (delta - 1) // 2) * h[k]
        assert value == expected[j]
        recovered[j] = value
    assert sum(recovered[j] * P ** (s - dimensions[j]) for j in subspaces) == len(data['classes'])

    # Charge subspaces must have linear joint radicals, a constraint that
    # arbitrary finite Z-sets with the same individual characters need not meet.
    joint_counts, joint_ranks = {}, {}
    for e in subspaces:
        common = set(data['ws'])
        for ell in e:
            common &= data['radicals'][ell]
        exponent = next(j for j in range(data['d'] + 1) if P ** j == len(common))
        joint_counts[e] = len(common)
        joint_ranks[e] = data['d'] - exponent
    submodular_checks = 0
    for e in subspaces:
        for f in subspaces:
            total = frozenset(span(list(e) + list(f), s))
            meet = e & f
            if e <= f:
                assert joint_ranks[e] <= joint_ranks[f]
            defect = joint_ranks[e] + joint_ranks[f] - joint_ranks[total] - joint_ranks[meet]
            assert defect >= 0
            assert (joint_counts[total] * joint_counts[meet]
                    == P ** defect * joint_counts[e] * joint_counts[f])
            submodular_checks += 1

    channel_checks = 0
    for nu in data['zs']:
        for ell in data['zs']:
            u = data['radicals'][ell] & data['radicals'][add(nu, neg(ell))]
            for rho in data['zs']:
                v = data['radicals'][rho] & data['radicals'][add(nu, neg(rho))]
                triple = (data['radicals'][ell] & data['radicals'][rho]
                          & data['radicals'][add(add(nu, neg(ell)), neg(rho))])
                assert u & v == triple
                assert len(u) + len(v) == len(u | v) + len(triple)
                channel_checks += 1
    return dict(center_subspaces=len(subspaces), recovered_orbit_types=len(expected),
                binary_triple_channel_checks=channel_checks,
                subspace_rank_inequality_checks=submodular_checks)


# Exact Q(zeta_3), represented by a+b*zeta, zeta^2=-1-zeta.
def zadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def zmul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def zscale(a, x):
    return a * x[0], a * x[1]


ROOTS = ((1, 0), (0, 1), (-1, -1))


def fermion_coefficients(cycle_shape, degree=4, species=24):
    """Finite truncation of the actual odd-cycle exterior determinant."""
    out = [1] + [0] * degree
    for d, number in cycle_shape.items():
        assert d % 2
        for m in range(1, degree // d + 1):
            step = m * d
            exponent = species * number
            previous = out[:]
            out = [sum(previous[n - step * j] * comb(exponent, j)
                       for j in range(min(n // step, exponent) + 1))
                   for n in range(degree + 1)]
    return out


def rigid_local_checks():
    a0 = [[0, 0, 0, 0], [0, 0, 0, 2],
          [0, 0, 0, 0], [0, 1, 0, 0]]
    a2 = [[0, 1, 2, 1], [2, 0, 1, 1],
          [1, 2, 0, 0], [2, 2, 0, 0]]
    data = seed([a0, [[0] * 4 for _ in range(4)], a2])
    assert Counter(data['ranks'].values()) == {0: 3, 2: 12, 4: 12}
    assert len(data['classes']) == 363

    # Independently check the class partition by BCH group conjugation.
    def mul(g, h):
        x, z = g
        y, t = h
        return add(x, y), add(add(z, t), scale(2, pairing(data['forms'], x, y)))

    generators = [(tuple(int(i == j) for i in range(4)), (0, 0, 0))
                  for j in range(4)]
    all_elements = {(w, z) for w in data['ws'] for z in data['zs']}
    count = 0
    while all_elements:
        start = min(all_elements)
        orbit, pending = {start}, [start]
        while pending:
            x = pending.pop()
            for g in generators:
                y = mul(mul((neg(g[0]), neg(g[1])), x), g)
                if y not in orbit:
                    orbit.add(y)
                    pending.append(y)
        w, z = start
        assert orbit == {(w, add(z, t)) for t in data['images'][w]}
        all_elements.difference_update(orbit)
        count += 1
    assert count == 363

    zplus, zminus = (1, 0, 1), (1, 0, 0)
    assert cycles(data['central'](zplus)) == {1: 264, 3: 33}
    assert cycles(data['central'](zminus)) == {1: 192, 3: 57}
    # Recover commutator-image strata directly, not from Fourier ranks.
    strata = Counter(frozenset(v) for v in data['images'].values())
    zero = frozenset({(0, 0, 0)})
    line1 = frozenset(span([(0, 0, 1)], 3))
    line2 = frozenset(span([(1, 0, 1)], 3))
    plane = frozenset(span([(1, 0, 0), (0, 0, 1)], 3))
    assert strata == {zero: 1, line1: 8, line2: 8, plane: 64}
    return data


def induced_checks(data):
    """Exact induction to Z semidirect C9, keeping left and right Z separate."""
    size = len(data['classes'])
    n = 9 * size

    def torus(z, power=1):
        for _ in range(power % 3):
            z = (z[0], (z[0] + z[1]) % 3, (z[1] + z[2]) % 3)
        return z

    def sigma(z):
        return z[0], -z[1] % 3, (z[1] + z[2]) % 3

    def left(z):
        local = [data['central'](torus(z, -r)) for r in range(9)]
        return tuple(r * size + local[r][i] for r in range(9) for i in range(size))

    def right(z):
        local = data['central'](z)
        return tuple(r * size + local[i] for r in range(9) for i in range(size))

    a = tuple(((r + 1) % 9) * size + i for r in range(9) for i in range(size))
    ai = inverse(a)
    theta_local = tuple(data['index'][neg(w), data['reps'][neg(w), sigma(z)]]
                        for w, z in data['classes'])
    theta = tuple((-r % 9) * size + theta_local[i]
                  for r in range(9) for i in range(size))
    identity = tuple(range(n))
    assert compose(theta, theta) == identity
    assert compose(compose(theta, a), theta) == ai
    for z in data['zs']:
        assert compose(a, right(z)) == compose(right(z), a)
        assert compose(compose(a, left(z)), ai) == left(torus(z))
        assert compose(compose(theta, left(z)), theta) == left(sigma(z))

    result = []
    for f, expected, expected_fixed, ell in [
        ((1, 2, 1), (1, 0, 1), 792, (1, 1, 1)),
        ((1, 2, 0), (1, 0, 0), 576, (2, 1, 1)),
    ]:
        cocycle = [(0, 0, 0)]
        for r in range(9):
            cocycle.append(add(cocycle[-1], torus(f, r)))
        assert cocycle[9] == (0, 0, 0)
        for r in range(9):
            assert torus(sigma(cocycle[r]), r) == cocycle[r]
            for s in range(9):
                assert cocycle[(r + s) % 9] == add(cocycle[r], torus(cocycle[s], r))
        u = left(f)
        norm = lambda v: compose(compose(compose(v, a), v), ai)
        probe = norm(norm(u))
        assert probe == left(expected)
        assert fixed(probe) == expected_fixed
        assert cycles(probe) == {1: expected_fixed, 3: (n - expected_fixed) // 3}
        assert fixed(right(expected)) == 3 * expected_fixed
        coeff = fermion_coefficients(cycles(probe), 4)
        # Newton's exterior-power trace formula, independently of cycle products.
        t1, t2, t3 = 24 * fixed(probe), 24 * fixed(compose(probe, probe)), 24 * n
        assert coeff[1] == t1
        assert coeff[2] == t1 + (t1 * t1 - t2) // 2
        assert coeff[3] == (t1**3 - 3 * t1 * t2 + 2 * t3) // 6 + t1**2 + t1
        result.append(dict(f=f, probe=expected, left_fixed=expected_fixed,
                           right_fixed=fixed(right(expected)), coefficients=coeff,
                           selected_induced_dimension=9 * len(data['radicals'][ell])))

    # Project actual graded traces onto all right charges by exact Fourier sums.
    series = {z: fermion_coefficients(cycles(right(z)), 3) for z in data['zs']}
    multiplicities = {ell: 9 * len(rad) for ell, rad in data['radicals'].items()}
    for ell in data['zs']:
        projected = []
        for degree in range(4):
            total = (0, 0)
            for z in data['zs']:
                phase = -sum(x * y for x, y in zip(ell, z)) % P
                total = zadd(total, zscale(series[z][degree], ROOTS[phase]))
            assert total[1] == 0 and total[0] % 27 == 0
            projected.append(total[0] // 27)
        assert min(projected) >= 0
        assert projected[1] == 24 * multiplicities[ell]
        convolution = sum(multiplicities[alpha] * multiplicities[add(ell, neg(alpha))]
                          for alpha in data['zs'])
        assert projected[2] == (24 * multiplicities[ell]
                                 + (576 * convolution - 24 * multiplicities[scale(2, ell)]) // 2)
    return dict(seed_classes=size, induced_points=n, cases=result,
                projected_charges=27, projected_through_degree=3)


def same_rank_controls():
    # The first 4x4 pencil has off-diagonal I and an irreducible C over F3.
    forms1 = [[[0] * 6 for _ in range(6)] for _ in range(2)]
    for k, block in enumerate([[[1, 0], [0, 1]], [[0, 2], [1, 0]]]):
        for i in range(2):
            for j in range(2):
                forms1[k][i][j + 2] = block[i][j]
                forms1[k][j + 2][i] = -block[i][j] % 3
    forms2 = [[[0] * 6 for _ in range(6)] for _ in range(2)]
    for offset in (0, 3):
        for k in range(2):
            forms2[k][offset][offset + k + 1] = 1
            forms2[k][offset + k + 1][offset] = 2
    first, second = seed(forms1), seed(forms2)
    assert first['ranks'] == second['ranks']
    assert Counter(first['ranks'].values()) == {0: 1, 4: 8}
    assert len(first['classes']) == len(second['classes']) == 801
    fusion = []
    for ell in first['zs']:
        for mu in first['zs']:
            intersection1 = first['radicals'][ell] & first['radicals'][mu]
            intersection2 = second['radicals'][ell] & second['radicals'][mu]
            for item, intersection in [(first, intersection1), (second, intersection2)]:
                assert intersection <= item['radicals'][add(ell, mu)]
            if rank([ell, mu]) == 2:
                assert len(intersection1) == 9 and len(intersection2) == 1
                fusion.append((len(intersection1), len(intersection2)))
    for z in first['zs']:
        assert cycles(first['central'](z)) == cycles(second['central'](z))
        if any(z):
            assert cycles(first['central'](z)) == {1: 720, 3: 27}

    # The phase-complete sewing probe has eigenvalues of a permutation of
    # type 1^(2N-3s) 3^s in this control. Its current-defined s differs.
    profiles = [{1: 1602 - 3 * s, 3: s} for s in (9, 1)]
    coeffs = [fermion_coefficients(shape, 4) for shape in profiles]
    assert coeffs[0][1] == 37800 and coeffs[1][1] == 38376
    assert coeffs[1][1] - coeffs[0][1] == 576
    return dict(classes_each=801, ranks={"0": 1, "4": 8},
                independent_charge_pairs=len(fusion), fusion_dimensions=[9, 1],
                all_central_cycle_profiles_equal=True,
                sewing_probe_coefficients=coeffs)


def car_checks():
    """Check the actual finite exterior action on 3 points x 3 modes."""
    npoints, nmodes = 3, 3
    a = ROOTS
    b = (ROOTS[0], ROOTS[2], ROOTS[1])
    ab = tuple(zmul(x, y) for x, y in zip(a, b))

    def current(state, values, m, n):
        out = {}
        for x, value in enumerate(values):
            source, target = n * npoints + x, m * npoints + x
            if not (state >> source) & 1:
                continue
            sign = (-1) ** ((state & ((1 << source) - 1)).bit_count())
            middle = state ^ (1 << source)
            if (middle >> target) & 1:
                continue
            sign *= (-1) ** ((middle & ((1 << target) - 1)).bit_count())
            end = middle | (1 << target)
            out[end] = zadd(out.get(end, (0, 0)), zscale(sign, value))
        return {s: c for s, c in out.items() if c != (0, 0)}

    def apply(states, values, m, n):
        out = {}
        for state, coefficient in states.items():
            for end, value in current(state, values, m, n).items():
                out[end] = zadd(out.get(end, (0, 0)), zmul(coefficient, value))
        return {s: c for s, c in out.items() if c != (0, 0)}

    def difference(x, y):
        keys = x.keys() | y.keys()
        out = {k: zadd(x.get(k, (0, 0)), zscale(-1, y.get(k, (0, 0)))) for k in keys}
        return {s: c for s, c in out.items() if c != (0, 0)}

    tests = 0
    for m, n, r, s in [(0, 1, 1, 2), (0, 1, 1, 0), (0, 0, 0, 2),
                        (0, 1, 2, 2), (1, 2, 0, 1)]:
        for state in range(1 << (npoints * nmodes)):
            lhs = difference(apply(current(state, b, r, s), a, m, n),
                             apply(current(state, a, m, n), b, r, s))
            rhs = difference(current(state, ab, m, s) if n == r else {},
                             current(state, ab, r, n) if s == m else {})
            assert lhs == rhs
            tests += 1
    return dict(exterior_basis_states=512, exact_cyclotomic_commutator_checks=tests)


def admissibility_control():
    """A 51-point Z-set has legal separate ranks but an impossible joint count."""
    forms = [[[0] * 3 for _ in range(3)] for _ in range(2)]
    for k in range(2):
        forms[k][0][k + 1] = 1
        forms[k][k + 1][0] = 2
    genuine = seed(forms)
    zs = genuine['zs']
    zero = frozenset({(0, 0)})
    lines = sorted({frozenset(span([z], 2)) for z in zs if any(z)}, key=sorted)
    whole = frozenset(zs)
    strata = Counter(frozenset(j) for j in genuine['images'].values())
    assert strata == Counter({zero: 1, **{j: 2 for j in lines}, whole: 18})

    # Build the alternative Z-set as actual coset orbits, not a character list.
    stabilizers = [zero] * 2 + lines + [whole] * 21
    representatives, points = {}, []
    for orbit, j in enumerate(stabilizers):
        for z in zs:
            representatives[orbit, z] = min(add(z, t) for t in j)
        points.extend((orbit, z) for z in sorted({representatives[orbit, z] for z in zs}))
    index = {point: i for i, point in enumerate(points)}
    assert len(points) == len(genuine['classes']) == 51

    def supports(ell, j):
        return all(sum(a * b for a, b in zip(ell, z)) % P == 0 for z in j)

    for ell in zs:
        count = sum(supports(ell, j) for j in stabilizers)
        assert count == len(genuine['radicals'][ell]) == (27 if not any(ell) else 3)
    for z in zs:
        permutation = tuple(index[orbit, representatives[orbit, add(t, z)]]
                            for orbit, t in points)
        assert cycles(permutation) == cycles(genuine['central'](z))
        if any(z):
            assert cycles(permutation) == {1: 24, 3: 9}
    for ell in zs:
        for mu in zs:
            if rank([ell, mu]) == 2:
                assert len(genuine['radicals'][ell] & genuine['radicals'][mu]) == 1
                assert sum(supports(ell, j) and supports(mu, j) for j in stabilizers) == 2
    assert 2 not in {P ** j for j in range(4)}
    coefficients = [fermion_coefficients({1: 102 - 3 * s, 3: s}, 2)
                    for s in (1, 2)]
    assert [c[1] for c in coefficients] == [2376, 2304]
    return dict(points_each=51, trivial_charge_dimension=27,
                nontrivial_charge_dimension=3, independent_fusion_dimensions=[1, 2],
                alternative_joint_count_is_prime_power=False,
                first_fusion_trace_coefficients=[2376, 2304])


def main():
    assert __debug__, "Run with assertions enabled"
    data = rigid_local_checks()
    report = dict(status="PASS", reduced_rigid=induced_checks(data),
                  fusion_reconstruction=reconstruction_checks(data),
                  same_rank=same_rank_controls(), fermion_currents=car_checks(),
                  admissibility_control=admissibility_control())
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
