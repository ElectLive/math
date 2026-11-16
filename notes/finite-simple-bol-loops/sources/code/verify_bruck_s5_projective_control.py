#!/usr/bin/env python3
"""Finite P(M) local-envelope control; Python 3.11+.

Nagy arXiv:0709.4544v1 Lemma 3.3 gives the six-point action;
Lemma 4.1 identifies the M and N modules. This
checks module data only; it does not construct a loop or K.
"""


assert __debug__, "Run with assertions enabled"

# Matrix model for M and N; Nagy Lemmas 3.3 and 4.1.
c6=[1,0,3,2,5,4];d6=[0,2,3,4,1,5]
c5=[1,0,2,3,4];d5=[0,2,3,4,1]
def actm(v,p):
 bits=0
 for i in range(4):
  if v>>i&1:bits^=(1<<p[0])^(1<<p[i+1])
 if bits>>5&1:bits^=63
 return (bits>>1)&15
def actn(v,p):
 bits=0
 for i in range(4):
  if v>>i&1:bits^=(1<<p[0])^(1<<p[i+1])
 return (bits>>1)&15
def tensor(p6,p5):
 out=[]
 for i in range(4):
  a=actm(1<<i,p6)
  for j in range(4):
   b=actn(1<<j,p5);v=0
   for x in range(4):
    for y in range(4):
     if a>>x&1 and b>>y&1:v^=1<<(4*x+y)
   out.append(v)
 return tuple(out)

p=globals()
C=tensor(c6,c5);D=tensor(d6,d5)
def rank(vecs):
 B={}
 for v in vecs:
  while v:
   q=v.bit_length()-1
   if q in B:v^=B[q]
   else:B[q]=v;break
 return len(B)
C,D=p['C'],p['D'];actm,actn=p['actm'],p['actn'];c6,d6,c5,d5=(p[x] for x in ('c6','d6','c5','d5'))
def tens(A,B):
 n=len(B);return tuple(sum((B[j]<<(n*i)) for i in range(len(A)) if a>>i&1) for a in A for j in range(n))
def fixed(A,B):return len(A)-rank([(A[i]^(1<<i))|((B[i]^(1<<i))<<len(A)) for i in range(len(A))])
for kind,fn in [('M',actm),('N',actn)]:
 cc=c6 if kind=='M' else c5;dd=d6 if kind=='M' else d5
 a=[fn(1<<i,cc) for i in range(4)];b=[fn(1<<i,dd) for i in range(4)]
 assert fixed(tens(C,a),tens(D,b)) == (1 if kind == 'M' else 0)
assert fixed(C,D) == 0
def pmul(a,b):return tuple(a[b[i]] for i in range(len(a)))
I5=tuple(range(5));I6=tuple(range(6));gens=[(tuple(c5),tuple(c6)),(tuple(d5),tuple(d6))]; G=[(I5,I6)]
for x,y in G:
 for a,b in gens:
  z=(pmul(x,a),pmul(y,b))
  if z not in G:G.append(z)
assert len(G)==120
def ppow(p,n):
 x=tuple(range(len(p)))
 for i in range(n):x=pmul(x,p)
 return x
cy=next((x,y) for x,y in G if x!=I5 and ppow(x,5)==I5)
qx=next((x,y) for x,y in G if ppow(x,4)==I5 and ppow(x,2)!=I5 and pmul(pmul(x,cy[0]),ppow(x,3))==ppow(cy[0],2))
PC=p['tensor'](cy[1],cy[0]);QC=p['tensor'](qx[1],qx[0]);assert 16-rank([PC[i]^(1<<i) for i in range(16)]) == 4
def ma(A,v):
 out=0
 while v:
  bit=v&-v;out^=A[bit.bit_length()-1];v-=bit
 return out
def basis(vs):
 b={}
 for v in vs:
  while v:
   q=v.bit_length()-1
   if q in b:v^=b[q]
   else:
    b[q]=v
    for i in b:
     if i!=q and b[i]>>q&1:b[i]^=v
    break
 return tuple(b[i] for i in sorted(b,reverse=True))
def closure(vs, gens):
 b=basis(vs)
 while 1:
  x=basis(list(b)+[ma(a,v) for a in gens for v in b])
  if len(x)==len(b):return x
  b=x
fixedp=[v for v in range(65536) if ma(PC,v)==v]
w0=basis([ma(QC,v)^v for v in fixedp]);assert len(fixedp)==16 and len(w0)==3
lines=set()
for v in range(1,65536):
 e=v;x=v
 for i in range(4):x=ma(PC,x);e^=x
 v^=e
 if v:
  b=closure([v],(PC,QC))
  if len(b)!=4: continue
  lines.add(b)
  if len(lines)==7:break
assert len(lines)==7
t=p['tensor'](c6,c5);images=basis([t[i]^(1<<i) for i in range(16)]);assert len(images)==8
for i,b in enumerate(sorted(lines)):
 W=basis(w0+b); inter=len(W)+len(images)-len(basis(W+images))
 assert inter == (0,0,2,0,2,3,0)[i]
for i,b in enumerate(sorted(lines)):
 stable=all(rank(list(b)+[ma(A,v) for v in b])==4 for A in (C,D))
 assert stable == (i == 5)
syl=next((x,y) for x,y in G if x!=I5 and ppow(x,2)==I5 and pmul(pmul(x,qx[0]),x)==ppow(qx[0],3) and x!=ppow(qx[0],2))
SC=p['tensor'](syl[1],syl[0]);assert fixed(QC,SC)==2
ll=sorted(lines);soc=ll[5];B=basis(ll[0]+ll[1])
assert len(B)==8 and rank(B+soc)>8
assert len(B)+len(images)-len(basis(B+images))==0
print("P(M): all 7 lines checked; 4 corefree collision-free 7-spaces; 8-space B checked")
