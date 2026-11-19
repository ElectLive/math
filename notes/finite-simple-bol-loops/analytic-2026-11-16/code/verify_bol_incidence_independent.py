#!/usr/bin/env python3
"""Independent diagnostic; no imports from authored repository checkers.

Uses the actual h=1 F729 spread pencil, all parameter projective directions,
and exact F3 image enumeration. Whole W is not enumerated.
"""
from functools import lru_cache
from itertools import product
from fractions import Fraction
from collections import Counter
import random
import json

@lru_cache(None)
def coeff(x):
    return tuple((x//3**i)%3 for i in range(6))

def encode(v):
    return sum((c%3)*3**i for i,c in enumerate(v))

def add(x,y):
    return encode([a+b for a,b in zip(coeff(x),coeff(y))])

def neg(x):
    return encode([-a for a in coeff(x)])

@lru_cache(None)
def mul(x,y):
    v=[0]*11
    for i,a in enumerate(coeff(x)):
        for j,b in enumerate(coeff(y)):
            v[i+j]+=a*b
    for d in range(10,5,-1):
        t=v[d]%3
        for j in range(d-6,d):
            v[j]-=t
    return encode(v[:6])

def power(x,n):
    ans=1
    while n:
        if n&1:
            ans=mul(ans,x)
        x=mul(x,x)
        n>>=1
    return ans

@lru_cache(None)
def tr(x):
    ans=0
    for _ in range(6):
        ans=add(ans,x)
        x=power(x,3)
    assert ans in (0,1,2)
    return ans

def det(z,u,v):
    ans=0
    for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
        ans=add(ans,mul(z[i],add(mul(u[j],v[k]),neg(mul(u[k],v[j])))))
    return ans

params=list(product(range(3),repeat=3))
tbasis=(1,3,9)
zbasis=[(t,power(t,3),power(t,9)) for t in tbasis]

def injection(v):
    ans=0
    for a,t in zip(v,tbasis):
        ans=add(ans,mul(a,t))
    return ans

@lru_cache(None)
def beta(u,y):
    return tuple(tr(add(det(z,u[:3],y[:3]),det(z,u[3:],y[3:]))) for z in zbasis)

def span(vectors):
    found={(0,)*len(vectors[0])}
    for v in vectors:
        if v not in found:
            found={tuple((a+c*b)%3 for a,b in zip(x,v)) for x in found for c in range(3)}
    return found

@lru_cache(None)
def image(u):
    cols=[]
    for axis in range(6):
        for e in range(6):
            y=[0]*6;y[axis]=3**e
            cols.append(beta(u,tuple(y)))
    return span(cols)

def dot(v,w):
    return sum(a*b for a,b in zip(v,w))%3

def readout(v):
    return sum((1,2,4)[a] for a in v)%7

def degree_hist(u,a):
    values=image(u)
    hist=Counter(readout(tuple((x-b)%3 for x,b in zip(a,v))) for v in values)
    return tuple(Fraction(hist[s],len(values)) for s in range(7))

def predicted_hist(line,a):
    values=params if line is None else [v for v in params if dot(line,v)==dot(line,a)]
    hist=Counter(readout(v) for v in values)
    return tuple(Fraction(hist[s],len(values)) for s in range(7))

def check_actual_degrees():
    lines=[v for v in params if v!=(0,0,0) and next(x for x in v if x)==1]
    assert len(lines)==13
    checked=0; generic=0
    for v in lines:
        t=injection(v)
        z=(t,power(t,3),power(t,9))
        for u in (z+(0,0,0), (0,0,0)+z, z+z):
            im=image(u)
            assert len(im)==9
            assert im==set(w for w in params if dot(v,w)==0)
            for a in params:
                assert degree_hist(u,a)==predicted_hist(v,a)
                checked+=7
    rng=random.Random(1132307)
    for _ in range(20):
        u=tuple(rng.randrange(729) for _ in range(6))
        im=image(u)
        assert len(im)==27
        generic+=1
        for a in params:
            assert degree_hist(u,a)==predicted_hist(None,a)
            checked+=7
    for a in params:
        hist=degree_hist((0,)*6,a)
        assert hist[readout(a)]==1 and sum(hist)==1
        checked+=7
    return {"projective_lines":13,"exceptional_u":39,"generic_u":generic,"exact_degrees_compared":checked}

def convolution_min(k):
    minimum=3**(k-1);witness=None;classes=0
    for n0 in range(k):
        for n1 in range(k-n0+1):
            nu=(0,)*n0+(1,)*n1+(2,)*(k-n0-n1)
            counts={(0,0):1}
            for c in nu:
                nxt=Counter()
                for (target,s),n in counts.items():
                    for b in range(3):
                        nxt[((target+c*b)%3,(s+(1,2,4)[b])%7)]+=n
                counts=nxt
            assert sum(counts.values())==3**k
            assert all(sum(counts[(target,s)] for s in range(7))==3**(k-1) for target in range(3))
            v=min(counts[(c,s)] for c in range(3) for s in range(7))
            if v<minimum:
                minimum=v;witness=(n0,n1,k-n0-n1)
            classes+=1
    return {"k":k,"classes":classes,"minimum_numerator":minimum,"denominator":3**(k-1),"witness":witness}

def check_normalization():
    # A small exact restriction is counted directly; no full-space norm
    # is claimed for this slice.
    ys=[tuple(v)+(0,0,0) for v in params]
    us=[tuple(v)+(0,0,0) for v in params]
    aset=[y for y in ys if y[0]==y[2]]
    dset={((0,1,0,0,0,0),(0,0,0),3)}
    n=len(ys);m=len(us)*27*7
    total=sum(readout(tuple((x-b)%3 for x,b in zip(a,beta(u,y))))==s for y in ys for u,a,s in dset)
    actual=sum(readout(tuple((x-b)%3 for x,b in zip(a,beta(u,y))))==s for y in aset for u,a,s in dset)
    alpha=Fraction(len(aset),n)
    discrepancy=Fraction(actual,n*m)-alpha*Fraction(total,n*m)
    centered=sum((Fraction(int(y in aset))-alpha)*(Fraction(int((u,a,s) in dset))-Fraction(len(dset),m))*(readout(tuple((x-b)%3 for x,b in zip(a,beta(u,y))))==s) for y in ys for u in us for a in params for s in range(7))
    assert centered/(n*m)==discrepancy
    return {"slice_inputs":n,"slice_outputs":m,"A":len(aset),"D":len(dset),"incidences":actual,"degree_baseline":str(alpha*total),"centered_discrepancy":str(discrepancy),"full_space_norm_used":False}

def check_full_counts():
    """Count full-W incidences through exact linear image fibers."""
    aa,bb=add(1,3),9
    uu=add(power(bb,3),neg(mul(power(aa,2),bb)))
    assert uu
    xi=(mul(power(uu,2),power(aa,2)),neg(add(power(aa,6),power(uu,2))),1)
    def linear(y):
        return tr(add(add(mul(xi[0],y[0]),mul(xi[1],y[1])),mul(xi[2],y[2])))
    lines=[v for v in params if v!=(0,0,0) and v[0]==v[1] and next(c for c in v if c)==1]
    us=set()
    for nu in lines:
        t=injection(nu);z=(t,power(t,3),power(t,9))
        assert add(add(mul(z[0],xi[0]),mul(z[1],xi[1])),mul(z[2],xi[2]))==0
        inv=power(z[2],727)
        base=(mul(xi[1],inv),neg(mul(xi[0],inv)),0)
        for c,d in product((0,1,3),repeat=2):
            us.add(tuple(add(x,mul(c,y)) for x,y in zip(base,z))+tuple(mul(d,x) for x in z))
    n=729**6;m=n*27*7
    eall=0;ea=0;nd=0;image_cases=0
    for u in us:
        generators=[]
        for axis,j in product(range(6),range(6)):
            y=[0]*6;y[axis]=3**j;y=tuple(y)
            generators.append((linear(y),)+beta(u,y))
        values=span(generators)
        assert sum(v[0]==0 for v in values)*3==len(values)
        fiber=n//len(values)
        for a in params:
            full=Counter();inside=Counter()
            for v in values:
                s=readout(tuple((x-b)%3 for x,b in zip(a,v[1:])))
                full[s]+=1
                if v[0]==0:
                    inside[s]+=1
            for s in range(7):
                if 3*inside[s]>full[s]:
                    nd+=1;eall+=full[s]*fiber;ea+=inside[s]*fiber
        image_cases+=1
    alpha=Fraction(1,3);beta_d=Fraction(nd,m)
    discrepancy=Fraction(ea,n*m)-alpha*Fraction(eall,n*m)
    eps2=Fraction(6,49)*Fraction(343,729)*Fraction(1,729**4)
    rhs2=eps2*alpha*(1-alpha)*beta_d*(1-beta_d)
    assert discrepancy>0 and discrepancy*discrepancy<=rhs2
    return {"N":n,"M":m,"A":n//3,"D":nd,"incidences":ea,"degree_baseline":str(alpha*eall),"u_fiber_cases":image_cases,"positive_discrepancy":str(discrepancy),"squared_bound_ratio":str(discrepancy*discrepancy/rhs2),"full_W_counted_by_exact_fibers":True}

@lru_cache(None)
def collision(z):
    values=image(z)
    count=sum(readout(a)==readout(tuple((x-b)%3 for x,b in zip(a,v))) for a in params for v in values)
    return Fraction(count,27*len(values))

def check_variance():
    pk=predicted_hist(None,(0,0,0))
    pk2=sum(x*x for x in pk)
    t=injection((1,1,1));z=(t,power(t,3),power(t,9))
    records=[]
    for n in (1,2,3,7,20):
        aset=[tuple(mul(c,x) for x in z)+(0,0,0) for c in range(n)]
        second=sum(collision(tuple(add(x,neg(y)) for x,y in zip(v,w))) for v in aset for w in aset)/n**2
        actual=second-pk2
        bound=Fraction(6,7)*(Fraction(1,1)-Fraction(2,9)**3)/n+Fraction(6,7)*Fraction(n-1,n)*Fraction(196,729)
        assert actual==bound
        records.append({"source":"maximal_radical","n":n,"variance":str(actual),"bound_attained":True})
    rng=random.Random(1132308)
    aset=[tuple(rng.randrange(729) for _ in range(6)) for _ in range(10)]
    n=len(aset)
    second=sum(collision(tuple(add(x,neg(y)) for x,y in zip(v,w))) for v in aset for w in aset)/n**2
    actual=second-pk2
    baseline=Fraction(6,7)*(1-Fraction(2,9)**3)/n
    assert actual==baseline
    records.append({"source":"generic_distinct_differences","n":n,"variance":str(actual),"diagonal_only":True})
    return records

def check_transverse():
    # The first coordinate of both L^3 blocks is zero, so no nonzero
    # difference can lie in a spread radical.
    rng=random.Random(1132309)
    aset=[(0,rng.randrange(729),rng.randrange(729),0,rng.randrange(729),rng.randrange(729)) for _ in range(8)]
    assert len(set(aset))==len(aset)
    marg=Counter(readout(a) for a in params)
    pairs=0
    for i,y in enumerate(aset):
        for z in aset[:i]:
            diff=tuple(add(x,neg(t)) for x,t in zip(y,z))
            im=image(diff)
            assert len(im)==27
            joint=Counter((readout(a),readout(tuple((x-v)%3 for x,v in zip(a,b)))) for a in params for b in im)
            assert all(joint[(s,t)]==marg[s]*marg[t] for s,t in product(range(7),repeat=2))
            pairs+=1
    return {"transverse_points":len(aset),"actual_pair_joint_laws_checked":pairs,"law":"p_k tensor p_k"}

def check_aligned_axis():
    # For source c in a single star-vector coordinate, only beta_1 can
    # vary. All other u coordinates are irrelevant to the readout.
    source=range(37)
    max_values=0
    for u0 in range(729):
        ts={tr(mul(u0,c)) for c in source}
        for a in params:
            values={readout(((a[0]-t)%3,a[1],a[2])) for t in ts}
            assert len(values)<=3
            max_values=max(max_values,len(values))
    return {"aligned_source_size":37,"u0_cases":729,"shift_cases":27,"maximum_values":max_values}

if __name__=='__main__':
    assert power(3,7)==1 and 3!=1
    print(json.dumps({"actual_field_degrees":check_actual_degrees(),"exact_exceptional_minima":[convolution_min(k) for k in (3,5,7,9,11)],"full_counts":check_full_counts(),"slice_normalization":check_normalization(),"actual_readout_variances":check_variance(),"transverse":check_transverse(),"aligned_axis":check_aligned_axis()},sort_keys=True))
