#!/usr/bin/env python3
"""F9 certificate: anisotropic orbit spans all Frobenius bilinear coefficients."""
def add(x,y):return (x%3+y%3)%3+3*((x//3+y//3)%3)
def neg(x):return (-x%3)+3*((-(x//3))%3)
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x%3,x//3;c,d=y%3,y//3
 return (a*c+2*b*d)%3+3*((a*d+b*c)%3)
def power(x,n):
 y=1
 while n:
  if n&1:y=mul(y,x)
  x=mul(x,x);n//=2
 return y
points=[(1,0,4),(1,0,5),(1,0,7),(1,1,3),(1,1,5),(1,1,6),(1,2,3),(1,2,5),(1,3,3)]
squares={power(x,2) for x in range(1,9)}
assert all(sub(power(v[1],2),mul(v[0],v[2])) not in squares|{0} for v in points)
a=[[mul(v[i],power(v[j],3)) for i in range(3) for j in range(3)] for v in points]
det=1
for k in range(9):
 pivot=next(i for i in range(k,9) if a[i][k])
 if pivot!=k:a[k],a[pivot]=a[pivot],a[k];det=neg(det)
 z=a[k][k];det=mul(det,z)
 for i in range(k+1,9):
  t=mul(a[i][k],power(z,7));a[i]=[sub(x,mul(t,y)) for x,y in zip(a[i],a[k])]
assert det==3
print('9 nonsquare-discriminant points; determinant i; rank 9 over F9')
