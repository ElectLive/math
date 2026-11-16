#!/usr/bin/env python3
"""Fixed component checks for the one-M noncentral radical reduction.

Synchronized five/six-point S5 actions; U=N tensor F2[C2].
Standard library only; Python 3.11+, assertions enabled.
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

# J is the six-point module modulo constants; U is two N coordinates
# swapped by either odd generator, with N action on both coordinates.
def jact(v,p):
 out=0
 for i in range(5):
  if v>>i&1:out^=1<<p[i]
 return (out^63 if out&32 else out)&31
def uact(v,p):return nact(v>>4,p)|(nact(v&15,p)<<4)
def nullspace(rows,n):
 piv={}
 for r in rows:add(piv,r)
 out=[]
 for i in range(n):
  if i in piv:continue
  v=1<<i
  for j in sorted(piv):
   if (piv[j]&v).bit_count()&1:v|=1<<j
  assert all((r&v).bit_count()%2==0 for r in rows)
  out.append(v)
 return out
# End_A(U) from commuting equations.
endrows=[]
for p5 in (c5,d5):
 cols=[uact(1<<i,p5) for i in range(8)]
 for i in range(8):
  for j in range(8):
   row=0
   for k in range(8):
    if cols[j]>>k&1:row^=1<<(8*k+i)
    if cols[k]>>i&1:row^=1<<(8*j+k)
   endrows.append(row)
end=nullspace(endrows,64)
assert len(end)==2
idmask=sum(1<<(8*i+i) for i in range(8))
epscols=tuple(((1<<i) if i<4 else (1<<(i-4))) | ((1<<(i+4)) if i<4 else (1<<i)) for i in range(8))
epsmask=sum(x<<(8*i) for i,x in enumerate(epscols))
assert idmask in {0,end[0],end[1],end[0]^end[1]}
assert epsmask in {end[0],end[1],end[0]^end[1]} and epsmask!=idmask
assert all(mv(epscols,mv(epscols,1<<i))==0 for i in range(8))

def spaces(kind):
 base=6 if kind=='P6' else 5; dim=base+8
 def source(v,p5,p6):
  x=v&((1<<base)-1); y=v>>base
  return (pact(x,p6) if kind=='P6' else jact(x,p6)) | (uact(y,p5)<<base)
 mon=[(i,i) for i in range(dim)]+list(combinations(range(dim),2))
 def feat(v):return sum(((v>>i&1)&(v>>j&1))<<k for k,(i,j) in enumerate(mon))
 samples=[1<<i for i in range(dim)]+[(1<<i)^(1<<j) for i,j in combinations(range(dim),2)]
 rows=[]
 for p5,p6 in ((c5,c6),(d5,d6)):
  for v in samples:
   a=feat(v);b=feat(source(v,p5,p6))
   for bit in range(4):
    row=0
    for k in range(len(mon)):
     if b>>k&1:row^=1<<(4*k+bit)
     if a>>k&1:
      for j in range(4):
       if mact(1<<j,p6)>>bit&1:row^=1<<(4*k+j)
    rows.append(row)
 groups={'X':[],'U':[],'cross':[]}
 for k,(i,j) in enumerate(mon):
  key='X' if j<base else 'U' if i>=base else 'cross'
  groups[key].extend(4*k+x for x in range(4))
 def restrict(indices):
  return [sum(((r>>i)&1)<<j for j,i in enumerate(indices)) for r in rows]
 sx=nullspace(restrict(groups['X']),len(groups['X']))
 su=nullspace(restrict(groups['U']),len(groups['U']))
 sc=nullspace(restrict(groups['cross']),len(groups['cross']))
 assert [len(sx),len(su),len(sc)]==[1,0,2]
 inds=groups['cross']
 def lift(co):return sum(((co>>j)&1)<<i for j,i in enumerate(inds))
 def q(co,v):
  f=feat(v);out=0
  for i in range(len(mon)):
   if f>>i&1:out^=(co>>(4*i))&15
  return out
 def eps(v):return mv(epscols,v>>base)<<base
 images=[]
 for co in sc:
  full=lift(co);res=0
  for j,i in enumerate(inds):
   bit=i%4; x,y=mon[i//4]
   val=q(full,(1<<x)^eps(1<<y))^q(full,1<<x)^q(full,eps(1<<y))
   if val>>bit&1:res|=1<<j
  images.append(res)
 assert rank(images)==1 and all(v in {0,sc[0],sc[1],sc[0]^sc[1]} for v in images)

 # Hom_F(S, X⊕U): generators p (even) and qgen (odd).
 def umat(v,g,odd):
  a=v&15;b=v>>4
  return ((nact(b,g[0]) | (nact(a,g[0])<<4)) if odd else
          (nact(a,g[0]) | (nact(b,g[0])<<4)))
 def xumat(v,g,odd):
  x=v&((1<<base)-1); y=v>>base
  return (pact(x,g[1]) if kind=='P6' else jact(x,g[1])) | (umat(y,g,odd)<<base)
 arrows=[]
 for g,odd in ((p,False),(qgen,True)):
  A=[nact(1<<i,g[0]) for i in range(4)]
  B=[xumat(1<<i,g,odd) for i in range(dim)]
  for j in range(4):
   for i in range(dim):
    row=0
    for k in range(4):
     if A[j]>>k&1:row^=1<<(dim*k+i)
    for k in range(dim):
     if B[k]>>i&1:row^=1<<(dim*j+k)
    arrows.append(row)
 inter=nullspace(arrows,4*dim);assert len(inter)==3
 lines=[]
 for mask in range(1,8):
  co=0
  for i in range(3):
   if mask>>i&1:co^=inter[i]
  cols=tuple((co>>(dim*i))&((1<<dim)-1) for i in range(4))
  assert rank(cols)==4
  lines.append(cols)
 def basis(vs):
  piv={}
  for v in vs:add(piv,v)
  return tuple(piv.values())
 planes={}
 for i,j in combinations(range(7),2):
  B=basis(lines[i]+lines[j]);assert len(B)==8
  planes[frozenset(mv(B,v) for v in range(256))]=B
 assert len(planes)==7
 # On U the two F-complements to the socle avoid C_U(t).
 pure=[tuple(v>>base for v in B) for B in lines if all((v&((1<<base)-1))==0 for v in B)]
 assert len(pure)==3
 timg=tuple((1<<i)^uact(1<<i,c5) for i in range(8))
 def intersection_dim(A,B):return rank(A)+rank(B)-rank(A+B)
 soc=tuple(epscols)
 assert sorted(intersection_dim(B,timg) for B in pure)==[0,0,3]
 assert all((intersection_dim(B,soc)==4)==(intersection_dim(B,timg)==3) for B in pure)
 xS=[v if kind=='P6' else (v^63 if v&32 else v)&31 for v in S]
 qx=sum(((sx[0]>>j)&1)<<i for j,i in enumerate(groups['X']))
 assert all(q(qx,mv(xS,v))!=0 for v in range(1,16))
 unit=next(i for i,v in enumerate(images) if v)
 unitco=lift(sc[unit]);epsco=lift(images[unit])
 expected={('unit',0):(3,1,1,0),('unit',1):(3,1,1,0),
           ('eps',0):(3,2,1,1),('eps',1):(3,0,1,0)}
 for label,cr in (('unit',unitco),('eps',epsco)):
  for eta in (0,1):
   co=cr^(qx if eta else 0)
   goodL=[B for B in lines if all(q(co,mv(B,v))==0 for v in range(16))]
   goodP=[B for B in planes.values() if all(q(co,mv(B,v))==0 for v in range(256))]
   xp=lambda B:rank(v&((1<<base)-1) for v in B)
   result=(sum(xp(B)==0 for B in goodL),sum(xp(B)>0 for B in goodL),
           sum(xp(B)==0 for B in goodP),sum(xp(B)>0 for B in goodP))
   assert result==expected[(label,eta)]
   if label=='eps' and eta==0:
    exceptional=next(B for B in goodP if xp(B)>0)
    expected_plane=xS+[v<<base for v in soc]
    assert rank(exceptional+tuple(expected_plane))==8
    assert all(v.bit_count()%2==0 for v in xS)
    tx=[((1<<i)^(pact(1<<i,c6) if kind=='P6' else jact(1<<i,c6))) for i in range(base)]
    assert rank(tx)==(3 if kind=='P6' else 2)
    assert all(v.bit_count()%2==0 for v in tx)
 print(kind,': qX nonzero on 15 S vectors; unit/epsilon line-plane checks passed')

 print(kind,': Q(X)->M 1; Q(U)->M 0; X tensor U -> M 2; epsilon rank 1')
spaces('J');spaces('P6')
# Bilinear U×U -> M, checked independently on the two-generator action.
rows=[]
for p5,p6 in ((c5,c6),(d5,d6)):
 U=[uact(1<<i,p5) for i in range(8)]
 for x in range(8):
  for y in range(8):
   for bit in range(4):
    row=0
    for i in range(8):
     for j in range(8):
      if U[x]>>i&1 and U[y]>>j&1:row^=1<<(4*(8*i+j)+bit)
    for k in range(4):
     if mact(1<<k,p6)>>bit&1:row^=1<<(4*(8*x+y)+k)
    rows.append(row)
assert len(nullspace(rows,256))==0
print('End(U): dual numbers; Hom(U tensor U,M)=0; paired S5 order 120')
