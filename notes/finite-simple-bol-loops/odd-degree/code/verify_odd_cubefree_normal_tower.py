#!/usr/bin/env python3
"""Finite mechanism controls for the odd cube-free normal-tower proof. Python 3, no dependencies."""
from collections import deque, Counter
from itertools import product, permutations

def gen(one, gens, mul):
    seen={one}; todo=deque([one])
    while todo:
        a=todo.popleft()
        for b in gens:
            c=mul(a,b)
            if c not in seen: seen.add(c);todo.append(c)
    return seen

def rank(A,p):
    A=[list(row) for row in A];r=0
    for j in range(len(A[0])):
        i=next((i for i in range(r,len(A)) if A[i][j]%p),None)
        if i is None: continue
        A[r],A[i]=A[i],A[r];t=pow(A[r][j]%p,-1,p)
        A[r]=[t*x%p for x in A[r]]
        for i in range(len(A)):
            if i!=r:
                u=A[i][j]%p;A[i]=[(x-u*y)%p for x,y in zip(A[i],A[r])]
        r+=1
    return r

def mprod(A,B,p):
    d=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(d))%p for j in range(d)) for i in range(d))
def ident(d): return tuple(tuple(int(i==j) for j in range(d)) for i in range(d))
def trank(A,p):return rank([[a-int(i==j) for j,a in enumerate(row)] for i,row in enumerate(A)],p)
def order(x,one,mul):
    z=one
    for i in range(1,2001):
        z=mul(z,x)
        if z==one:return i
    raise ValueError()

def squarefree_double():
    # Q is the nonabelian group C7:C3 with its actual left-regular rows.
    group=list(product(range(7),range(3)));e=(0,0)
    def mul(a,b):return ((a[0]+pow(2,a[1],7)*b[0])%7,(a[1]+b[1])%3)
    def inv(a):return (-pow(2,-a[1],7)*a[0]%7,-a[1]%3)
    def times(a,b):return (mul(a[0],b[0]),mul(a[1],b[1]))
    T={(x,inv(x)) for x in group};D=gen((e,e),T,times)
    assert len(D)==147 and len(T)==21
    N={y for y in D if y[0][1]==y[1][1]==0}
    assert len(N)==49 and len({a for a,b in N})==7 and len([y for y in N if y[0]==e])==7
    assert len({u for u in N if u[0]==u[1]})==7
    # Every class fiber and every physical block. Projection mod N is first exponent.
    fibers=Counter(y[0][1] for y in T)
    for base in group:
        blocks=Counter(mul(y[0],base)[1] for y in T)
        assert blocks==fibers=={0:7,1:7,2:7}
        for a in group:
            for b in group:assert mul(a,b)[1]==(a[1]+b[1])%3
    threes=[z for z in group if order(z,e,mul)==3]
    assert len(threes)==14 # seven Sylow 3, despite normal quotient C3
    print('squarefree actual double: |D|=147, |N|=49, |ker(pr1|N)|=7, 21 physical origins, b=Delta=7; quotient Sylow 3 does not naively lift')

def cube_group():
    # An honest cube-free group in which no order-prime subgroup is normal.
    p=5; I=ident(2);c=((0,4),(1,4));c2=mprod(c,c,p)
    assert mprod(c2,c,p)==I
    def act(m,x):return tuple(sum(a*b for a,b in zip(r,x))%p for r in m)
    mats=[I,c,c2]; G=list(product(range(5),range(5),range(3)));e=(0,0,0)
    def mul(a,b):
        v=act(mats[a[2]],b[:2])
        return ((a[0]+v[0])%5,(a[1]+v[1])%5,(a[2]+b[2])%3)
    inv={x:next(y for y in G if mul(x,y)==e) for x in G}
    pr={frozenset(gen(e,[g],mul)) for g in G if g!=e};assert {len(h) for h in pr}=={3,5}
    def normal(h):return all(mul(mul(g,x),inv[g]) in h for g in G for x in h)
    assert len(pr)==31 and not any(normal(h) for h in pr)
    N={g for g in G if not g[2]};assert len(N)==25 and normal(N)
    # Nonsplit weight lines over F5, conjugated torus order3 and rank-one inversion.
    j=((1,4),(0,4));assert mprod(j,j,p)==I and trank(j,p)==1 and mprod(mprod(j,c,p),j,p)==c2
    assert len(gen(I,[j,mprod(c,j,p)],lambda a,b:mprod(a,b,p)))==6
    print('physical order-75 group: 31 candidate prime subgroups, zero normal; normal factor 25. Irreducible nonsplit F5 torus has rotation prime 3 dividing 5+1, not 5-1')

def heisenberg_exception():
    p=13;z=3;d=3;I=ident(d)
    X=tuple(tuple(int(i==(j+1)%d) for j in range(d)) for i in range(d))
    Y=tuple(tuple(pow(z,j,p)*int(i==j) for j in range(d)) for i in range(d))
    J=tuple(tuple(int(i==(-j)%d) for j in range(d)) for i in range(d))
    # sqrt(3)=4 mod 13, making the normalized Fourier fourth root of unity.
    A=tuple(tuple(pow(4,-1,p)*pow(z,i*j,p)%p for j in range(d)) for i in range(d))
    mm=lambda a,b:mprod(a,b,p)
    assert mm(A,A)==J and trank(J,p)==1
    P=gen(I,[X,Y],mm);H=gen(I,[X,Y,A],mm);assert (len(P),len(H))==(27,108)
    inv={g:next(h for h in H if mm(g,h)==I) for g in H}
    rr=[g for g in H if mm(g,g)==I and trank(g,p)==1]
    C=gen(I,rr,mm);assert len(rr)==9 and len(C)==54
    cc=lambda a,b:mm(mm(a,b),inv[a])
    assert set(rr)=={cc(h,J) for h in H}
    diag=lambda g:all(i==j or not g[i][j] for i in range(3) for j in range(3))
    B={a for a in P if diag(a)};assert len(B)==9 and all(cc(g,b) in B for g in C for b in B)
    assert any(cc(A,b) not in B for b in B)
    # C4 permutes all four lines of F/Z in two 2-cycles: none is preserved by A.
    center={a for a in P if all(mm(a,g)==mm(g,a) for g in P)};assert len(center)==3
    planes={frozenset(gen(I,list(center)+[a],mm)) for a in P-center};assert len(planes)==4
    assert all(any(cc(A,h) not in B for h in B) for B in planes)
    sl=[((a,b),(c,d)) for a,b,c,d in product(range(3),repeat=4) if (a*d-b*c)%3==1]
    invs=[g for g in sl if g!=ident(2) and mprod(g,g,3)==ident(2)]
    assert len(sl)==24 and invs==[((2,0),(0,2))]
    print('Heisenberg dimension 3: actual 108 matrices; 9 conjugate rank-one involutions generate 54, fixing an abelian order-9 plane; full Fourier order-4 action fixes none of 4 planes; SL2(3) sole involution -I')

def cubicfield():
    # GF(3)[u]/(u^3-u+1), encoding coefficients in base 3.
    V=list(product(range(3),repeat=3))
    def mul(a,b):
        w=[0]*5
        for i in range(3):
            for j in range(3):w[i+j]+=a[i]*b[j]
        for j in (4,3):w[j-3]-=w[j];w[j-2]+=w[j]
        return tuple(x%3 for x in w[:3])
    one=(1,0,0);u=next(x for x in V if x!=(0,0,0) and order(x,one,mul)==13)
    pw=[one]
    for _ in range(12):pw.append(mul(pw[-1],u))
    return pw,mul

def three_lines():
    # 13^2:S3 in characteristic 3 *over GF(27)*: prime-field assumption matters.
    pw,fmul=cubicfield();perms=list(permutations(range(3)));id3=tuple(range(3));one=((0,0,0),id3)
    def mu(a,b):
        aa,s=a;bb,t=b
        return (tuple((bb[j]+aa[t[j]])%13 for j in range(3)),tuple(s[t[j]] for j in range(3)))
    G={( (a,b,(-a-b)%13),s) for a,b in product(range(13),repeat=2) for s in perms};assert len(G)==1014
    invols=[g for g in G if g!=one and mu(g,g)==one];assert len(invols)==39 and gen(one,invols,mu)==G
    ranks=set()
    for expo,s in invols:
        A=[[0]*9 for _ in range(9)]
        for j in range(3):
            for k in range(3):
                basis=tuple(int(i==k) for i in range(3))
                for i,x in enumerate(fmul(pw[expo[j]],basis)):A[3*s[j]+i][3*j+k]=x
        ranks.add(trank(A,3))
    assert ranks=={3}
    print('field-descent adverse control: GF(27) monomial 13^2:S3 of order 1014 generated by 39 reflections; all have rank 3, not 1, on restriction to GF(3)')
if __name__=='__main__':
    squarefree_double();cube_group();heisenberg_exception();three_lines()
