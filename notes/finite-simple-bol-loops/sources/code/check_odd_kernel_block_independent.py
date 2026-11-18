"""Independent finite-group boundary controls for the odd-kernel block theorem.
Run with stock Python 3. None of the fixtures is asserted to be a simple loop.
"""
from itertools import permutations, product
from collections import Counter


def generated(one, gens, mul):
    found, stack = {one}, [one]
    while stack:
        a = stack.pop()
        for g in gens:
            z = mul(a,g)
            if z not in found:
                found.add(z); stack.append(z)
    return frozenset(found)


def power(x,k,one,mul):
    for _ in range(k): one=mul(one,x)
    return one


def nonabelian_pure():
    # (C7:C3):S4; odd permutations act on C7 by inversion and fix C3.
    perms=list(permutations(range(4))); idp=tuple(range(4))
    comp=lambda p,q:tuple(p[q[i]] for i in range(4))
    sign={p:(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)) for p in perms}
    def mul(x,y):
        a,b,p=x; c,d,q=y
        return ((a+pow(2,b,7)*sign[p]*c)%7,(b+d)%3,comp(p,q))
    unit=(0,0,idp); G=list(product(range(7),range(3),perms)); N=[x for x in G if x[2]==idp]
    assert len(N)==21 and any(mul(x,y)!=mul(y,x) for x in N for y in N)
    inv={x:next(y for y in G if mul(x,y)==unit) for x in G}
    def conj(x,g): return mul(mul(g,x),inv[g])
    # Work in the outside coset of central t, represented by its G-coordinate.
    # Start from a non-pure lift, not the full involution set or a pure section.
    trans=next(p for p in perms if sum(i!=v for i,v in enumerate(p))==2)
    seed=(3,0,trans); assert mul(seed,seed)==unit
    Lambda={unit}|{conj(seed,g) for g in G}; selected={x[2] for x in Lambda}
    natural={p for p in perms if comp(p,p)==idp}
    assert len(natural-selected)==3 and len(selected)==7
    for p in selected:
        fiber={x for x in G if x[2]==p and mul(x,x)==unit}
        actual={x for x in Lambda if x[2]==p}
        assert actual==fiber=={conj((0,0,p),n) for n in N}
    squares={mul(x,y) for x in Lambda for y in Lambda}
    projected={comp(p,q) for p in selected for q in selected}
    assert all((0,0,p) in squares for p in projected)
    counts=Counter(next(k for k in range(1,7) if power(p,k,idp,comp)==idp) for p in projected)
    assert counts[3]==8
    print('Nonabelian kernel 21 in group 504: selected/available projected involutory labels',len(selected),len(natural),'; selected lifts',len(Lambda),'; pure products by order',sorted(counts.items()))


def moved_normal_subgroup():
    # V=C9; Y=C2 x C2 x C3. Both first two involutions invert V.
    unit=(0,0,0,0)
    def mul(x,y):
        u,a,b,c=x; v,d,e,f=y
        return ((u+(-1)**(a+b)*v)%9,a^d,b^e,(c+f)%3)
    Y=list(product(range(2),range(2),range(3))); G=list(product(range(9),range(2),range(2),range(3)))
    def tau(x):
        u,a,b,c=x
        return ((-u+1-(-1)**(a+b))%9,b,a,c)
    assert all(tau(tau(x))==x for x in G) and all(tau(mul(x,y))==mul(tau(x),tau(y)) for x in G for y in G)
    zD=(0,1,0,0); D={(0,0,0),(1,0,0)}
    assert {tau((0,*d))[1:] for d in D} != D
    assert [v for v in range(9) if mul((v,0,0,0),zD)==mul(zD,(v,0,0,0))]==[0]
    complements=set()
    for x,y,z in product(range(9),repeat=3):
        A,B,C=(x,1,0,0),(y,0,1,0),(z,0,0,1)
        if any(power(g,k,unit,mul)!=unit for g,k in ((A,2),(B,2),(C,3))): continue
        if any(mul(g,h)!=mul(h,g) for g,h in ((A,B),(A,C),(B,C))): continue
        S=generated(unit,[A,B,C],mul)
        assert {g[1:] for g in S}==set(Y) and len(S)==len(Y)
        complements.add(S)
    assert len(complements)==9
    fixed=[S for S in complements if frozenset(map(tau,S))==S]
    canonical=frozenset((0,*y) for y in Y)
    assert len(fixed)==1 and canonical not in fixed
    data={next(g[0] for g in S if g[1:]==zD[1:]):S for S in complements}
    assert len(data)==9
    # Independent normalizer characterization for EVERY possible lift of D.
    for x,S in data.items():
        z=(x,1,0,0)
        assert {g for g in G if mul(g,z)==mul(z,g)}==S
    # Quotient fixed-space lift and coprime H1 with non-elementary kernel.
    for modulus in (3,9):
        # j^2=c^3=1 and jc=cj; j acts -1 and c acts trivially.
        allowable={(a,b) for a,b in product(range(modulus),repeat=2) if 3*b%modulus==0 and 2*b%modulus==0}
        principal={((2*v)%modulus,0) for v in range(modulus)}
        assert allowable==principal and [v for v in range(modulus) if 2*v%modulus==0]==[0]
    print('C9 non-Hall kernel: all complements',len(complements),'; tau moves D, fixes',len(fixed),'complement; standard complement not fixed. Both C9 and C3 quotient pass averaging.')


def genuine_nonsplit():
    # SL2(Z/25)/{+-I} maps onto PSL2(5) with abelian kernel sl2(F5).
    I=(1,0,0,1)
    def mm(X,Y,n):
        a,b,c,d=X; e,f,g,h=Y
        return ((a*e+b*g)%n,(a*f+b*h)%n,(c*e+d*g)%n,(c*f+d*h)%n)
    def neg(X,p): return tuple(-a%p for a in X)
    def canon(X,p): return min(X,neg(X,p))
    def inv(X,p): a,b,c,d=X; return (d,-b%p,-c%p,a)
    def det(X,p): a,b,c,d=X; return (a*d-b*c)%p
    def mm5(x,y): return canon(mm(x,y,5),5)
    def mm25(x,y): return canon(mm(x,y,25),25)
    Y={canon(x,5) for x in product(range(5),repeat=4) if det(x,5)==1}; assert len(Y)==60
    one=canon(I,5)
    for g in Y-{one}:
        cls={mm5(mm5(h,g),canon(inv(h,5),5)) for h in Y}
        assert generated(one,cls,mm5)==Y  # no nontrivial proper normal D
    pairs=lambda A: (A[0],A[1],A[2])
    def act(g,v):
        a,b,c=v; X=(a,b,c,-a%5)
        return pairs(mm(mm(g,X,5),inv(g,5),5))
    pts=list(product(range(5),repeat=3)); zero=(0,0,0)
    assert [g for g in Y if all(act(g,v)==v for v in pts)]==[one]
    # Every candidate proper nontrivial F5^3 subspace is a line or a plane.
    normals={tuple(i*pow(next(j for j in v if j),-1,5)%5 for i in v) for v in pts if v!=zero}
    subspaces={frozenset(tuple(k*i%5 for i in v) for k in range(5)) for v in normals}
    subspaces|={frozenset(x for x in pts if sum(a*b for a,b in zip(x,v))%5==0) for v in normals}
    assert len(subspaces)==62
    for S in subspaces: assert any(act(g,v) not in S for g in Y for v in S)
    fibers=Counter(canon(tuple(i%5 for i in x),5) for x in product(range(25),repeat=4) if det(x,25)==1 and canon(x,25)==x)
    assert set(fibers)==Y and set(fibers.values())=={125}
    def kernel(v):
        a,b,c=v; return canon((1+5*a,5*b,5*c,(1-5*a)%25),25)
    for v in pts:
        for w in pts:
            assert mm25(kernel(v),kernel(w))==kernel(tuple((a+b)%5 for a,b in zip(v,w)))
    target=(1,1,0,1)
    # Exhaust the entire positive representative fiber; its negatives give the same quotient elements.
    lifts={canon(X,25) for off in product(range(5),repeat=4) if det(X:=tuple(a+5*b for a,b in zip(target,off)),25)==1}
    assert len(lifts)==125 and power(canon(target,5),5,one,mm5)==one
    ords={next(i for i in range(1,26) if power(x,i,canon(I,25),mm25)==canon(I,25)) for x in lifts}
    assert ords=={25} # an honest section would need a lift of order 5
    print('Non-split congruence control: simple quotient',len(Y),'; faithful irreducible three-dimensional F5 module (all',len(subspaces),'proper nontrivial subspaces rejected);',len(lifts),'lifts of one order-5 element all have order 25.')


if __name__=='__main__':
    nonabelian_pure(); moved_normal_subgroup(); genuine_nonsplit()
