"""Direct finite wreath-coordinate controls. Standard library; no simple-loop claim."""
from itertools import permutations,product
from collections import Counter,defaultdict
from math import gcd,prod
from random import Random
R=Random(43161)
def pm(a,b):return tuple(a[i] for i in b)
def pi(a):return tuple(a.index(i) for i in range(len(a)))
class Letters:
 def __init__(self,n):
  P=list(permutations(range(n)));self.P=P; ix={a:i for i,a in enumerate(P)}
  self.S=list(range(len(P))); self.e=0
  self.T=[i for i,a in enumerate(P) if sum(x>y for k,x in enumerate(a) for y in a[k+1:])%2==0]
  self.par=[int(i not in self.T) for i in self.S]
  self.m=[[ix[pm(a,b)] for b in P] for a in P]
  self.v=[ix[pi(a)] for a in P]
  self.cl=[min(self.m[self.m[t][x]][self.v[t]] for t in self.T) for x in self.S]
  self.cls=Counter(self.cl);self.cos=[self.T,sorted(set(self.S)-set(self.T))]
# Wreath means all arrows in Sym(n); inner kernel A_n. For n=5 these
# are actual nonabelian-simple centerless coordinates with outer automorphisms.
def wmul(g,h,L):
 s,a=g;t,b=h;return pm(s,t),tuple(L.m[a[t[i]]][b[i]] for i in range(len(s)))
def winv(g,L):
 s,a=g;u=pi(s);return u,tuple(L.v[a[u[i]]] for i in range(len(s)))
def wo(g,L):
 s,a=g;e=(tuple(range(len(s))),(0,)*len(s));x=e
 for k in range(1,400):
  x=wmul(x,g,L)
  if x==e:return k
 raise AssertionError(g)
def out(g,L):return g[0],tuple(L.par[z] for z in g[1])
def sig(g,L):
 s,a=g
 return out(g,L),tuple((i,L.cl[x]) for i,x in enumerate(a) if s[i]==i)
def cycles(p):
 rem=set(range(len(p)));acc=[]
 while rem:
  i=min(rem);c=[]
  while i in rem:rem.remove(i);c.append(i);i=p[i]
  acc.append(c)
 return acc
def invclasses(L,k,perms):
 ident=tuple(range(k));e=(ident,(0,)*k);D=defaultdict(list)
 for s in perms:
  if pm(s,s)!=ident:continue
  for a in product(L.S,repeat=k):
   if any(L.m[a[s[i]]][a[i]] for i in range(k)):continue
   g=(s,a);D[sig(g,L)].append(g)
 for (u,fixed),v in D.items():
  assert len(v)==len(L.T)**(sum(i!=u[0][i] for i in range(k))//2)*prod(L.cls[x] for i,x in fixed)
 return D
def solver(h,la,lb,L):
 (rho,tags),fa=la;(eta,etags),fb=lb;fa=dict(fa);fb=dict(fb)
 sigma,hv=h;k=len(rho);identity=tuple(range(k))
 if pm(rho,eta)!=sigma:return False
 # Complete OUTER product, not just the permutation.
 if tuple(tags[eta[i]]^etags[i] for i in range(k))!=out(h,L)[1]:return False
 C=cycles(sigma);sets={frozenset(c):c for c in C};rem=set(sets);invperm=pi(sigma)
 while rem:
  v=min(rem,key=lambda c:min(c));c=sets[v];partner=frozenset(rho[j] for j in c);rem.discard(v);rem.discard(partner);hit=False
  for z in L.cos[tags[c[0]]]:
   A={c[0]:z};ok=True
   for j in c:
    q=sigma[j];a=L.m[L.m[L.v[hv[invperm[rho[j]]]]][A[j]]][L.v[hv[j]]]
    if q in A and A[q]!=a:ok=False;break
    A[q]=a
   if not ok:continue
   if partner!=v:
    for j in c:A[rho[j]]=L.v[A[j]]
   for j,a in A.items():
    if L.par[a]!=tags[j] or L.m[A[rho[j]]][a]:ok=False;break
    if j in fa and L.cl[a]!=fa[j]:ok=False;break
    if j in fb and L.cl[L.m[A[sigma[j]]][hv[j]]]!=fb[j]:ok=False;break
   if ok:hit=True;break
  if not hit:return False
 return True
def sample_reversals(L,k,perms,n):
 D=invclasses(L,k,perms);keys=list(D);ans=0;ct=Counter()
 for it in range(n):
  la,lb=R.choice(keys),R.choice(keys)
  x,y=R.choice(D[la]),R.choice(D[lb]);h=wmul(x,y,L)
  if it%2:
   i=R.randrange(k);a=list(h[1]);a[i]=L.m[R.choice(L.T)][a[i]];h=h[0],tuple(a)
  right=set(D[lb]);direct=any(wmul(x,h,L) in right for x in D[la])
  calc=solver(h,la,lb,L);assert calc==direct,(h,la,lb,calc,direct)
  ans+=calc;cs=cycles(h[0]);pairs=sum(frozenset(la[0][0][i] for i in c)!=frozenset(c) for c in cs)//2
  ct[(bool(pairs),len(cs)>2)]+=1
 print('wreath reversal',len(L.P),k,'distinct decorated labels',len(keys),'checks/positive',n,ans,'cycle shapes',dict(ct))
 return D
def projection_controls(L):
 k=3;perm=tuple(range(k));swap=(1,0,2)
 D=invclasses(L,k,(swap,));ls=list(D);tests=0
 for C in ((),(0,),(0,2),(0,1),(1,2),(0,1,2)):
  # B comprises independent outer signs. Quotient out all signs on D only.
  for trial in range(15):
   sel=R.sample(ls,R.randrange(1,len(ls)+1));images=set();pred={}
   for u,f in sel:
    fp=dict(f);s,tags=u
    # alpha=swap, with identity arrows; bar(alpha*u) retains these tags.
    restriction=(tuple(tags[i] for i in C),tuple((i,fp[i]) for i in C if s[i]==i))
    w=len(L.T)**sum(any(i in C for i in cyc) for cyc in cycles(s) if len(cyc)==2)*prod(L.cls[fp[i]] for i in C if s[i]==i)
    assert pred.setdefault(restriction,w)==w
    images.update((tuple(tags[i] for i in C),tuple(z[1][i] for i in C)) for z in D[(u,f)])
   assert sum(pred.values())==len(images);tests+=1
 print('cut-signature checks, including cuts split by inversion and forgotten fixed labels',tests)
def hols(g,L):
 s,a=g;e=0;out=[]
 for c in cycles(s):
  x=e
  for i in c:x=L.m[a[i]][x]
  out.append(L.cl[x])
 return tuple(out)
def order_lifts(L):
 for s,tags in (((1,0),(1,1)),((1,0,2),(0,0,0)),((1,0,2),(1,1,1))):
  k=len(s);m=2;C=cycles(s)
  pred={}
  for c in C:
   o=sum(tags[i] for i in c)%2;r=m//len(c)
   pred[c[0]]=set(L.cl[t] for t in L.cos[o] if (t==0 if r==1 else L.m[t][t]==0))
  # Enumerate fully for rank two; for a fixed third coordinate only its
  # involutions can contribute. All lifts with order two are then exhausted.
  cnt=Counter()
  for a in product(*(L.cos[t] if s[i]!=i else [x for x in L.cos[t] if L.m[x][x]==0] for i,t in enumerate(tags))):
   if any(L.m[a[s[i]]][a[i]] for i in range(k)):continue
   cnt[hols((s,a),L)]+=1
  expect={v:prod(len(L.T)**(len(c)-1)*L.cls[x] for c,x in zip(C,v)) for v in product(*(pred[c[0]] for c in C))}
  assert cnt==expect,(cnt,expect)
  print('A5 outer-coset order-two lifts; cycles/tags, actual classes and weights',s,tags,dict(cnt))
def true_socle_controls(L):
 # True radical-free G=S5 x S5 with simple socle A5 x A5. Compute all
 # principal normal closures directly; join closure then certifies ALL normals.
 n=len(L.P);G=range(n*n);q=lambda a,b:a*n+b
 def mul2(a,b):return q(L.m[a//n][b//n],L.m[a%n][b%n])
 def span(s):
  src=[];H={0}
  for g in s:
   if g in H:continue
   src.append(g);todo=[0];H={0}
   while todo:
    h=todo.pop()
    for y in src:
     z=mul2(h,y)
     if z not in H:H.add(z);todo.append(z)
  return frozenset(H)
 classes={}
 for x,p in enumerate(L.P):classes.setdefault(tuple(sorted(map(len,cycles(p)))),[]).append(x)
 cls=list(classes.values())
 Bs=[{0},{0,1},{0,2},{0,3},{0,1,2,3}]
 N={}
 for D in range(4):
  for B in Bs:
   if any((b&D)!=b for b in B):continue
   N[D,tuple(sorted(B))]=frozenset(g for g in G if (D&1 or g//n==0) and (D&2 or g%n==0)
     and L.par[g//n]+2*L.par[g%n] in B)
 vals=set(N.values());assert len(vals)==10
 princ=set()
 for X,Y in product(cls,repeat=2):
  z=q(X[0],Y[0]);P=span(q(x,y) for x,y in product(X,Y))
  assert P==min((Q for Q in vals if z in Q),key=len)
  princ.add(P)
 cur={frozenset({0})}
 while True:
  plus=set()
  for U,V in product(cur,princ):
   J=min((Q for Q in vals if U<=Q and V<=Q),key=len)
   assert len(J)*len(U&V)==len(U)*len(V)
   plus.add(J)
  if plus<=cur:break
  cur|=plus
 assert vals==cur
 H={q(a,a) for a in L.S};A={q(a,a) for a in L.T};t=next(x for x in L.S if L.par[x]);ns={0:0,3:q(t,t)}
 K={q(L.v[a],a) for a in L.S}
 assert span(K)==frozenset(g for g in G if L.par[g//n]==L.par[g%n])
 for (D,B),M in N.items():
  rest=lambda g:tuple(v for i,v in enumerate(divmod(g,n)) if not D&(1<<i))
  Ac={rest(a) for a in A};pred=sum(1 for a in A if not any(rest(a)))*sum(j in B and rest(v) in Ac for j,v in ns.items())
  assert pred==len(H&M)
  # Distinct actual quotient signatures on α-swapping marks versus direct cosets.
  def key(g):
   top=L.par[g//n]+2*L.par[g%n];return min(top^b for b in B),rest(g)
  actual=len({key(k) for k in K})
  weight=(len(L.T) if D!=3 else 1)
  sigs={min(j^b for b in B) for j in (0,3)}
  assert actual==weight*len(sigs)
 assert span([q(x,0) for x,p in enumerate(L.P) if sum(i!=z for i,z in enumerate(p))==2])==frozenset(q(x,0) for x in L.S)
 print("S5 x S5: 49 direct principal normal closures, all",len(vals),"normals; diagonal H intersections, split-by-inversion cuts, projected-vs-active generation")
def wcompareouter(g,L):return out(g,L)
def odd_semiregular(L):
 # Full direct enumeration of the order-3 lift class over each signed
 # three-cycle of prescribed outer parity, then search for actual inversion.
 s=(1,2,0);rho=(0,2,1);e=(tuple(range(3)),(0,0,0));rs=[x for x in L.S if L.m[x][x]==0]
 choices=[]
 for bits in product((0,1),repeat=3):
  if sum(bits)%2:continue
  G=[]
  for x in L.cos[bits[0]]:
   for y in L.cos[bits[1]]:
    z=L.v[L.m[y][x]]
    G.append((s,(x,y,z)))
  assert len(G)==len(L.T)**2 and all(wmul(wmul(g,g,L),g,L)==e for g in G)
  choices.append((bits,G))
 cases=0
 for bits,G in choices:
  for it in range(35):
   x=R.choice(rs);y=R.choice(L.S);a=(rho,(x,y,L.v[y]));ai=winv(a,L)
   if out(wmul(wmul(a,G[0],L),ai,L),L)!=out(winv(G[0],L),L):continue
   g=next((g for g in G if wmul(wmul(a,g,L),a,L)==winv(g,L)),None)
   assert g is not None
   # Product of the original mark and a conjugate equals a generator:
   w=wmul(a,wmul(wmul(winv(g,L),a,L),g,L),L);assert w in (g,winv(g,L))
   cases+=1
 print("A5 cubed: actual odd dihedral lifts for",cases,"outer-compatible selected reflectors among four complete order-three lift classes")
 # True sharp boundary: in A5^3, one order-three decoration on a rotating
 # cycle gives order nine, with cube an actual full-support element of order 3.
 x=next(x for x in L.T if x and L.m[L.m[x][x]][x]==0)
 h=(s,(x,0,0));z=wmul(wmul(h,h,L),h,L);assert wo(h,L)==9 and wo(z,L)==3 and all(z[1])
 # Counterexample to dropping 'odd': in A5^2 the top swap is reversed
 # modulo inners by the actual fixed-coordinate (1,u), u an involution.
 # No order-two swap commutes with it (the two actual decorations differ).
 u=next(x for x in L.T if x and L.m[x][x]==0);a=((0,1),(0,u));sw=(1,0)
 assert not any(wmul(a,(sw,(v,L.v[v])),L)==wmul((sw,(v,L.v[v])),a,L) for v in L.T)
 print("sharp 9-to-3 support example; even-order fixed-class shortcut rejected")
def main():
 L=Letters(5);small=Letters(4)
 sample_reversals(L,2,((0,1),(1,0)),350)
 sample_reversals(small,3,tuple(permutations(range(3))),650)
 # Four coordinates allow two full sigma-cycles interchanged by rho.
 sample_reversals(small,4,tuple(permutations(range(4))),800)
 projection_controls(small);order_lifts(L);true_socle_controls(L);odd_semiregular(L)
if __name__=='__main__':main()
