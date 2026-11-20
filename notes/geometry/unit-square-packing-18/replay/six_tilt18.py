"""Independent exact SAT for the six-tilt 18-site reconstruction, not a lower bound by itself."""
from fractions import Fraction as F
from dataclasses import dataclass
from functools import total_ordering
from itertools import combinations
from pathlib import Path
import json
@total_ordering
@dataclass(frozen=True)
class Q:
 a:F=F(0);b:F=F(0)
 def __add__(s,t):
  t=q(t);return Q(s.a+t.a,s.b+t.b)
 __radd__=__add__
 def __neg__(s):return Q(-s.a,-s.b)
 def __sub__(s,t):return s+-q(t)
 def __rsub__(s,t):return q(t)+-s
 def __mul__(s,t):
  t=q(t);return Q(s.a*t.a+7*s.b*t.b,s.b*t.a+t.b*s.a)
 __rmul__=__mul__
 def __lt__(s,t):
  v=s-t;a,b=v.a,v.b
  if a*b>=0:return a+b<0
  return (a<0)==(a*a>7*b*b)
 def __abs__(s):return -s if s<q(0) else s
def q(x):return x if isinstance(x,Q)else Q(F(x))
def dot(x,y):return x[0]*y[0]+x[1]*y[1]
def sub(x,y):return x[0]-y[0],x[1]-y[1]
def load():
 o=json.loads(Path(__file__).with_name('six-tilt18.json').read_text());P={i:(t,tuple(Q(F(a),F(b))for a,b in (x,y)))for i,t,x,y in o['centers']};H=Q(*[F(z)for z in o['side']]);assert H==Q(F(7,2),F(1,2)) and len(P)==18 and sum(t for t,p in P.values())==6
 u=Q(F(1,4),F(1,4)),Q(F(-1,4),F(1,4));V=[((q(1),q(0)),(q(0),q(1))),(u,(-u[1],u[0]))]
 def rad(t,d):return (abs(dot(V[t][0],d))+abs(dot(V[t][1],d)))*F(1,2)
 for t,p in P.values():
  for d in V[0]:assert rad(t,d)<=dot(d,p)<=H-rad(t,d)
 for (t,p),(s,r) in combinations(P.values(),2):assert any(abs(dot(d,sub(p,r)))>=rad(t,d)+rad(s,d)for d in V[t]+V[s])
 return H,P,u
if __name__=='__main__':load();print('PASS sqrt(7) witness: 18 tiles, 6 tilted (rather than 8), 72 walls, 153 genuine pairs.')
