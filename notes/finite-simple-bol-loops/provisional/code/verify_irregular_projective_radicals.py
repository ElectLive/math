#!/usr/bin/env python3
"""Actual ring units, affine group words and unique native left-section factorizations.
Use NumPy and the earlier exact F3 echelon and augmentation helpers. Only 20 physical
sites (never a generic T-torus) are used, including the quotient by constants at top.
"""
import sys,json,hashlib,base64,zlib,random
from pathlib import Path
from itertools import product
from verify_class_two_psl2_19_cubic_multiplicity import np,I,ref,col,null,rank,pw,fix,modules,pmat,HASH
rng=np.random.default_rng(4313907)
def eq(a,b):return np.array_equal(a%3,b%3)
def z(n):return np.zeros(n,dtype=np.int32)
def invperm(p):return np.argsort(p)
class Ring:
 def __init__(self,n):
  self.n=n;self.N=1<<n;self.top=self.N-1;self.inds=list(range(1,self.N));self.one=[s for s in self.inds if s.bit_count()==1]
  self.zero=np.zeros((self.N,20),np.int32)
  self.UU=[[i,j,(i|j)] for i in self.inds for j in self.inds if not i&j]
 def proj(self,a):return (a-2*int(a.sum()))%3
 def rand(self,unit=False):
  a=rng.integers(0,3,(self.N,20),dtype=np.int32);a[0]=0
  for i in (self.inds if unit else self.one+[self.top]):a[i]=self.proj(a[i]);
  return a
 def mult(self,a,b):
  c=self.zero.copy()
  for i,j,k in self.UU:c[k]+=a[i]*b[j]
  c[self.top]=self.proj(c[self.top]);return c%3
 def um(self,a,b):return (a+b+self.mult(a,b))%3
 def poly(self,x):
  a=self.zero.copy()
  for i in self.inds:
   k=x[i]
   if not k.any():continue
   for s in self.inds:
    if not i&s:a[s|i]+=a[s]*k
   a[i]+=k;a[self.top]=self.proj(a[self.top]);a%=3
  return a
 def fac(self,a):
  acc=self.zero.copy();out=acc.copy()
  for i in self.inds:
   k=(a[i]-acc[i])%3;out[i]=k
   if not k.any():continue
   for s in self.inds:
    if not i&s:acc[s|i]+=acc[s]*k
   acc[i]+=k;acc[self.top]=self.proj(acc[self.top]);acc%=3
  assert eq(acc,a);return out
 def act(self,x,y):return (y+self.mult(self.poly(x),y))%3
 def g(self,k,h):
  x,y=k;a,b=h;return ((x+a)%3,(y+self.act(x,b))%3)
 def inv(self,k):x,y=k;return ((-x)%3,self.act((-x)%3,-y))
 def randg(self):return (self.rand(True),self.rand(False))
 def sign(self,k,p,zz=0):x,y=k;return (x[:,p],(-1)**zz*y[:,p]%3)
 def graph(self,x):return (x,self.poly(x))
 def geq(self,k,h):return eq(k[0],h[0]) and eq(k[1],h[1])

def base(D):
 X={g:pmat(D['X'+g]) for g in 'urw'};Y={g:pmat(D['Y'+g]) for g in X};f=pmat(D['f']);d=pmat(D['d'])[:,0];M=modules()
 F=(f+Y['w']@f@X['w'])%3;D3=(I(119)+Y['r']+pw(Y['r'],2))@d%3
 sep=null(np.column_stack((F,pw(Y['r'],3)-I(119))).T).T@(I(119)-Y['w'])%3
 phi=next(v for v in sep if (v@(I(119)-Y['w'])@D3)%3);phi=phi*int((phi@(I(119)-Y['w'])@D3)%3)%3
 B=fix(Y,'r');us=[pw(Y['u'],j) for j in range(19)];cons=(I(19)-M['w']).T@np.vstack([phi@u for u in us])@B%3
 good=B@null(cons)%3;bad=col(np.column_stack((f@(X['w']-I(117))@fix(X,'ur')%3,(Y['w']-I(119))@fix(Y,'ur')%3)))
 be=next(v for v in good.T if rank(np.column_stack((bad,v)))>bad.shape[1]);A=np.column_stack([u@be%3 for u in us]);assert all(eq(Y[g]@A,A@M[g]) for g in 'ur')
 assert not np.any(phi@(A+Y['w']@A@M['w'])%3);C=np.column_stack((F,(A+Y['w']@A@M['w'])%3,pw(Y['r'],3)-I(119)));assert rank(np.column_stack((C,(I(119)-Y['w'])@D3%3)))==rank(C)+1
 print('actual single passive top shear, constrained/harmful-B-map space dimensions',good.shape[1],bad.shape[1],'r3 physical residue rank',rank(C),rank(C)+1)
 return X,Y,f,d,A
class Group:
 def __init__(self,R,base):
  self.R=R;X,Y,self.f,self.d,self.A=base
  r=np.array([4*i%19 for i in range(19)]+[19]);w=np.array([19]+[-pow(i,-1,19)%19 for i in range(1,19)]+[0]);rr=np.arange(20);self.mx={};self.my={};self.pi={};self.invo=[];self.ds=[z(119)]
  for j in range(9):
   for w1 in (0,1):
    key=(j,w1);self.mx[key]=pw(X['r'],j)@(X['w'] if w1 else I(117))%3;self.my[key]=pw(Y['r'],j)@(Y['w'] if w1 else I(119))%3;self.pi[key]=invperm(rr[w] if w1 else rr)
   self.ds.append((self.ds[-1]+self.my[j,0]@self.d)%3);rr=r[rr]
  assert np.array_equal(rr,np.arange(20)) and not self.ds[-1].any()
  # Store the injective linear solve in the true base torus sheet, not an inverse on arbitrary RHSs.
  self.sol={};
  for i in [(0,0)]+[(j,1) for j in range(9)]:
   Q=col(I(117)-self.mx[i]);S=(I(119)-self.my[i])@self.my[i]@self.f@Q%3
   piv=ref(S.T)[1];assert len(piv)==Q.shape[1];A0=S[piv,:];U=ref(np.column_stack((A0,I(len(piv)))))[0][:,len(piv):];self.sol[i]=(I(119)-self.my[i],Q@U%3,piv)
 def mk(self,x,y,a,b,g):return (x%3,y%3,a%3,b%3,g)
 def gg(self,g,h):return ((g[0]+(-1)**g[1]*h[0])%9,g[1]^h[1])
 def prod(self,k,h):
  x,y,a,b,g=k;u,v,c,d,j=h;p=self.pi[g];return self.mk(x+self.mx[g]@u,y+self.my[g]@v,a+c[:,p],b+self.R.act(a,d[:,p]),self.gg(g,j))
 def same(self,k,h):return k[-1]==h[-1] and all(eq(a,b) for a,b in zip(k[:-1],h[:-1]))
 def H(self,x,a,j):
  return self.mk(x,self.f@x+self.A@a[-1,:19]+self.ds[j],a,self.R.poly(a),(j,0))
 def mark(self,j0):
  i=(j0,1) if j0!=9 else (0,0);p=self.pi[i];x=rng.integers(0,3,117,dtype=np.int32);x=(x-self.mx[i]@x)%3;y=rng.integers(0,3,119,dtype=np.int32);y=(y+self.my[i]@y)%3
  a=self.R.rand(True);a=(a-a[:,p])%3;b=self.R.rand();b=(b+b[:,p])%3
  return self.mk(x,y,a,self.R.act(2*a%3,b),i)
 def factor(self,g):
  R=self.R;x,y,a,b,t=g;v=(b-R.poly(a))%3;vf=R.fac(v);hits=[]
  for j in (range(9) if t[1] else (-1,)):
   i=(j,1) if j>=0 else (0,0);p=self.pi[i];k=self.gg(i,t);assert not k[1]
   ac=(vf-vf[:,p])%3;assert all(int(q.sum())%3==0 for q in ac);ha=(a-ac)[:,p]%3
   bb=R.act(ac,(v+R.poly(ac))%3);assert eq(bb[:,p],bb)
   c=(y-self.my[i]@(self.f@(self.mx[i]@x%3)+self.A@ha[-1,:19]+self.ds[k[0]]))%3
   E,B,rows=self.sol[i];rhs=E@c%3;xx=B@rhs[rows]%3;yy=(c-self.my[i]@self.f@xx)%3
   if not eq(yy,self.my[i]@yy):continue
   assert eq(self.mx[i]@xx,-xx);hx=self.mx[i]@(x-xx)%3
   out=self.mk(xx,yy,ac,R.act(2*ac%3,bb),i);hh=self.H(hx,ha,k[0]);assert self.same(self.prod(out,hh),g);hits.append(out)
  assert len(hits)==1;return hits[0]
 def op(self,k,h):return self.factor(self.prod(k,h))

class Projective(Group):
 # All 3,420 real group elements, canonical decomposition through i_{q0} and the genuine Borel.
 def __init__(self,R,B):
  super().__init__(R,B);self.store=B; X,Y=B[:2]
  Id=tuple(range(20));uu=tuple([(x+1)%19 for x in range(19)]+[19]);rw=tuple([4*x%19 for x in range(19)]+[19]);W=tuple([19]+[-pow(x,-1,19)%19 for x in range(1,19)]+[0]);c=self.pc
  self.Id=Id;self.mx2={Id:I(117)};self.my2={Id:I(119)};self.pi2={Id:np.arange(20)};self.bor={};self.folds={};self.S2={};self.cand={19:[Id]}
  U=[Id];V=[Id]
  for j in range(18):U.append(c(uu,U[-1]))
  for j in range(8):V.append(c(rw,V[-1]))
  for a in range(19):
   self.cand[a]=[]
   for j in range(9):
    b=c(U[a],V[j]);self.bor[b]=(a,j);i=c(b,c(W,U[-a%19]));assert i[19]==a and c(i,i)==Id
    self.cand[a].append(i);self.folds[i]=(a,j)
  assert len(self.bor)==171 and len(self.folds)==171
  self.S2[Id]=self.sol[0,0]
 def pc(self,x,y):return tuple(x[i] for i in y)
 def lookup(self,t):
  if t not in self.mx2:
   X,Y=self.store[:2];a=t[19];parts=[]
   if a!=19:
    i=self.cand[a][0];q=self.pc(i,t);parts=[('u',a),('w',1),('u',(-a)%19)]
   else:q=t
   j,k=self.bor[q];parts+=[('u',j),('r',k)];
   for S,tab in [(X,self.mx2),(Y,self.my2)]:
    A=I(len(S['r']))
    for ch,j in parts:A=A@pw(S[ch],j)%3
    tab[t]=A
   self.pi2[t]=invperm(t)
  return self.mx2[t],self.my2[t],self.pi2[t]
 def raw(self,t):
  a,b,p=self.lookup(t);x=rng.integers(0,3,117,dtype=np.int32);x=(x-a@x)%3;y=rng.integers(0,3,119,dtype=np.int32);y=(y+b@y)%3;h=self.R.rand(True);h=(h-h[:,p])%3;k=self.R.rand();k=(k+k[:,p])%3;return self.mk(x,y,h,self.R.act(2*h%3,k),t)
 def prod(self,k,h):
  x,y,a,b,g=k;u,v,c,d,j=h;mx,my,p=self.lookup(g);return self.mk(x+mx@u,y+my@v,a+c[:,p],b+self.R.act(a,d[:,p]),self.pc(g,j))
 def factor(self,g):
  R=self.R;x,y,a,b,t=g;v=(b-R.poly(a))%3;vf=R.fac(v);hits=[]
  for i in self.cand[t[19]]:
   mx,my,p=self.lookup(i);k=self.pc(i,t);un,rr=self.bor[k];dk=pw(self.store[1]['u'],un)@self.ds[rr]%3
   if i not in self.S2:
    Q=col(I(117)-mx);E=I(119)-my;S=E@my@self.f@Q%3;pvs=ref(S.T)[1];assert len(pvs)==Q.shape[1];U=ref(np.column_stack((S[pvs,:],I(len(pvs)))))[0][:,len(pvs):];self.S2[i]=E,Q@U%3,pvs
   ac=(vf-vf[:,p])%3;ha=(a-ac)[:,p]%3;bb=R.act(ac,(v+R.poly(ac))%3);assert eq(bb[:,p],bb) and not np.any(ac.sum(axis=1)%3)
   c=(y-my@(self.f@(mx@x%3)+self.A@ha[-1,:19]+dk))%3;E,L,rows=self.S2[i];xx=L@(E@c%3)[rows]%3;yy=(c-my@self.f@xx)%3
   if not eq(yy,my@yy):continue
   assert eq(mx@xx,-xx);hx=mx@(x-xx)%3;out=self.mk(xx,yy,ac,R.act(2*ac%3,bb),i);hh=self.mk(hx,self.f@hx+self.A@ha[-1,:19]+dk,ha,R.poly(ha),k);assert self.same(self.prod(out,hh),g);hits.append(out)
  assert len(hits)==1;return hits[0]

def full_controls(B):
 R=Ring(3);G=Projective(R,B);sample=[G.raw(G.Id)]+[G.raw(i) for i in G.folds];assert len(sample)==172
 for k in sample:assert G.same(k,G.factor(k))
 rd=random.Random(8713);n=14;roles=set()
 for _ in range(n):
  x,y,z0=rd.choices(sample,k=3);roles.update([x[-1][19],y[-1][19],z0[-1][19]])
  a=G.op(x,G.op(y,G.op(x,z0)));b=G.op(G.op(x,G.op(y,x)),z0);assert G.same(a,b)
 print('full n=3 projective controls, all true grades',len(sample),'projective sites',len(G.cand),'arbitrary Bol triples',n,'distinct sampled nonregistered sites',len(roles),'native factorizations',len(sample)+6*n,flush=True)

def controls(n,B,triples):
 R=Ring(n);G=Group(R,B);samp=18 if n<=4 else 8;nc=0
 xunit=lambda pos,m:(np.eye(R.N,dtype=np.int32)[1<<pos])[:,None]*m
 sg=lambda i,j:(np.eye(20,dtype=np.int32)[i]-np.eye(20,dtype=np.int32)[j])%3
 e0=sg(0,1);e1=sg(0,2);h=R.zero.copy();a=xunit(0,e0)+xunit(1,e1);v=xunit(2,e0);g=(a,v);cube=R.g(R.g(g,g),g);assert not cube[0].any() and cube[1].any() and not R.g(R.g(cube,cube),cube)[1].any()
 # A length-n genuine commutator; [x,y] as conjugation minus identity in the normal additive subgroup.
 q=xunit(0,e0)
 for j in range(1,n):
  u=xunit(j,e1 if j==1 else e0);k=R.g(R.g((u,R.zero),(R.zero,q)),R.inv((u,R.zero)));q=(k[1]-q)%3
 assert q[-1].any() and not q[:-1].any();assert not R.mult(q,R.rand()).any()
 # All three projections in a true cubic failure of semi-3-abelianity: find same cubes/difference discrepancy in a tiny actual subfamily.
 e=(R.zero,R.zero);rot=(a,R.zero);lift=(R.zero,v);assert R.geq(R.g(R.g(rot,rot),rot),e) and R.geq(R.g(R.g(lift,lift),lift),e)
 mix=R.g(rot,R.inv(lift));assert not R.geq(R.g(R.g(mix,mix),mix),e)
 for z0 in range(samp):
  x=R.rand(True);y=R.rand(True);z1=R.rand();q1=R.rand();q2=R.rand();assert eq(R.fac(R.poly(x)),x);assert eq(R.fac(R.um(z1,q1)),R.fac(z1)+R.fac(q1));assert eq(R.mult(R.mult(z1,q1),q2),R.mult(z1,R.mult(q1,q2)))
  assert R.geq(R.g(R.graph(x),R.graph(y)),R.graph((x+y)%3))
  k1,k2,k3=R.randg(),R.randg(),R.randg();assert R.geq(R.g(R.g(k1,k2),k3),R.g(k1,R.g(k2,k3)))
  xx,yy=R.graph(x);t=R.randg();p=G.pi[z0%9,1];lz=R.sign(R.g(R.g(R.inv(t),(xx,yy)),t),p,1);actual=R.g(R.g(t,lz),R.inv(t));naive=R.sign((xx,yy),p,1)
  nc+=not R.geq(actual,naive);assert not R.geq(actual,R.inv((xx,yy)))
 # Hostile structural cases: a cut with correlated monomial slots, and last-coordinate imputation using the *honest* top, not unrestricted K.
 for k0 in (1,2):
  j=min(k0,n-1);vv=R.zero.copy();i0=(1<<j)-1;ss=sg(2,3);vv[i0]=ss;alt=i0^(1<<(j-1))^(1<<j);vv[alt]=ss
  for t0 in range(j,n):vv=R.mult(vv,xunit(t0,sg(2,0)))
  assert vv[-1].any() and not vv[:-1].any()
 # A noncentral normal R whose graph is tilted in two degree-(n-1) slots. U=pure top Y; z-flat, not sign-stable.
 pp,qq=R.top^1,R.top^2
 def nr(g):
  x,y=g;xx=R.zero.copy();yy=R.zero.copy();xx[pp]=xx[qq]=x[pp];yy[pp]=yy[qq]=x[pp];yy[-1]=y[-1];return eq(x,xx) and eq(y,yy)
 def rr(a,b):
  x=R.zero.copy();x[pp]=x[qq]=a;y=x.copy();y[-1]=b;return (x,y)
 nt=0;pf=G.pi[0,1];pos=col((I(20)+I(20)[pf])@(I(20)-2*np.ones((20,20),np.int32))%3);assert pos.shape[1]==9
 for _ in range(14):
  t=R.randg();g=rr(R.proj(rng.integers(0,3,20)),R.proj(rng.integers(0,3,20)));assert nr(g) and nr(R.g(R.g(t,g),R.inv(t))) and R.geq(R.graph(g[0]),rr(g[0][pp],z(20)))
  if not nr(R.sign(g,np.arange(20),1)):nt+=1
  # Starting on the physical i-sheet, changing the y by a top i-positive and no x is a genuine R-equivalence.
  a=R.rand(True);a=(a-a[:,pf])%3;b=R.rand();b=(b+b[:,pf])%3;k=(a,R.act(2*a%3,b));add=R.zero.copy();add[-1]=pos@rng.integers(0,3,9)%3
  k1=(a,R.act(2*a%3,b+add));assert nr(R.g(R.inv(k),k1))
  # Adding a nonzero i-negative in J has a forbidden negative required y change modulo U.
  j=rr(sg(0,19),z(20))[0];assert eq(j[:,pf],-j);k2=((a+j)%3,R.act(2*(a+j)%3,b));assert not nr(R.g(R.inv(k),k2))
 assert nt;print('tilted nongraded-in-subset normal R, projected z-flat, reflected collision divisor 3^9 vs required 3^19; actual non-sign-stable tests',nt,flush=True)
 marks=[G.mark(j%10) for j in range(20)];draw=random.Random(8971+n)
 for k in marks:
  assert G.same(G.factor(k),k);k2=G.prod(k,k);k6=G.prod(G.prod(k2,k2),k2);assert k6[-1]==(0,0) and all(not a.any() for a in k6[:-1])
 products=0
 for _ in range(triples):
  x,y,z0=draw.choices(marks,k=3)
  left=G.op(x,G.op(y,G.op(x,z0)));right=G.op(G.op(x,G.op(y,x)),z0);products+=6;assert G.same(left,right)
 print('n',n,'loop 3-part log',119+19*(n+1)+20*(2**n-n-2),'ring group true powers',9,'max true commutator grade',n,'all actual nonlinear inversion vs pure discrepancies',nc,'of',samp,'unique native pivot tests including six products/triple',20+products,flush=True)
if __name__=='__main__':
 path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'evidence/psl2-19-explicit-matrix-input.json.zlib.b64'
 raw=zlib.decompress(base64.b64decode(path.read_bytes()));assert hashlib.sha256(raw).hexdigest()==HASH;B=base(json.loads(raw))
 for n,k in ((3,15),(4,8),(5,3)):controls(n,B,k)
 full_controls(B)
 print('PASS: actual projective products and explicit nonsign-stable cuts; the proof handles all ring sizes and all normal subgroups.')
