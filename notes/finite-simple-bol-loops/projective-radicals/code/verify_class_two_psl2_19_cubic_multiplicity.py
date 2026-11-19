#!/usr/bin/env python3
"""Native nonlinear class-two controls. Requires numpy; run from the code directory.
The earlier chain's published row-reduction routines are reused. Brackets, physical
group products, simultaneous couplings, all native torus collision tests after
central projection and ordinary loop operations on two actual blocks are new."""
import base64,hashlib,json,sys,zlib
from pathlib import Path
import numpy as np
from verify_psl2_19_infinite_chain import I,ref,rank,col,null,block,pw,modules,fix,check,widen,HASH
def cat(*A):return np.concatenate(A,axis=0)
def z(n):return np.zeros(n,dtype=np.int32)
def pmat(B):return np.array([list(map(int,s)) for s in B],np.int32)
def make(D,s):
    M=modules();X={g:pmat(D['X'+g]) for g in 'urw'};Y={g:pmat(D['Y'+g]) for g in 'urw'}
    f=pmat(D['f']);d=pmat(D['d']);F=(f+Y['w']@f@X['w'])%3
    D3=(I(len(d))+Y['r']+pw(Y['r'],2))@d%3
    sep=null(np.column_stack((F,pw(Y['r'],3)-I(len(d)))).T).T
    sep=sep@(I(len(d))-Y['w'])%3
    phi=next(v for v in sep if int((v@(I(len(d))-Y['w'])@D3)[0])%3)
    phi=phi*int((phi@(I(len(d))-Y['w'])@D3)[0])%3
    assert (phi@(I(len(d))-Y['w'])@D3%3)[0]==1
    def batch(n,report):
        nonlocal X,Y,f,d,phi
        B=fix(Y,'r')
        U=[I(len(Y['u']))]
        for _ in range(18):U.append(Y['u']@U[-1]%3)
        constraints=(I(19)-M['w']).T@np.vstack([phi@u for u in U])@B%3
        good=B@null(constraints)%3
        bad=col(np.column_stack((f@(X['w']-I(len(X['w'])))@fix(X,'ur')%3,
                                (Y['w']-I(len(Y['w'])))@fix(Y,'ur')%3)))
        A=[];span=bad
        for v in good.T:
            if rank(np.column_stack((span,v)))>span.shape[1]:
                span=np.column_stack((span,v)); A.append(np.column_stack([u@v%3 for u in U]))
                if len(A)==n:break
        assert len(A)==n and rank(constraints)<=7
        assert all(not ((phi@(a+Y['w']@a@M['w']))%3).any() for a in A)
        print(report,"available/constrained/bad/selected",B.shape[1],good.shape[1],bad.shape[1],n)
        f=widen(f,np.column_stack(A));d=cat(d,np.zeros((19*n,1),np.int32));phi=cat(phi,z(19*n))
        for _ in range(n):
            X={g:block(X[g],M[g]) for g in X};Y={g:block(Y[g],M[g]) for g in Y}
    for i in range(s):batch(1,"passive"+str(i+1))
    batch(s,"active batch")
    old,new,steps=check(X,Y,f,d,2*s)
    assert not ((phi@(f+Y['w']@f@X['w']))%3).any() and not(phi[119:]%3).any()
    assert not (phi@(pw(Y['r'],3)-I(len(d)))%3).any()
    print("frozen additive cut control",s,old,new,steps)
    return M,X,Y,f,d[:,0],phi

def beta(x,y):
    # dot/multiply in all 20 physical positions; return first 19.
    x0=-x.sum()%3;y0=-y.sum()%3;xy=x*y%3
    return (xy-(xy.sum()+x0*y0)*2)%3
class Native:
    def __init__(self,datum,s,C):
        self.M,self.X,self.Y,self.f,self.d,self.phi=datum;self.s=s;self.C=np.array(C,np.int32)
        self.nx=nx=self.f.shape[1];self.ny=ny=self.f.shape[0];self.n=nx+ny
        self.z=z(self.n); self.offx=117+19*s;self.offy=119+19*s
        self.mx={};self.my={}
        for j in range(9):
            for w in [0,1]:
                self.mx[j,w]=pw(self.X['r'],j)@(self.X['w'] if w else I(nx))%3
                self.my[j,w]=pw(self.Y['r'],j)@(self.Y['w'] if w else I(ny))%3
        self.ds=[z(ny)]
        for j in range(9):self.ds.append((self.ds[-1]+self.my[j,0]@self.d)%3)
        assert not self.ds[-1].any()
        self.dmaps={}
    def bracket(self,v,w):
        t=self.s
        x=v[self.offx:self.nx].reshape(t,19); y=v[self.nx+self.offy:].reshape(t,19)
        a=w[self.offx:self.nx].reshape(t,19); b=w[self.nx+self.offy:].reshape(t,19)
        out=z(self.n);U=out[self.nx+119:self.nx+self.offy].reshape(t,19)
        for j in range(t):
            for l in range(t):U+=self.C[:,j,l,None]*(beta(x[j],b[l])-beta(a[j],y[l]))
        return out%3
    def coremul(self,v,w):return (v+w+2*self.bracket(v,w))%3
    def act(self,g,v):
        i,w,sg=g
        return cat(self.mx[i,w]@v[:self.nx],(-1)**sg*(self.my[i,w]@v[self.nx:]))%3
    def gm(self,g,h):
        i,w,a=g;j,t,b=h;return ((i+(-1)**w*j)%9,w^t,a^b)
    def mul(self,k,h):
        v,g=k;u,j=h
        return (self.coremul(v,self.act(g,u)),self.gm(g,j))
    def inv(self,k):
        v,(i,w,sg)=k;g=(-(-1)**w*i%9,w,sg);return (self.act(g,-v),g)
    def eq(self,k,h):return k[1]==h[1] and np.array_equal(k[0]%3,h[0]%3)
    def H(self,x,j):return (cat(x,(self.f@x+self.ds[j])%3),(j,0,0))
    def inH(self,v):
        u,(j,w,sg)=v
        return not w and not sg and np.array_equal(u[self.nx:]%3,(self.f@u[:self.nx]+self.ds[j])%3)
    def mark(self,i,w,rng,as_sign=False):
        raw=rng.integers(0,3,self.n,dtype=np.int32);sg=(i,w,1)
        v=(raw-self.act(sg,raw))%3
        # z Lambda multiplies the vector by z, but z permutes this
        # entire eigenspace, so v can be used directly in either sheet.
        return (v,(i,w,int(as_sign)))
    def pre_linear(self,i,w):
        g=(i,w);X=self.mx[g];Y=self.my[g]
        ap=I(self.nx)+X;am=I(self.ny)-Y
        A=np.vstack([ap,am@self.f])%3;rows=ref(A.T)[1]
        assert len(rows)==self.nx
        rr,piv=ref(np.column_stack([A[rows],I(self.nx)]));assert piv==list(range(self.nx))
        self.dmaps[g]=(ap,am,A,rows,rr[:,self.nx:])
    def reduced(self,k,with_stats=False):
        n,g=k;good=[];nonlinear=0
        for i,w in ([(0,0)] if not g[1] else [(i,1) for i in range(9)]):
            ig=(i,w,0);jh=self.gm(ig,g);assert jh[1:]==(0,0)
            if (i,w) not in self.dmaps:self.pre_linear(i,w)
            ap,am,A,rows,L=self.dmaps[i,w];X=self.mx[i,w];Y=self.my[i,w]
            # First solve the *two opposite high signs* for the common
            # active H input. This determines the entire central BCH error.
            highx=n[self.offx:self.nx];highy=n[self.nx+self.offy:]
            hi=X[self.offx:,self.offx:]
            sw=(2*((I(len(hi))+hi)@highx+(I(len(hi))-hi)@highy))%3
            hv=z(self.n);hv[self.offx:self.nx]=sw;hv[self.nx+self.offy:]=sw
            kv=z(self.n);kv[self.offx:self.nx]=(highx-sw)%3;kv[self.nx+self.offy:]=(highy-sw)%3
            corr=2*self.bracket(kv,hv)%3
            u=(n-corr)%3
            rhs=cat(ap@u[:self.nx],-am@(u[self.nx:]-Y@self.ds[jh[0]]))%3
            x=L@rhs[rows]%3
            if (A@x%3!=rhs).any():continue
            h=self.H(x,jh[0]);v=(u-self.act(ig,h[0]))%3
            out=(v,ig)
            assert np.array_equal(self.act((i,w,1),v),-v%3)
            assert self.eq(self.mul(out,h),k) and self.inH(self.mul(self.inv(out),k))
            good.append(out);nonlinear+=corr.any()
        assert len(good)==1,(len(good),g)
        return (good[0],nonlinear) if with_stats else good[0]
    def star(self,a,b):return self.reduced(self.mul(a,b))
    def all_proj(self):
        # Test exact simultaneous affine square system on quotient by ALL
        # passive-minus outputs; this is a negative-sufficiency test only.
        ix=np.r_[np.arange(119),np.arange(self.offy,self.ny)]
        X=self.X;Y={g:m[np.ix_(ix,ix)] for g,m in self.Y.items()};f=self.f[ix];nx=self.nx;ny=len(ix)
        mu=block(X['w'],-Y['w'])%3;Id=I(nx+ny);W=np.vstack([I(nx),f])
        checks=[]
        for j in range(1,9):
            nu=mu@block(self.mx[j,0],self.my[j,0][np.ix_(ix,ix)])%3
            A=(Id+nu)@np.column_stack([Id-mu,mu@W])%3
            c=(Id+nu)@mu@cat(z(nx),self.ds[j][ix])%3
            k=rank(A);l=rank(np.column_stack([A,c]));assert l==k+1;checks.append(k)
        return checks
    def physical(self,rng,iters):
        C=self.C;s=self.s;changed=corrections=signphase=0
        for _ in range(iters):
            R=lambda n:rng.integers(0,3,n,dtype=np.int32)
            a,b,c=[R(self.n) for _ in range(3)]
            assert np.array_equal(self.coremul(a,self.coremul(b,c)),self.coremul(self.coremul(a,b),c))
            assert not self.coremul(self.coremul(a,a),a).any()
            for g in [(1,0,0),(0,1,0),(0,0,1)]:
                assert np.array_equal(self.act(g,self.coremul(a,b)),self.coremul(self.act(g,a),self.act(g,b)))
            h=self.H(R(self.nx),int(rng.integers(9)));h2=self.H(R(self.nx),int(rng.integers(9)))
            assert self.inH(self.mul(h,h2)) and self.inH(self.inv(h))
            i=int(rng.integers(9));sg=self.mark(i,1,rng,True)
            assert self.eq(self.mul(sg,sg),(self.z,(0,0,0)))
            vertical=self.H(R(self.nx),0)
            sg_conj=self.mul(self.mul(sg,vertical),sg)
            signphase+=not np.array_equal(sg_conj[0],self.act(sg[1],vertical[0]))
            marks=[self.mark(int(rng.integers(9)),1,rng) if rng.integers(3) else self.mark(0,0,rng) for _ in range(3)]
            a,b,c=marks;ab=self.mul(a,b);o,n=self.reduced(ab,True);corrections+=n
            changed+=not np.array_equal(ab[0],(a[0]+self.act(a[1],b[0]))%3)
            assert self.eq(self.star(a,self.star(b,self.star(a,c))),self.star(self.star(a,self.star(b,a)),c))
        assert min(changed,corrections,signphase)>0
        return int(changed),int(corrections),int(signphase)
def main():
    src=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'evidence/psl2-19-explicit-matrix-input.json.zlib.b64'
    b=zlib.decompress(base64.b64decode(src.read_bytes()));assert hashlib.sha256(b).hexdigest()==HASH
    M=modules();rng=np.random.default_rng(190619)
    bg=np.column_stack([beta(v,w) for v in I(19) for w in I(19)]);assert rank(bg)==19
    for g in 'urw':
        for _ in range(15):
            a=rng.integers(3,size=19);b0=rng.integers(3,size=19)
            assert np.array_equal(M[g]@beta(a,b0)%3,beta(M[g]@a%3,M[g]@b0%3))
    for s,it in [(1,20),(2,22)]:
        ds=make(json.loads(b),s)
        C=[I(s)]
        if s==2:C.append(np.array([[0,1],[1,1]],np.int32))
        n=Native(ds,s,C)
        print("s =",s,"all eight actual quotient collision ranks (+1 each)",n.all_proj(),flush=True)
        print("s =",s,"native left Bol triples",it,"nonzero group/solve/conjugated-sign corrections",n.physical(rng,it),flush=True)
        if s==2:
            # Different arrays can be equivalent at the radical-tensor
            # level (so counting arrays as isotypes would be spurious).
            n2=Native(ds,2,[C[0],(C[0]+C[1])%3])
            for _ in range(12):
                a=rng.integers(3,size=n.n);v=rng.integers(3,size=n.n)
                u=n.bracket(a,v);t=n2.bracket(a,v);j=n.nx+119
                assert np.array_equal(u[j:j+19],t[j:j+19]) and np.array_equal((u[j:j+19]+u[j+19:j+38])%3,t[j+19:j+38])
    print("PASS: actual nonlinear products, conjugated outside signs, eight projected square obstructions and two-block native Bol operations.")
if __name__=='__main__':main()
