"""Independent finite mechanism controls. These are not Bol loops or a classification search."""
from itertools import permutations, combinations,product
from collections import deque

def mul(p,q): return tuple(p[i] for i in q)
def inv(p): return tuple(p.index(i) for i in range(len(p)))
def conj(p,q): return mul(p,mul(q,inv(p)))
def even(p): return sum(p[i]>p[j] for i,j in combinations(range(len(p)),2))%2==0
def sqone(p): return all(p[p[i]]==i for i in range(len(p)))
def perm(n,*cycles):
    a=list(range(n))
    for c in cycles:
        for i,j in zip(c,c[1:]+c[:1]):a[i]=j
    return tuple(a)
def component():
    # R=A5 point stabilizer, inside T=A6. The first mark arrow moves the omitted
    # letter, so the literal common R^4 is NOT normalized by the mark.
    T=[p for p in permutations(range(6)) if even(p)]
    R=[p for p in T if p[5]==5];I=tuple(range(6))
    U=[p for p in R if p!=I and sqone(p)];assert len(U)==15
    aa=(perm(6,(0,5)),perm(6,(2,5,4)))
    spin=perm(6,(0,1));rho=perm(6,(2,3,4));edges=[(0,1),(2,3)]
    assert any(conj(aa[0],u)[5]!=5 for u in U)
    def pack(p,sw):
        return tuple(6*sw[i]+p[i][j] for i in range(4) for j in range(6))
    allid=(0,1,2,3);sigma=(1,0,3,2)
    mark=pack([aa[0],inv(aa[0]),aa[1],inv(aa[1])],sigma)
    # Actual two strips {0,2} and {1,3}, with different twists.
    tests=out=0
    for u,v in product(U,repeat=2):
        w=(u,v,conj(spin,u),conj(rho,v));q=[I]*4;q2=[I]*4
        for (i,j),a in zip(edges,aa):
            r=next(r for r in T if conj(mul(r,a),inv(w[i]))==w[j])
            q[j]=r
            q2[j]=mul(r,conj(a,w[i]));assert even(q2[j]);out+=r[5]!=5
        first=conj(pack(q,allid),mark);second=conj(pack(q2,allid),mark)
        assert first!=second and sqone(first) and sqone(second) and mul(first,second)==pack(w,allid)
        tests+=1
    # Real, but not Aut-invariant: alternating 5-cycles across an odd arrow.
    U5=[p for p in permutations(range(5)) if even(p)];x=perm(5,(0,1,2,3,4))
    odd=perm(5,(0,1));cl={conj(a,x) for a in U5}
    assert inv(x) in cl and conj(odd,x) not in cl and not any(conj(mul(a,odd),inv(x))==x for a in U5)
    # Without C_U(R)=1 the ->one strip-> actual order identity can fail.
    c2=perm(9,(5,6),(7,8));unit=perm(9)
    u0=[p+tuple(range(5,9)) for p in U5]
    G={tuple(mul(r,c2 if b else unit) for b in bs) for r in u0 for bs in product((0,1),repeat=3)}
    assert all(all(even(v) for v in g) for g in G)
    loc={g[0] for g in G};W={tuple([r]*3) for r in u0};assert len(G)==480 and len(loc)==120 and len(W)==60
    assert sum(g[0]==unit for g in G)==4
    print(f'{tests} physical 24-point products of two separate (A6)^4 conjugates of one involution realize two independently twisted A5 strips; {out} returned inner adjustments move the omitted site. An odd A5 arrow breaks the same test on a merely real class. A9 with local A5×C2: true diagonal perfect residual order 60, full stabilizer 480, local projection 120.')
def sharpA6():
    # PΓL₂(9) on the 10 points of the actual projective line; GF(9)=F3[i], i²=-1.
    F=range(9);add=lambda x,y:(x%3+y%3)%3+3*((x//3+y//3)%3)
    m=lambda x,y:(x%3*(y%3)-x//3*(y//3))%3+3*((x%3*(y//3)+x//3*(y%3))%3)
    neg=lambda a:(-a%3)+3*(-(a//3)%3)
    mi={a:next(y for y in F if m(a,y)==1) for a in F if a}
    MS={(a,b,c,d) for a,b,c,d in product(F,repeat=4) if add(m(a,d),neg(m(b,c))) and next(i for i in (a,b,c,d) if i)==1}
    assert len(MS)==720
    group=set()
    for a,b,c,d in MS:
        P=[]
        for x in range(10):
            top,bot=(a,c) if x==9 else (add(m(a,x),b),add(m(c,x),d))
            P.append(m(top,mi[bot]) if bot else 9)
        group.add(tuple(P));group.add(tuple(P[m(x,m(x,x))] if x<9 else P[9] for x in range(10)))
    assert len(group)==1440
    I=sum(sqone(g) for g in group);upper=3*I*len(group);needed=6*360**2
    assert I<180 and upper<needed and 3*180*len(group)==needed
    print(f'Aut(A6)=PΓL₂(9): all {len(group)} actual degree-10 permutations, {I} square-one including identity; three rank-three signed permutation images admit at most {upper} actions, but {needed} needed. Replacing I<180 by I≤180 loses strictness exactly.')
def orth():
    # All q=2 orthogonal root maps via their actual moved singular planes, not just formal roots.
    Q=lambda z:((z&15)&(z>>4)).bit_count()&1
    B=lambda x,y:Q(x)^Q(y)^Q(x^y)
    plane=lambda x,y:tuple(sorted((x,y,x^y)))
    singular=[z for z in range(1,256) if not Q(z)]
    roots={plane(x,y) for x,y in combinations(singular,2) if not B(x,y)}
    assert len(roots)==1575
    v=136 # e4 + f4; nonsingular
    assert Q(v) and sum(not B(v,z) for z in range(256))==128
    per=[p for p in roots if all(not B(w,v) for w in p)]
    assert len(per)==315
    six=lambda x: (x&7)|((x>>1)&56)  # delete e4 and f4
    B6=lambda x,y:(((x&7)&(y>>3)).bit_count()+((x>>3)&(y&7)).bit_count())&1
    U=list(range(64))
    im={}
    for p in per:
        a,b=p[:2]; maps={};image=set()
        for z in range(256):
            if B(v,z):continue
            delta=(b if B(z,a) else 0)^(a if B(z,b) else 0);w=z^delta
            assert Q(z)==Q(w) and not B(w,v)
            y=six(z)
            if y in maps:assert maps[y]==six(w)
            maps[y]=six(w);image.add(six(delta));assert not B6(y,six(delta))
        assert set(maps)==set(U) and len(image)==4
        key=tuple(sorted(image-{0}));assert key==tuple(sorted(six(t) for t in p)) and key not in im
        im[key]=tuple(maps[z] for z in U)
    planes={plane(x,y) for x,y in combinations(U[1:],2) if not B6(x,y)}
    assert set(im)==planes
    Ts={tuple(z^(a if B6(z,a) else 0) for z in U) for a in U[1:]}
    orbit={next(iter(im.values()))};q=deque(orbit)
    while q:
        g=q.popleft()
        for t in Ts:
            h=mul(t,mul(g,t))
            if h not in orbit:orbit.add(h);q.append(h)
    assert orbit==set(im.values()) and len(Ts)==63 and not orbit&Ts
    print('PΩ₈⁺(2): 1575 distinct actual singular two-plane root maps. Exactly 315 fix the selected nonsingular vector and act on the 6-space quotient in one 315-element Sp₆(2) conjugacy orbit, all rank two. None is one of its 63 genuine symplectic transvections.')
component();sharpA6();orth()
