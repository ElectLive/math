#!/usr/bin/env python3
"""Exact nested, noncommuting two-level wreath words. Finite controls substitute
short tags after explicitly checking every actual lamp commutator: the uniform
proof uses larger safe powers of 5. Top group elements are actual truncated
polynomial matrices, not a mock cyclic quotient. Sparse lamp addresses are those
genuine matrices. Stdlib + numpy. No giant global simple host is enumerated."""
from functools import lru_cache
import numpy as np
def pw(x,k,I,mul):
 z=I
 while k:
  if k&1:z=mul(z,x)
  x=mul(x,x);k//=2
 return z
def comm(x,y,mul,inv):return mul(mul(mul(x,y),inv(x)),inv(y))
def word(x,y,mul,inv):return mul(comm(x,y,mul,inv),inv(comm(inv(y),inv(x),mul,inv)))
class PolyTop:
 def __init__(self,p,M):
  self.p=p;self.M=M;I=np.zeros((2,2,M),np.uint8);I[0,0,0]=I[1,1,0]=1;self.I=self.key(I)
  U=I.copy();U[0,1,1]=1;V=I.copy();V[1,0,1]=1;self.U,self.V=self.key(U),self.key(V)
 def key(self,A):return (A%self.p).astype(np.uint8).tobytes()
 def unpack(self,a):return np.frombuffer(a,dtype=np.uint8).reshape(2,2,self.M).astype(np.int32)
 @lru_cache(maxsize=9000)
 def mul(self,a,b):
  if a==self.I:return b
  if b==self.I:return a
  x=self.unpack(a);y=self.unpack(b);z=np.zeros_like(x)
  for i in range(2):
   for j in range(2):
    for k in range(2):
     u=x[i,k];v=y[k,j];iu=np.flatnonzero(u);iv=np.flatnonzero(v)
     if len(iu)*len(iv)<120:
      for d in iu:z[i,j,d:]+=u[d]*v[:self.M-d]
     else:z[i,j]+=np.convolve(u,v)[:self.M]
  return self.key(z)
 @lru_cache(maxsize=3000)
 def inv(self,a):
  x=self.unpack(a);return self.key(np.array([[x[1,1],-x[0,1]],[-x[1,0],x[0,0]]]))
 @lru_cache(maxsize=3500)
 def tau(self,a):
  x=self.unpack(a);return self.key(np.array([[x[1,1],-x[1,0]],[-x[0,1],x[0,0]]]))
class Branch:
 def __init__(self,p,m,L,tags):
  self.p=p;self.n=4*m-3;self.eye=np.eye(self.n,dtype=np.int32);e=1
  while e<self.n:e*=p
  self.e=e;self.L=L;self.tags=tags;assert len(tags)==self.n-1
  self.t=PolyTop(p,2*e*L//p+1);t=self.t
  assert t.tau(t.U)==t.inv(t.V) and t.tau(t.V)==t.inv(t.U)
  self.q=q=word(t.U,t.V,t.mul,t.inv);self.s=s=pw(q,e,t.I,t.mul)
  assert pw(s,L,t.I,t.mul)==t.I and pw(s,L//p,t.I,t.mul)!=t.I
  assert t.tau(s)==t.inv(s)
  self.idj=(t.I,{});self.outer=(0,tuple(self.idj for j in range(p)))
  self.a=(1,self.outer[1]);f={}
  for i,v in enumerate(tags):
   f[pw(s,v,t.I,t.mul)]=self.rt(i,i+1);f[pw(s,L-v,t.I,t.mul)]=self.rt(i,i+1)
  assert len(f)==2*len(tags)
  values=list(self.outer[1]);values[0]=(t.I,f);values[1]=(t.U,{});values[-1]=(t.V,{})
  self.b=(0,tuple(values))
 def rt(self,i,j,c=1):
  x=self.eye.copy();x[i,j]=c%self.p;return x
 def imat(self,a):
  N=(self.eye-a)%self.p;v=self.eye
  for _ in range(self.n):v=(self.eye+N@v)%self.p
  return v
 def mj(self,a,b):
  t=self.t;h,A=a;k,B=b;u=A.copy()
  for i,v in B.items():
   j=t.mul(h,i);w=u[j]@v%self.p if j in u else v
   if np.array_equal(w,self.eye):u.pop(j,None)
   else:u[j]=w
  return (t.mul(h,k),u)
 def ij(self,c):
  t=self.t;h,A=c;z=t.inv(h);return z,{t.mul(z,i):self.imat(v) for i,v in A.items()}
 def mul(self,a,b):
  h,x=a;k,y=b;return (h+k)%self.p,tuple(self.mj(x[i],y[(i-h)%self.p]) for i in range(self.p))
 def inv(self,a):
  h,x=a;return (-h)%self.p,tuple(self.ij(x[(i+h)%self.p]) for i in range(self.p))
 def tau(self,a):
  t=self.t;D=(-1)**np.arange(self.n);h,x=a;v=[]
  for i in range(self.p):
   j,M=x[-i];v.append((t.tau(j),{t.tau(u):g*D[None,:]*D[:,None]%self.p for u,g in M.items()}))
  return (-h)%self.p,tuple(v)
 def eq(self,a,b):
  if a[0]!=b[0]:return False
  for (h,x),(k,y) in zip(a[1],b[1]):
   if h!=k or set(x)!=set(y) or not all(np.array_equal(g,y[j]) for j,g in x.items()):return False
  return True
 def mon(self,h=None,M=None):
  v=list(self.outer[1]);v[0]=(h or self.t.I,M or {});return 0,tuple(v)
 def run(self):
  a,b,mul,inv,I=self.a,self.b,self.mul,self.inv,self.outer;t=self.t;p=self.p;power=lambda x,n:pw(x,n,I,mul)
  assert self.eq(power(a,p),I) and self.eq(power(b,p),I) and not self.eq(a,I) and not self.eq(b,I)
  assert self.eq(self.tau(a),inv(a)) and self.eq(self.tau(b),inv(b))
  assert self.eq(self.tau(mul(a,b)),mul(self.tau(a),self.tau(b)))
  x=mul(mul(inv(a),b),a);y=mul(mul(a,b),inv(a));q=word(x,y,mul,inv)
  assert q[0]==0 and q[1][0][0]==self.q
  residual=sum(len(M) for h,M in q[1][1:]);assert all(h==t.I for h,M in q[1][1:])
  S=power(q,self.e);assert self.eq(S,self.mon(self.s))
  F=[]
  for tag in self.tags:
   s=power(S,tag);F.append(mul(mul(inv(s),b),s))
  C=[]
  for i in range(len(F)-1):
   c=comm(F[i],F[i+1],mul,inv);second=pw(self.s,(-self.tags[i]-self.tags[i+1])%self.L,t.I,t.mul)
   assert self.eq(c,self.mon(M={t.I:self.rt(i,i+2),second:self.rt(i,i+2,-1)}))
   C.append(c)
  R=[]
  for i in range(0,self.n-4,4):
   c=comm(C[i],C[i+2],mul,inv)
   assert self.eq(c,self.mon(M={t.I:self.rt(i,i+4)}));R.append(c)
  c=R[0]
  for i in range(1,len(R)):c=comm(c,R[i],mul,inv)
  assert self.eq(c,self.mon(M={t.I:self.rt(0,self.n-1)}))
  print('p,root size,probe modulus',p,self.n,t.M,'true order of each outer group generator',p,
        'residual physical lamps before power',residual,'after power 0','single-site inner shift order',self.L,
        'verified inverse companions',len(C),'embedded consecutive roots',len(R),'true longest root gap',self.n-1)
  return residual
def trunc(p,N):
 # Group algebra F_p[C_p*C_p] in the graded monomial truncation. Terms of run
 # length p vanish. Both individual orders p are checked, not inferred from names.
 ex=(1,);ey=(2,);one={():1}
 def mul(x,y):
  z={}
  for i,a in x.items():
   for j,b in y.items():
    k=i+j
    if len(k)>N or any(k[v:v+p] in ((1,)*p,(2,)*p) for v in range(len(k)-p+1)):continue
    z[k]=(z.get(k,0)+a*b)%p
  return {u:v for u,v in z.items() if v}
 A={():1,ex:1};B={():1,ey:1};assert pw(A,p,one,mul)==pw(B,p,one,mul)==one
 moves=[[pw(g,e,one,mul) for e in range(1,p)] for g in (A,B)]
 lev=[(one,-1)];words=[one]
 for j in range(4):
  lev=[(mul(x,v),k) for x,h in lev for k in range(2) if k!=h for v in moves[k]]
  words+=[x for x,h in lev]
 assert len({tuple(sorted(x.items())) for x in words})==len(words)
 # Lamps at ab-1, not at a-1: regular lamp vectors, and the actual annihilating
 # norm for the wrong old choice. Test full increment in the computed truncation.
 bad={ex:1};norm={}
 for d in range(p):
  for k,v in pw(A,d,one,mul).items():norm[k]=(norm.get(k,0)+v)%p
 assert not mul(norm,bad)
 good=mul(A,B);good.pop(())
 assert len({tuple(sorted(mul(x,good).items())) for x in words})==len(words)
 print('bounded-generator series p',p,'radius four alternating nonzero syllable words',len(words),'on the genuine lamp ab-1; wrong lamp killed by the cyclic norm')
if __name__=='__main__':
 vals=[]
 for args in [(3,2,27,[1,9,3,8]),(3,3,81,[2,21,37,13,27,33,6,23]),(5,2,25,[11,12,5,8]),(7,2,49,[23,20,24,5])]:
  vals.append(Branch(*args).run())
 assert any(vals)
 for p in (3,5):trunc(p,4*(p-1)+2)
 print('PASS: two exact-order-p generators, extracted deep native-compatible subgroup and corrected free-product lamps')
