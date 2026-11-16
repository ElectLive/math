#!/usr/bin/env python3
"""Finite ATLAS class-square and scalar certificate; see linked manuscript.

The embedded permutations reproduce ATLAS GAP generators whose exact URLs and
SHA-256 values are recorded in manuscripts/sd-finite-common-classes.md.
This computation does not verify ATLAS group identification or folder proofs.
"""

DATA = {'j2': {'c': [(1, 88),
              (2, 22),
              (4, 5),
              (6, 98),
              (7, 66),
              (8, 24),
              (9, 20),
              (10, 75),
              (12, 74),
              (13, 39),
              (14, 45),
              (15, 58),
              (16, 46),
              (17, 55),
              (18, 96),
              (19, 48),
              (21, 94),
              (23, 76),
              (26, 42),
              (27, 65),
              (29, 51),
              (30, 86),
              (31, 70),
              (32, 71),
              (34, 78),
              (35, 93),
              (36, 56),
              (37, 87),
              (38, 67),
              (40, 83),
              (41, 59),
              (43, 73),
              (47, 100),
              (49, 72),
              (50, 77),
              (52, 95),
              (54, 84),
              (57, 82),
              (61, 91),
              (62, 64),
              (69, 81),
              (79, 97),
              (89, 99)],
        'd': [(1, 59, 75, 7, 64),
              (2, 84, 69, 93, 9),
              (3, 78, 51, 10, 30),
              (4, 14, 20, 67, 8),
              (5, 99, 43, 32, 46),
              (6, 54, 89, 11, 90),
              (12, 33, 21, 56, 35),
              (13, 58, 87, 49, 45),
              (15, 18, 76, 94, 37),
              (16, 50, 88, 79, 27),
              (17, 70, 52, 82, 38),
              (19, 91, 41, 73, 62),
              (22, 55, 23, 65, 86),
              (24, 61, 29, 98, 63),
              (25, 81, 96, 83, 48),
              (26, 68, 77, 100, 44),
              (28, 92, 97, 57, 34),
              (31, 36, 72, 85, 47),
              (39, 95, 60, 66, 42),
              (40, 80, 74, 71, 53)],
        'degree': 100},
 'm12': {'c': [(1, 4),
               (2, 17),
               (3, 15),
               (5, 18),
               (6, 19),
               (7, 12),
               (8, 10),
               (9, 21),
               (11, 13),
               (14, 16),
               (20, 23),
               (22, 24)],
         'd': [(2, 18, 23), (3, 19, 14), (4, 11, 21), (5, 10, 16), (7, 22, 13), (17, 24, 20)],
         'degree': 24},
 'u42': {'c': [(2, 3), (4, 6), (5, 8), (7, 12), (9, 16), (19, 22)],
         'd': [(1, 2, 4, 7, 13, 17, 9, 5, 3),
               (6, 10, 15, 8, 14, 21, 23, 18, 11),
               (12, 19, 24, 26, 27, 25, 22, 16, 20)],
         'degree': 27}}
from collections import deque

def cycles(degree, data):
    ans = list(range(degree))
    for cyc in data:
        c = [x-1 for x in cyc]
        for i, x in enumerate(c):
            ans[x] = c[(i+1) % len(c)]
    return bytes(ans)

def mul(a,b):
    return bytes(a[x] for x in b)

def inv(a):
    result = bytearray(len(a))
    for i, v in enumerate(a):
        result[v] = i
    return bytes(result)

def verify(label, size, expectations, target):
    row = DATA[label]
    degree = row['degree']
    one = bytes(range(degree))
    c, d = (cycles(degree, row[key]) for key in ('c','d'))
    assert c != one and mul(c,c) == one
    generators = [d, mul(c,mul(d,c))]
    inverse = [inv(g) for g in generators]
    group = {one}
    todo = deque([one])
    while todo:
        v = todo.popleft()
        for g in generators:
            h = mul(v,g)
            if h not in group:
                group.add(h)
                todo.append(h)
    assert len(group)==size and c not in group
    invols = {g for g in group if g != one and mul(g,g)==one}
    invols.update(mul(c,g) for g in group if mul(mul(c,g),mul(c,g))==one)
    classes = []
    while invols:
        alpha = min(invols)
        orbit = {alpha}
        todo = deque([alpha])
        while todo:
            v=todo.popleft()
            for g, gi in zip(generators,inverse):
                h=mul(gi,mul(v,g))
                if h not in orbit:
                    orbit.add(h)
                    todo.append(h)
        assert orbit <= invols
        invols.difference_update(orbit)
        classes.append((alpha,orbit,alpha in group))
    assert sorted((inside,len(orbit)) for _,orbit,inside in classes)==sorted(expectations)
    selected=[orbit for _,orbit,inside in classes if inside and len(orbit)==target]
    assert len(selected)==1
    common=selected[0]
    for alpha,orbit,inside in classes:
        assert any(mul(alpha,beta) in common for beta in orbit)
    print(label,'group',size,'involution classes',sorted((inside,len(orbit)) for _,orbit,inside in classes),'common',target,flush=True)

verify('m12',95040,[(True,396),(True,495),(False,792)],495)
verify('j2',604800,[(True,315),(True,2520),(False,1800)],315)
verify('u42',25920,[(True,45),(True,270),(False,36),(False,540)],270)
for n,a,b,r in [(95040,190080,1684,7),(604800,1209600,4636,11),(25920,51840,892,7)]:
    K = 2*r-1
    limit = max(K,24)
    f,g=[1,b],[1,b-1]
    for k in range(2,limit+1):
        f.append(b*f[-1]+(k-1)*a*f[-2])
        g.append((b-1)*g[-1]+(k-1)*a*g[-2])
    assert n%r and b*b>=a and 2*b<n
    assert all(f[k]-g[k]<n**(k-1) for k in range(3,limit+1))
    assert K*f[K-1]<n**(K-1)
    assert 50*(2*b)**24<n**24 and 52*b<=25*n
print('scalar comparisons passed')
