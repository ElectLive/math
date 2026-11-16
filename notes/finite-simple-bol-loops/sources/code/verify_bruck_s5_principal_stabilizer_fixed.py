#!/usr/bin/env python3
"""Test necessary P-fixed stabilizer feasibility for one-M principal blocks."""
import argparse,contextlib,io,sys,runpy,collections
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--models',action='store_true',help='identify four modules and enumerate all feasible P-fixed subspaces')
args=parser.parse_args()
p=Path(__file__).with_name('classify_bruck_s5_principal_isotypes.py')
with contextlib.redirect_stdout(io.StringIO()): z=runpy.run_path(str(p))
d=z['d'];add=d['add'];apply=d['apply'];mul=d['mul'];hom=d['hom_basis'];null=d['nullspace']; inv=d['inv']; C=d['C']; D=d['Dp']; clusters=z['clusters']
def pmul(a,b):return tuple(a[b[i]] for i in range(6))
idp=tuple(range(6)); perms={idp:()};todo=[idp]
for g in todo:
 for i,s in enumerate((C,D)):
  h=pmul(g,s)
  if h not in perms:perms[h]=perms[g]+(i,);todo.append(h)
assert len(perms)==120
def order(g):
 x=idp
 for i in range(1,121):
  x=pmul(x,g)
  if x==idp:return i
P=next(g for g in todo if order(g)==5)
def power(g,n):
 a=idp
 for _ in range(n):a=pmul(a,g)
 return a
Pset={power(P,i) for i in range(5)}
def inverse(g):return tuple(g.index(i) for i in range(6))
N=[g for g in todo if pmul(pmul(g,P),inverse(g)) in Pset]
assert len(N)==20
Q=next(g for g in N if order(g)==4)
assert len({pmul(power(P,i),power(Q,j)) for i in range(5) for j in range(4)})==20
print('P,Q,words',P,Q,perms[P],perms[Q])
def evalword(X,w):
 a=tuple(1<<j for j in range(len(X[0])))
 for i in w:a=mul(a,X[i])
 return a
def kernel(matrix):
 n=len(matrix);return null([sum(((matrix[j]>>i)&1)<<j for j in range(n)) for i in range(n)],n)
def rank(v):
 b={}
 for x in v:add(b,x)
 return len(b)
def coords(b,v):
 for mask in range(1<<len(b)):
  if apply(b,mask)==v:return mask
 raise ValueError
def subspaces(n):
 # Closure under adjoining any vector; canonical identity is its bitset.
 spaces={1:()};queue=[(1,())]
 for bits,basis in queue:
  for v in range(1,1<<n):
   if bits>>v&1:continue
   vals=[i for i in range(1<<n) if bits>>i&1]
   new=bits
   for w in vals:new|=1<<(v^w)
   if new not in spaces:
    bb=basis+(v,);spaces[new]=bb;queue.append((new,bb))
 return [b for _,b in queue]
def image_space(matrix, basis):return tuple(apply(matrix,v) for v in basis)
def affine_maps(domain_action,target_action):
 n=len(domain_action);m=len(target_action)
 if not n:yield ();return
 if not m:yield (0,)*n;return
 bas=hom((domain_action,),(target_action,))
 for mask in range(1<<len(bas)):
  cols=[0]*n
  for i,v in enumerate(bas):
   if mask>>i&1:cols=[x^y for x,y in zip(cols,v)]
  yield tuple(cols)
res=collections.Counter(); found=[]; failures=[]; checks=0
for ci,cl in enumerate(clusters):
 label,X,_=cl[0];n=len(X[0]);h=label[6];m=n-4
 pm=evalword(X,perms[P]); qm=evalword(X,perms[Q]);k=kernel(tuple(pm[i]^(1<<i) for i in range(n)))
 assert len(k)==m
 for u in range(m-h+1):
  for v in range(m-h-u+1):
   adim=u+2*v; sig=d['sign'](adim,u,v)
   # full module fixed vectors and coinvariant differences
   F=tuple((X[j][i]^(1<<i)) for j in range(2) for i in range(n))
   # fixed vectors in X0 plus sign fixed vectors in A
   eq=[]
   for j in range(2):
    for bit in range(n):eq.append(sum(((X[j][i]^(1<<i))>>bit&1)<<i for i in range(n)))
   fixed=null(eq,n)
   afix=kernel(tuple(sig[i]^(1<<i) for i in range(adim))) if adim else []
   fixedfull=list(fixed)+[a<<n for a in afix]
   diffs=list(F)+[(sig[i]^(1<<i))<<n for i in range(adim)]
   wanted=n+adim-rank(diffs)
   assert wanted==h+u+v
   yes=None
   for U in subspaces(m):
    if len(U)<wanted:continue
    Uvec=image_space(k,U);Uset={apply(Uvec,t) for t in range(1<<len(U))}
    if any(apply(qm,w) not in Uset for w in Uvec):continue
    qU=tuple(coords(Uvec,apply(qm,w)) for w in Uvec)
    for f in affine_maps(qU,sig):
     checks+=1
     graph=tuple(w|(f[j]<<n) for j,w in enumerate(Uvec))
     if rank(graph+tuple(fixedfull)) != len(graph)+len(fixedfull):continue
     if rank(tuple(diffs)+graph)!=n+adim:continue
     yes=(U,f);break
    if yes is not None:break
   if yes is None: failures.append((ci,u,v,label))
   else:found.append((ci,u,v,yes))
   res[(label[5],label[6],yes is not None)]+=1
print('found',len(found),'failures',len(failures),'graph checks',checks,'hist',sorted(res.items()))
print('rejected triples',[(i,u,v) for i,u,v,_ in failures])
print('witnesses',found)
assert [len(subspaces(n)) for n in range(5)]==[1,2,5,16,67]
assert len(found)==6 and len(failures)==73 and checks==2403
assert [(ci,u,v) for ci,u,v,_ in found]==[(0,0,0),(1,0,0),(3,0,0),(4,0,0),(7,0,0),(13,0,0)]

assert (1,0,1) in [(i,u,v) for i,u,v,_ in failures]
assert (2,0,0) in [(i,u,v) for i,u,v,_ in failures]

if args.models:
 def dual(matrix):
  n=len(matrix); inverse_matrix=inv(matrix)
  return tuple(sum(((inverse_matrix[i]>>j)&1)<<i for i in range(n)) for j in range(n))
 def find_isomorphisms(source,target):
  basis=hom(source,target); n=len(source[0]); maps=[]
  for mask in range(1<<len(basis)):
   matrix=tuple(0 for _ in range(n))
   for j,b in enumerate(basis):
    if mask>>j&1:matrix=tuple(x^y for x,y in zip(matrix,b))
   if rank(matrix)==n:
    assert all(mul(matrix,a)==mul(b,matrix) for a,b in zip(source,target))
    maps.append(matrix)
  return basis,maps
 v6=d['getq']('V6')
 models={1:tuple(dual(a) for a in v6),
         7:tuple(tuple(1<<g[i] for i in range(6)) for g in (C,D))}
 expected={1:(63,31,60,58,54,46),7:(63,62,2,4,8,16)}
 for ci,target in models.items():
  basis,maps=find_isomorphisms(clusters[ci][0][1],target)
  assert expected[ci] in maps
  assert (len(basis),len(maps))==({1:(1,1),7:(2,2)}[ci])
  print('model',ci,'Hom dimension',len(basis),'isomorphisms',len(maps),'witness',expected[ci])
 all_feasible={}
 for ci in (1,4,7,13):
  label,X,_=clusters[ci][0];n=len(X[0]);pm=evalword(X,perms[P]);qm=evalword(X,perms[Q])
  K=kernel(tuple(pm[i]^(1<<i) for i in range(n)))
  equations=[sum(((X[j][i]^(1<<i))>>bit&1)<<i for i in range(n)) for j in range(2) for bit in range(n)]
  fixed=null(equations,n)
  diffs=tuple(X[j][i]^(1<<i) for j in range(2) for i in range(n))
  feasible=[]
  for U in subspaces(len(K)):
   vectors=image_space(K,U)
   points={apply(vectors,t) for t in range(1<<len(vectors))}
   if any(apply(qm,w) not in points for w in vectors):continue
   if rank(vectors+tuple(fixed))!=len(vectors)+len(fixed):continue
   if rank(diffs+vectors)!=n:continue
   feasible.append(tuple(sorted(points)))
  all_feasible[ci]=feasible
  print('W0 model',ci,'P-fixed basis',K,'Q images',tuple(apply(qm,w) for w in K),'S5-fixed basis',fixed,'feasible subspaces',feasible)
 assert all_feasible=={1:[(0,)],4:[(0,4)],7:[(0,8),(0,9)],13:[(0,4,40,44)]}
 # Under the displayed isomorphism, the two P6 lines are the fixed point and the five-point orbit sum.
 assert apply(expected[7],8)==4 and apply(expected[7],9)==59
 assert P[2]==2 and sum(1<<i for i in range(6) if i!=2)==59
