"""Hostile finite controls for rectangular colored mark moments. Python 3.10+."""
from itertools import combinations, permutations, product
from collections import Counter

def parity(g):
    return sum(x > y for i, x in enumerate(g) for y in g[i+1:]) % 2

def a6_flat():
    # K6 synthemes are perfect matchings; six pentads partition all 15 edges.
    verts = tuple(range(6))
    def match(v):
        if not v:
            yield frozenset()
            return
        x = v[0]
        for i, y in enumerate(v[1:], 1):
            for rest in match(v[1:i]+v[i+1:]):
                yield rest | {(x, y)}
    synt = tuple(match(verts))
    assert len(synt) == 15
    pent = [frozenset(v) for v in combinations(synt, 5) if len(set().union(*v)) == 15]
    assert len(pent) == 6
    def act(g, x):
        return frozenset(frozenset(tuple(sorted((g[i], g[j]))) for i, j in s) for s in x)
    A6 = [g for g in permutations(verts) if not parity(g)]
    P = pent[0]
    left = {g for g in A6 if g[0] == 0}
    right = {g for g in A6 if act(g, P) == P}
    pair_orbit = {(g[0], act(g, P)) for g in A6}
    comp = lambda g,h: tuple(g[j] for j in h)
    assert len(pair_orbit) == 36 and len(left) == len(right) == 60
    assert len(left & right) == 10 and {comp(g,h) for g in left for h in right} == set(A6)
    # A6 cannot conjugate these stabilizers: the second is transitive on six points.
    assert {g[0] for g in right} == set(verts)
    print("A6 physical cross action: all 36 point/pentad pairs; two subgroups"
          " of order 60, intersection 10, actual product all 360")

def fano_relations():
    pts = tuple(range(1,8))
    dot = lambda x,y: (x & y).bit_count() % 2
    mats = []
    for a,b,c in permutations(pts,3):
        if c == a^b:
            continue
        P = {x: (a if x&1 else 0) ^ (b if x&2 else 0) ^ (c if x&4 else 0) for x in pts}
        Q = {y: next(z for z in pts if all(dot(P[x], z)==dot(x, y) for x in pts))
             for y in pts}
        mats.append((P,Q))
    assert len(mats) == 168
    orbits = [{(p[1],q[y]) for p,q in mats} for y in (1,2)]
    assert sorted(map(len,orbits)) == [21,28] and not (orbits[0] & orbits[1])
    # f is 4 on incident point-line pairs, -3 otherwise; always zero margins.
    f = lambda x,y: 4 if not dot(x,y) else -3
    assert all(sum(f(x,y) for y in pts)==0 for x in pts)
    norm = sum(f(x,y)**2 for x in pts for y in pts)
    # graph duality composed with every GL3(2) matrix, zero -> one and back.
    # Its maps on a point x and on a line y are in general DIFFERENT.
    genuine_nonself = 0
    for P,Q in mats:
        invQ = {b:a for a,b in Q.items()}
        assert all(f(x,P[y]) == f(y,invQ[x]) for x in pts for y in pts)
        assert sum(f(x,P[y])*f(y,invQ[x]) for x in pts for y in pts) == norm
        if P != Q:
            genuine_nonself += 1
    assert genuine_nonself > 0
    print(f"Fano: 21 incident and 28 nonincident pairs, positive-sign norm² {norm}"
          f" for 168 genuine dual arrows ({genuine_nonself} distinct directions)")

def signed_arrows():
    # Genuinely nonabelian color group, and opposite/adjacent/equal orbital types.
    square = {tuple((r+s*k)%4 for k in range(4)) for r in range(4) for s in (-1,1)}
    assert len(square) == 8
    C3 = {(0,1,2), (1,2,0), (2,0,1)}
    count = Counter()
    def F(b,c,x,y):
        if (b-c) % 2:  # antisymmetric centered kernel on data Z3
            return (0,1,-1)[(y-x)%3]
        return 3*int(x==y)-1
    for g,k,bi,bj,p in product(square,range(3),range(4),range(4),range(4)):
        # Source color is p (not necessarily zero); g sends p->bi and bj->p.
        if g[p]!=bi or g[bj]!=p:
            continue
        s = -1 if (bi-p)%2 else 1
        entries = [(F(p,bi,x,(y+k)%3),F(p,bj,y,(x-k)%3)) for x,y in product(range(3),repeat=2)]
        assert all(a==s*b for a,b in entries)
        assert sum(a*b for a,b in entries) == s * sum(a*a for a,b in entries)
        count[s]+=1
    assert min(count.values()) and set(count)=={-1,1}
    # C3 has two disjoint ordered orbits on different colors: no swap.
    assert not any(g[0]==1 and g[1]==0 for g in C3)
    def F3(p,b,x,y):
        d=(b-p)%3
        if d==1:
            return 3*int((y-x)%3==1)-1
        if d==2:
            return 3*int((x-y)%3==1)-1
        return 3*int(x==y)-1
    for g,k,j,p,x,y in product(C3,range(3),range(3),range(3),range(3),range(3)):
        if g[j]==p:
            assert F3(p,g[p],x,(y+k)%3)==F3(p,j,y,(x-k)%3)
    print(f"D8 colors with actual shifts: {count[1]} positive and {count[-1]} negative"
          " reciprocal-arrow tests; C3 reverse orbital given independent transpose")

def shifted_uniform():
    # G=C4 x C3 and its actual signed inversion coset. Source even, target odd
    # colors shared on both sites, rather than a Cartesian union of color orbits.
    bits = list(product(range(2),repeat=2))
    E = [(u,v,2*j) for u,v in bits for j in range(3)]
    O = [(u,v,2*j+1) for u,v in bits for j in range(3)]
    L = list(product(range(4),range(3)))
    def a(w,ell):
        x,y,c=w
        i,j=ell
        for _ in range(i):
            x,y=1-y,x
        return y,x,(1-c-2*j)%6
    assert all(a(a(w,l),l)==w for w in E+O for l in L)
    assert all(set(a(w,l) for l in L)==set(O) for w in E)
    M=[l for l in L if a((0,0,0),l)[2]==1]
    assert len(M)==4 and all({a((x,y,0),l)[:2] for l in M}==set(bits) for x,y in bits)
    # The centered binary equality relation has entries ±1/2, Frobenius norm 1.
    # Multiply local weights by 2 to remain in Gaussian integers.
    eps=lambda x,y: 1 if x==y else -1
    vals=[]
    for l in M:
        z=1j
        val=0j
        for x,y in bits:
            u,v,c=a((x,y,0),l)
            assert c==1
            val+=(1+z*eps(x,u))*(1+z*eps(y,v))
        vals.append(val)
        if l[0]%2==0:  # actual coordinate exchange
            assert val==0
    assert sum(vals)==16 and any(v!=0 for v in vals)
    print("12x12 genuinely off-diagonal uniform map; four 4x4 conditional"
          " involution maps; exchanged labels vanish at i, constant survives")

if __name__=="__main__":
    a6_flat()
    fano_relations()
    signed_arrows()
    shifted_uniform()
