"""Genuine eight-coordinate normalizer transports and correlated layers, independent of author's code."""
from itertools import permutations,product
from random import Random
def cm(a,b):return tuple(a[i] for i in b)
def iv(a):return tuple(a.index(i) for i in range(len(a)))
def cj(a,b):return cm(cm(a,b),iv(a))
def par(p):return sum(a>b for i,a in enumerate(p) for b in p[i+1:])%2
def permute(c,w):return sum(((w>>i)&1)<<c[i] for i in range(len(c)))
Z=tuple(range(8));C={tuple((k+(-1)**s*i)%8 for i in Z):s for k,s in product(Z,range(2))}
F={tuple((x^t) if not s else ((((x&1)<<1)|((x&2)>>1)|(x&4))^t) for x in Z) for t,s in product(Z,range(2))}
assert len(C)==len(F)==16 and all(len({g[i] for g in C})==8 for i in Z)
for G in (C,F):
 for w in range(1,256):
    S={0}
    for g in G:S|={v^permute(g,w) for v in S}
    assert 255 in S
neg={0,0b110110,0b101101,0b011011};cyc=(1,2,3,4,5,0)
assert {permute(cyc,w) for w in neg}==neg and 63 not in neg
print("two different nonregular transitive eight-site 2-groups: all 510 nonzero-vector orbit spans contain the all-ones word; transitive six-cycle control has a real invariant binary code without it")
L=tuple(range(5));S5=tuple(permutations(L));A5=[g for g in S5 if not par(g)]
def affine(u,v):return tuple((u*x+v)%5 for x in L)
tor={affine(1,v) for v in L};refl=tuple(affine(4,v) for v in L)
Norm={s for s in S5 if {cj(s,g) for g in tor}==tor}
assert Norm=={affine(u,v) for u,v in product(range(1,5),L)}
oddinvol=[g for g in S5 if par(g) and cm(g,g)==L]
alltor={frozenset(cj(s,g) for g in tor) for s in A5};assert len(alltor)==6
assert all(all(frozenset(cj(s,g) for g in R)!=R for R in alltor) for s in oddinvol)
def actual(c,gs):return tuple(5*c[i]+gs[i][x] for i,x in product(Z,L))
gauge=[affine(pow(2,e,5),t) for e,t in zip((0,1,2,3,2,1,1,0),(0,1,4,0,2,2,3,1))]
A={actual(Z,[cj(g,affine(1,t)) for g in gauge]) for t in L}
e40=tuple(range(40));B={};sec={}
for c,s in C.items():
    arr=[cm(gauge[c[i]],cm(affine((-1)**s,0),iv(gauge[i]))) for i in Z]
    B[c]=tuple(map(par,arr));sec[c]=actual(c,arr)
assert any(len(set(v))>1 for v in B.values())
assert all(cm(sec[c],sec[d])==sec[cm(c,d)] for c,d in product(C,repeat=2))
H={cm(w,x) for w,x in product(A,sec.values())}
assert len(H)==80 and all(cm(p,q) in H for p,q in product(H,repeat=2))
mixed=0;valid=0;cases=0;mass=0;linear=0
for c in C:
 if cm(c,c)!=Z:continue
 coset={cm(w,sec[c]) for w in A};lifts=[p for p in coset if cm(p,p)==e40]
 assert lifts and not any(B[c][i] for i in Z if c[i]==i)
 if len(lifts)<len(coset):mixed+=1
 valid+=len(lifts);f=sum(c[i]==i for i in Z);p=(8-f)//2
 w=10**f*60**p;mass+=w;linear-=w*f;cases+=1
assert mixed and linear<0
print(f"actual H≤F20 wr D16 of order {len(H)}, nontrivial gauge-twisted binary graph and diagonal five-kernel: all {cases} square-one labels lift, {valid} physical square-one lifts, {mixed} cosets also include nonsquare-one lifts; full outside fixed-site coefficient {linear} at physical mass {mass}")
# A legal but physically non-liftable binary graph: reflection bit on every fixed site.
bc={c:(C[c],)*8 for c in C}
assert all(bc[cm(c,d)]==tuple(bc[c][d[i]]^bc[d][i] for i in Z) for c,d in product(C,repeat=2))
bad=next(c for c,s in C.items() if s and any(c[i]==i for i in Z))
assert any(bc[bad][i] for i in Z if bad[i]==i)
assert all(cm(g,g) in refl for g in Norm if par(g))
print("honest binary graph with a forbidden fixed-site bit: all group laws hold, but its rooted reflection admits no square-one arrow over the five-torus normalizer")
rng=Random(719);match=[c for c in C if cm(c,c)==Z and all(c[i]!=i for i in Z)]
count=0
for c in match:
 pairs=[(i,j) for i,j in enumerate(c) if i<j]
 for _ in range(64):
    val=[rng.choice(refl) for i in Z];a=[None]*8;b=[None]*8
    for i,j in pairs:
        bit=rng.randrange(2)
        s=next(s for s in S5 if par(s)==bit and cj(s,iv(val[i]))==val[j]);t=cm(s,val[i])
        assert par(s)==par(t)==bit
        a[i]=s;a[j]=iv(s);b[i]=t;b[j]=iv(t)
    p=actual(c,a);q=actual(c,b)
    assert cm(p,p)==cm(q,q)==e40
    assert cm(p,q)==actual(Z,val);count+=1
print(f"{count} eight-coordinate correlated all-reflection tuples explicitly factor into TWO genuine same-outer-labeled all-paired involutions on 40 points, with independently varied inner/odd transports")
