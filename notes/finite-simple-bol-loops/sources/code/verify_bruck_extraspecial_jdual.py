#!/usr/bin/env python3
"""Check stabilizer shadows in the hyperbolic J plus J* S5 module.

Standalone Python 3.11+; the six-point generators are from Nagy,
arXiv:0709.4544v1 Lemma 3.1. No files are read or written.
"""
assert __debug__, 'Assertions must be enabled.'
C6=(1,0,3,2,5,4); D6=(0,2,3,4,1,5); I6=tuple(range(6))

def compose(a,b):return tuple(a[b[i]] for i in range(len(a)))
def act(A,v):
 out=0
 for i,col in enumerate(A):
  if v>>i&1:out^=col
 return out

def mul(A,B):return tuple(act(A,x) for x in B)
def inv(A):
 n=len(A);p={}
 for i,v in enumerate(A):
  w=1<<i
  while v:
   j=v.bit_length()-1
   if j in p:v^=p[j][0];w^=p[j][1]
   else:p[j]=(v,w);break
 assert len(p)==n
 out=[]
 for i in range(n):
  v,w=1<<i,0
  while v:
   j=v.bit_length()-1;v^=p[j][0];w^=p[j][1]
  out.append(w)
 return tuple(out)
def dual(A):
 B=inv(A);return tuple(sum(((B[j]>>i)&1)<<j for j in range(len(B))) for i in range(len(B)))
def add(p,v):
 while v:
  j=v.bit_length()-1
  if j in p:v^=p[j]
  else:p[j]=v;return True
 return False
def rank(vs):
 p={}
 for v in vs:add(p,v)
 return len(p)
def nullspace(rows,n):
 p={}
 for r in rows:add(p,r)
 out=[]
 for i in range(n):
  if i in p:continue
  v=1<<i
  for j in sorted(p):
   if (p[j]&v).bit_count()&1:v|=1<<j
  assert all((r&v).bit_count()%2==0 for r in rows)
  out.append(v)
 return out
def span(B):return {act(B,i) for i in range(1<<len(B))}
def aj(v,p):
 out=0
 for i in range(5):
  if v>>i&1:out^=1<<p[i]
 return (out^63 if out&32 else out)&31
J=tuple(tuple(aj(1<<i,p) for i in range(5)) for p in (C6,D6))
Jstar=tuple(dual(a) for a in J)
V=tuple(tuple(list(J[g])+[x<<5 for x in Jstar[g]]) for g in range(2))
I=tuple(1<<i for i in range(10));seen={I6:I};queue=[I6]
for x in queue:
 for p,A in ((C6,V[0]),(D6,V[1])):
  y=compose(x,p);B=mul(seen[x],A)
  if y not in seen:seen[y]=B;queue.append(y)
  else:assert seen[y]==B
assert len(seen)==len(set(seen.values()))==120

def order(p):
 x=I6
 for n in range(1,121):
  x=compose(x,p)
  if x==I6:return n
 raise AssertionError
P=next(p for p in queue if order(p)==5)
cyclic={I6};x=I6
for _ in range(4):x=compose(x,P);cyclic.add(x)
F=[g for g in queue if compose(compose(g,P),tuple(g.index(i) for i in range(6))) in cyclic]
assert len(F)==20
Q=next(g for g in F if order(g)==4 and len({compose(power,P) for power in [I6,g,compose(g,g),compose(compose(g,g),g)]})==4)
# P normal in F and Q mod P has order 4; together they generate F.
assert {compose(a,b) for a in cyclic for b in (I6,Q,compose(Q,Q),compose(compose(Q,Q),Q))}==set(F)
pv,qv=seen[P],seen[Q]
def form(v):return ((v&31)&(v>>5)).bit_count()&1
assert all(form(act(A,v))==form(v) for A in V for v in range(1024))
fixed=span(nullspace([sum(((pv[j]^(1<<j))>>i&1)<<j for j in range(10)) for i in range(10)],10))
assert fixed=={0,4,992,996}
fixed_info=[(v,form(v),(v&31).bit_count()&1) for v in sorted(fixed) if v]
assert fixed_info==[(4,0,1),(992,0,0),(996,1,1)]
l=4
# Build S=[P,J] and its restricted P,Q matrices.
pj=tuple(pv[i]&31 for i in range(5));qj=tuple(qv[i]&31 for i in range(5));piv={}
for i in range(5):add(piv,pj[i]^(1<<i))
basis=tuple(piv.values());assert len(basis)==4

def coord(B,v):
 for i in range(1<<len(B)):
  if act(B,i)==v:return i
 raise AssertionError('outside S')
S=tuple(tuple(coord(basis,act(A,x)) for x in basis) for A in (pj,qj))
# All equivariant maps S→V are the nullspace of these P,Q equations.
rows=[]
for A,B in zip(S,(pv,qv)):
 for j in range(4):
  for i in range(10):
   row=0
   for k in range(4):
    if A[j]>>k&1:row^=1<<(10*k+i)
   for k in range(10):
    if B[k]>>i&1:row^=1<<(10*j+k)
   rows.append(row)
solutions=nullspace(rows,40);assert len(solutions)==2
hom=[tuple((v>>(10*j))&1023 for j in range(4)) for v in solutions]
# Irreducibility and distinctness validate the full three F-simple lines.
for h in hom:
 assert rank(h)==4
for i in range(1,16):
 orbit={act(S[0],i),act(S[1],i),i};todo=list(orbit)
 for x in todo:
  for A in S:
   y=act(A,x)
   if y not in orbit:orbit.add(y);todo.append(y)
 assert rank(orbit)==4
T=V[0];image={v^act(T,v) for v in range(1024)}
assert len(image)==16
Uset=set();ranks=[]
for mask in range(1,4):
 h=tuple(0 for _ in range(4))
 for i,B in enumerate(hom):
  if mask>>i&1:h=tuple(x^y for x,y in zip(h,B))
 assert rank(h)==4 and all(((x&31).bit_count()&1)==0 for x in h)
 U=span((l,)+h);assert len(U)==32 and all(form(x)==0 for x in U)
 assert all(act(A,x) in U for A in (pv,qv) for x in (l,)+h)
 assert frozenset(U) not in Uset;Uset.add(frozenset(U))
 ranks.append(len(U&image).bit_length()-1)
assert len(Uset)==3 and sorted(ranks)==[1,1,2]
print('Paired S5 order 120; F20 order 20; hyperbolic form invariant.')
print('P-fixed nonzero (vector,q,functional):',fixed_info)
print('F20 Hom dimension 2; 3 singular Wbar candidates of dimension 5.')
print('transposition rank 4; intersection dimensions:',ranks)
print('Wbar dimension 4 has no functional image; dimensions <4 violate the cited strict bound.')

# All invariant quadratic functions: 10 linear plus 45 squarefree quadratic
# coefficients. Generator invariance is a quadratic identity, determined by
# its values on basis vectors and pairwise sums.
monomials=[(i,i) for i in range(10)]+[(i,j) for i in range(10) for j in range(i+1,10)]
def monomial_values(v):
 return sum((((v>>i)&1)&((v>>j)&1))<<n for n,(i,j) in enumerate(monomials))
def evalpoly(coeff,v):return (coeff&monomial_values(v)).bit_count()&1
def polynomial_of(fn):
 coeff=0
 for i in range(10):coeff|=fn(1<<i)<<i
 for k,(i,j) in enumerate(monomials[10:],10):
  bit=fn(1<<i)^fn(1<<j)^fn((1<<i)^(1<<j))
  coeff|=bit<<k
 return coeff
samples=[1<<i for i in range(10)]+[(1<<i)^(1<<j) for i in range(10) for j in range(i+1,10)]
form_rows=[monomial_values(v)^monomial_values(act(A,v)) for A in V for v in samples]
assert rank(form_rows)==52 and len(nullspace(form_rows,55))==3

def linear_J(v):return (v&31).bit_count()&1
def q_Jstar(v):
 w=(v>>5).bit_count()
 return ((w+(w&1))//2)&1
named=[polynomial_of(fn) for fn in (linear_J,q_Jstar,form)]
assert rank(named)==3
assert all((row & co).bit_count()%2==0 for row in form_rows for co in named)
assert all(evalpoly(co,v)==fn(v) for co,fn in zip(named,(linear_J,q_Jstar,form)) for v in range(1024))

def polar_columns(coeff):
 out=[]
 for i in range(10):
  col=0
  for j in range(10):
   # XOR is essential: ei+ei=0, so the diagonal vanishes.
   val=evalpoly(coeff,1<<i)^evalpoly(coeff,1<<j)^evalpoly(coeff,(1<<i)^(1<<j))
   col|=val<<j
  assert not (col>>i&1)
  out.append(col)
 return tuple(out)

assert all(rank(polar_columns((named[0] if mask&1 else 0) ^ (named[1] if mask&2 else 0)))<10 for mask in range(4))
expected={
 (0,0):[(4,1,2),(4,2,1),(4,3,1)],
 (1,0):[(996,1,2),(996,2,1),(996,3,1)],
 (0,1):[(4,1,2),(996,1,2)],
 (1,1):[],
}
for e,d in ((0,0),(1,0),(0,1),(1,1)):
 coeff=named[2]^(named[0] if e else 0)^(named[1] if d else 0)
 assert rank(polar_columns(coeff))==10
 candidates=[]
 for line in sorted(fixed-{0}):
  if not linear_J(line) or evalpoly(coeff,line):continue
  for mask in range(1,4):
   h=tuple(0 for _ in range(4))
   for i,B in enumerate(hom):
    if mask>>i&1:h=tuple(x^y for x,y in zip(h,B))
   U=span((line,)+h)
   if all(evalpoly(coeff,v)==0 for v in U):
    candidates.append((line,mask,len(U&image).bit_length()-1))
 assert candidates==expected[e,d]
 print('form (e,d)=', (e,d), 'admissible (fixed,S-line,intersection rank):', candidates)
print('Invariant quadratic space dimension 3; exactly 4 nondegenerate forms; all surviving intersections nonzero.')

# Uniform multiplicity interface: identify the unique nonzero F-intertwiner
# into each axis, then compare their preimages of im(1+t) inside the SAME S.
# This is a module-vector certificate, not a general envelope classification.
nonzero_hom=[]
for mask in range(1,4):
 h=tuple(0 for _ in range(4))
 for i,B in enumerate(hom):
  if mask>>i&1:h=tuple(x^y for x,y in zip(h,B))
 nonzero_hom.append(h)
j_axis=[h for h in nonzero_hom if all((x>>5)==0 for x in h)]
star_axis=[h for h in nonzero_hom if all((x&31)==0 for x in h)]
assert len(j_axis)==len(star_axis)==1
assert rank(j_axis[0])==rank(star_axis[0])==4
pre_j={v for v in range(16) if act(j_axis[0],v) in image}
pre_star={v for v in range(16) if act(star_axis[0],v) in image}
common=pre_j&pre_star
assert len(pre_j)==4 and len(pre_star)==2 and len(common)==2
assert 0 in common
print('J-axis intertwiner:',j_axis[0],'; J*-axis intertwiner:',star_axis[0])
print('S preimages of transposition image: J',sorted(pre_j),
      'J*',sorted(pre_star),'intersection',sorted(common))
