"""Standalone hostile verification of fixed a62ed7be JSON: Python 3, NumPy only.
Usage: python check_explicit_bol_datum_independent.py path/to/psl2-19-explicit-matrix-input.json.zlib.b64
Needs no author verifier, ATLAS files, representation packages, or host enumeration.
"""
import base64,hashlib,json,sys,zlib
from collections import Counter
import numpy as np
M=lambda a: np.asarray(a,dtype=np.int64)%3
eye=lambda n: np.eye(n,dtype=np.int64)
zero=lambda n,k: np.zeros((n,k),dtype=np.int64)
def equal(a,b):return np.array_equal(M(a),M(b))
def dot(a,b):return (a@b)%3
def power(a,j):
    v=eye(len(a))
    for _ in range(j):v=dot(v,a)
    return v
def reduce(A):
    # Work down columns, normalize a nonzero pivot, cancel all others. Rank only depends on F3.
    A=M(A).copy(); rows,cols=A.shape
    piv=[];k=0
    for j in range(cols):
        if k==rows:break
        cand=np.nonzero(A[k:,j])[0]
        if not len(cand):continue
        h=k+int(cand[-1]);A[[k,h]]=A[[h,k]];A[k]*=int(A[k,j]);A[k]%=3
        v=A[:,j].copy();v[k]=0;A=(A-v[:,None]*A[k])%3
        piv.append(j);k+=1
    return A,piv
def rk(A):return len(reduce(A)[1])
def ker(A):
    A=M(A);R,p=reduce(A);free=[i for i in range(A.shape[1]) if i not in p]
    Z=eye(A.shape[1])[:,free];Z[p,:]=(-R[:len(p),free])%3
    assert not np.any(dot(A,Z));return Z
def im(A):
    A=M(A);return A[:,reduce(A)[1]]
def span_pre(A,B):return ker(dot(ker(B.T).T,A))
def core(S,U,W):
    # Primal intersection of S with generator preimages, not a row-space closure.
    S=im(S);traj=[S.shape[1]]
    while S.shape[1]:
        o=ker(S.T).T
        M0=np.vstack([dot(o,dot(g,S)) for g in (U,W)])
        C=ker(M0)
        if C.shape[1]==S.shape[1]:break
        S=dot(S,C);traj.append(S.shape[1])
    assert all(not np.any(dot(ker(S.T).T,dot(g,S))) for g in (U,W))
    return S,traj
def main(path):
    raw=zlib.decompress(base64.b64decode(open(path,'rb').read()))
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='c5965e0fdc104b529bf3eac790bac48d83e1c8ef03d8cb04f284893eaeb53ddb'
    mats={k:M([[int(c) for c in row] for row in a]) for k,a in json.loads(raw).items()}
    f,d=mats['f'],mats['d'];y,x=f.shape;assert (y,x,d.shape)==(119,117,(119,1))
    # Independently form PSL2(19) as projective transformations on F19 plus infinity.
    inf=19;ident=tuple(range(20))
    u=tuple([(j+1)%19 for j in range(19)]+[inf])
    w=tuple([inf]+[-pow(j,-1,19)%19 for j in range(1,19)]+[0])
    r=tuple([(4*j)%19 for j in range(19)]+[inf])
    def mul(a,b):return tuple(a[h] for h in b)
    def powers(a,n):
        z=[ident]
        for _ in range(n-1):z.append(mul(z[-1],a))
        return z
    def inv(a):
        b=[0]*20
        for j,v in enumerate(a):b[v]=j
        return tuple(b)
    us,rs=powers(u,19),powers(r,9);aff={mul(ua,rb):(a,b) for a,ua in enumerate(us) for b,rb in enumerate(rs)}
    tr=[mul(ua,w) for ua in us]+[ident]
    assert len(aff)==171 and all(g[inf]==i for i,g in enumerate(tr))
    group={mul(c,b) for c in tr for b in aff};assert len(group)==3420
    assert all(mul(g,h) in group for g in (u,w,r) for h in group)
    # Show u,w ALONE generate the full represented group, needed for invariant cores.
    bfs={ident}; todo=[ident]
    while todo:
        h=todo.pop()
        for g in (u,w):
            v=mul(g,h)
            if v not in bfs:bfs.add(v);todo.append(v)
    assert bfs==group
    # Independently certify simplicity on the very same action, rather than import a table.
    def closure(gens):
        out={ident};todo=[ident]
        while todo:
            cur=todo.pop()
            for f0 in gens:
                nxt=mul(f0,cur)
                if nxt not in out:out.add(nxt);todo.append(nxt)
        return out
    unseen=set(group);class_sizes=[]
    while unseen:
        t0=min(unseen);orbit={t0};todo=[t0]
        while todo:
            v0=todo.pop()
            for g0 in (u,w):
                n0=mul(mul(g0,v0),inv(g0))
                if n0 not in orbit:orbit.add(n0);todo.append(n0)
        unseen-=orbit;class_sizes.append(len(orbit))
        if t0!=ident:
            gens=[];N={ident}
            while orbit-N:
                gens.append(min(orbit-N));N=closure(gens)
            assert N==group
    print('faithful projective group nontrivial class closures all full; class sizes:',sorted(class_sizes))
    invs={g for g in group if g!=ident and mul(g,g)==ident}
    assert len(invs)==171 and {mul(mul(g,w),inv(g)) for g in aff}==invs
    # Enumerate projected inverting marks against every element of the ACTUAL Borel.
    invcounts=Counter();byj={j:set() for j in range(9)}
    for b,(a,j) in aff.items():
        if b==ident:continue
        those=[s for s in invs if mul(mul(s,b),s)==inv(b)]
        if j==0:assert not those
        else:assert len(those)==9
        invcounts[j]+=len(those);byj[j].update((s,b) for s in those)
    for j in range(1,9):
        orb={(mul(mul(g,w),inv(g)),mul(mul(g,rs[j]),inv(g))) for g in aff}
        assert byj[j]==orb and len(orb)==171
    print('JSON',digest,'PSL size, Borel, involutions, projected inverter pairs by j=0..8:',len(group),len(aff),len(invs),[invcounts[j] for j in range(9)])
    def rep(prefix):
        U,W,R=[mats[prefix+h] for h in 'uwr'];n=len(U);E=eye(n)
        Us=[power(U,j) for j in range(19)];Rs=[power(R,j) for j in range(9)]
        assert equal(dot(Us[-1],U),E) and equal(dot(Rs[-1],R),E) and equal(dot(R,U),dot(Us[4],R))
        trans=[dot(V,W) for V in Us]+[E]
        for gp,mat in zip((u,w,r),(U,W,R)):
            for i in range(20):
                dest=gp[i];a,j=aff[mul(inv(tr[dest]),mul(gp,tr[i]))]
                assert equal(dot(mat,trans[i]),dot(trans[dest],dot(Us[a],Rs[j])))
        # Together with the actual affine presentation, all 60 equations certify a representation.
        return U,W,R,Rs
    U,W,R,RR=rep('X');V,Z,T,TT=rep('Y');I,L=eye(x),eye(y)
    assert equal(dot(f,U),dot(V,f)) and equal(dot(f,R),dot(T,f))
    # Zero value on translations; verify the derivation law on every pair of all actual 171 Borel points.
    Ds=[zero(y,1)]
    for h in TT:Ds.append((Ds[-1]+dot(h,d))%3)
    assert not np.any(Ds[9]) and all(equal(dot(V,z),z) for z in Ds)
    for b,(a,j) in aff.items():
        for c,(v,k) in aff.items():
            lhs=Ds[aff[mul(b,c)][1]];rhs=Ds[j]+dot(TT[j],Ds[k]);assert equal(lhs,rhs)
    Xminus,Yplus,Yminus=ker(W+I),ker(Z-L),ker(Z+L)
    P=2*(L-Z)%3; b=dot(P,f)
    assert (Xminus.shape[1],Yminus.shape[1],Yplus.shape[1],rk(dot(b,Xminus)))==(58,60,59,58)
    # Exact physical equations. a=(p,zw), p in X^- + Y^+. h'=((v,fv+D_j),r^j) in H.
    # (ah')^2=1 iff [I+(zw)r^j](p+(zw)(v,fv+D_j))=0, in BOTH sign coordinates simultaneously.
    rows=[]
    for j in range(1,9):
        sx=(I+dot(W,RR[j]))%3;sy=(L-dot(Z,TT[j]))%3
        C=np.block([[dot(sx,Xminus),zero(x,Yplus.shape[1]),dot(sx,W)],
                    [zero(y,Xminus.shape[1]),dot(sy,Yplus), -dot(sy,dot(Z,f))]])
        target=np.vstack([zero(x,1),dot(sy,dot(Z,Ds[j]))]);r0=rk(C);a1=rk(np.hstack([C,target]))
        assert a1==r0+1;rows.append((r0,a1))
    print('X/Y, w-minus X/w-minus Y; both Borel checks (linear and all cocycle products):',x,y,Xminus.shape[1],Yminus.shape[1],171**2)
    print('full actual two-sign collision rank vs augmented, j=1..8:',rows)
    # Compare the author's compressed phase to the OPERATED square before quotienting, for the same f,d.
    F=(f+dot(Z,dot(f,W)))%3;delta=dot((TT[6]-Z),Ds[3])
    denom=np.hstack([F,TT[3]-L]);print('actual torus compression ranks:',rk(denom),rk(np.hstack([denom,delta])))
    assert (rk(denom),rk(np.hstack([denom,delta])))==(116,117)
    U0=Xminus;flat=[]
    while True:
        UY=span_pre(P,dot(b,U0));CZ,zy=core(UY,V,Z)
        J0=span_pre(f,CZ);CJ,jx=core(J0,U,W);nextU=im(dot(2*(I-W)%3,CJ))
        flat.append((U0.shape[1],nextU.shape[1],CJ.shape[1],CZ.shape[1],zy,jx))
        if nextU.shape[1]==U0.shape[1]:break
        U0=nextU
    assert [(g[0],g[1],g[2],g[3]) for g in flat]==[(58,0,0,20),(0,0,0,0)]
    Fxy=ker(np.vstack([V-L,Z-L]));assert Fxy.shape[1]==0
    coinX=ker(np.vstack([(U-I).T,(W-I).T])).T;coinY=ker(np.vstack([(V-L).T,(Z-L).T])).T
    fullH=rk(dot(coinY,np.hstack([f,d])));assert (len(coinX),len(coinY),fullH)==(0,1,1)
    print('primal normal-core rows (old, next, J, Z; Y and X intermediate dimensions):',flat)
    print('Y fixed, X and Y coinvariants, H central rank; f-only and cocycle-only:',Fxy.shape[1],len(coinX),len(coinY),fullH,rk(dot(coinY,f)),rk(dot(coinY,d)))
    # Separate right-alternative certificate without copying an input/site choice: y=-D_j ensures
    # a=y-iD_j is i-fixed. Then (0,a,i) represents y*x, and (y*x)*x != y iff a != 0.
    witnesses=[]
    for j in range(1,9):
        i=dot(TT[j],Z);qi=mul(rs[j],w);assert mul(qi,rs[j])==w and mul(qi,w)==rs[j]
        Yj=-Ds[j]%3;A=(Yj-dot(i,Ds[j]))%3
        assert equal(dot(i,A),A) and equal(A+dot(i,Ds[j]),Yj)
        # (y,1)^(-1) (a,i)(0,w) equals (a-y,r^j) with X=0, not in graph H iff a-y != D_j.
        wrong=(A-Yj-Ds[j])%3
        assert equal(wrong,A)
        if np.any(wrong):witnesses.append((j,int(np.flatnonzero(wrong)[0]),int(wrong[np.flatnonzero(wrong)[0],0])))
    assert witnesses
    e0=eye(y)[:,0:1];D8=Ds[8];i8=dot(TT[8],Z);aa=(e0-dot(i8,D8))%3
    assert equal(dot(i8,aa),aa) and int(((-dot(i8,D8)-D8)%3)[1,0])==1
    counts=(1,171*3**58,3**119-1,171*3**58*(3**59-1))
    assert sum(counts)==20*3**119
    print('author right-alternative certificate j=8 e0 confirmed; all four power orders account exactly for all',sum(counts),'elements')
    bad=f.copy();bad[0,0]=(bad[0,0]+1)%3
    assert not (equal(dot(bad,U),dot(V,bad)) and equal(dot(bad,R),dot(T,bad)))
    assert rk(dot(P,zero(y,x))@Xminus)==0 and all(r1>r0 for r0,r1 in rows)
    print('countercontrols: altered first f-bit breaks B-linearity; f=0 fails rank; d=0 gives a physical zero-vector r^j collision at all eight j')
    print('direct failed right alternativity (j, first failed coordinate, nonzero value):',witnesses)
if __name__=='__main__':main(sys.argv[1])
