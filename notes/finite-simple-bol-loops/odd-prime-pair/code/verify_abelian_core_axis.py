#!/usr/bin/env python3
"""Concrete adverse groups for a normalizer/Frattini escape and the axis quotient."""
from itertools import product
from collections import deque

def rank(rows,p):
    B={}
    for a in rows:
        v=list(a)
        for i in sorted(B):
            c=v[i];v=[(a-c*b)%p for a,b in zip(v,B[i])]
        j=next((j for j,a in enumerate(v) if a%p),None)
        if j is not None:B[j]=[a*pow(v[j],-1,p)%p for a in v]
    return len(B)
def cc(x):
    # multiply by zeta modulo 1+x+...+x^6 in characteristic three
    return tuple((r-x[-1])%3 for r in (0,)+x[:-1])
def powerop(op,x,k):
    for _ in range(k):x=op(x)
    return x
def B(v,a,b):
    return sum((powerop(cc,v[6*j:6*j+6],(pow(2,j,7)*a+pow(2,-j,7)*b)%7) for j in range(3)),())
def P(v):return v[6:]+v[:6]
def T(v):return v[:6]+v[12:]+v[6:12]
def dot(x,y):return sum(a*b for a,b in zip(x,y))%3
def hep(g,h):
    x,y,c=g;u,v,d=h
    return (tuple((a+b)%3 for a,b in zip(x,u)),tuple((a+b)%3 for a,b in zip(y,v)),(c+d+dot(x,v))%3)
def extraspecial():
    e=[tuple(int(i==j) for j in range(18)) for i in range(18)];zero=(0,)*18
    # every nontrivial V2 element fixed-point-free, on U and on the dual (same rank)
    for b in range(1,7):
        assert rank([[x-y for x,y in zip(B(w,0,b),w)] for w in e],3)==18
    for a,b in product(range(7),repeat=2):
        assert all(T(B(T(w),a,b))==B(w,b,a) for w in e)
        assert all(P(B(powerop(P,w,2),a,b))==B(w,2*a,4*b) for w in e)
    # each actual mixed label acts faithfully on the total three-site module
    assert sum(all(B(w,a,b)==w for w in e) for a,b in product(range(7),repeat=2))==1
    # actual unit Heisenberg commutator is the nontrivial fixed center generator
    x=(e[0],zero,0);y=(zero,e[0],0)
    def neg(v):return tuple(-i%3 for i in v)
    def inv(g):u,v,c=g;return neg(u),neg(v),(dot(u,v)-c)%3
    z=hep(hep(x,y),hep(inv(x),inv(y)));assert z==(zero,zero,1)
    for a,b in [(0,1),(2,3),(6,6)]:
        # diagonal GL lift preserves the exact bilinear group law using dual action
        invcols=[B(w,-a,-b) for w in e]
        def act(g):
            u,v,c=g;return B(u,a,b),tuple(dot(col,v) for col in invcols),c
        for i,j in product(range(18),repeat=2):
            g=(e[i],e[j],1);h=(e[j],e[(i+1)%18],2)
            assert act(hep(g,h))==hep(act(g),act(h))
        assert act(z)==z
    # S=<z,h>=F3^2. Intersect all four maximal subgroups, then form the tilted one.
    lines={frozenset((k*a%3,k*b%3) for k in range(3)) for a,b in product(range(3),repeat=2) if a or b}
    assert set.intersection(*(set(H) for H in lines))=={(0,0)}
    tilt={(j,j) for j in range(3)};assert {b for a,b in tilt}==set(range(3)) and (1,0) not in tilt
    print('actual Heisenberg group of order 3^37: all six nonidentity elements of V2 fix exactly Z in N; V on 18-space faithful, 972 dual-lift multiplication checks; [N,V]=N by full Frattini image')
    print('C_[N,V](V)=Z=C3 outside Phi(S)=1 for S=C3^2; tilted proper line surjects S/Z; illustrates the nonabelian escape only, not a Bol folder')

def hyperplanes():
    p=5;v=list(product(range(5),repeat=3));lookup={x:i for i,x in enumerate(v)};I=lookup[(1,0,0)]
    def fm(x,y):
        w=[0]*5
        for i,a in enumerate(v[x]):
            for j,b in enumerate(v[y]):w[i+j]+=a*b
        for j in (4,3):w[j-3]-=w[j];w[j-2]-=w[j]
        return lookup[tuple(z%5 for z in w[:3])]
    def pw(x,n):
        out=I
        while n:
            if n&1:out=fm(out,x)
            x=fm(x,x);n//=2
        return out
    def tr(x):return sum(v[a][0] for a in [x,pw(x,5),pw(x,25)])%5
    E=set(range(125));assert all(pw(x,124)==I for x in E-{0})
    Hs={frozenset(x for x in E if tr(fm(c,x))==0) for c in E-{0}}
    assert len(Hs)==31 and all(len(h)==25 for h in Hs)
    H=next(iter(Hs));assert {frozenset(fm(c,x) for x in H) for c in E-{0}}==Hs
    base=[tuple(int(i==j) for j in range(15)) for i in range(15)]
    rot=lambda v:v[3:]+v[:3];assert rank([[a-b for a,b in zip(rot(v),v)] for v in base],p)==12
    # Every point of the 3D coinvariant space represented by one summand.
    sm=lambda v:tuple(sum(v[3*j+i] for j in range(5))%5 for i in range(3))
    assert rank([sm(v) for v in base],5)==3 and all(sm(v)==sm(rot(v)) for v in base)
    assert {sm(x+(0,)*12) for x in product(range(5),repeat=3)}==set(v)
    print('p=5,q=31:f=3, elementary first d=15; P-cycles 5 distinct q-types, coinvariant dimension 3, all 31 field-trace hyperplanes form one GF(125)^x orbit')
if __name__=='__main__':extraspecial();hyperplanes()
