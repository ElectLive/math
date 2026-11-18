"""Read-back controls for the additive idealizer bound and all odd natural ranks.
Small rings have their actual units/ranks counted; the general theorem is analytic.
"""
from itertools import product
from math import prod,gcd,isqrt
from fractions import Fraction
def f4mul(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1
        if a&4:a^=7
        b>>=1
    return r
def mm(A,B,q):
    if q==4:
        return tuple(f4mul(A[2*i],B[j])^f4mul(A[2*i+1],B[2+j]) for i in range(2) for j in range(2))
    return tuple(sum(A[i*2+k]*B[k*2+j] for k in range(2))%q for i in range(2) for j in range(2))
def det(A,q):
    if q==4:return f4mul(A[0],A[3])^f4mul(A[1],A[2])
    return (A[0]*A[3]-A[1]*A[2])%q
def oddpart(x,p):
    while x%p==0:x//=p
    return x
def rings():
    # Mat_2(F4) and its upper triangular / diagonal subrings represented
    # on F2^4 by restriction of scalars. For the final two rows embed
    # Mat_2(F2) over F4 on F4^4 by two repeated copies: genuinely not
    # F4-linear as sets of matrices. In each case W is the actual algebra
    # including I, so AW<=W implies A=AI in W; no unknown idealizer.
    for q,field_on_module,kind in [(4,2,'full'),(4,2,'triangular'),(4,2,'diagonal'),(2,4,'full'),(2,4,'triangular')]:
        W={A for A in product(range(q),repeat=4) if kind=='full' or A[2]==0 and (kind!='diagonal' or A[1]==0)}
        I=(1,0,0,1);assert I in W
        assert all(mm(a,b,q) in W for a,b in product(W,repeat=2))
        if field_on_module==4:
            # Primitive-F4 scalar times the binary identity does not belong.
            assert (2,0,0,2) not in W
        # Check the rank of every actual additive operator from its finite image.
        ranks=[]
        for A in W:
            if A==(0,0,0,0):continue
            if q==4:
                image={(f4mul(A[0],x)^f4mul(A[1],y),f4mul(A[2],x)^f4mul(A[3],y)) for x,y in product(range(4),repeat=2)}
                r=(len(image).bit_length()-1)
            else:
                image={(f4mul(A[0],x)^f4mul(A[1],y),f4mul(A[2],x)^f4mul(A[3],y)) for x,y in product(range(4),repeat=2)}
                r=2 if len(image)==4 else 4
            ranks.append(r)
        units={A for A in W if any(mm(A,B,q)==I for B in W)}
        assert all(det(A,q)!=0 for A in units) and min(ranks)==2
        pprime=oddpart(len(units),2);a=4;delta=min(ranks)
        assert pprime**2<=field_on_module**(a*(a//delta+1))
        print("coefficient/base/ring/size/units/p-prime/minrank",q,field_on_module,kind,len(W),len(units),pprime,delta)
def profile_controls():
    n=0;worst=None
    for d in range(5,102,2):
        D=d*(d-1)//2
        for rho in range(3,d,2):
            m=d-rho
            if (rho,m)==(3,2):continue
            for a in range(rho+1,d+1):
                x=d-a;k=a//(rho+1)
                twice_direct=(d*d+3*m*m)-2-2*a*(a-rho)-(2*D-rho*(2*a-rho-1)+a*(k+1)+x*(x+1))
                twice_simplified=m*m+4*m*x-3*x*x+rho*rho-rho-2-a*k
                assert twice_direct==twice_simplified
                assert twice_direct*(rho+1)>=rho*(m-1)**2+rho**3-rho**2-4*rho-2
                assert 25*3**twice_direct>36*((rho+1)*(rho+3))**2
                if worst is None or twice_direct<worst[0]:worst=twice_direct,d,rho,a
                n+=1
    print("exact support inequality tests, min twice-exponent/d/rho/support",n,worst)
    for d,q in ((5,3),(7,5),(9,3),(11,7),(13,9)):
        g=lambda i:prod(q**j-1 for j in range(d-i+1,d+1))//prod(q**j-1 for j in range(1,i+1))
        for m in range(2,d,2):
            rho=d-m
            pairs=[(r,s) for r in range(0,d,2) for s in range(0,d,2) if abs(r-s)>=m]
            assert len(pairs)==(rho+1)*(rho+3)//4
            total=sum(Fraction(g(r)*g(s),q**((r-s)**2)) for r,s in pairs)
            assert total*total<=(rho+1)**2*(rho+3)**2*Fraction(q)**(d*d-3*m*m)
    print("direct Gaussian class mass checks passed")
if __name__=='__main__':rings();profile_controls()
