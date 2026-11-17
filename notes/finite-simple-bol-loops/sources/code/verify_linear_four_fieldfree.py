#!/usr/bin/env python3
"""Integer certificate for nine q=5 (mod 8) class patterns.

Run with Python 3.11+ and assertions enabled. The source class inventory is
a mathematical input; polynomial identities and all finite checks are exact.
Regenerate frozen data using generate_linear_four_overgroups.py (SymPy 1.14.0).
"""
import json
from itertools import product
DATA=json.loads(r'''[[[0,1,0,1],[2,0,-2,0,-2,0,2,0,0],[1,2,-1],[656,1584],[-1312,-544,1088,448,1504,608,-1024,-512],512],[[0,1,1,0],[2,0,-4,-2,2,4,0,-2,0,0,0],[1,0,0,3,4],[237568,303104,-942080,2195456],[-475136,-606208,2834432,-1277952,81920,-737280,-2441216,4718592,-6291456,8388608],33554432],[[0,1,1,1],[2,0,-2,-2,-2,2,2,2,0,-2,0,0,0],[1,2,-1,3,2,5,4],[20623392768,24993857536,-42102423552,94728355840,-26394755072,110914174976],[-41246785536,32505856000,19193135104,19637731328,24712839168,-53980692480,-939524096,-40038825984,30492590080,18253611008,-21474836480,17179869184],68719476736],[[1,0,0,1],[1,0,-1,0,-1,0,1,0,0,0,0],[1,-1,0,1],[16,-29,22],[-16,13,7,-6,19,-17,-5,5,0,5],5],[[1,0,1,0],[1,0,-1,-1,-1,1,1,1,0,-1,0,0,0,0],[2,3,2,2,-1],[-731096,-1330780,-1160980,-1114508],[365548,117068,-326208,-466988,-519032,192692,427072,506412,164236,-311296,-98304,-32768,-16384],16384],[[1,0,1,1],[1,0,-1,-1,-1,1,1,1,0,-1,0,0,0,0],[1,-1,2,2,3,2,-1],[-2020604,1297696,-3460056,-5464720,-7653892,-6781212],[2020604,722908,-1878848,-2624060,-2903064,1067556,2477376,2784316,964892,-1802240,-573440,-163840,-81920],81920],[[1,1,0,1],[2,-2,0,0,-2,2,0,0,0,0],[1,1,-2,2],[-2624,-6912,-2176],[5248,3328,-2304,-5888,-10624,-5120,5120,10240,10240],20480],[[1,1,1,0],[2,0,-2,-2,-2,2,2,2,0,-2,0,0,0,0],[1,0,1,3,6,3,4,-2],[-348043345920,-115376914432,-388862312448,-1176502272000,-2478313570304,-1874988105728,-2040277237760],[696086691840,230753828864,-614448758784,-892849881088,-1002270883840,347993014272,810943512576,973380517888,330880253952,-584115552256,-188978561024,-68719476736,-34359738368],68719476736],[[1,1,1,1],[2,-2,0,-2,0,2,0,2,-2,0,0,0,0],[1,1,-2,5,-1,6,-2],[27592753152,36512464896,-43255857152,124097396736,12152995840,170117824512],[-55185506304,37346082816,11819548672,59279147008,19357761536,-49064968192,-15837691904,-60394831872,35567697920,11408506880,4026531840,1342177280],-2684354560]]''')
def trim(a):
 while len(a)>1 and not a[-1]:a.pop()
 return a
def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return trim(out)
def scale(a,n):return trim([n*x for x in a])
def powp(a,n):
 v=[1]
 for _ in range(n):v=mul(v,a)
 return v
def ev(a,x):
 t=0
 for c in a:t=t*x+c
 return t
def main():
 x=[0,1]; one=[1]; xm1=add(x,[-1]); xp1=add(x,[1]); x2p1=add(powp(x,2),[1]); x2m1=add(powp(x,2),[-1]);x3m1=add(powp(x,3),[-1]);x4m1=add(powp(x,4),[-1])
 S4=mul(mul(mul(powp(x,6),x2m1),x3m1),x4m1)
 sizes4=[scale(mul(powp(x,2),x3m1),2),mul(mul(powp(x,4),x3m1),x2p1),scale(mul(mul(powp(x,3),xp1),x2p1),4),scale(mul(mul(powp(x,4),xm1),x3m1),2)]
 patterns={p for p in product(range(2),repeat=4) if any(p[:2]) and any(p[2:])}
 assert {tuple(row[0]) for row in DATA}==patterns and len(DATA)==9
 for p,N,D,A,B,k in DATA:
  N,D,A,B=([*reversed(z)] for z in (N,D,A,B));assert k and D[-1]>0
  lam=[0]
  for c,term in zip(p,sizes4):lam=add(lam,scale(term,c))
  assert scale(mul(S4,D),2)==mul(lam,N)
  assert add(mul(A,N),mul(B,D))==[k]
  d=len(D)-1;X=128
  assert 2*sum(abs(D[i])*X**i for i in range(d))<D[-1]*X**d
  assert D[-1]*X**d>2*abs(k)
 for q in range(5,128,8):
  s=ev(list(reversed(S4)),q);zs=[ev(list(reversed(t)),q) for t in sizes4]
  for p in patterns:
   v=sum(c*z for c,z in zip(p,zs));assert 2*s%v!=0,(q,p)
 print('PASS 9 polynomial and Bezout identities; tail q>=128; 16 finite residues')

if __name__ == "__main__":
 main()
