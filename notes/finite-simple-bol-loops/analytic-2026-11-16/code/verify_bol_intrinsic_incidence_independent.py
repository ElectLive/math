#!/usr/bin/env python3
"""Independent h=1 incidence, AQ.27--29 multiplicity and relabeling checks.

Standard library only. No authored verifier or spectral-table implementation
is imported. Field-image intersections are calculated from actual 6 by 6
matrices over F_3[lambda]/(1+lambda+...+lambda^6). The regular loop table is
not enumerated. AQ.29 is a mathematical input; its orbit-label aggregation
is checked against the proposed compressed table.
"""

from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import comb
import json

Q, K, N, DIM = 729, 3, 27, 6
W = Q**DIM
R = F(1, Q**4)


@lru_cache(None)
def digits(x):
    return tuple((x // 3**i) % 3 for i in range(6))


def pack(xs):
    return sum((x % 3) * 3**i for i, x in enumerate(xs))


@lru_cache(None)
def add(x, y):
    return pack(a + b for a, b in zip(digits(x), digits(y)))


@lru_cache(None)
def neg(x):
    return pack(-a for a in digits(x))


@lru_cache(None)
def mul(x, y):
    if not x or not y:
        return 0
    out = [0] * 11
    for i, a in enumerate(digits(x)):
        for j, b in enumerate(digits(y)):
            out[i + j] += a * b
    for j in range(10, 5, -1):
        coefficient = out[j] % 3
        out[j] = 0
        for i in range(6):
            out[j - 6 + i] -= coefficient
    return pack(out[:6])


def power(x, n):
    answer = 1
    while n:
        if n & 1:
            answer = mul(answer, x)
        x = mul(x, x)
        n >>= 1
    return answer


@lru_cache(None)
def inverse(x):
    assert x
    answer = power(x, 727)
    assert mul(x, answer) == 1
    return answer


def trace(x):
    answer = 0
    for _ in range(6):
        answer = add(answer, x)
        x = power(x, 3)
    assert answer in (0, 1, 2)
    return answer


def rank(matrix, prime=False):
    rows = [list(row) for row in matrix]
    plus = (lambda a, b: (a + b) % 3) if prime else add
    minus = (lambda a: -a % 3) if prime else neg
    times = (lambda a, b: a * b % 3) if prime else mul
    inv = (lambda a: a) if prime else inverse
    pivot_row = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = inv(rows[pivot_row][col])
        rows[pivot_row] = [times(scale, a) for a in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row and rows[i][col]:
                factor = rows[i][col]
                rows[i] = [plus(a, minus(times(factor, b)))
                           for a, b in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


PARAMETERS = tuple(product(range(3), repeat=K))
ZERO = (0,) * K


def matrix(nu, family):
    t = sum(nu[i] * 3**i for i in range(K))
    out = [[0] * DIM for _ in range(DIM)]
    if family == "spread":
        z = (t, power(t, 3), power(t, 9))
        for offset in (0, 3):
            for i, j, remaining, sign in ((0, 1, 2, 1), (0, 2, 1, 2), (1, 2, 0, 1)):
                value = mul(sign, z[remaining])
                out[offset + i][offset + j] = value
                out[offset + j][offset + i] = neg(value)
    else:
        for i, value in enumerate(nu):
            out[0][i + 1], out[i + 1][0] = value, neg(value)
        out[4][5], out[5][4] = t, neg(t)
    return out


def incidence_counts(family):
    matrices = {nu: matrix(nu, family) for nu in PARAMETERS}
    ranks = {nu: rank(b) for nu, b in matrices.items()}
    assert Counter(ranks.values()) == {0: 1, 4: 26}
    assert rank([row for b in matrices.values() for row in b]) == DIM
    histogram, dimensions = Counter(), {}
    counts = {}
    for alpha, nu in product(PARAMETERS, repeat=2):
        concat = [a + b for a, b in zip(matrices[alpha], matrices[nu])]
        intersection = ranks[alpha] + ranks[nu] - rank(concat)
        if alpha == ZERO or nu == ZERO:
            expected = 0
        elif nu in (alpha, tuple(2 * a % 3 for a in alpha)):
            expected = 4
        else:
            expected = 2 if family == "spread" else 3
        assert intersection == expected, (family, alpha, nu, intersection)
        histogram[intersection] += 1
        dimension = DIM - ranks[nu] + intersection
        dimensions[(alpha, nu)] = dimension
        counts[(alpha, nu)] = Q**dimension
    expected_histogram = {0: 53, 4: 52, (2 if family == "spread" else 3): 624}
    assert dict(histogram) == expected_histogram
    return ranks, counts, dict(sorted(histogram.items()))


def actual_plane_orbits():
    unseen = set(product(range(7), repeat=2))
    orbit_sizes = Counter()
    while unseen:
        start = min(unseen)
        orbit = {tuple(pow(2, a, 7) * x % 7 for x in start) for a in range(3)}
        assert orbit <= unseen
        unseen.difference_update(orbit)
        orbit_sizes[len(orbit)] += 1
    assert orbit_sizes == {1: 1, 3: 16}
    return orbit_sizes[3]


def source_spectrum(ranks, counts, nonzero_plane_orbits):
    """Enumerate AQ labels, using matrix-derived W-compatible counts."""
    spectrum = defaultdict(int)
    sector_dimensions = defaultdict(int)
    contributions = 0
    for support in product((0, 1), repeat=K):
        active = sum(support)
        v_orbits = nonzero_plane_orbits**active
        for alpha in PARAMETERS:
            if any(a and not s for a, s in zip(alpha, support)):
                continue
            rank_factor = F(1, Q**ranks[alpha])
            for nu in PARAMETERS:
                compatible = counts[(alpha, nu)]
                assert (compatible - 1) % 7 == (W - compatible) % 7 == 0
                for rho in range(7):
                    # w=0: one W orbit, only sigma=0.
                    ring_factor = F(1, 9**active) if rho else F(1)
                    spectrum[rank_factor * ring_factor] += v_orbits
                    sector_dimensions[(nu, rho)] += v_orbits
                    contributions += 1
                    # w!=0: every scalar orbit has seven vectors.
                    for sigma in range(7):
                        ring_factor = F(1, 49**K) if sigma else (F(1, 9**active) if rho else F(1))
                        for vector_count, loss in ((compatible - 1, 1), (W - compatible, 49)):
                            multiplicity = v_orbits * (vector_count // 7)
                            spectrum[rank_factor * ring_factor / loss] += multiplicity
                            sector_dimensions[(nu, rho)] += multiplicity
                            contributions += 1
    assert len(sector_dimensions) == 7 * N
    assert set(sector_dimensions.values()) == {W * 49**K}
    return {e: m for e, m in spectrum.items() if m}, contributions


def compressed_spectrum(family):
    x = Q**4 if family == "spread" else Q**5
    small_radical = Q**2
    a0 = (W - 1 + (N - 1) * (small_radical - 1)) // 7
    b0 = (N - 1) * (W - small_radical) // 7
    a1 = (3 * (W - 1) + (N - 3) * (x - 1)) // 7
    b1 = (N - 3) * (W - x) // 7
    answer = defaultdict(int)
    for j in range(K + 1):
        c = comb(K, j) * 16**j
        zero_base = [(F(1), N), (R, N * (3**j - 1))]
        nonzero_base = [(F(1), a0), (F(1, 49), b0),
                        (R, (3**j - 1) * a1), (R / 49, (3**j - 1) * b1)]
        for bases, rings in ((zero_base, [(F(1), 1), (F(1, 9**j), 6)]),
                             (nonzero_base, [(F(1), 1), (F(1, 9**j), 6), (F(1, 49**K), 42)])):
            for (value, count), (factor, choices) in product(bases, rings):
                answer[value * factor] += c * count * choices
    return {e: m for e, m in answer.items() if m}


def moment(spectrum, exponent):
    return sum(m * e**exponent for e, m in spectrum.items())


def moment_difference(exponent):
    s = F(1, 49**exponent)
    ring = (1 + 42 * F(1, 49**(K * exponent))) * (49**K - 17**K)
    ring += 6 * ((1 + 48 * F(1, 9**exponent))**K - (1 + 16 * F(1, 9**exponent))**K)
    return F((N - 3) * (Q**5 - Q**4), 7) * R**exponent * (1 - s) * ring


def finite_loop_controls():
    original = [[0, 1, 2, 3, 4], [1, 0, 3, 4, 2], [2, 3, 4, 0, 1],
                [3, 4, 1, 2, 0], [4, 2, 0, 1, 3]]
    def matrices(table):
        n = len(table)
        assert all(sorted(row) == list(range(n)) for row in table)
        assert all(sorted(col) == list(range(n)) for col in zip(*table))
        a, m = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
        associating = 0
        for x, y in product(range(n), repeat=2):
            xy = table[x][y]
            defect = [table[xy].index(table[x][table[y][z]]) for z in range(n)]
            for z in range(n):
                a[defect[z]][z] += 1
                associating += table[x][table[y][z]] == table[xy][z]
            for t in range(n):
                for z in range(n):
                    end = table[t].index(defect[table[t][z]])
                    m[end][z] += 1
        assert sum(a[i][i] for i in range(n)) == associating
        assert sum(m[i][i] for i in range(n)) == n * associating
        return a, m, associating
    a, m, associating = matrices(original)
    phi = [2, 4, 1, 0, 3]
    relabeled = [[0] * 5 for _ in range(5)]
    for x, y in product(range(5), repeat=2):
        relabeled[phi[x]][phi[y]] = phi[original[x][y]]
    ap, mp, countp = matrices(relabeled)
    assert countp == associating
    assert all(ap[phi[y]][phi[x]] == a[y][x] and mp[phi[y]][phi[x]] == m[y][x]
               for x, y in product(range(5), repeat=2))
    group = [[(i + j) % 3 for j in range(3)] for i in range(3)]
    assert matrices(group)[2] == 27
    return {"order_five_associating_triples": associating,
            "order_five_total_triples": 125, "arbitrary_relabeling_checked": phi,
            "cyclic_group_associating_triples": 27}


def main():
    assert power(3, 7) == 1 and 3 != 1
    for a in range(1, Q):
        assert mul(a, inverse(a)) == 1
    pairing = [[trace(mul(3**i, 3**j)) for j in range(6)] for i in range(6)]
    assert trace(1) == 0 and rank(pairing, prime=True) == 6
    plane_orbits = actual_plane_orbits()
    # Independently enumerate the order-seven scalar action on one E line.
    unseen, scalar_sizes = set(range(Q)), Counter()
    while unseen:
        a = min(unseen)
        orbit = {mul(power(3, t), a) for t in range(7)}
        assert orbit <= unseen
        unseen -= orbit
        scalar_sizes[len(orbit)] += 1
    assert scalar_sizes == {1: 1, 7: 104}
    output, spectra = {}, {}
    for family in ("spread", "aligned"):
        ranks, counts, histogram = incidence_counts(family)
        spectrum, contributions = source_spectrum(ranks, counts, plane_orbits)
        assert spectrum == compressed_spectrum(family)
        spectra[family] = spectrum
        assert sum(spectrum.values()) == 7 * N * W * 49**K
        assert max(e for e in spectrum if e != 1) == F(1, 9)
        assert min(e for e in spectrum if e > R) >= F(1, 49**(K + 1)) > R
        low = {e: m for e, m in spectrum.items() if e <= R}
        assert sum(low.values()) == 7 * N * W * (49**K - 17**K)
        x = Q**4 if family == "spread" else Q**5
        top = (49**K - 17**K) * (3 * W + (N - 3) * x + 6 * N) // 7
        assert low[R] == top
        assert max(e / R for e in low if e != R) == F(1, 9)
        canonical = [(str(e), spectrum[e]) for e in sorted(spectrum)]
        output[family] = {"ordered_parameter_pairs": N**2, "intersection_histogram": histogram,
                          "distinct_eigenvalues": len(spectrum), "eigenvalue_multiset_sha256": sha256(json.dumps(canonical,separators=(",", ":")).encode()).hexdigest(),
                          "source_label_contributions": contributions, "total_dimension": sum(spectrum.values()),
                          "fixed_dimension": spectrum[F(1)], "low_dimension": sum(low.values()),
                          "low_top_multiplicity": top, "trace": str(moment(spectrum, 1))}
    assert spectra["spread"][F(1)] == spectra["aligned"][F(1)]
    for exponent in (1, 2, 3, 4):
        difference = moment(spectra["aligned"], exponent) - moment(spectra["spread"], exponent)
        assert difference == moment_difference(exponent) > 0
    output["controls"] = finite_loop_controls()
    output["trace_difference"] = str(moment_difference(1))
    output["absolute_trace_pairing_rank"] = rank(pairing, prime=True)
    output["trace_of_one"] = trace(1)
    output["scalar_orbit_sizes"] = dict(scalar_sizes)
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

