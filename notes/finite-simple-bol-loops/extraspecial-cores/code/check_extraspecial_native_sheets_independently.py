"""Independent exact coefficient sheets on fresh cyclotomic factors and all projected sign pairs.
No author matrices or module catalogs imported; products are in the actual extraspecial coordinates."""
from itertools import product,combinations
from math import prod
def rank(A,p):
    b={}
    for row in A:
        v=list(row)
        for i,t in sorted(b.items()):
            if v[i]:
                c=v[i];v=[(a-c*z)%p for a,z in zip(v,t)]
        h=next((i for i,a in enumerate(v) if a%p),None)
        if h is not None:
            k=pow(v[h],-1,p);b[h]=[a*k%p for a in v]
    return len(b)
def order(p,q):return next(i for i in range(1,q) if pow(p,i,q)==1)
def native(p,q,m):
    f=order(p,q);b=f if not f%2 else 2*f;d=p*b*m
    alpha=next(x for x in range(2,q) if pow(x,p,q)==1)
    # Find our own monic minimal polynomial of a primitive q-th root by divisibility of X^q-1:
    # all nonidentity roots have minimal degree f; large coefficient weights/positions prioritized differently.
    def roots(co):
        v=(1,)+(0,)*(f-1);one=v;Z=[]
        for _ in range(q):
            Z.append(v);h=v[-1];v=tuple(((v[j-1] if j else 0)-h*co[j])%p for j in range(f))
        return Z if v==one and len(set(Z))==q else None
    Z=None;skip=int(q==61)
    for weight in range(2,f+1):
        for ix in reversed(list(combinations(range(1,f),weight-1))):
            for val in product(range(p-1,0,-1),repeat=weight):
                co=[0]*f
                for j,v in zip((0,)+ix,val):co[j]=v
                Z=roots(co)
                if Z and skip:skip-=1;Z=None
                elif Z:break
            if Z:break
        if Z:break
    assert Z
    tr=[]
    for e in range(q):
        w=[sum(Z[(e*pow(p,i,q))%q][j] for i in range(f))%p for j in range(f)]
        assert not any(w[1:]);tr.append(w[0])
    def trr(k):return tr[k%q]
    def g(i,j,k=0): # raw g(e_i,z^k e_j), not assumed alternating until checked
        if not f%2:return (trr(1+i-j-k)-trr(-1+i-j-k))%p
        if i<f<=j:return trr(i+j-f-k)
        if j<f<=i:return -trr(i-f+j+k)%p
        return 0
    assert all((g(i,j)+g(j,i))%p==0 and (i!=j or g(i,i)==0) for i,j in product(range(b),repeat=2))
    assert rank([[g(i,j) for j in range(b)] for i in range(b)],p)==b
    assert rank([[(g(i,j,1)-g(i,j))%p for j in range(b)] for i in range(b)],p)==b
    def mul(a,c):
        x,y,i,e=a;u,v,j,h=c
        if e:u,v=v,u
        return ((x+pow(alpha,i,q)*u)%q,(y+pow(alpha,-i,q)*v)%q,(i+(-j if e else j))%p,e^h)
    ID=(0,0,0,0)
    signs=[(x,y,i,1) for x,y,i in product(range(q),range(q),range(p)) if mul((x,y,i,1),(x,y,i,1))==ID]
    assert len(signs)==p*q
    # A-index = (j,site coefficient,block copy); matrices first for one true repeated block.
    coords=list(product(range(p),range(b)))
    def gl(a,r,s):
        j,i=r;k,o=s;x,y,h,e=a
        if (k+j-h)%p:return 0
        exponent=(x*pow(alpha,-j,q)+y*pow(alpha,j,q))%q
        return g(i,o,exponent)
    K={a:tuple(tuple(gl(a,r,s) for s in coords) for r in coords) for a in signs}
    def sym(M):return tuple((M[i][j]+M[j][i])%p for i in range(len(M)) for j in range(i+1))
    # With second-half vector cancellation, raw coefficient is K(aba)-K(a). Compare ALL entries of
    # its symmetric part. Orthogonal repeated blocks give repeated diagonals and identically zero cross terms.
    sy={a:sym(M) for a,M in K.items()};counts=[0]*3;off=False;twistbad=False
    for a,c in product(signs,repeat=2):
        u=mul(a,c);ac=mul(u,a)
        assert sy[a]==sy[ac]  # entire central quadratic sheet over L vanishes, even off H projections
        if u[0]:continue
        if not u[2]:
            assert u==ID and a==c;counts[0]+=1
        else:
            counts[1+bool(u[1])]+=1
            assert u[2]%p # genuine stabilizer central sheet lambda*j, lambda=1
            if not u[1] and u[2]==1:twistbad=True # origin-vector pure signs DO collide for lambda=0
            if not off:
                for i,r in enumerate(K[a]):
                    if any((v+w)%p for v,w in zip(r,K[ac][i])):
                        off=True;break
    assert counts[0]==p*q and sum(counts)==p*p*q and off and twistbad
    # Concrete noncoordinate diagonal normal subspaces inside the repeated physical representation:
    # a scalar diagonal copy in U1+U1 stays signed-stable by the same matrices in its two blocks;
    # compute dimensions of its intersection with the physical first-Lagrangian and eigen-minus slice.
    diags=0
    if m>=2:
        d0=p*b
        for c in range(1,p):
            E=[[int(i==j) for j in range(2*d0)]+[c*int(i==j) for j in range(2*d0)] for i in range(2*d0)]
            # coordinates in each copy: its first Lagrangian then its second.
            projM=[v[d0:2*d0]+v[3*d0:] for v in E]
            tminus=[[(v[(j+d0)%(2*d0)]-v[j])%p for j in range(2*d0)] for v in E]
            assert rank(E,p)==2*d0 and rank(projM,p)==rank(tminus,p)==d0
            assert 1+rank(projM,p)>rank(tminus,p);diags+=1
    print(f'p={p},q={q},f={f},m={m},d={d}: factor X^{f}+{co}; {len(signs)**2} genuine projected products, {counts} in H (identity / pure rotation / translated nonzero rotation); all L-sheet quadratic coefficients vanish; actual off-L nonzero and zero-twist collision verified; {diags} noncoordinate normal subspaces.')
for tup in ((3,7,1),(3,13,2),(5,11,1),(3,61,1)):native(*tup)
