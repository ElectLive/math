#!/usr/bin/env python3
"""Exact F3 screens from FG class-number upper bounds, not exact counts."""
from math import gcd,isqrt

LIMIT=1030**2

def prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def powers():
    result=[]
    for p in range(2,512):
        if prime(p):
            q,f=p,1
            while q<512:
                result.append((q,f))
                q,f=q*p,f+1
    assert len(result)==len({q for q,f in result})
    return sorted(result)

def sqrt_ceiling_tenths(v):
    # Least integer B with 10 B² >= v.
    b=isqrt(v//10)
    return b+(10*b*b<v)

expected_good={
 ('B',2):[17,19,23,29,31,37,41,43,47,49,53,59,61,125,256],
 ('B',3):[3], ('B',4):[],
 ('D+',4):[], ('D-',4):[3], ('D+',5):[], ('D-',5):[]}
expected_fail={
 ('B',2):[5,7,8,9,11,13,16,25,27,32,64,81,128],
 ('B',3):[2], ('B',4):[],
 ('D+',4):[2,3], ('D-',4):[2], ('D+',5):[], ('D-',5):[]}

for r in (2,3,4):
    good=[]; fail=[]
    for q,f in powers():
        if (r==3 and q>=5) or (r==4 and q>=3):
            continue
        g=gcd(2,q-1)
        n=q**(r*r)
        for i in range(1,r+1): n*=q**(2*i)-1
        assert n%g==0
        n//=g
        t=2*f if r==2 else g*f
        if n<2**20 or n>LIMIT*t**3*q**(3*r):
            continue
        # FG Table 2: k(T) <= 7.3 q^r for q odd; <=15.2 q^r for even.
        # Lemma 2.1 gives k(Aut T)<=t*k(T); Cor 1.2 also gives <=100 q^r.
        c10=min(1000,(152 if q%2==0 else 73)*t)
        a=n*t
        B=sqrt_ceiling_tenths(a*q**r*c10)
        assert 10*B*B>=a*q**r*c10
        (good if B**3+3*a*B<n*n else fail).append(q)
    assert good==expected_good['B',r],(r,good)
    assert fail==expected_fail['B',r],(r,fail)

for r in (4,5):
    for eps in (1,-1):
        label='D+' if eps==1 else 'D-'
        good=[];fail=[]
        for q,f in powers():
            if (r==4 and q>=7) or (r==5 and q>=3):
                continue
            g=gcd(4,q**r-eps)
            n=q**(r*(r-1))*(q**r-eps)
            for i in range(1,r): n*=q**(2*i)-1
            assert n%g==0
            n//=g
            t=(6 if r==4 and eps==1 else 2)*f*g
            if n>LIMIT*t**3*q**(3*r):
                continue
            # Table 2: k(T) <=6.8 q^r odd, <=14 q^r even.
            c10=min(1000,(140 if q%2==0 else 68)*t)
            a=n*t
            B=sqrt_ceiling_tenths(a*q**r*c10)
            assert 10*B*B>=a*q**r*c10
            (good if B**3+3*a*B<n*n else fail).append(q)
        assert good==expected_good[label,r],(label,r,good)
        assert fail==expected_fail[label,r],(label,r,fail)
print('orthogonal class-bound F3 checks passed')

# GAP 4.15.1 release: https://github.com/gap-system/gap/releases/download/v4.15.1/gap-4.15.1.tar.gz
# SHA256 6049d53e99b12e25c2d848db21ac4a06380a46fe4c4157243d556fe06930042c
# Bundled CTblLib 1.3.11, data/ctoorth2.tbl SHA256
# cf250c9b4ada37a8c8e5fc93570ba3c24c9cd9197baf8a646e568194de2afdce
# data/ctoorth3.tbl SHA256 736b8f34211dd8a20c51312015fa72c1bb0a4931db19b317ea436ac0e9644626
# Extract unique MOT("NAME", record: regex centralizer list then square-map
# list; retain entries whose square-map index is 1. This is format-specific.
# The lists below contain the nonidentity centralizers, in that source order.
rows = [
 ('O8+(2).3.2',174182400,1045094400,183376,[663552,92160,18432,2903040,9216]),
 ('O8+(3).S4',4952179814400,118852315545600,93148624,[209018880,7962624,97044480,4147200,18341406720,2488320]),
 ('O8-(2).2',197406720,394813440,112592,[368640,92160,6144,2903040,9216]),
]
for name,n,a,b,centralizers in rows:
    assert all(a%c==0 for c in centralizers), name
    assert 1+sum(a//c for c in centralizers)==b, name
    assert b**3+3*a*b<n*n, name
print('three full-automorphism table F3 checks passed')
