#!/usr/bin/env python3
"""Three actual ternary coefficient rings, twenty projective sites and native coset
products. Import only the audited base-matrix controls from the neighboring code.
Usage: python verify_general_local_algebra_hosts.py matrix-data.json.zlib.b64
Does not enumerate a huge simple host or replace the uniform normal-cut proof."""
import sys,base64,zlib,hashlib,json
from pathlib import Path
from itertools import product
import numpy as np
from verify_irregular_projective_radicals import base
from verify_psl2_19_infinite_chain import HASH,rank
rng=np.random.default_rng(6319431)
def eq(x,y): return np.array_equal((x-y)%3,np.zeros_like(x-y))
class Ring:
 def __init__(self,mons,images):
  self.mon=mons;self.c=c=len(mons);self.n=2*c;self.eye=np.eye(2*c,dtype=np.int16);self.one=self.eye[0];self.soc=self.eye[c]
  self.terms=[]
  for i,a in enumerate(mons):
   for j,b in enumerate(mons):
    k=tuple(x+y for x,y in zip(a,b))
    if k in mons:
     k=mons.index(k);self.terms.extend([(i,j,k),(i,c+k,c+j),(c+k,i,c+j)])
  # Basis action is given only on C; no involution on the dual extension is used.
  self.sg=np.asarray(images,dtype=np.int16);assert eq(self.sg@self.sg,np.eye(c,dtype=np.int16))
 def mul(self,x,y):
  z=np.zeros(np.broadcast_shapes(x.shape[:-1],y.shape[:-1])+(self.n,),np.int16)
  for i,j,k in self.terms:z[...,k]+=x[...,i]*y[...,j]
  return z%3
 def pw(self,x,k):
  v=np.broadcast_to(self.one,x.shape).copy()
  while k:
   if k&1:v=self.mul(v,x)
   x=self.mul(x,x);k//=2
  return v
 def inv(self,x):return self.pw(x,26)
 def char(self,x):
  b=x.copy();b[...,self.c:]=0;ell=x.copy();ell[...,:self.c]=0
  return self.mul(self.inv(b),ell)[...,self.c]
 def sig(self,y):
  z=np.zeros_like(y);z[...,:self.c]=y[...,:self.c]@self.sg%3;return z
 def rand(self,shape,unit=True):
  a=rng.integers(0,3,shape+(self.n,),dtype=np.int16);a[...,0]=int(unit);return a
 def ring_tests(self):
  n=self.n;Z=self.eye[1:];T=self.mul(Z[:,None],Z)
  n2=rank(T.reshape(-1,n));h=(n-1)-n2
  assert (n-1)-rank(T.transpose(1,2,0).reshape(-1,n-1))==1 and not self.mul(self.soc,Z).any()
  socdimC=self.c-rank(self.mul(self.eye[1:self.c,None],self.eye[:self.c]).transpose(0,2,1).reshape(-1,self.c))
  assert h==(self.c-1-rank(self.mul(self.eye[1:self.c,None],self.eye[1:self.c]).reshape(-1,n)))+socdimC
  x=self.rand((260,));y=self.rand((260,));z=self.rand((260,))
  assert eq(self.mul(self.mul(x,y),z),self.mul(x,self.mul(y,z)))
  assert eq(self.mul(self.inv(x),x),self.one)
  assert eq(self.char(self.mul(x,y)),(self.char(x)+self.char(y))%3)
  wrong=np.count_nonzero((self.mul(x,y)[:,self.c]-x[:,self.c]-y[:,self.c])%3)
  assert wrong>0
  # Compute all products of length k in the radical basis until its actual socle.
  words=[self.one[None]];L=0
  while True:
   nxt=np.unique(self.mul(words[-1][:,None],Z).reshape(-1,n),axis=0)
   nxt=nxt[np.any(nxt,axis=1)]
   if not len(nxt):break
   words.append(nxt);L+=1
  assert L>=2 and rank(words[-1])==1 and not np.delete(words[-1],self.c,axis=1).any()
  U=np.zeros((3**(n-1),n),np.int16);U[:,1:]=np.asarray(list(product(range(3),repeat=n-1)),dtype=np.int16)
  # Each actual nonzero radical element reaches the real one-dimensional socle;
  # this includes mixtures of degrees, and x,y-rings with larger old socle.
  unresolved=np.any(U,axis=1).copy()
  for ww in reversed(words):
   for v in ww:
    vals=self.mul(U,v)
    reached=(vals[:,self.c]!=0)&(~np.any(np.delete(vals,self.c,axis=1),axis=1))
    unresolved &= ~reached
  assert not unresolved.any()
  return h,socdimC,L,wrong,len(U)-1
 def native(self,alpha):
  # Genuine projective Weyl permutation; choose the first three of its ten pairs.
  w=np.array([19]+[-pow(j,-1,19)%19 for j in range(1,19)]+[0])
  left=np.array([i for i in range(20) if i<w[i]][:3]);right=w[left]
  def emb(y):
   v=np.zeros(y.shape[:-1]+(20,self.n),np.int16)
   v[...,left,:]=y[...,None,:];v[...,right,:]=self.sig(y)[...,None,:];return v
  def mag(x):return np.sum(x[...,1:self.c]*(3**np.arange(self.c-2,-1,-1)),axis=-1)
  v=np.zeros((3**(self.c-1),self.n),np.int16)
  v[:,1:self.c]=list(product(range(3),repeat=self.c-1));assert eq(mag(v),np.arange(len(v)))
  p=emb(v);q=len(v);assert not (p.sum(axis=1)%3).any()
  assert eq(p[:,w],emb(self.sig(v))) and eq(self.mul(p[:,None],p[None]),emb(self.mul(v[:,None],v[None])))
  assert eq(self.mul(self.sig(v[:,None]),self.sig(v)),self.sig(self.mul(v[:,None],v)))
  a=self.mul(p+self.one,self.inv(p[:,w]+self.one))
  assert eq(a[:,w],self.inv(a)) and not self.char(a).any()
  b=self.pw(a,14);assert eq(self.mul(b,b),a)
  fixed=self.mul(self.inv(b),(p-self.one+a)%3); assert eq(fixed[:,w],fixed)
  offs=self.mul(b,fixed);assert eq(offs+self.one-a,p)
  asmall=self.mul(v+self.one,self.inv(self.sig(v)+self.one));done=0
  for sx in (0,1):
   for i in range(q):
    unit=a[i] if sx else np.broadcast_to(self.one,a[i].shape)
    true=(offs[i] if sx else p[i])+self.mul(unit,(p[:,w] if sx else p))
    ordinary=(v[i]+(self.mul(asmall[i],self.sig(v)) if sx else v))%3
    diff=(true-p[mag(ordinary)])%3
    for sy in (0,1):
     target=sx^sy;res=diff[:,w] if target else diff;actual=unit[w] if target else unit
     assert eq(res,actual-self.one)
     assert not (alpha@self.char(actual)[:19]%3).any()
     done+=q
  assert done==(2*q)**2
  # An involutory signed unit with deliberately nonzero top shear.
  bad=np.broadcast_to(self.one,(20,self.n)).copy()
  bad[0]=(bad[0]+self.soc)%3;bad[19]=(bad[19]-self.soc)%3
  assert eq(bad[w],self.inv(bad))
  weight=np.count_nonzero(alpha@self.char(bad)[:19]%3);assert weight
  # Almost-socle, multi-site vectors, actual true principal-unit differences.
  uu=self.rand((20,));uu[0]=self.one
  for k in range(1,20):uu[0]=self.mul(uu[0],self.inv(uu[k]))
  ap=self.one.copy()
  for s in uu:ap=self.mul(ap,s)
  assert eq(ap,self.one) and np.sum(self.char(uu))%3==0
  for _ in range(90):
   x,y=self.rand((),False),self.rand((),False)
   u=np.broadcast_to(self.one,(20,self.n)).copy();u[0]+=x;u[1]=self.inv(u[0])
   h=np.zeros_like(u);h[0]=y;h[2]=(-y)%3
   got=self.mul(u-self.one,h)
   assert eq(got[0],self.mul(x,y)) and not got[1:].any()
  # If only one pair were used, some first-grade traces may be prohibited.
  n2=self.mul(self.eye[1:,None],self.eye[1:]).reshape(-1,self.n)
  wrongpair=sum(rank(np.vstack([n2,u+self.sig(u)]))>rank(n2) for u in v)
  return done,weight,wrongpair
def run(label,mons,sg,alpha):
 R=Ring(mons,sg);h,cs,L,wrong,ex=R.ring_tests();done,weight,pairs=R.native(alpha)
 print(label,'dim V',R.c-1,'original socle',cs,'double Loewy last grade',L,'dim N/N^2',h,
       'nonzero radical inputs driven to socle',ex,'bad naive characters',wrong,'of 260','native host cells',done,
       'actual wrong graph 119-vector weight',weight,'single-pair rejected entries',pairs)
 return pairs
if __name__=='__main__':
 raw=zlib.decompress(base64.b64decode(Path(sys.argv[1]).read_bytes()));assert hashlib.sha256(raw).hexdigest()==HASH
 *_,alpha=base(json.loads(raw))
 run('non-Gorenstein x^2=xy=y^3=0, nonlinear sign',[(0,0),(1,0),(0,1),(0,2)],[[1,0,0,0],[0,-1,0,1],[0,0,-1,0],[0,0,0,1]],alpha)
 assert run('x^2=y^2=0, exchange generators',[(0,0),(1,0),(0,1),(1,1)],[[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]],alpha)>0
 run('t^5=0, invert 1+t',[(k,) for k in range(5)],[[1,0,0,0,0],[0,-1,1,-1,1],[0,0,1,-2,3],[0,0,0,-1,3],[0,0,0,0,1]],alpha)
 print('PASS: actual ternary trivial extensions, norm units, protected 3-Weyl-pair embedding, both native sheets')
