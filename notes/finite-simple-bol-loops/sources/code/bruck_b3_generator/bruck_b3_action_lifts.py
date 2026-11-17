"""Construct genuine S5 action on b3 P, and solve generator lift corrections."""
import runpy,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path('bruck_two_n_c1_b3_noncentral.py');sh=runpy.run_path('bruck_b3_shapiro.py')
assert d['sol']; a=d['a'];nact=d['nact'];n=30;Es=[1<<i for i in range(n)];q1=d['evalform'];q0=lambda v:d['values'](v)[0]
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
   v,z=step(gen,v,z);v2,mask=symbolic(gen, v if False else 0, mask) if False else (v,mask)
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
