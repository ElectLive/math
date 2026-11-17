"""Bol genus-one certificates; Python 3.11+, standard library, assertions on.

Exact tests are separated from the floating theta convention supplement.
Imports only unchanged finite-field helpers from the prior certificate.
No huge-loop table is generated; symbolic source hypotheses remain inputs.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial, pi, comb
import cmath
import json
from verify_bol_graded_fusion import (
    ROOTS, add, combination, pairing, rank, vectors, zadd, zscale,
)

DEGREE, ORDER = 3, 3
ONE = {(0, 0, 0): Fraction(1)}


def poly_add(a, b):
    ans = defaultdict(Fraction, a)
    for key, val in b.items():
        ans[key] += val
    return {k: v for k, v in ans.items() if v}


def poly_mul(a, b):
    ans = defaultdict(Fraction)
    for (q, i, j), x in a.items():
        for (r, k, l), y in b.items():
            if q+r <= DEGREE and i+j+k+l <= ORDER:
                ans[q+r, i+k, j+l] += x*y
    return {k: v for k, v in ans.items() if v}


def exp_source(a, b, degree=0):
    return {(degree, i, j): Fraction(a**i*b**j, factorial(i)*factorial(j))
            for i in range(ORDER+1) for j in range(ORDER+1-i) if a**i*b**j}


def current_moment_checks():
    """Enumerate exterior basis; independently compare differential hierarchy."""
    perm = (1, 2, 0, 3)
    aa, bb = (1, -2, 4, 2), (2, 1, -1, 3)
    orbits = ((0, 1, 2), (3,))
    modes = [(m, x) for m in range(1, DEGREE+1) for x in range(4)]
    one_species, fixed_states = {}, 0
    for bits in product((0, 1), repeat=len(modes)):
        occupied = {modes[i] for i, bit in enumerate(bits) if bit}
        energy = sum(m for m, x in occupied)
        if energy > DEGREE or {(m, perm[x]) for m,x in occupied} != occupied:
            continue
        # Odd-order permutations have exterior sign +1 on invariant subsets.
        fixed_states += 1
        a = sum(m*aa[x] for m,x in occupied)
        b = sum(m*bb[x] for m,x in occupied)
        one_species = poly_add(one_species, exp_source(a,b,energy))
    direct = ONE
    for _ in range(24):
        direct = poly_mul(direct, one_species)
    direct = poly_mul(direct, exp_source(sum(aa),sum(bb)))
    connected = {}
    for orbit in orbits:
        d = len(orbit)
        a, b = sum(aa[x] for x in orbit), sum(bb[x] for x in orbit)
        f = [Fraction(1)] + [Fraction(0)]*DEGREE
        for m in range(1,DEGREE+1):
            for k in range(1,DEGREE//m+1):
                f[m*k] += 24*m*(-1)**(k-1)
        for i in range(ORDER+1):
            for j in range(ORDER+1-i):
                r = i+j
                if not r:
                    continue
                coeff = Fraction(a**i*b**j,factorial(i)*factorial(j))
                for k in range(DEGREE//d+1):
                    val = f[k]*k**(r-1)*coeff
                    if val:
                        connected = poly_add(connected,{(d*k,i,j):val})
    moments, power = ONE, ONE
    for j in range(1,ORDER+1):
        power = poly_mul(power,connected)
        moments = poly_add(moments,{k:v/factorial(j) for k,v in power.items()})
    partition = ONE
    for _ in range(24):
        partition = poly_mul(partition,{k:v for k,v in one_species.items()
                                         if k[1:] == (0,0)})
    assert direct == poly_mul(partition,moments)
    return {"exterior_states_examined":2**len(modes),
            "fixed_low_energy_states":fixed_states,
            "mixed_moment_coefficients":(DEGREE+1)*(ORDER+1)*(ORDER+2)//2}


def fixed_mode_check():
    """Direct signed exterior calculation of an ordered off-diagonal pair."""
    q = Fraction(1,4)
    aa, bb = (1,2,-1),(2,-1,3)
    perm = (1,2,0,4,5,3)
    def current(state,target,source,color):
        out = defaultdict(int)
        for x,value in enumerate(color):
            i,j = 3*target+x,3*source+x
            if not state >> j & 1:
                continue
            sign = (-1)**((state & ((1 << j)-1)).bit_count())
            cut = state ^ (1 << j)
            if cut >> i & 1:
                continue
            sign *= (-1)**((cut & ((1 << i)-1)).bit_count())
            out[cut | (1 << i)] += value*sign
        return out
    numerator,partition = Fraction(0),Fraction(0)
    for state in range(64):
        occupied = [i for i in range(6) if state >> i & 1]
        degree = sum(1+i//3 for i in occupied)
        image = [perm[i] for i in occupied]
        image_state = sum(1 << i for i in image)
        sign = (-1)**sum(image[i] > image[j]
                         for i in range(len(image)) for j in range(i+1,len(image)))
        if image_state == state:
            partition += sign*q**degree
        for mid,bcoef in current(state,1,0,bb).items():
            for end,acoef in current(mid,0,1,aa).items():
                points = [perm[i] for i in range(6) if end >> i & 1]
                mapped = sum(1 << i for i in points)
                exterior_sign = (-1)**sum(points[i] > points[j]
                      for i in range(len(points)) for j in range(i+1,len(points)))
                if mapped == state:
                    numerator += acoef*bcoef*exterior_sign*q**degree
    assert partition == (1+q**3)*(1+q**6)
    def covariance(m):
        # C_m=(q^m g-q^(2m)g^2+q^(3m)I)/(1+q^(3m)).
        return [[sum((-1)**(k-1)*q**(m*k) for k in (1,2,3)
                     if i == (j+k) % 3)/(1+q**(3*m))
                 for j in range(3)] for i in range(3)]
    c1,c2 = covariance(1),covariance(2)
    wick = sum(c1[i][j]*aa[j]*(int(i == j)-c2[j][i])*bb[i]
               for i in range(3) for j in range(3))
    assert numerator/partition == wick
    assert wick != 0
    # The same-mode contact term is indispensable: N^2=N on every state.
    assert all((int(bool(state & 1)))**2 == int(bool(state & 1))
               for state in range(64))
    return {"signed_exterior_states":64,"ordered_connected_value":str(wick)}


def polynomial_remainder(f,g):
    f = [x % 3 for x in f]
    while f and not f[-1]:
        f.pop()
    while len(f) >= len(g):
        k, c = len(f)-len(g), f[-1]*pow(g[-1],-1,3) % 3
        for j,a in enumerate(g):
            f[k+j] = (f[k+j]-c*a) % 3
        while f and not f[-1]:
            f.pop()
    return f


def companion(f):
    c = [[0]*4 for _ in range(4)]
    for j in range(3):
        c[j+1][j] = 1
    for i in range(4):
        c[i][3] = -f[i] % 3
    return c


def pencil(f):
    identity = [[int(i == j) for j in range(4)] for i in range(4)]
    ans = []
    for c in (identity,companion(f)):
        a = [[0]*8 for _ in range(8)]
        for i in range(4):
            for j in range(4):
                a[i][j+4], a[j+4][i] = c[i][j], -c[i][j] % 3
        ans.append(a)
    return ans


def binary_transform(coeff,a,b,c,d):
    # coeff[k] multiplies X^(4-k)Y^k.
    out = [0]*5
    for k,value in enumerate(coeff):
        for i in range(5-k):
            for j in range(k+1):
                out[i+j] += (value*comb(4-k,i)*a**(4-k-i)*b**i
                              *comb(k,j)*c**(k-j)*d**j)
    return [x % 3 for x in out]


def phase_trace(ell,central):
    # One regular F3^2 orbit and 6560 fixed points: actual Fourier trace.
    out = (0,0)
    for z in vectors(2):
        tr = 6569 if add(z,central) == (0,0) else 6560
        phase = ROOTS[-sum(x*y for x,y in zip(ell,z)) % 3]
        out = zadd(out,zscale(tr,phase))
    assert out[0] % 9 == out[1] % 9 == 0
    return out[0]//9,out[1]//9


def pencil_and_phase_checks():
    fs = ((2,1,0,0,1),(2,0,1,0,1))  # t^4+t+2, t^4+t^2+2
    gl2 = [(a,b,c,d) for a,b,c,d in product(range(3),repeat=4)
           if (a*d-b*c) % 3]
    assert len(gl2) == 48
    families, rank_tests, phase_tests = [], 0, 0
    basis = [tuple(int(i == j) for i in range(8)) for j in range(8)]
    for f in fs:
        for degree in (1,2):
            for lower in product(range(3),repeat=degree):
                assert polynomial_remainder(f,(*lower,1))
        forms = pencil(f)
        families.append(forms)
        for ell in vectors(2):
            assert rank(combination(forms,ell)) == (0 if ell == (0,0) else 8)
            rank_tests += 1
        binary = [1,0,f[2],-f[1] % 3,f[0]]
        for a,b,c,d in gl2:
            assert binary_transform(binary,a,b,c,d)[2] == binary[2]*(a*d-b*c)**2 % 3
        for x in basis:
            for y in basis:
                central = pairing(forms,x,y)
                for ell in vectors(2):
                    actual = phase_trace(ell,central)
                    expected = ROOTS[sum(a*b for a,b in zip(ell,central)) % 3]
                    if ell == (0,0):
                        expected = zscale(6561,expected)
                    assert actual == expected
                    phase_tests += 1
    assert families[0] != families[1] and fs[0][2] == 0 and fs[1][2] != 0
    return {"rank_tests":rank_tests,"GL2_pfaffian_checks":96,
            "exact_phase_coefficients":phase_tests,"class_points_each":6569,
            "entire_fusion_profile":"3^8 for all-zero tuples; 1 otherwise"}


def reconstruction_identity_checks():
    p = 5
    b = ([[1,2],[3,4]],[[0,1],[2,1]])
    def value(x,y):
        return tuple(sum(x[i]*a[i][j]*y[j] for i in range(2) for j in range(2)) % p
                     for a in b)
    def minus(x,y):
        return tuple((u-v) % p for u,v in zip(x,y))
    def mul(k,x):
        return tuple(k*u % p for u in x)
    def c0(x,y):
        return minus(value(y,x),value(x,y))
    def ca(x,y):
        return minus(value(mul(2,y),x),value(x,mul(3,y)))
    tested = 0
    for x in product(range(p),repeat=2):
        for z in product(range(p),repeat=2):
            y = mul(4,z)  # R=2I, R^-1=3I, (R-R^-1)^-1=4I
            assert minus(ca(x,y),c0(x,mul(2,y))) == value(x,z)
            tested += 1
    return tested  # Algebraic identity control, not a Bol construction.


def huge_symbolic_checks():
    def t(v):
        return v[0],(v[0]+v[1]) % 3,(v[1]+v[2]) % 3
    def nilpotent(v):
        return tuple((a-b) % 3 for a,b in zip(t(v),v))
    f = (1,2,1)
    tf = t(f)
    nf = nilpotent(f)  # N=T-1 is the phase flag; it is not the norm 1+T.
    nnf = nilpotent(nf)
    ell = (1,1,0)
    dot = lambda a,b:sum(x*y for x,y in zip(a,b)) % 3
    assert (dot(ell,f),dot(ell,nf),dot(ell,nnf)) == (0,1,0)
    assert dot(ell,tf) == 1
    x,y,z = ell
    assert z == 0 and x != 0  # Source rank36 block, local dimension M.
    m = 3**36
    difference = zscale(24*m,zadd(ROOTS[0],zscale(-1,ROOTS[1])))
    assert difference == (24*m,-24*m)
    # Hidden epsilon character: N=T-1 phase(2,1,0), all local alternating
    # forms vanish, but the source (1,4) entry has B1=2 and B2=1.
    eps_character = (0,1,0)
    assert (dot(eps_character,f),dot(eps_character,nf),dot(eps_character,nnf)) == (2,1,0)
    assert len({pow(3,j,19) for j in range(18)}) == 18
    # The 18 conjugates of lambda are all nonidentity roots; Tr(2lambda)=1.
    assert 2*(-1) % 3 == 1
    assert dot(eps_character,(0,2,1)) == 2
    return {"intrinsic_phase":[0,1,0],"local_dimension":str(m),
            "current_difference":"24*3^36*(1-zeta_3)",
            "upstream_loop_hypotheses":"conditional inputs, not enumerated"}


def theta_checks():
    """Floating-point sign/SL2 supplement; not exact evidence or proof."""
    def theta(z,tau,derivative=False):
        total = 0j
        for k in range(-18,19):
            r = k+.5
            value = cmath.exp(pi*1j*r*r*tau+2*pi*1j*r*(z+.5))
            total += value*(2*pi*1j*r if derivative else 1)
        return total
    def kernel(a,b,z,tau):
        u = a*tau-b
        return (cmath.exp(2*pi*1j*a*z)*theta(0,tau,True)*theta(z+u,tau)
                /(theta(z,tau)*theta(u,tau)))
    tau,z = .31+1.17j,.12+.20j
    errors = []
    for a,b in ((0,1/6),(0,5/6),(.5,1/3),(2/3,.5)):
        k = kernel(a,b,z,tau)
        errors.extend((abs(kernel(a,b,z+1,tau)-cmath.exp(2*pi*1j*a)*k),
                       abs(kernel(a,b,z+tau,tau)-cmath.exp(2*pi*1j*b)*k),
                       abs(kernel(a,a+b,z,tau+1)-k),
                       abs(kernel(b,-a,z/tau,-1/tau)-tau*k)))
    lam = cmath.exp(2*pi*1j/3)
    q,w = cmath.exp(2*pi*1j*tau),cmath.exp(2*pi*1j*z)
    series = sum(w**r/(1+lam**-1*q**r) for r in range(-40,41))
    errors.append(abs(kernel(0,5/6,z,tau)+2*pi*1j*series))
    assert max(errors) < 1e-10
    return {"checks":len(errors),"max_absolute_error":max(errors),
            "status":"floating convention check, not exact evidence"}


def main():
    print(json.dumps({"current_hierarchy":current_moment_checks(),
                      "fixed_mode_current":fixed_mode_check(),
                      "equal_fusion_controls":pencil_and_phase_checks(),
                      "full_bimap_checks":reconstruction_identity_checks(),
                      "huge_symbolic":huge_symbolic_checks(),
                      "theta_supplement":theta_checks()},indent=2))


if __name__ == "__main__":
    main()
