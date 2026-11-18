"""Exact deterministic first steps and adverse controls for the uniform augmentation tower."""
import base64,hashlib,json,sys,zlib
from pathlib import Path
import numpy as np
HASH='c5965e0fdc104b529bf3eac790bac48d83e1c8ef03d8cb04f284893eaeb53ddb'
def I(n):return np.eye(n,dtype=np.int32)
def ref(A):
 M=A.copy()%3;n,m=M.shape;k=0;p=[]
 for j in range(m):
  if k==n:break
  ss=np.flatnonzero(M[k:,j])
  if not len(ss):continue
  a=k+ss[0];M[[k,a]]=M[[a,k]];M[k]=M[k]*M[k,j]%3
  v=M[:,j].copy();v[k]=0;M=(M-v[:,None]*M[k])%3;p.append(j);k+=1
 return M,p
def rank(A):return len(ref(A)[1])
def col(A):return A[:,ref(A)[1]]
def null(A):
 R,p=ref(A);n=A.shape[1];q=[j for j in range(n) if j not in p];U=I(n)[:,q]
 if p:U[p,:]=-R[:len(p),q]%3
 return U
def block(A,B):
 m,n=A.shape;y,x=B.shape
 return np.block([[A,np.zeros((m,x),np.int32)],[np.zeros((y,n),np.int32),B]])
def pw(A,j):
 M=I(len(A))
 for _ in range(j):M=A@M%3
 return M
def modules():
 def act(g):
  all=np.vstack([I(19),-np.ones((1,19),dtype=np.int32)]);out=np.zeros_like(all)
  for s,t in enumerate(g):out[t]=all[s]
  return out[:19]%3
 return {'u':act([(j+1)%19 for j in range(19)]+[19]),'r':act([4*j%19 for j in range(19)]+[19]),'w':act([19]+[-pow(j,-1,19)%19 for j in range(1,19)]+[0])}
def fix(N,letters):return null(np.vstack([N[g]-I(len(N[g])) for g in letters]))
def core(rows,N):
 W=col(rows.T).T
 while len(W):
  H=col(np.vstack([W,W@N['u']%3,W@N['w']%3]).T).T
  if len(H)==len(W):break
  W=H
 return null(W)
def check(X,Y,f,d,n):
 nx,ny=f.shape[1],f.shape[0];E=I(ny)-Y['w'];S=col(I(nx)-X['w']);bad=0
 assert ny==119+19*n and nx==117+19*n and rank(E)-len(S.T)==2 and rank(E@f@S%3)==len(S.T)
 assert all(np.array_equal(f@X[g]%3,Y[g]@f%3) for g in 'ur')
 F=(f+Y['w']@f@X['w'])%3;T=(pw(Y['r'],3)-I(ny))%3;D=(I(ny)+Y['r']+pw(Y['r'],2))@d%3
 A=np.column_stack([F,T]);old=rank(A);new=rank(np.column_stack([A,E@D%3]));assert new==old+1
 W=S;steps=[]
 while True:
  Z=core(null((E@f@W%3).T).T@E%3,Y);J=core(null(Z.T).T@f%3,X);N=col((I(nx)-X['w'])@J%3)
  steps.append((W.shape[1],N.shape[1],J.shape[1],Z.shape[1]))
  if W.shape[1]==N.shape[1]:break
  W=N
 assert not J.shape[1] and not Z.shape[1]
 xcoin=null(np.vstack([(X[g]-I(nx)).T for g in 'uw']));ycoin=null(np.vstack([(Y[g]-I(ny)).T for g in 'uw']))
 assert not xcoin.shape[1] and ycoin.shape[1]==1 and rank(ycoin.T@np.column_stack([f,d])%3)==1
 return old,new,steps
def widen(f,a):
 x=f.shape[1];m=a.shape[1]
 return np.block([[f,a],[np.zeros((m,x),dtype=np.int32),I(m)]])
def run(D,last):
 m=modules()
 assert pow(3,18,19)==1 and all(pow(3,j,19)!=1 for j in (1,2,3,6,9))
 assert [fix(m,s).shape[1] for s in ('uw','ur','r')]==[0,1,3]
 X={k:np.array([list(map(int,s)) for s in D['X'+k]],np.int32) for k in 'urw'}
 Y={k:np.array([list(map(int,s)) for s in D['Y'+k]],np.int32) for k in 'urw'}
 f=np.array([list(map(int,s)) for s in D['f']],np.int32);d=np.array([list(map(int,s)) for s in D['d']],np.int32)
 print('augmentation dim 19, T/B/P fixed dimensions 0,1,3; ord_19(3)=18')
 for n in range(last+1):
  old,new,steps=check(X,Y,f,d,n);p=fix(Y,'r');xb=fix(X,'ur');yb=fix(Y,'ur')
  assert [xb.shape[1],yb.shape[1],p.shape[1]]==[1+n,2+n,14+3*n]
  bad=col(np.column_stack([f@(X['w']-I(len(X['w'])))@xb%3,(Y['w']-I(len(Y['w'])))@yb%3]))
  assert not ((Y['r']-I(len(Y['r'])))@bad%3).any() and bad.shape[1]<=3+2*n
  j=next(i for i in range(len(p.T)) if rank(np.column_stack([bad,p[:,i]]))>bad.shape[1]);beta=p[:,j]
  a=np.column_stack([pw(Y['u'],g)@beta%3 for g in range(19)])
  assert all(np.array_equal(a@m[g]%3,Y[g]@a%3) for g in 'ur')
  print('n',n,'X,Y',f.shape[1],f.shape[0],'bottom ranks',old,new,'all-cut rounds',steps,'bad/available beta dimensions',bad.shape[1],len(p.T),'chosen pivot',j,flush=True)
  if n==last:break
  oldf,oldd=f,d;XX={g:block(X[g],m[g]) for g in 'urw'};YY={g:block(Y[g],m[g]) for g in 'urw'}
  # beta=0 is a genuine dangerous extension: both copies of M form a flat pair.
  nz=19;J0=np.vstack([np.zeros((f.shape[1],nz),np.int32),I(nz)]);Z0=np.vstack([np.zeros((f.shape[0],nz),np.int32),I(nz)])
  assert np.array_equal(widen(f,a*0)@J0%3,Z0) and rank((I(len(XX['w']))-XX['w'])@J0%3)==rank((I(len(YY['w']))-YY['w'])@Z0%3)>0
  f=widen(f,a);d=np.vstack([d,np.zeros((19,1),np.int32)])
  # Local shear commutes with r, sends the new uncompressed bottom to the old one.
  bridge=(a+Y['w']@a@m['w'])%3;L=np.column_stack([I(len(Y['r'])),-2*bridge%3])
  assert np.array_equal(L@YY['r']%3,Y['r']@L%3)
  FF=(f+YY['w']@f@XX['w'])%3;F=(oldf+Y['w']@oldf@X['w'])%3
  assert np.array_equal(L@FF%3,np.column_stack([F,np.zeros_like(a)])) and np.array_equal(L@d%3,oldd)
  X,Y=XX,YY
 print('All requested finite stages and split bad-coupling controls pass. Unboundedness uses induction, not sampling.')
if __name__=='__main__':
 p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'evidence/psl2-19-explicit-matrix-input.json.zlib.b64'
 last=int(sys.argv[2]) if len(sys.argv)>2 else 3
 b=p.read_bytes();v=b if b[:1]==b'{' else zlib.decompress(base64.b64decode(b));assert hashlib.sha256(v).hexdigest()==HASH
 run(json.loads(v),last)
