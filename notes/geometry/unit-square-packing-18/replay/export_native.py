"""Generate every trusted initialization value (no importer of supplied polygon tables).
Uses rational half-angle, supports and conservative closed lattice enclosures."""
from check_stabs import marks,uv
from check_wall import clip as rawclip
from fractions import Fraction as F
from math import floor,ceil
from pathlib import Path
from itertools import product,combinations
import json,sys
def hull(points):
 p=sorted(set(points))
 if len(p)<3:return tuple(p)
 def chain(pp):
  h=[]
  for x,y in pp:
   while len(h)>1:
    (a,b),(c,d)=h[-2:]
    if (c-a)*(y-b)>(d-b)*(x-a):break
    h.pop()
   h.append((x,y))
  return h[:-1]
 return tuple(chain(p)+chain(reversed(p)))
def clip(P,n,d):return hull(rawclip(P,*n,d))
def rect(a,b):return hull(product([a,b],repeat=2))
def dot(n,p):return n[0]*p[0]+n[1]*p[1]
def dist(p,q):return sum((a-b)**2 for a,b in zip(p,q))
def export(n,B,mode,path):
 assert n in(11,17) and 4<=B<=256 and mode in ('rack','center')
 o=json.load(open(f'stabs{n}.json'));L=F(o['cap']);scale=10**6;D=L-1
 if mode=='rack':
  S=marks(o);r=F(o['erosion'])/4;P=[rect(F(1,2),L-F(1,2))]*len(S);radii=[r]*len(S)
 else:
  s=[tuple(map(F,p)) for p in json.load(open(f'center{n}.json'))['sites']];S=[tuple(F(1,2)+D*v for v in p) for p in s];P=[];radii=[]
  for i,(x,y) in enumerate(s):
   pp=rect(F(0),F(1))
   for a,b in s:pp=clip(pp,(2*(a-x),2*(b-y)),a*a+b*b-x*x-y*y)
   pp=hull((F(1,2)+D*u,F(1,2)+D*v) for u,v in pp)
   assert max(dist(v,w) for v,w in combinations(pp,2))<1
   span=max(dist(S[i],v) for v in pp);lo=0;hi=2**19
   while hi>lo+1:
    mid=(lo+hi)//2
    if span<(F(1,2)-F(mid,2**20))**2:lo=mid
    else:hi=mid
   r=F(lo,2**20);radii.append(r);P.append(pp)
 K=[hull(((x+r,y),(x-r,y),(x,y+r),(x,y-r))) if r else () for (x,y),r in zip(S,radii)]
 with open(path,'w') as f:
  def emit(*a):print(*a,file=f)
  def poly(pp):
   emit(len(pp))
   for v in pp:emit(*v)
  emit('EXACT_OWNED_INIT_V1');emit(L,scale,B,len(P))
  for pp in K:poly(pp)
  for k in range(B):
   c,s=uv(F(2*k+1,2*B));axes=[(c,s),(-s,c),(-c,-s),(s,-c)];ends=list(map(uv,[F(k,B),F(k+1,B)]))
   assert all(c*C+s*S>=abs(s*C-c*S) and c*C+s*S>0 for C,S in ends)
   rm=max(c*C+s*S+abs(s*C-c*S) for C,S in ends);h=min(C+S for C,S in ends)/2;rr=(1-F(1,10**7))/2
   core=hull([(rr*(i*c-j*s)/rm,rr*(i*s+j*c)/rm) for i,j in product((-1,1),repeat=2)]+[(rr*a,rr*b) for a,b in axes])
   emit(h,rm/2)
   for v in axes:emit(*v)
   poly(core)
   for pp,own in zip(P,K):
    for axis,z in [((1,0),L-h),((0,1),L-h),((-1,0),-h),((0,-1),-h)]:pp=clip(pp,axis,z)
    for v in axes:
     if own:pp=clip(pp,v,rm/2+min(dot(v,x) for x in own))
    out=hull((F(i,scale),F(j,scale)) for x,y in pp for i in [floor(x*scale),ceil(x*scale)] for j in [floor(y*scale),ceil(y*scale)])
    poly(out)
if __name__=='__main__':export(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],sys.argv[4])
