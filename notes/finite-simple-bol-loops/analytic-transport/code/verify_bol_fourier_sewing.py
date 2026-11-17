"""Exact Fourier-sewing certificates; Python 3.11+, standard library only.

Run with assertions enabled. No huge-loop or induced-set table is generated.
The quartic groups are algebraic controls, not asserted simple proper Bol
realizations. The 363-class model replaces F_(3^18) by F_3 only for local
arithmetic. The large selected-loop and strict-transport interfaces are inputs.

Convention: A(Tx,y)=B(x,y), Fourier kernel psi(A(x,y)), and
F_A F_B^(-1)=P_T, where P_T eta_x=eta_(Tx).
"""

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, factorial
from pathlib import Path
from random import Random


P = 3
ROOTS = ((1, 0), (0, 1), (-1, -1))  # 1,zeta,zeta^2 in Z[zeta_3].


def vectors(d):
    return list(product(range(P), repeat=d))


def add(x, y):
    return tuple((a + b) % P for a, b in zip(x, y))


def scale(c, x):
    return tuple(c * a % P for a in x)


def dot(x, y):
    return sum(a * b for a, b in zip(x, y)) % P


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col)) % P
             for col in zip(*b)] for row in a]


def mv(a, x):
    return tuple(dot(row, x) for row in a)


def madd(a, b, coefficient=1):
    return [[(x + coefficient * y) % P for x, y in zip(r, s)]
            for r, s in zip(a, b)]


def rank(rows):
    a = [list(row) for row in rows]
    if not a:
        return 0
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j] % P), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        c = pow(a[r][j], -1, P)
        a[r] = [c * x % P for x in a[r]]
        for i in range(len(a)):
            if i != r:
                c = a[i][j]
                a[i] = [(x - c * y) % P for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def inverse(a):
    n = len(a)
    m = [list(row) + e for row, e in zip(a, eye(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if m[i][j] % P)
        m[j], m[pivot] = m[pivot], m[j]
        c = pow(m[j][j], -1, P)
        m[j] = [c * x % P for x in m[j]]
        for i in range(n):
            if i != j:
                c = m[i][j]
                m[i] = [(x - c * y) % P for x, y in zip(m[i], m[j])]
    return [row[n:] for row in m]


def basis(vs):
    result = []
    for v in vs:
        if rank(result + [v]) > len(result):
            result.append(v)
    return result


def span(generators, d):
    result = {(0,) * d}
    for v in generators:
        result = {add(w, scale(c, v)) for w in result for c in range(P)}
    return result


def pairing(forms, x, y):
    return tuple(dot(x, mv(a, y)) for a in forms)


def scalar_form(forms, ell):
    d = len(forms[0])
    return [[sum(c * a[i][j] for c, a in zip(ell, forms)) % P
             for j in range(d)] for i in range(d)]


def cycle_counts(permutation):
    remaining, result = set(range(len(permutation))), Counter()
    while remaining:
        first = next(iter(remaining))
        x, length = first, 0
        while x in remaining:
            remaining.remove(x)
            length += 1
            x = permutation[x]
        assert x == first
        result[length] += 1
    return dict(sorted(result.items()))


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def fixed_from_cycles(cycles, k):
    return sum(d * number for d, number in cycles.items() if k % d == 0)


def remainder(f, g):
    f = [x % P for x in f]
    while f and not f[-1]:
        f.pop()
    while len(f) >= len(g):
        k, c = len(f) - len(g), f[-1] * pow(g[-1], -1, P) % P
        for j, a in enumerate(g):
            f[k + j] = (f[k + j] - c * a) % P
        while f and not f[-1]:
            f.pop()
    return f


class QuarticField:
    def __init__(self, polynomial):
        self.polynomial = polynomial
        self.one = (1, 0, 0, 0)
        self.theta = (0, 1, 0, 0)
        for degree in (1, 2):
            for low in product(range(P), repeat=degree):
                assert remainder(polynomial, (*low, 1))

    def mul(self, x, y):
        values = [0] * 7
        for i, a in enumerate(x):
            for j, b in enumerate(y):
                values[i + j] = (values[i + j] + a * b) % P
        for k in range(6, 3, -1):
            c = values[k]
            for j in range(4):
                values[k - 4 + j] = (
                    values[k - 4 + j] - c * self.polynomial[j]) % P
        return tuple(values[:4])

    def power(self, x, k):
        result = self.one
        while k:
            if k & 1:
                result = self.mul(result, x)
            x = self.mul(x, x)
            k //= 2
        return result

    def order(self, x):
        assert any(x)
        return next(k for k in (1, 2, 4, 5, 8, 10, 16, 20, 40, 80)
                    if self.power(x, k) == self.one)

    def character_value(self, ell, generators=None):
        u, v = generators or (self.one, self.theta)
        return add(scale(ell[0], u), scale(ell[1], v))

    def relative(self, alpha, beta, generators=None):
        a = self.character_value(alpha, generators)
        b = self.character_value(beta, generators)
        return self.mul(self.power(a, 79), b)


def companion(f):
    c = [[0] * 4 for _ in range(4)]
    for j in range(3):
        c[j + 1][j] = 1
    for i in range(4):
        c[i][3] = -f[i] % P
    return c


def block_form(d):
    n = len(d)
    out = [[0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            out[i][n + j] = d[i][j]
            out[n + j][i] = -d[i][j] % P
    return out


def small_fourier_checks():
    ws = vectors(2)
    a = [[0, 1], [2, 0]]
    b = [[0, 2], [1, 0]]
    t = mm(inverse(a), b)
    assert t == [[2, 0], [0, 2]]
    n = len(ws)
    entries = 0
    for x in ws:
        for z in ws:
            total = [0, 0]
            for y in ws:
                phase = (dot(x, mv(a, y)) + dot(y, mv(b, z))) % P
                for j, value in enumerate(ROOTS[phase]):
                    total[j] += value
            assert tuple(total) == ((n, 0) if x == mv(t, z) else (0, 0))
            entries += 1
    network = {}
    for k in (1, 2):
        total = [0, 0]
        for xs in product(ws, repeat=k):
            for ys in product(ws, repeat=k):
                phase = sum(dot(xs[(i + 1) % k], mv(a, ys[i]))
                            - dot(xs[i], mv(b, ys[i])) for i in range(k)) % P
                for j, value in enumerate(ROOTS[phase]):
                    total[j] += value
        expected = 1 if k == 1 else n
        assert total == [n ** k * expected, 0]
        network[str(k)] = expected

    # Relabel the points themselves, transporting both Fourier kernels and T.
    shuffled = list(range(n))
    Random(323438).shuffle(shuffled)
    index = {x: i for i, x in enumerate(ws)}
    point_t = tuple(index[mv(t, x)] for x in ws)
    relabeled = tuple(shuffled[point_t[shuffled.index(i)]] for i in range(n))
    assert cycle_counts(point_t) == cycle_counts(relabeled) == {1: 1, 2: 4}
    return {"exact_cyclotomic_matrix_entries": entries,
            "cyclic_network_traces": network,
            "network_terms_through_length_two": n ** 2 + n ** 4,
            "relabeling_seed": 323438}


def quartic_controls():
    polynomials = ((2, 1, 0, 0, 1), (2, 0, 1, 0, 1))
    expected_histograms = ({20: 16, 80: 32},
                           {5: 4, 10: 4, 16: 8, 40: 16, 80: 16})
    charges = vectors(2)
    pairs = [(a, b) for a in charges for b in charges if rank([a, b]) == 2]
    assert len(pairs) == 48
    gl2 = [list(map(list, (x[:2], x[2:])))
           for x in product(range(P), repeat=4)
           if (x[0] * x[3] - x[1] * x[2]) % P]
    relabelings, rank_checks, result = 0, 0, []
    for f, expected in zip(polynomials, expected_histograms):
        field = QuarticField(f)
        for x in vectors(4):
            if any(x):
                assert field.power(x, 80) == field.one
                assert field.mul(x, field.power(x, 79)) == field.one
        forms = [block_form(eye(4)), block_form(companion(f))]
        scalar_rank_histogram = Counter(rank(scalar_form(forms, ell))
                                        for ell in charges)
        assert scalar_rank_histogram == {0: 1, 8: 8}
        histogram = Counter()
        for alpha, beta in pairs:
            order = field.order(field.relative(alpha, beta))
            histogram[order] += 1
            a, b = scalar_form(forms, alpha), scalar_form(forms, beta)
            t = mm(inverse(a), b)
            assert mm(transpose(t), a) == mm(a, t) == b
            power = eye(8)
            for k in range(1, 81):
                power = mm(power, t)
                deficiency = rank(madd(power, eye(8), -1))
                assert deficiency == (0 if k % order == 0 else 8)
                assert deficiency % 2 == 0
                rank_checks += 1
        assert histogram == expected
        for change in gl2:
            transformed = Counter(field.order(field.relative(
                mv(change, alpha), mv(change, beta))) for alpha, beta in pairs)
            assert transformed == histogram
            relabelings += 1

        # A simultaneous W-basis change conjugates T, including its orientation.
        s = eye(8)
        s[0][1], s[2][5] = 1, 2
        s[0], s[7] = s[7], s[0]
        s[3] = scale(2, s[3])
        a, b = forms
        aa, bb = mm(mm(transpose(s), a), s), mm(mm(transpose(s), b), s)
        t = mm(inverse(a), b)
        tt = mm(inverse(aa), bb)
        assert tt == mm(mm(inverse(s), t), s)
        ws = vectors(8)
        lookup = {x: i for i, x in enumerate(ws)}
        actual = tuple(lookup[mv(t, x)] for x in ws)
        order = field.order(field.theta)
        expected_cycles = {1: 1, order: 6560 // order}
        assert cycle_counts(actual) == expected_cycles
        result.append({"polynomial_low_to_high": list(f),
                       "distinguished_transfer_order": order,
                       "scalar_rank_histogram": dict(sorted(scalar_rank_histogram.items())),
                       "order_at_alpha11_beta12": field.order(
                           field.relative((1, 1), (1, 2))),
                       "all_48_pair_order_histogram": dict(sorted(histogram.items())),
                       "V_cycle_counts": expected_cycles,
                       "local_class_cycle_counts": {1: 9, order: 6560 // order}})
    assert set(result[0]["all_48_pair_order_histogram"]) != set(
        result[1]["all_48_pair_order_histogram"])
    assert result[1]["order_at_alpha11_beta12"] == 5
    return {"controls": result, "GL2_relabelings_checked": relabelings,
            "self_adjoint_power_rank_checks": rank_checks,
            "class_points_each": 6569,
            "same_entire_fusion_profile": True,
            "group_realization_limit": "Class-two groups; no selected proper-Bol claim"}


def multiply_series(a, b, degree):
    out = [0] * (degree + 1)
    for i, x in enumerate(a[:degree + 1]):
        if x:
            for j, y in enumerate(b[:degree + 1 - i]):
                if y:
                    out[i + j] += x * y
    return out


def odd_mode_series(cycles, degree):
    """Unshifted 24-species trace, directly from the odd-mode determinants."""
    out = [1] + [0] * degree
    for d, number in cycles.items():
        sign = 1 if d % 2 else -1
        exponent = 24 * number
        for m in range(1, degree // d + 1, 2):
            step = m * d
            factor = [0] * (degree + 1)
            for j in range(min(exponent, degree // step) + 1):
                factor[step * j] = comb(exponent, j) * sign ** j
            out = multiply_series(out, factor, degree)
    return out


def divide_series(a, b):
    assert a[0] == b[0] == 1 and len(a) == len(b)
    out = [1] + [0] * (len(a) - 1)
    for n in range(1, len(a)):
        out[n] = a[n] - sum(b[j] * out[n - j] for j in range(1, n + 1))
    return out


def logarithmic_coefficients(series):
    """[q^n] D log(series)/24, computed from the expanded trace."""
    out = [0] * len(series)
    for n in range(1, len(series)):
        value = n * series[n] - 24 * sum(
            out[j] * series[n - j] for j in range(1, n))
        assert value % 24 == 0
        out[n] = value // 24
    return out


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    result, prime = 1, 2
    while prime * prime <= n:
        if n % prime == 0:
            n //= prime
            result = -result
            if n % prime == 0:
                return 0
        prime += 1
    return -result if n > 1 else result


def spectral_extraction(cycles, degree):
    coefficients = logarithmic_coefficients(odd_mode_series(cycles, degree))
    for n in range(1, degree + 1):
        m, power = n, 1
        while m % 2 == 0:
            m //= 2
            power *= 2
        sign = 1 if power == 1 else -1
        recovered = sign * sum(mobius(m // d) * (m // d) * coefficients[power * d]
                               for d in divisors(m))
        actual = fixed_from_cycles(cycles, n)
        assert recovered == actual
        dimension = next(k for k in range(9) if P ** k == actual)
        assert dimension % 2 == 0
    return degree


def analytic_checks():
    first, second = {1: 1, 80: 82}, {1: 1, 16: 410}
    tested = spectral_extraction(first, 80) + spectral_extraction(second, 80)
    tested += spectral_extraction({1: 9, 2: 36}, 16)
    for index in (1, 2):
        a = odd_mode_series({1: 9 * index, 80: 82 * index}, 16)
        b = odd_mode_series({1: 9 * index, 16: 410 * index}, 16)
        quotient = divide_series(a, b)
        assert quotient[:16] == [1] + [0] * 15
        assert quotient[16] == 9840 * index
    return {"exact_logarithmic_inverse_coefficients": tested,
            "first_ratio_term_local": {"degree": 16, "coefficient": 9840},
            "first_ratio_coefficient_at_induced_index_6561": 9840 * 6561,
            "symbolic_ratio": "(Delta(80tau)/Delta(160tau))^(82I) / "
                              "(Delta(16tau)/Delta(32tau))^(410I)",
            "common_group": "Gamma_0(320)"}


def class_seed(forms):
    d, s = len(forms[0]), len(forms)
    ws, zs = vectors(d), vectors(s)
    unit = eye(d)
    images, representatives, classes = {}, {}, []
    for w in ws:
        image = span([pairing(forms, w, v) for v in unit], s)
        images[w] = image
        for z in zs:
            representatives[w, z] = min(add(z, t) for t in image)
        classes.extend((w, z) for z in sorted(
            {representatives[w, z] for z in zs}))
    lookup = {c: i for i, c in enumerate(classes)}
    radicals = {ell: {w for w in ws
                     if all(dot(ell, z) == 0 for z in images[w])} for ell in zs}
    return ws, zs, images, representatives, classes, lookup, radicals


def annihilator_zero(s, r):
    for i in range(len(s)):
        values = Counter({s[r[i]]: 1})
        values[i] += 1
        values[s[i]] -= 1
        values[r[i]] -= 1
        if any(values.values()):
            return False
    return True


def determinant_factor_exponents(cycles):
    """Exact normalized cyclotomic factors for cycle lengths 1,2,3,6."""
    factors = {1: (0, 1, 0, 0), 2: (1, 1, 0, 0),
               3: (0, 1, 0, 1), 6: (1, 1, 1, 1)}
    out = [0] * 4  # 1-t,1+t,1+t+t^2,1-t+t^2
    for d, count in cycles.items():
        for i, exponent in enumerate(factors[d]):
            out[i] += count * exponent
    return out


def four_sector_difference(s, r):
    sr = compose(s, r)
    assert sr == compose(r, s)
    shapes = [cycle_counts(p) for p in
              (sr, tuple(range(len(s))), s, r)]
    exponents = [determinant_factor_exponents(c) for c in shapes]
    difference = [exponents[0][i] + exponents[1][i]
                  - exponents[2][i] - exponents[3][i] for i in range(4)]
    first_coefficient = 24 * (shapes[0].get(1, 0) + len(s)
                              - shapes[2].get(1, 0) - shapes[3].get(1, 0))
    assert (not any(difference)) == annihilator_zero(s, r)
    return shapes, difference, first_coefficient


def rigid_checks():
    b = [
        [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 2, 0, 0]],
        [[0, 0, 0, 2], [0, 1, 1, 0], [0, 1, 0, 0], [2, 0, 0, 0]],
        [[0, 2, 1, 1], [1, 1, 0, 2], [2, 2, 0, 0], [0, 1, 0, 0]],
    ]
    forms = [madd(transpose(a), a, -1) for a in b]  # actual Q commutator
    ws, zs, images, reps, classes, lookup, radicals = class_seed(forms)
    assert len(classes) == 363
    a, bb = forms[2], madd(forms[2], forms[0])
    t = mm(inverse(a), bb)
    assert mm(t, t) == eye(4)
    assert rank(madd(t, eye(4), -1)) == rank(madd(t, eye(4))) == 2
    regular = [ell for ell in zs if rank(scalar_form(forms, ell)) == 4]
    assert len(regular) == 12
    restriction_checks = 0
    for alpha in regular:
        aa = scalar_form(forms, alpha)
        for ell in zs:
            basis_r = basis(sorted(radicals[ell]))
            gram = [[dot(x, mv(aa, y)) for y in basis_r] for x in basis_r]
            assert rank(gram) == len(basis_r)
            restriction_checks += 1

    transfer_histogram = Counter()
    transfer_matrices = {}
    independent_histogram = Counter()
    for alpha in regular:
        for beta in regular:
            transfer = mm(inverse(scalar_form(forms, alpha)),
                          scalar_form(forms, beta))
            key = tuple(tuple(row) for row in transfer)
            transfer_histogram[key] += 1
            transfer_matrices[key] = transfer
            if rank([alpha, beta]) == 2:
                independent_histogram[key] += 1
    assert len(transfer_histogram) == 4
    assert sorted(transfer_histogram.values()) == [36] * 4
    assert sorted(independent_histogram.values()) == [24, 24, 36, 36]

    zero = (0, 0, 0)
    j_u = span([(0, 0, 1)], 3)
    j_v = span([(1, 0, 1)], 3)
    central = {z: tuple(lookup[w, reps[w, add(c, z)]] for w, c in classes)
               for z in zs}
    identity = tuple(range(len(classes)))
    family_locus, all_checks, distinguished = set(), 0, None
    for key, transfer in transfer_matrices.items():
        for ell in zs:
            assert {mv(transfer, w) for w in radicals[ell]} == radicals[ell]
        assert all(images[mv(transfer, w)] == images[w] for w in ws)
        sewing = tuple(lookup[mv(transfer, w), c] for w, c in classes)
        locus = set()
        for z in zs:
            shapes, factors, defect = four_sector_difference(sewing, central[z])
            assert defect == 144 * shapes[0].get(6, 0)
            if not any(factors):
                locus.add(z)
            all_checks += 1
        if transfer != eye(4):
            family_locus |= locus
        if transfer == t:
            assert locus == j_v
            assert cycle_counts(sewing) == {1: 99, 2: 132}
            plus = four_sector_difference(sewing, central[(1, 0, 1)])
            minus = four_sector_difference(sewing, central[(1, 0, 0)])
            assert plus[0][0] == {2: 132, 3: 33} and not any(plus[1])
            assert minus[0][0] == {2: 96, 3: 33, 6: 12}
            assert minus[2] == 1728  # 216*(M-1), M=9.
            distinguished = {"S": cycle_counts(sewing),
                             "S_R_plus": plus[0][0], "S_R_minus": minus[0][0],
                             "plus_exact_determinant_identity": True,
                             "minus_cyclotomic_factor_defect": minus[1],
                             "minus_first_odd_mode_ratio_coefficient": minus[2]}
        elif transfer == [[-v % P for v in row] for row in t]:
            assert locus == j_u
        elif transfer == [[-v % P for v in row] for row in eye(4)]:
            assert locus == {zero}
        else:
            assert transfer == eye(4) and locus == set(zs)
    assert family_locus == j_u | j_v
    assert (1, 0, 1) in family_locus and (1, 0, 0) not in family_locus

    # Canonical BCH origin from S=H intersect P, without an arbitrary section.
    for x in ws:
        central_part = scale(1, pairing(b, x, scale(-1, x)))
        product_center = scale(2, central_part)  # BCH half.
        corrected_center = add(product_center, scale(-2, central_part))
        assert corrected_center == zero
    f = (1, 2, 1)
    t_center = lambda v: (v[0], (v[0] + v[1]) % 3, (v[1] + v[2]) % 3)
    def cocycle_norm(v):
        f2 = add(v, t_center(v))
        f3 = add(f2, t_center(t_center(v)))
        return add(add(f3, f2), scale(-1, v))
    assert cocycle_norm(f) == (1, 0, 1)
    assert cocycle_norm((1, 2, 0)) == (1, 0, 0)

    # Equal positive-cocycle phase flags transform x->x+z.
    common = []
    for ell in regular:
        changed = ((ell[0] + ell[2]) % 3, ell[1], ell[2])
        if changed in regular:
            assert ell[0] == 0 and ell[2] != 0
            common.append(ell)
    assert len(common) == 6
    for alpha in common:
        for beta in common:
            shift = lambda ell: ((ell[0] + ell[2]) % 3, ell[1], ell[2])
            first = mm(inverse(scalar_form(forms, alpha)), scalar_form(forms, beta))
            second = mm(inverse(scalar_form(forms, shift(alpha))),
                        scalar_form(forms, shift(beta)))
            assert first == second
            assert first in (eye(4), [[-v % P for v in row] for row in eye(4)])
    return {"local_points": 363, "nondegenerate_charge_count": 12,
            "ordered_regular_pairs": 144,
            "relative_transfer_multiplicities": [36, 36, 36, 36],
            "independent_pair_multiplicities": [24, 24, 36, 36],
            "nondegenerate_radical_restriction_checks": restriction_checks,
            "central_sector_identity_checks": all_checks,
            "canonical_origin_checks": len(ws),
            "nonidentity_transfer_factorization_locus": sorted(family_locus),
            "distinguished_transfer": distinguished,
            "common_phase_admissible_charges": len(common),
            "common_phase_scalar_transfer_checks": len(common) ** 2,
            "symbolic_large": {
                "M": "3^36", "V_dimension": "M^2", "class_count": "3(M+2)^2",
                "full_transfer_fixed": "9M+18",
                "full_transfer_two_cycles": "3(M^2+M-2)/2",
                "norm_plus_c2_c3_c6": ["3(M^2+M-2)/2", "3M+6", "0"],
                "norm_minus_c2_c3_c6": ["3(M-1)^2/2", "3M+6", "3(M-1)/2"],
                "norm_minus_first_ratio_coefficient": "216 I(M-1)"},
            "scope": "Finite local validation; huge proper-loop hypotheses inherited"}


def twelve_point_ablation():
    s_a = tuple(i ^ 1 if i < 6 else i for i in range(12))
    r_a = tuple(i if i < 6 else 6 + 3 * ((i - 6) // 3) + (i - 6 + 1) % 3
                for i in range(12))
    s_b = tuple((i + 3) % 6 if i < 6 else i for i in range(12))
    r_b = tuple((i + 2) % 6 if i < 6 else i for i in range(12))
    assert cycle_counts(s_a) == cycle_counts(s_b) == {1: 6, 2: 3}
    assert cycle_counts(r_a) == cycle_counts(r_b) == {1: 6, 3: 2}
    first = four_sector_difference(s_a, r_a)
    second = four_sector_difference(s_b, r_b)
    assert first[0][0] == {2: 3, 3: 2} and not any(first[1])
    assert second[0][0] == {1: 6, 6: 1} and second[2] == 144
    source_report = common_current_source_checks(s_a, r_a, s_b, r_b)
    return {"points": 12, "same_individual_cycle_profiles": True,
            "same_faithful_abstract_group_relations": "C2 x C3 = C6",
            "product_profiles": [first[0][0], second[0][0]],
            "factorization_holds": [True, False],
            "failure_first_odd_mode_ratio_coefficient": 144,
            "mode_resolved_source_check": source_report,
            "limit": "Individual spectra agree; full joint group characters do not"}


def source_multiply(a, b):
    """Exact q^0..3 t^0..2 u^0..2 truncation, with rational coefficients."""
    out = Counter()
    for (q, t, u), value in a.items():
        for (qq, tt, uu), other in b.items():
            key = q + qq, t + tt, u + uu
            if key[0] <= 3 and key[1] <= 2 and key[2] <= 2:
                out[key] += value * other
    return {key: value for key, value in out.items() if value}


def source_power(a, exponent):
    out = {(0, 0, 0): Fraction(1)}
    while exponent:
        if exponent & 1:
            out = source_multiply(out, a)
        a = source_multiply(a, a)
        exponent //= 2
    return out


def finite_current_source_trace(permutation, colors_a, colors_b):
    """Direct wedge trace of exp(t E_a^{1,3}) exp(u E_b^{3,1}).

    One species, with the actual positive odd modes 1 and 3.  No other mode
    contributes through energy three.  Intermediate states are retained even
    when their energy exceeds three; only the initial trace state is truncated.
    This intentionally does not use a one-particle determinant or the desired
    common-source factorization.
    """
    n = len(permutation)
    initial = [(0, 0)]
    for count in (1, 2, 3):
        initial.extend((sum(1 << i for i in occupied), count)
                       for occupied in combinations(range(n), count))
    initial.extend((1 << (n + i), 3) for i in range(n))

    def current(state, coefficients, target_mode, source_mode):
        out = Counter()
        for occupied, value in state.items():
            for x, coefficient in enumerate(coefficients):
                source, target = source_mode * n + x, target_mode * n + x
                if not (occupied >> source) & 1:
                    continue
                reduced = occupied ^ (1 << source)
                if (reduced >> target) & 1:
                    continue
                parity = (occupied & ((1 << source) - 1)).bit_count()
                parity += (reduced & ((1 << target) - 1)).bit_count()
                out[reduced | (1 << target)] += (
                    value * coefficient * (-1 if parity % 2 else 1))
        return {key: value for key, value in out.items() if value}

    def permute(occupied):
        images = [(i // n) * n + permutation[i % n]
                  for i in range(2 * n) if (occupied >> i) & 1]
        parity = sum(images[i] > images[j]
                     for i in range(len(images)) for j in range(i + 1, len(images)))
        return sum(1 << i for i in images), (-1 if parity % 2 else 1)

    out = Counter()
    for occupied, energy in initial:
        right = {occupied: 1}
        for u in range(3):
            left = right
            for t in range(3):
                value = 0
                for target, coefficient in left.items():
                    image, sign = permute(target)
                    if image == occupied:
                        value += sign * coefficient
                if value:
                    out[energy, t, u] += Fraction(value, factorial(t) * factorial(u))
                left = current(left, colors_a, 0, 1)
            right = current(right, colors_b, 1, 0)
    return {key: value for key, value in out.items() if value}, len(initial)


def common_current_source_checks(s_a, r_a, s_b, r_b):
    colors_a = tuple(x - 5 for x in range(12))
    colors_b = tuple((x * x + 2) % 7 - 3 for x in range(12))
    identity = tuple(range(12))
    evaluations, nonzero_correlations = 0, []
    for number, (s, r) in enumerate(((s_a, r_a), (s_b, r_b))):
        traces = []
        for permutation in (compose(s, r), identity, s, r):
            one, initial_states = finite_current_source_trace(
                permutation, colors_a, colors_b)
            assert initial_states == 311
            evaluations += 1
            traces.append(source_power(one, 24))
        left, right = source_multiply(traces[0], traces[1]), source_multiply(
            traces[2], traces[3])
        if number == 0:
            assert left == right
            nonzero_correlations = sorted(
                (list(key), str(value)) for key, value in left.items()
                if key[1] and key[2])
            assert nonzero_correlations
        else:
            assert left.get((1, 0, 0), 0) - right.get((1, 0, 0), 0) == 144
    return {"currents": ["E_a^{1,3}", "E_b^{3,1}"],
            "source": "exp(t E_a^{1,3}) exp(u E_b^{3,1})",
            "colors_a": colors_a, "colors_b": colors_b,
            "grade_bound": 3, "each_source_degree_bound": 2,
            "initial_signed_wedge_states_per_trace": initial_states,
            "one_species_trace_evaluations": evaluations,
            "fermion_species": 24,
            "all_36_truncated_coefficients_agree_in_disjoint_control": True,
            "nonzero_mixed_source_coefficients_in_product": nonzero_correlations,
            "overlapping_control_already_fails_at_q": 144}


def main():
    assert __debug__, "Run with assertions enabled"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path,
                        help="Also write the exact JSON report to this path")
    args = parser.parse_args()
    report = {
        "status": "PASS",
        "arithmetic": "Exact F3, F81, integers, rationals, and Z[zeta_3]",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "convention": "A(Tx,y)=B(x,y); F_A F_B^-1=P_T; P_T eta_x=eta_Tx",
        "small_fourier": small_fourier_checks(),
        "quartic_controls": quartic_controls(),
        "analytic_extraction": analytic_checks(),
        "rigid_local_and_symbolic": rigid_checks(),
        "twelve_point_ablation": twelve_point_ablation(),
        "limits": [
            "No huge loop or induced set enumerated",
            "Manual exact execution; no repository CI result claimed",
            "No independent proof of inherited selected-loop or strict-transport interfaces",
            "No claim that generic free-field identities imply the new geometric annihilator",
            "No uniquely Bol analytic mechanism or historical-priority claim",
        ],
    }
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.certificate:
        args.certificate.write_text(encoded)
        summary = {"status": report["status"],
                   "script_sha256": report["script_sha256"],
                   "certificate": str(args.certificate),
                   "quartic_power_rank_checks": 7680,
                   "rigid_central_sector_checks": 108,
                   "mode_resolved_source_coefficients": 36}
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
