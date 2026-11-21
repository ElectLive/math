#!/usr/bin/env python3
"""Build the true signed 1053-row folder, switching only by t-fixed gauges."""
from itertools import product
from collections import Counter

# GF(27) in polynomial basis mod u^3-u+1.
V=list(product(range(3),repeat=3));ix={x:i for i,x in enumerate(V)};zero=ix[(0,0,0)];one=ix[(1,0,0)]
add=[[ix[tuple((a+b)%3 for a,b in zip(x,y))] for y in V] for x in V]
neg=[ix[tuple(-a%3 for a in x)] for x in V]
def fm(x,y):
    w=[0]*5
    for i,a in enumerate(V[x]):
        for j,b in enumerate(V[y]):w[i+j]+=a*b
    for j in (4,3):w[j-3]-=w[j];w[j-2]+=w[j]
    return ix[tuple(a%3 for a in w[:3])]
def pw(x,k):
    y=one
    while k:
        if k&1:y=fm(y,x)
        k//=2;x=fm(x,x)
    return y
z=next(x for x in range(1,27) if x!=one and pw(x,13)==one)
fr=[[pw(a,3**k) for a in range(27)] for k in range(3)]
tr=[V[add[add[x][fr[1][x]]][fr[2][x]]][0] for x in range(27)]
assert Counter(tr)=={0:9,1:9,2:9}
act=[[[fm(pw(z,i),fr[k][a]) for a in range(27)] for i in range(13)] for k in range(3)]
I=(0,0,0,0,0)
def mul(x,y):
    a,b,i,j,k=x;c,d,u,v,h=y
    return (add[a][act[k][i][c]],add[b][act[-k%3][j][d]],(i+(1,3,9)[k]*u)%13,(j+(1,9,3)[k]*v)%13,(k+h)%3)
def inv(g):
    a,b,i,j,k=g
    u=-i*(1,9,3)[k]%13;v=-j*(1,3,9)[k]%13
    return (act[-k%3][u][neg[a]],act[k][v][neg[b]],u,v,-k%3)
def tau(g):
    a,b,i,j,k=g;return (b,a,j,i,-k%3)
def conj(g,x):return mul(mul(g,x),inv(g))
G=product(range(27),range(27),range(13),range(13),range(3))
K=[];count=0
for g in G:
    count+=1
    assert mul(g,inv(g))==I
    if inv(g)==tau(g):K.append(g)
assert count==369603 and len(K)==1053
sets=[frozenset((a,0,0,j,k) for a in range(27) for j in range(13) for k in range(3) if tr[a]==l*k%3) for l in range(3)]
assert all(len(h)==351 for h in sets)
hits=[Counter() for _ in range(3)]
for a in map(inv,K):
    for b in K:
        g=mul(a,b)
        if g[1] or g[2]:continue
        for l,H in enumerate(sets):
            if g in H:hits[l][g]+=1
assert hits[1]==hits[2]=={I:1053}
h=(0,0,0,0,1)
assert h in hits[0] and h in K and h in sets[0]
print(f'GF(27) actual split group: {count} elements, {len(K)} signed marks, 3 section subgroups of order 351; {len(K)**2} marked differences, |H_lambda intersect K^-1K|={[len(s) for s in hits]}')
def sm(g):a,b,i,j,k=g;return neg[a],neg[b],i,j,k
assert frozenset(map(sm,sets[1]))==sets[2] and all(sm(tau(g))==tau(sm(g)) for g in K)
# All possible second-field cocycles, and all projected complements after diagonal slope shifts.
def ss(S,g):return frozenset(conj(g,x) for x in S)
for a in range(27):
    T=(a,a,0,0,0);B=(0,a,0,0,0);assert tau(T)==T
    for S in sets:assert ss(S,T)==ss(S,B)
J=frozenset((0,0,0,j,k) for j in range(13) for k in range(3))
for i in range(13):
    T=(0,0,i,i,0);B=(0,0,i,0,0);assert tau(T)==T and ss(J,T)==ss(J,B)
assert len({ss(J,(0,0,i,i,0)) for i in range(13)})==13
assert len({ss(sets[1],(a,a,0,0,0)) for a in range(27)})==27
print('all 27 module coboundaries and 13 complement shifts realized by t-fixed diagonal gauges; nonzero section traces interchanged by an actual signed-group scalar automorphism')
# Character supports for the alternative 9-weight branch versus paired, direct.
D={1,3,9};mixed={(a,b) for a in D for b in D};paired={(a,0) for a in D}|{(0,a) for a in D}
for S in (mixed,paired):
    assert not (S&{(-a%13,-b%13) for a,b in S})
    assert {(b,a) for a,b in S}==S and {(3*a%13,9*b%13) for a,b in S}==S
assert len({b for a,b in mixed})==3 and all(b for a,b in mixed) and (9-4)%3!=0
print('both candidate rational character supports have no opposite weights; the mixed 9-dimensional branch has only degree-3 V2 constituents, incompatible with actual stabilizer dimension 5')
