from wall_chord_guard import *
from six_tilt_guard import enclosure
from six_tilt18 import load
def add(A,B):return A[0]+B[0],A[1]+B[1]
def neg(A):return -A[1],-A[0]
def dif(A,B):return add(A,neg(B))
def mul(A,B):x=[i*j for i in A for j in B];return min(x),max(x)
def pd(U,V):return add(mul(U[0],V[0]),mul(U[1],V[1]))
def subbox(A,B):return (dif(A[0],B[0]),dif(A[1],B[1]))
def astate(x):
 l,h,y,Y,u,w=x;ax=(tuple(sorted([u[0],w[0]])),tuple(sorted([u[1],w[1]])));v=(neg(ax[1]),ax[0]);t=tuple(sorted([z[1]/(1+z[0]) for z in (u,w)]))
 return ((l,h),(y,Y)),ax,v,t
def lagrange(S,L,ids):
 p0,p1,ip,q0,iq,f,g=ids;A=orient((lambda p:p,lambda p:p),S);C=orient((lambda p:(L-p[1],L-p[0]),lambda u:(-u[1],-u[0])),S)
 if not set(ids[:3])<=set(A)or not set(ids[3:5])<=set(C):return False,'angle'
 P=tuple(zip(*[(A[ip][2][0],A[ip][2][2]),(A[ip][2][1],A[ip][2][3])]))
 Q=tuple(zip(*[(L-C[iq][2][3],L-C[iq][2][1]),(L-C[iq][2][2],L-C[iq][2][0])]))
 F1=[astate(x)for x in S[f]];G=[astate(x)for x in S[g]]
 if min(ax[0][0]*ax[1][0]for z,ax,v,t in F1+G)<=0:return False,'cone'
 r=min(ax[1][0]/ax[0][1]for z,ax,v,t in F1+G);R=max(ax[1][1]/ax[0][0]for z,ax,v,t in F1+G)
 if not stack(A,ids[:3],r,R)[0]or not stack(C,ids[3:5],1/R,1/r)[0]:return False,'stacks'
 for X,K,k in ((F1,P,1),(G,Q,-1)):
  for c,u,v,t in X:
   Z=subbox(c,K) if k==1 else subbox(K,c);forward=pd(u,Z);side=pd(v,Z)
   if forward[0] >= F(1,2):continue
   if forward[0]<=-F(1,2)or side[0]<=-F(1,2)or side[1]>=F(1,2):return False,('face',k,side)
 for a,u,v,t in F1:
  for b,U,V,T in G:
   delta=subbox(b,a)
   al=(t[0]-T[1])/(1+t[0]*T[1]);ar=(t[1]-T[0])/(1+t[1]*T[0])
   if max(abs(s) for s in pd(v,delta)+pd(V,delta))>=1:return False,'cross' # each true transverse support >=1
   if min(pd(u,delta)[0],pd(U,delta)[0])<=-1:return False,'reverse'
   TR=pd(V,subbox(Q,b));TL=pd(v,subbox(a,P))
   if ar>0 and (F(1,2)+TR[0]<ar or F(1,2)-TL[1]<ar):return False,'+'
   if al<0 and (F(1,2)-TR[1]<-al or F(1,2)+TL[0]<-al):return False,'-'
 return True,'facing'
def fixture(e):
 H,P,u=load();S={};l,h=enclosure(H)
 for i,(t,p)in P.items():
  x,X=enclosure(p[0]);y,Y=enclosure(p[1]);S[i]=[(x-e,X+e,y-e,Y+e,vb(k,128),vb(k+1,128))for k in ([26,27,28,29]if t else [0,1,126,127])]
 return S,h,[2,4,1,18,13,5,11]
if __name__=='__main__':
 if __import__('sys').flags.optimize:raise RuntimeError('assertions required')
 S,h,ids=fixture(F(1,10))
 assert lagrange(S,h,ids)==(True,'facing') and not guard(S,h,ids)[0]
 print('PASS exact six-tilt H layout enclosed; all seven centers independently padded by 1/10 in each coordinate, two independent tilted angles, five independent wall angles; face bridge proves H, raw straight traversal test inconclusive.')
