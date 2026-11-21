"""Pencil graph orbit and full native signed-phase controls. Requires numpy and the companion field checker."""
from verify_frobenius_graph_extraspecial import Field,rank,invert
import numpy as np
import itertools,math

def number(p,f):
    Q=p**(f//2)+1;out={}
    for i in range(1,f//2):
        h=f//math.gcd(f,i)
        if h%2==0 and h%4:continue
        g=math.gcd(Q,p**i-1)
        ss=0
        for k in range(f):
            x=p**k-1;a=math.gcd(x,g)
            if (x//2)%a==0:ss+=a
        assert ss%f==0;out[i]=(g,ss//f)
    return out

def y_folders():
    p=3;f=10;q=61;al=13
    k=Field(3,[1,0,0,1,1,1,1,1,0,0,1]);prim=k.primitive();v=k.pw(prim,(k.n-1)//q);Q=3**5+1
    c=k.pw(prim,Q//2);assert k.pw(c,Q-1)==k.neg(c)
    U=[k.pw(prim,(Q-2)*i) for i in range(Q)]
    assert len(set(U))==Q and all(k.mul(u,k.pw(u,Q-1))==k.one for u in U)
    S={pow(3,k,q)*pow(al,j,q)%q for j in range(p) for k in range(f)}
    def weights(mu):
        return frozenset((mu*pow(3,k,q)*pow(al,j,q)%q,pow(3,k,q)*pow(al,-j,q)%q) for j in range(p) for k in range(f))
    Ws={u:weights(u) for u in S}
    fixed={u for u,W in Ws.items() if W==frozenset((b,a) for a,b in W)}
    assert len(fixed)==2*p
    bad=[u for u in fixed if any((a+b)%q==0 for a,b in Ws[u])]
    assert len(bad)==p and all(u in {(-pow(al,r,q))%q for r in range(p)} for u in bad)
    for i,(g,n) in number(3,10).items():
        eta0=k.pw(prim,(p**i+Q-3)//2)
        rho=k.pw(prim,(p-1)//2)
        assert k.pw(eta0,Q)==k.neg(k.mul(k.pw(c,p**i),k.pw(c,-1)))
        etas={k.mul(eta0,u) for u in U}
        # Orbit really on field scalars: two generators, not on j modulo a guessed modulus.
        zz=U[1];aa=k.mul(zz,k.pw(zz,-p**i));bb=k.mul(rho,k.pw(rho,-p**i))
        lens=[]
        while etas:
            x=etas.pop();todo=[x];le=1
            while todo:
                a=todo.pop()
                for y in (k.mul(aa,a),k.mul(bb,k.pw(a,p))):
                    if y in etas:etas.remove(y);todo.append(y);le+=1
            lens.append(le)
        assert len(lens)==n
        print('q=61 irreducible pair i=%d on all %d actual anti-isometries, signed gauge orbit sizes'%(i,Q),sorted(lens))
    d=p*f;eye=np.eye(d,dtype=np.int64);ee=np.eye(2*d,dtype=np.int64)
    mm=lambda fun:np.array([fun(a) for a in k.e],dtype=np.int64).T
    g=np.array([[k.tr(k.mul(c,k.mul(x,k.pw(y,Q-1)))) for y in k.e] for x in k.e],dtype=np.int64)
    Om=np.kron(np.eye(2*p,dtype=np.int64),g)
    et=k.pw(prim,(Q-2)//2);assert k.pw(et,Q)==k.neg(k.one)
    T=np.kron(np.eye(p,dtype=np.int64),mm(lambda x:k.mul(x,et)));L=np.vstack((eye,T));pr=np.hstack((-T,eye))
    zs=[k.one]
    for _ in range(1,q):zs.append(k.mul(zs[-1],v))
    zm=[mm(lambda x,a=a:k.mul(a,x)) for a in zs]
    def act(l,sg,s,t,j):# (s,t) h^j tau restriction to a fixed sheet with shift l
        g=np.zeros((d,d),dtype=np.int64)
        for m in range(p):
            j0=(-m-j-l)%p;a=(pow(al,l+m,q)*s+pow(al,-m,q)*t)%q
            g[m*f:(m+1)*f,j0*f:(j0+1)*f]=sg*zm[a]
        return g
    def piv(a):
        a=a.copy()%p;h=0;cols=[]
        for i in range(a.shape[1]):
            j=next((j for j in range(h,len(a)) if a[j,i]),None)
            if j is None:continue
            a[[h,j]]=a[[j,h]];a[h]=a[h]*pow(int(a[h,i]),-1,p)%p
            v=a[:,i].copy();v[h]=0;a=(a-v[:,None]*a[h])%p;cols.append(i);h+=1
        return cols
    signs=[(s,-pow(al,-j,q)*s%q,j) for s in range(q) for j in range(p)]
    seen=[]
    for r in range(1,p):
        tbad=np.block([[act(0,1,0,0,0),0*eye],[0*eye,act(r,1,0,0,0)]])
        assert rank(np.hstack((L,tbad@L)),p)<2*d
        rr={}
        for a in signs:
            mat=np.block([[act(0,1,*a),0*eye],[0*eye,act(r,-1,*a)]])
            assert not np.any((mat@mat-ee)%p) and not np.any((mat.T@Om@mat-Om)%p)
            U0=(ee-mat)%p;cols=piv(pr@U0%p);assert len(cols)==d
            U0=U0[:,cols];rr[a]=U0@invert(pr@U0%p,p)%p
        items=0
        for a,b in itertools.product(signs,repeat=2):
            s,t,j=a;x,y,l=b
            z=((s+pow(al,j,q)*y)%q,(t+pow(al,-j,q)*x)%q,(j-l)%p)
            if z[0] or z[2]==0 and z[1]:continue
            m,n,s0=z;o=((m+pow(al,s0,q)*s)%q,(n+pow(al,-s0,q)*t)%q,(s0+j)%p)
            A=rr[a].T@Om@rr[o]%p;assert not np.any((A+A.T)%p);items+=1
        assert items==549
        # Signed color plus / minus is distinguished on the true h-fixed spaces of the separate V-orbits.
        def sig(mu,t):return (Ws[mu],t)
        obj=[(Ws[1],1),(Ws[pow(al,r,q)],-1)]
        reps=[]
        for z in S:
            reps.append(tuple(tuple(sorted((z*x%q,z*y%q) for x,y in W)) for W,tag in obj))
        can=min(reps);assert can not in seen;seen.append(can)
        print('q=61 fixed-distinct offset %d: all 183 signed matrices, %d full native central-quadratic systems; equal-sign adverse lost transversality'%(r,items))
    for p,f in ((3,10),(3,16),(5,4),(5,12),(7,20),(11,8)):
        result=number(p,f);print('p=%d f=%d signed pair orbit data'% (p,f),result,'total incl canonical',p+1+sum(x[1] for x in result.values()))
if __name__=='__main__':y_folders()
