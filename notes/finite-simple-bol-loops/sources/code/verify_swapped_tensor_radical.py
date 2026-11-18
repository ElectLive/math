"""Original radical-fiber, transposed orbit and projective proper-factor controls (stdlib)."""
from itertools import product,permutations
from math import gcd
def mm(a,b,n,p):return tuple(sum(a[n*i+k]*b[n*k+j] for k in range(n))%p for i in range(n) for j in range(n))
def matrix_orbits():
    p=3;n=3;els=list(product(range(p),repeat=9)); I=(1,0,0,0,1,0,0,0,1)
    def rank(a):
        row=[list(a[3*i:3*i+3]) for i in range(3)];r=0
        for j in range(3):
            z=next((i for i in range(r,3) if row[i][j]),None)
            if z is None:continue
            row[z],row[r]=row[r],row[z]; iv=pow(row[r][j],-1,3)
            row[r]=[x*iv%3 for x in row[r]]
            for i in range(r+1,3):
                d=row[i][j];row[i]=[(x-d*y)%3 for x,y in zip(row[i],row[r])]
            r+=1
        return r
    ranks={a:rank(a) for a in els}
    rt=lambda a:tuple(a[j*3+i] for i in range(3) for j in range(3))
    def closure(initial):
        seen=set(initial);ls=list(seen)
        for a in ls:
            for i,j in permutations(range(3),2):
                for left in (0,1):
                    b=list(a)
                    for k in range(3):
                        u,v=(3*i+k,3*j+k) if left else (3*k+i,3*k+j)
                        b[u]=(a[u]+a[v])%3
                    b=tuple(b)
                    if b not in seen:seen.add(b);ls.append(b)
        return seen
    sym={a for a in els if rt(a)==a};skew={a for a in els if all((x+y)%3==0 for x,y in zip(a,rt(a)))}
    assert len(sym)==729 and len(skew)==27
    assert closure(sym)==set(els); ck=closure(skew)
    assert ck=={a for a in els if ranks[a] in (0,2)}
    # All 28 full-left submodules via row spaces, actual collision ranks.
    lv=list(product(range(3),repeat=3));zero=(0,0,0)
    lines={frozenset((zero,v,tuple(2*x%3 for x in v))) for v in lv if v!=zero}
    planes={frozenset(w for w in lv if sum(x*y for x,y in zip(v,w))%3==0) for v in lv if v!=zero}
    ds=[]
    for rows in [frozenset([zero]),*lines,*planes,frozenset(lv)]:
        sub=[a for a in els if all(a[i:i+3] in rows for i in (0,3,6))]
        if not any(ranks[a]==2 for a in sub):ds.append(len(sub))
    assert sorted(ds)==[1]+[27]*13
    return len(els),len(sym),len(skew),len(ck),len(ds)

def cocycles():
    # For SL3(3) normalized on the determinant-one sign torus, the restriction
    # to each x_ij has only a third-coordinate coefficient. Test all 3^6 tuples
    # against actual affine products in the two required elementary relations.
    pairs=list(permutations(range(3),2));z=(0,0,0);I=(1,0,0,0,1,0,0,0,1)
    gen={ij:tuple((1 if a==b or (a,b)==ij else 0) for a,b in product(range(3),repeat=2)) for ij in pairs}
    def aff(g,h):
        a,u=g;b,v=h;return mm(a,b,3,3),tuple((u[i]+sum(a[i*3+j]*v[j] for j in range(3)))%3 for i in range(3))
    good=[]
    for c in product(range(3),repeat=6):
        el={ij:(gen[ij],tuple(k*((v not in ij)) for v in range(3))) for ij,k in zip(pairs,c)}
        ok=True
        for i,j,k in permutations(range(3)):
            a,b,d=el[i,j],el[j,k],el[i,k]
            if aff(a,d)!=aff(d,a) or aff(a,b)!=aff(aff(b,a),d):ok=False;break
        if ok:good.append(c)
    assert good==[(0,)*6]
    for n,q in ((3,5),(3,11),(5,3),(5,7)):
        diag=[v for v in product(range(1,q),repeat=n) if __import__('math').prod(v)%q==1 and v[0]==v[1]]
        assert all(any(x[i]!=1 for x in diag) for i in range(n))
    return len(good)

def factor(q):
    p=2;v=q;out=[]
    while p*p<=v:
        if v%p==0:out.append(p)
        while v%p==0:v//=p
        p+=1
    if v>1:out.append(v)
    return out
def projective():
    qs=(3,5,9,11,17,23,27,81,125,243,729,1331);sh=[]
    for q in qs:
        p=factor(q)[0];v=q;f=0
        while v%p==0:f+=1;v//=p
        assert v==1 and gcd(q-1,3)==1
        T=lambda x:x**3*(x**3-1)*(x*x-1)//gcd(3,x-1)
        U=lambda x:x**3*(x**3+1)*(x*x-1)//gcd(3,x+1)
        t=T(q);pp=q**3*(q-1)**2*(q+1);sn=3*(q*q+q+1)
        orders={pp,sn,6*(q-1)**2,q*(q*q-1),360,216,72,36,168}
        for b in factor(f):orders.add(T(p**(f//b))*gcd(gcd(q-1,3),b))
        if f%2==0:orders.add(U(p**(f//2)))
        actual=[u for u in orders if t%u==0]
        vals=[(a,b) for a,b in product(actual,repeat=2) if a*b%(p*t)==0]
        if p!=3:assert not vals
        else:assert all(sn in (a,b) and max(a,b)<=pp and a*b//t<=3 for a,b in vals)
        sh.append((q,len(vals)))
    return sh
if __name__=="__main__":
    print("SL3(3) tensor: matrices, symmetric/skew, skew orbit union, avoiding full-left modules:",matrix_orbits())
    print("Residual normalized SL3(3) natural derivations of 729:",cocycles())
    print("Proper overfactor order bounds in 12 odd fields:",projective())
