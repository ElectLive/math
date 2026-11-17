#!/usr/bin/env python3
"""Exact law, naturality, and colored Eisenstein checks; standard library only.

Universal polynomial reductions are separate from the finite table checks.
No test here asserts an exhaustive search over graphs of unbounded order.
Run without arguments from any directory. Outputs concise JSON, not artifacts.
"""
from collections import defaultdict
from itertools import product, permutations
from array import array
import json
import random


class Prime:
    def __init__(self, p):
        self.p = p
        self.zero, self.one = 0, 1
        self.elements = tuple(range(p))

    def add(self, a, b): return (a + b) % self.p
    def neg(self, a): return -a % self.p
    def mul(self, a, b): return a * b % self.p


class Eisenstein:
    """Z[omega]/(d), represented by a+b*omega, omega^2=-omega-1."""
    def __init__(self, d):
        self.d = d
        self.zero, self.one, self.omega = (0, 0), (1, 0), (0, 1)
        self.elements = tuple(product(range(d), repeat=2))

    def add(self, x, y): return ((x[0]+y[0]) % self.d, (x[1]+y[1]) % self.d)
    def neg(self, x): return (-x[0] % self.d, -x[1] % self.d)
    def mul(self, x, y):
        a, b = x; c, d = y
        return ((a*c-b*d) % self.d, (a*d+b*c-b*d) % self.d)
    def conjugate(self, x): return ((x[0]-x[1]) % self.d, -x[1] % self.d)


def sub(r, a, b): return r.add(a, r.neg(b))
def scale_int(r, k, x):
    a = r.zero
    for _ in range(abs(k)): a = r.add(a, x)
    return a if k >= 0 else r.neg(a)


def form(r, edges, u, v, scalar=False):
    terms = [r.mul(c, sub(r, r.mul(u[i], v[j]), r.mul(u[j], v[i])))
             for i, j, c in edges]
    if not scalar: return tuple(terms)
    a = r.zero
    for t in terms: a = r.add(a, t)
    return (a,)


def multiply(r, edges, x, y, kind='bol', scalar=False):
    """Element is (marker scalar, vertex tuple, central tuple)."""
    a, u, z = x; b, v, t = y
    bv = form(r, edges, u, v, scalar)
    if kind == 'bol':
        k = r.add(a, scale_int(r, 2, b))
        correction = tuple(r.mul(k, w) for w in bv)
    else:
        assert isinstance(r, Prime) and r.p == 2 and not scalar
        q = tuple(r.mul(c, r.mul(u[i], u[j])) for i, j, c in edges)
        correction = tuple(r.add(r.mul(a, w), r.mul(b, h)) for w, h in zip(bv, q))
    return (r.add(a, b), tuple(map(r.add, u, v)),
            tuple(r.add(r.add(s, t0), f) for s, t0, f in zip(z, t, correction)))


def elt(r, n, e, marker=0, vertices=(), center=(), scalar=False):
    a = r.one if marker else r.zero
    u = [r.zero]*n; z = [r.zero]*(1 if scalar else e)
    for i in vertices: u[i] = r.one
    for i in center: z[i] = r.one
    return a, tuple(u), tuple(z)


class Poly:
    """Sparse polynomial over Z; monomials are sorted tuples of variable IDs."""
    def __init__(self, terms=None): self.t = {m:c for m,c in (terms or {}).items() if c}
    @staticmethod
    def coerce(x): return x if isinstance(x, Poly) else Poly({():x})
    def __add__(self, other):
        out = defaultdict(int, self.t)
        for m, c in self.coerce(other).t.items(): out[m] += c
        return Poly(out)
    __radd__ = __add__
    def __neg__(self): return Poly({m:-c for m,c in self.t.items()})
    def __sub__(self, other): return self + -self.coerce(other)
    def __rsub__(self, other): return self.coerce(other) + -self
    def __mul__(self, other):
        out = defaultdict(int)
        for m,c in self.t.items():
            for n,d in self.coerce(other).t.items(): out[tuple(sorted(m+n))] += c*d
        return Poly(out)
    __rmul__ = __mul__
    def reduce(self, p=None, boolean=False):
        out = defaultdict(int)
        for m,c in self.t.items(): out[tuple(sorted(set(m))) if boolean else m] += c
        return {m:(c % p if p else c) for m,c in out.items() if (c % p if p else c)}


def polynomial_checks():
    variables = [Poly({(i,):1}) for i in range(14)]
    x, y, z = [tuple(variables[4*i:4*i+4]) for i in range(3)]
    alpha, beta = variables[12:14]
    def det(u, v): return u[1]*v[2]-u[2]*v[1]
    def mul(u, v, kind='bol', coefficients=None):
        if kind == 'bol':
            aa, bb = coefficients if coefficients else (1, 2)
            f = (aa*u[0]+bb*v[0])*det(u,v)
        else: f = u[0]*(u[1]*v[2]+u[2]*v[1])+v[0]*u[1]*u[2]
        return tuple(u[i]+v[i] for i in range(3))+(u[3]+v[3]+f,)
    def lhs_bol(m): return m(x,m(y,m(x,z)))
    def rhs_bol(m): return m(m(x,m(y,x)),z)
    def moufang_difference(m): return m(m(x,y),m(z,x))[3]-m(x,m(m(y,z),x))[3]
    br = lambda u,v: mul(u,v)
    assert all(not (a-b).t for a,b in zip(lhs_bol(br),rhs_bol(br)))
    assoc = br(br(x,y),z)[3]-br(x,br(y,z))[3]
    expected = x[0]*det(y,z)-y[0]*det(x,z)-2*z[0]*det(x,y)
    assert not (assoc-expected).t
    assert not moufang_difference(br).reduce(3)
    assert moufang_difference(br).t
    generic = lambda u,v: mul(u,v,coefficients=(alpha,beta))
    discrepancy = lhs_bol(generic)[3]-rhs_bol(generic)[3]
    predicted = (beta-2*alpha)*((x[0]+y[0])*det(x,z)+x[0]*det(y,z))
    assert not (discrepancy-predicted).t
    cm = lambda u,v: mul(u,v,'cubic')
    assert not (lhs_bol(cm)[3]-rhs_bol(cm)[3]).reduce(2, True)
    assert not moufang_difference(cm).reduce(2, True)
    assoc2 = cm(cm(x,y),z)[3]-cm(x,cm(y,z))[3]
    alt2 = x[0]*det(y,z)+y[0]*det(x,z)+z[0]*det(x,y)
    assert not (assoc2-alt2).reduce(2, True)
    return {'integer_bol_identity':True, 'integer_associator':True,
            'ansatz_residual_factorization':True, 'ternary_moufang_identity':True,
            'binary_cubic_identities':True}


def table_check(p, n, edge_pairs, kind, quotient_triples=False):
    r = Prime(p); edges = [(i,j,1) for i,j in edge_pairs]; e = len(edges)
    vertices = tuple(product(r.elements, repeat=n))
    centers = tuple(product(r.elements, repeat=e))
    es = [(a,u,z) for a in r.elements for u in vertices for z in centers]
    idx = {x:i for i,x in enumerate(es)}; size=len(es)
    table = [array('I', (idx[multiply(r,edges,x,y,kind)] for y in es)) for x in es]
    all_ids=set(range(size)); identity=idx[(0,(0,)*n,(0,)*e)]
    for i,row in enumerate(table):
        assert set(row)==all_ids and row[identity]==i and table[identity][i]==i
    for j in range(size): assert {table[i][j] for i in range(size)}==all_ids
    ids = [i for i,x in enumerate(es) if not any(x[2])] if quotient_triples else list(range(size))
    moufang=True; triples=0
    for a in ids:
        ta=table[a]
        for b in ids:
            tb=table[b]; ab=ta[b]; aba=ta[tb[a]]
            for c in ids:
                assert ta[tb[ta[c]]] == table[aba][c]
                if table[ab][table[c][a]] != ta[table[tb[c]][a]]: moufang=False
                triples+=1
    assert moufang == (kind=='cubic' or p==3 or not edges)
    if kind=='bol':
        inverse=[idx[(r.neg(a),tuple(map(r.neg,u)),tuple(map(r.neg,z)))] for a,u,z in es]
        for i in range(size):
            assert table[i][inverse[i]]==identity and table[inverse[i]][i]==identity
            for j in range(size): assert inverse[table[i][j]]==table[inverse[i]][inverse[j]]
    return {'kind':kind,'p':p,'n':n,'edges':edge_pairs,'order':size,
            'triple_count':triples,'central_zero_lifts_only':quotient_triples,
            'left_bol':True,'moufang':moufang,'latin':True}


def naturality_checks():
    checks=0
    for p,kind in [(2,'cubic'),(3,'bol'),(5,'bol')]:
        r=Prime(p); n=3; pairs=[(0,1),(1,2)]
        edges=[(i,j,1) for i,j in pairs]
        for perm in permutations(range(n)):
            targets=sorted((min(perm[i],perm[j]),max(perm[i],perm[j])) for i,j in pairs)
            te=[(i,j,1) for i,j in targets]
            def transport(x):
                a,u,z=x; v=[0]*n; w=[0]*len(edges)
                for i in range(n): v[perm[i]]=u[i]
                for k,(i,j) in enumerate(pairs):
                    ii,jj=perm[i],perm[j]
                    w[targets.index((min(ii,jj),max(ii,jj)))]=z[k] if ii<jj else -z[k]%p
                return a,tuple(v),tuple(w)
            rng=random.Random(1000+p)
            samples=[(rng.randrange(p),tuple(rng.randrange(p) for _ in range(n)),
                      tuple(rng.randrange(p) for _ in edges)) for _ in range(24)]
            for x,y in product(samples,repeat=2):
                assert transport(multiply(r,edges,x,y,kind))==multiply(r,te,transport(x),transport(y),kind)
                checks+=1
        # All quotient-coordinate pairs: central edge deletion and vertex retraction.
        qs=[(a,u,(0,0)) for a in r.elements for u in product(r.elements,repeat=n)]
        def edge_delete(x): return x[0],x[1],(x[2][0],)
        def vertex_delete(x): return x[0],x[1][:2],(x[2][0],)
        for x,y in product(qs,repeat=2):
            xy=multiply(r,edges,x,y,kind)
            assert edge_delete(xy)==multiply(r,edges[:1],edge_delete(x),edge_delete(y),kind)
            assert vertex_delete(xy)==multiply(r,edges[:1],vertex_delete(x),vertex_delete(y),kind)
            checks+=2
    return {'product_compatibilities':checks,'permutations':18}


def ring_and_example_checks():
    rings=[]; examples=[]; rng=random.Random(2468)
    for d in (2,3,7):
        r=Eisenstein(d); w=r.omega; w2=r.mul(w,w)
        assert r.add(r.add(w2,w),r.one)==r.zero
        for a in r.elements:
            assert r.conjugate(r.conjugate(a))==a
            for b in r.elements:
                assert r.conjugate(r.mul(a,b))==r.mul(r.conjugate(a),r.conjugate(b))
        units=[a for a in r.elements if any(r.mul(a,b)==r.one for b in r.elements)]
        six=[r.one,w,w2,r.neg(r.one),r.neg(w),r.neg(w2)]
        assert len(set(six))==(3 if d==2 else 6)
        assert len(units)=={2:3,3:6,7:36}[d]
        edges=[(0,1,w)]
        samples=[(rng.choice(r.elements),tuple(rng.choice(r.elements) for _ in range(2)),
                  (rng.choice(r.elements),)) for _ in range(48)]
        mul=lambda x,y:multiply(r,edges,x,y,scalar=True)
        for _ in range(2048):
            x,y,z=[rng.choice(samples) for __ in range(3)]
            assert mul(x,mul(y,mul(x,z)))==mul(mul(x,mul(y,x)),z)
            if d==3: assert mul(mul(x,y),mul(z,x))==mul(x,mul(mul(y,z),x))
        if d==3:
            eps=sub(r,w,r.one);assert eps!=r.zero and r.mul(eps,eps)==r.zero
        if d==7:
            a=sub(r,w,(2,0));b=sub(r,w,(4,0))
            assert a!=r.zero and b!=r.zero and r.mul(a,b)==r.zero
        rings.append({'quotient':f'Z[omega]/({d})','order':len(r.elements),
                      'characteristic':d,'units':len(units),'distinct_six_units':len(set(six)),
                      'sampled_triples':2048})
    # Split prime (2-omega) above7: omega maps to2; colors1,omega,omega² map1,2,4.
    r=Prime(7);colors=(1,2,4)
    assert set(colors).isdisjoint({-c%7 for c in colors})
    cases=[('empty',2,[]),('one_edge',2,[(0,1,1)]),
           ('reversed_edge',2,[(1,0,1)]),('recolored_edge',2,[(0,1,2)]),
           ('directed_path',3,[(0,1,1),(1,2,1)]),
           ('directed_four_cycle',4,[(0,1,1),(1,2,1),(2,3,1),(3,0,1)]),
           ('transitive_triangle',3,[(0,1,1),(1,2,1),(0,2,1)]),
           ('directed_triangle',3,[(0,1,1),(1,2,1),(2,0,1)]),
           ('colored_path',3,[(0,1,2),(1,2,4)]),
           ('cancelled_bidirected_pair',2,[(0,1,1),(1,0,1)])]
    for name,n,edges in cases:
        m=elt(r,n,1,marker=1,scalar=True)
        vi=[elt(r,n,1,vertices=(i,),scalar=True) for i in range(n)]
        mul=lambda x,y:multiply(r,edges,x,y,scalar=True)
        vals={}
        for i in range(n):
            for j in range(i+1,n):
                left=mul(mul(m,vi[i]),vi[j]);right=mul(m,mul(vi[i],vi[j]))
                expected=form(r,edges,vi[i][1],vi[j][1],True)[0]
                assert left[:2]==right[:2] and sub(r,left[2][0],right[2][0])==expected
                vals[f'{i+1},{j+1}']={'left_center':left[2][0],
                                     'right_center':right[2][0],'associator':expected}
        examples.append({'name':name,'marker_edge_products':vals})
    # Doubled roles: arcs0->1 and1->0 use distinct coordinate pairs (0,3),(1,2).
    edges=[(0,3,1),(1,2,2)]; n=4
    basis=[elt(r,n,1,vertices=(i,),scalar=True) for i in range(n)]
    assert form(r,edges,basis[0][1],basis[3][1],True)==(1,)
    assert form(r,edges,basis[1][1],basis[2][1],True)==(2,)
    # Explicit proper-Bol right-alternative failure over7.
    edges=[(0,1,1)]; x=elt(r,2,1,vertices=(0,),scalar=True)
    y=elt(r,2,1,marker=1,vertices=(1,),scalar=True)
    mul=lambda a,b:multiply(r,edges,a,b,scalar=True)
    left=mul(mul(x,y),y);right=mul(x,mul(y,y))
    assert left[:2]==right[:2] and sub(r,left[2][0],right[2][0])==4
    # Scalar quadratic collapse P3 -> K2 plus isolate in characteristic2.
    r=Prime(2)
    for x in product(range(2),repeat=3):
        y=(x[0]^x[2],x[1],x[2])
        assert (x[0]*x[1]+x[1]*x[2])%2==y[0]*y[1]
    return {'rings':rings,'examples':examples,'doubled_bidirected_values':[1,2],
            'proper_bol_witness_centers':[left[2][0],right[2][0]],'scalar_collapse':True}


def main():
    out={'polynomial':polynomial_checks()}
    tables=[]
    possible=[(0,1),(0,2),(1,2)]
    for mask in range(8):
        edges=[v for i,v in enumerate(possible) if mask>>i&1]
        tables.append(table_check(2,3,edges,'cubic'))
    for p in (2,3,5):
        tables.append(table_check(p,2,[(0,1)],'bol',quotient_triples=(p==5)))
    tables.append(table_check(2,2,[],'bol'))
    out['finite_tables']=tables
    out['naturality']=naturality_checks()
    out['colored_arithmetic']=ring_and_example_checks()
    out['status']='all checks passed'
    print(json.dumps(out,sort_keys=True,indent=2))


if __name__=='__main__': main()
