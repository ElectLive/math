#!/usr/bin/env python3
"""Finite controls for the explicit odd prime Burnside quotient; standard-library field arithmetic, numpy array table checks."""
import itertools
import numpy as np
from sympy import symbols, cancel

class Field:
 def __init__(self,p,poly):
  self.p=p;self.poly=poly;self.d=len(poly);self.q=p**self.d
  # Low-to-high coefficients; list is the monic modulus without its leading 1.
  self.dig=[tuple((x//p**i)%p for i in range(self.d)) for x in range(self.q)]
  self.ad=np.asarray([[self.enc((i+j for i,j in zip(a,b))) for b in self.dig] for a in self.dig])
  self.mu=np.asarray([[self.times(a,b) for b in self.dig] for a in self.dig])
  assert all(tuple(sorted(row))==tuple(range(self.q)) for row in self.mu[1:])
  self.iv=[0]+[int(np.where(row==1)[0][0]) for row in self.mu[1:]]
 def enc(self,w):return sum((int(z)%self.p)*self.p**i for i,z in enumerate(w))
 def times(self,a,b):
  h=[0]*(2*self.d-1)
  for i,v in enumerate(a):
   for j,w in enumerate(b):h[i+j]+=v*w
  for k in range(len(h)-1,self.d-1,-1):
   for i,v in enumerate(self.poly):h[k-self.d+i]-=h[k]*v
  return self.enc(h[:self.d])

def run(p,poly):
 F=Field(p,poly);q=F.q;n=q*p;A=F.ad;M=F.mu;ids=np.arange(n);T=np.zeros((n,n),np.int32)
 tau=p  # polynomial t
 f=[int(A[1,M[i,tau]]) for i in range(p)];assert all(f)
 for i,j in itertools.product(range(p),repeat=2):
  # Build the table instead from the BCH class-2 coset representatives, BEFORE the fiber change.
  # C=U x W x Z, all coefficients additive; b((i,u),(j,v))=2t(iv-ju).
  # H=(0,z,z); native v-coordinate is f_i times the W-coordinate of K=(i,u,0).
  u=M[F.iv[f[i]],:][:,None];v=M[F.iv[f[j]],:][None,:]
  delta=M[tau,A[M[i,v],M[(-j)%p,u]]]
  removed=M[F.iv[f[(i+j)%p]],delta]
  w=A[A[u,v],M[p-1,removed]]
  block=M[f[(i+j)%p],w];T[i*q:(i+1)*q,j*q:(j+1)*q]=((i+j)%p)*q+block
  scalar=M[f[(i+2*j)%p],F.iv[f[i]]];formula=A[M[scalar,:][:,None],np.arange(q)[None,:]]
  assert np.array_equal(block,formula)
 assert np.array_equal(T[0],ids) and np.array_equal(T[:,0],ids)
 assert np.all(np.sort(T,axis=0)==ids[:,None]) and np.all(np.sort(T,axis=1)==ids[None,:])
 # Compare whole native permutations; this evaluates every ordinary triple.
 for x in range(n):
  inner=T[x,T[:,x]]
  v=T[x,T[:,T[x]]];assert np.array_equal(v,T[inner])
  k=ids.copy()
  for _ in range(p):k=T[x,k]
  assert np.array_equal(k,ids)
 S=np.array([0,1,q])
 while True:
  new=np.unique(T[S[:,None],S[None,:]])
  if len(new)==len(S):break
  S=new
 assert len(S)==n
 # Wrong-hand product and inflation to the full root extension are measured on actual points.
 U=T[T[:,q],(p-1)*q];assert U[0]==0 and U[1]!=1
 c=0;v=1
 while True:
  v=U[v];c+=1
  if v==1:break
 assert c>1 and (q-1)%c==0
 # The two left translations at b and z generate exactly p^3 in every finite example,
 # never the full (size-unbounded) native loop merely by acting on the origin.
 g=[T[1],T[q]];todo=[ids];seen={tuple(ids)}
 for v in todo:
  for x in g:
   w=x[v];key=tuple(w)
   if key not in seen:seen.add(key);todo.append(w)
 assert len(todo)==p**3
 print('F_%s^%s'%(p,F.d),'native loop order',n,'literal left Bol triples',n**3,'products from only b,z generate',len(S),'wrong-hand product order on (0,1)',c,'subgroup of the two matched left translations',len(todo),flush=True)

if __name__=='__main__':
 i,j,t=symbols('i j t')
 a=lambda i:2*t/(1+i*t)
 assert cancel(a(2*i+j)*(2+(i+j)*a(i))-2*a(i))==0
 assert cancel(a(2*i+j)*(1+i*a(j))-a(j))==0
 for p,h in [(3,[1,0]),(3,[1,2,0]),(3,[2,1,0,0]),(5,[2,0]),(7,[1,0])]:run(p,h)
 print('PASS: separate class-two coset construction and direct native-table tests; not an independent review.')
