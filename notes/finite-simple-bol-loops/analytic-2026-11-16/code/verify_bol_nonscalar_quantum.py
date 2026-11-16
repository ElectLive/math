#!/usr/bin/env python3
"""Exact authored two-point checks in an actual admissible reciprocal Bol loop.

Independent arithmetic implementation: p=3, q=13, A=1,
E=F3[X]/(X^3-X-1)=F27, n=2, k=1, standard alternating matrix.
No existing authored checker is imported. Finite evidence, not an independent
mathematical review or an enumeration of the full enormous channel.

The field and ring averages below enumerate the actual u,v pairs, retain their
actual central defect g=b(u,v), and sum all corresponding actor c,d phases.
Their tensor product is the literal synchronized actual-defect orbit kernel.
"""
from fractions import Fraction
from itertools import product
import json
import random

SEED=2026111632
P,Q,R=3,27,13
DIG=[(a%3,(a//3)%3,a//9) for a in range(27)]


def encode(v):return sum((x%3)*3**i for i,x in enumerate(v))


def multiply(a,b):
    v=[0]*5
    for i,x in enumerate(DIG[a]):
        for j,y in enumerate(DIG[b]):v[i+j]+=x*y
    for j in (4,3):
        v[j-3]+=v[j]
        v[j-2]+=v[j]
    return encode(v[:3])


ADD=[[encode([x+y for x,y in zip(DIG[a],DIG[b])]) for b in range(Q)] for a in range(Q)]
NEG=[encode([-x for x in DIG[a]]) for a in range(Q)]
SUB=[[ADD[a][NEG[b]] for b in range(Q)] for a in range(Q)]
MUL=[[multiply(a,b) for b in range(Q)] for a in range(Q)]


def power(a,n):
    y=1
    while n:
        if n&1:y=MUL[y][a]
        a=MUL[a][a];n//=2
    return y


LAMBDA=3
LP=[power(LAMBDA,j) for j in range(R)]
ETA=[1,3,9]
TRACE=[ADD[ADD[a][power(a,3)]][power(a,9)] for a in range(Q)]
WV=list(product(range(Q),repeat=2))
VV=list(product(range(R),repeat=2))
Z=list(product(range(P),range(R)))


def detw(a,b):return SUB[MUL[a[0]][b[1]]][MUL[a[1]][b[0]]]
def detv(a,b):return (a[0]*b[1]-a[1]*b[0])%R
def aw(a,b):return ADD[a[0]][b[0]],ADD[a[1]][b[1]]
def nw(a):return NEG[a[0]],NEG[a[1]]
def av(a,b):return (a[0]+b[0])%R,(a[1]+b[1])%R
def nv(a):return (-a[0])%R,(-a[1])%R
def au(a,b):return aw(a[0],b[0]),av(a[1],b[1])
def nu(a):return nw(a[0]),nv(a[1])
def su(a,b):return au(a,nu(b))
def ac(a,b):return (a[0]+b[0])%P,(a[1]+b[1])%R
def nc(a):return (-a[0])%P,(-a[1])%R
def bform(u,v):return TRACE[detw(u[0],v[0])],detv(u[1],v[1])


def actor(c,u):
    return ((MUL[LP[c[1]]][u[0][0]],MUL[LP[c[1]]][u[0][1]]),
            ((ETA[c[0]]*u[1][0])%R,(ETA[c[0]]*u[1][1])%R))


def loop(x,y):
    u,c=x;v,d=y
    return au(u,actor(c,v)),ac(ac(c,d),nc(bform(u,v)))


def ldivide(x,target):
    u,c=x;w,e=target
    v=actor(nc(c),su(w,u))
    return v,ac(ac(e,nc(c)),bform(u,v))


def chi(character,c):return (R*character[0]*c[0]+P*character[1]*c[1])%(P*R)


def pi(x,state,character):
    u,phase=state;a,c=x
    return au(a,actor(c,u)),(phase+chi(character,ac(c,nc(bform(a,u)))))%(P*R)


def pi_inverse(x,state,character):
    out,phase=state;a,c=x
    u=actor(nc(c),su(out,a))
    return u,(phase-chi(character,ac(c,nc(bform(a,u)))))%(P*R)


def correction(x,y):
    u,c=x;v,d=y;g=bform(u,v)
    h=au(su(actor(g,u),actor(d,u)),su(actor(ac(c,g),v),v))
    return h,g


def random_u(rng):return rng.choice(WV),rng.choice(VV)
def random_x(rng):return random_u(rng),rng.choice(Z)


def arithmetic_and_loop_checks():
    assert len(set(LP))==13 and power(LAMBDA,13)==1
    assert all(power(a,26)==1 for a in range(1,Q))
    assert set(TRACE)==set(range(3))
    assert pow(3,3,13)==1
    rng=random.Random(SEED)
    for _ in range(300):
        x,y,z=(random_x(rng) for j in range(3))
        assert ldivide(x,loop(x,y))==y
        assert loop(x,loop(y,loop(x,z)))==loop(loop(x,loop(y,x)),z)
        h,g=correction(x,y);w,e=z
        assert ldivide(loop(x,y),loop(x,loop(y,z)))==(actor(g,w),ac(e,bform(h,w)))
        for character in [(0,0),(1,0),(0,1),(1,1),(2,5)]:
            actual=pi_inverse(loop(x,y),pi(x,pi(y,(w,0),character),character),character)
            assert actual==(actor(g,w),chi(character,bform(h,w)))
    return {'sampled_loop_triples':300,'sampled_exact_sector_defects':1500}


def root_product(counts1,counts2,modulus):
    out=[0]*modulus
    for a,n in enumerate(counts1):
        if n:
            for b,m in enumerate(counts2):
                if m:out[(a+b)%modulus]+=n*m
    return out


def root_rational(counts,denominator):
    # For prime modulus, 1+z+...+z^(p-1)=0. Constant iff all nonconstant
    # coefficients equal the last one; no floating point is involved.
    assert all(v==counts[-1] for v in counts[1:])
    return Fraction(counts[0]-counts[-1],denominator)


def field_kernel(target):
    # Histogram of actual (Tr det(u,v),det(u,target),det(v,target)).
    values=[detw(u,target) for u in WV]
    hist=[[[0]*Q for _ in range(Q)] for j in range(P)]
    for i,u in enumerate(WV):
        a=values[i]
        for j,v in enumerate(WV):hist[TRACE[detw(u,v)]][a][values[j]]+=1
    kernel={}
    denominator=len(WV)**2*R**2
    for gp,gq in Z:
        ccounts=[];dcounts=[]
        for a in range(Q):
            dc=[0]*P;cc=[0]*P
            for d in range(R):dc[TRACE[MUL[SUB[LP[gq]][LP[d]]][a]]]+=1
            for c in range(R):cc[TRACE[MUL[SUB[LP[(c+gq)%R]][1]][a]]]+=1
            dcounts.append(dc);ccounts.append(cc)
        total=[0]*P
        for a in range(Q):
            for b in range(Q):
                count=hist[gp][a][b]
                if count:
                    coefficient=root_product(dcounts[a],ccounts[b],P)
                    total=[x+count*y for x,y in zip(total,coefficient)]
        kernel[gp,gq]=root_rational(total,denominator)
    return kernel


def ring_kernel(target):
    values=[detv(u,target) for u in VV]
    hist=[[[0]*R for _ in range(R)] for j in range(R)]
    for i,u in enumerate(VV):
        a=values[i]
        for j,v in enumerate(VV):hist[detv(u,v)][a][values[j]]+=1
    denominator=len(VV)**2*P**2
    kernel={}
    for gp,gq in Z:
        ccounts=[];dcounts=[]
        for a in range(R):
            dc=[0]*R;cc=[0]*R
            for d in range(P):dc[(ETA[gp]-ETA[d])*a%R]+=1
            for c in range(P):cc[(ETA[(c+gp)%P]-1)*a%R]+=1
            dcounts.append(dc);ccounts.append(cc)
        total=[0]*R
        for a in range(R):
            for b in range(R):
                count=hist[gq][a][b]
                if count:
                    coefficient=root_product(dcounts[a],ccounts[b],R)
                    total=[x+count*y for x,y in zip(total,coefficient)]
        kernel[gp,gq]=root_rational(total,denominator)
    return kernel


def fourier_39(kernel,alpha,sigma):
    # Sum over e_3(alpha*gp)e_13(sigma*gq), reduce exactly modulo Phi_39.
    polynomial=[Fraction(0)]*39
    for (gp,gq),value in kernel.items():polynomial[(13*alpha*gp+3*sigma*gq)%39]+=value
    phi={24:1,23:-1,21:1,20:-1,18:1,17:-1,15:1,14:-1,12:1,
         10:-1,9:1,7:-1,6:1,4:-1,3:1,1:-1,0:1}
    for d in range(38,23,-1):
        coefficient=polynomial[d]
        if coefficient:
            for j,c in phi.items():polynomial[d-24+j]-=coefficient*c
    assert all(v==0 for v in polynomial[1:])
    return polynomial[0]


def spectrum_checks():
    field_targets=[(0,0),(1,0),(0,1),(3,7)]
    ring_targets=[(0,0),(1,0),(4,9)]
    fields={z:field_kernel(z) for z in field_targets}
    rings={z:ring_kernel(z) for z in ring_targets}
    record=[]
    for zw,zv in product(field_targets,ring_targets):
        # Every tested target is realized by a full 39-point actual pair orbit
        # in the nondegenerate chi=psi=(1,1) sector, including target zero.
        t=((1,0),(1,0));s=au(t,(zw,zv))
        orbit={(actor(g,s),actor(g,t)) for g in Z}
        assert len(orbit)==39
        literal={g:fields[zw][g]*rings[zv][g] for g in Z}
        eigenvalues={}
        for alpha,sigma in Z:
            got=fourier_39(literal,alpha,sigma)
            # Expected theorem value is checked only after independent enumeration.
            field=Fraction(1,Q**2) if alpha else Fraction(1,R**2) if any(zw) else Fraction(1)
            ring=Fraction(1,R**2) if sigma else Fraction(1,P**2) if any(zv) else Fraction(1)
            assert got==field*ring
            eigenvalues[alpha,sigma]=got
        assert min(eigenvalues.values())>=0
        if any(zw) or any(zv):assert max(eigenvalues.values())<=Fraction(1,9)
        else:assert eigenvalues[0,0]==1 and max(v for g,v in eigenvalues.items() if g!=(0,0))<Fraction(1,9)
        record.append({'field_target':zw,'ring_target':zv,'max_eigenvalue':str(max(eigenvalues.values()))})
    # Same literal counts give exact diagonal channel zero-probabilities.
    beta0=fields[0,0][0,0]
    gamma0=rings[0,0][0,0]
    Lambda=Fraction(1,3)+Fraction(2,3*Q**2)
    assert beta0==Lambda and gamma0<Fraction(1,3)
    return {'all_39_entry_kernels':len(record),'all_39_eigenvalues_per_kernel':39,
            'field_pair_enumerations':len(field_targets)*len(WV)**2,
            'ring_pair_enumerations':len(ring_targets)*len(VV)**2,
            'kernel_maxima':record,'diagonal_exact_Lambda':str(Lambda),
            'diagonal_other_multiplier':str(gamma0)}


def actual_pair_phase_checks():
    # Verify actual pi(xy)^-1 pi(x)pi(y) synchronized phases depend on precisely
    # nu*s_W-mu*t_W and rho*s_V-tau*t_V; also monomial pi preserves offdiagonals.
    rng=random.Random(SEED+1)
    characters=[(0,0),(1,0),(0,1),(1,1),(2,5)]
    for chi0,psi0 in product(characters,repeat=2):
        for _ in range(15):
            x,y=random_x(rng),random_x(rng);s,t=random_u(rng),random_u(rng)
            h,g=correction(x,y)
            sout,sp=pi_inverse(loop(x,y),pi(x,pi(y,(s,0),chi0),chi0),chi0)
            tout,tp=pi_inverse(loop(x,y),pi(x,pi(y,(t,0),psi0),psi0),psi0)
            zw=tuple(SUB[MUL[chi0[0]][a]][MUL[psi0[0]][b]] for a,b in zip(s[0],t[0]))
            zv=tuple((chi0[1]*a-psi0[1]*b)%R for a,b in zip(s[1],t[1]))
            expected=(R*TRACE[detw(h[0],zw)]+P*detv(h[1],zv))%(P*R)
            assert (sp-tp)%(P*R)==expected
            assert (sout,tout)==(actor(g,s),actor(g,t))
            assert (s==t)==(pi(x,(s,0),chi0)[0]==pi(x,(t,0),psi0)[0])
    return {'character_pairs':25,'actual_two_point_phase_cases':375}


def main():
    output={'parameters':{'p':P,'q':R,'E_size':Q,'n':2,'k':1,'level':1},
            'seed':SEED,'independent_arithmetic_no_checker_imports':True,
            'actual_loop':arithmetic_and_loop_checks(),
            'actual_two_point_phase':actual_pair_phase_checks(),
            'direct_actor_averaged_spectra':spectrum_checks()}
    print(json.dumps(output,sort_keys=True,indent=2))


if __name__=='__main__':main()

