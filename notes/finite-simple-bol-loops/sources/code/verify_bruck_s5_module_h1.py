#!/usr/bin/env python3
"""Finite cocycle calculation used in bruck-s5-dimension-five.md.

The action is the even-weight six-point module modulo its constant line.
Nagy arXiv:0709.4544v1, Lemma 3.1 supplies the c,d presentation.
Enumerate all 16^2 possible cocycle values on the two generators and check
all defining relators in the semidirect product. Independent review of the
presentation/action identification is required for the mathematical conclusion.
"""
from itertools import product
c=[1,0,3,2,5,4];d=[0,2,3,4,1,5]
def act(v,p):
    bits=0
    for i in range(4):
      if v>>i&1: bits^=(1<<p[0])^(1<<p[i+1])
    if bits>>5&1: bits^=63
    return (bits>>1)&15
def mul(a,b):
 p,x=a;q,y=b
 return ([q[p[i]] for i in range(6)],act(x,q)^y)
def inv(a):
 p,x=a;q=[p.index(i) for i in range(6)]
 return q,act(x,q)
def power(a,n):
 out=(list(range(6)),0)
 for i in range(n):out=mul(out,a)
 return out
z=(list(range(6)),0)
sol=[]
for x,y in product(range(16),repeat=2):
 C=(c,x);D=(d,y);comm=mul(mul(mul(inv(C),inv(D)),C),D)
 if power(C,2)==z and power(D,4)==z and power(mul(C,D),5)==z and power(comm,3)==z:sol.append((x,y))
inner={(act(v,c)^v,act(v,d)^v) for v in range(16)}
assert inner <= set(sol)
assert len(sol) == 32 and len(inner) == 16
print('Z1=32, B1=16, H1 dimension=1')
