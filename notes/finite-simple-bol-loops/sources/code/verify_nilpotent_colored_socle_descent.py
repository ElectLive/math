"""Finite controls for the color descent theorem. Standard library, Python 3.10+."""
from itertools import product

def tup(x, p):
    return tuple(a % p for a in x)

def add(x, y, p):
    return tup((a + b for a, b in zip(x, y)), p)

def sub(x, y, p):
    return tup((a - b for a, b in zip(x, y)), p)

def rot(x):
    return x[-1:] + x[:-1]

def rev(x):
    return x[:1] + x[:0:-1]

def norm(x, p):
    s = (0,) * len(x)
    y = x
    for _ in x:
        s = add(s, y, p)
        y = rot(y)
    return s

def cyclic_modules():
    for p in (3, 9):  # the latter is not a vector space
        D = {x + tup((-a for a in x), p) for x in product(range(p), repeat=3)}
        zero = (0,) * 6
        assert {sub(rot(x), x, p) for x in D} == D
        assert {x for x in D if rot(x) == x} == {zero}
        # C_6 cocycle specified at its generator subject only to vanishing norm.
        assert {x for x in D if norm(x, p) == zero} == D
        constants = {(k,) * 6 for k in range(p)}
        predicted = {add(x, u, p) for x in D for u in constants}
        assert len(predicted) == len(D) * p
        # For any v, (rot-1)v in D iff there is a representative invariant
        # modulo D; enumerate the entire ambient module, not sample cocycles.
        actual = {x for x in product(range(p), repeat=6) if sub(rot(x), x, p) in D}
        assert actual == predicted
        assert all(x in D for x in actual if add(x, rev(x), p) == zero)
        print(f"C6 on Z/{p}: |D|={len(D)} cyclic cocycles, all principal;"
              f" {len(actual)} phase vectors lift constants uniquely mod D")

    # Without D=[C,D] a C-invariant coset need not lift to a constant.
    p = 3
    D = {(k,) * 3 for k in range(p)}
    x = (0, 1, 2)
    assert sub(rot(x), x, p) in D and add(x, rev(x), p) == (0,) * 3
    assert not any(add(x, d, p) in D for d in D)
    assert {sub(rot(d), d, p) for d in D} == {(0,) * 3}
    # With even colors and D=[C,D], genuine displacement to a second orbit.
    p = 2
    D = {x for x in product(range(p), repeat=3) if sum(x) % 2 == 0}
    one = (1, 1, 1)
    assert {sub(rot(x), x, p) for x in D} == D and one not in D
    assert add(one, rev(one), p) == (0, 0, 0)
    assert D.isdisjoint({add(one, x, p) for x in D})
    print("Adverse C3 cases: nonsplitting constant-code coset over F3;"
          " nonzero displacement interchanges parities over F2")

def binary_rank(rows):
    echelon = {}
    for x in rows:
        while x:
            j = x.bit_length() - 1
            if j not in echelon:
                echelon[j] = x
                break
            x ^= echelon[j]
    return len(echelon)

def nonabelian_bar():
    # D8 x C3 on 4 x 3 sites; D is all four-row binary even-weight codes.
    G = list(product(range(4), range(2), range(3)))
    pos = {g: i for i, g in enumerate(G)}
    def mul(g, h):
        r, s, k = g
        a, b, c = h
        return ((r + (-1 if s else 1) * a) % 4, (s + b) % 2, (k + c) % 3)
    def act(g, x):
        r, s, k = g
        y = 0
        for i in range(4):
            j = (r + (-i if s else i)) % 4
            u, v = (x >> (2*i)) & 1, (x >> (2*i+1)) & 1
            a = (u, v, u ^ v)
            y |= a[(-k) % 3] << (2*j)
            y |= a[(1-k) % 3] << (2*j+1)
        return y
    assert all(act(mul(g, h), 1<<k) == act(g, act(h, 1<<k))
               for g in G for h in G for k in range(8))
    assert binary_rank(act(g, 1<<k) ^ (1<<k) for g in G for k in range(8)) == 8
    assert [x for x in range(256) if all(act(g, x) == x for g in G)] == [0]
    # Unnormalized, unrestricted z(g) for ALL 24 group elements. Use XOR for
    # collisions of indices in z(gh) + z(g) + g z(h) = 0.
    rows = []
    for g in G:
        pulls = [sum(((act(g, 1<<i)>>k) & 1) << i for i in range(8)) for k in range(8)]
        for h in G:
            gh = mul(g, h)
            for k in range(8):
                rows.append((1 << (8*pos[gh]+k)) ^ (1 << (8*pos[g]+k)) ^
                            (pulls[k] << (8*pos[h])))
    dim = len(G)*8 - binary_rank(rows)
    principals = {tuple(act(g, x) ^ x for g in G) for x in range(256)}
    assert dim == 8 and len(principals) == 2**dim
    print("D8 x C3 (12 sites, dimension 8): 4608 unrestricted bar equations;"
          " exactly 256 cocycles, all principal")

def true_principal_block():
    def r(x, y, k):
        for _ in range(k):
            x, y = 1-y, x
        return x, y
    states = list(product(range(2), range(2), range(3)))
    # The same color z occurs in both coordinates, so not the full product
    # on 2x3-element sites. G=C4 x C3 acts regularly on the 12 actual tuples.
    def mark(w, i, j):
        x, y, z = w
        u, v = r(x, y, i)
        return (v, u, (-z-j) % 3)
    marks = list(product(range(4), range(3)))
    assert all(mark(mark(w, *a), *a) == w for w in states for a in marks)
    assert all(sorted(mark(w, *a) for a in marks) == states for w in states)
    Y = [w for w in states if w[2] == 0]
    M = [a for a in marks if mark(Y[0], *a)[2] == 0]
    assert len(M) == 4 and all(sorted(mark(w, *a) for a in M) == Y for w in Y)
    fixed = [[sum(mark(w, *a) == w for w in Y), a[0] % 2 == 1] for a in M]
    assert sum(n for n, _ in fixed) == 4 and sum(b for _, b in fixed) == 2
    def off(w, i, j):
        x, y, z = w
        u, v = r(x, y, i)
        return (v, u, (1-z-2*j) % 6)
    even = [(x,y,2*z) for x,y,z in states]
    odd = [(x,y,2*z+1) for x,y,z in states]
    assert all(sorted(off(w, *a) for a in marks) == odd for w in even)
    assert all(off(off(w, *a), *a) == w for w in even + odd for a in marks)
    print("Actual 12 marked involutions: 12x12 uniform map and 4x4 principal"
          " block from four labels, two unpermuted; shifted control has zero diagonal block")

def field32_classes():
    # GF(32) = F2[x]/(x^5+x^2+1).
    def mult(x, y):
        z = 0
        while y:
            if y & 1:
                z ^= x
            y >>= 1
            x <<= 1
            if x & 32:
                x ^= 0b100101
        return z
    nz = tuple(range(1, 32))
    assert all({mult(a, b) for b in nz} == set(nz) for a in nz)
    # PSL2(32)=PGL2(32): translation subspaces have the unique common
    # projective fixed point infinity. Their conjugators within this family
    # must be affine, which sends the translation parameters to one scalar multiple.
    subs = {frozenset((0, a, b, a^b)) for a in nz for b in nz if a != b}
    def inner(U):
        return frozenset(frozenset(mult(a, u) for u in U) for a in nz)
    orbits = {inner(U) for U in subs}
    assert len(subs) == 155 and len(orbits) == 5 and all(len(A) == 31 for A in orbits)
    def F(A):
        return frozenset(frozenset(mult(x, x) for x in V) for V in A)
    A = next(iter(orbits))
    seen = {A}
    for _ in range(4):
        A = F(A)
        seen.add(A)
    assert seen == orbits and F(A) in seen
    assert all(F(A) != A for A in orbits)
    print("PSL2(32): 155 actual translation four-groups, 5 inner classes;"
          " Frobenius cycles all 5 (no invariant local class)")

if __name__ == "__main__":
    cyclic_modules()
    nonabelian_bar()
    true_principal_block()
    field32_classes()
