"""The order-63 pair from a scalar formula; no group construction or third-party package."""
from itertools import product,combinations
from collections import Counter
from hashlib import sha256
from pathlib import Path
import sys
X=list(product(range(3),repeat=2));I=(0,0)
U=list(product(X,range(7)))
def add(x,y):return tuple((a+b)%3 for a,b in zip(x,y))
def neg(x):return (-x[0]%3,-x[1]%3)
def s(x):return 1 if x==I else 3
def coeff(x,y):
 z=add(x,y);w=(x[1]*y[0]-x[0]*y[1])%3
 return z,(pow(2,w,7)*s(add(x,neg(y))))%7,(pow(2,-w,7)*s(y))%7,(pow(2,-w,7)-1)%7,s(z)
def operation(xh,yt,j):
 x,h=xh;y,t=yt;z,a,b,c,d=coeff(x,y)
 return z,((a*h+b*t+c*j)*pow(d,-1,7))%7
def rr(rows,dim):
 a=[list(row) for row in rows];k=0;idx=[]
 for c in range(dim):
  u=next((i for i in range(k,len(a)) if a[i][c]%7),None)
  if u is None:continue
  a[k],a[u]=a[u],a[k];a[k]=[(z*pow(a[k][c],-1,7))%7 for z in a[k]]
  for i in range(len(a)):
   if i!=k:
    z=a[i][c];a[i]=[(v-z*w)%7 for v,w in zip(a[i],a[k])]
  idx.append(c);k+=1
 return len(idx),a
def equations():
 rows=[];labs=[]
 for x,y in product(X,repeat=2):
  z,a,b,c,d=coeff(x,y);r=[0]*9
  for t,k in [(z,d),(x,-a),(y,-b)]:
   if t!=I:r[X.index(t)-1]=(r[X.index(t)-1]+k)%7
  r[8]=c;rows.append(r);labs.append((x,y))
 assert rr(rows,8)[0]==6 and rr(rows,9)[0]==7
 ids=[i for i,row in enumerate(rows) if any(row)]
 for i in ids[:]:
  f=[j for j in ids if i!=j];a=[rows[j] for j in f]
  if rr(a,9)[0]>rr(a,8)[0]:ids=f
 rows0=[rows[i]+[int(i==j) for j in ids] for i in ids]
 witness=next(r for r in rr(rows0,8)[1] if not any(r[:8]) and r[8]);scale=pow(witness[8],-1,7)
 lin=[scale*c%7 for c in witness[9:]]
 assert [sum(a*rows[i][j] for a,i in zip(lin,ids))%7 for j in range(9)]==[0]*8+[1]
 print('81 graph equations in 8 unknowns; coefficient rank 6, tilted augmented rank 7.')
 print('normalized 0=1 certificate (weight,x,y):',[(a,*labs[i]) for a,i in zip(lin,ids)])
def tests(j,dump=False):
 n=len(U);tab=[[U.index(operation(x,y,j)) for y in U] for x in U]
 b=('\n'.join(','.join(map(str,row)) for row in tab)+'\n').encode();h=sha256(b).hexdigest()
 if dump:Path(dump).write_bytes(b)
 assert all(set(r)==set(range(n)) for r in tab) and all(len({r[k] for r in tab})==n for k in range(n))
 assert tab[0]==list(range(n)) and [r[0] for r in tab]==list(range(n))
 assert all(tab[x][tab[y][tab[x][z]]]==tab[tab[x][tab[y][x]]][z] for x,y,z in product(range(n),repeat=3))
 def order(x):
  v=0
  for m in range(1,64):
   v=tab[x][v]
   if v==0:return m
 orders=[order(x) for x in range(n)];assert Counter(orders)=={1:1,3:56,7:6}
 def cl(x,y):
  c={0,x,y}
  while len(c)<=9:
   d=c|{tab[u][v] for u,v in product(c,repeat=2)}
   if d==c:break
   c=d
  return c
 pairs=0;small=set()
 for x,y in combinations([k for k,v in enumerate(orders) if v==3],2):
  if y==tab[x][x]:continue
  pairs+=1;v=cl(x,y);assert len(v)>=9
  if len(v)==9:small.add(frozenset(v))
 assert pairs==1512 and len(small)==(49 if j==0 else 0)
 ra=next(((x,y,tab[tab[x][y]][y],tab[x][tab[y][y]]) for x,y in product(range(n),repeat=2) if tab[tab[x][y]][y]!=tab[x][tab[y][y]]),None)
 print('native j',j,'Latin, identity, 250047 left Bol triples; cyclic-line pairs',pairs,'9-subloops',len(small),'right-alternative witness',ra,'table SHA256',h)
 return tab
if __name__=='__main__':
 equations();tests(0);tests(1,sys.argv[1] if len(sys.argv)>1 else False)
