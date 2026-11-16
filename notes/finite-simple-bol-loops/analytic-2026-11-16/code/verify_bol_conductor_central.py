#!/usr/bin/env python3
"""Reproducible exact central-conductor and stabilized-histogram checks.

Run from any directory. This single file supplies exact cyclotomic trace,
finite Gram, histogram, all-plane and stable correspondence checks.
It does not implement the separate vector coisometry.
"""

import itertools
import json
import math
from collections import Counter
from fractions import Fraction

import numpy as np

def reduce_cyclotomic(coefficients, N, characteristic=None):
    """Reduce modulo Phi_(7^A)=sum_(j=0)^6 X^(j*N/7)."""
    a = np.array(coefficients, dtype=np.int64, copy=True)
    assert len(a) == N
    m = N // 7
    top = a[6 * m : 7 * m].copy()
    for j in range(6):
        a[j * m : (j + 1) * m] -= top
    a[6 * m :] = 0
    if characteristic:
        a %= characteristic
    return a[: 6 * m]


def monomial(exponent, N):
    a = np.zeros(N, dtype=np.int64)
    a[exponent % N] = 1
    return a


def conductor(rho, A):
    if not rho:
        return 0
    valuation = 0
    while rho % 7 == 0:
        valuation += 1
        rho //= 7
    return A - valuation


def socle_defect(A):
    N = 7**A
    d = np.zeros(N, dtype=np.int64)
    for j in range(1, 7):
        d[j * (N // 7)] = 1
    return d


def verify_level(A):
    N = 7**A
    degree = 6 * 7 ** (A - 1)
    assert pow(3, degree, N) == 1
    for prime in (2, 3, 7):
        if degree % prime == 0:
            assert pow(3, degree // prime, N) != 1
    frobenius = []
    exponent = 1
    for _ in range(degree):
        frobenius.append(exponent)
        exponent = 3 * exponent % N
    assert exponent == 1 and len(set(frobenius)) == degree
    assert set(frobenius) == {a for a in range(N) if a % 7}
    frobenius = np.array(frobenius, dtype=np.int64)
    defect = socle_defect(A)
    trace_values = []
    for t in range(N):
        coefficients = np.zeros(N, dtype=np.int64)
        np.add.at(coefficients, (t * frobenius) % N, 1)
        value = reduce_cyclotomic(coefficients, N, 3)
        assert not np.any(value[1:])
        expected = 2 * int(defect[t])
        assert int(value[0]) == expected
        trace_values.append(expected)

    relative_trace_checked = 0
    if A >= 2:
        lower_degree = degree // 7
        q_lower_mod_N = pow(3, lower_degree, N)
        galois = [pow(q_lower_mod_N, j, N) for j in range(7)]
        assert len(set(galois)) == 7
        for t in range(N):
            coefficients = np.zeros(N, dtype=np.int64)
            np.add.at(coefficients, (t * np.array(galois)) % N, 1)
            actual = reduce_cyclotomic(coefficients, N, 3)
            expected = (
                reduce_cyclotomic(monomial(t, N), N, 3)
                if t % 7 == 0
                else np.zeros(degree, dtype=np.int64)
            )
            assert np.array_equal(actual, expected)
            relative_trace_checked += 1

    # theta(t)=1+c*d(t), c=omega^2-1=-2-omega.  Represent coefficients
    # in Q(omega) by the pair of integer polynomials in 1 and omega.
    theta_real = 1 - 2 * defect
    theta_omega = -defect
    t_values = np.arange(N, dtype=np.int64)
    sector_counts = {}
    sector_weight_totals = {}
    for rho in range(N):
        exponents = (-rho * t_values) % N
        polynomial_real = np.zeros(N, dtype=np.int64)
        polynomial_omega = np.zeros(N, dtype=np.int64)
        np.add.at(polynomial_real, exponents, theta_real)
        np.add.at(polynomial_omega, exponents, theta_omega)
        result_real = reduce_cyclotomic(polynomial_real, N)
        result_omega = reduce_cyclotomic(polynomial_omega, N)
        assert not np.any(result_real[1:]) and not np.any(result_omega[1:])
        ramanujan = 6 if rho % 7 == 0 else -1
        a = (N if rho == 0 else 0) - 2 * ramanujan
        b = -ramanujan
        assert int(result_real[0]) == a and int(result_omega[0]) == b
        weight = Fraction(a * a - a * b + b * b, N * N)
        c = conductor(rho, A)
        sector_counts[c] = sector_counts.get(c, 0) + 1
        sector_weight_totals[c] = sector_weight_totals.get(c, Fraction(0)) + weight
        expected = (
            Fraction(N * N - 18 * N + 108, N * N)
            if rho == 0
            else Fraction(108 if rho % 7 == 0 else 3, N * N)
        )
        assert weight == expected
    assert sum(sector_weight_totals.values()) == 1
    for c in range(A + 1):
        expected_count = 1 if c == 0 else 6 * 7 ** (c - 1)
        assert sector_counts[c] == expected_count

    # Exact autocorrelation intersection counts; these imply the two-scale
    # collision Gram identity in the proof note.
    overlap = np.zeros(N, dtype=np.int64)
    for s in np.flatnonzero(defect):
        overlap += defect[(s + t_values) % N]
    expected_overlap = 5 * defect
    expected_overlap[0] = 6
    assert np.array_equal(overlap, expected_overlap)

    return {
        "A": A,
        "central_order": N,
        "field_degree_over_F3": degree,
        "absolute_trace_powers_checked": N,
        "relative_trace_powers_checked": relative_trace_checked,
        "fourier_coefficients_checked_by_exact_cyclotomic_reduction": N,
        "trace_zero_count": N - 6,
        "trace_two_count": 6,
        "zero_character_weight": str(sector_weight_totals[0]),
        "theta_variance": str(Fraction(18 * (N - 6), N * N)),
        "characters_per_conductor": sector_counts,
        "total_fourier_weight_per_conductor": {
            c: str(value) for c, value in sector_weight_totals.items()
        },
        "autocorrelation_overlap_formula_checked": True,
    }


def eta_lifts(max_A):
    lifts = {1: 2}
    for A in range(1, max_A):
        N, eta = 7**A, lifts[A]
        candidates = [eta + j * N for j in range(7)]
        roots = [a for a in candidates if (a * a + a + 1) % (7 * N) == 0]
        assert len(roots) == 1
        lifts[A + 1] = roots[0]
    for A, eta in lifts.items():
        assert eta % 7 == 2 and pow(eta, 3, 7**A) == 1
    return lifts


def M_numerator(f, A):
    """Six times the positive Markov operator M_A."""
    N = 7**A
    return sum(np.roll(f, j * (N // 7)) for j in range(1, 7))


def verify_tower(max_A=4):
    checks = []
    lifts = eta_lifts(max_A)
    for A in range(1, max_A):
        N = 7**A
        lower_defect = socle_defect(A)
        for B in range(A + 1, max_A + 1):
            larger = 7**B
            index = larger // N
            upper_defect = socle_defect(B)
            fiber_sum = upper_defect.reshape(index, N).sum(axis=0)
            expected_fiber_sum = np.zeros(N, dtype=np.int64)
            expected_fiber_sum[0] = 6
            assert np.array_equal(fiber_sum, expected_fiber_sum)
            assert np.array_equal(M_numerator(fiber_sum, A), 6 * lower_defect)
            checks.append(
                {
                    "lower_A": A,
                    "upper_B": B,
                    "index": index,
                    "positive_kernel_defect_transfer_factor": f"1/{index}",
                    "upper_primitive_and_other_discarded_character_count": larger - N,
                    "retained_singular_value_1_multiplicity": N // 7,
                    "retained_singular_value_1_over_6_multiplicity": 6 * N // 7,
                }
            )
        # Exact subgroup-induction identity d_(A+1)(7s)=d_A(s), zero off 7C.
        next_defect = socle_defect(A + 1)
        induced = np.zeros(7 * N, dtype=np.int64)
        induced[::7] = lower_defect
        assert np.array_equal(next_defect, induced)

    phase_checks = []
    for A in range(1, max_A):
        N, upper_N = 7**A, 7 ** (A + 1)
        for k in (1, 3, 5):
            shifts = set()
            for labels in itertools.product(range(3), repeat=k):
                upper_shift = sum(pow(lifts[A + 1], a, upper_N) for a in labels) % upper_N
                lower_shift = sum(pow(lifts[A], a, N) for a in labels) % N
                assert upper_shift % N == lower_shift
                shifts.add((lower_shift, upper_shift))
            for lower_shift, upper_shift in shifts:
                upper = np.roll(socle_defect(A + 1), upper_shift)
                fiber_sum = upper.reshape(7, N).sum(axis=0)
                actual_numerator = M_numerator(fiber_sum, A)
                expected_numerator = 6 * np.roll(socle_defect(A), lower_shift)
                assert np.array_equal(actual_numerator, expected_numerator)
            phase_checks.append(
                {
                    "A": A,
                    "parameter_dimension": k,
                    "all_label_tuples_checked": 3**k,
                    "distinct_section_phase_shifts_checked": len(shifts),
                    "all_lower_central_positions_checked": N,
                }
            )
    return {
        "compatible_eta_lifts": lifts,
        "all_consecutive_and_nonconsecutive_central_transfers": checks,
        "actual_eta_section_phase_compatibility": phase_checks,
    }




BASELINE_SCIENTIFIC_PIN = "ab2af8ae4f8437ca9451bb71a1bc66592daa57ce"
BASELINE_DELIVERY_PIN = "d6edc4f86ae6ff7fc5216afa1565958abac4418c"


def histograms(k):
    return [(a, b, k - a - b) for a in range(k + 1) for b in range(k - a + 1)]


def multinomial(h):
    result = math.factorial(sum(h))
    for count in h:
        result //= math.factorial(count)
    return result


def collision_moment(ell):
    numerator = sum(multinomial(h) ** 2 for h in histograms(ell))
    return Fraction(numerator, 3 ** (2 * ell))


def rref_planes(k):
    for pivots in itertools.combinations(range(k), 2):
        positions = [
            (i, j)
            for i, pivot in enumerate(pivots)
            for j in range(pivot + 1, k)
            if j not in pivots
        ]
        for values in itertools.product(range(3), repeat=len(positions)):
            rows = [[0] * k for _ in range(2)]
            for i, pivot in enumerate(pivots):
                rows[i][pivot] = 1
            for (i, j), value in zip(positions, values):
                rows[i][j] = value
            yield rows


def plane_points(rows):
    return [
        tuple((s * x + t * y) % 3 for x, y in zip(*rows))
        for s, t in itertools.product(range(3), repeat=2)
    ]


def histogram_weights(k):
    labels = list(itertools.product(range(3), repeat=k))
    array = np.array(labels, dtype=np.int64)
    hist = [tuple(label.count(a) for a in range(3)) for label in labels]
    hist_set = histograms(k)
    phases = (-array @ array.T) % 3
    numerators = np.zeros(len(labels), dtype=np.int64)
    for h in hist_set:
        indices = [i for i, current in enumerate(hist) if current == h]
        counts = [(phases[:, indices] == a).sum(axis=1) for a in range(3)]
        # Sum of omega^phase is (count0-count2)+(count1-count2)*omega.
        a, b = counts[0] - counts[2], counts[1] - counts[2]
        numerators += a * a - a * b + b * b
    denominator = 3 ** (2 * k)
    assert int(numerators.sum()) == denominator
    assert Fraction(int(numerators[0]), denominator) == collision_moment(k)
    lookup = {label: int(value) for label, value in zip(labels, numerators)}
    masses = Counter()
    max_mass = -1
    max_planes = 0
    number_planes = 0
    seen = set()
    for rows in rref_planes(k):
        points = plane_points(rows)
        key = tuple(sorted(points))
        assert key not in seen and len(set(points)) == 9
        seen.add(key)
        mass = sum(lookup[point] for point in points)
        masses[mass - lookup[(0,) * k]] += 1
        number_planes += 1
        if mass > max_mass:
            max_mass, max_planes = mass, 1
        elif mass == max_mass:
            max_planes += 1
    expected_planes = ((3**k - 1) * (3**k - 3)) // 48
    assert number_planes == expected_planes
    assert Fraction(max_mass, denominator) == 3 * collision_moment(k - 1)
    assert 3 * collision_moment(k - 1) >= collision_moment(k - 2)
    repeated_plane = [[1] * (k - 1) + [0], [0] * (k - 1) + [1]]
    coordinate_plane = [[1] + [0] * (k - 1), [0, 1] + [0] * (k - 2)]
    assert sum(lookup[p] for p in plane_points(repeated_plane)) == max_mass
    coordinate_mass = sum(lookup[p] for p in plane_points(coordinate_plane))
    assert Fraction(coordinate_mass, denominator) == collision_moment(k - 2)
    good = Fraction(max_mass - int(numerators[0]), denominator)
    aligned = 1 - collision_moment(k)
    if k == 3:
        assert Counter(map(int, numerators)) == {93: 3, 12: 6, 21: 18}
        assert masses == {150: 9, 258: 1, 312: 3}
        assert good == Fraction(104, 243) and aligned == Fraction(212, 243)
    return {
        "labels": labels,
        "label_array": array,
        "label_histograms": hist,
        "histogram_set": hist_set,
        "numerators": numerators,
        "denominator": denominator,
        "summary": {
            "k": k,
            "all_character_labels_checked": len(labels),
            "histogram_count": len(hist_set),
            "common_weight_denominator": denominator,
            "weight_numerator_multiplicities": dict(sorted(Counter(map(int, numerators)).items())),
            "all_two_planes_checked": number_planes,
            "maximizing_planes": max_planes,
            "exact_maximum_plane_mass": str(Fraction(max_mass, denominator)),
            "exact_coordinate_plane_mass": str(Fraction(coordinate_mass, denominator)),
            "exact_good_nonzero_image_mass": str(good),
            "exact_aligned_nonzero_image_mass": str(aligned),
            "exact_good_over_aligned_squared_norm_ratio": str(good / aligned),
            "nonzero_plane_mass_numerator_multiplicities": dict(sorted(masses.items())),
        },
    }


def verify_stable_level(A, k, weight_data, eta):
    N, lower_N = 7**A, 7 ** (A - 1)
    hs = weight_data["histogram_set"]
    values = [sum(h[j] * pow(eta, j, N) for j in range(3)) % N for h in hs]
    assert len(set(v % lower_N for v in values)) == len(hs)
    assert lower_N > k * k
    maximum_norm_divided_by_three = 0
    for left, right in itertools.product(hs, repeat=2):
        d = [left[j] - right[j] for j in range(3)]
        assert sum(d) == 0
        x, y = d[0] - d[2], d[1] - d[2]
        eisenstein_norm = x * x - x * y + y * y
        norm_divided = d[0] * d[0] + d[0] * d[1] + d[1] * d[1]
        assert eisenstein_norm == 3 * norm_divided
        assert 0 <= norm_divided <= k * k
        maximum_norm_divided_by_three = max(maximum_norm_divided_by_three, norm_divided)

    # The exact center inner product of two translated theta functions,
    # multiplied by N, is N-18+3*(socle support intersection count).
    def central_gram_numerator(delta):
        if delta % N == 0:
            overlap = 6
        elif delta % lower_N == 0:
            overlap = 5
        else:
            overlap = 0
        return N - 18 + 3 * overlap

    M = len(hs)
    histogram_gram = np.array(
        [[central_gram_numerator(x - y) for y in values] for x in values],
        dtype=np.int64,
    )
    expected = (N - 18) * np.ones((M, M), dtype=np.int64) + 18 * np.eye(M, dtype=np.int64)
    assert np.array_equal(histogram_gram, expected)
    # M*P is integral, where P projects onto histogram coefficients of sum0.
    projection_numerator = M * np.eye(M, dtype=np.int64) - np.ones((M, M), dtype=np.int64)
    assert np.array_equal(
        projection_numerator @ histogram_gram @ projection_numerator,
        18 * M * projection_numerator,
    )

    # Compute every aggregate character weight directly from the finite
    # central Gram, before invoking the stabilized histogram formula.
    labels = weight_data["labels"]
    array = weight_data["label_array"]
    hist_to_value = dict(zip(hs, values))
    phase_values = [hist_to_value[h] for h in weight_data["label_histograms"]]
    raw_gram = np.array(
        [[central_gram_numerator(x - y) for y in phase_values] for x in phase_values],
        dtype=np.int64,
    )
    denominator = weight_data["denominator"]
    for index, nu in enumerate(array):
        phase = (-array @ nu) % 3
        phase_difference = (phase[:, None] - phase[None, :]) % 3
        sums = [int(raw_gram[phase_difference == j].sum()) for j in range(3)]
        real, omega = sums[0] - sums[2], sums[1] - sums[2]
        expected_real = 18 * int(weight_data["numerators"][index])
        if index == 0:
            expected_real += (N - 18) * denominator
        assert omega == 0 and real == expected_real
    Ck = collision_moment(k)
    good_mass = 3 * collision_moment(k - 1) - Ck
    aligned_mass = 1 - Ck
    return {
        "A": A,
        "k": k,
        "N": N,
        "original_sufficient_condition_7_to_A_minus_1_gt_3k_squared": lower_N > 3 * k * k,
        "sharper_sufficient_condition_7_to_A_minus_1_gt_k_squared": lower_N > k * k,
        "all_histograms_distinct_mod_7_to_A_minus_1": True,
        "histogram_pairs_checked": M * M,
        "max_Eisenstein_norm_divided_by_three": maximum_norm_divided_by_three,
        "stable_histogram_gram": "(1-18/N)11*+(18/N)I",
        "zero_sum_histogram_isometry_verified_exactly": True,
        "all_character_weights_checked_against_raw_central_gram": len(labels),
        "good_squared_norm_coefficient_before_Q_A_to_minus_4h": str(Fraction(18, N) * good_mass),
        "aligned_squared_norm_coefficient_before_Q_A_to_minus_4h": str(Fraction(18, N) * aligned_mass),
        "ratio": str(good_mass / aligned_mass),
    }


def unstable_witness(A, k, eta):
    modulus = 7 ** (A - 1)
    seen = {}
    for h in histograms(k):
        residue = sum(h[j] * pow(eta, j, modulus) for j in range(3)) % modulus
        if residue in seen:
            return {"A": A, "k": k, "modulus": modulus, "histogram_1": seen[residue], "histogram_2": h, "equal_phase_residue": residue}
        seen[residue] = h
    return None


def main():
    eta = eta_lifts(4)
    weights = {k: histogram_weights(k) for k in (3, 5)}
    stable = [
        verify_stable_level(3, 3, weights[3], eta[3]),
        verify_stable_level(4, 5, weights[5], eta[4]),
        verify_stable_level(3, 5, weights[5], eta[3]),
    ]
    assert unstable_witness(2, 3, eta[2]) is not None
    moments = {ell: collision_moment(ell) for ell in range(0, 12)}
    for ell in range(11):
        assert 3 * moments[ell + 1] >= moments[ell]
    result = {
        "baseline_scientific_pin": BASELINE_SCIENTIFIC_PIN,
        "baseline_delivery_pin": BASELINE_DELIVERY_PIN,
        "arithmetic": "Exact integral cyclotomic reduction, rational weights, and exact F_3 character sums.",
        "central_levels": [verify_level(A) for A in range(1, 5)],
        "central_tower": verify_tower(4),
        "histogram_collision_moments": {ell: str(value) for ell, value in moments.items()},
        "histogram_character_and_all_plane_checks": [weights[k]["summary"] for k in (3, 5)],
        "stable_full_central_gram_checks": stable,
        "preserved_unstable_histogram_collision": unstable_witness(2, 3, eta[2]),
        "scope": {
            "exhaustive": "All central powers and Fourier characters through A=4; all histogram character labels and all two-planes at k=3,5; all stable histogram Gram entries at A3/k3, A4/k5 and A3/k5.",
            "analytic_proofs_needed_beyond_finite_checks": "The general trace/order formulas, the all-k mixture Holder inequality and histogram separation proof are written separately.",
            "not_encoded": "The vector trace-input isometry, vector coisometries and full alternating-pencil matrix checks are owned by the separate vector proof/verifier.",
        },
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

