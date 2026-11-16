#!/usr/bin/env python3
"""Exact arithmetic checks of the all-unit Bol section over Z/p^a.

Verifies sparse Fourier block action and enumerates two-step point-start
probabilities. Experiments support, but do not replace, the proofs.
"""
from collections import Counter
from fractions import Fraction
from math import gcd
import json


def orbit_check(p, depth, z):
    n = p**depth
    units = [b for b in range(n) if gcd(b,n)==1]
    m = len(units)
    fibers = {}
    for b in units:
        fibers.setdefault(b*z % n, []).append(b)
    h = len(fibers)
    k = m//h
    nonzero, diagonal = 0, 0
    for xi in range(n):
        for b in units:
            first = [(b*z % n,v) for v in fibers.get(xi,[])]
            if first:
                nonzero += 1
                assert len(first)==k
                # The Fourier B=mA matrix is symmetric.
                assert all((xi,b) in [(v*z % n,w) for w in fibers.get(eta,[])]
                           for eta,v in first)
                # On stabilizer-constant quotient coordinates it is k*transpose.
                assert all(eta==b*z % n and v*z % n==xi for eta,v in first)
            diagonal += (xi,b) in first
    assert nonzero == h*m
    assert diagonal==m
    rank = h*h
    return {"p":p,"depth":depth,"z":z,"orbit":h,
            "leaf_dimension":n*m,"rank":rank,
            "multiplicity_plus":h*(h+1)//2,
            "multiplicity_minus":h*(h-1)//2,
            "multiplicity_zero":n*m-rank}


def mixing_check(p, depth):
    n=p**depth
    units=[b for b in range(n) if gcd(b,n)==1]
    m=len(units)
    counts=Counter()
    # Initial (x0,b0,s0)=(0,1,0), primitive leaf r=1.
    for b1 in units:
        for b2 in units:
            for x1 in range(n):
                for x2 in range(n):
                    s2=((b2-1)*x1-b1*x2)%n
                    counts[(x2,b2,s2)]+=1
    total=(m*n)**2
    assert sum(counts.values())==total
    # Uniform probability corresponds to count m for every endpoint.
    l1=sum(abs(counts[(x,b,s)]-m)
           for x in range(n) for b in units for s in range(n))
    tv=Fraction(l1,2*total)
    expected=Fraction(2*p,p**3-1)*(1-Fraction(1,p**(3*depth)))
    assert tv==expected, (p,depth,tv,expected)
    return {"p":p,"depth":depth,"histories":total,
            "tv_exact":str(tv),"formula_exact":str(expected)}


if __name__=='__main__':
    print(json.dumps({
        "orbit_cases":[orbit_check(*args) for args in
                       [(3,1,0),(3,1,1),(3,2,1),(3,2,3),
                        (7,2,0),(7,2,1),(7,2,7)]],
        "mixing_cases":[mixing_check(*args) for args in
                        [(3,1),(3,2),(3,3),(5,1),(5,2),(7,1)]]
    },indent=2))

