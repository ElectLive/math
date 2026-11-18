"""Independent c96 stress tests, not an all-field/odd-rank proof."""
from itertools import product
from math import prod
from collections import Counter
from fractions import Fraction

def mul(a,b):
 x=0
 while b:
  if b&1:x^=a
  b>>=1;a=(a<<1)^ (7 if a&2 else 0)
 return x

def sc(t,x):return mul(t,x&3)|(mul(t,x>>2)<<2)

def small():
 # Exhaust all full-first-column additive rank-2 codes in Mat_2(F4).
 plane=list(range(16));C4={x:{sc(t,x) for t in range(4)} for x in plane}
 lin=[]
 for a,b in product(plane,repeat=2):lin.append(tuple(sc(x&3,a)^sc(x>>2,b) for x in plane))
 counts=Counter();notq=0;cases=0
 def go(F):
  nonlocal cases,notq
  h=len(F)
  if h==16:
   cases+=1;assert len(set(F))==16
   B=[D for D in lin if all(D[F[x]]==F[D[x]] for x in plane)]
   assert all(len(set(D))==16 for D in B if any(D)) and len(B)<=16
   if any(F[sc(2,x)]!=sc(2,F[x]) for x in plane):notq+=1
   counts[len(B)]+=1
   return
  for y in plane:
   rep=tuple(y^v for v in F)
   if any(rep[x] in C4[x+h] for x in range(h)):continue
   go(F+rep)
 go((0,));assert notq and cases==sum(counts.values());print('GF4 two-column rank-two graph codes, non-GF4-linear codes, idealizer cardinality multiplicities:',cases,notq,sorted(counts.items()))

def small_field():
 q=3;d=5;S=q**10*prod(q**j-1 for j in range(2,6));g1=121;g2=1210
 # Generously allow BOTH oriented difference-four profiles along with all four at difference two.
 mass=2*(Fraction(g2*(1+g1),q**4)+Fraction(g1,q**16))
 for a in [4,5]:
  x=d-a;rho=3;k=a//(rho+1)
  e=10-rho*(2*a-rho-1)//2+(a*(k+1)+x*(x+1))//2
  lo=Fraction(S,q**(a*(a-rho)))/mass; hi=q**e
  assert lo>hi;print('d=5,q=3 exact NO-divisibility lower/upper, support',a,':',lo,hi)

if __name__=='__main__':small();small_field()
