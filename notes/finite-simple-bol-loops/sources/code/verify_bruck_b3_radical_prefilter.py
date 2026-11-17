#!/usr/bin/env python3
"""Fixed-shadow b=3 two-N radical prefilter; not a folder construction.

Uses only reviewed quadratic-support/P6 and one-M module models. The full
rank-two ordered pairs and eight shears are checked, with one representative
per F20 orbit on U1. Assertions must remain enabled.
"""
assert __debug__
from pathlib import Path
import runpy,io,contextlib,itertools
path=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
 z=runpy.run_path(str(path/'verify_bruck_n_quadratic_support.py')); a=runpy.run_path(str(path/'verify_bruck_one_m_noncentral.py'))
add=z['add'];rank=z['rank']; null=a['nullspace'];nact=a['nact'];mv=a['mv'];gens=(a['p'],a['qgen'])
def hom(domain, codomain, dim):
 eq=[]
 for pp in gens:
  for i in range(4):
   for bit in range(dim):
    v=nact(1<<i,pp[0]);row=0
    for j in range(4):
     if v>>j&1:row^=1<<(dim*j+bit)
    for j in range(dim):
     if codomain(1<<j,pp)>>bit&1:row^=1<<(dim*i+j)
    eq.append(row)
 return [tuple((h>>(dim*i))&((1<<dim)-1) for i in range(4)) for h in null(eq,4*dim)]
def sols(inds,rr):
 piv={}
 for row in rr:add(piv,sum(((row>>i)&1)<<j for j,i in enumerate(inds)))
 out=[]
 for i in range(len(inds)):
  if i in piv:continue
  v=1<<i
  for j in sorted(piv):
   if (piv[j]&v).bit_count()&1:v|=1<<j
  out.append(sum(((v>>j)&1)<<h for j,h in enumerate(inds)))
 return out

import itertools
d=z['component']('P6');base=d['base'];mon=d['mon'];feat=d['feat'];rows=d['allrows']+d['extra']
def qco(co,v):
 f=feat(v);out=0
 for i in range(len(mon)):
  if f>>i&1:out^=(co>>(4*i))&15
 return out
cross=sols(d['groups']['XU0'],rows);top,=sols(d['groups']['U0'],rows)
X=next(x for x in hom(None,lambda x,p:d['baseact'](x,p[1]),base) if rank(x)==4)
hs=hom(None,lambda x,p:a['uact'](x,p[0]) if p==gens[1] else nact(x&15,p[0])|(nact(x>>4,p[0])<<4),8)
eps=lambda v:((v&15)^(v>>4))*17
Soc=tuple(eps(x) for x in next(h for h in hs if rank(eps(x) for x in h)==4));Dc=next(h for h in hs if rank(h+Soc)==8)
U=lambda x,i:x<<(base+8*i)
f=a['u1'];one=63

# q-basis indexed X, U(i,k), cross(i,k), pair(i,j,k), using full d equations.
from functools import lru_cache
full=d['allrows'];QX=sols(d['groups']['X'],full);QU=sols(d['groups']['U0'],full);Qpair=sols(d['groups']['U0U1'],full)
def pairval(c,x,y):return qco(c,U(x,0)|U(y,1))
psi=next(c for c in [Qpair[0],Qpair[1],Qpair[0]^Qpair[1]] if all(pairval(c,v,v)==0 for v in range(256)))
epspsi=next(c for c in [Qpair[0],Qpair[1],Qpair[0]^Qpair[1]] if all(pairval(c,x,y)==pairval(psi,eps(x),y) for x in (1,2,4,8,16,32,64,128) for y in (1,2,4,8,16,32,64,128)))
terms=[('X',0,0,QX[0])]
for i in range(3):
 for k,c in enumerate(QU):terms.append(('U',i,k,c))
for i in range(3):
 for k,c in enumerate(cross):terms.append(('XU',i,k,c))
for i in range(3):
 for j in range(i+1,3):
  for k,c in enumerate((psi,epspsi)):terms.append(('PAIR',3*i+j,k,c))
@lru_cache(None)
def termval(index,v):
 typ,i,k,c=terms[index];x=v&63;u=[(v>>(base+8*j))&255 for j in range(3)]
 if typ=='X':return qco(c,x)
 if typ=='U':return qco(c,U(u[i],0))
 if typ=='XU':return qco(c,x|U(u[i],0))
 return qco(c,U(u[i//3],0)|U(u[i%3],1))


from functools import lru_cache
@lru_cache(None)
def feature(v):
 vals=[termval(i,v) for i in range(len(terms))]
 return tuple(sum(((val>>bit)&1)<<i for i,val in enumerate(vals)) for bit in range(4))
rowsR=[]
for j in range(3):
 u=U(Dc[0],j); zf=tuple(x^y^z for x,y,z in zip(feature(one^u),feature(one),feature(u)))
 rowsR.append(zf[0])

# K=<e2,e3>, z=e2, v=e3, top graph 0.
kern=[U(Soc[i],1) for i in range(4)]+[X[i]^U(Soc[i],2) for i in range(4)]
gens=[kern[:4],kern[4:8]]+[[U(Dc[i],j) for i in range(4)] for j in (1,2)]
bas=[f,one]+sum(gens,[]); eq=[]
for v in bas+[x^y for x,y in itertools.combinations(bas,2)]:eq.extend(feature(v))
zero=null(eq+rowsR,len(terms)); mat=eq+[r|((int(j==0))<<len(terms)) for j,r in enumerate(rowsR)]
q0=next(v for v in null(mat,len(terms)+1) if v>>len(terms)&1)&((1<<len(terms))-1)
print('affine q0',q0,'zero basis',zero,'dim',len(zero),flush=True)
@lru_cache(None)
def val(co,v):return reduce(int.__xor__,(termval(i,v) for i in range(len(terms)) if co>>i&1),0)
def pol(co,v,w):return val(co,v)^val(co,w)^val(co,v^w)
def tact(v):
 out=d['baseact'](v&63,d['c6'])
 for j in range(3):out^=U(a['uact']((v>>(base+8*j))&255,d['c5']),j)
 return out
bs=[1<<i for i in range(30)];sm=bs+[x^y for x,y in itertools.combinations(bs,2)]
im=[(1<<i)^nact(1<<i,d['c5']) for i in range(4)]; piv={}
for v in im:
 while v:
  j=(v&-v).bit_length()-1
  if j in piv:v^=piv[j]
  else:piv[j]=v;break
def red(v):
 for j in sorted(piv):
  if v>>j&1:v^=piv[j]
 return v
@lru_cache(None)
def signature(co):return tuple(red(pol(co,v,tact(v))) for v in sm)
@lru_cache(None)
def radline(co):return tuple(pol(co,v,w) for v in gens[0] for w in bs)

from functools import reduce

# These data are defined by the solved coefficient equations, not an assumed
# seven-generator list. The component solver's symbols use F2 bit vectors.
assert len(zero)==7
forms=spanforms=[reduce(int.__xor__,(zero[j] for j in range(7) if mask>>j&1),0) for mask in range(128)]
assert len(set(forms))==128
R=[1<<i for i in range(6)]+[U(1<<i,j) for j in (1,2) for i in range(8)]
assert len(R)==22 and len(bas)==18
# Derive F20 orbits using its actual actions on the U1 module.
def action(u,g):
 perm=g[0]
 parity=sum(perm[i]>perm[j] for i in range(5) for j in range(i+1,5))%2
 if parity:return a['uact'](u,perm)
 return nact(u&15,perm)|(nact(u>>4,perm)<<4)
remaining=set(range(256));orbits=[]
while remaining:
 u=min(remaining);orbit={action(u,g) for g in a['F']}
 assert u in orbit and orbit<=remaining
 orbits.append(orbit);remaining-=orbit
assert len(orbits)==19 and sum(map(len,orbits))==256
reps=[min(o) for o in orbits]
allforms=[q0]+forms
# Check the reduction's zero and fixed-shadow hypotheses for every scalar form.
for form in allforms:
 assert all(val(form,v)==0 for v in R)
 assert all(pol(form,v,w)==0 for v,w in itertools.combinations(R,2))
 assert all(val(form,v)==0 for v in bas)
 assert all(pol(form,v,w)==0 for v,w in itertools.combinations(bas,2))
# Explicit subspace-set construction is independent of the earlier bit-pivot
# implementation; it also certifies alpha and ell0 invariance at each point.
def values(q,u,vecs):return tuple(pol(q,U(u,0),v) for v in vecs)
bdata=[[values(q,u,bas) for u in reps] for q in allforms]
rdata=[[values(q,u,R) for u in reps] for q in allforms]
qdata=[[val(q,U(u,0)) for u in reps] for q in allforms]
fdata=[[pol(q,f,U(u,0)) for u in reps] for q in allforms]
sigs=[signature(q) for q in allforms];rads=[radline(q) for q in allforms]
assert len(set(sigs[1:]))==2 and len(set(rads[1:]))==2
from collections import Counter
masks=Counter();counts=[[0]*8 for _ in range(2)];total=0
independent_masks=Counter();independent_counts=[[0]*8 for _ in range(2)];independent_total=0
for i in range(1,129):
 for j in range(1,129):
  sig0=tuple(x^y for x,y in zip(sigs[0],sigs[i]));sig1=sigs[j]
  if not(any(sig0) or any(sig1)):continue
  assert not(any(sig0) and any(sig1) and sig0!=sig1)
  total+=1; radical=not any(x^y for x,y in zip(rads[0],rads[i])) and not any(rads[j]);mask=255
  for k,u in enumerate(reps):
   B=[(x^y)|(z<<4) for x,y,z in zip(bdata[0][k],bdata[i][k],bdata[j][k])]
   S={0}
   for v in B:S|={x^v for x in S}
   RR=[(x^y)|(z<<4) for x,y,z in zip(rdata[0][k],rdata[i][k],rdata[j][k])]
   if any(x not in S for x in RR):mask=0;break
   q=qdata[0][k]^qdata[i][k]^(qdata[j][k]<<4)
   fpol=fdata[0][k]^fdata[i][k]^(fdata[j][k]<<4)
   top=(u&15)^(u>>4)
   assert fpol in S and top in S
   for t in range(8):
    if mask>>t&1:
     z=q^(fpol if t&1 else 0)^(top if t&2 else 0)^((top<<4) if t&4 else 0)
     if z not in S:mask&=~(1<<t)
   if not mask:break
  masks[mask]+=1
  independent=allforms[j]!=0
  if independent:
   independent_total+=1;independent_masks[mask]+=1
  for t in range(8):
   counts[int(radical)][t]+=(mask>>t)&1
   if independent:independent_counts[int(radical)][t]+=(mask>>t)&1
assert total==12288
assert masks==Counter({0:2432,15:68,240:68,255:9720})
assert counts==[[8160]*8,[1628]*8]
assert independent_total==12224
assert independent_masks==Counter({0:2432,15:4,240:68,255:9720})
assert independent_counts==[[8128]*4+[8160]*4,[1596]*4+[1628]*4]
print('independent-center population:',independent_total,dict(sorted(independent_masks.items())),independent_counts)
print('b3 radical prefilter passed:', total, 'pairs;', len(orbits), 'F20 orbits;', dict(sorted(masks.items())))
