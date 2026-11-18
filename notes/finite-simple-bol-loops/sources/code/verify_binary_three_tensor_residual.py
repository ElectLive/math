"""Exact GL_3(2) cocycle, affine phase, and marked-lift controls; stdlib only."""
from collections import deque
from itertools import product


def mv(a, x):
    return sum((((a >> (3*i)) & x).bit_count() % 2) << i for i in range(3))


def outer(x, y):
    return sum((y << (3*i)) for i in range(3) if x >> i & 1)


def tr(a):
    return sum(((a >> (3*i+j)) & 1) << (3*j+i) for i,j in product(range(3), repeat=2))


def mm(a, b):
    return sum(outer(mv(a, mv(b, 1 << j)), 1 << j) for j in range(3))


def unit(i, j):
    return 1 << (3*i+j)


one = sum(unit(i, i) for i in range(3))
cyc = unit(1,0) | unit(2,1) | unit(0,2)
gen = (cyc, one | unit(0,1))
G = {a for a in range(512) if len({mv(a,x) for x in range(8)}) == 8}
P = {a for a in G if a & (one | unit(1,0) | unit(2,0) | unit(2,1)) == one}
b = one ^ unit(1,2)
assert len(G) == 168 and len(P) == 8 and b in P
edges = {(a,s):mm(a,s) for a in G for s in gen}
mul = {(a,h):mm(a,h) for a in G for h in G}
assert {x for x in range(8) if all(mv(a,x) == x for a in P)} == {0,1}
assert {x for x in range(8) if all((mv(a,x)^x) < 2 for a in P)} == {0,1,2,3}
principals = {tuple(mv(s,w)^w for s in gen) for w in range(8)}


def extend(vals):
    ans, q = {one:0}, deque([one])
    while q:
        a = q.popleft()
        for s,v in zip(gen,vals):
            h, z = edges[a,s], ans[a] ^ mv(a,v)
            if h in ans and ans[h] != z:
                return None
            if h not in ans:
                ans[h] = z
                q.append(h)
    assert set(ans) == G
    return ans


sym = {x for x in range(512) if tr(x) == x}
alt = {x for x in sym if not (x & one)}
W = {outer(x,1) for x in range(8)}
assert len(sym) == 64 and len(alt) == 8 and len(W) == 8
counts = [0,0,0]
collisions = [0,0]
for vals in product(range(8), repeat=2):
    coc = extend(vals)
    if coc is None:
        continue
    counts[0] += 1
    for (a,h),ah in mul.items():
        assert coc[ah] == (coc[a] ^ mv(a,coc[h]))
    isprin = vals in principals
    counts[1+int(not isprin)] += 1
    for K in ({0},{0,1}):
        fixed_mod = {x for x in range(8) if all((mv(a,x)^coc[a]^x) in K for a in P)}
        assert bool(fixed_mod) == isprin
    if not isprin:
        assert all(len({mv(a,x)^coc[a] for a in P}) == 8 for x in range(8))
    assert not (coc[b] & 4)
    for i,(D,Z,m0) in enumerate(((sym,{0},1),(alt,W,2))):
        products = {u ^ mm(b,v) for u in D for v in D}
        Hcoset = {outer(coc[b],m0)^z for z in Z}
        assert products & Hcoset
        collisions[i] += 1
assert counts == [16,8,8] and collisions == [16,16]
print("GL3(2) derivations / principal / fixed-point-free:", *counts)
print("Both reductions to the Sylow 2-subgroup detect all 8 nonprincipal cocycles")
print("Full/small marked-square collisions for every cocycle:", *collisions)
