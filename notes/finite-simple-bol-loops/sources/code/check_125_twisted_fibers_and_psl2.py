"""Additional non-simple exact-factorization folders with faithful coset action and even/odd top quotients."""
from collections import Counter
from itertools import product

def fold(m):
 assert m%3
 # X=C_m wr C3. Exact factors: coordinate plane A, central diagonal × rotation B. G ⊂ X×X satisfies opposite abelianizations.
 V=list(product(range(m),repeat=3));X=[(v,j) for v in V for j in range(3)];M=set(X);e=((0,0,0),0)
 def mul(x,y):return tuple((x[0][i]+y[0][(i-x[1])%3])%m for i in range(3)),(x[1]+y[1])%3
 def inv(x):return tuple((-x[0][(i+x[1])%3])%m for i in range(3)),(-x[1])%3
 def ab(x):return sum(x[0])%m
 A={(v,0) for v in V if v[2]==0};B={((c,c,c),j) for c,j in product(range(m),range(3))};assert {mul(a,b) for a,b in product(A,B)}==M and len(A)*len(B)==len(X)
 H=[(a,b) for a,b in product(A,B) if (ab(a)+ab(b))%m==0 and (a[1]+b[1])%3==0];assert len(H)==m**2 and {ab(a) for a,b in H}==set(range(m));HH=set(H)
 # The identity has ordinary stabilizer H. The K-translate indexed by y means (y,y^-1)H. Check the proposed label of each ordinary tau(h) image by membership of the coset correction in H.
 moves={x:set() for x in X};bad=0
 for a,b in H:
  fixed=0
  for x in X:
   y=mul(mul(b,x),inv(a));moves[x].add(y)
   # k_y^-1 tau(h) k_x = h, not tau(h).
   c1=mul(mul(inv(y),b),x);c2=mul(mul(y,a),inv(x));assert (c1,c2) in HH and (c1,c2)==(a,b)
   assert ab(y)==(ab(x)-2*ab(a))%m;fixed+=y==x
  if 2*ab(a)%m:assert not fixed;bad+=1
 for x,orb in moves.items():
  lab=Counter(ab(y) for y in orb);s=len({2*z%m for z in range(m)});assert len(orb)%s==0 and len(lab)==s and len(set(lab.values()))==1
 assert e in moves[e];print('C_m quotient of actual coset-labelled factorization controls: m, |Q|, |H|, derangements forced, tau(H)-orbit lengths',m,len(X),len(H),bad,sorted({len(z) for z in moves.values()}))

def sl(f,mod):
 q=1<<f
 def mult(a,b):
  t=0
  while b:
   if b&1:t^=a
   b>>=1;a<<=1
   if a&q:a^=mod
  return t
 T=[[mult(a,b) for b in range(q)] for a in range(q)]
 def mat(x,y):return tuple(T[x[2*i]][y[j]]^T[x[2*i+1]][y[2+j]] for i in range(2) for j in range(2))
 def inv(x):return (x[3],x[1],x[2],x[0])
 e=(1,0,0,1);G=[(a,b,c,d) for a,b,c,d in product(range(q),repeat=4) if T[a][d]^T[b][c]==1];assert len(G)==q*(q*q-1)
 o2={g for g in G if g!=e and mat(g,g)==e};o3={g for g in G if g!=e and mat(mat(g,g),g)==e}
 def orbit(h):return {mat(mat(g,h),inv(g)) for g in G}
 assert o2==orbit(next(iter(o2))) and o3==orbit(next(iter(o3)))
 def cube(g):return mat(mat(g,g),g)
 nine=[g for g in G if cube(g)!=e and cube(cube(g))==e]
 counter=False
 if nine:
  g=nine[0];fg=tuple(T[u][u] for u in inv(g));counter=fg not in orbit(g);assert counter
 assert bool(nine)==(f%3==0)
 print('SL2 in actual GF(2^f): q, unique 2/3-class sizes, order-9 elements, inversion-Frobenius fails on order 9:',q,len(o2),len(o3),len(nine),counter)
if __name__=='__main__':
 for m in (4,5,8):fold(m)
 for f,mod in [(2,0b111),(3,0b1011),(4,0b10011)]:sl(f,mod)
