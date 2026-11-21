#!/usr/bin/env python3
"""Finite controls for rationally induced simple construction and actual center transfer."""
from itertools import product
from collections import Counter
from math import gcd,lcm
def orde(a,p):
    n=1
    while pow(a,n,p)!=1:n+=1
    return n
def rank(rows,p):
    D={}
    for row in rows:
        v=list(row)
        for i in sorted(D):
            c=v[i];v=[(a-c*b)%p for a,b in zip(v,D[i])]
        i=next((i for i,a in enumerate(v) if a%p),None)
        if i is not None:D[i]=[a*pow(v[i],-1,p)%p for a in v]
    return len(D)
def rational():
    p=5;q=31;alpha=2;f=orde(p,q);assert orde(alpha,q)==p and f==3
    A=list(product(range(p),repeat=3));idx={v:i for i,v in enumerate(A)};zz=idx[(0,0,0)];one=idx[(1,0,0)]
    def mul(x,y):
        w=[0]*5
        for i,a in enumerate(A[x]):
            for j,b in enumerate(A[y]):w[i+j]+=a*b
        for j in (4,3):w[j-3]-=w[j];w[j-2]-=w[j]
        return idx[tuple(z%p for z in w[:3])]
    def power(x,n):
        v=one
        while n:
            if n%2:v=mul(v,x)
            x=mul(x,x);n//=2
        return v
    assert all(power(x,124)==one for x in range(1,125))
    z=next(x for x in range(1,125) if x!=one and power(x,q)==one)
    def ba(v):
        return tuple(mul(power(z,pow(alpha,i,q)),x) for i,x in enumerate(v))
    def hh(v):return v[1:]+v[:1]
    def pl(v):return tuple(a for x in v for a in A[x])
    def cn(op,v,n):
        for _ in range(n):v=op(v)
        return v
    weights=[{pow(alpha,i,q)*pow(p,k,q)%q for k in range(f)} for i in range(p)]
    assert len(set.union(*weights))==lcm(p,f)==15
    bas=[tuple(idx[tuple(int(j==k) for j in range(3))] if i==r else zz for i in range(p)) for r in range(p) for k in range(3)]
    for w in bas:
        assert hh(ba(cn(hh,w,4)))==cn(ba,w,alpha)
        assert cn(hh,w,p)==cn(ba,w,q)==w
    w=(one,zz,zz,zz,zz)
    assert rank([pl(cn(ba,w,i)) for i in range(q)],p)==3
    assert rank([pl(cn(hh,cn(ba,w,i),j)) for i in range(q) for j in range(p)],p)==15
    moved=rank([tuple((x-y)%p for x,y in zip(pl(hh(w)),pl(w))) for w in bas],p)
    assert moved==12
    # Actual outside marks of the little signed quotient V:q slopes times t, all original J cosets.
    I=(0,0,0);allx=list(product(range(q),range(q),range(p)))
    def op(x,y):
        a,b,k=x;c,d,j=y
        return ((a+pow(alpha,k,q)*c)%q,(b+pow(alpha,-k,q)*d)%q,(k+j)%p)
    def t(x):a,b,k=x;return b,a,-k%p
    T=[x for x in allx if op(x,t(x))==I]
    assert len(T)==p*q and Counter(x[0] for x in T)=={i:p for i in range(q)}
    print(f'GF(125)^5: genuine rational module in characteristic 5, q=31, ord=3; a single C31-orbit spans dimension 3, full C31:C5 orbit spans 15, rank(h-1)={moved}; {len(allx)} quotient elements, {len(T)} marks distributed 5 per actual axis-stabilizer coset')
    assert orde(3,7)==6 and 3 in [i for i in range(3,7) if (7-1)%i==0]
    assert (lcm(3,6)+1,lcm(5,3)+1)==(7,16)
    print('admissible (3,7) construction: degree 3^7*7 hits the conditional lower bound; (5,31) construction degree 5^16*31, no optimality asserted')
def transfer():
    # Actual odd group D=(C7:C3) x C7, center C7 last coordinate, abelian Sylow 7.
    q=7
    def mul(a,b):return ((a[0]+2**a[1]*b[0])%7,(a[1]+b[1])%3,(a[2]+b[2])%7)
    G=list(product(range(7),range(3),range(7)));I=(0,0,0)
    inv={g:next(h for h in G if mul(g,h)==I) for g in G}
    reps=[(0,k,0) for k in range(3)]
    def v(g):
        total=I
        for u in reps:
            x=mul(u,g);r=reps[x[1]]
            total=mul(total,mul(x,inv[r]))
        return total
    for g,h in product(G,repeat=2):assert v(mul(g,h))==mul(v(g),v(h))
    for c in range(7):assert v((0,0,c))==(0,0,3*c%7)
    # Determinant on the true Heisenberg commutator, not a claim that any extension splits.
    def hb(x,y):return ((x[0]+y[0])%7,(x[1]+y[1])%7,(x[2]+y[2]+x[0]*y[1])%7)
    def hta(x):return (x[0],-x[1]%7,-x[2]%7)
    H=list(product(range(7),repeat=3))
    assert all(hta(hb(x,y))==hb(hta(x),hta(y)) for x,y in product(H,repeat=2))
    assert hta((0,0,1))==(0,0,6)
    print('abelian Sylow transfer: all 21,609 products in the odd group, central C7 maps by cubing; all 117,649 Heisenberg products show a determinant-minus-one reflection inverts, not fixes, the commutator center')
if __name__=='__main__':rational();transfer()
