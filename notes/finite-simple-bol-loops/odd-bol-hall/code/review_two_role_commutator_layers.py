"""Hostile control for the local result: compute left annihilators in raw affine space, not the submitted operator L or tester."""
from itertools import product
from collections import Counter
from verify_every_odd_prime_sylow_obstruction import Field

def test(p,l,f,eachdet):
 ff=Field(l,f);q=ff.q;r=p//2;plus,mult,neg,iv=ff.plus,ff.times,ff.neg,ff.inv
 def orb(z):
  a=[1];x=z
  while x!=1:a.append(x);x=mult[x][z]
  return a
 zz=next(a for x in range(2,q) if len(a:=orb(x))==p)
 A=lambda a,b:tuple(plus[x][y] for x,y in zip(a,b));M=lambda a,b:tuple(plus[x][neg[y]] for x,y in zip(a,b));S=lambda k,a:tuple(mult[k][x] for x in a);e=lambda j:tuple(int(i==j) for i in range(p));zero=S(0,e(0));half=pow(2,-1,p)
 pb=[e(0)]+[A(e(j),e(-j%p)) for j in range(1,r+1)];nb=[M(e(j),e(-j%p)) for j in range(1,r+1)]
 def W(x,a):i,j=x;return tuple(mult[zz[(i*j*half+j*(k-i))%p]][a[(k-i)%p]] for k in range(p))
 def ev(x,v):
  a=0
  for i,j in zip(x,v):a=plus[a][mult[i][j]]
  return a
 def ref(rows):
  a=[list(x) for x in rows];k=0;pc=[]
  for col in range(len(a[0])):
   i=next((n for n in range(k,len(a)) if a[n][col]),None)
   if i is None:continue
   a[k],a[i]=a[i],a[k];a[k]=S(iv[a[k][col]],a[k]);
   for i in range(len(a)):
    if i!=k and a[i][col]:a[i]=M(a[i],S(a[i][col],a[k]))
   pc.append(col);k+=1
  return a[:k],pc
 def normal(C):
  R,piv=ref(C);assert len(piv)==p-1;h=next(j for j in range(p) if j not in piv);out=[0]*p;out[h]=1
  for a,k in zip(R,piv):out[k]=neg[a[h]]
  assert all(ev(out,a)==0 for a in C)
  return out
 def basis(pt):return xhalf[pt]
 xs=list(product(range(p),repeat=2));xhalf={x:[W(tuple((i*half)%p for i in x),n) for n in nb] for x in xs};hist={d:Counter() for d in (range(1,p) if eachdet else [1])};cnt=0
 for x,y in product(xs,repeat=2):
  det=(x[0]*y[1]-x[1]*y[0])%p
  if det not in hist:continue
  # All possible differences of the two actual origins of the affine compositions, plus their common flat direction.
  gen=[W(x,W(y,a)) for a in pb]+[M(a,W(y,a)) for a in basis(x)]+[M(W(x,a),a) for a in basis(y)];nu=normal(gen);h=tuple(ev(nu,M(W(x,W(y,a)),W(y,W(x,a)))) for a in nb);assert any(h);h=S(iv[next(i for i in h if i)],h);hist[det][h]+=1;cnt+=1
  # Confirm every sampled Y,X-conjugate pair is in the raw endpoints (in A, not modulo the loop table).
  w=pb[sum(x+y)%len(pb)];a=M(w,W(x,w));b=M(w,W(y,w));assert ev(nu,M(A(a,W(x,b)),A(b,W(y,a))))==0
 polys=[]
 for i in range(r):
  for tail in product(range(q),repeat=r-i-1):polys.append((0,)*i+(1,)+tail)
 data=[]
 for d,lines in hist.items():
  assert sum(lines.values())==p*(p*p-1) and len(ref(list(lines))[1])==r
  bad=Counter(sum(w for h,w in lines.items() if ev(h,t)) for t in polys);assert min(bad)*r>=sum(lines.values()) and sum(bad.values())==len(polys)
  data.append((d,len(lines),sorted(bad.items())))
 print(f'p={p} q={q} char={l} raw codimension-one cases={cnt} projective tilts exhaustively tested per determinant={len(polys)} complete failure histograms',data)
for pa in [(3,7,1,True),(5,3,4,True),(7,29,1,True)]:test(*pa)
