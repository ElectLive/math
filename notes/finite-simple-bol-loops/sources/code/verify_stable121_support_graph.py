#!/usr/bin/env python3
"""Exact support-graph control; Python >=3.11, standard library only."""
from collections import Counter

p=11
r=3
powers=[pow(r,j,p) for j in range(5)]
assert len(set(powers))==5 and pow(r,5,p)==1
A=set(powers)
B={(-v)%p for v in A}
assert A.isdisjoint(B) and A|B==set(range(1,p))
inv={x:pow(x,-1,p) for x in range(1,p)}

class DSU:
    def __init__(self,n):self.parent=list(range(n))
    def find(self,x):
        while self.parent[x]!=x:
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
        return x
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x!=y:self.parent[y]=x

def build(s,d):
    # Factor coordinates are tagged ('s',a,b), ('x',x), ('y',y).
    vertex={}
    groups=[]
    def put(*coords):
        v=len(groups); groups.append(coords)
        for c in coords:
            assert c not in vertex
            vertex[c]=v
    for x in range(p):put(('s',x,0),('x',x))
    for b in sorted(A):
        for x in range(p):
            put(('s',x,b),('s',(x+s*inv[b])%p,(d*b)%p))
    for y in range(1,p):put(('y',y))
    put(('y',0))
    assert len(groups)==77 and len(vertex)==143
    return vertex,groups

def sigma(c,t,j):
    z=powers[j]; zi=pow(z,-1,p)
    if c[0]=='s':
        _,a,b=c
        return ('s',(t+z*b)%p,(zi*(a-t))%p)
    if c[0]=='x':return ('y',(zi*(c[1]-t))%p)
    return ('x',(t+z*c[1])%p)

def evaluate(vertex,t,j):
    dsu=DSU(77); fixed=[]; paircount=0
    for c in vertex:
        d=sigma(c,t,j)
        assert d in vertex and sigma(d,t,j)==c
        if c==d:fixed.append(vertex[c])
        elif c<d:dsu.union(vertex[c],vertex[d]);paircount+=1
    assert len(fixed)==11 and paircount==66
    allcomp={dsu.find(v) for v in range(77)}
    anchored={dsu.find(v) for v in fixed}
    return len(allcomp),len(anchored),len(allcomp-anchored)

hist=Counter(); candidate_hist=Counter(); survivors=[]; first=None
for s in range(p):
    for d in sorted(B):
        vertex,groups=build(s,d)
        # Verify full strips are carried to full strips by generators of U.
        def a(c):
            if c[0]=='s':return ('s',(c[1]+1)%p,c[2])
            if c[0]=='x':return ('x',(c[1]+1)%p)
            return c
        def c3(c):
            if c[0]=='s':return ('s',(r*c[1])%p,(pow(r,-1,p)*c[2])%p)
            if c[0]=='x':return ('x',(r*c[1])%p)
            return ('y',(pow(r,-1,p)*c[1])%p)
        for action in (a,c3):
            for group in groups:
                assert len({vertex[action(c)] for c in group})==1
        fail=0
        for t in range(p):
            for j in range(5):
                counts=evaluate(vertex,t,j)
                hist[counts]+=1
                if counts[2]:
                    fail+=1
                    if first is None:first=(s,d,t,j,counts)
        candidate_hist[fail]+=1
        if not fail:survivors.append((s,d))
assert sum(hist.values()) == 3025
assert all(k[2] > 0 for k in hist)
assert candidate_hist == Counter({55:55}) and not survivors
print('U-invariant strip systems:',55)
print('selected class tests:',55*55)
print('number of failed selected classes per strip system:',dict(sorted(candidate_hist.items())))
print('component/anchored/unanchored counts:',dict(sorted(hist.items())))
print('surviving strip systems:',survivors)
print('first failure (s,d,t,j,counts):',first)
