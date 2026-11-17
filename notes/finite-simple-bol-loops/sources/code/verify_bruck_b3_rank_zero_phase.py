#!/usr/bin/env python3
"""Rank-zero one-shadow affine phase checks, proposed finite evidence.

Uses the immutable 22db crossed-system verifier and 84bb shear wrapper. The
full run checks 14 affine points for each of identity and second-central shear;
--probe checks the base point for identity only. No folder is constructed.
"""
import ast, contextlib, hashlib, io, multiprocessing, os, sys
from pathlib import Path
from itertools import combinations
from functools import reduce
assert __debug__
code=Path(__file__).resolve().parent
root=code.parents[2]
os.chdir(root)
expected={
 'verify_bruck_b3_affine_phase.py':'694b31e0463eab0f7e66501a18063a326dd71cc008e5fa70020620b7284f6298',
 'verify_bruck_b3_noninner_phase.py':'168e5667f86f0ef4f7979d6f782b7fb08fb8d42c37c82247bdf34fd3dc04b4dd',
 'verify_bruck_n_quadratic_support.py':'68f3d80229609d2217608c69cc203fc49176a6509f3fb5c476c3805bbe0e675d',
 'verify_bruck_one_m_noncentral.py':'59c0ed355bffdf316d93c37f99f2094acc4a09b2eff3db13459f9d208782e15a',
 'verify_bruck_p6_frattini.py':'9e42fe025aaa9dce6690badef3145da2f9a2dffb56670136fe63435b02358705',
}
for name,digest in expected.items():assert hashlib.sha256((code/name).read_bytes()).hexdigest()==digest,name
text=(code/'verify_bruck_b3_affine_phase.py').read_text()
tree=ast.parse(text)
BASE=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='SOURCES' for x in n.targets))
SOURCES=BASE.copy()
def load(name):
 ns={'__name__':'__main__','__file__':'<pinned-'+name+'>','__WORKSPACE__':str(root),'SOURCES':SOURCES,'load':load}
 exec(compile(SOURCES[name],'<pinned-'+name+'>','exec'),ns)
 return ns

def eta_source():
 s=BASE['phase']
 def rep(old,new):
  nonlocal s
  assert s.count(old)==1,(old,s.count(old));s=s.replace(old,new)
 rep('def conj(a,b):return prod(prod(a,b),inverse(a))','''def top(v):return ((v>>6)&15)^((v>>10)&15)
def eta(x):
 (v,z),g=x
 return ((v,z^(top(v)<<4)),g)
def conj(a,b):return prod(prod(eta(a),b),inverse(a))
def markprod(a,b):return prod(eta(a),b)
for g in G:
 for i in range(30):
  v=1<<i;tv,_=alpha(g,v,0)
  assert top(tv)==(actZ(top(v)<<4,g)>>4)
 for h in G:assert top(F[g,h][0])==0
for v in s['basis']:assert top(v)==0
for g in K:assert top(s['xv'][g])==0 and eta(H[g])==H[g]
assert top(1<<6)!=0
''')
 rep('prod(((0,z),t),((0,z),t))==id','markprod(((0,z),t),((0,z),t))==id')
 rep('basep=prod(prod(lam,mu),inverse(H[dd]))','basep=prod(markprod(lam,mu),inverse(H[dd]))')
 rep('cols.append(prod(prod(aa,bb),inverse(H[dd]))[0][0]^basep[0][0])','cols.append(prod(markprod(aa,bb),inverse(H[dd]))[0][0]^basep[0][0])')
 rep('pp=prod(prod(conj(p,lam),conj(q,mu)),inverse(H[dd]))','pp=prod(markprod(conj(p,lam),conj(q,mu)),inverse(H[dd]))')
 return s

os.environ['B3_Q0']='256';os.environ['B3_Q1']='0'
with contextlib.redirect_stdout(io.StringIO()):model=load('data')
terms=model['terms'];termval=model['termval'];bas=model['basis'];null=model['null'];rank=model['rank'];one=model['one'];U=model['U'];Dc=model['Dc']
assert len(terms)==19 and len(bas)==18
@__import__('functools').lru_cache(None)
def val(co,v):return reduce(int.__xor__,(termval(i,v) for i in range(19) if co>>i&1),0)
def pol(co,v,w):return val(co,v)^val(co,w)^val(co,v^w)
def feature(v):return tuple(sum(((termval(i,v)>>bit)&1)<<i for i in range(19)) for bit in range(4))
eq=[]
for v in bas+[x^y for x,y in combinations(bas,2)]:eq.extend(feature(v))
rowsR=[]
for j in range(3):
 u=U(Dc[0],j);rowsR.append(feature(one^u)[0]^feature(one)[0]^feature(u)[0])
zero=null(eq+rowsR,19);all_basis=[2,4,128,8192,16384,32768,65536]
assert len(zero)==7 and rank(zero+all_basis)==7
assert all(not ((r&256).bit_count()&1) for r in eq)
assert [int((r&256).bit_count()&1) for r in rowsR]==[1,0,0]
d=model['d'];aa=model['a'];nact=model['nact'];base=model['base']
def tact(v):
 out=d['baseact'](v&63,d['c6'])
 for j in range(3):out^=U(aa['uact']((v>>(base+8*j))&255,d['c5']),j)
 return out
piv={}
for i in range(4):
 v=(1<<i)^nact(1<<i,d['c5'])
 while v:
  j=(v&-v).bit_length()-1
  if j in piv:v^=piv[j]
  else:piv[j]=v;break
def red(v):
 for j in sorted(piv):
  if v>>j&1:v^=piv[j]
 return v
bs=[1<<i for i in range(30)];samples=bs+[x^y for x,y in combinations(bs,2)]
def dsig(co):return tuple(red(pol(co,v,tact(v))) for v in samples)
free=[2,128,8192,16384,32768,65536]
assert all(not any(dsig(x)) for x in [256]+free)
assert any(dsig(4))
print('rank-zero affine family: six free generators per component',flush=True)

def do_point(job):
 label,q0,q1=job
 os.environ['B3_Q0']=str(q0);os.environ['B3_Q1']=str(q1)
 with contextlib.redirect_stdout(io.StringIO()):ns=load('phase')
 return label,ns['rec']

for mode in ('identity','eta'):
 SOURCES['phase']=BASE['phase'] if mode=='identity' else eta_source()
 points=[('base',256,0)]
 for j,x in enumerate(free):points.extend([(f'q0_{j}',256^x,0),(f'q1_{j}',256,x)])
 both=reduce(int.__xor__,free,0);points.append(('all',256^both,both))
 if '--probe' in sys.argv:points=points[:1]
 result={}
 if '--probe' in sys.argv:stream=map(do_point,points);pool=None
 else:
  pool=multiprocessing.get_context('fork').Pool(2);stream=pool.imap(do_point,points)
 for label,rec in stream:
  if label!='base':
   assert rec['assoc_exact_matrix']==result['base']['assoc_exact_matrix'],(mode,label,'assoc_exact_matrix')
   del rec['assoc_exact_matrix']
  result[label]=rec
  assert rec['origin']==0 and rec['fphase']==0
  assert (rec['hindex'],rec['p_shadow'],rec['q_shadow'])==(8,16,1)
  assert len(rec['disp_space'])==4
  print(mode,label,'origin=0 phase=0 displacement=4',flush=True)
 if pool is not None:pool.close();pool.join()
 if '--probe' in sys.argv:break
 base_rec=result['base']
 for label,cur in result.items():
  for key in ('action_matrix','assoc_reduced_matrix','H_matrix','disp_space','Hquotient'):
   assert cur[key]==base_rec[key],(mode,label,key)
 for key in ('action_solution','assoc_solution','H_solution'):
  x=int(base_rec[key],16)
  for j in range(6):
   for i in (0,1):x^=int(result[f'q{i}_{j}'][key],16)^int(base_rec[key],16)
  assert x==int(result['all'][key],16),(mode,key)
 print(mode,'exact matrices, displacement spaces and cochain XOR agree',flush=True)
