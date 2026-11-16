#!/usr/bin/env python3
"""Exact finite checks for the blocked-coordinate polynomial small-bias sampler.

This contributor-authored check imports no authored Bol checker. It tests the
character sum used by the sparse randomization construction in small fields,
including all seeds and all additive characters in each stated case. It also
checks the symbolic resource inequalities at representative larger parameters.
It does not enumerate the full reciprocal Bol channel or prove the uniform
theorems. The fixed polynomials are verified irreducible by root tests (degree
at most three), so no external finite-field package is needed.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
import json


class Field3:
    def __init__(self, modulus):
        assert modulus[-1] == 1
        self.modulus = tuple(modulus)
        self.r = len(modulus) - 1
        self.q = 3**self.r
        self.digits = tuple(
            tuple((a // 3**i) % 3 for i in range(self.r))
            for a in range(self.q)
        )
        # In degrees two and three, absence of a base-field root is sufficient.
        if self.r in (2, 3):
            assert all(
                sum(c * a**i for i, c in enumerate(modulus)) % 3
                for a in range(3)
            )
        else:
            assert self.r == 1
        self.add_table = tuple(
            tuple(self._add(a, b) for b in range(self.q))
            for a in range(self.q)
        )
        self.mul_table = tuple(
            tuple(self._mul(a, b) for b in range(self.q))
            for a in range(self.q)
        )
        assert all(self.power(a, self.q - 1) == 1 for a in range(1, self.q))
        self.trace_table = tuple(self._trace(a) for a in range(self.q))
        assert set(self.trace_table) == {0, 1, 2}
        for a in range(1, self.q):
            counts = Counter(self.trace(self.mul(a, b)) for b in range(self.q))
            assert [counts[i] for i in range(3)] == [self.q // 3] * 3

    def _add(self, a, b):
        return sum(
            ((x + y) % 3) * 3**i
            for i, (x, y) in enumerate(zip(self.digits[a], self.digits[b]))
        )

    def _mul(self, a, b):
        coefficients = [0] * (2 * self.r - 1)
        for i, x in enumerate(self.digits[a]):
            for j, y in enumerate(self.digits[b]):
                coefficients[i + j] = (coefficients[i + j] + x * y) % 3
        for i in range(2 * self.r - 2, self.r - 1, -1):
            c = coefficients[i]
            for j in range(self.r):
                coefficients[i - self.r + j] = (
                    coefficients[i - self.r + j] - c * self.modulus[j]
                ) % 3
            coefficients[i] = 0
        return sum(coefficients[i] * 3**i for i in range(self.r))

    def add(self, a, b):
        return self.add_table[a][b]

    def mul(self, a, b):
        return self.mul_table[a][b]

    def power(self, a, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            exponent >>= 1
        return result

    def _trace(self, a):
        result = 0
        conjugate = a
        for _ in range(self.r):
            result = self.add(result, conjugate)
            conjugate = self.power(conjugate, 3)
        assert result < 3
        return result

    def trace(self, a):
        return self.trace_table[a]

    def polynomial(self, coefficients, b):
        value = 0
        for c in reversed(coefficients):
            value = self.add(self.mul(value, b), c)
        return value


def sampler_case(field, length):
    blocks = (length + field.r - 1) // field.r
    seeds = []
    for a in range(field.q):
        for b in range(field.q):
            power = 1
            vector = []
            for block in range(blocks):
                for i in range(min(field.r, length - block * field.r)):
                    vector.append(field.trace(field.mul(field.mul(a, power), 3**i)))
                power = field.mul(power, b)
            seeds.append(tuple(vector))
    multiplicities = Counter(seeds)
    assert sum(multiplicities.values()) == field.q**2
    max_roots = 0
    character_count = 0
    for z in product(range(3), repeat=length):
        counts = [0, 0, 0]
        for vector, multiplicity in multiplicities.items():
            dot = sum(x * y for x, y in zip(z, vector)) % 3
            counts[dot] += multiplicity
        coefficients = [sum(z[j] * 3**(j % field.r)
                            for j in range(block * field.r,
                                           min((block + 1) * field.r, length)))
                        for block in range(blocks)]
        assert bool(any(coefficients)) == bool(any(z))
        roots = sum(field.polynomial(coefficients, b) == 0 for b in range(field.q))
        # e_3(1)+e_3(2)=-1. Equality of the two nonzero bins proves
        # reality, so this computes the character expectation exactly.
        assert counts[1] == counts[2]
        fourier = Fraction(counts[0] - counts[1], field.q**2)
        assert fourier == Fraction(roots, field.q)
        if any(z):
            assert roots <= blocks - 1
            assert Fraction(0) <= fourier <= Fraction(blocks - 1, field.q)
            max_roots = max(max_roots, roots)
            character_count += 1
        else:
            assert fourier == 1
    return {
        "character_count": character_count,
        "degree": field.r,
        "field_size": field.q,
        "length": length,
        "coefficient_blocks": blocks,
        "max_nontrivial_bias": str(Fraction(max_roots, field.q)),
        "modulus_low_to_high": list(field.modulus),
        "multiset_size": field.q**2,
        "distinct_outputs": len(multiplicities),
        "root_bound": str(Fraction(blocks - 1, field.q)),
    }


def resource_cases():
    cases = []
    for n_trits in (12, 24, 48):
        field_dimension = 3**n_trits
        dimension = 49 * field_dimension
        for epsilon in (Fraction(1), Fraction(1, 10), Fraction(1, 100)):
            threshold = Fraction(3 * 3**(n_trits // 2), 1) / epsilon
            r = 1
            q = 3
            while q < threshold:
                r += 1
                q *= 3
            assert q >= threshold
            assert q < 3 * threshold
            multiset_size = 7**4 * q**2
            upper = Fraction(3969 * dimension, 1) / epsilon**2
            assert multiset_size < upper
            blocks = (2 * n_trits + r - 1) // r
            assert blocks <= 4
            actual_bias_bound = Fraction(blocks - 1, q)
            assert field_dimension * actual_bias_bound**2 <= epsilon**2
            # Independent fixed-pair rounds: compare squared thresholds to
            # keep the possibly irrational delta entirely in exact arithmetic.
            sqrt_D = 3**(n_trits // 2)
            delta_squared = epsilon**2 / (3 * sqrt_D)
            round_r, round_q = 1, 3
            while round_q**2 < 9 / delta_squared:
                round_r += 1
                round_q *= 3
            assert round_q**2 < 81 / delta_squared
            round_blocks = (n_trits + round_r - 1) // round_r
            assert round_blocks <= 4
            assert Fraction(round_blocks - 1, round_q)**2 <= delta_squared
            round_choices = 49 * round_q**2
            assert round_choices < 11907 * sqrt_D / epsilon**2
            trace_squared = ((field_dimension - 1) * delta_squared**2
                             + 2 * (sqrt_D - 1) * (delta_squared - delta_squared**2))
            assert trace_squared <= epsilon**2
            cases.append({
                "n_trits": n_trits,
                "epsilon": str(epsilon),
                "extension_degree": r,
                "coefficient_blocks": blocks,
                "sampler_multiset_size": multiset_size,
                "exact_twirl_size": dimension**2,
                "selected_size_bound": min(multiset_size, dimension**2),
                "fixed_pair_round_extension_degree": round_r,
                "fixed_pair_round_choices": round_choices,
                "fixed_pair_round_blocks": round_blocks,
                "fixed_pair_trace_bound_squared": str(trace_squared),
            })
    return cases


def main():
    fields = {
        1: Field3((0, 1)),
        2: Field3((1, 0, 1)),
        3: Field3((1, 2, 0, 1)),
    }
    checks = [
        sampler_case(fields[r], length)
        for r, length in ((1, 2), (2, 2), (2, 4), (3, 4), (3, 6))
    ]
    result = {
        "status": "all exact checks passed",
        "sampler_cases": checks,
        "resource_cases": resource_cases(),
        "scope": (
            "All sampler seeds and all additive characters in five stated small "
            "cases; exact resource inequalities at nine parameters. No full "
            "growing Bol channel is enumerated."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
