"""Finite parity, diagonal-class, binary-cohomology and factor-capacity controls."""
from itertools import permutations,product
from math import gcd
def rank(x,d):
    basis={}
    for i in range(d):
        v=(x>>(i*d))&((1<<d)-1)
        while v and (j:=v.bit_length()-1) in basis:v^=basis[j]
        if v:basis[v.bit_length()-1]=v
    return len(basis)
def matrix(d):
    mask=(1<<d)-1
    def tr(x):
        return sum(((x>>(i*d+j))&1)<<(j*d+i) for i in range(d) for j in range(d))
    def row(x,i,j):return x^(((x>>(j*d))&mask)<<(i*d))
    def col(x,i,j):return x^(((x>>j)&sum(1<<(a*d) for a in range(d)))<<i)
    allg=range(1<<(d*d));sym={x for x in allg if tr(x)==x}
    alt={x^tr(x) for x in allg}
    def close(st):
        seen=set(st); ls=list(st); cs=[sum(1<<(a*d) for a in range(d))<<j for j in range(d)]
        for x in ls:
            for i,j in permutations(range(d),2):
                for y in (row(x,i,j), x^(((x&cs[j])>>j)<<i)):
                    if y not in seen:seen.add(y);ls.append(y)
        return seen
    even=close(alt);assert even=={x for x in allg if rank(x,d)%2==0}
    assert len(close(sym))==len(allg)
    # Actual diagonal-congruence orbits on symmetric matrices modulo alternating ones.
    def diag(x):return sum(((x>>(i*(d+1)))&1)<<i for i in range(d))
    ph=set([1]);ls=[1]
    for x in ls:
        mx=sum(((x>>i)&1)<<(i*(d+1)) for i in range(d))
        for i,j in permutations(range(d),2):
            y=diag(col(row(mx,i,j),i,j))
            if y not in ph:ph.add(y);ls.append(y)
    assert ph==set(range(1,1<<d))
    # Projective graphs over F2, incidence inner products mod 3 = rank parity test.
    rowspace=[a for a in range(1<<(d*d)) if not(a&~sum(1<<(i*d) for i in range(d)))]
    def act(a,x):return sum((((a>>(i*d))&x).bit_count()%2)<<i for i in range(d))
    vec={a:{(x,act(a,x)) for x in range(1,1<<d)} for a in rowspace}
    assert all(len(vec[a]&vec[b])%3==(int(a==b) if d%2 else int(a!=b)) for a in rowspace for b in rowspace)
    return len(sym),len(alt),len(even),len(ph)

def arithmetic():
    vals=0
    for d in range(3,52):
        for q in (2,3,4,5,8,9,11,13,16,17,25,27,32,49,64):
            if gcd(d,q-1)!=1:continue
            p=next(i for i in range(2,q+1) if q%i==0)
            bound=q**d*(q**d-1)//(q-1)+(1-d%2)
            e=d*(d+1)//2
            if d%2 and d>=5:
                for b in [b for b in range(2,d+1) if d%b==0 and all(b%j for j in range(2,int(b**.5)+1))]:
                    assert q**e>bound*(b if b==p else 1)*q**(d*(d//b-1)//2)
            if d%2==0 and d>=6:
                assert p==2 and q**e>bound*q**(d*d//4)
            if d==4 and q>=4:assert q**10>bound*2*q*q
            vals+=1
    return vals
if __name__=="__main__":
    print("Actual symmetric/alternating matrices, even-rank orbit union, nonzero diagonal phases:",[matrix(d) for d in (3,4)])
    print("Rank/field capacity inequalities:",arithmetic())
