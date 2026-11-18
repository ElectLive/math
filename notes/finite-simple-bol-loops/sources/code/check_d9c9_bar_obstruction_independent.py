#!/usr/bin/env python3
"""Binary bar equations, necessary mixed-commutation splitter test and all stabilizer cocycles."""
from itertools import product

def act(g,x):
    v=0
    for i,z in enumerate(g):
        if x>>i&1:v^=z
    return v

def compose(g,h):return tuple(act(g,x) for x in h)
I=(1,2,4)
T=sorted(g for g in product(range(1,8),repeat=3) if len({act(g,x) for x in range(8)})==8)
P=[g for g in T if g[0]==1 and g[1]>>1==1 and g[2]>>2==1]
assert len(T)==168 and len(P)==8
ti={x:i for i,x in enumerate(T)};pi={x:i for i,x in enumerate(P)}
tg=[(2,4,1),(1,3,4)]; pg=[(1,3,4),(1,2,6)];b=pg[1]
def gen(G):
    seen={I};q=[I]
    for a in q:
        for s in G:
            z=compose(a,s)
            if z not in seen:seen.add(z);q.append(z)
    return seen
assert gen(tg)==set(T) and gen(pg)==set(P)

class System:
    def __init__(self):self.B={}
    def add(self,z):
        while z:
            j=z.bit_length()-1
            if j not in self.B:self.B[j]=z;return
            z^=self.B[j]
    def kernel(self,n):
        F=set(range(n))-set(self.B)
        basis=[]
        for h in F:
            z=1<<h
            for j in sorted(self.B):
                if (z&self.B[j]).bit_count()%2:z^=1<<j
            basis.append(z)
        return basis

def col_masks(f,D):
    return [sum(1<<i for i in range(D) if f(1<<i)>>j&1) for j in range(D)]

def internal(sys,G,idx,gs,offset,D,op):
    for g in G:
        rows=col_masks(lambda v:op(g,v),D)
        for s in gs:
            gg=idx[compose(g,s)]
            for i,r in enumerate(rows):
                sys.add((1<<(offset+D*gg+i))^(1<<(offset+D*idx[g]+i))^(r<<(offset+D*idx[s])))

def derivations():
    S=System();internal(S,T,ti,tg,0,3,act)
    basis=S.kernel(3*len(T)); assert len(basis)==4
    vals={0}
    for z in basis:vals |= {x^z for x in vals}
    prin={sum((a^act(g,a))<<(3*i) for i,g in enumerate(T)) for a in range(8)}
    assert len(prin)==8 and prin<=vals
    non=min(vals-prin)
    return {g:(non>>(3*i))&7 for i,g in enumerate(T)}

def work(coc,K):
    m=3-K;D=3*m;off=len(T)*D
    # tensor word uses one m-bit row for each first-module coordinate.
    def tens(x,y):
        return sum(y<<(m*i) for i in range(3) if (x>>i)&1)
    def left(g,z):
        w=0
        for i in range(3):w^=tens(g[i],(z>>(m*i))&((1<<m)-1))
        return w
    def right(g,z):
        return sum((act(g,((z>>(m*i))&((1<<m)-1))<<K)>>K)<<(m*i) for i in range(3))
    # Unknown lifts at each individual element of the two factors.
    # Necessary if the external-product class split: EVERY commuting cross pair
    # would obey (1+p)u_a+(1+a)v_p=delta(a) tensor bar(delta(p)).
    # No internal factor cocycle equations are assumed to prove inconsistency.
    fail=System();hom=System()
    internal(hom,T,ti,tg,0,D,left);internal(hom,P,pi,pg,off,D,right)
    RC={p:col_masks(lambda z:z^right(p,z),D) for p in P}
    LC={a:col_masks(lambda z:z^left(a,z),D) for a in T}
    for a in T:
        for p in P:
            rhs=tens(coc[a],coc[p]>>K)
            for i in range(D):
                core=(RC[p][i]<<(D*ti[a]))^(LC[a][i]<<(off+D*pi[p]))
                hom.add(core)
                fail.add((core<<1)^((rhs>>i)&1))
    assert fail.B.get(0)==1 # impossible 0=1 after elimination
    dimension=D*(len(T)+len(P))-len(hom.B);assert dimension==D+1
    # Evaluate all actual restricted-stabilizer cocycles, not just principal-adjusted representatives.
    basis=hom.kernel(D*(len(T)+len(P)));forms={0}
    for t in basis:forms|={z^t for z in forms}
    # To form the actual marked-square fiber over (b,b), multiply at every
    # projected pair x,y with x*y=b and x^{-1}*y^{-1}=b. Work first in V, then project.
    def outer(x,y):return sum(y<<(3*i) for i in range(3) if x>>i&1)
    def L(a,z):
        ans=0
        for i in range(3):ans^=outer(a[i],(z>>(3*i))&7)
        return ans
    def R(p,z):return sum(act(p,(z>>(3*i))&7)<<(3*i) for i in range(3))
    def proj(z):return sum((((z>>(3*i))&7)>>K)<<(m*i) for i in range(3))
    inv={g:next(z for z in T if compose(g,z)==I) for g in T}
    def tr(z):return sum(((z>>(3*i+j))&1)<<(3*j+i) for i,j in product(range(3),repeat=2))
    sheet=[z for z in range(512) if tr(z)==z and (not K or not(z&273))]
    products=set()
    for x in T:
        y=compose(inv[x],b)
        if compose(inv[x],inv[y])!=b:continue
        S=[L(x,z) for z in sheet];Q=[R(inv[x],L(b,z)) for z in sheet]
        products|={proj(i^j) for i in S for j in Q}
    assert forms
    entries=set()
    for z in forms:
        A=(z>>(D*ti[b]))&((1<<D)-1);B=(z>>(off+D*pi[b]))&((1<<D)-1)
        v=A^left(b,B);assert v in products;entries.add(v)
    return (m,dimension,len(forms),len(entries),len(products))

if __name__=='__main__':
    c=derivations();print('global natural Z1 dimension 4; independent nonprincipal input, T/P:',len(T),len(P))
    for k in (0,1):print('quotient dimension, actual Z1 dimension, ALL stabilizer cocycles, attained (b,b) vectors, marked-square phases; degree-two mixed obstruction inconsistent:',work(c,k))
