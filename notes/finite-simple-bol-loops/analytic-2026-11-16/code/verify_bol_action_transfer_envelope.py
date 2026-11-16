#!/usr/bin/env python3
"""Authored exact checks of the polarized envelope and sector transfer.

Uses the pre-existing authored field/conductor implementation. It is not
independent evidence. No huge coset or Hilbert-space matrix is enumerated.
"""
from fractions import Fraction
import json
import random

import verify_bol_associator_weyl as A

F = A.F
SEED = 202611160304
ZERO_U = ((F.ZERO,)*6, (0,)*6)
ZERO_C = ((0,)*3, 0)


def half(c, level):
    return tuple(2*x % 3 for x in c[0]), pow(2, -1, 7**level)*c[1] % (7**level)


def group_mul(g, h, family, level):
    X,Y,z,c = g
    X1,Y1,z1,c1 = h
    RX = A.actor(c,X1,level)
    RY = A.actor(A.cneg(c,level),Y1,level)
    cross = A.cadd(A.b(X,RY,family,level), A.b(Y,RX,family,level),level)
    return (A.add(X,RX,level), A.add(Y,RY,level),
            A.cadd(A.cadd(z,z1,level),half(cross,level),level),A.cadd(c,c1,level))


def group_inverse(g, level):
    X,Y,z,c = g
    nc=A.cneg(c,level)
    return (A.actor(nc,A.neg(X,level),level),
            A.actor(c,A.neg(Y,level),level),A.cneg(z,level),nc)


def section(x, level):
    u,c=A.split(x)
    return (A.neg(A.actor(A.cneg(c,level),u,level),level),u,ZERO_C,A.cneg(c,level))


def group_action(g, point, family, level):
    X,Y,z,c=g
    u,e=A.split(point)
    Ru=A.actor(A.cneg(c,level),u,level)
    out=A.add(Y,Ru,level)
    cc=A.cadd(A.cadd(e,z,level),A.cneg(c,level),level)
    cc=A.cadd(cc,half(A.b(X,Y,family,level),level),level)
    cc=A.cadd(cc,A.b(X,Ru,family,level),level)
    return A.join(out,cc)


def lift_u(u, rng):
    v=[]
    for i in range(3):
        v.extend((7*u[1][2*i],u[1][2*i+1]+7*rng.randrange(7)))
    return u[0],tuple(v)


def lift_c(c):
    return c[0],7*c[1]


def lower_u(u):
    assert all(x[1:] == (0,)*6 for x in u[0])
    assert all(u[1][2*i] % 7 == 0 for i in range(3))
    v=[]
    for i in range(3):
        v.extend((u[1][2*i]//7,u[1][2*i+1]%7))
    return u[0],tuple(v)


def lower_c(c):
    assert c[1]%7 == 0
    return c[0],c[1]//7


def lift_point(x,rng):
    u,c=A.split(x)
    return A.join(lift_u(u,rng),lift_c(c))


def lower_point(x):
    u,c=A.split(x)
    return A.join(lower_u(u),lower_c(c))


def lower_group(g):
    X,Y,z,c=g
    return lower_u(X),lower_u(Y),lower_c(z),lower_c(c)


def lift_group(g,rng):
    X,Y,z,c=g
    return lift_u(X,rng),lift_u(Y,rng),lift_c(z),lift_c(c)


def random_group(rng):
    X,z=A.split(F.random_state(rng,1))
    Y,c=A.split(F.random_state(rng,1))
    return X,Y,z,c


def main():
    rng=random.Random(SEED)
    record={'seed':SEED,'shared_authored_field_dependency':True}
    cases=0
    sector_cases=0
    identity=(ZERO_U,ZERO_U,ZERO_C,ZERO_C)
    for family in ('good','aligned'):
        for _ in range(24):
            g,h,j=(random_group(rng) for _ in range(3))
            G,H,J=(lift_group(v,rng) for v in (g,h,j))
            x,y,z=(F.random_state(rng,1) for _ in range(3))
            X,Y,Z=(lift_point(v,rng) for v in (x,y,z))
            assert lower_group(group_mul(G,H,family,2)) == group_mul(g,h,family,1)
            assert lower_group(group_inverse(G,2)) == group_inverse(g,1)
            assert group_mul(G,group_inverse(G,2),family,2)==identity
            assert group_mul(group_mul(G,H,family,2),J,family,2)==group_mul(G,group_mul(H,J,family,2),family,2)
            assert lower_group(section(X,2))==section(x,1)
            assert group_action(section(X,2),Y,family,2)==F.op(X,Y,family,2)
            assert group_action(group_mul(G,H,family,2),Z,family,2)==group_action(G,group_action(H,Z,family,2),family,2)
            assert lower_point(group_action(G,Z,family,2))==group_action(g,z,family,1)
            XY=F.op(X,Y,family,2)
            defect=group_mul(group_inverse(section(XY,2),2),group_mul(section(X,2),section(Y,2),family,2),family,2)
            direct=A.left_division(XY,F.op(X,F.op(Y,Z,family,2),family,2),family,2)
            assert group_action(defect,Z,family,2)==direct
            assert lower_group(defect)==group_mul(group_inverse(section(F.op(x,y,family,1),1),1),group_mul(section(x,1),section(y,1),family,1),family,1)
            # Faithful upper action makes this actual group Bol palindrome.
            lhs=group_mul(group_mul(section(X,2),section(Y,2),family,2),section(X,2),family,2)
            assert lhs==section(F.op(X,F.op(Y,X,family,2),family,2),2)
            # Every upper ring-charge label, with selected p-part labels and exact phases.
            for rho in range(49):
                nu=(rho%3,(rho//3)%3,(rho//9)%3)
                up=A.pi(X,(A.split(Z)[0],0),(nu,rho),family,2)
                lo=A.pi(x,(A.split(z)[0],0),(nu,rho%7),family,1)
                assert lower_u(up[0])==lo[0] and up[1]==7*lo[1]
                upj=A.correction(X,Y,(A.split(Z)[0],0),(nu,rho),family,2)
                loj=A.correction(x,y,(A.split(z)[0],0),(nu,rho%7),family,1)
                assert lower_u(upj[0])==loj[0] and upj[1]==7*loj[1]
                sector_cases+=1
            cases+=1
    record['actual_envelope_cases']=cases
    record['full_section_and_defect_sector_cases']=sector_cases
    # Actual order-49 scalar subgroup retains seven coset labels. The cocycle
    # is checked on every ordered pair of scalar actors and every label.
    scalar_cases=0
    for t in range(49):
        for s in range(49):
            for i in range(7):
                j=(s+i)%7
                k=(t+j)%7
                h1=(s+i-j)//7
                h2=(t+j-k)//7
                whole=((t+s)%49+i-k)//7
                assert (h1+h2)%7==whole%7
                scalar_cases+=1
    record['scalar_coset_cocycle_cases']=scalar_cases
    # Exact scalar-orbit compression obstruction on an E1-line: the only
    # surviving vector is zero for any scalar exponent not divisible by7.
    support_cases=0
    for t in range(49):
        if t%7:
            for x in range(729):
                out=F.fm(F.TP[t],F.emb(x))
                assert (out[1:]==(0,)*6)==(x==0)
                support_cases+=1
    record['scalar_orbit_support_cases']=support_cases
    # Norm factors are rational at the Gram level, including towers.
    for a,b,c in ((1,2,3),(1,2,4),(2,3,4)):
        def delta(i,j,k=3,n=6):
            return Fraction(1,3**(6*(7**(j-1)-7**(i-1))*n)*7**((j-i)*(k+1)))
        assert delta(a,b)*delta(b,c)==delta(a,c)
        d=7**(b-a)
        assert d*Fraction(1,d)==1
        assert Fraction(1,d**3)*d**3==1
    record['normalization_towers']=3
    print(json.dumps(record,indent=2,sort_keys=True))


if __name__=='__main__':
    main()

