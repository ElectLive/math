from genuine_facing_bridge import *
from verify_endpoint_orbit_window import transform
from wall_chord_guard import orient
def cap_chart(S,U):
 return {i:[(U-X,U-x,U-Y,U-y,u,v)for x,X,y,Y,u,v in st]for i,st in S.items()}
def walls(S,vrow,hrow,r,R):
 # Two orthogonal probe rows can share their real terminal (and MUST here).
 assert vrow[-1]==hrow[-1] and len(set(vrow))==len(vrow)and len(set(hrow))==len(hrow)
 T={j:S[j]for j in set(vrow+hrow)};A=orient((lambda p:p,lambda p:p),T);C=orient((lambda p:p[::-1],lambda p:p[::-1]),T);k=vrow[-1]
 if not set(vrow)<=set(A)or not set(hrow)<=set(C):return None,'axis'
 # Identical upper-right corner when original and swapped frame both choose a unique near-axis direction.
 if A[k][4]<=F(3,4)or C[k][4]<=F(3,4):return None,'axis2'
 if not all(A[i][-1][1]<A[k][-1][0]for i in vrow[:-1])or not all(C[i][-1][1]<C[k][-1][0]for i in hrow[:-1]):return None,'order'
 vL=max(A[i][0] for i in vrow);vH=min(A[i][1]for i in vrow);hL=max(C[i][0]for i in hrow);hH=min(C[i][1]for i in hrow)
 p,P,q,Q=A[k][2]
 if R is None:return A[k][2],None
 assert 0<r<=R
 lo=max(0,P-vH,(Q-hH)/r);hi=min(p-vL,(q-hL)/R)
 return (A[k][2],None)if lo<hi else(None,('probe',float(lo),float(hi)))
def cert(S,U,roles,kind='faces'):
 av,ah,bv,bh,f,g=roles
 assert all(len(p)>0 for p in (av,ah,bv,bh));G=set(av+ah+bv+bh);assert f!=g and f not in G and g not in G and not set(av+ah)&set(bv+bh)
 assert sorted((len(ah)+len(bh),len(av)+len(bv)))==[3,4]
 X=cap_chart(S,U);xx,e=walls(S,av,ah,None,None);yy,E=walls(X,bv,bh,None,None)
 if xx is None or yy is None:return False,('axes',e,E)
 pp=coords(xx);qq=[(U-x,U-y)for x,y in coords(yy)];ds=[sub(q,p)for p,q in product(pp,qq)]
 if kind=='chord':
  if not all(x>0 and y>0 for x,y in ds):return False,'direction'
  r=min(y/x for x,y in ds);R=max(y/x for x,y in ds)
 else:
  assert kind=='faces'
  F1=[astate(z)for z in S[f]];G1=[astate(z)for z in S[g]]
  if min(u[0][0]*u[1][0]for _,u,_,_ in F1+G1)<=0:return False,'cone'
  r=min(u[1][0]/u[0][1]for _,u,_,_ in F1+G1);R=max(u[1][1]/u[0][0]for _,u,_,_ in F1+G1)
 x,e=walls(S,av,ah,r,R);y,E=walls(X,bv,bh,r,R)
 if x is None or y is None:return False,('stacks',e,E)
 if kind=='chord':
  for j in (f,g):
   for x,X,y,Y,u,v in S[j]:
    cs=coords((x,X,y,Y));det=max(abs(cross(sub(q,p),sub(z,p)))for q,p,z in product(qq,pp,cs))
    for a in range(4):
     u0,u1=turnk(u,a),turnk(v,a);pairs=[(k[0]+s*w[0],k[1]+s*w[1])for k in (u0,u1)for w in [turn(k)]for s in (-1,1)]
     if min(dot(d,k)for d,k in product(ds,pairs))<=2*det:continue
     kbox=coords(bound([u0,u1]))
     if all(dot(sub(p,z),k)<F(1,2)for p,z,k in product(pp,cs,kbox)) and all(dot(sub(q,z),k)>F(-1,2)for q,z,k in product(qq,cs,kbox)):break
    else:return False,('miss',j)
  return True,'chord'
 P=((xx[0],xx[1]),(xx[2],xx[3]));Q=((U-yy[1],U-yy[0]),(U-yy[3],U-yy[2]))
 for A,K,k in ((F1,P,1),(G1,Q,-1)):
  for c,u,v,t in A:
   Z=subbox(c,K)if k==1 else subbox(K,c);forward=pd(u,Z);side=pd(v,Z)
   if forward[0]>=F(1,2):continue
   if forward[0]<=-F(1,2)or side[0]<=-F(1,2)or side[1]>=F(1,2):return False,('face',k)
 for a,u,v,t in F1:
  for b,W,V,T in G1:
   delta=subbox(b,a);al=(t[0]-T[1])/(1+t[0]*T[1]);ar=(t[1]-T[0])/(1+t[1]*T[0])
   if max(abs(s) for s in pd(v,delta)+pd(V,delta))>=1:return False,'cross'
   if min(pd(u,delta)[0],pd(W,delta)[0])<=-1:return False,'reverse'
   TR=pd(V,subbox(Q,b));TL=pd(v,subbox(a,P))
   if ar>0 and (F(1,2)+TR[0]<ar or F(1,2)-TL[1]<ar):return False,'+'
   if al<0 and (F(1,2)-TR[1]<-al or F(1,2)+TL[0]<-al):return False,'-'
 return True,'faces'
