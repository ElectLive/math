"""Actual finite field, native coset product, graph and stabilizer controls (stdlib Python 3)."""
from itertools import product
from random import Random
from math import prod

class Field:
 def __init__(self,l,f):
  self.q=q=l**f
  def digs(n,d):return [(n//l**i)%l for i in range(d)]
  def rem(a,b):
   a=a[:];d=len(b)-1
   for i in range(len(a)-1,d-1,-1):
    z=a[i]%l
    for j in range(d+1):a[i-d+j]=(a[i-d+j]-z*b[j])%l
   return a[:d]
  irr=next(c+[1] for i in range(l**f) if (c:=digs(i,f)) is not None and c[0] and all(any(rem(c+[1],digs(n,d)+[1])) for d in range(1,1+f//2) for n in range(l**d)))
  digits=[digs(n,f) for n in range(q)];enc=lambda a:sum(x*l**i for i,x in enumerate(a));self.irr=irr
  self.plus=[[enc([(x+y)%l for x,y in zip(a,b)]) for b in digits] for a in digits]
  def times(a,b):
   c=[0]*(2*f-1)
   for i,x in enumerate(a):
    for j,y in enumerate(b):c[i+j]+=x*y
   return enc([v%l for v in rem(c,irr)])
  self.times=[[times(a,b) for b in digits] for a in digits]
  self.neg=[next(i for i in range(q) if r[i]==0) for r in self.plus]
  self.inv=[0]+[next(i for i in range(1,q) if self.times[x][i]==1) for x in range(1,q)]

def case(p,l,f):
 F=Field(l,f);add,mul,neg,inv,q=F.plus,F.times,F.neg,F.inv,F.q
 rng=Random(271828+p+q);r=p//2;half=pow(2,-1,p);halfF=inv[add[1][1]]
 def powers(z):
  a=[1];t=z
  while t!=1:a.append(t);t=mul[t][z]
  return a
 z=next(a for a in range(2,q) if len(powers(a))==p);zz=powers(z)
 small=lambda m:tuple(0 for _ in range(m));plus=lambda a,b:tuple(add[x][y] for x,y in zip(a,b));minus=lambda a,b:tuple(add[x][neg[y]] for x,y in zip(a,b));sc=lambda h,a:tuple(mul[h][x] for x in a)
 def J(a):return tuple(a[-i%p] for i in range(p))
 def emb(h):return (0,)+tuple(h)+tuple(neg[x] for x in reversed(h))
 def d(a):return tuple(mul[halfF][add[a[j]][neg[a[-j]]]] for j in range(1,r+1))
 def E(j,n):return tuple(int(i==j) for i in range(n))
 def B(m,n):a,b,c=m;i,j,k=n;return (a+i)%p,(b+j)%p,(b*i+c+k)%p
 def S(x):a,b=x;return a,b,a*b*half%p
 def act(m,v):a,b,c=m;return tuple(mul[zz[(c+b*(i-a))%p]][v[(i-a)%p]] for i in range(p))
 def A(x,y):return (x[0]+y[0])%p,(x[1]+y[1])%p
 def N(x):return -x[0]%p,-x[1]%p
 def div2(x):return half*x[0]%p,half*x[1]%p
 points=list(product(range(p),repeat=2));B0=(0,0,0)
 for a,b,c in product(range(p),repeat=3):
  m=(a,b,c); jm=(-a%p,-b%p,c);mi=(-a%p,-b%p,(a*b-c)%p)
  assert B(m,mi)==B0 and (jm==mi)==(m==S((a,b))) and (m==jm)==(a==b==0)
  for _ in range(1):
   v=tuple(rng.randrange(q) for i in range(p));n=tuple(rng.randrange(p) for i in range(3))
   assert J(act(m,J(v)))==act(jm,v) and act(B(m,n),v)==act(m,act(n,v))
 def inverse(cols):
  n=len(cols);M=[[cols[j][i] for j in range(n)]+list(E(i,n)) for i in range(n)]
  for c in range(n):
   u=next(k for k in range(c,n) if M[k][c]);M[c],M[u]=M[u],M[c];M[c]=list(sc(inv[M[c][c]],M[c]))
   for k in range(n):
    if k!=c:M[k]=list(minus(M[k],sc(M[k][c],M[c])))
  return [tuple(v[n:]) for v in M]
 def row(x,y):
  a=0
  for b,c in zip(x,y):a=add[a][mul[b][c]]
  return a
 inverses={x:inverse([d(act(S(N(div2(x))),emb(E(j,r)))) for j in range(r)]) for x in points}
 def mark(x,h):return act(S(div2(x)),emb(h))
 def op(k,k2,v):
  x,h=k;y,t=k2;w=A(x,y);b=B(S(N(w)),B(S(x),S(y)));assert b[:2]==(0,0)
  hvec=act(S(N(w)),plus(mark(x,h),act(S(x),mark(y,t))));beta=zz[b[2]]
  rhs=plus(d(hvec),sc(add[beta][neg[1]],v));out=(w,tuple(row(rr,rhs) for rr in inverses[w]));u=act(S(N(w)),minus(plus(mark(x,h),act(S(x),mark(y,t))),mark(*out)))
  assert d(u)==sc(add[1][neg[beta]],v) # actual stabilizer condition on k_out^-1 k1 k2
  return out
 for x in points:
  for j in range(r):
   aa=mark(x,E(j,r));m=S(x);assert J(aa)==sc(neg[1],act(S(N(x)),aa))
   if x!=(0,0):
    accum=small(p)
    for _ in range(p):accum=plus(aa,act(m,accum))
    assert not any(accum) # true pth power in all fiber directions
 vv=E(0,r);assert J(emb(vv))==sc(neg[1],emb(vv))
 def elt():return (rng.choice(points),tuple(rng.randrange(q) for j in range(r)))
 for v in [small(r),vv,tuple(rng.randrange(q) for j in range(r))]:
  for i in range(100):
   x,y,t=elt(),elt(),elt();assert op(x,op(y,op(x,t,v),v),v)==op(op(x,op(y,x,v),v),t,v)
 # Positive graphs from true conjugates of B, verification in the original coset action, and wrong-basepoint control.
 for t in range(4):
  w=tuple(rng.randrange(q) for j in range(p));w=plus(w,J(w));sec={}
  for x in points:
   actual=minus(w,act(S(x),w));coord=act(S(N(div2(x))),actual);h=d(coord)
   assert emb(h)==coord and mark(x,h)==actual;sec[x]=x,h
  tests=list(product(points,repeat=2)) if p<=5 else [(rng.choice(points),rng.choice(points)) for i in range(384)]
  assert all(op(sec[x],sec[y],small(r))==sec[A(x,y)] for x,y in tests)
  assert any(op(sec[x],sec[y],vv)!=sec[A(x,y)] for x,y in tests)
  hits=[]
  for tilt in [small(r),vv]:
   hits.append(sum(d(sc(add[1][neg[b]],w))==sc(add[1][neg[b]],tilt) for b in zz))
  assert hits==[p,1]
 print(f'p={p:2} field={l}^{f}={q:2} modulus={F.irr} root={z:2} group-Sylow-order={p**3} native-order={p*p*q**r} stable-complements={q**(r+1)} intersections=[{p},1] all {p*p} native fiber inverses, every p-power norm, 300 Bol triples and both graph controls PASS')
if __name__=='__main__':
 for p,l,f in [(3,7,1),(3,5,2),(5,11,1),(5,3,4),(7,29,1),(11,23,1)]:case(p,l,f)
