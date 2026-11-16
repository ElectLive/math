#!/usr/bin/env python3
"""Exact arithmetic only; group-theoretic hypotheses are not checked here."""
from math import gcd,isqrt

LIMIT=1030**2

def prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def powers():
    result=[]
    for p in range(2,512):
        if prime(p):
            q,f=p,1
            while q<512:
                result.append((q,f))
                q,f=q*p,f+1
    assert len(result)==len({q for q,f in result})
    return sorted(result)

Bexpected={2:[5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53,59,61,64,81,125,128,256],3:[2,3],4:[]}
for r in (2,3,4):
    residual=[]
    for q,f in powers():
        if (r==3 and q>=5) or (r==4 and q>=3):
            continue
        g=gcd(2,q-1)
        n=q**(r*r)
        for i in range(1,r+1):
            n*=q**(2*i)-1
        assert n%g==0
        n//=g
        t=2*f if r==2 else g*f
        if n>=2**20 and n<=LIMIT*t**3*q**(3*r):
            residual.append(q)
    assert residual==Bexpected[r],(r,residual)

for r in (4,5):
    for eps in (-1,1):
        residual=[]
        for q,f in powers():
            if (r==4 and q>=7) or (r==5 and q>=3):
                continue
            g=gcd(4,q**r-eps)
            n=q**(r*(r-1))*(q**r-eps)
            for i in range(1,r):
                n*=q**(2*i)-1
            assert n%g==0
            n//=g
            t=(6 if r==4 and eps==1 else 2)*f*g
            if n>=2**20 and n<=LIMIT*t**3*q**(3*r):
                residual.append(q)
        assert residual==([2,3] if r==4 else []),(r,eps,residual)

# Conservative tail inequalities. q=5 in rank 3 needs its own check.
assert 2**40 > 24*LIMIT
assert 3**24 > 24*2**3*LIMIT
assert 5**12 > 24*LIMIT
assert 7**12 > 24*3**3*LIMIT
assert 512**4 > 24*9**3*LIMIT
assert 2**48 > 12*24**3*LIMIT
assert 3**30 > 12*24**3*2**3*LIMIT
assert 7**16 > 12*24**3*3**3*LIMIT
print('orthogonal R-screen arithmetic passed')
