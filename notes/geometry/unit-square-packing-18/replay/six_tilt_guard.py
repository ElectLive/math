"""All-seven finite neighborhoods, using the true native field data; all other 11 tiles unbounded."""
from fractions import Fraction as F
from six_tilt18 import load,Q
from wall_chord_guard import guard,vb
from pathlib import Path
def enclosure(z):
 # Fixed rational enclosure of sqrt(7), wider than machine epsilon. No rounded trig values.
 l,h=F(264575131,10**8),F(264575132,10**8);assert l*l<7<h*h
 return tuple(sorted([z.a+z.b*l,z.a+z.b*h]))
def calc(e):
 H,P,u=load();a=F(1,128);B=128;S={};lo,hi=enclosure(H)
 for i,(tilted,center) in P.items():
  n=2 if not tilted else 1
  x,X=enclosure(center[0]);y,Y=enclosure(center[1])
  # symmetric near-axis sectors modulo a quarter turn, and entire true tilted slabs
  bands=[*range(0,2),*range(126,128)] if not tilted else [26,27,28,29]
  if tilted:
   # Actual angle belongs to these intervals, certified using monotone sine.
   assert Q(vb(26,128)[1])<=u[1]<=Q(vb(30,128)[1])
  S[i]=[(x-e,X+e,y-e,Y+e,vb(k,B),vb(k+1,B))for k in bands]
 # Real cap variable: use one rational cap e.g. upper endpoint for the reflected frame,
 # padding its reflected absolute positions covers H or any smaller actual L up to |L-hi|<=e.
 # guard() uses L only to move coordinates into/out of the opposite frame; the subtraction
 # cancels exactly on the moving corner pair. Verify via two exact reflection extrema instead.
 ids=[2,4,1,18,13,5,11]
 return window(S,lo-e,hi+e,ids)
def window(S,l,h,ids):
 # Work with nominal h. True p,q are absolute corners: replace only reflected stack pose
 # bounds by union of every possible L-shift in [l,h]. Double-inflate their original boxes,
 # covering both the true reflected coordinates [l−y,h−y] and true recovered Q in absolute
 # coordinates. (Line differences transferred back through h may now err with either sign.)
 pad=h-l;E={i:[(x-pad,X+pad,y-pad,Y+pad,A,B)for x,X,y,Y,A,B in S[i]] if i in ids[3:5] else S[i] for i in S}
 return guard(E,h,ids)
if __name__=='__main__':
 for d in (128,64,40,24,22):
  yes,diag=calc(F(1,d));print('radius',1,d,yes,diag)
 assert calc(F(1,24))[0] and not calc(F(1,22))[0]
