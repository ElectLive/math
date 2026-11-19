"""Native semidirect group, genuine marked-square, all subspaces and full table controls.
Pure Python. No paper formula is used to generate the involution-inverted marks.
"""
from itertools import product,combinations
from collections import Counter
import random

class Group:
    # exp(v) exp(s*a), v=(b,d,c[,w]). Relations p*a=A*c, p*b=B*c.
    def __init__(self,p,m,A=0,B=0):
        self.p=p;self.m=m;self.A=A;self.B=B
        self.V=list(product(range(p),repeat=m));self.E=list(product(range(p),repeat=m+1))
        self.zero=self.E[0]
        self.shift={}
        from math import factorial
        for s in range(p):
            for v in self.V:
                self.shift[s,v]=tuple(sum(pow(factorial(h),-1,p)*s**h*v[i-h] for h in range(i+1))%p for i in range(m))
    def reduce(self,s,v):
        p=self.p;v=list(v);u,s=divmod(s,p);b,v[0]=divmod(v[0],p);v[2]+=self.A*u+self.B*b
        return (s,)+tuple(a%p for a in v)
    def mult(self,x,y):
        s=x[0];w=self.shift[s,y[1:]]
        return self.reduce(s+y[0],(a+b for a,b in zip(x[1:],w)))
    def inv(self,x):
        v=self.shift[-x[0]%self.p,x[1:]]
        return self.reduce(-x[0],(-u for u in v))
    def sign(self,x):
        return self.reduce(-x[0],((-1 if i%2==0 else 1)*a for i,a in enumerate(x[1:])))
    def marked(self):return [x for x in self.E if self.inv(x)==self.sign(x)]
    def powset(self,g):
        z=self.zero;h={z}
        while True:
            z=self.mult(z,g)
            if z in h:return frozenset(h)
            h.add(z)
    def tables(self,H,K,verifyfull=False):
        pts={}
        for i,x in enumerate(K):
            for h in H:
                u=self.mult(x,h);assert u not in pts;pts[u]=i
        assert len(pts)==len(self.E)
        r=[[pts[self.mult(x,y)] for y in K] for x in K];n=len(K);assert r[0]==list(range(n))
        assert all(len(set(x))==n for x in zip(*r)) and all(len(set(x))==n for x in r)
        if verifyfull:
            fixed=set(range(n)); central=[i for i in range(n) if all(r[i][j]==r[j][i] for j in range(n))]
            lnu=set(range(n));mid=set(range(n));rnu=set(range(n))
            for i in range(n):
                for j in range(n):
                    ij=r[r[i][j]];iji=r[r[i][r[j][i]]];irow,jrow=r[i],r[j]
                    assert all(iji[u]==irow[jrow[irow[u]]] for u in range(n))
                    for u in tuple(rnu):
                        if ij[u]!=irow[jrow[u]]:rnu.remove(u)
                    if i in lnu or j in mid:
                        if any(ij[u]!=irow[jrow[u]] for u in range(n)):lnu.discard(i);mid.discard(j)
            center=set(central)&lnu&mid&rnu
            sq=[r[i][i] for i in range(n)];roots={u:i for i,u in enumerate(sq)}
            bruck=tuple(roots[r[i][r[sq[j]][i]]] for i in range(n) for j in range(n))
            return r,bruck,(len(center),len(lnu),len(mid),len(rnu))
        return r,None,None

def planes(p,n,k):
    for piv in combinations(range(n),k):
        free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
        for v in product(range(p),repeat=len(free)):
            mat=[[int(a==j) for j in range(n)] for a in piv]
            for (i,j),t in zip(free,v):mat[i][j]=t
            yield tuple(tuple(r) for r in mat)
def plane(p,rs):return frozenset((0,)+tuple(sum(a*b for a,b in zip(c,k))%p for k in zip(*rs)) for c in product(range(p),repeat=len(rs)))

def cubic_data(p):
    irr={(b,c,d) for b,c,d in product(range(p),repeat=3) if all((x**3+b*x*x+c*x+d)%p for x in range(p))}
    def iso(f,s):b,c,d=f;return (b*s%p,c*s*s%p,d*s**3%p)
    def trans(f,u):b,c,d=f;return ((b-3*u)%p,(c-2*b*u+3*u*u)%p,(d-c*u+b*u*u-u**3)%p)
    srep={f:min(iso(f,s) for s in range(1,p)) for f in irr}
    arep={f:min(iso(trans(f,u),s) for s in range(1,p) for u in range(p)) for f in irr}
    assert len(set(srep.values()))==(p*(p+1)+(4 if p%3==1 else 0))//3
    assert len(set(arep.values()))==((p+1)+(4 if p%3==1 else 0))//3
    return irr,srep,arep

def class4(p):
    g=Group(p,4);K=g.marked();assert len(K)==p**3
    S2={g.mult(x,y) for x in K for y in K};z=g.zero
    assert all(e in S2 for e in g.E if e[0])
    irr,srep,arep=cubic_data(p);passing=Counter();examples={};n=0;actual_squares=len(K)**2
    for rows in planes(p,4,2):
        n+=1;H=plane(p,rows)
        admissible=(H&S2=={z});w=(0,0,0,0,1)
        if w in H:
            if admissible:passing['w']+=1
            continue
        if (rows[0][0],rows[0][1],rows[1][0],rows[1][1])!=(1,0,0,1):
            assert not admissible;continue
        alpha,gamma=rows[0][2:];beta,delta=rows[1][2:]
        f=(-3*beta%p,3*(delta-alpha)%p,3*gamma%p)
        assert admissible==(f in irr)
        if admissible:passing['noncentral']+=1; examples.setdefault(srep[f],H)
    assert passing['w']==p and passing['noncentral']==p*len(irr)
    npairs=0
    if p==5:
        bsignatures=set()
        for f,H in sorted(examples.items()):
            r,bruck,nucs=g.tables(H,K,True);bsignatures.add(bruck)
            assert nucs[0]==1;npairs+=len(K)**3
        assert len(bsignatures)==1
    print('filiform p=%d: true squares=%d all V-planes=%d passing with/without central w=%d/%d; irreducibles=%d true isotypes=%d isotope orbits=%d; full native Bol triples=%d'%(p,actual_squares,n,passing['w'],passing['noncentral'],len(irr),len(examples),len(set(arep.values())),npairs))

def class3(p):
    ns=next(i for i in range(1,p) if pow(i,(p-1)//2,p)!=1)
    sig=Counter();nt=0
    for A,B in [(0,0),(1,0),(0,1),(0,ns)]:
        g=Group(p,3,A,B);K=g.marked();assert len(K)==p**3
        bad={g.mult(x,y) for x in K for y in K};allh={g.powset(e) for e in g.E}
        lines=[h for h in allh if len(h)==p]
        good=[h for h in lines if h&bad=={g.zero}]
        physical={frozenset((0,0,d,d*r%p) for d in range(p)) for r in range(p)}
        assert set(good)==physical
        # True signed bases: count actual exotic p-power laws, not just reduced parameters.
        ds=range(1,p) if not B else (1,p-1)
        orbits={min(s*r%p for s in ds) for r in range(p)}
        bsign=set()
        for r in orbits:
            H=frozenset((0,0,d,d*r%p) for d in range(p))
            tab,br,nucs=g.tables(H,K,p==5)
            if p==5:assert nucs[0]==p;bsign.add(br);nt+=p**9
        if p==5:assert len(bsign)==1
        sig[A,B]=(len(lines),len(good),len(orbits))
        if A or B:
            assert any(len(g.powset(e))==p*p for e in g.E)
    assert sum(s[2] for s in sig.values())==p+5
    print('Engel p=%d: all actual order-p lines/passing/isotypes by (A,B) %s; full native Bol triples=%d'%(p,str(dict(sig)),nt))

def idealizer_test(p):
    # True signed bracket-preserving transformations on V, with negative shear in b -> tb+rc;
    # compare H rather than only scalar action on a polynomial.
    irr,sr,ar=cubic_data(p);rng=random.Random(1948)
    for _ in range(800):
        f=rng.choice(sorted(irr));s,t=rng.randrange(1,p),rng.randrange(1,p);r,u=(rng.randrange(p) for _ in range(2))
        al=rng.randrange(p);be=-f[0]*pow(3,-1,p)%p;de=(al+f[1]*pow(3,-1,p))%p;ga=f[2]*pow(3,-1,p)%p
        # Interpret actual conjugation exp(u a) and signed automorphism at every vector in H.
        A=(r*pow(t,-1,p)+s*s*(al+u*u*pow(2,-1,p)-(be+u)*u))%p
        B=s*(be+u)%p
        C=s**3*(ga+u*al+u**3*pow(6,-1,p)-u*(de+u*be+u*u*pow(2,-1,p)))%p
        D=(r*pow(t,-1,p)+s*s*(de+u*be+u*u*pow(2,-1,p)))%p
        for i,j in product(range(p),repeat=2):
            z=al*i+be*j;w=ga*i+de*j
            jj=j+u*i;zz=z+u*j+u*u*i*pow(2,-1,p);ww=w+u*z+u*u*j*pow(2,-1,p)+u**3*i*pow(6,-1,p)
            aa=t*i;bb=s*t*jj
            assert (r*i+s*s*t*zz-A*aa-B*bb)%p==0
            assert (s*r*jj+s**3*t*ww-C*aa-D*bb)%p==0
        f2=(-3*B%p,3*(D-A)%p,3*C%p)
        assert ar[f]==ar[f2]
        if u==0:assert sr[f]==sr[f2]
    print('p=%d: 800 full physical conjugate/shear graph maps, each on all %d stabilizer vectors'%(p,p*p))

if __name__=='__main__':
    for p in (5,7):
        class3(p);class4(p);idealizer_test(p)
    for p in (11,13,17,19):
        a,b,c=cubic_data(p); print('polynomial orbits p=%d: isom=%d affine=%d'%(p,len(set(b.values())),len(set(c.values()))))
