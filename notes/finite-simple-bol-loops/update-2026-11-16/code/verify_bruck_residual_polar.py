#!/usr/bin/env python3
"""Independent group-word control for residual and polar formulas.

A finite class-two toy group and two commuting marked involutions; it is NOT
an S5 extension, a Bruck envelope, or a test of existence of the main case.
Python 3.11+; assertions enabled; standard library only; no file I/O.
"""
from itertools import product
assert __debug__

def f(v,w):return int(bool(v&1) and bool(w&2))^int(bool(v&4) and bool(w&8))
def q(v):return f(v,v)
def beta(v,w):return f(v,w)^f(w,v)
def t1(v):return (v&12)|((v&1)<<1)|((v&2)>>1)
def t2(v):return (v&3)|((v&4)<<1)|((v&8)>>1)
def a1(v):return int(bool(v&1) and bool(v&2))
def a2(v):return int(bool(v&4) and bool(v&8))
def pmul(p,q_):return (p[0]^q_[0],p[1]^q_[1]^f(p[0],q_[0]))
def pinv(p):return (p[0],p[1]^q(p[0]))
def act(g,p):
 v,z=p
 if g&1:z^=a1(v);v=t1(v)
 if g&2:z^=a2(v);v=t2(v)
 return v,z
# Elements of (P ⋊ C2²) × <τhat>; τhat is a formal central involution.
def mul(A,B):return (pmul(A[0],act(A[1],B[0])),A[1]^B[1],A[2]^B[2])
def inv(A):return (act(A[1],pinv(A[0])),A[1],A[2])
def conj(A,p):
 P=(p,0,0);return mul(mul(P,A),inv(P))
identity=((0,0),0,0)
# Check the maps really act as commuting involutory automorphisms of P.
P=list(product(range(16),range(2)))
for u,v in product(P,repeat=2):
 for g in (1,2,3):assert act(g,pmul(u,v))==pmul(act(g,u),act(g,v))
for p in P:assert act(1,act(1,p))==act(2,act(2,p))==p and act(1,act(2,p))==act(2,act(1,p))
L1=((0,0),1,1);L2=((0,0),2,1);h=((2,0),3,0)
assert mul(L1,L1)==mul(L2,L2)==identity
G0=mul(mul(L1,L2),inv(h));assert G0[1:]==(0,0)
c,z0=G0[0]
# B = span(e0,e2), whose elementary section is w(s)=(s,0).
B={0,1,4,5};assert all(q(s)==0 for s in B)
assert all(pmul((s,0),(t,0))==(s^t,0) for s,t in product(B,repeat=2))
def C(x,y):return x^t1(x)^t1(y^t2(y))
def E(t,v,w):return f(t(v),t(w))^f(v,w)
def D(t,a,v):return a(v)^q(v)^f(v,t(v))
def Dpol(t,v,w):return E(t,v,w)^beta(v,w)^f(v,t(w))^f(w,t(v))
def formula(x,y):
 u=x^t1(x);v=t1(y^t2(y));s=c^C(x,y)
 assert s in B
 return D(t1,a1,x)^D(t2,a2,y)^a1(y^t2(y))^f(u,v)^f(C(x,y),c)^z0
solutions=[(x,y) for x,y in product(range(16),repeat=2) if c^C(x,y) in B]
kernel=[(x,y) for x,y in product(range(16),repeat=2) if C(x,y) in B]
assert solutions and len(solutions)==len(kernel)==64
for x,y in solutions:
 s=c^C(x,y)
 word=mul(mul(mul(conj(L1,(x,0)),conj(L2,(y,0))),inv(h)),inv(((s,0),0,0)))
 assert word[1:]==(0,0) and word[0][0]==0
 assert word[0][1]==formula(x,y)
x0,y0=solutions[0]
for x,y in kernel:
 for x2,y2 in kernel:
  actual=formula(x0^x,y0^y)^formula(x0^x2,y0^y2)^formula(x0^x^x2,y0^y^y2)^formula(x0,y0)
  predicted=(Dpol(t1,x,x2)^Dpol(t2,y,y2)^E(t1,y^t2(y),y2^t2(y2))^
   f(x^t1(x),t1(y2^t2(y2)))^f(x2^t1(x2),t1(y^t2(y)))^f(C(x,y),C(x2,y2)))
  assert actual==predicted
print('group-word residual:',len(solutions),'solutions; polar:',len(kernel)**2,'ordered kernel pairs')
