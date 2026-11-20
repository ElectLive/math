"""Fixed-point implementation: certify all integer seed and core vertices *inward*."""
from export_native import *
from tempfile import NamedTemporaryFile
from math import gcd
def inside(P,p):
 return len(P)>=3 and all((q[0]-a[0])*(p[1]-a[1]) >= (q[1]-a[1])*(p[0]-a[0]) for a,q in zip(P,P[1:]+P[:1]))
def to_inner(P,D,sym=False):
 if len(P)<3:return ()
 centroid=tuple(sum(p[k] for p in P)/len(P) for k in [0,1]);out=[]
 for z in tuple(P)+(centroid,):
  for f in [F(1),F(99999,10**5),F(999,1000),F(99,100),F(9,10),F(0)]:
   x,y=(floor(D*(f*a+(1-f)*b)+F(1,2)) for a,b in zip(z,centroid));candidates=[(x,y),(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
   vv=[(i,j) for i,j in candidates if inside(P,(F(i,D),F(j,D)))]
   if vv:out+=vv;break
 if sym:out=[v for v in out if inside(P,(-F(v[0],D),-F(v[1],D)))];out+= [(-x,-y) for x,y in out]
 return hull(out)
def build(n,B,mode,path):
 with NamedTemporaryFile() as tmp:
  export(n,B,mode,tmp.name);tokens=iter(Path(tmp.name).read_text().split())
 assert next(tokens)=='EXACT_OWNED_INIT_V1'
 L=F(next(tokens));D,A,C=(int(next(tokens)) for _ in range(3));assert A==B and D==10**6
 def p():return (F(next(tokens)),F(next(tokens)))
 def poly():return tuple(p() for _ in range(int(next(tokens))))
 with open(path,'w') as f:
  def pp(P):print(len(P),*(c for v in P for c in v),file=f)
  print(ceil(L*D),D,A,C,file=f)
  for i in range(C):pp(to_inner(poly(),D))
  for k in range(A):
   h=F(next(tokens));hm=F(next(tokens))
   for j in range(4):
    x,y=p();m=x.denominator*y.denominator//gcd(x.denominator,y.denominator)
    print(int(m*x),int(m*y),ceil(m*hm*D),file=f)
   core=to_inner(poly(),D,True);assert len(core)>=4;pp(core)
   for j in range(C):
    P=poly();assert all((x*D).denominator==(y*D).denominator==1 for x,y in P);pp(tuple((int(x*D),int(y*D)) for x,y in P))
 assert next(tokens,None)==None
if __name__=='__main__':build(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],sys.argv[4])
