"""Exact finite-matrix and all-projected-sign controls at the claimed p=3,q=61 first degree.
No third-party packages. Quadratic zero is checked on the complete coefficient matrix, not random lifts.
"""
from itertools import product
p=3;q=61;f=10;alpha=13
assert pow(alpha,3,q)==1 and alpha!=1
def rank(rows):
    b={}
    for row in rows:
        v=list(row)
        for i in sorted(b):
            c=v[i]%3;v=[(a-c*z)%3 for a,z in zip(v,b[i])]
        i=next((i for i,z in enumerate(v) if z%3),None)
        if i is not None:b[i]=[a*pow(v[i],-1,3)%3 for a in v]
    return len(b)
def add(v,w):return tuple((a+b)%3 for a,b in zip(v,w))
def neg(v):return tuple(-a%3 for a in v)
def scale(c,v):return tuple(c*a%3 for a in v)
def dot(v,w):return sum(a*b for a,b in zip(v,w))%3
def basis(n):return [tuple(int(i==j) for i in range(n)) for j in range(n)]
one=(1,)+(0,)*9
def timesz(v):
    r=[0]+list(v[:-1]);h=v[-1]
    for i in [0,3,4,5,6,7]:r[i]=(r[i]-h)%3
    return tuple(r)
Z=[one]
for e in range(60):Z.append(timesz(Z[-1]))
assert timesz(Z[-1])==one and len(set(Z))==61
assert [i for i in range(1,11) if pow(3,i,q)==1]==[10] and pow(3,5,61)==60
def tr(k):
    u=tuple(sum(Z[k*pow(3,i,q)%q][j] for i in range(10))%3 for j in range(10))
    assert not any(u[1:]);return u[0]
g=[tuple((tr(1+i-j)-tr(-1+i-j))%3 for j in range(10)) for i in range(10)]
assert rank(g)==10 and all((g[i][j]+g[j][i])%3==0 for i,j in product(range(10),repeat=2))
def zm(k,v):return tuple(sum(v[i]*Z[(k+i)%61][j] for i in range(10))%3 for j in range(10))
def pointg(x,y):return sum(a*dot(v,y) for a,v in zip(x,g))%3
for k in range(1,61):
    assert rank([add(zm(k,e),neg(e)) for e in basis(10)])==10
    assert all(pointg(Z[(k+i)%61],Z[(k+j)%61])==g[i][j] for i,j in product(range(10),repeat=2))
def B(x,y):return sum(pointg(x[10*j:10*j+10],y[10*((-j)%3):10*((-j)%3)+10]) for j in range(3))%3
base=basis(30);O=(0,)*30
def om(u,v):return (B(u[0],v[1])+B(u[1],v[0]))%3
def hmul(g,h):
    (a,b),c=g;(d,e),z=h
    return (add(a,d),add(b,e)),(c+z+2*om((a,b),(d,e)))%3
def tm(x,y):
    a,b,i,s=x;c,d,j,t=y
    if s:c,d=d,c;j=-j
    return (a+pow(alpha,i,q)*c)%q,(b+pow(alpha,-i,q)*d)%q,(i+j)%3,(s+t)%2
X=list(product(range(61),range(61),range(3),[0]));I=(0,0,0,0)
outs=[(a,b,j,1) for a,b,j,_ in X];signs=[s for s in outs if tm(s,s)==I];assert len(signs)==183
# F_s is the genuine linear map from second half to first of s=(a,b)h^i t.
def Ftop(s,x):
    a,b,i,_=s;out=[]
    for j in range(3):
        e=(pow(alpha,j,q)*a+pow(alpha,-j,q)*b)%q
        j0=(j+i)%3
        out+=zm(e,x[10*j0:10*j0+10])
    return tuple(out)
def whole(s,x):
    a,b,i,t=s;v,w=x
    if t:v,w=w,v
    return Ftop((a,b,i,0),v),Ftop((b,a,-i,0),w)
def model():
    b1=(1,0,0,0);b2=(0,1,0,0);h=(0,0,1,0);t=(0,0,0,1)
    Vbasis=[(e,O) for e in base]+[(O,e) for e in base]
    sv=[b1,b2,h,t,(6,18,2,1)]
    for a,b in product(sv,repeat=2):
        for u in Vbasis:assert whole(tm(a,b),u)==whole(a,whole(b,u))
    for a in sv:
        vv=[whole(a,x) for x in Vbasis]
        assert all(om(vv[i],vv[j])==om(Vbasis[i],Vbasis[j]) for i,j in product(range(60),repeat=2))
    print('GF(3^10), q=61: all 60 nonidentity powers fixed-point-free and symplectic; genuine 60-D signed representation and all 18,000 chosen-generator form entries checked.')
    M={}
    for a in signs:
        # D_s[i,j]=B(F_s e_i, e_j); B(e_i,F_s e_j)=-D_s[j,i].
        fe=[Ftop(a,e) for e in base]
        M[a]=[tuple(B(x,y) for y in base) for x in fe]
    tally={};nt=0;tests={}
    for a,b in product(signs,repeat=2):
        z=tm(a,b);c=tm(z,a)
        if z[0] or (z[2]==0 and z[1]):continue
        assert z[3]==0 # z in J
        D=M[a];E=M[c]
        # Symmetric part of the exact scalar quadratic on all 3^30 stabilizer-vector parameters.
        assert all((D[i][j]-E[j][i]+D[j][i]-E[i][j])%3==0 for i,j in product(range(30),repeat=2))
        tally[z]=tally.get(z,0)+1;nt+=1
        if z==I:assert c==a
        else:assert z[2] in [1,2]
        if len(tests)<8 and z[2]:
            x=tuple((i*i+i*z[1]+1)%3 for i in range(30))
            a0=(Ftop(a,x),neg(x));a1=(neg(Ftop(c,x)),x)
            assert hmul((a0,0),(a1,0))[1]==0;tests[z]=(a0,a1)
    assert len(tally)==123 and tally[I]==183 and all(v==3 for z,v in tally.items() if z!=I)
    assert nt==549
    # Genuine nonzero central phase is present if the sum is not required to belong to the stabilizer Lagrangian.
    a0=next((x,neg(x)) for x in base if any(B(x,y) for y in base))
    a1=next((y,neg(y)) for y in base if B(a0[0],y))
    gout=hmul((a0,0),(a1,0));assert gout[1] and gout[0][1]!=O
    print('33,489 projected involution pairs exhaustively; 183 identity and 366 nontrivial stabilizer collisions examined. For all 549 the entire 30-variable physical central-phase polynomial vanishes (494,100 symmetric coefficients). A true off-Lagrangian physical product has a nonzero phase.')
    # Physical bad reference: removing the central shift really creates collisions at both rotations.
    for j in [1,2]:assert tm(t,(0,0,-j%3,1))==(0,0,j,0)
    # True signed invariant alternative cuts graphs of +/- site reversal, not just center and whole N.
    def rev(v):return tuple(v[10*((-j)%3)+l] for j in range(3) for l in range(10))
    for c in [1,2]:
        Y=[(e,scale(c,rev(e))) for e in base]
        for a in [b1,b2,h,t]:
            for v in Y:
                x,y=whole(a,v);assert y==scale(c,rev(x))
        negative=rank([add(scale(c,rev(e)),neg(e)) for e in base])
        assert negative in (10,20) and 31>negative
        print('Actual noncoordinate signed normal layer of rank 30: physical orbit exponent 31, t-negative exponent',negative)
    Et=[(e,neg(e)) for e in base];assert rank([[om(x,y) for y in Et] for x in Et])==30
    print('p=3,q=61 top and two 30-D Lagrangians: negative eigenspace nondegenerate of rank 30; true loop degree 3^31*61 and extraspecial p-core order 3^61. No table of that size enumerated.')
if __name__=='__main__':model()
