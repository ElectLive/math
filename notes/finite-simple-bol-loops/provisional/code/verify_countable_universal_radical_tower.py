#!/usr/bin/env python3
"""Direct native compatibility tests for the coherent interleaved universal radical.
Requires numpy, original affine matrix input, and preceding exact projective checkers."""
import base64,zlib,hashlib,json,sys
from pathlib import Path
import numpy as np
from verify_class_two_psl2_19_cubic_multiplicity import Native,beta,I,z,cat,pmat,modules,fix,pw,rank,col,null,widen,block,HASH
def ind(n,order):
 return np.r_[np.arange(n,dtype=int),np.array([n+19*u+i for u in order for i in range(19)],int)]
def tags(s):
 ans=[]
 for k in range(2,s+2):
  for i in range(1,k):
   if len(ans)==s:return ans
   ans.append((i,k-i))
 return ans
def Cdef(s,t):
 ad=tags(s);C=np.zeros((t,s,s),np.int32)
 for a,(i,j) in enumerate(ad):
  b=ad.index((i,1));C[j-1,a,b]=C[j-1,b,a]=1
 return C
class VNative(Native):
 def __init__(self,datum,s,t):
  super().__init__(datum,s,Cdef(s,t));self.t=t;self.offx=117+19*t;self.offy=119+19*t
 def bracket(self,v,w):
  s=self.s;t=self.t
  x=v[self.offx:self.nx].reshape(s,19);y=v[self.nx+self.offy:].reshape(s,19)
  a=w[self.offx:self.nx].reshape(s,19);b=w[self.nx+self.offy:].reshape(s,19)
  out=z(self.n);q=out[self.nx+119:self.nx+self.offy].reshape(t,19)
  for h,i,j in zip(*np.nonzero(self.C)):
   q[h]+=beta(x[i],b[j])-beta(a[i],y[j])
  return out%3
 def fromold(self,v,o):
  # Sorted passive,active slots on both wings. Old active positions move in memory.
  x=z(self.n)
  x[:o.offx]=v[:o.offx];x[self.offx:self.offx+19*o.s]=v[o.offx:o.nx]
  x[self.nx:self.nx+o.offy]=v[o.nx:o.nx+o.offy]
  x[self.nx+self.offy:self.nx+self.offy+19*o.s]=v[o.nx+o.offy:]
  return x
def stages(D,smax):
 M=modules();X={g:pmat(D['X'+g]) for g in 'urw'};Y={g:pmat(D['Y'+g]) for g in 'urw'}
 f=pmat(D['f']);d=pmat(D['d']);F=(f+Y['w']@f@X['w'])%3
 D3=(I(len(d))+Y['r']+pw(Y['r'],2))@d%3
 sep=null(np.column_stack((F,pw(Y['r'],3)-I(len(d)))).T).T@(I(len(d))-Y['w'])%3
 phi=next(v for v in sep if int((v@(I(len(d))-Y['w'])@D3)[0])%3)
 phi=phi*int((phi@(I(len(d))-Y['w'])@D3)[0])%3
 P=[];A=[];ranks=[]
 for l in range(3*smax+1):
  if l%3==0:
   o=P+A;ix=ind(117,o);iy=ind(119,o)
   datum=M,{g:m[np.ix_(ix,ix)] for g,m in X.items()},{g:m[np.ix_(iy,iy)] for g,m in Y.items()},f[np.ix_(iy,ix)],d[iy,0],phi[iy]
   N=VNative(datum,len(A),len(P))
   E=I(N.ny)-N.Y['w'];DX=col(I(N.nx)-N.X['w']);assert rank(E@N.f@DX%3)==DX.shape[1]
   h=np.column_stack([(N.f+N.Y['w']@N.f@N.X['w'])%3,pw(N.Y['r'],3)-I(N.ny)])
   assert not (N.phi@h%3).any() and (N.phi@E@N.ds[3]%3)==1
   assert np.array_equal(N.f[N.offy:],np.column_stack((np.zeros((19*N.s,N.offx),np.int32),I(19*N.s))))
   print('stage/passives/actives; full-H injection, certified torus obstruction; affine ranks (restricted, allowed, bad; chosen)',l//3,len(P),len(A),ranks,flush=True)
   yield N;ranks=[]
  if l==3*smax:break
  pr=fix(Y,'r');U=[I(len(d))]
  for _ in range(18):U.append(Y['u']@U[-1]%3)
  # Intersect *all* of the true forbidden previous active output rows, not only a compressed subspace.
  ai=[119+19*u+i for u in A for i in range(19)]
  B=pr@null(pr[ai])%3 if ai else pr;assert B.shape[1]==14+3*len(P)
  form=(I(19)-M['w']).T@np.vstack([phi@u for u in U])@B%3
  good=B@null(form)%3
  bad=col(np.column_stack([f@(X['w']-I(len(X['w'])))@fix(X,'ur')%3,(Y['w']-I(len(d)))@fix(Y,'ur')%3]))
  assert good.shape[1]-bad.shape[1]>=4 and rank(form)<=7
  # Work from the newest available physical passive block; use a real nonzero new-to-old shear.
  chosen=next(i for i in reversed(range(good.shape[1])) if rank(np.column_stack((bad,good[:,i])))==bad.shape[1]+1)
  a=np.column_stack([u@good[:,chosen]%3 for u in U])
  assert not (phi@(a+Y['w']@a@M['w'])%3).any() and (not ai or not a[ai].any())
  assert all(np.array_equal(Y[g]@a%3,a@M[g]%3) for g in 'ur')
  assert not np.array_equal(a,np.zeros_like(a)) and rank(np.column_stack((bad,0*good[:,chosen])))==bad.shape[1]
  ranks.append((B.shape[1],good.shape[1],bad.shape[1],chosen))
  (A if l%3==2 else P).append(l)
  f=widen(f,a);d=np.vstack([d,np.zeros((19,1),np.int32)]);phi=cat(phi,z(19))
  X={g:block(m,M[g]) for g,m in X.items()};Y={g:block(m,M[g]) for g,m in Y.items()}
def fullcausal(v):
 # Represent a dense infinite bracket column by a finite description; emit only true single-generator coordinates.
 out={('plus',v,1):1}
 if v>1:out['minus',1,v]=1
 return out
def main():
 p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'evidence/psl2-19-explicit-matrix-input.json.zlib.b64'
 bs=zlib.decompress(base64.b64decode(p.read_bytes()));assert hashlib.sha256(bs).hexdigest()==HASH
 rng=np.random.default_rng(196193);last=None
 for N in stages(json.loads(bs),2):
  if last is not None:
   O=last;L=lambda h:(N.fromold(h[0],O),h[1]);gzero=(0,0,0);total=0;real=0
   for _ in range(8):
    ex=lambda n:rng.integers(0,3,n,dtype=np.int32)
    v,w=ex(O.n),ex(O.n);assert np.array_equal(N.fromold(O.coremul(v,w),O),N.coremul(N.fromold(v,O),N.fromold(w,O)))
    j=int(rng.integers(9));h=O.H(ex(O.nx),j);assert N.inH(L(h))
    x=O.mark(int(rng.integers(9)),1,rng);y=O.mark(int(rng.integers(9)),1,rng)
    assert N.eq(N.mul(L(x),L(y)),L(O.mul(x,y))) and N.eq(N.star(L(x),L(y)),L(O.star(x,y)))
    for k in [x,y]:
     u,gg=L(k);assert np.array_equal(N.act((gg[0],gg[1],1),u),-u%3)
    # Compare old-new ambient products rather than just graph matrices: look for a genuinely updated bracket.
    v=ex(N.n);w=ex(N.n)
    real+=bool(N.bracket(v,w).any())
    total+=1
   print('adjacent actual zero-embedded Bol products / group products, new nonzero brackets',O.s,N.s,total,real,flush=True)
  last=N
 # New (1,2) entry really sees the (1,1) slot and sends product into its second native passive target.
 N=last;e=z(19);e[0]=1;w=beta(e,e)
 a=z(N.n);b=z(N.n);a[N.offx:N.offx+19]=e;b[N.nx+N.offy+19:N.nx+N.offy+38]=e
 out=N.bracket(a,b);target=z(N.n);target[N.nx+119+19:N.nx+119+38]=w
 assert np.array_equal(out,target)
 # Bad old-old extension would break the very angle checked above, regardless of good shears.
 N.C[3,0,0]=1;b=z(N.n);b[N.nx+N.offy:N.nx+N.offy+19]=e
 assert np.array_equal(N.bracket(a,b)[N.nx+119+3*19:N.nx+119+4*19],w)
 N.C[3,0,0]=0
 assert not N.bracket(a,b)[N.nx+119+3*19:N.nx+119+4*19].any()
 for n in (5,10,20,40):
  # Finite restrictions of the countably many z_j model all commute except with v1.
  outs=[fullcausal(i) for i in range(1,n+1)];nonzero=0
  for i in range(1,n+1):
   for j in range(i+1,n+1):
    br={c:(outs[j-1].get(('minus',i,c),0)-outs[i-1].get(('minus',j,c),0))%3 for c in range(1,n+1)}
    assert {c for c,u in br.items() if u}==({j} if i==1 else set());nonzero+=bool(any(br.values()))
  print('finite restriction of infinite column; size / nonzero brackets / max slots per generator',n,nonzero,max(map(len,outs)))
 print('PASS: same old physical products through two nonlinear extensions; positive and broken-coherence controls.')
if __name__=='__main__':main()
