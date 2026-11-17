from math import factorial, isqrt

def invol(n):
 a,b=1,1
 for i in range(2,n+1): a,b=b,b+(i-1)*a
 return b

def primepower(q):
 for p in range(2,q+1):
  if any(p%k==0 for k in range(2,isqrt(p)+1)): continue
  z=p;e=1
  while z<q:z*=p;e+=1
  if z==q:return e
 return 0

def affine(e):
 v=2**e
 for i in range(e):v*=2**e-2**i
 return v
survivors=[]
for m in range(10,54):
 d=m-3;q=m-1;e=primepower(q)
 families=[]
 if e:families.append(('semilinear',q*(q*q-1)*e))
 if m&(m-1)==0:families.append(('affine',affine(m.bit_length()-1)))
 for n,name,order in [(11,'M11',7920),(12,'M11/M12',95040),(22,'M22.2',887040),(23,'M23',10200960),(24,'M24',244823040)]:
  if m==n:families.append((name,order))
 for name,order in families:
  if factorial(m)<=12*order*invol(d):
   survivors.append((m,name))
   print(m,name,'degree lower',factorial(m)//(2*order),'capacity',6*invol(d))

assert survivors==[(10,'semilinear'),(11,'M11'),(12,'M11/M12')]
print('PASS')
assert factorial(10)//(2*720)==2520
assert 6*invol(7)==1392
assert factorial(11)//(2*7920)==2520
assert factorial(12)//(2*95040)==2520
assert factorial(12)//(2*7920)==30240
assert factorial(8)//(2*1344)==15
assert factorial(8)//(2*168)==120
assert 26*3==78 and 10*4==40
assert (factorial(8)//2 & -(factorial(8)//2))==64
assert (factorial(9)//2 & -(factorial(9)//2))==64
assert [n & -n for n in (2520,30240)]==[8,32]
assert 3*(1+28)==87 and 3*(1+36)==111
print('PASS low-degree exact comparisons')
