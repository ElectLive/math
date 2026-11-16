#!/usr/bin/env python3
"""Finite control for the extraspecial principal-projective shadow.

The paired permutations act on five points and on the six cosets of F20.
The 24-dimensional induced module is N tensor the six-point module.
Only Python's standard library is required; assertions must be enabled.
"""
assert __debug__
from functools import reduce

c5=(1,0,2,3,4);d5=(0,2,3,4,1);c6=(1,0,3,2,5,4);d6=(0,2,3,4,1,5)
def comp(a,b):return tuple(a[b[i]] for i in range(len(a)))
def porder(p):
 a=tuple(range(len(p)))
 for i in range(1,121):
  a=comp(a,p)
  if a==tuple(range(len(p))):return i
 raise AssertionError
I5,I6=tuple(range(5)),tuple(range(6));pairs={(I5,I6)};todo=[(I5,I6)]
for x,y in todo:
 for a,b in ((c5,c6),(d5,d6)):
  z=(comp(x,a),comp(y,b))
  if z not in pairs:pairs.add(z);todo.append(z)
assert len(pairs)==120
three=[g for g in todo if porder(g[0])==3];assert len(three)==20

def nact(v,p):
 z=0
 for i in range(4):
  if v>>i&1:z^=(1<<p[0])^(1<<p[i+1])
 return (z>>1)&15

def action(v,g):
 p5,p6=g; out=0
 for i in range(6):out^=nact((v>>(4*i))&15,p5)<<(4*p6[i])
 return out

def mat_apply(a,v):
 out=0
 for i,x in enumerate(a):
  if v>>i&1:out^=x
 return out

def mm(A,B):return tuple(mat_apply(A,x) for x in B)
def add(p,v):
 while v:
  i=v.bit_length()-1
  if i in p:v^=p[i]
  else:p[i]=v;return True
 return False
def rank(vec):
 p={}
 for v in vec:add(p,v)
 return len(p)
def contains(p,v):
 while v:
  i=v.bit_length()-1
  if i not in p:return False
  v^=p[i]
 return True

Z=tuple(reduce(int.__xor__,(action(1<<j,g) for g in three),0) for j in range(24))
for _ in range(5):Z=mm(Z,Z)
I=tuple(1<<i for i in range(24)); E=tuple(Z[i]^I[i] for i in range(24))
assert mm(Z,Z)==Z and mm(E,E)==E and all(x==0 for x in mm(E,Z))
assert rank(Z)==8 and rank(E)==16
C=tuple(action(1<<i,(c5,c6)) for i in range(24));D=tuple(action(1<<i,(d5,d6)) for i in range(24))
assert mm(C,E)==mm(E,C) and mm(D,E)==mm(E,D)
P={}
for e in E:add(P,e^mat_apply(C,e))
assert len(P) == 8
# Express principal block and all F20-simple submodules in independent coordinates.
pbas={}
for x in E:add(pbas,x)
basis=tuple(pbas.values());assert len(basis)==16

def coord(v):
 for mask in range(1<<16):
  if mat_apply(basis,mask)==v:return mask
 raise ValueError

def powers(p,n):
 out=tuple(range(len(p)))
 for _ in range(n):out=comp(out,p)
 return out
p=next(g for g in todo if porder(g[0])==5)
cyclic={powers(p[0],i) for i in range(5)}
def pinv(x):return tuple(x.index(i) for i in range(len(x)))
F=[g for g in todo if comp(comp(g[0],p[0]),pinv(g[0])) in cyclic];assert len(F)==20
fixed_cosets=[i for i in range(6) if all(g[1][i]==i for g in F)]
assert len(fixed_cosets)==1
assert {g for g in todo if g[1][fixed_cosets[0]]==fixed_cosets[0]}==set(F)
assert {g[1][fixed_cosets[0]] for g in todo}==set(range(6))
q=next(g for g in F if porder(g[0])==4)
FA=[tuple(coord(action(x,g)) for x in basis) for g in (p,q)]
SA=[tuple(nact(1<<i,g[0]) for i in range(4)) for g in(p,q)]
IA=tuple(coord(x^mat_apply(C,x)) for x in basis);image={}
for x in IA:add(image,x)
rows=[]
for A,B in zip(SA,FA):
 for j in range(4):
  for i in range(16):
   row=0
   for k in range(4):
    if A[j]>>k&1:row^=1<<(16*k+i)
   for k in range(16):
    if B[k]>>i&1:row^=1<<(16*j+k)
   rows.append(row)
def null(rows,n):
 piv={}
 for x in rows:add(piv,x)
 out=[]
 for i in range(n):
  if i in piv:continue
  x=1<<i
  for j in sorted(piv):
   if (piv[j]&x).bit_count()&1:x|=1<<j
  assert all((r&x).bit_count()%2==0 for r in rows)
  out.append(x)
 return out
hom=null(rows,64);assert len(hom)==3
lines=[]
for mask in range(1,8):
 v=0
 for i,x in enumerate(hom):
  if mask>>i&1:v^=x
 cols=tuple((v>>(16*i))&65535 for i in range(4));assert rank(cols)==4
 lines.append(cols)

line_intersections = sorted(4+len(image)-rank(line+tuple(image.values())) for line in lines)
assert line_intersections == [0, 0, 0, 0, 0, 0, 2]
# Six actual F-simple lines are counterexamples to a universal displacement vector.

Pmat,Qmat=FA
fixrows=[sum(((Pmat[j]^(1<<j))>>i&1)<<j for j in range(16)) for i in range(16)]
fixed_basis=null(fixrows,16);assert len(fixed_basis)==4
# Check the class-sum action on all three simple modules directly.
# The twenty class elements sum to zero on 1; N is the even-five module.
Nsum=[]
for i in range(4):
 v=0
 for p5,p6 in three:v^=nact(1<<i,p5)
 Nsum.append(v)
assert tuple(Nsum)==(1,2,4,8)
def mact(v,p):
 out=0
 for i in range(4):
  if v>>i&1:out^=(1<<p[0])^(1<<p[i+1])
 if out&32:out^=63
 return (out>>1)&15
Msum=[]
for i in range(4):
 v=0
 for p5,p6 in three:v^=mact(1<<i,p6)
 Msum.append(v)
assert Msum==[0]*4

fixed=fixed_basis
A=[tuple(coord(action(x,g)) for x in basis) for g in ((c5,c6),(d5,d6))]
def apply(A,v):
 out=0
 for i,x in enumerate(A):
  if v>>i&1:out^=x
 return out
n=16;mon=[(i,i) for i in range(n)]+[(i,j) for i in range(n) for j in range(i+1,n)]
def mons(v):return sum((((v>>i)&1)&((v>>j)&1))<<k for k,(i,j) in enumerate(mon))
samples=[1<<i for i in range(n)]+[(1<<i)^(1<<j) for i in range(n) for j in range(i+1,n)]
rows=[mons(v)^mons(apply(g,v)) for g in A for v in samples]
forms=null(rows,len(mon));assert len(forms)==3 and rank(rows)==133 and len(mon)==136
def q(co,v):return (co&mons(v)).bit_count()&1
def polar(co,x,y):return q(co,x)^q(co,y)^q(co,x^y)
def polarcols(co):return tuple(sum(polar(co,1<<i,1<<j)<<j for j in range(n)) for i in range(n))
def rankbasis(vec):
 p={}
 for v in vec:add(p,v)
 return tuple(p.values())
def issingular(co,vec):
 B=rankbasis(vec)
 return all(q(co,x)==0 for x in B) and all(polar(co,x,y)==0 for x in B for y in B)
planes={}
for i in range(7):
 for j in range(i+1,7):
  B=rankbasis(lines[i]+lines[j]);assert len(B)==8
  S=frozenset(apply(B,k) for k in range(256));planes[S]=B
assert len(planes)==7
nondeg=[]
for mask in range(1<<len(forms)):
 co=0
 for i,f in enumerate(forms):
  if mask>>i&1:co^=f
 pc=polarcols(co);r=rank(pc)
 if r!=16:continue
 assert all(not(pc[i]>>i&1) for i in range(16))
 rf=rank([sum(polar(co,x,y)<<j for j,y in enumerate(fixed)) for x in fixed])
 valid=[]; plane_polar=[]
 for B in planes.values():
  plane_polar.append(rank([sum(polar(co,x,y)<<j for j,y in enumerate(B)) for x in B]))
  if issingular(co,B):valid.append(8+len(image)-rank(B+tuple(image.values())))
 nondeg.append((mask,rf,issingular(co,tuple(image.values())),sorted(plane_polar),sorted(valid)))
assert len(nondeg) == 4
assert all(x[1] == 4 and x[3] == [4,4,4,8,8,8,8] and x[4] == [] for x in nondeg)
assert sum(x[2] for x in nondeg) == 2
print('S5 order 120; projector ranks 16 and 8; transposition rank 8')
print('F-simple lines: displacement intersection dimensions', line_intersections)
print('Invariant quadratics: dimension 3; nondegenerate forms: 4')
print('Each nondegenerate form: fixed polar rank 4; seven plane polar ranks 4,4,4,8,8,8,8')
print('Totally singular F-stable 8-planes: 0; q vanishes on transposition image for 2 forms')
