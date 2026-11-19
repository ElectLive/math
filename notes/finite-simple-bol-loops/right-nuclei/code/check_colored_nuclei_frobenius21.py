"""Independent check for the fixed-envelope theorem; no author routines imported.
P is the entire true auxiliary group, realized sparsely. Its marked points form
a native subloop since S,T factor P exactly; no giant ambient table is simulated."""
from itertools import product
from collections import Counter
from functools import lru_cache
import random
import numpy as np
rng=random.Random(219345)
def pw(x,n):
 a=np.eye(3,dtype=int)
 while n:
  if n%2:a=a@x%11
  x=x@x%11;n//=2
 return a
I=np.eye(3,dtype=int)
X=np.array([[0,0,-1],[1,0,0],[0,1,-4]])%11;C=I+X
A=np.column_stack([pw(X,11*j)[:,0] for j in range(3)]);T=C@A%11
C0=[I,C,pw(C,2)]
Z=[pw(C,190*i) for i in range(7)]
As=[[pw(a,i) for i in range(3)] for a in (A,C@A@pw(C,1329)%11)]
vs=list(product(range(11),repeat=3));ns={v:i for i,v in enumerate(vs)}
def vm(M):return tuple(ns[tuple(row)] for row in np.array(vs)@M.T%11)
def det(x):return round(np.linalg.det(x))%11
def inv(x):
 a=np.concatenate((x%11,I),axis=1)
 for j in range(3):
  i=next(i for i in range(j,3) if a[i,j]);a[[j,i]]=a[[i,j]];a[j]=a[j]*pow(int(a[j,j]),-1,11)%11
  for i in range(3):
   if i!=j:a[i]=(a[i]-a[i,j]*a[j])%11
 assert (a[:,:3]==I).all();return a[:,3:]
assert (pw(C,1330)==I).all() and all(not(pw(C,1330//s)==I).all() for s in (2,5,7,19))
z=list(map(vm,Z));c=list(map(vm,C0));t=vm(T);fr=[list(map(vm,x)) for x in As]
dif={e:vm(inv(T-C0[e])) for e in (0,2)}
assert [i for i in range(1331) if c[1][i]==t[i]].__len__()==11
@lru_cache(49152)
def add(x,y):return ns[tuple((a+b)%11 for a,b in zip(vs[x],vs[y]))]
neg=[ns[tuple(-a%11 for a in x)] for x in vs]
def fm(x,y):return add(x[0],z[x[1]][y[0]]),(x[1]+y[1])%7
def fi(x):return z[-x[1]%7][neg[x[0]]],-x[1]%7
def fa(x,w,i):return fr[w][i][x[0]],pow(4,i,7)*x[1]%7
def theta(x):return t[x[0]],4*x[1]%7
def psi(x,e):return c[e][x[0]],x[1]
F1=(0,0)
def decomposition(x,y,e):
 h=(y[1]-x[1])*5%7;k=(x[1]-h)%7
 d=dif[e][z[-k%7][add(y[0],neg[c[e][x[0]]])]]
 s=(add(x[0],neg[z[k][d]]),k);d=(d,h)
 assert fm(s,d)==x and fm(psi(s,e),theta(d))==y
 return s,d
for e in (0,2):
 for u,i,j in product(range(1331),range(7),range(7)):decomposition((u,i),((2*u+3)%1331,j),e)
matches=[]
for a,b,i in product([0,2],[0,2],range(3)):
 arrow=C0[b]@As[0][i]%11;arrow=As[1][i]@C0[a]@inv(arrow)%11
 if any((arrow==s).all() for s in Z):matches.append((a,b,i))
assert matches==[(0,0,0),(2,2,0)]
# U is the Frobenius group of order 21; 4 acts mod7 with order three.
U=list(product(range(7),range(3)));ui={x:i for i,x in enumerate(U)};n=len(U)
def m(x,y):return ui[((U[x][0]+pow(4,U[x][1],7)*U[y][0])%7,(U[x][1]+U[y][1])%3)]
iv=[next(j for j in range(n) if m(i,j)==0) for i in range(n)]
top=lambda i:({},0,i)
def pm(x,y):
 d,s,r=x;dd,ss,rr=y;b=d.copy()
 for (j,w),v in dd.items():
  key=m(r,j),w;h=fm(b.get(key,F1),fa(v,w,s))
  if h==F1:b.pop(key,None)
  else:b[key]=h
 return b,(s+ss)%3,m(r,rr)
def pi(x):
 d,s,r=x;i=(-s)%3;u=iv[r];return {(m(u,j),w):fa(fi(h),w,i) for (j,w),h in d.items()},i,u
def factor(x,colors):
 d,s,r=x;l={};t0={}
 for j in set(j for (j,w) in d):
  e=2*int(j in colors);v,w=decomposition(d.get((j,0),F1),d.get((j,1),F1),e)
  if v!=F1:l[j,0]=v;l[j,1]=psi(v,e)
  if w!=F1:t0[j,0]=w;t0[j,1]=theta(w)
 k=(l,0,0);j0=(t0,s,r)
 assert pm(k,j0)==x;return k,j0
def native(x,y,colors):
 # Solve aH=d_zH with a=d_x d_y, using KJ on each signed component.
 a=pm(x,y);b=pm(pi(x),pi(y));_,j=factor(pi(a),colors);k,_=factor(b,colors);z0=pm(pi(j),pi(k))
 ik,jj=factor(pm(pi(z0),a),colors);kk,jj2=factor(pm(z0,b),colors)
 assert jj==top(0) and kk==top(0)
 return z0
subsets={frozenset({0}),frozenset(range(n))}
for r in range(1,n):
 h={r};x=m(r,r)
 while x not in h:h.add(x);x=m(x,r)
 subsets.add(frozenset(h))
assert Counter(map(len,subsets))=={1:1,3:7,7:1,21:1}
h=next(h for h in subsets if len(h)==3);u=next(i for i in range(n) if i not in h and U[i][1]==0)
ag=lambda r:m(m(u,r),iv[u]);conj=frozenset(map(ag,h));assert conj!=h and conj in subsets
def translate(r,s):return {m(r,c) for c in s}
assert not any(translate(r,h)==conj for r in range(n))
def lift(x):
 d,s,r=x;return {(ag(j),w):v for (j,w),v in d.items()},s,ag(r)
def ran():
 d={}
 for j,w in [(rng.randrange(n),rng.randrange(2)) for _ in range(5)]:
  v=rng.randrange(1,1331),rng.randrange(7);d[j,w]=v
 return d,rng.randrange(3),rng.randrange(n)
colors=[h,conj,next(s for s in subsets if len(s)==7),frozenset(),frozenset({0,1,3,7}),frozenset(range(n))]
for s in colors:
 # literal one-site coefficient mark queries and native associators on actual P, not projected arrows
 failures=Counter(); tests=0
 for j in range(n):
  a=({(j,0):(0,1),(j,1):(0,1)},0,0)
  e=2*int(j in s);p=(121,0);b=({(j,0):p,(j,1):psi(p,e)},0,0)
  bb=({(j,0):p,(j,1):p},0,0)
  ab=native(a,b,s);assert ab==pm(b,a);assert (native(a,bb,s)==pm(bb,a))==(e==0)
  for r in range(n):
   good=native(ab,top(r),s)==native(a,native(b,top(r),s),s)
   assert good==((j in s)==(m(iv[r],j) in s));failures[r]+=not good;tests+=1
 for r in range(n):
  assert failures[r]==len(s^translate(r,s))
  for q in range(n):assert native(top(r),top(q),s)==top(m(r,q))
 print('colour',sorted(s),'true native associators',tests,'stabilizer order',sum(failures[r]==0 for r in range(n)))
for _ in range(350):
 x,y=ran(),ran();assert lift(pm(x,y))==pm(lift(x),lift(y))
 assert lift(native(x,y,h))==native(lift(x),lift(y),conj)
print('C7:C3 two distinct conjugate subgroups not left translates; 350 mixed native products transported by their coefficient relabeling')
# Transitive D-set counts: lattice above is complete by elementary group orders; colour fixed by H iff union of right H-orbits (left H-action).
a={};tot=Counter()
for H in sorted(subsets,key=len,reverse=True):
 a[H]=2**(n//len(H))-sum(v for S,v in a.items() if H<S);tot[len(H)]+=a[H]
assert sum(tot.values())==2**n
orbits={s:v//(n//s) for s,v in sorted(tot.items())}
assert orbits=={1:99822,3:126,7:2,21:2}
burn=sum(2**(n//next(len(s) for s in subsets if u in s and len(s) in ([1] if u==0 else [3,7]))) for u in range(n))//n
assert burn==sum(orbits.values())
print('2^21 exact colouring D-set orbit counts by stabilizer order',orbits,'Burnside',burn)
print('local physical factor checks',2*1331*49,'det(e=0,2)',[det(T-C0[i]) for i in [0,2]],'bad e=1 intersection',sum(c[1][i]==t[i] for i in range(1331)))
