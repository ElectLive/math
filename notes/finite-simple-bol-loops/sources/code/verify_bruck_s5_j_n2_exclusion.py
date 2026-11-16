#!/usr/bin/env python3
"""Finite J+N² outer-class collision certificate; see linked manuscript.

Permutations c,d are copied from Nagy arXiv:0709.4544v1 Lemma 3.2;
this program does not independently establish that source or J-branch premises.
"""
assert __debug__, "Run with assertions enabled"
c6=(1,0,3,2,5,4);d6=(0,2,3,4,1,5)
c5=(1,0,2,3,4);d5=(0,2,3,4,1)
def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
def parity(p): return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2
def jact(v,p):
 z=0
 for i in range(5):
  if v>>i&1:z^=1<<p[i]
 return (z^63 if z&32 else z)&31
def nact(v,p):
 z=0
 for i in range(4):
  if v>>i&1:z^=(1<<p[0])^(1<<p[i+1])
 return (z>>1)&15
def action(v,p6,p5):
 j=jact(v&31,p6); x=nact((v>>5)&15,p5); y=nact(v>>9,p5)
 return j|(x<<5)|(y<<9)
def powp(p,n):
 r=tuple(range(len(p)))
 for _ in range(n):r=compose(r,p)
 return r
pairs={(tuple(range(6)),tuple(range(5)))}; queue=list(pairs)
for a,b in queue:
 for aa,bb in ((c6,c5),(d6,d5)):
  h=(compose(a,aa),compose(b,bb))
  if h not in pairs:pairs.add(h);queue.append(h)
assert len(pairs)==120 and len({g[0] for g in queue})==120 and len({g[1] for g in queue})==120
for g in queue:
 for h in ((c6,c5),(d6,d5)):
  gh=(compose(g[0],h[0]),compose(g[1],h[1]))
  assert all(action(action(1<<i,*h),*g)==action(1<<i,*gh) for i in range(13))
p=(compose(c6,d6),compose(c5,d5));assert powp(p[0],5)==tuple(range(6))
def pinv(x):return tuple(x.index(i) for i in range(len(x)))
normal=[g for g in queue if compose(compose(g[1],p[1]),pinv(g[1])) in [powp(p[1],k) for k in range(1,5)]]
assert len(normal)==20
def span(values):
 s={0}
 for v in values:s|={v^x for x in s.copy()}
 return s
def forbit(x):return {action(x,*g) for g in normal}
def fspan(x):return span(forbit(x))
L={v for v in range(32) if action(v,*p)==v};assert len(L)==2
J0={v^action(v,*p) for v in range(32)};assert len(J0)==16
soc={x<<5 for x in range(16)}
T=soc
assert all((v&31)==0 for v in T)
# Equivariant isomorphism S_J -> T: a nonzero image fixes the map.
x=next(v for v in J0 if v);mapping=None
for target in sorted(T-{0}):
 candidates={0:0};valid=True
 for g in normal:
  a=action(x,*g);b=action(target,*g)
  if a in candidates:
   if candidates[a]!=b:valid=False;break
  else:
   for k,v in list(candidates.items()):candidates[k^a]=v^b
 if valid and set(candidates)==J0 and len(set(candidates.values()))==16:
  mapping=candidates;break
assert mapping
assert all(mapping[action(v,*g)]==action(mapping[v],*g) for v in J0 for g in normal)
W1={l^v^mapping[v] for l in L for v in J0};assert len(W1)==32
assert all(action(w,*g) in W1 for w in W1 for g in normal)
assert all(mapping[x^y]==mapping[x]^mapping[y] for x in J0 for y in J0)

Ct={v for v in range(8192) if action(v,c6,c5)==v}; Bt={v^action(v,c6,c5) for v in range(8192)}
assert (len(Ct),len(Bt),len(W1&Ct),len(W1&Bt))==(512,16,4,1)
def cyc(n,s):
 z=list(range(n))
 for a in s:
  for i,x in enumerate(a):z[x-1]=a[(i+1)%len(a)]-1
 return tuple(z)
def invp(x):return tuple(x.index(i) for i in range(len(x)))
def conj(x,g):return compose(compose(g,x),invp(g))
c=cyc(40,[(1,4),(2,9),(3,10),(6,11),(7,12),(13,21),(14,22),(15,24),(16,23),(17,30),(18,29),(19,31),(20,32),(33,35),(38,40)])
d=cyc(40,[(1,2,4,6,8,7,5,3),(9,13,25,18,10,14,26,17),(11,15,27,20,12,16,28,19),(21,30,38,34,23,31,40,35),(22,32,39,36,24,29,37,33)])
id40=tuple(range(40));id5=tuple(range(5));id6=tuple(range(6))
E={id40:(id6,id5)}; words={id40:""}; todo=[id40]
for x in todo:
 a,b=E[x]
 for z,r,s,letter in ((c,c6,c5,"c"),(d,d6,d5,"d")):
  y=compose(x,z);h=(compose(a,r),compose(b,s))
  if y not in E:E[y]=h;words[y]=words[x]+letter;todo.append(y)
  else:assert E[y]==h
assert len(E)==3840
P=compose(c,d); assert powp(P,5)==id40
H0=[g for g in todo if conj(P,g) in {powp(P,i) for i in range(1,5)}];assert len(H0)==40
u1=powp(d,4);u2=conj(u1,c);u3=conj(u2,d);u4=conj(u3,c);u5=conj(u4,d);u=[u1,u2,u3,u4,u5]
jvec=[]
for v in range(32):
 z=id40
 for i in range(5):
  if v>>i&1:z=compose(z,u[i])
 jvec.append(z)
assert len(set(jvec))==32
# Check action conventions of J model against conjugation by E generators.
for i in range(5):
 for g,pg in ((c,c6),(d,d6)):
  assert conj(jvec[1<<i],g)==jvec[jact(1<<i,pg)]

# In G=U⋊E, pairs are (E permutation, 8-bit U vector).
def nu(v,p):return nact(v&15,p)|(nact(v>>4,p)<<4)
def mul(a,b):
 e,x=a;f,y=b
 return compose(e,f),x^nu(y,E[e][1])
def inverse(a):
 e,x=a;f=invp(e);return f,nu(x,E[f][1])
Id=(id40,0);gens=[(c,0),(d,0)]+[(id40,1<<i) for i in range(8)]
def classorb(x):
 seen={x};q=[x]
 for v in q:
  for g in gens:
   y=mul(mul(g,v),inverse(g))
   if y not in seen:seen.add(y);q.append(y)
 return seen
fixed=[u for u in range(256) if nu(u,c5)==u]
classes=[];remaining={(c,u) for u in fixed}
while remaining:
 a=min(remaining);orb=classorb(a);remaining.difference_update(orb);classes.append((a,orb))
assert len(classes)==6 and sorted(len(o) for a,o in classes)==[320]+[960]*5
# All involutions above the designated transposition, including every J lift.
all_lifts={(e,u) for e in E if E[e][1]==c5 and compose(e,e)==id40 for u in fixed}
assert len(all_lifts)==512
assert all_lifts<=set().union(*(orb for _,orb in classes))
assert all(len({x for x in orb if E[x[0]][1]==c5})==len(orb)//10 for _,orb in classes)
print('outer G-class sizes',sorted(len(o) for a,o in classes))
H={(compose(jvec[w&31],h),w>>5) for w in W1 for h in H0};assert len(H)==640
assert Id in H and all(mul(x,inverse(x))==Id for x in H)
hgens=[(h,0) for h in H0]+[(jvec[w&31],w>>5) for w in W1]
assert all(mul(h,g) in H for h in H for g in hgens)
base=next(o for a,o in classes if a==(c,0));others=[(a,o) for a,o in classes if a!=(c,0)]
print('base size',len(base),'extra representatives',[(a[1],len(o)) for a,o in others],flush=True)
base_witness=None
for k in sorted(base):
 for h in sorted(H):
  if h!=Id and mul(k,h) in base:
   base_witness=(k,h,mul(k,h));break
 if base_witness:break
assert base_witness is not None
k,h,v=base_witness
print('base collision E-words/U:', (words[k[0]],k[1]), (words[h[0]],h[1]), (words[v[0]],v[1]))
for a,o in others:
 K=base|o; assert len(K)==1280
 collision=None
 for k in sorted(K):
  for h in sorted(H):
   if h==Id:continue
   v=mul(k,h)
   if v in K:collision=(k,h,v);break
  if collision:break
 assert collision is not None
 k,h,v=collision
 assert h in H and h!=Id and k in K and v in K and mul(k,h)==v and k!=v
 print('extra',a[1], 'witness E-words/U:', (words[k[0]],k[1]), (words[h[0]],h[1]), (words[v[0]],v[1]), 'base-membership', (k in base,v in base))
print('all five outer choices violate transversality')
