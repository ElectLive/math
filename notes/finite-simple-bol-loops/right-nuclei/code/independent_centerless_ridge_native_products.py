"""Independent physical coset multiplication and mixed-module tests for the centerless ridge construction.
The oracle factors a^-1 and b in X=KJ to recover the true mark of (a,b)H,
rather than testing membership in the two normalizers."""
from itertools import product
from math import gcd,prod,lcm
import numpy as np
rng=np.random.default_rng(71853)
def calculate(rs,q,t,target):
 k=len(rs);rs=np.array(rs,dtype=int);P=list(product(*(range(int(i)) for i in rs)));u=len(P)
 V=np.array(list(product(range(q),repeat=k)),dtype=int);n=len(V); enc=np.array([q**i for i in reversed(range(k))]);z=np.zeros(k,dtype=int)
 beta=[next(a for a in range(2,q) if next(i for i in range(1,q) if pow(a,i,q)==1)==r) for r in rs]
 def ch(h):return np.array([pow(a,int(i),q) for a,i in zip(beta,h)])
 ds={(1,)+s for s in product(range(1,q),repeat=k-1)};os=[]
 while ds:
  x=np.array(min(ds));O=set()
  for h in P:
   v=x*ch(h)%q;O.add(tuple(v*pow(int(v[0]),-1,q)%q))
  ds-=O;os.append(O)
 assert all(len(O)==u//gcd(*map(int,rs)) for O in os)
 # Pick deliberately nonconsecutive available orbits.
 ix=np.random.default_rng(922+k).choice(len(os),t,replace=False)
 dirs=sorted(set.union(*(os[j] for j in ix)));D=len(dirs);L=np.array(dirs);pts=V@L.T%q
 empty=np.zeros((n,k),dtype=int);I=(empty,z,z)
 def lift(F):return sum(F[j,pts[:,j]] for j in range(D))%rs
 def randomword():
  F=rng.integers(0,450,size=(D,q,k))%rs;F[:,-1,:]=-F[:,:-1,:].sum(axis=1)%rs;return lift(F)
 def onecol(j,one,neg,coeff):
  F=np.zeros((D,q,k),dtype=int);F[j,one]=coeff;F[j,neg]=-np.array(coeff);return lift(F)
 def dictkey(x):return tuple(map(int,x))
 def act(v,h,w):return w[(((V-v)*ch(-h))%q)@enc]
 def g(v,h):return empty,np.array(v),np.array(h)
 def W(w):return w,z,z
 def mul(a,b):
  wa,v,h=a;wb,vv,hh=b;return (wa+act(v,h,wb))%rs,(v+ch(h)*vv)%q,(h+hh)%rs
 def inv(a):
  w,v,h=a;v1=-v*ch(-h)%q;return -act(v1,-h,w)%rs,v1,-h%rs
 def eq(x,y):return all(np.array_equal(a,b) for a,b in zip(x,y))
 def factor(y):
  w,v,h=y;d=w[0].copy();return (w,z,d),g(v*ch(-d)%q,(h-d)%rs)
 def inK(a):return not a[1].any() and np.array_equal(a[2],a[0][0])
 def inJ(a):return not a[0].any()
 def mark(a,b):
  k,j=factor(inv(a));k2,j2=factor(b);c=mul(inv(j),inv(k2))
  assert inK(mul(inv(c),a)) and inJ(mul(c,b))
  return c
 def op(x,y):return mark(mul(x,y),mul(inv(x),inv(y)))
 def el():return randomword(),rng.integers(q,size=k),rng.integers(0,100,size=k)%rs
 def gp(x,n):
  y=I
  while n:
   if n&1:y=mul(y,x)
   x=mul(x,x);n//=2
  return y
 def hasord(x,n,primes):return eq(gp(x,n),I) and all(not eq(gp(x,n//p),I) for p in primes)
 # All nuclear candidates are actual distinct points and act on native products.
 testr=[np.array(t) for t in P];xs=[el() for _ in range(5)];bad=0;rc=0;assoc=0;actual=0
 for h in testr:
  nh=g(z,h); assert inK(factor(nh)[0]) and inJ(nh)
  for x,y in zip(xs,xs[1:]):
   assert eq(op(op(x,y),nh),op(x,op(y,nh)));rc+=1
   if eq(op(x,nh),op(nh,x)):continue
   bad+=1;break
 for _ in range(20):
  x,y,w=el(),el(),el()
  assert eq(op(x,op(y,op(x,w))),op(op(x,op(y,x)),w));actual+=1
  assoc+=not eq(op(op(x,y),w),op(x,op(y,w)))
 assert bad==u-1 and assoc
 # Check physical orders r^2 and rq by group powering; find actual order r^2
 # for a nonzero affine shift as well, not just the author's chosen h representative.
 r=lcm(*map(int,rs));h=np.ones(k,dtype=int);primes=[j for j in range(2,r+1) if r%j==0 and all(j%a for a in range(2,int(j**.5)+1))]
 zz=None
 for step in range(1,q):
  v=onecol(0,0,step,np.ones(k,dtype=int));x=(v,z,h)
  if hasord(x,r*r,primes):zz=x;break
 if zz is None:
  for step in range(2,q):
   v=onecol(0,1,step,np.ones(k,dtype=int));x=(v,z,h)
   if hasord(x,r*r,primes):zz=x;break
 assert zz is not None
 ex=mul(mul(g(np.ones(k,dtype=int),z),zz),g(-np.ones(k,dtype=int)%q,z))
 assert hasord(ex,r*r,primes) and ex[1].any()
 if k>=2:
  nu=next(v for v in V if v.any() and (v@L[0])%q==0);w=onecol(0,0,1,np.ones(k,dtype=int))
  assert hasord((w,nu,z),r*q,primes+[q])
 # Recover a deliberately nonsummand word module from its actual translated evaluations.
 # Cyclic order-three phases (3,0) in C9 x C3, all q^2 sites; complementary
 # module above would erroneously predict a line-preserving coordinate complement.
 if tuple(rs)==(9,3):
  w=onecol(0,1,2,(3,0)); vals={tuple(x) for x in w}
  assert vals=={(0,0),(3,0),(6,0)} and tuple(w[0])==(0,0)
  evals={tuple(act(v,z,w)[0]) for v in V};assert evals==vals
  assert all(any(np.any((act(v,z,w)-w)%rs) for v in V if v[i] and np.count_nonzero(v)==1) for i in range(k))
 # A dishonest input direction missing one coordinate yields a genuine nonzero
 # fixed by that axis, invalidating the key normal-cut commutator, even though
 # evaluation at 0 of translated words still detects every function.
 if k>=2:
  raw=np.zeros((q,k),dtype=int);raw[1,0]=1;raw[2,0]=rs[0]-1;false=raw[V[:,0]]
  last=np.zeros(k,dtype=int);last[-1]=1
  assert np.array_equal(act(last,z,false),false) and false.any()
 print('P',list(map(int,rs)),'q',q,'selected genuine directions',D,'true H-coset native left-Bol',actual,'right-nuclear tests',rc,'distinct nonidentity nuclear/noncommuting witnesses',bad,'failed associativity controls',assoc,'r^2 test with nonzero affine component',r*r,'mixed order',r*q if k>=2 else 'separately excluded')
 return (q-1)*D==u*(q-1)
assert calculate((9,3),19,1,False)==False
assert calculate((3,5),31,1,True)==True
calculate((9,),19,1,False)
