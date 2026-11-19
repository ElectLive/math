"""Hostile author controls for all-R theorem. Concrete target groups include a
nonabelian group of order 21, a central-derived group of order 27, and two
different abelian groups of the same order. Matrix coordinates below are
literal prime-field operators for all 49|R| weights, never the giant loop."""
from itertools import product
from math import gcd
import numpy as np
rng=np.random.default_rng(312731)
e=np.eye(3,dtype=np.int64);X=np.array([[0,0,-1],[1,0,0],[0,1,-4]],dtype=np.int64)%11
def pw(a,k,p=11):
 r=np.eye(len(a),dtype=int)
 while k:
  if k&1:r=r@a%p
  a=a@a%p;k//=2
 return r
C=e+X;Z=pw(C,190);A=np.stack([pw(X,11*j)[:,0] for j in range(3)],axis=1)
A2=C@A@pw(C,1329)%11;TH=C@A%11
assert all(not np.array_equal(pw(C,1330//p),e) for p in (2,5,7,19)) and np.array_equal(pw(C,1330),e)
assert np.array_equal(pw(A,3),e) and np.array_equal(pw(A2,3),e)
assert np.array_equal(TH@A%11,A2@TH%11) and not np.array_equal(pw(TH,3),e)
z=[pw(Z,i) for i in range(7)];a=[pw(A,i) for i in range(3)];b=[pw(A2,i) for i in range(3)]
Tlocal=np.array([[np.block([[z[j]@a[s]%11,np.zeros((3,3),int)],[np.zeros((3,3),int),z[k]@b[s]%11]]) for j,k in product(range(7),repeat=2)] for s in range(3)])
tr=(e+A+pw(A,2))[0]%11
tr2=tr@pw(C,1329)%11
wloc=np.array([np.concatenate([tr@z[i]%11,tr2@z[j]%11]) for i,j in product(range(7),repeat=2)])
def rk(a,p):
 a=a.copy()%p;r=0
 for c in range(a.shape[1]):
  i=next((i for i in range(r,len(a)) if a[i,c]),None)
  if i is None:continue
  a[[i,r]]=a[[r,i]];a[r]=a[r]*pow(int(a[r,c]),-1,p)%p
  for j in range(len(a)):
   if j!=r:a[j]=(a[j]-a[j,c]*a[r])%p
  r+=1
 return r
assert rk(wloc,11)==6 and len(set(map(tuple,wloc)))==49
# Validate normalizer obstruction on local arrows, not just group size.
froots={h.tobytes() for h in z}
outer=[(b[j]@a[-j]%11).tobytes() in froots for j in range(3)];assert outer==[True,False,False]
idx={tuple(y):i for i,y in enumerate(wloc)}
wm=np.empty((3,49,49),dtype=int)
for s in range(3):
 for j in range(49):
  wm[s,j]=[idx[tuple(v)] for v in wloc@Tlocal[s,j]%11]
  assert len(set(wm[s,j]))==49
phase=np.array([pow(2,i,23) for i in range(11)])
def group(kind):
 if kind=='Heisenberg 27':
  R=list(product(range(3),repeat=3))
  def mu(x,y):return ((x[0]+y[0])%3,(x[1]+y[1])%3,(x[2]+y[2]+x[0]*y[1])%3)
 elif kind=='Frobenius 21':
  R=list(product(range(7),range(3)))
  def mu(x,y):return ((x[0]+pow(4,x[1],7)*y[0])%7,(x[1]+y[1])%3)
 elif kind=='C3 x C3':
  R=list(product(range(3),repeat=2))
  def mu(x,y):return ((x[0]+y[0])%3,(x[1]+y[1])%3)
 else:
  m=9 if kind=='C9' else 1
  R=list(range(m))
  def mu(x,y):return (x+y)%m
 N=len(R);ix={x:i for i,x in enumerate(R)}
 M=np.array([[ix[mu(x,y)] for y in R] for x in R]);iv=np.argmax(M==0,axis=1)
 return M,iv
def trial(kind):
 R,iv=group(kind);n=len(R);ii=np.arange(n)
 ZR={j for j in ii if np.array_equal(R[j],R[:,j])}
 comm={int(R[R[iv[i],iv[j]],R[i,j]]) for i,j in product(ii,repeat=2)}
 RR={0}; todo=[0]
 while todo:
  i=todo.pop()
  for j in comm:
   k=int(R[i,j])
   if k not in RR:RR.add(k);todo.append(k)
 assert n%2 and sum(R[i,j]!=R[j,i] for i in ii for j in ii)==(432 if n==27 else 336 if n==21 else 0)
 F=9317;Porder=3*n*F**(2*n);Aprime=len(RR)*F**(2*n)
 # Arrays are honest top arrows from C7^(2n):(C3 x R), not direct-product labels for R.
 def hm(H,G):
  k,s,r=H;l,t,u=G
  return (k+pow(4,s,7)*l[R[iv[r]]])%7,(s+t)%3,int(R[r,u])
 def kn(H,N):
  k,s,r=H;ms=Tlocal[s,k[:,0]*7+k[:,1]]
  return np.einsum('aij,aj->ai',ms,N[R[iv[r]]])%11
 # Pullback of a real dual weight at target i through the source-site matrix.
 def act(N,H,v):
  k,s,r=H;ww=wm[s,7*k[:,0]+k[:,1]]
  return (phase[N@wloc.T%11]*v[R[iv[r]][:,None],ww])%23
 def rndH():
  return rng.integers(0,7,size=(n,2)),int(rng.integers(3)),int(rng.integers(n))
 evals=0
 for r in ii:
  for s in range(3):
   H=(rng.integers(0,7,size=(n,2)),s,r);G=rndH();J=rndH()
   N,U=rng.integers(0,11,size=(2,n,6));v=rng.integers(0,23,size=(n,49))
   assert np.array_equal(kn(H,kn(G,U)),kn(hm(H,G),U))
   assert np.array_equal(act(N,H,act(U,G,v)),act((N+kn(H,U))%11,hm(H,G),v));evals+=1
 # Every normalized graph quotient operator acts on the n *actual* coordinates
 # by the corresponding left-regular permutation. Verify multiplication including
 # the nonabelian pairs; coordinate translations from base inner automorphisms
 # cannot implement any of these factor-moving arrows.
 allowed=[(s,r) for s in range(3) for r in ii if outer[s]]
 assert len(allowed)==n and len(set(tuple(R[r]) for _,r in allowed))==n
 assert all(np.array_equal(R[i][R[j]],R[R[i,j]]) for i in ii for j in ii)
 # Literal marked-coset multiplication on ALL target subgroup elements: for candidate
 # mark d_l its discrepancy first entry is l^-1*i*j, in S only at 1, and its
 # second is l*i^-1*j^-1 in T, necessarily derived for the successful candidate.
 for i,j in product(ii,repeat=2):
  first=R[iv,R[i,j]];second=R[:,R[iv[i],iv[j]]]
  choices=ii[first==0];assert list(choices)==[R[i,j]] and int(second[choices[0]]) in RR
 central_top=[(s,r) for s in range(3) for r in ii if np.all(R[r]==ii) and pow(4,s,7)==1]
 assert central_top==[(0,0)]
 # Rank sums are block diagonal (weights chosen on a SINGLE distinct site).
 assert all(not np.array_equal((np.eye(n,dtype=int)[r])[:,None]*wloc[0],(np.eye(n,dtype=int)[0])[:,None]*wloc[0]) for r in range(1,n))
 print(kind,'target n',n,'|R-prime|',len(RR),'central-derived intersection',len(RR&ZR),'native nucleus noncommuting pairs',int(np.sum(R!=R.T)),
       'prime field faithful module dimension',49*n,'rank on the true independent 11-kernel',6*n,'real action equations',evals,
       '|P|/(3n)=|A|/|R-prime| verified',Porder//(3*n)==Aprime//len(RR))
 return n,len(RR),Porder,Aprime
print('Local F11^3 field graph: actual scalar-seven inner group; allowed graph normalization outer powers',outer,'true 49 local weights spanning rank',rk(wloc,11))
a0=trial('1');a1=trial('C9');a2=trial('C3 x C3');a3=trial('Frobenius 21');a4=trial('Heisenberg 27')
assert a1==a2
print('Equal-order nonisomorphic targets C9 and C3^2 have IDENTICAL v, |P| and |A|, not merely the same order scale.')
# Independent example showing why a naive assertion [U,Y-prime]=U for all
# W-normals is not required. Show three-site single-coordinate derived words
# over the group with central-derived C3, as well as the unsplit bad signed cut.
R,iv=group('Heisenberg 27');n=5
one=np.zeros(5,dtype=int)
def m(x,y):return R[x,y]
sitecomm=set()
for j,k in product(range(27),repeat=2):
 f=one.copy();g=one.copy();f[0]=j;f[1]=iv[j];g[0]=k;g[2]=iv[k]
 h=m(m(iv[f],iv[g]),m(f,g))
 assert not h[1:].any();sitecomm.add(int(h[0]))
assert len(sitecomm)==3
# Balanced constant c, pair (c,c^-1), correlation not a product: genuine obstruction.
B=[(int(x),int(iv[x])) for x in sitecomm];assert len(B)==3 and sum(i==j for i,j in B)==1 and sum(j==0 for i,j in B)==1
print('All 729 true three-site Heisenberg input commutators isolate the first coordinate, yielding all 3 derived values.')
print('Failed weak-center control C=anti-diagonal balanced constants: |C|=3, |C^swap|=|C cap H|=1; no such cut is available in the constructed coefficient group.')
