exec(open('bruck_b1_planes.py').read().split('planes=set()')[0])
import itertools
d=z['component']('P6');base=d['base'];mon=d['mon'];feat=d['feat'];rows=d['allrows']+d['extra']
def qco(co,v):
 f=feat(v);out=0
 for i in range(len(mon)):
  if f>>i&1:out^=(co>>(4*i))&15
 return out
cross=sols(d['groups']['XU0'],rows);top,=sols(d['groups']['U0'],rows)
X=next(x for x in hom(None,lambda x,p:d['baseact'](x,p[1]),base) if rank(x)==4)
hs=hom(None,lambda x,p:a['uact'](x,p[0]) if p==gens[1] else nact(x&15,p[0])|(nact(x>>4,p[0])<<4),8)
eps=lambda v:((v&15)^(v>>4))*17
Soc=tuple(eps(x) for x in next(h for h in hs if rank(eps(x) for x in h)==4));Dc=next(h for h in hs if rank(h+Soc)==8)
U=lambda x,i:x<<(base+8*i)
f=a['u1'];one=63
# graph XS+soc3, pure soc2, top2+soc1, top3; fixed plane f,1
basis=[f,one]+[X[i]^U(Soc[i],2) for i in range(4)]+[U(Soc[i],1) for i in range(4)]+[U(Dc[i],1)^U(Soc[i],0) for i in range(4)]+[U(Dc[i],2) for i in range(4)]
assert rank(basis)==18
for g in a['F']:
 def vact(v):
  out=d['baseact'](v&63,g[1])
  for i in range(3):
   u=(v>>(base+8*i))&255
   # parity of permutation determines swapped U factors
   parity=sum(g[0][i]>g[0][j] for i in range(5) for j in range(i+1,5))%2
   val=a['uact'](u,g[0]) if parity else nact(u&15,g[0])|(nact(u>>4,g[0])<<4)
   out^=U(val,i)
  return out
 assert all(rank(basis+[vact(v)])==18 for v in basis)
def values(v):
 x=v&63;u=[(v>>(base+8*i))&255 for i in range(3)]
 return (qco(top,U(u[0],0)),qco(cross[1],x|U(u[0],0))^qco(cross[0],x|U(u[1],0)))
for v in basis+[x^y for x,y in itertools.combinations(basis,2)]:assert values(v)==(0,0)
# The S5-fixed all-ones vector has nonzero, rank-one polar row.
assert all((values(one^U(u,0))[1]^values(one)[1]^values(U(u,0))[1])==((u&15)^(u>>4)) for u in range(256))
assert all((values(one^U(u,1))[1]^values(one)[1]^values(U(u,1))[1])==0 for u in range(256))
# P6_S not contained: direct rank; pure soc intersection is exactly soc2.
assert any(rank(basis+[v])>18 for v in X)
socall=[U(Soc[i],j) for j in range(3) for i in range(4)]
assert 18+12-rank(basis+socall)==4
assert any(values(U(Dc[i],0))[0]!=0 for i in range(4))
assert any(values(f^U(Dc[i],1))[0]==0 and values(f^U(Dc[i],1))[1]!=0 for i in range(4))
print('F20-stable c=1 b=3 shadow control passed; no pure P6_S; rank=18')

