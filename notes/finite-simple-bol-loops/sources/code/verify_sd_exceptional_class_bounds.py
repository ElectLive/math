#!/usr/bin/env python3
"""Exact endpoint checks; source class bounds and asymptotic proofs are external."""
from math import isqrt

def screen(n,t,k):
    a=t*n
    v=a*k
    b=isqrt(v)
    b += b*b<v
    assert n>=2**20 and b**3+3*a*b<n*n

for q,t in [(3,2),(4,2),(5,1),(7,1),(8,3),(9,4),(11,1),(13,1)]:
    n=q**6*(q**6-1)*(q*q-1)
    screen(n,t,t*(q*q+2*q+9))
q=2
n=q**12*(q**8+q**4+1)*(q**6-1)*(q*q-1)
screen(n,3,3*(q**4+q**3+q*q+q+6))
# Rational endpoint estimates from the manuscript.
from fractions import Fraction as F
assert 96*F(4**3,16**4)+36*F(4**2,16**6)<1
assert F(108,3**5)+F(54,3**10)<1
assert F(4,8**7)+F(6,8**10)<1
print('exceptional class-bound endpoint checks passed')
