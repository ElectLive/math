#!/usr/bin/env python3
"""All-shadow finite checks for the fixed b3 model; Python 3.12; assertions required."""
import runpy,io,contextlib,functools,itertools,random,sys
from pathlib import Path
assert __debug__
# Default to the adjacent reviewed actual-group verifier; optionally use an explicit path.
P=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('verify_bruck_b3_noncentral.py')
with contextlib.redirect_stdout(io.StringIO()):s=runpy.run_path(str(P))
G=list(range(120));M=s['M'];mul=lambda g,h:M[g][h];unit=s['I'];alpha=s['a'];F={(g,h):tuple(s['F'][g][h]) for g in G for h in G};f=s['f'];beta=s['beta'];K=s['K'];actZ=s['zact'];rank=s['rank']
lines=[(17,18,24,48),(1088,2176,4352,8704),(278528,557056,1114112,2228224),(71303168,142606336,285212672,570425344),(3047424,3375104,901120,3489792),(780140544,864026624,230686720,893386752)]
fixed=[4,63]
def encode(v,j):
 z=0
 for i in range(6):
  if v>>i&1:z^=lines[i][j]
 return z
def q(v):return f(v,v)
def tops(v):return [((v>>(6+8*i))&15)^((v>>(10+8*i))&15) for i in range(3)]
# The first quadratic coordinate is exactly the linear top1 map.
for i in range(30):
 assert (q(1<<i)&15)==tops(1<<i)[0]
 for j in range(i):assert (beta(1<<i,1<<j)&15)==0
# In the frozen formula τ(s_g)=(u(g),0)s_g; u vanishes on F.
for g in K:
 for v0 in (0,4):assert (v0^alpha(g,v0,0)[0])==0

def row(v,m):
 ts=tops(v);return (ts[0] if m&1 else 0)^(ts[1] if m&2 else 0)^(ts[2] if m&4 else 0)
def null(rows,n):
 piv={}
 for x in rows:
  while x:
   j=x.bit_length()-1
   if j in piv:x^=piv[j]
   else:piv[j]=x;break
 out=[]
 for j in range(n):
  if j in piv:continue
  x=1<<j
  for i in sorted(piv):
   if (piv[i]&x).bit_count()&1:x^=1<<i
  assert all(not ((r&x).bit_count()&1) for r in rows)
  out.append(x)
 return out
# Verify displayed six S-lines synchronize under F action and span ker(top1).
for g in K:
 for j in range(4):
  target=alpha(g,lines[0][j],0)[0]
  coeff=next(m for m in range(16) if functools.reduce(int.__xor__,(lines[0][i] for i in range(4) if m>>i&1),0)==target)
  for line in lines:
   expected=functools.reduce(int.__xor__,(line[i] for i in range(4) if coeff>>i&1),0)
   assert alpha(g,line[j],0)[0]==expected
   assert tops(line[j])[0]==0
assert rank([v for line in lines for v in line])==24
planes={tuple(sorted((x,y,x^y))) for x,y in itertools.combinations(range(1,64),2)};assert len(planes)==651
sing=[]
for p in planes:
 bs=null([p[0],p[1]],6);vv=[encode(v,j) for v in bs for j in range(4)]
 if all(q(v)==0 for v in vv) and all(beta(vv[i],vv[j])==0 for i in range(16) for j in range(i)):sing.append((p,bs))
assert len(sing)==61
candidates=[]
for p,bs in sing:
 vv=[encode(v,j) for v in bs for j in range(4)]+fixed
 if all(q(v)==0 for v in vv) and all(beta(vv[i],vv[j])==0 for i in range(18) for j in range(i)):candidates.append((p,bs,vv))
assert len(candidates)==31
# The two possible augmentation-one fixed lines have the same 31 planes.
for fixedline in ([4],[4^63]):
 other=[]
 for p,bs in sing:
  vv=[encode(v,j) for v in bs for j in range(4)]+fixedline
  if all(q(v)==0 for v in vv) and all(beta(vv[i],vv[j])==0 for i in range(len(vv)) for j in range(i)):other.append(p)
 assert set(other)=={p for p,_,_ in candidates}

rng=random.Random(4212);samples=[1<<i for i in range(30)]+[rng.getrandbits(30) for _ in range(30)]
surv=[]
for p,bs,B in candidates:
 allowed=[m for m in range(8) if all(row(v,m)==0 for v in B)]
 pairs={(x,y,z) for x in allowed for y in allowed for z in (0,1)}
 for v in samples:
  vals=[beta(v,b) for b in B];r=rank(vals)
  pairs={(x,y,z) for x,y,z in pairs if rank(vals+[q(v)^row(v,x)^(row(v,y)<<4)^(beta(v,4) if z else 0)])==r}
  if not pairs:break
 if pairs:surv.append((p,bs,B,pairs))
assert len(surv)==27
assert all(pairs=={(1,0,0),(1,0,1),(1,1,0),(1,1,1)} for _,_,_,pairs in surv)
print('651 shadows; 61 singular; 31 fixed-plane; 27 survive witnesses')
def test_lift(basis):
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
  return functools.reduce(int.__xor__,(vec[j] for j in range(8) if actZ(g,1<<j)>>bit&1),0)
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
 return locals()

for p,bs,oldbasis,pairs in surv:
 basis=fixed+oldbasis[:16]
 with contextlib.redirect_stdout(io.StringIO()):ns=test_lift(basis)
 assert len(ns['central_kernel'])==16 and ns['rank']==288
 assert ns['xv'][83]==0
 J=[(1<<i)^actZ(1,1<<i) for i in range(8)]+[(1<<i)^actZ(97,1<<i) for i in range(8)]
 shift=18*8+8*ns['ki'][83]
 phase=lambda x:(x&255)^((x>>shift)&255)
 
 if rank(J+[phase(ns['y'])]+[phase(v) for v in ns['central_kernel']])!=rank(J):print('BAD',p,rank(J),rank(J+[phase(ns['y'])]+[phase(v) for v in ns['central_kernel']]),phase(ns['y']), 'basis',basis,'xv83',ns['xv'][83]);raise AssertionError
 for v0 in (0,4):
  for eps in (0,1):
   def delta(x):
    a=tops(x)[0];return beta(v0,x)^a^((a<<4) if eps else 0)
   assert all(delta(v)==0 for v in basis)
   assert all(delta(ns['xv'][g])==0 for g in K)
print('all 27 actual stabilizer lift systems and collision phases pass')
