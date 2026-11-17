#!/usr/bin/env python3
"""Exact polynomial resultant and finite checks; SymPy 1.14.0.

For manuscripts/e7-odd-diagonal-union.md. Covers all eight sign triples and
all odd integer q >= 3 via an exact resultant bound and the written tail proof.
It does not verify the external group centralizer or canonical loop inputs."""
import sympy as s
assert s.__version__=='1.14.0'
x=s.symbols('x')
expected={(1,1): (1,2**42),(1,-1):(2*3**2,2**17*3**14*5**2*31),(-1,-1):(2**8,2**34*5**4),(-1,1):(2**13,2**37*5**2*7**2*13**2)}
# Table keys encode eps*delta, delta*eta.
R=2**63*5**2*7**2*13**2
assert 17**22>256*R
allowed=[x,x-1,x+1]+[s.cyclotomic_poly(j,sign*x) for j in (3,5,6,9,12) for sign in (1,-1)]
for eps in (1,-1):
 for delta in (1,-1):
  for eta in (1,-1):
   A=x**28*s.prod(x**i-eps**i for i in range(2,9))
   B=(x-eta)*x**36*s.prod(x**i-delta**i for i in (2,5,6,8,9,12))
   d=s.gcd(A,B);a=s.cancel(A/d);b=s.cancel(B/d)
   r1=abs(int(s.resultant(a,b,x)));r2=abs(int(s.resultant(a+b,d,x)))
   assert (r1,r2)==expected[(eps*delta,delta*eta)]
   assert r1*r1*r2<=R
   coeff, fac=s.factor_list(b)
   assert coeff==1 and s.degree(b)>=22
   assert all(any(s.expand(p-z)==0 for z in allowed) for p,m in fac)
   assert sum(m for p,m in fac if p!=x)<=8
   assert next(m for p,m in fac if p==x)==8
   for q in (3,5,7,9,11,13,15):
    aa=int(a.subs(x,q));bb=int(b.subs(x,q));dd=int(d.subs(x,q))
    assert dd*aa*bb%(aa+bb)!=0,(eps,delta,eta,q)
print('PASS all eight sign triples, exact resultants, finite q and universal tail bound and factors')
