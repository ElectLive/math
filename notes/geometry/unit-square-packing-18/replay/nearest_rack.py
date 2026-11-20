"""Produce exact integer nearest-deep-mark exclusion facets on fixed endpoint angle bins."""
from fractions import Fraction as F
from math import lcm,floor
from check_stabs import uv,marks
import sys,json
def emit(o,B,f):
 S=marks(o);D=10**6;scale=F(o['erosion']); print(B,len(S),file=f)
 for k in range(B):
  angles=[]
  for k0 in [k,k+1]:
   c,s=uv(F(k0,B))
   d=lcm(c.denominator,s.denominator);x,y=int(d*c),int(d*s)
   angles.append([(x,y),(-y,x),(-x,-y),(y,-x)])
  for i,m in enumerate(S):
   bans=[]
   for j,z in enumerate(S):
    if i==j or sum((a-b)**2 for a,b in zip(z,m))>=2:continue
    for a in range(4):
     hs=[];empty=False
     for axes in angles:
      x,y=axes[a]
      for X,Y in axes:
       u,v=X-x,Y-y;b=D*(X*z[0]+Y*z[1]-x*m[0]-y*m[1])
       if u or v: hs.append((u,v,floor(b)))
       elif b<=0:empty=True
     if not empty:bans.append(hs)
   print(len(bans),file=f)
   for hs in bans:print(len(hs),*(n for h in hs for n in h),file=f)
if __name__=='__main__':
 with open(sys.argv[3],'w') as f:emit(json.load(open(sys.argv[1])),int(sys.argv[2]),f)
