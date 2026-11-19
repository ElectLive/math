"""Finite checks of the actual coefficient group, both graph factors, faithful
prime-field representation, and normal signed-cut arithmetic. Never form the
v=23^49 site wreath or claim an exhaustive loop multiplication table."""
import itertools as it
from math import gcd
from collections import deque, Counter
import numpy as np
p=11; q=p**3
def digs(x):
 return (x%p,(x//p)%p,x//(p*p))
def enc(x):return sum(int(a)%p*p**i for i,a in enumerate(x))
def add(x,y):return enc([a+b for a,b in zip(digs(x),digs(y))])
def neg(x):return enc([-a for a in digs(x)])
mod=next((a,b,c) for a,b,c in it.product(range(1,p),range(p),range(p)) if all((a+b*j+c*j*j+j**3)%p for j in range(p)))
def mslow(x,y):
 d=[0]*5
 for i,a in enumerate(digs(x)):
  for j,b in enumerate(digs(y)):d[i+j]+=a*b
 for i in (4,3):
  for j,k in enumerate(mod):d[i-3+j]-=d[i]*k
 return enc(d[:3])
def pw0(x,k):
 y=1
 while k:
  if k&1:y=mslow(x,y)
  x=mslow(x,x);k//=2
 return y
c=next(x for x in range(2,q) if all(pw0(x,(q-1)//l)!=1 for l in (2,5,7,19)))
ex=[1]
for i in range(1,q-1):ex.append(mslow(ex[-1],c))
assert len(set(ex))==q-1
lg={x:i for i,x in enumerate(ex)}
def times(x,y):return ex[(lg[x]+lg[y])%(q-1)] if x*y else 0
def pw(x,k):return ex[(lg[x]*k)%(q-1)] if x else 0
z=ex[(q-1)//7];zm=[pw(z,i) for i in range(7)]
def tr(x):return add(add(x,pw(x,11)),pw(x,121))
assert all(tr(x)<11 for x in range(q))
F=list(it.product(range(q),range(7)));one=(0,0)
def m(x,y):return (add(x[0],times(zm[x[1]],y[0])),(x[1]+y[1])%7)
def auto(s,x):return times(s,pw(x[0],11)),(4*x[1])%7
def ai(x):return pw(x[0],121),(2*x[1])%7
def ti(x):return pw(times(pw(c,-1),x[0]),121),2*x[1]%7
s2=pw(c,1-11)
a=lambda x:auto(1,x)
t=lambda x:auto(c,x)
a2=lambda x:auto(s2,x)
gs=[(1,0),(0,1)]
def gen(m,id,G):
 seen={id};Q=deque([id])
 while Q:
  x=Q.popleft()
  for g in G:
   y=m(x,g)
   if y not in seen:seen.add(y);Q.append(y)
 return frozenset(seen)
assert len(gen(m,one,gs))==len(F)
for f in (a,t,a2):
 assert len({f(x) for x in F})==len(F) and all(f(m(x,g))==m(f(x),f(g)) for x in F for g in gs)
assert all(a2(x)==t(a(ti(x))) and a2(a2(a2(x)))==x and a(a(a(x)))==x for x in F)
assert [x for x in F if t(x)==x]==[one]
assert (q-1)//gcd(lg[pw(c,133)],q-1)==10
assert [x for x in F if all(m(x,g)==m(g,x) for g in gs)]==[one]
normalizing=[]
for i in range(3):
 scalar=pw(c,1-11**i);normalizing.append(scalar in zm)
 if i:assert (q-1)//gcd(lg[scalar],q-1)==133
assert normalizing==[True,False,False]
# Genuine fixed-free alternative tilt retaining the factorization but not N(S)=S:
d=next(d for d in range(2,11) if pow(d,3,11)!=1);alt=lambda x:auto(d,x)
assert [x for x in F if alt(x)==x]==[one] and all(alt(a(x))==a(alt(x)) for x in F)
print('F=F_1331^+:C7:',len(F),'actual elements; field modulus (ascending lower coefficients)',mod,'primitive c',digs(c),'seventh root',digs(z))
print('All 3 automorphisms agree on every element and each right-generator edge with multiplication; theta fixed points 1, theta^3 scalar order 10.')
print('Graph intersection trivial, F center trivial; relative outer scalar orders at powers 1,2: 133,133; inner-scalar powers',normalizing)
print('False control: scalar',d,'times Frobenius still fixed-free, but commutes with a; exact graph factorization then has outer normalizing lift.')
# Faithful 49-dimensional monomial representation in prime characteristic 23.
# First construct the TRUE 147 field actions on N=F_1331^+ x F_1331^+.
B=[1,p,p*p]
def matrix(f):return np.array([digs(f(x)) for x in B],dtype=np.int64).T
E=np.eye(3,dtype=np.int64);O=np.zeros((3,3),dtype=np.int64)
def block(X,Y):return np.block([[X,O],[O,Y]])%p
ZM=matrix(lambda x:times(z,x));A=matrix(lambda x:pw(x,11));A2=matrix(lambda x:times(s2,pw(x,11)))
G=[block(ZM,E),block(E,ZM),block(A,A2)];Id=np.eye(6,dtype=np.int64)
def key(z):return tuple(map(int,z.flatten()))
D={key(Id):Id};Q=deque([Id])
while Q:
 x=Q.popleft()
 for y in G:
  w=x@y%p
  if key(w) not in D:D[key(w)]=w;Q.append(w)
assert len(D)==147
L=np.array([tr(x) for x in B]+[tr(times(pw(c,-1),x)) for x in B],dtype=np.int64)
assert np.array_equal(L@G[2]%11,L)
orbit=sorted({tuple(map(int,L@h%11)) for h in D.values()});assert len(orbit)==49
weights=np.array(orbit,dtype=np.int64)
def rk(rows,p):
 a=rows.copy()%p;i=0
 for j in range(a.shape[1]):
  z=next((z for z in range(i,len(a)) if a[z,j]),None)
  if z is None:continue
  a[[i,z]]=a[[z,i]];a[i]=a[i]*pow(int(a[i,j]),-1,p)%p
  for k in range(len(a)):
   if k!=i:a[k]=(a[k]-a[k,j]*a[i])%p
  i+=1
 return i
assert rk(weights,p)==6
wi={w:i for i,w in enumerate(orbit)}
perm={k:np.array([wi[tuple(row)] for row in weights@h%11]) for k,h in D.items()}
assert len({tuple(z) for z in perm.values()})==147
rng=np.random.default_rng(12073);char=np.array([pow(2,i,23) for i in range(11)])
def act(n,h,v):return (char[weights@n%11]*v[perm[key(h)]])%23
coll=0
for h in D.values():
 for j in G:
  n,u=rng.integers(0,11,(2,6));v=rng.integers(0,23,49)
  assert np.array_equal(act(n,h,act(u,j,v)),act((n+h@u)%11,h@j%11,v));coll+=1
print('Actual P order',len(F)**2*3,'of which |P-prime|=',len(F)**2,
      '; 147 true actions on six kernel coordinates, 49 distinct character weights spanning rank 6.')
print('All 147 top matrices give distinct permutations of weights;',coll,'real composition equations tested over F23; native v=23^49, no full wreath enumeration.')
# All signed normal subgroups, not just the normal closures of individual elements, for two concrete control groups.
def topcheck(h3):
 if h3:
  P=list(it.product(range(3),repeat=3));id=(0,0,0)
  def mul(x,y):return ((x[0]+y[0])%3,(x[1]+y[1])%3,(x[2]+y[2]+x[0]*y[1])%3)
  def inv(x):return -x[0]%3,-x[1]%3,(x[0]*x[1]-x[2])%3
  def opp(x,y):return not (x[0]+y[0])%3 and not (x[1]+y[1])%3
  T=set(P)
 else:
  P=list(it.product(range(7),range(3)));id=(0,0)
  def mul(x,y):return (x[0]+pow(4,x[1],7)*y[0])%7,(x[1]+y[1])%3
  def inv(x):return -pow(4,-x[1],7)*x[0]%7,-x[1]%3
  def opp(x,y):return not (x[1]+y[1])%3
  T={x for x in P if x[0]==0}
 top=set((x,y) for x in P for y in P if opp(x,y));e=(id,id)
 prod=lambda x,y:(mul(x[0],y[0]),mul(x[1],y[1]))
 cn=lambda g,z:mul(mul(g,z),inv(g))
 # Precompute all tau-stable normal conjugacy classes and join them until closure under ALL normal subgroup additions.
 closures=set()
 for z in top:
  conj={(cn(g,z[0]),cn(h,z[1])) for g,h in top}
  conj|={(h,g) for g,h in conj};closures.add(gen(prod,e,conj))
 subs={frozenset([e])};todo=list(subs)
 while todo:
  n=todo.pop()
  for b in closures:
   if b.issubset(n):continue
   union=frozenset(prod(x,y) for x in n for y in b)
   if union not in subs:subs.add(union);todo.append(union)
 count=Counter();eqbad=0;nonprod=0
 for I in subs:
  U={x for x,y in I};M={x for x,y in I if y==id};fix={x for x,y in I if x==y};istar=sum(y in T for x,y in I)
  assert istar==len(M)*len(U&T)
  graph={frozenset(mul(x,v) for v in M):frozenset(mul(y,v) for v in M) for x,y in I}
  assert len(graph)==len(U)//len(M) and all(graph[graph[z]]==z for z in graph)
  assert len(fix)==len(M)*sum(x==y for x,y in graph.items())
  assert (len(T)*len(fix)>istar)==(len(I)<len(top))
  nonprod+=len(M)!=len(U);count[len(I)]+=1
  if not h3:
   badT={x for x in P if x[1]==0}
   eqbad+=len(I)<len(top) and len(badT)*len(fix)==sum(y in badT for x,y in I)
 print('Signed top',len(top),'all swap-normal subgroup sizes/counts',sorted(count.items()),'nonproduct rows',nonprod,'bad non-generating T proper equality counts',eqbad)
 if not h3:assert eqbad
topcheck(False);topcheck(True)
