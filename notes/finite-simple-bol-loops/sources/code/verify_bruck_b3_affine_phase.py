#!/usr/bin/env python3
"""Scratch b3 affine-phase interpolation; committed repository imports only.

Run from repository root with Python 3.12 and assertions enabled.
Optional --probe runs the aligned base only. Full run takes several minutes.
This file bundles the exploratory linear-system code; independent review pending.
"""
import os,sys,io,contextlib
assert __debug__
from pathlib import Path
__WORKSPACE__=str(Path.cwd())
SOURCES={
    'planes': r'''
from pathlib import Path
import runpy,io,contextlib,itertools
path=Path(__WORKSPACE__)/'problems/0323-finite-simple-non-moufang-bol-loops/code'
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
''',
    'control': r'''
exec(SOURCES['planes'].split('planes=set()')[0])
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
# graph XS+soc3, pure soc2, top2+soc1, top3; fixed plane f,1
basis=[f,one]+[X[i]^U(Soc[i],2) for i in range(4)]+[U(Soc[i],1) for i in range(4)]+[U(Dc[i],1)^U(Soc[i],0) for i in range(4)]+[U(Dc[i],2) for i in range(4)]
assert rank(basis)==18
for g in a['F']:
 def vact(v):
  out=d['baseact'](v&63,g[1])
  for i in range(3):
   u=(v>>(base+8*i))&255
   # parity of permutation determines swapped U factors
   parity=sum(g[0][i]>g[0][j] for i in range(5) for j in range(i+1,5))%2
   val=a['uact'](u,g[0]) if parity else nact(u&15,g[0])|(nact(u>>4,g[0])<<4)
   out^=U(val,i)
  return out
 assert all(rank(basis+[vact(v)])==18 for v in basis)
def values(v):
 x=v&63;u=[(v>>(base+8*i))&255 for i in range(3)]
 return (qco(top,U(u[0],0)),qco(cross[1],x|U(u[0],0))^qco(cross[0],x|U(u[1],0)))
for v in basis+[x^y for x,y in itertools.combinations(basis,2)]:assert values(v)==(0,0)
# The S5-fixed all-ones vector has nonzero, rank-one polar row.
assert all((values(one^U(u,0))[1]^values(one)[1]^values(U(u,0))[1])==((u&15)^(u>>4)) for u in range(256))
assert all((values(one^U(u,1))[1]^values(one)[1]^values(U(u,1))[1])==0 for u in range(256))
# P6_S not contained: direct rank; pure soc intersection is exactly soc2.
assert any(rank(basis+[v])>18 for v in X)
socall=[U(Soc[i],j) for j in range(3) for i in range(4)]
assert 18+12-rank(basis+socall)==4
assert any(values(U(Dc[i],0))[0]!=0 for i in range(4))
assert any(values(f^U(Dc[i],1))[0]==0 and values(f^U(Dc[i],1))[1]!=0 for i in range(4))
print('F20-stable c=1 b=3 shadow control passed; no pure P6_S; rank=18')
''',
    'noncentral': r'''
exec(SOURCES['control'].split('for v in basis+')[0])
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
samples=basis+[x^y for x,y in itertools.combinations(basis,2)]
eq=[]
for v in samples:
 for bit in range(4):eq.append(sum(((termval(i,v)>>bit)&1)<<i for i in range(len(terms))))
# find one form with β(1,U) row e1 and C0_12=1. use affine solve via extra RHS variable.
def solve(required):
 rows=eq[:]
 for i,val in required.items():rows.append((1<<i)|((val&1)<<len(terms)))
 homogeneous=null(rows,len(terms)+1)
 good=next((x for x in homogeneous if x>>len(terms)&1),None)
 return None if good is None else good&((1<<len(terms))-1)
# identify β(1,U) from each term as binary top row (3 bits)
def r1(idx):
 v=0
 for j in range(3):
  u=U(Dc[0],j)
  if termval(idx,one^u)^termval(idx,one)^termval(idx,u):v|=1<<j
 return v
rowsR=[]
for j in range(3):rowsR.append(sum(((r1(i)>>j)&1)<<i for i in range(len(terms))))
psi12=next(i for i,t in enumerate(terms) if t[:3]==('PAIR',1,0))
# impose the linear rows, values 100 (e1) and noncentral C0_12=1.
reqrows=rowsR+[1<<psi12];rhs=[1,0,0,1]
mat=eq+[r|(v<<len(terms)) for r,v in zip(reqrows,rhs)]
sol=next((x for x in null(mat,len(terms)+1) if x>>len(terms)&1),None)
print('terms',len(terms),'equation rank',rank(eq),'noncentral allowed',bool(sol))
if sol:
 coef=sol&((1<<len(terms))-1);print('chosen form',[(terms[i][:3]) for i in range(len(terms)) if coef>>i&1])
 # find independent zero-d form with β(1)=0 (so total R1 rank1) and output pair
 d0indices=[i for i,(typ,ii,kk,_) in enumerate(terms) if typ=='X' or (typ=='U' and kk==1)]
 mat0=eq+rowsR+[1<<i for i in d0indices]
 cand=[x for x in null(mat0,len(terms)) if x and x!=coef]
 print('d0 candidates basis',len(cand))
 if cand:print('d0 form',[(terms[i][:3]) for i in range(len(terms)) if cand[0]>>i&1])
if sol:
 def evalform(v):
  out=0
  for i in range(len(terms)):
   if coef>>i&1:out^=termval(i,v)
  return out
 def tact(v):
  out=d['baseact'](v&63,d['c6'])
  for j in range(3):out^=U(a['uact']((v>>(base+8*j))&255,d['c5']),j)
  return out
 im=[(1<<i)^nact(1<<i,d['c5']) for i in range(4)]
 vectors=[1<<i for i in range(30)]; samples=vectors+[x^y for x,y in itertools.combinations(vectors,2)]
 img=[evalform(v)^evalform(tact(v))^evalform(v^tact(v)) for v in samples]
 print('marked d rank mod im',rank(im+img)-rank(im))
''',
    'data': r'''
exec(SOURCES['noncentral'].split('samples=basis+')[0])
def ix(tag):return next(i for i,t in enumerate(terms) if t[:3]==tag)
import os
c0=int(os.environ['B3_Q0']);c1=int(os.environ['B3_Q1'])
def q0(v):
 out=0
 for i in range(len(terms)):
  if c0>>i&1:out^=termval(i,v)
 return out
def q1(v):
 out=0
 for i in range(len(terms)):
  if c1>>i&1:out^=termval(i,v)
 return out
basis=[f,one]+[X[i]^U(Soc[i],2) for i in range(4)]+[U(Soc[i],1) for i in range(4)]+[U(Dc[i],j) for j in (1,2) for i in range(4)]
assert rank(basis)==18
''',
    'shapiro': r'''
"""Nonzero S5 extension by P6 via explicit Shapiro C5:C8 carry cocycle."""
import runpy,contextlib,io,itertools
with contextlib.redirect_stdout(io.StringIO()):a=runpy.run_path('problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_one_m_noncentral.py')
comp=a['comp'];inv=a['inv'];power=a['power'];G=a['queue'];F=a['F'];unit=a['I'];fixed=a['fixed'][0];p=a['p'];q=a['qgen'];
def mul(x,y):return (comp(x[0],y[0]),comp(x[1],y[1]))
def inverse(x):return (inv(x[0]),inv(x[1]))
Fdata={mul((power(p[0],i),power(p[1],i)),(power(q[0],j),power(q[1],j))):(i,j) for i in range(5) for j in range(4)}
assert len(Fdata)==20 and set(Fdata)==set(F)
rep={}
for g in G:rep.setdefault(g[1][fixed],g)
assert len(rep)==6 and rep[fixed]==unit

def schreier(g,x):
 y=g[1][x];z=mul(mul(inverse(rep[y]),g),rep[x]);return Fdata[z]

def e(g,h):
 bits=0
 for x in range(6):
  i,j=schreier(g,h[1][x]);k,l=schreier(h,x)
  if j+l>=4:bits|=1<<(g[1][h[1][x]])
 return bits

def act(g,v):return a['pact'](v,g[1])
def extmul(x,y):
 v,g=x;w,h=y;return (v^act(g,w)^e(g,h),mul(g,h))
def extinv(x):
 v,g=x;gi=inverse(g);return (act(gi,v^e(g,gi)),gi)
def word(c,d,terms):
 out=(0,unit)
 for i in terms:
  out=extmul(out,c if i==1 else d if i==2 else extinv(c if i==-1 else d))
 return out
C=((0,(a['c5'],a['c6'])));D=((0,(a['d5'],a['d6'])))
rels=[[1,1],[2,2,2,2],[1,2]*5,[-1,-2,1,2]*3]
for R in rels:
 v,g=word(C,D,R);assert g==unit;print('relator',len(R),'P6-shadow',v)
for g in G:
 for h in G:
  for k in (unit,C[1],D[1]):
   assert e(g,h)^e(mul(g,h),k)==act(g,e(h,k))^e(g,mul(h,k))
print('Shapiro cocycle passed 43200 generator cocycle checks; stabilizer F',len(F))
X=(0,q);xx=(0,unit)
for _ in range(4):xx=extmul(xx,X)
# C5 average kills the S-block and retains the induced fixed line.
v=xx[0];avg=0
for i in range(5):avg^=act((power(p[0],i),power(p[1],i)),v)
assert avg==63
print('F C4 fourth-power shadow',v,'C5 average',avg,'= constant')
''',
    'actions': r'''
"""Construct genuine S5 action on b3 P, and solve generator lift corrections."""
import runpy,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):d=load('data');sh=load('shapiro')
a=d['a'];nact=d['nact'];n=30;Es=[1<<i for i in range(n)];q1=d['q1'];q0=d['q0']
def qs(v):return q0(v)|(q1(v)<<4)
diag=[qs(x) for x in Es];pol=[[qs(Es[i]^Es[j])^diag[i]^diag[j] for j in range(n)]for i in range(n)]
def f(v,w):
 z=0
 while v:
  b=v&-v;v^=b;i=b.bit_length()-1
  if w>>i&1:z^=diag[i]
  u=w&~((1<<(i+1))-1)
  while u:
   b2=u&-u;u^=b2;z^=pol[i][b2.bit_length()-1]
 return z
def beta(v,w):return f(v,w)^f(w,v)
def actV(v,g):
 out=d['d']['baseact'](v&63,g[1]);p=g[0]
 for j in range(3):out|=a['uact']((v>>(6+8*j))&255,p)<<(6+8*j)
 return out
def actZ(z,g):return nact(z&15,g[0])|(nact(z>>4,g[0])<<4)
Gens=[sh['C'][1],sh['D'][1]];Inv=[sh['inverse'](g) for g in Gens]
# For each positive generator, construct the canonical quadratic lift, zero on basis.
P=[]
for g in Gens:
 tv=[actV(x,g) for x in Es]
 P.append([[f(tv[i],tv[j])^actZ(f(Es[i],Es[j]),g) for j in range(n)] for i in range(n)])
def ag(g,v):
 z=0
 while v:
  b=v&-v;v^=b;i=b.bit_length()-1;u=v
  while u:
   c=u&-u;u^=c;z^=P[g][i][c.bit_length()-1]
 return z
def step(i,v,z):
 g=abs(i)-1
 if i>0:return actV(v,Gens[g]),actZ(z,Gens[g])^ag(g,v)
 w=actV(v,Inv[g]);return w,actZ(z^ag(g,w),Inv[g])
# Masks encode linear dependence of z on the two 30×8 correction maps L_c,L_d.
NV=2*n*8

def symbolic(i,v,masks):
 g=abs(i)-1
 if i>0:
  w=actV(v,Gens[g]);out=[0]*8
  for bit in range(8):
   for j in range(8):
    if actZ(1<<j,Gens[g])>>bit&1:out[bit]^=masks[j]
   for k in range(n):
    if w>>k&1:out[bit]^=1<<(g*n*8+k*8+bit)
  return w,out
 w=actV(v,Inv[g]);raw=masks[:]
 for bit in range(8):
  for k in range(n):
   if v>>k&1:raw[bit]^=1<<(g*n*8+k*8+bit)
 out=[0]*8
 for bit in range(8):
  for j in range(8):
   if actZ(1<<j,Inv[g])>>bit&1:out[bit]^=raw[j]
 return w,out
rows=[]
for R in sh['rels']:
 relv,gg=sh['word'](sh['C'],sh['D'],R);assert gg==sh['unit']
 for x in Es:
  v=x;z=0;mask=[0]*8
  for gen in reversed(R):
   v,z=step(gen,v,z)
  assert v==x
  v=x
  for gen in reversed(R):v,mask=symbolic(gen,v,mask)
  assert v==x
  rhs=z^beta(relv,x)
  for bit in range(8):rows.append(mask[bit]|(((rhs>>bit)&1)<<NV))
piv={};bad=False
for row in rows:
 w=row
 while w&((1<<NV)-1):
  i=(w&((1<<NV)-1)).bit_length()-1
  if i in piv:w^=piv[i]
  else:piv[i]=w;break
 else:
  if w>>NV&1:bad=True;break
print('generator action system',NV,'variables',len(rows),'equations','rank',len(piv),'soluble',not bad)
if not bad:
 sol=0
 for i in sorted(piv):
  if ((piv[i]&sol).bit_count()&1)^((piv[i]>>NV)&1):sol|=1<<i
 assert all((((row&sol).bit_count()^(row>>NV))&1)==0 for row in rows)
 print('one correction as integer:',sol)
''',
    'crossed': r'''
import runpy,contextlib,io,collections,time,functools
with contextlib.redirect_stdout(io.StringIO()):
 t=load('actions')
assert not t['bad']; sh=t['sh']; d=t['d']; sol=t['sol']; f=t['f']; beta=t['beta']; G=sh['G']; unit=sh['unit']; mul=sh['mul']; e=sh['e']; actV=t['actV'];actZ=t['actZ'];gens=t['Gens']; inv=sh['inverse']; n=30
# Apply the two corrected generator automorphisms. Corrections are indexed by output v.
def step(i,v,z):
 w,z=t['step'](i,v,z)
 if i>0:
  for j in range(n):
   if w>>j&1:z^=(sol>>((i-1)*n*8+j*8))&255
 else:
  # undo L on the original input, before applying the inverse action on Z
  g=-i-1; raw=0
  for j in range(n):
   if v>>j&1:raw^=(sol>>(g*n*8+j*8))&255
  z^=actZ(raw,inv(gens[g]))
 return w,z
# Positive words only; section word has quotient kernel component shadow w_g.
words={unit:()}; queue=collections.deque([unit])
while queue:
 g=queue.popleft()
 for i,h in enumerate(gens):
  gh=mul(g,h)
  if gh not in words:words[gh]=words[g]+(i+1,);queue.append(gh)
assert len(words)==120
shadow={}
for g in G:
 v,h=sh['word'](sh['C'],sh['D'],words[g]);assert h==g;shadow[g]=v
# The word lift has shadow w; correcting on the left by w gives section action.
@functools.lru_cache(None)
def alpha(g,v,z):
 for i in reversed(words[g]):v,z=step(i,v,z)
 return v,z^beta(shadow[g],v)
# Verify the full crossed-action identity on every shadow basis vector.
for g in G:
 for h in G:
  for x in (1<<i for i in range(30)):
   v,z=alpha(h,x,0);v,z=alpha(g,v,z);w,y=alpha(mul(g,h),x,0)
   assert v==w and z^y==beta(e(g,h),w),(g,h,x)
# central symbolic bits hold 1920 variables and one constant bit.
NV=120*2*8;CONST=1<<NV; index={g:i for i,g in enumerate(G)}
def symfactor(g,k):return [1<<((index[g]*2+k)*8+j) for j in range(8)]
def applyz(g,z):
 out=[0]*8
 for j in range(8):
  a=actZ(1<<j,g)
  for k in range(8):
   if a>>k&1:out[k]^=z[j]
 return out
def xor(*vs):return [__import__('functools').reduce(int.__xor__,xs,0) for xs in zip(*vs)]
def const(v):return [CONST if v>>i&1 else 0 for i in range(8)]
# Factors as (V, symbolic Z); inverse (v,z+f(v,v)).
def pmul(a,b):return (a[0]^b[0],xor(a[1],b[1],const(f(a[0],b[0]))))
def pinv(a):return (a[0],xor(a[1],const(f(a[0],a[0]))))
def pa(g,a):
 v,z=alpha(g,a[0],0);return v,xor(applyz(g,a[1]),const(z))
zero=[0]*8; fac={}
for g in G:
 fac[g,unit]=(0,zero)
 for h in G:
  if h==unit:continue
  pr=unit
  for j,i in enumerate(words[h]):
   hk=mul(pr,gens[i-1]); gh=mul(g,pr)
   # equation alpha_g(f(pr,k)) f(g,pr*k)=f(g,pr) f(g*pr,k)
   z=pmul(pinv(pa(g,(e(pr,gens[i-1]),symfactor(pr,i-1)))),pmul(fac[g,pr],(e(gh,gens[i-1]),symfactor(gh,i-1))))
   assert z[0]==e(g,hk)
   if (g,hk) not in fac:fac[g,hk]=z
   pr=hk
# row reduction streaming; low-bit pivots and descending substitution.
piv={}; bad=0; count=0; mask=CONST-1; coeff_rows=[]

def add(row):
 coeff_rows.append(row & mask)
 global bad,count
 count+=1
 while row&mask:
  j=(row&-row).bit_length()-1
  if j in piv:row^=piv[j]
  else:piv[j]=row;return
 if row&CONST:bad+=1
for k in range(2):
 for row in symfactor(unit,k):add(row)
for gi,g in enumerate(G):
 for h in G:
  for kidx,k in enumerate(gens):
   l=pmul(pa(g,fac[h,k]),fac[g,mul(h,k)])
   r=pmul(fac[g,h],fac[mul(g,h),k]);assert l[0]==r[0]
   for row in xor(l[1],r[1]):add(row)
 if gi%20==0:print('processed',gi,'rank',len(piv),'inconsistent rows',bad,flush=True)
print('central associativity:',NV,'variables',count,'equations rank',len(piv),'inconsistent rows',bad,flush=True)
if bad:raise SystemExit(1)
ans=0
for j in sorted(piv,reverse=True):
 if ((piv[j]&ans).bit_count()&1)^bool(piv[j]&CONST):ans|=1<<j
assert all(((row&ans).bit_count()&1)==bool(row&CONST) for row in piv.values())
print('solution integer',ans,flush=True)
def evaluate(a):return a[0],sum(((r&ans).bit_count()&1 ^ bool(r&CONST))<<j for j,r in enumerate(a[1]))
F={(g,h):evaluate(v) for (g,h),v in fac.items()}
f=functools.lru_cache(None)(f)
mul=functools.lru_cache(None)(mul)
def mult(a,b):return (a[0]^b[0],a[1]^b[1]^f(a[0],b[0]))
# Associativity for all third arguments follows by induction from the
# verified crossed action and the generator-edge associator equations.
''',
    'stabilizer': r'''
import runpy,contextlib,io,functools
with contextlib.redirect_stdout(io.StringIO()):s=load('crossed')
G=s['G'];mul=s['mul'];unit=s['unit'];alpha=s['alpha'];F=s['F'];f=s['f'];beta=s['beta'];d=s['d']; basis=d['basis'];K=list(s['sh']['F']);assert len(K)==20 and len(basis)==18
# Pivots reduce modulo B and simultaneously recover B coordinates.
bp={}
for i,b in enumerate(basis):
 x=b;c=1<<i
 while x:
  j=(x&-x).bit_length()-1
  if j in bp:x^=bp[j][0];c^=bp[j][1]
  else:bp[j]=(x,c);break
 assert x
non=[i for i in range(30) if i not in bp];assert len(non)==12
def reduce(v):
 c=0
 for i in sorted(bp):
  if v>>i&1:v^=bp[i][0];c^=bp[i][1]
 return sum(((v>>j)&1)<<i for i,j in enumerate(non)),c
assert all(reduce(b)[0]==0 for b in basis)
def qact(g,v):return reduce(alpha(g,v,0)[0])[0]
# GF(2) linear equations; augmented RHS at bit n.
def solve(rows,n):
 piv={};mask=(1<<n)-1
 for row in rows:
  while row&mask:
   j=(row&-row).bit_length()-1
   if j in piv:row^=piv[j]
   else:piv[j]=row;break
  else:
   if row>>n&1:return None,len(piv)
 x=0
 for j in sorted(piv,reverse=True):
  if ((piv[j]&x).bit_count()&1)^((piv[j]>>n)&1):x|=1<<j
 assert all(((r&x).bit_count()&1)==((r>>n)&1) for r in rows)
 return x,len(piv)
ki={g:i for i,g in enumerate(K)}; n=20*30;rows=[]
for g in K:
 for h in K:
  gh=mul(g,h); assert gh in ki
  rhs=reduce(F[g,h][0])[0]
  imgs=[reduce(1<<i)[0] for i in range(30)];gimgs=[qact(g,1<<i) for i in range(30)]
  for b in range(12):
   row=((rhs>>b)&1)<<n
   for i in range(30):
    if imgs[i]>>b&1:row^=1<<(ki[g]*30+i);row^=1<<(ki[gh]*30+i)
    if gimgs[i]>>b&1:row^=1<<(ki[h]*30+i)
   rows.append(row)
for i in range(30):rows.append(1<<(ki[unit]*30+i))
x,rank=solve(rows,n);print('quotient cochain',n,len(rows),rank,'soluble',x is not None,flush=True)
if x is None:raise SystemExit(1)
xv={g:(x>>(30*ki[g]))&((1<<30)-1) for g in K}
coords={}
for g in K:
 for h in K:
  v=xv[g]^alpha(g,xv[h],0)[0]^F[g,h][0]^xv[mul(g,h)]
  rem,c=reduce(v);assert rem==0;coords[g,h]=c
# w0(c) is the ordered product of lifts (b_i,0) in P.
def w0(c):
 v=z=0
 for i,b in enumerate(basis):
  if c>>i&1:z^=f(v,b);v^=b
 return v,z
for i,b in enumerate(basis):
 assert f(b,b)==0
 for c in basis:assert beta(b,c)==0
# unknown ell_i in Z and section central z_g. Equality of subgroup W and F lifts.
n=18*8+20*8;ROWS=[]
def lv(c,bit):return sum(1<<(i*8+bit) for i in range(18) if c>>i&1)
def zvar(g,bit):return 1<<(18*8+8*ki[g]+bit)
def linact(g,vec,bit):
 return functools.reduce(int.__xor__,(vec[j] for j in range(8) if s['actZ'](1<<j,g)>>bit&1),0)
for g in K:
 for i,b in enumerate(basis):
  av,az=alpha(g,b,0);rem,c=reduce(av);assert rem==0
  _,wz=w0(c);rhs=az^beta(xv[g],av)^wz
  for bit in range(8):
   ROWS.append(linact(g,[lv(1<<i,j) for j in range(8)],bit)^lv(c,bit)^(((rhs>>bit)&1)<<n))
for g in K:
 for h in K:
  gh=mul(g,h); agv,agz=alpha(g,xv[h],0);ev,ez=F[g,h]; b,c0=w0(coords[g,h]); assert b^xv[gh]==xv[g]^agv^ev
  rhs=agz^ez^f(xv[g],agv)^f(xv[g]^agv,ev)^c0^f(b,xv[gh])
  for bit in range(8):
   row=zvar(g,bit)^linact(g,[zvar(h,j) for j in range(8)],bit)^zvar(gh,bit)^lv(coords[g,h],bit)^(((rhs>>bit)&1)<<n)
   ROWS.append(row)
for bit in range(8):ROWS.append(zvar(unit,bit))
y,rank=solve(ROWS,n);print('central stabilizer system',n,len(ROWS),rank,'soluble',y is not None,flush=True)
if y is None:raise SystemExit(1)
ell=[(y>>(8*i))&255 for i in range(18)];zv={g:(y>>(18*8+8*ki[g]))&255 for g in K}
def W(c):
 v,z=w0(c)
 for i in range(18):
  if c>>i&1:z^=ell[i]
 return v,z
# Independently verify the equations by actual group multiplication.
def pmul(a,b):return a[0]^b[0],a[1]^b[1]^f(a[0],b[0])
def emul(A,B):
 p,g=A;q,h=B
 return pmul(pmul(p,alpha(g,*q)),F[g,h]),mul(g,h)
Hsec={g:((xv[g],zv[g]),g) for g in K}
for g in K:
 for h in K:
  lhs=emul(Hsec[g],Hsec[h]);rhs=emul((W(coords[g,h]),unit),Hsec[mul(g,h)]);assert lhs==rhs
for g in K:
 for i,b in enumerate(basis):
  left=emul(Hsec[g],(W(1<<i),unit));av=alpha(g,b,0)[0];_,c=reduce(av)
  right=emul((W(c),unit),Hsec[g]);assert left==right
print('H verification: 400 products, 360 conjugation equations, W is elementary of dimension 18',flush=True)
print('ell',ell,'section V,Z',[(ki[g],xv[g],zv[g]) for g in K],flush=True)

# Full affine kernel, with one vector for every nonpivot coordinate.
def nullbasis(rows,n):
 piv={};mask=(1<<n)-1
 for row in rows:
  row &= mask
  while row:
   j=(row&-row).bit_length()-1
   if j in piv: row ^= piv[j]
   else: piv[j]=row;break
 out=[]
 for free in range(n):
  if free in piv:continue
  v=1<<free
  for j in sorted(piv,reverse=True):
   if (piv[j]&v).bit_count()&1:v |= 1<<j
  assert all(not ((r&v).bit_count()&1) for r in rows)
  out.append(v)
 return out
central_kernel=nullbasis(ROWS,n)
assert len(central_kernel)==16
def set_central(choice):
 global ell,zv,Hsec
 z=y
 for i,k in enumerate(central_kernel):
  if choice>>i&1:z^=k
 ell=[(z>>(8*i))&255 for i in range(18)]
 zv={g:(z>>(18*8+8*ki[g]))&255 for g in K}
 Hsec={g:((xv[g],zv[g]),g) for g in K}
 return ell,zv,Hsec
print('central homogeneous kernel dimension',len(central_kernel),flush=True)
''',
    'phase': r'''
import runpy,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):s=load('stabilizer')
a=s['s'];alpha=s['alpha'];F=s['F'];mul=s['mul'];unit=s['unit'];f=s['f'];inv=a['inv'];actV=a['actV'];actZ=a['actZ'];G=s['G'];K=s['K'];H=s['Hsec'];W=s['W'];reduce=s['reduce'];solve=s['solve'];t=a['gens'][0];n=30
def pmul(a,b):return (a[0]^b[0],a[1]^b[1]^f(a[0],b[0]))
def pinv(p):return p[0],p[1]^f(p[0],p[0])
def prod(a,b):
 p,g=a;q,h=b;return pmul(pmul(p,alpha(g,*q)),F[g,h]),mul(g,h)
def inverse(a):
 p,g=a;gi=inv(g);return pmul(pinv(F[gi,g]),alpha(gi,*pinv(p))),gi
def conj(a,b):return prod(prod(a,b),inverse(a))
def rs(vs):
 p={}
 for i,v in enumerate(vs):
  c=1<<i
  while v:
   j=(v&-v).bit_length()-1
   if j in p:v^=p[j][0];c^=p[j][1]
   else:p[j]=(v,c);break
 return p
def red(x,p):
 c=0
 for j in sorted(p):
  if x>>j&1:x^=p[j][0];c^=p[j][1]
 return x,c
id=((0,0),unit)
im=[(1<<i)^actV(1<<i,t) for i in range(n)];pv=rs(im);ker=[]
for i in range(n):
 rem,c=red(im[i],rs(im[:i]))
 if not rem:ker.append(c^(1<<i))
# e(t,t)=0 in this fixed quotient gauge, so involution shadows are im(1+t).
assert F[t,t][0]==0
zs=[z for z in range(256) if prod(((0,z),t),((0,z),t))==id]
if not zs:raise AssertionError('no transposition involution')
base=((0,zs[0]),t);disp=[]
for v in ker:
 out=conj(((v,0),unit),base);assert out[0][0]==0;disp.append(out[0][1]^zs[0])
for i in range(8):
 out=conj(((0,1<<i),unit),base);assert out[0][0]==0;disp.append(out[0][1]^zs[0])
pz=rs(disp)
def norm(x):
 rem,pre=red(x[0][0],pv);assert not rem
 out=conj(((pre,0),unit),x);return red(out[0][1]^zs[0],pz)[0]
classes={}
for z in zs:classes.setdefault(red(z^zs[0],pz)[0],z)
C=[g for g in G if mul(g,t)==mul(t,g)]
fixed=[key for key,z in classes.items() if all(norm(conj(((0,0),g),((0,z),t)))==key for g in C)]
if len(fixed)!=1:raise AssertionError(('non-unique origin',len(zs),len(pz),fixed))
lam=((0,classes[fixed[0]]),t)
support=lambda g:{i for i in range(5) if g[0][i]!=i}
for h in K:
 mu=conj(H[h],lam);u=mu[1]
 if support(t)&support(u):continue
 dd=mul(t,u)
 if dd not in H:continue
 basep=prod(prod(lam,mu),inverse(H[dd]));cols=[]
 for j in range(60):
  v=1<<(j%30);p=((v,0),unit)
  aa=conj(p,lam) if j<30 else lam;bb=mu if j<30 else conj(p,mu)
  cols.append(prod(prod(aa,bb),inverse(H[dd]))[0][0]^basep[0][0])
 fvec=s['d']['f'];rhs=basep[0][0]^fvec
 rows=[sum(((cols[i]>>j)&1)<<i for i in range(60))^(((rhs>>j)&1)<<60) for j in range(30)]
 x,rk=solve(rows,60)
 if x is None:continue
 p=((x&((1<<30)-1),0),unit);q=((x>>30,0),unit)
 pp=prod(prod(conj(p,lam),conj(q,mu)),inverse(H[dd]));rem,c=reduce(fvec);assert not rem
 z=pp[0][1]^W(c)[1]
 J=[(1<<i)^actZ(1<<i,t) for i in range(8)]+[(1<<i)^actZ(1<<i,u) for i in range(8)]
 rj=rs(J);phase=red(z,rj)[0]
 print('PHASE',phase,'origin',classes[fixed[0]],'hindex',K.index(h),'p',p[0][0],'q',q[0][0],'rank',rk,'Jrank',len(rj),flush=True);break
else:raise AssertionError('no fixed-shadow witness')
act=a['t']; amask=(1<<act['NV'])-1; cmask=a['CONST']-1;hmask=(1<<304)-1
rec={'assoc_exact_matrix':tuple(a['coeff_rows']),'action_matrix':tuple(row&amask for row in act['rows']), 'assoc_reduced_matrix':tuple(a['piv'][i]&cmask for i in sorted(a['piv'])),'H_matrix':tuple(row&hmask for row in s['ROWS']),'action_solution':hex(act['sol']),'assoc_solution':hex(a['ans']),'H_solution':hex(s['y']),'disp_space':[v for v in range(256) if red(v,pz)[0]==0],'origin':classes[fixed[0]],'fphase':phase,'hindex':K.index(h),'p_shadow':p[0][0],'q_shadow':q[0][0],'Hquotient':[(g,s['xv'][g]) for g in K]}
''',
}

def load(name):
 ns={'__name__':'__main__','__file__':'<embedded-'+name+'>','__WORKSPACE__':__WORKSPACE__,'SOURCES':SOURCES,'load':load}
 exec(compile(SOURCES[name],'<embedded-'+name+'>','exec'),ns)
 return ns
os.environ['B3_Q0']='260';os.environ['B3_Q1']='0'
with contextlib.redirect_stdout(io.StringIO()): model=load('data')
terms=model['terms']; termval=model['termval']; bas=model['basis']; null=model['null']; rank=model['rank']; one=model['one']; U=model['U']; Dc=model['Dc']
assert len(terms)==19 and len(bas)==18
def feature(v):
 return tuple(sum(((termval(i,v)>>bit)&1)<<i for i in range(19)) for bit in range(4))
from itertools import combinations
eq=[]
for v in bas+[x^y for x,y in combinations(bas,2)]:eq.extend(feature(v))
rowsR=[]
for j in range(3):
 u=U(Dc[0],j);rowsR.append(feature(one^u)[0]^feature(one)[0]^feature(u)[0])
zero=null(eq+rowsR,19); expected=[2,4,128,8192,16384,32768,65536]
assert len(zero)==7 and rank(zero+expected)==7
assert all(not ((r&256).bit_count()&1) for r in eq)
assert [int((r&256).bit_count()&1) for r in rowsR]==[1,0,0]
print('quadratic singularity basis: dimension 7',flush=True)
from functools import reduce
def val(co,v):return reduce(int.__xor__,(termval(i,v) for i in range(19) if co>>i&1),0)
def pol(co,v,w):return val(co,v)^val(co,w)^val(co,v^w)
d=model['d']; aa=model['a']; nact=model['nact']; base=model['base']
def tact(v):
 out=d['baseact'](v&63,d['c6'])
 for j in range(3):out^=U(aa['uact']((v>>(base+8*j))&255,d['c5']),j)
 return out
piv={}
for i in range(4):
 v=(1<<i)^nact(1<<i,d['c5'])
 while v:
  j=(v&-v).bit_length()-1
  if j in piv:v^=piv[j]
  else:piv[j]=v;break
def red(v):
 for j in sorted(piv):
  if v>>j&1:v^=piv[j]
 return v
bs=[1<<i for i in range(30)]; samples=bs+[x^y for x,y in combinations(bs,2)]
def dsig(co):return tuple(red(pol(co,v,tact(v))) for v in samples)
marked=dsig(4); assert rank(marked)==2
assert all(not any(dsig(x)) for x in [256,2,128,8192,16384,32768,65536])
print('fixed marked signature: one generator',flush=True)
import multiprocessing
free=[2,128,8192,16384,32768,65536]
def do_point(job):
 label,q0,q1=job
 os.environ['B3_Q0']=str(q0);os.environ['B3_Q1']=str(q1)
 with contextlib.redirect_stdout(io.StringIO()): ns=load('phase')
 return label,ns['rec']
for case in ('aligned','independent'):
 b0,b1=(260,0) if case=='aligned' else (256,4)
 points=[('base',b0,b1)]
 for j,x in enumerate(free):points += [(f'q0_{j}',b0^x,b1),(f'q1_{j}',b0,b1^x)]
 both=0
 for x in free:both^=x
 points.append(('all',b0^both,b1^both))
 if '--probe' in sys.argv:points=points[:1]
 result={}
 if '--probe' in sys.argv:
  stream=map(do_point,points); pool=None
 else:
  pool=multiprocessing.get_context('fork').Pool(4);stream=pool.imap(do_point,points)
 for label,rec in stream:
  if label!='base':
   assert rec['assoc_exact_matrix']==result['base']['assoc_exact_matrix'],(case,label,'assoc_exact_matrix')
   del rec['assoc_exact_matrix']
  result[label]=rec
  assert rec['origin']==0 and rec['fphase']==0
  assert (rec['hindex'],rec['p_shadow'],rec['q_shadow'])==(8,16,1)
  assert len(rec['disp_space'])==16
  print(case,label,'origin=0 phase=0',flush=True)
 if pool is not None:pool.close();pool.join()
 if '--probe' in sys.argv:break
 base=result['base']
 for label,cur in result.items():
  for key in ('action_matrix','assoc_reduced_matrix','H_matrix','disp_space','Hquotient'):
   assert cur[key]==base[key],(case,label,key)
 for key in ('action_solution','assoc_solution','H_solution'):
  x=int(base[key],16)
  for j in range(6):
   for i in (0,1):x^=int(result[f'q{i}_{j}'][key],16)^int(base[key],16)
  assert x==int(result['all'][key],16),(case,key)
 print(case,'exact matrices, displacement spaces and cochain XOR agree',flush=True)
