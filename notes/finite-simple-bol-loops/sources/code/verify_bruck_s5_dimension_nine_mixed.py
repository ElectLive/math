#!/usr/bin/env python3
"""Involution classes in split N+(M+1) and N+J* S5 extensions.

The class calculation is independent of the choice of the F20 graph W.
The related cohomology and loop reductions are documented in the manuscript.
"""
from itertools import combinations

C6 = (1, 0, 3, 2, 5, 4)
D6 = (0, 2, 3, 4, 1, 5)
C5 = (1, 0, 2, 3, 4)
D5 = (0, 2, 3, 4, 1)
I6, I5 = tuple(range(6)), tuple(range(5))


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def n_action(v, p):
    out = 0
    for i in range(4):
        if v >> i & 1:
            out ^= (1 << p[0]) ^ (1 << p[i + 1])
    return (out >> 1) & 15


def e_action(v, p, kind):
    if kind == 'split':
        out = 0
        for i in range(4):
            if v >> i & 1:
                out ^= (1 << p[0]) ^ (1 << p[i + 1])
        if out >> 5 & 1:
            out ^= 63
        return ((out >> 1) & 15) | (v & 16)
    out = 0
    for i in range(5):
        if v >> i & 1:
            out ^= (1 << p[i]) ^ (1 << p[5])
    return out & 31


paired = {(I6, I5)}
queue = [(I6, I5)]
for a, b in queue:
    for x, y in ((C6, C5), (D6, D5)):
        element = (compose(a, x), compose(b, y))
        if element not in paired:
            paired.add(element)
            queue.append(element)
assert len(paired) == 120 and len({a for a, _ in paired}) == 120
natural = dict(paired)
transpositions = {compose(compose(g, C6), inverse(g)) for g in natural}
assert len(transpositions) == 10


def check(kind):
    def action(g, v):
        return n_action(v & 15, natural[g]) | (e_action(v >> 4, g, kind) << 4)

    def multiply(a, b):
        g, v = a
        h, w = b
        return compose(g, h), v ^ action(g, w)

    def group_inverse(a):
        g, v = a
        h = inverse(g)
        return h, action(h, v)

    def conjugate(a, b):
        return multiply(multiply(a, b), group_inverse(a))

    remaining = {(g, v) for g in transpositions for v in range(512)
                 if action(g, v) == v}
    assert len(remaining) == 640
    generators = [(C6, 0), (D6, 0)] + [(I6, 1 << j) for j in range(9)]
    classes = []
    while remaining:
        first = min(remaining)
        seen, pending = {first}, [first]
        for element in pending:
            for generator in generators:
                other = conjugate(generator, element)
                if other not in seen:
                    seen.add(other)
                    pending.append(other)
        assert seen <= remaining
        classes.append(seen)
        remaining -= seen
    data = sorted((len(orbit), sum(v == 0 for _, v in orbit)) for orbit in classes)
    assert data == [(80, 0), (80, 10), (240, 0), (240, 0)]
    choices = [choice for count in range(1, len(classes) + 1)
               for choice in combinations(range(len(classes)), count)
               if sum(len(classes[i]) for i in choice) == 160]
    assert len(choices) == 1
    selected = set().union(*(classes[i] for i in choices[0]))
    assert all((g, 0) in selected for g in transpositions)
    print(kind, 'class sizes and pure elements:', data,
          '160-element choices:', len(choices), 'all pure transpositions forced')


for module in ('split', 'dual'):
    check(module)
