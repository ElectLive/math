"""Independent hostile extension, gauge, tilted-section, nonnormal-generation controls; no simple-loop fixture claimed."""
from itertools import product,permutations
from collections import Counter
def group_ops(univ,mul,e):
    G=frozenset(univ);inv={x:next(y for y in G if mul(x,y)==e) for x in G}
    def span(els):
        src=tuple(els);s={e};w=[e]
        while w:
            x=w.pop()
            for a in src:
                y=mul(x,a)
                if y not in s:s.add(y);w.append(y)
        return frozenset(s)
    def conj(x,S):return frozenset(mul(mul(x,s),inv[x]) for s in S)
    hs={frozenset({e})};w=list(hs)
    while w:
        k=w.pop()
        for x in G-k:
            h=span(k|{x})
            if h not in hs:hs.add(h);w.append(h)
    norms={h for h in hs if all(conj(x,h)==h for x in G)}
    return G,inv,span,conj,hs,norms
# Q8 x C2, represented by actual signed i^a j^b and an extra central e.
V4=list(product((0,1),repeat=2));zero=(0,0,0,0)
def mul(x,y):
    s,a,b,e=x;t,c,d,h=y
    return (s^t^(a*c)^(b*d)^(b*c),a^c,b^d,e^h)
def tau(x):
    s,a,b,e=x;return s^(a*b),b,a,e
Q,inv,span,conj,hs,norm=group_ops(product((0,1),repeat=4),mul,zero)
assert all(tau(tau(g))==g and tau(mul(g,h))==mul(tau(g),tau(h)) for g,h in product(Q,repeat=2))
central=frozenset(x for x in Q if all(mul(x,y)==mul(y,x) for y in Q));assert len(central)==4
omega={x for x in central if mul(x,x)==zero};assert omega==central and len(omega)==4
H=span([(0,1,0,0)]);N=span([(0,1,0,1)]);U=N&central;W=H&central
proj=lambda g:(g[1],g[2])
assert N in norm and {tau(n) for n in N}!=N and set(map(proj,H))==set(map(proj,N))
HN={mul(h,n) for h,n in product(H,N)}
assert len(U)==len(W)==2 and len(HN&central)==4 and {mul(u,w) for u,w in product(U,W)}==U
# Explicit coordinates in the whole formal extension, TWO biased sections, including t fixed in each.
E=frozenset(product(Q,(0,1)));one=(zero,0);t0=(zero,1)
def em(x,y):
    a,b=x;c,d=y;return mul(a,tau(c) if b else c),b^d
def PR(x):return x[0][1],x[0][2],x[1]
X=frozenset(map(PR,E));V=frozenset(it for it in E if PR(it)==(0,0,0));invE={x:next(y for y in E if em(x,y)==one) for x in E}
def EC(g,a):return em(em(g,a),invE[g])
def base(q,which):
    a,b,k=q
    s,h=((a&(1^k))^b,a^(b&k)) if which else (0,0)
    return (s,a,b,h),k
def vec(x):return x[0][0],x[0][3]
def vecelt(x):return (x[0],0,0,x[1]),0
def xor(*xs):return (sum(v[0] for v in xs)%2,sum(v[1] for v in xs)%2)
def xm(x,y):return PR(em(base(x,0),base(y,0)))
def decomp(el,k):return vec(em(el,invE[base(PR(el),k)]))
def act(x,v):return vec(EC(base(x,0),vecelt(v)))
def f(x,y,k):return decomp(em(base(x,k),base(y,k)),k)
def shift(x):return decomp(base(x,0),1)
assert shift((0,0,1))==shift((0,0,0))==(0,0)
assert any(shift(x)!=(0,0) for x in X)
assert all(xor(f(x,y,0),shift(xm(x,y)))==xor(shift(x),act(x,shift(y)),f(x,y,1)) for x,y in product(X,repeat=2))
outer={x for x in E if x[1] and em(x,x)==one}
classes={frozenset(EC(y,x) for y in E) for x in outer}
tcl=next(c for c in classes if t0 in c);other=list(classes-{tcl});gauge_ct=strict_ct=extra_witness=0
for take in product((0,1),repeat=len(other)):
    M=tcl.union(*(c for c,k in zip(other,take) if k))
    fibers=[{q:{decomp(x,i) for x in M if PR(x)==q} for q in set(map(PR,M))} for i in (0,1)]
    for q,S in fibers[0].items():
        assert {xor(v,shift(q)) for v in S}==fibers[1][q]
        D={xor(v,act(q,v)) for v in V4}
        assert all({xor(v,d) for d in D}<=S for v in S)
        gauge_ct+=1
    sq={em(a,b)[0] for a,b in product(M,repeat=2)}
    obs=bool(sq&(HN-N));hn_co=0
    for j in set(map(proj,H)):
        for d in set(map(proj,N)):
            h=next(g for g in H if proj(g)==j);n=next(g for g in N if proj(g)==d)
            off=mul(h,n);fiber={mul(off,w) for w in W|U} # W=U central in this specific example
            assert fiber=={mul(a,b) for a,b in product(H,N) if proj(a)==j and proj(b)==d}
            A=sq&fiber
            if A-N:hn_co+=1
    assert obs==bool(hn_co);strict_ct+=1
    extra_witness+=bool(sq&(HN&central)-U)
print(f'Q8 x C2: true canonical central elementary layer 4; tilted C4 lifts H,N share projection/kernel, N is not t-stable, |(HN)∩V|=4 vs |W+U|=2; {gauge_ct} actual phase-fiber transports across nontrivial normalized gauges, {strict_ct} true mark-mask comparisons, {extra_witness} detect additional purely vertical product.')
# S4 binary faithful module and nonnormal complements: a single point stabilizer surjects on S3, but generates only itself.
S4=frozenset(permutations(range(4)));id4=tuple(range(4))
def smul(a,b):return tuple(a[b[i]] for i in range(4))
S,si,sg,sc,subs,ns=group_ops(S4,smul,id4)
V=frozenset(g for g in S if g==id4 or all(g[g[i]]==i and g[i]!=i for i in range(4)))
assert len(V)==4 and V in ns
qcos=lambda g:frozenset(smul(g,v) for v in V)
surj={k for k in subs if k!=S and len({qcos(g) for g in k})==6}
assert len(surj)==4 and all(len(k)==6 and not(k in ns) for k in surj)
d=next(iter(surj));gs=[x for x in d if any(i==x[i] for i in range(4)) and x!=id4]
assert sg(gs)==d and len(set(map(qcos,gs))|{qcos(id4)})==6
# Of the six quotient classes, precisely identity centralizes V; O3(S3) therefore has no nontrivial normal lift.
assert {qcos(g) for g in S if all(smul(g,v)==smul(v,g) for v in V)}=={V}
assert all(len(h)!=3 for h in ns)
print('S4/V4=S3: all four proper surjecting subgroups are nonnormal point stabilizers, but every normal-generation-only test would miss them; O3(S3) has no lift to a normal 3-subgroup of S4.')
# Anchor is not phase data in characteristic two: both decompose the same genuine invariant fiber in an elementary abelian formal ambient group.
B={(0,0),(1,0),(0,1)};a=(1,0);C={xor(x,a) for x in B}
assert B!=C and (0,0) in C and {xor(x,a) for x in C}==B
print('Binary anchor obstruction: two distinct pointed 3-of-4 shapes and anchors define literally the same actual marked fiber; equality of shapes would overcount.')
