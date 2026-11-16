#!/usr/bin/env python3
"""Reproduce the exponent-4 Bruck section for Nagy's fixed (G,H).

Standalone Python 3.11+ certificate. Permutations follow Nagy arXiv:
0709.4544v1 Lemma 3.2; the source comparison uses Baumeister--Stein,
BS.pdf Remark 3.5. This is not a census of all order-96 loops.
"""
from collections import Counter

assert __debug__, 'Assertions must be enabled.'
N = 40
ID = tuple(range(N))

def cycles(*items):
    p = list(ID)
    for cycle in items:
        for i, a in enumerate(cycle):
            p[a - 1] = cycle[(i + 1) % len(cycle)] - 1
    return tuple(p)

def mul(a, b):
    return tuple(a[x] for x in b)

def inv(a):
    out = [0] * len(a)
    for i, x in enumerate(a):
        out[x] = i
    return tuple(out)

def conj(a, g):
    return mul(inv(g), mul(a, g))

def generated(generators):
    gens = list(dict.fromkeys(list(generators) + [inv(g) for g in generators]))
    seen, queue = {ID}, [ID]
    for x in queue:
        for g in gens:
            y = mul(x, g)
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen

def orbit(x, gens):
    seen, queue = {x}, [x]
    for y in queue:
        for g in gens:
            z = conj(y, g)
            if z not in seen:
                seen.add(z)
                queue.append(z)
    return seen

def orbit_partition(items, gens):
    remain, out = set(items), []
    while remain:
        part = orbit(min(remain), gens)
        assert part <= remain
        remain -= part
        out.append(part)
    return out

def small_generators(items):
    subgroup, gens = {ID}, []
    for x in sorted(items):
        if x not in subgroup:
            gens.append(x)
            subgroup = generated(gens)
    assert set(items) <= subgroup
    return gens

# Nagy's explicit generators. Composition is the usual left action; his GAP
# right-action product c*d corresponds to mul(d,c).
c = cycles((1,4),(2,9),(3,10),(6,11),(7,12),(13,21),(14,22),
           (15,24),(16,23),(17,30),(18,29),(19,31),(20,32),(33,35),(38,40))
d = cycles((1,2,4,6,8,7,5,3),(9,13,25,18,10,14,26,17),
           (11,15,27,20,12,16,28,19),(21,30,38,34,23,31,40,35),
           (22,32,39,36,24,29,37,33))
gens = (c,d,inv(c),inv(d))
G = generated((c,d))
assert len(G) == 3840
u = mul(mul(d,d),mul(d,d))
J = generated(orbit(u, gens))
assert len(J) == 32 and all(mul(a,b) == mul(b,a) for a in J for b in J)
M = generated([mul(inv(j),conj(j,g)) for j in J for g in (c,d)])
assert len(M) == 16 and M <= J
P = generated((mul(d,c),))
assert len(P) == 5
H = {g for g in G if {conj(p,g) for p in P} == P}
assert len(H) == 40 and len(H & J) == 2 and H & M == {ID}
z = next(iter((H & J) - {ID}))
assert all(mul(z,h) == mul(h,z) for h in H)
assert any(mul(z,g) != mul(g,z) for g in (c,d))

# Calculate Hom_S5(J*,J) from the 6-point action. Matrices are column bit
# masks. Gaussian elimination imposes both generator intertwining equations.
def aj(v, p):
    out = 0
    for i in range(5):
        if v >> i & 1:
            out ^= 1 << p[i]
    return out ^ 63 if out & 32 else out

def matrix_inverse(a):
    n=len(a); piv={}
    for i,col in enumerate(a):
        x,y=col,1<<i
        while x:
            j=x.bit_length()-1
            if j in piv:
                x^=piv[j][0]; y^=piv[j][1]
            else:
                piv[j]=(x,y); break
    assert len(piv)==n
    out=[]
    for i in range(n):
        x,y=1<<i,0
        while x:
            j=x.bit_length()-1
            x^=piv[j][0]; y^=piv[j][1]
        out.append(y)
    return tuple(out)

def dual(a):
    b=matrix_inverse(a)
    return tuple(sum(((b[j]>>i)&1)<<j for j in range(len(b))) for i in range(len(b)))

def matrix_rank(rows):
    piv={}
    for x in rows:
        while x:
            j=x.bit_length()-1
            if j in piv:x^=piv[j]
            else:piv[j]=x; break
    return len(piv)

pc=(1,0,3,2,5,4); pd=(0,2,3,4,1,5)
# Match the abstract six-point module to the explicitly generated radical:
# label the conjugates of d^4 by the two six-point generator permutations.
point_values={0:u}; points=[0]
for i in points:
    for g,p in ((c,pc),(d,pd)):
        target=p[i]; value=conj(point_values[i],inv(g))
        if target not in point_values:
            point_values[target]=value; points.append(target)
        else:
            assert point_values[target]==value
assert len(point_values)==len(set(point_values.values()))==6
product=ID
for i in range(6):product=mul(product,point_values[i])
assert product==ID
jvec=[]
for mask in range(32):
    value=ID
    for i in range(5):
        if mask>>i&1:value=mul(value,point_values[i])
    jvec.append(value)
assert set(jvec)==J
for mask in range(32):
    for g,p in ((c,pc),(d,pd)):
        assert conj(jvec[mask],inv(g))==jvec[aj(mask,p)]
JM=tuple(tuple(aj(1<<i,p) for i in range(5)) for p in (pc,pd))
ED=tuple(dual(a) for a in JM)
rows=[]
for A,B in zip(ED,JM):
    for j in range(5):
        for i in range(5):
            row=0
            for k in range(5):
                if A[j]>>k&1:row^=1<<(5*k+i)
                if B[k]>>i&1:row^=1<<(5*j+k)
            rows.append(row)
assert matrix_rank(rows)==24
# Relative derivations vanishing on F20 are Hom(J*,J), dimension one. The
# nonzero one is conjugation by z because z centralizes H but not G.

jorbits=orbit_partition(J,gens)
assert sorted(map(len,jorbits))==[1,6,10,15]
assert {x for part in jorbits if z in part or len(part)==10 for x in part} == J-M
assert {mul(z,x) for x in M} == J-M
outer={g for g in G-J if mul(g,g)==ID}
assert len(outer)==80 and outer==orbit(c,gens)
K=M | {mul(z,x) for x in outer}
assert len(K)==96 and ID in K
assert all(conj(k,h) in K for k in K for h in H)
# BS Remark 3.5: z is v1 and c is v1*y_*n_*. Its specified JH-orbit
# of y_*n_* is therefore the following orbit of z*c.
JH={mul(j,h) for j in J for h in H}
assert len(JH)==640
assert {conj(mul(z,c),g) for g in JH} == K-M
assert generated(small_generators(K)) == G
core=set(H)
for g in G:
    core &= {conj(h,g) for h in H}
    if core=={ID}:break
assert core=={ID}
print('G,H,J,M,outer,K:',len(G),len(H),len(J),len(M),len(outer),len(K))
print('Hom(J*,J): 1; J orbits: 1,6,10,15; source JH orbit agrees')
print('G=<K>; H core-free; marked radical section forced to M')

# Enumerate every normal subgroup: each is generated by the conjugacy classes
# it contains; joins of all class normal closures exhaust the normal lattice.
classes=orbit_partition(G,gens)
closures={}
for part in classes:
    if ID in part:continue
    # Generate the subgroup generated by the entire conjugacy class using a
    # short accumulating basis; the class itself need not be a subgroup.
    subgroup={ID}; basis=[]
    for g in sorted(part):
        if g not in subgroup:
            basis.append(g); subgroup=generated(basis)
    assert part <= subgroup
    closures[frozenset(subgroup)]=basis
lattice={frozenset([ID]):[]}; queue=[frozenset([ID])]
for normal in queue:
    for closure,basis in closures.items():
        if closure<=normal:continue
        newbasis=lattice[normal]+basis
        new=frozenset(generated(newbasis))
        if new not in lattice:
            lattice[new]=newbasis; queue.append(new)
assert sorted(map(len,lattice))==[1,16,32,1920,3840]
for normal in sorted(lattice,key=len):
    if len(normal)==1:continue
    HR={mul(h,r) for h in H for r in normal}
    if len(HR)==len(G):
        print('normal',len(normal),'is H-transitive'); continue
    images={frozenset(mul(k,r) for r in normal) for k in K}
    index=len(G)//len(HR)
    assert (len(normal),len(images),index) in {(16,21,6),(32,11,6)}
    assert len(images)!=index
    print('normal',len(normal),'section images',len(images),'quotient index',index)

# Directly verify the left-coset folder and its complete loop table. The
# opposite is the right-Bol convention of the primary sources.
K=[ID]+sorted(K-{ID}); H=sorted(H)
for s in K:
    hs={conj(h,s) for h in H}; seen=set()
    for k in K:
        block={mul(k,h) for h in hs}
        assert not (seen & block)
        seen |= block
    assert seen==G
kset=set(K)
for a in K:
    assert inv(a) in kset
    for b in K:assert mul(a,mul(b,a)) in kset
representative={mul(k,h):i for i,k in enumerate(K) for h in H}
assert len(representative)==len(G)
table=[[representative[mul(a,b)] for b in K] for a in K]
n=len(K); full=set(range(n))
assert all(set(row)==full for row in table)
assert all({table[i][j] for i in range(n)}==full for j in range(n))
assert all(table[x][table[y][table[x][z0]]] == table[table[x][table[y][x]]][z0]
           for x in range(n) for y in range(n) for z0 in range(n))
inverse=[next(y for y in range(n) if table[x][y]==table[y][x]==0) for x in range(n)]
assert all(inverse[table[x][y]]==table[inverse[x]][inverse[y]] for x in range(n) for y in range(n))
orders=[]
for x in range(n):
    p=0
    for k in range(1,5):
        p=table[x][p]
        if p==0:orders.append(k);break
    else:raise AssertionError('order greater than four')
assert Counter(orders)=={1:1,2:15,4:80}
witness=next((x,y,z0) for x in range(n) for y in range(n) for z0 in range(n)
             if table[table[x][y]][table[z0][x]] != table[table[x][table[y][z0]]][x])
print('folder: all H-conjugates; left Bol and AIP: passed')
print('element orders:',dict(sorted(Counter(orders).items())))
print('non-Moufang witness (indices):',witness)
print('simple: exhaustive normal-subgroup quotient test passed')
