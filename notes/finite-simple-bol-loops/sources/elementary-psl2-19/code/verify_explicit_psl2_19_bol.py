"""Pure Python replay from frozen matrices alone; no NumPy, ATLAS, or builder imports."""
import base64,hashlib,json,sys,zlib
from collections import deque
from pathlib import Path
from random import Random
HASH='c5965e0fdc104b529bf3eac790bac48d83e1c8ef03d8cb04f284893eaeb53ddb'
Z=(0,0)
def add(v,h):
    a,b=v;c,d=h;z=~(a|b);y=~(c|d)
    return ((a&y)|(z&c)|(b&d),(b&y)|(z&d)|(a&c))
def sub(v,h):return add(v,h[::-1])
def pack(xs):
    a=b=0
    for i,v in enumerate(xs):
        if int(v)==1:a|=1<<i
        elif int(v)==2:b|=1<<i
        else:assert int(v)==0
    return a,b
def coef(v,j):return ((v[0]>>j)&1)+2*((v[1]>>j)&1)
def unit(i):return (1<<i,0)
def idm(n):return [unit(i) for i in range(n)]
def addbasis(p,v):
    a,b=v
    while a|b:
        h=(a|b)&-(a|b);j=h.bit_length()-1
        if b&h:a,b=b,a
        if j not in p:p[j]=(a,b);return True
        a,b=sub((a,b),p[j])
    return False
def span(vs):
    p={}
    for v in vs:addbasis(p,v)
    return [p[i] for i in sorted(p)]
def rank(vs):return len(span(vs))
def orth(vs,n):
    p={}
    for v in vs:addbasis(p,v)
    # Back-eliminate each new tall pivot from all smaller rows.
    ps=sorted(p)
    for k in reversed(ps):
        for j in ps:
            if j>=k:break
            h=coef(p[j],k)
            if h:p[j]=sub(p[j],p[k] if h==1 else p[k][::-1])
    out=[]
    for k in range(n):
        if k in p:continue
        v=unit(k)
        for j in ps:
            a=coef(p[j],k)
            if a:v=add(v,unit(j)[::-1] if a==1 else unit(j))
        out.append(v)
    assert len(out)+len(p)==n
    return out
def trans(M,n):
    return [pack(coef(v,j) for v in M) for j in range(n)]
def app(M,v):
    q=Z
    for a,b in enumerate(v,1):
        while b:
            k=b&-b;b^=k;t=M[k.bit_length()-1]
            q=add(q,t if a==1 else t[::-1])
    return q
def table(M):
    n=len(M);T=[]
    for l in range(0,n,4):
        rows=[Z]*256
        for a in range(16):
            for b in range(16):
                if not a&b:rows[a+16*b]=app(M[l:l+4]+[Z]*4,(a,b))
        T.append(rows)
    def run(v):
        a,b=v;q=Z
        for t in T:q=add(q,t[(a&15)|((b&15)<<4)]);a>>=4;b>>=4
        assert not a|b
        return q
    return run
def cp(a,b):return tuple(a[j] for j in b)
def group():
    n=20;one=tuple(range(n));u=tuple([(i+1)%19 for i in range(19)]+[19]);w=tuple([19]+[-pow(j,-1,19)%19 for j in range(1,19)]+[0]);r=tuple([4*j%19 for j in range(19)]+[19])
    T=[one];at={one:0};edges=[]
    for g in T:
        rr=[]
        for b in [u,w]:
            h=cp(b,g)
            if h not in at:at[h]=len(T);T.append(h)
            rr.append(at[h])
        edges.append(rr)
    assert len(T)==3420 and r in at
    rg=[at[cp(r,g)] for g in T]
    I=[g for g in T if cp(g,g)==one];B=[g for g in T if g[19]==19]
    R=[one]
    for _ in range(8):R.append(cp(r,R[-1]))
    assert len(I)==172 and len(B)==171 and cp(r,R[-1])==one and set(R)<=set(B)
    inv={b:tuple(b.index(j) for j in one) for b in B}
    orbit={(cp(cp(b,w),inv[b]),cp(cp(b,rr),inv[b])) for b in B for rr in R[1:]}
    real={(i,b) for i in I for b in B if b!=one and cp(cp(i,b),i)==inv[b]}
    assert orbit==real and len(real)==1368
    assert len({cp(cp(b,w),inv[b]) for b in B})==171
    print("PSL2(19) 3420 actual projective permutations; B=171; 1368 true nonvertical inverters in eight B-orbits.") 
    return edges,rg
def representation(M,edges,rg):
    n=len(M['u']);U,W,R=[table(M[g]) for g in 'uwr']
    p={};used=0;rng=Random(17390+n)
    while len(p)<n:
        if used<5:seed=pack(rng.randrange(3) for i in range(n))
        else:seed=unit(next(i for i in range(n) if i not in p))
        # Test all two-generator and r edges on a cyclic vector. Their orbit
        # spans an actual T-module because every defining relation fixes its
        # entire orbit. Continue until the tested orbits span all coordinates.
        orbit=[None]*3420;orbit[0]=seed
        for j,(a,b) in enumerate(edges):
            v=orbit[j];assert v is not None
            for i,y in [(a,U(v)),(b,W(v))]:
                if orbit[i] is None:orbit[i]=y
                else:assert orbit[i]==y
        for j,v in enumerate(orbit):assert R(v)==orbit[rg[j]]
        for v in orbit:addbasis(p,v)
        used+=1;assert used<=n+5
    print("Whole group action degree %d checked on spanning cyclic vectors: %d."%(n,used))
def sumM(A,B):return [add(a,b) for a,b in zip(A,B)]
def negM(A):return [v[::-1] for v in A]
def comp(A,B):return [app(A,v) for v in B]
def cat(x,y,n):return x[0]|(y[0]<<n),x[1]|(y[1]<<n)
def pw(A,n):
    I=idm(len(A))
    for j in range(n):I=comp(A,I)
    return I
def run(data):
    def fromrows(k):
        rows=data[k];h=len(rows[0]);assert len(rows)>0 and all(len(r)==h for r in rows)
        return trans([pack(s) for s in rows],h)
    X={k:fromrows('X'+k) for k in 'uwr'};Y={k:fromrows('Y'+k) for k in 'uwr'};f=fromrows('f');d=fromrows('d')[0]
    nx,ny=117,119;assert all(len(A)==nx for A in X.values()) and all(len(A)==ny for A in Y.values()) and len(f)==nx
    ed,rg=group();representation(X,ed,rg);representation(Y,ed,rg)
    assert all(comp(f,X[t])==comp(Y[t],f) for t in 'ur') and app(Y['u'],d)==d
    dj=[Z];dt=d
    for i in range(9):dj.append(add(dj[-1],dt));dt=app(Y['r'],dt)
    assert dj[-1]==Z
    ex=sumM(idm(nx),negM(X['w']));ey=sumM(idm(ny),negM(Y['w']));EX=span(ex);EY=span(ey)
    assert [len(EX),len(EY),rank(comp(ey,comp(f,EX))) ]==[58,60,58]
    F=sumM(f,comp(Y['w'],comp(f,X['w'])));C=F+sumM(pw(Y['r'],3),negM(idm(ny)))
    a3=sub(app(pw(Y['r'],6),dj[3]),app(Y['w'],dj[3]));assert rank(C)==116 and rank(C+[a3])==117
    print("Full vertical injection 58/58, minus surplus 60-58=2; actual bottom compressed ranks 116 -> 117.")
    # Genuine unsimplified equations (1+k b)(c+k(x,f(x)+d_j))=0,
    # with c an arbitrary representative of (1-k)V and k=zw.
    KX=X['w'];KY=negM(Y['w']);dv=nx+ny;kk=[cat(v,Z,nx) for v in KX]+[cat(Z,v,nx) for v in KY]
    dirs=sumM(idm(dv),negM(kk))+[cat(app(KX,unit(i)),app(KY,f[i]),nx) for i in range(nx)]
    out=[]
    for j in range(1,9):
        nu=[cat(v,Z,nx) for v in comp(KX,pw(X['r'],j))]+[cat(Z,v,nx) for v in comp(KY,pw(Y['r'],j))]
        op=table(sumM(idm(dv),nu));space=[op(v) for v in dirs]
        q=op(cat(Z,app(KY,dj[j]),nx));v=rank(space);z=rank(space+[q]);assert z==v+1
        out.append((v,z))
    print("Eight full unsimplified marked-square obstruction ranks:",out)
    # Explicit failure of the right alternative law: x=wH, y=e_0 in Y.
    # The true representative of y*x is (a,i), i=r^8 w, a=y-i d(r^8).
    ii=comp(pw(Y['r'],8),Y['w']); iD=app(ii,dj[8]); a=sub(unit(0),iD)
    assert app(ii,a)==a and coef(sub(iD[::-1],dj[8]),1)==1
    print("Actual right-alternative failure at x=wH, y=e_0: residual coordinate 1 equals 1.")
    # Contrasts: zero cocycle kills the actual bottom rank gain; zero graph
    # map loses all 58 vertical dimensions even though the two sign sizes agree.
    assert rank(C+[Z])==116 and rank(comp(ey,comp([Z]*nx,EX)))==0
    def core(rows,M):
        n=len(M['u']);p={};Q=deque()
        for row in rows:
            if addbasis(p,row):Q.append(row)
        U,W=[table(trans(M[g],n)) for g in 'uw']
        while Q:
            t=Q.popleft()
            for v in (U(t),W(t)):
                if addbasis(p,v):Q.append(v)
        return orth(p.values(),n)
    U=EX; b=comp(ey,f);Fe=table(trans(ey,ny));Ft=table(trans(f,ny));trace=[]
    while True:
        Z0=core([Fe(s) for s in orth(comp(b,U),ny)],Y)
        J=core([Ft(s) for s in orth(Z0,ny)],X)
        V=span(comp(ex,J));trace.append((len(U),len(V),len(J),len(Z0)))
        if len(V)==len(U):break
        U=V
    assert trace==[(58,0,0,20),(0,0,0,0)]
    def coin(M):
        n=len(M['u'])
        return orth(sumM(M['u'],negM(idm(n)))+sumM(M['w'],negM(idm(n))),n)
    tx,ty=coin(X),coin(Y);assert not tx and len(ty)==1
    cy=trans(ty,ny);assert rank(comp(cy,f+[d]))==1
    print("All-cut descent (old,new,J,Z):",trace,"; trivial quotient dimensions 0,1 and stabilizer central rank one.")
    print("PASS; this proof checks the supplied finite input, not historical novelty or unrestricted classification.")
if __name__=='__main__':
    p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'evidence/psl2-19-explicit-matrix-input.json.zlib.b64'
    a=p.read_bytes();raw=a if a[:1]==b'{' else zlib.decompress(base64.b64decode(a))
    assert hashlib.sha256(raw).hexdigest()==HASH
    run(json.loads(raw))
