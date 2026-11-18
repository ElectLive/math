"""Independent hostile actual finite tests, not a search for a simple loop."""
from itertools import product,permutations,combinations
from collections import Counter
# Heisenberg group UT_3(3) and a nonnormal, core-free index-nine point stabilizer.
C=set(product(range(3),repeat=3));e=(0,0,0)
def mul(a,b):return ((a[0]+b[0])%3,(a[1]+b[1])%3,(a[2]+b[2]+a[0]*b[1])%3)
def inv(a):return (-a[0]%3,-a[1]%3,(a[0]*a[1]-a[2])%3)
def sub(g):
 g=set(g);D={e};todo=[e]
 for x in todo:
    for a in g:
        z=mul(x,a)
        if z not in D:todo.append(z);D.add(z)
 return D
P=sub({(1,0,0)});M9=sub(P|{(0,0,1)})
def left(a,U):return frozenset(mul(a,u) for u in U)
coset={a:left(a,P) for a in C};omega=set(coset.values());assert len(omega)==9
conj=lambda x,g:mul(mul(x,g),inv(x))
core=set.intersection(*({conj(x,p) for p in P} for x in C));assert core=={e}
total=perms=bad=passgen=multigen=0; stats=Counter()
for sx,sy in product((1,2),repeat=2):
 def theta(x):return (sx*x[0]%3,sy*x[1]%3,sx*sy*x[2]%3)
 assert {theta(p) for p in P}==P and all(theta(mul(x,y))==mul(theta(x),theta(y)) for x in C for y in C)
 for M in [P,M9,C]:
    U=sub(M|{theta(x) for x in M})
    allowed={}; gens={}
    for p in P:
        if mul(p,theta(p))!=e:continue
        def eta(x):return conj(p,theta(x))
        blocks={x:left(x,M) for x in C};A={B:set() for B in omega}
        actions={B:coset[eta(next(iter(B)))] for B in omega}
        for B in omega:
            A[B].add(actions[B]);x=next(iter(B))
            for y in blocks[x]:A[B].add(coset[y])
        unseen=set(omega);Pcomp=[]
        while unseen:
            y=unseen.pop();cc={y};todo=[y]
            for v in todo:
                for w in A[v]&unseen:unseen.remove(w);cc.add(w);todo.append(w)
            Pcomp.append(cc)
            x=next(iter(y));expect={coset[z] for z in left(x,U)|left(eta(x),U)}
            assert cc==expect;total+=1
        ok=all(any(actions[z]==z for z in a) for a in Pcomp)
        allowed[p]=ok;bad+=not ok;perms+=1
        gens[p]={mul(theta(mul(x,p)),inv(x)) for x in C}
    keys=list(allowed)
    for k in range(1,len(keys)+1):
      for J in combinations(keys,k):
        if e not in J:continue
        X=sub(set.union(*(gens[p] for p in J)))
        if all(allowed[p] for p in J) and X==C:
            assert M==C and len(omega)%2==1
            passgen+=1;multigen+=len(J)>1
        stats[(all(allowed[p] for p in J),X==C)]+=1
assert bad and passgen and multigen
print("UT3(3) nine-site nonregular P: 4 automorphism choices, 3 closed subgroups; component/label/failing-label checks",total,perms,bad)
print("actual selected signed-class families: passing AND generating",passgen,"with multiple base labels",multigen,"; pass/generate table",sorted(stats.items()))
# Real conjugates/products on S=A5^3: pair coordinates always one genuine inner coset of S5.
S=list(permutations(range(5)));I=tuple(range(5))
def pm(a,b):return tuple(a[y] for y in b)
def pi(a):return tuple(a.index(x) for x in range(5))
def sign(a):return sum(x>y for i,x in enumerate(a) for y in a[i+1:])%2
A5=[s for s in S if not sign(s)];invS=[s for s in S if pm(s,s)==I];v4=[s for s in invS if sum(a==b for a,b in zip(s,I))==1]
assert len(invS)==26 and len(v4)==15
K={b:{pm(pm(a,b),pi(a)) for a in A5} for b in invS}
fg={}
for b in invS:
 for x in K[b]:
    for y in K[b]:
        z=pm(x,y)
        if z in v4:fg[b,z]=x,y
cf={(z,h):next(f for f in S if sign(f)==h and pm(f,z)==pm(z,f)) for z in v4 for h in (0,1)}
nbr=0
for b,s,z in product(invS,S,v4):
    if b==I:
        assert (b,z) not in fg;continue
    x,y=fg[b,z];f=cf[z,sign(s)];g=pm(f,z)
    # Both swapped return arrows are inverses; left multipliers exhibit INNER conjugacy to s.
    assert not sign(pm(f,pi(s))) and not sign(pm(g,pi(s)))
    assert pm(x,y)==pm(pi(f),g)==pm(f,pi(g))==z
    nbr+=1
print("explicit diagonal double-transposition products of TWO real A5^3-conjugates:",nbr,"; identity fixed arrow is genuine exception")
# Restricted constant outer kernel versus unrestricted outer arrows in a fixed reflection.
# Enumerate the three chosen labels (arrow at fixed site, one arrow on paired sites, its inverse).
free=len(invS)*len(S);rest=sum(sign(b)==sign(f) for b in invS for f in S)
ident=sum(not sign(f) for f in S)
assert free==3120 and rest==1560 and ident==60
print("one genuine 3-site reflection: unrestricted 3120 vs constant outer stabilizer 1560; identity fixed arrow in restricted fiber 60")
