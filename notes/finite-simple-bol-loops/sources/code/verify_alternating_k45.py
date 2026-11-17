#!/usr/bin/env python3
"""Arithmetic and low-degree class-square controls, not subgroup classifications."""
from itertools import permutations, combinations
from math import factorial

def inv(n):
    a,b=1,1
    if n==0:return 1
    for j in range(2,n+1): a,b=b,b+(j-1)*a
    return b

def class_size(n,j):
    return factorial(n)//(2**j*factorial(j)*factorial(n-2*j))

def subsets(values,target):
    return [tuple(i for i in range(len(values)) if mask>>i&1)
            for mask in range(1<<len(values))
            if sum(values[i] for i in range(len(values)) if mask>>i&1)==target]

cases=[(23,4,10200960,1267136462592000,115432834560),
       (24,4,244823040,1267136462592000,570207938304),
       (24,5,244823040,1267136462592000,577164172800),
       (33,4,163680,26525285981219105863630848000000,2447765430112957440)]
for m,k,order,n,bound in cases:
    assert factorial(m)//(2*order)==n and factorial(k)*inv(m-k)==bound and n>bound
assert [factorial(5)//2, factorial(7)//2, factorial(8)//2]==[60,2520,20160]
assert [next(2**j for j in range(20) if v%2**(j+1)) for v in (60,2520,20160,120)]==[4,8,64,8]
assert 24*(1+class_size(8,1))==696<2520
assert [sum(class_size(7,j) for j in range(4) if j%2==p) for p in (0,1)]==[106,126]
assert [sum(class_size(5,j) for j in range(3) if j%2==p) for p in (0,1)]==[16,10]
assert [sum(class_size(4,j) for j in range(3) if j%2==p) for p in (0,1)]==[4,6]
assert 106*6+126*4==1140<2520
assert max(126*16,106*10,126*10)<2520
assert max(16*6,10*4,10*6)<120
v75=[class_size(7,i)*class_size(5,j) for i in range(4) for j in range(3) if (i+j)%2]
assert v75==[10,21,315,1050,105,1575] and subsets(v75,2520)==[]
v54=[class_size(5,i)*class_size(4,j) for i in range(3) for j in range(3) if (i+j)%2]
assert v54==[6,10,30,90] and subsets(v54,120)==[(2,3)]

def parity(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2

def comp(p,q): return tuple(p[q[i]] for i in range(len(p)))

def cycle_lengths(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i not in seen:
            j=i;n=0
            while j not in seen:seen.add(j);n+=1;j=p[j]
            out.append(n)
    return sorted(out)

p5=list(permutations(range(5)))
a5={p for p in p5 if parity(p)==0}
doubles=[p for p in p5 if cycle_lengths(p)==[1,2,2]]
squares={comp(a,b) for a in doubles for b in doubles}
assert len(doubles)==15 and squares==a5
p4=list(permutations(range(4)))
trans=[p for p in p4 if cycle_lengths(p)==[1,1,2]]
assert {p for p in p4 if cycle_lengths(p)==[1,3]} <= {comp(a,b) for a in trans for b in trans}
print('PASS: four large bounds; small parity counts and subset sums; A5 and S4 class squares')
