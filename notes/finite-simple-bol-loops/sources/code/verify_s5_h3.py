#!/usr/bin/env python3
"""Exact H^3(S5,F2) computation by normalized bar cochains and stable elements.

All groups are explicit permutations on five points. The Sylow subgroup is
D8=< (1234), (13) >. Compute H^3(D8,F2), then test every one of its 16
classes against all 120 conjugations using the appropriate intersection.
Cartan--Eilenberg, Homological Algebra, XII section 10, Theorem 10.1 supplies
the stable-elements identification; see bruck-s5-dimension-five.md.
No network, randomization or external algebra package is used.
"""
from itertools import permutations, product
from collections import Counter
P=list(permutations(range(5))); identity=tuple(range(5))
def mul(a,b): return tuple(a[b[i]] for i in range(5))
def inv(a): return tuple(a.index(i) for i in range(5))
a=(1,2,3,0,4); b=(2,1,0,3,4)
S={identity}; todo=[identity]
while todo:
 x=todo.pop()
 for y in (a,b):
  z=mul(x,y)
  if z not in S:S.add(z);todo.append(z)
S=tuple(sorted(S)); assert len(S)==8

def pivadd(basis,x):
 while x:
  p=x.bit_length()-1
  if p in basis:x ^= basis[p]
  else:basis[p]=x;return True
 return False

def reduce(basis,x):
 while x:
  p=x.bit_length()-1
  if p not in basis:return x
  x ^= basis[p]
 return 0

def drow(t,idx):
 # inhomogeneous normalized bar differential, trivial F2 coefficients
 n=len(t)-1; terms=[t[1:],t[:-1]]
 for i in range(n):terms.append(t[:i]+(mul(t[i],t[i+1]),)+t[i+2:])
 r=0
 for s in terms:
  if identity not in s:r ^= 1<<idx[s]
 return r

def setup(G):
 X=tuple(x for x in G if x!=identity)
 pairs=list(product(X,repeat=2)); triples=list(product(X,repeat=3)); i2={x:i for i,x in enumerate(pairs)};i3={x:i for i,x in enumerate(triples)}
 # columns of d2 are vectors in C3
 cols=[0]*len(pairs)
 for j,t in enumerate(triples):
  row=drow(t,i2)
  while row:
   bit=row & -row; cols[bit.bit_length()-1] |= 1<<j;row ^= bit
 B={}
 for c in cols:pivadd(B,c)
 return X,triples,i3,cols,B

X,trips,idx,cols,B=setup(S)
D={}
for t in product(X,repeat=4):pivadd(D,drow(t,idx))
# Check each d2 column in kernel d3, not just ranks.
assert all((row & col).bit_count()%2==0 for row in D.values() for col in cols)
# Nullspace: echelon pivots are largest bits, so solve ascending.
Z=[]
for f in range(len(trips)):
 if f in D:continue
 v=1<<f
 for p in sorted(D):
  if (D[p]&v).bit_count()%2:v|=1<<p
 assert all((r&v).bit_count()%2==0 for r in D.values())
 Z.append(v)
H=dict(B); reps=[]
for z in Z:
 if pivadd(H,z):reps.append(z)
assert len(Z)==len(trips)-len(D) and len(H)==len(B)+len(reps)
print('S order',len(S),'d2 rank',len(B),'d3 rank',len(D),'Z3 dimension',len(Z),'H3 dimension',len(reps),flush=True)
# Q-dependent cochain space and coboundary basis, cached by subgroup.
cache={}; tests=[]; hist=Counter()
for g in P:
 gi=inv(g)
 Q=tuple(x for x in S if mul(mul(g,x),gi) in S)
 if Q not in cache:cache[Q]=setup(Q)
 qx,qt,qi,qcols,qB=cache[Q]
 hist[len(Q)]+=1
 # Matrix of differences on each S-cohomology generator.
 diffs=[]
 for c in reps:
  v=0
  for i,t in enumerate(qt):
   gt=tuple(mul(mul(g,x),gi) for x in t)
   if ((c>>idx[t])^(c>>idx[gt]))&1:v |=1<<i
  diffs.append(v)
 tests.append((qB,diffs))
stable=[]
for mask in range(1<<len(reps)):
 ok=True
 for qB,diffs in tests:
  v=0
  for i,d in enumerate(diffs):
   if mask>>i&1:v^=d
  if reduce(qB,v):ok=False;break
 if ok:stable.append(mask)
print('intersection order histogram',sorted(hist.items()))
print('distinct intersections',len(cache),'stable masks',stable,'number',len(stable))
assert len(stable)==8
assert len(stable) & (len(stable)-1) == 0
print("H3(S5,F2) dimension", len(stable).bit_length()-1)
