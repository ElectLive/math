#!/usr/bin/env python3
"""Physical radical controls for one-size-optimal universal group hosts.
Requires numpy and the two preceding matrix/augmentation checkers in this directory."""
import sys,json,hashlib,zlib,base64,itertools
from pathlib import Path
import numpy as np
from verify_class_two_psl2_19_cubic_multiplicity import Native,make,beta,z,I,HASH
def shape(k):
 S=[(i,j) for i in range(k) for j in range(k) if i+j+2<=k];s=max(k,len(S));C=np.zeros((s,s,s),np.int32)
 if not S:C[0,0,0]=1
 for a,(i,j) in enumerate(S):
  b=S.index((i,0));C[j,a,b]=C[j,b,a]=1
 return S,C
class Spec:
 def __init__(self,k,B):
  self.S,self.C=shape(k);self.B=np.array(B,np.int32);self.om=(self.B-self.B.transpose(0,2,1))%3;self.c,self.d,_=self.B.shape
  self.e=z(19);self.e[0]=1;self.w=beta(self.e,self.e);assert self.w.any()
 def mul(self,A,B):
  x,h=A;y,k=B
  return ((x+y)%3,(h+k+np.einsum('i,sij,j->s',x,self.B,y))%3)
 def image(self,A):
  x,h=A;S=self.S;s=len(self.C);u=np.zeros((s,19),np.int32);v=np.zeros_like(u);a=np.zeros_like(u)
  for i in range(self.d):
   u[S.index((i,0))]=x[i]*self.e
   for j in range(self.c):
    for n in range(i+1,self.d):
     v[S.index((i,j))]+=x[n]*self.om[j,i,n]*self.e
  # Input uses a possibly nonsymmetric matrix-group cocycle, not BCH.
  hz=(h-2*np.einsum('i,sij,j->s',x,self.B,x))%3
  for j in range(self.c):a[j]=hz[j]*self.w
  return (u%3,v%3,a%3)
 def pr(self,U,V):
  x,y,z=U;a,b,c=V
  # Independent 20-site literal ambient computation on sparse nonzero native slots
  def twenty(u):return np.r_[u,-u.sum()%3]
  zc=z+c
  for h,i,j in zip(*np.nonzero(self.C)):
   t=twenty(x[i])*twenty(b[j])-twenty(a[i])*twenty(y[j]);zc[h]+=2*(t[:19]-2*t.sum())*self.C[h,i,j]
  return (x+a)%3,(y+b)%3,zc%3
 def body(self,N,g):
  x,y,c=self.image(g);s=len(self.C);u=z(N.n);u[N.offx:N.nx]=x.ravel();u[N.nx+N.offy:]=y.ravel();u[N.nx+119:N.nx+N.offy]=c.ravel();return u
def eq(a,b):return all(np.array_equal(x,y) for x,y in zip(a,b))
def main():
 rng=np.random.default_rng(61987);data=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'evidence/psl2-19-explicit-matrix-input.json.zlib.b64'
 b=zlib.decompress(base64.b64decode(data.read_bytes()));assert hashlib.sha256(b).hexdigest()==HASH
 s=3;S,C=shape(3);N=Native(make(json.loads(b),s),s,C)
 for d,c in ((0,3),(2,1)):
  B=np.zeros((c,d,d),np.int32)
  if d:B[0,0,1]=1;B[0,0,0]=2
  F=Spec(3,B);ele=[(np.array(a[:d],np.int32),np.array(a[d:],np.int32)) for a in itertools.product(range(3),repeat=d+c)]
  allouts=[F.body(N,e) for e in ele];assert len(set(x.tobytes() for x in allouts))==len(ele)
  nc=0
  for i,g in enumerate(ele):
   for j,h in enumerate(ele):
    r=F.body(N,F.mul(g,h));x=N.coremul(allouts[i],allouts[j]);assert np.array_equal(r,x)
    nc+=not np.array_equal(x,N.coremul(allouts[j],allouts[i]))
  print('same literal radical, d,c =',d,c,'every pair',len(ele)**2,'verified; ordered noncommuting pairs',nc,flush=True)
 # Actual signs and at least one genuine loop multiplication, not subgroup vs subloop confusion.
 print('eight native torus collision-system ranks, each augmented +1:',N.all_proj(),flush=True)
 print('fresh physical Bol products, nonlinear group/solve/sign hit counts:',N.physical(rng,8),flush=True)
 for k,d,c,n in [(5,3,2,180),(6,3,3,180),(8,5,3,80),(10,6,4,24)]:
  # In some cases the central coordinate is not necessarily the exact center; the group
  # check still tests the construction with an arbitrary declared central target.
  B=rng.integers(0,3,size=(c,d,d),dtype=np.int32);F=Spec(k,B);mixed=0
  for _ in range(n):
   g=(rng.integers(3,size=d),rng.integers(3,size=c));h=(rng.integers(3,size=d),rng.integers(3,size=c));prod=F.mul(g,h)
   assert eq(F.pr(F.image(g),F.image(h)),F.image(prod));mixed+=bool((prod[1]!=F.mul(h,g)[1]).any())
  print('actual 20-site BCH, k,d,c / input products / nonsymmetric:',k,d,c,n,mixed,flush=True)
 print('PASS: embeddings into the group radical only. Enumeration is not the uniform lower-bound proof.')
if __name__=='__main__':main()
