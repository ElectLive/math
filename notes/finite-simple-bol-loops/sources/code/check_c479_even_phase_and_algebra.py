#!/usr/bin/env python3
"""Independent finite tests in genuine F4 and on actual restriction-of-scalars operators."""
from itertools import product,permutations
from collections import deque
from random import Random

def mul(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1
        if a&4:a^=7
        b>>=1
    return r

def linspan(words):
    B={}
    for w in words:
        while w and (b:=w.bit_length()-1) in B:w^=B[b]
        if w:B[w.bit_length()-1]=w
    return B

def reduce(v,B):
    for j in sorted(B,reverse=True):
        if v>>j&1:v^=B[j]
    return v

def diag_control():
    d=4;R=Random(71411);orb={(1,0,0,0)};work=list(orb)
    for x in work:
        for i,j in permutations(range(d),2):
            for c in range(1,4):
                y=list(x);y[i]^=mul(mul(c,c),x[j]);y=tuple(y)
                if y not in orb:orb.add(y);work.append(y)
    assert len(orb)==4**4-1
    tests=0
    for _ in range(500):
        Z=[[0]*d for i in range(d)]
        for i in range(d):
            for j in range(i+1):Z[i][j]=Z[j][i]=R.randrange(4)
        for i,j in permutations(range(d),2):
            for c in range(1,4):
                A=[r.copy() for r in Z];A[i]=[u^mul(c,v) for u,v in zip(A[i],A[j])]
                for r in A:r[i]^=mul(c,r[j])
                assert A[i][i]==(Z[i][i]^mul(mul(c,c),Z[j][j]))
                assert all(A[r][r]==Z[r][r] for r in range(d) if r!=i);tests+=1
    # A nonzero diagonal E_11 cannot be (1-transpose)X in characteristic two.
    alt=lambda X: tuple(tuple(X[i][j]^X[j][i] for j in range(d)) for i in range(d))
    assert all(alt([[int(a==i and b==j) for b in range(d)] for a in range(d)])[0][0]==0
               for i,j in product(range(d),repeat=2))
    return len(orb),tests

def scalar_algebra():
    # Coordinates: F4^2 = F2^4 in basis (1,z) in each factor.
    def encode(A):
        a,b,c,d=A;cols=[]
        for x,y in ((1,0),(2,0),(0,1),(0,2)):
            cols.append(mul(a,x)^mul(b,y)^((mul(c,x)^mul(d,y))<<2))
        return sum(v<<(4*j) for j,v in enumerate(cols))
    g=[encode((a,b,c,d)) for a,b,c,d in product(range(4),repeat=4) if mul(a,d)^mul(b,c)==1]
    B=linspan(g)
    assert len(g)==60 and len(B)==8 and reduce(encode((2,0,0,2)),B)==0
    return len(g),len(B)

def normalizer():
    S=list(permutations(range(6)))
    c=(1,2,3,4,0,5)
    def m(p,q):return tuple(p[i] for i in q)
    H={tuple(range(6))};cur=c
    while cur not in H:H.add(cur);cur=m(c,cur)
    N=[p for p in S if m(p,c) in {m(h,p) for h in H}]
    assert len(H)==5 and len(N)==20
    return len(N)

print('GF4 transpose-fiber nonzero-orbit size and true conjugation/diagonal tests:',diag_control())
print('actual SL2(4) over F2 order, group-algebra binary dimension, primitive scalar included:',scalar_algebra())
print('normalizer of a 5-cycle subgroup in actual S6:',normalizer())
