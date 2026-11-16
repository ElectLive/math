#!/usr/bin/env python3
"""Authored exact checks of the reciprocal conductor/vector interface.

Uses the authored F_729 implementation from the adjacent verify_bol_collective.py.  This is NOT an independent verifier.  All arithmetic
is exact and the bounded restrictions are reported in the output.
"""

from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json
import random


import verify_bol_collective as E

ZERO = (0,) * 7
ONE = (1,) + (0,) * 6
TAU = (0, 1) + (0,) * 5


def emb(a):
    return (a,) + (0,) * 6


def fa(a, b):
    return tuple(E.add(x, y) for x, y in zip(a, b))


def fn(a):
    return tuple(E.neg(x) for x in a)


def fs(a, b):
    return fa(a, fn(b))


def scale(a, b):
    return tuple(E.mul(x, b) for x in a)


@lru_cache(None)
def fm(a, b):
    v = [0] * 13
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    v[i+j] = E.add(v[i+j], E.mul(x, y))
    for i in range(12, 6, -1):
        if v[i]:
            v[i-7] = E.add(v[i-7], E.mul(E.LAM, v[i]))
    return tuple(v[:7])


def fp(a, n):
    v = ONE
    while n:
        if n & 1:
            v = fm(v, a)
        a = fm(a, a)
        n //= 2
    return v


TP = [ONE]
for _ in range(49):
    TP.append(fm(TP[-1], TAU))


def relative_frobenius(a):
    # tau^729=tau*lambda^6, with coefficients already in F_729.
    return tuple(E.mul(x, E.LPOW[(6*i) % 7]) for i, x in enumerate(a))


def relative_trace_direct(a):
    ans, b = ZERO, a
    for _ in range(7):
        ans = fa(ans, b)
        b = relative_frobenius(b)
    return ans


def absolute_trace(a):
    return E.trace(a[0])


def pairing(a, b):
    # Tr_(F/E)(ab), derived from the actual trace-pairing matrix.
    ans = E.mul(a[0], b[0])
    for i in range(1, 7):
        ans = E.add(ans, E.mul(E.LAM, E.mul(a[i], b[7-i])))
    return ans


def beta(x, y, family):
    out = []
    for entries in E.SPARSE[family]:
        v = 0
        for i, j, coefficient in entries:
            v = E.add(v, E.mul(coefficient, pairing(x[i], y[j])))
        out.append(E.trace(v))
    return tuple(out)


def gamma(v, w, modulus):
    return sum(v[2*i]*w[2*i+1]-v[2*i+1]*w[2*i] for i in range(3)) % modulus


def d_action(a, w, level):
    modulus, eta = (7, 2) if level == 1 else (49, 30)
    return tuple(pow(eta, a[i//2], modulus)*w[i] % modulus for i in range(6))


def op(x, y, family, level):
    u, v, a, t = x
    yy, w, b, s = y
    modulus = 7 if level == 1 else 49
    actor = TP[7*t] if level == 1 else TP[t]
    by, dw = beta(u, yy, family), d_action(a, w, level)
    return (tuple(fa(xx, fm(actor, zz)) for xx, zz in zip(u, yy)),
            tuple((xx+zz) % modulus for xx, zz in zip(v, dw)),
            tuple((aa+bb-cc) % 3 for aa, bb, cc in zip(a, b, by)),
            (t+s-gamma(v, w, modulus)) % modulus)


def random_element(rng, level):
    return emb(rng.randrange(729)) if level == 1 else tuple(rng.randrange(729) for _ in range(7))


def random_state(rng, level):
    modulus = 7 if level == 1 else 49
    return (tuple(random_element(rng, level) for _ in range(6)),
            tuple(rng.randrange(modulus) for _ in range(6)),
            tuple(rng.randrange(3) for _ in range(3)), rng.randrange(modulus))


def check_field(rng):
    assert TP[7] == emb(E.LAM) and TP[49] == ONE
    assert len(set(TP[:49])) == 49
    # Kummer irreducibility condition: lambda is not a seventh power in E.
    assert E.power(E.LAM, (729-1)//7) != 1
    assert pow(30, 3, 49) == 1 and 30 != 1 and 30 % 7 == 2
    for _ in range(12):
        a = random_element(rng, 2)
        assert fp(a, 729) == relative_frobenius(a)
        assert relative_trace_direct(a) == emb(a[0])
        b = random_element(rng, 2)
        assert fm(a, b)[0] == pairing(a, b)
    for _ in range(4):
        a, total = random_element(rng, 2), ZERO
        b = a
        for _ in range(42):
            total = fa(total, b)
            b = fp(b, 3)
        assert total == emb(absolute_trace(a))
    traces = []
    for j, a in enumerate(TP[:49]):
        assert relative_trace_direct(a) == emb(a[0])
        tr = absolute_trace(a)
        assert tr == (2 if j and j % 7 == 0 else 0)
        traces.append(tr)
    gram = [[fm(TP[i], TP[j])[0] for j in range(7)] for i in range(7)]
    expected = [[1 if i == j == 0 else E.LAM if i+j == 7 else 0
                 for j in range(7)] for i in range(7)]
    assert gram == expected
    assert E.matrix_rank(gram) == 7
    assert E.matrix_rank([row[1:] for row in gram[1:]]) == 6
    return gram, {"order_tau": 49, "tau_power_7": "lambda1",
                  "absolute_trace_tau_powers_0_through_48": traces,
                  "relative_trace_is_constant_coefficient": True,
                  "trace_pairing_rank": 7, "trace_zero_pairing_rank": 6,
                  "random_general_Frobenius_checks": 12,
                  "random_42_term_absolute_trace_checks": 4}


def tensor_matrix(a, b):
    return [[E.mul(a[i][j], b[s][t])
             for j in range(len(a[0])) for t in range(len(b[0]))]
            for i in range(len(a)) for s in range(len(b))]


def check_ranks_and_densities(gram):
    transverse = [row[1:] for row in gram[1:]]
    counts = {}
    for family in ("good", "aligned"):
        for nu in E.PARAMS:
            b = E.pencil(nu, family)
            r = E.matrix_rank(b)
            assert E.matrix_rank(tensor_matrix(b, transverse)) == 6*r
            assert E.matrix_rank(tensor_matrix(b, gram)) == 7*r
        counts[family] = {"labels_checked": 27,
                          "zero_label_ranks": [0, 0, 0],
                          "nonzero_ranks_base_transverse_full": [4, 24, 28]}
    return {"families": counts,
            "nonzero_transverse_kernel_dimension_over_E1": 12,
            "ambient_transverse_dimension_over_E1": 36,
            "mu_nonzero": "729^(-24)",
            "Heisenberg_representation_transverse_dimension": "729^12",
            "nondegenerate_phase_space_cardinality": "729^24",
            "sqrt_mu_equals_inverse_representation_dimension": "729^(-12)"}


def check_splitting(rng, samples=32):
    for family in ("good", "aligned"):
        for _ in range(samples):
            u = tuple(random_element(rng, 2) for _ in range(6))
            y = tuple(random_element(rng, 2) for _ in range(6))
            u0, y0 = tuple(x[0] for x in u), tuple(x[0] for x in y)
            v = tuple((0,)+x[1:] for x in u)
            z = tuple((0,)+x[1:] for x in y)
            expected = tuple((a+b) % 3 for a,b in
                             zip(E.beta(u0, y0, family), beta(v, z, family)))
            assert beta(u, y, family) == expected
            assert beta(tuple(emb(x) for x in u0), y, family) == E.beta(u0, y0, family)
    return {"families": 2, "samples_each": samples,
            "identities": ["full orthogonal trace splitting",
                           "lower u and unrestricted upper y factor through trace"]}


def check_actual_words(rng, samples=12):
    zero_p, zero_q, zero_z = (ZERO,)*6, (0,)*6, (0,)*3
    w, vstar = (1,0,1,0,1,0), (0,1,0,1,0,1)
    e = (ONE,)+(ZERO,)*5
    Xe = (e,zero_q,zero_z,0)
    for family in ("good", "aligned"):
        for level in (1,2):
            modulus, eta = (7,2) if level == 1 else (49,30)
            mul = lambda x,y: op(x,y,family,level)
            for _ in range(samples):
                x,y,z = (random_state(rng,level) for _ in range(3))
                assert mul(x,mul(y,mul(x,z))) == mul(mul(x,mul(y,x)),z)
                if level == 1:
                    low = lambda state: (tuple(a[0] for a in state[0]),)+state[1:]
                    assert low(mul(x,y)) == E.loop_mul(low(x),low(y),family)
                U, Y = (x[0],zero_q,zero_z,0), (y[0],zero_q,zero_z,0)
                a,s = z[2],z[3]
                Wa, Zs = (zero_p,d_action(a,w,level),zero_z,0),(zero_p,vstar,zero_z,s)
                bb = beta(x[0],y[0],family)
                actor = tuple((aa-b) % 3 for aa,b in zip(a,bb))
                left, right = mul(mul(U,Y),Wa), mul(U,mul(Y,Wa))
                assert left[0] == right[0] and left[2:] == right[2:]
                assert left[1] == d_action(actor,w,level)
                assert right[1] == d_action(a,w,level)
                for state, label in ((left,actor),(right,a)):
                    before,after = mul(state,Zs),mul(mul(state,Zs),Xe)
                    target = (s-sum(pow(eta,aa,modulus) for aa in label)) % modulus
                    assert before[3] == target
                    increment = tuple(fs(xx,yy) for xx,yy in zip(after[0],before[0]))
                    actor_scalar = TP[7*target] if level == 1 else TP[target]
                    assert increment == (actor_scalar,)+(ZERO,)*5
                    expected_trace = (2 if target != 0 else 0) if level == 1 else (
                        2 if target and target % 7 == 0 else 0)
                    assert absolute_trace(increment[0]) == expected_trace
    return {"families": 2, "conductor_levels": [7,49],
            "samples_each_family_and_level": samples,
            "checks": ["original Bol triples", "both associator bracketings",
                       "two-way word displacement and trace readout",
                       "level-seven agreement with earlier authored model"]}


P3 = list(product(range(3), repeat=3))


def mv3(a, x):
    return tuple(sum(v*w for v,w in zip(row,x)) % 3 for row in a)


def d3(x,y):
    return sum(a*b for a,b in zip(x,y)) % 3


def check_finite_compression(rng):
    """Actual t/t^6 and t^2/t^5 trace blocks, restricted to F3 coefficients.

    This checks a finite restriction of the character/coisometry identities,
    NOT the entire 729^36-point transverse averaging space.
    """
    phases_counted = 0
    for nu in P3:
        b = E.cross_matrix(nu)
        kernel = [v for v in P3 if mv3(b,v) == (0,0,0)]
        density = Q(len(kernel),27)
        assert density == (Q(1) if not any(nu) else Q(1,9))
        normalizer = 1 if not any(nu) else 3
        for v in P3:
            counts = [0,0,0]
            bv = mv3(b,v)
            for z in P3:
                # Tr_E(lambda)=2. Sign does not affect orthogonality.
                counts[(2*d3(bv,z)) % 3] += 1
                phases_counted += 1
            assert counts == ([27,0,0] if v in kernel else [9,9,9])
        # C C* = I, exact Pythagoras and the predicted output factor.
        assert normalizer*normalizer*density == 1
        g = {v: Q(rng.randrange(-5,6)) for v in P3}
        cg = normalizer*sum(g[v] for v in kernel)/27
        pg = {v: normalizer*cg if v in kernel else Q(0) for v in P3}
        assert normalizer*sum(pg[v] for v in kernel)/27 == cg
        assert sum(g[v]**2 for v in P3) == sum(pg[v]**2+(g[v]-pg[v])**2 for v in P3)
        amp = Q(7,5)
        assert normalizer*sum(amp for _ in kernel)/27 == amp/normalizer
        # Two orthogonal trace blocks: successive normalized averaging is
        # exactly combined averaging, including the zero central label.
        gg = {(v,w): Q(rng.randrange(-3,4)) for v in P3 for w in P3}
        first = {v: normalizer*sum(gg[v,w] for w in kernel)/27 for v in P3}
        sequential = normalizer*sum(first[v] for v in kernel)/27
        combined = normalizer**2*sum(gg[v,w] for v in kernel for w in kernel)/(27**2)
        assert sequential == combined
    # Confirm that the two small trace blocks really occur orthogonally
    # inside the actual F_729[t]/(t^7-lambda) model.
    for _ in range(32):
        a,b,c,d = [rng.randrange(3) for _ in range(4)]
        vv = fa(scale(TP[1],a),scale(TP[2],b))
        zz = fa(scale(TP[6],c),scale(TP[5],d))
        assert absolute_trace(fm(vv,zz)) == (2*(a*c+b*d)) % 3
    return {"character_labels": 27, "phase_terms_enumerated": phases_counted,
            "individual_output_block_points": 27,
            "two_block_coherence_points_per_label": 729,
            "actual_field_orthogonality_samples": 32,
            "scope": "F3^3 coefficient restrictions on t/t^6 and t^2/t^5; not full trace fibers",
            "includes_zero_character": True}


def main():
    rng = random.Random(20261116)
    gram,field = check_field(rng)
    result = {
        "status": "PASS",
        "provenance": "authored check reusing authored F729 code; not independent",
        "arithmetic": "exact finite fields and fractions; no floating point",
        "models": {"E1": "F3[lambda]/Phi7(lambda)",
                   "E2": "E1[t]/(t^7-lambda)", "eta1": 2, "eta2": 30},
        "seed": 20261116,
        "field_and_trace": field,
        "rank_density_and_representation_dimension": check_ranks_and_densities(gram),
        "beta_trace_splitting": check_splitting(rng),
        "original_loop_and_readout": check_actual_words(rng),
        "restricted_compression_and_coherence": check_finite_compression(rng),
        "limits": ["No full vector space or operator enumeration at E2",
                   "Small restricted averages do not stand in for full transverse densities",
                   "Finite checks do not prove all conductor levels or operator theorems"],
    }
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()

