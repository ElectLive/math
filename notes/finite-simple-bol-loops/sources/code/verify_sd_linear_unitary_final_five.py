#!/usr/bin/env python3
"""Arithmetic only; see sd-linear-unitary-final-five.md for hypotheses."""
from math import gcd,prod

def gl(d,q): return prod(q**d-q**i for i in range(d))
def sp4(q): return q**4*(q*q-1)*(q**4-1)
def o4(q,e): return 2*q*q*(q*q-e)*(q*q-1)
q=5; D=gl(4,q); P=D//(q-1); n=P//4; a=2*P
pairs=[(D,gl(1,q)*gl(3,q)),(D,2*gl(2,q)**2),(D,2*gl(2,q*q)),(D,o4(q,1)),(D,o4(q,-1)),(D,sp4(q))]
assert all(x%y==0 for x,y in pairs)
inner=sum(x//y for x,y in pairs[:3]); matrices=sum(x//y for x,y in pairs[3:])
assert matrices%(q-1)==0
b=1+inner+matrices//(q-1)
assert (n,a,b)==(7254000000,58032000000,2366976)
assert n>=2**20 and b**3+3*a*b<n*n
print('PSL4(5)',n,a,b)

for typ,d,q,f in [('L',4,9,2),('U',4,7,1),('U',4,8,3),('U',5,4,2)]:
 if typ=='L': n=50759843097600; a=16*n
 else:
  n=q**(d*(d-1)//2)*prod(q**i-(-1)**i for i in range(2,d+1))//gcd(d,q+1)
  a=2*f*gcd(d,q+1)*n
 B=1+2*(q+1)*q**((d*d+d-2)//2-1)
 assert n>=2**20 and B**3+3*a*B<n*n
 print(typ,d,q,n,a,B)
