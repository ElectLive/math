#!/usr/bin/env python3
"""Independent GF(2) rank checks for fixed b=3 witness; Python 3.12.
Finite linear-algebra certificate, not a proof of folder exhaustiveness.
"""
import json
import sys
from collections import deque
from pathlib import Path
P=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('bruck_b3_witness.json')
D=json.loads(P.read_text()); mult=D['mul']; one=D['unit']; F=D['K']; B=D['B']; acts=D['alphaV']; zacts=D['onZ']
def rank(rows):
 p={}
 for x in rows:
  while x:
   j=x.bit_length()-1
   if j in p:x^=p[j]
   else:p[j]=x;break
 return len(p)
def act(cols,v):
 out=0
 while v:
  bit=v&-v;v^=bit;out^=cols[bit.bit_length()-1]
 return out
def symbolic_action(cols, rows):
 n=len(cols); out=[0]*n
 for i in range(n):
  for j in range(n):
   if cols[j]>>i&1:out[i]^=rows[j]
 return out
def add(a,b):return [x^y for x,y in zip(a,b)]
def table_cocycles(elems,gens,columns,n,restrict=None):
 # Each c(g) coordinate is a linear form on the independent c(generator) bits.
 syms={one:[0]*n};q=deque([one]);
 while q:
  g=q.popleft()
  for k,s in enumerate(gens):
   gs=mult[g][s]
   cs=[1<<(k*n+i) for i in range(n)]
   test=add(syms[g],symbolic_action(columns[g],cs))
   if gs not in syms:syms[gs]=test;q.append(gs)
 assert set(syms)==set(elems)
 equations=[]
 for g in elems:
  for k,s in enumerate(gens):
   cs=[1<<(k*n+i) for i in range(n)]
   equations+=add(syms[mult[g][s]],add(syms[g],symbolic_action(columns[g],cs)))
 if restrict is not None:
  for g in restrict:
   for i in range(n):
    cob=0
    for j in range(n):
     if ((columns[g][j]^(1<<j))>>i)&1:cob ^= 1<<(len(gens)*n+j)
    equations.append(syms[g][i]^cob)
 return rank(equations)
def fixed_dim(elems,columns,n):
 rows=[]
 for g in elems:
  for i in range(n):
   rows.append(sum(1<<j for j in range(n) if ((columns[g][j]^(1<<j))>>i)&1))
 return n-rank(rows)
G=list(range(120));gs=D['gen'];fg=[D['p'],D['q']]
assert set(fg)<=set(F)
# Quotient V/B, using low-bit echelon pivots.
piv={}
for b in B:
 x=b
 while x:
  i=(x&-x).bit_length()-1
  if i in piv:x^=piv[i]
  else:piv[i]=x;break
assert len(piv)==18
free=[i for i in range(30) if i not in piv];assert len(free)==12
def red(x):
 for i in sorted(piv):
  if x>>i&1:x^=piv[i]
 assert not any(x>>i&1 for i in piv)
 return sum(((x>>j)&1)<<i for i,j in enumerate(free))
quot=[]
for g in G:
 if g in F:
  assert all(red(act(acts[g],b))==0 for b in B)
  quot.append([red(acts[g][j]) for j in free])
 else: quot.append(None)
# F20 projectivity: C5 fixed-free and C4 regular Jordan blocks.
fixp=fixed_dim([D['p']],quot,12)
q=D['q']; nq=[quot[q][i]^(1<<i) for i in range(12)]
def compose(A,B):return [act(A,x) for x in B]
nq2=compose(nq,nq);nq3=compose(nq,nq2)
print('quotient dimension',len(free),'C5 fixed',fixp,'rank((1+q)^3)',rank(nq3))
assert fixp==0 and rank(nq3)==3
# H1 on F quotient, and G on V and Z.
def cohom(elems,gens,columns,n,name):
 rg=table_cocycles(elems,gens,columns,n); fixed=fixed_dim(elems,columns,n)
 z1=len(gens)*n-rg; b1=n-fixed
 print(name,'Z1',z1,'B1',b1,'H1',z1-b1,'fixed',fixed)
 return z1-b1
assert cohom(F,fg,quot,12,'H1(F,V/B)')==0
assert cohom(G,gs,zacts,8,'H1(S5,Z)')==0
assert fixed_dim(F,zacts,8)==0
fv=fixed_dim(F,acts,30);gv=fixed_dim(G,acts,30)
assert fv==2 and gv==1
assert all(act(acts[g],4)==4 and act(acts[g],63)==63 for g in F)
assert all(act(acts[g],63)==63 for g in G)
fullrank=table_cocycles(G,gs,acts,30); rest_rank=table_cocycles(G,gs,acts,30,F)
proj_dim=(len(gs)+1)*30-rest_rank-fv
cobdim=30-gv
print('H1(S5,V) Z1',60-fullrank,'B1',cobdim,'restriction kernel representatives',proj_dim)
assert proj_dim==cobdim
# Hom(V,Z) and its additional vanishing on B.
def hom_rows(use_B):
 eq=[]
 for g in gs:
  for i in range(30):
   for a in range(8):
    row=0
    for j in range(30):
     if acts[g][i]>>j&1:row ^= 1<<(8*j+a)
    for b in range(8):
     if zacts[g][b]>>a&1:row ^= 1<<(8*i+b)
    eq.append(row)
 if use_B:
  for v in B:
   for a in range(8):
    eq.append(sum(1<<(8*i+a) for i in range(30) if v>>i&1))
 return rank(eq)
r1=hom_rows(False);r2=hom_rows(True)
print('Hom(V,Z) dimension',240-r1,'vanishing B dimension',240-r2)
assert 240-r1==6 and 240-r2==2
# Exhibited top1 maps span the constrained space; top(v)=(v>>6) XOR (v>>10).
def top(v):return ((v>>6)&15)^((v>>10)&15)
for shift in (0,4):
 assert all(top(b)==0 for b in B)
 for g in gs:
  assert all((top(acts[g][i])<<shift)==act(zacts[g],top(1<<i)<<shift) for i in range(30))
assert len(gs)==2
print('all module/cohomology assertions passed')
# The concrete rank witness for the radical-factorization constraint.
def beta(x,y):
 out=0
 for i in range(30):
  if x>>i&1:
   for j in range(30):
    if y>>j&1 and i!=j:out ^= D['pol'][min(i,j)][max(i,j)]
 return out
def square(x):
 out=0
 for i in range(30):
  if x>>i&1:
   out ^= D['diag'][i]
   for j in range(i+1,30):
    if x>>j&1:out ^= D['pol'][i][j]
 return out
v=91042246; directions=[beta(v,b) for b in B];d=rank(directions);ranks=[]
for a,b in ((0,0),(1,0),(0,1),(1,1)):
 target=square(v)^(top(v) if a else 0)^((top(v)<<4) if b else 0)
 ranks.append(rank(directions+[target]))
print('radical witness base rank',d,'augmented ranks',ranks)
assert d==4 and ranks==[5,4,5,4]
# Rank of all central lifts of the fixed quotient section: 18*8+20*8 variables.
ki={g:i for i,g in enumerate(F)};nvar=304
# Carry coefficient with each low-pivot vector to recover B-coordinates.
bp={}
for i,v in enumerate(B):
 x=v;c=1<<i
 while x:
  j=(x&-x).bit_length()-1
  if j in bp:x^=bp[j][0];c^=bp[j][1]
  else:bp[j]=(x,c);break
def bcoord(x):
 c=0
 for j in sorted(bp):
  if x>>j&1:x^=bp[j][0];c^=bp[j][1]
 assert x==0
 return c
def lv(c,bit):return sum(1<<(8*i+bit) for i in range(18) if c>>i&1)
def zv(g,bit):return 1<<(144+8*ki[g]+bit)
def linear(g,vec,bit):
 out=0
 for j in range(8):
  if zacts[g][j]>>bit&1:out^=vec[j]
 return out
rows=[]
for g in F:
 for i,b in enumerate(B):
  c=bcoord(act(acts[g],b))
  for bit in range(8):rows.append(linear(g,[lv(1<<i,j) for j in range(8)],bit)^lv(c,bit))
for g in F:
 for h in F:
  gh=mult[g][h]
  v=D['H'][str(g)][0]^act(acts[g],D['H'][str(h)][0])^D['F'][g][h][0]^D['H'][str(gh)][0]
  c=bcoord(v)
  for bit in range(8):rows.append(zv(g,bit)^linear(g,[zv(h,j) for j in range(8)],bit)^zv(gh,bit)^lv(c,bit))
rows.extend(zv(one,bit) for bit in range(8))
print('central lift variables',nvar,'equations',len(rows),'rank',rank(rows),'dimension',nvar-rank(rows))
assert len(rows)==6088 and rank(rows)==288

# Exact membership and spanning of the frozen 16-vector kernel.
directions=[sum(v<<(8*i) for i,v in enumerate(dl+dz)) for dl,dz in D['Hdelta']]
assert len(directions)==16 and rank(directions)==16
assert all((row&vec).bit_count()%2==0 for row in rows for vec in directions)
assert nvar-rank(rows)==rank(directions)
assert red(4)==0
assert all(rank([beta(v,b) for b in B]+[beta(4,v)])==rank([beta(v,b) for b in B]) for v in [1<<i for i in range(30)]+[91042246])
print('frozen directions form the full 16-dimensional kernel; beta(f,v) is absorbed')
