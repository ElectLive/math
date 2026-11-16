#!/usr/bin/env python3
"""Check extracted CTblLib class centralizers and raw inequalities.

These are the selected classes, including the identity, not a complete table.
The selection and identification of the source tables are external inputs.
"""
CASES = {
    'L4(3).2^2': (6065280, 24261120, 27640, [24261120,11520,4608,22464,103680,2304,2880], True),
    'L4(4).2^2': (987033600, 3948134400, 414704, [3948134400,737280,61440,80640,3916800,15360,103680], True),
    'U4(3).D8': (3265920, 26127360, 28576, [26127360,9216,48384,5760,103680,2304,2880], False),
    'U4(4).4': (1018368000, 4073472000, 335856, [4073472000,1228800,61440,3916800,15360], True),
    'U4(5).2^2': (14742000000, 58968000000, 2391776, [58968000000,345600,249600,18720000,57600,4536000,62400], True),
    'U5(2).2': (13685760, 27371520, 22144, [27371520,165888,9216,1440], True),
    'U6(2).3.2': (9196830720, 55180984320, 1529056, [55180984320,79626240,884736,221184,2903040,46080], True),
}

for name, (n, a, b, centralizers, expected) in CASES.items():
    assert n >= 2**20 and a % n == 0
    assert centralizers[0] == a and all(a % c == 0 for c in centralizers)
    assert sum(a // c for c in centralizers) == b
    assert (b**3 + 3*a*b < n**2) == expected, name
n,a,b,*_ = CASES['U4(3).D8']
assert b**3 + 3*a*b == 25574658605056
assert n**2 == 10666233446400
print('finite classical Aut class-count arithmetic passed')
