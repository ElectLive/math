#!/usr/bin/env python3
"""Contributor checks of fusion and joint shear ranks; not independent review.

Imports the accepted PR440 field/loop implementations, with exact arithmetic.
Checks sampled actual reciprocal operators at conductors 7 and 49, exhaustive
ring decoupling conditions at both levels, and all h=1/sampled h=2 coupled
pair ranks. No full enormous operator is enumerated.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import random
import sys

CODE = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE))
from verify_bol_associator_independent import Loop
import verify_bol_coupled as cp

SEED = 2026111602


def phase(loop, char, z):
    return (char[0]*z[0] % 3, char[1]*z[1] % loop.modulus)


def addphase(loop, a, b):
    return ((a[0]+b[0]) % 3, (a[1]+b[1]) % loop.modulus)


def subphase(loop, a, b):
    return ((a[0]-b[0]) % 3, (a[1]-b[1]) % loop.modulus)


def check_fusion(level, samples, rng):
    loop = Loop(level)
    m = loop.modulus
    count = 0
    for _ in range(samples):
        x, y, z, zz = [loop.random(rng) for _ in range(4)]
        a, c = x
        u, v = z[0], zz[0]
        kw, kv = rng.randrange(3), rng.randrange(m)

        def K(t):
            f = loop.field
            return (f.scale(t[0], kw), f.scale(t[1], kw), kv*t[2] % m, kv*t[3] % m)

        t = loop.sub_u(v, u)
        r = loop.add_u(u, K(t))
        assert loop.sub_u(r, K(t)) == u
        assert loop.add_u(r, loop.sub_u(t, K(t))) == v
        assert K(loop.action(c, t)) == loop.action(c, K(t))

        up = loop.add_u(a, loop.action(c, u))
        vp = loop.add_u(a, loop.action(c, v))
        assert loop.sub_u(vp, up) == loop.action(c, t)
        assert loop.add_u(up, K(loop.sub_u(vp, up))) == loop.add_u(a, loop.action(c, r))

        ux, cx = x
        uy, cy = y
        g = loop.bimap(ux, uy)
        h = loop.sub_u(loop.action(g, loop.add_u(ux, loop.action(cx, uy))),
                      loop.add_u(loop.action(cy, ux), uy))
        assert loop.defect_actual(x, y, (u, loop.zero_c)) == loop.hg(h, g, (u, loop.zero_c))
        assert K(loop.action(g, t)) == loop.action(g, K(t))

        ringchars = sorted({0, 1, m-1, 7 % m, (-7) % m})
        for nu, mu, rho, tau in product(range(3), range(3), ringchars, ringchars):
            chi, psi = (nu, rho), (mu, tau)
            sig = ((nu+mu) % 3, (rho+tau) % m)
            original = addphase(loop, phase(loop, chi, loop.sub_c(c, loop.bimap(a, u))),
                               phase(loop, psi, loop.sub_c(c, loop.bimap(a, v))))
            residual = subphase(loop, phase(loop, psi, loop.bimap(a, t)),
                               phase(loop, sig, loop.bimap(a, K(t))))
            fused = subphase(loop, phase(loop, sig, loop.sub_c(c, loop.bimap(a, r))), residual)
            assert original == fused
            original_j = addphase(loop, phase(loop, chi, loop.bimap(h, u)),
                                 phase(loop, psi, loop.bimap(h, v)))
            residual_j = subphase(loop, phase(loop, psi, loop.bimap(h, t)),
                                 phase(loop, sig, loop.bimap(h, K(t))))
            fused_j = addphase(loop, phase(loop, sig, loop.bimap(h, r)), residual_j)
            assert original_j == fused_j
            if (sig[0]*kw-mu) % 3 == 0 and (sig[1]*kv-tau) % m == 0:
                assert residual == residual_j == (0, 0)
            count += 1
    return {'level': level, 'sampled_vector_states': samples, 'phase_and_full_defect_cases': count}


def check_ring(level):
    m = 7**level
    counts = Counter()
    for rho, tau in product(range(m), repeat=2):
        sigma = (rho+tau) % m
        radical_chi = {h for h in range(m) if rho*h % m == 0}
        radical_psi = {h for h in range(m) if tau*h % m == 0}
        radical_sum = {h for h in range(m) if sigma*h % m == 0}
        solutions = [k for k in range(m) if sigma*k % m == tau]
        assert bool(solutions) == (radical_sum == radical_chi & radical_psi)
        image_joint = {(rho*u+tau*v) % m for u, v in product(range(m), repeat=2)}
        image_sum = {sigma*u % m for u in range(m)}
        assert len(image_joint) >= len(image_sum)
        counts['decoupled' if solutions else 'residual_required'] += 1
    return {'level': level, 'character_pairs': m*m, **counts}


def check_triples_gauges_isomorphisms(level, samples, rng):
    loop = Loop(level)
    m = loop.modulus
    modulus = 3*m
    checked_triples = checked_gauges = 0

    def scalar(t, k):
        f = loop.field
        return (f.scale(t[0], k), f.scale(t[1], k), k*t[2] % m, k*t[3] % m)

    def fuse(u, v, k):
        t = loop.sub_u(v, u)
        return loop.add_u(u, scalar(t, k)), t

    def unfuse(r, t, k):
        return loop.sub_u(r, scalar(t, k)), loop.add_u(r, scalar(t, 1-k))

    def char(charge):
        return charge % 3, charge % m

    def residual(a, t, first, second, k):
        return subphase(loop, phase(loop, char(second), loop.bimap(a, t)),
                        phase(loop, char(first+second), loop.bimap(a, scalar(t, k))))

    def gauge(u):
        f = loop.field
        return f.trace(f.mul(u[0], u[0])), u[2]**2 % m

    def symplectic(u):
        f = loop.field
        return f.root_mul(u[0], 1), f.root_mul(u[1], -1), 3*u[2] % m, pow(3, -1, m)*u[3] % m

    def phi(x):
        return symplectic(x[0]), x[1]

    for _ in range(samples):
        x, y, uu, vv, ww = [loop.random(rng) for _ in range(5)]
        a, c = x
        u, v, w = uu[0], vv[0], ww[0]
        # A regular triple with all ring charges nonzero; the first p-charge is zero.
        aa = 3*pow(3, -1, m)
        cases = [
            (aa, 1, 1, pow(aa+1, -1, modulus), pow(aa+2, -1, modulus),
             pow(2, -1, modulus), 2*pow(aa+2, -1, modulus), 'regular'),
            (1, modulus-1, 1, 0, 1, 0, 0, 'intermediate_total_zero'),
            (1, 1, 1, 2, 0, 2, 0, 'zero_p_total_with_residual'),
            (1, 6, 1, 0, pow(8, -1, modulus), 0, 7*pow(8, -1, modulus), 'imprimitive_or_zero_ring_pair'),
        ]
        for alpha, beta, gamma, k12, klast, k23, kfirst, label in cases:
            r12, s = fuse(u, v, k12)
            r, t = fuse(r12, w, klast)
            r23, ss = fuse(v, w, k23)
            rr, tt = fuse(u, r23, kfirst)
            # The recoupling is the exact inverse-coordinate composition, with
            # no division through the zero or imprimitive channels.
            restored12, restoredw = unfuse(r, t, klast)
            restoredu, restoredv = unfuse(restored12, s, k12)
            assert (restoredu, restoredv, restoredw) == (u, v, w)
            rer23, ress = fuse(restoredv, restoredw, k23)
            rerr, rett = fuse(restoredu, rer23, kfirst)
            assert (rerr, ress, rett) == (rr, ss, tt)

            direct = (0, 0)
            for charge, state in [(alpha, u), (beta, v), (gamma, w)]:
                direct = addphase(loop, direct, phase(loop, char(charge), loop.sub_c(c, loop.bimap(a, state))))
            left = phase(loop, char(alpha+beta+gamma), loop.sub_c(c, loop.bimap(a, r)))
            left = subphase(loop, left, residual(a, s, alpha, beta, k12))
            left = subphase(loop, left, residual(a, t, alpha+beta, gamma, klast))
            right = phase(loop, char(alpha+beta+gamma), loop.sub_c(c, loop.bimap(a, rr)))
            right = subphase(loop, right, residual(a, ss, beta, gamma, k23))
            right = subphase(loop, right, residual(a, tt, alpha, beta+gamma, kfirst))
            assert direct == left == right
            # The full shear phase is the same trilinear identity with positive sign.
            direct_j = (0, 0)
            for charge, state in [(alpha, u), (beta, v), (gamma, w)]:
                direct_j = addphase(loop, direct_j, phase(loop, char(charge), loop.bimap(a, state)))
            left_j = phase(loop, char(alpha+beta+gamma), loop.bimap(a, r))
            left_j = addphase(loop, left_j, residual(a, s, alpha, beta, k12))
            left_j = addphase(loop, left_j, residual(a, t, alpha+beta, gamma, klast))
            right_j = phase(loop, char(alpha+beta+gamma), loop.bimap(a, rr))
            right_j = addphase(loop, right_j, residual(a, ss, beta, gamma, k23))
            right_j = addphase(loop, right_j, residual(a, tt, alpha, beta+gamma, kfirst))
            assert direct_j == left_j == right_j
            if label == 'regular':
                assert r == rr
                s_expected = loop.sub_u(t, scalar(s, alpha*pow(alpha+beta, -1, modulus)))
                t_expected = loop.add_u(scalar(s, beta*(alpha+beta+gamma)*pow((alpha+beta)*(beta+gamma), -1, modulus)),
                                        scalar(t, gamma*pow(beta+gamma, -1, modulus)))
                assert ss == s_expected and tt == t_expected
            checked_triples += 1

        k1, k2 = rng.randrange(modulus), rng.randrange(modulus)
        r1, t = fuse(u, v, k1)
        r2, _ = fuse(u, v, k2)
        assert r2 == loop.add_u(r1, scalar(t, k2-k1))
        alpha, beta = rng.randrange(modulus), rng.randrange(modulus)
        c1, c2 = residual(a, t, alpha, beta, k1), residual(a, t, alpha, beta, k2)
        assert c2 == subphase(loop, c1, phase(loop, char(alpha+beta), loop.bimap(a, scalar(t, k2-k1))))
        gauge_original = addphase(loop, phase(loop, char(alpha), gauge(u)), phase(loop, char(beta), gauge(v)))
        restored = unfuse(r1, t, k1)
        gauge_fused = addphase(loop, phase(loop, char(alpha), gauge(restored[0])), phase(loop, char(beta), gauge(restored[1])))
        assert gauge_original == gauge_fused
        checked_gauges += 1

        # An actual symplectic loop isomorphism, checked in the multiplication.
        assert phi(loop.mul(x, y)) == loop.mul(phi(x), phi(y))
        assert symplectic(loop.add_u(u, v)) == loop.add_u(symplectic(u), symplectic(v))
        assert symplectic(loop.action(c, u)) == loop.action(c, symplectic(u))
        assert loop.bimap(symplectic(u), symplectic(v)) == loop.bimap(u, v)
        assert fuse(symplectic(u), symplectic(v), k1) == (symplectic(r1), symplectic(t))

        # The affine commutator in the induced coset action is a translation.
        cstar = (1, 1)
        commutator = loop.action(cstar, loop.add_u(a, loop.action(loop.neg_c(cstar), loop.sub_u(u, a))))
        expected = loop.add_u(u, loop.sub_u(loop.action(cstar, a), a))
        assert commutator == expected
    # Faithfulness of all actor labels on two distinguishing axes certifies
    # uniqueness of the pure-translation representative in this finite chart.
    f = loop.field
    probe = (f.one, f.zero, 1, 0)
    actors_fixing_probe = [(ap, tq) for ap, tq in product(range(3), range(m))
                          if loop.action((ap, tq), probe) == probe]
    assert actors_fixing_probe == [(0, 0)]
    return {'level': level, 'state_samples': samples, 'triple_recoupling_cases': checked_triples,
            'K_and_nonlinear_section_gauge_cases': checked_gauges,
            'actual_symplectic_isomorphism_cases': samples, 'actor_labels_checked': 3*m}


def check_pairs(h, L, M, exhaustive, rng):
    k = 2*h+1
    params = list(product(range(3), repeat=k))
    basis_l, basis_m = cp.parameter_basis(L, k), cp.parameter_basis(M, k)
    good, aligned = [], []
    for nu in params:
        t = cp.linear_combination(L, nu, basis_l)
        m = cp.linear_combination(M, nu, basis_m)
        good.append(cp.good_matrix(L, t))
        aligned.append(cp.aligned_matrix(M, nu, m))
    pairs = list(product(range(len(params)), repeat=2)) if exhaustive else [(rng.randrange(len(params)), rng.randrange(len(params))) for _ in range(384)]
    histogram = Counter()
    for i, j in pairs:
        nu, mu = params[i], params[j]
        pr = cp.prank(cp.np.array([nu, mu], dtype=cp.np.uint16))
        rg = cp.erank(cp.np.column_stack((good[i], good[j])))
        ra = cp.erank(cp.np.column_stack((aligned[i], aligned[j])))
        if pr == 0:
            assert rg == ra == 0
        elif pr == 1:
            assert rg == ra == 4*h
        else:
            assert rg == 6*h and ra == 4*h+1
        histogram[(pr, rg, ra)] += 1
    return {'h': h, 'pair_cases': len(pairs), 'exhaustive': exhaustive,
            'histogram_parameter_rank_spread_rank_aligned_rank': {str(k): v for k, v in sorted(histogram.items())}}


def main():
    rng = random.Random(SEED)
    E = cp.Extension(1)
    quadratic = cp.Extension(2, [14, 0])
    assert cp.epow(14, 364) == 2
    cubic = cp.Extension(3, [3, 1, 0])
    result = {'seed': SEED,
              'fusion': [check_fusion(1, 24, rng), check_fusion(2, 8, rng)],
              'ring': [check_ring(1), check_ring(2)],
              'triple_gauge_isomorphism': [check_triples_gauges_isomorphisms(1, 16, rng), check_triples_gauges_isomorphisms(2, 8, rng)],
              'pair_ranks': [check_pairs(1, E, E, True, rng), check_pairs(2, quadratic, cubic, False, rng)],
              'limitations': 'Authored finite checks; imports accepted implementations. No independent proof review or exhaustive huge loop enumeration.'}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

