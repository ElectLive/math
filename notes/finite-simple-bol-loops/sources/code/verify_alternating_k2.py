"""C0010 k=2 degree/order overbounds, conditional on Kantor 1985 §2 roster.
Python standard library only; all operations exact. No group-library census.
"""
from math import factorial, isqrt, prod

def prime_power(n):
    for p in range(2, n+1):
        if any(p % d == 0 for d in range(2, isqrt(p)+1)):
            continue
        x,e=p,1
        while x<n:
            x*=p; e+=1
        if x==n:
            return p,e
    return None

def gl(d,q):
    return prod(q**d-q**i for i in range(d))

def j(n):
    a,b=1,1
    for r in range(2,n+1):
        a,b=b,b+(r-1)*a
    return b if n else a

rows={n:[] for n in range(9,54)}
def add(n,name,order):
    if n in rows:
        rows[n].append((name,order))

# Full automorphism-group bounds; duplicate degrees are intentional.
for n,name,order in [
 (11,'PSL2(11) exceptional action',1320),
 (11,'M11 natural',7920), (12,'M11 degree 12',7920),
 (12,'M12 natural (outer fuses actions)',95040),
 (15,'A7 exceptional degree 15',5040),
 (22,'M22.2',887040), (23,'M23',10200960), (24,'M24',244823040),
 (28,'PSU3(3) automorphism overbound',2*3**3*(3**3+1)*(3**2-1)),
 (28,'small Ree q=3: PΓL2(8), distinct degree-28 action',1512),
 (28,'Sp6(2) minus action',1451520),
 (36,'Sp6(2) plus action',1451520),
]: add(n,name,order)

for n in rows:
    z=prime_power(n)
    if z:
        p,e=z
        add(n,f'full AGL({e},{p})',n*gl(e,p))
    for q in range(2,53):
        z=prime_power(q)
        if z is None: continue
        _,f=z
        points=1
        for d in range(2,7):
            points+=q**(d-1)
            if points==n:
                # PΓL_d(q); add a graph factor for d>2 as safe overbound.
                add(n,f'PΓL({d},{q}) and graph overbound',
                    (f if d==2 else 2*f)*gl(d,q)//(q-1))
            if points>n: break

survivors=[]
for n,entries in rows.items():
    if not entries: continue
    bound=max(order for _,order in entries)
    if factorial(n)<=4*bound*j(n-2):
        survivors.append(n)
    else:
        assert factorial(n)>4*bound*j(n-2)
assert survivors==[9,10,11,12],survivors
assert any('small Ree' in name and order==1512 for name,order in rows[28])
assert max(order for _,order in rows[28])==1451520
for n in survivors:
    bound=max(order for _,order in rows[n])
    print('survivor',n,'U',bound,'rows',rows[n])
print('all other listed degrees 9..53: strict comparison passed')
print('distinct Ree degree-28 action explicitly included')
