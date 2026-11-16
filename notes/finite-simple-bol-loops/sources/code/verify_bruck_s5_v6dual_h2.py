#!/usr/bin/env python3
"""Candidate V6-dual stable-elements H2 and H1 restriction checks.

Adapted from verify_s5_v6_h2.py at reviewed source
5c011bc5e8b375a1e85058811590bf0d672198f2. Changes: inverse-transpose
module action; H1 dimensions and explicit F20 restriction, fixed-line,
and transposition fixed/image controls. Python 3.11+; no tracked outputs.
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
 for i in range(6):
  if v>>i&1:out^=A[i]
 return out
def mm(A,B):return tuple(ma(A,v) for v in B)
C=tuple([actj(1<<i,c) for i in range(5)]+[32^21]);D=tuple([actj(1<<i,d) for i in range(5)]+[32^1]);Id=tuple(1<<i for i in range(6))
def transpose(A):
 return tuple(sum(((A[j]>>i)&1)<<j for j in range(6)) for i in range(6))
C=transpose(C)
D=transpose(mm(mm(D,D),D))
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
   off=6*ind[tup]
   for j in range(6):
    if A[j]>>bit&1:row^=1<<(off+j)
  return row
 # d1 rows; collect columns in C².
 cols=[0]*(6*len(X))
 for k,(x,y) in enumerate(pairs):
  for b in range(6):
   row=termsrow([((y,),G[x]),((mul(x,y),),Id),((x,),Id)],sidx,b)
   while row:
    v=row&-row;cols[v.bit_length()-1]|=1<<(6*k+b);row^=v
 B={}
 for v in cols:add(B,v)
 rows={}
 for x,y,z in product(X,repeat=3):
  terms=[((y,z),G[x]),((mul(x,y),z),Id),((x,mul(y,z)),Id),((x,y),Id)]
  for b in range(6):add(rows,termsrow(terms,pidx,b))
 assert all((r&col).bit_count()%2==0 for r in rows.values() for col in cols)
 return X,pairs,pidx,B,rows
X,pairs,idx,B,R=complex2(S)
Z=[]
for f in range(6*len(pairs)):
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
def val(v,ind,t):return (v>>(6*ind[t]))&63
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
   w |= a<<(6*k)
  diffs.append(normal(qb,w))
 for bit in range(6*len(qp)):
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
assert len(stable)==1
v=0
for j in range(len(reps)):
 if stable[0]>>j&1:v^=reps[j]
for label,K in [('transposition',subgroup((t,))),('order4',next(subgroup((x,)) for x in S if order(x)==4))]:
 _,kp,_,kb,kr=complex2(K);v0=0
 for k,pair in enumerate(kp):v0|=val(v,idx,pair)<<(6*k)
 nonzero=bool(normal(kb,v0))
 assert nonzero == (label=='order4')
 print('restriction',label,'rank d1,d2',len(kb),len(kr),'nonzero',nonzero)
K=next(subgroup((x,)) for x in S if order(x)==4)
P5=next(subgroup((p,)) for p in sorted(G) if order(p)==5 and all(mul(mul(k,p),inv(k)) in subgroup((p,)) for k in K))
F=subgroup((next(x for x in K if order(x)==4),next(x for x in P5 if order(x)==5)))
assert len(F)==20 and set(K)<=set(F) and set(P5)<=set(F)
print('normalizer witness: |C4|,|C5|,|F20|',len(K),len(P5),len(F))

# Corestrict the stable cocycle and verify its global bar identity.
T=[]; covered=set()
for x in sorted(G):
 if x not in covered:
  T.append(x);covered.update(mul(x,s) for s in S)
assert len(T)==15 and len(covered)==120
lookup={mul(r,s):r for r in T for s in S}
def sc(a,b):
 if a==I or b==I:return 0
 return (v>>(6*idx[(a,b)]))&63
# h(g,r)=r(gr)^(-1) gr, g r=r(gr) h(g,r).
def hf(g,r):return mul(inv(lookup[mul(g,r)]),mul(g,r))
L=sorted(G);h={(g,r):hf(g,r) for g in L for r in T}
f={}
for g in L:
 for k in L:
  z=0
  for r in T:
   kr=lookup[mul(k,r)];gkr=lookup[mul(g,kr)]
   z ^= ma(G[gkr],sc(h[g,kr],h[k,r]))
  f[g,k]=z
assert all(f[I,g]==f[g,I]==0 for g in L)
for g in L:
 for k in L:
  gk=mul(g,k)
  for l in L:
   assert ma(G[g],f[k,l])^f[gk,l]^f[g,mul(k,l)]^f[g,k]==0
# restriction differs from stable representative by a boundary.
from itertools import product
cols=[0]*(6*(len(S)-1));X=[x for x in S if x!=I]; si={x:i for i,x in enumerate(X)}
for j,(g,k) in enumerate(product(X,repeat=2)):
 for b in range(6):
  for x,A in ((k,G[g]),(mul(g,k),Id),(g,Id)):
   if x==I:continue
   for q in range(6):
    if A[q]>>b&1:cols[6*si[x]+q]^=1<<(6*j+b)
B={}
for col in cols:add(B,col)
w=0
for j,p in enumerate(product(X,repeat=2)):w |= (f[p]^sc(*p))<<(6*j)
assert not normal(B,w)
print('global cocycle verified, restriction agrees with stable class')

# Enumerate derivations from values at c and d, checking every Cayley edge.
# This uses the generated group itself, independently of a presentation.
derivations=set()
for a,b in product(range(64),repeat=2):
 values={I:0}; todo=[I]; valid=True
 for g in todo:
  for h0,u in ((c,a),(d,b)):
   gh=mul(g,h0); value=values[g]^ma(G[g],u)
   if gh in values:
    if values[gh]!=value:
     valid=False;break
   else:values[gh]=value;todo.append(gh)
  if not valid:break
 if valid:
  assert len(values)==120
  derivations.add((a,b))
inner={(ma(C,u)^u,ma(D,u)^u) for u in range(64)}
assert inner<=derivations
assert len(derivations)==64 and len(inner)==32
print('H1: derivations',len(derivations),'principal',len(inner),'dimension', (len(derivations)//len(inner)).bit_length()-1)

q4=next(x for x in K if order(x)==4)
pa=next(x for x in P5 if order(x)==5)
fixed=[u for u in range(64) if ma(G[pa],u)==u]
proj=lambda u: __import__('functools').reduce(int.__xor__,(ma(G[x],u) for x in P5),0)
bound={ma(G[q4],u)^u for u in fixed}
x,y=next(iter(derivations-inner))
values={I:0}; todo=[I]
for g in todo:
 for h0,u in ((c,x),(d,y)):
  gh=mul(g,h0); vv=values[g]^ma(G[g],u)
  if gh not in values: values[gh]=vv;todo.append(gh)
assert fixed == [0,31,32,63] and bound == {0,32}
assert proj(values[q4]) in {31,63}
assert all(ma(G[g],32)==32 for g in G)
print('fixed',fixed,'boundary',sorted(bound),'global cocycle q4 projected',proj(values[q4]),'restriction nonzero',proj(values[q4]) not in bound)
assert sum(ma(G[t],u)==u for u in range(64))==8
assert len({ma(G[t],u)^u for u in range(64)})==8
print('t fixed',sum(ma(G[t],u)==u for u in range(64)),'(1+t) image',len({ma(G[t],u)^u for u in range(64)}))

# Export only on explicit request; generated JSON is not tracked.
import argparse
import json
parser=argparse.ArgumentParser()
parser.add_argument('--json',help='write generated cocycle JSON to this path')
args=parser.parse_args()
if args.json:
 LL=[I]+[x for x in L if x!=I]
 with open(args.json,'w') as fp:
  json.dump({'perms':[list(x) for x in LL], 'matrices':[list(G[x]) for x in LL], 'cocycle':[[f[g,k] for k in LL] for g in LL], 'c':list(c),'d':list(d)},fp)
