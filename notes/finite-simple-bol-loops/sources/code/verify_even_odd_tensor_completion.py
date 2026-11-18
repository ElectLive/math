"""Small quadratic-class, determinant, rank and endpoint controls; stdlib only."""
from math import prod,gcd
from itertools import product
from fractions import Fraction
def v2(z):
 a=0
 while z%2==0:z//=2;a+=1
 return a
def ordp(n,p):
 a=1
 for k in range(1,p):
  a=a*n%p
  if a==1:return k
def prime_list(n):return [i for i in range(2,n+1) if all(i%j for j in range(2,int(i**.5)+1))]
def tag_counts():
 count=0
 for q in (3,5,7,11,13,17,19,29,41,73):
  sq={x*x%q for x in range(1,q)};c=next(x for x in range(1,q) if x not in sq)
  for d in range(2,25,2):
   e=d//2;pows={pow(x,d,q) for x in range(1,q)}
   tag=pow(-c,e,q)
   assert (tag not in pows)==(q%4==1 and v2(d)<=v2(q-1))
   same=tag not in pows and any(tag*(-1)%q==z for z in pows)
   assert same==(v2(d)==v2(q-1) and v2(d)>=2)
   G=lambda n,x:x**(n*(n-1)//2)*prod(x**i-1 for i in range(1,n+1))
   single=(G(d,q)//G(e,q*q))**2//2
   formula=Fraction(q**(d*d),2)*prod((1-Fraction(1,q**i))**2 for i in range(1,d+1,2))
   assert single==formula
   # Odd prime primitive for q^4-1; actual normalized nonsplit class
   # does not consume it, while each projective factor has it.
   if d in (4,6):
    l=next((l for l in prime_list(min(3000,q**d)) if q%l and ordp(q,l)==d),None)
    if l:assert single%l and (G(d,q)//(q-1)//gcd(d,q-1))%l==0
   count+=1
 print("normalized coset and nonsplit-class order tests",count)
def block_ranks(q):
 c=next(z for z in range(1,q) if z not in {v*v%q for v in range(1,q)})
 # F_{q^2} = F_q[t]/(t^2-c); restriction-of-scalars companion matrices.
 elems=range(q*q)
 mul=lambda a,b:(a%q*(b%q)+c*(a//q)*(b//q))%q+q*((a%q*(b//q)+a//q*(b%q))%q)
 minus=lambda a,b:((a%q-b%q)%q)+q*((a//q-b//q)%q)
 norm=lambda a:((a%q)**2-c*(a//q)**2)%q
 ranks=set();dets=set();num=0
 for a,b,c0,d in product(elems,repeat=4):
  z=minus(mul(a,d),mul(b,c0))
  rank=4 if z else (2 if a or b or c0 or d else 0)
  ranks.add(rank);dets.add(norm(z));num+=1
 assert ranks=={0,2,4} and dets==set(range(q))
 # Direct F_q basis check, not only the abstract extension-field rank.
 for a,b,c0,d in ((1,0,0,q),(q,0,0,0),(q,1,1,q),(0,0,0,0)):
  def bl(z):return (z%q,c*(z//q)%q,z//q,z%q)
  x,y,z,w=map(bl,(a,b,c0,d))
  mat=(x[:2]+y[:2],x[2:]+y[2:],z[:2]+w[:2],z[2:]+w[2:])
  sz=len({tuple(sum(t*u for t,u in zip(row,v))%q for row in mat) for v in product(range(q),repeat=4)})
  det=minus(mul(a,d),mul(b,c0))
  assert sz==q**(4 if det else 2 if a or b or c0 or d else 0)
 print("quadratic intertwiner rank and determinant spectrum",q,num,sorted(ranks),sorted(dets))
def exponent_controls():
 ns=mx=0
 for d in range(4,82,2):
  D=d*(d-1)//2
  for rho in range(1,d):
   m=d-rho
   if rho>2 and not(d==4 and rho==3):
    for a in range(rho+1,d+1):
     x=d-a
     g=m*m+4*m*x-3*x*x+rho*rho-rho-2-a*(a//(rho+1))
     assert 25*3**g>36*(rho+2)**4,(d,rho,a)
     ns+=1
   if d%4 or d<8 or m%2 or m*m>2*d-1:continue
   for a in range(rho+1,d+1):
    x=d-a
    cap=2*D-rho*(2*a-rho-1)+a*(a//(rho+1)+1)+x*(x+1)
    g=d*d-2-2*min(a*(a-rho),2*d-1)-cap
    assert 25*5**g>36*((rho+2)**2+1)**2,(d,m,a)
    mx+=1
 print("split/mixed supporting inequality instances",ns,mx)
def double_units():
 for q in (3,5):
  # Both left/right matrix units enable two identical disjoint blocks:
  # the sum literally has twice the F_q rank, not merely even dimensions.
  for r in (1,3):
   a=2*r
   I=lambda k:tuple(tuple(int(i==j) for j in range(k)) for i in range(k))
   v=tuple(tuple(int(i==j and i<r) for j in range(a)) for i in range(a))
   w=tuple(tuple(int(i==j and i>=r) for j in range(a)) for i in range(a))
   assert tuple(tuple((v[i][j]+w[i][j])%q for j in range(a)) for i in range(a))==I(a)
def bruhat_graphs():
 from itertools import permutations
 count=0
 for d in range(2,7):
  perms=list(permutations(range(d)))
  gens=[(s,) for s in perms]
  if d<=4:gens.extend(product(perms,repeat=2))
  for ss in gens:
   roots={(j,i) for j in range(d) for i in range(j)}
   while True:
    more={(s[i],s[j]) for s in ss for i,j in roots}
    if more<=roots:break
    roots|=more
   while True:
    more={(i,k) for i,j in roots for v,k in roots if j==v}
    if more<=roots:break
    roots|=more
   all_roots=all((i,j) in roots for i in range(d) for j in range(d) if i!=j)
   prefix=any(all(set(s[:k])==set(range(k)) for s in ss) for k in range(1,d))
   assert all_roots!=prefix,(d,ss)
   count+=1
 print("Bruhat root-closure versus common invariant proper initial flag",count)
if __name__=='__main__':
 tag_counts();block_ranks(3);block_ranks(5);exponent_controls();double_units();bruhat_graphs()
