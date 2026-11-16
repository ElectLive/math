from pathlib import Path
import runpy,io,contextlib,itertools
path=Path('..')
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
planes=set()
for u,v in itertools.combinations(range(1,8),2):planes.add(tuple(sorted([u,v,u^v])))
for kind in ('J','P6'):
 d=z['component'](kind);base=d['base'];mon=d['mon'];feat=d['feat'];rr=d['allrows']+d['extra']
 def q(co,v):
  f=feat(v);out=0
  for i in range(len(mon)):
   if f>>i&1:out^=(co>>(4*i))&15
  return out
 cross=sols(d['groups']['XU0'],rr);top,=sols(d['groups']['U0'],rr)
 X=hom(None,lambda x,p:d['baseact'](x,p[1]),base);X=next(x for x in X if rank(x)==4)
 hs=hom(None,lambda x,p:a['uact'](x,p[0]) if p==gens[1] else nact(x&15,p[0])|(nact(x>>4,p[0])<<4),8)
 eps=lambda v:((v&15)^(v>>4))*17
 Soc=tuple(eps(x) for x in next(h for h in hs if rank(eps(x) for x in h)==4)); D=next(h for h in hs if rank(h+Soc)==8)
 def embed(i,s):
  return (mv(X,s) if i&1 else 0)^((mv(D,s) if i&2 else 0)<<(base))^((mv(Soc,s) if i&4 else 0)<<base)
 print('kind',kind,'cross dim',len(cross))
 for ell in (0,1):
  for c in range(1<<len(cross)):
   coeff=(top if ell else 0)
   for j,x in enumerate(cross):
    if c>>j&1:coeff^=x
   good=[]
   for plane in sorted(planes):
    u,v=plane[:2]
    if all(q(coeff,embed(u,s)^embed(v,t))==0 for s in range(16) for t in range(16)):good.append(plane)
   print('ell',ell,'cross',c,'good',good)

