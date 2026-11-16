#!/usr/bin/env python3
"""Fixed S5/F20 quadratic-component checks for the N-Frattini marked bound."""
from itertools import combinations

assert __debug__
C5 = (1, 0, 2, 3, 4)
D5 = (0, 2, 3, 4, 1)
C6 = (1, 0, 3, 2, 5, 4)
D6 = (0, 2, 3, 4, 1, 5)


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def power(a, n):
    out = tuple(range(len(a)))
    for _ in range(n):
        out = compose(out, a)
    return out


def add(pivots, value):
    while value:
        i = value.bit_length() - 1
        if i in pivots:
            value ^= pivots[i]
        else:
            pivots[i] = value
            return


def rank(values):
    pivots = {}
    for value in values:
        add(pivots, value)
    return len(pivots)


def permute(v, p):
    return sum(((v >> i) & 1) << p[i] for i in range(len(p)))


def natural(v, p):
    out = 0
    for i in range(4):
        if v >> i & 1:
            out ^= (1 << p[0]) ^ (1 << p[i + 1])
    return (out >> 1) & 15


def j_action(v, p):
    out = permute(v, p)
    return (out ^ 63 if out & 32 else out) & 31


def group_control():
    identity = (tuple(range(5)), tuple(range(6)))
    group = {identity}
    queue = [identity]
    for g in queue:
        for a, b in ((C5, C6), (D5, D6)):
            h = (compose(g[0], a), compose(g[1], b))
            if h not in group:
                group.add(h)
                queue.append(h)
    assert len(group) == 120
    assert len({g[0] for g in group}) == len({g[1] for g in group}) == 120
    p = next(g for g in group if power(g[0], 5) == tuple(range(5)) and g[0] != tuple(range(5)))
    cyclic = {power(p[0], i) for i in range(5)}
    normalizer = [g for g in group if compose(compose(g[0], p[0]), inverse(g[0])) in cyclic]
    assert len(normalizer) == 20
    assert rank((1 << i) ^ natural(1 << i, p[0]) for i in range(4)) == 4
    assert rank((1 << i) ^ j_action(1 << i, p[1]) for i in range(5)) == 4
    assert rank((1 << i) ^ permute(1 << i, p[1]) for i in range(6)) == 4
    assert rank((1 << i) ^ natural(1 << i, C5) for i in range(4)) == 1
    assert rank((1 << i) ^ j_action(1 << i, C6) for i in range(5)) == 2
    assert rank((1 << i) ^ permute(1 << i, C6) for i in range(6)) == 3
    assert rank((1 << i) ^ (natural((1 << i) >> 4, C5) | (natural((1 << i) & 15, C5) << 4)) for i in range(8)) == 4
    fixed_j = [v for v in range(32) if all(j_action(v, g[1]) == v for g in normalizer)]
    fixed_p6 = [v for v in range(64) if all(permute(v, g[1]) == v for g in normalizer)]
    assert len(fixed_j) == 2 and len(fixed_p6) == 4
    print('paired S5 order 120, F20 order 20; fixed dimensions and transposition ranks verified')


def component_control(kind):
    base = 5 if kind == 'J' else 6
    dim = base + 16

    def source(v, p5, p6):
        first = v & ((1 << base) - 1)
        out = j_action(first, p6) if kind == 'J' else permute(first, p6)
        for j in range(2):
            x = (v >> (base + 8*j)) & 255
            out |= (natural(x >> 4, p5) | (natural(x & 15, p5) << 4)) << (base + 8*j)
        return out

    monomials = [(i, i) for i in range(dim)] + list(combinations(range(dim), 2))

    def feature(v):
        return sum((((v >> i) & 1) & ((v >> j) & 1)) << k
                   for k, (i, j) in enumerate(monomials))

    samples = [1 << i for i in range(dim)] + [(1 << i) ^ (1 << j)
                                               for i, j in combinations(range(dim), 2)]
    rows = []
    for p5, p6 in ((C5, C6), (D5, D6)):
        for v in samples:
            f, g = feature(v), feature(source(v, p5, p6))
            for bit in range(4):
                row = 0
                for k in range(len(monomials)):
                    if g >> k & 1:
                        row ^= 1 << (4*k + bit)
                    if f >> k & 1:
                        for j in range(4):
                            if natural(1 << j, p5) >> bit & 1:
                                row ^= 1 << (4*k + j)
                rows.append(row)
    image = [(1 << i) ^ natural(1 << i, C5) for i in range(4)]
    annihilator = [a for a in range(1, 16)
                   if all((a & x).bit_count() % 2 == 0 for x in image)]
    extra = []
    for v in samples:
        tv = source(v, C5, C6)
        polar = feature(v) ^ feature(tv) ^ feature(v ^ tv)
        for covector in annihilator:
            row = 0
            for k in range(len(monomials)):
                if polar >> k & 1:
                    for j in range(4):
                        if covector >> j & 1:
                            row ^= 1 << (4*k+j)
            extra.append(row)
    groups = {'X': [], 'U': [], 'XU': [], 'UU': []}
    for k, (i, j) in enumerate(monomials):
        if i < base and j < base:
            name = 'X'
        elif base <= i < base+8 and base <= j < base+8:
            name = 'U'
        elif i < base and base <= j < base+8:
            name = 'XU'
        elif base <= i < base+8 and base+8 <= j < base+16:
            name = 'UU'
        else:
            continue
        groups[name].extend(4*k+x for x in range(4))

    result = {}
    for name, indices in groups.items():
        def project(row):
            return sum(((row >> i) & 1) << j for j, i in enumerate(indices))
        before = len(indices) - rank(project(row) for row in rows)
        after = len(indices) - rank(project(row) for row in rows + extra)
        result[name] = before, after
    expected = {'X': (1, 0), 'U': (2, 1),
                'XU': ((1, 1) if kind == 'J' else (2, 2)), 'UU': (2, 2)}
    assert result == expected, (kind, result)
    # Every equivariant U-U cross map vanishes on soc(U) x soc(U).
    # In swap coordinates the socle is the diagonal {(a,a): a in N}.
    indices = groups['UU']
    def project_uu(row):
        return sum(((row >> i) & 1) << j for j, i in enumerate(indices))
    base_rows = [project_uu(row) for row in rows]
    evaluations = []
    for i in range(4):
        for j in range(4):
            v = ((1 << i) | (1 << (i+4))) << base
            w = ((1 << j) | (1 << (j+4))) << (base+8)
            f = feature(v) ^ feature(w) ^ feature(v ^ w)
            for bit in range(4):
                evaluations.append(project_uu(sum(((f >> k) & 1) << (4*k+bit)
                                                  for k in range(len(monomials)))))
    assert rank(base_rows + evaluations) == rank(base_rows)
    print(kind, 'both U-U cross maps vanish on socle pairs')
    # The compatible U map is the linear top projection (a,b) -> a+b.
    for p5, p6 in ((C5, C6), (D5, D6)):
        for v in range(256):
            transported = (source(v << base, p5, p6) >> base) & 255
            image_v = (transported & 15) ^ (transported >> 4)
            expected_v = natural((v & 15) ^ (v >> 4), p5)
            assert image_v == expected_v
    print(kind, 'component dimensions (full, marked-compatible):', result)


if __name__ == '__main__':
    group_control()
    component_control('J')
    component_control('P6')
