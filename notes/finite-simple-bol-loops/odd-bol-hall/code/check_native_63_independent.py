"""Reconstruct the loop as actual permutations of 63 affine planes over F7, with no scalar product formula input."""
from itertools import product
from collections import Counter
from hashlib import sha256

Q=7; G=range(3); F=range(7); zeta=(1,2,4)
basis=list(product(G,G,F))
W={(a,b,b) for a,b in product(F,F)}
vec=(0,1,6)
def add(u,v):
    return tuple((a+b)%7 for a,b in zip(u,v))
def wh(x,y,v):
    # Z^(xy/2) X^x Y^y, operating on an actual vector.
    return tuple((v[(k-x)%3] * zeta[(2*x*y+((k-x)%3)*y)%3])%7 for k in G)
def rep(x,y,h):
    shift=wh((2*x)%3,(2*y)%3,tuple(t*h%7 for t in vec))
    return {v:add(wh(x,y,v),shift) for v in product(F,F,F)}
M=[rep(*r) for r in basis]
def real_table(e):
    base=frozenset(add(s,tuple(e*j%7 for j in vec)) for s in W)
    P=[frozenset(g[s] for s in base) for g in M]
    num={s:i for i,s in enumerate(P)}
    assert len(num)==63 and len(set(P[0]))==49
    return [[num[frozenset(g[v] for v in b)] for b in P] for g in M]
def closure(T,U):
    S={0,*U}
    while True:
        R=S|{T[x][y] for x,y in product(S,S)}
        if R==S:return frozenset(S)
        S=R
def check(T):
    V=list(range(63))
    assert list(T[0])==V and [r[0] for r in T]==V
    assert all(set(r)==set(V) for r in T+list(zip(*T)))
    n=0
    for a,b in product(V,repeat=2):
        w=T[a][T[b][a]]
        central=T[w]
        assert all(central[c]==T[a][T[b][T[a][c]]] for c in V)
        n+=len(V)
    groups=Counter(len(closure(T,[x])) for x in V)
    sections={closure(T,[7+h,21+k]) for h,k in product(F,F)}
    for U in sections:
        pr={(v//21,(v//7)%3) for v in U}
        assert len(pr)==9
        if len(U)==9:assert all(T[x][y]==T[y][x] for x,y in product(U,U))
    return n,groups,sections
for e in (1,0):
    T=real_table(e)
    triples,ord_,gen=check(T)
    text=''.join(','.join(map(str,row))+'\n' for row in T).encode()
    digest=sha256(text).hexdigest()
    expected={1:'5d3a7c768043e044bd644ffbee89bb62e36a6977d9c295c00d5bc555d13c5795'}
    if e in expected:assert digest==expected[e]
    assert ord_=={1:1,3:56,7:6}
    assert sum(len(U)==9 for U in gen)==(49 if e==0 else 0)
    noncomm=sum(T[7+h][21+k]!=T[21+k][7+h] for h,k in product(F,F))
    assert noncomm==(49 if e==1 else 0)
    inverse=[next(v for v in range(63) if T[v][u]==T[u][v]==0) for u in range(63)]
    invauto=all(inverse[T[x][y]]==T[inverse[x]][inverse[y]] for x,y in product(range(63),repeat=2))
    print('e=',e,'physical affine planes=63, Latin, Bol triples=',triples,'cyclic sizes=',sorted(ord_.items()))
    print('two basis lift section closures:',sorted(Counter(map(len,gen)).items()),'noncommuting among all 49 basis lifts=',noncomm,'automorphic inverse=',invauto)
    print('table SHA256',digest,'ralt witness (1*7)*7 vs 1*(7*7):',T[T[1][7]][7],T[1][T[7][7]])
print('PASS')
