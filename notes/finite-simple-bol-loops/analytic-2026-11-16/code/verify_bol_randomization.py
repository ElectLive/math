#!/usr/bin/env python3
"""Exact finite checks for Bol quantum randomization and its obstructions.

Python standard library only.  This is a new implementation, importing none of
the preceding Bol checkers.  It checks the actual reciprocal loop at p=3,q=7,
A=1,k=1,E=F3[X]/(X^6+X+2), W=E^2.  Its Hilbert dimension is 26,040,609;
the full channel is NOT materialized or enumerated.  Direct ket/phase tests are
seeded samples.  The two-draw label bijections are exhaustively enumerated on
each scalar factor, and a full 49-dimensional ring-factor channel is checked
through its 2,401-element Weyl basis and all 400 Lagrangian stabilizer supports.
These are finite corroboration, not proofs
of the uniform statements or an independent review of this program's authors.
"""

from fractions import Fraction
from itertools import combinations, product
import json
import random

SEED = 2026111644
P, Q, M = 3, 729, 7
MODULUS = (2, 1, 0, 0, 0, 0, 1)
DIGITS = [tuple((a // 3**i) % 3 for i in range(6)) for a in range(Q)]


def encode(coefficients):
    return sum((x % 3) * 3**i for i, x in enumerate(coefficients))


def add(a, b):
    return encode(x + y for x, y in zip(DIGITS[a], DIGITS[b]))


def neg(a):
    return encode(-x for x in DIGITS[a])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    coefficients = [0] * 11
    for i, x in enumerate(DIGITS[a]):
        for j, y in enumerate(DIGITS[b]):
            coefficients[i + j] += x * y
    # X^6 = -X-2, reducing in descending degree.
    for j in range(10, 5, -1):
        coefficients[j - 6] -= 2 * coefficients[j]
        coefficients[j - 5] -= coefficients[j]
    return encode(coefficients[:6])


def power(a, exponent):
    result = 1
    while exponent:
        if exponent & 1:
            result = mul(result, a)
        a = mul(a, a)
        exponent >>= 1
    return result


def trace_direct(a):
    result = 0
    for _ in range(6):
        result = add(result, a)
        a = power(a, 3)
    assert result < 3
    return result


TRACE_BASIS = [trace_direct(3**i) for i in range(6)]


def trace(a):
    return sum(x * y for x, y in zip(DIGITS[a], TRACE_BASIS)) % 3


LAMBDA = power(3, 104)
LP = [power(LAMBDA, i) for i in range(7)]
EP = [1, 2, 4]
ZERO_U = (0, 0, 0, 0)
ZERO_Z = (0, 0)
G = (1, 1)


def uadd(a, b):
    return add(a[0], b[0]), add(a[1], b[1]), (a[2] + b[2]) % 7, (a[3] + b[3]) % 7


def uneg(a):
    return neg(a[0]), neg(a[1]), -a[2] % 7, -a[3] % 7


def usub(a, b):
    return uadd(a, uneg(b))


def zadd(a, b):
    return (a[0] + b[0]) % 3, (a[1] + b[1]) % 7


def zneg(a):
    return -a[0] % 3, -a[1] % 7


def form(a, b):
    return trace(sub(mul(a[0], b[1]), mul(a[1], b[0]))), (a[2] * b[3] - a[3] * b[2]) % 7


def actor(c, u):
    return mul(LP[c[1]], u[0]), mul(LP[c[1]], u[1]), EP[c[0]] * u[2] % 7, EP[c[0]] * u[3] % 7


def phase(chi, central):
    # Exact exponent of exp(2*pi*i/21).
    return (7 * chi[0] * central[0] + 3 * chi[1] * central[1]) % 21


def loop(x, y):
    a, c = x
    b, e = y
    return uadd(a, actor(c, b)), zadd(zadd(c, e), zneg(form(a, b)))


def pi(x, ket, chi):
    a, c = x
    u, exponent = ket
    return uadd(a, actor(c, u)), (exponent + phase(chi, zadd(c, zneg(form(a, u))))) % 21


def pi_inverse(x, ket, chi):
    a, c = x
    out, exponent = ket
    u = actor(zneg(c), usub(out, a))
    return u, (exponent - phase(chi, zadd(c, zneg(form(a, u))))) % 21


def defect(x, y):
    a, c = x
    b, e = y
    g = form(a, b)
    h = usub(uadd(usub(actor(g, a), actor(e, a)), actor(zadd(c, g), b)), b)
    return h, g


def translated_direct(x, y, z, ket, chi):
    # pi(z)^-1 pi(x*y)^-1 pi(x) pi(y) pi(z), with no defect formula.
    state = pi(z, ket, chi)
    state = pi(y, state, chi)
    state = pi(x, state, chi)
    state = pi_inverse(loop(x, y), state, chi)
    return pi_inverse(z, state, chi)


def translated_formula(h, g, z, ket, chi):
    a, c = z
    u, exponent = ket
    translation = actor(zneg(c), usub(actor(g, a), a))
    modulation = uadd(actor(c, h), usub(actor(g, a), a))
    constant = zadd(form(h, a), form(a, translation))
    return (uadd(actor(g, u), translation),
            (exponent + phase(chi, zadd(constant, form(modulation, u)))) % 21)


def random_u(rng):
    return rng.randrange(Q), rng.randrange(Q), rng.randrange(7), rng.randrange(7)


def random_loop(rng):
    return random_u(rng), (rng.randrange(3), rng.randrange(7))


def polynomial_remainder(a, b):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    while len(a) >= len(b):
        coefficient = a[-1] * pow(b[-1], -1, 3) % 3
        offset = len(a) - len(b)
        for i, value in enumerate(b):
            a[offset + i] = (a[offset + i] - coefficient * value) % 3
        while a and a[-1] == 0:
            a.pop()
    return a


def arithmetic_checks():
    divisors = 0
    for degree in (1, 2, 3):
        for coefficients in product(range(3), repeat=degree):
            assert polynomial_remainder(MODULUS, (*coefficients, 1))
            divisors += 1
    assert len(set(LP)) == 7 and power(LAMBDA, 7) == 1
    assert power(LAMBDA, 6) == power(LAMBDA, 27)
    assert len(set(EP)) == 3 and pow(2, 3, 7) == 1
    assert TRACE_BASIS == [0, 0, 0, 0, 0, 1]
    for a in range(1, Q):
        assert power(a, Q - 1) == 1
    return {"irreducibility_trial_divisors": divisors, "nonzero_field_elements": Q - 1,
            "lambda_encoding": LAMBDA, "trace_basis": TRACE_BASIS}


def actual_native_checks():
    rng = random.Random(SEED)
    characters = [(1, 1), (2, 3), (0, 1), (1, 0), (0, 0)]
    count = 0
    for _ in range(160):
        x, y, z = (random_loop(rng) for _ in range(3))
        ket = random_u(rng), rng.randrange(21)
        h, g = defect(x, y)
        for chi in characters:
            assert translated_direct(x, y, z, ket, chi) == translated_formula(h, g, z, ket, chi)
            count += 1
    # An explicit actual defect is the pure actor J(0,(1,1)).
    a, b = (1, 0, 1, 0), (0, 243, 0, 1)
    x, y = (a, zneg(G)), (b, G)
    assert form(a, b) == G and defect(x, y) == (ZERO_U, G)
    inverse_difference = power(sub(LAMBDA, 1), Q - 2)
    for _ in range(160):
        t, u = random_u(rng), random_u(rng)
        # R-I acts by lambda-1 on W and by 1 on the ring planes.
        center = (mul(inverse_difference, t[0]), mul(inverse_difference, t[1]), t[2], t[3])
        assert usub(actor(G, center), center) == t
        actual = translated_direct(x, y, (center, ZERO_Z), (u, 0), (1, 1))
        desired = uadd(actor(G, u), t), phase((1, 1), form(t, u))
        assert actual == desired
    # Pure shears are actual defects too, using y=(0,G).
    for _ in range(100):
        a = random_u(rng)
        assert defect((a, ZERO_Z), (ZERO_U, G)) == (usub(a, actor(G, a)), ZERO_Z)
    return {"direct_translated_defect_checks": count, "native_actor_conjugates": 160,
            "native_shears": 100, "hilbert_dimension": Q**2 * M**2}


def prescribed_defect_witness(h):
    """Actual (x,y) with ell_(x,y)=H_(h,(1,1)), in this exact field model."""
    inv_difference = power(sub(LAMBDA, 1), Q - 2)
    if h[:2] == (0, 0):
        aw, bw, eq = (1, 0), (0, 243), 1
    else:
        aw = mul(inv_difference, h[0]), mul(inv_difference, h[1])
        if aw[0]:
            bw = 0, mul(power(aw[0], Q - 2), 243)
        else:
            bw = neg(mul(power(aw[1], Q - 2), 243)), 0
        eq = 0
    if h[2:] == (0, 0):
        av, bv, ep = (1, 0), (0, 1), 1
    else:
        av = h[2], h[3]  # eta-1 = 1
        if av[0]:
            bv = 0, pow(av[0], -1, 7)
        else:
            bv = -pow(av[1], -1, 7) % 7, 0
        ep = 0
    return ((*aw, *av), zneg(G)), ((*bw, *bv), (ep, eq))


def weyl_actor_witness(t, k):
    """Actual translated defect equal, up to scalar, to X_t Z_k D_R."""
    h = usub(actor(G, k), t)
    x, y = prescribed_defect_witness(h)
    inv_difference = power(sub(LAMBDA, 1), Q - 2)
    center = (mul(inv_difference, t[0]), mul(inv_difference, t[1]), t[2], t[3])
    return x, y, (center, ZERO_Z), phase((1, 1), form(h, center))


def arbitrary_defect_checks():
    # The two reciprocal blocks choose their actor coordinates independently;
    # c=-g kills the coefficient of b in the correction formula.

    rng = random.Random(SEED + 2)
    targets = [ZERO_U]
    targets.extend((0, 0, a, b) for a, b in product(range(7), repeat=2))
    targets.extend((a, b, 0, 0) for a, b in [(1, 0), (0, 1), (243, 0), (0, 243)])
    targets.extend(random_u(rng) for _ in range(160))
    for h in targets:
        x, y = prescribed_defect_witness(h)
        assert form(x[0], y[0]) == G and defect(x, y) == (h, G)
    phase_space = []
    for tw, tv, kw, kv in product((0, 1), repeat=4):
        phase_space.append(((tw, 0, tv, 0), (0, kw, 0, kv)))
    for _ in range(100):
        t, k = random_u(rng), random_u(rng)
        phase_space.append((t, k))
        phase_space.append((actor(G, k), k))  # h=0 special case
    for t, k in phase_space:
        x, y, z, scalar = weyl_actor_witness(t, k)
        u = random_u(rng)
        ru = actor(G, u)
        desired = uadd(t, ru), (scalar + phase((1, 1), form(k, ru))) % 21
        assert translated_direct(x, y, z, (u, 0), (1, 1)) == desired
    return {"prescribed_full_defects": len(targets), "all_ring_targets_exhausted": 49,
            "full_Weyl_actor_realizations": len(phase_space)}


def field_commutant_checks():
    # Four actual native unitaries (K=2n at n=2) have a nonzero, traceless
    # fixed operator: the seven-term orbit sum of translations along e1.
    # This is one finite witness for the general phase-space obstruction.
    e1, e2 = (1, 0, 0, 0), (0, 1, 0, 0)
    labels = [(ZERO_U, ZERO_U), (e1, ZERO_U), (e2, ZERO_U), (ZERO_U, e1)]
    orbit = [(coefficient, 0, 0, 0) for coefficient in LP]
    assert len(set(orbit)) == 7 and ZERO_U not in orbit
    assert set(actor(G, w) for w in orbit) == set(orbit)
    rng = random.Random(SEED + 3)
    checks = 0
    for t, k in labels:
        x, y, z, scalar = weyl_actor_witness(t, k)
        for w in orbit:
            assert phase((1, 1), form(k, actor(G, w))) == 0
            for _ in range(4):
                u = random_u(rng)
                left = translated_direct(x, y, z, (uadd(u, w), 0), (1, 1))
                target, exponent = translated_direct(x, y, z, (u, 0), (1, 1))
                assert left == (uadd(target, actor(G, w)), exponent)
                checks += 1
    # The inverse eigenvalue is Frobenius-conjugate to lambda in F729.
    # Checking every element certifies the concrete twist used in the witness.
    inverse_lambda = power(LAMBDA, 6)
    for a in range(Q):
        assert power(mul(inverse_lambda, a), 27) == mul(LAMBDA, power(a, 27))
    return {"field_dimension": 2, "native_generators": 4, "fixed_Weyl_orbit_size": 7,
            "exact_ket_covariance_checks": checks, "Frobenius_twist_elements_exhausted": Q}


def scalar_pair_bijections():
    # Two draws s,t give translation R*s+t and modulation s+R*t,
    # followed by a fixed actor R^2.  This checks every scalar pair.
    ls = [mul(LAMBDA, a) for a in range(Q)]
    field_images = {(add(ls[s], t), add(s, ls[t])) for s in range(Q) for t in range(Q)}
    assert len(field_images) == Q**2
    ring_images = {((2 * s + t) % 7, (s + 2 * t) % 7) for s in range(7) for t in range(7)}
    assert len(ring_images) == 49
    assert sub(mul(LAMBDA, LAMBDA), 1) != 0 and (2**2 - 1) % 7 != 0
    return {"field_pairs_exhausted": Q**2, "ring_pairs_exhausted": 49}


def ring_channel_checks():
    points = list(product(range(7), repeat=2))
    indices = list(product(points, repeat=2))

    def step(v, h):
        return tuple(2 * x % 7 for x in v), tuple(4 * x % 7 for x in h)

    def argument(v, h):
        return tuple((a + 4 * b) % 7 for a, b in zip(v, h))

    def bias_full(a):
        return int(a == (0, 0))

    def bias_line(a):
        # Uniform t=(s,0); det(t,a)=s*a[1].
        return int(a[1] == 0)

    full_one, full_two, line_two = [], [], []
    for v, h in indices:
        first = argument(v, h)
        v1, h1 = step(v, h)
        second = argument(v1, h1)
        full_one.append(bias_full(first))
        full_two.append(bias_full(first) * bias_full(second))
        line_two.append(bias_line(first) * bias_line(second))
    assert sum(full_one) == 49
    assert sum(full_two) == 1  # only identity Weyl operator survives
    assert sum(line_two) == 49
    assert max(full_one[1:]) == 1 and max(full_two[1:]) == 0
    # Every diagonal traceless Weyl has v=0,h!=0 and is killed in one draw.
    assert all(bias_full(argument((0, 0), h)) == 0 for h in points[1:])
    # Uniform group shifts plus phases also give exact depolarization.
    control_survivors = [int(v == (0, 0) and h == (0, 0)) for v, h in indices]
    assert control_survivors == full_two
    return {"ring_hilbert_dimension": 49, "weyl_basis_exhausted": len(indices),
            "full_twirl_one_step_rank": sum(full_one), "full_twirl_two_step_rank": sum(full_two),
            "line_twirl_two_step_rank": sum(line_two), "tracezero_HS_norm_one_step": 1,
            "tracezero_HS_norm_two_steps": 0, "group_control_identical": True}


def fused_decorrelation_checks():
    # This is an algebraic, non-trace-preserving ablation, not a competing
    # physical randomizer.  Decoupling V and conjugate(V) gives A*T*A*, where
    # A is the average of the exact displayed fixed-pair representatives.
    # Work on the complete F7^2 ring factor, without floating-point roots.
    points = list(product(range(7), repeat=2))

    def determinant(a, b):
        return (a[0] * b[1] - a[1] * b[0]) % 7

    entries = {}
    for s, u in product(points, repeat=2):
        t = tuple((x - 2 * y) % 7 for x, y in zip(s, u))
        exponent = determinant(t, u)
        assert exponent == determinant(s, u)
        entries[s, u] = exponent  # A entry is zeta_7**exponent / 49.

    diagonal, off_diagonal, terms = 0, 0, 0
    for u, v in product(points, repeat=2):
        histogram = [0] * 7
        for s in points:
            histogram[(entries[s, v] - entries[s, u]) % 7] += 1
            terms += 1
        if u == v:
            assert histogram == [49, 0, 0, 0, 0, 0, 0]
            diagonal += 1
        else:
            # 1 + zeta + ... + zeta^6 = 0 exactly.
            assert histogram == [7] * 7
            off_diagonal += 1
    assert diagonal == 49 and off_diagonal == 2352
    return {"ring_hilbert_dimension": 49, "average_matrix_entries": len(entries),
            "gram_character_terms": terms, "gram_diagonal_entries": diagonal,
            "gram_zero_offdiagonal_entries": off_diagonal,
            "A_star_A": "I/49", "decoupled_state_output_trace": "1/49",
            "trace_preserving": False,
            "scope": "Chosen exact V_t representatives; phase-dependent algebraic ablation."}


def stabilizer_purity_checks():
    # Exact finite check of the improved arbitrary-state purity bound.  The
    # distribution is theta*delta_0+(1-theta)*uniform on F7^2; every nontrivial
    # Fourier coefficient equals theta.  All 400 Lagrangian planes give pure
    # stabilizer states.  Their coefficient magnitudes, and hence purity, need
    # no floating-point roots of unity or explicit density matrices.
    p = 7
    theta = Fraction(1, 5)
    expected_bound = (49 - 1) * theta**4 + 2 * (7 - 1) * (theta**2 - theta**4)

    def omega(a, b):
        return (a[2] * b[1] - a[3] * b[0] - b[2] * a[1] + b[3] * a[0]) % p

    checked, equality, largest = 0, 0, Fraction(0)
    intersections = {}
    for first, second in combinations(range(4), 2):
        free = [(0, j) for j in range(first + 1, 4) if j != second]
        free.extend((1, j) for j in range(second + 1, 4))
        for values in product(range(p), repeat=len(free)):
            rows = [[0] * 4, [0] * 4]
            rows[0][first], rows[1][second] = 1, 1
            for (row, column), value in zip(free, values):
                rows[row][column] = value
            a, b = rows
            if omega(a, b):
                continue
            plane = {tuple((s * x + t * y) % p for x, y in zip(a, b))
                     for s, t in product(range(p), repeat=2)}
            assert len(plane) == 49
            g1 = sum(h0 == -2 * v0 % 7 and h1 == -2 * v1 % 7 for v0, v1, h0, h1 in plane)
            g2 = sum(h0 == -v0 % 7 and h1 == -v1 % 7 for v0, v1, h0, h1 in plane)
            assert g1 <= 7 and g2 <= 7
            exceptional = g1 + g2 - 2
            # This is d*HS-error^2, the numerator of the purity excess.
            value = 48 * theta**4 + exceptional * (theta**2 - theta**4)
            assert value <= expected_bound
            largest = max(largest, value)
            equality += value == expected_bound
            intersections[str((g1, g2))] = intersections.get(str((g1, g2)), 0) + 1
            checked += 1
    assert checked == 400 and equality > 0 and largest == expected_bound
    return {"ring_hilbert_dimension": 49, "lagrangian_planes_exhausted": checked,
            "nontrivial_bias": str(theta), "sharp_d_times_HS_error_squared": str(largest),
            "equality_stabilizer_states": equality, "graph_intersection_counts": intersections}


def degenerate_checks():
    rng = random.Random(SEED + 1)
    checks = 0
    for chi in [(0, 1), (1, 0), (0, 0)]:
        for _ in range(100):
            x, y, z = (random_loop(rng) for _ in range(3))
            h, g = defect(x, y)
            u, v = random_u(rng), random_u(rng)
            if chi == (0, 1):
                v = v[0], v[1], 0, 0
            elif chi == (1, 0):
                v = 0, 0, v[2], v[3]
            # V*T_v = T_{R(g)v}*V exactly, including phase, for v in D_chi.
            left = translated_direct(x, y, z, (uadd(u, v), 0), chi)
            right_u, right_phase = translated_direct(x, y, z, (u, 0), chi)
            right = uadd(right_u, actor(g, v)), right_phase
            assert left == right
            checks += 1
    # P_D/Tr(P_D) has distance 2(1-1/|D|), for each displayed radical.
    distances = {"field_radical": str(2 * (1 - Fraction(1, Q**2))),
                 "ring_radical": str(2 * (1 - Fraction(1, 49))),
                 "zero_character": str(2 * (1 - Fraction(1, Q**2 * 49)))}
    return {"exact_radical_translation_checks": checks, "stationary_state_trace_norm": distances}


def sparse_orbit_checks():
    # A tiny affine-scalar model over F7, dimension four, with two native-shaped
    # maps.  This is an isolated support obstruction control, not another Bol
    # loop admissibility claim.  It permits full orbit enumeration.
    modulus, dimension = 7, 4
    translations = [(1, 0, 0, 0), (0, 1, 0, 0)]
    generators = [(2, translations[0]), (4, translations[1])]
    # Choose the fixed point of the first generator.  Centering there removes
    # its translation, improving the span bound from K to K-1 directions.
    anchor = (6, 0, 0, 0)
    orbit = {anchor}
    frontier = list(orbit)
    while frontier:
        point = frontier.pop()
        for scalar, t in generators:
            out = tuple((scalar * x + y) % modulus for x, y in zip(point, t))
            if out not in orbit:
                orbit.add(out)
                frontier.append(out)
    assert len(orbit) == 7 and all(point[2:] == (0, 0) for point in orbit)
    bound = 2 * (1 - Fraction(len(orbit), modulus**dimension))
    assert bound == Fraction(684, 343)
    return {"toy_field_size": modulus, "toy_dimension": dimension,
            "generators": len(generators), "anchor": anchor,
            "complete_reachable_orbit": len(orbit),
            "trace_norm_lower_bound": str(bound)}


def baseline_rates():
    # Exact diagonal eigenvalues from the recovered k=1,A=1 formula; finite
    # arithmetic check only.  The baseline proof establishes the full spectrum.
    d = Q**2 * 49
    population = Fraction(1, 3) + Fraction(2, 3 * Q**2)
    field_multiplier = Fraction(1, 7) * (1 + Fraction(6, 49))
    coherence_bound = Fraction(1, 9)
    assert population > field_multiplier > coherence_bound
    return {"dimension": d, "population_rate": str(population),
            "field_diagonal_rate": str(field_multiplier),
            "coherence_upper_bound": str(coherence_bound),
            "three_step_uniform_population_purity_bound":
                str(Fraction(1, d) + Fraction(1, 3**12) * (1 - Fraction(1, d)))}


def doeblin_checks():
    # The ring conditional law is completely enumerated, retaining the actual
    # determinant and all original actor choices.  Field checks certify exact
    # trace-functional ranks for stated finite targets; they do not enumerate
    # the enormous complete field pair distribution.
    points = list(product(range(7), repeat=2))
    ring_fibers, ring_terms = 0, 0
    for gp, gq in product((1, 2), range(1, 7)):
        histogram = {h: 0 for h in points}
        for a, v in product(points, repeat=2):
            if (a[0] * v[1] - a[1] * v[0]) % 7 != gq:
                continue
            for c, e in product(range(3), repeat=2):
                alpha = (EP[gp] - EP[e]) % 7
                beta = (EP[(c + gp) % 3] - 1) % 7
                h = tuple((alpha * x + beta * y) % 7 for x, y in zip(a, v))
                histogram[h] += 1
                ring_terms += 1
        total = sum(histogram.values())
        assert total == 3024
        assert Fraction(histogram[(0, 0)], total) == Fraction(1, 9)
        assert all(Fraction(count, total) == Fraction(1, 54)
                   for h, count in histogram.items() if h != (0, 0))
        ring_fibers += 1

    field_basis = [(3**i, 0) for i in range(6)] + [(0, 3**i) for i in range(6)]
    targets = field_basis + [(1, 243), (721, 571), (533, 671)]
    field_rank_checks = 0
    coefficient_pairs = []
    for c, e in product(range(7), repeat=2):
        alpha = sub(LP[1], LP[e])
        beta = sub(LP[(c + 1) % 7], 1)
        coefficient_pairs.append((alpha, beta))
        if not alpha and not beta:
            continue
        for h in [(0, 0)] + targets:
            if beta:
                inverse = power(beta, Q - 2)
                functional = [trace(mul(inverse, sub(mul(a[0], h[1]), mul(a[1], h[0]))))
                              for a in field_basis]
            else:
                inverse = power(alpha, Q - 2)
                a = mul(inverse, h[0]), mul(inverse, h[1])
                functional = [trace(sub(mul(a[0], v[1]), mul(a[1], v[0])))
                              for v in field_basis]
            assert bool(any(functional)) == (h != (0, 0))
            field_rank_checks += 1
    assert coefficient_pairs.count((0, 0)) == 1
    dimension = Q**2
    # Given a nonzero pairing, each nonzero h has D/p preimages for every
    # nonzero actor coefficient pair.  The rank checks above verify this on
    # exactly the listed targets; the manuscript proves it for all targets.
    field_atom = Fraction(1, 49)
    field_nonzero_point = Fraction(48, 49 * (dimension - 1))
    c_field = dimension * field_nonzero_point
    c_ring = Fraction(49, 54)
    assert c_field <= dimension * field_atom
    gp_nonzero = Fraction(2, 3) * (1 - Fraction(1, dimension))
    gq_nonzero = Fraction(288, 343)
    minorization = gp_nonzero * gq_nonzero * c_field * c_ring
    assert minorization == Fraction(512, 1029)
    assert 1 - minorization == Fraction(517, 1029)
    return {"complete_nonzero_ring_pairing_histograms": ring_fibers,
            "actual_ring_pair_actor_terms_enumerated": ring_terms,
            "ring_conditional_zero_mass": "1/9", "ring_conditional_each_nonzero_mass": "1/54",
            "field_actor_coefficient_pairs_exhausted": len(coefficient_pairs),
            "field_nonzero_targets_checked": len(targets),
            "field_trace_functional_rank_checks": field_rank_checks,
            "field_conditional_zero_mass": str(field_atom),
            "field_nonzero_fiber_size": dimension // 3,
            "uniform_field_component": str(c_field), "uniform_ring_component": str(c_ring),
            "depolarizing_minorization": str(minorization), "diamond_residual_base": "517/1029"}


def main():
    result = {"seed": SEED, "arithmetic": arithmetic_checks(),
              "native": actual_native_checks(), "prescribed_defects": arbitrary_defect_checks(),
              "field_commutant": field_commutant_checks(),
              "two_draw_bijections": scalar_pair_bijections(),
              "ring_channel": ring_channel_checks(), "degenerate": degenerate_checks(),
              "fused_decorrelation": fused_decorrelation_checks(),
              "stabilizer_purity": stabilizer_purity_checks(),
              "sparse_orbit": sparse_orbit_checks(), "baseline": baseline_rates(),
              "doeblin": doeblin_checks()}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
