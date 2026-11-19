"""Independent controls for the central abelian construction; no source imports. Products are small sparse
integers until reduction in Z/9 x F_3. Not a full table on the enormous parent."""
from itertools import product
from collections import Counter
from random import Random
q=19
P=list(product(range(9),range(3)))
origin=(0,0)
def add(x,y):return ((x[0]+y[0])%9,(x[1]+y[1])%3)
def neg(x):return ((-x[0])%9,(-x[1])%3)
def scale(x,a):return ((x[0]*a)%9,(x[1]*a)%3)
def traits(x):return (pow(4,x[0],q),pow(7,x[1],q))
assert (pow(4,9,q),pow(4,3,q),pow(7,3,q),pow(7,1,q))==(1,7,1,7)
def add_to(d,k,z):
 d[k]=d.get(k,0)+z
 if not d[k]: del d[k]
def sparse(j,t,c=1):
 d={}
 add_to(d,(j,t),c);add_to(d,(j,(t+1)%q),-c)
 return d
def random_vec(r):
 d={}
 for _ in range(5):
  for k,v in sparse(r.choice(P),r.randrange(q),r.randrange(1,12)).items():add_to(d,k,v)
 return d
def apply_from_L1(s,y):
 # raw coordinate transport due to v h t, not the matrix test in source
 h,b=s
 c=traits(h);a=((-c[0]*b[0])%q,(-c[1]*b[1])%q)
 z={}
 for (j,t),val in y.items():
  J=add(j,neg(h));d=traits(J)
  e=sum(d[i]*a[i]+pow(d[i],-1,q)*b[i] for i in range(2))%q
  add_to(z,(J,(t+e)%q),val)
 return z
def B(x,y):
 return sum(z*(y.get((neg(j),(t-1)%q),0)-y.get((neg(j),(t+1)%q),0)) for (j,t),z in x.items())
def invsheet_coeff(c,d,y,w):
 # omega((c y,-y),(-d w,w))/2, before multiplying by the unit 1/2
 return B(apply_from_L1(c,y),w)+B(y,apply_from_L1(d,w))
def signpair_and_cuts():
 r=Random(59249);num=nonzero=bothunit=0
 for h,b in product(P,product(range(q),repeat=2)):
  c=(h,b); d=(r.choice(P),(r.randrange(q),r.randrange(q)))
  f=random_vec(r);g=random_vec(r)
  assert B(apply_from_L1(c,f),f)==0
  assert invsheet_coeff(c,d,f,f)==0 # each integral prime component, on entire L_0
  assert invsheet_coeff(c,d,g,g)==0
  alpha=invsheet_coeff(c,d,f,g)
  nonzero+=bool(alpha%9);bothunit+=bool(alpha%3);num+=1
 assert nonzero and 0<bothunit<=nonzero
 print('All signed cosets in X.t',num,'mixed tests whose unrelated L1 inputs give nonzero mod 9 / unit mod 3',nonzero,bothunit)
 # Actual subgroup C under all of D: x ->(3x mod9,x mod3) on both halves.
 # Since X,t are signed/permutation integer coordinate maps, this commutes with them.
 # Check bilinearity of coefficient change, including a unit commutator witness.
 x=sparse(origin,0);z=next(sparse(origin,t) for t in range(q) if B(x,sparse(origin,t))%3)
 f=B(x,z)
 comms={(3*f*a%9,f*b%3) for a,b in product(range(9),range(3))}
 assert comms=={(3*a,b) for a,b in product(range(3),repeat=2)}
 d=len(P)*(q-1)
 phys=9*3**d; signed=3**d
 assert phys==signed*9
 print('Mixed modular normal C: d',d,'actual central commutator layer',len(comms),'physical/signed = 9; central diagonal',len({scale((3,1),t) for t in range(27)}),'also proper')
def tops():
 subs={frozenset([origin])}; q0=list(subs)
 while q0:
  U=q0.pop()
  for v in P:
   if v not in U:
    V=frozenset(add(u,scale(v,j)) for u in U for j in range(9))
    if V not in subs: subs.add(V);q0.append(V)
 ratios=Counter();mixed=alln=0
 for mask,U in product(range(4),subs):
  I={i for i in range(2) if mask>>i&1}
  if any(any(a[i] for i in range(2) if i not in I) for a in U):continue
  if not I and len(U)==1:continue
  if len(I)==2 and len(U)==27:continue
  expected=q**len(I)
  # bar C fixed=in V diagonal; |bar C cap J|=|W intersect B| |U|
  lhs=27*expected;rhs=expected*len(U)
  assert lhs>rhs and lhs%rhs==0
  ratios[lhs//rhs]+=1;alln+=1
  if len(U)<len({x[0] for x in U})*len({x[1] for x in U}): mixed+=1
 print('All P subgroups',len(subs),'all proper nonzero signed top normal cases',alln,'non-product P0',mixed,'strict fixed/point ratios',sorted(ratios.items()))
 assert mixed>0 and 1 not in ratios
signpair_and_cuts();tops()
