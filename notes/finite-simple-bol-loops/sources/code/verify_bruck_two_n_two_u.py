#!/usr/bin/env python3
"""P6 + 2U / 2N: exact F20 shadow and quadratic-component test.

Imports verify_bruck_n_quadratic_support.py (which imports the P6 and
one-M verifiers), and verify_bruck_one_m_noncentral.py. Assertions required.
"""
assert __debug__
import runpy,io,contextlib,itertools
from collections import Counter
from pathlib import Path
path=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
 z=runpy.run_path(str(path/'verify_bruck_n_quadratic_support.py'))
 a=runpy.run_path(str(path/'verify_bruck_one_m_noncentral.py'))
add=z['add'];rank=z['rank'];null=a['nullspace'];nact=a['nact'];mv=a['mv'];gens=(a['p'],a['qgen'])
def hom(codomain,dim):
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

with contextlib.redirect_stdout(io.StringIO()): d=z['component']('P6')
base=d['base'];mon=d['mon'];feat=d['feat']; rows=d['allrows'];extra=d['extra']
qspaces=[]
for key in ('X','U0','XU0','U0U1'):
 for co in sols(d['groups'][key],rows):qspaces.append((co,False,key))
for key in ('U0','XU0'):
 for co in sols(d['groups'][key],rows):qspaces.append((co,True,key+'swap'))
assert len(qspaces)==11
assert Counter(k for _,_,k in qspaces)=={'X':1,'U0':2,'U0swap':2,'XU0':2,'XU0swap':2,'U0U1':2}
print('basis component dimensions:',Counter(k for _,_,k in qspaces),flush=True)
def swap(v):
 low=v&63;a=(v>>6)&255;b=(v>>14)&255
 return low|(b<<6)|(a<<14)
def qval(co,sw,v):
 f=feat(swap(v) if sw else v); out=0
 while f:
  bit=f&-f; j=bit.bit_length()-1; out^=(co>>(4*j))&15;f^=bit
 return out
def signature(v):return tuple(qval(co,sw,v) for co,sw,_ in qspaces)
X=next(x for x in hom(lambda x,p:d['baseact'](x,p[1]),base) if rank(x)==4)
hs=hom(lambda x,p:a['uact'](x,p[0]) if p==gens[1] else nact(x&15,p[0])|(nact(x>>4,p[0])<<4),8)
eps=lambda v:((v&15)^(v>>4))*17
Soc=tuple(eps(x) for x in next(h for h in hs if rank(eps(x) for x in h)==4));D=next(h for h in hs if rank(h+Soc)==8)
# Align the top and socle intertwiners for the stable U-graph test.
assert tuple(eps(v) for v in D)==Soc
def embed(i,s):
 return (mv(X,s) if i&1 else 0)^((mv(D,s) if i&2 else 0)<<6)^((mv(Soc,s) if i&4 else 0)<<6)^((mv(D,s) if i&8 else 0)<<14)^((mv(Soc,s) if i&16 else 0)<<14)
planes={}
for x,y,z0 in itertools.combinations(range(1,32),3):
 if rank([x,y,z0])!=3:continue
 span=tuple(sorted((0,x,y,z0,x^y,x^z0,y^z0,x^y^z0)))
 planes.setdefault(span,(x,y,z0))
assert len(planes)==155
f=a['u1'];other=a['u2'];assert f^other==63
assert rank([f,other])==2
assert all(d['baseact'](v,pp[1])==v for v in (f,other) for pp in gens)
# Build equations for d=0 via direct test on basis vectors and pair sums.
t5,t6=z['m']['c5'],z['m']['c6']
def source(v):
 return d['baseact'](v&63,t6)|(a['uact']((v>>6)&255,t5)<<6)|(a['uact']((v>>14)&255,t5)<<14)
im=[(1<<i)^nact(1<<i,t5) for i in range(4)]
ann=[a0 for a0 in range(1,16) if all((a0&u).bit_count()%2==0 for u in im)]
basis=[1<<i for i in range(22)]
drows=[]
for v in basis+[x^y for x,y in itertools.combinations(basis,2)]:
 sv=signature(v);tv=source(v);st=signature(tv);sx=signature(v^tv)
 vals=[sv[i]^st[i]^sx[i] for i in range(11)]
 for cov in ann:drows.append(sum((((v0&cov).bit_count()&1)<<i) for i,v0 in enumerate(vals)))
# β(1,V) must be nonzero in at least one central component.
constrows=[]
for v in basis:
 s1=signature(63);s2=signature(v);s3=signature(63^v)
 for bit in range(4):constrows.append(sum(((((s1[i]^s2[i]^s3[i])>>bit)&1)<<i) for i in range(11)))
assert 11-rank(drows)==8 and rank(constrows)==2
print('d0 dimension',11-rank(drows),'global constant-polar rank',rank(constrows),flush=True)
results=Counter();examples=[]
for plane,gens3 in planes.items():
 vec=[embed(g,1<<i) for g in gens3 for i in range(4)]+[f,other]
 sig=[signature(v) for v in vec]; eq=[]
 for value in sig:
  for bit in range(4):eq.append(sum(((value[i]>>bit)&1)<<i for i in range(11)))
 for i,j in itertools.combinations(range(len(vec)),2):
  qij=signature(vec[i]^vec[j]); vals=[sig[i][k]^sig[j][k]^qij[k] for k in range(11)]
  for bit in range(4):eq.append(sum(((vals[k]>>bit)&1)<<k for k in range(11)))
 dim=11-rank(eq);dim0=11-rank(eq+drows); dimconst=rank(eq+constrows)-rank(eq)
 c=sum(1 for v in plane if v & ~20==0).bit_length()-1
 results[(c,dim,dim0,dimconst)]+=1
 if dim>=2 and dim0>=1 and dimconst>0:
  examples.append((gens3,c,dim,dim0,dimconst))
print('classes',sorted(results.items()),flush=True)
assert len(examples)==6
for gens3,c,dim,dim0,dimconst in examples:
 span={0}
 for g in gens3: span |= {v^g for v in list(span)}
 assert 1 in span and c==1
 soc=next(v for v in span if v and v & ~20==0)
 assert any((v&1)==0 and (v&10) and (((v&2)<<1)|((v&8)<<1))==soc for v in span)
print('surviving planes',len(examples),'examples',examples[:10],flush=True)
