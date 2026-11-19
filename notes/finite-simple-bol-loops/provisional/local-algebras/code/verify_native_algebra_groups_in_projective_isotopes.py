#!/usr/bin/env python3
"""Direct physical residuals on the two noncommuting matrix limbs in three Weyl
pairs. The old passive coordinate vanishes identically on pure algebra units,
as checked against the actual matrix data in the immediately preceding checker."""
import numpy as np
from itertools import product
def eq(a,b):return not np.any((a-b)%3)
def pw(a,p):
 eye=np.eye(a.shape[-1],dtype=np.int16);b=np.broadcast_to(eye,a.shape).copy()
 while p:
  if p%2:b=b@a%3
  a=a@a%3;p//=2
 return b
def run(n):
 I=np.eye(n,dtype=np.int16);rt=[(i,j) for i in range(n) for j in range(i+1,n)];d=len(rt);q=3**d
 xs=np.zeros((q,n,n),np.int16);vals=np.array(list(product(range(3),repeat=d)),np.int16)
 for k,(i,j) in enumerate(rt):xs[:,i,j]=vals[:,k]
 gs=xs+I;inv=pw(gs,26);hal=pw(gs,14);hi=pw(inv,14)
 assert eq(gs@inv,I) and eq(hal@hal,gs) and eq(hi@hi,inv)
 # Native odd input is (x,0) in R + R; physical scalar is (g,g^-1).
 # Midpoint parameter must be fixed under the physical w swapping the two limbs.
 fixed=hi@(xs-I+gs)%3;fixed2=hal@(-I+inv)%3
 assert eq(fixed,fixed2)
 bi=hal@fixed%3;bi2=hi@fixed%3
 # Within the genuine isotope the two original odd marks multiply as left
 # cosets with the actual intervening k, not as composition of whole slopes.
 nbr=0;coll=0
 for j in range(q):
  value=(xs[j]+gs[j]@xs)%3
  assert eq(value+I,gs[j]@gs)
  # Compare actual old graph for each limb (the opposite physical site exchanges them).
  residual=bi[j]+gs[j]@xs-value
  assert eq(residual,gs[j]-I) and eq(bi2[j],inv[j]-I)
  key=value[:,tuple(a for a,b in rt),tuple(b for a,b in rt)]@(3**np.arange(d-1,-1,-1))
  assert eq(xs[key],value)
  coll+=np.count_nonzero(np.any((value-(xs+gs@xs[j]))%3,axis=(1,2)));nbr+=q
 # Concrete native higher-class word, not confusing the p-core with the subtable.
 def e(i,j,k=1):
  z=I.copy();z[i,j]=k;return z
 def comm(x,y):return x@y@pw(x,26)@pw(y,26)%3
 a=e(0,1)
 for k in range(1,n-1):a=comm(a,e(k,k+1))
 assert eq(a,e(0,n-1))
 J=I.copy()
 for s in range(n-1):J[s,s+1]=1
 order=1
 while not eq(pw(J,order),I):order*=3
 print('UT_'+str(n)+'(3), group subloop size',q,'full physical principal-isotope group cells',nbr,'noncommuting ordered pairs',coll,'native last root commutator length',n-1,'regular Jordan element order',order)
def tiny():
 P=list(product(range(2),range(3),range(3)));ix={v:k for k,v in enumerate(P)}
 t=np.array([[ix[(e^f,(x+(-1)**e*y)%3,(z+h+e*x*y)%3)] for f,y,h in P] for e,x,z in P])
 k=ix[1,0,0];T=t[:,t[k]];j=np.arange(18)
 assert np.array_equal(T[k],j) and np.array_equal(T[:,k],j)
 for a in j:
  assert np.all(T[a,T[:,T[a]]]==T[T[a,T[:,a]]])
 f=np.array([ix[1^e,(-x)%3,z] for e,x,z in P]);a=f[ix[0,1,0]];b=f[ix[1,0,0]]
 assert P[T[T[a,b],a]][2]==0 and P[T[a,T[b,a]]][2]==1
 print('18-point native proper isotope: all 5832 left Bol triples; flexibility witness central coordinates 0 versus 1')
def cyc(s):
 n=3**(s-1)+1;I=np.eye(n,dtype=np.int64);J=I.copy()
 for i in range(n-1):J[i,i+1]=1
 assert not eq(pw(J,3**(s-1)),I) and eq(pw(J,3**s),I)
 print('cyclic witness',s,'literal algebra-unit/native element order',3**s,'while original exponent six')
if __name__=='__main__':
 tiny()
 for n in (3,4):run(n)
 for s in range(2,6):cyc(s)
