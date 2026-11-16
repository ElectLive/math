#!/usr/bin/env python3
"""Classify the reviewed one-M extension cover by exact intertwiner enumeration."""
import contextlib,io,runpy,sys,collections
from pathlib import Path
p=Path(__file__).with_name('enumerate_bruck_s5_principal_modules.py')
old_argv=sys.argv
try:
 sys.argv=[str(p)]
 with contextlib.redirect_stdout(io.StringIO()): d=runpy.run_path(str(p))
finally:
 sys.argv=old_argv
coh,block,getq,split,hom,add,mul,r_unit=(d[k] for k in ('coh','block','getq','splits_sign_summand','hom_basis','add','mul','r_unit'))
assert r_unit((1,2)) and r_unit((2,1))
assert not r_unit((0,0)) and not r_unit((3,3))
def rank(cols):
 piv={}
 for c in cols:add(piv,c)
 return len(piv)
def invertible_combination(basis,n):
 if not basis:return None
 value=[0]*n; previous=0
 for t in range(1,1<<len(basis)):
  gray=t^(t>>1);changed=(gray^previous).bit_length()-1; previous=gray
  value=[x^y for x,y in zip(value,basis[changed])]
  if rank(value)==n:return tuple(value)
 return None
xs=[]
for name,amax in [('M',1),('J',2),('V6',1)]:
 qc,qd=getq(name)
 for a in range(amax+1):
  for b in range(3):
   classes,k=coh(qc,qd,a,b)
   for index,f in enumerate(classes):
    X=(block(qc,a,b,f&((1<<k)-1)),block(qd,a,b,f>>k))
    if not any(split(X,s) for s in (1,2)):
     img={}
     for matrix in X:
      for j in range(len(matrix)):add(img,matrix[j]^(1<<j))
     h=len(X[0])-len(img)
     xs.append(((name,a,b,index,f,len(X[0]),h),X))
clusters=[]; maxhom=0; checked=0
for label,X in xs:
 found=False
 for group in clusters:
  Y=group[0][1]
  if len(X[0])!=len(Y[0]):continue
  basis=hom(X,Y);maxhom=max(maxhom,len(basis));checked+=1
  mat=invertible_combination(basis,len(X[0]))
  if mat is not None:
   assert rank(mat)==len(X[0]) and all(mul(mat,a)==mul(b,mat) for a,b in zip(X,Y))
   group.append((label,X,mat));found=True;break
 if not found:clusters.append([(label,X,None)])
assert len(xs)==28 and len(clusters)==17 and checked==56 and maxhom==5
print('classes',len(clusters),'comparisons',checked,'maxhom',maxhom)
for j,g in enumerate(clusters):
 print('class',j,'labels',[t[0] for t in g]);print('witnesses',[t[2] for t in g[1:]])
 print('endomorphism_dim',len(hom(g[0][1],g[0][1])))
tails=sum((g[0][0][5]-4-g[0][0][6]+1)*(g[0][0][5]-4-g[0][0][6]+2)//2 for g in clusters)
assert tails==79
print('tails',tails)
print('invariants: d,h0,fixed,endomdim,Hom(M,X),Hom(J,X),Hom(V6,X),Hom(X,M),Hom(X,J),Hom(X,V6)')
probes=[clusters[i][0][1] for i in (0,4,13)]
signatures=[]
for j,g in enumerate(clusters):
 lab,X,_=g[0]; one=((1,),(1,))
 values=(lab[5],lab[6],len(hom(one,X)),len(hom(X,X)))+tuple(len(hom(P,X)) for P in probes)+tuple(len(hom(X,P)) for P in probes)
 signatures.append(values)
 print(j,values)
assert len(set(signatures))==16 and signatures[7]==signatures[8]
X=clusters[7][0][1];Y=clusters[8][0][1]
for j,g in enumerate(clusters):
 P=g[0][1]; a=(len(hom(P,X)),len(hom(X,P)));b=(len(hom(P,Y)),len(hom(Y,P)))
 if a!=b:print('distinguish 7,8 probe',j,a,b)

assert len(hom(clusters[6][0][1],X))==1 and len(hom(clusters[6][0][1],Y))==2

