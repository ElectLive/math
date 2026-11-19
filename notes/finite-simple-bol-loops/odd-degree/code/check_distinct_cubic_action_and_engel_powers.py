"""Fresh controls using ordinary polynomials acting on a plane, and a separate
class-three BCH group with genuine additive p-carries. No author imports."""
from itertools import product,combinations
from collections import Counter
from functools import lru_cache
from math import comb
from random import Random
R=Random(902)
def rref_planes(p):
    for i,j in combinations(range(4),2):
        free=[(r,k) for r,l in enumerate((i,j)) for k in range(l+1,4) if k not in (i,j)]
        for coords in product(range(p),repeat=len(free)):
            X=[[int(i==k) for k in range(4)],[int(j==k) for k in range(4)]]
            for v,(r,k) in zip(coords,free):X[r][k]=v
            yield tuple(map(tuple,X))
def p4(p):
    F=list(product(range(p),repeat=4));ev={c:tuple(sum(z*t**i for i,z in enumerate(c))%p for t in range(p)) for c in F}
    co={x:c for c,x in ev.items()}
    def acted(x,shift):return x[shift:]+x[:shift]
    def plus(x,y):return tuple((a+b)%p for a,b in zip(x,y))
    allK=[];odd={}
    for s in range(p):
        allK.extend((s,f) for f in co if all((f[(-t)%p]+f[(t-s)%p])%p==0 for t in range(p)))
    for sx,fx in allK:
        for sy,fy in allK:
            odd.setdefault((sx+sy)%p,set()).add(plus(fy,acted(fx,sy)))
    assert len(allK)==p**3 and all(len(odd[t])==p**4 for t in range(1,p))
    below=set(co[f] for f in odd[0]);zero=(0,0,0,0)
    def span(v,w):return {tuple((i*a+j*b)%p for a,b in zip(v,w)) for i in range(p) for j in range(p)}
    good=set();wcase=bad=0
    def canonical(P):
        # display actual plane by its unique monic cubic with zero quadratic
        # and unique monic quadratic for which cubic coefficient is zero
        a,=[x for x in P if x[3:]==(1,) and not x[2]]
        b,=[x for x in P if not x[3] and x[2]==1]
        return a,b
    for v,w in rref_planes(p):
        P=span(v,w);allow=P&below=={zero}
        if not allow:bad+=1;continue
        if (1,0,0,0) in P:wcase+=1;continue
        M,Q=canonical(P)
        assert all((sum(a*(-u*pow(3,-1,p))**i for i,a in enumerate(M))+u*sum(a*(-u*pow(3,-1,p))**i for i,a in enumerate(Q)))%p !=0 for u in range(p))
        good.add((M,Q))
    assert wcase==p and len(good)==p*(p**3-p)//3
    def change(f,s,h,c):
        g=tuple(sum(f[k]*comb(k,i)*s**i*h**(k-i) for k in range(i,4))%p for i in range(4))
        return tuple((a+(c*(i+1)*(i+2)*g[i+2] if i<2 else 0))%p for i,a in enumerate(g))
    def normalize(X,Y):
        u=pow(Y[2],-1,p);Y=tuple(u*v%p for v in Y)
        c=X[2];v=pow(X[3],-1,p);X=tuple(v*(a-c*b)%p for a,b in zip(X,Y))
        return X,Y
    def orb(h,trans):
        X,Y=h;o={normalize(change(X,s,b,c),change(Y,s,b,c)) for s in range(1,p) for b in (range(p) if trans else (0,)) for c in range(p)}
        assert o<=good;return o
    def partition(trans):
        left=set(good);O=[]
        while left:
            x=min(left);o=orb(x,trans);O.append(o);left-=o
        return O
    iso,atp=partition(False),partition(True)
    assert len(iso)==(p*(p+1)+(4 if p%3==1 else 0))//3
    assert len(atp)==(p+1+(4 if p%3==1 else 0))//3
    evaluated=0;bol=0
    for O in iso:
        M,Q=min(O)
        def rem(f):return tuple((f[i]-f[3]*M[i]-f[2]*Q[i])%p for i in (0,1))
        dom=list(product(range(p),repeat=3));maps={(s,*rem(co[f])):f for s,f in allK}
        assert len(maps)==len(dom);ix={x:i for i,x in enumerate(dom)}
        def native(x,y):
            s=x[0];t,u,v=y;z=co[acted(maps[x],t)];a,b=rem(z)
            return ((s+t)%p,(a+u)%p,(b+v)%p)
        if p==5 or O is iso[0]:
            T=[[ix[native(x,y)] for y in dom] for x in dom];zeroix=ix[(0,0,0)]
            assert all(len(set(x))==len(dom) for x in zip(*T))
            selected=dom if (p==5 and O is iso[0]) else [R.choice(dom) for _ in range(3)]
            for X in selected:
                x=ix[X]
                for y in range(len(dom)):
                    u=T[x][T[y][x]];r1=T[u];rx=T[x];ry=T[y]
                    assert all(r1[z]==rx[ry[rx[z]]] for z in range(len(dom)));bol+=len(dom)
            evaluated+=1
    fibers=Counter(sum(O<=(A) for O in iso) for A in atp)
    print('cubic p, true squares, actual planes rejected, central-kernel, faithful, scalar sectors, affine sectors, native table samples, native Bol triples:',
          p,sum(map(len,odd.values())),bad,wcase,len(good),len(iso),len(atp),evaluated,bol)
    print('actual point isotypes per full isotope sector:',sorted(fibers.items()))
def c3(p):
    for A,B in ((0,0),(1,0),(0,1),(0,next(i for i in range(1,p) if pow(i,(p-1)//2,p)>1))):
        E=list(product(range(p),repeat=4));z=(0,0,0,0)
        def red(a,b,d,c):
            x,a=divmod(a,p);y,b=divmod(b,p)
            return a,b,d%p,(c+A*x+B*y)%p
        def mul(x,y):
            a,b,d,c=x;u,v,vv,ww=y;bd=(a*v-b*u)%p;bc=(a*vv-d*u)%p
            return red(a+u,b+v,d+vv+bd*pow(2,-1,p),c+ww+bc*pow(2,-1,p)+(a-u)*bd*pow(12,-1,p))
        def inv(x):return red(*(-a for a in x))
        def sign(x):a,b,d,c=x;return red(-a,-b,d,-c)
        K=[x for x in E if inv(x)==sign(x)];sq={mul(x,y) for x in K for y in K}
        assert len(K)==p**3
        lines=set()
        for x in E[1:]:
            g=z;H=set()
            for j in range(p):H.add(g);g=mul(g,x)
            if g==z and H&sq=={z}:lines.add(frozenset(H))
        allowed={frozenset((0,0,d,(s*d)%p) for d in range(p)) for s in range(p)}
        assert lines==allowed
        for _ in range(3000):
            x,y,t=(R.choice(E) for i in range(3));assert mul(x,mul(y,t))==mul(mul(x,y),t)
        print('Engel BCH p,pa,pb, actual squared elements, complete sharp lines:',p,A,B,len(sq),len(lines))
if __name__=='__main__':
    for p in (5,7):p4(p);c3(p)
