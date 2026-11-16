#!/usr/bin/env python3
"""Finite d=9 mixed-module cocycle and radical-transversal certificate.

No group extensions or loop simplicity claims are computed. The two-generator
presentation is Nagy arXiv:0709.4544v1 Lemma 3.1; all arithmetic is over F2.
"""
from itertools import product

# Ext^1(M,N) via H^1(S5,M* tensor N); Nagy Lemma 3.1 presentation.
c6=[1,0,3,2,5,4];d6=[0,2,3,4,1,5]
c5=[1,0,2,3,4];d5=[0,2,3,4,1]
def actm(v,p):
 bits=0
 for i in range(4):
  if v>>i&1:bits^=(1<<p[0])^(1<<p[i+1])
 if bits>>5&1:bits^=63
 return (bits>>1)&15
def actn(v,p):
 bits=0
 for i in range(4):
  if v>>i&1:bits^=(1<<p[0])^(1<<p[i+1])
 return (bits>>1)&15
def tensor(p6,p5):
 out=[]
 for i in range(4):
  a=actm(1<<i,p6)
  for j in range(4):
   b=actn(1<<j,p5);v=0
   for x in range(4):
    for y in range(4):
     if a>>x&1 and b>>y&1:v^=1<<(4*x+y)
   out.append(v)
 return tuple(out)
def ma(A,v):
 z=0
 for i in range(16):
  if v>>i&1:z^=A[i]
 return z
def mm(A,B):return tuple(ma(A,x) for x in B)
I=tuple(1<<i for i in range(16));C=tensor(c6,c5);D=tensor(d6,d5)
G={I}; queue=[I]
for x in queue:
 for y in (C,D):
  z=mm(x,y)
  if z not in G:G.add(z);queue.append(z)
assert len(G)==120
inv={x:next(y for y in G if mm(x,y)==I) for x in G}
def mul(a,b):p,v=a;q,w=b;return mm(p,q),v^ma(p,w)
def inverse(a):p,v=a;q=inv[p];return q,ma(q,v)
z=(I,0)
def power(a,n):
 r=z
 for _ in range(n):r=mul(r,a)
 return r
def resid(x,y):
 a=(C,x);b=(D,y);comm=mul(mul(mul(inverse(a),inverse(b)),a),b)
 vals=[power(a,2),power(b,4),power(mul(a,b),5),power(comm,3)]
 assert all(p==I for p,v in vals)
 return sum(v<<(16*j) for j,(p,v) in enumerate(vals))
def rank(vecs):
 B={}
 for v in vecs:
  while v:
   p=v.bit_length()-1
   if p in B:v^=B[p]
   else:B[p]=v;break
 return len(B)
constraints=[resid(1<<i,0) for i in range(16)]+[resid(0,1<<i) for i in range(16)]
inner=[(ma(C,1<<i)^(1<<i)) | ((ma(D,1<<i)^(1<<i))<<16) for i in range(16)]
assert all(resid(x&65535,x>>16)==0 for x in inner)
assert rank(constraints) == 16 and rank(inner) == 16
print('tensor cocycle: constraint rank 16, Z1 dimension 16, B1 dimension 16, H1 dimension 0')

def eact(v,p,kind):
 if kind=='split': return actm(v&15,p)| (v&16)
 if kind=='J':
  z=0
  for i in range(5):
   if v>>i&1:z^=1<<p[i]
  if z>>5:z^=63
  return z
 if kind=='dual':
  z=0
  for i in range(5):
   if v>>i&1:z^=(1<<p[i])^(1<<p[5])
  return z&31

def nact(v,p):return actn(v,p)
def vecgen(f,v):
 seen={v};q=[v]
 for x in q:
  for fn in f:
   y=fn(x)
   if y not in seen:seen.add(y);q.append(y)
 return seen
def comp(a,b):return [a[b[i]] for i in range(len(a))]
def powperm(a,n):
 b=list(range(len(a)))
 for i in range(n):b=comp(a,b)
 return b
p6=comp(c6,d6);p5=comp(c5,d5)
assert powperm(p6,5)==list(range(6)) and powperm(p5,5)==list(range(5))
pairs={(tuple(range(6)),tuple(range(5)))}; queue=list(pairs)
for a,b in queue:
 for aa,bb in ((c6,c5),(d6,d5)):
  q=(tuple(comp(a,aa)),tuple(comp(b,bb)))
  if q not in pairs:pairs.add(q);queue.append(q)
assert len(pairs)==120
h6,h5=next((list(a),list(b)) for a,b in sorted(pairs) if powperm(a,4)==list(range(6)) and powperm(a,2)!=list(range(6)) and comp(comp(a,p6),[a.index(i) for i in range(6)]) in [powperm(p6,i) for i in range(1,5)])
for kind in ('split','J','dual'):
 def pp(v):return eact(v,p6,kind)
 U={v^pp(v) for v in range(32)};assert len(U)==16
 def lin(cols,v):
  out=0
  for i in range(4):
   if v>>i&1:out^=cols[i]
  return out
 maps=[]
 for cols in product(U,repeat=4):
  if any(eact(cols[i],q,kind)!=lin(cols,nact(1<<i,r)) for i in range(4) for q,r in ((p6,p5),(h6,h5))):continue
  mapping={n:lin(cols,n) for n in range(16)}
  if len(set(mapping.values()))==16:maps.append(mapping)
 assert len(maps)==1
 phi=maps[0]
 C9=lambda v: nact(v&15,c5) | (eact(v>>4,c6,kind)<<4)
 D9=lambda v: nact(v&15,d5) | (eact(v>>4,d6,kind)<<4)
 orbs=[];unseen=set(range(512))
 while unseen:
  o=vecgen((C9,D9),min(unseen));orbs.append(o);unseen-=o
 print(kind,'orbit sizes',sorted(len(o) for o in orbs))
 for mode in ('Eonly','diagonal'):
  W={((n if mode=='diagonal' else 0)|(phi[n]<<4)) for n in range(16)}; assert len(W)==16
  keys=sorted({min(v^w for w in W) for v in range(512)});idx={v:i for i,v in enumerate(keys)}
  rows=[]
  for o in orbs:
   m=0;ok=True
   for x in o:
    b=1<<idx[min(x^w for w in W)]
    if m&b:ok=False;break
    m|=b
   if ok:rows.append((m,o))
  bykey=[[] for _ in keys]
  for m,o in rows:
   for j in range(32):
    if m>>j&1:bykey[j].append((m,o))
  full=(1<<32)-1;found=[]
  def solve(covered,chosen):
   if covered==full:found.append(chosen);return
   holes=[j for j in range(32) if not covered>>j&1]
   j=min(holes,key=lambda h:sum(not (m&covered) for m,o in bykey[h]))
   for m,o in bykey[j]:
    if not(m&covered):solve(covered|m,chosen+[o])
  solve(0,[])
  expected = {('split','Eonly'): 1, ('split','diagonal'): 4, ('J','Eonly'): 0, ('J','diagonal'): 2, ('dual','Eonly'): 1, ('dual','diagonal'): 4}
  assert len(found) == expected[(kind,mode)]
  assert all(any(0 in orbit for orbit in sol) for sol in found)
  if (kind,mode)==('J','Eonly'):
   assert sorted(len(o) for _,o in rows)==[1,5,10,10]
  print(' ',mode,'eligible',[(len(o),0 in o) for m,o in rows], 'covers',len(found), 'withzero',sum(any(0 in o for o in sol) for sol in found))

  for sol in found:
   k=set().union(*sol); span={0}
   for v in k:span|={x^v for x in list(span)}
   fixed=[v for v in range(1,512) if C9(v)==v and D9(v)==v]
   periods=[v for v in fixed if {x^v for x in k}==k]
   print('   K0 is span',len(span)==32,'span',len(span),'fixed',fixed,'periods',periods)

from itertools import combinations


def check_j_h1_restriction():
 c=(1,0,3,2,5,4);d=(0,2,3,4,1,5);I=tuple(range(6))
 def mul(a,b):return tuple(a[b[i]] for i in range(6))
 def inv(p):return tuple(p.index(i) for i in range(6))
 def act(p,v):
  z=0
  for i in range(5):
   if v>>i&1:z^=1<<p[i]
  if z>>5:z^=63
  return z
 G={I};queue=[I]
 for a in queue:
  for b in (c,d):
   x=mul(a,b)
   if x not in G:G.add(x);queue.append(x)
 assert len(G)==120
 def order(p):
  a=p;n=1
  while a!=I:a=mul(a,p);n+=1
  return n
 p=mul(c,d);P={I};a=I
 for _ in range(4):a=mul(a,p);P.add(a)
 assert len(P)==5
 h=next(a for a in sorted(G) if order(a)==4 and mul(mul(a,p),inv(a)) in P)
 def fixedproj(v):
  out=0;a=I
  for _ in range(5):out^=act(a,v);a=mul(a,p)
  return out
 sol=[]
 for x,y in product(range(32),repeat=2):
  f={I:0};q=[I];good=True
  for g in q:
   for a,v in ((c,x),(d,y)):
    k=mul(g,a);val=f[g]^act(g,v)
    if k in f:
     if f[k]!=val:good=False;break
    else:f[k]=val;q.append(k)
   if not good:break
  if good:sol.append((x,y,f))
 B={(v^act(c,v),v^act(d,v)) for v in range(32)}
 assert len(sol)==64 and len(B)==32
 values={fixedproj(f[h]) for x,y,f in sol}
 principals={fixedproj(f[h]) for x,y,f in sol if (x,y) in B}
 assert len(values)==2 and principals=={0}
 print('J H1 normalizer restriction: 64 cocycles, 32 principal, nonzero restriction')

check_j_h1_restriction()


def check_j_split_involutions():
 I6=tuple(range(6));I5=tuple(range(5))
 def pc(a,b):return tuple(a[b[i]] for i in range(len(a)))
 def inv(a):return tuple(a.index(i) for i in range(len(a)))
 pair={(I6,I5)};queue=[(I6,I5)]
 for a,b in queue:
  for x,y in ((c6,c5),(d6,d5)):
   q=pc(a,x),pc(b,y)
   if q not in pair:pair.add(q);queue.append(q)
 assert len(pair)==120 and len({a for a,b in pair})==120
 G={a:b for a,b in pair}
 def action(g,v):return actn(v&15,G[g])|(eact(v>>4,g,'J')<<4)
 def mul(a,b):g,v=a;h,w=b;return pc(g,h),v^action(g,w)
 def inverse(a):g,v=a;h=inv(g);return h,action(h,v)
 def conj(a,b):return mul(mul(a,b),inverse(a))
 z=(I6,0)
 def pp(v):return eact(v,p6,'J')
 U={v^pp(v) for v in range(32)}
 def lin(cols,v):
  r=0
  for i in range(4):
   if v>>i&1:r^=cols[i]
  return r
 maps=[]
 for cols in product(U,repeat=4):
  if any(eact(cols[i],q,'J')!=lin(cols,actn(1<<i,r)) for i in range(4) for q,r in ((p6,p5),(h6,h5))):continue
  mapping=[lin(cols,n) for n in range(16)]
  if len(set(mapping))==16:maps.append(mapping)
 assert len(maps)==1;phi=maps[0]
 W={n|(phi[n]<<4) for n in range(16)}
 # F20 is the normalizer of the five-cycle.
 P={tuple(powperm(p6,i)) for i in range(5)}
 F={g for g in G if pc(pc(g,p6),inv(g)) in P};assert len(F)==20
 H={(g,w) for g in F for w in W}; assert len(H)==320
 # All invariant radical transversals under diagonal W.
 C=lambda x:action(tuple(c6),x); DD=lambda x:action(tuple(d6),x)
 orb=[];rem=set(range(512))
 while rem:
  o=vecgen((C,DD),min(rem));orb.append(o);rem-=o
 key=lambda v:min(v^w for w in W)
 keys=sorted({key(v) for v in range(512)});ind={x:i for i,x in enumerate(keys)}
 rows=[]
 for o in orb:
  bits=0
  for x in o:bits|=1<<ind[key(x)]
  if bits.bit_count()==len(o):rows.append((bits,o))
 ans=[]
 def solve(bits,chosen):
  if bits==(1<<32)-1:ans.append(set().union(*chosen));return
  j=next(i for i in range(32) if not bits>>i&1)
  for m,o in rows:
   if m>>j&1 and not(m&bits):solve(bits|m,chosen+[o])
 solve(0,[]);assert len(ans)==2 and all(0 in s for s in ans)
 T={pc(pc(g,c6),inv(g)) for g in G};assert len(T)==10
 allinv={(g,v) for g in T for v in range(512) if action(g,v)==v}; assert len(allinv)==640
 # The ambient group is generated by two S5 lifts and the nine translations.
 gens=[(tuple(c6),0),(tuple(d6),0)]+[(I6,1<<j) for j in range(9)]
 classes=[]
 while allinv:
  x=min(allinv);seen={x};q=[x]
  for y in q:
   for a in gens:
    b=conj(a,y)
    if b not in seen:seen.add(b);q.append(b)
  classes.append(seen);allinv-=seen
 class_data=[(len(cc),sum(v==0 for g,v in cc)) for cc in classes]
 assert sorted(class_data)==[(80,0),(80,10),(240,0),(240,0)]
 print('J split involution classes (size,pure):',class_data,flush=True)
 combos=[ii for n in range(1,len(classes)+1) for ii in combinations(range(len(classes)),n) if sum(len(classes[i]) for i in ii)==160]
 assert len(combos)==1
 print('J split radical choices',len(ans),'fiber class combinations',len(combos),flush=True)
 for ix,(k0,sel) in enumerate(product(ans,combos)):
  K={(I6,v) for v in k0}
  for i in sel:K.update(classes[i])
  assert len(K)==192
  # A transversal iff K H has no collisions.
  cos={}; fail=None
  for k in sorted(K):
   for h in H:
    x=mul(k,h)
    if x in cos:fail=(cos[x],k);break
    cos[x]=k
   if fail:break
  assert fail is not None
  print('J split case',ix,'classes',sel,'transversal failure',fail,flush=True)

check_j_split_involutions()
