"""Exact noncentral, non-Hall control for the odd-kernel core obstruction."""
from collections import deque
from itertools import permutations, product

n = 3
points = tuple(product(range(3), repeat=3))
zero = (0,0,0)
one = ((0,1,2),(1,1,1))


def add(a,b):
    return tuple((x+y)%3 for x,y in zip(a,b))


def neg(x):
    return tuple(-j%3 for j in x)


def act(g,x):
    p,s = g
    return tuple(s[i]*x[p[i]]%3 for i in range(3))


def mul(g,h):
    p,s = g
    q,t = h
    return tuple(q[p[i]] for i in range(3)),tuple(s[i]*t[p[i]]%3 for i in range(3))


D = [(one[0],s) for s in product((1,2),repeat=3) if s.count(2)%2 == 0]
perms = tuple(permutations(range(3)))
Y = {(p,s) for p in perms for _,s in D}
J = {(p,s) for p,s in Y if p in (one[0],(1,2,0),(2,0,1))}
assert len(Y) == 24 and len(J) == 12
assert {x for x in points if all(act(d,x) == x for d in D)} == {zero}
assert all(sum(act(d,x) == x for x in points) == 3 for d in D if d != one)
gen = (D[-1],((1,2,0),(1,1,1)))
principal = {tuple(add(act(g,x),neg(x)) for g in gen) for x in points}
assert len(principal) == 27


def extends(vals):
    c,todo = {one:zero},deque([one])
    while todo:
        g = todo.popleft()
        for z,v in zip(gen,vals):
            h = mul(g,z)
            w = add(c[g],act(g,v))
            if h in c and c[h] != w:
                return False
            if h not in c:
                c[h] = w
                todo.append(h)
    assert set(c) == J
    return True


found = {v for v in product(points,repeat=2) if extends(v)}
assert found == principal
# tau fixes Y and acts as minus identity on the abelian odd vector kernel.
# All involutions above the chosen projected marks are actual pure conjugates.
marks = [y for y in Y if mul(y,y) == one]
fibers = []
for y in marks:
    lifts = {x for x in points if x == act(y,x)}
    conj = {add(x,act(y,x)) for x in points}
    assert lifts == conj and zero in lifts
    fibers.append(len(lifts))
# A nonidentity 3-cycle is an odd collision of two pure transposition marks.
trans = [(p,(1,1,1)) for p in perms if p != one[0] and mul((p,one[1]),(p,one[1])) == one]
c = mul(trans[0],trans[1])
assert c in J and c != one and mul(mul(c,c),c) == one
print("S4 quotient, A4 shadow, V4 common-fixed-free with no fixed-free member:",
      len(Y),len(J),len(D))
print("All A4 derivations on the 27-vector coefficient module are principal:",len(found))
print("Actual outside involution fibers above all involutory quotient labels:", sorted(fibers))
print("Verified genuine order-three pure collision (group control, not a claimed Bol loop)")
