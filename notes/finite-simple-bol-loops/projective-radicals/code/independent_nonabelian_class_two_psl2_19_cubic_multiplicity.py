"""Exact F3 check at s=3 on the original affine matrices, without importing the source checker."""
import base64,zlib,json,hashlib,sys
from itertools import product
from pathlib import Path
import numpy as np
S=3;M0=int(3);rng=np.random.default_rng(118033)
def eye(n):return np.eye(n,dtype=np.int32)
def z(*s):return np.zeros(s,dtype=np.int32)
def mm(x,y):return (x@y)%3
def red(A,pivotmax=None):
 U=(A%3).copy();d=0;idx=[]
 for j in range(U.shape[1] if pivotmax is None else pivotmax):
  ids=np.flatnonzero(U[d:,j])
  if not len(ids):continue
  t=ids[-1]+d;U[[d,t]]=U[[t,d]];U[d]=(U[d]*U[d,j])%3
  w=U[:,j].copy();w[d]=0
  # Only nonzero rows need the genuine multiple of the pivot.
  zz=np.flatnonzero(w)
  if len(zz):U[zz]=(U[zz]-w[zz,None]*U[d])%3
  idx.append(j);d+=1
  if d==len(U):break
 return U,idx
def rk(A):return len(red(A)[1])
def span(A):return A[:,red(A)[1]]
def null(A):
 U,I=red(A);J=[j for j in range(A.shape[1])if j not in I];Q=z(A.shape[1],len(J));Q[J]=eye(len(J));Q[I]=-U[:len(I),J];return Q%3
def pwr(A,j):
 P=eye(len(A))
 for i in range(j):P=mm(P,A)
 return P
def blk(A,B):
 n,m=A.shape;p,q=B.shape;C=z(n+p,m+q);C[:n,:m]=A;C[n:,m:]=B;return C
def fixed(X,keys):return null(np.vstack([(X[g]-eye(len(X[g])))%3 for g in keys]))
def permfun(g,i):
 if g=='u':return (i+1)%19 if i!=19 else 19
 if g=='r':return 4*i%19 if i!=19 else 19
 return (19 if i==0 else 0 if i==19 else -pow(i,-1,19)%19)
def aug(g):
 P=z(20,20)
 for i in range(20):P[permfun(g,i),i]=1
 return (P[:19,:19]-P[:19,19,None])%3
MM={g:aug(g)for g in 'urw'}
def readbase(f):
 Y=zlib.decompress(base64.b64decode(Path(f).read_bytes()))
 assert hashlib.sha256(Y).hexdigest()=='c5965e0fdc104b529bf3eac790bac48d83e1c8ef03d8cb04f284893eaeb53ddb'
 return {k:np.array([list(map(int,r))for r in a],np.int32)for k,a in json.loads(Y).items()}
def batch(A):
 X={g:A['X'+g]for g in 'urw'};Y={g:A['Y'+g]for g in 'urw'};f=A['f'];d=A['d'];I=eye(len(d))
 D=mm((I+Y['r']+pwr(Y['r'],2))%3,d);G=np.column_stack(((f+mm(mm(Y['w'],f),X['w']))%3,pwr(Y['r'],3)-I))
 K=null(G.T);u=mm(I-Y['w'],D);y0=next(c for c in K.T if mm(c,u)[0]);phi=mm(y0,(I-Y['w'])*2);phi=phi*int(mm(phi,u)[0])%3
 assert mm(phi,G).sum()==0 and mm(phi,u)[0]==1 and not (phi+mm(phi,Y['w'])).__mod__(3).any()
 cf=[]
 for it,l in enumerate([1]*S+[S]):
  B=fixed(Y,'r');U=[pwr(Y['u'],j)for j in range(19)]
  cond=mm((eye(19)-MM['w']).T,mm(np.vstack([mm(phi,t)for t in U]),B))
  allowed=mm(B,null(cond))
  DX=mm(X['w']-eye(len(X['w'])),fixed(X,'ur'));DY=mm(Y['w']-eye(len(Y['w'])),fixed(Y,'ur'))
  bad=span(np.column_stack((mm(f,DX),DY)));old=bad.shape[1]
  sel=[]
  for unused in range(100):
   h=mm(allowed,rng.integers(3,size=allowed.shape[1],dtype=np.int32))
   nb=span(np.column_stack((bad,h)))
   if nb.shape[1]>bad.shape[1]:sel.append(np.column_stack([mm(t,h)for t in U]));bad=nb
   if len(sel)==l:break
  assert len(sel)==l and rk(cond)<=7
  if l>1:
   # Independently test every nonzero active coupling combination, not just one echelon test.
   orig=span(np.column_stack((mm(f,DX),DY)))
   for w in product(range(3),repeat=l):
    if any(w):assert rk(np.column_stack((orig,sum(i*a[:,0] for i,a in zip(w,sel))%3)))==old+1
  assert all(not(mm(Y[g],h)-mm(h,MM[g])).__mod__(3).any()for h in sel for g in 'ur')
  cf.append((B.shape[1],rk(cond),old,l));ax=np.column_stack(sel);nf=z(len(f)+19*l,f.shape[1]+19*l);nf[:len(f),:f.shape[1]]=f;nf[:len(f),f.shape[1]:]=ax;nf[len(f):,f.shape[1]:]=eye(19*l);f=nf
  for _ in range(l):X={g:blk(X[g],MM[g])for g in X};Y={g:blk(Y[g],MM[g])for g in Y}
  d=np.vstack((d,z(19*l,1)));phi=np.r_[phi,z(19*l)]
 assert not mm(phi,(f+mm(mm(Y['w'],f),X['w']))%3).any()
 assert not mm(phi,pwr(Y['r'],3)-eye(len(d))).any()
 ex=(eye(len(X['w']))-X['w'])%3;ey=(eye(len(Y['w']))-Y['w'])%3
 assert rk(mm(mm(ey,f),ex))==rk(ex)
 print('actual s=3 passive/active allowed and rejected dimensions (available, #constraints, bad, selected)',cf,flush=True)
 return X,Y,f,d,phi
def torus(X,Y,f,d,phi):
 J=list(range(119))+list(range(119+19*S,len(Y['w'])))
 Xw=X['w'];Yw=Y['w'][np.ix_(J,J)];Yr=Y['r'][np.ix_(J,J)];qr=blk(X['r'],Yr)
 K=blk(Xw,-Yw)%3;I=eye(len(K));W=np.vstack((eye(len(Xw)),f[J]));d0=d[J];u=z(len(d0),1);out=[]
 for j in range(1,9):
  u=(u+mm(pwr(Yr,j-1),d0))%3;h=(I+mm(K,pwr(qr,j)))%3
  col=mm(h,mm(K,np.vstack((z(len(Xw),1),u))))
  T=mm(h,np.column_stack((I-K,mm(K,W))))
  # One simultaneous reduction, including the affine column as the LAST potential pivot.
  T1=np.column_stack((T,col));piv=red(T1)[1];assert piv[-1]==T.shape[1];out.append(len(piv)-1)
 print('all eight true simultaneous torus ranks modulo exactly the central passive outputs, each affine rise 1',out,flush=True)
def beta(v,u):
 a=np.r_[v,-sum(v)%3];b=np.r_[u,-sum(u)%3];c=(a*b)%3;return (c[:19]-2*sum(c))%3
def tensors(X,Y,f,d):
 nx=f.shape[1];ny=f.shape[0];N=nx+ny;V=lambda:rng.integers(3,size=N,dtype=np.int32);off=nx+119;zs=19*S
 C=np.array([[[1,0,0],[0,1,0],[0,0,1]],[[0,1,1],[1,2,0],[1,0,1]],[[2,0,1],[0,0,1],[1,1,1]]],np.int32)
 assert rk(C.reshape(S,-1))==S
 def bracket(v,w):
  H=z(N);a=v[nx-zs:nx].reshape(S,19);b=v[N-zs:].reshape(S,19);u=w[nx-zs:nx].reshape(S,19);t=w[N-zs:].reshape(S,19);B=H[off:off+zs].reshape(S,19)
  for i,j in product(range(S),repeat=2):B+=C[:,i,j,None]*(beta(a[i],t[j])-beta(u[i],b[j]))
  return H%3
 def mul(v,w):return (v+w+2*bracket(v,w))%3
 wk=blk(X['w'],-Y['w'])%3;upr=blk(X['u'],Y['u']);one=eye(N);rp=blk(X['r'],Y['r']);dy=lambda x:np.r_[x,mm(f,x)]
 pairs=0
 for idx in range(100):
  v,w,t=V(),V(),V();assert np.array_equal(mul(mul(v,w),t),mul(v,mul(w,t)))
  assert not mul(mul(v,v),v).any()
  assert np.array_equal(mul(mul(mul(v,w),-v%3),-w%3),bracket(v,w))
  assert not bracket(dy(v[:nx]),dy(w[:nx])).any()
  for g in(wk,upr,rp):assert np.array_equal(mm(g,mul(v,w)),mul(mm(g,v),mm(g,w)))
  c=mm(one-wk,w);obj=dy(v[:nx]);pure=mm(wk,obj);real=mul(mul(c,pure),-c%3)
  if not np.array_equal(real,pure):pairs+=1
  # A physically conjugated sign need not equal a linear sign, but if it inverts, the opposite active coordinates vanish.
  if np.array_equal(real,-obj%3):assert not obj[nx-zs:nx].any()
 assert pairs>0
 # A genuinely noncentral T-submodule/ideal that is NOT sign-stable: equal active X/Y in first M, all passive outputs.
 R=z(N,zs+19);R[off:off+zs,:zs]=eye(zs);R[nx-zs:nx-zs+19,zs:]=eye(19);R[N-zs:N-zs+19,zs:]=eye(19)
 signed=blk(eye(nx),-eye(ny))%3
 assert rk(np.column_stack((R,mm(signed,R))))>R.shape[1]
 for g in(upr,rp,blk(X['w'],Y['w'])):assert rk(np.column_stack((R,mm(g,R))))==R.shape[1]
 for h in range(10):
  v=V();x=mm(R,rng.integers(3,size=R.shape[1]));c=bracket(x,v);assert not c[:off].any()and not c[off+zs:].any()
 W=dy(eye(nx));Yspace=np.vstack((z(nx,ny),eye(ny)));Aw=span((one-wk)%3)
 dim=lambda Z:rk(Z);meet=lambda P,Q:dim(P)+dim(Q)-rk(np.column_stack((P,Q)))
 dr=R.shape[1]-meet(R,W);ss=(dr-meet(R,Yspace),dr-meet(R,Aw));assert max(ss)>0 and min(ss)>=0
 # A changed but equivalent central output basis must not be counted as an independent isotype.
 for v,w in [(V(),V())for _ in range(12)]:
  old=bracket(v,w)[off:off+zs].copy().reshape(S,19);C[1]=(C[1]+C[0])%3
  got=bracket(v,w)[off:off+zs].reshape(S,19);assert np.array_equal(got[1],(old[1]+old[0])%3)
  C[1]=(C[1]-C[0])%3
 print('100 actual ternary BCH/physical inverter tests, conjugated-sign differs',pairs,'times; noncentral non-sign-stable ideal two strict-cut exponents',ss,flush=True)
D=readbase(sys.argv[1]);X,Y,f,d,phi=batch(D);torus(X,Y,f,d,phi);tensors(X,Y,f,d)
for s in range(21,202):
 assert (s-1)*(s*(s+1)//2-1)-15-5*s*s>=s**3/4
print('all coefficient/aut inequalities at 21..201; analytic monotone polynomial establishes larger s')
