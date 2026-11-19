"""Independent small true group mechanisms, not a claim to enumerate a large simple loop."""
from itertools import product
from collections import Counter
def mm(x,y):return ((x[0]+pow(2,x[1],7)*y[0])%7,(x[1]+y[1])%3)
def inv(x):return ((-pow(2,-x[1],7)*x[0])%7,(-x[1])%3)
J21=list(product(range(7),range(3)));ii=(0,0)
# D=(C7:C3 x C9) x (C7:C3), H0=last vertex stabilizer C3, B=3C9.
# It is deliberate this test uses its own faithful, tractable normalizer geometry rather than assuming it is a simple Bol folder.
D=list(product(J21,range(9),J21));I=(ii,0,ii)
def mul(a,b):return mm(a[0],b[0]),(a[1]+b[1])%9,mm(a[2],b[2])
def di(a):return inv(a[0]),(-a[1])%9,inv(a[2])
def pp(d):
 a,c,s=d;return tuple((a[0]+pow(2,a[1],7)*i)%7 for i in range(7))+tuple(7+(i+c)%9 for i in range(9))+tuple(16+(s[0]+pow(2,s[1],7)*i)%7 for i in range(7))
P={d:pp(d)for d in D};assert len(set(P.values()))==len(D)
# U over F3: 2 actual Lagrangian halves, each two slot arrays, symplectic swap pairing.
def perm(d,v):
 return {(h,j,P[d][s]):v0 for (h,j,s),v0 in v.items()}
def zz(v):
 return {q:x%3 for q,x in v.items()if x%3}
def add(a,b):return zz({q:a.get(q,0)+b.get(q,0)for q in a.keys()|b.keys()})
def neg(a):return {q:3-x for q,x in a.items()}
def omega(a,b):
 return sum(x*b.get((1-h,1-j,s),0)*(1 if j==0 else -1)for (h,j,s),x in a.items())%3
def nm(a,b):
 u,z,d=a;v,w,g=b;t=perm(d,v)
 return add(u,t),(z+w+2*omega(u,t))%3,mul(d,g)
def ni(a):
 u,z,d=a;g=di(d);return perm(g,neg(u)),(-z)%3,g
def in_j(d):return d[0]==ii and d[1]%3==0 and d[2][0]==0
def in_h(a):
 u,z,d=a;return in_j(d) and z==d[1]//3 and all(k[0]==0 for k in u)
def coupled():
 # Conjugation of true data, with every pure noncentral top tested.
 j0=(ii,0,(0,1));b=(ii,3,ii)
 H=[({},0,j0),({},1,b)]
 normd=[]
 for d in D:
  g=({},0,d);h=ni(g)
  yes=all(in_h(nm(nm(g,v),h))for v in H)
  assert yes==(d[2][0]==0)
  if yes:normd.append(d)
 assert len(normd)==567
 # Normalizing a zero-sheet L0 site tests all 46 nondegenerate directions of L1, every d.
 tests=0
 for d in normd:
  for i in range(46):
   s,j=divmod(i,2);a={(1,j,s):1};p=P[d].index(s);u={(0,1-j,p):1}
   g=(a,0,d);h=({},0,I)
   q=nm(nm(g,(u,0,I)),ni(g));assert not in_h(q) and q[1]!=0;tests+=1
  u={(0,0,P[d][0]):1,(0,1,P[d][1]):2};g=(u,2,d);assert all(in_h(nm(nm(g,h),ni(g)))for h in H)
 R=list(product(J21,range(9)));normalclasses=Counter()
 for j,c in R:
  g=({},0,(j,c,ii))
  for z in range(3):
   center=({},z,I);yes=in_h(nm(ni(center),g))
   assert yes==(j==ii and c%3==0 and (z+c//3)%3==0)
   if yes:normalclasses[j,c]+=1
 assert sum(normalclasses.values())==3
 # All 35,721 actual top products, and the coset comparisons in the full semidirect group rather than modding B out inside R.
 for j,c in R:
  for k,f in R:
   g=nm(({},0,(j,c,ii)),({},0,(k,f,ii)));assert in_h(nm(ni(({},0,(mm(j,k),(c+f)%9,ii))),g))
 assert len({(j,c)for j,c in R if j==ii and c%3==0})==3
 # Negative normalizer control with a noncentral J inside C7:C3 and its literal phase graph.
 defect=0
 for x in J21:
  for y in range(7):
   a=mm(mm(x,(y,0)),inv(x))[0]
   if a!=y:defect+=1
 assert defect==84
 print('genuine coupled pure tops tested',len(D),'normalize',len(normd),'nonzero L1 conjugation certificates',tests,'native right-normalizer representatives',len(R),'protected subgroup',len(normalclasses),'failed noncentral phase equations',defect)
def plus(a,b):return tuple((i+j)%3 for i,j in zip(a,b))
def sc(k,x):return tuple(k*i%3 for i in x)
def dot(x,y):return sum(a*b for a,b in zip(x,y))%3
V=list(product(range(3),repeat=2));z=(0,0)
def subsp():
 out=[((),[z])]
 for a in [(1,0),(1,1),(1,2),(0,1)]:out.append(((a,),[sc(i,a)for i in range(3)]))
 out.append((((1,0),(0,1)),V));return out
def omega9(x,y):
 return (x[0]*y[3]-x[1]*y[2]+x[2]*y[1]-x[3]*y[0])%9
def torsion():
 n=eq=tilt=strict=0;B=(0,3,6);gap=Counter()
 # All swap-stable A in 3*(Z9)^4, all normal lifts over B0=3Z9, including genuine nontrivial sections
 # A lies in the center modulo B0, hence these are actual NORMAL subgroups (not arbitrary invariant vector spaces).
 for (bp,ap),(bm,am)in product(subsp(),repeat=2):
  for coeff in product(range(3),repeat=len(bp)):
   C=set();A=set();nonzero=False
   for v in ap:
    coef=next(i for i in product(range(3),repeat=len(bp))if tuple(sum(k*u[j]for k,u in zip(i,bp))%3 for j in range(2))==v)
    f=dot(coeff,coef);nonzero|=bool(f)
    for w in am:
     a=tuple(3*t for t in plus(v,w)+plus(v,sc(2,w)));A.add(a)
     for b in B:C.add((a,(b+f)%9))
   # Actual group law on these coordinates has zero internal carry (both vectors divisible by 3);
   # normality is checked on ambient unit vector commutators; every literal sign is checked.
   for u,q in C:
    assert (u[2:]+u[:2],q)in C
    for i in range(4):
     e=tuple(int(i==j)for j in range(4));assert ((0,)*4,omega9(u,e)) in C
   fixed=sum(u[2:]==u[:2]for u,q in C);h=sum(u[2:]==(0,0)and q==0 for u,q in C)
   bound=sum(u[2:]==(0,0)for u in A);assert fixed>bound>=h
   eq+=h==bound;strict+=h<bound;tilt+=nonzero;n+=1;gap[fixed//h]+=1
 print('all integral signed lifts over 3Z9 on the swap-stable 3-torsion strata',n,'nonzero tilt',tilt,'strict loss of stabilizer vs naive image',strict,'literal fixed/stabilizer ratios',sorted(gap.items()))
if __name__=='__main__':coupled();torsion()
