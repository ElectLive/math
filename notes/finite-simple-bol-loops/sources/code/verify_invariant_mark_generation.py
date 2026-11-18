"""Invariant-square generation, plus a counterexample when mark invariance is removed."""
from itertools import permutations, product

def mul(a,b):return tuple(a[i] for i in b)
def inv(a):return tuple(a.index(i) for i in range(len(a)))
def conj(a,b):return mul(mul(a,b),inv(a))
def even(a):return sum(x>y for i,x in enumerate(a) for y in a[i+1:])%2==0
def group(K,e):
    gg={e};todo=[e]
    while todo:
        a=todo.pop()
        for k in K:
            b=mul(a,k)
            if b not in gg:gg.add(b);todo.append(b)
    return gg
def check(n,alternate):
    e=tuple(range(n));S=set(permutations(e));G={g for g in S if not alternate or even(g)}
    # Conjugation by any ambient involution, including an actual outer one
    # for A_4/A_5. For r in G use the formally distinguished r even if it
    # acts trivially. The signed presentation has the same real K in G.
    cases=0;proper=0;outer=0
    for r in S:
        if mul(r,r)!=e:continue
        C={mul(r,g) for g in G};outside={a for a in C if mul(a,a)==e}
        classes=[];rest=set(outside)
        while rest:
            a=next(iter(rest));cl={conj(g,a) for g in G}
            assert cl<=rest;rest-=cl;classes.append(cl)
        for bits in product((0,1),repeat=len(classes)):
            marks=set().union(*(c for c,b in zip(classes,bits) if b))
            if r not in marks:continue
            # G-invariance plus r-stability; the latter is automatic here,
            # but keep the explicit test as in the theorem.
            if any(conj(r,a) not in marks for a in marks):continue
            K={mul(r,a) for a in marks};sq={mul(a,b) for a,b in product(marks,repeat=2)}
            L=group(K,e)
            assert K<=sq and sq=={mul(inv(a),b) for a,b in product(K,repeat=2)}
            assert L==group(sq,e) and all(conj(g,a) in L for g in G for a in L)
            cases+=1;proper+=L!=G;outer+=r not in G
    return cases,proper,outer

if __name__=="__main__":
 for n,alt in ((3,False),(4,True),(4,False),(5,True)):
    print(("A" if alt else "S")+str(n),"invariant masks/proper generation/outer cases",*check(n,alt))
 e=(0,1,2,3);S=set(permutations(e))
 v4={g for g in S if g==e or all(g[i]!=i for i in e) and mul(g,g)==e}
 K={e,(1,0,2,3),(2,1,0,3)};L=group(K,e)
 assert len(v4)==4 and len(L)==6 and len({mul(a,b) for a,b in product(v4,L)})==24
 assert any(conj(g,k) not in K for g in S for k in K)
 assert group({conj(g,k) for g in S for k in K},e)==S
 print("Without mark invariance: K generates a nonnormal S3, maps onto S4/V4, and has full normal closure S4.")
