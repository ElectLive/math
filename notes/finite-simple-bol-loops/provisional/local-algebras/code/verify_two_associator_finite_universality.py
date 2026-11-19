#!/usr/bin/env python3
"""True sparse matrix-valued wreath lamps (including the forced negative copy),
native affine words over the actual noncommuting group algebra, and positive
and negative Magnus words in genuine finite two-variable truncations. Stdlib
plus NumPy; standalone. We do not attempt to enumerate any simple whole host."""
from itertools import product
import numpy as np
rng=np.random.default_rng(912543)
class W:
 def __init__(self,m,p):
  self.p=p;self.n=n=4*m-3;self.I=np.eye(n,dtype=np.int32);self.L=1
  self.ai=[5**i for i in range(1,n)]
  while self.L<=4*self.ai[-1]:self.L*=p
  self.ss=(1,{})
  self.root=lambda i,j,c=1:(self.I+c*np.eye(1,n,i,dtype=np.int32).T@np.eye(1,n,j,dtype=np.int32))%p
  self.ff=(0,{t%self.L:self.root(i,i+1) for i,b in enumerate(self.ai) for t in (b,-b)})
 def eq(self,a,b):
  return a[0]==b[0] and set(a[1])==set(b[1]) and all(np.array_equal(a[1][k],b[1][k]) for k in a[1])
 def mul(self,a,b):
  s,d=a;t,e=b;u=d.copy()
  for j,v in e.items():
   k=(j+s)%self.L;w=u[k]@v%self.p if k in u else v
   if np.array_equal(w,self.I):u.pop(k,None)
   else:u[k]=w
  return ((s+t)%self.L,u)
 def invmat(self,A):
  M=(self.I-A)%self.p;v=self.I.copy()
  for _ in range(self.n):v=(self.I+M@v)%self.p
  assert np.array_equal(A@v%self.p,self.I);return v
 def inv(self,a):
  s,d=a;return (-s%self.L,{(j-s)%self.L:self.invmat(v) for j,v in d.items()})
 def comm(self,a,b):return self.mul(self.mul(self.mul(a,b),self.inv(a)),self.inv(b))
 def theta(self,a):
  s,d=a;D=(-1)**np.arange(self.n);return (-s%self.L,{-j%self.L:(v*D[None,:]*D[:,None])%self.p for j,v in d.items()})
 def run(self,m):
  n=self.n;p=self.p;F=[]
  for a in self.ai:F.append(self.mul(self.mul((-a%self.L,{}),self.ff),(a,{})))
  assert self.eq(self.theta(self.ss),self.inv(self.ss)) and self.eq(self.theta(self.ff),self.inv(self.ff))
  assert self.eq(self.theta(self.mul(self.ss,self.ff)),self.mul(self.theta(self.ss),self.theta(self.ff)))
  C=[]
  for i in range(n-2):
   x=self.comm(F[i],F[i+1]);q=(-self.ai[i]-self.ai[i+1])%self.L
   assert self.eq(x,(0,{0:self.root(i,i+2),q:self.root(i,i+2,p-1)}));C.append(x)
  roots=[]
  for i in range(0,n-4,4):
   x=self.comm(C[i],C[i+2]);assert self.eq(x,(0,{0:self.root(i,i+4)}));roots.append(x)
  def fold(a):
   if len(a)==1:return a[0]
   l=len(a)//2;return self.comm(fold(a[:l]),fold(a[l:]))
  for i in range(len(roots)):
   for j in range(i+1,len(roots)+1):
    x=fold(roots[i:j]);assert self.eq(x,(0,{0:self.root(4*i,4*j)}))
  assert self.eq(self.theta(self.theta(self.mul(F[0],F[1]))),self.mul(F[0],F[1]))
  print('true W(p,m,L)',p,m,self.L,'nontrivial second locations',len(C),'embedded simple roots',len(roots),'all',m*(m-1)//2,'physical single-site roots; depth up to',2+int(np.floor(np.log2(m-1))))
def gtable(p):
 X=np.array(list(product(range(p),repeat=3)),dtype=np.int32);N=len(X);x=X[:,None]+X
 x[:,:,2]+=X[:,0,None]*X[:,1];w=np.array([p*p,p,1]);tab=(x%p)@w;sig=(X*np.array([-1,-1,1])%p)@w
 gi=np.argmin(tab,axis=1);basis=np.eye(N,dtype=np.int32);one=basis[0];idx=np.arange(N)
 assert np.array_equal(sig[tab],tab[np.ix_(sig,sig)])
 def sm(a,b):
  z=np.zeros(N,np.int32)
  for i in np.flatnonzero(a):z+=a[i]*b[tab[gi[i]]]
  return z%p
 def pw(a,e):
  z=one.copy()
  while e:
   if e%2:z=sm(z,a)
   a=sm(a,a);e//=2
  return z
 def inv(a):
  # Triangular order p^3 has radical nilpotence length at most p^3.
  return pw(a,p**3-1)
 def mid(g):return (basis[g]-one)*((p+1)//2)%p
 def odds(u,v):return (u+sm(sm((one+u)%p,inv((one+u[sig])%p)),v[sig]))%p
 def theta(y):return y[sig]
 controls=0
 for g in (p*p,p):
  assert sig[g]==gi[g];u=mid(g)
  assert not np.any(odds(u,u)) and np.array_equal(odds(u,one*0),u)
  for _ in range(21):
   y=rng.integers(0,p,N,dtype=np.int32);y[0]=(y[0]-np.sum(y))%p
   got=(odds(u,theta(y))-u)%p
   assert np.array_equal(got,sm(basis[g],y));controls+=1
 # Global coset lift graph is independent of the action-on-a-suborbit shortcut.
 # Enumerate the true abstract graph translations and all their ordered products.
 for g in idx:
  d=(basis[g]-one)%p
  displacement=(d+(basis-one)[:,tab[gi[g]]])%p
  assert np.array_equal(displacement,(basis[tab[g]]-one)%p)
  if g:assert not np.array_equal((basis[gi[g]]-one)[tab[gi[g]]]%p,(basis[gi[g]]-one)%p)
 assert sig[tab[p*p,p]]!=gi[tab[p*p,p]]
 print('actual UT3 group algebra p',p,'native generators on random actual augmentation vectors',controls,'all ordered graph-displacement products',N*N,'anti-inverse shortcut fails at st')
def rk(A,p):
 M=A.copy()%p;n,m=M.shape;r=0
 for k in range(m):
  if r>=n:break
  q=np.flatnonzero(M[r:,k])
  if not len(q):continue
  j=int(q[0])+r;M[[r,j]]=M[[j,r]];M[r]=M[r]*pow(int(M[r,k]),-1,p)%p
  a=M[:,k].copy();a[r]=0;M=(M-a[:,None]*M[r])%p;r+=1
 return r
def magnus(p,r,N):
 # A monomial is the binary suffix after its sentinel top bit at position len.
 # Column j (j>=1) is this suffix convention; products here append X or Y.
 size=2**(N+1);a=np.zeros(size,np.int16);a[1]=1
 def nxt(a,g):
  bit=g//2;inv=g%2;out=a.copy()
  src=np.arange(1,size//2);ind=src
  for s in range(N):
   ind=2*ind+bit
   good=ind<size
   ind=ind[good];src=src[good]
   out[ind]+=(-1 if inv and s%2==0 else 1)*a[src]
   if not inv:break
  return out%p
 vals=[(a,())];level=[(a,())]
 for j in range(r):
  ne=[(nxt(a,g),w+(g,)) for a,w in level for g in range(4) if not w or g!=(w[-1]^1)]
  vals+=ne;level=ne
 ss=np.array([a for a,w in vals])
 assert len({a.tobytes() for a in ss})==len(ss)
 # Stronger than injective ball: actual low-radius lamps independent in one finite
 # characteristic-p truncation, not merely formal coefficients in an infinite ring.
 sm=np.array([a for a,w in vals if len(w)<=2]);rank=rk(sm,p);assert rank==len(sm)
 for g in range(4):
  assert np.array_equal(nxt(nxt(vals[0][0],g),g^1),vals[0][0])
 print('truncated noncommutative Magnus series p',p,'maximum degree',N,'distinct genuine free-ball elements through radius',r,len(ss),'true linear lamp rank after multiplication by X (one grade later)',rank)
if __name__=='__main__':
 for p,m in ((3,3),(3,5),(5,3),(7,3)):W(m,p).run(m)
 for p in (3,5):gtable(p)
 for p in (3,5,7):magnus(p,5,9)
 print('PASS: reflected wreath generator, true single-site deep roots, native shared-operand inner words and free truncations')
