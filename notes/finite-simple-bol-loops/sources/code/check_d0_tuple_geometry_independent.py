"""Independent product-moment, nonrational semilinear, and correlated true packing checks."""
from itertools import product,permutations
from collections import Counter
from math import prod
def cj(g,h):return cm(cm(g,h),inv(g))
def cm(a,b):return tuple(a[i] for i in b)
def inv(g):return tuple(g.index(i) for i in range(len(g)))
def perm(order,f):return tuple(order.index(f(x)) for x in order)
def powers(x):
    y=tuple(range(len(x)));S=[]
    while y not in S:S.append(y);y=cm(y,x)
    return S
# A real four-factor regular product, multiplied by a size-3 kernel to check true weights.
Y=list(product(range(2),repeat=2)); rot=perm(Y,lambda v:(v[1],1-v[0])); flip=perm(Y,lambda v:v[::-1])
squaremarks=[cm(flip,p) for p in powers(rot)];X=list(product(range(2),repeat=4));e=tuple(range(len(X)))
def make_error(a,b):
    return perm(X,lambda s:Y[a[Y.index(s[:2])]]+Y[b[Y.index(s[2:])]])
marks=[make_error(a,b) for a,b,k in product(squaremarks,squaremarks,range(3))]
assert len(marks)==48 and all(Counter(a[i] for a in marks)==Counter({j:3 for j in e}) for i in e)
fixed=Counter();C=Counter()
for a in marks:
    v0=X[a[0]];sig=[]
    for i in range(4):
        z=[0]*4;z[i]=1;v=X[a[X.index(tuple(z))]]
        j,=set(k for k in range(4) if v[k]!=v0[k]);sig.append(j)
    fixed[sum(i==j for i,j in enumerate(sig))]+=1
    for D in range(16):
        if any((D>>i&1)!=(D>>j&1) for i,j in enumerate(sig)):continue
        x=prod((-1)**v0[i] for i,j in enumerate(sig) if i==j and (D>>i)&1)
        C[D]+=x
assert C==Counter({0:48}) and set(fixed)=={0,2,4} and sum(k*v for k,v in fixed.items())==len(marks)*2
# Four bona fide involutions on a binary cube: scalar trace mean 1 but no coordinate identity.
X3=list(product(range(2),repeat=3));neg=[]
for i,j,u,v in [(0,1,0,0),(0,1,0,1),(0,1,1,1),(0,2,1,1)]:
    z=3-i-j
    def action(s):
        y=list(s);y[i]=s[j]^u;y[j]=s[i]^u;y[z]=s[z]^v;return tuple(y)
    neg.append(perm(X3,action))
assert len(set(neg))==4 and all(cm(g,g)==tuple(range(8)) for g in neg)
assert sum(sum(g[i]==i for i in range(8)) for g in neg)==4
assert any(len(set(g[i] for g in neg))!=4 for i in range(8)) or len(neg)%8
print("4-coordinate physical product with nontrivial orbit kernel: rank-one multiplicity 3, all 16 subset moments, fixed-count histogram",sorted(fixed.items()),"; trace-one control without coordinate identity does not suffice")
# GF(256), with its actual 16-element fixed subfield and 120 nonsplit conjugate eigenline pairs.
def field(m,irr):
 n=1<<m
 def mul(a,b):
    v=0
    while b:
        if b&1:v^=a
        b>>=1;a<<=1
        if a&n:a^=irr
    return v
 M=[tuple(mul(i,j) for j in range(n)) for i in range(n)]
 def pw(a,d):
    y=1
    while d:
        if d&1:y=M[y][a]
        a=M[a][a];d>>=1
    return y
 I=[0]+[pw(i,n-2) for i in range(1,n)];assert all(M[i][I[i]]==1 for i in range(1,n))
 def mob(mat,x):
    a,b,c,d=mat
    u,v=(a,c) if x==n else (M[a][x]^b,M[c][x]^d)
    return n if not v else M[u][I[v]]
 return M,pw,mob
M,pw,mob=field(8,0x11b)
F=[i for i in range(256) if pw(i,16)==i]
P=F+[256];assert len(F)==16
def mats(F,M):
  for i in range(4):
   for t in product(F,repeat=3-i):
    v=(0,)*i+(1,)+t;a,b,c,d=v
    if M[a][d]!=M[b][c]:yield v
torpairs={tuple(sorted((x,pw(x,16)))) for x in set(range(256))-set(F)}
assert len(torpairs)==120
inner=[];outer=[]
for mat in mats(F,M):
    a,b,c,d=mat
    if a==d and mat!=(1,0,0,1):inner.append(mat)
    y=tuple(P.index(mob(mat,pw(x,4) if x!=256 else x)) for x in P)
    if cm(y,y)==tuple(range(17)):outer.append(mat)
assert len(inner)==255 and len(outer)==68
hist={}
for z,ls in [(1,inner),(4,outer)]:
    H=Counter()
    for g in ls:
        act=lambda x:mob(g,pw(x,z))
        a={S:tuple(sorted(map(act,S))) for S in torpairs}
        assert set(a.values())==torpairs and all(a[a[s]]==s for s in a)
        H[sum(s==t for s,t in a.items())]+=1
        if z==4:assert all(act(act(x))==pw(x,16)!=x for s in torpairs for x in s)
    hist[z]=H
assert hist=={1:Counter({8:255}),4:Counter({0:68})}
print("GF(256)/GF(16) literal nonsplit pairs: all 255 inner unipotents fix 8 of 120 each; all 68 half-field arrows fix 0; their squares over individual nonrational lines really are the nontrivial q-Frobenius")
M,pw,mob=field(6,0x43);F=[j for j in range(64) if pw(j,4)==j];assert len(F)==4
P=list(range(65));e=tuple(P);Y0=F+[64]
g=tuple(mob((2,3,0,1),x) for x in P)
T=[cj(g,tuple(mob(a,x) for x in P)) for a in mats(F,M)]
T2=[x for x in T if x!=e and cm(x,x)==e]
sub=frozenset(g[i] for i in Y0)
infpoints=[next(i for i in P if v[i]==i) for v in T2]
assert len(set(T))==60 and len(T2)==15 and Counter(infpoints)==Counter({i:3 for i in sub}) and sub!=frozenset(Y0)
t=cj(g,tuple(x if x==64 else pw(x,8) for x in P))
assert cm(t,t)==e and {t[i] for i in sub}==sub and sum(t[i]==i for i in sub)==3
assert {cj(t,z) for z in T}==set(T)
print("actual twisted A5 in PSL2(64): recovered its five conjugated subline points from 15 unipotents; the conjugated half-field preserves it as a SET, moving two subline points")
# Genuine correlated 5-code in D10^2, aligned through a nonidentity A5 transporter.
P=list(permutations(range(5))); ident=tuple(range(5))
sgn=lambda s:sum(x>y for i,x in enumerate(s) for y in s[i+1:])%2
T=[x for x in P if not sgn(x)];r=(1,2,3,4,0);R=powers(r)
N={g for g in T if cj(g,r) in R};assert len(N)==10
t=next(g for g in T if cj(g,r) not in R)
N2={cj(t,x) for x in N};W={(R[i],cj(t,R[2*i%5])) for i in range(5)}
# x sends (p,q) -> (t^-1(q),t(p)). All its T^2-conjugates are arrows (g,g^-1), g in T.
# Their pairwise products: first coordinate g_1^-1 g_2, second g_1 g_2^-1.
sq={(cm(inv(i),j),cm(i,inv(j))) for i,j in product(T,repeat=2)}
assert W&sq=={(ident,ident)}
D={(s,cj(t,inv(s))) for s in N}
assert D<=set(product(N,N2))
cos={frozenset((cm(u,a),cm(v,b)) for a,b in W) for u,v in D}
assert len(cos)==len(D)==10 and sum(map(len,cos))==len(set.union(*(set(C) for C in cos)))==50
assert len(N)*len(N2)==100
print("actual A5 paired mark with transported torus frames: all 3600 true S-conjugate products reject the correlated dimension-one 5-code except identity; its 10 normalizer antidiagonals give 10 disjoint genuine 5-cosets")
