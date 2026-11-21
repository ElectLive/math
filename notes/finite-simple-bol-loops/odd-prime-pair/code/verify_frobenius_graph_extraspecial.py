"""Independent construction controls (author), Python 3 with numpy for prime-field arrays."""
import itertools,math
import numpy as np
class Field:
    def __init__(self,p,poly):
        self.p=p;self.f=len(poly)-1;self.poly=poly[:-1];self.n=p**self.f;self.one=(1,)+(0,)*(self.f-1);self.zero=(0,)*self.f
        self.e=[tuple(int(i==j) for i in range(self.f)) for j in range(self.f)]
    def add(self,a,b):return tuple((x+y)%self.p for x,y in zip(a,b))
    def neg(self,a):return tuple(-x%self.p for x in a)
    def mul(self,a,b):
        f=self.f;p=self.p;c=[0]*(2*f-1)
        for i,u in enumerate(a):
            if u:
                for j,v in enumerate(b):c[i+j]+=u*v
        for j in range(f-2,-1,-1):
            z=c[j+f]%p
            if z:
                for i,v in enumerate(self.poly):c[i+j]-=z*v
        return tuple(x%p for x in c[:f])
    def pw(self,a,n):
        if n<0:n%=self.n-1
        r=self.one
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n//=2
        return r
    def tr(self,a):
        acc=self.zero
        for i in range(self.f):acc=self.add(acc,a);a=self.pw(a,self.p)
        assert not any(acc[1:]);return acc[0]
    def primitive(self):
        n=self.n-1;v=n;pr=[];u=2
        while u*u<=v:
            if v%u==0:
                pr.append(u)
                while v%u==0:v//=u
            u+=1
        if v>1:pr.append(v)
        for k in range(2,self.n):
            a=tuple((k//self.p**j)%self.p for j in range(self.f))
            if all(self.pw(a,n//d)!=self.one for d in pr):return a
        raise ValueError()

def rank(a,p):
    a=np.array(a,dtype=np.int64).copy()%p;h=0
    for j in range(a.shape[1]):
        i=next((i for i in range(h,a.shape[0]) if a[i,j]),None)
        if i is None:continue
        a[[i,h]]=a[[h,i]];a[h]=a[h]*pow(int(a[h,j]),-1,p)%p
        val=a[:,j].copy();val[h]=0;a=(a-val[:,None]*a[h])%p;h+=1
    return h

def invert(a,p):
    h=len(a);b=np.concatenate((a%p,np.eye(h,dtype=np.int64)),axis=1)
    for j in range(h):
        i=next(i for i in range(j,h) if b[i,j]);b[[i,j]]=b[[j,i]]
        b[j]=b[j]*pow(int(b[j,j]),-1,p)%p
        v=b[:,j].copy();v[j]=0;b=(b-v[:,None]*b[j])%p
    return b[:,h:]

def run(q,poly,is_,geom):
    p=3;k=Field(p,poly);f=k.f;d=p*f;P=k.n-1;e=k.primitive();z=k.pw(e,P//q);assert k.pw(z,q)==k.one and z!=k.one
    c=k.add(z,k.neg(k.pw(z,p**(f//2))));assert c!=k.zero and k.pw(c,p**(f//2))==k.neg(c)
    alpha=next(a for a in range(2,q) if pow(a,p,q)==1); eye=np.eye(d,dtype=np.int64)
    n=p**(f//2)-1;n0=k.pw(e,p**(f//2)+1);logs={};u=k.one
    for j in range(n):logs[u]=j;u=k.mul(u,n0)
    assert len(logs)==n
    mm=lambda fn:np.array([fn(x) for x in k.e],dtype=np.int64).T
    g=np.array([[k.tr(k.mul(c,k.mul(x,k.pw(y,p**(f//2))))) for y in k.e] for x in k.e],dtype=np.int64)
    assert rank(g,p)==f and not np.any((g.T+g)%p)
    geom0=np.kron(np.eye(2*p,dtype=np.int64),g);supset=set()
    for i in is_:
        h=f//math.gcd(f,i);target=k.neg(k.mul(k.pw(c,p**i),k.pw(c,-1)));eta=k.pw(e,logs[target])
        T0=mm(lambda x:k.mul(eta,k.pw(x,p**i)));t2diff=rank((T0@T0-np.eye(f,dtype=np.int64))%p,p)
        assert not np.any((T0.T@g@T0+g)%p)
        ok=h%2==1 or h%4==0
        assert ok==(t2diff==f)
        if not ok:
            print('q=%d f=%d i=%d, Frobenius order %d: adverse root T^2, rank %d < %d; not a loop construction.'%(q,f,i,h,t2diff,f));continue
        assert h>2
        T=np.zeros((d,d),dtype=np.int64)
        for j in range(p):T[j*f:(j+1)*f,(-j%p)*f:(-j%p+1)*f]=T0
        L=np.vstack((eye,T));M=np.vstack((T,eye));LM=np.hstack((L,M));assert rank(LM,p)==2*d
        assert not np.any((L.T@geom0@L)%p) and not np.any((M.T@geom0@M)%p)
        def orbit(i):
            return frozenset(((pow(p,i+t,q)*pow(alpha,j,q))%q,(pow(p,t,q)*pow(alpha,-j,q))%q) for t in range(f) for j in range(p))
        u=orbit(i);v=frozenset((y,x) for x,y in u);assert len(u)==len(v)==d and not(u&v)
        normal=frozenset((i%f,(-i)%f));assert normal not in supset;supset.add(normal)
        if not geom:
            print('q=%d f=%d i=%d, Frobenius order %d: actual transverse isotropic sheets, full rank %d, two disjoint weight orbits.'%(q,f,i,h,2*d));continue
        zs=[k.one]
        for j in range(1,q):zs.append(k.mul(zs[-1],z))
        zm=[mm(lambda x,a=a:k.mul(a,x)) for a in zs];ILM=invert(LM,p)
        # sign = (s,t)h^a tau; map F from second original orthogonal block to first
        def F(s,t,a):
            o=np.zeros((d,d),dtype=np.int64)
            for j in range(p):
                l=(j+a)%p;w=(pow(p,i,q)*pow(alpha,j,q)*s+pow(alpha,-j,q)*t)%q
                o[j*f:(j+1)*f,l*f:(l+1)*f]=zm[w]
            return o
        def top(s,t,a):return np.block([[F(s,t,a),0*eye],[0*eye,F(t,s,-a)]])
        for test in [(0,1,0),(0,0,1)]:assert rank(np.hstack((L,top(*test)@L)),p)==d
        assert rank(np.hstack((L,top(1,0,0)@L)),p)>d # genuinely not stable under first axis
        signs=[(s,-pow(alpha,-a,q)*s%q,a) for s in range(q) for a in range(p)]
        def prod(a,b):
            s,t,j=a;v,w,l=b
            return ((s+pow(alpha,j,q)*w)%q,(t+pow(alpha,-j,q)*v)%q,(j-l)%p)
        def prodES(x,a):
            s,t,j=x;v,w,l=a
            return ((s+pow(alpha,j,q)*v)%q,(t+pow(alpha,-j,q)*w)%q,(j+l)%p)
        tabs={}
        for a in signs:
            feat=np.vstack((F(*a),-eye))%p
            proj=(ILM@feat)%p
            tabs[a]=feat@invert(proj[d:],p)%p
            assert not np.any((ILM[d:]@tabs[a]-eye)%p)
        counts=[0,0];nonzero=0
        for a,b in itertools.product(signs,repeat=2):
            u=prod(a,b)
            if u[0] or u[2]==0 and u[1]:continue
            v=prodES(u,a);Y=tabs[a].T@geom0@tabs[v]%p
            assert not np.any((Y+Y.T)%p)
            nonzero+=int(np.any(Y));counts[u[2]!=0]+=1
        assert counts==[q*p,(p-1)*q*p] and nonzero
        print('q=%d f=%d i=%d order=%d: all %d outside signs, %d projected pairs, all %d actual physical phase quadratics on %d variables identically zero at the stabilizer; native L is not first-axis invariant.'%(q,f,i,h,len(signs),len(signs)**2,sum(counts),d))

if __name__=='__main__':
    run(61,[1,0,0,1,1,1,1,1,0,0,1],[1,2,4],True)
    run(193,[2,0,0,0,1]+[0]*11+[1],[1,2,4],False)
