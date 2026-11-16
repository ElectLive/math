#!/usr/bin/env python3
"""Exact F20 complement and transposition-fixed-space controls on U."""
from itertools import combinations
assert __debug__

def rank(vectors):
    pivots = {}
    for v in vectors:
        while v:
            i = v.bit_length()-1
            if i in pivots: v ^= pivots[i]
            else:
                pivots[i] = v
                break
    return len(pivots)

def natural(v,p):
    out=0
    for i in range(4):
        if v>>i&1: out ^= (1<<p[0])^(1<<p[i+1])
    return (out>>1)&15

def parity(p):
    return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2

def action(v,p):
    x,y=v&15,v>>4
    if parity(p): x,y=y,x
    return natural(x,p)|(natural(y,p)<<4)

def compose(p,q): return tuple(p[q[i]] for i in range(5))

p=(1,2,3,4,0)
g=(0,2,4,1,3)
group={tuple(range(5))}; queue=list(group)
for x in queue:
    for gen in (p,g):
        z=compose(x,gen)
        if z not in group: group.add(z); queue.append(z)
assert len(group)==20
soc=[17,34,68,136]
# These are a computed F-complement and its translate by the socle map.
D=[186,206,55,213]
D2=[D[i]^soc[i] for i in range(4)]
assert rank(D+soc)==rank(D2+soc)==8
for basis in (D,D2):
    for h in (p,g):
        assert rank(basis+[action(v,h) for v in basis])==4
transpositions=[]
for i,j in combinations(range(5),2):
    t=list(range(5)); t[i],t[j]=t[j],t[i];transpositions.append(tuple(t))
allfixed=[]
for t in transpositions:
    fixed=[(1<<i)^action(1<<i,t) for i in range(8)]
    assert rank(fixed)==4
    assert all(action(v,t)==v for v in fixed)
    assert all(rank(basis+fixed)==8 for basis in (D,D2))
    allfixed.extend(fixed)
assert rank(allfixed)==8
print('F20 order 20; both complements meet each transposition-fixed space trivially; fixed spaces span U')
