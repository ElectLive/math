#!/usr/bin/env python3
"""Genuine noncommutative doubles, physical midpoint products, and every
saturated small Heisenberg group cut (including noncentral tilted graphs).
Uses the old published base matrix only for its actual 119-coordinate shear."""
from itertools import product
from pathlib import Path
import sys,base64,hashlib,zlib,json
import numpy as np
from verify_irregular_projective_radicals import base
from verify_psl2_19_infinite_chain import HASH
rng=np.random.default_rng(943151)
def eq(x,y):return not np.any((x-y)%3)
def elt(n):return list(product(range(3),repeat=n))
class Double:
 def __init__(self,n):
  rt=[(i,j) for i in range(n) for j in range(i+1,n)];self.rs=rt;self.c=c=len(rt)+1;self.n=2*c
  self.eye=np.eye(2*c,dtype=np.int16);self.one=self.eye[0];self.soc=self.eye[c];self.terms=[]
  for i in range(c):
   for j in range(c):
    if not i:k=j
    elif not j:k=i
    elif rt[i-1][1]==rt[j-1][0]:k=rt.index((rt[i-1][0],rt[j-1][1]))+1
    else:continue
    # e_i e_j=e_k; e_j f_k=f_i and f_k e_i=f_j, in general NOT reversed.
    self.terms.extend(((i,j,k),(j,c+k,c+i),(c+k,i,c+j)))
  self.sign=np.array([1]+[(-1)**(j-i) for i,j in rt],np.int16);self.sign=np.tile(self.sign,2)
 def mul(self,x,y):
  Z=np.zeros(np.broadcast_shapes(x.shape[:-1],y.shape[:-1])+(self.n,),np.int16)
  for i,j,k in self.terms:Z[...,k]+=x[...,i]*y[...,j]
  return Z%3
 def pw(self,x,k):
  v=np.broadcast_to(self.one,x.shape).copy()
  while k:
   if k%2:v=self.mul(v,x)
   x=self.mul(x,x);k//=2
  return v
 def inv(self,x):return self.pw(x,26)
 def char(self,x):
  b=x.copy();b[...,self.c:]=0
  return np.sum(x[...,self.c:]*self.inv(b)[...,:self.c],axis=-1)%3
 def run(self,alpha):
  c=self.c;one=self.one;n=self.n
  w=np.array([19]+[-pow(j,-1,19)%19 for j in range(1,19)]+[0])
  left=np.array([j for j in range(20) if j<w[j]][:3]);right=w[left]
  def em(y):
   v=np.zeros(y.shape[:-1]+(20,n),np.int16);v[...,left,:]=y[...,None,:];v[...,right,:]=y[...,None,:]*self.sign%3;return v
  a,b,g=rng.integers(0,3,(3,200,n),dtype=np.int16);a[:,0]=b[:,0]=g[:,0]=1
  assert eq(self.mul(self.mul(a,b),g),self.mul(a,self.mul(b,g))) and eq(self.mul(a,self.inv(a)),one)
  law=self.mul(a,b);reversed=self.mul(b,a)
  neq=np.count_nonzero(np.any((law-reversed)%3,axis=1));assert neq>100
  assert eq(self.char(law),self.char(a)+self.char(b))
  badchar=np.count_nonzero((law[:,c]-a[:,c]-b[:,c])%3);assert badchar
  assert eq(self.mul(a,b)*self.sign,self.mul(a*self.sign%3,b*self.sign%3))
  # Check both one-sided socles of the actual matrix double.
  rows=self.eye[1:];M=self.mul(rows[:,None],rows)
  from verify_psl2_19_infinite_chain import rank
  assert rank(M.transpose(1,2,0).reshape(-1,n-1))==rank(M.transpose(0,2,1).reshape(-1,n-1))==n-2
  assert not self.mul(rows,self.soc).any() and not self.mul(self.soc,rows).any()
  v=np.zeros((3**(c-1),n),np.int16);v[:,1:c]=elt(c-1);q=len(v)
  lab=lambda z:z[...,1:c]@(3**np.arange(c-2,-1,-1,dtype=np.int64))
  P=em(v);unit=self.mul(P+one,self.inv(P[:,w]+one));loc=self.mul(v+one,self.inv(v*self.sign%3+one))
  assert eq(unit[:,w],self.inv(unit)) and not self.char(unit).any()
  s=self.pw(unit,14);fixed=self.mul(self.inv(s),(P-one+unit)%3);bias=self.mul(s,fixed)
  assert eq(fixed[:,w],fixed) and eq(bias+one-unit,P)
  # Noncommuting two genuine sign-inverted units whose product is not inverted.
  xx=int(lab(self.eye[self.rs.index((0,1))+1])); yy=int(lab(self.eye[self.rs.index((1,2))+1]))
  prod=self.mul(unit[xx],unit[yy]);assert not eq(prod[w],self.inv(prod))
  # Each pair still cancels in abelianization, as a product of paired units.
  # On an oriented pair their literal product is the nontrivial commutator.
  unpaired=self.mul(prod[left[0]],prod[right[0]]);assert not eq(unpaired,one)
  actualcomm=np.count_nonzero((unpaired-one)%3)
  done=0;small=np.zeros((2*q,2*q),np.int16) if q==27 else None
  for side in (0,1):
   for j in range(q):
    ids=np.arange(q) if q==27 else rng.choice(q,4,replace=False)
    A=unit[j] if side else np.broadcast_to(one,(20,n));B=bias[j] if side else P[j]
    got=B+self.mul(A,P[ids][:,w] if side else P[ids])
    ans=(v[j]+(self.mul(loc[j],v[ids]*self.sign%3) if side else v[ids]))%3
    for par in (0,1):
     rs=got-P[lab(ans)];sc=A
     if side^par:rs=rs[:,w];sc=sc[w]
     assert eq(rs,sc-one) and not np.any(alpha@self.char(sc)[:19]%3)
     if small is not None:small[side*q+j,par*q+ids]=(par^side)*q+lab(ans)
     done+=len(ids)
  if small is not None:
   t=small;k=q;ii=np.arange(2*q);assert np.array_equal(np.sort(t,axis=1),np.tile(ii,(2*q,1)))
   for j in ii:assert np.all(t[j,t[:,t[j]]]==t[t[j,t[:,j]]])
   # Principal isotope c=k,d=1. Its p-points form a genuinely nonabelian group.
   tt=t[:,np.argsort(t[k])];pi=np.where(tt[ii,tt[ii,ii]]==k)[0]
   assert len(pi)==q and np.array_equal(pi,np.arange(q,2*q))
   actual=tt[np.ix_(pi,pi)];noncomm=np.count_nonzero(actual!=actual.T);assert noncomm>0
   for j in pi:assert np.array_equal(tt[tt[j,pi,None],pi],tt[j,actual])
   print('actual 54-point Bol table and odd-left-parameter isotope: native 27-point subgroup ordered noncommuting pairs',noncomm,'versus zero in original')
  wrong=np.broadcast_to(one,(20,n)).copy();wrong[0]=(one+self.soc)%3;wrong[19]=(one-self.soc)%3
  wt=np.count_nonzero(alpha@self.char(wrong)[:19]%3);assert wt
  print('upper dimension',len(self.rs),'actual noncommuting double-unit controls',neq,'/200, false naive characters',badchar,
        'genuine sign units with nontrivial ordered pair-product coordinates',actualcomm,'native host cells',done,'wrong old shear weight',wt)
def all_cuts():
 # P = additive 3-space semidirect UT3; group element (coalgebra x, displacement y).
 # Triple x=(x12,x23,x13); Lie and ordinary coordinates must not be interchanged.
 V=np.array(elt(3),np.int16);lab=lambda x: x@np.array([9,3,1]);n=27;S=np.arange(n)
 xy=np.zeros((n,n,3),np.int16);xy[:,:,2]=V[:,0,None]*V[:,1]
 add=lab((V[:,None]+V)%3);G=lab((V[:,None]+V+xy)%3);act=lab((V[None]+xy)%3)
 gi=np.argmin(G,axis=1);sq=G[S,S];root=np.argsort(sq)
 I=np.arange(n*n);X=I//n;Y=I%n
 T=G[X[:,None],X]*n+add[Y[:,None],act[X[:,None],Y]]
 pinv=np.argmin(T,axis=1);Vneg=lab((-V)%3);ZP=X*n+Vneg[Y]
 def subs(table):
  ss={frozenset([0])};queue=list(ss)
  for v in queue:
   for h in S:
    if h in v:continue
    got=set(v)|{int(h)};old=-1
    while len(got)!=old:
     old=len(got);a=np.array(list(got));got.update(map(int,table[np.ix_(a,a)].flatten()))
    f=frozenset(got)
    if f not in ss:ss.add(f);queue.append(f)
  return sorted(ss,key=lambda t:(len(t),sorted(t)))
 js=subs(G);us=subs(add);assert len(js)==19 and len(us)==28
 gens=[v*n for v in (9,3,1)]+[9,3,1];conj=T[T[gens],pinv[gens,None]]
 counts=[];noncentr=[];flag=0;tilt=0;allcases=0
 for signs in ((2,2,1),(2,1,2),(1,2,2)):
  si=lab((V*np.array(signs))%3);ip=si[X]*n+si[Y]
  neg=S[si==gi];pos=S[si==S]
  mids=(neg[:,None]*n+act[root[neg,None],pos]).flatten()
  # Twist conjugating origin in full *nonabelian* P: z(p) i(p^-1).
  orbit=set(T[ZP,ip[pinv]].tolist())
  assert orbit==set(mids.tolist())
  if np.any(~np.isin(G[np.ix_(neg,neg)],neg)):flag+=1
  single=0;nc=0
  for J in js:
   if not all(si[j] in J for j in J):continue
   for U in us:
    if not all(si[u] in U for u in U):continue
    j,u=np.array(sorted(J)),np.array(sorted(U));ids=(j[:,None]*n+add[np.ix_(j,u)]).flatten()
    inside=np.zeros(n*n,bool);inside[ids]=True
    if not np.all(inside[conj[:,ids]]) or not np.all(inside[ip[ids]]):continue
    if not np.all(inside[T[np.ix_(ids,ids)]]):continue
    # D(j)=j as an additive vector, but J is under the genuine UT3 product.
    J1=set(J)&set(U);expect=len(set(neg)&J1)*len(set(pos)&set(U))
    fibers=inside[T[np.ix_(pinv[mids],mids)]].sum(axis=1)
    assert np.all(fibers==expect)
    single+=1;allcases+=1
    if not np.all(inside[ZP[ids]]):tilt+=1
    if len(J)==27 and len(U)<27:
     # Is R/U central? Compare actual commutators, including their plus projection.
     comm=T[conj[:,ids],pinv[ids]]
     if np.any(comm//n):nc+=1
  counts.append(single);noncentr.append(nc)
 assert flag and tilt and min(noncentr)>0
 print('actual Heisenberg affine control',[(len(js),len(us))], 'saturated normal cuts by sign',counts,'of which not z-stable (aggregate)',tilt,
       'noncentral R/U with genuinely nonabelian J by sign',noncentr,'nonclosed inverted sets',flag,'all true fibers equal predicted',allcases)
def rootcopy(m):
 n=2*m-1;idn=np.eye(n,dtype=np.int16);rt=[(i,j) for i in range(m) for j in range(i+1,m)]
 def em(a):
  z=np.broadcast_to(idn,a.shape[:-1]+(n,n)).copy()
  for h,(i,j) in enumerate(rt):z[...,2*i,2*j]=a[...,h]
  return z
 for i,j in rt:
  a=idn.copy();b=idn.copy();c=idn.copy();d=idn.copy();s=2*i+1
  a[2*i,s]=b[s,2*j]=1;c[2*i,s]=d[s,2*j]=2
  t=idn.copy();t[2*i,2*j]=1;assert eq(a@b@c@d,t)
 if m<=4:
  words=np.array(elt(len(rt)),np.int16);z=em(words);base=z[:,::2,::2]
  count=0
  for j in range(len(z)):
   ab=base[j]@base%3;coords=np.stack([ab[:,i,k] for i,k in rt],axis=-1)
   assert eq(z[j]@z,em(coords));count+=len(z)
 else:count=0
 print('UT dimension',m,'true commutator elementary roots in the single-site larger derived group',len(rt),'actual products',count)
if __name__=='__main__':
 raw=zlib.decompress(base64.b64decode(Path(sys.argv[1]).read_bytes()));assert hashlib.sha256(raw).hexdigest()==HASH
 *_,alpha=base(json.loads(raw));all_cuts()
 for n in (3,4):Double(n).run(alpha)
 for m in (3,4,9,17):rootcopy(m)
 print('PASS: noncommutative units, saturated nonsign-stable cuts, both native sheets and single-site radical groups')
