from fractions import Fraction as F
from itertools import product
from pathlib import Path

import sys
D=10**6
def vb(k,B):
 t=F(k,B);return (1-t*t)/(1+t*t),2*t/(1+t*t)
def make(D0):
 S={}
 for j,(_,cs,_) in D0.items():
  L=[]
  for k,P in enumerate(cs):
   if not P:continue
   A=vb(k,len(cs));B=vb(k+1,len(cs));p=[(F(x,D),F(y,D)) for x,y in P];L.append((min(x for x,y in p),max(x for x,y in p),min(y for x,y in p),max(y for x,y in p),A,B))
  S[j]=L
 return S
def sign(a):return 1 if a>=0 else -1
def coords(h):x,X,y,Y=h;return list(product((x,X),(y,Y)))
def bound(p):return min(x for x,y in p),max(x for x,y in p),min(y for x,y in p),max(y for x,y in p)
def turn(u):return -u[1],u[0]
def turnk(u,n):
 for i in range(n):u=turn(u)
 return u
def dot(p,q):return p[0]*q[0]+p[1]*q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def cross(x,y):return x[0]*y[1]-x[1]*y[0]
def orient(c,S): # upper-right tip & row probe regions in local frame with its walls bottom/left 
 R={}
 for j in S:
  B=[];tips=[];ts=[];cc=[];C=[]
  for x,X,y,Y,A,A1 in S[j]:
   A,A1=c[1](A),c[1](A1)
   box=bound([c[0](p) for p in coords((x,X,y,Y))])
   opts=[(turnk(A,k),turnk(A1,k))for k in range(4)]
   v,w=max(opts,key=lambda z:min(z[0][0],z[1][0]))
   if min(v[0],w[0])<=F(7,10):break
   lx,hx,ly,hy=box;lo=min(v[0],w[0]);hi=max(v[0],w[0]);s=min(v[1],w[1]);S1=max(v[1],w[1]);a=max(abs(s),abs(S1))
   B.append((hx-(lo-a)/2,lx+(lo-a)/2));ts.append(a);cc.append(lo);C.append((ly-a/lo,hy+a/lo))
   tips+=list(coords((lx+(lo-S1)/2,hx+(hi-s)/2,ly+(lo+s)/2,hy+(hi+S1)/2)))
  else:R[j]=(max(l for l,h in B),min(h for l,h in B),bound(tips),max(ts),min(cc),(min(l for l,h in C),max(h for l,h in C)))
 return R
def stack(R,S,rl,rh):
 l=max(R[j][0]for j in S);h=min(R[j][1]for j in S);z=R[S[-1]];p,P,_,_=z[2];t,c=z[3:5];eper=t/(1+c)
 l=max(l,P-(1-eper)*c/rh);h=min(h,p-eper/rl)
 return l<h and all(R[j][-1][1]<z[-1][0]for j in S[:-1]),(l,h)
def guard(S,L,ids,verbose=False):
 if len(ids)!=7 or len(set(ids))!=7:raise ValueError('seven distinct physical owners required')
 p0,p1,ip,q0,iq,f,g=ids;A=orient((lambda p:p,lambda p:p),S);C=orient((lambda p:(L-p[1],L-p[0]),lambda v:(-v[1],-v[0])),S)
 if not set([p0,p1,ip])<=A.keys() or not set([q0,iq])<=C.keys():return False,'axis'
 pp=coords(A[ip][2]);qq=[(L-y,L-x) for x,y in coords(C[iq][2])]
 ds=[sub(q,p)for p,q in product(pp,qq)]
 if not all(x>0 and y>0 for x,y in ds):return False,'direction'
 rl=min(y/x for x,y in ds);rh=max(y/x for x,y in ds)
 a,ab=stack(A,(p0,p1,ip),rl,rh);b,bb=stack(C,(q0,iq),1/rh,1/rl)
 if not (a and b):return False,('stacks',a,b,[float(z)for z in (rl,rh)])
 for j in (f,g):
  for x,X,y,Y,u,v in S[j]:
   cs=coords((x,X,y,Y));det=max(abs(cross(sub(q,p),sub(z,p))) for q,p,z in product(qq,pp,cs))
   for a in range(4):
    u0,u1=turnk(u,a),turnk(v,a);pairs=[(k[0]+s*w[0],k[1]+s*w[1]) for k in (u0,u1) for w in [turn(k)] for s in (-1,1)]
    low=min(dot(d,k) for d,k in product(ds,pairs))
    if low<=2*det:continue
    kbox=coords(bound([u0,u1]))
    if all(dot(sub(p,z),k)<F(1,2)for p,z,k in product(pp,cs,kbox)) and all(dot(sub(q,z),k)>F(-1,2)for q,z,k in product(qq,cs,kbox)):break
   else:return False,('miss',j,float(det),float(low))
 return True,([float(z)for z in ab],[float(z)for z in bb])
