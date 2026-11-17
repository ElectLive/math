#!/usr/bin/env python3
"""Regenerate and compare the frozen PSL4 overgroup polynomial certificates.

Optional development tool: requires Python 3.11+ and SymPy exactly 1.14.0.
The two verify_linear_four_*.py certificates require only the standard library.
Run this file from any directory; it writes no files and performs no networking.
Its centralizer formulas are independent expressions for the verifier's sizes.
"""
from itertools import product

import sympy as sp

import verify_linear_four_fieldfree as fieldfree
import verify_linear_four_semilinear as semilinear


def coefficients(expression, variable):
    return list(map(int, sp.Poly(expression, variable, domain=sp.ZZ).all_coeffs()))


def record(pattern, ratio, variable):
    numerator, denominator = sp.fraction(sp.cancel(ratio))
    if sp.degree(denominator, variable) == 0:
        return None
    resultant = sp.resultant(numerator, denominator, variable)
    a, b, gcd = sp.gcdex(numerator, denominator, variable)
    assert gcd == 1 and resultant != 0
    a, b = a * resultant, b * resultant
    assert sp.expand(a * numerator + b * denominator) == resultant
    return [list(pattern), coefficients(numerator, variable),
            coefficients(denominator, variable), coefficients(a, variable),
            coefficients(b, variable), int(resultant)]


def main():
    assert sp.__version__ == "1.14.0", sp.__version__
    x = sp.symbols("x")
    q = x * x
    order = q**6 * (q**2 - 1) * (q**3 - 1) * (q**4 - 1) / 4
    diagonal = q**2 * (q**2 - 1) * (q**4 - 1) / (2 * (q - 1))
    orthogonal_plus = q**2 * (q**2 - 1)**2
    symplectic = q**4 * (q**2 - 1) * (q**4 - 1) / 2
    orthogonal_minus = q**2 * (q**4 - 1)
    for sign in (1, -1):
        df, du = (2, 1) if sign == 1 else (1, 2)
        field = x**6 * (x**2 - 1) * (x**3 - 1) * (x**4 - 1) / df
        unitary = x**6 * (x**2 - 1) * (x**3 + 1) * (x**4 - 1) / du
        central, reflecting = (field, unitary) if sign == 1 else (unitary, field)
        sizes = [order / c for c in
                 (diagonal, orthogonal_plus, symplectic, orthogonal_minus,
                  central, reflecting)]
        rows = []
        for pattern in sorted(semilinear.pattern_set(sign)):
            marked = sum(n * size for n, size in zip(pattern, sizes))
            row = record(pattern, 16 * order / marked, x)
            if row is not None:
                rows.append(row)
        assert rows == semilinear.DATA[str(sign)]
    order = x**6 * (x**2 - 1) * (x**3 - 1) * (x**4 - 1) / 4
    sizes = [x**2 * (x**3 - 1) / 2,
             x**4 * (x**3 - 1) * (x**2 + 1) / 4,
             x**3 * (x + 1) * (x**2 + 1),
             x**4 * (x - 1) * (x**3 - 1) / 2]
    rows = []
    for pattern in product(range(2), repeat=4):
        if any(pattern[:2]) and any(pattern[2:]):
            marked = sum(n * size for n, size in zip(pattern, sizes))
            rows.append(record(pattern, 2 * order / marked, x))
    assert rows == fieldfree.DATA
    print("PASS: reproduced all 202 semilinear and 9 field-free frozen records")


if __name__ == "__main__":
    main()
