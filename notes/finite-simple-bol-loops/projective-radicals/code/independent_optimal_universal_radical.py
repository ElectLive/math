#!/usr/bin/env python3
"""BLAS/NumPy eager finite check, independent of the author's module/model checker."""
import itertools as it
import numpy as np
from fractions import Fraction
from math import comb

def base(k):
 names=[(i,j) for j in range(1,k+1) for i in range(1,k+1-j)];s=max(k,len(names));out=np.zeros((s,s,s),np.int16)
 for b,(i,j) in enumerate(names):
  a=names.index((i,1));out[j-1,a,b]=out[j-1,b,a]=1
 if not names:out[0,0,0]=1
 return names,out

def beta(a,b):
 ab=a*b;return (ab-2*sum(ab))%3

def main():
 e=np.zeros(20,dtype=np.int16);e[7]=1;e[16]=2;w=beta(e,e);assert np.count_nonzero(w)==18 and sum(w)%3==0
 S,A=base(6);s=len(A);v=np.array(list(it.product(range(3),repeat=6)),dtype=np.int16);d=v[:,:4];zz=v[:,4:];assert len(S)==s==15
 for name,M,expected in [('split',[[0,0],[0,1]],2),('nonsplit',[[0,-1],[1,0]],0)]:
  mats=np.array([np.eye(2,dtype=np.int16),M],dtype=np.int16);I,J=np.indices((len(v),len(v)));qform=np.einsum('ni,hij,nj->nh',d[:,:2],mats,d[:,2:])%3
  z=(zz-2*qform)%3
  xy=np.zeros((len(v),2,s),np.int16);om=np.zeros((2,4,4),dtype=np.int16);om[:,:2,2:]=mats;om[:,2:,:2]=-mats.transpose(0,2,1)
  for j in range(4):
   xy[:,0,S.index((j+1,1))]=d[:,j]
   for i in range(j):
    for hh in range(2):xy[:,1,S.index((i+1,hh+1))]+=d[:,j]*om[hh,i,j]
  xy%=3
  # 81 actual noncentral cosets; all 729 images discriminated by native active-plus and passive- records.
  assert len({(tuple(x.ravel()),tuple(a)) for x,a in zip(xy,z)})==729
  cval=np.stack([d[:,:2]@a@d[:,2:].T%3 for a in mats],axis=2);br=(cval-cval.transpose(1,0,2))%3
  truecenter=np.where(~br.any(axis=(1,2)))[0];assert len(truecenter)==9 and not xy[truecenter].any()
  for l,a in enumerate(A):
   cv=(xy[:,0,:]@a@xy[:,1,:].T)%3;cv=(cv-cv.T)%3
   if l>=2:assert not cv.any() # other actual passive output slots and all old base coordinates remain zero
   else:
    assert np.array_equal(cv,br[:,:,l]);pr=(z[I,l]+z[J,l]+2*cv)%3
    sm=(d[I]+d[J])%3;zl=(zz[I,l]+zz[J,l]+cval[:,:,l]-2*np.einsum('mni,ij,mnj->mn',sm[:,:,:2],mats[l],sm[:,:,2:]))%3
    for b in w:assert np.array_equal((pr*b)%3,(zl*b)%3)
  rr=[]
  for a,b in [(1,0),(1,1),(1,2),(0,1)]:
   m=(a*mats[0]+b*mats[1])%3;rr.append(not (int(m[0,0])*int(m[1,1])-int(m[0,1])*int(m[1,0]))%3)
  assert sum(rr)==expected;print(name,'all',len(v)**2,'true image laws on all 20 physical output coordinates; center',len(truecenter),'singular projective alternating pencils',sum(rr))
 assert base(1)[1][0,0,0]==1
 for t in range(2,130):
  h=comb(2*t,2); assert (t-1)*(h-1)-5*t*t==2*t**3-8*t*t+1
 print('same k=6 native coefficient tensor for both nonisomorphic order-729 groups; exact lower exponent identity at t=2..129')
if __name__=='__main__':main()
