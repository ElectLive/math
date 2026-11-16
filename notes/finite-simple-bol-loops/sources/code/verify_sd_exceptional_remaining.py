#!/usr/bin/env python3
"""Exact rational endpoint and Tits F3 arithmetic; group data are inputs."""
from fractions import Fraction
endpoint = Fraction(34992, 2**17) + Fraction(1944, 2**22)
assert endpoint == Fraction(140211, 524288) and endpoint < 1
n, a = 17971200, 35942400
assert a % 20480 == 0 and a % 3072 == 0
b = 1 + a // 20480 + a // 3072
assert b == 13456 and n >= 2**20
assert b**3 + 3*a*b == 3887319126016 < n*n
print("exceptional remaining arithmetic passed")
