#!/usr/bin/env python3
"""Finite adverse controls and deterministic arithmetic sieve, not a loop census."""
from collections import Counter,deque
from itertools import product

def factors(n):
    o={};i=2
    while i*i<=n:
        if n%i==0:
            a=0
            while n%i==0:n//=i;a+=1
            o[i]=a
        i+=1
    if n>1:o[n]=1
    return o
def ordermod(a,m):
    x=1
    for i in range(1,m+1):
        x=x*a%m
        if x==1:return i
    raise ValueError
def sieve():
    survivors=[];c=Counter()
    for n in range(3,1054,2):
        f=factors(n)
        if len(f)==1:c['prime-power']+=1;continue
        if max(f.values())<=2:c['cube-free']+=1;continue
        if len(f)==2 and 1 in f.values():
            p,a=next((p,a) for p,a in f.items() if a!=1);q=next(q for q,b in f.items() if b==1)
            if q<p or a<=p or (a==p+1 and ordermod(p,q)!=p):c['two-prime exclusion']+=1;continue
        survivors.append(n)
    assert survivors==[675,945,1053] and ordermod(3,13)==3
    print(f'526 odd degrees 3..1053: {dict(c)}; pre-final survivors {survivors}; separate exclusions 675,945 and witness 1053')

def fieldtests():
    # GF(81)=GF(3)[u]/(u^4+u^3+u^2+u+1); ord_5(3)=4.
    v=list(product(range(3),repeat=4));idx={x:i for i,x in enumerate(v)};n=len(v)
    O=idx[(0,0,0,0)];I=idx[(1,0,0,0)];Z=idx[(0,1,0,0)]
    add=[[idx[tuple((a+b)%3 for a,b in zip(x,y))] for y in v] for x in v]
    def mul(x,y):
        w=[0]*7
        for i,a in enumerate(v[x]):
            for j,b in enumerate(v[y]):w[i+j]+=a*b
        for k in (6,5,4):
            for j in range(1,5):w[k-j]-=w[k]
        return idx[tuple(a%3 for a in w[:4])]
    def pw(x,a):
        y=I
        while a:
            if a%2:y=mul(y,x)
            x=mul(x,x);a//=2
        return y
    assert pw(Z,5)==I and Z!=I and all(pw(x,80)==I for x in range(1,n))
    rot=[mul(Z,x) for x in range(n)];t=[pw(x,9) for x in range(n)]
    assert len([x for x in range(n) if t[x]==x])==9
    assert all(t[rot[t[rot[x]]]]==x for x in range(n))
    scalars=[pw(Z,3**i) for i in range(4)]
    assert len(set(scalars))==4
    # Physical affine maps x -> z*x+b, order 5. Distinct cyclic complements.
    powersets=set();comm=set()
    neg=[idx[tuple(-a%3 for a in x)] for x in v]
    for b in range(n):
        S=[];a,c=I,O
        for i in range(5):
            S.append((a,c));a,c=mul(Z,a),add[rot[c]][b]
        assert a==I and c==O
        powersets.add(frozenset(S));comm={add[rot[x]][neg[x]] for x in range(n)}
        assert len(comm)==81
    assert len(powersets)==81
    cur={frozenset([O])};todo=deque(cur)
    while todo:
        b=todo.popleft()
        for x in range(n):
            if x in b:continue
            a=frozenset(set(b)|{add[x][y] for y in b}|{add[neg[x]][y] for y in b})
            if a not in cur:cur.add(a);todo.append(a)
    fixed=[b for b in cur if all(rot[x] in b for x in b)]
    assert len(cur)==212 and sorted(map(len,fixed))==[1,81]
    print('genuine GF(3) degree-four C5 inversions: negative rank 2; all 81 order-five affine complements have [N,S]=N; among all 212 subspaces, only 0 and N are C5-invariant (first nontrivial block index 81, not 27)')
    # Nonlinear constituent with Frobenius length four. Heisenberg X,Y,J on five sites:
    # X advances one, Y e_i=z^i e_i, J reverses i. The central commutator is z^+-1.
    basis=tuple(range(5))
    # each monomial uses a primitive fifth root, stored as exponent mod5
    one=((0,)*5,basis);X=((0,)*5,tuple((i+1)%5 for i in basis));Y=(basis,basis);J=((0,)*5,tuple(-i%5 for i in basis))
    def mm(a,b):
        v,s=a;w,u=b
        return tuple((w[i]+v[u[i]])%5 for i in basis),tuple(s[u[i]] for i in basis)
    H={one};todo=deque([one])
    while todo:
        h=todo.popleft()
        for g in X,Y:
            c=mm(h,g)
            if c not in H:H.add(c);todo.append(c)
    center=[h for h in H if mm(h,X)==mm(X,h) and mm(h,Y)==mm(Y,h)]
    assert len(H)==125 and len(center)==5 and list(J[1])==[0,4,3,2,1]
    # Two independent swaps over the field become eight prime-field negative dimensions.
    r=sum(J[1][i]!=i for i in basis)//2
    assert r==2 and r*len(scalars)==8
    print('actual nonlinear Heisenberg(5): 125 operators, 5 scalars; four different Frobenius central characters, parity rank 2 over GF(81) but rank 8 over GF(3)')
def gls():
    orders=[]
    for i in range(1,5):
        v=3**i
        for j in range(i):v*=3**i-3**j
        orders.append(v)
    assert [x%5==0 for x in orders]==[False,False,False,True]
    print('affine primitive block controls for degree 3,9,27,81: 5 divides the order exactly at 81; 5-rank and normal Sylow lift are distinct checks')
if __name__=='__main__':sieve();fieldtests();gls()
