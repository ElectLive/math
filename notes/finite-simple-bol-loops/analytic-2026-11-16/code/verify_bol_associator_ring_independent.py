#!/usr/bin/env python3
"""Direct exact character counts for the proposed prime-power sector factor.

This enumerates every pair u,v in (Z/49)^2 for every c,d in F3 in selected
zero/primitive/imprimitive cases. NumPy is used only for integer arrays.
No authored checker or asserted bilinear-Gaussian formula is imported.
"""

from fractions import Fraction
from itertools import product
import json
import numpy as np


Q = 7
A = 2
M = Q**A
P = 3
ETA = 30


def cyclotomic_reduce(counts):
    # Phi_49(X)=1+X^7+...+X^42. Coefficients are exact integers.
    result = [int(x) for x in counts]
    for residue in range(7):
        leading = result[42 + residue]
        for j in range(6):
            result[7*j + residue] -= leading
    return tuple(result[:42])


def valuation(x):
    if x == 0:
        return A
    return 1 if x % Q == 0 else 0


def main():
    vectors = np.array(list(product(range(M), repeat=2)), dtype=np.int16)
    u0, u1 = vectors[:, 0], vectors[:, 1]
    symplectic = (u0[:, None]*u1[None, :] - u1[:, None]*u0[None, :]) % M
    assert symplectic.shape == (M*M, M*M)
    cases = [
        (0, 1, (1, 0), 0),
        (0, 1, (0, 0), 1),
        (0, 7, (7, 0), 2),
        (7, 1, (1, 0), 0),
        (7, 1, (7, 0), 1),
        (7, 7, (1, 0), 2),
        (1, 1, (1, 2), 0),
        (14, 3, (7, 14), 2),
    ]
    answers = []
    for sigma, rho, z, g in cases:
        total = [0] * M
        linear = (u0*z[1] - u1*z[0]) % M
        bilinear = (sigma * symplectic) % M
        for c, d in product(range(P), repeat=2):
            first = rho * (pow(ETA, g, M) - pow(ETA, d, M)) % M
            second = rho * (pow(ETA, c+g, M) - 1) % M
            exponents = (bilinear + (first*linear)[:, None] + (second*linear)[None, :]) % M
            counts = np.bincount(exponents.ravel(), minlength=M)
            assert int(counts.sum()) == M**4
            total = [a + int(b) for a, b in zip(total, counts)]
        reduced = cyclotomic_reduce(total)
        assert all(x == 0 for x in reduced[1:]), (sigma, rho, z, g, reduced)
        observed = Fraction(reduced[0], P**2 * M**4)
        divisor = Q**valuation(sigma)
        admissible = all((rho*x) % divisor == 0 for x in z)
        bad = 0 if admissible else 1
        predicted = Fraction(1, Q**(2*(A-valuation(sigma))) * P**(2*bad))
        assert observed == predicted, (sigma, rho, z, g, observed, predicted)
        answers.append({'sigma': sigma, 'rho': rho, 'z': z, 'g': g,
                        'bad_planes': bad, 'value': str(observed)})
    print(json.dumps({'modulus': M, 'eta': ETA, 'cases': answers,
                      'exact_character_terms': len(cases)*P**2*M**4,
                      'all_passed': True}, indent=2))


if __name__ == '__main__':
    main()

