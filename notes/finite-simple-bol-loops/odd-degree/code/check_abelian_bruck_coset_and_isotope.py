"""Independent rooted-coset and modular controls for abelian Bruck associates."""
from itertools import product
from collections import Counter
from random import Random
rng=Random(35425)
def square_modules(r,alltr=False):
    # J=(Z/r)^2; multiplication by the square root of -1 for p=3,7.
    dom=list(product(range(r),repeat=3));zero=(0,0,0)
    def add(x,y):return tuple((a+b)%r for a,b in zip(x,y))
    neg=lambda x:tuple(-a%r for a in x)
    def B(x,y):
        a,b,c=x;d,f,g=y
        return (0,(-a*g+c*d)%r,(a*f-b*d)%r)
    def solve(x,y):
        a,b,c=add(x,y);_,v,w=B(x,y);u=pow((1+a*a)%r,-1,r)
        return (a,(b+u*(v-a*w))%r,(c+u*(a*v+w))%r)
    # independent action on true cosets: recover z by solving s(0,z)H=k_x k_yH,
    # enumerating every stabilizer graph element for random pairs, not the resolvent.
    def physical(x,y):
        a=add(x,y);wanted=neg(B(x,y));found=[]
        for i,j in product(range(r),repeat=2):
            u=(0,i,j); z=add(a,neg(u))
            if add(u,neg(B(z,u)))==wanted:found.append(z)
        assert len(found)==1;return found[0]
    for _ in range(900):
        x,y,z=(rng.choice(dom) for _ in range(3))
        assert solve(x,y)==physical(x,y)
        assert solve(x,solve(y,solve(x,z)))==solve(solve(x,solve(y,x)),z)
        q=solve(x,solve(solve(y,y),x))
        assert tuple(a*pow(2,-1,r)%r for a in q)==add(x,y)
        # inverse left translations are L_-x; compose the literal four mark actions.
        h=solve(neg(x),solve(neg(y),solve(x,solve(y,zero))))
        assert h==add(B(x,y),B(x,y))
    if alltr:
        ix={x:i for i,x in enumerate(dom)};X=list(range(len(dom)))
        T=[[ix[solve(x,y)] for y in dom] for x in dom];assert all(len(set(col))==len(dom) for col in zip(*T))
        ids=Counter();L=set(X);R=set(X);M=set(X);comm=set(X)
        for x,y,z in product(X,repeat=3):
            assert T[T[x][T[y][x]]][z]==T[x][T[y][T[x][z]]]
            if T[T[x][y]][z]!=T[x][T[y][z]]:L.discard(x);M.discard(y);R.discard(z)
            if T[x][y]!=T[y][x]:comm.discard(x)
        assert (len(L),len(M),len(R),len(comm))==(1,1,r*r,1)
        print('literal prime table',r,len(dom),'Bol triples',len(dom)**3,'nuclei/comm',list(map(len,(L,M,R,comm))))
    print('actual central-coset unique decodes/commutator/Bruck/Bol at size',len(dom),':',900)
def elliptic(p):
    # Use Cayley-Hamilton: enumerate characteristic polynomials, then their scalar and
    # all fractional-linear isotope transports. Check one actual native product on each.
    ir={(t,d)for t in range(p) for d in range(1,p) if all((x*x-t*x+d)%p for x in range(p))}
    def scalar(td,s):return (td[0]*s%p,td[1]*s*s%p)
    def reciprocal_shift(td,b):
        # If u^-1 is shifted by b, u becomes u/(1+bu), no zero in this field orbit.
        t,d=td;e=pow((1+b*t+b*b*d)%p,-1,p)
        return ((t+2*b*d)*e%p,d*e%p)
    scalarorbs={min(scalar(x,s) for s in range(1,p)) for x in ir}
    allorb={min(scalar(reciprocal_shift(x,b),s)for s in range(1,p) for b in range(p)) for x in ir}
    assert len(scalarorbs)==(p+1)//2 and len(allorb)==1
    print('prime elliptic characteristic polynomials/ordinary/full isotope',p,len(ir),len(scalarorbs),len(allorb))
if __name__=='__main__':
    square_modules(3,True);square_modules(9);square_modules(7)
    for p in (3,5,7,11,13,17,19,23,29,31):elliptic(p)
