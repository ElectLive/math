#!/usr/bin/env python3
"""Finite UOD checks for explicit ATLAS degree-100 actions and one local action.

Inputs: ATLAS of Finite Group Representations v3.004, GAP generator files:
https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/J2d2G1-p100B0
https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/HSd2G1-p100B0
Generator byte paths, each followed by .g1 or .g2:
https://brauer.maths.qmul.ac.uk/Atlas/spor/J2/gap/J2d2G1-p100B0
https://brauer.maths.qmul.ac.uk/Atlas/spor/HS/gap/HSd2G1-p100B0
Each verbatim downloaded file and SHA-256 is embedded below; no network at runtime.
The U3(3):2 action is the restriction of the J2:2 point stabilizer to its
36-point suborbit. The identification with the classified degree-36 graph uses Brouwer--Van
Maldeghem, Strongly Regular Graphs, sections 10.14 and 10.32: the Hall--Janko
graph is locally the G2(2) graph. See the canonical C0017 proof for source
coverage; it is not established merely by the computed graph parameters.

The script uses PermGroup to compute point-stabilizer generators. It independently
enumerates their full closure and the ordered-pair orbit from the input generators.
It checks all elements mapping 0 to a selected point in each target suborbit.
Conjugacy under the point stabilizer then handles every point in the suborbit.
Results concern only these explicit permutation actions; they are not an
independent mathematical review or a classification theorem.
"""
import hashlib
import re
from collections import deque
from perm_group import PermGroup

J1 = b'b11 := (1,88)(2,22)(4,5)(6,98)(7,66)(8,24)(9,20)(10,75)(12,74)(13,39)(14,45)\n     (15,58)(16,46)(17,55)(18,96)(19,48)(21,94)(23,76)(26,42)(27,65)(29,51)\n     (30,86)(31,70)(32,71)(34,78)(35,93)(36,56)(37,87)(38,67)(40,83)(41,59)\n     (43,73)(47,100)(49,72)(50,77)(52,95)(54,84)(57,82)(61,91)(62,64)(69,81)\n     (79,97)(89,99);\n'
J1_SHA256 = '5c6a7e401315a278d32c957b7b2044a1e8f249e801dbed5ec8a0ff0295f43fa7'
J2 = b'b21 := (1,59,75,7,64)(2,84,69,93,9)(3,78,51,10,30)(4,14,20,67,8)(5,99,43,32,46)\n     (6,54,89,11,90)(12,33,21,56,35)(13,58,87,49,45)(15,18,76,94,37)(16,50,88,\n     79,27)(17,70,52,82,38)(19,91,41,73,62)(22,55,23,65,86)(24,61,29,98,63)\n     (25,81,96,83,48)(26,68,77,100,44)(28,92,97,57,34)(31,36,72,85,47)(39,95,\n     60,66,42)(40,80,74,71,53);\n'
J2_SHA256 = '200077d5cc3ce21bd60461b1bd9278d8a92ce3b80b7f5426ccbedb2aebc56cf5'
H1 = b'b11 := (1,86)(4,54)(5,30)(6,57)(8,44)(9,52)(11,14)(13,42)(18,43)(19,85)(20,65)\n     (22,91)(23,71)(24,87)(25,50)(26,78)(27,88)(29,73)(31,76)(33,84)(34,72)\n     (35,97)(36,53)(37,63)(39,47)(40,99)(45,80)(55,81)(58,79)(62,83)(66,77)\n     (67,98)(68,100)(69,93)(74,89);\n'
H1_SHA256 = '343bd1acd153425f272e7b7d223e3ff7fa9221553fad0253e4f39ad7b039620f'
H2 = b'b21 := (1,49,14,37,74)(2,16,52,96,44)(3,99,38,18,61)(5,62,64,65,95)(6,8,40,85,\n     58)(7,68,80,9,39)(10,19,31,97,72)(11,77,93,84,98)(12,46,86,78,42)(13,23,\n     54,29,15)(17,82,69,34,30)(21,28,56,88,89)(22,100,73,87,35)(24,79,67,59,\n     32)(25,43,27,66,75)(26,92,47,50,94)(33,36,57,70,81)(41,83,55,91,51)(45,\n     90,60,48,71);\n'
H2_SHA256 = 'c8656a5b1e12a5647128d6a18a3bec3b1d89b2b3f482b888e728a9bc46ab653d'

def parse(data, expected_hash, n):
    if hashlib.sha256(data).hexdigest() != expected_hash:
        raise ValueError("embedded ATLAS input hash mismatch")
    text = data.decode("ascii").split(":=", 1)[1]
    p = list(range(n))
    for cycle in re.findall(r"\(([^()]*)\)", text):
        points = [int(x) - 1 for x in cycle.split(",")]
        for x, y in zip(points, points[1:] + points[:1]):
            p[x] = y
    if sorted(p) != list(range(n)):
        raise ValueError("input is not a permutation")
    return tuple(p)


def pair_orbit(gens, seed):
    seen = {seed}
    queue = deque([seed])
    while queue:
        a, b = queue.popleft()
        for h in gens:
            pair = (h[a], h[b])
            if pair not in seen:
                seen.add(pair)
                queue.append(pair)
    return seen


def stabilizer_closure(gens, n):
    # Bytes store a permutation compactly; translate computes left composition.
    tables = [bytes(g) + bytes(range(n, 256)) for g in gens]
    identity = bytes(range(n))
    seen = {identity}
    queue = deque([identity])
    while queue:
        a = queue.popleft()
        for table in tables:
            b = a.translate(table)
            if b not in seen:
                seen.add(b)
                queue.append(b)
    return seen


def point_transversal(gens, n):
    trans = {0: tuple(range(n))}
    queue = deque([0])
    while queue:
        a = queue.popleft()
        for g in gens:
            b = g[a]
            if b not in trans:
                trans[b] = tuple(g[v] for v in trans[a])
                queue.append(b)
    if len(trans) != n:
        raise AssertionError("action is not transitive")
    return trans


def check(name, n, gens, order, expected_stabilizer, expected_counts):
    group = PermGroup(n, gens, initial_base=[0], allow_jordan_fastpath=False)
    assert group.order() == order
    stab_gens = group.stabilizer_generators(0)
    assert all(g[0] == 0 for g in stab_gens)
    stab = stabilizer_closure(stab_gens, n)
    assert len(stab) == expected_stabilizer
    assert len(stab) * n == order
    trans = point_transversal(gens, n)
    unseen = set(range(1, n))
    counts = {}
    while unseen:
        x = min(unseen)
        suborbit = {h[x] for h in stab}
        unseen.difference_update(suborbit)
        pairs = pair_orbit(gens, (0, x))
        assert len(pairs) == n * len(suborbit)
        t = trans[x]
        count = sum(all((v, t[h[v]]) in pairs for v in range(n)) for h in stab)
        assert len(suborbit) not in counts
        counts[len(suborbit)] = count
        print(f"{name}: subdegree={len(suborbit)}, orbital_size={len(pairs)}, "
              f"representative_coset_UOD={count}", flush=True)
    assert counts == expected_counts
    return group


def main():
    j = [parse(J1, J1_SHA256, 100), parse(J2, J2_SHA256, 100)]
    hs = [parse(H1, H1_SHA256, 100), parse(H2, H2_SHA256, 100)]
    jgroup = check("J2:2 degree 100", 100, j, 1209600, 12096, {36: 0, 63: 64})
    local_orbit = sorted(next(o for o in jgroup.stabilizer_orbits(0) if len(o) == 36))
    index = {point: i for i, point in enumerate(local_orbit)}
    local = [tuple(index[h[v]] for v in local_orbit)
             for h in jgroup.stabilizer_generators(0)]
    check("U3(3):2 local degree 36", 36, local, 12096, 336, {14: 4, 21: 0})
    check("HS:2 degree 100", 100, hs, 88704000, 887040, {22: 0, 77: 1920})
    print("These checks do not establish action identification or mathematical review.")


if __name__ == "__main__":
    main()
