"""Author controls. Genuine commuting loop elements are points with equal final affine flats."""
from itertools import product
from collections import Counter
def check(p,q,all_bases=True,physical=False):
    z=next(z for z in range(2,q) if pow(z,p,q)==1)
    half=pow(2,-1,p); hq=pow(2,-1,q); r=(p-1)//2; zero=(0,)*p
    def plus(a,b):return tuple((u+v)%q for u,v in zip(a,b))
    def neg(a):return tuple(-u%q for u in a)
    def sub(a,b):return plus(a,neg(b))
    def sm(c,a):return tuple(c*u%q for u in a)
    def sx(x,t):
        a,b=x
        return tuple(pow(z,(a*b*half+b*(j-a))%p,q)*t[(j-a)%p]%q for j in range(p))
    def ns(x):return tuple(-a%p for a in x)
    def hj(x):return tuple(a*half%p for a in x)
    def xpy(x,y):return tuple((a+b)%p for a,b in zip(x,y))
    def flatquot(x,t):
        s=sx(ns(x),t)
        return tuple(hq*(s[j]-s[-j])%q for j in range(1,r+1))
    def minus(v):
        a=[0]*p
        for j,t in enumerate(v,1):a[j]=t;a[-j]=-t%q
        return tuple(a)
    neg_basis=[minus(tuple(int(i==j) for i in range(r))) for j in range(r)]
    def rref(rows):
        A=list(map(list,rows)); i=0; piv=[]
        for j in range(r):
            m=next((k for k in range(i,len(A)) if A[k][j]%q),None)
            if m is None:continue
            A[i],A[m]=A[m],A[i]; d=pow(A[i][j],-1,q)
            A[i]=[d*e%q for e in A[i]]
            for k in range(len(A)):
                if k!=i: A[k]=[(a-A[k][j]*c)%q for a,c in zip(A[k],A[i])]
            piv.append(j);i+=1
        return i,piv,A[:i]
    def norm(rows):
        i,piv,A=rref(rows);assert i==r-1; j=(set(range(r))-set(piv)).pop()
        v=[0]*r;v[j]=1
        for t,k in enumerate(piv):v[k]=-A[t][j]%q
        c=pow(next(k for k in v if k),-1,q);return tuple(c*k%q for k in v)
    def laws(x,y,u,t,V):
        # Compare true flats (u,S_x)(t,S_y)(V+A+) vs their reverse.
        # S_xS_y and S_yS_x differ only by scalar, so the two linear
        # directions agree. Test vector-origin difference in that common direction.
        s=xpy(x,y); P=plus(plus(u,sx(x,t)),sx(x,sx(y,V)))
        Q=plus(plus(t,sx(y,u)),sx(y,sx(x,V)))
        return flatquot(s,sub(P,Q))
    vecs=list(product(range(p),repeat=2)); ds=range(1,p) if all_bases else (1,)
    tested=0; physical_tests=0
    for d in ds:
        normals=Counter()
        for x in vecs:
            for y in vecs:
                if (x[0]*y[1]-x[1]*y[0])%p!=d:continue
                rows=[laws(x,y,sx(hj(x),v),zero,zero) for v in neg_basis]
                rows +=[laws(x,y,zero,sx(hj(y),v),zero) for v in neg_basis]
                N=norm(rows); normals[N]+=1; tested+=1
                if physical and (p==3 or (x==(1,0) and y==(0,1))):
                    U=[sx(hj(x),minus(v)) for v in product(range(q),repeat=r)]
                    T=[sx(hj(y),minus(v)) for v in product(range(q),repeat=r)]
                    pairs=Counter(laws(x,y,u,t,zero) for u in U for t in T)
                    assert len(pairs)==q**(r-1)
                    for v in product(range(q),repeat=r):
                        target=tuple((-b)%q for b in laws(x,y,zero,zero,minus(v)))
                        assert pairs[target]==(q**(r+1) if sum(a*b for a,b in zip(N,v))%q==0 else 0)
                    if p==5:
                        # Independent exhaustive actual affine product at a nonzero v in the
                        # hyperplane and at a nonzero v outside, without rerouting through v=0.
                        vs=list(product(range(q),repeat=r)); inside=next(v for v in vs if any(v) and sum(a*b for a,b in zip(N,v))%q==0)
                        outside=next(v for v in vs if sum(a*b for a,b in zip(N,v))%q)
                        for v,k in ((inside,q**(r+1)),(outside,0)):
                            assert sum(not any(laws(x,y,u,t,minus(v))) for u in U for t in T)==k
                            physical_tests+=len(U)*len(T)
                    else:
                        for v in product(range(q),repeat=r):
                            assert sum(not any(laws(x,y,u,t,minus(v))) for u in U for t in T)==(q**(r+1) if not any(v) else 0)
                            physical_tests+=len(U)*len(T)
        assert rref(normals)[0]==r
        vv=product(range(q),repeat=r) if p<=5 else (tuple((3+i*t*t)%q for i in range(r)) for t in range(41))
        frac=[]
        for v in vv:
            if any(v):
                outside=sum(c for N,c in normals.items() if sum(a*b for a,b in zip(N,v))%q)
                assert outside*r>=sum(normals.values());frac.append(outside)
        if d==1: print('p,q',p,q,'bases of determinant one',sum(normals.values()),'distinct codim-one tests',len(normals),'tested nonzero tilts',len(frac),'minimum incompatible bases observed',min(frac))
    print('total native pair-direction ranks tested',tested,'direct fixed-tilt affine product comparisons',physical_tests)
if __name__=='__main__':
    check(3,7,physical=True);check(5,11,physical=True);check(7,29);check(11,23,False)
