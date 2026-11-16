#!/usr/bin/env python3
"""Normalized bar/stable-elements H2 calculations for M and J* over F2.

Run with M or dual. The restriction target C4 is selected inside the
normalizer of a Sylow 5-subgroup. Python 3.11+ is required.
"""
from itertools import product
from collections import Counter
I=tuple(range(6)); c=(1,0,3,2,5,4); d=(0,2,3,4,1,5)
def mul(a,b):return tuple(a[b[i]] for i in range(6))
def inv(a):return tuple(a.index(i) for i in range(6))
def actj(v,p):
 z=0
 for i in range(5):
  if v>>i&1:z^=1<<p[i]
 if z>>5:z^=63
 return z
def ma(A,v):
 out=0
 for i in range(kdim):
  if v>>i&1:out^=A[i]
 return out
def mm(A,B):return tuple(ma(A,v) for v in B)
import sys
assert len(sys.argv)==2 and sys.argv[1] in ('M','dual')
kind=sys.argv[1]
kdim=5 if kind=='dual' else 4
def actmod(v,p):
 if kind=='dual':
  z=0
  for i in range(5):
   if v>>i&1:z^=(1<<p[i])^(1<<p[5])
  return z&31
 bits=0
 for i in range(4):
  if v>>i&1:bits^=(1<<p[0])^(1<<p[i+1])
 if bits>>5&1:bits^=63
 return (bits>>1)&15
C=tuple(actmod(1<<i,c) for i in range(kdim));D=tuple(actmod(1<<i,d) for i in range(kdim));Id=tuple(1<<i for i in range(kdim))
G={I:Id}; queue=[I]
for x in queue:
 for y,A in ((c,C),(d,D)):
  z=mul(x,y); M=mm(G[x],A)
  if z not in G:G[z]=M;queue.append(z)
  else:assert G[z]==M
assert len(G)==120
# Find transposition and 4-cycle whose generated subgroup has order 8.
def subgroup(gens):
 R={I}; q=[I]
 for x in q:
  for y in gens:
   z=mul(x,y)
   if z not in R:R.add(z);q.append(z)
 return tuple(sorted(R))
def order(x):
 y=x;n=1
 while y!=I:y=mul(y,x);n+=1
 return n
t=next(x for x in sorted(G) if G[x]==C)
S=next(subgroup((t,x)) for x in sorted(G) if order(x)==4 and len(subgroup((t,x)))==8)
assert len(S)==8

def add(B,x):
 while x:
  p=x.bit_length()-1
  if p in B:x^=B[p]
  else:B[p]=x;return True
 return False
def red(B,x):
 while x:
  p=x.bit_length()-1
  if p not in B:break
  x^=B[p]
 return x

def complex2(K):
 X=tuple(x for x in K if x!=I); pairs=list(product(X,repeat=2)); pidx={t:i for i,t in enumerate(pairs)}; sidx={(t,):i for i,t in enumerate(X)}
 # Add coefficient block A from f(tuple) to each corresponding output bit.
 def termsrow(terms,ind,bit):
  row=0
  for tup,A in terms:
   if I in tup:continue
   off=kdim*ind[tup]
   for j in range(kdim):
    if A[j]>>bit&1:row^=1<<(off+j)
  return row
 # d1 rows; collect columns in C².
 cols=[0]*(kdim*len(X))
 for k,(x,y) in enumerate(pairs):
  for b in range(kdim):
   row=termsrow([((y,),G[x]),((mul(x,y),),Id),((x,),Id)],sidx,b)
   while row:
    v=row&-row;cols[v.bit_length()-1]|=1<<(kdim*k+b);row^=v
 B={}
 for v in cols:add(B,v)
 rows={}
 for x,y,z in product(X,repeat=3):
  terms=[((y,z),G[x]),((mul(x,y),z),Id),((x,mul(y,z)),Id),((x,y),Id)]
  for b in range(kdim):add(rows,termsrow(terms,pidx,b))
 assert all((r&col).bit_count()%2==0 for r in rows.values() for col in cols)
 return X,pairs,pidx,B,rows
X,pairs,idx,B,R=complex2(S)
Z=[]
for f in range(kdim*len(pairs)):
 if f in R:continue
 v=1<<f
 for p in sorted(R):
  if (R[p]&v).bit_count()%2:v|=1<<p
 assert all((r&v).bit_count()%2==0 for r in R.values())
 Z.append(v)
H=dict(B);reps=[]
for z in Z:
 if add(H,z):reps.append(z)
print('group,S',len(G),len(S),'ranks d1,d2',len(B),len(R),'Z2',len(Z),'H2',len(reps),flush=True)
# Each difference yields linear equations in quotient H2(Q). Reducing by B must
# be linear: eliminate ALL present pivots, not stop at a free leading bit.
def normal(B,v):
 for p in sorted(B,reverse=True):
  if v>>p&1:v^=B[p]
 return v
def val(v,ind,t):return (v>>(kdim*ind[t]))&((1<<kdim)-1)
cache={}; eq={};hist=Counter()
for g in sorted(G):
 gi=inv(g);Q=tuple(x for x in S if mul(mul(g,x),gi) in S);hist[len(Q)]+=1
 if Q not in cache:cache[Q]=complex2(Q)
 _,qp,_,qb,_=cache[Q]
 diffs=[]
 for v in reps:
  w=0
  for k,(x,y) in enumerate(qp):
   gx=mul(mul(g,x),gi);gy=mul(mul(g,y),gi)
   a=val(v,idx,(x,y))^ma(G[gi],val(v,idx,(gx,gy)))
   w |= a<<(kdim*k)
  diffs.append(normal(qb,w))
 for bit in range(kdim*len(qp)):
  row=sum(((v>>bit)&1)<<j for j,v in enumerate(diffs))
  add(eq,row)
print('intersection histogram',sorted(hist.items()),'distinct',len(cache),'stable constraint rank',len(eq),'stable dim',len(reps)-len(eq),flush=True)
# compute stable quotient representatives in S-coordinates
stable=[]
for f in range(len(reps)):
 if f in eq:continue
 m=1<<f
 for p in sorted(eq):
  if (eq[p]&m).bit_count()%2:m|=1<<p
 stable.append(m)
print('stable masks',stable)
assert len(stable)==(0 if kind=='M' else 2)

K=next(subgroup((x,)) for x in S if order(x)==4)
P5=next(subgroup((p,)) for p in sorted(G) if order(p)==5 and all(mul(mul(k,p),inv(k)) in subgroup((p,)) for k in K))
F=subgroup((next(x for x in K if order(x)==4),next(x for x in P5 if order(x)==5)))
assert len(F)==20 and set(K)<=set(F) and set(P5)<=set(F)
print('normalizer witness: |C4|,|C5|,|F20|',len(K),len(P5),len(F))


Ks=[subgroup((t,)),K]
spaces=[complex2(X) for X in Ks]
patterns=[]
for i,mask in enumerate(stable):
 v=0
 for j in range(len(reps)):
  if mask>>j&1:v^=reps[j]
 vals=[]
 for _,pairs0,_,bound,_ in spaces:
  w=0
  for j,pair in enumerate(pairs0):w|=val(v,idx,pair)<<(kdim*j)
  vals.append(normal(bound,w))
 pattern=tuple(bool(x) for x in vals)
 patterns.append(pattern)
 print('basis',i,'restriction T,C4',pattern,flush=True)
assert patterns==([] if kind=='M' else [(False,True),(True,False)])
