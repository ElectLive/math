#!/usr/bin/env python3
"""Exact diagnostics for intrinsic frames and the broader hyperplane deck.

Standard library only. Exhaustive and sampled frame scopes are reported apart.
General claims are proved in manuscripts/loop-deletion-decks.md.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations, product
import json
import random


def rank(rows, p):
    a = [list(x) for x in rows]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        j = next((j for j in range(r, len(a)) if a[j][c] % p), None)
        if j is None:
            continue
        a[r], a[j] = a[j], a[r]
        inv = pow(a[r][c] % p, -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for j in range(len(a)):
            if j != r and a[j][c] % p:
                t = a[j][c] % p
                a[j] = [(x - t*y) % p for x, y in zip(a[j], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def unit(n, i):
    return tuple(int(j == i) for j in range(n))


@lru_cache(None)
def vectors(p, n):
    return tuple(product(range(p), repeat=n))


def lincomb(coeff, rows, dim, p):
    return tuple(sum(c*v[j] for c, v in zip(coeff, rows)) % p
                 for j in range(dim))


class Form:
    def __init__(self, p, n, e, entries):
        self.p, self.n, self.e = p, n, e
        self.entries = tuple((i, j, tuple(z)) for i, j, z in entries)

    @classmethod
    def graph(cls, p, n, edges):
        edges = tuple(sorted(edges))
        return cls(p, n, len(edges), [(i, j, unit(len(edges), k))
                                    for k, (i, j) in enumerate(edges)])

    def b(self, u, v):
        z = [0]*self.e
        for i, j, out in self.entries:
            scalar = u[i]*v[j] - u[j]*v[i]
            for k, val in enumerate(out):
                z[k] += scalar*val
        return tuple(t % self.p for t in z)

    def mul(self, x, y):
        a, b = x[0], y[0]
        u, v = x[1:1+self.n], y[1:1+self.n]
        z = self.b(u, v)
        return ((a+b) % self.p,) + tuple((i+j) % self.p for i, j in zip(u, v)) + tuple(
            (x[1+self.n+k] + y[1+self.n+k] + (a+2*b)*z[k]) % self.p
            for k in range(self.e))

    def associator(self, x, y, z):
        a, b, c = x[0], y[0], z[0]
        u, v, w = (t[1:1+self.n] for t in (x, y, z))
        vw, uw, uv = self.b(v, w), self.b(u, w), self.b(u, v)
        return tuple((a*r-b*s-2*c*t) % self.p for r, s, t in zip(vw, uw, uv))

    def zero(self):
        return (0,)*(1+self.n+self.e)

    def lift(self, a, u, z=None):
        return (a,) + tuple(u) + ((0,)*self.e if z is None else tuple(z))


def generated(form, gens):
    found = {form.zero()}
    queue = deque()
    for g in gens:
        if g not in found:
            found.add(g)
            queue.append(g)
    while queue:
        x = queue.popleft()
        for y in tuple(found):
            for z in (form.mul(x, y), form.mul(y, x)):
                if z not in found:
                    found.add(z)
                    queue.append(z)
    return found


@lru_cache(None)
def canonical_graph(n, edges):
    if n == 0:
        return ()
    return min(tuple(sorted(tuple(sorted((perm[i], perm[j]))) for i, j in edges))
               for perm in permutations(range(n)))


def graph_deck(n, edges):
    cards = []
    for deleted in range(n):
        keep = [i for i in range(n) if i != deleted]
        index = {v: i for i, v in enumerate(keep)}
        ee = tuple(sorted((index[i], index[j]) for i, j in edges
                          if i != deleted and j != deleted))
        cards.append(canonical_graph(n-1, ee))
    return tuple(sorted(cards))


def all_bases(p, n):
    if n == 0:
        return [()]
    nonzero = vectors(p, n)[1:]
    return [rows for rows in product(nonzero, repeat=n) if rank(rows, p) == n]


def sample_bases(p, n, count, rng):
    ans = []
    while len(ans) < count:
        rows = tuple(tuple(rng.randrange(p) for _ in range(n)) for _ in range(n))
        if rank(rows, p) == n:
            ans.append(rows)
    return ans


def test_frames():
    rng = random.Random(447)
    totals = Counter()
    for p, n, sampled in ([(2, n, False) for n in range(4)] +
                          [(5, n, False) for n in range(3)] +
                          [(2, 4, True), (5, 3, True)]):
        pairs = tuple(combinations(range(n), 2))
        bases = sample_bases(p, n, 32, rng) if sampled else all_bases(p, n)
        for flags in product((0, 1), repeat=len(pairs)):
            edges = tuple(e for e, flag in zip(pairs, flags) if flag)
            f = Form.graph(p, n, edges)
            expected = graph_deck(n, edges)
            for basis in bases:
                label = 'sampled' if sampled else 'exhaustive'
                totals[label+'_frames'] += 1
                vals = [(ij, f.b(basis[ij[0]], basis[ij[1]])) for ij in pairs]
                nz = [(ij, z) for ij, z in vals if any(z)]
                if len(nz) != f.e or rank([z for _, z in nz], p) != f.e:
                    continue
                totals[label+'_admissible'] += 1
                h_edges = tuple(ij for ij, _ in nz)
                assert canonical_graph(n, h_edges) == canonical_graph(n, edges)
                assert graph_deck(n, h_edges) == expected
    return dict(totals)


def test_lifts_and_generation():
    rng = random.Random(446447)
    cases = [
        (Form.graph(2, 2, [(0, 1)]), (unit(2, 0), unit(2, 1)), 1, (0, 0)),
        (Form.graph(5, 2, [(0, 1)]), (unit(2, 0), unit(2, 1)), 2, (0, 0)),
        (Form.graph(2, 3, [(0, 1)]), tuple(unit(3, i) for i in range(3)), 1, (0, 0, 1)),
        (Form.graph(2, 3, [(0, 1), (1, 2)]), ((1, 0, 1), (0, 1, 0), (0, 0, 1)), 1, (0, 0, 0)),
        (Form.graph(2, 4, [(0, 1), (2, 3)]), tuple(unit(4, i) for i in range(4)), 1, (0, 0, 0, 0)),
    ]
    cards, comparisons = 0, 0
    for f, basis, scale, radical in cases:
        central = [tuple(rng.randrange(f.p) for _ in range(f.e)) for _ in range(f.n+1)]
        marker = f.lift(scale, radical, central[0])
        lifts = [f.lift(0, w, central[i+1]) for i, w in enumerate(basis)]
        for omitted in range(f.n):
            keep = [j for j in range(f.n) if j != omitted]
            rows = [basis[j] for j in keep]
            cpairs = list(combinations(range(len(keep)), 2))
            cedges = [ij for ij in cpairs if any(f.b(rows[ij[0]], rows[ij[1]]))]
            outputs = [tuple(scale*t % f.p for t in f.b(rows[i], rows[j])) for i, j in cedges]
            model = Form.graph(f.p, f.n-1, cedges)

            def transport(x):
                a, coeff, z = x[0], x[1:f.n], x[f.n:]
                u = lincomb(coeff, rows, f.n, f.p)
                u = tuple((u[j]+a*radical[j]) % f.p for j in range(f.n))
                out = lincomb(z, outputs, f.e, f.p)
                out = tuple((out[k]+a*central[0][k]+sum(
                    coeff[j]*central[keep[j]+1][k] for j in range(len(keep)))) % f.p
                            for k in range(f.e))
                return f.lift(a*scale % f.p, u, out)

            elements = vectors(f.p, 1+model.n+model.e)
            images = {transport(x) for x in elements}
            actual = generated(f, [marker]+[lifts[j] for j in keep])
            assert len(images) == len(elements) and images == actual
            for x in elements:
                for y in elements:
                    assert f.mul(transport(x), transport(y)) == transport(model.mul(x, y))
                    comparisons += 1
            cards += 1
    return {'actual_generated_cards': cards, 'card_product_transports': comparisons}


def hyperplanes(p, n):
    for ell in vectors(p, n)[1:]:
        pivot = next(i for i, t in enumerate(ell) if t)
        if ell[pivot] != 1:
            continue
        basis = []
        for j in range(n):
            if j != pivot:
                v = list(unit(n, j)); v[pivot] = (-ell[j]) % p
                basis.append(tuple(v))
        yield basis


def image_dimension(f, basis):
    return rank([f.b(u, v) for u, v in combinations(basis, 2)], f.p)


def scalar_rank(f, basis):
    return rank([[f.b(u, v)[0] for v in basis] for u in basis], f.p)


def test_hyperplanes():
    checked = 0
    for p in (2, 5):
        for n in range(2, 5):
            for r in range(n//2+1):
                f = Form(p, n, 1, [(2*i, 2*i+1, (1,)) for i in range(r)])
                got = Counter(scalar_rank(f, h) for h in hyperplanes(p, n))
                total = (p**n-1)//(p-1)
                if r == 0:
                    expected = Counter({0: total})
                else:
                    small = (p**(2*r)-1)//(p-1)
                    expected = Counter({2*r-2: small})
                    if total > small:
                        expected[2*r] = total-small
                assert got == expected, (p, n, r, got, expected)
                checked += total
    return {'scalar_hyperplanes_checked': checked, 'fields': [2, 5], 'dimensions': [2, 3, 4]}


def test_obstructions():
    result = {}
    for p in (2, 5):
        f = Form.graph(p, 2, [(0, 1)])
        bad = f.lift(1, (1, 0)); v2 = f.lift(0, (0, 1))
        size = len(generated(f, [bad, v2]))
        assert size == p**3
        assert f.associator(v2, bad, bad) == (3 % p,)
        marker = f.lift(1, (0, 0)); v1 = f.lift(0, (1, 0))
        z = f.lift(0, (0, 0), (1,))
        assert len(generated(f, [marker, v1])) == p**2
        assert len(generated(f, [marker, v1, z])) == p**3
        result['bad_marker_p'+str(p)] = {'wrong_order': size, 'correct_order': p**2}
    f0 = Form.graph(2, 4, [(0, 1), (2, 3)])
    f1 = Form(2, 4, 1, [(0, 1, (1,)), (2, 3, (1,))])
    basis = tuple(unit(4, i) for i in range(4))
    cardsets = []
    for f in (f0, f1):
        m = f.lift(1, (0,)*4)
        cards = [generated(f, [m]+[f.lift(0, basis[j]) for j in range(4) if j != i])
                 for i in range(4)]
        assert [len(c) for c in cards] == [32]*4
        cardsets.append(cards)
    def quotient(x):
        return x[:5]+((x[5]+x[6]) % 2,)
    for c0, c1 in zip(*cardsets):
        assert {quotient(x) for x in c0} == c1
        for x in c0:
            for y in c0:
                assert quotient(f0.mul(x, y)) == f1.mul(quotient(x), quotient(y))
    mixed = ((1, 0, 1, 0), unit(4, 1), unit(4, 2), unit(4, 3))
    m0 = f0.lift(1, (0,)*4)
    sizes = [len(generated(f0, [m0]+[f0.lift(0, mixed[j]) for j in range(4) if j != i]))
             for i in range(4)]
    assert sizes == [32, 32, 64, 32]
    d0 = Counter(2**(4+image_dimension(f0, h)) for h in hyperplanes(2, 4))
    d1 = Counter(2**(4+image_dimension(f1, h)) for h in hyperplanes(2, 4))
    assert d0 == {32: 6, 64: 9} and d1 == {32: 15}
    result.update({'amalgamation_parent_orders': [128, 64],
                   'common_coordinate_card_orders': [32]*4,
                   'nonadmissible_basis_card_orders': sizes,
                   'hyperplane_decks': [dict(d0), dict(d1)],
                   'quotient_card_product_comparisons': 4096})
    return result


def main():
    print(json.dumps({'status': 'all checks passed', 'seed': 447,
                      'frames': test_frames(),
                      'lifts': test_lifts_and_generation(),
                      'hyperplanes': test_hyperplanes(),
                      'obstructions': test_obstructions()}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
