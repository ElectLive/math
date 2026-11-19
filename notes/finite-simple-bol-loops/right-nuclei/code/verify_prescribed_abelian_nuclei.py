"""Projected groups and physical augmentation lattices, over the actual rings.
Requires Python 3 and NumPy. No gigantic loop development/table is enumerated."""
from itertools import product
from math import gcd,lcm,prod
from collections import Counter
import numpy as np
from random import Random

def order(a,q):
    b=a;x=1
    while b!=1:b=b*a%q;x+=1
    return x
def fac(n): return [p for p in range(2,n+1) if n%p==0 and all(p%d for d in range(2,int(p**.5)+1))]
def rank(A,p):
    A=np.array(A,dtype=np.int64)%p; n,m=A.shape; t=0
    for j in range(m):
        ii=next((i for i in range(t,n) if int(A[i,j])),None)
        if ii is None:continue
        A[[ii,t]]=A[[t,ii]];A[t]=A[t]*pow(int(A[t,j]),-1,p)%p
        co=A[:,j].copy();co[t]=0;A=(A-co[:,None]*A[t])%p;t+=1
        if t==n:break
    return t

class Model:
    def __init__(self,rr,q):
        self.rr=rr;self.q=q;self.k=k=len(rr);self.P=P=list(product(*(range(s) for s in rr)))
        self.pp={h:i for i,h in enumerate(P)}; self.Z=P[0];self.zero=tuple([0]*(2*k));self.I=(self.zero,0,0)
        self.C=np.array([[pow(next(a for a in range(2,q) if order(a,q)==s),h[i],q) for i,s in enumerate(rr)] for h in P])
        self.Cm=np.array([[pow(int(a),-1,q) for a in v] for v in self.C])
        self.hadd=np.array([[self.pp[tuple((x+y)%s for x,y,s in zip(a,b,rr))] for b in P] for a in P]);self.hm=[self.pp[tuple(-x%s for x,s in zip(a,rr))] for a in P]
        self.cp=[tuple(map(int,x)) for x in self.C];self.cm=[tuple(map(int,x)) for x in self.Cm]
        self.signs=[(tuple((-c[i]*b[i])%q for i in range(k))+b,h,1) for h,c in enumerate(self.cp) for b in product(range(q),repeat=k)]
        self.phases={};self.check_lattice()
    def mul(self,X,Y):
        v,h,s=X;w,j,t=Y;k=self.k
        if s:w=w[k:]+w[:k];j=self.hm[j]
        coeff=self.cp[h]+self.cm[h]
        return tuple((x+a*y)%self.q for x,a,y in zip(v,coeff,w)),int(self.hadd[h,j]),s^t
    def evals(self,v):
        k=self.k;a=v[:k];b=v[k:];return (self.C@a+self.Cm@b)%self.q
    def check_lattice(self):
        q=self.q;E=np.zeros((q-1,q),dtype=np.int64);E[:,:q-1]=np.eye(q-1,dtype=np.int64);E[:,-1]=-1
        gram=lambda A,B:A@(np.roll(B,1,axis=1)-np.roll(B,-1,axis=1)).T
        for s in set(self.rr):
            p=fac(s)[0];G=gram(E,E)%s
            assert rank(G,p)==q-1 and np.array_equal((G+G.T)%s,np.zeros_like(G))
            for i in range(1,q):
                assert rank((np.roll(E,i,axis=1)-E)[:,:q-1],p)==q-1
                assert np.array_equal(gram(np.roll(E,i,axis=1),np.roll(E,i,axis=1))%s,G)
            Ds=[gram(np.roll(E,i,axis=1),E)%s for i in range(q)]
            self.phases[s]={(a,b):not np.any((Ds[a]+Ds[b].T)%s) for a,b in product(range(q),repeat=2)}
            assert all(np.all(Ds[a].diagonal()%s==0) for a in range(q) if self.phases[s][a,a])
    def physical_polynomials(self):
        ct=0
        for v,h,sg in self.signs:
            assert self.mul((v,h,sg),(v,h,sg))==self.I
            ell=self.evals(v)
            # For F_s acting from second to first: source site i leads to output
            # j=i-h, which B pairs with site -j. Compare transposed genuine blocks.
            for i in range(len(self.P)):
                j=self.hadd[i,self.hm[h]];partner=self.hm[j];z=self.hadd[partner,self.hm[h]]
                assert all(M[int(ell[j]),int(ell[z])] for M in self.phases.values())
                ct+=1
        return ct
    def collisions(self,allpairs):
        q=self.q;k=self.k;zz=tuple([0]*k);seen=Counter();r=Random(134)
        it=product(self.signs,repeat=2) if allpairs else ((r.choice(self.signs),r.choice(self.signs)) for _ in range(25000))
        count=0
        for a,b in it:
            v,j,s=self.mul(a,b);assert not s;count+=1
            if v[:k]!=zz:continue
            assert j or v[k:]==zz
            seen[j]+=1
        if allpairs:assert seen[0]==len(self.signs)
        return count,dict(sorted(seen.items()))
    def act(self,X,u):
        v,h,s=X
        a,b=u if not s else u[::-1]
        k=self.k;vv=v[k:]+v[:k]
        def perform(x,h,els):
            w=x[self.hadd[:,h]]; ii=(np.arange(self.q)[None,:]-els[:,None])%self.q
            return np.take_along_axis(w,ii,axis=1)
        return np.array([perform(a,h,self.evals(v)),perform(b,self.hm[h],self.evals(vv))])
    def B(self,x,y):
        v=y[self.hm];return int(np.sum(x*(np.roll(v,1,axis=1)-np.roll(v,-1,axis=1))))
    def om(self,u,v):return self.B(u[0],v[1])+self.B(u[1],v[0])
    def raw(self,rng,s):
        v=np.array(rng.integers(s,size=(2,len(self.P),self.q)),dtype=np.int64);v[:,:,-1]=-v[:,:,:-1].sum(axis=2)%s;return v%s
    def actual(self):
        rng=np.random.default_rng(673);pgen=[self.pp[tuple(int(i==j) for j in range(self.k))] for i in range(self.k)]
        gens=[(self.zero,h,0) for h in pgen]+[(tuple(int(i==j) for j in range(2*self.k)),0,0) for i in range(2*self.k)]+[(self.zero,0,1)]
        r=lcm(*self.rr);h=next(i for i,a in enumerate(self.P) if lcm(*(s//gcd(s,x) for s,x in zip(self.rr,a)))==r);H=(self.zero,h,0);t=(self.zero,0,1)
        adm=bad=0;factor=[]
        for s in set(self.rr):
            x=self.raw(rng,s);y=self.raw(rng,s)
            for g in gens:
                assert (self.om(self.act(g,x),self.act(g,y))-self.om(x,y))%s==0
                for z in gens:assert np.array_equal(self.act(self.mul(g,z),x)%s,self.act(g,self.act(z,x))%s)
            for _ in range(70):
                a,b=[self.signs[int(rng.integers(len(self.signs)))] for _ in range(2)]
                aba=self.mul(self.mul(a,b),a); x=self.raw(rng,s)*0; x[1]=self.raw(rng,s)[1]
                # exact vectors of the actual two signed class lifts, not just projected equations
                u=(self.act(a,x)-x)%s;w=(x-self.act(aba,x))%s;v=self.act(a,w)%s
                assert not np.any((self.act(a,u)+u)%s) and not np.any((self.act(b,v)+v)%s)
                uw=self.act(a,v)%s;assert not np.any((u+uw)[1]%s) and self.om(u,uw)%s==0;adm+=1
                another=self.raw(rng,s);v=(another-self.act(b,another))%s
                if self.om(u,self.act(a,v))%s:bad+=1
            x=np.zeros((len(self.P),self.q),dtype=np.int64);x[0,0]=1;x[0,-1]=-1;u=np.array([x,-x[self.hadd[:,self.hm[h]]]])%s
            assert not np.any((self.act(t,u)+self.act((self.zero,self.hm[h],0),u))%s)
            # semidirect marked r-th power, including central carries
            acc=np.zeros_like(u);c=0;w=u.copy();inv2=pow(2,-1,s)
            for _ in range(r):
                c=(c+inv2*self.om(acc,w))%s;acc=(acc+w)%s;w=self.act(H,w)%s
            assert int(acc[0,0,0])==1 and not np.any((r*acc)%s)
            antidiag=tuple([1]+[0]*(self.k-1))+tuple([self.q-1]+[0]*(self.k-1))
            ux=np.array([x,-x])%s
            assert np.array_equal(self.act((antidiag,0,0),ux)%s,ux) and not np.any((self.act(t,ux)+ux)%s)
            factor.append((s,c))
        assert bad>0
        # finite geometric normalizer check of J on X/J: exactly 0 is fixed by all pure tops
        fixed=[a for a in product(range(self.q),repeat=self.k) if all(all((c*x-x)%self.q==0 for c,x in zip(row,a)) for row in self.cp)]
        assert fixed==[tuple(0 for _ in range(self.k))]
        return adm,bad,factor
def partial():
    # Nonfree, non-full-preimage normal subgroup in an actual Z/9 Heisenberg group.
    # Alternate beta on R^2, two halves exchanged. C has only the order-3 central sheet.
    s=9
    def om(u,v):return u[0]*v[3]-u[1]*v[2]+u[2]*v[1]-u[3]*v[0]
    def mul(u,v):return tuple((u[i]+v[i])%s for i in range(4))+((u[4]+v[4]+5*om(u,v))%s,)
    def inv(u):return tuple(-y%s for y in u)
    def t(u):return u[2:4]+u[:2]+u[4:]
    C={(a,0,b,0,c) for a,b,c in product([0,3,6],repeat=3)}
    gs=[tuple(int(i==j) for j in range(5)) for i in range(5)]
    assert all(mul(mul(g,x),inv(g)) in C and t(x) in C for g,x in product(gs,C))
    assert all(mul(x,y) in C for x,y in product(C,repeat=2))
    cut=len(C)//sum(x[2:]==(0,0,0) for x in C),len(C)//sum(t(x)==x for x in C)
    assert cut==(9,3);print('Actual nonfree partial-center cut over Z/9: subgroup 27; physical and signed indices',cut)
def main():
    for rr,q,allpairs in [((9,),19,True),((3,3),7,True),((3,5),31,False)]:
        m=Model(rr,q);c=m.physical_polynomials();cnt,cols=m.collisions(allpairs);a,b,f=m.actual()
        print('ring',rr,'q',q,'signs',len(m.signs),'all signed alternating block tests',c,
              'pair checks',cnt,'exhaustive' if allpairs else 'sample','physical L cancellation/off-L nonzero',a,b,
              'native top-power central residues',f,'all fixed points of quotient J: 1')
        if rr==(9,):
            assert set(cols)==set(range(9)) and cols[3]==cols[6]==171
            for j in [3,6]:
                t=m.zero,0,1; z=m.zero,m.hm[j],1
                assert m.mul(t,z)==(m.zero,j,0) and 3*j%9==0 and j%9!=0
            print('Nonunit twist 3 admits actual zero-lift collisions at top j=3,6; faithful twist detects both.')
    partial()
    print('All stated positive and adverse controls passed. No independence, exhaustive kernel classification or full large table computation asserted.')
if __name__=='__main__':main()
