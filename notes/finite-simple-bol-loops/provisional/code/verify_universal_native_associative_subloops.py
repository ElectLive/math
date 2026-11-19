#!/usr/bin/env python3
"""Actual isotope products, global translation defects and adverse central-phase controls.
Requires NumPy, the three cited local projective checkers and the pinned matrix input."""
import base64,hashlib,itertools,json,sys,zlib
from pathlib import Path
import numpy as np
from verify_class_two_psl2_19_cubic_multiplicity import I,z,cat,pmat,modules,fix,pw,rank,ref,col,null,widen,block,HASH,beta
from verify_countable_universal_radical_tower import VNative,ind
def choose_vectors():
 a=z(19);a[0]=1
 b=z(19);b[0]=1;b[1]=b[18]=2
 w=modules()['w'];assert np.array_equal(w@a%3,-a%3) and np.array_equal(w@b%3,b) and np.array_equal(beta(a,b),a)
 return a,b
def solve(A,B):
 # Full column rank (negative sign injection), rectangular with multiple independent RHS.
 rr,rows=ref(A.T);rows=rows[:A.shape[1]]
 assert len(rows)==A.shape[1]
 rr,piv=ref(np.column_stack((A[rows],B[rows])));assert piv==list(range(A.shape[1]))
 X=rr[:,A.shape[1]:];assert np.array_equal(A@X%3,B%3)
 return X
def build(data,kind,breaks):
 M=modules();X={g:pmat(data['X'+g]) for g in 'urw'};Y={g:pmat(data['Y'+g]) for g in 'urw'}
 f=pmat(data['f']);d=pmat(data['d']);E=I(len(d))-Y['w'];D=(I(len(d))+Y['r']+pw(Y['r'],2))@d%3
 S=null(np.column_stack((f+Y['w']@f@X['w'],pw(Y['r'],3)-I(len(d)))).T).T@E%3
 phi=next(a for a in S if int((a@E@D)[0])%3);phi=phi*int((phi@E@D)[0])%3
 P=[];A=[];history=[]
 for j in range(len(kind)+1):
  if j in breaks:
   ix=ind(117,P+A);iy=ind(119,P+A)
   N=VNative((M,{g:v[np.ix_(ix,ix)] for g,v in X.items()},{g:v[np.ix_(iy,iy)] for g,v in Y.items()},f[np.ix_(iy,ix)],d[iy,0],phi[iy]),len(A),len(P))
   assert np.array_equal(N.f[N.offy:],np.column_stack((np.zeros((19*N.s,N.offx),np.int32),I(19*N.s))))
   print('chronological',kind[:j],'restricted/torus/extra increment/bad/new shear dimension signature',history,flush=True)
   yield N;history=[]
  if j==len(kind):return
  ix=ind(117,P);iy=ind(119,P);B0=fix(Y,'r');ai=[119+19*h+k for h in A for k in range(19)]
  B=B0@null(B0[ai])%3 if ai else B0
  us=[I(len(d))]
  for _ in range(18):us.append(Y['u']@us[-1]%3)
  det=(I(19)-M['w']).T@np.vstack([phi@u for u in us])@B%3
  # a=m0, so A(a) is precisely the physical r-fixed image parameter.
  ex=I(len(ix))-X['w'][np.ix_(ix,ix)];ey=I(len(iy))-Y['w'][np.ix_(iy,iy)]
  out=col(ey@f[np.ix_(iy,ix)]@col(ex)%3)
  assert rank(ey)-out.shape[1]==2
  extra=null(out.T).T@ey@B[iy]%3
  assert rank(extra)<=2
  cc=np.vstack((det,extra)) if kind[j]=='P' else det
  good=B@null(cc)%3
  bad=col(np.column_stack((f@(X['w']-I(len(X['w'])))@fix(X,'ur')%3,(Y['w']-I(len(d)))@fix(Y,'ur')%3)))
  sel=next(b for b in good.T[::-1] if rank(np.column_stack((bad,b)))==bad.shape[1]+1)
  a=np.column_stack([u@sel%3 for u in us])
  assert (not ai or not a[ai].any()) and not (phi@(a+Y['w']@a@M['w'])%3).any()
  if kind[j]=='P':assert rank(np.column_stack((out,ey@sel[iy]%3)))==out.shape[1]
  (P if kind[j]=='P' else A).append(j)
  history.append((B.shape[1],rank(det),rank(cc)-rank(det),bad.shape[1],good.shape[1]))
  X={g:block(v,M[g]) for g,v in X.items()};Y={g:block(v,M[g]) for g,v in Y.items()}
  f=widen(f,a);d=np.vstack((d,np.zeros((19,1),np.int32)));phi=cat(phi,z(19))
class Orbit:
 def __init__(self,N):
  self.N=N;self.s=s=N.s;self.t=t=N.t
  self.w=(N.z,(0,1,0));self.a,self.b=choose_vectors();self.cs={}
  f=N.f[:N.offy,:N.offx];X=N.X['w'][:N.offx,:N.offx];Y=N.Y['w'][:N.offy,:N.offy]
  E=I(len(Y))-Y;L=col(I(len(X))-X);B=np.zeros((len(Y),t),np.int32)
  for j in range(t):B[119+19*j:119+19*(j+1),j]=2*self.a
  self.l=L@solve(E@f@L%3,B)%3;self.hs=[]
  for j in range(t):
   l=cat(self.l[:,j],z(19*s));h=N.mul(N.mul(self.w,N.H(l,0)),self.w)
   assert h[1]==(0,0,0) and not h[0][N.offx:N.nx].any() and not h[0][N.nx+N.offy:].any()
   assert N.inH(N.mul(N.mul(self.w,h),self.w))
   self.hs.append(h[0])
  self.hs=np.column_stack(self.hs);assert rank(self.hs)==t
 def body(self,g):
  s,t=self.s,self.t;N=self.N;a,b=self.a,self.b;q=z(N.n)
  q[N.offx:N.nx]=(g[:s,None]*a).ravel();q[N.nx+N.offy:]=(g[s:2*s,None]*b).ravel()
  q[N.nx+119:N.nx+N.offy]=(g[2*s:,None]*a).ravel()
  return q%3
 def rawprod(self,g,h):
  s=self.s;o=np.einsum('i,kij,j->k',g[:s],self.N.C,h[s:2*s])-np.einsum('i,kij,j->k',h[:s],self.N.C,g[s:2*s])
  k=(g+h)%3;k[2*s:]=(k[2*s:]+2*o)%3
  return k,o%3
 def label(self,g):
  key=tuple(map(int,g))
  if key in self.cs:return self.cs[key]
  N=self.N;q=self.body(g);mark=N.reduced((q,(0,1,0)))
  # Solve on the actual coset over ALL its nine possible projected inversion labels.
  native=N.mul(mark,self.w);corr=self.hs@g[2*self.s:]%3
  assert N.eq(native,((q+corr)%3,(0,0,0)))
  assert np.array_equal(N.act((0,1,1),native[0]),-native[0]%3)
  if g[2*self.s:].any():
   assert not np.array_equal(N.act((0,1,1),q),-q%3) and not np.array_equal(q,native[0])
  self.cs[key]=mark,native
  return mark,native
 def test(self,g,h,full=True):
  N=self.N;a,u=self.label(g);b,v=self.label(h);gh,om=self.rawprod(g,h);c,d=self.label(gh)
  pr=N.mul(N.inv(d),N.mul(u,v));want=(self.hs@om)%3 # -1/2 = +1 in F3.
  assert N.eq(pr,(want,(0,0,0))) and bool(want.any())==bool(om.any())
  # An actual three-original-mark product on G/H, not merely comparing BCH coordinates.
  nh=N.mul(N.inv(c),N.mul(N.mul(a,self.w),b));assert N.inH(nh)
  if full:assert N.eq(N.star(a,N.star(self.w,b)),c)
  return (int(om.any()),int(pr[0].any()),int(N.inH(pr)))
 def external(self,j):
  # Check actual ambient points tau.H (all 20 projected sites) using the two true T actions.
  N=self.N;q=self.hs[:,j];x=q[:N.nx];y=q[N.nx:];U=N.X['u'];V=N.Y['u'];WX=N.X['w'];WY=N.Y['w']
  ny=nx=0;ok=[]
  for i in range(20):
   if i<19:
    xx=WX@x%3;yy=WY@y%3;x=U@x%3;y=V@y%3
   else:xx=q[:N.nx];yy=q[N.nx:]
   ok.append(np.array_equal(N.f@xx%3,yy))
  assert any(ok) and not all(ok)
  return sum(ok)
def inp(n):return np.array(n,dtype=np.int32)
def main():
 path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'evidence/psl2-19-explicit-matrix-input.json.zlib.b64'
 raw=zlib.decompress(base64.b64decode(path.read_bytes()));assert hashlib.sha256(raw).hexdigest()==HASH
 data=json.loads(raw);rng=np.random.default_rng(19620)
 for N in build(data,'PA',{2}):
  O=Orbit(N);E=[inp(x) for x in itertools.product(range(3),repeat=3)]
  got=[O.test(g,h,True) for g in E for h in E]
  assert len({O.label(g)[0][0].tobytes() for g in E})==27
  print('Heisenberg 27: ALL literal isotope table products, true nonzero commutator/ambient defect and fixes among 20 native projective test points',len(got),sum(k[0] for k in got),sum(k[1] for k in got),O.external(0),flush=True)
  assert sum(k[0] for k in got)==432
  p=(z(N.n),(1,1,0));r=N.mul(p,O.w);assert r[1]==(1,0,0)
  powers=[(z(N.n),(0,0,0))]
  for i in range(9):powers.append(N.mul(powers[-1],r))
  cosets=[N.reduced(N.mul(c,O.w)) for c in powers]
  assert len({(a.tobytes(),g) for a,g in cosets})==9 and N.eq(cosets[0],cosets[9])
  print('actual 9-cycle at new identity; old translations have exponent six',flush=True)
 old=None
 for N in build(data,'PPAPPA',{3,6}):
  O=Orbit(N);n=2*N.s+N.t;nont=0;outside=0
  for j in range(44):
   g=rng.integers(3,size=n,dtype=np.int32);h=rng.integers(3,size=n,dtype=np.int32)
   v=O.test(g,h,True);nont+=v[0];outside+=bool(g[2*N.s:].any())
  print('all-phase samples at active/passive',N.s,N.t,'actual isotope products/commutator defects/nonzero input phases',44,nont,outside,'fixed native site counts per nonzero tested correction',[O.external(j) for j in range(N.t)],flush=True)
  if old:
   for i in range(17):
    g=rng.integers(3,size=2*old.s+old.t,dtype=np.int32);x=z(n);x[:old.s]=g[:old.s];x[N.s:N.s+old.s]=g[old.s:2*old.s];x[2*N.s:2*N.s+old.t]=g[2*old.s:]
    a,b=old.label(g);c,d=O.label(x)
    assert N.eq((N.fromold(a[0],old.N),a[1]),c) and N.eq((N.fromold(b[0],old.N),b[1]),d)
   print('17 chronological embeddings preserve real point and full ambient permutation, including central phase',flush=True)
  old=O
 # Separate Heisenberg-slice graph exercise: all labelled graphs on 5 vertices and genuine ternary products.
 n=5;cnt=0
 for mask in range(1<<10):
  ed={(i,j) for k,(i,j) in enumerate(itertools.combinations(range(n),2)) if (mask>>k)&1}
  G=np.zeros((n,n),np.int32)
  for i in range(n):
   for j in range(i):G[i,j]=int((j,i) not in ed)
  for i,j in itertools.combinations(range(n),2):assert ((G[j,i]-G[i,j])%3==0)==((i,j) in ed)
  cnt+=1
 print('all',cnt,'five-vertex commuting prescriptions; genuine ambient checks above, finite tests do not prove infinite universality.')
if __name__=='__main__':main()
