#!/usr/bin/env python3
"""Fixed-component checks for proposed N-Frattini quadratic support."""
from pathlib import Path
import runpy,contextlib,io,itertools
assert __debug__
with contextlib.redirect_stdout(io.StringIO()):
 m=runpy.run_path(str(Path(__file__).with_name("verify_bruck_p6_frattini.py")))
add,rank=m["add"],m["rank"]
def component(kind):
 b=2;target="N"
 base=6 if kind=='P6' else 5;dim=base+8*b
 c5,d5,c6,d6=m['c5'],m['d5'],m['c6'],m['d6'];pact,mact,nact=m['pact'],m['mact'],m['nact']
 def baseact(v,p):
  if kind=='P6':return pact(v,p)
  out=0
  for i in range(5):
   if v>>i&1:out^=1<<p[i]
  return (out^63 if out&32 else out)&31
 def source(v,p5,p6):
  out=baseact(v&((1<<base)-1),p6)
  for j in range(b):
   x=(v>>(base+8*j))&255
   y=nact(x>>4,p5)|(nact(x&15,p5)<<4)
   out|=y<<(base+8*j)
  return out
 fn,ind=(mact,1) if target=='M' else (nact,0)
 mon=[(i,i) for i in range(dim)]+list(itertools.combinations(range(dim),2)); n=len(mon)*4
 def feat(v):return sum(((v>>i&1)&(v>>j&1))<<k for k,(i,j) in enumerate(mon))
 samples=[1<<i for i in range(dim)]+[(1<<i)^(1<<j) for i,j in itertools.combinations(range(dim),2)]
 rows={}
 allrows=[]
 for p5,p6 in ((c5,c6),(d5,d6)):
  for v in samples:
   f=feat(v);g=feat(source(v,p5,p6))
   for bit in range(4):
    row=0
    for k in range(len(mon)):
     if g>>k&1:row^=1<<(4*k+bit)
     if f>>k&1:
      for j in range(4):
       if fn(1<<j,(p5,p6)[ind])>>bit&1:row^=1<<(4*k+j)
    add(rows,row);allrows.append(row)
 
 if b>=1:
  groups={"X":[],"U0":[],"XU0":[],"U0U1":[]}
  for k,(i,j) in enumerate(mon):
   if i<base and j<base:key="X"
   elif base<=i<base+8 and base<=j<base+8:key="U0"
   elif i<base and base<=j<base+8:key="XU0"
   elif b>=2 and base<=i<base+8 and base+8<=j<base+16:key="U0U1"
   else:continue
   groups[key].extend(4*k+x for x in range(4))
  for key,inds in groups.items():
   if not inds:continue
   rr=[]
   for row in allrows:
    val=0
    for j,i in enumerate(inds):
     if row>>i&1:val|=1<<j
    rr.append(val)
 # Test necessary β(v,tv) in im(1+t)target for all v; enough basis and pairs.
 targetp=(c5,c6)[ind]
 IM=[(1<<i)^fn(1<<i,targetp) for i in range(4)]
 ann=[a for a in range(1,16) if all((a&x).bit_count()%2==0 for x in IM)]
 extra=[]
 for v in samples:
  tv=source(v,c5,c6); moncoef=feat(v)^feat(tv)^feat(v^tv)
  for lam in ann:
   row=0
   for k in range(len(mon)):
    if moncoef>>k&1:
     for j in range(4):
      if lam>>j&1:row^=1<<(4*k+j)
   extra.append(row)
 for key,inds in groups.items():
  if not inds:continue
  proj=lambda row:sum(((row>>i)&1)<<j for j,i in enumerate(inds))
  r0=rank(proj(row) for row in allrows);r1=rank(proj(row) for row in allrows+extra)
  expected={"X":(1,0),"U0":(2,1),"XU0":((1,1) if kind=="J" else (2,2)),"U0U1":(2,2)}
  assert (len(inds)-r0,len(inds)-r1)==expected[key]

 return locals()

def test(kind):
 d=component(kind);groups=d['groups'];rows=d['allrows'];extra=d['extra'];base=d['base'];mon=d['mon'];feat=d['feat'];nact=d['nact']
 def sols(inds,rr):
  piv={}
  for row in rr:add(piv,sum(((row>>i)&1)<<j for j,i in enumerate(inds)))
  out=[]
  for i in range(len(inds)):
   if i in piv:continue
   v=1<<i
   for j in sorted(piv):
    if (piv[j]&v).bit_count()&1:v|=1<<j
   out.append(sum(((v>>j)&1)<<i for j,i in enumerate(inds)))
  return out
 def q(c,v):
  z=0;f=feat(v)
  for i in range(len(mon)):
   if f>>i&1:z^=(c>>(4*i))&15
  return z
 def eps(v):return ((v&15)^(v>>4))*17
 forms=sols(groups['U0U1'],rows);assert len(forms)==2
 def pair(f,x,y):return q(f,(x<<base)|(y<<(base+8)))
 basis=[1<<i for i in range(8)]
 def sig(f,left=False,right=False,swap=False):
  return sum(pair(f,eps(y) if left else y,eps(x) if right else x)<<(4*(8*i+j)) if swap else pair(f,eps(x) if left else x,eps(y) if right else y)<<(4*(8*i+j)) for i,x in enumerate(basis) for j,y in enumerate(basis))
 uv=[sig(f) for f in forms];assert rank(uv)==2
 assert all(sig(f,swap=True)==sig(f) for f in forms)
 le=[sig(f,left=True) for f in forms];re=[sig(f,right=True) for f in forms]
 assert le==re and rank(le)==1 and rank(uv+le)==2
 zero_diag=[f for f in (forms[0],forms[1],forms[0]^forms[1]) if all(pair(f,v,v)==0 for v in range(256))]
 assert len(zero_diag)==1
 psi=zero_diag[0]
 assert all(pair(psi,eps(v),v)==((v&15)^(v>>4)) for v in range(256))
 top,=sols(groups['U0'],rows+extra)
 assert all(q(top,v<<base)==((v&15)^(v>>4)) for v in range(256))
 # Solve the F20 intertwiner equations to find D and soc(U).
 with contextlib.redirect_stdout(io.StringIO()):
  a=runpy.run_path(str(Path(__file__).with_name('verify_bruck_one_m_noncentral.py')))
 p,g=a['p'],a['qgen'];uact=a['uact'];mv=a['mv'];null=a['nullspace']
 equations=[]
 for gen in (p,g):
  odd=gen==g
  for j in range(4):
   v=nact(1<<j,gen[0])
   for bit in range(8):
    row=0
    for k in range(4):
     if v>>k&1:row^=1<<(8*k+bit)
    for k in range(8):
     w=uact(1<<k,gen[0]) if odd else nact((1<<k)&15,gen[0])|(nact((1<<k)>>4,gen[0])<<4)
     if w>>bit&1:row^=1<<(8*j+k)
    equations.append(row)
 hom=null(equations,32);assert len(hom)==2
 maps=[tuple((h>>(8*i))&255 for i in range(4)) for h in hom]
 S=tuple(eps(x) for x in next(B for B in maps if rank(eps(x) for x in B)==4))
 D=next(B for B in maps if rank(list(B)+list(S))==8)
 def res(f,A,B):return sum(pair(f,A[i],B[j])<<(4*(4*i+j)) for i in range(4) for j in range(4))
 dd=[res(f,D,D) for f in forms]; ds=[res(f,D,S) for f in forms];sd=[res(f,S,D) for f in forms];ss=[res(f,S,S) for f in forms]
 assert rank(dd)==2 and rank(ds)==rank(sd)==1 and rank(ss)==0
 assert rank(dd+ds+sd)==2 and rank(ds+sd)==1
 edd=[res(f,tuple(eps(x) for x in D),D) for f in forms]
 assert rank(edd)==1 and rank(edd+ds)==1
 cross=sols(groups['XU0'],rows);cv=[];ce=[]
 for f in cross:
  cv.append(sum(q(f,x|(y<<base))<<(4*(8*i+j)) for i,x in enumerate(1<<i for i in range(base)) for j,y in enumerate(basis)))
  ce.append(sum(q(f,x|(eps(y)<<base))<<(4*(8*i+j)) for i,x in enumerate(1<<i for i in range(base)) for j,y in enumerate(basis)))
 assert rank(ce)==(0 if kind=='J' else 1) and rank(cv+ce)==len(cross)
 # End_A(X) and the effect of the P6 all-ones endomorphism on the cross row.
 equations=[]
 for p6 in (d['c6'],d['d6']):
  def xact(v):return d['baseact'](v,p6)
  for i in range(base):
   for bit in range(base):
    row=0
    for j in range(base):
     if xact(1<<i)>>j&1:row^=1<<(base*j+bit)
     if xact(1<<j)>>bit&1:row^=1<<(base*i+j)
    equations.append(row)
 end=null(equations,base*base)
 assert len(end)==(1 if kind=='J' else 2)
 if kind=='P6':
  for ix,f in enumerate(cross):
   allones=sum(q(f,(63 if x.bit_count()&1 else 0)|(y<<base))<<(4*(8*i+j)) for i,x in enumerate(1<<i for i in range(base)) for j,y in enumerate(basis))
   assert allones==ce[ix]
 print(kind, 'quadratic components and complement restrictions verified')
for kind in ('J','P6'):test(kind)
