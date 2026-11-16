#!/usr/bin/env python3
"""Exact finite checks for the shared-input reciprocal Bol Gram theorem.

Standard library only.  F_729 is F_3[lambda]/Phi_7(lambda).  Complex roots
of unity are handled exactly in Q[zeta_21]/Phi_21, never in floating point.
The full E^6 Gram matrix is not enumerated.  A stated 27-input restriction
of an actual loop readout checks the Gram and Fourier formulas directly.
Finite checks are evidence, not proofs of the general/tensor statements.
"""

from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
import random


# ---- F_729, with lambda satisfying 1+lambda+...+lambda^6=0. ----

@lru_cache(None)
def digits(a):
    return tuple((a // (3**i)) % 3 for i in range(6))


def encode(v):
    return sum((a % 3) * 3**i for i, a in enumerate(v))


@lru_cache(None)
def add(a, b):
    return encode([x + y for x, y in zip(digits(a), digits(b))])


@lru_cache(None)
def neg(a):
    return encode([-x for x in digits(a)])


def sub(a, b):
    return add(a, neg(b))


@lru_cache(None)
def mul(a, b):
    av, bv = digits(a), digits(b)
    v = [0] * 11
    for i, x in enumerate(av):
        if x:
            for j, y in enumerate(bv):
                v[i + j] += x * y
    for i in range(10, 5, -1):
        c = v[i] % 3
        if c:
            for j in range(6):
                v[i - 6 + j] -= c
    return encode(v[:6])


def power(a, n):
    v = 1
    while n:
        if n & 1:
            v = mul(v, a)
        a = mul(a, a)
        n //= 2
    return v


@lru_cache(None)
def inverse(a):
    assert a
    v = power(a, 727)
    assert mul(a, v) == 1
    return v


def trace(a):
    return (2 * sum(digits(a)[1:])) % 3


LAM = 3
LPOW = [power(LAM, t) for t in range(7)]


def matrix_rank(matrix):
    a = [list(row) for row in matrix]
    if not a:
        return 0
    rank = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        z = inverse(a[rank][j])
        a[rank] = [mul(z, x) for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][j]:
                z = a[i][j]
                a[i] = [sub(x, mul(z, y)) for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def cross_matrix(nu):
    a, b, c = nu
    return [[0, neg(c), b], [c, 0, neg(a)], [neg(b), a, 0]]


def pencil(nu, family):
    a = [[0] * 6 for _ in range(6)]
    if family == "good":
        c = cross_matrix(nu)
        for offset in (0, 3):
            for i in range(3):
                for j in range(3):
                    a[offset + i][offset + j] = c[i][j]
    else:
        for i, x in enumerate(nu):
            a[0][i + 1] = x
            a[i + 1][0] = neg(x)
        ell = 0
        for i, x in enumerate(nu):
            ell = add(ell, mul(x, LPOW[i]))
        a[4][5], a[5][4] = ell, neg(ell)
    return a


PARAMS = list(product(range(3), repeat=3))
BASIS = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
SPARSE = {
    family: [
        [(i, j, a[i][j]) for i in range(6) for j in range(6) if a[i][j]]
        for a in (pencil(nu, family) for nu in BASIS)
    ]
    for family in ("good", "aligned")
}


def beta(x, y, family):
    ans = []
    for entries in SPARSE[family]:
        z = 0
        for i, j, b in entries:
            z = add(z, mul(mul(x[i], b), y[j]))
        ans.append(trace(z))
    return tuple(ans)


def gamma(v, w):
    return sum(v[2*i] * w[2*i+1] - v[2*i+1] * w[2*i] for i in range(3)) % 7


def d_action(a, v):
    return tuple(pow(2, a[i // 2] % 3, 7) * v[i] % 7 for i in range(6))


def loop_mul(x, y, family):
    u, v, a, t = x
    yy, w, b, s = y
    by = beta(u, yy, family)
    dw = d_action(a, w)
    return (
        tuple(add(xx, mul(LPOW[t], zz)) for xx, zz in zip(u, yy)),
        tuple((xx + zz) % 7 for xx, zz in zip(v, dw)),
        tuple((aa + bb - cc) % 3 for aa, bb, cc in zip(a, b, by)),
        (t + s - gamma(v, w)) % 7,
    )


# ---- Exact cyclotomic arithmetic in Q[zeta_21]/Phi_21. ----
# Phi_21 = x^12-x^11+x^9-x^8+x^6-x^4+x^3-x+1.
PHI21 = (1, -1, 0, 1, -1, 0, 1, 0, -1, 1, 0, -1, 1)
CZ = (F(0),) * 12
CO = (F(1),) + (F(0),) * 11


def cadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def cscale(a, q):
    return tuple(q * x for x in a)


def csum(xs):
    ans = CZ
    for x in xs:
        ans = cadd(ans, x)
    return ans


@lru_cache(None)
def cmul(a, b):
    v = [F(0)] * 23
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    v[i+j] += x*y
    for i in range(22, 11, -1):
        c = v[i]
        if c:
            for j in range(12):
                if PHI21[j]:
                    v[i-12+j] -= c * PHI21[j]
    return tuple(v[:12])


CX = (F(0), F(1)) + (F(0),) * 10
ZPOW = [CO]
for _ in range(21):
    ZPOW.append(cmul(ZPOW[-1], CX))
assert ZPOW[21] == CO


def root(n):
    return ZPOW[n % 21]


def conjugate(a):
    return csum(cscale(root(-i), x) for i, x in enumerate(a) if x)


def abs_square(a):
    return cmul(a, conjugate(a))


def rational(a):
    assert all(x == 0 for x in a[1:]), a
    return a[0]


# Match hhat(nu) = E_a h(a) e_3(-nu*a) in the manuscript.
G = [cscale(csum(root(3*pow(2, a, 7)-7*nu*a) for a in range(3)), F(1, 3))
     for nu in range(3)]
WONE = [abs_square(g) for g in G]
WEIGHT = {nu: cmul(cmul(WONE[nu[0]], WONE[nu[1]]), WONE[nu[2]])
          for nu in PARAMS}


def weighted_mass(predicate, remove_zero=False):
    return rational(csum(w for nu, w in WEIGHT.items()
                         if (not remove_zero or any(nu)) and predicate(nu)))


def dot(a, b, modulus=3):
    return sum(x*y for x, y in zip(a, b)) % modulus


def projective(v):
    return any(v) and next(x for x in v if x) == 1


def hyperplane_expected(v):
    nz = [x for x in v if x]
    if len(nz) == 1:
        return F(154, 729)
    if len(nz) == 2:
        return F(154 if nz[0] == nz[1] else 343, 729)
    return F(280 if len(set(nz)) == 1 else 217, 729)


def check_weights():
    assert rational(WONE[0]) == F(2, 9)
    assert rational(cadd(WONE[1], WONE[2])) == F(7, 9)
    assert rational(cmul(WONE[1], WONE[2])) == F(7, 81)
    assert rational(csum(WONE)) == 1
    assert weighted_mass(lambda _: True, True) == F(721, 729)
    table = []
    for v in PARAMS:
        if projective(v):
            mass = weighted_mass(lambda nu: dot(v, nu) == 0, True)
            assert mass == hyperplane_expected(v), (v, mass)
            table.append({"direction": v, "mass": str(mass)})
    assert len(table) == 13
    assert max(F(row["mass"]) for row in table) == F(343, 729)
    assert weighted_mass(lambda nu: nu[0] == nu[1] == nu[2], True) == F(196, 729)
    assert weighted_mass(lambda nu: nu[0] == nu[1] and nu[2] == -nu[0] % 3,
                         True) == F(49, 729)
    return table


def check_field_and_ranks():
    assert power(LAM, 7) == 1 and len(set(LPOW)) == 7
    for a in range(729):
        f, tr = a, 0
        for _ in range(6):
            tr = add(tr, f)
            f = power(f, 3)
        assert tr == trace(a)
        if a:
            assert mul(a, inverse(a)) == 1
    assert [trace(x) for x in LPOW] == [0, 2, 2, 2, 2, 2, 2]
    answer = {}
    for family in ("good", "aligned"):
        ranks = [matrix_rank(pencil(nu, family)) for nu in PARAMS]
        assert ranks == [0] + [4] * 26
        common_rank = matrix_rank([row for nu in BASIS for row in pencil(nu, family)])
        assert common_rank == 6
        independent = matrix_rank([[x for row in pencil(nu, family) for x in row]
                                   for nu in BASIS])
        assert independent == 3
        answer[family] = {"rank_histogram": dict(Counter(ranks)),
                          "stacked_rank": common_rank,
                          "tuple_rank_over_E": independent}
    e0 = [1, 0, 0, 0, 0, 0]
    good_frequency = [0, 1, 2, 0, 0, 0]
    active_good = []
    for nu in PARAMS[1:]:
        b = pencil(nu, "aligned")
        assert matrix_rank([row + [e0[i]] for i, row in enumerate(b)]) == 4
        b = pencil(nu, "good")
        incidence = matrix_rank([row + [good_frequency[i]] for i, row in enumerate(b)]) == 4
        assert incidence == (nu[1] == nu[2])
        if incidence:
            active_good.append(nu)
    assert rational(csum(WEIGHT[nu] for nu in active_good)) == F(343, 729)
    return answer


def random_state(rng):
    return (tuple(rng.randrange(729) for _ in range(6)),
            tuple(rng.randrange(7) for _ in range(6)),
            tuple(rng.randrange(3) for _ in range(3)), rng.randrange(7))


def check_words(samples=64):
    rng = random.Random(20261116)
    z6, z3 = (0,)*6, (0,)*3
    w, vstar = (1,0,1,0,1,0), (0,1,0,1,0,1)
    e = (1,0,0,0,0,0)
    xe = (e,z6,z3,0)
    for family in ("good", "aligned"):
        op = lambda x,y: loop_mul(x,y,family)
        for _ in range(samples):
            x,y,z = (random_state(rng) for _ in range(3))
            assert op(x,op(y,op(x,z))) == op(op(x,op(y,x)),z)
            u, yy = x[0], y[0]
            a, s = z[2], z[3]
            U, Y = (u,z6,z3,0), (yy,z6,z3,0)
            Wa, Zs = (z6,d_action(a,w),z3,0), (z6,vstar,z3,s)
            b = beta(u,yy,family)
            actor = tuple((a[i]-b[i])%3 for i in range(3))
            A = op(op(U,Y),Wa)
            B = op(U,op(Y,Wa))
            assert A[0] == B[0] and A[2:] == B[2:]
            assert A[1] == d_action(actor,w) and B[1] == d_action(a,w)
            before, after = op(A,Zs), op(op(A,Zs),xe)
            tt = (s-sum(pow(2,x,7) for x in actor))%7
            assert before[3] == tt
            increment = tuple(sub(x,y) for x,y in zip(after[0],before[0]))
            assert increment == tuple(mul(LPOW[tt],x) for x in e)
            assert trace(increment[0]) == (0 if tt == 0 else 2)
            before_b, after_b = op(B,Zs), op(op(B,Zs),xe)
            tt_b = (s-sum(pow(2,x,7) for x in a))%7
            assert before_b[3] == tt_b
            assert sub(after_b[0][0],before_b[0][0]) == LPOW[tt_b]
    return {"families": 2, "Bol_triples_each": samples,
            "two_bracketings_and_roundtrip_words_each": samples,
            "seed": 20261116}


def check_roundtrip_weights():
    theta = [root(0 if t == 0 else -7) for t in range(7)]
    weights = []
    for rho in range(7):
        ft = cscale(csum(cmul(theta[t],root(-3*rho*t)) for t in range(7)),F(1,7))
        weight = rational(abs_square(ft))
        assert weight == F(31 if rho == 0 else 3,49)
        weights.append(str(weight))
    for rho in range(1,7):
        wrho = [abs_square(cscale(csum(root(3*rho*pow(2,a,7)-7*nu*a)
                                      for a in range(3)),F(1,3)))
                for nu in range(3)]
        expected = WONE if rho in (1,2,4) else [WONE[0],WONE[2],WONE[1]]
        assert wrho == expected
    return weights


def check_direct_restricted_gram():
    # Actual good loop: u=(lambda*u0,0) and y=(y0,0), u0,y0 in F_3^3.
    # Trace(lambda)=-1, so this is an exact 27-point input restriction.
    kernels = {}
    for d in PARAMS:
        counts = [0]*7
        dd = d+(0,0,0)
        for u0 in PARAMS:
            uu = tuple(mul(LAM,x) for x in u0)+(0,0,0)
            b = beta(uu,dd,"good")
            for a in PARAMS:
                phase = sum(pow(2,(a[i]-b[i])%3,7)-pow(2,a[i],7)
                            for i in range(3))%7
                counts[phase] += 1
        direct = cscale(csum(cscale(root(3*j),F(counts[j])) for j in range(7)),
                        F(1,27*27))
        expected = csum(WEIGHT[nu] for nu in PARAMS
                        if all(sum(c*x for c,x in zip(row,d))%3 == 0
                               for row in cross_matrix(nu)))
        assert direct == expected, d
        kernels[d] = direct
    for xi in PARAMS:
        direct = cscale(csum(cmul(kernels[d],root(7*dot(xi,d))) for d in PARAMS),F(1,27))
        expected = cscale(csum(WEIGHT[nu] for nu in PARAMS[1:] if dot(nu,xi)==0),F(1,9))
        if not any(xi):
            expected = cadd(expected,WEIGHT[(0,0,0)])
        assert direct == expected, xi
    return {"input_points": 27, "output_points": 729,
            "direct_readout_pairs_counted": 27*27*27,
            "Gram_differences_checked": 27, "Fourier_multipliers_checked": 27,
            "scope": "u in lambda*F3^3, y in F3^3, second E^3 block zero"}


def main():
    summary = {
        "arithmetic": "exact: F729 and rational cyclotomic Q(zeta21); no floating point",
        "field": "F3[lambda]/(1+X+X^2+X^3+X^4+X^5+X^6)",
        "aligned_scalar": "nu1+lambda*nu2+lambda^2*nu3",
        "field_and_ranks": check_field_and_ranks(),
        "hyperplane_table": check_weights(),
        "loop_checks": check_words(),
        "roundtrip_character_weights": check_roundtrip_weights(),
        "direct_restricted_Gram": check_direct_restricted_gram(),
        "one_block_squared_norm_factors_before_Q_power": {
            "good": "343/729", "aligned_and_separate_sector": "721/729",
            "roundtrip_multiplier_on_mean_zero": "18/49"},
        "limitations": "No full E^6 matrix enumeration; finite evidence does not prove arbitrary h.",
    }
    print(json.dumps(summary,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()

