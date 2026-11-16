#!/usr/bin/env python3
"""Contributor exact finite checks; imports existing authored field/loop code.

Checks joint ranks for all base-family sector pairs, explicit ring orbit counts,
and full actual-loop defect compatibility for non-scalar orbit-sum intertwiners.
This is evidence, not an independent proof check or full-loop enumeration.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import random
import sys

code = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
sys.path.insert(0, str(code))
import verify_bol_associator_weyl as W
F = W.F
E = F.E
SEED = 2026111631


def kernel_basis(matrix):
    a = [list(row) for row in matrix]
    pivots=[]
    r=0
    for col in range(len(a[0])):
        pos=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pos is None:
            continue
        a[r],a[pos]=a[pos],a[r]
        z=E.inverse(a[r][col])
        a[r]=[E.mul(z,x) for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][col]:
                z=a[i][col]
                a[i]=[E.sub(x,E.mul(z,y)) for x,y in zip(a[i],a[r])]
        pivots.append(col)
        r+=1
        if r==len(a):
            break
    basis=[]
    for free in (j for j in range(len(a[0])) if j not in pivots):
        v=[0]*len(a[0]);v[free]=1
        for row,col in enumerate(pivots):
            v[col]=E.neg(a[row][free])
        basis.append(v)
    return basis


def joint_matrix(nu,mu,family):
    a=E.pencil(nu,family);b=E.pencil(mu,family)
    return [x+[E.neg(z) for z in y] for x,y in zip(a,b)]


def q_conductor(rho,level):
    if rho==0:return 0
    out=level
    while rho%7==0:
        rho//=7;out-=1
    return out


def rank_checks():
    outputs={}
    for family in ('good','aligned'):
        counts=Counter()
        for nu,mu in product(E.PARAMS,repeat=2):
            rank=E.matrix_rank(joint_matrix(nu,mu,family))
            parameter_rank=E.matrix_rank([list(nu),list(mu)])
            expected=0 if parameter_rank==0 else 4 if parameter_rank==1 else 6 if family=='good' else 5
            assert rank==expected
            assert len(kernel_basis(joint_matrix(nu,mu,family)))==12-rank
            counts[rank]+=1
        outputs[family]=dict(counts)
    return outputs


def ring_checks():
    outputs=[]
    for rho,tau in product(range(7),repeat=2):
        pairs=[(s,t) for s,t in product(range(7),repeat=2) if (rho*s-tau*t)%7==0]
        kernel={(s1,s2,t1,t2) for (s1,t1),(s2,t2) in product(pairs,repeat=2)}
        conductor=max(q_conductor(rho,1),q_conductor(tau,1))
        assert len(kernel)==7**(4-2*conductor)
        remaining=set(kernel);orbits=0
        while remaining:
            point=next(iter(remaining))
            orbit={tuple(pow(2,j,7)*x%7 for x in point) for j in range(3)}
            assert orbit<=kernel
            assert len(orbit)==(1 if not any(point) else 3)
            remaining-=orbit;orbits+=1
        assert orbits==1+(len(kernel)-1)//3
        outputs.append((rho,tau,len(kernel),orbits))
    # Direct scalar-kernel enumeration at imprimitive level; square gives two coordinates.
    imprimitive=[]
    for rho,tau in [(0,0),(1,0),(7,0),(7,14),(1,7),(14,21)]:
        pairs=[(s,t) for s,t in product(range(49),repeat=2) if (rho*s-tau*t)%49==0]
        a=max(q_conductor(rho,2),q_conductor(tau,2))
        assert len(pairs)**2==7**(8-2*a)
        imprimitive.append((rho,tau,len(pairs)**2))
    return {'all_mod7_sector_pairs':len(outputs),'mod7_total_kernel_points':sum(x[2] for x in outputs),'level49_cases':imprimitive}


def sample_kernel_pair(nu,mu,rho,tau,family,level,rng):
    basis=kernel_basis(joint_matrix(nu,mu,family))
    fieldvec=[F.ZERO for _ in range(12)]
    for v in basis:
        scalar=F.random_state(rng,level)[0][0]
        fieldvec=[F.fa(x,F.scale(scalar,coefficient)) for x,coefficient in zip(fieldvec,v)]
    modulus=7**level
    pairs=[(s,t) for s,t in product(range(modulus),repeat=2) if (rho*s-tau*t)%modulus==0]
    ringpairs=[rng.choice(pairs) for _ in range(6)]
    return ((tuple(fieldvec[:6]),tuple(x for x,y in ringpairs)),
            (tuple(fieldvec[6:]),tuple(y for x,y in ringpairs)))


def actual_loop_checks():
    rng=random.Random(SEED)
    records=[]
    zero=(0,0,0)
    for family in ('good','aligned'):
        for level in (1,2):
            chpairs=[((zero,0),(zero,0)),(((1,0,0),0),((0,1,0),0)),
                     (((1,0,0),1),((0,1,0),2))]
            if level==2:
                chpairs+=[(((1,2,0),7),((2,0,1),14)),((zero,7),((1,0,0),0))]
            points=0;checks=0
            for chi,psi in chpairs:
                s,t=sample_kernel_pair(*chi[:1],*psi[:1],chi[1],psi[1],family,level,rng)
                actors=[(a,g) for a in product(range(3),repeat=3) for g in range(7**level)]
                orbit={(W.actor(g,s,level),W.actor(g,t,level)) for g in actors}
                assert len(orbit)>1
                points+=len(orbit)
                for _ in range(3):
                    x=F.random_state(rng,level);y=F.random_state(rng,level)
                    out=set()
                    for s0,t0 in orbit:
                        s1,phase_s=W.correction(x,y,(s0,0),chi,family,level)
                        t1,phase_t=W.correction(x,y,(t0,0),psi,family,level)
                        assert phase_s==phase_t
                        out.add((s1,t1))
                        checks+=1
                    assert out==orbit
            records.append({'family':family,'level':level,'sector_pairs':len(chpairs),'orbit_points':points,'full_defect_terms_checked':checks})
    return records


def main():
    print(json.dumps({'seed':SEED,'shared_existing_authored_dependencies':True,
                      'joint_ranks':rank_checks(),'ring_orbits':ring_checks(),
                      'actual_loop_orbit_intertwiners':actual_loop_checks()},sort_keys=True,indent=2))

if __name__=='__main__':main()

