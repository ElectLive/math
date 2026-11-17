# Finite arithmetic for 0323-finite-simple-non-moufang-bol-loops:C0010.
# Canonical proof: manuscripts/unitary-four-odd-overgroups.md.
# Python 3.11+ standard library; run with assertions enabled.
# Input: four exact class-size formulas and nine mixed masks, defined below.
# Integer Bezout data are self-verified; their generator used SymPy 1.14.0
# extended polynomial gcd, but SymPy is NOT required by this certificate.
# This verifies polynomial identities/tail/finite arithmetic, not group theory.
# C0010, q == 3 mod 8 mixed-label endpoint. Python standard library only.
# Coefficient lists are ascending. All identities are verified, not assumed.
from math import comb
DATA = {5: ([0, 0, 0, 0, 1, 0, -1, 1, -1, -1, 1, -1, 0, 1], [1, -2, 2, -1, 2], [-2467, -19967, -11599, -16022], [4096, 8192, 8192, 4096, -5725, -7867, -7440, -14541, -4718, 1083, -1136, 9805, 8011], 4096), 6: ([0, 0, 0, 2, 0, -4, 2, 2, -4, 0, 2], [-4, 5, 0, 0, 1], [14348, 1453, 1963, 2653], [-1024, -1280, -1600, 5174, 6938, -5014, 380, 7706, -3926, -5306], 4096), 7: ([0, 0, 0, 0, 2, 0, -2, 2, -2, -2, 2, -2, 0, 2], [2, -4, 5, -2, 5, 1, 0, 1], [-10562, -6322, -12331, -3495, -1954, -2103, -109], [2048, 4096, 3072, -2048, -2238, -1226, -6864, -2606, 676, -2294, 3472, 4206, 218], 4096), 9: ([0, 0, 0, 0, 1, 0, -1, 0, -1, 0, 1], [1, 0, 1, 1], [8, 11, 4], [9, 0, -9, -9, 1, 7, 12, 3, -7, -4], 9), 10: ([0, 0, 2, 0, -2, 0, -2, 0, 2], [3, 2, 1], [1, 1], [96, -64, 10, 14, -12, 4, 2, -2], 288), 11: ([0, 0, 0, 0, 2, 0, -2, 0, -2, 0, 2], [2, 0, 3, 2, 1], [94, 128, 71, 18], [64, 0, -96, -64, 18, 64, 108, 28, -70, -36], 128), 13: ([0, 0, 0, 0, 1, 0, -1, 1, -1, -1, 1, -1, 0, 1], [1, -2, 3, 0, 2, 1, 1], [-450803, 138929, -218578, 89570, 54184, 108581], [36864, 73728, 36864, -147456, -28429, 62261, -206736, 84227, 93618, -126389, 181776, 54397, -108581], 36864), 14: ([0, 0, 0, 2, 0, -2, 2, -2, -2, 2, -2, 0, 2], [-4, 7, -2, 5, 3, 2, 1], [484076, 111159, 465607, 280122, 163557, 64061], [-36864, -64512, -94464, 62902, 104602, -42528, 166102, 89028, -66970, 93984, -70870, -128122], 147456), 15: ([0, 0, 0, 0, 2, 0, -2, 2, -2, -2, 2, -2, 0, 2], [2, -4, 7, 0, 5, 3, 2, 1], [-32630, 21898, -13535, 16995, 11026, 9061, 5049], [2048, 4096, 1024, -12288, -650, 6498, -14576, 9702, 8316, -10082, 14192, 2074, -10098], 4096)}
def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return trim(out)
def val(a,q):
    z=0
    for c in reversed(a): z=z*q+c
    return z
def shifted(a,c):
    out=[0]*len(a)
    for i,v in enumerate(a):
        for j in range(i+1): out[j]+=v*comb(i,j)*c**(i-j)
    return out
assert sorted(DATA)==[5,6,7,9,10,11,13,14,15]
for mask,(n,d,a,b,k) in DATA.items():
    assert add(mul(a,n),mul(b,d))==[k], (mask,'Bezout')
    # D(1027+x)>k, coefficientwise, for every x>=0.
    z=shifted(d,1027);z[0]-=k
    assert all(c>0 for c in z), (mask,'tail')
    # Verify 2*S4*D = C4*N as a polynomial identity, with S4=4|S|.
    def power(p,k):
        r=[1]
        for _ in range(k): r=mul(r,p)
        return r
    Q=[0,1]; Q2=power(Q,2); Q3=power(Q,3); Q4=power(Q,4)
    S4=mul(mul(mul(power(Q,6),add(Q2,[-1])),add(Q3,[1])),add(Q4,[-1]))
    C4=[mul([2],mul(Q2,add(Q3,[1]))),mul(Q4,mul(add(Q3,[1]),add(Q2,[1]))),mul([4],mul(Q3,mul(add(Q,[-1]),add(Q2,[1])))),mul([2],mul(Q4,mul(add(Q,[1]),add(Q3,[1]))))]
    C=[0]
    for j,c in enumerate(C4):
        if mask>>j&1: C=add(C,c)
    assert mul(mul([2],S4),d)==mul(C,n), (mask,'polynomial identity')
    for q in range(3,1027,8):
        S=q**6*(q*q-1)*(q**3+1)*(q**4-1)//4
        sizes=[q*q*(q**3+1)//2,q**4*(q**3+1)*(q*q+1)//4,q**3*(q-1)*(q*q+1),q**4*(q+1)*(q**3+1)//2]
        den=sum(c for j,c in enumerate(sizes) if mask>>j&1)
        h,rem=divmod(2*S,den)
        assert rem or h%4==0, (mask,q,'survivor')
print('9 mixed masks: Bezout identities, uniform tail, and 128 finite q values passed')
