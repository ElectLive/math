"""True local group and arithmetic controls for the homogeneous strip endpoint."""
from itertools import product, permutations
from collections import deque, Counter
from math import gcd

def cycles(k, *C):
    g = list(range(k))
    for c in C:
        for x,y in zip(c,c[1:]+c[:1]):
            g[x-1]=y-1
    return tuple(g)

def mathieu():
    # Standard ATLAS M12G1-p12aB0 representation, g1 and g2.
    a=cycles(12,(1,4),(3,10),(5,11),(6,12))
    b=cycles(12,(1,8,9),(2,3,4),(5,12,11),(6,10,7))
    e=tuple(range(12))
    S={e};todo=deque([e])
    while todo:
        g=todo.popleft()
        for h in [a,b]:
            z=tuple(h[i] for i in g)
            if z not in S:
                S.add(z);todo.append(z)
    R={g for g in S if g[0]==0}
    assert len(S)==95040 and len(R)==7920
    inv=[g for g in S if g!=e and all(g[g[k]]==k for k in e)]
    subsets={n:[g for g in inv if sum(g[k]==k for k in e)==n] for n in (0,4)}
    assert {i:len(v) for i,v in subsets.items()} == {0:396,4:495}
    def cent(G,x):
        return sum(all(x[g[i]]==g[x[i]] for i in e) for g in G)
    assert [cent(S,subsets[n][0]) for n in (0,4)]==[240,192]
    ri=set(inv)&R;assert len(ri)==165 and cent(R,next(iter(ri)))==48
    print("Actual degree-12 Mathieu groups: M12 95040 and M11 7920;"
          " 396 and 495 involutions, centralizers 240 and 192, M11 has one class of size 165")

def field4_16():
    q=16
    def mul(x,y):
        z=0
        while y:
            if y&1:z^=x
            y>>=1;x<<=1
            if x&16:x^=0x13
        return z
    M=[[mul(i,j) for j in range(q)] for i in range(q)]
    def fourth(i):return M[M[i][i]][M[i][i]]
    K=[i for i in range(q) if i==fourth(i)]
    assert len(K)==4 and all(sorted(M[i])==list(range(q)) for i in range(1,q))
    iv={i:M[i].index(1) for i in range(1,q)}
    V=list(product(K,repeat=4));zero=(0,)*4
    def normalize(v):
        return tuple(M[iv[next(t for t in v if t)]][x] for x in v)
    pts={normalize(v) for v in V if v!=zero}
    def pairing(x,y):
        return M[x[0]][y[2]]^M[x[1]][y[3]]^M[x[2]][y[0]]^M[x[3]][y[1]]
    def span(a,b):
        return frozenset(tuple(M[s][x]^M[t][y] for x,y in zip(a,b))
                         for s,t in product(K,repeat=2))
    lag={span(a,b) for a in pts for b in pts if a!=b and pairing(a,b)==0}
    assert len(pts)==len(lag)==85 and all(len(A)==16 for A in lag)
    # Count orbits of actual nonsingular bilinear forms by GL2-congruence.
    bas=[(a,b,c,d) for a,b,c,d in product(K,repeat=4) if M[a][d]!=M[b][c]]
    forms={(a,b,d) for a,b,d in product(K,repeat=3) if M[a][d]!=M[b][b]}
    def change(f,B):
        a,b,d=f;x,y,u,v=B
        aa=M[M[x][x]][a]^M[M[u][u]][d]
        bb=M[M[x][y]][a]^M[(M[x][v]^M[u][y])][b]^M[M[u][v]][d]
        dd=M[M[y][y]][a]^M[M[v][v]][d]
        return (aa,bb,dd)
    formorbits={frozenset(change(f,B) for B in bas) for f in forms}
    assert sorted(map(len,formorbits))==[3,45]
    assert sorted(len(lag)*len(c) for c in formorbits)==[255,3825]
    # ALL involutions of SL2(16) in the real rank-four GF4 restriction.
    def tr(x):return x^fourth(x)
    vectors=list(product(range(q),repeat=2))
    def sym(v,w):return tr(M[v[0]][w[1]]^M[v[1]][w[0]])
    inv=[(a,b,c) for a,b,c in product(range(q),repeat=3)
         if M[a][a]^M[b][c]==1 and (a,b,c)!=(1,0,0)]
    assert len(inv)==255
    for a,b,c in inv:
        N=[(M[a^1][x]^M[b][y],M[c][x]^M[a^1][y]) for x,y in vectors]
        image=set(N)
        assert len(image)==16 and (0,0) in image
        assert any(sym(v,w) for v,w in zip(vectors,N))
        assert all((M[a^1][x]^M[b][y],M[c][x]^M[a^1][y])==(0,0) for x,y in image)
        assert all(not sym(v,w) for v,w in product(image,repeat=2))
    print("Sp4(4): 85 true Lagrangians; GL2(4)-orbits on nonsingular forms 3,45;"
          " class sizes 255,255,3825. All 255 SL2(16) involutions rank two, nonalternating")

def roots():
    # D4 roots in simple-root coordinates: e1-e2, e2-e3, e3-e4, e3+e4.
    basis=((1,-1,0,0),(0,1,-1,0),(0,0,1,-1),(0,0,1,1))
    roots={v for v in product((-1,0,1),repeat=4) if sum(abs(k) for k in v)==2}
    def embed(c):
        return tuple(sum(c[i]*basis[i][j] for i in range(4)) for j in range(4))
    C={c for c in product(range(-2,3),repeat=4) if embed(c) in roots}
    assert len(C)==len(roots)==24
    for outer in permutations([0,2,3]):
        pp=(outer[0],1,outer[1],outer[2])
        assert {tuple(c[i] for i in pp) for c in C}==C
    for q in (2,3,5,7):
        V=tuple(range(8))
        B=[tuple(int(i==j) for i in V) for j in V]
        def root(s,v): # g=I+sE12 on all e's, with inverse transpose on all f's
            a=list(v);a[0]=(a[0]+s*a[1])%q;a[5]=(a[5]-s*a[4])%q
            return tuple(a)
        def h(z,v):  # common determinant-one rescaling diag(z,1,z^-1)
            a=list(v);u=pow(z,-1,q)
            for i,k in ((0,z),(2,u),(4,u),(6,z)):a[i]=a[i]*k%q
            return tuple(a)
        def form(v):return sum(v[i]*v[i+4] for i in range(4))%q
        vectors=B+[tuple(x+y for x,y in zip(i,j)) for i in B for j in B]
        for s in range(1,q):
            assert any(root(s,v)!=v for v in B)
            assert all(root(-s,root(s,v))==tuple(x%q for x in v) for v in B)
            assert all(form(root(s,v))==form(v) for v in vectors)
            for c in range(1,q):
                v=(0,0,0,1,0,0,0,c)
                assert form(v)==c and root(s,v)==v
            for z in range(1,q):
                assert all(h(z,root(s,h(pow(z,-1,q),v)))==root(z*s,v) for v in B)
    print("D4: all 6 diagram permutations preserve all 24 roots; actual common"
          " SL3 root matrices over q=2,3,5,7 preserve the split form and nonsingular"
          " vectors; every parameter and inverse realized by inner scalings")

def arithmetic():
    cases=[("A6",360,4,6),("M12",95040,2,12)]
    for f in range(2,11):
        q=2**f;L=q**4*(q**2-1)*(q**4-1)
        m=q**2*(q**2-1)//2
        cases.append(("C2",L,2*f,m))
    for p in (2,3,5,7,11):
        for f in range(1,7):
            q=p**f;d=gcd(4,q**4-1)
            L=q**12*(q**4-1)**2*(q**2-1)*(q**6-1)//d
            m=q**3*(q**4-1)//gcd(2,q-1)
            cases.append(("D4",L,6*f*d,m))
    for _,L,o,m in cases:
        assert 2*m>=3*o and (2*L)**2>27*o**2
        for n in (3,5,7,9,27):
            # cube both sides (n odd degrees, no floating-point roots).
            assert (m*L**(n-1))**3 * 2**n >=3**(3*((n-1)//2))*(L**2*o)**n
    assert [g for g,L,o,m in cases if 2*m==3*o]==["A6"]
    print(f"Strict threshold: {len(cases)} real order/outer/index triples and"
          " five odd degrees; rank-three A6 is the exact equality endpoint")

if __name__=="__main__":
    mathieu()
    field4_16()
    roots()
    arithmetic()
