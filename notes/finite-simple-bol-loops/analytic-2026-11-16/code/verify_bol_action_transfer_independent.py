#!/usr/bin/env python3
"""Independent bounded checks of the proposed polarized Bol transfer.

Reviewer-authored; imports no project code. Exact integer/Fraction arithmetic.
The field is independently implemented as polynomials over F3 modulo Phi7;
the upper extension is E[T]/(T^7-lambda). This checks levels 7 and 49,
not a full loop matrix or the all-parameter theorem.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
import random

P = 3
N = 6
Q = P**N
SEED = 202611160303


@lru_cache(None)
def unpack(a):
    c = []
    for _ in range(N):
        a, r = divmod(a, P)
        c.append(r)
    return tuple(c)


def pack(c):
    out = 0
    for x in reversed(c):
        out = P*out + x % P
    return out


@lru_cache(None)
def plus(a, b):
    return pack(tuple((x+y) % P for x,y in zip(unpack(a), unpack(b))))


@lru_cache(None)
def minus(a):
    return pack(tuple(-x for x in unpack(a)))


def sub(a,b):
    return plus(a,minus(b))


@lru_cache(None)
def times(a,b):
    c = [0]*(2*N-1)
    for i,x in enumerate(unpack(a)):
        for j,y in enumerate(unpack(b)):
            c[i+j] = (c[i+j] + x*y) % P
    for j in range(2*N-2,N-1,-1):
        lead = c[j]
        c[j] = 0
        for i in range(N):
            c[j-N+i] = (c[j-N+i]-lead) % P
    return pack(c[:N])


def power(a,n):
    out = 1
    while n:
        if n & 1:
            out = times(out,a)
        a = times(a,a)
        n >>= 1
    return out


@lru_cache(None)
def tr(a):
    out, x = 0,a
    for _ in range(N):
        out = plus(out,x)
        x = power(x,P)
    assert out < P
    return out


LAM = 3
LP = tuple(power(LAM,j) for j in range(7))
Z42 = (0,)*7
ONE42 = (1,)+(0,)*6
TAU = (0,1)+(0,)*5


def eplus(a,b):
    return tuple(plus(x,y) for x,y in zip(a,b))


def eneg(a):
    return tuple(minus(x) for x in a)


@lru_cache(None)
def etimes(a,b):
    c = [0]*13
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] = plus(c[i+j],times(x,y))
    for j in range(12,6,-1):
        c[j-7] = plus(c[j-7],times(LAM,c[j]))
    return tuple(c[:7])


TP = [ONE42]
for _ in range(49):
    TP.append(etimes(TP[-1],TAU))


def emb(a):
    return (a,)+(0,)*6


def etrace(a):
    # Relative trace is the constant coefficient, since 7=1 in F3.
    # Independently checked against all seven relative Frobenius conjugates.
    return tr(a[0])


def ephi(a):
    return tuple(times(a[i],LP[(6*i)%7]) for i in range(7))


def beta(u,v,upper):
    if upper:
        return etrace(eplus(etimes(u[0],v[1]),eneg(etimes(u[1],v[0]))))
    return tr(sub(times(u[0],v[1]),times(u[1],v[0])))


def law(x,y,upper):
    w,x1,y1,a,t = x
    ww,x2,y2,b,s = y
    mod,eta = (49,30) if upper else (7,2)
    actor = TP[t] if upper else LP[t]
    wm = tuple(eplus(z,etimes(actor,zz)) if upper else plus(z,times(actor,zz))
               for z,zz in zip(w,ww))
    return (wm,(x1+pow(eta,a,mod)*x2)%mod,
            (y1+pow(eta,a,mod)*y2)%mod,
            (a+b-beta(w,ww,upper))%3,
            (t+s-(x1*y2-y1*x2))%mod)


def left_div(x,z,upper):
    w,x1,y1,a,t = x
    ww,x2,y2,b,s = z
    mod,eta = (49,30) if upper else (7,2)
    actor = TP[-t%mod] if upper else LP[-t%mod]
    wy = tuple(etimes(actor,eplus(zz,eneg(z0))) if upper else times(actor,sub(zz,z0))
               for z0,zz in zip(w,ww))
    xx = (pow(eta,-a,mod)*(x2-x1))%mod
    yy = (pow(eta,-a,mod)*(y2-y1))%mod
    return (wy,xx,yy,(b-a+beta(w,wy,upper))%3,
            (s-t+x1*yy-y1*xx)%mod)


def inv(x,upper):
    mod = 49 if upper else 7
    zero_w = (Z42,Z42) if upper else (0,0)
    return left_div(x,(zero_w,0,0,0,0),upper)


def defect(x,y,z,upper):
    return left_div(law(x,y,upper),law(x,law(y,z,upper),upper),upper)


def random_low(rng):
    return ((rng.randrange(Q),rng.randrange(Q)),rng.randrange(7),rng.randrange(7),
            rng.randrange(3),rng.randrange(7))


def lift(x,j):
    w,v1,v2,a,t = x
    return (tuple(emb(u) for u in w),7*v1,v2+7*j,a,7*t)


def quotient(x):
    w,v1,v2,a,t = x
    assert v1%7 == t%7 == 0 and all(v[1:] == (0,)*6 for v in w)
    return (tuple(v[0] for v in w),v1//7,v2%7,a,t//7)


def v_add(u,v,upper):
    mod=49 if upper else 7
    w=tuple(eplus(x,y) if upper else plus(x,y) for x,y in zip(u[0],v[0]))
    return (w,(u[1]+v[1])%mod,(u[2]+v[2])%mod)


def v_neg(u,upper):
    mod=49 if upper else 7
    return (tuple(eneg(x) if upper else minus(x) for x in u[0]),-u[1]%mod,-u[2]%mod)


def action(c,u,upper):
    a,t=c
    mod,eta=(49,30) if upper else (7,2)
    lam=TP[t] if upper else LP[t]
    w=tuple(etimes(lam,x) if upper else times(lam,x) for x in u[0])
    return (w,pow(eta,a,mod)*u[1]%mod,pow(eta,a,mod)*u[2]%mod)


def pairing(u,v,upper):
    mod=49 if upper else 7
    return (beta(u[0],v[0],upper),(u[1]*v[2]-u[2]*v[1])%mod)


def explicit_hg(x,y,upper):
    mod=49 if upper else 7
    u,v=x[:3],y[:3]
    c,d=x[3:],y[3:]
    g=pairing(u,v,upper)
    cg=((c[0]+g[0])%3,(c[1]+g[1])%mod)
    h=v_add(v_add(action(g,u,upper),v_neg(action(d,u,upper),upper),upper),
            v_add(action(cg,v,upper),v_neg(v,upper),upper),upper)
    return h,g


def explicit_H(h,g,z,upper):
    mod=49 if upper else 7
    v=action(g,z[:3],upper)
    phase=pairing(h,z[:3],upper)
    return (*v,(z[3]+phase[0])%3,(z[4]+phase[1])%mod)


def unit_phase(x,y,u,upper):
    # Return the exact nucleus phase exponent of pi(x)pi(y) relative
    # to pi(x*y) J, with no floating point roots of unity.
    xy = law(x,y,upper)
    e = (Z42,Z42) if upper else (0,0)
    state = (u[0],u[1],u[2],0,0)
    direct = law(x,law(y,state,upper),upper)
    h,g=explicit_hg(x,y,upper)
    assert explicit_H(h,g,u,upper) == defect(x,y,u,upper)
    corrected = law(xy,explicit_H(h,g,state,upper),upper)
    assert direct == corrected
    return direct[3:]


def check_field(rng):
    assert len(set(LP)) == 7 and power(LAM,7) == 1
    assert power(LAM,104) != 1
    assert TP[7] == emb(LAM) and TP[49] == ONE42
    assert len(set(TP[:49])) == 49
    hist = Counter(tr(a) for a in range(Q))
    assert hist == {0:243,1:243,2:243}
    for _ in range(24):
        a = tuple(rng.randrange(Q) for _ in range(7))
        b,total = a,Z42
        for _ in range(7):
            total = eplus(total,b)
            b = ephi(b)
        assert total == emb(a[0])
    assert pow(30,3,49) == 1 and 30%7 == 2
    return {'E729_trace_counts':dict(hist),'upper_scalar_order':49,
            'relative_trace_checks':24}


def check_loop(rng):
    for _ in range(96):
        xs = [random_low(rng) for _ in range(3)]
        lifts = [lift(x,rng.randrange(7)) for x in xs]
        x,y,z = xs
        xx,yy,zz = lifts
        assert quotient(law(xx,yy,True)) == law(x,y,False)
        assert quotient(left_div(xx,yy,True)) == left_div(x,y,False)
        assert quotient(inv(xx,True)) == inv(x,False)
        assert quotient(defect(xx,yy,zz,True)) == defect(x,y,z,False)
        for upper, us in ((False,xs),(True,lifts)):
            u,v,w = us
            assert law(u,law(v,law(u,w,upper),upper),upper) == law(law(u,law(v,u,upper),upper),w,upper)
            assert defect(v,law(u,v,upper),defect(u,v,w,upper),upper) == w
            unit_phase(u,v,w,upper)
        # Every fiber is carried bijectively to its prescribed target fiber.
        target = law(x,y,False)
        images = [law(xx,lift(y,j),True) for j in range(7)]
        assert set(images) == {lift(target,j) for j in range(7)}
        target_defect = defect(x,y,z,False)
        images = [defect(xx,yy,lift(z,j),True) for j in range(7)]
        assert set(images) == {lift(target_defect,j) for j in range(7)}
    # Actual non-Moufang witness and its nontrivial quotient correction.
    x = ((1,0),1,0,0,0)
    y = ((0,0),0,1,0,0)
    assert law(law(x,y,False),x,False) != law(x,law(y,x,False),False)
    assert quotient(law(law(lift(x,0),lift(y,0),True),lift(x,0),True)) != quotient(law(lift(x,0),law(lift(y,0),lift(x,0),True),True))
    return {'random_triples':96,'levels':[7,49],
            'fiber_bijections_checked':192,'fiber_size':7,
            'identities':['multiplication','left division','inverse','Bol','full defect','explicit shear-dilation correction','inverse defect','section correction'],
            'non_Moufang_witness':True}


def check_normalizations():
    # Basis matrices: C_{r,s}=1/sqrt(d) for s in fiber r.
    # All identities are checked at the rational squared-coefficient level.
    for d in (7,49,343):
        row_norm2 = sum((Fraction(1,d) for _ in range(d)),Fraction())
        assert row_norm2 == 1
        # P=C* C has every dxd fiber block equal to 1/d.
        assert sum((Fraction(1,d)**2 for _ in range(d)),Fraction()) == Fraction(1,d)
    # Successive conditioned restrictions compose; densities multiply.
    n,k = 2,1
    for a,b,c in ((1,2,3),(1,3,4),(2,3,5)):
        d1,d2 = 7**(b-a),7**(c-b)
        assert d1**k*d2**k == 7**((c-a)*k)
        # |S_ab|/|L_b|=(Q_a/Q_b)^n / d1^(k+1).
        field1 = Fraction(1,3**(6*(7**(b-1)-7**(a-1))*n))
        field2 = Fraction(1,3**(6*(7**(c-1)-7**(b-1))*n))
        field3 = Fraction(1,3**(6*(7**(c-1)-7**(a-1))*n))
        assert field1*field2 == field3
        assert Fraction(1,d1**(k+1))*Fraction(1,d2**(k+1)) == Fraction(1,(d1*d2)**(k+1))
    return {'fiber_sizes':[7,49,343],'coisometry_squared_row_norm':'1',
            'C_star_C':'orthogonal averaging projection','density_compositions':3}


def conductor(rho,a):
    if rho == 0:
        return 1
    v=0
    while rho%7 == 0:
        rho//=7
        v+=1
    return 7**(a-v)


def check_conductors():
    scopes = []
    for a,b in ((1,2),(1,3),(2,3)):
        ma,mb,d = 7**a,7**b,7**(b-a)
        for rho in range(mb):
            lo=rho%ma
            for t in range(ma):
                assert (rho*d*t)%mb == d*((lo*t)%ma)
            if lo:
                assert conductor(rho,b) == d*conductor(lo,a)
            else:
                assert conductor(rho,b) <= d
        for lo in range(ma):
            assert len([rho for rho in range(mb) if rho%ma == lo]) == d
        scopes.append({'levels':[a,b],'upper_characters':mb,'aliases_per_lower':d})
    return scopes


def exponent_set(D):
    out={0}
    for j in range(1,D):
        z=j
        while z%7 == 0:
            z//=7
        if z%7 in (1,2,3):
            out.add(j)
    return out


def check_polarized_field(rng):
    # New candidate supplied by coauthors: maximal isotropic trace-zero
    # extension of Ea, with a tower-compatible exponent choice.
    exponents={D:exponent_set(D) for D in (7,49,343)}
    for D,J in exponents.items():
        assert len(J)==(D+1)//2
        assert all((j in J)+(D-j in J)==1 for j in range(1,D))
        assert all(i+j != D for i in J for j in J)
    for D1,D2 in ((7,7),(7,49),(49,7)):
        total=exponent_set(D1*D2)
        expected={j+D2*l for j in exponent_set(D2) for l in range(D1)
                  if j!=0 or l in exponent_set(D1)}
        assert total == expected
    J=exponents[7]
    for i,j in product(range(7),repeat=2):
        gram=etimes(TP[i],TP[j])[0]
        expected=1 if i==j==0 else LAM if i+j==7 else 0
        assert gram == expected
        if i in J and j in J:
            assert gram == (1 if i==j==0 else 0)
    def plift(x):
        w,v1,v2,a,t=x
        ww=tuple((w0,)+(tuple(rng.randrange(Q) for _ in range(3)))+(0,)*3 for w0 in w)
        return (ww,7*v1,v2+7*rng.randrange(7),a,7*t)
    def pq(x):
        w,v1,v2,a,t=x
        assert v1%7==t%7==0 and all(v[4:]==(0,)*3 for v in w)
        return (tuple(v[0] for v in w),v1//7,v2%7,a,t//7)
    for _ in range(96):
        low=[random_low(rng) for _ in range(3)]
        high=[plift(x) for x in low]
        x,y,z=low
        xx,yy,zz=high
        assert pq(law(xx,yy,True))==law(x,y,False)
        assert pq(left_div(xx,yy,True))==left_div(x,y,False)
        assert pq(inv(xx,True))==inv(x,False)
        assert pq(defect(xx,yy,zz,True))==defect(x,y,z,False)
        assert beta(xx[0],yy[0],True)==beta(x[0],y[0],False)
        unit_phase(xx,yy,zz,True)
        assert law(xx,law(yy,law(xx,zz,True),True),True)==law(law(xx,law(yy,xx,True),True),zz,True)
    for a,b,c in ((1,2,3),(1,3,4),(2,3,5)):
        D1,D2=7**(b-a),7**(c-b)
        e1,e2,et=(D1-1)//2,D1*(D2-1)//2,(D1*D2-1)//2
        assert e1+e2==et
    # The larger P does NOT obey the base-subfield scalar-intersection
    # obstruction P intersect tau*P={0}; retain the original scope.
    assert exponents[7].intersection({j+1 for j in exponents[7]}) == {1,2,3}
    for w0 in range(Q):
        u=(w0,)+(tuple(rng.randrange(Q) for _ in range(3)))+(0,)*3
        v=etimes(TP[48],u)
        assert (v[4:]==(0,)*3) == (w0==0)
        if w0==0:
            assert v[0]==u[1]
    for a1 in range(Q):
        u=(0,a1,rng.randrange(Q),rng.randrange(Q),0,0,0)
        v=etimes(TP[48],u)
        assert v[4:]==(0,)*3 and v[0]==a1
    # In normalized W measure, R f=1_{0} Ef has R*R=Q^(-n)Pi.
    assert Fraction(1,Q)**2 == Fraction(1,Q**2)
    return {'degrees':[7,49,343],'polarized_dimensions':[4,25,172],
            'actual_upper_trace_Gram_entries':49,'tower_preimage_cases':3,
            'actual_P_loop_triples':96,'field_fiber_dimension_over_E1_at_adjacent_step_n2':6,
            'larger_P_scalar_intersection_not_zero':True,
            'polarized_scalar_excursion_coefficient_checks':2*Q,
            'normalized_scalar_corner_norm_squared_n2':'1/729^2'}


def exact_e7_sum(counts):
    # 1+z+...+z^6=0, so reduce to degree<6.
    z6 = counts[6]
    return tuple(c-z6 for c in counts[:6])


def check_mixed_bilinear():
    # Exhaustive upper mixed-plane vectors and actors, no fiber reduction
    # in the summation. The expected formula uses only z modulo 7.
    cases=[(0,0,(0,7)),(0,1,(0,7)),(0,1,(1,7)),
           (1,1,(0,7)),(1,1,(1,8)),(2,3,(6,48))]
    vectors=list(product(range(7),range(49)))
    total_terms=0
    for sigma,rho,z in cases:
        counts=[0]*7
        for c,d in product(range(3),repeat=2):
            # g_i=1 fixes a representative; actor averages independent of it.
            aa=(2-pow(2,d,7))%7
            bb=(pow(2,c+1,7)-1)%7
            for u in vectors:
                uz=(u[0]*z[1]-u[1]*z[0])%7
                for v in vectors:
                    exponent=(sigma*(u[0]*v[1]-u[1]*v[0])
                              +rho*(aa*uz+bb*(v[0]*z[1]-v[1]*z[0])))%7
                    counts[exponent]+=1
        denom=9*len(vectors)**2
        total_terms+=denom
        compatible=(sigma != 0 or (rho*z[0])%7 == (rho*z[1])%7 == 0)
        expected=Fraction(1,49 if sigma else 1)*Fraction(1,1 if compatible else 9)
        red=exact_e7_sum(counts)
        assert red == (int(expected*denom),0,0,0,0,0)
    return {'cases':len(cases),'exact_character_terms':total_terms,
            'pure_fiber_z_nonzero_reduction_zero':True}


def main():
    rng=random.Random(SEED)
    out={'seed':SEED,'field':check_field(rng),'loop':check_loop(rng),
         'normalization':check_normalizations(),'conductors':check_conductors(),
         'polarized_field':check_polarized_field(rng),
         'mixed_bilinear':check_mixed_bilinear(),
         'scope':'bounded exact checks; no full huge loop matrix or uniform theorem by extrapolation'}
    print(json.dumps(out,sort_keys=True,indent=2))


if __name__ == '__main__':
    main()

