from itertools import product
from collections import Counter
from math import gcd
for m in range(1,5):
 f=9*m
 basis=lambda i:tuple(int(j==i) for j in range(f))
 def add(v,w,c=1): return tuple((a+c*b)%3 for a,b in zip(v,w))
 def fr(v,k): return tuple(v[(i-k)%f] for i in range(f))
 def J(v):return add(fr(v,m),v,-1)
 x=basis(0); gens=[J(x)]+[add(basis(r),x,-1) for r in range(1,m)]
 cols=[]
 for g,z in enumerate(gens):
  for k in range(8 if g==0 else 9):
   cols.append((g,k,z));z=J(z)
 n=len(cols)
 mat=[[cols[j][2][i] for j in range(n)]+[int(i==j) for j in range(f)] for i in range(f)]
 for j in range(n):
  pivot=next(i for i in range(j,f) if mat[i][j]%3)
  mat[j],mat[pivot]=mat[pivot],mat[j]
  scale=pow(mat[j][j],-1,3);mat[j]=[(e*scale)%3 for e in mat[j]]
  for i in range(f):
   if i!=j:
    c=mat[i][j];mat[i]=[(a-c*b)%3 for a,b in zip(mat[i],mat[j])]
 def coord(v):
  z=tuple(sum(a*b for a,b in zip(row[n:],v))%3 for row in mat);assert z[-1]==0
  return z[:-1]
 def formula(v):
  av=[0]*m;bv=[0]*m
  for a,(g,k,_) in zip(coord(v),cols):
   if k==0: av[g]=a
   if k==1: bv[g]=a
  return av,bv
 pre=[formula(fr(g,-1)) for g in gens]; ph=formula(add(x,fr(x,-1),-1)) # Fr^-1(Fr x - x)
 def evaleta(eta,c):
  a,b=c
  return (sum(k*e[0] for k,e in zip(a,eta))%3,
          sum(k*e[1]+l*e[0] for k,l,e in zip(a,b,eta))%3)
 def step(z):
  eta,u=z
  a,b=evaleta(eta,ph)
  return tuple(evaleta(eta,c) for c in pre),(u-b+2*a)%3
 seen=set(); sizes=Counter()
 for y in product(range(3),repeat=2*m):
  eta=((1,y[0]),)+tuple(zip(y[1:-1:2],y[2:-1:2]))
  z=(eta,y[-1])
  if z in seen:continue
  n=0
  while z not in seen:
   seen.add(z);n+=1;z=step(z)
  assert 3*m%n==0
  sizes[n]+=1
 k=m
 a=1
 while k%3==0:k//=3;a*=3
 assert sum(sizes.values())*3*m==sum(3**(2*a*gcd(k,j)) for j in range(k))
 print('m',m,'objects',len(seen),'orbits',sum(sizes.values()),'size inventory',dict(sizes))
