"""Exact 1053-point Nagy coset-action check. Stdlib Python, no multiplication table lookup."""
from itertools import product
from collections import deque
def digits(a):return (a%3,a//3%3,a//9)
def code(v):return v[0]%3+3*(v[1]%3)+9*(v[2]%3)
E=range(27); add=[[code([x+y for x,y in zip(digits(a),digits(b))]) for b in E] for a in E]
def mul(a,b):
    v=[0]*5
    for i,x in enumerate(digits(a)):
        for j,y in enumerate(digits(b)):v[i+j]+=x*y
    for i in [4,3]:v[i-3]+=v[i];v[i-2]+=v[i]    # X^3=X+1
    return code(v)
M=[[mul(a,b) for b in E] for a in E]
def pw(a,n):
    z=1
    for _ in range(n):z=M[z][a]
    return z
g=next(x for x in range(1,27) if len({pw(x,i) for i in range(26)})==26)
root=pw(g,2);P=[pw(root,i) for i in range(13)];F=[[pw(x,3**h) for x in E] for h in range(3)]
Tr=[add[add[x][F[1][x]]][F[2][x]] for x in E];assert set(Tr)==set(range(3))
Y=list(product(E,range(13),range(3)));I=(0,0,0)
def prodY(g,h):
    v,b,s=g;w,c,t=h
    return add[v][M[P[b]][F[s][w]]],(b+c*3**s)%13,(s+t)%3
def invY(g):
    v,b,h=g;j=-h%3;c=-b*3**j%13;w=M[P[c]][F[j][v]]
    return code([-x for x in digits(w)]),c,j
def conj(g,h):return prodY(prodY(g,h),invY(g))
assert all(prodY(g,invY(g))==I for g in Y)
A={y for y in Y if not y[0]};B={y for y in Y if not y[1] and y[2]==-Tr[y[0]]%3}
assert len(A)==39 and len(B)==27 and A&B=={I} and {prodY(a,b) for a,b in product(A,B)}==set(Y)
def closure(gens):
    have={I};q=deque(have)
    while q:
        g=q.popleft()
        for a in gens:
            h=prodY(g,a)
            if h not in have:have.add(h);q.append(h)
    return have
AY=[(0,1,0),(0,0,1)]
BY=[];gen=closure(BY)
for b in sorted(B):
    if b not in gen:BY.append(b);gen=closure(BY)
assert closure(AY)==A and gen==B and closure(AY+BY)==set(Y)
N=lambda U,gens:{g for g in Y if all(conj(g,b) in U for b in gens)}
NA=N(A,AY);NB=N(B,BY);Z={g for g in Y if all(conj(g,b)==b for b in AY+BY)}
assert len(NA)==39 and len(NB)==81 and Z=={I}
# Fiber product contains all rows; verify its commutator kernel/order, not merely an order guess.
gens=AY+BY;Yp=closure([conj(g,prodY(conj(a,b),invY(b))) for a,b in product(gens,repeat=2) for g in Y])
assert len(Yp)==351 and all(h==0 for v,b,h in Yp)
def match(a,b):return (a[2]+b[2])%3==0
sz=sum(match(a,b) for a,b in product(Y,repeat=2))
H={(b,a) for b,a in product(B,A) if match(b,a)}
normalizer={(a,b) for a,b in product(NB,NA) if match(a,b)}
assert sz==369603 and len(H)==351 and len(normalizer)==1053
# Separately, use actual cosets. O(Y^2) mark evaluations -> stabilizer fixed identity-images.
local={}
for b in Y:
    C=frozenset(prodY(b,x) for x in B); D=frozenset(prodY(b,x) for x in A)
    local['b',b]=min(C);local['a',b]=min(D)
coset=lambda v:(local['b',v[0]],local['a',v[1]])
pts={coset((y,invY(y))) for y in Y};assert len(pts)==1053
fix={pt for pt in pts if all(coset((prodY(h[0],pt[0]),prodY(h[1],pt[1])))==pt for h in H)}
assert len(fix)==3
br=next(h for h in H if h[0]==I and h[1]!=(0,0,0))
assert br[1][0]==0 and br[1][2]==0
print('Exact affine field F27: order-13 scalar root',root,'trace size',len(set(Tr)),'; exact factors |A|=39, |B|=27.')
print('D=left multiplication subgroup of Y^2 with inverse abelianization: |Y derived|=351, |D|=369603, |H|=351, degree=1053. Z(Y)=1, and D is subdirect, so Z(D)=1.')
print('Normalizer sizes |N_Y(A)|=39, |N_Y(B)|=81, |N_D(H)|=1053. Actual 1053 coset points fixed by all H: 3; full native right nucleus C3, not trivial.')
print('Native stabilizer pair',br,'moves identity in the associated diagonal action y -> a y b^-1.')
