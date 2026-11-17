#!/usr/bin/env python3
"""Quotient-only C5 normalizer control for the fixed b=3 phase section.

Run from any directory using Python 3.12 with assertions enabled. The embedded
fixed quotient construction is read from the exact phase-verifier bytes at
22db023526be99e25f93bd9f5643104c153b29f0; its committed component imports
must be present. This checks G/Z and the F20 section only; it does not construct
H, check marked phases, or treat nonidentity inversion automorphisms.
"""
import ast,contextlib,hashlib,io,os
from pathlib import Path
assert __debug__
code_dir=Path(__file__).resolve().parent
root=code_dir.parents[2]
os.chdir(root)
p=code_dir/'verify_bruck_b3_affine_phase.py'
raw=p.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='694b31e0463eab0f7e66501a18063a326dd71cc008e5fa70020620b7284f6298', 'phase source is not the pinned 22db version'
for name,expected in {
 'verify_bruck_n_quadratic_support.py':'68f3d80229609d2217608c69cc203fc49176a6509f3fb5c476c3805bbe0e675d',
 'verify_bruck_one_m_noncentral.py':'59c0ed355bffdf316d93c37f99f2094acc4a09b2eff3db13459f9d208782e15a',
 'verify_bruck_p6_frattini.py':'9e42fe025aaa9dce6690badef3145da2f9a2dffb56670136fe63435b02358705',
}.items():
 assert hashlib.sha256((code_dir/name).read_bytes()).hexdigest()==expected, (name,'does not match pinned source')
tree=ast.parse(raw);src=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='SOURCES' for x in n.targets))
os.environ['B3_Q0']='260';os.environ['B3_Q1']='0'
def load(name):
 d={'__name__':'__main__','__file__':'<embedded>','load':load,'SOURCES':src,'__WORKSPACE__':os.getcwd()}
 with contextlib.redirect_stdout(io.StringIO()):exec(src[name],d)
 return d
sh=load('shapiro');d=load('data');a=d['a']; basis=d['basis'];mul=sh['mul']; unit=sh['unit'];K=list(sh['F']); ki={g:i for i,g in enumerate(K)};e=sh['e'];
def act(v,g):
 out=d['d']['baseact'](v&63,g[1]); p=g[0]
 for j in range(3): out|=a['uact']((v>>(6+8*j))&255,p)<<(6+8*j)
 return out

bp={}
for i,b in enumerate(basis):
 x=b;c=1<<i
 while x:
  j=(x&-x).bit_length()-1
  if j in bp:x^=bp[j][0];c^=bp[j][1]
  else:bp[j]=(x,c);break
non=[i for i in range(30) if i not in bp]
def reduce(v):
 c=0
 for i in sorted(bp):
  if v>>i&1:v^=bp[i][0];c^=bp[i][1]
 return sum(((v>>j)&1)<<i for i,j in enumerate(non)),c
def solve(rows,n):
 piv={};mask=(1<<n)-1
 for row in rows:
  while row&mask:
   j=(row&-row).bit_length()-1
   if j in piv:row^=piv[j]
   else:piv[j]=row;break
  else:
   if row>>n&1:raise ValueError('inconsistent')
 x=0
 for j in sorted(piv,reverse=True):
  if ((piv[j]&x).bit_count()&1)^((piv[j]>>n)&1):x|=1<<j
 return x
n=600;rows=[];imgs=[reduce(1<<i)[0] for i in range(30)]
for g in K:
 gimgs=[reduce(act(1<<i,g))[0] for i in range(30)]
 for h in K:
  gh=mul(g,h);rhs=reduce(e(g,h))[0]
  for b in range(12):
   row=((rhs>>b)&1)<<n
   for i in range(30):
    if imgs[i]>>b&1:row^=1<<(ki[g]*30+i);row^=1<<(ki[gh]*30+i)
    if gimgs[i]>>b&1:row^=1<<(ki[h]*30+i)
   rows.append(row)
for i in range(30):rows.append(1<<(ki[unit]*30+i))
x=solve(rows,n);xv={g:(x>>(30*ki[g]))&((1<<30)-1) for g in K}
def qm(x,y):return x[0]^act(y[0],x[1])^e(x[1],y[1]),mul(x[1],y[1])
def qi(x):
 g=sh['inverse'](x[1]);return act(x[0]^e(x[1],g),g),g
def qp(x,n):
 y=(0,unit)
 for _ in range(n):y=qm(y,x)
 return y
def conj(x,y):return qm(qm(x,y),qi(x))
p=sh['p'];r=qp((xv[p],p),6)
powers=[qp(r,i) for i in range(5)]
assert len(set(powers))==5 and qp(r,5)==(0,unit)
assert r[0]==16
trans=sh['C'][1]; h=K[8]
u=mul(mul(h,trans),sh['inverse'](h));tu=mul(trans,u)
assert ki[tu]==12
for label,g in [('h',h),('tu',tu)]:
 x=(xv[g],g)
 assert xv[g]==0
 assert conj(x,r) in powers, (label,'does not normalize C5')
 print(label,'quotient section index',ki[g],'normalizes C5; shadow',xv[g])
print('common C5 has order 5; generator shadow',r[0])
