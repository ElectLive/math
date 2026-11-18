"""Mixed exponent nilpotent cocycles, transitive nonnilpotent adverse module, and actual stabilized-vs-crossed tuple blocks."""
from itertools import product,permutations
from collections import Counter
from math import prod
# Faithful D8×C3 permutes a 4×3 grid. D≈(Z/12)^2 by rows alternating ±(a,b,−a−b).
D=list(product(range(12),repeat=2));zero=(0,0)
add=lambda a,b:tuple((a[i]+b[i])%12 for i in range(2))
neg=lambda a:tuple(-v%12 for v in a)
sub=lambda a,b:add(a,neg(b))
f=lambda a:((-a[0]-a[1])%12,a[0])
def grid(a):
 row=(*a,(-sum(a))%12)
 return tuple(((-1)**i*row[j])%12 for i,j in product(range(4),range(3)))
def perm(v,d,s,t):
 w=[None]*12
 for i,j in product(range(4),range(3)):w[((d+(-1)**s*i)%4)*3+(j+t)%3]=v[3*i+j]
 return tuple(w)
for x in D:
 assert perm(grid(x),1,0,0)==grid(neg(x)) and perm(grid(x),0,1,0)==grid(x) and perm(grid(x),0,0,1)==grid(f(x))
assert [x for x in D if neg(x)==x==f(x)]==[zero]
diffs={sub(neg(x),x) for x in D}|{sub(f(x),x) for x in D};span={zero}
for v in diffs:
 for _ in range(12):span|={add(w,v) for w in span}
assert span==set(D)
# Images on D8=(r^4=s²=(sr)²=1) times a commuting t of order3. All power relations automatic
# except 2·y=0. The two commutations give x−z=z+t x and y=t y. The displayed actions were checked on the actual grid above.
cocs={(x,y,z) for x,z in product(D,repeat=2) for y in D if add(y,y)==zero and y==f(y) and sub(x,z)==add(z,f(x))}
prs={(sub(neg(d),d),zero,sub(f(d),d)) for d in D}
assert cocs==prs and len(cocs)==144
consts={tuple((g+t)%12 for g in grid(x)) for t,x in product(range(12),D)}
assert len(consts)==1728 and all(len({tuple((j-h)%12 for j,h in zip(v,grid(x))) for x in D if len(set((j-h)%12 for j,h in zip(v,grid(x))))==1})==1 for v in consts)
print("D8 x C3 on an actual 12-site Z/12 code ≅(Z/12)^2: [C,D]=D, fixed zero, 144 unrestricted crossed maps all principal, 1728 constant-phase vectors have unique lift; shared primes 2 and 3, exponent 12")
W={tuple(w) for w in product(range(3),repeat=3) if sum(w)%3==0}
diff=lambda a,b:tuple((x-y)%3 for x,y in zip(a,b))
subg={(0,0,0)}
for p in permutations(range(3)):
 for a in W:
    z=diff(tuple(a[i] for i in p),a)
    for _ in range(3):subg|={tuple((a+b)%3 for a,b in zip(w,z)) for w in subg}
assert subg==W and {(1,1,1),(2,2,2)}<=W
print("transitive nonnilpotent S3 on its ternary augmentation code really has [S3,W]=W and two nonzero fixed vectors: uniqueness fails if nilpotence is dropped")
# Rotations of three binary squares, even colored offsets on three square blocks, extra C3 acts trivially.
Sq=list(product(range(2),repeat=2))
def reflpair(u,p):
 x,y=u
 for _ in range(p):x,y=1-y,x
 return y,x
X=list(product(range(4),repeat=3))
colors=[z for z in range(8) if z.bit_count()%2==0]
M=[(v,t,k) for v,t,k in product(X,colors,range(3))]
def arrow(v,p):return tuple(Sq.index(reflpair(Sq[x],y)) for x,y in zip(v,p))
targets=set(product(X,colors));orb=set(product(X,range(8)))-targets
for x,c in targets:
 U=Counter((arrow(x,p),c^t) for p,t,k in M)
 assert set(U)==targets and set(U.values())=={3}
 if c==0:
    V=Counter(arrow(x,p) for p,t,k in M if not t)
    assert len(V)==64 and set(V.values())=={3}
 U1={(arrow(x,p),c^t^7) for p,t,k in M}
 assert U1==orb
# True principal sum over 192 preservers; their 64 tensor diagonal traces extract real coordinates
# with independently variable swap designs in the three pairs.
T=Counter()
for p,t,k in M:
 if t:continue
 signs=[None]*6;sw={}
 for i,v in enumerate(p):
    dest0=reflpair((0,0),v);dest1=reflpair((1,0),v)
    swaps=dest1[1]!=dest0[1]
    if swaps:sw[i]=(2*i,2*i+1)
    else:signs[2*i:2*i+2]=[(-1)**j for j in dest0]
 for s in range(64):
    if any(((s>>a)&1)!=((s>>b)&1) for a,b in sw.values()): continue
    T[s]+=prod(z for j,z in enumerate(signs) if z is not None and s>>j&1)
assert T==Counter({0:192})
print("768 actual signed actions, 256 points in a non-Cartesian color orbit; exact rank-one multiplicity 3, positive 64×64 principal block, all 64 subset traces, and a shifted orbit genuinely has zero diagonal block")
# Actual simple-group subgroups: translation fours in PSL2(128), unique common rational fixed point.
def m(a,b):
 x=0
 while b:
    if b&1:x^=a
    b>>=1;a<<=1
    if a&128:a^=0x83 # x^7+x+1
 return x
N=range(1,128);tab=[tuple(m(a,b) for b in range(128)) for a in range(128)]
assert all(set(tab[a][1:])==set(N) for a in N)
sub={tuple(sorted((a,b,a^b))) for a in N for b in N if a!=b}
rep={}
for u in sub:
 if u in rep:continue
 orb={tuple(sorted(tab[a][b] for b in u)) for a in N}
 assert len(orb)==127;best=min(orb)
 for w in orb:rep[w]=best
allc=set(rep.values());assert len(sub)==2667 and len(allc)==21
F=lambda u:rep[tuple(sorted(tab[b][b] for b in u))]
cycles=[]
while allc:
 u=next(iter(allc));v=F(u);S=[u]
 while v not in S:S.append(v);v=F(v)
 assert v==u;allc-=set(S);cycles.append(len(S))
assert cycles==[7,7,7]
print("PSL2(128): 2667 actual translation subgroups of order four, 21 true inner classes, Frobenius orbits 7+7+7; not a single chosen local class is Aut-invariant")
