#!/usr/bin/env python3
"""Exact scalar-parameter orbit controls; no loop, field, or simplicity claims."""
from itertools import product
from math import lcm, prod

def primitive(p):
    for g in range(2,p):
        if len({pow(g,n,p) for n in range(p-1)})==p-1:
            return g
    raise ValueError(p)

def group_generated(generators, mods):
    zero=(0,)*len(mods)
    seen={zero}; queue=[zero]
    for x in queue:
        for g in generators:
            y=tuple((a+b)%m for a,b,m in zip(x,g,mods))
            if y not in seen:
                seen.add(y); queue.append(y)
    return seen

def check(primes, edges, expected):
    edges=sorted(edges); mods=tuple(primes[j]-1 for j,i in edges)
    refs=[primitive(primes[j]) for j,i in edges]
    logs=[{pow(g,n,primes[j]):n for n in range(primes[j]-1)} for (j,i),g in zip(edges,refs)]
    sg=[tuple(int(j==v) for j,i in edges) for v in range(len(primes))]
    tg=[tuple(logs[k][primes[i]%primes[j]] if i==v else 0 for k,(j,i) in enumerate(edges)) for v in range(len(primes))]
    s=group_generated(sg,mods); t=group_generated(tg,mods); st=group_generated(sg+tg,mods)
    # Independently calculate the common elements by direct source and target
    # powers, without using the generated sets or their intersection.
    r=[lcm(*(next(n for n in range(1,primes[j]) if pow(primes[i],n,primes[j])==1)
             for j,k in edges if k==i)) for i in range(len(primes))]
    equal=0
    for vs in product(*(range(p-1) for p in primes)):
        for ts in product(*(range(z) for z in r)):
            if all(vs[j]==(ts[i]*logs[k][primes[i]%primes[j]])%(primes[j]-1)
                   for k,(j,i) in enumerate(edges)):
                equal+=1
    intersection=len(s&t)
    assert equal==intersection and len(st)*intersection==len(s)*len(t)
    size=prod(mods); assert len(st)==len(s)*len(t)//intersection
    # Partition the entire parameter set by actual translation orbits.
    remaining=set(product(*(range(m) for m in mods))); reps=[]
    while remaining:
        x=min(remaining); reps.append(x)
        orbit={tuple((a+b)%m for a,b,m in zip(x,g,mods)) for g in st}
        assert orbit<=remaining and len(orbit)==len(st)
        remaining-=orbit
    result=(size,len(s),len(t),intersection,len(reps))
    assert result==expected,(result,expected)
    print('primes',primes,'edges',[(primes[j],primes[i]) for j,i in edges])
    print('L,S,T,S∩T,classes =',result,'; Frobenius orders =',tuple(r))
    print('edge primitive roots =',refs,'; lexicographic exponent representatives =',reps)

check((3,7,13),[(0,1),(1,2),(2,0)],(144,144,6,6,1))
check((3,7,13),[(i,j) for i in range(3) for j in range(3) if i!=j],(20736,144,144,2,2))
check((3,5,7),[(i,j) for i in range(3) for j in range(3) if i!=j],(2304,48,288,6,1))
print('Finite parameter-orbit checks only; no loop or simplicity enumeration.')
