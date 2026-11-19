"""Independent physical tests. Compute each native commutation via the original
class-two group and its actual stabilizer, over all CRT components. In particular
a nonprimitive address can disappear over the residue field and still work."""
import numpy as np
from itertools import product
from math import lcm
from random import Random
r=Random(543912)
def rank(a,p):
 a=a.copy()%p;i=0
 for j in range(a.shape[1]):
  u=next((u for u in range(i,len(a)) if a[u,j]),None)
  if u is None:continue
  a[[u,i]]=a[[i,u]];a[i]=a[i]*pow(int(a[i,j]),-1,p)%p
  v=a[:,j].copy();v[i]=0;a=(a-v[:,None]*a[i])%p;i+=1
 return i
def trial(rs,q,repeat):
 P=list(product(*map(range,rs)));N=len(P);I={h:i for i,h in enumerate(P)};k=len(rs);h0=I[(1,)*k];zero=tuple([0]*(2*k));i0=zero,0
 ch=[]
 for i,s in enumerate(rs):
  t=next(t for t in range(2,q) if pow(t,s,q)==1 and all(pow(t,j,q)!=1 for j in range(1,s)))
  ch.append([pow(t,j,q) for j in range(s)])
 add=np.array([[I[tuple((a+b)%s for a,b,s in zip(h,j,rs))] for j in P] for h in P]);iv=[I[tuple(-a%s for a,s in zip(h,rs))] for h in P]
 cp=np.array([[ch[i][h[i]] for i in range(k)] for h in P]);cm=cp[iv];full=np.hstack((cp,cm));rev=np.hstack((cm,cp))
 v=(1,)+(0,)*(k-1)+(q-1,)+(0,)*(k-1);tupleq=lambda x:tuple(int(t)%q for t in x)
 def xm(x,y):
  t,h=x;s,j=y;return tupleq(t+full[h]*s),int(add[h,j])
 def xi(x):
  t,h=x;return tupleq(-full[iv[h]]*t),iv[h]
 def xt(x):
  t,h=x;return t[k:]+t[:k],iv[h]
 def sh(x):return np.array(x.copy())
 def act(x,u):
  t,h=x;u0,u1=u
  def row(a,h,t):
   ii=(np.arange(q)[None,:]-t[:,None])%q
   return a[add[h],:, :][np.arange(N)[:,None,None],np.arange(repeat*k)[None,:,None],ii[:,None,:]]
  return np.array([row(u0,h,full@t),row(u1,iv[h],rev@t)])
 rings=np.array(list(rs)*repeat);rr=rings[None,None,:,None];half=np.array([pow(2,-1,s) for s in rs])
 def pairing(a,b):
  def B(x,y):return np.sum(x*(np.roll(y[iv],1,axis=-1)-np.roll(y[iv],-1,axis=-1)),axis=(0,2)).reshape(repeat,k).sum(axis=0)
  return (B(a[0],b[1])+B(a[1],b[0]))%rs
 def dm(a,b):
  u,c,x=a;v,d,y=b;w=act(x,v);return (u+w)%rr,(c+d+half*pairing(u,w))%rs,xm(x,y)
 def di(a):
  u,c,x=a;y=xi(x);return (-act(y,u))%rr,-c%rs,y
 def dt(a):
  u,c,x=a;return u[::-1],c,xt(x)
 def eq(a,b):return np.array_equal(a[0],b[0]) and np.array_equal(a[1],b[1]) and a[2]==b[2]
 def comm(a,b):
  u,c,(v,h)=dm(di(dm(b,a)),dm(a,b))
  return not any(v[:k]) and not np.any(u[1]) and tuple(c)==P[h]
 U0=np.zeros((2,N,k*repeat,q),dtype=int);C0=np.zeros(k,dtype=int)
 def pure(x):return U0,C0,x
 identity=pure(i0);a=pure((zero,h0));bare=pure((v,0))
 w=U0.copy()
 scalar=3 if rs[0]==9 else 1
 w[1,0,0,0]=scalar;w[1,0,0,1]=-scalar;w[0]=-w[1];w%=rr
 b=dm((w,C0,i0),bare)
 assert eq(dt(b),di(b)) and eq(dt(a),di(a)) and eq(dm(bare,(w,C0,i0)),b)
 hbare=haddr=0
 for h in range(N):
  g=pure((zero,h));assert eq(dt(g),di(g)) and comm(g,a);hbare+=comm(g,bare);haddr+=comm(g,b)
 assert hbare==N//rs[0] and haddr==1
 # True native marks, not arbitrary group elements. Test actual commutators in H.
 rng=np.random.default_rng(15112);nk=0
 for _ in range(250):
  u=rng.integers(0,rings.max(),size=U0.shape);u[:,:,:,-1]=-u[:,:,:,:-1].sum(axis=3);u%=rr
  x=tuple(r.randrange(q) for _ in range(2*k)),r.randrange(N)
  g=(u,np.array([r.randrange(s) for s in rs]),x);marked=dm(g,di(dt(g)))
  assert eq(dt(marked),di(marked)) and eq(dm(marked,di(marked)),identity)
  if comm(marked,a) and comm(marked,b):assert eq(marked,identity)
  nk+=1
 # Complete augmented system after exact h0(period) elimination: every h0 orbit
 # shares a physical coefficient; draw one nonzero-v site, and impose its true
 # q-cycle difference on the full q−1 sum-zero coordinates, modulo each p | S.
 unseen=set(range(N));shifts=[]
 while unseen:
  j=next(iter(unseen));o={j};z=int(add[j,h0])
  while z not in o:o.add(z);z=int(add[z,h0])
  unseen-=o;i=next(i for i in o if int(rev[i]@v)%q);shifts.append(int(rev[i]@v)%q)
 basis=np.hstack((np.eye(q-1,dtype=int),-np.ones((q-1,1),dtype=int)))
 for s in set(rs):
  p=next(i for i in range(2,s+1) if s%i==0)
  for d in shifts:assert rank((basis-np.roll(basis,d,axis=1))[:,:-1],p)==q-1
 # Mark with only higher-ring address: mistaken mod-p screening misses a true top.
 if rs[0]==9:
  assert not np.any(w[:,:,:,:]%3) and any(comm(pure((zero,h)),bare) and not comm(pure((zero,h)),b) for h in range(1,N))
 print('ring',rs,'q',q,'copies',repeat,'true pure common with bare vs addressed',hbare,haddr,'nonzero address',scalar,'actual signed sampled marks',nk,'full unit minor ranks',len(shifts),'x',q-1)
for rs,q,m in [((9,3),19,1),((3,5),31,2),((3,3,3),7,2),((3,),7,1)]:trial(rs,q,m)
