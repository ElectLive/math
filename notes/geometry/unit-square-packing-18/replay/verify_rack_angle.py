"""Check a global rack lower-bound certificate, including all split leaves from the bare initialization."""
from pathlib import Path
from collections import defaultdict,Counter
from itertools import combinations,product
from fractions import Fraction as F
import sys,tempfile,json,time,subprocess
from check_stabs import check as check_rack,marks
from rack_lattice_input import build_rack
from angle_split_variant import extend_angle as extend
def chartrows(spec,n):
 S=marks(spec);L=F(spec['cap']);Z=len(S);gg=[[S.index((L-p[w] if a else p[w],L-p[1-w] if b else p[1-w])) for p in S] for w,a,b in product((0,1),repeat=3)]
 assert len({tuple(g) for g in gg})==8 and all(sorted(g)==list(range(Z)) for g in gg)
 whole=set(combinations(range(Z),Z-n));reps={}
 for t in sorted(whole):
  if t in reps:continue
  for g in gg:
   qt=tuple(sorted(g[i] for i in t));assert qt not in reps or reps[qt]==t;reps[qt]=t
 assert set(reps)==whole
 return sorted({(1<<Z)-1-sum(1<<i for i in t) for t in reps.values()})
def covered(paths):
 if not paths:return False
 if [] in paths:return paths==[[]]
 j,t,v=paths[0][0];a=t//2*2
 if any(p[0][0]!=j or p[0][1]//2*2!=a or p[0][2]!=v for p in paths):return False
 return all(covered([p[1:] for p in paths if p[0][1]==tt]) for tt in (a,a+1))
def verify(o,n,casefile):
 time0=time.monotonic();result=check_rack(o);assert result['status']=='STRICT_STABBING';print(result,flush=True)
 Z=len(marks(o));reps=chartrows(o,n);items=json.loads(Path(casefile).read_text(),object_pairs_hook=unique);assert set(items)=={f'{m:x}' for m in reps}
 cases=Counter();jobs=defaultdict(list)
 for m in reps:
  recipe,b=items[f'{m:x}'];nm=recipe[0];B=int(recipe[1:]);assert B in (32,64,96,128);O=[i for i in range(Z) if m>>i&1];assert len(O)==n;cases[recipe]+=1
  if nm in ('A','B'):leaves=[(b,[])]
  else:assert nm=='S' and b;leaves=b;tt=[]
  for rounds,raw in leaves:
   assert type(rounds) is int and 1<=rounds<=1000 and len(raw)%3==0
   p=[raw[i:i+3] for i in range(0,len(raw),3)]
   assert len(p)<32 and all(j in O and d in(0,1,2,3,4,5) and type(v)is int and ((1<=v<B) if d>=4 else (0<=v<=10**6*F(o['cap']))) for j,d,v in p)
   if nm=='S':tt.append(p)
   jobs[recipe].append((O,' '.join(map(str,[rounds,len(O),*O,*raw]))))
  if nm=='S':assert covered(tt),('uncovered split',m)
 print('cover',len(reps),'stages',dict(cases),'end leaves',{s:len(J) for s,J in jobs.items()},flush=True)
 with tempfile.TemporaryDirectory() as td:
  d=Path(td);sources={'A':Path('lattice_kernel.cpp'),'B':d/'pair.cc','S':d/'split.cc'}
  subprocess.run([sys.executable,'pair_variant.py',sources['A'],sources['B']],check=True);extend(sources['B'],sources['S'])
  for B in sorted({int(k[1:]) for k in jobs}):build_rack(o,B,d/f'init-{B}')
  for recipe in sorted(jobs):
   nm=recipe[0];B=int(recipe[1:])
   st=time.monotonic();exe=d/nm;subprocess.run(['g++','-std=c++17','-O3',sources[nm],'-o',exe],check=True)
   J=jobs[recipe];out=subprocess.run([exe,d/f'init-{B}'],input=''.join(s+'\n' for _,s in J),text=True,capture_output=True,check=True).stdout
   C=Counter()
   for (O,job),l in zip(J,out.splitlines(),strict=True):
    code,i,r=map(int,l.split());assert code in(1,2) and i in O and 0<=r<int(job.split()[0]),('unproved',nm,job,l);C[code]+=1
   print('stage',recipe,'all',len(J),'rejected',dict(C),'wall',round(time.monotonic()-st,3),flush=True)
 print('GLOBAL_FIXED_CAP_EXCLUDED',n,F(o['cap']),'seconds',round(time.monotonic()-time0,3),flush=True)
def unique(pairs):
 d={}
 for k,v in pairs:
  if k in d:raise ValueError('duplicate field')
  d[k]=v
 return d
if __name__=='__main__':
 if sys.flags.optimize:raise RuntimeError('assertions required')
 if len(sys.argv)!=4:raise ValueError('rack.json owner_count cases.json')
 verify(json.loads(Path(sys.argv[1]).read_text()),int(sys.argv[2]),sys.argv[3])
