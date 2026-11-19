#!/usr/bin/env python3
"""Author's exact rational/combinatorial checks for bol-collective-incidence.md.

Python 3.11+; standard library only. All assertions use integers or Fraction.
Decimal strings in the JSON output are display-only. This program does not
enumerate the ambient field/vector spaces and is not an independent review.
The separate actual-field checker tests the field and radical interfaces.

Run from any directory:
    python -B problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_incidence.py
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import factorial
import json


Q = 729
A = F(2, 9)
BM = F(7, 81)
H = (1, 2, 4)


@lru_cache(None)
def u_power(k):
    """S^k+conj(S)^k, where S+conj(S)=-1 and S*conj(S)=2."""
    if k == 0:
        return 2
    if k == 1:
        return -1
    return -u_power(k - 1) - 2 * u_power(k - 2)


@lru_cache(None)
def e_power(k):
    """9^k*(m_*^k+b_*^k), an integer."""
    if k == 0:
        return 2
    if k == 1:
        return 7
    return 7 * e_power(k - 1) - 7 * e_power(k - 2)


def ell(k):
    return F(e_power(k), 9**k)


def p_power(k):
    return A**k + ell(k)


def g(h):
    return p_power(2 * h) - A ** (2 * h + 1)


def generic_counts(k):
    assert k >= 1
    numerators = (
        3**k + 3 * u_power(k),
        3**k + 2 * u_power(k - 1),
        3**k + u_power(k + 1),
    )
    assert all(v % 7 == 0 for v in numerators)
    c0, cp, cm = (v // 7 for v in numerators)
    result = (c0, cp, cp, cm, cp, cm, cm)
    assert min(result) >= 0 and sum(result) == 3**k
    return result


def types(k, include_zero=False):
    for n0 in range(k + int(include_zero)):
        for n1 in range(k - n0 + 1):
            yield n0, n1, k - n0 - n1


@lru_cache(None)
def conditional_counts(n0, n1, n2):
    """Counts for (normal dot b, sum 2^b), indexed as 7*c+s."""
    if n0 + n1 + n2 == 0:
        return (1,) + (0,) * 20
    ns = [n0, n1, n2]
    j = next(i for i in range(3) if ns[i])
    ns[j] -= 1
    previous = conditional_counts(*ns)
    result = [0] * 21
    for c in range(3):
        for s in range(7):
            value = previous[7 * c + s]
            for b in range(3):
                result[7 * ((c + j * b) % 3) + (s + H[b]) % 7] += value
    return tuple(result)


def check_exhaustive_distributions():
    """A direct word enumeration independent of the coefficient recurrence."""
    words_checked = 0
    normal_words_checked = 0
    for k in range(1, 10):
        type_list = list(types(k))
        direct_types = {ns: [0] * 21 for ns in type_list}
        direct_generic = [0] * 7
        for word in product(range(3), repeat=k):
            prefix = [0]
            for b in word:
                prefix.append(prefix[-1] + b)
            symbol = sum(H[b] for b in word) % 7
            direct_generic[symbol] += 1
            for n0, n1, n2 in type_list:
                normal_value = (
                    prefix[n0 + n1] - prefix[n0]
                    + 2 * (prefix[k] - prefix[n0 + n1])
                ) % 3
                direct_types[n0, n1, n2][7 * normal_value + symbol] += 1
            words_checked += 1
            normal_words_checked += len(type_list)
        assert tuple(direct_generic) == generic_counts(k)
        for ns, direct in direct_types.items():
            assert tuple(direct) == conditional_counts(*ns), (k, ns)
    return {
        "k_range": [1, 9],
        "generic_words": words_checked,
        "normal_type_word_pairs": normal_words_checked,
    }


def check_degree_tables():
    expected_generic = {
        3: (6, 3, 4), 5: (30, 35, 36), 7: (318, 315, 308),
        9: (2814, 2803, 2820), 11: (25278, 25323, 25300),
    }
    expected_minimum = {3: 0, 5: 0, 7: 35, 9: 378, 11: 5610}
    expected_maximum = {3: 6, 5: 30, 7: 210, 9: 1680, 11: 11770}
    expected_seven = [(35, 210), (45, 180), (71, 135), (86, 123),
                      (90, 117), (95, 108), (101, 108)]
    rows = []
    coefficient_types = 0
    for k, generic in expected_generic.items():
        counts = generic_counts(k)
        assert (counts[0], counts[1], counts[3]) == generic
        assert min(counts) > 0
        minimum, maximum = 3**k, 0
        for ns in types(k):
            array = conditional_counts(*ns)
            coefficient_types += 1
            for c in range(3):
                assert sum(array[7 * c:7 * c + 7]) == 3 ** (k - 1)
            for s in range(7):
                assert sum(array[7 * c + s] for c in range(3)) == counts[s]
            minimum = min(minimum, min(array))
            maximum = max(maximum, max(array))
        assert minimum == expected_minimum[k]
        assert maximum == expected_maximum[k]
        rows.append({
            "k": k, "generic_orbit_counts": generic,
            "nonzero_normal_minimum": minimum,
            "nonzero_normal_maximum": maximum,
            "conditional_denominator": 3 ** (k - 1),
        })
    seven = []
    for n0 in range(7):
        arrays = [conditional_counts(n0, n1, 7 - n0 - n1)
                  for n1 in range(8 - n0)]
        pair = min(min(a) for a in arrays), max(max(a) for a in arrays)
        assert pair == expected_seven[n0]
        seven.append([n0, *pair])
    assert conditional_counts(0, 5, 0)[3] == 0
    return {"rows": rows, "k7_minmax": seven, "coefficient_types": coefficient_types}


def line_mass(n0, n1, n2):
    """w(nu)+w(-nu); conjugate powers cancel to a rational number."""
    return A**n0 * BM**min(n1, n2) * ell(abs(n1 - n2))


def check_weights():
    count = 0
    for k in range(1, 26):
        mass_sum = F(0)
        largest = F(0)
        for ns in types(k):
            n0, n1, n2 = ns
            mass = line_mass(*ns)
            multiplicity = factorial(k) // (factorial(n0) * factorial(n1) * factorial(n2))
            mass_sum += multiplicity * mass / 2
            largest = max(largest, mass)
            count += 1
        assert mass_sum == 1 - A**k
        assert largest == ell(k)
        assert line_mass(0, k, 0) == ell(k)
    assert p_power(2) == F(13, 27)
    assert g(3) == F(340018, 4782969) < F(1, 12)
    assert all(g(h + 1) < g(h) for h in range(1, 25))
    # Parseval and the two equivalent centerings used in COL/SMALL/COVER.
    for h in range(1, 21):
        k = 2 * h + 1
        probabilities = [F(c, 3**k) for c in generic_counts(k)]
        assert sum(p * p for p in probabilities) == F(1, 7) + F(6, 7) * A**k
        for n in (1, 2, 7, 36, 37, 100, Q ** (2 * h)):
            theta = (1 - A**k) / n + (1 - F(1, n)) * ell(k)
            capital_theta = F(1, n) + (1 - F(1, n)) * p_power(k)
            assert capital_theta == theta + A**k
            assert F(6, 7) * theta == F(6, 7 * n * n) * (
                n * (1 - A**k) + n * (n - 1) * ell(k)
            )
    return {"k_range": [1, 25], "normal_types": count,
            "g3": str(g(3)), "ell3": str(ell(3))}


def m_less_than(q):
    """Prove (7+sqrt(21))/18 < q using rational arithmetic."""
    t = 18 * q - 7
    return t > 0 and t * t > 21


def b_less_than(q):
    """Prove (7-sqrt(21))/18 < q using rational arithmetic."""
    t = 7 - 18 * q
    return t <= 0 or t * t < 21


def check_strict_certificates():
    # Generic-mass actual rectangle separation, uniformly for h>=3.
    ratio_upper_h1 = F(7, 4) * F(9, Q**2) / (1 - F(1, Q**4))
    assert F(9, Q**2) < 1 and ratio_upper_h1 < F(1, 100)
    sep_coefficient = F(61, 64)**2 * F(6, 7) * F(99, 100)**3
    assert sep_coefficient > F(1, 2) > 6 * g(3)
    assert A < F(1, 2)**2

    # Uniform h>=5 nonzero-u comparison, with square-root upper bounds.
    assert b_less_than(F(3, 8)**2)
    assert m_less_than(F(81, 100)**2)
    eta5_upper = 6 * (F(1, 2)**11 + F(3, 8)**11 + F(81, 100)**11)
    g5_upper = F(1, 2)**20 + F(3, 8)**20 + F(81, 100)**20
    assert eta5_upper < F(3, 5)
    assert g(5) < g5_upper < F(1, 60)
    assert 6 * g5_upper / (1 - eta5_upper)**2 < F(5, 8)
    assert F(5, 8) < F(6, 7) * (1 - F(1, Q**11))

    # COVER: rational upper bound for P_17, hence all h>=8,n>=37.
    assert m_less_than(F(29, 45)) and b_less_than(F(7, 50))
    p17_upper = A**17 + F(29, 45)**17 + F(7, 50)**17
    assert p_power(17) < p17_upper < F(1, 1700)
    failure_upper = F(36, 37) + F(1296, 37 * 1700)
    assert failure_upper == F(62496, 62900) < 1
    assert 1 - failure_upper == F(101, 15725)
    return {
        "sep_tau_over_beta_upper": decimal(ratio_upper_h1),
        "sep_coefficient": decimal(sep_coefficient),
        "eta5_upper": decimal(eta5_upper),
        "g5_upper": decimal(g5_upper),
        "P17_exact": str(p_power(17)),
        "P17_upper_less_than": "1/1700",
        "h_ge_8_n_ge_37_good_seed_fraction": "101/15725",
    }


def decimal(value):
    return format(float(value), ".12g")


def check_normalizations_and_slices():
    rows = []
    for h in range(1, 21):
        k = 2 * h + 1
        n_space = Q ** (6 * h)
        v = (3**k - 1) // 2
        exceptional = 1 + v * (Q ** (2 * h) - 1)
        tau = F(exceptional, n_space)
        gamma = 1 - tau
        assert 0 < gamma < 1
        assert tau < F(v, Q ** (4 * h))
        assert n_space % 3**k == 0
        assert n_space % 3 ** (k - 1) == 0
        balanced_beta = F(6, 7) * (1 - F(1, Q ** (4 * h))) / Q ** (2 * h)
        assert tau / balanced_beta < F(1, 100)

        incidence_square = F(6, 49) * g(h) / Q ** (4 * h)
        word_square = F(18, 49) * g(h) / Q ** (4 * h)
        assert word_square == 3 * incidence_square
        m_full = 7 * n_space * 3**k
        assert m_full // 7 == n_space * 3**k
        assert incidence_square * n_space * m_full == F(6, 7) * 3**k * Q ** (8 * h) * g(h)
        m_slice = (n_space - exceptional) * 3**k
        fixed_square = F(7, 3) * incidence_square / gamma
        assert fixed_square * n_space * m_slice == F(2, 7) * 3**k * Q ** (8 * h) * g(h)
        fixed_zero_square = 6 * incidence_square / gamma
        assert fixed_zero_square * n_space * m_slice == F(36, 49) * 3**k * Q ** (8 * h) * g(h)
        assert 0 < 1 - F(v - 1, Q ** (2 * h)) < 1

        counts = generic_counts(k)
        probabilities = [F(counts[s], 3**k) for s in (1, 3)]
        ratios = []
        for p in probabilities:
            rank_square = p * (1 - p) / (gamma * Q ** (4 * h))
            assert rank_square * n_space * m_slice == 3**k * Q ** (8 * h) * p * (1 - p)
            ratio = fixed_square / rank_square
            assert ratio == 2 * g(h) / (7 * p * (1 - p))
            assert (ratio < 1) == (h >= 2)
            ratios.append(decimal(ratio))
        rows.append({"h": h, "fixed_s_new_over_rank_H": ratios[0],
                     "fixed_s_new_over_rank_minus_H": ratios[1]})
    return {"h_range": [1, 20], "slice_threshold_ratios": rows}


def check_coverage_thresholds():
    rows = []
    expected_uniform = {4: 111, 5: 50, 6: 41, 7: 38, 8: 37}
    expected_biased = {4: 113, 5: 50, 6: 41, 7: 38, 8: 37}
    for h in range(4, 9):
        k = 2 * h + 1
        pk = p_power(k)
        c_min = min(generic_counts(k))
        lam = F(7 * c_min, 3**k)
        assert 1 - 36 * pk > 0
        uniform_need = 36 * (1 - pk) // (1 - 36 * pk) + 1
        biased_denominator = 49 * c_min**2 - 36 * e_power(k)
        biased_numerator = 36 * (9**k - 2**k - e_power(k))
        assert biased_denominator > 0
        biased_need = biased_numerator // biased_denominator + 1
        assert uniform_need == expected_uniform[h]
        assert biased_need == expected_biased[h]
        for needed, biased in ((uniform_need, False), (biased_need, True)):
            for n, expected_strict in ((needed - 1, False), (needed, True)):
                theta = (1 - A**k) / n + (1 - F(1, n)) * ell(k)
                bound = 36 * theta / lam**2 if biased else 36 * (theta + A**k)
                assert (bound < 1) == expected_strict
        rows.append({"h": h, "uniform_min_n": uniform_need,
                     "biased_min_n": biased_need,
                     "best_min_n": min(uniform_need, biased_need)})
    return rows


def check_pairwise_36_obstruction():
    # Each seed is one function: choose the missing symbol, then a balanced
    # assignment to the other six labels. Count exact singleton/pair events.
    seeds = 7 * factorial(36) // factorial(6)**6
    singleton = 6 * factorial(35) // (factorial(5) * factorial(6)**5)
    equal_pair = 6 * factorial(34) // (factorial(4) * factorial(6)**5)
    distinct_pair = 5 * factorial(34) // (factorial(5)**2 * factorial(6)**4)
    assert F(singleton, seeds) == F(1, 7)
    assert F(equal_pair, seeds) == F(1, 49)
    assert F(distinct_pair, seeds) == F(1, 49)
    assert F(5, 35) == F(1, 7)
    assert 6 * F(6, 36)**2 - F(1, 7) == F(1, 42) == F(6, 7 * 36)
    return {"source_size": 36, "seed_functions": str(seeds),
            "singleton_probability": "1/7", "every_ordered_pair_probability": "1/49",
            "missing_symbols_per_seed": 1}


def main():
    result = {
        "status": "PASS",
        "scope": "Author exact rational/combinatorial checks; no ambient-field enumeration",
        "exhaustive_distributions": check_exhaustive_distributions(),
        "degree_tables": check_degree_tables(),
        "weight_checks": check_weights(),
        "strict_certificates": check_strict_certificates(),
        "normalizations": check_normalizations_and_slices(),
        "coverage_thresholds": check_coverage_thresholds(),
        "pairwise_36_obstruction": check_pairwise_36_obstruction(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
