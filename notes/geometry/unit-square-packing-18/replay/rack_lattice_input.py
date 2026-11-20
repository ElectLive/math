"""Standalone exact initialization for an arbitrary rack JSON, independent of the number of packed squares."""
from export_lattice import F,uv,marks,rect,hull,clip,product,dot,to_inner,gcd,ceil,floor
def build_rack(o,B,path):
 L=F(o['cap']);D=10**6;S=marks(o);assert 2<=L<=10 and 4<=B<=256 and 0<F(o['erosion'])<1
 r=F(o['erosion'])/4;K=[hull(((x+r,y),(x-r,y),(x,y+r),(x,y-r))) for x,y in S]
 def pp(f,P):print(len(P),*(w for v in P for w in v),file=f)
 with open(path,'w') as f:
  print(ceil(L*D),D,B,len(S),file=f)
  for own in K:pp(f,to_inner(own,D))
  for k in range(B):
   c,s=uv(F(2*k+1,2*B));axes=[(c,s),(-s,c),(-c,-s),(s,-c)];ends=[uv(F(k,B)),uv(F(k+1,B))]
   assert all(c*C+s*T>=abs(s*C-c*T) and c*C+s*T>0 for C,T in ends)
   rm=max(c*C+s*T+abs(s*C-c*T) for C,T in ends);h=min(C+T for C,T in ends)/2;rr=(1-F(1,10**7))/2
   for x,y in axes:
    m=x.denominator*y.denominator//gcd(x.denominator,y.denominator);print(int(m*x),int(m*y),ceil(m*rm*D/2),file=f)
   core=hull([(rr*(i*c-j*s)/rm,rr*(i*s+j*c)/rm) for i,j in product((-1,1),repeat=2)]+[(rr*a,rr*b) for a,b in axes])
   pp(f,to_inner(core,D,True))
   for own in K:
    P=rect(h,L-h)
    for n in axes:P=clip(P,n,rm/2+min(dot(n,x) for x in own))
    pp(f,hull((i,j) for x,y in P for i in (floor(x*D),ceil(x*D)) for j in (floor(y*D),ceil(y*D))))
