"""Check one explicit b=3 extension and stabilizer; The frozen mathematical input is in bruck_b3_witness.json.
Checks four involutions and a marked-orbit collision; does not verify corefreeness or construct a Bol envelope.
"""
import json,functools
from pathlib import Path
D=json.loads(Path(__file__).with_name("bruck_b3_witness.json").read_text()); M=D['mul'];I=D['unit'];di=D['diag'];pol=D['pol'];F=D['F'];AV=D['alphaV'];AZ=D['alphaZ'];Z=D['onZ']; B=D['B'];L=D['ell'];K=D['K'];H={int(k):tuple(v) for k,v in D['H'].items()}
@functools.lru_cache(None)
def f(v,w):
 out=0
 while v:
  b=v&-v;v^=b;i=b.bit_length()-1
  if w>>i&1:out^=di[i]
  u=w&~((1<<(i+1))-1)
  while u:
   c=u&-u;u^=c;out^=pol[i][c.bit_length()-1]
 return out
def p(a,b):return a[0]^b[0],a[1]^b[1]^f(a[0],b[0])
def zact(g,z):
 out=0
 for i in range(8):
  if z>>i&1:out^=Z[g][i]
 return out
@functools.lru_cache(None)
def a0(g,v):
 # Input (v,0) differs by central f-carry from ordered product of basis lifts.
 source=(0,0);target=(0,0)
 for i in range(30):
  if v>>i&1:
   source=p(source,(1<<i,0));target=p(target,(AV[g][i],AZ[g][i]))
 return target[0],target[1]^zact(g,source[1])
def a(g,v,z):
 v,w=a0(g,v);return v,w^zact(g,z)
def beta(v,w):return f(v,w)^f(w,v)
def emul(x,y):
 pv,g=x;qw,h=y
 return p(p(pv,a(g,*qw)),tuple(F[g][h])),M[g][h]
def rank(vs):
 piv={}
 for x in vs:
  while x:
   i=x.bit_length()-1
   if i in piv:x^=piv[i]
   else:piv[i]=x;break
 return len(piv)
perms=D['perms'];assert len({tuple(p[0]) for p in perms})==120
for p5,p6 in perms:assert sorted(p5)==list(range(5)) and sorted(p6)==list(range(6))
assert all(0<=j<120 for row in M for j in row)
for g in range(120):
 for h in range(120):
  for t in (0,1):assert perms[M[g][h]][t]==[perms[g][t][perms[h][t][i]] for i in range(len(perms[g][t]))]
 assert any(M[g][h]==I and M[h][g]==I for h in range(120))
 assert F[g][I]==[0,0] and F[I][g]==[0,0]
 assert rank(AV[g])==30 and rank(Z[g])==8
 assert all(0<=v<1<<30 for v in AV[g]) and all(0<=z<256 for z in AZ[g]+Z[g])
 for h in range(120):assert 0<=F[g][h][0]<1<<30 and 0<=F[g][h][1]<256
assert AV[I]==[1<<i for i in range(30)] and AZ[I]==[0]*30 and Z[I]==[1<<i for i in range(8)]
assert len(M)==120 and all(len(row)==120 for row in M)
assert all(M[I][g]==M[g][I]==g for g in range(120))
assert len({M[g][h] for g in range(120) for h in (I,)})==120
assert all(M[M[g][h]][k]==M[g][M[h][k]] for g in range(120) for h in range(120) for k in range(120))
for g in range(120):
 assert len({a(g,1<<i,0)[0] for i in range(30)})==30
 for i in range(30):
  v=1<<i;assert f(AV[g][i],AV[g][i])==zact(g,f(v,v))
  for j in range(i):assert beta(AV[g][i],AV[g][j])==zact(g,beta(v,1<<j))
for g in range(120):
 for h in range(120):
  v0,z0=F[g][h]
  for i in range(30):
   v,z=a(h,1<<i,0);v,z=a(g,v,z);w,t=a(M[g][h],1<<i,0);assert v==w and z^t==beta(v0,w)
  for i in range(8):assert zact(g,zact(h,1<<i))==zact(M[g][h],1<<i)
print('group table and 432000 crossed-action identities passed',flush=True)
for g in range(120):
 for h in range(120):
  for k in range(120):assert p(a(g,*F[h][k]),tuple(F[g][M[h][k]]))==p(tuple(F[g][h]),tuple(F[M[g][h]][k]))
print('1728000 associativity identities passed',flush=True)
def W(c):
 r=(0,0)
 for i,b in enumerate(B):
  if c>>i&1:r=p(r,(b,L[i]))
 return r
piv={}
for i,b in enumerate(B):
 x=b;c=1<<i
 while x:
  j=(x&-x).bit_length()-1
  if j in piv:x^=piv[j][0];c^=piv[j][1]
  else:piv[j]=(x,c);break
 assert x
for b in B:
 assert f(b,b)==0
 for c in B:assert beta(b,c)==0

def coord(x):
 c=0
 for j in sorted(piv):
  if x>>j&1:x^=piv[j][0];c^=piv[j][1]
 assert x==0
 return c
assert len(K)==20 and I in K and all(M[g][h] in H for g in K for h in K)
for g in K:
 for h in K:
  lhs=emul((H[g],g),(H[h],h));gh=M[g][h]; c=coord(lhs[0][0]^H[gh][0]);assert lhs==emul((W(c),I),(H[gh],gh))
 for i,b in enumerate(B):
  av=a(g,b,0)[0];c=coord(av);assert emul((H[g],g),(W(1<<i),I))==emul((W(c),I),(H[g],g))
print('W rank 18 elementary; H verified on 400 products and 360 conjugation equations')

# Nonzero quotient extension: the C5 average of q^4 survives all section changes.
pidx,qidx=D['p'],D['q']
def va(g,v):return a(g,v,0)[0]
def avg(v):
 out=0;w=I
 for _ in range(5):out^=va(w,v);w=M[w][pidx]
 assert w==I
 return out
v=0;g=I
for _ in range(4):v^=va(g,0)^F[g][qidx][0];g=M[g][qidx]
assert g==I and avg(v)==63
for i in range(30):
 v=1<<i;norm=0;g=I
 for _ in range(4):norm^=va(g,v);g=M[g][qidx]
 assert avg(norm)==0
print('nonsplit quotient: C5 average of q^4 is 63 and kills every section-change norm')
# τ(v,z;g)=(v,z+δ(v)) (u(g),0;g), with zero section cochain.
def top(v):return ((v>>6)&15)^((v>>10)&15)
for v0 in (0,4):
 for eps in (0,1):
  def delta(v):return beta(v0,v)^top(v)^(top(v)<<4 if eps else 0)
  def tau(x):
   (v,z),g=x;u=v0^va(g,v0)
   return (p((v,z^delta(v)),(u,0)),g)
  for g in range(120):
   assert tau(tau(((0,0),g)))==((0,0),g)
   for i in range(30):
    v=1<<i
    assert tau(emul(((0,0),g),((v,0),I)))==emul(tau(((0,0),g)),tau(((v,0),I)))
    assert tau(tau(((v,0),I)))==((v,0),I)
   for h in range(120):assert tau(emul(((0,0),g),((0,0),h)))==emul(tau(((0,0),g)),tau(((0,0),h)))
  for i in range(18):assert tau((W(1<<i),I))==(W(1<<i),I)
  for g in K:assert tau((H[g],g))==(H[g],g)
  print('τ automorphism, involution and pointwise H checks passed',v0,eps,flush=True)
# Identify the concrete module and radical properties used by this witness.
assert rank(di+[pol[i][j] for i in range(30) for j in range(i+1,30)])==8
assert rank([beta(63,1<<i) for i in range(30)])==4
for g in range(120):
 assert all(AV[g][i]==1<<perms[g][1][i] for i in range(6))
 for block in range(3):
  for i in range(8):assert AV[g][6+8*block+i]==AV[g][6+i]<<(8*block)
 for i in range(4):assert Z[g][i+4]==Z[g][i]<<4 and Z[g][i]<16
assert all(F[g][h][0]<64 for g in range(120) for h in range(120))
cyc={I};u=I
for _ in range(5):u=M[u][pidx];cyc.add(u)
assert u==I and len(cyc)==5
normalizer={g for g in range(120) if all(any(M[M[g][h]][x] in cyc for x in range(120) if M[g][x]==I and M[x][g]==I) for h in cyc)}
assert normalizer==set(K) and len(K)==20
print('Φ(P)=Z rank 8, noncentral fixed-vector polar rank 4, module blocks and F20 normalizer verified')
# The full lift of a transposition is classified modulo twisted P conjugacy.
def solve(rows,n):
 piv={};mask=(1<<n)-1
 for row in rows:
  while row&mask:
   j=(row&-row).bit_length()-1
   if j in piv:row^=piv[j]
   else:piv[j]=row;break
  else:
   if row>>n&1:return None,[]
 def lift(v,aff):
  for j in sorted(piv,reverse=True):
   if ((piv[j]&v).bit_count()&1)^(((piv[j]>>n)&1) if aff else 0):v^=1<<j
  return v
 return lift(0,True),[lift(1<<j,False) for j in range(n) if j not in piv]
def pivots(vectors):
 piv={}
 for i,v in enumerate(vectors):
  c=1<<i
  while v:
   j=(v&-v).bit_length()-1
   if j in piv:v^=piv[j][0];c^=piv[j][1]
   else:piv[j]=(v,c);break
 return piv
def reduce(x,piv):
 c=0
 for j in sorted(piv):
  if x>>j&1:x^=piv[j][0];c^=piv[j][1]
 return x,c
def pinv(x):return x[0],x[1]^f(x[0],x[0])
def einv(X):
 q,g=X;gi=next(h for h in range(120) if M[g][h]==I and M[h][g]==I)
 return p(pinv(tuple(F[gi][g])),a(gi,*pinv(q))),gi
Id=((0,0),I)
for g in range(120):
 for v in [0]+[1<<i for i in range(30)]:
  x=((v,0),g); xi=einv(x)
  assert emul(x,xi)==Id and emul(xi,x)==Id
print('3720 two-sided extension inverse checks passed')
t=1; t2=97
assert sum(i!=v for i,v in enumerate(perms[t][0]))==2
assert sum(i!=v for i,v in enumerate(perms[t2][0]))==2
assert M[t][t2]==M[t2][t] and M[t][t2] in K
for v0 in (0,4):
 for eps in (0,1):
  def delta(v):return beta(v0,v)^top(v)^(top(v)<<4 if eps else 0)
  def tau(X):
   (v,z),g=X;u=v0^a(g,v0,0)[0]
   return p((v,z^delta(v)),(u,0)),g
  def twisted(X,k):return emul(emul(tau(X),k),einv(X))
  im=[(1<<i)^a(t,1<<i,0)[0] for i in range(30)];iv=pivots(im);ker=[]
  for i in range(30):
   rem,c=reduce(im[i],pivots(im[:i]))
   if not rem:ker.append(c^(1<<i))
  fv=F[t][t][0]^v0^a(t,v0,0)[0]
  rows=[sum(((im[i]>>j)&1)<<i for i in range(30))^(((fv>>j)&1)<<30) for j in range(30)]
  base,solker=solve(rows,30);assert base==v0 and len(solker)==len(ker)==15
  assert all(reduce(x,iv)[0]==0 for x in solker)
  k0=((base,0),t);r=emul(k0,tau(k0));assert r[1]==I and r[0][0]==0
  rhs=r[0][1]
  rows=[sum(((((1<<i)^Z[t][i])>>j)&1)<<i for i in range(8))^(((rhs>>j)&1)<<8) for j in range(8)]
  zbase,zker=solve(rows,8);assert zbase==0 and len(zker)==6
  ref=((base,zbase),t);assert emul(ref,tau(ref))==Id
  disp=[]
  for x in ker:
   out=twisted(((x,0),I),ref);assert out[0][0]==base and out[1]==t;disp.append(out[0][1]^zbase)
  for i in range(8):
   out=twisted(((0,1<<i),I),ref);assert out[0][0]==base;disp.append(out[0][1]^zbase)
  cp=pivots(disp);assert len(cp)==4
  def cls(z):return reduce(z,cp)[0]
  classes={}
  for m in range(1<<len(zker)):
   z=zbase
   for i,b in enumerate(zker):
    if m>>i&1:z^=b
   classes.setdefault(cls(z^zbase),z)
  assert sorted(classes)==[0,6,10,12]
  def norm(k):
   assert k[1]==t
   rem,pre=reduce(k[0][0]^base,iv);assert rem==0
   out=twisted(((pre,0),I),k);assert out[0][0]==base
   return cls(out[0][1]^zbase)
  centralizer=[g for g in range(120) if M[g][t]==M[t][g]];assert len(centralizer)==12
  survivors=[]
  for key,z in classes.items():
   k=((base,z),t);assert emul(k,tau(k))==Id and norm(k)==key
   if all(norm(twisted(((0,0),g),k))==key for g in centralizer):survivors.append(key)
  assert survivors==[0]
  # Propagate the unique selected orbit by an explicit H element.
  hg=emul((W(16),I),(H[58],58)); k1=ref;k2=emul(emul(hg,k1),einv(hg))
  assert k2==(((7^v0),0),t2) and emul(k2,tau(k2))==Id
  # In τG the product of conjugated marks is k1'^{-1}k2'.
  k1prime=twisted(((5,0),I),k1);h=(H[M[t][t2]],M[t][t2])
  assert emul(emul(einv(k1prime),k2),einv(h))==(W(1),I)
  print('τ',v0,eps,'four twisted P-orbits; unique invariant orbit; H collision verified')
# Check all 16 central stabilizer directions and collision stability modulo J.
# Linearity in these central coordinates makes basis checks cover their span.
deltas=D['Hdelta'];assert len(deltas)==16
assert rank([sum(v<<(8*i) for i,v in enumerate(dl+dz)) for dl,dz in deltas])==16
jvec=[(1<<i)^Z[t][i] for i in range(8)]+[zact(t,(1<<i)^Z[t2][i]) for i in range(8)]
jp=pivots(jvec);assert len(jp)==4
for v0 in (0,4):
 for eps in (0,1):
  def delta(v):return beta(v0,v)^top(v)^(top(v)<<4 if eps else 0)
  def tau(X):
   (v,z),g=X;return p((v,z^delta(v)),(v0^a(g,v0,0)[0],0)),g
  def twisted(X,k):return emul(emul(tau(X),k),einv(X))
  for dl,dz in deltas:
   LH=[x^y for x,y in zip(L,dl)];HH={g:(H[g][0],H[g][1]^dz[i]) for i,g in enumerate(K)}
   def WH(c):
    r=(0,0)
    for i,b in enumerate(B):
     if c>>i&1:r=p(r,(b,LH[i]))
    return r
   for g in K:
    assert tau((HH[g],g))==(HH[g],g)
    for h in K:
     lhs=emul((HH[g],g),(HH[h],h));gh=M[g][h];cc=coord(lhs[0][0]^HH[gh][0]);assert lhs==emul((WH(cc),I),(HH[gh],gh))
    for i,b in enumerate(B):
     cc=coord(a(g,b,0)[0]);assert emul((HH[g],g),(WH(1<<i),I))==emul((WH(cc),I),(HH[g],g))
   for i in range(18):assert tau((WH(1<<i),I))==(WH(1<<i),I)
   hg=emul((WH(16),I),(HH[58],58));k1=((v0,0),t);k2=emul(emul(hg,k1),einv(hg))
   assert emul(k2,tau(k2))==Id
   h=(HH[M[t][t2]],M[t][t2]);r=emul(emul(einv(twisted(((5,0),I),k1)),k2),einv(h))
   assert r[1]==I and r[0][0]==WH(1)[0] and reduce(r[0][1]^WH(1)[1],jp)[0]==0
print('16 independent central stabilizer directions preserve H, τ, and collision modulo J')
