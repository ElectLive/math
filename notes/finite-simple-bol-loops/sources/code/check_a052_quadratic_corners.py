"""Independent controls for the even-rank ordinary residual, including q=9 nonprime."""
from fractions import Fraction
from math import prod,gcd
from itertools import product

def fops(q):
 p=3 if q==9 else q
 if q!=9:return (lambda x,y:(x+y)%p), (lambda x,y:(x*y)%p),(lambda x:-x%p)
 # F3[j]/(j²+1); j²=2
 return (lambda x,y:(x%3+y%3)%3+3*((x//3+y//3)%3)),(lambda x,y:(x%3*(y%3)+2*(x//3)*(y//3))%3+3*((x%3*(y//3)+(x//3)*(y%3))%3)),(lambda x:(-(x%3))%3+3*((-(x//3))%3))

def actual(q):
 add,mul,neg=fops(q)
 def powr(x,k):
  y=1
  for _ in range(k):y=mul(y,x)
  return y
 def mats(A,B):return tuple(add(mul(A[2*i],B[j]),mul(A[2*i+1],B[2+j])) for i,j in product(range(2),repeat=2))
 def det(A):return add(mul(A[0],A[3]),neg(mul(A[1],A[2])))
 def tensor(A,B):return tuple(mul(x,y) for x in A for y in B)
 c=next(x for x in range(1,q) if x not in {mul(y,y) for y in range(1,q)})
 ci=powr(c,q-2);P=(0,c,1,0);Qi=(0,ci,1,0);S=(1,0,0,neg(1));C=set(range(1,q));
 ops={a for a in product(range(q),repeat=4) if mats(a,a)==(c,0,0,c)};ops2={a for a in product(range(q),repeat=4) if mats(a,a)==(ci,0,0,ci)}
 phys={tensor(A,B) for A,B in product(ops,ops2)}
 assert len(ops)==len(ops2)==q*(q-1) and 2*len(phys)==len(ops)*len(ops2)
 E={g for g in product(range(q),repeat=4) if det(g)==1}
 orbit={mats(mats(g,P),(g[3],neg(g[1]),neg(g[2]),g[0])) for g in E};assert orbit==ops
 # In degree four, negative intertwiners on one block satisfy PX=-XP; two blocks give every full determinant, rank 2 by zeroing one.
 anti={g for g in product(range(q),repeat=4) if mats(P,g)==tuple(map(neg,mats(g,P)))}
 assert len(anti)==q*q and {det(g) for g in anti if any(g)}==C and all(det(g)!=0 for g in anti if any(g));assert {mul(det(g),det(S)) for g in anti if any(g)}==C
 for d in range(4,21,2):
  powers={powr(x,d) for x in C};tag=powr(neg(c),d//2);both=tag not in powers and mul(tag,neg(1)) in powers
  assert both==((q-1)&-(q-1)==d&-d and (d&-d)>=4)
 print('q / rank-2 quadratic SL-class / reciprocal-sign quotient / negative block norm determinants:',q,len(orbit),len(phys),len(C))

def orders():
 # Direct integer quotients, including many fields where q is not the characteristic.
 def pp(z,p):
  k=1
  while z%p==0:z//=p;k*=p
  return k
 def GL(n,q):return q**(n*(n-1)//2)*prod(q**i-1 for i in range(1,n+1))
 cases=0
 for q,p in [(3,3),(5,5),(7,7),(9,3),(13,13),(25,5),(27,3),(49,7),(81,3)]:
  for d in range(4,19,2):
   e=d//2;S=GL(d,q)//(q-1);T=S//gcd(d,q-1);Y=T*S;D=d*(d-1)//2
   CN=(GL(d,q)//GL(e,q*q))**2//2;assert pp(CN,p)==q**(d*d//2)
   if d==4 and q%4==1 and (q-1)%8==4:
    n=(q**4-1)//(q-1);idx=Fraction(n*n,q**4)+Fraction((q-1)**2*(q**3-1)**2,2)
    assert Fraction(Y)/idx>0 and Fraction(pp(idx.numerator,p),pp(idx.denominator,p))==Fraction(1,q**4)
   for m in range(1,d):
    rho=d-m
    for a in range(rho+1,d+1):
     x=d-a;up=Fraction(2*D-rho*(2*a-rho-1)+a*(a//(rho+1)+1)+x*(x+1),2)
     if d%4==0 and m%2==0 and m*m<=2*d-1 and d>=8:
      lo=Fraction(d*d,2)-1-min(2*d-1,a*(a-rho)); assert 25*5**int(2*(lo-up))>36*((rho+2)**2+1)**2;cases+=1
 print('Exact nonsplit characteristic parts and mixed-gap support comparisons:',cases)
if __name__=='__main__':
 for q in (3,5,9):actual(q)
 orders()
