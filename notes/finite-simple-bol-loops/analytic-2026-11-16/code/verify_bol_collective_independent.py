#!/usr/bin/env python3
"""Independent exact incidence/round-trip check on a 27-input restriction.

No imports from the authored verifier.  The restriction is the actual good
Bol word with u in lambda*F_3^3, y in F_3^3, and the second E^3 block zero.
Its beta is u cross y because Tr(lambda)=-1.  This checks the counting
observable, normalization and round-trip Gram factor, not the full E^6 norm.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
import json


POINTS = list(product(range(3), repeat=3))
ZERO = (0, 0, 0)


def dot(x, y):
    return sum(a*b for a, b in zip(x, y)) % 3


def cross(x, y):
    return ((x[1]*y[2]-x[2]*y[1]) % 3,
            (x[2]*y[0]-x[0]*y[2]) % 3,
            (x[0]*y[1]-x[1]*y[0]) % 3)


# Q(sqrt(21)) pair arithmetic; no approximate square roots.
def smul(x, y):
    return (x[0]*y[0]+21*x[1]*y[1], x[0]*y[1]+x[1]*y[0])


W = [(F(2, 9), F(0)), (F(7, 18), F(1, 18)),
     (F(7, 18), F(-1, 18))]
WEIGHTS = {nu: smul(smul(W[nu[0]], W[nu[1]]), W[nu[2]])
           for nu in POINTS}


def mass(predicate):
    value = (F(0), F(0))
    for nu, w in WEIGHTS.items():
        if predicate(nu):
            value = (value[0]+w[0], value[1]+w[1])
    assert value[1] == 0
    return value[0]


# Integer arithmetic in Z[omega], omega^2+omega+1=0.
def omul(x, y):
    return (x[0]*y[0]-x[1]*y[1],
            x[0]*y[1]+x[1]*y[0]-x[1]*y[1])


def theta(t):
    return (1, 0) if t % 7 == 0 else (-1, -1)


def conjugate(x):
    return (x[0]-x[1], -x[1])


CORR = {}
for g, h in product(range(7), repeat=2):
    pieces = [omul(theta(s-g), conjugate(theta(s-h))) for s in range(7)]
    CORR[g, h] = tuple(sum(x[i] for x in pieces) for i in range(2))


def observable(u, y, a):
    b = cross(u, y)
    return sum(pow(2, (ai-bi) % 3, 7) for ai, bi in zip(a, b)) % 7


def main():
    assert sorted(pow(3, j, 7) for j in range(6)) == list(range(1, 7))
    assert mass(lambda _: True) == 1
    counts = {}
    round_sums = {}
    for d in POINTS:
        equal = 0
        total = [0, 0]
        for u, a in product(POINTS, repeat=2):
            gd, gz = observable(u, d, a), observable(u, ZERO, a)
            equal += gd == gz
            rr = CORR[gd, gz]
            total[0] += rr[0]
            total[1] += rr[1]
        assert total[1] == 0
        counts[d] = equal
        round_sums[d] = total[0]

    incidence = {}
    roundtrip = {}
    one_way = {}
    for xi in POINTS:
        c = [sum(counts[d] for d in POINTS if dot(xi, d) == j)
             for j in range(3)]
        r = [sum(round_sums[d] for d in POINTS if dot(xi, d) == j)
             for j in range(3)]
        assert c[1] == c[2] and r[1] == r[2]
        mi = F(c[0]-c[1], 27**3*7)
        mr = F(r[0]-r[1], 27**3*7)
        mt = mass(lambda nu: nu != ZERO and dot(nu, xi) == 0)/9
        if xi == ZERO:
            mt += F(8, 729)
        assert mi == F(1, 49)*(xi == ZERO)+F(6, 49)*mt
        assert mr == F(31, 49)*(xi == ZERO)+F(18, 49)*mt
        if xi != ZERO:
            assert mr == 3*mi
        incidence[xi], roundtrip[xi], one_way[xi] = mi, mr, mt

    max_one = max(v for xi, v in one_way.items() if xi != ZERO)
    max_inc = max(v for xi, v in incidence.items() if xi != ZERO)
    max_round = max(v for xi, v in roundtrip.items() if xi != ZERO)
    assert max_one == F(343, 6561)
    assert max_inc == F(14, 2187)
    assert max_round == F(14, 729)
    result = {
        "status": "PASS",
        "arithmetic": "exact fractions, Q(sqrt(21)), and Z[omega]",
        "input_points": 27,
        "output_points": 27*27*7,
        "word_difference_cases": 27**3,
        "roundtrip_correlation_terms": 27**3*7,
        "multipliers_checked": 27,
        "incidence_collision_histogram": dict(sorted(Counter(counts.values()).items())),
        "centered_squared_norms_on_restriction": {
            "one_way": str(max_one), "incidence": str(max_inc),
            "roundtrip": str(max_round)},
        "constant_squared_norms_on_restriction": {
            "one_way": str(one_way[ZERO]), "incidence": str(incidence[ZERO]),
            "roundtrip": str(roundtrip[ZERO])},
        "limits": "Restricted 27-input model only; not full E^6 or arbitrary h."
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

