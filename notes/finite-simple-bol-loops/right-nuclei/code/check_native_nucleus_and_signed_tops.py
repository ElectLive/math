"""Independent tests. Exact P=F_0^(2n):(C3 x R) and the full embedded native subloop on P;
plus all swap-stable normal subgroups of two actual top groups. Pure Python standard library."""
from itertools import product
from collections import deque
from random import Random
from math import gcd
rnd=Random(102753)
# A different field basis: discover monic irreducible and primitive element instead of importing matrices.
p=11;q=p**3
def unpack(x):return x%p,x//p%p,x//(p*p)%p
def pack(a):return sum((v%p)*p**i for i,v in enumerate(a))
f,g=next((f,g)for f,g in product(range(1,p), repeat=2) if all((i**3+f*i+g)%p for i in range(p)))
def pm(x,y):
 a=unpack(x);b=unpack(y);v=[0]*5
 for i,j in product(range(3),repeat=2):v[i+j]+=a[i]*b[j]
 for i in (4,3):
  v[i-2]-=v[i]*f;v[i-3]-=v[i]*g
 return pack(v[:3])
def power(x,e):
 a=1
 while e:
  if e&1:a=pm(a,x)
  x=pm(x,x);e//=2
 return a
c=next(x for x in range(11,q)if all(power(x,(q-1)//t)!=1 for t in (2,5,7,19)))
ep=[1]
for _ in range(q-2):ep.append(pm(ep[-1],c))
lg={x:i for i,x in enumerate(ep)};assert len(lg)==q-1
def add(x,y):return pack([v+w for v,w in zip(unpack(x),unpack(y))])
def neg(x):return pack([-v for v in unpack(x)])
def scal(x,e):return ep[(lg[x]+e)%(q-1)] if x else 0
def fr(x,i):return ep[(lg[x]*11**i)%(q-1)] if x else 0
# Code (x,j) as x+q*j. zeta=c^190.
def mu(a,b):
 x,i=a%q,a//q;y,j=b%q,b//q
 return add(x,scal(y,190*i))+q*((i+j)%7)
def iv(a):
 x,i=a%q,a//q;return neg(scal(x,-190*i))+q*((-i)%7)
def auto(a,i,wing):
 x,j=a%q,a//q
 return scal(fr(x,i),wing*(1-11**i))+q*((j*pow(4,i,7))%7)
def theta(a):
 x,i=a%q,a//q
 return scal(fr(x,1),1)+q*(4*i%7)
def grp(mul,A,e):
 ix={z:i for i,z in enumerate(A)};G=[[ix[mul(u,v)]for v in A]for u in A]
 assert ix[e]==0
 return G,[row.index(0)for row in G]
def met21():
 return grp(lambda u,v:((u[0]+pow(2,u[1],7)*v[0])%7,(u[1]+v[1])%3),list(product(range(7),range(3))),(0,0))
def met27():
 return grp(lambda u,v:((u[0]+pow(4,u[1],9)*v[0])%9,(u[1]+v[1])%3),list(product(range(9),range(3))),(0,0))
def unit27():
 return grp(lambda u,v:((u[0]+v[0])%3,(u[1]+v[1])%3,(u[2]+v[2]+u[0]*v[1])%3),list(product(range(3),repeat=3)),(0,0,0))
def signed(g,inv,T):
 m=len(g);A={g[g[inv[i]][inv[j]]][g[i][j]] for i,j in product(range(m),repeat=2)}
 assert all(g[x][y] in A for x,y in product(A,repeat=2))
 E=[(i,j)for i,j in product(range(m),repeat=2) if g[i][j] in A];ix={k:i for i,k in enumerate(E)};k=len(E)
 h=[[ix[g[x][u],g[y][v]]for u,v in E]for x,y in E];invh=[row.index(0)for row in h]
 swap=[ix[j,i]for i,j in E]
 orbs=[];left=set(range(k))
 while left:
  x=min(left);cl={h[h[z][x]][invh[z]]for z in range(k)};B=cl|{swap[x]for x in cl};orbs.append(B);left-=B
 def cls(H,V):
  gs=H|V;pool=set(H);todo=list(H)
  while todo:
   x=todo.pop()
   for z in gs:
    w=h[x][z]
    if w not in pool:pool.add(w);todo.append(w)
  return frozenset(pool)
 trivial=frozenset([0]);seen={trivial};Q=deque([trivial]);hist={};cor=0
 while Q:
  H=Q.popleft()
  if len(H)<k:
   I=[E[z]for z in H];U={z[0]for z in I};B={v for v,w in I if w==0};diag=sum(i==j for i,j in I);hit=sum(j in T for _,j in I)
   num=len(T)*diag;assert num%hit==0;ratio=num//hit;hist[ratio]=hist.get(ratio,0)+1
   assert ratio>1
   if len(I)>1 and len(B)<len(U):cor+=1
  for V in orbs:
   if not V<=H:
    K=cls(H,V)
    if K not in seen:seen.add(K);Q.append(K)
 return k,len(seen),cor,hist
nt=q*7
# Complete nonlinear twisted solve t^-1 Theta(t) used in EVERY honest native multiplication below.
solve={mu(iv(t),theta(t)):t for t in range(nt)};assert len(solve)==nt
def trial(G,inv,name):
 n=len(G);z=(0,)*n;one=(z,z,0,0)
 def mul(A,B):
  x,y,i,r=A;u,v,j,s=B;perm=G[inv[r]]
  return tuple(mu(x[t],auto(u[perm[t]],i,0))for t in range(n)),tuple(mu(y[t],auto(v[perm[t]],i,1))for t in range(n)),(i+j)%3,G[r][s]
 def inverse(A):
  x,y,i,r=A;k=(-i)%3;perm=G[r]
  return tuple(auto(iv(x[perm[t]]),k,0) for t in range(n)),tuple(auto(iv(y[perm[t]]),k,1)for t in range(n)),k,inv[r]
 def factor(A):
  x,y,i,r=A;t=tuple(solve[mu(iv(j),k)] for j,k in zip(x,y));b=tuple(mu(j,iv(k))for j,k in zip(x,t))
  K=(b,b,0,0);J=(t,tuple(map(theta,t)),i,r);assert mul(K,J)==A
  return K,J
 def loop(x,y):
  p,b=mul(x,y),mul(inverse(x),inverse(y))
  s1,t1=factor(inverse(p));s2,t2=factor(b);u=mul(inverse(t1),inverse(s2))
  # Verify both actual coset constraints, not their degrees/abelianizations.
  l=mul(inverse(u),p);right=mul(u,b)
  assert l[0]==l[1] and l[2:]==(0,0) and right[1]==tuple(map(theta,right[0]))
  return u
 def Rand():return tuple(rnd.randrange(nt)for _ in range(n)),tuple(rnd.randrange(nt)for _ in range(n)),rnd.randrange(3),rnd.randrange(n)
 marks=[(z,z,0,r)for r in range(n)]
 ab=0
 for r,t in product(range(n),repeat=2):
  # For two pure top elements this is the exact fast specialization of the factor computation:
  # first and second slots have identical zero words, so both K entries are 1.
  x,y=marks[r],marks[t];p=mul(x,y);b=mul(inverse(x),inverse(y));u=p
  assert u==marks[G[r][t]] and mul(inverse(u),p)==one and mul(u,b)[1]==tuple(map(theta,mul(u,b)[0]))
  ab+=G[r][t]!=G[t][r]
 # Exercise full nontrivial top-factorized native subloop on random words and every target mark.
 num=0;rev_fail=0;left_switch=0;bol=0
 for r,v in enumerate(marks):
  x,y=Rand(),Rand()
  assert loop(loop(x,y),v)==loop(x,loop(y,v));num+=1
  rev_fail+=loop(loop(x,v),y)!=loop(x,loop(v,y))
  left_switch+=loop(v,x)!=loop(x,v)
  u=Rand();assert loop(x,loop(y,loop(x,u)))==loop(loop(x,loop(y,x)),u);bol+=1
 print(name,'native ordered nuclear products',n*n,'genuinely noncommuting',ab,'non-scalar word pairs testing right nucleus',num,'middle and commutant failures',rev_fail,left_switch,'full physical Bol tests',bol)
if __name__=='__main__':
 print('independent F11^3 basis t^3+%d*t+%d and primitive code %d: nonlinear S*T solver has %d actual entries'%(f,g,c,len(solve)))
 for C,name in [(met21,'C7:C3'),(met27,'C9:C3'),(unit27,'UT3(3)')]:
  G,inv=C()
  T=set(range(len(G))) if len(G)==27 else {0,1,2}
  order,nn,cor,hist=signed(G,inv,T);print(name,'all normal swap cuts (incl endpoints) in top order',order,nn,'proper nontrivial correlated',cor,'proper cut ratios',sorted(hist.items()))
  trial(G,inv,name)
