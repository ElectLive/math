"""Genuine local group, signed permutation and arithmetic controls (Python 3.10+)."""
from itertools import permutations, product
from math import factorial

def comp(a,b):return tuple(a[x] for x in b)
def inv(a):return tuple(a.index(i) for i in range(len(a)))
def con(a,b):return comp(comp(a,b),inv(a))
def parity(a):return sum(x>y for i,x in enumerate(a) for y in a[i+1:])%2
def pair_mapping(arrows,sigma):
    n=len(arrows[0]);return tuple(n*sigma[i]+arrows[i][x] for i in range(len(sigma)) for x in range(n))

def central_layer():
    P=list(permutations(range(8)))
    even=[g for g in P if not parity(g)]
    one=tuple(range(8))
    z=(1,0,3,2,4,5,6,7)
    zz=(1,0,3,2,5,4,7,6)
    for zi in (z,zz):
        Z={con(g,zi) for g in even}
        assert Z=={con(g,zi) for g in P}
        gauge=(one,(1,0,2,3,4,5,6,7),(2,1,0,3,4,5,6,7),(0,2,1,3,4,5,6,7))
        w=tuple(con(g,zi) for g in gauge)
        C={tuple((k+s*i)%4 for i in range(4)) for k in range(4) for s in (-1,1)}
        # P is the even-weight base code on four C2 sites, extended by D8;
        # z is one *actual* central all-one lift, in nonidentical frames.
        A={pair_mapping(tuple(w[i] if u[i] else one for i in range(4)),tuple(range(4)))
           for u in product(range(2),repeat=4) if not sum(u)%2}
        lifts={pair_mapping(tuple(comp(gauge[c[i]],inv(gauge[i])) for i in range(4)),c) for c in C}
        H={comp(x,y) for x,y in product(A,lifts)}
        assert len(A)==8 and len(H)==64
        wbig=pair_mapping(w,tuple(range(4)))
        assert wbig in A and all(comp(wbig,h)==comp(h,wbig) for h in H)
        for sigma in C:
            if comp(sigma,sigma)!=tuple(range(4)) or any(i==j for i,j in enumerate(sigma)):continue
            pairs=[(i,j) for i,j in enumerate(sigma) if i<j]
            for labels in product(range(2),repeat=len(pairs)):
                a=[None]*4;b=[None]*4
                for (i,j),bit in zip(pairs,labels):
                    g=next(g for g in P if parity(g)==bit and con(g,inv(w[i]))==w[j])
                    t=comp(g,w[i])
                    a[i],a[j],b[i],b[j]=g,inv(g),t,inv(t)
                x,y=pair_mapping(a,sigma),pair_mapping(b,sigma)
                assert comp(x,x)==comp(y,y)==tuple(range(32)) and comp(x,y)==wbig
    print("Actual 64-element 2-groups in transported A8 coordinates: central"
          " involutions of two different cycle classes both give physical paired-square collisions")

def stable_odd_containers():
    def affine(q,a,b):return tuple((a*x+b)%q for x in range(q))
    M={affine(7,a,b) for a in (1,2,4) for b in range(7)}
    R={affine(7,1,b) for b in range(7)}
    r=affine(7,3,0);e=tuple(range(7))
    assert len(M)==21 and all(not parity(x) for x in M)
    assert parity(r) and {con(r,x) for x in M}==M
    D={(x,inv(x)) for x in M}
    cosets={frozenset((comp(x,a),comp(y,a)) for a in R) for x,y in D}
    assert len(cosets)==21 and sum(map(len,cosets))==len(set.union(*(set(c) for c in cosets)))
    a=affine(7,1,1)
    S=list(permutations(range(7)))
    for rr,expected in ((e,False),(r,True)):
        hit=any(con(comp(rr,t),inv(a))==a for t in S if not parity(t))
        assert hit==expected
    # Genuine odd outer class changes this other diagonal intersection. The
    # stable container does not assert that every diagonal avoids the mark.
    for q,p in ((3,2),(5,2),(7,3)):
        cyc={affine(q,1,t) for t in range(q)}
        s=affine(q,p,0);assert parity(s) and {con(s,u) for u in cyc}==cyc
    Syl3={tuple(3*((i//3+s)%3)+(i%3+c[i//3])%3 for i in range(9))
          for c in product(range(3),repeat=3) for s in range(3)}
    assert len(Syl3)==81 and all(not parity(g) for g in Syl3)
    assert all(comp(g,h) in Syl3 for g,h in product(Syl3,repeat=2))
    assert all(81%p!=0 for p in (2,5,7))
    print("Odd containers: true F21 odd-normalized in A7; 21 distinct paired"
          " cosets; the same C7 diagonal collides exactly after the odd class change;"
          " actual Sylow 3 subgroup of A9 has 81 elements")

def sylow_moments():
    def rec(W):
        m=len(W[0]);return [tuple((m*s if i<m else m*(1-s)) +
            (a[i] if i<m else b[i-m]) for i in range(2*m)) for a,b,s in product(W,W,range(2))]
    I=112;V=1440
    W=[(0,)];F=I
    for n in (1,2,4,8,16):
        if n>1:
            F=F*F+2**(n//2-1)*V**(n//2)
            W=rec(W)
        assert len(set(W))==2**(n-1)
        hist={}
        for w in W:
            if all(w[w[i]]==i for i in range(n)):
                s=sum(w[i]==i for i in range(n))
                hist[s]=hist.get(s,0)+1
        assert sum(c*I**s*V**((n-s)//2) for s,c in hist.items())==F
        assert F<120**n
    assert 112**6<120**4*(112**2-2*1440)
    assert 2*112*3>360 # crude estimate really fails.
    print("All 32768 actual binary Sylow permutations on 16 sites counted;"
          " full fixed-site polynomials agree recursively; A6 I=112 bound is strictly below 120")

def degrees():
    I=[1,1]
    for d in range(2,121):I.append(I[-1]+(d-1)*I[-2])
    assert [I[d] for d in range(7,13)]==[232,764,2620,9496,35696,140152]
    for d in range(11,121):assert factorial(d)**2>16*I[d]**2*3**(d-1)
    for d,s in ((7,21),(8,21)):
        assert (factorial(d)//2)**2>4*I[d]**2*s
    assert factorial(9)//2>2*I[9]*27 and factorial(10)//2>2*I[10]*81
    assert 5**6<=3**12 and 11**4<=3**10
    for k in range(3,101):assert 2*k*(k+1)<=3**k-1
    print("Alternating small-degree packing, two large-degree recurrence bases"
          " and degrees through 120 verified in integers (uniform proof is symbolic)")

if __name__=="__main__":
    central_layer()
    stable_odd_containers()
    sylow_moments()
    degrees()
