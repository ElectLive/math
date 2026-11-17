#!/usr/bin/env python3
"""Classify a conditional finite cover of fixed-free two-M S5 modules.

Python 3.11+, assertions required. This computes 48 extension classes and
counts 7,994 support-subspace pairs; it does not construct those 7,994 modules
or classify loop envelopes. See bruck-s5-two-m-cover.md for dependencies.
"""
import runpy,contextlib,io,sys,collections,argparse
from pathlib import Path
assert __debug__, 'Run with assertions enabled'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--representatives',action='store_true',help='print generator columns and labels for the ten candidates')
args=parser.parse_args()
root=Path(__file__).resolve().parent

def import_checked(name):
 path=root/name
 old_argv=sys.argv[:]
 try:
  sys.argv=[str(path)]
  with contextlib.redirect_stdout(io.StringIO()):
   return runpy.run_path(str(path))
 finally:
  sys.argv=old_argv

src=import_checked('classify_bruck_s5_principal_isotypes.py')
d=src['d'];clusters=src['clusters']; assert len(clusters)==17
apply,mul,inv,add,nullspace,hom,tensor=(d[k] for k in ('apply','mul','inv','add','nullspace','hom_basis','tensor_action'))
J=d['getq']('J'); one=((1,),(1,)); R=((2,1),(2,1))
def direct(X,Y):
 n=len(X[0]);return tuple(tuple(A)+tuple(v<<n for v in B) for A,B in zip(X,Y))
def fixed(X):return len(hom(one,X))
Zs=[]
for i,group in enumerate(clusters):
 X=group[0][1]
 for tail in (None,one,R):
  Z=X if tail is None else direct(X,tail)
  if fixed(Z)<=1:Zs.append((i,0 if tail is None else len(tail[0]),Z))
assert len(Zs)==20
print('one-M isotypes 17; eligible Z presentations:',len(Zs),flush=True)

def cocycles(Q,A):
 n=len(Q[0]);k=len(A[0]);dim=n*k
 hc=tensor(A[0],inv(Q[0]),k,n);hd=tensor(A[1],inv(Q[1]),k,n)
 qi=tuple(1<<i for i in range(n));ai=tuple(1<<i for i in range(k));hi=tuple(1<<i for i in range(dim));ident=(qi,ai)
 seen={ident:(hi,(0,)*(2*dim))};queue=[ident];rows=[]
 for pair in queue:
  hg,f=seen[pair]
  for j in range(2):
   target=mul(pair[0],Q[j]),mul(pair[1],A[j]);hh=mul(hg,(hc,hd)[j])
   vals=tuple(f[i]^(hg[i-j*dim] if j*dim<=i<(j+1)*dim else 0) for i in range(2*dim))
   if target not in seen:seen[target]=(hh,vals);queue.append(target)
   else:
    assert hh==seen[target][0]
    diffs=[x^y for x,y in zip(vals,seen[target][1])]
    rows += [sum(((v>>bit)&1)<<i for i,v in enumerate(diffs)) for bit in range(dim)]
 assert len(seen)==120
 Z=nullspace(rows,2*dim);B={}
 for i in range(dim):
  v=(hc[i]^(1<<i))|((hd[i]^(1<<i))<<dim)
  assert all((row&v).bit_count()%2==0 for row in rows)
  add(B,v)
 reps=[]
 for v in Z:
  if add(B,v):reps.append(v)
 return reps,dim
stats=collections.Counter()
for i,tail,Z in Zs:
 reps,k=cocycles(Z,J);stats[(len(Z[0]),tail,len(reps),fixed(Z))]+=1
 pass
assert sum((1<<k[2])*v for k,v in stats.items())==48
def extension(Q,A,f,k):
 n=len(Q); m=len(A); cols=list(A)
 for j in range(n):
  y=apply(Q,1<<j);v=0
  for i in range(m):
   if ((f>>(i*n)) & ((1<<n)-1) & y).bit_count()%2:v^=1<<i
  cols.append(v|(y<<m))
 return tuple(cols)
def gf2rank(cols):
 B={}
 for x in cols:add(B,x)
 return len(B)
def is_idempotent_free(Q,B):
 n=len(Q[0]);ident=tuple(1<<i for i in range(n));zero=(0,)*n
 v=[0]*n;last=0
 for i in range(1,1<<len(B)):
  gray=i^(i>>1); bit=(gray^last).bit_length()-1;last=gray
  v=[x^y for x,y in zip(v,B[bit])]
  if tuple(v)!=ident and mul(v,v)==tuple(v):return False
 return True
summary=collections.Counter();totalclasses=0;examples=[];allfixed=[]
for i,tail,Z in Zs:
 reps,k=cocycles(Z,J)
 for mask in range(1<<len(reps)):
  f=0
  for j,v in enumerate(reps):
   if mask>>j&1:f^=v
  q=tuple(extension(Z[j],J[j],(f>>(j*k))&((1<<k)-1),k) for j in range(2))
  # All four S5 presentation relators checked on every extension.
  c,dd=q;ident=tuple(1<<n for n in range(len(c)))
  comm=mul(mul(mul(inv(c),inv(dd)),c),dd)
  assert all(d['power'](a,n)==ident for a,n in ((c,2),(dd,4),(mul(c,dd),5),(comm,3)))
  totalclasses+=1
  if fixed(q):continue
  allfixed.append(((i,tail,mask,len(q[0])),q))
  end=hom(q,q);dim=len(end)
  assert dim<=16, 'endomorphism space exceeds exhaustive limit'
  indec=is_idempotent_free(q,end)
  summary[(len(q[0]),dim,indec)]+=1
  if indec:examples.append((i,tail,mask,len(q[0]),dim))
assert totalclasses==48 and len(allfixed)==12
assert len(examples)==5 and sorted(x[3] for x in examples)==[10,10,11,11,12]
assert max(key[1] for key in summary)==4
print('extension classes 48; fixed-free representatives 12; indecomposable representatives 5',flush=True)
# Q with no trivial factors is separately M².

clusters2=[]; maxhom=0
for label,Q in allfixed:
 for cluster in clusters2:
  target=cluster[0][1]
  if len(Q[0])!=len(target[0]):continue
  B=hom(Q,target);maxhom=max(maxhom,len(B))
  assert len(B)<=18, 'isomorphism space exceeds exhaustive limit'
  iso=src['invertible_combination'](B,len(Q[0]))
  if iso is not None:
   assert all(mul(iso,a)==mul(b,iso) for a,b in zip(Q,target))
   cluster.append((label,Q));break
 else:clusters2.append([(label,Q)])
assert len(clusters2)==9 and maxhom==3
indecomp_labels={tuple(x[:4]) for x in examples}
indecomp_clusters=[cl for cl in clusters2 if tuple(cl[0][0]) in indecomp_labels]
assert len(indecomp_clusters)==4 and sorted(len(cl[0][1][0]) for cl in indecomp_clusters)==[10,10,11,12]
assert all((tuple(label) in indecomp_labels)==(cl in indecomp_clusters) for cl in clusters2 for label,_ in cl)
print('fixed-free isotypes containing J: 9; indecomposable isotypes: 4; maximum dimension: 12',flush=True)
control=import_checked('verify_bruck_s5_two_m10.py')
known=control['Q']; matches=[]
for i,cluster in enumerate(clusters2):
 Q=cluster[0][1]
 if len(Q[0])!=10:continue
 B=hom(Q,known)
 assert len(B)<=18, 'control isomorphism space exceeds exhaustive limit'
 iso=src['invertible_combination'](B,10)
 if iso is not None:
  assert all(mul(iso,a)==mul(b,iso) for a,b in zip(Q,known))
  matches.append(i)
print('known 10D witness matches fixedfree clusters',matches,flush=True)
assert len(matches)==1
principal=import_checked('verify_s5_principal_h1_bounds.py')
dual=principal['dual'];h1=principal['h1'];power=principal['power']
M=d['getq']('M'); m2=direct(M,M)
fixedfree=[('M2',m2)]+[(f'cluster{i}',cluster[0][1]) for i,cluster in enumerate(clusters2)]

def choose2(n,k):
 out=1
 for i in range(k):out=out*((1<<n)-(1<<i))//1
 den=1
 for i in range(k):den*=((1<<k)-(1<<i))
 assert out%den==0
 return out//den

def subspace_count(n):return sum(choose2(n,k) for k in range(n+1))
assert fixed(m2)==0 and all(len(cl[0][1][0])>len(m2[0]) for cl in clusters2)
print('fixed-free isotypes including M²: 10',flush=True)
max_e1=max_eR=0;total=0;largest=0;cohom_rows=[]
for label,Q in fixedfree:
 a,b=map(dual,Q);comm=mul(mul(mul(inv(a),inv(b)),a),b)
 e1=h1(a,b,120)[2];eR=h1(power(b,2),comm,60)[2]
 max_e1=max(max_e1,e1);max_eR=max(max_eR,eR)
 count=subspace_count(e1)*subspace_count(eR); total+=count
 bound=len(Q[0])+e1+2*eR;largest=max(largest,bound)
 cohom_rows.append((len(Q[0]),e1,eR,count,bound))
expected=[(8,2,4,335,18),(9,3,4,1072,20),(10,2,4,335,20),
          (10,1,2,10,15),(10,4,4,4489,22),(10,2,4,335,20),
          (11,3,4,1072,22),(11,2,1,10,15),(12,2,4,335,22),(12,0,0,1,12)]
assert cohom_rows==expected and total==7994 and max_e1==max_eR==4 and largest==22
print('support cohomology rows:',cohom_rows,flush=True)
print('support subspace pairs:',total,'maximum supported dimension:',largest,flush=True)
if args.representatives:
 for label,Q in fixedfree:
  print('representative',label,'columns c=',Q[0],'d=',Q[1],flush=True)
 for i,cl in enumerate(clusters2):
  print('cluster',i,'extension labels',[label for label,_ in cl],flush=True)
