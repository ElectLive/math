#!/usr/bin/env python3
"""Independent negative control: uniform inner-defect averages need not reverse.

The supplied order-five Latin loop is enumerated directly.  No formula from the
reciprocal-family construction is used.  Rows of the integer matrix are starting
states and columns are resulting states, with denominator |Q|^2 = 25.
"""

import json


TABLE = [
    [0, 1, 2, 3, 4],
    [1, 0, 3, 4, 2],
    [2, 3, 4, 0, 1],
    [3, 4, 1, 2, 0],
    [4, 2, 0, 1, 3],
]
EXPECTED = [
    [25, 0, 0, 0, 0],
    [0, 16, 3, 3, 3],
    [0, 3, 11, 5, 6],
    [0, 3, 6, 11, 5],
    [0, 3, 5, 6, 11],
]


def mul(x, y):
    return TABLE[x][y]


def ldiv(x, y):
    return TABLE[x].index(y)


def defect(x, y, z):
    return ldiv(mul(x, y), mul(x, mul(y, z)))


def main():
    states = range(len(TABLE))
    assert all(sorted(row) == list(states) for row in TABLE)
    assert all(sorted(TABLE[i][j] for i in states) == list(states) for j in states)
    assert all(mul(0, x) == x == mul(x, 0) for x in states)
    bol_failures = []
    counts = [[0 for _ in states] for _ in states]
    for x in states:
        for y in states:
            for z in states:
                counts[z][defect(x, y, z)] += 1
                lhs = mul(x, mul(y, mul(x, z)))
                rhs = mul(mul(x, mul(y, x)), z)
                if lhs != rhs:
                    bol_failures.append([x, y, z, lhs, rhs])
    assert counts == EXPECTED
    assert bol_failures
    assert counts[2][3] == 5 and counts[3][2] == 6
    assert all(sum(row) == 25 for row in counts)
    assert all(sum(counts[i][j] for i in states) == 25 for j in states)
    print(json.dumps({
        "check": "direct-loop-defect-average",
        "order": len(TABLE),
        "point_compositions": len(TABLE) ** 3,
        "denominator": 25,
        "matrix_convention": "row = start, column = end",
        "matrix_numerator": counts,
        "bol_identity_failures": len(bol_failures),
        "first_bol_failure_xyz_lhs_rhs": bol_failures[0],
        "not_self_adjoint_witness": [2, 3, counts[2][3], counts[3][2]],
        "result": "PASS: generic loop averaging is not automatically reversible",
    }, sort_keys=True))


if __name__ == "__main__":
    main()

