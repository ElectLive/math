"""Direct small-group controls for quotient-only normal, generation and cut filters.

Build subgroups by multiplication independently of lower cochain tests. Fixtures
are controls, not claims of a simple Bol example. Standard library only.
"""
from itertools import product

def order(g,tab):
    a=0
    for n in range(1,len(tab)+1):
        a=tab[a][g]
        if a==0:return n
    assert False
def subgroups(tab):
    """Full lattice via adjoining an element with no assumed subgroup types."""
    n=len(tab); done={frozenset([0])}; stack=list(done)
    while stack:
        h=stack.pop()
        for a in range(n):
            if a in h:continue
            gen=tuple(h)+(a,); k={0}; todo=[0]
            while todo:
                b=todo.pop()
                for x in gen:
                    z=tab[b][x]
                    if z not in k:k.add(z);todo.append(z)
            k=frozenset(k)
            if k not in done:done.add(k);stack.append(k)
    return sorted(done,key=lambda h:(len(h),sorted(h)))
def test(p,r,Y,ym,vm,theta,sigma,tag):
    # Each group model exposes an explicit (v,y) multiplication; get lower
    # action and cocycle using the section; theta on actual G is independent.
    V=list(range(p**r)); Y=list(Y); nv=len(V); ny=len(Y)
    va=lambda v,w:sum(((v//p**i+w//p**i)%p)*p**i for i in range(r))
    vn=lambda v:sum((-(v//p**i)%p)*p**i for i in range(r))
    sub=lambda v,w:va(v,vn(w))
    enc=lambda v,y:y*nv+v
    n=ny*nv; elems=range(n); G=frozenset(elems)
    tab=[[enc(vm(i%nv,i//nv,j%nv,j//nv),ym(i//nv,j//nv)) for j in elems] for i in elems]
    assert all(tab[tab[i][j]][k]==tab[i][tab[j][k]] for i,j,k in product(elems,repeat=3))
    inv=[next(j for j in elems if tab[i][j]==0) for i in elems]
    th=[enc(*theta(i%nv,i//nv)) for i in elems]
    assert all(th[th[i]]==i and th[tab[i][j]]==tab[th[i]][th[j]] for i,j in product(elems,repeat=2))
    ytab=[[ym(i,j) for j in Y] for i in Y]; yinv=[next(j for j in Y if ym(i,j)==0) for i in Y]
    lat=subgroups(tab); ylat=subgroups(ytab); vlat=subgroups([[va(i,j) for j in V] for i in V])
    is_norm=lambda h,T:all({T[i][x] for x in h}=={T[x][i] for x in h} for i in range(len(T)))
    norms={h for h in lat if is_norm(h,tab)}; ynorm=[d for d in ylat if is_norm(d,ytab)]
    f=lambda i,j:vm(0,i,0,j)
    act=lambda y,v:vm(0,y,v,0)
    cuts={}; found=set();surjs=set()
    for U in vlat:
        if any(act(y,u) not in U for u in U for y in Y):continue
        rep={v:min(va(v,u) for u in U) for v in V}; cos=sorted(set(rep.values()))
        def section_list(D,central):
            ds=sorted(set(D)-{0})
            for vals in product(cos,repeat=len(ds)):
                eta=dict(zip(ds,vals));eta[0]=0
                if any(rep[eta[ym(d,e)]]!=rep[va(va(eta[d],act(d,eta[e])),f(d,e))] for d,e in product(D,repeat=2)):continue
                if central and any(rep[eta[z]]!=rep[va(act(y,eta[d]),sub(f(y,d),f(z,y)))]
                    for y,d in product(Y,D) for z in (ym(ym(y,d),yinv[y]),)):continue
                yield eta
        for D in ynorm:
            if any(sub(act(d,v),v) not in U for d,v in product(D,V)):continue
            for eta in section_list(D,True):
                N=frozenset(enc(v,d) for d in D for v in V if rep[v]==eta[d])
                found.add(N);cuts[N]=(U,D,eta)
        if len(U)<nv:
            for gamma in section_list(Y,False):
                yield_key=frozenset(enc(v,y) for y in Y for v in V if rep[v]==gamma[y])
                # All subgroups surjective on Y, not just normals.
                surjs.add(yield_key)
    assert found==norms
    assert surjs=={h for h in lat if h!=G and {i//nv for i in h}==set(Y)}
    # Ghat = G semidirect <t>. Mark all, or just some, Ghat conjugacy classes.
    E=range(2*n); etab=[[tab[i%n][th[j%n] if i//n else j%n]+n*((i//n+j//n)%2) for j in E] for i in E]
    einv=[next(j for j in E if etab[i][j]==0) for i in E]
    allmarks={x for x in range(n,2*n) if etab[x][x]==0}
    classes=[];rem=set(allmarks)
    while rem:
        x=min(rem);cl={etab[etab[i][x]][einv[i]] for i in E};classes.append(cl);rem-=cl
    a0=next(cl for cl in classes if n in cl); rest=[c for c in classes if c!=a0]
    masks=[a0|set().union(*(c for b,c in zip(bits,rest) if b)) for bits in product((0,1),repeat=len(rest))][:48]
    assert all(n in M for M in masks)
    sz_tests=mass_tests=gen_tests=core_tests=bad_naive=0; yset=set(Y)
    for marks in masks:
        K={etab[n][x] for x in marks}; proK={k//nv for k in K}
        # Compare only projected data, lower saturation, direct generated group.
        ygen=not any(proK<=s<yset for s in ylat)
        recognizes=ygen and not any(K<=h for h in surjs)
        generated=not any(K<=h<G for h in lat);assert recognizes==generated;gen_tests+=1
        fibers={}
        for x in marks:fibers.setdefault((x%n)//nv,set()).add(x%nv)
        Dvec={a:{sub(v,act(a,sigma(v))) for v in V} for a in fibers}
        phases={}
        for a,S in fibers.items():
            A=[]; rem=set(S)
            while rem:
                v=min(rem);A.append(v); rem-={va(v,w) for w in Dvec[a]}
            assert set().union(*({va(v,w) for w in Dvec[a]} for v in A))==S
            phases[a]=A
        # Representatives of the product fibers; directions derived below solely
        # from the lower quotient action. Direct square used only as oracle.
        products={}
        for a,b in product(fibers,repeat=2):
            au=n+enc(0,a);bu=n+enc(0,b);z=etab[au][bu]//nv
            scale=lambda v:act(a,sigma(v))
            fab=etab[au][bu]%nv
            dirs={va(x,y) for x,y in product(Dvec[a],Dvec[b])}
            for i,j in product(phases[a],phases[b]):
                off=va(va(i,scale(j)),fab);products.setdefault(z,[]).append({va(off,x) for x in dirs})
        sq={etab[a][b] for a,b in product(marks,repeat=2)}
        assert {enc(v,z) for z,parts in products.items() for S in parts for v in S}==sq
        for H in lat:
            J={i//nv for i in H};W={i%nv for i in H if i<nv}
            s={j:min(i%nv for i in H if i//nv==j) for j in J}
            actual_core=all(not (N<=H) for N in norms if len(N)>1)
            co_core=all(not(U<=W and D<=J and all(sub(eta[d],s[d]) in W for d in D))
              for N,(U,D,eta) in cuts.items() if len(N)>1)
            assert actual_core==co_core;core_tests+=1
            mass=(len(K)*len(H)==n and (sq&H)=={0})
            if mass:mass_tests+=1
            for N,(U,D,eta) in cuts.items():
                if len(N) in (1,n):continue
                HN={tab[h][u] for h,u in product(H,N)}
                direct=bool(sq&(HN-N))
                ker={i%nv for i in HN if i<nv}
                wu={va(w,u) for w,u in product(W,U)}
                if ker!=wu:bad_naive+=1
                bycoords=False
                for j,d in product(J,D):
                    z=ym(j,d);hnoff=va(va(s[j],act(j,eta[d])),f(j,d))
                    for S in products.get(z,[]):
                        ints=[v for v in S if sub(v,hnoff) in wu]
                        if any(z not in D or sub(v,eta[z]) not in U for v in ints):bycoords=True;break
                    if bycoords:break
                assert bycoords==direct
                if mass:
                    kN={frozenset(tab[k][u] for u in N) for k in K}
                    assert (len(kN)*len(HN)>n)==direct
                sz_tests+=1
    # Canonical V against all true O_l(G), not just exponent/central counts.
    def pgroup(h,q):
        z=len(h)
        while z%q==0:z//=q
        return z==1
    primes=[q for q in range(2,n+1) if n%q==0 and all(q%j for j in range(2,int(q**.5)+1))]
    ol=lambda ns,q:max((h for h in ns if pgroup(h,q)),key=len)
    op=ol(norms,p);P=ol(ynorm,p)
    assert {enc(v,y) for y in P for v in V}==op
    actual_omega={a for a in op if (a==0 or order(a,tab)==p) and all(tab[a][b]==tab[b][a] for b in op)}
    central=all(act(y,v)==v for y,v in product(P,V))
    ban=False
    if central:
        for d in P:
            if not d or order(d,ytab)!=p or not all(ym(d,y)==ym(y,d) for y in P):continue
            if not all(f(d,y)==f(y,d) for y in P):continue
            vv=0;di=d
            for _ in range(1,p):vv=va(vv,f(di,d));di=ym(di,d)
            if vv==0:ban=True
    assert (set(V)==actual_omega)==(central and not ban)
    for l in primes:
        if l==p:continue
        assert {i//nv for i in ol(norms,l)}=={y for y in ol(ynorm,l) if all(act(y,v)==v for v in V)}
    print(tag, "normal",len(norms),"surjective proper",len(surjs),"mark masks",gen_tests,"core",core_tests,
          "cuts",sz_tests,"sharp folders",mass_tests,"extra vertical HN",bad_naive,"canonical omega",set(V)==actual_omega,"non-stable N",sum({th[i] for i in h}!=h for h in norms))
    return bad_naive
def main():
    add2=lambda i,j:(i+j)%2
    add3=lambda i,j:(i+j)%3
    yy=lambda i,j:(i%3+j%3)%3+3*((i//3+j//3)%3)
    neg=lambda i:(-i)%3
    ny=lambda i:neg(i%3)+3*neg(i//3)
    # Few Ghat marked classes: central C3 in both genuine nonsplit extensions.
    bad=test(3,1,range(9),yy,lambda v,i,w,j:(v+w+(i%3)*(j//3))%3,
             lambda v,i:(v,ny(i)),lambda v:v,"Heisenberg-27")
    # Inverting C9 x C3 needs the carry in the chosen C9 section.
    bad+=test(3,1,range(9),yy,lambda v,i,w,j:(v+w+(i%3+j%3)//3)%3,
              lambda v,i:((-v-(i%3!=0))%3,ny(i)),neg,"C9xC3")
    bad+=test(3,1,range(3),add3,lambda v,i,w,j:(v+w)%3,lambda v,i:(neg(v),neg(i)),neg,"C3xC3")
    sw=lambda v:((v&1)<<1)+(v>>1)
    bad+=test(2,2,range(2),add2,lambda v,i,w,j:v^(sw(w) if i else w),
              lambda v,i:(sw(v),i),sw,"D8 reducible binary")
    bad+=test(3,1,range(2),add2,lambda v,i,w,j:(v+((-w) if i else w))%3,
              lambda v,i:(-v%3,i),neg,"S3 effective")
    # S3 with an extra central order-two marked direction: lower action on V is trivial.
    sy=lambda i,j:(i%3+(-1 if i>=3 else 1)*(j%3))%3+3*((i//3+j//3)%2)
    bad+=test(2,1,range(6),sy,lambda v,i,w,j:v^w,lambda v,i:(v,i),lambda v:v,"S3xC2 ineffective")
    bad+=test(2,2,range(2),add2,lambda v,i,w,j:v^w,lambda v,i:(sw(v),i),sw,"C2^3 nonstable normals")
    bad+=test(3,1,range(2),add2,lambda v,i,w,j:(v+w)%3,lambda v,i:(neg(v),i),neg,"C6 smaller O2 survives")
    assert bad>0
if __name__=="__main__": main()
