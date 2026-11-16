#!/usr/bin/env python3
"""S5-equivariant quadratic maps from the six-point J to five-point N.

The two pairs of permutations are synchronized generators of S5.  J is
F2^6/constants, N is the even subspace of F2^5.  Python 3.11+; no I/O.
"""
from itertools import combinations
assert __debug__
c5=(1,0,2,3,4); d5=(0,2,3,4,1)
c6=(1,0,3,2,5,4); d6=(0,2,3,4,1,5)
def comp(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inv(a):return tuple(a.index(i) for i in range(len(a)))
def power(a,n):
 r=tuple(range(len(a)))
 for _ in range(n):r=comp(r,a)
 return r
def order(a):
 for n in range(1,121):
  if power(a,n)==tuple(range(len(a))):return n
 raise AssertionError
def add(p,v):
 while v:
  i=v.bit_length()-1
  if i in p:v^=p[i]
  else:p[i]=v;return True
 return False
def rank(vs):
 p={}
 for v in vs:add(p,v)
 return len(p)
def nact(v,p):
 out=0
 for i in range(4):
  if v>>i&1:out^=(1<<p[0])^(1<<p[i+1])
 return (out>>1)&15
def jact(v,p):
 out=0
 for i in range(5):
  if v>>i&1:out^=1<<p[i]
 return (out^63 if out&32 else out)&31
identity=(tuple(range(5)),tuple(range(6)));group={identity};queue=[identity]
for g in queue:
 for a,b in ((c5,c6),(d5,d6)):
  h=(comp(g[0],a),comp(g[1],b))
  if h not in group:group.add(h);queue.append(h)
assert len(group)==120 and len({g[0] for g in group})==120 and len({g[1] for g in group})==120
p=next(g for g in queue if order(g[0])==5)
cyclic={power(p[0],i) for i in range(5)}
F=[g for g in queue if comp(comp(g[0],p[0]),inv(g[0])) in cyclic]
assert len(F)==20
for v in range(1,16):assert rank(nact(v,g[0]) for g in F)==4
M=[1^(1<<i) for i in range(1,5)]
assert rank(M)==4 and all(rank(M+[jact(x,g[1])])==4 for x in M for g in group)
def combine(cols,mask):
 out=0
 for i,col in enumerate(cols):
  if mask>>i&1:out^=col
 return out
assert all(rank(jact(combine(M,v),g[1]) for g in F)==4 for v in range(1,16))
assert sum(all(jact(v,g[1])==v for g in F) for v in range(32))==2
assert rank((1<<i)^jact(1<<i,c6) for i in range(5))==2
assert rank((1<<i)^nact(1<<i,c5) for i in range(4))==1
# Coefficients encode four output bits for each linear/squarefree monomial.
mon=[(i,i) for i in range(5)]+list(combinations(range(5),2))
def feat(v):return sum(((v>>i&1)&(v>>j&1))<<k for k,(i,j) in enumerate(mon))
samples=[1<<i for i in range(5)]+[(1<<i)^(1<<j) for i in range(5) for j in range(i+1,5)]
rows=[]
for p5,p6 in ((c5,c6),(d5,d6)):
 for v in samples:
  f=feat(v);g=feat(jact(v,p6))
  for bit in range(4):
   row=0
   for k in range(15):
    if g>>k&1:row^=1<<(4*k+bit)
    if f>>k&1:
     for j in range(4):
      if nact(1<<j,p5)>>bit&1:row^=1<<(4*k+j)
   rows.append(row)
piv={}
for row in rows:add(piv,row)
assert len(piv)==59
solutions=[]
for i in range(60):
 if i in piv:continue
 v=1<<i
 for j in sorted(piv):
  if (piv[j]&v).bit_count()&1:v|=1<<j
 assert all((v&r).bit_count()%2==0 for r in rows)
 solutions.append(v)
assert len(solutions)==1
co=solutions[0]
def q(v):
 f=feat(v);out=0
 for i in range(15):
  if f>>i&1:out^=(co>>(4*i))&15
 return out
def polar(x,y):return q(x)^q(y)^q(x^y)
assert all(q(jact(v,g[1]))==nact(q(v),g[0]) for g in group for v in range(32))
values=[polar(M[i],M[j]) for i,j in combinations(range(4),2)]
assert rank(values)==4
print('Paired group 120; F20 order 20; N|F20 irreducible; t ranks J,N = 2,1')
print('Equivariant quadratic maps J -> N: dimension 1; polar image on M: rank 4')
