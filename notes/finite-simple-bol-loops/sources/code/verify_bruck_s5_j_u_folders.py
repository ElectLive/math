#!/usr/bin/env python3
"""Exhaust J+U radical transversals and quotient tests; see linked manuscript.

This verifies finite vector-model calculations, not the cited structural,
generation, normal-subgroup, or faithful-folder arguments. Run without -O.
"""
import sys
assert __debug__, "Run with assertions enabled"
c6=(1,0,3,2,5,4);d6=(0,2,3,4,1,5)
c5=(1,0,2,3,4);d5=(0,2,3,4,1)
def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
def parity(p): return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2
def jact(v,p):
 z=0
 for i in range(5):
  if v>>i&1:z^=1<<p[i]
 return (z^63 if z&32 else z)&31
def nact(v,p):
 z=0
 for i in range(4):
  if v>>i&1:z^=(1<<p[0])^(1<<p[i+1])
 return (z>>1)&15
def action(v,p6,p5):
 j=jact(v&31,p6); x=nact((v>>5)&15,p5); y=nact(v>>9,p5)
 if parity(p5): x,y=y,x
 return j|(x<<5)|(y<<9)
def powp(p,n):
 r=tuple(range(len(p)))
 for _ in range(n):r=compose(r,p)
 return r
pairs={(tuple(range(6)),tuple(range(5)))}; queue=list(pairs)
for a,b in queue:
 for aa,bb in ((c6,c5),(d6,d5)):
  h=(compose(a,aa),compose(b,bb))
  if h not in pairs:pairs.add(h);queue.append(h)
assert len(pairs)==120 and len({g[0] for g in queue})==120 and len({g[1] for g in queue})==120
for g in queue:
 for h in ((c6,c5),(d6,d5)):
  gh=(compose(g[0],h[0]),compose(g[1],h[1]))
  assert all(action(action(1<<i,*h),*g)==action(1<<i,*gh) for i in range(13))
p=(compose(c6,d6),compose(c5,d5));assert powp(p[0],5)==tuple(range(6))
def pinv(x):return tuple(x.index(i) for i in range(len(x)))
normal=[g for g in queue if compose(compose(g[1],p[1]),pinv(g[1])) in [powp(p[1],k) for k in range(1,5)]]
assert len(normal)==20
def span(values):
 s={0}
 for v in values:s|={v^x for x in s.copy()}
 return s
def forbit(x):return {action(x,*g) for g in normal}
def fspan(x):return span(forbit(x))
L={v for v in range(32) if action(v,*p)==v};assert len(L)==2
J0={v^action(v,*p) for v in range(32)};assert len(J0)==16
soc={x<<5|x<<9 for x in range(16)}
T=next(s for i in range(1,256) if len(s:=fspan(i<<5))==16 and s!=soc)
assert all((v&31)==0 for v in T)
# Equivariant isomorphism S_J -> T: a nonzero image fixes the map.
x=next(v for v in J0 if v);mapping=None
for target in sorted(T-{0}):
 candidates={0:0};valid=True
 for g in normal:
  a=action(x,*g);b=action(target,*g)
  if a in candidates:
   if candidates[a]!=b:valid=False;break
  else:
   for k,v in list(candidates.items()):candidates[k^a]=v^b
 if valid and set(candidates)==J0 and len(set(candidates.values()))==16:
  mapping=candidates;break
assert mapping
assert all(mapping[a^b]==(mapping[a]^mapping[b]) for a in J0 for b in J0)
assert all(mapping[action(v,*g)]==action(mapping[v],*g) for v in J0 for g in normal)
W0={l^u for l in L for u in T}; W1={l^v^mapping[v] for l in L for v in J0};assert len(W0)==len(W1)==32
seen=set();orbits=[]
for v in range(8192):
 if v not in seen:
  orb={action(v,*g) for g in queue};orbits.append(orb);seen.update(orb)
assert len(seen)==8192
assert len(orbits)==106 and sum(map(len,orbits))==8192
def basis(vecs):
 B={}
 for v in vecs:
  while v:
   k=v.bit_length()-1
   if k in B:v^=B[k]
   else:B[k]=v;break
 return B
def reduce(v,B):
 for k in sorted(B,reverse=True):
  if v>>k&1:v^=B[k]
 return v
Jspaces=[{0},J0,set(range(32))]
Uspaces=[{0},soc,{i<<5 for i in range(256)}]
Smods=[]
for ji,J in enumerate(Jspaces):
 for ui,U in enumerate(Uspaces):
  if ji==ui==0:continue
  B=basis(list(J)+list(U))
  Smods.append(((ji,ui),B))
# Exhaustively generate the S5-submodule lattices on each block.
def invariant_lattice(ambient):
 cyclic={frozenset(span(action(v,*g) for g in queue)) for v in ambient}
 lattice={frozenset({0})}; todo=[frozenset({0})]
 for X in todo:
  for Y in cyclic:
   Z=frozenset(x^y for x in X for y in Y)
   if Z not in lattice:lattice.add(Z);todo.append(Z)
 return lattice
assert invariant_lattice(set(range(32)))==set(map(frozenset,Jspaces))
assert invariant_lattice({i<<5 for i in range(256)})==set(map(frozenset,Uspaces))
Cfixed={v for v in range(8192) if action(v,c6,c5)==v};assert len(Cfixed)==128
for label,W in [('pure',W0),('graph',W1)]:
 assert all(action(w,*g) in W for w in W for g in normal)
 cosets=sorted({min(v^w for w in W) for v in range(8192)});assert len(cosets)==256
 idx={v:i for i,v in enumerate(cosets)}
 rows=[]
 for o in orbits:
  cs=[idx[min(v^w for w in W)] for v in o]
  if len(set(cs))==len(o):rows.append((o,sum(1<<i for i in cs)))
 assert len(rows)=={'pure':48,'graph':39}[label]

 full=(1<<256)-1
 rmask=[m for o,m in rows]; options=[[i for i,m in enumerate(rmask) if m>>c&1] for c in range(256)]
 zero=next(i for i,(o,m) in enumerate(rows) if o=={0})
 nodes=[0];solutions=[0];first=[None]; equality_counts={name:0 for name,B in Smods}; multisimp=[0]; checks=[]
 for name,B in Smods:
  cs=sum(reduce(v,B)==0 for v in Cfixed)
  assert cs and 128%cs==0
  rhs=6*(2**(13-len(basis(list(B.values())+list(W)))))
  checks.append((name,B,10*128//cs,rhs))
 def search(used,chosen):
  nodes[0]+=1
  if used==full:
   solutions[0]+=1
   D=set().union(*(rows[i][0] for i in chosen))
   assert len(D)==256 and 0 in D and len({min(v^w for w in W) for v in D})==256
   possible=0
   for name,B,outcount,rhs in checks:
    delta=len({reduce(v,B) for v in D})+outcount-rhs
    assert delta>=0
    if delta==0:
     equality_counts[name]+=1;possible+=1
   if possible==0:multisimp[0]+=1
   if first[0] is None:first[0]=tuple(chosen)
   if '--representatives' in sys.argv: print(label, sorted(min(rows[i][0]) for i in chosen), 'quotients',possible)
   return
  best=None
  for c in range(256):
   if not (used>>c)&1:
    valid=[i for i in options[c] if not (rmask[i]&used)]
    if not valid:return
    if best is None or len(valid)<len(best):best=valid
    if len(best)==1:break
  for i in best:search(used|rmask[i],chosen+[i])
 search(rmask[zero],[zero])
 assert solutions[0]=={'pure':56,'graph':21}[label]
 assert multisimp[0]=={'pure':32,'graph':21}[label]
 assert equality_counts[(0,2)]=={'pure':24,'graph':0}[label]
 assert all(v==0 for k,v in equality_counts.items() if k!=(0,2))
 print(label,'covers',solutions[0],'simple',multisimp[0], 'U-quotients',equality_counts[(0,2)],'search nodes',nodes[0])
def unit(v):return (v&31)|(((v>>9)&15)<<5)|(((v>>5)&15)<<9)
assert all(unit(action(v,*g))==action(unit(v),*g) for v in [1<<i for i in range(13)] for g in queue)
assert {unit(v) for v in W0}!=W0 and {unit(v) for v in W1}!=W1
assert len({v&31 for v in W0})==2 and len({v&31 for v in W1})==32
print('module lattices, stabilizer controls and quotient tests passed')
