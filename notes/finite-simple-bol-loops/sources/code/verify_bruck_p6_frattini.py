#!/usr/bin/env python3
"""S5 quadratic maps and F20 graph controls for a P6 Frattini shadow.

Coordinates: P6 is the six-point permutation module; M is the six-point
heart; N is the even five-point module. Python 3.11+, standard library.
"""
from itertools import combinations
assert __debug__
c5=(1,0,2,3,4);d5=(0,2,3,4,1)
c6=(1,0,3,2,5,4);d6=(0,2,3,4,1,5)
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
def mv(cols,v):
 out=0
 for i,x in enumerate(cols):
  if v>>i&1:out^=x
 return out
def pact(v,p):
 out=0
 for i in range(6):
  if v>>i&1:out^=1<<p[i]
 return out
def mact(v,p):
 out=0
 for i in range(4):
  if v>>i&1:out^=(1<<p[0])^(1<<p[i+1])
 if out&32:out^=63
 return (out>>1)&15
def nact(v,p):
 out=0
 for i in range(4):
  if v>>i&1:out^=(1<<p[0])^(1<<p[i+1])
 return (out>>1)&15
I=(tuple(range(5)),tuple(range(6)));group={I};queue=[I]
for g in queue:
 for a,b in ((c5,c6),(d5,d6)):
  h=(comp(g[0],a),comp(g[1],b))
  if h not in group:group.add(h);queue.append(h)
assert len(group)==120 and len({g[0] for g in group})==120 and len({g[1] for g in group})==120
p=next(g for g in queue if order(g[0])==5)
cyclic={power(p[0],i) for i in range(5)}
F=[g for g in queue if comp(comp(g[0],p[0]),inv(g[0])) in cyclic]
assert len(F)==20
qgen=next(g for g in F if order(g[0])==4)
assert len({comp(power(qgen[0],i),x) for i in range(4) for x in cyclic})==20
fixed=[i for i in range(6) if all(g[1][i]==i for g in F)]
assert len(fixed)==1
u1=1<<fixed[0];u2=63^u1
orbit=[i for i in range(6) if i!=fixed[0]]
S=[(1<<orbit[0])^(1<<i) for i in orbit[1:]]
assert rank(S+[u1,u2])==6
for v in range(1,16):
 assert rank(pact(mv(S,v),g[1]) for g in F)==4
for fn,ind in ((mact,1),(nact,0)):
 for v in range(1,16):assert rank(fn(v,g[ind]) for g in F)==4
assert rank((1<<i)^pact(1<<i,c6) for i in range(6))==3
assert rank((1<<i)^mact(1<<i,c6) for i in range(4))==2
assert rank((1<<i)^nact(1<<i,c5) for i in range(4))==1
# All F-intertwiners M -> N; the unique nonzero one defines the mixed graph.
intertwiners=[]
for mask in range(1<<16):
 cols=tuple((mask>>(4*i))&15 for i in range(4))
 if all(mv(cols,mact(1<<i,g[1]))==nact(cols[i],g[0]) for i in range(4) for g in (p,qgen)):
  intertwiners.append(cols)
assert len(intertwiners)==2
phi=next(cols for cols in intertwiners if any(cols));assert rank(phi)==4
fixed_graph=[v for v in range(16) if mact(v,c6)==v and nact(mv(phi,v),c5)==mv(phi,v)]
assert len(fixed_graph)==2
# All equivariant quadratic maps P6 -> each simple target.
mon=[(i,i) for i in range(6)]+list(combinations(range(6),2))
def feat(v):return sum(((v>>i&1)&(v>>j&1))<<k for k,(i,j) in enumerate(mon))
samples=[1<<i for i in range(6)]+[(1<<i)^(1<<j) for i,j in combinations(range(6),2)]
def quadratic_space(fn,ind):
 rows=[]
 for g in ((c5,c6),(d5,d6)):
  for v in samples:
   f=feat(v);h=feat(pact(v,g[1]))
   for bit in range(4):
    row=0
    for k in range(len(mon)):
     if h>>k&1:row^=1<<(4*k+bit)
     if f>>k&1:
      for j in range(4):
       if fn(1<<j,g[ind])>>bit&1:row^=1<<(4*k+j)
    rows.append(row)
 piv={}
 for r in rows:add(piv,r)
 assert len(piv)==83
 out=[]
 for i in range(84):
  if i in piv:continue
  v=1<<i
  for j in sorted(piv):
   if (piv[j]&v).bit_count()&1:v|=1<<j
  assert all((r&v).bit_count()%2==0 for r in rows)
  out.append(v)
 assert len(out)==1
 return out[0]
def evaluate(co,v):
 out=0;f=feat(v)
 for i in range(len(mon)):
  if f>>i&1:out^=(co>>(4*i))&15
 return out
def polar(co,x,y):return evaluate(co,x)^evaluate(co,y)^evaluate(co,x^y)
qm=quadratic_space(mact,1);qn=quadratic_space(nact,0)
for co,fn,ind in ((qm,mact,1),(qn,nact,0)):
 assert all(evaluate(co,pact(v,g[1]))==fn(evaluate(co,v),g[ind]) for g in group for v in range(64))
 assert rank(evaluate(co,v) for v in S)==4
assert rank(polar(qm,x,y) for x in S for y in S)==0
assert rank(polar(qn,x,y) for x in S for y in S)==4
assert all(polar(co,63,1<<i)==0 for co in (qm,qn) for i in range(6))
# In the w=6 residual, τ-shear f vanishes on the fixed two-space and is
# one of four F-maps on S. Count all inversion shadows, including cross terms.
counts=[]
for em,en in ((0,0),(0,1),(1,0),(1,1)):
 count=0
 for si in range(16):
  s=mv(S,si); fm=em*evaluate(qm,s);fn=en*mv(phi,evaluate(qm,s))
  for ui in range(4):
   v=s^(u1 if ui&1 else 0)^(u2 if ui&2 else 0)
   if evaluate(qm,v)==fm and evaluate(qn,v)==fn:count+=1
 counts.append(count)
assert counts==[14,4,4,14]
print('S5 120; F20 20; t ranks P6,M,N = 3,2,1; mixed graph fixed dimension 1')
print('Quadratic dimensions P6 -> M,N = 1,1; S polar ranks = 0,4')
print('Residual inversion-shadow counts:',counts)
