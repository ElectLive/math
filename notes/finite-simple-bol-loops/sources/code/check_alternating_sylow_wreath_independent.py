"""Independent alternating-socle checks in the actual exceptional automorphism group and permutation actions."""
from itertools import product
from collections import Counter
from math import factorial,prod,isqrt
def mul(f,g):return tuple(f[x] for x in g)
def inv(f):return tuple(f.index(i) for i in range(len(f)))
def con(g,f):return mul(g,mul(f,inv(g)))
def sq(f):return all(f[f[x]]==x for x in range(len(f)))
def a6():
 F=range(9)
 def add(x,y):return (x%3+y%3)%3+3*((x//3+y//3)%3)
 def neg(x):return (-x%3)+3*(-(x//3)%3)
 def m(x,y):return (x%3*(y%3)-x//3*(y//3))%3+3*((x%3*(y//3)+x//3*(y%3))%3)
 I=tuple(range(10));mi={x:next(y for y in F if m(x,y)==1) for x in F if x};squares={m(x,x) for x in F if x}
 phi=tuple(m(x,m(x,x)) for x in F)+(9,)
 cos=[set() for i in range(4)]
 for a,b,c,d in product(F,repeat=4):
  det=add(m(a,d),neg(m(b,c)))
  if not det or next(x for x in (a,b,c,d) if x)!=1:continue
  f=[]
  for x in range(10):
   y,z=(a,c) if x==9 else (add(m(a,x),b),add(m(c,x),d))
   f.append(m(y,mi[z]) if z else 9)
  f=tuple(f);j=int(det not in squares);cos[j].add(f);cos[j+2].add(mul(f,phi))
 T=cos[0];A=set.union(*cos);V=len(A);assert V==1440 and all(len(v)==360 for v in cos)
 counts=[sum(sq(x) for x in vv) for vv in cos];II=sum(counts);assert II==112
 u=next(a for a in T if a!=I and sq(a));C={con(t,u) for t in T}
 assert len(C)==45 and all(con(v,u) in C for v in A)
 # Distinct exchange signed marks lambda_i on the real twenty points carry genuinely exceptional field arrows.
 M={tuple(add(x,b) for x in F)+(9,) for b in F}
 assert M<=T and len(M)==9
 s=tuple(9 if x==0 else (0 if x==9 else neg(mi[x])) for x in range(10))
 assert s in T
 r=mul(s,phi);assert r not in cos[0]|cos[1] and {con(r,t) for t in M}!=M
 rr=mul(inv(s),r);assert rr==phi and {con(rr,t) for t in M}==M
 def mark(a):
  return tuple([10+a[i] for i in range(10)]+list(inv(a)))
 def base(a,b):return tuple(a)+tuple(10+x for x in b)
 lam=mark(r);q=base(I,inv(s));adj=con(q,lam);assert adj==mark(rr)
 marks={con(base(I,t),lam) for t in T};assert len(marks)==360 and adj in marks and all(sq(x) for x in marks)
 Mdiag={base(t,con(rr,t)) for t in M}
 anti={base(t,con(rr,inv(t))) for t in M}
 assert set.intersection(*(Mdiag,anti))=={base(I,I)}
 assert all(mul(adj,a) in marks for a in anti)
 sheets={frozenset(mul(f,g) for g in Mdiag) for f in anti}
 assert len(sheets)==9 and len(set().union(*sheets))==81
 # A different actual correlated subgroup with identical two site projections now yields collisions.
 assert all(mul(adj,x) in marks for x in anti) and len(anti)>1
 # Keep the full direct square-one kernel and all exchanging marks on the wreath of two actual A6 factors.
 S1=[a for a in A if sq(a)]
 two={base(a,b) for a,b in product(S1,repeat=2)}|{mark(g) for g in A}
 assert len(two)==II**2+V and all(sq(w) for w in two)
 print(f'Full Aut(A6) on 10 actual points: physical square-one counts by four PΓL₂(9)/PSL₂(9) cosets {counts}, {II} total, one 45-element inner involution class fused by none of {V} automorphisms. All {len(two)} actual square-one two-site permutations agree with F₂; fixed-site crude 2I>120 really fails.')
 print(f'A genuinely outer field arrow moves a physical Sylow-3 translation group to a different one. After an actual inner target correction, {len(marks)} two-site conjugate involutions realize all anti-diagonals; all nine true cosets of a correlated nine-element diagonal partition M². Switching to the anti-diagonal (same projections) gives an actual marked-square collision.')
def numeric():
 # Independent group-order upper DP from orbits, blocks and regular affine primitive alternatives;
 # this is a bound, not an enumeration of permutation groups.
 def odd(x):
  while x%2==0:x//=2
  return x
 def primes(m):return [p for p in range(3,m+1,2) if all(p%j for j in range(2,isqrt(p)+1))]
 H=[1,1];aff={}
 for p in primes(255):
  k=1;t=p
  while t<=255:
   aff[t]=t*odd(prod(t-p**j for j in range(k)));k+=1;t*=p
 for n in range(2,256):
  pos=[H[k]*H[n-k] for k in range(1,n)]
  pos += [H[a]**(n//a)*H[n//a] for a in range(2,n) if n%a==0]
  if n in aff:pos.append(aff[n])
  H.append(max(pos));assert H[n]**2<=3**(n-1)
 assert H[9]==81 and H[10]<=81
 assert aff[3]==3 and aff[5]==5 and aff[7]==21 and aff[9]==27
 assert 112**6<120**4*(112**2-2*1440)
 digits=[1,1]
 for n in range(2,251):
  actual=sum(factorial(n)//(2**k*factorial(k)*factorial(n-2*k)) for k in range(n//2+1))
  digits.append(actual)
  if n>=11:assert factorial(n)**2>16*actual**2*3**(n-1)
 print('Union/block/affine dynamic caps verified for every degree 1..255, odd natural action caps d=7..10:',H[7:11],'; direct involution conjugacy-class formula checked all large-degree inequalities 11..250, with exact exceptional A6 normalized bound <120.')
a6();numeric()
