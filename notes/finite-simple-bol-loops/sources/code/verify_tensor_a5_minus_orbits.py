#!/usr/bin/env python3
"""Exact F4 tensor/trace action on the 120 minus quadratic refinements.

Python 3.11+ standard library; run with assertions enabled. See
../manuscripts/sp8-a5-square-minus-action.md for the all-embedding deduction.
The module roster and simple-loop application are separate mathematical inputs.
This finite control does not construct a loop or prove those inputs.
"""
from collections import deque

def mul(a,b):
 z=0
 while b:
  if b&1:z^=a
  b>>=1;a<<=1
  if a&4:a^=7
 return z

def trace(a):return a^mul(a,a)
# F4 basis e_(i,j)*{1,w}: index 2*(2*i+j)+k
def fcoords(x):return [(x>>(2*i))&3 for i in range(4)]
def B(x,y):
 a=fcoords(x);b=fcoords(y);z=0
 for i in range(2):
  for j in range(2):z^=mul(a[2*i+j],b[2*(1-i)+(1-j)])
 return trace(z)
def q0(x):
 s=0
 for i in range(8):
  if x>>i&1:
   for j in range(i):
    if x>>j&1:s^=B(1<<i,1<<j)
 return s

def q(t,x):return q0(x)^(bin(t&x).count("1")&1)
mins=[t for t in range(256) if sum(q(t,x)==0 for x in range(256))==120]
assert len(mins)==120

def transform(x,side,c,upper):
 a=fcoords(x);o=a[:]
 if side==0:
  i,j=(0,1) if upper else (1,0)
  for k in range(2):o[2*i+k]^=mul(c,a[2*j+k])
 else:
  i,j=(0,1) if upper else (1,0)
  for k in range(2):o[2*k+i]^=mul(c,a[2*k+j])
 return sum(v<<(2*i) for i,v in enumerate(o))

def act(t,side,c,upper):
 # involutory characteristic-two generators
 tt=0
 for i in range(8):
  v=transform(1<<i,side,c,upper)
  tt|=(q(t,v)^q0(1<<i))<<i
 return tt
G=[(s,c,u) for s in range(2) for c in [1,2] for u in [0,1]]
assert all(B(x,y)==B(transform(x,*g),transform(y,*g)) for g in G for x in [1<<i for i in range(8)] for y in [1<<i for i in range(8)])
rows=[sum(B(1<<i,1<<j)<<j for j in range(8)) for i in range(8)]
rank=0
for col in range(8):
 pivot=next((j for j in range(rank,8) if rows[j]>>col&1),None)
 if pivot is None:continue
 rows[rank],rows[pivot]=rows[pivot],rows[rank]
 for j in range(8):
  if j!=rank and rows[j]>>col&1:rows[j]^=rows[rank]
 rank+=1
assert rank==8
assert all(sorted(transform(x,*g) for x in range(256))==list(range(256)) for g in G)
assert all(act(t,*g) in mins for g in G for t in mins)
left=set(mins);orbits=[]
while left:
 x=min(left);seen={x};todo=deque([x])
 while todo:
  a=todo.popleft()
  for g in G:
   z=act(a,*g)
   if z not in seen:seen.add(z);todo.append(z)
 left-=seen;orbits.append(seen)
assert sorted(map(len,orbits))==[60,60]
print('minus orbit lengths',sorted(map(len,orbits)))
print('stabilizer orders',[3600//len(o) for o in sorted(orbits,key=min)])
print('representative t',[min(o) for o in sorted(orbits,key=min)])
for orb in sorted(orbits,key=min):
 t=min(orb);ls=[]
 for side in (0,1):
  seen={t};todo=deque([t]);gens=[g for g in G if g[0]==side]
  while todo:
   a=todo.popleft()
   for g in gens:
    z=act(a,*g)
    if z not in seen:seen.add(z);todo.append(z)
  ls.append(len(seen))
 assert ls==[60,60]
 print('representative',t,'individual factor orbits',ls)
