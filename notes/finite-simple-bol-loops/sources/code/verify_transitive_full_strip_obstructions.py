"""Finite controls for nilpotent-transitive-socle-proper-projections.md. Python 3, no dependencies."""
from itertools import permutations, product
from functools import lru_cache


@lru_cache(None)
def mul(a, b):
    return tuple(a[i] for i in b)


@lru_cache(None)
def inv(a):
    return tuple(a.index(i) for i in range(len(a)))


def conj(a, b):
    return mul(mul(a, b), inv(a))


def gen(e, gens):
    gs = set(gens)
    ans = {e}
    todo = [e]
    for x in todo:
        for g in gs:
            y = mul(x, g)
            if y not in ans:
                ans.add(y)
                todo.append(y)
    return frozenset(ans)


def parity(x):
    return sum(a > b for j, a in enumerate(x) for b in x[j+1:]) % 2


def allsubs(C, e):
    seen = {frozenset((e,))}
    todo = list(seen)
    for H in todo:
        for g in C-H:
            K = gen(e, H | {g})
            if K not in seen:
                seen.add(K)
                todo.append(K)
    return seen


def cosets(C, H):
    return sorted({tuple(sorted(mul(x, h) for h in H)) for x in C})


def perm_checks():
    tested = bad = sharp = nonnormal = multiple = 0
    for n, alt in [(3, False), (4, False), (4, True), (5, True)]:
        e = tuple(range(n))
        S = set(permutations(e))
        C = frozenset(g for g in S if not alt or parity(g) == 0)
        subs = allsubs(C, e)
        chosen_P = {}
        for P in sorted(subs, key=lambda H:(len(H),sorted(H))):
            if len(P) in (1,len(C)) or P in chosen_P: continue
            # Only core-free nontrivial P; all conjugacy types.
            orbit = {frozenset(conj(x,p) for p in P) for x in C}
            if set.intersection(*(set(h) for h in orbit)) != {e}: continue
            for other in orbit: chosen_P[other] = P
        for P in set(chosen_P.values()):
            X = cosets(C,P)
            owner = {x:i for i,Q in enumerate(X) for x in Q}
            Ms = [M for M in subs if P <= M]
            for r in S:
                if mul(r,r)!=e or {conj(r,p) for p in P}!=set(P): continue
                theta = {x:conj(r,x) for x in C}
                assert set(theta.values()) == set(C)
                for M in Ms:
                    U = gen(e,M|{theta[x] for x in M})
                    blocks = [frozenset(owner[y] for y in Y) for Y in cosets(C,M)]
                    approved, rejected = [], []
                    for p in P:
                        if mul(p,theta[p])!=e: continue
                        eta={x:conj(p,theta[x]) for x in C}
                        signed=tuple(owner[eta[Y[0]]] for Y in X)
                        assert mul(signed,signed)==tuple(range(len(X)))
                        unseen=set(range(len(X)))
                        components=[]
                        while unseen:
                            v=min(unseen)
                            stack=[v]; comp={v}
                            for j in stack:
                                adj=next(b for b in blocks if j in b)|{signed[j]}
                                for k in adj-comp: stack.append(k); comp.add(k)
                            unseen-=comp
                            x=X[v][0]
                            formula={owner[mul(a,h)] for a in (x,eta[x]) for h in U}
                            assert comp==formula
                            components.append(comp)
                        good=all(any(signed[i]==i for i in A) for A in components)
                        (approved if good else rejected).append(p)
                        if good: assert all(mul(inv(x),eta[x]) in U for x in C)
                        tested+=1; bad+=not good
                    if e not in approved: continue
                    if len(approved)>1: multiple+=1
                    ks={mul(mul(theta[x],theta[p]),inv(x)) for p in approved for x in C}
                    # theta(x p) x^-1 is the product t[x(pt)x^-1].
                    for p in approved:
                        assert all(conj(x,p) in U for x in C)
                    assert ks<=U
                    if gen(e,ks)==C:
                        sharp+=1
                        assert U==C
                        der=gen(e,{mul(conj(x,y),inv(y)) for x in C for y in C})
                        assert gen(e,M|der)==C
                        squares={mul(x,x) for x in C}
                        assert gen(e,P|der|squares)==C
                        if len(M)==2*len(P):
                            assert gen(e,{conj(x,p) for x in C for p in P})==C
                    if r==e and rejected and P<M<C:
                        # Old one-label shortcut, forced with a genuine nonnormal point stabilizer.
                        allks={conj(x,p) for p in rejected for x in C}
                        if gen(e,allks)==C: nonnormal+=1
    assert min(bad,sharp,nonnormal,multiple)>0
    print("signed coset/block tests, fixed-free components, passing generators, nonnormal adverse, multi-base-label:",tested,bad,sharp,nonnormal,multiple)


def cycles(n,*cs):
    v=list(range(n))
    for c in cs:
        for i,j in zip(c,c[1:]+c[:1]): v[i]=j
    return tuple(v)


def stable_class_checks():
    m=8; e=tuple(range(m))
    S=set(permutations(e)); A={x for x in S if parity(x)==0}
    # Don't cache the large group table: compare local orbit sets directly, including odd frame twists.
    def raw_conj(x,c):
        b=[0]*m
        for i in e: b[x[i]]=x[c[i]]
        return tuple(b)
    for c,sz in [(cycles(8,(0,1),(2,3)),210),(cycles(8,(0,1),(2,3),(4,5),(6,7)),105)]:
        inner={raw_conj(x,c) for x in A}
        assert {raw_conj(x,c) for x in S}==inner and len(inner)==sz
    e=tuple(range(5)); S=set(permutations(e)); A={x for x in S if parity(x)==0}
    F={x for x in A if x!=e and mul(x,x)==e}
    sqall={x for x in S if mul(x,x)==e}
    assert len(F)==15 and len(sqall)==26
    found=0
    for u in sqall-{e}:
        cl={conj(x,u) for x in A}
        hit={mul(x,y) for x in cl for y in cl}&F
        assert hit==F; found+=1
    assert not ({mul(e,e)}&F)
    print("A8 distinct Aut-invariant inner involution class sizes: 210,105; A5 fixed-arrow obstruction for",found,"nonidentity physical automorphisms, identity control fails as required")


def projective_field(p,f,mod):
    q=p**f; V=range(q)
    def vec(x):
        return tuple((x//(p**i))%p for i in range(f))
    def value(d):
        return sum((v%p)*p**i for i,v in enumerate(d))
    def fm(x,y):
        a,b=vec(x),vec(y); h=[0]*(2*f-1)
        for i in range(f):
            for j in range(f): h[i+j]+=a[i]*b[j]
        for k in range(2*f-2,f-1,-1):
            for j in range(f): h[k-f+j]-=h[k]*mod[j]
        return value(h[:f])
    add=[[value([i+j for i,j in zip(vec(x),vec(y))]) for y in V] for x in V]
    mult=[[fm(x,y) for y in V] for x in V]
    inverse=[0]+[next(y for y in V if mult[x][y]==1) for x in range(1,q)]
    def norm(x):
        k=inverse[next(v for v in x if v)]
        return tuple(mult[k][v] for v in x)
    def mm(a,b):
        return tuple(add[mult[a[i]][b[j]]][mult[a[i+1]][b[j+2]]] for i in (0,2) for j in (0,1))
    mats={norm((a,b,c,d)) for a,b,c,d in product(V,repeat=4) if mult[a][d]!=mult[b][c]}
    assert len(mats)==q*(q*q-1)
    phi=[]
    for x in V:
        y=1
        for _ in range(p): y=mult[x][y]
        phi.append(y)
    cnt=[]
    for j in range(f):
        z=0
        for A in mats:
            B=A
            for _ in range(j): B=tuple(phi[v] for v in B)
            if 2*j%f==0 and norm(mm(A,B))==(1,0,0,1): z+=1
        cnt.append(z)
    return len(mats),tuple(cnt)


def scalar_checks():
    expected=[(7,1,(0,),336,(50,)),(2,3,(1,1,0),504,(64,0,0)),(3,2,(1,0),720,(82,30))]
    for p,f,mod,n,cnt in expected:
        answer=projective_field(p,f,mod); assert answer==(n,cnt)
        print("PGL order and semilinear square-one count by field coset at q =",p**f,":",answer)
    roster=[(60,2),(168,2),(360,4),(504,3),(660,2),(1092,2),(2448,2),(2520,2),(3420,2),(4080,4),(5616,2),(6048,2),(6072,2),(7800,4),(7920,1),(9828,6)]
    assert [t for t,o in roster if not 3**200*o**141<t**59]==[60,168,360,504]
    assert 12**235<20160**59 and 12000**59>3**500 and 360**59>2**500
    assert 60**2>9**3 and 60>8
    assert 3*26>60 and 3*1<60 and 3*50<168 and 3*112<360 and 3*64<504
    # A genuinely nonregular odd nilpotent group: C3 wr C3 on its 9 points.
    n=9; e=tuple(range(n))
    a=cycles(n,(0,1,2)); b=cycles(n,(0,3,6),(1,4,7),(2,5,8))
    C=gen(e,[a,b]); assert len(C)==81 and len(C)==3**((n-1)//2)
    r=tuple(((-i//3)%3)*3+(-j)%3 for i in (0,3,6) for j in range(3))
    assert mul(r,r)==e and conj(r,a)==inv(a) and conj(r,b)==inv(b)
    marked={mul(c,r) for c in C if mul(mul(c,r),mul(c,r))==e}
    fixed=[sum(v==i for i,v in enumerate(m)) for m in marked]
    assert max(fixed)<=3 and gen(e,[mul(r,m) for m in marked])==C
    print("16 simple orders below 12000, four refined-bound exceptions; nine-point nonregular nilpotent control: group order, square-one labels, fixed counts",len(C),len(marked),sorted(set(fixed)))


if __name__=="__main__":
    perm_checks(); stable_class_checks(); scalar_checks()
