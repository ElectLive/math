"""Exhaustive rational rectangle-union sweep on genuine angular intervals. stdlib."""
from fractions import Fraction as F
from itertools import product
import json,time,sys
def uv(t):return (1-t*t)/(1+t*t),2*t/(1+t*t)
def marks(o):
 L=F(o['cap']);d=o['scale']
 return sorted({(x if not h else L-x,y if not v else L-y) for a,b in o['orbits'] for x,y in [(F(a,d)*L,F(b,d)*L),(F(b,d)*L,F(a,d)*L)] for h,v in product(range(2),repeat=2)})
def slab(L,S,t,u,shrink):
 c,s=uv((t+u)/2)
 # True minimal coordinate wall halfwidth on [t,u] (concavity of c+s as a function of angle).
 h=min(sum(uv(t)),sum(uv(u)))/2
 b=(1-shrink)/(2*(1+u-t))
 def rot(p):x,y=p;return c*x+s*y,-s*x+c*y
 pts=sorted(rot(p) for p in S)
 P=[rot((x,y)) for x,y in [(h,h),(L-h,h),(L-h,L-h),(h,L-h)]]
 xl=min(x for x,y in P);xr=max(x for x,y in P)
 cuts=sorted({x for x,y in P}|{q for a,z in pts for q in (a-b,a+b) if xl<q<xr})
 for l,r in zip(cuts,cuts[1:]):
  ys=[y for x,y in P if l<=x<=r]
  for (x,y),(X,Y) in zip(P,P[1:]+P[:1]):
   if x==X:continue
   for w in (l,r):
    if min(x,X)<w<max(x,X):ys.append(y+(Y-y)*(w-x)/(X-x))
  assert ys
  end=min(ys);target=max(ys)
  ranges=sorted((z-b,z+b) for a,z in pts if a-b<=l and a+b>=r)
  for lo,hi in ranges:
   if lo>end:break
   end=max(end,hi)
   if end>=target:break
  if end<target:return False
 return True
def check(o):
 L=F(o['cap']);S=marks(o);eps=F(o['erosion']);assert L>2 and 0<eps<1 and len(S)==o['marks']
 # By full D4 symmetry of square and entire mark inventory, it suffices to test orientations [0,pi/4]; 5/12>tan(pi/8) since (17/12)^2>2.
 cap=F(5,12);todo=[(F(0),cap,0)];records=[];maxdep=o['depth']
 while todo:
  t,u,d=todo.pop()
  if slab(L,S,t,u,eps):records.append((t,u,d));continue
  if d>=maxdep:return {'status':'UNRESOLVED','t':str(t),'u':str(u),'passed':len(records)}
  mid=(t+u)/2;todo.extend([(mid,u,d+1),(t,mid,d+1)])
 assert sum(b-a for a,b,d in records)==cap
 return {'status':'STRICT_STABBING','marks':len(S),'rows':len(records),'max_depth':max(d for a,b,d in records),'erosion':str(eps)}
if __name__=='__main__':print(check(json.load(open(sys.argv[1]))))
