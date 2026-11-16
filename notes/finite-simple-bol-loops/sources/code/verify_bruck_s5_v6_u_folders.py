#!/usr/bin/env python3
"""Exact V6⊕U nonsplit-folder census; conditional structural inputs are in the manuscript."""
import runpy,io,contextlib,argparse,tempfile,subprocess,sys,json,collections
from pathlib import Path
if not __debug__:
 raise RuntimeError("This certificate requires Python assertions enabled")
parser=argparse.ArgumentParser()
parser.add_argument('--representatives',action='store_true')
args=parser.parse_args()
code=Path(__file__).resolve().parent
old=sys.argv;sys.argv=[str(code/'verify_bruck_s5_principal_stabilizer_fixed.py')]
try:
 with contextlib.redirect_stdout(io.StringIO()):z=runpy.run_path(str(code/'verify_bruck_s5_principal_stabilizer_fixed.py'))
finally:sys.argv=old
d=z['d'];apply=z['apply'];rank=z['rank'];hom=z['hom'];mul=z['mul'];evalword=z['evalword'];perms=z['perms'];P=z['P'];Q=z['Q'];kernel=z['kernel'];add=d['add'];X=d['getq']('V6')
c5=(1,0,2,3,4);d5=(0,2,3,4,1)
def actn(v,p):
 out=0
 for i in range(4):
  if v>>i&1:out^=(1<<p[0])^(1<<p[i+1])
 return (out>>1)&15
N=tuple(tuple(actn(1<<i,p) for i in range(4)) for p in (c5,d5))
# U=N tensor regular sign, generators both odd; halves are interchanged
U=tuple(tuple([a<<4 for a in g]+list(g)) for g in N)
V=tuple(tuple(list(X[j])+[a<<6 for a in U[j]]) for j in range(2))
n=14;pv=evalword(V,perms[P]);qv=evalword(V,perms[Q]);k=kernel(tuple(pv[i]^(1<<i) for i in range(n)));assert len(k)==2
# build principal irreducible 4-space with known basis
px=evalword(X,perms[P]);bb={}
for i in range(6):add(bb,px[i]^(1<<i))
B=tuple(bb.values());assert len(B)==4
def coord(b,v):
 for i in range(1<<len(b)):
  if apply(b,i)==v:return i
 raise ValueError
def restrict(A,b):return tuple(coord(b,apply(A,x)) for x in b)
S=(restrict(evalword(X,perms[P]),B),restrict(evalword(X,perms[Q]),B))
F=(pv,qv);h=hom(S,F)
assert len(hom(S,S))==1
for sub in z['subspaces'](4):
 pts={apply(sub,i) for i in range(1<<len(sub))}
 if all(apply(g,v) in pts for g in S for v in sub):assert len(sub) in (0,4)
print('K',k,'Hom dim',len(h));assert len(h)==3
Timage=[V[0][i]^(1<<i) for i in range(n)];print('rank transposition',rank(Timage))
def span(B):return {apply(B,i) for i in range(1<<len(B))}
# S5-stability of W and collision with transposition displacement
for mask in range(1,8):
 f=tuple(0 for i in range(4))
 for j,b in enumerate(h):
  if mask>>j&1:f=tuple(x^y for x,y in zip(f,b))
 assert rank(f)==4
 W=tuple(k)+f;ws=span(W);intersection=ws & span(Timage)
 assert all(apply(g,v) in ws for g in F for v in W)
 stable=all(apply(g,v) in ws for g in V for v in W)
 irank=len(intersection).bit_length()-1
 assert irank=={1:3,2:3,3:2,4:0,5:0,6:0,7:0}[mask]
 print('line',mask,'basis',f,'W S5-stable',stable,'intersectionrank',irank,'intersection',sorted(intersection))
remain=set(range(1<<14));orbits=[]
while remain:
 x=min(remain);O={x};queue=[x]
 for v in queue:
  for A in V:
   y=apply(A,v)
   if y not in O:O.add(y);queue.append(y)
 remain-=O;orbits.append(O)
assert len(orbits)==196 and sum(map(len,orbits))==1<<14
print('vector orbits',len(orbits),'distribution',collections.Counter(map(len,orbits)))
# Pair disjoint natural transpositions whose product belongs to F20
C=z['C'];D=z['D'];m=z['pmul'];i6=tuple(range(6));i5=tuple(range(5));pairs={(i6,i5)};queue=[(i6,i5)]
for a,b in queue:
 for g,h5 in ((C,c5),(D,d5)):
  pair=(m(a,g),tuple(b[h5[i]] for i in range(5)))
  if pair not in pairs:pairs.add(pair);queue.append(pair)
assert len(queue)==120
with tempfile.TemporaryDirectory(prefix='v6-u-cocycle-') as td:
 cocycle_path=Path(td)/'cocycle.json'
 subprocess.run([sys.executable,str(code/'verify_s5_v6_h2.py'),'--json',str(cocycle_path)],check=True,stdout=subprocess.DEVNULL)
 coc=json.loads(cocycle_path.read_text())
assert all(tuple(coc['matrices'][{tuple(g):i for i,g in enumerate(coc['perms'])}[g]])==X[j] for j,g in enumerate((C,D)))
perms6=[tuple(x) for x in coc['perms']]; mats=[tuple(x) for x in coc['matrices']]; F=coc['cocycle'];ix={g:i for i,g in enumerate(perms6)}
def gm(a,b):
 i,x=a;j,y=b;return (ix[m(perms6[i],perms6[j])],x^apply(mats[i],y)^F[i][j])
def inverse(a):
 i,x=a;g=perms6[i];invp=tuple(g.index(k) for k in range(6));j=ix[invp];return j,apply(mats[j],x^F[i][j])
def powg(a,e):
 r=(0,0)
 for _ in range(e):r=gm(r,a)
 return r
def conj(a,b):return gm(gm(a,b),inverse(a))
pidx=ix[P];p=(pidx,0);p=(pidx,powg(p,5)[1]);assert powg(p,5)==(0,0)
Psub={powg(p,j) for j in range(5)}
# Test every unordered pair of distinct transpositions with product in F20.
T6=[g6 for g6,g5 in queue if sum(g5[i]!=i for i in range(5))==2]
from itertools import combinations
for mask in (4,5,6,7):
 f=tuple(0 for _ in range(4))
 for j,b in enumerate(h):
  if mask>>j&1:f=tuple(x^y for x,y in zip(f,b))
 collisions=0;tested=0;hist={}
 for t,u in combinations(T6,2):
  gu=m(t,u)
  if gu not in z['N']:continue
  ta=evalword(V,perms[t]);ua=evalword(V,perms[u])
  timg=tuple(ta[i]^(1<<i) for i in range(n));uimg=tuple(ua[i]^(1<<i) for i in range(n))
  ti=ix[t];ui=ix[u];gi=ix[gu]
  tx=next((ti,x) for x in range(64) if powg((ti,x),2)==(0,0))
  ux=next((ui,x) for x in range(64) if powg((ui,x),2)==(0,0))
  gx=next((gi,x) for x in range(64) if conj((gi,x),p) in Psub)
  delta=gm(gm(tx,ux),inverse(gx));assert delta[0]==0
  space=tuple(k)+f+timg+uimg;r=rank(space);hits=rank(space+(delta[1],))==r
  tested+=1;collisions+=hits;hist[r]=hist.get(r,0)+1
 print('all pair results',mask,'tested',tested,'collisions',collisions,'rank histogram',hist)
 assert tested==5 and collisions==0 and hist=={13:5}
# Complete module-lattice and endomorphism controls.
def vector_orbit(generators,v):
 seen={v};queue=[v]
 for x in queue:
  for g in generators:
   y=apply(g,x)
   if y not in seen:seen.add(y);queue.append(y)
 return seen
def submodules(generators):
 m=len(generators[0]);mods={frozenset({0})};queue=[frozenset({0})]
 for S0 in queue:
  for v in range(1<<m):
   if v in S0:continue
   piv={}
   for x in S0:add(piv,x)
   for x in vector_orbit(generators,v):add(piv,x)
   B=tuple(piv.values());S1=frozenset(span(B))
   if S1 not in mods:mods.add(S1);queue.append(S1)
 return sorted(mods,key=lambda v:(len(v),min(v)))
def basis_of(S):
 b={}
 for v in sorted(S):add(b,v)
 return tuple(b.values())
xs=submodules(X);us=submodules(U)
assert [len(s) for s in xs]==[1,16,32,64] and [len(s) for s in us]==[1,16,256]
assert len(hom(X,X))==1 and len(hom(U,U))==2 and not hom(X,U) and not hom(U,X)
print('module lattice orders',[len(s) for s in xs],[len(s) for s in us],'endomorphism and cross-Hom controls passed')
N=tuple((1<<(6+i))|(1<<(10+i)) for i in range(4));uu=tuple(1<<(6+i) for i in range(8))
assert span(tuple(x>>6 for x in N))==set(us[1])
def f_for(mask):
 f=tuple(0 for _ in range(4))
 for j,b in enumerate(h):
  if mask>>j&1:f=tuple(x^y for x,y in zip(f,b))
 return f
def swapu(v):return (v&63)|(((v>>6)&15)<<10)|(((v>>10)&15)<<6)
assert all(swapu(apply(g,1<<i))==apply(g,swapu(1<<i)) for g in V for i in range(n))
for case,target in ((4,6),(5,7),(6,4),(7,5)):
 assert {swapu(v) for v in span(tuple(k)+f_for(case))}==span(tuple(k)+f_for(target))
Ss=[]
for xb in xs:
 for ub in us:
  S=tuple(basis_of(xb))+tuple(v<<6 for v in basis_of(ub))
  if S:Ss.append((len(xb).bit_length()-1,len(ub).bit_length()-1,S))
assert len(Ss)==11
# Verify the A5 and S5 displacement modules and W0 complement to M.
M=basis_of(xs[1]);J=basis_of(xs[2]);Ub=tuple(v<<6 for v in basis_of(us[2]))
assert rank(tuple(k)+M)==6
comm_s5=tuple(V[j][i]^(1<<i) for j in range(2) for i in range(n))
even_words=((0,1),(1,1));even_generators=tuple(evalword(V,w) for w in even_words)
comm_a5=tuple(g[i]^(1<<i) for g in even_generators for i in range(n))
assert rank(comm_s5)==rank(J+Ub)==rank(comm_s5+J+Ub)==13
assert rank(comm_a5)==rank(M+Ub)==rank(comm_a5+M+Ub)==12
# The same two words generate the full alternating subgroup in the six-point action.
even_perms=tuple(evalword(tuple(tuple(1<<x for x in g) for g in (C,D)),w) for w in even_words)
identity=tuple(1<<i for i in range(6));even_group={identity};even_queue=[identity]
for a in even_queue:
 for b in even_perms:
  c=mul(a,b)
  if c not in even_group:even_group.add(c);even_queue.append(c)
assert len(even_group)==60
for typ in (4,5,6,7):
 W=tuple(k)+f_for(typ)
 assert all(rank(W+S)>len(W) for _,_,S in Ss)
ct=kernel(tuple(V[0][i]^(1<<i) for i in range(n)));assert len(ct)==7
for typ in (4,5):
 W=tuple(k)+f_for(typ);ws=span(W)
 assert all(rank(W+S)>len(W) for _,_,S in Ss)
 rep={v:min(v^w for w in ws) for v in range(1<<n)}
 cosets=sorted(set(rep.values()));assert len(cosets)==256
 ixcos={v:i for i,v in enumerate(cosets)};usable=[]
 for O in orbits:
  cols=[ixcos[rep[v]] for v in O]
  if len(set(cols))!=len(cols):continue
  usable.append((O,sum(1<<i for i in cols),any(v&32 for v in O)))
 bycol=[[i for i,(_,mask,_) in enumerate(usable) if mask>>j&1] for j in range(256)]
 prep=[]
 for dx,du,S in Ss:
  SS=span(S);R={v:min(v^s for s in SS) for v in range(1<<n)}
  masks=[]
  for O,_,_ in usable:
   mask=0
   for v in O:mask|=1<<R[v]
   masks.append(mask)
  intdim=len(S)+len(ct)-rank(S+tuple(ct));outer=1280//(1<<intdim)
  index=6*(1<<(14-rank(W+S)))
  if dx==6 and du==8:assert index==6 and outer==10
  prep.append((dx,du,masks,outer,index))
 hist=collections.Counter();covers=[0,0];goal=(1<<256)-1
 def recurse(covered,chosen,outside):
  if covered==goal:
   Dset=set().union(*(usable[i][0] for i in chosen))
   assert len(Dset)==256 and 0 in Dset and len({rep[x] for x in Dset})==256
   assert all(apply(g,x) in Dset for g in V for x in Dset)
   covers[outside]+=1
   if not outside:return
   bad=[]
   for dx,du,masks,outer,index in prep:
    bits=0
    for i in chosen:bits|=masks[i]
    size=bits.bit_count()+outer
    if dx==6 and du==8:assert size==11 and index==6
    if size==index and index>1:bad.append((dx,du))
   hist[tuple(bad)]+=1
   if args.representatives:print('cover',typ,'orbits',[min(usable[i][0]) for i in chosen],'bad',bad)
   return
  best=None
  for j in range(256):
   if covered>>j&1:continue
   cand=[i for i in bycol[j] if not usable[i][1]&covered]
   if not cand:return
   if best is None or len(cand)<len(best):best=cand
  for i in best:recurse(covered|usable[i][1],chosen+[i],outside or usable[i][2])
 zero=next(i for i,(O,_,_) in enumerate(usable) if O=={0})
 recurse(usable[zero][1],[zero],False)
 assert covers=={4:[56,362],5:[21,123]}[typ] and hist=={():covers[1]}
 print('type',typ,'inside/outside covers',covers,'proper quotient tests',dict(hist))
