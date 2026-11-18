"""Regenerate one concrete finite matrix datum from four hash-pinned ATLAS files. Requires NumPy."""
import argparse,hashlib,json,re
from math import comb
from pathlib import Path
import numpy as np
HASH={"f9r9aB0.g1":"7927140ce59b3187a861d4cde606ba417aabac7a2cbacb59e3b74ad245a76be2","f9r9aB0.g2":"8e73ac8d0ad3769e65a4f90106983551cf76731743599e4f6ebadfa7598f8dd8","p20B0.g1":"219f295fac0d6dac9e9b3f77120bcde3030edc66a570e87afe48a0c0cf1be3c5","p20B0.g2":"404579d642dd8f1f0f84e92f51495086de8c97f838776656c432a0c9cfe2abae"}
inf=19;ID2=(1,0,0,1);r=(2,0,0,10);w=(0,-1,1,0);u=(1,1,0,1)
def mul(X,Y):
    a,b,c,d=X;e,f,g,h=Y
    return tuple(i%19 for i in (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h))
def inverse(X):
    a,b,c,d=X;return d,-b,-c,a
def site(X,i):
    a,b,c,d=X;A,B=(a,c) if i==inf else (a*i+b,c*i+d)
    return A*pow(B,-1,19)%19 if B%19 else inf
def chart(X):
    frame={i:(i,-1,1,0) for i in range(19)};frame[inf]=ID2
    log={pow(4,j,19):j for j in range(9)}
    p=[]
    for i in range(20):
        j=site(X,i);h=mul(mul(inverse(frame[j]),X),frame[i])
        assert h[2]==0;p.append((j,log[h[0]**2%19]))
    return p
CR,CW,CU=map(chart,(r,w,u))
assert all(j==(i+1)%19 and h==0 for i,(j,h) in enumerate(CU[:19])) and CU[19]==(19,0)
assert all(h==8 for i,(j,h) in enumerate(CR[:19])) and CR[19]==(19,1)
def transports():
    Q=[ID2];seen={ID2};pairs={}
    for g in Q:
        y,x=site(g,19),site(g,0)
        if (y,x) not in pairs:
            C=chart(g);pairs[y,x]=(C[19][1]+C[0][1])%9
        for a in (u,w):
            v=mul(a,g);neg=tuple(-i%19 for i in v);v=min(v,neg)
            if v not in seen:seen.add(v);Q.append(v)
        if len(pairs)==380:break
    assert len(pairs)==380
    return pairs
def I(n):return np.eye(n,dtype=np.int32)
def rref(A):
    M=A.copy()%3;n,m=M.shape;i=0;ps=[]
    for j in range(m):
        if i==n:break
        picks=np.flatnonzero(M[i:,j])
        if not len(picks):continue
        k=i+picks[0];M[[i,k]]=M[[k,i]];M[i]=M[i]*M[i,j]%3
        c=M[:,j].copy();c[i]=0;M=(M-c[:,None]*M[i])%3;ps.append(j);i+=1
    return M,ps
def col(A):return A[:,rref(A)[1]]
def rank(A):return len(rref(A)[1])
def null(A):
    R,P=rref(A);n=A.shape[1];free=[j for j in range(n) if j not in P];N=I(n)[:,free]
    if P:N[P,:]=-R[:len(P),free]%3
    return N
def pm(A,k):
    B=I(len(A))
    while k:
        if k&1:B=B@A%3
        k//=2
        if k:A=A@A%3
    return B
def ico(W):
    rows=rref(W.T)[1];A=W[rows];inv=rref(np.column_stack([A,I(len(A))]))[0][:,len(A):]
    def co(V):return inv@V[rows]%3
    assert np.array_equal(co(W),I(W.shape[1]));return co
def signed(k,sign,pairs):
    n=20*k;A=np.zeros((n,n),dtype=np.int32)
    def act(C):
        m=np.zeros((n,n),dtype=np.int32)
        for x,(y,l) in enumerate(C):
            for a in range(k):
                for b in range(a,k):m[k*y+b,k*x+a]=comb(l,b-a)%3
        return m
    for (y,x),v in pairs.items():
        for a in range(k):
            for b in range(a,k):A[k*y+b,k*x+a]=(-1)**a*comb((v-a)%9,b-a)%3
    M={i:act(C) for i,C in zip(('r','w','u'),(CR,CW,CU))}
    for v in M.values():assert np.array_equal(A@v%3,v@A%3)
    H=pm(A,9);assert np.array_equal(H@H%3,I(n))
    W=col((I(n)+sign*H)%3);co=ico(W);D={i:co(z@W%3) for i,z in M.items()}
    assert all(np.array_equal(W@D[i]%3,M[i]@W%3) for i in M)
    return D
def simple18(mode):
    # F9=F3[t]/(t^2+2*t+2); t^2=t+1. The ATLAS supplies row actions.
    def mul9(x,y):
        a,b=x%3,x//3;c,d=y%3,y//3
        return (a*c+b*d)%3+3*((a*d+b*c+b*d)%3)
    powers=[1]
    for j in range(8):powers.append(mul9(3,powers[-1]))
    assert len(set(powers[:8]))==8 and powers[8]==1
    mats={};perms={}
    for key,h in HASH.items():
        src=(Path(mode)/('L219G1-'+key)).read_bytes()
        assert hashlib.sha256(src).hexdigest()==h
        t=src.decode();n=int(key[-1])
        if key.startswith('p20'):
            a=list(range(20))
            for cycle in re.findall(r'\(([\d,]+)\)',t):
                c=[int(x)-1 for x in cycle.split(',')]
                for i,j in zip(c,c[1:]+c[:1]):a[i]=j
            perms[n]=tuple(a)
        else:
            ds=[0 if k.startswith('0') else powers[int(k.split('^')[-1])%8]
                for k in re.findall(r'(?:0\*Z\(9\)|Z\(9\)\^\d+)',t)]
            assert len(ds)==81
            rows=[ds[i:i+9] for i in range(0,81,9)]
            mats[n]=np.array([[j for v in row for j in (mul9(scale,v)%3,mul9(scale,v)//3)]
                for row in rows for scale in (1,3)],dtype=np.int32).T
    cp=lambda a,b:tuple(a[i] for i in b)
    a,b=perms[1],perms[2]; one=tuple(range(20)); Q=[one]; words={one:()}
    for h in Q:
        for l,g in [(1,a),(2,b)]:
            n=cp(g,h)
            if n not in words:Q.append(n);words[n]=words[h]+(l,)
    assert len(Q)==3420
    u=cp(a,b);w=a;inf=next(i for i in one if u[i]==i);s=[w[inf]]
    for i in range(18):s.append(u[s[-1]])
    assert len(set(s))==19 and all(w[s[j]]==s[-pow(j,-1,19)%19] for j in range(1,19))
    r=list(one)
    for i,t in enumerate(s):r[t]=s[4*i%19]
    r=tuple(r)
    def rep(g):
        M=I(18)
        for l in words[g]:M=mats[l]@M%3
        return M
    return {k:rep(g) for k,g in [('u',u),('r',r),('w',w)]}
def prep(X):
    n=len(X['u']);t=(X['r']-I(n))%3;u=X['u']
    nu=sum((pm(u,j) for j in range(19)),np.zeros((n,n),dtype=np.int32))%3
    fx=col(nu);mov=col((I(n)-nu)%3);gy=mov@null(t@mov%3)%3
    k=fx.shape[1];tags=[];basis=[];top=None
    if k:
        H=pm(t,k-1);top=next(v for v in fx.T if (H@v%3).any());v=top
        for _ in range(k):basis.append(v);v=t@v%3
        assert not v.any();tags.append(('I',k))
    W=np.stack(basis,axis=1) if basis else np.zeros((n,0),dtype=np.int32);r0=rank(W)
    for v in gy.T:
        if rank(np.column_stack([W,v]))==r0:continue
        for _ in range(18):basis.append(v);v=u@v%3
        W=np.stack(basis,axis=1);assert rank(W)==r0+18;r0+=18;tags.append(('D',18))
    assert W.shape==(n,n);return t,fx,gy,top,tags,ico(W)(I(n))
def maps(X,Y,XX,YY):
    tx,fx,gx,hx,tags,inv=XX;ty,fy,gy,hy,_,_=YY
    out=[];start=0
    for name,k in tags:
        G=fy@null(pm(ty,k)@fy%3)%3 if name=='I' else gy
        for g in G.T:
            A=np.zeros((len(ty),len(tx)),dtype=np.int32);v=g
            for j in range(k):A[:,start+j]=v;v=(ty if name=='I' else Y['u'])@v%3
            f=A@inv%3;assert all(np.array_equal(f@X[i]%3,Y[i]@f%3) for i in ('u','r'));out.append(f)
        start+=k
    return np.stack(out)
def block(A,B):return np.block([[A,np.zeros((A.shape[0],B.shape[1]),dtype=np.int32)],[np.zeros((B.shape[0],A.shape[1]),dtype=np.int32),B]])
def build(mode):
    pairs=transports();X0=signed(9,-1,pairs);X1=simple18(mode);Y0=signed(3,-1,pairs);Y1=signed(8,1,pairs)
    xx=[prep(t) for t in (X0,X1)]; yy=[prep(t) for t in (Y0,Y1)]
    coeffs=('11200012012111111121222120202012112222210200001101210211021000012112210','011021112112')
    pv=[np.array([int(t) for t in s],dtype=np.int32) for s in coeffs]
    parts=[]
    for x,pre,coeff in zip([X0,X1],xx,pv):
        zz=0;partsY=[]
        for y,pte in zip([Y0,Y1],yy):
            gg=maps(x,y,pre,pte);partsY.append(np.tensordot(coeff[zz:zz+len(gg)],gg,axes=1)%3);zz+=len(gg)
        assert zz==len(coeff);parts.append(np.vstack(partsY))
    f=np.hstack(parts);d=np.r_[yy[0][3],np.zeros(len(Y1['u']),dtype=np.int32)]
    X={g:block(X0[g],X1[g]) for g in X0};Y={g:block(Y0[g],Y1[g]) for g in Y0}
    return X,Y,f,d
def data(X,Y,f,d):
    mm={'Xu':X['u'],'Xw':X['w'],'Xr':X['r'],'Yu':Y['u'],'Yw':Y['w'],'Yr':Y['r'],'f':f,'d':d[:,None]}
    return {k:[''.join(str(a) for a in row) for row in v] for k,v in mm.items()}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('atlas_directory');p.add_argument('output_json')
    a=p.parse_args();raw=(json.dumps(data(*build(a.atlas_directory)),separators=(',',':'))+'\n').encode()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='c5965e0fdc104b529bf3eac790bac48d83e1c8ef03d8cb04f284893eaeb53ddb'
    Path(a.output_json).write_bytes(raw);print('Canonical JSON:',len(raw),'bytes, SHA256',digest)
