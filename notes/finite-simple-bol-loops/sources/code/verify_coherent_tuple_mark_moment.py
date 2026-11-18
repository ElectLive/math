"""Exact finite controls for the coherent tuple moment and even-field PSL2 reduction."""
from itertools import permutations, product, combinations
from collections import Counter
from functools import lru_cache


def cm(x,y):
    return tuple(x[i] for i in y)


def iv(x):
    return tuple(x.index(i) for i in range(len(x)))


def cj(x,y):
    return cm(cm(x,y),iv(x))


def sg(x):
    return sum(a>b for i,a in enumerate(x) for b in x[i+1:])%2


def gen(e,gs):
    ans={e}; queue=[e]
    for x in queue:
        for g in gs:
            y=cm(x,g)
            if y not in ans: ans.add(y); queue.append(y)
    return frozenset(ans)


def subgroups(C,e):
    seen={frozenset((e,))}; queue=list(seen)
    for P in queue:
        for g in C-P:
            M=gen(e,P|{g})
            if M not in seen: seen.add(M);queue.append(M)
    return seen


def order(x):
    e=tuple(range(len(x)));y=x;i=1
    while y!=e: y=cm(y,x);i+=1
    return i


def action_moments():
    # Rotation group C4, regular on binary square, formal inversion represented by a reflection.
    Q=list(product(range(2),repeat=2)); idx=Q.index
    r=tuple(idx((y,1-x)) for x,y in Q); t=tuple(idx((y,x)) for x,y in Q);e=tuple(range(4))
    G=gen(e,(r,)); L={cm(t,k) for k in G}
    assert len(G)==len(L)==len(Q) and G.isdisjoint(L)
    assert all(cm(a,a)==e for a in L) and set(cj(g,a) for a in L for g in G)==L
    assert all(Counter(a[i] for a in L)==Counter(e) for i in e)
    dec=[]
    for a in L:
        flip=Q[a[0]]
        swap=(Q[a[idx((1,0))]][1]!=flip[1])
        dec.append((swap,flip))
    assert len({flip for swap,flip in dec if swap})==2
    for z1,z2 in product(range(-3,4),repeat=2):
        value=sum((1+z1*z2) if swap else (1+(-1)**flip[0]*z1)*(1+(-1)**flip[1]*z2) for swap,flip in dec)
        assert value==4
    # An arbitrary outside involution class is not automatically a uniform transversal.
    swapped=[a for a in L if Q[a[idx((1,0))]][1]!=Q[a[0]][1]]
    assert len({a[0] for a in swapped})<len(Q)
    assert sum(2*(not sw) for sw,_ in dec)==len(L)*2//2
    print("genuine C4 square transversal: 4 marked reflections, all 16 source-target multiplicities one, 49 two-variable identities; fixed-free-subset control rejected")


def small_a5():
    e=tuple(range(5)); S=frozenset(permutations(e)); T=frozenset(g for g in S if not sg(g))
    subs=subgroups(T,e); tors={h for h in subs if len(h)==5}
    geom=[set(range(5)),set(combinations(range(5),2)),tors]
    def act(g,y,k):
        if k==0:return g[y]
        if k==1:return tuple(sorted(g[i] for i in y))
        return frozenset(cj(g,h) for h in y)
    kinds=Counter()
    for U in subs-{frozenset((e,)),T}:
        N=[g for g in S if frozenset(cj(g,h) for h in U)==U]
        hits=[]
        for k,Y in enumerate(geom):
            if any(all(act(g,y,k)==y for g in N) for y in Y):hits.append(k)
        assert hits
        kinds[tuple(hits)]+=1
    bytype={}
    for g in S:
        if cm(g,g)!=e:continue
        key=(g==e,sg(g))
        row=tuple(sum(act(g,y,k)==y for y in Y) for k,Y in enumerate(geom))
        assert row==bytype.setdefault(key,row)
    assert bytype=={(True,0):(5,10,6),(False,0):(1,2,2),(False,1):(3,4,0)}
    assert sum(kinds.values())==len(subs)-2 and kinds[(2,)]>0
    print("all actual proper nontrivial A5 subgroups, S5-normalizer geometry classes:",sum(kinds.values()),sorted(kinds.items()))
    print("A5 point/pair/nonsplit geometry fixed counts for id, inner, half-field:",bytype[(True,0)],bytype[(False,0)],bytype[(False,1)])


def subfield16():
    q=16; inf=16
    def m(x,y):
        v=0
        while y:
            if y&1:v^=x
            y//=2;x*=2
            if x&16:x^=19
        return v
    def pw(x,e):
        y=1
        while e:
            if e&1:y=m(x,y)
            x=m(x,x);e//=2
        return y
    invs=[0]+[pw(x,14) for x in range(1,q)]
    def pgl(a,b,c,d):
        def at(x):
            y,z=(a,c) if x==inf else (m(a,x)^b,m(c,x)^d)
            return inf if not z else m(y,invs[z])
        return tuple(at(x) for x in range(q+1))
    G=set()
    for i in range(4):
        for tail in product(range(q),repeat=3-i):
            a,b,c,d=(0,)*i+(1,)+tail
            if m(a,d)!=m(b,c):G.add(pgl(a,b,c,d))
    assert len(G)==4080
    Y0=frozenset([inf]+[x for x in range(q) if pw(x,4)==x])
    Y={frozenset(g[x] for x in Y0) for g in G}
    assert len(Y0)==5 and len(Y)==68
    t=tuple(pw(x,4) if x!=inf else inf for x in range(q+1))
    A={g for g in G if frozenset(g[x] for x in Y0)==Y0}
    assert len(A)==60 and {x for x in range(q+1) if any(g[x]==x for g in A if order(g)==2)}==set(Y0)
    def fixed_sub(g):return sum(frozenset(g[x] for x in y)==y for y in Y)
    ident=tuple(range(q+1))
    inner=[g for g in G if g!=ident and cm(g,g)==ident]
    half={cm(g,t) for g in G if cm(cm(g,t),cm(g,t))==ident}
    assert len(inner)==255 and len(half)==68
    ans=(set(fixed_sub(g) for g in inner),set(fixed_sub(g) for g in half));assert min(ans[0]|ans[1])>0
    print("PSL2(16) subfield geometry: 68 real sublines, 60-element point stabilizer; fixed sublines on all 255 inner/68 half-field involutions:",tuple(sorted(x) for x in ans))


def packing():
    for f in range(2,180):
        q=2**f;L=q*(q*q-1); M=2*(q+1)
        I=q*q+((1<<(f//2))*(q+1) if not f%2 else 0)
        assert L*f<q**4
        if f>=4: assert L*L>4*I*I*M
        if f==2: assert L*L<4*I*I*M
    assert 4080**2>4*324**2*34
    print("178 integral field bounds, including strict q=16 and the genuine q=4 failure.")


if __name__=="__main__":
    action_moments(); small_a5(); subfield16(); packing()
