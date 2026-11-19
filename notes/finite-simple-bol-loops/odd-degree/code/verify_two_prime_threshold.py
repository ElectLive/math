#!/usr/bin/env python3
"""Actual dual-character orbit controls; exact arithmetic, no external dependencies."""
from collections import Counter,deque
from itertools import product

def closure(x,gens):
    S={x};todo=deque([x])
    while todo:
        y=todo.popleft()
        for g in gens:
            z=g(y)
            if z not in S:S.add(z);todo.append(z)
    return frozenset(S)

def ordermod(a,m):
    x=1
    for k in range(1,m+1):
        x=x*a%m
        if x==1:return k
    raise ValueError

def partition(S,gens):
    T=set(S);out=[]
    while T:
        B=closure(next(iter(T)),gens);assert B<=T
        out.append(B);T-=B
    return out

def cyclic(p,q,h):
    f=ordermod(p,q);z=None
    if (q-1)%h==0:
        z=next(i for i in range(1,q) if ordermod(i,q)==h)
        rot=lambda v:(z*v[0]%q,pow(z,-1,q)*v[1]%q)
        t=lambda v:(v[1],v[0])
        kind='split'
    else:
        assert (q+1)%h==0
        # Companion matrix with reciprocal roots, and field conjugation on 1,lambda.
        for trace in range(q):
            rot=lambda v:(-v[1]%q,(v[0]+trace*v[1])%q)
            if len(closure((1,0),[rot]))==h:break
        else:raise AssertionError
        t=lambda v:((v[0]+trace*v[1])%q,-v[1]%q)
        kind='nonsplit'
    allv=set(product(range(q),repeat=2))-{(0,0)}
    F=lambda v:tuple(p*x%q for x in v)
    assert all(t(t(v))==v and t(rot(t(rot(v))))==v for v in allv)
    assert all(len(B)==h for B in partition(allv,[rot]))
    stats=Counter();minr=100000
    for S in partition(allv,[rot,t,F]):
        r=sum(t(x)!=x for x in S)//2;minr=min(r,minr)
        pr=partition(S,[rot]);A=pr[0]
        stable=frozenset(t(x) for x in A)==A
        if stable:
            assert all(frozenset(t(x) for x in B)==B for B in pr)
            assert len(pr)==f and r==f*((h-1)//2)
        else:
            ds=partition(S,[rot,t]);assert all(len(d)==2*h for d in ds)
            assert r==h*len(ds)
            if r==h: assert f in (2,)+tuple(i for i in range(1,h+1) if h%i==0)
        assert r>=max(f,h)
        if r==p==h:assert f==p
        stats['stable' if stable else 'exchanged',r]+=1
    print(f'p={p} q={q} h={h} {kind}: f={f}, {q*q-1} physical characters, min moved pairs={minr}, strata={sorted(stats.items())}')
    return minr,stats

def noncyclic():
    q=7;p=3
    V=set(product(range(q),repeat=3))-{(0,0,0)}
    z=2
    A=lambda v:(z*v[0]%q,pow(z,-1,q)*v[1]%q,v[2])
    B=lambda v:(v[2],v[0],v[1])
    T=lambda v:(v[1],v[0],v[2])
    F=lambda v:tuple(p*x%q for x in v)
    # actual P of order 27, stored as permutations of the basis-vector orbits
    basis=((1,0,0),(0,1,0),(0,0,1));P=closure(basis,[lambda m:tuple(A(x) for x in m),lambda m:tuple(B(x) for x in m)])
    C=[m for m in P if tuple(T(m[j]) for j in (1,0,2))==m]
    assert len(P)==27 and len(C)==3
    f=ordermod(p,q);assert f==6
    counts=Counter()
    for O in partition(V,[A,B,T,F]):
        orbs=partition(O,[F]);r=sum(T(x)!=x for x in O)//2
        assert any(frozenset(T(x) for x in H)!=H for H in orbs) and r>=f
        counts[r]+=1
    print(f'noncyclic p=3, q=7 actual 3-Sylow of order 27: index of reflection centralizer 9, {len(V)} characters, f=6, moving pairs {sorted(counts.items())}')
if __name__=='__main__':
    cases=[(3,13,3),(3,5,3),(3,7,3),(3,19,9),(5,11,5),(5,19,5),(5,31,5),(5,101,25),(7,29,7),(7,13,7),(11,23,11)]
    r={x:cyclic(*x)[0] for x in cases}
    assert r[(3,13,3)]==3 and r[(5,11,5)]==5 and r[(7,29,7)]==7
    assert r[(3,5,3)]>3 and r[(5,19,5)]>5
    noncyclic()
