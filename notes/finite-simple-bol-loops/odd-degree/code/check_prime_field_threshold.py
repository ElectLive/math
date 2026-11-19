#!/usr/bin/env python3
"""Native prime-field modules at the threshold, and independently built coset centralizers."""
from itertools import product
from math import gcd

def rank_mod(cols,p):
    if not cols:return 0
    basis={}
    for v in cols:
        v=list(v)
        for i in sorted(basis):
            if v[i]:
                c=v[i]
                v=[(x-c*y)%p for x,y in zip(v,basis[i])]
        i=next((i for i,x in enumerate(v) if x%p),None)
        if i is not None:
            c=pow(v[i],-1,p)
            basis[i]=[c*x%p for x in v]
    return len(basis)

def prime_field_module(p,q):
    # d=p is prime: Rabin's criterion is X^(p^d)=X and no linear factor.
    d=p; zero=(0,)*d;one=(1,)+(0,)*(d-1);x=(0,1)+(0,)*(d-2)
    def multiply(a,b):
        t=[0]*(2*d-1)
        for i,u in enumerate(a):
            for j,v in enumerate(b):t[i+j]+=u*v
        for i in reversed(range(d,len(t))):
            c=t[i]%p
            if c:
                for k,v in enumerate(F):t[i-d+k]-=c*v
        return tuple(c%p for c in t[:d])
    def power(a,k):
        out=one
        while k:
            if k&1:out=multiply(out,a)
            a=multiply(a,a);k>>=1
        return out
    for weight in (1,2,3):
        found=False
        for k in product(range(p),repeat=weight):
            if not k[0]:continue
            F=k+(0,)*(d-weight)
            if any((pow(y,d,p)+sum(z*pow(y,i,p) for i,z in enumerate(F)))%p==0 for y in range(p)):continue
            if power(x,p**d)==x:found=True;break
        if found:break
    assert found and (p**d-1)%q==0
    for i in range(p):
        z=power((i,1)+(0,)*(d-2),(p**d-1)//q)
        if z!=one:break
    assert z!=one and power(z,q)==one
    # D=(C_q^2 : C_p) extended by outside t on W=F_(p^p)^2;
    # no semisimplicity of this W over the full group. X=rot and V0,V1 diagonals.
    basis=[tuple(int(i==j) for j in range(2*d)) for i in range(2*d)]
    def rr(v):return power(v[:d],p)+power(v[d:],p**(d-1))
    def tt(v):return v[d:]+v[:d]
    def zz(v,i,k):
        zt=power(z,k%q);return (multiply(v[:d],zt)+v[d:]) if i==0 else (v[:d]+multiply(v[d:],zt))
    def diff(A,B):return [tuple((i-j)%p for i,j in zip(a,b)) for a,b in zip(A,B)]
    def rep(g,n,v):
        for _ in range(n):v=g(v)
        return v
    assert all(rep(rr,p,v)==v and tt(rr(tt(rr(v))))==v for v in basis)
    assert all(tt(zz(tt(v),0,1))==zz(v,1,1) and
               rr(zz(v,0,1))==zz(rr(v),0,p) and
               rr(zz(v,1,1))==zz(rr(v),1,pow(p,-1,q)) for v in basis)
    s=rank_mod(diff([tt(v) for v in basis],basis),p)
    u=rank_mod(diff([rr(v) for v in basis],basis),p)
    assert s==p and u==2*(p-1)
    # Frobenius is not semisimple; the N-index budget would fail if one silently replaced it by its semisimplification!
    print(f'F_{p}: q={q}, field modulus low-first below monic {F}, actual dimension {2*p}, rank(t-I)={s}, rank(r-I)={u}, r^p=I')

def cycles(P):
    seen=set();ans=[]
    for i in range(len(P)):
        if i not in seen:
            j=i;c=0
            while j not in seen:seen.add(j);j=P[j];c+=1
            assert j==i;ans.append(c)
    return sorted(ans)

def port(h,bits):
    N=h*bits
    V=tuple((u,s) for s in range(bits) for u in range(h));idx={x:i for i,x in enumerate(V)}
    A=[idx[((u+1)%h,s)] for u,s in V]
    T=[idx[(-u%h,1-s if bits==2 else s)] for u,s in V]
    # D-map determined by a single seed, derive it from actual generated actions.
    orders=set();n=0
    for dest in range(N):
        image={0:dest};stack=[0];okay=True
        while stack and okay:
            p=stack.pop()
            for g in (A,T):
                a,b=g[p],g[image[p]]
                if a in image:okay=image[a]==b
                else:image[a]=b;stack.append(a)
                if not okay:break
        if okay:
            assert len(image)==N and len(set(image.values()))==N
            L=cycles(tuple(image[i] for i in range(N)));assert len(set(L))==1
            n+=1;orders.add(L[0])
    cost=(N-sum(T[i]==i for i in range(N)))//2
    assert cost==(h if bits==2 else (h-1)//2)
    assert orders==({1} if bits==1 else {2}|{u for u in range(1,h+1) if h%u==0})
    assert n==(1 if bits==1 else 2*h)
    return cost,orders

def spectrum():
    cells=0;equality=set();novel=0
    primes=[p for p in range(3,252,2) if all(p%i for i in range(2,int(p**.5)+1))]
    for p in (3,5,7,11):
        for h in (p,p*p):
            trans=[port(h,i) for i in (1,2)]
            for q in primes:
                if q<=p or (q-1)%h and (q+1)%h:continue
                f=next(j for j in range(1,q) if pow(p,j,q)==1)
                # An orbit of c ports under Frobenius closes with a genuine commuting map
                # whose cycles all have equal length j; hence the common field cycle is c*j.
                costs=[c*(f//j) for c,orders in trans for j in orders if f%j==0]
                assert min(costs)>=max(h,f)
                if h==p and min(costs)==p:
                    assert f==p;equality.add((p,q))
                if h==p and f==2*p:
                    assert min(costs)>p;novel+=1
                cells+=1
    assert {(3,13),(5,11),(7,29)}<=equality and novel
    print(f'actual homogeneous-port centralizers and least field costs for {cells} odd q/p^k torus cases (q<=251); boundary {sorted(equality)}; {novel} false 2p-order shortcuts ruled out')
if __name__=='__main__':
    spectrum()
    for p,q in [(3,13),(5,11),(7,29)]:prime_field_module(p,q)
