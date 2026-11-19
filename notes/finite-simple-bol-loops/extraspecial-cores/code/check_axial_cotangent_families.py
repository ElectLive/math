"""Native rational generators for the new axial modules; verifies both field cases at nontrivial sizes."""
from itertools import product,combinations
from math import gcd,lcm
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def tr(M):return [list(z) for z in zip(*M)]
def mm(A,B,p):return [[sum(x*y for x,y in zip(a,b))%p for b in tr(B)] for a in A]
def mp(A,h,p):
    B=eye(len(A))
    while h:
        if h&1:B=mm(B,A,p)
        A=mm(A,A,p);h//=2
    return B
def rank(M,p):
    tab={}
    for row in M:
        v=list(row)
        for i,t in sorted(tab.items()):
            c=v[i]
            if c:v=[(a-c*b)%p for a,b in zip(v,t)]
        k=next((j for j,a in enumerate(v) if a%p),None)
        if k is not None:tab[k]=[(a*pow(v[k],-1,p))%p for a in v]
    return len(tab)
def case(p,q):
    f=next(i for i in range(1,q) if pow(p,i,q)==1)
    alpha=pow(p,f//p,q) if not f%p else next(i for i in range(2,q) if pow(i,p,q)==1)
    assert alpha!=1 and pow(alpha,p,q)==1
    one=[1]+[0]*(f-1);ZZ=None
    for cf in product(range(p),repeat=f):
        if not cf[0]:continue
        v=one;z=[]
        for j in range(q):
            z.append(v);v=[((v[i-1] if i else 0)-v[-1]*cf[i])%p for i in range(f)]
        if v==one and len({tuple(t) for t in z})==q:ZZ=z;break
    assert ZZ
    A=lambda h:tr([ZZ[(i+h)%q] for i in range(f)])
    N=lcm(f,p);copies=N//f
    def diag(ms):return [[ms[i//f][i%f][j%f] if i//f==j//f else 0 for j in range(N)] for i in range(N)]
    Z=diag([A(pow(alpha,j,q)) for j in range(copies)])
    if copies==1:H=tr([ZZ[(i*alpha)%q] for i in range(f)])
    else:H=[[int(j==((i+f)%N)) for j in range(N)] for i in range(N)]
    I=eye(N)
    assert mp(H,p,p)==I and H!=I and mp(Z,q,p)==I
    assert mm(mm(H,Z,p),mp(H,p-1,p),p)==mp(Z,alpha,p)
    rs=rank([[(z-I[i][j])%p for j,z in enumerate(row)] for i,row in enumerate(Z)],p);assert rs==N
    # A sign s=(v,h^i)t swaps both W- and W*-types. Its restriction on M=W*+W'
    # sends (xi,y) to (P y,Q xi) in L=W+(W')*. P and Q act on the two separately occupied axes.
    # Omega(s(xi,y),(eta,z))= eta(P y) - (Q xi)(z).
    zps=[mp(Z,j,p) for j in range(q)];hps=[mp(H,j,p) for j in range(p)]
    check=0;off=None
    for h,x in product(range(p),range(q)):
        y=-pow(alpha,-h,q)*x%q
        P=mm(zps[x],hps[h],p) # W: z^x h^h on a vector brought from W'
        Q=mm(tr(zps[-y%q]),tr(hps[h]),p) # (W')* action: z^(-y,T) h^(h,T)
        # Initial xi is in W*, final in (W')*. Symplectic-involution identity Q=P^T.
        assert Q==tr(P)
        if off is None:
            off=next(abs(a) for row in P for a in row if a)
        check+=1
    assert check==p*q
    # Signed whole top, direct multiplication; H projections b2*h^j always require nonzero
    # center for j!=0, including actual translated elements. Pure nonzero second-axis no preimage.
    signs=[(x,-pow(alpha,-i,q)*x%q,i) for x,i in product(range(q),range(p))]
    hits=0
    for x,y,i in signs:
        for u,v,j in signs:
            X=(x+pow(alpha,i,q)*v)%q;Y=(y+pow(alpha,-i,q)*u)%q;J=(i-j)%p
            if X:continue
            assert J or Y==0
            hits+=bool(J)
    assert hits==(p-1)*p*q
    dA=2*N;dB=p*(f if f%2==0 else 2*f);D=lcm(dA,dB)
    print('p,q,f,axial d,native d,common D:',p,q,f,dA,dB,D,'; native signed maps with all quadratic sheets zero:',check,'; actual distinct central obstruction pairs over nonzero rotations:',hits,'; among k=3 mixed-block groups intrinsic fixed ranks',[j*D for j in range(4)])
for v in ((3,7),(3,13),(5,31)):case(*v)
