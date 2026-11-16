#!/usr/bin/env python3
"""Construct a finite superset of one-M principal-module extensions.

Python 3.11+; all calculations are over F2. The 567 classes are extension
classes with fixed kernel and quotient, not module-isomorphism classes. The
optional envelope filter is conditional on a separate candidate bound and does
not classify stabilizers, sections, group extensions, or loops.
"""
import argparse
import collections

# Matrices agree with verify_s5_principal_h1_bounds.py: C,D are Nagy
# generators in the 6-point action; J is the permutation module modulo
# constants and M is its even-weight constituent. Arithmetic is over F2.
C = (1, 0, 3, 2, 5, 4)
Dp = (0, 2, 3, 4, 1, 5)

def aj(v, p):
 out = 0
 for i in range(5):
  if v >> i & 1: out ^= 1 << p[i]
 if out >> 5: out ^= 63
 return out

def am(v, p):
 out = 0
 for i in range(4):
  if v >> i & 1: out ^= (1 << p[0]) ^ (1 << p[i + 1])
 if out >> 5 & 1: out ^= 63
 return (out >> 1) & 15

def apply(matrix, v):
 out = 0
 for i, col in enumerate(matrix):
  if v >> i & 1: out ^= col
 return out

def mul(a, b):
 return tuple(apply(a, col) for col in b)

def inv(matrix):
 n = len(matrix); pivots = {}
 for i, col in enumerate(matrix):
  value, witness = col, 1 << i
  while value:
   bit = value.bit_length() - 1
   if bit in pivots:
    value ^= pivots[bit][0]; witness ^= pivots[bit][1]
   else:
    pivots[bit] = (value, witness); break
 assert len(pivots) == n
 result = []
 for i in range(n):
  value, witness = 1 << i, 0
  while value:
   bit = value.bit_length() - 1
   value ^= pivots[bit][0]; witness ^= pivots[bit][1]
  result.append(witness)
 return tuple(result)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--envelope-filter', action='store_true',
                    help='also apply candidate principal-block dimension and functional bounds')
parser.add_argument('--indecomposable', action='store_true',
                    help='test splitting off the sign-only indecomposables 1 and R')
args = parser.parse_args()

def add(B,v):
 while v:
  j=v.bit_length()-1
  if j in B:v^=B[j]
  else:B[j]=v;return True
 return False

def sign(k,a,b):
 cols=[1<<i for i in range(k)]
 for j in range(b):
  i=a+2*j;cols[i]=1<<(i+1);cols[i+1]=1<<i
 return tuple(cols)
def tensor_action(AA,QI,k,n):
 # columns indexed output coordinate times domain coordinate, A f Q^-1
 out=[]
 for i in range(k):
  for j in range(n):
   v=0
   for x in range(k):
    for y in range(n):
     if AA[i]>>x&1 and QI[y]>>j&1:v^=1<<(x*n+y)
   out.append(v)
 return tuple(out)
def nullspace(rows,n):
 piv={}
 for x in rows:add(piv,x)
 out=[]
 for j in range(n):
  if j in piv:continue
  v=1<<j
  for r in sorted(piv):
   if (piv[r]&v).bit_count()%2:v^=1<<r
  assert all((r&v).bit_count()%2==0 for r in rows)
  out.append(v)
 return out

def hom_basis(source, target):
 # Generator-equivariant maps, stored as column matrices over F2.
 ns,nt=len(source[0]),len(target[0]); rows=[]
 for a,b in zip(source,target):
  for j in range(ns):
   for i in range(nt):
    row=0
    for k in range(ns):
     if a[j]>>k&1:row^=1<<(k*nt+i)
    for k in range(nt):
     if b[k]>>i&1:row^=1<<(j*nt+k)
    rows.append(row)
 return [tuple((v>>(j*nt))&((1<<nt)-1) for j in range(ns))
         for v in nullspace(rows,ns*nt)]

def r_unit(matrix):
 assert (matrix[0]&1)==(matrix[1]>>1&1) and (matrix[0]>>1&1)==(matrix[1]&1)
 return bool(matrix[0].bit_count()&1)

assert r_unit((1,2)) and r_unit((2,1))
assert not r_unit((0,0)) and not r_unit((3,3))

def splits_sign_summand(module, size):
 # R has swap action and End(R) = F2[e]/(e^2), e=swap+I.
 action=sign(size,1 if size==1 else 0,1 if size==2 else 0)
 small=(action,action)
 for inclusion in hom_basis(small,module):
  for projection in hom_basis(module,small):
   comp=mul(projection,inclusion)
   if size==2:
    assert (comp[0]&1)==(comp[1]>>1&1) and (comp[0]>>1&1)==(comp[1]&1)
   if r_unit(comp) if size==2 else (comp[0]&1):return True
 return False

def coh(qc,qd,a,b):
 n=len(qc);k=a+2*b;dim=k*n
 if dim==0:return [0],0
 A=sign(k,a,b);hc=tensor_action(A,inv(qc),k,n);hd=tensor_action(A,inv(qd),k,n)
 QI=tuple(1<<i for i in range(n)); AI=tuple(1<<i for i in range(k));HI=tuple(1<<i for i in range(dim))
 # Cayley graph indexed by (Q_g,A_g), with associated action on Hom and derivation coefficient columns.
 ident=(QI,AI); seen={ident:(HI,(0,)*(2*dim))};queue=[ident];rows=[]
 for pair in queue:
  hg,f=seen[pair]
  for j,(qq,aa,hh) in enumerate(((qc,A,hc),(qd,A,hd))):
   target=(mul(pair[0],qq),mul(pair[1],aa))
   hhnew=mul(hg,hh)
   vals=tuple(f[i]^(hg[i-j*dim] if j*dim<=i<(j+1)*dim else 0) for i in range(2*dim))
   if target not in seen:seen[target]=(hhnew,vals);queue.append(target)
   else:
    assert hhnew==seen[target][0]
    diffs=[x^y for x,y in zip(vals,seen[target][1])]
    rows += [sum(((v>>bit)&1)<<i for i,v in enumerate(diffs)) for bit in range(dim)]
 assert len(seen)==120
 Z=nullspace(rows,2*dim);B={}
 for i in range(dim):
  v=(hc[i]^(1<<i))|((hd[i]^(1<<i))<<dim)
  assert all((row&v).bit_count()%2==0 for row in rows)
  add(B,v)
 reps=[]
 for v in Z:
  if add(B,v):reps.append(v)
 classes=[]
 for mask in range(1<<len(reps)):
  v=0
  for j,r in enumerate(reps):
   if mask>>j&1:v^=r
  classes.append(v)
 return classes,dim

def block(q,a,b,f):
 n=len(q);k=a+2*b;A=sign(k,a,b);cols=list(A)
 for j in range(n):
  y=apply(q,1<<j);z=0
  for i in range(k):
   if (f>>(i*n) & ((1<<n)-1) & y).bit_count()%2:z^=1<<i
  cols.append(z|(y<<k))
 return tuple(cols)
def power(A,n):
 z=tuple(1<<i for i in range(len(A)))
 for _ in range(n):z=mul(z,A)
 return z

def getq(name):
 if name=='M':return tuple(am(1<<i,C) for i in range(4)),tuple(am(1<<i,Dp) for i in range(4))
 if name=='J':return tuple(aj(1<<i,C) for i in range(5)),tuple(aj(1<<i,Dp) for i in range(5))
 return tuple([aj(1<<i,C) for i in range(5)]+[32^21]),tuple([aj(1<<i,Dp) for i in range(5)]+[32^1])
counts=collections.Counter(); total=0; tails=0; histogram=collections.Counter()
indecomp=collections.Counter(); indecomp_tails=0; labels=[]
for name,amax in [('M',1),('J',2),('V6',1)]:
 qc,qd=getq(name)
 for a in range(amax+1):
  for b in range(3):
   classes,k=coh(qc,qd,a,b)
   exp=(a*(2 if name=='J' else 1)+2*b);assert len(classes)==1<<exp
   for index,f in enumerate(classes):
    f1=f & ((1<<k)-1);f2=f>>k
    c=block(qc,a,b,f1);d=block(qd,a,b,f2); ident=tuple(1<<i for i in range(len(c)))
    comm=mul(mul(mul(inv(c),inv(d)),c),d)
    assert power(c,2)==power(d,4)==power(mul(c,d),5)==power(comm,3)==ident
    if args.indecomposable and not any(splits_sign_summand((c,d),size) for size in (1,2)):
     image={}
     for matrix in (c,d):
      for i in range(len(c)):add(image,matrix[i]^(1<<i))
     h0=len(c)-len(image); m0=len(c)-4
     indecomp[(len(c),h0)]+=1
     indecomp_tails+=sum(1 for u in range(m0+1) for v in range(m0+1) if h0+u+v<=m0)
     labels.append((name,a,b,index,f,len(c),h0))
    if args.envelope_filter:
     image={}
     for matrix in (c,d):
      for i in range(len(c)):add(image,matrix[i]^(1<<i))
     h0=len(c)-len(image); m0=len(c)-4
     choices=[(u,v) for u in range(24) for v in range(12) if h0+u+v<=m0 and len(c)+u+2*v<=19]
     tails+=len(choices);histogram[(name,len(c),h0)]+=1
   total+=len(classes);counts[name]+=len(classes)
   print(name,'a',a,'b',b,'dim',len(qc)+a+2*b,'classes',len(classes),flush=True)
print('totals',dict(counts),'all',total);assert dict(counts)=={'M':63,'J':441,'V6':63} and total==567
if args.envelope_filter:
 print('candidate tail presentations after functional + dimension filters',tails,'hist',sorted(histogram.items()))
 assert tails==6302

if args.indecomposable:
 print('indecomposable extension representatives',sum(indecomp.values()),'dimension/h0',sorted(indecomp.items()))
 print('representative labels (quotient,a,b,index,cocycle,dimension,h0)',labels)
 print('maximum principal-block bound',max(3*d-8-2*h for d,h in indecomp),'labelled tails',indecomp_tails)
 assert sum(indecomp.values())==28 and max(3*d-8-2*h for d,h in indecomp)==14 and indecomp_tails==161

