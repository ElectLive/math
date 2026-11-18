"""Countercheck of 2c7ffe13 induction, from the immutable compressed base JSON.
Usage: python3 independent_augmentation_physical_squares.py <base-file>
Only NumPy and Python standard library; does not import either author checker.
"""
import base64,hashlib,json,sys,zlib
import numpy as np
E=lambda n:np.eye(n,dtype=np.int64)
Z=lambda m,n:np.zeros((m,n),dtype=np.int64)
def eq(a,b):return not np.any((a-b)%3)
def dot(a,b):return (a@b)%3
def rref(a):
    a=a.copy()%3;m,n=a.shape;i=0;ps=[]
    for j in range(n):
        if i==m:break
        p=np.flatnonzero(a[i:,j])
        if not len(p):continue
        k=i+int(p[-1]);a[[i,k]]=a[[k,i]];a[i]=(a[i]*a[i,j])%3
        col=a[:,j].copy();col[i]=0;a=(a-col[:,None]*a[i])%3
        i+=1;ps.append(j)
    return a,ps
def rank(a):return len(rref(a)[1])
def image(a):return a[:,rref(a)[1]]
def ker(a):
    b,ps=rref(a);free=[i for i in range(a.shape[1]) if i not in ps];k=E(a.shape[1])[:,free];k[ps,:]=(-b[:len(ps),free])%3
    assert eq(dot(a,k),0);return k
def pow3(a,j):
    r=E(len(a))
    while j:
        if j%2:r=dot(r,a)
        a=dot(a,a);j//=2
    return r
def paired(a,b):return np.block([[a,Z(len(a),len(b))],[Z(len(b),len(a)),b]])
def fixed(u,r):return ker(np.vstack([u-E(len(u)),r-E(len(r))]))
def inv_core(s,u,w):
    s=image(s)
    while s.shape[1]:
        ann=ker(s.T).T
        t=ker(np.vstack([dot(ann,dot(g,s)) for g in [u,w]]))
        if t.shape[1]==s.shape[1]:break
        s=dot(s,t)
    return s
def pre(a,b):return ker(dot(ker(b.T).T,a))
def flat(f,u,w,v,z):
    X=ker(w+E(len(w)));P=2*(E(len(z))-z)%3;H=dot(P,f);dims=[]
    while True:
        C=inv_core(pre(P,dot(H,X)),v,z)
        J=inv_core(pre(f,C),u,w)
        X1=image(dot(2*(E(len(w))-w)%3,J))
        dims.append((X.shape[1],X1.shape[1],J.shape[1],C.shape[1]))
        if X.shape[1]==X1.shape[1]:return dims
        X=X1
def phase(f,gx,gy,der):
    u,w,r=gx;v,z,t=gy; xx=E(len(u)); yy=E(len(v)); mx=ker(w+xx);py=ker(z-yy)
    ys=[pow3(t,i) for i in range(9)];ds=[Z(len(v),1)]
    for e in ys:ds.append((ds[-1]+dot(e,der))%3)
    assert eq(ds[9],0)
    den=np.hstack([(f+dot(z,dot(f,w)))%3,ys[3]-yy]);bt=dot(yy-z,ds[3]);rr=rank(den)
    assert rank(np.hstack([den,bt]))==rr+1
    nums=[]
    for j in range(1,9):
        # c belongs to X^- or Y^+, c+mu(x, f x+d(r^j)) occurs in an actual square.
        qx=xx+dot(w,pow3(r,j));qy=yy-dot(z,ys[j]);sw=dot(qx,w);sz=dot(qy,z)
        mat=np.block([[dot(qx,mx),Z(len(u),py.shape[1]),sw],
                      [Z(len(v),mx.shape[1]),dot(qy,py),-dot(sz,f)]])
        off=np.vstack([Z(len(u),1),dot(sz,ds[j])]);rk=rank(mat)
        assert rank(np.hstack([mat,off]))==rk+1;nums.append(rk)
    return (mx.shape[1],py.shape[1],rr,nums)
def main(path):
    raw=zlib.decompress(base64.b64decode(open(path,'rb').read()));assert hashlib.sha256(raw).hexdigest()=='c5965e0fdc104b529bf3eac790bac48d83e1c8ef03d8cb04f284893eaeb53ddb'
    F={k:np.array([[int(c) for c in row] for row in a],dtype=np.int64) for k,a in json.loads(raw).items()}
    f=F['f'];der=F['d'];gx=tuple(F['X'+c] for c in 'uwr');gy=tuple(F['Y'+c] for c in 'uwr')
    p=19;inf=19;v=lambda j: E(19)[:,j:j+1] if j!=inf else Z(19,1)
    maps=[lambda x:(x+1)%p if x!=inf else inf, lambda x:0 if x==inf else inf if not x else -pow(x,-1,p)%p,lambda x:(4*x)%p if x!=inf else inf]
    M=[np.hstack([v(g(j))-v(g(inf)) for j in range(p)])%3 for g in maps]
    assert [pow(3,i,19) for i in range(1,18)].count(1)==0 and pow(3,18,19)==1
    assert fixed(M[0],M[2]).shape[1]==1 and ker(M[2]-E(19)).shape[1]==3 and fixed(M[0],M[1]).shape[1]==0
    assert ker(np.vstack([(g-E(19)).T for g in M[:2]])).shape[1]==0
    rng=np.random.default_rng(137119)
    for n in range(4):
        u,w,r=gx;v1,z,t=gy;ix=E(len(u));iy=E(len(z));fx=fixed(u,r);fy=fixed(v1,t);yp=ker(t-iy)
        forb=image(np.hstack([dot(f,dot(w-ix,fx)),dot(z-iy,fy)]))
        assert (fx.shape[1],fy.shape[1],yp.shape[1])==(1+n,2+n,14+3*n) and forb.shape[1]<=3+2*n
        assert eq(dot(f,u),dot(v1,f)) and eq(dot(f,r),dot(t,f)); cc=flat(f,u,w,v1,z);assert cc[-1][1:]==(0,0,0)
        dims=phase(f,gx,gy,der); coin=ker(np.vstack([(v1-iy).T,(z-iy).T])).T
        assert coin.shape[0]==1 and rank(dot(coin,f))==1 and ker(np.vstack([(u-ix).T,(w-ix).T])).shape[1]==0
        print('stage',n,'X,Y',len(u),len(v1),'B X,B Y,P Y,actual forbidden',fx.shape[1],fy.shape[1],yp.shape[1],forb.shape[1],'flat',cc,'physical Xminus,Yplus,bottom,all eight native ranks',dims)
        if n==3:break
        while True:
            beta=dot(yp,rng.integers(0,3,(yp.shape[1],1)))
            if rank(np.hstack([forb,beta]))>forb.shape[1]:break
        a=np.hstack([dot(pow3(v1,j),beta) for j in range(p)]);assert eq(dot(a,M[0]),dot(v1,a)) and eq(dot(a,M[2]),dot(t,a))
        # Negative control n>=1: nonzero coupling -f l outside mere zero test, but
        # l is T-linear inclusion of the PREVIOUS M. The fully tilted graph of l is flat.
        if n>0:
            l=np.vstack([Z(len(u)-19,19),E(19)]);abad=-dot(f,l)%3;assert np.any(abad)
            bad=np.block([[f,abad],[Z(19,len(u)),E(19)]])
            J=np.vstack([l,E(19)]);Yp=np.vstack([Z(len(v1),19),E(19)])
            assert eq(dot(bad,J),Yp)
            assert all(eq(dot(paired(g,k),J),dot(J,k)) for g,k in zip(gx,M))
            assert all(eq(dot(paired(g,k),Yp),dot(Yp,k)) for g,k in zip(gy,M))
            print('nonzero forbidden coupling really produces a tilted flat pair; signed defect',ker(M[1]+E(19)).shape[1],ker(M[1]+E(19)).shape[1])
        f=np.block([[f,a],[Z(19,len(u)),E(19)]])
        der=np.vstack([der,Z(19,1)]);gx=tuple(paired(g,k) for g,k in zip(gx,M));gy=tuple(paired(g,k) for g,k in zip(gy,M))
if __name__=='__main__':main(sys.argv[1])
