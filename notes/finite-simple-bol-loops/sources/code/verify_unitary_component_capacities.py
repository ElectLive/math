"""Exact arithmetic only; group/classification inputs belong to the linked proofs."""

from math import prod

def unitary(n):
    return 2**(n*(n-1)//2)*prod(2**i-(-1)**i for i in range(1,n+1))

def symp(m):
    return 2**(m*m)*prod(2**(2*i)-1 for i in range(1,m+1))

su3=4**3*(4**3+1)*(4**2-1)
sp2=4*(4**2-1)
inner=(4**3+1)*(4-1)
assert su3==62400 and inner==195 and su3//sp2==1040
assert su3//3 == 20800
assert 5*(1+inner+su3//sp2) == 6180 < 20800
print('SU3(4): lower 20800 > upper 6180')

for q in (2,4):
    f=q.bit_length()-1
    Q=q*q
    gl2=(Q*Q-1)*(Q*Q-Q)
    H=(2*f)**2*gl2*(q+1)*Q*(Q*Q-1)
    rank1=(q**11+1)*(q**10-1)//(q+1)
    capacity=(q+1)*(1+rank1)
    assert q**55>H*capacity
    print('G2 extension:',q,'H bound',H,'capacity',capacity,'strict inequality passes')

U=unitary(11)
assert U%3==0
Y=U//3
counts=[]
for r in range(1,6):
    c=2**(r*(22-3*r))*unitary(r)*unitary(11-2*r)
    assert U%c==0
    counts.append(U//c)
assert Y%symp(5)==0
outside=Y//symp(5)
j=1+sum(counts)+outside
assert j==44060932153827917824
I=6*448345497600
assert Y>I*3*j
print('Suz: |Y|',Y,'j',j,'strict inequality passes')

# U6(2): odd-diagonal canonical extension, using the pinned maximal-order list.
maximal_orders=(13685760,13271040,10321920,6531840,1474560,1451520,443520,155520,93312,40320)
assert symp(3)==1451520 and symp(3)//3==483840
assert [x for x in maximal_orders if x%483840==0]==[1451520]
print("U6(2): only Sp6(2) order is divisible by 483840")
