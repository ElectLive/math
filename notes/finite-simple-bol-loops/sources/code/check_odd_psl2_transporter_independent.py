"""Independent actual projective and semilinear checks for 8d2c3f54 (stdlib only)."""
from itertools import product
from math import isqrt
class Quadratic:
 def __init__(self,p,t):
  self.p=p;self.t=t;self.q=p*p
  assert pow(t,(p-1)//2,p)==p-1
  self.add=[[((x%p+y%p)%p)+p*((x//p+y//p)%p) for y in range(self.q)] for x in range(self.q)]
  self.mul=[[((x%p*(y%p)+t*(x//p)*(y//p))%p)+p*((x%p*(y//p)+(x//p)*(y%p))%p) for y in range(self.q)] for x in range(self.q)]
  self.inv=[0]+[self.mul[x].index(1) for x in range(1,self.q)]
  self.neg=[r.index(0) for r in self.add]
  self.sq={self.mul[x][x] for x in range(1,self.q)}
  self.id=tuple(range(self.q+1));self.fr=tuple(self.pow(x,p) for x in range(self.q))+(self.q,)
 def pow(self,x,m):
  a=1
  for _ in range(m):a=self.mul[a][x]
  return a
 def det(self,w):
  a,b,c,d=w;return self.add[self.mul[a][d]][self.neg[self.mul[b][c]]]
 def perm(self,a,b,c,d):
  assert self.det((a,b,c,d))
  q=self.q;M=self.mul;A=self.add
  def rat(x,y):return q if not y else M[x][self.inv[y]]
  return tuple(rat(A[M[a][x]][b], A[M[c][x]][d]) for x in range(q))+(rat(a,c),)
def cm(a,b):return tuple(a[i] for i in b)
def inv(p):
 q=[0]*len(p)
 for i,j in enumerate(p):q[j]=i
 return tuple(q)
def conj(a,p):return cm(cm(a,p),inv(a))
def wreath(s,arr):
 q=len(arr[0]);return tuple(q*s[i]+arr[i][x] for i in range(len(s)) for x in range(q))
def q9():
 A=Quadratic(3,2);pgl=set();T=set()
 for index in range(4):
  for rest in product(range(9),repeat=3-index):
   w=(0,)*index+(1,)+rest
   if not A.det(w):continue
   u=A.perm(*w);pgl.add(u)
   if A.det(w) in A.sq:T.add(u)
 sem={cm(x,A.fr) for x in pgl};Q=pgl|sem
 assert (len(T),len(pgl),len(Q))==(360,720,1440)
 fixed=lambda H:{p for p in H if cm(p,p)==A.id}
 s0,s1,si=fixed(pgl),fixed(sem),fixed(T)
 assert len(s0)==82 and len(s1)==30 and len(si)==46
 assert {conj(p,A.fr) for p in pgl}==s1
 assert len({p for p in pgl if cm(p,A.fr)==cm(A.fr,p)})==24
 z=next(i for i in si if i!=A.id);assert {conj(g,z) for g in T}==si-{A.id}
 # Entire rational Borel and its actual odd slope preimage, not just valuations.
 B={a for a in T if a[-1]==9};O={a for a in B if all(a[x]==A.add[a[0]][x] for x in range(9))}
 assert len(B)==36 and len(O)==9
 I,V,L=112,1440,360
 assert I**6<120**4*(I*I-2*V) and len(O)==(L//120)**2
 print("q=9: full 1,440 actual semilinear permutations on 10 points; inner/PGL/field-coset square-one counts 46/82/30, one actual inner involution class, one Frobenius class with PGL-centralizer 24. Rational Borel size 36; odd-slope kernel 9; strict terminal inequality.")
def q49():
 A=Quadratic(7,3);I=A.id;F=A.fr;sig=(1,0);J=A.perm(0,1,1,0)
 # An order-four swap transporter and a different paired involution generate a genuine 2-group.
 h0=wreath(sig,(I,F));l0=wreath(sig,(F,F));Id=wreath((0,1),(I,I))
 subgroup={Id};front=[Id]
 while front:
  a=front.pop()
  for b in (h0,l0):
   v=cm(a,b)
   if v not in subgroup:subgroup.add(v);front.append(v)
 assert len(subgroup)==8 and cm(h0,h0)!=Id and cm(cm(h0,h0),cm(h0,h0))==Id
 assert cm(l0,l0)==Id and F!=I
 assert A.mul[2][2]==4 and A.mul[2][4]==1
 assert F[2]==2 and F[4]==4 and sum(F[i]==i for i in range(49))==7
 gauge=[A.perm(1,7,0,1),A.perm(0,1,1,6)]
 base=wreath((0,1),gauge);h=conj(base,h0);lam=conj(base,l0)
 for sign,d1 in [(1,2),(-1,4)]:
  W=[conj(a,A.perm(u,0,0,1)) for a,u in zip(gauge,(2,d1))]
  w=wreath((0,1),W); assert cm(cm(w,w),w)==Id and w!=Id
  assert conj(h,w)==(w if sign==1 else inv(w))
  # J is inner in this field, as -1 is a square. Multipliers used below also square.
  assert A.neg[1] in A.sq and {2,4}<=A.sq
  raw=cm(J if sign==1 else I,F)
  phi=cm(gauge[1],cm(raw,inv(gauge[0])))
  L=cm(gauge[1],cm(F,inv(gauge[0])))
  rr=cm(phi,inv(L))
  assert rr==conj(gauge[1],J if sign==1 else I)
  def paired(u):return wreath(sig,(u,inv(u)))
  x=paired(phi);y=paired(cm(phi,W[0]))
  # Actual single-site inner conjugators of the original mark, not only the right outer label.
  cx=wreath((0,1),(I,cm(phi,inv(L))))
  cy=wreath((0,1),(I,cm(cm(phi,W[0]),inv(L))))
  assert conj(cx,lam)==x and conj(cy,lam)==y and cm(x,y)==w
  assert W[0][0]!=0
 print("q=49: honest common group of order 8 on 100 points, h order 4 and λ order 2 with same permutation but DIFFERENT full field arrows. Both eigensigns on μ3 lift to actual mixed-frame inner slopes with nonzero translations and products of two explicitly inner-conjugate marks.")
def arith():
 num=0
 for p in range(3,400,2):
  if any(p%r==0 for r in range(2,isqrt(p)+1)):continue
  q=p;f=1
  while q<=10**9:
   if q>=5:
    l=q*(q*q-1)//2; v=2*f*l
    i=q*q+1+(isqrt(q)*(q+1) if f%2==0 else 0)
    if f%2==0 or q in [7,11,13]:
     c=q if f%2 else q*(q-1)//8
     assert i*i>2*v and c*c*i**6<l**4*(i*i-2*v)
    elif q>=17:assert 4*i*i*q<l*l
    num+=1
   f+=1;q*=p
 print(f"{num} independent exact prime-power comparisons through 10^9 (odd base primes <400); q=5 intentionally left to the separate A5 input.")
if __name__=='__main__':q9();q49();arith()
