#!/usr/bin/env python3
"""Independent-of-squarefree implementation of the one-variable, p-power unit host.
No finite group recognition or generic order bound is used for the actual point orbit.
"""
import sys,json,zlib,base64,hashlib
from pathlib import Path
import numpy as np
from verify_psl2_19_infinite_chain import HASH
from verify_irregular_projective_radicals import base
rng=np.random.default_rng(7011066)
def eq(a,b):return np.array_equal(a,b)
def ih(a):return (-a)%3
def me(a):return (a-int(a.sum())*2)%3
class U:
 def __init__(self,N):
  self.N=N;self.zero=np.zeros((N+1,20),np.int32);self.unit=self.zero.copy();self.unit[0]=1;self.js=[j for j in range(1,N+1) if j%3];self.m={}
  for j in self.js:
   b=1
   while j*b<=N:b*=3
   self.m[j]=b
 def mul(self,a,b):
  n=self.N;c=self.zero.copy()
  for i in range(n+1):
   if a[i].any():c[i:]+=a[i]*b[:n-i+1]
  c%=3;c[-1]=me(c[-1]);return c
 def power(self,a,k):
  b=self.unit.copy()
  while k:
   if k&1:b=self.mul(b,a)
   a=self.mul(a,a);k//=2
  return b
 def inv(self,a):return self.power(a,self.m[1]-1)
 def coords(self,a):
  assert eq(a[0],self.unit[0]);acc=self.unit.copy();e={j:np.zeros(20,np.int32) for j in self.js}
  for j in range(1,self.N+1):
   q=(a[j]-acc[j])%3;f=self.unit.copy();f[j]=q
   if 2*j<=self.N:f[2*j]=(q==2).astype(np.int32)
   if j==self.N:f[j]=me(f[j]);
   acc=self.mul(acc,f);t=j;b=1
   while not t%3:t//=3;b*=3
   e[t]+=b*q
  assert eq(acc,a);return e
 def fromcoords(self,e):
  acc=self.unit.copy();n=self.N
  for j,q in e.items():
   assert ((0<=q)&(q<self.m[j])).all()
   d=1
   while j*d<=n:
    v=j*d
    k=(q//d)%3;f=self.unit.copy();f[v]=k
    if v*2<=n:f[2*v]=(k==2)
    if v==n:f[v]=me(f[v])
    acc=self.mul(acc,f);d*=3
  return acc
 def randA(self):
  e={j:rng.integers(0,b,20,dtype=np.int32) for j,b in self.m.items()}
  for j,b in self.m.items():e[j][-1]=(int(e[j][-1])-int(e[j].sum()))%b
  return self.fromcoords(e)
 def randI(self):
  x=rng.integers(0,3,self.zero.shape,dtype=np.int32);x[0]=0;x[1]=me(x[1]);x[-1]=me(x[-1]);return x
 def gprod(self,g,h):
  x,y=g;u,v=h;return self.mul(x,u),(y+self.mul(x,v))%3
 def graph(self,s):return s,(s-self.unit)%3
 def native(self,g):return (g[1]-g[0]+self.unit)%3
 def geq(self,g,h):return eq(g[0],h[0]) and eq(g[1],h[1])
 def gf(self,g):x,y=g;r=self.inv(x);return r,self.mul(r,-y)
 def invert_site(self,s,p):return s[:,p]

def trial(N,B,randoms):
 R=U(N);power=R.m[1];ww=np.array([19]+[-pow(i,-1,19)%19 for i in range(1,19)]+[0]);z=R.zero;o=R.unit
 def af(sign,x):return x[:,ww] if sign else x
 def gp(g,h):x,y,i=g;a,b,j=h;u,v=R.gprod((x,y),(af(i,a),af(i,b)));return u,v,i^j
 def ep(g,h):return g[-1]==h[-1] and R.geq(g[:2],h[:2])
 e={j:np.zeros(20,np.int32) for j in R.js};e[1][0]=1;e[1][19]=power-1;s=R.fromcoords(e);assert eq(R.inv(s),s[:,ww]);assert all(eq(R.coords(s)[j],e[j]) for j in R.js)
 h=(s,z,1);k=(o,z,1);one=(o,z,0);assert ep(gp(h,h),one) and ep(gp(k,k),one)
 hk=gp(h,k);yy=R.native(hk[:2]);assert eq(yy,(o-s)%3) and np.any(yy)
 aa=gp((o,-yy%3,0),hk);assert R.geq(aa[:2],R.graph(s)) and not aa[2];assert ep(gp((o,yy,0),aa),hk)
 # Actual orbit of the native product under the genuine stabilizer; it never leaves the vertical abelian subloop.
 orbit=[];v=yy
 for j in range(power):
  orbit.append(v.tobytes());g=gp(aa,(o,v,0));v1=R.native(g[:2]);assert eq(v1,R.mul(s,v));v=v1
 assert len(set(orbit))==power and eq(v,yy)
 # The successive (alpha-1) differences in the true group of vertical points have leading degrees 1,...,N, then vanish.
 u=yy;lead=[]
 while u.any():
  d=next(i for i in range(1,N+1) if u[i].any());lead.append(d);u=(R.mul(s,u)-u)%3
 assert lead==list(range(1,N+1))
 # Recompute native grade equation from the polynomial itself: on reflected i it is (1+v)/(1+i v), not the elementary exponent-three formula x/2=2x.
 ctr=0;wrong_half=0;wrong_raw_top=0
 for _ in range(randoms):
  x=R.randA();q=R.randA();y=R.randI();r=R.randI(); ex=R.coords(x);eq0=R.coords(q);epq=R.coords(R.mul(x,q));top=B[4]
  assert all(eq((ex[j]+eq0[j])%R.m[j],epq[j]) for j in R.js)
  wrong_raw_top+=not eq(top@((x[-1]+q[-1])%3)[:19]%3,top@(R.mul(x,q)[-1,:19])%3)
  assert R.geq(R.gprod(R.graph(x),R.graph(q)),R.graph(R.mul(x,q)))
  signs=[ww,np.roll(np.arange(20),0)];p=signs[_%2];b=R.mul(o+y,R.inv((o+y)[:,p]));bcoord=R.coords(b)
  assert all(not int(v.sum())%R.m[j] for j,v in bcoord.items());assert eq(b[:,p],R.inv(b));half=R.power(b,(power+1)//2);assert eq(R.mul(half,half),b)
  wrong_half+=not eq(R.mul(b,b),half);vFixed=R.mul(R.inv(half),(y+b-o)%3);assert eq(vFixed[:,p],vFixed)
  # Undo an arbitrary H graph on the right, reconstruct its genuine ring mark, and compare the full standard group word.
  mark=(b,R.mul(half,vFixed));src=R.gprod(mark,R.graph(q));assert eq(R.native(src),y);assert eq(R.native(mark),y)
  signinv=R.gf(mark);actual=(b[:,p],(-mark[1][:,p])%3);assert R.geq(signinv,actual);ctr+=1
 assert wrong_raw_top>0 and (power<=3 or wrong_half>0)
 print('N',N,'host exponent log_3(|Q|/20)',117+20*N,'two true involutions / product site',2,3,'LhLk and actual associator orbit',power,'independent native ternary Jordan coordinates',len(lead),'non-elementary sign-fiber factorizations',ctr,'false raw-top / false half = 2x numerical controls',wrong_raw_top,wrong_half,flush=True)
if __name__=='__main__':
 path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'evidence/psl2-19-explicit-matrix-input.json.zlib.b64';raw=zlib.decompress(base64.b64decode(path.read_bytes()));assert hashlib.sha256(raw).hexdigest()==HASH;B=base(json.loads(raw))
 for n,k in [(2,18),(4,18),(10,16),(28,12),(82,6)]:trial(n,B,k)
 print('PASS: native product orbit 3,9,27,81,243 and growing single Jordan chain, not an independent proof of simplicity.')
