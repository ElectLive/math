#!/usr/bin/env python3
"""Authored exact, bounded checks of the trace-polarized Bol transfer.

Uses the preceding authored field implementation; this is not an
independent implementation or mathematical review. No floating point.
"""

import json
from pathlib import Path
import random
import sys

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import verify_bol_conductor_vector as V


def selected(r):
    result = {0}
    for j in range(1, 7**r):
        z = j
        while z % 7 == 0:
            z //= 7
        if z % 7 in (1, 2, 3):
            result.add(j)
    return result


def basis_pair_checks():
    rows = []
    for i in range(7):
        row = []
        for j in range(7):
            result = V.relative_trace_direct(V.fm(V.TP[i], V.TP[j]))
            expected = 1 if i == j == 0 else V.E.LAM if i + j == 7 else 0
            assert result == V.emb(expected)
            row.append(expected)
        rows.append(row)
    assert V.E.matrix_rank(rows) == 7
    assert V.E.matrix_rank([row[1:] for row in rows[1:]]) == 6
    assert V.E.matrix_rank([row[:4] for row in rows[:4]]) == 1
    assert all(rows[i][j] == 0 for i in range(1, 4) for j in range(4))
    return {"exact_F_729_to_F_729_power_7_basis_pair_traces": 49,
            "full_pairing_rank": 7, "trace_zero_pairing_rank": 6,
            "polarized_pairing_rank": 1,
            "polarized_dimension": 4, "isotropic_kernel_dimension": 3}


def digit_checks():
    sets = {r: selected(r) for r in range(1, 4)}
    for r, s in sets.items():
        d = 7**r
        assert len(s) == (d + 1) // 2
        assert all((j in s) != (d-j in s) for j in range(1, d))
        assert all(i+j != d for i in s for j in s)
    cases = []
    for r1 in range(1, 3):
        for r2 in range(1, 4-r1):
            d1, d2 = 7**r1, 7**r2
            expected = {i*d2+j for j in sets[r2] - {0} for i in range(d1)}
            expected |= {i*d2 for i in sets[r1]}
            assert expected == sets[r1+r2]
            cases.append([r1, r2, len(expected)])
    return {"gap_dimensions": {str(r): len(s) for r,s in sets.items()},
            "all_complement_pairs_checked": sum(7**r-1 for r in sets),
            "tower_recursions": cases}


def random_polar_element(rng):
    return tuple(rng.randrange(729) for _ in range(4)) + (0, 0, 0)


def random_polar_state(rng):
    ring = []
    for _ in range(3):
        ring += [7*rng.randrange(7), rng.randrange(49)]
    return (tuple(random_polar_element(rng) for _ in range(6)),
            tuple(ring), tuple(rng.randrange(3) for _ in range(3)),
            7*rng.randrange(7))


def reduce_state(s):
    w,v,a,t = s
    assert all(not any(x[4:]) for x in w)
    assert t % 7 == 0 and all(v[2*i] % 7 == 0 for i in range(3))
    return (tuple(x[0] for x in w),
            tuple(z//7 if i%2 == 0 else z%7 for i,z in enumerate(v)),
            a,t//7)


def action_checks():
    rng = random.Random(2026111617)
    count = 0
    for family in ("good", "aligned"):
        for _ in range(24):
            x,y,z = (random_polar_state(rng) for _ in range(3))
            mul = lambda a,b: V.op(a,b,family,2)
            low = lambda a,b: V.E.loop_mul(a,b,family)
            assert reduce_state(mul(x,y)) == low(reduce_state(x),reduce_state(y))
            assert mul(x,mul(y,mul(x,z))) == mul(mul(x,mul(y,x)),z)
            assert V.beta(x[0],y[0],family) == V.E.beta(
                reduce_state(x)[0],reduce_state(y)[0],family)
            # Polar kernel is genuinely present, not merely the subfield.
            assert any(any(u[1:4]) for u in x[0])
            count += 1
    return {"seed": 2026111617, "families": 2,
            "actual_polarized_section_and_Bol_cases": count,
            "identities": ["subloop closure and quotient multiplication",
                           "actual upper Bol identity",
                           "full pencil trace factorization",
                           "nonzero isotropic field fibers present"]}


if __name__ == "__main__":
    print(json.dumps({"basis": basis_pair_checks(),
                      "digits": digit_checks(),
                      "actions": action_checks(),
                      "scope": "exact bounded authored checks, not a proof or independent review"},
                     indent=2, sort_keys=True))

