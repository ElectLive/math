import runpy,contextlib,io,functools
with contextlib.redirect_stdout(io.StringIO()):s=runpy.run_path('bruck_crossed_system_fast.py')
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

