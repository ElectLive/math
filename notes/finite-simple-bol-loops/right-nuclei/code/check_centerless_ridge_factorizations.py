"""Ridge interpolation and a full small X: all native points, normalizers, spectrum and commutant."""
from itertools import product
from math import gcd,lcm,prod
from collections import Counter
from random import Random
R=Random(197103677)
def sm(fs,p):return tuple(sum(a[i] for a in fs)%t for i,t in enumerate(p))
def order(a,q):return next(i for i in range(1,q) if pow(a,i,q)==1)
def ridges(p,q):
 k=len(p);P=list(product(*(range(t) for t in p)));V=list(product(range(q),repeat=k));u=prod(p);g=gcd(*p)
 cs=[next(a for a in range(2,q) if order(a,q)==t) for t in p]
 dirs=[(1,)+x for x in product(range(1,q),repeat=k-1)]
 rs=set(dirs);orbits=[]
 while rs:
  w=min(rs);orb=set()
  for h in P:
   y=[x*pow(c,z,q)%q for x,c,z in zip(w,cs,h)]
   orb.add(tuple(x*pow(y[0],-1,q)%q for x in y))
  assert len(orb)==u//g;rs-=orb;orbits.append(orb)
 for t in {1,min(g,len(orbits)),len(orbits)}:
  family=sorted(set.union(*orbits[:t]));dt=(q-1)*len(family);rec=0
  for rep in range(2):
   F=[]
   for d in family:
    f=[tuple(R.randrange(b) for b in p) for _ in range(q-1)]
    f.append(tuple(-sum(v[i] for v in f)%b for i,b in enumerate(p)));F.append(f)
   L=lambda f,x:sum(a*b for a,b in zip(f,x))%q
   raw={x:sm([f[L(d,x)] for d,f in zip(family,F)],p) for x in V}
   for d,f in zip(family,F):
    for a in range(q):
     w=sm([val for x,val in raw.items() if L(d,x)==a],p)
     assert tuple(v*pow(q**(k-1),-1,b)%b for v,b in zip(w,p))==f[a];rec+=1
  print('ridge P,q,selected directions,additive rank,exact inverse bins:',p,q,len(family),dt,rec,'same m=1 central family order:',dt==u*(q-1))
# Full q7 grid ; every single x gives the actual pair (xK,x^{-1}J).
p,q=3,7;a=2;zero=(0,)*q
def plus(v,w):return tuple((x+y)%p for x,y in zip(v,w))
def scale(v,c):return tuple(c*x%p for x in v)
perms={(i,j):tuple((t-i)*pow(a,-j,q)%q for t in range(q)) for i in range(q) for j in range(p)}
def act(v,i,j):return tuple(v[s] for s in perms[i,j])
def mul(x,y):
 v,b,j=x;w,c,h=y
 return plus(v,act(w,b,j)),(b+pow(a,j,q)*c)%q,(j+h)%p
def inv(x):
 v,b,j=x;c=-pow(a,-j,q)*b%q;h=-j%p
 return scale(act(v,c,h),-1),c,h
I=(zero,0,0);V=[s+(-sum(s)%p,) for s in product(range(p),repeat=q-1)]
S=[(v,i,j) for v in V for i in range(q) for j in range(p)]
inK=lambda x:x[1]==0 and x[2]==x[0][0]
inJ=lambda x:x[0]==zero
K=[x for x in S if inK(x)];J=[x for x in S if inJ(x)];assert len(K)*len(J)==len(S) and set(K)&set(J)=={I}
def di(i):
 x=[0]*q;x[i]=1;x[-1]=p-1;return tuple(x)
kg=[(di(i),0,0) for i in range(1,q-1)]+[(di(0),0,1)]
jg=[(zero,1,0),(zero,0,1)];generators=kg+jg
def gen(v):
 T={I}; todo=[I]
 while todo:
  g=todo.pop()
  for a in v:
   x=mul(g,a)
   if x not in T:T.add(x);todo.append(x)
 return T
assert gen(kg)==set(K) and gen(jg)==set(J) and gen(generators)==set(S)
hfix=z=normal1=normal2=0;spec=Counter();comm=[]
# Extra probes are real loop marks corresponding to products of genuine X
# generators; we do NOT infer loop commutativity from testing generators.
probes=set(generators)|{mul(x,y) for x in generators for y in generators}
for x in S:
 ix=inv(x);assert mul(x,ix)==I
 a1=all(inK(mul(mul(ix,k),x)) for k in kg)
 a2=all(inJ(mul(mul(x,j),ix)) for j in jg)
 hfix+=bool(a1 and a2);normal1+=a1;normal2+=a2
 z+=all(mul(g,x)==mul(x,g) for g in generators)
 if all(inK(mul(mul(ix,inv(b)),mul(x,b))) and inJ(mul(mul(x,b),mul(ix,inv(b)))) for b in probes):comm.append(x)
 h=x;t=1
 while h!=I:h=mul(h,x);t+=1;assert t<=9
 spec[t]+=1
assert hfix==3 and normal1==len(K)*3 and normal2==len(J) and z==1 and comm==[I] and set(spec)=={1,3,7,9}
print('All actual order-15309 loop points: H-fixed cosets, native normalizers |N_X(K)|,|N_X(J)|, Z(X), universally commuting survivors:',hfix,normal1,normal2,z,len(comm))
print('Exact entire native mark order distribution:',sorted(spec.items()),'tested all literal commutator probes:',len(probes))
for p,q in (((9,),19),((3,3),19),((3,5),31)):ridges(p,q)
