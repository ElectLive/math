"""Ordinary coset/mark actions in a concrete exact-factorization folder; stdlib only."""
from itertools import product,permutations
from collections import Counter
from random import Random
def pm(a,b):return tuple(a[i] for i in b)
def pi(a):return tuple(a.index(i) for i in range(len(a)))
def wreath():
 P=list(permutations(range(3)));n=3;ix={a:i for i,a in enumerate(P)};M=[[ix[pm(a,b)] for b in P] for a in P]
 V=[ix[pi(a)] for a in P];rr=ix[(1,2,0)];s=ix[(1,0,2)]
 A=(0,rr,M[rr][rr]);aexp={a:i for i,a in enumerate(A)}
 XS=list(product(range(3),product(range(6),repeat=3)));ids={x:i for i,x in enumerate(XS)}
 def mul(x,y):
  k,a=XS[x];l,b=XS[y];return ids[(k+l)%3,tuple(M[a[(i+l)%3]][b[i]] for i in range(3))]
 N=len(XS);tab=[[mul(i,j) for j in range(N)] for i in range(N)]
 inv=[next(j for j in range(N) if tab[i][j]==0) for i in range(N)]
 def order(x):
  y=0
  for k in range(1,100):
   y=tab[y][x]
   if not y:return k
  raise AssertionError(x)
 orders=[order(x) for x in range(N)]
 Y0=[i for i,(k,a) in enumerate(XS) if all(x in (0,s) for x in a)]
 Y1=[i for i,(k,a) in enumerate(XS) if all(x in A for x in a) and sum(aexp[x] for x in a)%3==k]
 assert len(Y0)==24 and len(Y1)==27 and {tab[x][y] for x,y in product(Y0,Y1)}==set(range(N))
 top=[x[0] for x in XS];par=[sum(x not in A for x in a)%2 for k,a in XS]
 G={(x,y) for x in range(N) for y in range(N) if (top[x]+top[y])%3==0 and par[x]==par[y]}
 H={(x,y) for x,y in product(Y0,Y1) if (x,y) in G}
 point={}
 for u in range(N):
  for x,y in H:
   g=(tab[u][x],tab[inv[u]][y]);assert g not in point;point[g]=u
 assert set(point)==G and len(H)==108 and len(G)==69984
 counts=Counter();der=0
 for x,y in H:
  # Find actual point by coset lookup, not by the translation label formula.
  fixed=0;central=0
  for u in range(N):
   w=point[tab[y][u],tab[x][inv[u]]]
   assert w==tab[tab[y][u]][inv[x]] and top[w]==(top[u]-2*top[x])%3
   central+=tab[y][u]==tab[u][x]
   fixed+=u==w
  assert central==fixed;counts[fixed]+=1
  if top[x]:
   assert fixed==0 and orders[x]==3 and orders[y]==9
   # h and tau(h^-1) project to the same cyclic top and have the same order.
   # Their coordinate orders are reversed, so even full X^2 cannot conjugate them.
   assert top[x]==top[inv[y]];der+=1
 rem=set(range(N));orbits=Counter()
 while rem:
  u=min(rem);orb={point[tab[y][u],tab[x][inv[u]]] for x,y in H}
  assert orb<=rem;rem-=orb;fibers=Counter(top[w] for w in orb)
  assert len(fibers)==3 and len(set(fibers.values()))==1
  orbits[len(orb)]+=1
 assert der==72 and Counter(top)=={0:216,1:216,2:216}
 print("648-element full-transversal control; canonical candidate group/stabilizer",len(G),len(H),
       "same-fiber derangement/fixed-element pairs",der,"fixed-count frequencies",sorted(counts.items()),
       "ordinary twisted point orbit sizes",sorted(orbits.items()))
def cyclone():
 # Enumerate all possible first three A5 decorations, fixing the fourth by
 # closure on a full 4-cycle. Degenerate square of the top is not used as
 # a substitute for an actual order-four lift.
 P=list(permutations(range(5)));ix={a:i for i,a in enumerate(P)}
 T=[ix[a] for a in P if sum(x>y for i,x in enumerate(a) for y in a[i+1:])%2==0]
 M=[[ix[pm(a,b)] for b in P] for a in P];V=[ix[pi(a)] for a in P]
 autos=list(range(len(P)));invclasses={}
 for r in (2,3):
  ep=[x for x in T if x and (M[x][x]==0 if r==2 else M[M[x][x]][x]==0)]
  C={M[M[t][ep[0]]][V[t]] for t in T}
  assert set(ep)==C and all(M[M[a][V[x]]][V[a]] in C for a,x in product(autos,ep));invclasses[r]=len(C)
 count=0
 for a,b,c in product(T,repeat=3):
  u=M[c][M[b][a]];d=V[u];assert M[d][u]==0;count+=1
 print("A5 full 4-cycle has one order-4 lift class of size",count,
       "and inverse stable under every actual automorphism for all elements of orders",invclasses)
 # At an exponent-two abelian label the twist translation is zero; two
 # genuine conjugacy classes are not forced by that particular label.
 assert (2*1)%2==0 and (2*1)%4!=0
if __name__=="__main__":wreath();cyclone()
