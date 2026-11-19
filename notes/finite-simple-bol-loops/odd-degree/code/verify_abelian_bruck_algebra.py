"""Pure-Python checks on the bilinear normal form, not an all-prime proof."""
from itertools import product
from collections import Counter
import random

def span(vs, p, n):
    B=[]
    for w in vs:
        w=list(w)
        for i,v in B:
            c=w[i]; w=[(a-c*b)%p for a,b in zip(w,v)]
        if not any(w): continue
        i=next(i for i,a in enumerate(w) if a); a=pow(w[i],-1,p); v=tuple(x*a%p for x in w)
        B.append((i,v))
    return [v for i,v in B]

def mulm(M,x,p):return tuple(sum(a*b for a,b in zip(row,x))%p for row in M)
def triple(x,y):return (x[0]*y[1]-x[1]*y[0],x[0]*y[2]-x[2]*y[0],x[1]*y[2]-x[2]*y[1])
def T3(B,x,y):return mulm(B,triple(x,y),3)
def B3test():
    p=3; P=list(product(range(p),repeat=3))
    def valid(B):
        J=span(zip(*B),p,3)
        if not J:return True
        if len(J)==3:return False
        if any(any(T3(B,x,y)) for x in J for y in J):return False
        for x in P:
            vs=[tuple((a-b)%p for a,b in zip(y,T3(B,x,y))) for y in J]
            if len(span(vs,p,3))!=len(J):return False
        return True
    unseen=set()
    for a in product(range(3),repeat=9):
        M=(a[:3],a[3:6],a[6:])
        if valid(M):unseen.add(M)
    g1=((0,1,0),(0,0,1),(1,0,0));g2=((1,1,0),(0,1,0),(0,0,1));g3=((2,0,0),(0,1,0),(0,0,1))
    def transport(B,g):# g^-1 b(gx,gy)
        pre={mulm(g,x,3):x for x in P}
        col=list(zip(*g));vals=[pre[T3(B,col[i],col[j])] for i,j in ((0,1),(0,2),(1,2))]
        return tuple(zip(*vals))
    sizes=[]
    while unseen:
        M=unseen.pop();todo=[M];n=1
        while todo:
            a=todo.pop()
            for g in (g1,g2,g3):
                z=transport(a,g)
                if z in unseen:unseen.remove(z);todo.append(z);n+=1
        sizes.append((len(span(zip(*M),3,3)),n))
    assert len(sizes)==4 and sorted(i for i,j in sizes)==[0,1,2,2]
    print('F3^3: all 19683 bilinear alternating laws; admissible GL3 orbits (derived dimension,size)',sorted(sizes))

def elliptic(p):
    sq={i*i%p for i in range(p)}
    chars=set();matrices=0
    for a,b,c,d in product(range(p),repeat=4):
        tr=(a+d)%p; det=(a*d-b*c)%p
        if (tr*tr-4*det)%p in sq:continue
        chars.add((tr,det));matrices+=1
    reps=sorted({min(((s*t)%p,(s*s*n)%p) for s in range(1,p)) for t,n in chars})
    assert len(reps)==(p+1)//2
    return reps,matrices

def check_native(p,t,d):
    reps=list(product(range(p),repeat=3)); I={u:i for i,u in enumerate(reps)};n=p**3
    # F(u,v)=(-dv,u+tv). Use only actions on the additive states for the resolvent,
    # then recover bracket and associators again from literal LEFT permutations.
    def f(u):return (-d*u[1]%p,(u[0]+t*u[1])%p)
    invs=[]
    for k in range(p):
        D={}
        for u in product(range(p),repeat=2):
            fu=f(u);D[tuple((a-k*b)%p for a,b in zip(u,fu))]=u
        assert len(D)==p*p;invs.append(D)
    def br(x,y):
        v=f(y[1:]);w=f(x[1:]);return tuple((x[0]*a-y[0]*b)%p for a,b in zip(v,w))
    M=[]
    for x in reps:
        row=[]
        for y in reps:
            h=(x[0]+y[0])%p;b,c=invs[h][br(x,y)]
            row.append(I[(h,(x[1]+y[1]+b)%p,(x[2]+y[2]+c)%p)])
        M.append(row)
    assert all(len(set(x))==n for x in M) and all(len(set(x))==n for x in zip(*M))
    neg=[I[tuple(-a%p for a in x)] for x in reps];z2=[row[i] for i,row in enumerate(M)]
    root=dict(zip(z2,range(n))); assert len(root)==n
    central=[a for a in range(n) if all(M[a][b]==M[b][a] for b in range(n))]
    assert central==[0]
    rnu=set(range(n));lmn=set(range(n));Bols=0
    for i,x in enumerate(reps):
        for j,y in enumerate(reps):
            v=br(x,y);com=M[neg[i]][M[neg[j]][M[i][j]]]
            assert reps[com]==(0,2*v[0]%p,2*v[1]%p)
            assert reps[root[M[i][M[z2[j]][i]]]]==tuple((a+b)%p for a,b in zip(x,y))
            wij=M[M[i][j]]
            if any(wij[k]!=M[i][M[j][k]] for k in range(n)):lmn.discard(i)
            bad=[k for k in rnu if wij[k]!=M[i][M[j][k]]];rnu.difference_update(bad)
            rij=M[M[i][M[j][i]]]
            assert all(rij[k]==M[i][M[j][M[i][k]]] for k in range(n));Bols+=n
    assert rnu==set(range(p*p)) and lmn=={0}
    # True principal base-point change, not only affine parameters: conjugate H by k_s.
    # Evaluate explicit (id,beta,beta) from every pair; b'_s=(I-2sF)^-1 b on marks.
    seen=set()
    for s in range(p):
        j0=I[(s,0,0)];beta=[M[i][j0] for i in range(n)]
        ib={u:i for i,u in enumerate(beta)}
        for i,x in enumerate(reps):
            for j,y in enumerate(reps):
                z=reps[ib[M[i][beta[j]]]]
                z0=(x[0]+y[0])%p; b,c=invs[(z0+2*s)%p][br(x,y)]
                assert z==(z0,(x[1]+y[1]+b)%p,(x[2]+y[2]+c)%p)
        # determinant and trace of inverse transformed generator, mod base scaling.
        ti=t*pow(d,-1,p)%p;di=pow(d,-1,p)
        ti,di=(ti-4*s)%p,(di-2*s*ti+4*s*s)%p
        seen.add(min(((a*ti)%p,(a*a*di)%p) for a in range(1,p)))
    assert len(seen)==(p+1)//2
    return Bols

def nonlie_and_mixed():
    # A=F3^5 with [e1,e2]=j3, [e1,j2]=j1, [e2,j3]=j2. Noncommuting unipotent pencil.
    # Also A=(Z/9)^3 x Z/5 with [e1,e2]=j, [e1,j]=3j. No field-linear cancellation assumed.
    def b5(x,y):return (0,0,x[0]*y[3]-y[0]*x[3],x[1]*y[4]-y[1]*x[4],x[0]*y[1]-y[0]*x[1])
    def b9(x,y):return (0,0,x[0]*y[1]-y[0]*x[1]+3*(x[0]*y[2]-y[0]*x[2]),0)
    rng=random.Random(221353)
    for mods,b in (((3,)*5,b5),((9,9,9,5),b9)):
        n=len(mods); zero=(0,)*n
        mod=lambda v:tuple(x%m for x,m in zip(v,mods))
        add=lambda x,y:mod(a+c for a,c in zip(x,y))
        neg=lambda x:mod(-c for c in x)
        br=lambda x,y:mod(b(x,y))
        def table(x,y):
            s=add(x,y);v=br(x,y);h=zero
            for _ in range(4):
                h=add(h,v);v=br(s,v)
            assert v==zero
            return add(s,h)
        def word(x,y,z):return table(neg(x),table(neg(y),table(x,table(y,z))))
        for _ in range(3000):
            rand=lambda:tuple(rng.randrange(m) for m in mods)
            x,y,z=rand(),rand(),rand();v=br(x,y)
            assert word(x,y,zero)==add(v,v)
            assert table(x,table(y,table(x,z)))==table(table(x,table(y,x)),z)
            assert table(x,table(add(y,y),x))==add(add(x,x),add(y,y))
        if n==5:
            x,y,z=[tuple(int(i==k) for i in range(5)) for k in (0,1,4)]
            jac=add(br(x,br(y,z)),add(br(y,br(z,x)),br(z,br(x,y))))
            assert jac==(0,0,1,0,0)
        else:
            assert br((1,0,0,0),(0,0,3,0))==zero and br((1,0,0,0),(0,0,1,0))!=(0,0,0,0)
    print('Non-Jacobi F3^5 and non-elementary Z9^3 x Z5: each 3000 true product, Bruck, bracket and Bol controls.')

if __name__=='__main__':
    B3test()
    for p in (3,5,7,11,13):
        r,k=elliptic(p); tests=sum(check_native(p,*u) for u in r) if p in (3,5) else 0
        print('p=%d elliptic matrices=%d scalar/conjugacy classes=%d full native Bol triples=%d'%(p,k,len(r),tests))
    nonlie_and_mixed()
