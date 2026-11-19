"""Independent literal loop-table checks. No dependencies or source checker imports."""
from itertools import product
from collections import Counter
from math import lcm

def check(p,d,wrap):
    # N is a weighted cyclic shift or a nilpotent single Jordan block.
    points=list(product(range(p),repeat=d)); num={v:k for k,v in enumerate(points)}; s=len(points); n=p*s
    def f(i,v):
        return tuple((v[k]+i*(v[k-1] if k else wrap*v[-1]))%p for k in range(d))
    F=[[num[f(i,v)] for v in points] for i in range(p)]
    assert all(len(set(a))==s for a in F)
    inv=[[a.index(k) for k in range(s)] for a in F]
    add=[[num[tuple((x+y)%p for x,y in zip(u,v))] for v in points] for u in points]
    T=[[(i+j)%p*s+add[v][F[(i+2*j)%p][inv[i][u]]] for j in range(p) for v in range(s)]
       for i in range(p) for u in range(s)]
    universe=set(range(n)); assert T[0]==list(range(n)) and [a[0] for a in T]==T[0]
    assert all(set(a)==universe for a in T+list(zip(*T)))
    for x in range(n):
        for y in range(n):
            row=T[T[x][T[y][x]]]
            assert all(T[x][T[y][T[x][k]]]==row[k] for k in range(n))
        z=0
        for _ in range(p): z=T[x][z]
        assert z==0
    # No division supplied: close under all products of two already obtained points.
    gen={s,num[(1,)+(0,)*(d-1)]}; work=list(gen)
    while work:
        x=work.pop()
        for y in list(gen):
            for z in (T[x][y],T[y][x]):
                if z not in gen: gen.add(z);work.append(z)
    assert gen==universe
    U=[T[T[x][s]][(p-1)*s] for x in range(n)];todo=set(range(n)); cyc=Counter()
    while todo:
        x=min(todo); z=x; m=0
        while z in todo:todo.remove(z);z=U[z];m+=1
        assert z==x;cyc[m]+=1
    nonassoc=sum(T[T[x][y]][z]!=T[x][T[y][z]] for x in range(n) for y in range(n) for z in range(n))
    if not wrap: assert lcm(*cyc)==next(p**h for h in range(d+1) if 2*p**h>=d) and (not nonassoc)==(d<=2)
    else: assert nonassoc and lcm(*cyc)>1
    print(f"p={p} d={d} t^d={wrap}: sites {n}, generated {len(gen)}, Bol triples {n**3}, nonassociative triples {nonassoc}, full U cycles {dict(sorted(cyc.items()))}")

def large(p,d):
    # Literal right-translation product acting on the unit basis vector; no symbolic exponentiation.
    def reduce_step(i,j,u):
        x=[]
        for k,a in enumerate(u): x.append((a-(i*x[k-1] if k else 0))%p)
        return [(a+((i+2*j)*x[k-1] if k else 0))%p for k,a in enumerate(x)]
    orders=[]
    for i in range(p):
        start=[1]+[0]*(d-1);u=start;count=0
        while True:
            u=reduce_step(i+1,-1,reduce_step(i,1,u));count+=1
            if u==start:break
            assert count<2*p*d
        orders.append(count)
    assert len(set(orders))==1 and orders[0]==next(p**h for h in range(d+1) if 2*p**h>=d)
    print(f"p={p} Fp[t]/t^{d}: true basis point U-period in each of {p} native fibers = {orders[0]}")

if __name__=='__main__':
    for case in ((3,1,0),(3,2,0),(3,3,0),(3,4,0),(3,2,2),(5,2,0),(5,2,2)):check(*case)
    for p,d in ((3,7),(3,19),(3,55),(5,51),(7,99)):large(p,d)
