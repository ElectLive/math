#!/usr/bin/env python3
"""E6 Cartan/Weyl arithmetic; no finite-group or class assertions."""
from collections import deque
n=6
edges={(0,2),(2,3),(3,4),(4,5),(1,3)}
C=[[2*int(i==j)-int((i,j) in edges or (j,i) in edges)
    for j in range(n)] for i in range(n)]
def root(i):return tuple(int(j==i-1) for j in range(n))
def reflect(v,i):
    j=i-1; a=sum(C[j][k]*v[k] for k in range(n));w=list(v);w[j]-=a;return tuple(w)
def inner(v,w):return sum(v[i]*C[i][j]*w[j] for i in range(n) for j in range(n))
def add(v,w):return tuple(a+b for a,b in zip(v,w))
def neg(v):return tuple(-a for a in v)
def swap(v):return (v[5],v[1],v[4],v[3],v[2],v[0])
roots={tuple(sign*x for x in root(i)) for i in range(1,7) for sign in (-1,1)}
todo=deque(roots)
while todo:
    r=todo.popleft()
    for i in range(1,7):
        x=reflect(r,i)
        if x not in roots:roots.add(x);todo.append(x)
assert len(roots)==72
simple=[root(i) for i in range(1,7)]
theta=(1,2,2,3,2,1)
delta=tuple(theta[i]-simple[1][i] for i in range(n))
assert theta in roots and delta in roots
assert sum(theta)==max(map(sum,roots))
for end in (simple[0],simple[5]):
    for r in (theta,neg(simple[1])):
        assert inner(r,end)==0
        assert add(r,end) not in roots and add(r,neg(end)) not in roots
assert tuple(theta[i]-2*simple[1][i] for i in range(n)) not in roots
assert swap(theta)==theta and swap(delta)==delta
assert swap(simple[0])==simple[5] and swap(simple[1])==simple[1]
assert inner(theta,simple[1])==1
triple=[delta,simple[0],simple[5]]
for i,j in [(0,1),(0,2),(1,2)]:
    assert inner(triple[i],triple[j])==0
    assert add(triple[i],triple[j]) not in roots
    assert add(triple[i],neg(triple[j])) not in roots
word=(4,3,1,5,4,3,6,5,4)
for i in word:triple=[reflect(v,i) for v in triple]
assert set(triple)=={simple[1],simple[2],simple[4]}
print('PASS: E6 roots, graph involution, root string, orthogonal triple and Weyl word')
