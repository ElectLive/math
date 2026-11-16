#!/usr/bin/env python3
"""Authored exact checks for actual Bol-sector Weyl correction formulas.

This imports the existing authored field and conductor implementation. It is
not independent evidence. No huge representation matrix is enumerated: the
program checks exact monomial actions on sampled basis vectors, including
all-zero, primitive and imprimitive character cases at levels 7 and 49.
Pass the repository's code directory as the single optional argument.
"""
from pathlib import Path
import sys
import random
import json

code = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
sys.path.insert(0, str(code))
import verify_bol_conductor_vector as F

SEED = 2026111609


def split(x):
    return (x[0], x[1]), (x[2], x[3])


def join(u, c):
    return u[0], u[1], c[0], c[1]


def add(u, v, level):
    modulus = 7**level
    return (tuple(F.fa(a, b) for a, b in zip(u[0], v[0])),
            tuple((a+b) % modulus for a, b in zip(u[1], v[1])))


def neg(u, level):
    modulus = 7**level
    return tuple(F.fn(a) for a in u[0]), tuple(-a % modulus for a in u[1])


def sub(u, v, level):
    return add(u, neg(v, level), level)


def cadd(c, d, level):
    return tuple((a+b) % 3 for a, b in zip(c[0], d[0])), (c[1]+d[1]) % (7**level)


def cneg(c, level):
    return tuple(-a % 3 for a in c[0]), -c[1] % (7**level)


def b(u, v, family, level):
    return F.beta(u[0], v[0], family), F.gamma(u[1], v[1], 7**level)


PERM = (1, 2, 0)
PRIME_SPARSE = {
    family: [
        [(i, j, F.E.mul(coefficient, F.E.LPOW[(-i-j) % 7]))
         for i, j, coefficient in F.E.SPARSE[family][PERM[label]]]
        for label in range(3)]
    for family in ('good', 'aligned')}


def b_prime(u, v, family, level):
    output = []
    for entries in PRIME_SPARSE[family]:
        value = 0
        for i, j, coefficient in entries:
            value = F.E.add(value, F.E.mul(coefficient, F.pairing(u[0][i], v[0][j])))
        output.append(F.E.trace(value))
    return tuple(output), F.gamma(u[1], v[1], 7**level)


def actor(c, u, level):
    multiplier = F.TP[(7*c[1]) % 49] if level == 1 else F.TP[c[1]]
    return tuple(F.fm(multiplier, a) for a in u[0]), F.d_action(c[0], u[1], level)


def chi(c, character, level):
    nu, rho = character
    modulus = 7**level
    return (modulus * sum(a*b for a, b in zip(nu, c[0])) + 3*rho*c[1]) % (3*modulus)


def pi(x, state, character, family, level, b_function=b):
    u, phase = state
    a, c = split(x)
    out = add(a, actor(c, u, level), level)
    phase += chi(cadd(c, cneg(b_function(a, u, family, level), level), level), character, level)
    return out, phase % (3*7**level)


def correction_parameters(x, y, family, level):
    u, c = split(x); v, d = split(y)
    g = b(u, v, family, level)
    h = sub(actor(g, u, level), actor(d, u, level), level)
    h = add(h, sub(actor(cadd(c, g, level), v, level), v, level), level)
    return h, g


def correction(x, y, state, character, family, level):
    h, g = correction_parameters(x, y, family, level)
    w, phase = state
    return actor(g, w, level), (phase+chi(b(h, w, family, level), character, level)) % (3*7**level)


def left_division(x, target, family, level):
    u, c = split(x); w, e = split(target)
    v = actor(cneg(c, level), sub(w, u, level), level)
    d = cadd(cadd(e, cneg(c, level), level), b(u, v, family, level), level)
    return join(v, d)


def H(parameters, z, family, level):
    h, g = parameters; w, e = split(z)
    return join(actor(g, w, level), cadd(e, b(h, w, family, level), level))


def phi_u(u, level):
    modulus = 7**level
    new_w = tuple(F.scale(value, F.E.LPOW[i % 7]) for i, value in enumerate(u[0]))
    new_v = []
    for i, source in enumerate(PERM):
        factor = pow(2, i+1, modulus)
        new_v.extend((factor*u[1][2*source] % modulus,
                      pow(factor, -1, modulus)*u[1][2*source+1] % modulus))
    return new_w, tuple(new_v)


def phi(x, level):
    u, c = split(x)
    return join(phi_u(u, level), (tuple(c[0][i] for i in PERM), c[1]))


def op_prime(x, y, family, level):
    u, c = split(x); v, d = split(y)
    return join(add(u, actor(c, v, level), level),
                cadd(cadd(c, d, level), cneg(b_prime(u, v, family, level), level), level))


def gauge(u, level):
    # Deliberately nonlinear coset-section change; not asserted a loop isomorphism.
    r = 7**level
    return tuple((F.E.digits(u[0][i][0])[i] + u[1][2*i]**2) % 3 for i in range(3)),\
        (sum(x*x for x in u[1]) + F.E.digits(u[0][0][0])[0]) % r


def weyl_formula(x, state, character, family, level):
    a, c = split(x); u, phase = state
    u1 = actor(c, u, level)
    half = (tuple(F.scale(a_i, 2) for a_i in a[0]),
            tuple((pow(2, -1, 7**level)*a_i) % (7**level) for a_i in a[1]))
    p_argument = add(u1, half, level)
    covector = actor(cneg(c, level), a, level)
    phase += chi(c, character, level) - chi(b(covector, p_argument, family, level), character, level)
    return add(a, u1, level), phase % (3*7**level)


def main():
    rng = random.Random(SEED)
    record = {'seed': SEED, 'authored_shared_field_dependency': True, 'cases': []}
    for level in (1, 2):
        modulus = 7**level
        characters = [((0, 0, 0), 0), ((1, 0, 0), 0), ((0, 0, 0), 1),
                      ((1, 2, 1), 1)]
        if level == 2:
            characters += [((0, 0, 0), 7), ((2, 1, 2), 14)]
        for family in ('good', 'aligned'):
            count = 0
            for _ in range(24):
                x = F.random_state(rng, level)
                y = F.random_state(rng, level)
                z = F.random_state(rng, level)
                w = split(z)[0]
                xy = F.op(x, y, family, level)
                yx = F.op(y, x, family, level)
                xyx = F.op(x, yx, family, level)
                u, c = split(x)
                c_half = tuple(2*a % 3 for a in c[0]), pow(2, -1, modulus)*c[1] % modulus
                zero_u = (tuple(F.ZERO for _ in range(6)), (0,)*6)
                zero_c = ((0, 0, 0), 0)
                half_center = join(zero_u, c_half)
                middle = join(actor(cneg(c_half, level), u, level), zero_c)
                h1, g1 = correction_parameters(x, y, family, level)
                h2, g2 = correction_parameters(y, z, family, level)
                parameters_product = add(h2, actor(g2, h1, level), level), cadd(g1, g2, level)
                assert H((h1, g1), z, family, level) == left_division(
                    xy, F.op(x, F.op(y, z, family, level), family, level), family, level)
                assert H((h1, g1), H((h2, g2), z, family, level), family, level) == H(
                    parameters_product, z, family, level)
                assert phi(xy, level) == op_prime(phi(x, level), phi(y, level), family, level)
                for ch in characters:
                    state = w, 0
                    assert pi(x, state, ch, family, level) == weyl_formula(x, state, ch, family, level)
                    assert pi(x, pi(y, state, ch, family, level), ch, family, level) == pi(
                        xy, correction(x, y, state, ch, family, level), ch, family, level)
                    assert pi(x, pi(y, pi(x, state, ch, family, level), ch, family, level),
                              ch, family, level) == pi(xyx, state, ch, family, level)
                    assert pi(half_center, pi(middle, pi(half_center, state, ch, family, level),
                              ch, family, level), ch, family, level) == pi(x, state, ch, family, level)
                    assert correction(y, xy, correction(x, y, state, ch, family, level),
                                      ch, family, level) == state
                    transformed_ch = tuple(ch[0][i] for i in PERM), ch[1]
                    output, phase = pi(x, state, ch, family, level)
                    assert pi(phi(x, level), (phi_u(w, level), 0), transformed_ch,
                              family, level, b_prime) == (phi_u(output, level), phase)
                    # Direct push from the new representative (w,gauge(w)).
                    direct_output, direct_c = split(F.op(x, join(w, gauge(w, level)), family, level))
                    direct_phase = chi(cadd(direct_c, cneg(gauge(direct_output, level), level), level), ch, level)
                    gauged_phase = (phase + chi(gauge(w, level), ch, level)
                                    - chi(gauge(output, level), ch, level)) % (3*modulus)
                    assert (direct_output, direct_phase) == (output, gauged_phase)
                    count += 1
            record['cases'].append({'level': level, 'family': family, 'basis_character_cases': count,
                'checks': ['Weyl decomposition', 'full Jacobi correction', 'Bol sandwich',
                           'half-center palindrome', 'inverse defect',
                           'genuine pencil/basis isomorphism', 'nonlinear section gauge'],
                'permutation_cases': 24,
                'permutation_checks': ['direct left division defect', 'H group composition',
                                       'genuine loop isomorphism']})
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()

