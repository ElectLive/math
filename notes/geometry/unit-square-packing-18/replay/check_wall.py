"""Independent standard-library certificate consumer. No external geometric inputs."""
from fractions import Fraction as F
from itertools import product,combinations
from math import comb
import json,sys
def clip(P,a,b,c):
 if not P:return []
 out=[]
 for p,q in zip(P,P[1:]+P[:1]):
  u=a*p[0]+b*p[1]-c;v=a*q[0]+b*q[1]-c
  if u<=0:out.append(p)
  if (u<0<v) or (v<0<u):
   f=u/(u-v);out.append((p[0]+f*(q[0]-p[0]),p[1]+f*(q[1]-p[1])))
 return out
def census(perms,k):
 n=len(perms[0]);total=0;parts=[]
 for perm in perms:
  assert sorted(perm)==list(range(n))
  coeff=[1]+[0]*k;seen=set()
  for start in range(n):
   if start in seen:continue
   v=start;l=0
   while v not in seen:seen.add(v);l+=1;v=perm[v]
   for j in range(k,l-1,-1):coeff[j]+=coeff[j-l]
  total+=coeff[k];parts.append(coeff[k])
 assert total%len(perms)==0
 return parts,total//len(perms)
def check(o,k=17):
 cap,t,g=map(F,[o['cap'],o['strip'],o['sinmax']]);D=cap-1
 assert D>0 and 0<t<F(1,2) and 0<=g<=1
 W=1+2*t*D;assert W**2<2 and (2*g>=W or (W-2*g)**2<=2-W**2)
 S=sorted(set((x if sx==0 else 1-x,y if sy==0 else 1-y) for X,Y in o['seeds'] for x,y in [(F(X,o['seed_scale']),F(Y,o['seed_scale']))] for sx,sy in product(range(2),repeat=2)))
 assert all(0<=u<=1 for p in S for u in p)
 square=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
 oversized=[]; maxd=0; minsep=None; maxcentral=0; ntests=0
 for i,(x,y) in enumerate(S):
  P=square
  for a,b in S:
   if (a,b)!=(x,y):P=clip(P,2*(a-x),2*(b-y),a*a+b*b-x*x-y*y)
  assert len(P)>=3
  C=P
  for a,b,c in [(-1,0,-t),(1,0,1-t),(0,-1,-t),(0,1,1-t)]:C=clip(C,a,b,c)
  diam2=lambda p,q:sum(((p[j]-q[j])*D)**2 for j in [0,1])
  interior=max((diam2(p,q) for p,q in combinations(C,2)),default=F(0))
  assert interior<1,(i,'deep');maxcentral=max(maxcentral,interior)
  md=max(diam2(p,q) for p,q in combinations(P,2));maxd=max(maxd,md)
  if md>=1:oversized.append(i)
  for p,q in combinations(P,2):
   a,b=sorted(abs((p[j]-q[j])*D) for j in [0,1]);v=b+g*a
   gap=(2-v)**2-a*a-b*b
   if md>=1:assert v<2 and gap>0,(i,'wall')
   if md>=1:minsep=gap if minsep is None else min(gap,minsep)
   ntests+=1
 perm=[[S.index((x if sx==0 else 1-x,y if sy==0 else 1-y)) for x,y in S] for sx,sy in product(range(2),repeat=2)]
 counts,classes=census(perm,k)
 return dict(cells=len(S),non_disk=len(oversized),raw=comb(len(S),k),fixed=counts,classes=classes,vertex_pairs=ntests,max_disk_squared_approx=float(maxd),max_central_squared_approx=float(maxcentral),min_wall_squared_margin_approx=float(minsep) if minsep is not None else None)
if __name__=='__main__':
 print(json.dumps(check(json.load(open(sys.argv[1])),int(sys.argv[2]) if len(sys.argv)>2 else 17),sort_keys=True))
