"""Use concrete affine flats, not the manuscript checker or its cocycle/section parametrization."""
from itertools import product
class Field:
    def __init__(s,l,d):
        s.l=l;s.d=d;s.q=l**d
        s.ns=next(i for i in range(2,l) if pow(i,(l-1)//2,l)==l-1)
        s.add=[[s.pack(i%l+j%l,i//l+j//l) for j in range(s.q)] for i in range(s.q)]
        s.neg=[s.pack(-(i%l),-(i//l)) for i in range(s.q)]
        s.mul=[[s.pack((i%l)*(j%l)+s.ns*(i//l)*(j//l),(i%l)*(j//l)+(j%l)*(i//l)) for j in range(s.q)] for i in range(s.q)]
    def pack(s,a,b): return a%s.l+(s.l*(b%s.l) if s.d==2 else 0)
    def pow(s,a,k):
        ans=1
        for _ in range(k):ans=s.mul[ans][a]
        return ans

def test(p,l,d):
    F=Field(l,d);q=F.q;r=(p-1)//2
    z=next(c for c in range(2,q) if F.pow(c,p)==1)
    Z=[F.pow(z,i) for i in range(p)]
    add=lambda a,b: tuple(F.add[x][y] for x,y in zip(a,b))
    neg=lambda a: tuple(F.neg[x] for x in a)
    sub=lambda a,b: add(a,neg(b))
    zero=(0,)*p
    def act(a,b,c,u):
        return tuple(F.mul[Z[(c+b*(j-a))%p]][u[(j-a)%p]] for j in range(p))
    def rinv(a,b,u):
        return tuple(F.mul[Z[(-j*b)%p]][u[(j+a)%p]] for j in range(p))
    def fixed(u):return all(u[i]==u[-i%p] for i in range(p))
    def gauge(a,b,u): # translates of X^aY^b Fix(J), perfect geometric quotient
        t=rinv(a,b,u)
        return (a,b,tuple(F.add[t[i]][F.neg[t[-i]]] for i in range(1,r+1)))
    def stable(c):
        u=[0]*p
        for i,x in enumerate(c):u[i]=u[-i%p]=x
        return tuple(u)
    def vneg(i,x=1):
        u=[0]*p;u[i]=x;u[-i]=F.neg[x];return tuple(u)
    V=vneg(1,z)
    directions=[]
    # Each direction is different without relying on the direction labels in gauge.
    Jbasis=[stable([int(i==j) for j in range(r+1)]) for i in range(r+1)]
    U=list(product(range(p),repeat=2))
    for a,b in U:
        if (a,b)!=(0,0): assert any(not fixed(act(a,b,0,u)) for u in Jbasis)
    W=[stable(c) for c in product(range(q),repeat=r+1)]
    assert sum(fixed(act(1,0,0,w)) and fixed(act(0,1,0,w)) for w in W)==1
    # Check all stable complement centers at q=7; otherwise exhaustive vector test
    # above, uniformly spaced complement centers below.
    chosen=W if (p,q)==(3,7) else list(dict.fromkeys([W[0],W[-1],*W[::max(1,len(W)//31)]]))
    pos=set()
    for w in chosen:
        orbits=[set(),set()]
        for a,b,c in product(range(p),repeat=3):
            t=sub(w,act(a,b,c,w))
            for o,v in zip(orbits,(zero,V)):
                o.add(gauge(a,b,add(t,act(a,b,c,v))))
        assert len(orbits[0])==p*p and len(orbits[1])==p**3
        pos.add(frozenset(orbits[0]))
    assert len(pos)==len(chosen)
    norms=0
    iv=(p+1)//2
    for a,b in U:
        if (a,b)==(0,0):continue
        c=a*b*iv%p
        for j in range(1,r+1):
            # vector part in S_(x/2) A^-; compare actual affine power explicitly.
            x,y=a*iv%p,b*iv%p
            v=act(x,y,x*y*iv%p,vneg(j))
            accum=zero
            for _ in range(p):
                accum=add(v,act(a,b,c,accum))
            assert accum==zero
            norms+=1
    if (p,l,d)==(3,7,2):
        assert z<7                         # all B matrices prime-subfield valued
        subfield=[tuple(w) for w in product(range(7),repeat=p)]
        assert all(all(x<7 for x in act(1,1,1,w)) for w in subfield)
        assert F.mul[7][1]>=7               # genuinely not F49-linear
    print('p, char, field=',(p,l,q),'exhaustive W-plus',len(W),'X/Y simultaneous plus survivors=1;',
          'distinct positive orbits',len(pos),'native orbit for each',p**3,'signed powers',norms)
for triple in [(3,7,1),(3,5,2),(3,7,2),(5,11,1),(7,29,1)]:
    test(*triple)
print('PASS: positive and tilted native are different actual affine-flat orbits; F49 additive-only control')
