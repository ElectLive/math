#!/usr/bin/env python3
"""E6 P=16 outer-pattern and integer-polynomial certificate.

Requires Python 3.11+, SymPy 1.14.0 and assertions enabled. No file I/O.
The manuscript e6-odd-semilinear-full-socles.md owns the quantified proof.
Group/classification, Lang descent and marked-folder inputs are external.
The resultant tail proves the finite cutoff; the finite sweep does not.
"""
import sympy as sp
assert __debug__, 'Run with assertions enabled'
assert sp.__version__=='1.14.0'
from fractions import Fraction
from math import gcd
from itertools import product
x=sp.symbols('x');I=(2,5,6,8,9,12)
expected_patterns={(0,0,0,1),(0,0,0,3),(0,0,1,0),(0,0,1,1),(0,0,1,3),(0,1,0,1),(0,1,1,0),(0,3,0,3),(0,3,1,0),(1,0,0,1),(1,0,1,0),(1,1,0,1),(1,1,1,0),(3,0,0,3),(3,0,1,0),(3,3,0,3),(3,3,1,0)}
# Abstract outer S3 x C2; graph bit acts by inversion on the C3.
outer=list(product(range(3),range(2),range(2)))
one=(0,0,0)
def mul(x,y):
 i,j,k=x;a,b,c=y
 return ((i+(-1 if j else 1)*a)%3,j^b,k^c)
def inv(x):return next(y for y in outer if mul(x,y)==one and mul(y,x)==one)
def conj(x,y):return mul(mul(x,y),inv(x))
def generated(xs):
 h={one}|set(xs)
 while True:
  new=h|{mul(x,y) for x in h for y in h}
  if new==h:return frozenset(h)
  h=new
subgroups={generated(())}
while True:
 new=subgroups|{generated(tuple(h)+(x,)) for h in subgroups for x in outer}
 if new==subgroups:break
 subgroups=new
assert len(subgroups)==16
patterns=set()
for L in subgroups:
 for t in outer:
  if t in L or mul(t,t)!=one or any(conj(t,h) not in L for h in L):continue
  coset={mul(t,h) for h in L}
  # This deliberately overallows t not selected; it is a necessary overcount.
  labels=[(z,kind) for z in coset if mul(z,z)==one for kind in ((0,1) if z[1] and not z[2] else (2,) if z[2] and not z[1] else (3,) if z[2] and z[1] else ())]
  for mask in range(1,1<<len(labels)):
   selected={labels[i] for i in range(len(labels)) if mask>>i&1}
   if not any(kind>=2 for z,kind in selected):continue
   if any((conj(h,z),kind) not in selected for z,kind in selected for h in L):continue
   first=next(iter(selected))[0]
   if generated([mul(inv(first),z) for z,kind in selected])!=L:continue
   patterns.add(tuple(sum(kind==i for z,kind in selected) for i in range(4)))
assert patterns==expected_patterns
patterns=sorted(patterns)
print("outer group: 16 subgroups, 17 necessary count patterns",flush=True)
T=x**48*sp.prod(x**(2*i)-1 for i in I);A=x**16*(x**16+x**8+1);G=(x**18-1)*(x**10-1)
data={}
constant_patterns=set()
for e in (1,-1):
 U=sp.prod(x**i+e**i for i in I);V=sp.prod(x**i+(-e)**i for i in I)
 for pattern in patterns:
  a,b,n,m=pattern;F=(a+b*A)*G+x**12*(3*n*U+m*V)
  Fp=sp.Poly(F,x,domain=sp.ZZ);Tp=sp.Poly(T,x,domain=sp.ZZ)
  h=sp.gcd(Fp,Tp);assert h.LC()==1
  D=Fp.exquo(h);Q=Tp.exquo(h);d=D.degree()
  if d==0:
   constant_patterns.add((e,pattern))
   continue
  R=abs(int(D.resultant(Q)));assert R
  coeff=list(map(int,D.all_coeffs()));assert coeff[0]>0
  assert sum(Fraction(abs(c),3**i) for i,c in enumerate(coeff) if i)>Fraction(0)
  assert sum(Fraction(abs(c),3**i) for i,c in enumerate(coeff) if i)<Fraction(coeff[0],2)
  assert (2**21)**d > 24*R
  data[e,pattern]=(coeff,12*R)
assert len(data)==28
assert constant_patterns=={(e,p) for e in (1,-1) for p in ((0,0,0,1),(0,0,0,3),(0,0,1,0))}
print('28 nonconstant resultant tails; 6 singleton-type constant cases',flush=True)
mod=1<<23; survivors=[];seen=0
for s in range(3,2**21,2):
 if s%8 not in (3,5) or s%3==0:continue
 e=1 if s%3==1 else -1
 ps={i:pow(s,i,mod)for i in (2,5,6,8,9,10,12,16,18)}
 a=ps[16]*(ps[16]+ps[8]+1)%mod;g=(ps[18]-1)*(ps[10]-1)%mod
 u=1;v=1
 for i in I:u=u*(ps[i]+e**i)%mod;v=v*(ps[i]+(-e)**i)%mod
 u=3*ps[12]*u%mod;v=ps[12]*v%mod
 for pat in patterns:
  aa,bb,nn,mm=pat;F=((aa+bb*a)*g+nn*u+mm*v)%mod
  if F:continue
  seen+=1
  if (e,pat) not in data:survivors.append((s,pat,'constant'));continue
  co,R=data[e,pat];z=0
  for c in co:z=z*s+c
  if R%z==0:survivors.append((s,pat,z))
assert seen==45 and not survivors, (seen,survivors)
print('2-adic survivors 45; resultant divisibility survivors 0',flush=True)
# Characteristic 3: only one class per label; cover both form assignments.
patterns3=[(0,0,1,0),(0,0,0,1),(0,0,1,1),(1,0,1,0),(0,1,1,0),(1,1,1,0),(1,0,0,1),(0,1,0,1),(1,1,0,1)]
char3_tails=0
char3_constants=set()
for e in (1,-1):
 U=sp.prod(x**i+e**i for i in I);V=sp.prod(x**i+(-e)**i for i in I)
 for aa,bb,nn,mm in patterns3:
  F=(aa+bb*A)*G+x**12*(nn*U+mm*V)
  Fp=sp.Poly(F,x,domain=sp.ZZ);Tp=sp.Poly(T,x,domain=sp.ZZ)
  h=sp.gcd(Fp,Tp);assert h.LC()==1
  D=Fp.exquo(h);Q=Tp.exquo(h);d=D.degree()
  if d==0:
   char3_constants.add((e,(aa,bb,nn,mm)))
   continue
  char3_tails+=1
  R=abs(int(D.resultant(Q)));co=list(map(int,D.all_coeffs()));assert R and co[0]>0
  assert sum(Fraction(abs(c),3**i) for i,c in enumerate(co) if i)<Fraction(co[0],2)
  assert (2**21)**d>24*R

assert char3_tails==14
assert char3_constants=={(e,p) for e in (1,-1) for p in ((0,0,1,0),(0,0,0,1))}

def group(s,twisted=False):
 return s**36*(s**12-1)*(s**9+(1 if twisted else -1))*(s**8-1)*(s**6-1)*(s**5+(1 if twisted else -1))*(s*s-1)
def val2(z):return (z&-z).bit_length()-1
# Diagnostic checks of exact quotient formulas against full group orders.
for sample in (5,7,11,13):
 q=sample*sample;d=gcd(3,q-1);big=group(q)//d
 f=q**24*(q**12-1)*(q**8-1)*(q**6-1)*(q*q-1)
 c=q**16*(q*q-1)*(q**4-1)*(q**6-1)*(q**8-1)
 plus=group(sample)//gcd(3,sample-1)
 minus=group(sample,True)//gcd(3,sample+1)
 eps=1 if sample%3==1 else -1
 gg=(sample**18-1)*(sample**10-1)
 av=sample**16*(sample**16+sample**8+1)
 up=sp.prod(sample**i+eps**i for i in I)
 vp=sp.prod(sample**i+(-eps)**i for i in I)
 central,reflection=(plus,minus) if eps==1 else (minus,plus)
 assert all(big%z==0 for z in (f,c,central,reflection))
 assert big//f==sample**24*gg//d and big//c==sample**24*av*gg//d
 assert big//central==sample**36*3*up//d and big//reflection==sample**36*vp//d
s=3;checked=0
while s<2**21:
 q=s*s;big=group(q);f=q**24*(q**12-1)*(q**8-1)*(q**6-1)*(q*q-1)
 c=q**16*(q*q-1)*(q**4-1)*(q**6-1)*(q**8-1)
 ec,et=group(s),group(s,True)
 assert all(big%z==0 for z in (f,c,ec,et)) and val2(q*q-1)==4
 classes=[big//f,big//c,big//ec,big//et]
 for aa,bb,nn,mm in patterns3:
  total=sum(v*w for v,w in zip((aa,bb,nn,mm),classes));order=1 if aa+bb+nn+mm==1 else 2
  assert order*big%total!=0 or val2((order*big)//total)>2
  checked+=1
 s*=9
assert checked==63
print('characteristic 3: nonconstant resultant tails, 63 exact finite checks pass')
