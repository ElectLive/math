"""Real projected mark enumeration and complete affine fixed-space checks over
the original sum-zero q-cycle rings. No complete enormous loop is enumerated."""
from itertools import product
from collections import Counter
from math import lcm,prod
def test(rs,q):
 I=range(len(rs));P=list(product(*(range(s)for s in rs)));k=len(rs);zero=tuple(0 for _ in I);one=tuple(1 for _ in I)
 def mod(x):return tuple(a%s for a,s in zip(x,rs))
 def times(a,b):return mod(x+y for x,y in zip(a,b))
 def minus(a):return mod(-x for x in a)
 def ordg(g):
  a=g;d=1
  while a!=1:a=a*g%q;d+=1
  return d
 roots=[next(x for x in range(1,q)if ordg(x)==s)for s in rs]
 ph={j:tuple(pow(x,i,q)for x,i in zip(roots,j))for j in P}
 n=2*k
 def act(h,v):return tuple(x*a%q for x,a in zip(v,ph[h]+ph[minus(h)]))
 def mul(x,y):
  v,h=x;w,g=y;return tuple((a+b)%q for a,b in zip(v,act(h,w))),times(h,g)
 def inv(x):
  v,h=x;h=minus(h);return (act(h,tuple(-vv for vv in v)),h)
 def comm(a,b):return mul(mul(inv(a),inv(b)),mul(a,b))
 zq=(0,)*(2*k);h0=(zq,one)
 e=tuple(int(i==0)for i in I)
 v=(e+tuple(-x%q for x in e),zero)
 K={h for h in P if ph[h][0]==1};kept=set();test1=0;total=0
 for h,A in product(P,product(range(q),repeat=k)):
  B=tuple((-s*x)%q for s,x in zip(ph[minus(h)],A));g=(A+B,h)
  assert inv(g)==(B+A,minus(h)) # actual inverted native projection
  a=comm(g,h0);total+=1
  if any(a[0][:k]) or a[1]!=zero:continue
  test1+=1;assert g[0]==zq
  c=comm(g,v)
  if any(c[0][:k])or c[1]!=zero:continue
  assert c==(zq,zero);kept.add(h)
 assert kept==K and test1==len(P)
 # The L1 affine commutation equation restricted to j1=0 is independent of alpha:
 # every such native mark is fixed by the true v action there. The raw address
 # w=e0−e1 at j=0 is invariant under exactly one of the remaining tops.
 lane={(j,t)for j in K for t in range(q)}
 w={(zero,0),(zero,1)} # exact support as raw q-cycle; values are +1,−1
 remain=[h for h in K if {(times(j,h),t)for j,t in w}==w]
 assert remain==[zero]
 # Complete native L1 slot orbits: every point left fixed by h0,v as function
 # is constant on a full q-cycle per line. Sum-zero on each P-index then kills
 # that constant because q is invertible in each actual coefficient ring.
 slots={(j,t)for j in P for t in range(q)};orbs=[]
 while slots:
  i=next(iter(slots));seen={i};stack=[i]
  while stack:
   j,t=stack.pop();s=(ph[minus(j)][0]-ph[j][0])%q
   for a in [(times(j,one),t),(j,(t+s)%q)]:
    if a not in seen:seen.add(a);stack.append(a)
  assert seen<=(slots) and all(sum((j,t)in seen for t in range(q))in (0,q)for j in P)
  slots-=seen;orbs.append(len(seen))
 assert all(u==q*lcm(*rs) for u in orbs)
 print('P',rs,'q',q,'all inverted top projections',total,'after bare top, after two bare marks, after one addressed coefficient',test1,len(kept),len(remain),'L1 permutation orbits',sorted(Counter(orbs).items()))
for rs,q in [((3,),7),((9,),19),((3,3),7),((9,3),19),((3,5),31),((3,3,3),7)]:test(rs,q)
