"""Colored native factor experiment. The elementary field routines are reused from the separate universal right-nucleus audit;
the arbitrary colored factorization, literal nontrivial stabilizer tests and native query loops are new."""
from itertools import product
from collections import deque
from random import Random
from math import gcd
rnd=Random(102753)
# A different field basis: discover monic irreducible and primitive element instead of importing matrices.
p=11;q=p**3
def unpack(x):return x%p,x//p%p,x//(p*p)%p
def pack(a):return sum((v%p)*p**i for i,v in enumerate(a))
f,g=next((f,g)for f,g in product(range(1,p), repeat=2) if all((i**3+f*i+g)%p for i in range(p)))
def pm(x,y):
 a=unpack(x);b=unpack(y);v=[0]*5
 for i,j in product(range(3),repeat=2):v[i+j]+=a[i]*b[j]
 for i in (4,3):
  v[i-2]-=v[i]*f;v[i-3]-=v[i]*g
 return pack(v[:3])
def power(x,e):
 a=1
 while e:
  if e&1:a=pm(a,x)
  x=pm(x,x);e//=2
 return a
c=next(x for x in range(11,q)if all(power(x,(q-1)//t)!=1 for t in (2,5,7,19)))
ep=[1]
for _ in range(q-2):ep.append(pm(ep[-1],c))
lg={x:i for i,x in enumerate(ep)};assert len(lg)==q-1
def add(x,y):return pack([v+w for v,w in zip(unpack(x),unpack(y))])
def neg(x):return pack([-v for v in unpack(x)])
def scal(x,e):return ep[(lg[x]+e)%(q-1)] if x else 0
def fr(x,i):return ep[(lg[x]*11**i)%(q-1)] if x else 0
# Code (x,j) as x+q*j. zeta=c^190.
def mu(a,b):
 x,i=a%q,a//q;y,j=b%q,b//q
 return add(x,scal(y,190*i))+q*((i+j)%7)
def iv(a):
 x,i=a%q,a//q;return neg(scal(x,-190*i))+q*((-i)%7)
def auto(a,i,wing):
 x,j=a%q,a//q
 return scal(fr(x,i),wing*(1-11**i))+q*((j*pow(4,i,7))%7)
def theta(a):
 x,i=a%q,a//q
 return scal(fr(x,1),1)+q*(4*i%7)
nt=q*7
def psi(a,e):return scal(a%q,e)+q*(a//q)
L=[{}for _ in range(2)]
for i,e in enumerate([0,2]):
 for t in range(nt):L[i][mu(iv(psi(t,e)),theta(t))]=t
 assert len(L[i])==nt and sum(psi(t,e)==theta(t)for t in range(nt))==1
# Try EVERY true inner conjugator of the local group on the nonzero additive 1 AND z,
# rather than only inspecting the proportional exponents needed in the proof.
for i,e,d in product(range(3),(0,2),(0,2)):
 live=[]
 for w in range(nt):
  if all(mu(mu(w,psi(auto(x,i,0),d)),iv(w))==auto(psi(x,e),i,1) for x in (1,q)):live.append(w)
 assert live==([0] if e==d and i==0 else [])
print('all 12 relative-arrow tests over each of 9317 true inner conjugators; both nonlinear two-graph tables bijective')
def trial(U,op,tests):
 n=len(U);ix={x:i for i,x in enumerate(U)};M=[[ix[op(x,y)]for y in U]for x in U];mi=[a.index(0) for a in M];z=({},0,0)
 def pr(a,b):
  X,i,r=a;Y,j,s=b
  F=X.copy()
  for t,(u,v) in Y.items():
   g=M[r][t];x,y=F.get(g,(0,0));up=mu(x,auto(u,i,0));vp=mu(y,auto(v,i,1))
   if up or vp:F[g]=(up,vp)
   else:F.pop(g,None)
  return F,(i+j)%3,M[r][s]
 def ivp(a):
  X,i,r=a;j=(-i)%3;s=mi[r]
  return {M[s][g]:(auto(iv(x),j,0),auto(iv(y),j,1)) for g,(x,y) in X.items()},j,s
 for name,C,pure_H in tests:
  eps=[2*(j in C)for j in range(n)]
  def factor(a):
   X,i,r=a;B={};T={}
   for g,(x,y) in X.items():
    e=eps[g];t=L[e//2][mu(iv(psi(x,e)),y)];b=mu(x,iv(t))
    if b:B[g]=(b,psi(b,e))
    if t:T[g]=(t,theta(t))
   b,t=(B,0,0),(T,i,r);assert pr(b,t)==a
   return b,t
  def native(x,y):
   a=pr(x,y);b=pr(ivp(x),ivp(y));k1,j1=factor(ivp(a));k2,j2=factor(b);u=pr(ivp(j1),ivp(k2))
   s=pr(ivp(u),a);t=pr(u,b)
   assert s[1:]==(0,0) and all(y==psi(x,eps[g])for g,(x,y) in s[0].items()) and all(y==theta(x)for (x,y) in t[0].values())
   return u
  marks=[({},0,r)for r in range(n)]
  assert all(native(a,b)==marks[M[i][j]]for i,a in enumerate(marks)for j,b in enumerate(marks))
  # All n local bit tests and the full n-by-n associator matrix on real rather than symbolic marks.
  failures=[0]*n
  for j in range(n):
   a=({j:(q,q)},0,0);b0=({j:(1,1)},0,0);b=({j:(1,scal(1,eps[j]))},0,0)
   assert (native(a,b0)==pr(b0,a))==(eps[j]==0)
   u=native(a,b);assert u==pr(b,a)
   for r,m in enumerate(marks):
    fail=native(u,m)!=native(a,native(b,m));assert fail==(eps[j]!=eps[M[mi[r]][j]])
    failures[r]+=fail
  H={k for k,v in enumerate(failures)if not v}
  assert H=={r for r in range(n) if {M[r][j]for j in C}==C}
  if pure_H:
   assert H==C and all(v==2*len(C)for v in failures if v)
  print('ambient',n,name,'color population',len(C),'actual full nuclear group',len(H),'native ordered common-shell products checked',n*n,'associator failure distribution',[(x,failures.count(x))for x in sorted(set(failures))])
ua=list(product(range(3),repeat=4));mul=lambda u,v:((u[0]+v[0])%3,(u[1]+v[1])%3,(u[2]+v[2]+u[0]*v[1])%3,(u[3]+v[3])%3)
heis={i for i,x in enumerate(ua)if not x[3]};el27={i for i,x in enumerate(ua)if not x[1]};nn={i for i,x in enumerate(ua)if x[1:]==(0,0,0)}
def ds(U,S,op):
 ix={x:i for i,x in enumerate(U)}
 return sum(op(U[x],U[y])!=op(U[y],U[x])for x in S for y in S)
assert ds(ua,heis,mul)==432 and ds(ua,el27,mul)==0
trial(ua,mul,[('nonabelian H27',heis,True),('elementary H27',el27,True),('nonnormal H3',nn,True),('full H81',set(range(81)),True),('trivial H', {0},True),('non-subgroup, nonempty colored testing subset',{1,3,7,10,28,41},False)])
# Actual translate-orbits on every binary word of an abelian U with noncyclic group.
U=list(product(range(3),repeat=2));ix={x:i for i,x in enumerate(U)}
ap=[[ix[((x[0]+y[0])%3,(x[1]+y[1])%3)]for y in U]for x in U];left=set(range(512));hist={}
while left:
 s=min(left);o={sum(1<<p[i] for i in range(9)if s>>i&1)for p in ap};st=9//len(o);hist[st]=hist.get(st,0)+1;left-=o
assert sum(cnt*9//h for h,cnt in hist.items())==512
print('C3^2 all 512 subsets, exact action-orbit counts by stabilizer order',sorted(hist.items()))
