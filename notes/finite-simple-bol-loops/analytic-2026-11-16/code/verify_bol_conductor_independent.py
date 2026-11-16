#!/usr/bin/env python3
"""Independent exact finite checks for the conductor continuation.

No authored verifier is imported.  All arithmetic is integral or rational.
The actual level-1/2 Bol checks use F_3[X]/Phi_(7^A), A=1,2.
Central transport checks use the actual sparse trace readout at levels 3,4,5.
These finite checks do not replace the all-level proofs.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import factorial
import json
import random


SEED = 2026111607


class CyclotomicField:
    def __init__(self, level):
        self.level = level
        self.order_root = 7**level
        self.socle = self.order_root // 7
        self.degree = 6 * self.socle
        self.order = 3**self.degree
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)
        # This is an irreducibility certificate for Phi_(7^A) over F_3.
        assert pow(3, self.degree, self.order_root) == 1
        for prime in (2, 3, 7):
            if self.degree % prime == 0:
                assert pow(3, self.degree // prime, self.order_root) != 1
        self.trace_basis = []
        for exponent in range(self.degree):
            a = [0] * self.order_root
            frobenius_exponent = exponent
            for _ in range(self.degree):
                a[frobenius_exponent] += 1
                frobenius_exponent = 3 * frobenius_exponent % self.order_root
            reduced = self.reduce(a)
            assert not any(reduced[1:])
            self.trace_basis.append(reduced[0])

    def reduce(self, a):
        a = list(a)
        assert len(a) == self.order_root
        for residue in range(self.socle):
            top = a[6 * self.socle + residue]
            for j in range(6):
                a[j * self.socle + residue] -= top
        return tuple(x % 3 for x in a[: self.degree])

    def root(self, exponent):
        a = [0] * self.order_root
        a[exponent % self.order_root] = 1
        return self.reduce(a)

    def add(self, a, b):
        return tuple((x + y) % 3 for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple((x - y) % 3 for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x % 3 for x in a)

    def mul(self, a, b):
        result = [0] * self.order_root
        aa = [(i, x) for i, x in enumerate(a) if x]
        bb = [(i, x) for i, x in enumerate(b) if x]
        for i, x in aa:
            for j, y in bb:
                result[(i + j) % self.order_root] += x * y
        return self.reduce(result)

    def mul_root(self, a, exponent):
        result = [0] * self.order_root
        for i, x in enumerate(a):
            result[(i + exponent) % self.order_root] += x
        return self.reduce(result)

    def power(self, a, exponent):
        answer = self.one
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, a)
            a = self.mul(a, a)
            exponent >>= 1
        return answer

    def trace(self, a):
        return sum(x * y for x, y in zip(a, self.trace_basis)) % 3

    def random(self, rng):
        return tuple(rng.randrange(3) for _ in range(self.degree))


def eta_lifts(last):
    result = {1: 2}
    for a in range(2, last + 1):
        previous_modulus = 7 ** (a - 1)
        candidates = [result[a - 1] + j * previous_modulus for j in range(7)]
        roots = [x for x in candidates if (x * x + x + 1) % (7**a) == 0]
        assert len(roots) == 1
        result[a] = roots[0]
    return result


def field_rank(field, matrix):
    a = [list(row) for row in matrix]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(rank, len(a)) if a[j][col] != field.zero), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = field.power(a[rank][col], field.order - 2)
        a[rank] = [field.mul(inverse, x) for x in a[rank]]
        for j in range(len(a)):
            if j != rank and a[j][col] != field.zero:
                scale = a[j][col]
                a[j] = [field.sub(x, field.mul(scale, y)) for x, y in zip(a[j], a[rank])]
        rank += 1
        if rank == min(len(a), len(a[0])):
            break
    return rank


def beta(field, x, y):
    return field.trace(field.sub(field.mul(x[0], y[1]), field.mul(x[1], y[0])))


def circle(field, eta, left, right):
    x, v, a, t = left
    y, w, b, s = right
    n = field.order_root
    return (
        tuple(field.add(xx, field.mul_root(yy, t)) for xx, yy in zip(x, y)),
        tuple((vv + pow(eta, a, n) * ww) % n for vv, ww in zip(v, w)),
        (a + b - beta(field, x, y)) % 3,
        (t + s - v[0] * w[1] + v[1] * w[0]) % n,
    )


def verify_bol_level(field, eta, rng, count=48):
    zero_x = (field.zero, field.zero)
    unit_x = (field.one, field.zero)
    identity = (zero_x, (0, 0), 0, 0)

    def random_state():
        return (
            (field.random(rng), field.random(rng)),
            (rng.randrange(field.order_root), rng.randrange(field.order_root)),
            rng.randrange(3),
            rng.randrange(field.order_root),
        )

    def op(x, y):
        return circle(field, eta, x, y)

    for _ in range(count):
        a, b, c = random_state(), random_state(), random_state()
        assert op(identity, a) == a == op(a, identity)
        assert op(a, op(b, op(a, c))) == op(op(a, op(b, a)), c)
        u, y = a[0], b[0]
        actor, s = rng.randrange(3), rng.randrange(field.order_root)
        U, Y = (u, (0, 0), 0, 0), (y, (0, 0), 0, 0)
        Wa = (zero_x, (pow(eta, actor, field.order_root), 0), 0, 0)
        Zs = (zero_x, (0, 1), 0, s)
        Xe = (unit_x, (0, 0), 0, 0)
        previous = op(op(op(U, Y), Wa), Zs)
        final = op(previous, Xe)
        phase = (s - pow(eta, (actor - beta(field, u, y)) % 3, field.order_root)) % field.order_root
        increment = field.sub(final[0][0], previous[0][0])
        assert increment == field.root(phase)
        expected_trace = 2 if phase and phase % field.socle == 0 else 0
        assert field.trace(increment) == expected_trace
    a, b = (unit_x, (1, 0), 0, 0), (zero_x, (0, 1), 0, 0)
    assert op(op(a, b), a) != op(a, op(b, a))
    return {
        "level": field.level,
        "field_degree": field.degree,
        "central_order": field.order_root,
        "matrix_family": "n=2, k=1, B=[[0,1],[-1,0]]",
        "sampled_Bol_and_actual_two_state_word_cases": count,
        "properness_witness_checked": True,
    }


def verify_trace_geometry(low, high, rng):
    def embed(x):
        a = [0] * high.degree
        for i, c in enumerate(x):
            a[7 * i] = c
        return tuple(a)

    def tau(x):
        return tuple(x[7 * i] for i in range(low.degree))

    for exponent in range(high.degree):
        actual = high.zero
        for j in range(7):
            actual = high.add(actual, high.root(exponent * pow(low.order, j, high.order_root)))
        assert actual == embed(tau(high.root(exponent)))
    for _ in range(64):
        x = (high.random(rng), high.random(rng))
        y = (high.random(rng), high.random(rng))
        x0, y0 = tuple(map(tau, x)), tuple(map(tau, y))
        ex0, ey0 = tuple(map(embed, x0)), tuple(map(embed, y0))
        transverse_x = tuple(high.sub(a, b) for a, b in zip(x, ex0))
        transverse_y = tuple(high.sub(a, b) for a, b in zip(y, ey0))
        assert beta(high, ex0, transverse_y) == beta(high, transverse_x, ey0) == 0
        assert beta(high, x, y) == (beta(low, x0, y0) + beta(high, transverse_x, transverse_y)) % 3
        assert beta(high, ex0, ey0) == beta(low, x0, y0)
    gram = [[tau(high.mul(high.root(i), high.root(j))) for j in range(1, 7)] for i in range(1, 7)]
    expected = [[low.root(1) if i + j == 7 else low.zero for j in range(1, 7)] for i in range(1, 7)]
    assert gram == expected and field_rank(low, gram) == 6
    transverse_form = []
    for i in range(12):
        row = []
        for j in range(12):
            if i < 6 <= j:
                value = gram[i][j - 6]
            elif j < 6 <= i:
                value = low.neg(gram[i - 6][j])
            else:
                value = low.zero
            row.append(value)
        transverse_form.append(row)
    assert field_rank(low, transverse_form) == 12
    kernel_size = low.order**6
    density = Fraction(1, kernel_size**2)
    assert density == Fraction(low.order, high.order) ** 2
    assert density * kernel_size**2 == 1
    # Counts and norms, not enumeration of the enormous transverse space.
    return {
        "relative_trace_basis_elements_checked": high.degree,
        "sampled_orthogonal_trace_splittings": 64,
        "trace_kernel_dimension_over_E1": 6,
        "trace_pairing_rank_on_kernel": 6,
        "transverse_rank_for_rank_two_scalar_form": 12,
        "indicator_density": str(density),
        "normalized_indicator_squared_norm": 1,
        "zero_scalar_sector_density": 1,
    }


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub(x, y):
    return x[0] - y[0], x[1] - y[1]


def conjugate(x):
    return x[0] - x[1], -x[1]


def multiply(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0] - x[1] * y[1]


def squared_norm(x):
    return x[0] ** 2 - x[0] * x[1] + x[1] ** 2


def total(xs):
    answer = (0, 0)
    for x in xs:
        answer = add(answer, x)
    return answer


def histograms(k):
    return [(a, b, k - a - b) for a in range(k + 1) for b in range(k - a + 1)]


def central_vectors(level, k, eta):
    n, shell_step = 7**level, 7 ** (level - 1)
    hist = histograms(k)
    values = [sum(c[j] * pow(eta, j, n) for j in range(3)) % n for c in hist]
    vectors = []
    for value in values:
        shell = {(value + j * shell_step) % n for j in range(1, 7)}
        vectors.append([(-1, -1) if s in shell else (1, 0) for s in range(n)])
    return hist, values, vectors


def vector_combination(coefficients, vectors):
    return [total(multiply(c, v[s]) for c, v in zip(coefficients, vectors)) for s in range(len(vectors[0]))]


def verify_stable_transport(lifts):
    levels, k = (3, 4, 5), 3
    all_vectors = {}
    gram_checks = []
    for level in levels:
        hist, values, vectors = central_vectors(level, k, lifts[level])
        n, m = 7**level, len(hist)
        assert 7 ** (level - 1) > k * k
        assert len(set(x % (n // 7) for x in values)) == m
        for i in range(m):
            for j in range(i, m):
                inner = total(multiply(conjugate(x), y) for x, y in zip(vectors[i], vectors[j]))
                assert inner == (n - 18 + 18 * (i == j), 0)
        all_vectors[level] = vectors
        gram_checks.append({"level": level, "central_points": n, "histograms": m, "exact_Gram_pairs": m * (m + 1) // 2})
    m = len(all_vectors[3])
    coefficient_vectors = []
    for i in range(m - 1):
        z = [(0, 0)] * m
        z[i], z[-1] = (1, 0), (-1, 0)
        coefficient_vectors.append(z)
    z = [(j, j % 3) for j in range(m - 1)]
    last = total(z)
    z.append((-last[0], -last[1]))
    coefficient_vectors.append(z)
    images = {}
    for z in coefficient_vectors:
        assert total(z) == (0, 0)
        for level in levels:
            vectors = all_vectors[level]
            f = vector_combination(z, vectors)
            images[level] = f
            assert sum(map(squared_norm, f)) == 18 * sum(map(squared_norm, z))
            nonzero = [(i, x) for i, x in enumerate(f) if x != (0, 0)]
            moments = [total(multiply(conjugate(v[i]), x) for i, x in nonzero) for v in vectors]
            assert moments == [(18 * a, 18 * b) for a, b in z]
        # In the exact kernel (32), divide out sqrt(m_A*m_B).
        # It maps sum(z_c v_Bc) to (1/m_B) sum(z_c v_Ac).
        # These rational scalings test normalization and equality of norms.
        for a, b in combinations(levels, 2):
            n_a, n_b = 7**a, 7**b
            norm_a = Fraction(sum(map(squared_norm, images[a])), n_a)
            norm_b = Fraction(sum(map(squared_norm, images[b])), n_b)
            assert Fraction(n_a, n_b) * norm_a == norm_b
    # A direct old-conductor projection has strict loss on a histogram difference.
    a, b = 3, 4
    hist, values, _ = central_vectors(b, k, lifts[b])
    left, right = hist.index((3, 0, 0)), hist.index((2, 1, 0))
    f = [sub(x, y) for x, y in zip(all_vectors[b][left], all_vectors[b][right])]
    assert (values[left] - values[right]) % 7 != 0
    fiber_sums = [(0, 0)] * (7**a)
    for s, x in enumerate(f):
        fiber_sums[s % (7**a)] = add(fiber_sums[s % (7**a)], x)
    full_energy = Fraction(sum(map(squared_norm, f)), 7**b)
    projected_energy = Fraction(sum(map(squared_norm, fiber_sums)), 7**a * 7**2)
    assert projected_energy / full_energy == Fraction(6, 7)
    # Preserve an actual failed separation at level 2.
    hist2, values2, vectors2 = central_vectors(2, 3, lifts[2])
    collision = next((i, j) for i, j in combinations(range(len(hist2)), 2) if values2[i] % 7 == values2[j] % 7)
    i, j = collision
    inner = total(multiply(conjugate(x), y) for x, y in zip(vectors2[i], vectors2[j]))
    assert inner != (49 - 18, 0)
    return {
        "stable_actual_shift_Gram_checks": gram_checks,
        "zero_sum_coefficient_basis_and_extra_vectors_checked": len(coefficient_vectors),
        "adjoint_moments_equal_18_times_coefficients": True,
        "normalized_transport_energy_equalities_checked": 3 * len(coefficient_vectors),
        "old_projection_energy_fraction_on_unit_phase_difference": str(projected_energy / full_energy),
        "unstable_level_2_histograms": [hist2[i], hist2[j]],
        "unstable_Gram_numerator": inner,
    }


def moment(ell):
    numerator = 0
    for h in histograms(ell):
        coefficient = factorial(ell)
        for a in h:
            coefficient //= factorial(a)
        numerator += coefficient**2
    return Fraction(numerator, 3 ** (2 * ell))


def verify_histogram_weights(k):
    labels = list(product(range(3), repeat=k))
    buckets = defaultdict(list)
    for x in labels:
        buckets[tuple(x.count(j) for j in range(3))].append(x)
    numerators = {}
    for nu in labels:
        numerator = 0
        for bucket in buckets.values():
            counts = Counter(sum(a * b for a, b in zip(nu, x)) % 3 for x in bucket)
            numerator += squared_norm((counts[0] - counts[2], counts[1] - counts[2]))
        numerators[nu] = numerator
    denominator = 3 ** (2 * k)
    assert sum(numerators.values()) == denominator
    zero = (0,) * k
    assert Fraction(numerators[zero], denominator) == moment(k)
    # Enumerate planes by pairs of projective points, not an RREF generator.
    representatives = [x for x in labels if any(x) and next(a for a in x if a) == 1]
    planes = set()
    for x, y in combinations(representatives, 2):
        plane = tuple(sorted(tuple((s * a + t * b) % 3 for a, b in zip(x, y)) for s, t in product(range(3), repeat=2)))
        assert len(set(plane)) == 9
        planes.add(plane)
    expected_count = (3**k - 1) * (3**k - 3) // 48
    assert len(planes) == expected_count
    maximum = max(sum(numerators[x] for x in plane) for plane in planes)
    assert Fraction(maximum, denominator) == 3 * moment(k - 1)
    good = Fraction(maximum - numerators[zero], denominator)
    aligned = 1 - moment(k)
    return {
        "k": k,
        "all_character_weights_checked": len(labels),
        "all_parameter_two_planes_checked": len(planes),
        "exact_maximum_plane_mass": str(Fraction(maximum, denominator)),
        "exact_nonzero_spread_mass": str(good),
        "exact_nonzero_aligned_mass": str(aligned),
        "exact_squared_norm_ratio": str(good / aligned),
    }


def main():
    rng = random.Random(SEED)
    fields = [CyclotomicField(1), CyclotomicField(2)]
    lifts = eta_lifts(5)
    result = {
        "arithmetic": "Independent standard-library exact characteristic-three and Eisenstein/rational arithmetic.",
        "seed": SEED,
        "actual_Bol_tower": [verify_bol_level(f, lifts[f.level], rng) for f in fields],
        "trace_geometry": verify_trace_geometry(*fields, rng),
        "central_transport": verify_stable_transport(lifts),
        "histogram_mass": [verify_histogram_weights(k) for k in (3, 5)],
        "limits": "Finite levels and selected matrices only. No full huge vector operator, all-level theorem, direct-limit construction, or asymptotic theorem is proved by these tests.",
        "status": "PASS",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

