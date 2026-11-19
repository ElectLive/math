"""Mechanism controls for the new Heisenberg insertion, not a claim to list all
elements of the universal loop. Standard Python with NumPy for finite modules."""
from itertools import product
from math import gcd
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy
import numpy as np
rng=np.random.default_rng(28691)
# Independent quadratic-residue prime supplier: actual excluded primes including
# the former fixed characteristic 11. No Dirichlet progression black box.
def primes(n):
 a=2;out=[]
 while a*a<=n:
  if n%a==0:
   out.append(a)
   while n%a==0:n//=a
  a+=1
 if n>1:out.append(n)
 return out
for forbidden in ((3,11),(3,11,23),(3,5,11,23)):
 m=2*np.prod(forbidden).item();m=next(int(m*j) for j in range(1,8) if (m*j)**2%7==2)
 f=primes(m*m+7);ans=next(p for p in f if p%7 in (2,4))
 assert all(p%7 in (1,2,4) for p in f) and ans not in forbidden
 print('avoid',forbidden,'M',m,'prime support of M^2+7',f,'selected',ans)
# Two genuine permutational wings on zero-sum rows/columns in the nonfield Z/9.
q=7;m=9;Y=list(product(range(7),range(3)));s7=np.arange(7);I=(0,0)
def mul(x,y):return (x[0]+pow(2,x[1],7)*y[0])%7,(x[1]+y[1])%3
def inv(x):return -pow(2,-x[1],7)*x[0]%7,-x[1]%3
def perm(x):return (s7-x[0])*pow(2,-x[1],7)%7
def local():
 f=np.zeros((2,7,7),dtype=int);f[:,:6,:6]=rng.integers(9,size=(2,6,6));f[:,:6,6]=-f[:,:6,:6].sum(axis=2)%9
 f[:,6,:]=-f[:,:6,:].sum(axis=1)%9
 assert not(f.sum(axis=1)%9).any() and not(f.sum(axis=2)%9).any()
 return f
def LR(x,y,f):return f[:,perm(x)][:,:,perm(y)]
def anti(x,f):return LR(x,inv(x),f)
def beta(f,g):return int(np.sum(f[0]*g[1].T-f[1]*g[0].T)%9)
def omega(a,b):return (beta(a[0],b[1])+beta(a[1],b[0]))%9
def sig(x,U):return anti(x,U[1]),anti(inv(x),U[0])
for x,y in product(Y,repeat=2):
 f,g=local(),local();assert beta(LR(x,y,f),LR(y,x,g))==beta(f,g)
 A=(local(),local());B=(local(),local());assert omega(sig(x,A),sig(x,B))==omega(A,B)
off=0;tests=0
for x,y in product(Y,repeat=2):
 c=mul(mul(x,inv(y)),x);f,g=local(),local();v=(anti(x,f),-f%9);w=(-anti(c,f)%9,f)
 assert np.array_equal(sig(x,v)[0],-v[0]%9) and np.array_equal(sig(c,w)[1],-w[1]%9)
 assert omega(v,w)==0 and not ((v[1]+w[1])%9).any()
 v2=(-anti(c,g)%9,g);off+=omega(v,v2)!=0
 tests+=1
assert off>40
print('Physical two-wing over Z9: bilinear form and genuine symplectic signs; all',tests,'projected sign pairs have zero central carry on L0;',off,'off-L0 controls carry nonzero phase.')
# Exact target R of order 81 with Z(R)=C9 and derived 3C9 (nonsummand).
R=list(product(range(3),range(3),range(9)));e=(0,0,0)
def rm(x,y):return (x[0]+y[0])%3,(x[1]+y[1])%3,(x[2]+y[2]+3*x[0]*y[1])%9
def ri(x):return -x[0]%3,-x[1]%3,(-x[2]+3*x[0]*x[1])%9
def rp(x,n):
 z=e
 for _ in range(n):z=rm(z,x)
 return z
Z={r for r in R if all(rm(r,s)==rm(s,r) for s in R)}
B={(0,0,3*i) for i in range(3)}
RR={rm(rm(ri(r),ri(s)),rm(r,s)) for r,s in product(R,repeat=2)}
assert len(Z)==9 and RR==B and {rp(z,3) for z in Z}==B
# F=(B x R)/graph(B), computed in literal central-extension representatives.
def qmap(z,r):return rm((0,0,-3*z%9),r)
QR=list(product(range(3),R));fib={}
for z,r in QR:fib.setdefault(qmap(z,r),[]).append((z,r))
assert len(fib)==81 and all(len(x)==3 for x in fib.values())
for (z,r),(w,s) in product(QR,repeat=2):assert qmap((z+w)%3,rm(r,s))==rm(qmap(z,r),qmap(w,s))
assert {qmap(z,e) for z in range(3)}==B and len([x for x in Z if rp(x,3)==e])==3
print('True nonabelian target order 81: center C9, derived 3C9; all',len(QR)**2,'quotient products match the native R law, and central image is the nonsummand 3C9, not a chosen direct factor.')
# Check the external diagonal step over a complete honest finite Nagy folder;
# we use the canonical 1053 control only for actual K,J and the G-loop orbit,
# NOT as an instance of the arbitrary-R prime-module existence hypothesis.
depf=Path(__file__).with_name('check_nagy_1053_right_nucleus.py')
if not depf.exists():depf=Path(__file__).parent/'check_nagy_1053_right_nucleus.py'
with redirect_stdout(StringIO()):g=runpy.run_path(str(depf))
Y,K,J,invy,my,H,Yp=g['Y'],g['B'],g['A'],g['invY'],g['prodY'],g['H'],g['Yp']
nuc=[(0,0,i) for i in range(3)]
oldbar=set(product(K,J));newbar={}
for i,t in enumerate(nuc):
 for x,y in oldbar:
  point=(my(x,t),my(y,invy(t)))
  assert point not in newbar;newbar[point]=i
diag={x for x in Y if (x,x) in newbar};assert len(diag)==3
J0={p for p in newbar if (p[0][2]+p[1][2])%3==0}
assert len(J0)==3*len(H) and {x for x in J0 if not newbar[x]}==H
assert sum((x,x) in oldbar for x in Y)==1
assert len(newbar)==3159 and len(diag)*len(Y)==len(newbar)
print('Physical 1053-point Nagy base: |full previous Hbar|=1053, enlarged |Jbar|=3159, |Delta(Y) cap Jbar|=3, native |J|=',len(J0),'; |Delta(Y-prime) cap Jbar|=',len(diag&Yp),'. Not an assertion that 1053 supplies the detecting module.')
# Every signed-cut ratio in an actual central Heisenberg kernel, incl tilted
# lines, tested at small order in a symplectic swap that is NOT anti-symplectic.
p=3;vals=list(product(range(p),repeat=4))
def sw(v):return v[2:]+v[:2]
def om(v,w):return (v[0]*w[3]-v[1]*w[2]+v[2]*w[1]-v[3]*w[0])%p
def plus(v,w):return tuple((a+b)%p for a,b in zip(v,w))
def span(S,x):return frozenset(plus(a,tuple(b*i%p for b in x)) for a in S for i in range(p))
zero=(0,)*4;base=frozenset([zero]);subs={base};todo=[base]
while todo:
 V=todo.pop()
 for x in vals:
  if x in V:continue
  nV=span(V,x);nV=span(nV,sw(x))
  if nV not in subs:subs.add(nV);todo.append(nV)
for V in subs:
 l=sum(not any(v[2:]) for v in V);f=sum(sw(v)==v for v in V)
 assert f>=l and p*f>l
 if len(V)>1:assert any(om(x,y) for x in V for y in vals)
print('All',len(subs),'actual swap-invariant subspaces in F3^4: positive fixed bound vs L0 and nonzero pairing of every nontrivial image, including tilted supports.')
