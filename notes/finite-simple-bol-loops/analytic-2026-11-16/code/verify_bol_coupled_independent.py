#!/usr/bin/env python3
"""Independent exact edge check for the proposed coupled pencil at h=3.

E=F_3[lambda]/Phi_7 and L=E[T]/(T^3-T-lambda).  The latter is a
field because Tr_(E/F3)(lambda)=-1.  This deliberately tests a trace
extension with Tr_(L/E)(1)=0.  No authored verifier is imported.
"""

from functools import lru_cache
from fractions import Fraction as F
from itertools import combinations, product
import json
import random


@lru_cache(None)
def digits(x):
    out = []
    for _ in range(6):
        out.append(x % 3)
        x //= 3
    return tuple(out)


def pack(xs):
    return sum((x % 3)*3**i for i, x in enumerate(xs))


@lru_cache(None)
def ea(x, y):
    return pack([a+b for a, b in zip(digits(x), digits(y))])


@lru_cache(None)
def en(x):
    return pack([-a for a in digits(x)])


@lru_cache(None)
def em(x, y):
    out = [0]*11
    for i, a in enumerate(digits(x)):
        for j, b in enumerate(digits(y)):
            out[i+j] += a*b
    for degree in range(10, 5, -1):
        c = out[degree] % 3
        out[degree] = 0
        for j in range(6):
            out[degree-6+j] -= c
    return pack(out[:6])


def ep(x, n):
    out = 1
    while n:
        if n % 2:
            out = em(out, x)
        x = em(x, x)
        n //= 2
    return out


@lru_cache(None)
def ei(x):
    assert x
    out = ep(x, 727)
    assert em(out, x) == 1
    return out


LAM = 3
LO = (1, 0, 0)
LZ = (0, 0, 0)
TT = (0, 1, 0)


def la(x, y):
    return tuple(ea(a, b) for a, b in zip(x, y))


def ln(x):
    return tuple(en(a) for a in x)


@lru_cache(None)
def lm(x, y):
    out = [0]*5
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[i+j] = ea(out[i+j], em(a, b))
    for degree in (4, 3):
        c = out[degree]
        out[degree] = 0
        out[degree-2] = ea(out[degree-2], c)
        out[degree-3] = ea(out[degree-3], em(c, LAM))
    return tuple(out[:3])


def lp(x, n):
    out = LO
    while n:
        if n % 2:
            out = lm(out, x)
        x = lm(x, x)
        n //= 2
    return out


def trace_le(x):
    return em(2, x[2])


def rank(matrix, add, neg, mul, inv):
    a = [list(row) for row in matrix]
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inverse = inv(a[r][col])
        a[r] = [mul(inverse, x) for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][col]:
                c = a[i][col]
                a[i] = [add(x, neg(mul(c, y))) for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def erank(matrix):
    return rank(matrix, ea, en, em, ei)


def prank(matrix):
    return rank(matrix, lambda a,b:(a+b)%3, lambda a:-a%3,
                lambda a,b:a*b%3, lambda a:a)


TPOW = [lp(TT, i) for i in range(5)]


def form_matrix(t):
    z = [t, lp(t, 3), lp(t, 9)]
    result = [[0]*9 for _ in range(9)]
    for axis, axis2 in product(range(3), repeat=2):
        if axis == axis2:
            continue
        remaining = 3-axis-axis2
        sign = 1 if (remaining, axis, axis2) in ((0,1,2),(1,2,0),(2,0,1)) else 2
        for degree, degree2 in product(range(3), repeat=2):
            entry = trace_le(lm(z[remaining], TPOW[degree+degree2]))
            result[3*axis+degree][3*axis2+degree2] = em(sign, entry)
    return result


# A separate exact test of the proposed product-measure maximum.
def smul(x, y):
    return (x[0]*y[0]+21*x[1]*y[1],x[0]*y[1]+x[1]*y[0])


ATOMS = [(F(2,9),F(0)),(F(7,18),F(1,18)),(F(7,18),F(-1,18))]


def weight(nu):
    out = (F(1),F(0))
    for coordinate in nu:
        out = smul(out,ATOMS[coordinate])
    return out


def rational_sum(values):
    a,b = F(0),F(0)
    for x,y in values:
        a,b = a+x,b+y
    assert b == 0
    return a


def power_sum(n):
    return rational_sum(weight((j,)*n) for j in range(3))


def check_plane_masses(k):
    weights = {nu:weight(nu) for nu in product(range(3),repeat=k)}
    count,maximum,attaining = 0,F(0),0
    for p,q in combinations(range(k),2):
        free = [(0,j) for j in range(p+1,k) if j != q]+[(1,j) for j in range(q+1,k)]
        for entries in product(range(3),repeat=len(free)):
            rows = [[0]*k for _ in range(2)]
            rows[0][p],rows[1][q] = 1,1
            for (i,j),x in zip(free,entries):
                rows[i][j] = x
            plane = [tuple((s*x+t*y)%3 for x,y in zip(*rows))
                     for s,t in product(range(3),repeat=2)]
            total = rational_sum(weights[nu] for nu in plane)
            count += 1
            if total > maximum:
                maximum,attaining = total,1
            elif total == maximum:
                attaining += 1
    assert count == ((3**k-1)*(3**k-3))//48
    assert maximum == power_sum(k-1)
    return {'k':k,'planes':count,'maximum_mass':str(maximum),'attaining_planes':attaining}


def main():
    assert ep(LAM, 7) == 1 and LAM != 1
    assert lp(TT, 729) == la(TT, (2,0,0))
    rng = random.Random(20261117)
    for x in [LO, TT, lp(TT, 2)]+[tuple(rng.randrange(729) for _ in range(3)) for _ in range(20)]:
        tr = la(la(x, lp(x,729)), lp(x,729**2))
        assert tr == (trace_le(x),0,0)
    pairing = [[trace_le(lm(TPOW[i],TPOW[j])) for j in range(3)] for i in range(3)]
    assert trace_le(LO) == 0 and erank(pairing) == 3

    basis = [(3**i,0,0) for i in range(6)]+[TT]
    matrices = [form_matrix(t) for t in basis]
    assert erank([row for a in matrices for row in a]) == 9
    vectors = [[x for row in a for x in row] for a in matrices]
    rank_e = erank(vectors)
    rank_p = prank([[digit for x in row for digit in digits(x)] for row in vectors])
    assert rank_p == 7
    samples = basis[:]
    for _ in range(64):
        t = (rng.randrange(729),rng.randrange(3),0)
        if t != LZ:
            samples.append(t)
    for t in samples:
        a = form_matrix(t)
        assert erank(a) == 6
        assert all(a[i][j] == en(a[j][i]) for i in range(9) for j in range(9))

    roots = []
    for c, d in product(range(729),range(3)):
        t = (c,d,0)
        if la(lp(t,9),ln(t)) == LZ:
            roots.append(t)
    assert len(roots) == 9

    # Realize the proposed maximizing parameter plane (s,s,s,s,s,s,t).
    aa,bb = (sum(3**i for i in range(6)),0,0),TT
    a2 = lm(aa,aa)
    def pa(x):
        return la(lp(x,3),ln(lm(a2,x)))
    uu = pa(bb)
    assert uu != LZ
    u2 = lm(uu,uu)
    actual_roots = set()
    for c,d in product(range(729),range(3)):
        x = (c,d,0)
        y = pa(x)
        if la(lp(y,3),ln(lm(u2,y))) == LZ:
            actual_roots.add(x)
    expected_roots = {la(lm((s,0,0),aa),lm((t,0,0),bb))
                      for s,t in product(range(3),repeat=2)}
    assert actual_roots == expected_roots and len(actual_roots) == 9
    plane_mass = rational_sum(weight((s,)*6+(t,)) for s,t in product(range(3),repeat=2))
    assert plane_mass == power_sum(6)
    mass_checks = [check_plane_masses(k) for k in (3,5)]
    print(json.dumps({
        'status':'PASS','h':3,'Q':729,'parameter_dimension_F3':7,
        'parameter_space':'E plus F3*T in E[T]/(T^3-T-lambda)',
        'trace_of_one':trace_le(LO),'trace_pairing_rank_E':erank(pairing),
        'sampled_nonzero_parameters':len(samples),
        'single_copy_rank_E':6,'duplicated_rank_E':12,
        'stacked_single_copy_rank_E':9,
        'tuple_rank_F3':rank_p,'tuple_rank_E':rank_e,
        'roots_in_parameter_space_of_t9_minus_t':len(roots),
        'roots_of_maximizing_plane_polynomial':len(actual_roots),
        'maximizing_seven_coordinate_plane_mass':str(plane_mass),
        'exhaustive_plane_mass_checks':mass_checks,
        'seed':20261117,
        'limits':'One h=3 trace-extension check; no proof for all h or full norm enumeration.'
    },indent=2,sort_keys=True))


if __name__ == '__main__':
    main()

