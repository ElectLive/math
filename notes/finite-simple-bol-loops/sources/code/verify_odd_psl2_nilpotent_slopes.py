"""Actual semilinear edge products and bad gauges for the odd-PSL2 proof."""
from itertools import product
from math import isqrt

class Field:
    def __init__(self,mod):
        self.d=len(mod)-1;self.q=3**self.d;self.mod=mod
        self.vec=[tuple((x//3**i)%3 for i in range(self.d)) for x in range(self.q)]
    def code(self,a):
        return sum((x%3)*3**i for i,x in enumerate(a))
    def add(self,x,y):
        return self.code([a+b for a,b in zip(self.vec[x],self.vec[y])])
    def mul(self,x,y):
        a=[0]*(2*self.d-1)
        for i,u in enumerate(self.vec[x]):
            for j,v in enumerate(self.vec[y]):a[i+j]+=u*v
        for k in range(len(a)-1,self.d-1,-1):
            v=a[k]%3
            for j,t in enumerate(self.mod):a[k-self.d+j]-=v*t
        return self.code(a[:self.d])
    def pow(self,x,r):
        a=1
        while r:
            if r&1:a=self.mul(a,x)
            x=self.mul(x,x);r//=2
        return a

def irr(d):
    for tail in product(range(3),repeat=d):
        if not tail[0]:continue
        a=list(tail)+[1]
        def divisible(f,g):
            f=f[:]
            for j in range(len(f)-1,len(g)-2,-1):
                c=f[j]%3
                for i,u in enumerate(g):f[j-len(g)+1+i]-=c*u
            return not any(x%3 for x in f)
        if not any(divisible(a,list(g)+[1]) for k in range(1,d//2+1)
                   for g in product(range(3),repeat=k)):
            return tuple(a)
    raise AssertionError("no irreducible polynomial")

def cm(g,h):return tuple(g[i] for i in h)
def iv(g):return tuple(g.index(i) for i in range(len(g)))
def cj(g,h):return cm(cm(g,h),iv(g))

def actual_27():
    F=Field((1,2,0,1));q=27
    M=[[F.mul(x,y) for y in range(q)] for x in range(q)]
    A=[[F.add(x,y) for y in range(q)] for x in range(q)]
    inv=[0]+[M[x].index(1) for x in range(1,q)]
    assert all(len(set(M[x]))==q for x in range(1,q))
    neg=[row.index(0) for row in A]
    P=tuple(range(q+1));I=P
    def mob(a,b,c,d):
        def f(x):
            u,v=(a,c) if x==q else (A[M[a][x]][b],A[M[c][x]][d])
            return q if not v else M[u][inv[v]]
        return tuple(f(x) for x in P)
    T=set()
    for a,b,c in product(range(q),repeat=3):
        if a:
            d=M[inv[a]][A[1][M[b][c]]]
            T.add(mob(a,b,c,d))
        elif M[b][c]==neg[1]:
            # This branch is independent of d and already occurs once per b,c.
            for d in range(q):T.add(mob(a,b,c,d))
    assert len(T)==9828
    J=mob(0,1,1,0);assert J not in T and cm(J,J)==I
    primitive=next(x for x in range(2,q) if F.pow(x,13)!=1 and F.pow(x,2)!=1)
    u=M[primitive][primitive];assert F.pow(u,13)==1 and u!=1
    Frob=tuple(F.pow(x,3) for x in range(q))+(q,)
    F2=cm(Frob,Frob);assert cm(F2,Frob)==I
    gauge=[I,cm(mob(1,2,0,1),Frob),cm(mob(1,3,0,1),F2),mob(1,5,0,1)]
    sigma=(1,0,3,2);tau=(2,3,0,1);one=(0,1,2,3)
    def act(arr,s):
        return tuple((q+1)*s[i]+arr[i][x] for i,x in product(range(4),P))
    def transport(s,l):
        return [cm(gauge[s[i]],cm(l,iv(gauge[i]))) for i in range(4)]
    P2={act(transport(s,I),s) for s in (one,sigma,tau,cm(tau,sigma))}
    diagonal=act(transport(one,J),one)
    Q=P2|{cm(diagonal,h) for h in P2}
    assert len(Q)==8 and all(cm(x,y) in Q for x,y in product(Q,repeat=2))
    h=act(transport(sigma,I),sigma);arr=transport(sigma,J);lam=act(arr,sigma)
    assert h in P2 and lam in Q-P2
    for sign,ex in ((1,(1,1,0,0)),(-1,(1,-1,3,-3))):
        w=[cj(gauge[i],mob(F.pow(u,e%13),0,0,1)) for i,e in enumerate(ex)]
        assert all(x in T for x in w) and any(x!=I for x in w)
        assert any(x!=I and x[0]!=0 for x in w)
        ww=act(w,one)
        assert cj(h,ww)==(ww if sign==1 else iv(ww))
        first=[None]*4;second=[None]*4
        for i,j in ((0,1),(2,3)):
            # Same genuine field arrows and same PGL determinant class as lam.
            g=cm(gauge[j],cm(J if sign==1 else mob(primitive,0,0,1),iv(gauge[i])))
            assert cm(g,iv(arr[i])) in T and cj(g,iv(w[i]))==w[j]
            t=cm(g,w[i]);assert cm(t,iv(arr[i])) in T
            first[i],first[j],second[i],second[j]=g,iv(g),t,iv(t)
        x,y=act(first,sigma),act(second,sigma)
        assert cm(x,x)==cm(y,y)==tuple(range(112)) and cm(x,y)==ww
    # Bare permutation match without common Sylow: correct pair-exchange but
    # an extra cubic Frobenius transports a primitive 13-slope improperly.
    good=mob(u,0,0,1)
    bad=cm(J,Frob)
    wrong=cj(bad,iv(good))
    assert all(cj(g,wrong)!=good for g in T)
    assert F.pow(u,3) not in (u,inv[u])
    print("PSL2(27): all 9828 inner projectivities, honest common Sylow model"
          " on 112 points, both slope eigensigns and actual same-class products;"
          " a mismatched cubic edge fails all inner conjugators")

def even_gauge():
    F=Field(irr(6))
    assert all(F.pow(x,728)==1 for x in range(1,729))
    sub={x for x in range(729) if F.pow(x,27)==x}
    mu={x for x in range(1,729) if F.pow(x,13)==1}
    outside={x for x in range(1,729) if F.pow(x,7)==1}
    assert len(sub)==27 and len(mu)==13 and mu<=sub
    assert len(outside)==7 and outside&sub=={1}
    assert all(F.pow(x,27)!=x for x in outside-{1})
    print("GF(729): the order-two field gauge fixes all 27 odd-subfield values"
          " and all 13 roots, but changes all 6 primitive seventh roots")

def orders():
    cases=0
    for p in range(3,201,2):
        if any(p%a==0 for a in range(2,isqrt(p)+1)):continue
        q=p;f=1
        while q<=1000000:
            if q>=5:
                L=q*(q*q-1)//2;V=2*f*L
                I=q*q+1+(0 if f%2 else isqrt(q)*(q+1))
                assert I*I>=V
                if f%2:
                    if q>=17:assert L*L>4*I*I*q
                    elif q!=5:assert I*I>2*V and q*q*I**6<L**4*(I*I-2*V)
                else:
                    M=q*(q-1)//8
                    assert q%8==1 and M>=(q+1)//2 and I*I>2*V
                    assert M*M*I**6<L**4*(I*I-2*V)
                cases+=1
            q*=p;f+=1
    assert 756**4*25<4*625**4*19
    print(f"{cases} prime-power parameter checks to 10^6 (odd base primes ≤199),"
          " exact small exceptions and uniform rational failure threshold verified")

if __name__=="__main__":
    actual_27()
    even_gauge()
    orders()
