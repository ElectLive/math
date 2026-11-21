#!/usr/bin/env python3
"""Opposite weights and genuine trace hyperplanes at first even-f example."""
from itertools import product
from functools import lru_cache

p=3;n=6
words=list(product(range(p),repeat=n));index={x:i for i,x in enumerate(words)}
zero=index[(0,)*6];one=index[(1,0,0,0,0,0)];zeta=index[(0,1,0,0,0,0)]
def add(x,y):return index[tuple((a+b)%p for a,b in zip(words[x],words[y]))]
def neg(x):return index[tuple(-a%p for a in words[x])]
@lru_cache(maxsize=None)
def mul(x,y):
    w=[0]*11
    for i,a in enumerate(words[x]):
        for j,b in enumerate(words[y]):w[i+j]+=a*b
    for k in range(10,5,-1):
        for j in range(1,7):w[k-j]-=w[k]
    return index[tuple(i%p for i in w[:6])]
@lru_cache(maxsize=None)
def pw(x,j):
    if not j:return one
    a=pw(x,j//2);a=mul(a,a)
    return mul(a,x) if j%2 else a
def trrel(x):return add(add(x,pw(x,9)),pw(x,81))
def tr(x):
    t=trrel(x);d=words[add(t,pw(t,3))]
    assert not any(d[1:])
    return d[0]
def rank(rows):
    B={}
    for a in rows:
        v=list(a)
        for i in sorted(B):
            c=v[i];v=[(a-c*b)%p for a,b in zip(v,B[i])]
        i=next((i for i,a in enumerate(v) if a),None)
        if i is not None:B[i]=[a*pow(v[i],-1,p)%p for a in v]
    return len(B)
def basis(S):
    out=[]
    for a in S:
        if rank([words[b] for b in out+[a]])>len(out):out.append(a)
    return out
K=set(range(729));K0={x for x in K if pw(x,9)==x};K0s=K0-{zero}
assert len(K0)==9 and pw(zeta,7)==one and pw(zeta,3)!=zeta and all(pw(x,728)==one for x in K-{zero})
assert {trrel(x) for x in K}==K0 and {tr(x) for x in K}=={0,1,2} and tr(one)==0
planes={frozenset(x for x in K if tr(mul(c,x))==0) for c in K0s}
assert len(planes)==4 and all(len(H)==243 for H in planes)
H=next(iter(planes));assert {frozenset(mul(c,x) for x in H) for c in K0s}==planes
assert all(all(pw(x,9) in h for x in h) for h in planes)
c=next(x for x in K0s if pw(x,27)==neg(x))
def beta(x,y):return tr(mul(c,mul(x,pw(y,27))))
bs=basis(K)
assert len(bs)==6
mat=[[beta(a,b) for b in bs] for a in bs]
assert rank(mat)==6 and all(mat[i][j]==-mat[j][i]%3 for i,j in product(range(6),repeat=2)) and all(mat[i][i]==0 for i in range(6))
for x,y in product(bs,repeat=2):
    assert beta(mul(zeta,x),mul(zeta,y))==beta(x,y)==beta(pw(x,9),pw(y,9))
ranks=[]
for h in planes:
    bs1=basis(h);ranks.append(rank([[beta(a,b) for a in bs1] for b in bs1]))
assert ranks==[4]*4
mixed={(pow(3,g,7)*pow(2,i,7)%7,pow(3,g,7)*pow(2,-i,7)%7) for g in range(6) for i in range(3)}
assert len(mixed)==18 and {(-a%7,-b%7) for a,b in mixed}==mixed
assert sum(a!=b for a,b in mixed)//2==6 and all(b for a,b in mixed)
assert 2*6-1>18//2 and (2*6-1)%6==5
print('GF(729), p=3 q=7 f=6: opposite characters genuinely occur; actual V-invariant and Frobenius-invariant alternating trace form has rank 6')
print('all four invariant trace hyperplanes are in one GF(9)^x orbit; restrictions of the actual alternating form have ranks',ranks,'not zero; absolute trace of 1 is zero but the map is onto')
print('actual 18 mixed ternary weights include negatives; 6 swapped pairs, all V2-nontrivial; 11-dimensional forced isotropic subspace exceeds 9, and final elementary codimension has residue 5 modulo 6')
