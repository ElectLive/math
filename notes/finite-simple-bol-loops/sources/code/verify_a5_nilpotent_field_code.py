"""Exact controls for the residual A5 field-code obstruction. Standard-library Python."""
from itertools import permutations, product
from collections import Counter


def comp(x,y):
    return tuple(x[i] for i in y)


def inv(x):
    return tuple(x.index(i) for i in range(len(x)))


def cj(x,y):
    return comp(comp(x,y), inv(x))


def gen(e,gs):
    ans={e}; todo=[e]
    for x in todo:
        for g in gs:
            y=comp(x,g)
            if y not in ans:ans.add(y);todo.append(y)
    return frozenset(ans)


def subs(C,e):
    seen={frozenset((e,))}; todo=list(seen)
    for H in todo:
        for g in C-H:
            P=gen(e,H|{g})
            if P not in seen:seen.add(P);todo.append(P)
    return seen


def parity(x):
    return sum(a>b for j,a in enumerate(x) for b in x[j+1:])%2


def a5_layer():
    e=tuple(range(5)); S=set(permutations(e)); T={x for x in S if not parity(x)}
    r=(1,2,3,4,0);tor=gen(e,[r])
    N={g for g in S if frozenset(cj(g,h) for h in tor)==tor}
    D=N&T; refl=D-tor
    assert len(N)==20 and len(D)==10 and len(refl)==5
    assert all(comp(g,g) in refl for g in N-D)
    assert all(comp(g,g)==e and g in T for g in refl)
    actual=0
    for f in S:  # arbitrary exchange arrow, including odd
        for a,b in product(refl,repeat=2):
            # For a marked pair let its two opposed arrows be X, X^-1
            # in the prescribed coset. Their square products realize (a,b)
            # iff one transported inverse can be matched by an inner conjugator.
            assert any(cj(comp(h,f),a)==inv(b) for h in T)
            actual+=1
    tori={frozenset(cj(g,a) for a in tor) for g in T}
    invol=[g for g in S if parity(g) and comp(g,g)==e]
    assert len(tori)==6 and len(invol)==10
    assert all(all(frozenset(cj(g,a) for a in m)!=m for m in tori) for g in invol)
    print("F20 actual odd squares and reflection-pair witnesses:",len(N-D),actual,"; outer transpositions fixing a torus: 0/10")


def bitperm(p,v):
    return sum(((v>>i)&1)<<p[i] for i in range(len(p)))


def codes(n):
    seen={frozenset((0,))};todo=list(seen)
    for W in todo:
        for v in set(range(1<<n))-W:
            A=W|{v^w for w in W}
            if A not in seen:seen.add(A);todo.append(A)
    return seen


def arrow_tests():
    n=4; e=tuple(range(n)); S=frozenset(permutations(e)); Cs=[C for C in subs(S,e) if not len(C)&(len(C)-1) and {c[0] for c in C}==set(e)]
    Ws=codes(n);assert len(Ws)==67
    invariant=allpair=lifted=nonlifted=fams=0
    for C in Cs:
        for W in Ws:
            if len(W)==1 or any(bitperm(c,v) not in W for c in C for v in W):continue
            invariant+=1; assert 15 in W
            for sigma in C:
                if comp(sigma,sigma)==e and all(i!=j for i,j in enumerate(sigma)):
                    assert bitperm(sigma,15)==15;allpair+=1
        P=sorted(c for c in C if c[0]==0);P.sort(key=lambda x:x!=e)
        frames=[next(c for c in sorted(C) if c[0]==i) for i in e]
        # Enumerate all actual field-graph complements via basepoint characters
        # and arbitrary fiber gauges (anchor gauge fixed). Compare to characters
        # and full C4 gauges in the normalizer of a five-torus.
        def cocycles(m):
            ans=set(); idx={p:i for i,p in enumerate(P)}
            for vs in product(range(m),repeat=len(P)-1):
                v=(0,)+vs
                if any(v[idx[comp(x,y)]]!=(v[idx[x]]+v[idx[y]])%m for x in P for y in P):continue
                for gs in product(range(m),repeat=n-1):
                    g=(0,)+gs
                    def val(c,i):
                        h=comp(inv(frames[c[i]]),comp(c,frames[i]))
                        return (g[c[i]]+v[idx[h]]-g[i])%m
                    b=tuple(tuple(val(c,i) for i in e) for c in sorted(C))
                    ans.add(b)
            return ans
        B=cocycles(2)
        lifts={tuple(tuple(x%2 for x in row) for row in b) for b in cocycles(4)}
        assert lifts<=B; sz=0
        for b in B:
            arr=dict(zip(sorted(C),b))
            fixedodd=any(arr[c][i] for c in C if comp(c,c)==e for i in e if c[i]==i)
            if b not in lifts:
                if fixedodd:nonlifted+=1
                continue
            lifted+=1
            assert not fixedodd
            choices=[]
            for c in sorted(C):
                if comp(c,c)!=e:continue
                outer=tuple(1-x for x in arr[c])
                assert all(outer[i]==1 for i in e if i==c[i])
                k=sum(i!=c[i] for i in e)//2; s=n-2*k
                choices.append((c,s,60**k*10**s))
            assert arr[e]==(0,)*n
            # Every actual selection of outer labels with the identity label has
            # strictly negative total first moment; fixed-coordinate class is unique.
            for mask in range(1<<len(choices)):
                lc=[a for j,a in enumerate(choices) if mask>>j&1]
                if not any(a[0]==e for a in lc):continue
                assert sum(-s*w for c,s,w in lc)<0;fams+=1
    assert min(invariant,allpair,lifted,nonlifted,fams)>0
    # Odd-order transitivity alone does not put the all-ones vector in every nonzero binary code.
    c=(1,2,0);W={0,3,5,6};assert 7 not in W and {bitperm(c,v) for v in W}==W
    print("four-site transitive concrete 2-groups, invariant codes, all-paired checks, C4-liftable binary cocycles, adverse nonsplitting-of-fixed-bit tests, rooted marked label selections:",len(Cs),invariant,allpair,lifted,nonlifted,fams)


if __name__=="__main__":
    a5_layer(); arrow_tests()
