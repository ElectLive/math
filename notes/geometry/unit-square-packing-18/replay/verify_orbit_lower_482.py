"""Fresh fixed-cap 18 proof. All selected orbits and every emitted leaf are verified here."""
import sys,time,json,subprocess,tempfile,hashlib
from fractions import Fraction as F
from itertools import combinations_with_replacement
from pathlib import Path
from collections import defaultdict,Counter
from verify_arc_lower import build,certified_init
from verify_rack_angle import check_rack,chartrows,marks,covered,unique
from faithful_endpoint_mask_482 import jobs as minimum_jobs
def mirror(o,O,P,g,B):
 sw,rx,ry=g;U=F(o['cap']);R=marks(o)
 h=[R.index((U-z[sw]if rx else z[sw],U-z[1-sw]if ry else z[1-sw]))for z in R]
 assert sorted(h)==list(range(len(R))) and {h[j]for j in O}==set(O) and all(h[h[j]]==j for j in O)
 out=[];M=int(U*10**6);assert F(M,10**6)==U
 for i,t,v in zip(P[0::3],P[1::3],P[2::3]):
  if t<4:
   axis=(t//2)^sw;sg=(rx,ry)[axis];out.extend([h[i],2*axis+((t%2)^sg),M-v if sg else v]);continue
  assert sw^rx^ry
  # Under a reflected chart the closed threshold q/B becomes (B-q)/(B+q).
  # Retain every ORIGINAL band with even endpoint-only intersection.
  a=9-t;z=F(B*(B-v),B+v)
  val=-((-z.numerator)//z.denominator)-1 if a==5 else z.numerator//z.denominator+1
  if not 0<val<B:continue
  out.extend([h[i],a,val])
 return out
def make(o,D):
 J=defaultdict(list);R=chartrows(o,18);missing=[];assert set(D)=={format(m,'x')for m in R}
 for i,m in enumerate(R):
  O=[j for j in range(21)if m>>j&1];B,leaves=D[format(m,'x')];assert B in (32,64,96,128)
  paths=[p for p,r,a in leaves];assert covered([[p[h:h+3]for h in range(0,len(p),3)]for p in paths])
  def add(p,r,a):
   assert a in (0,1)and len(r)==4 and 1<=r[0]<=1000 and 2<=r[1]<=64 and 4<=r[2]<=1024 and 1<=r[-1]<=1000
   assert len(p)%3==0 and all(type(x)is int for x in [*p,*r])
   assert all(z in O and t in range(6)and (0<v<B if t>=4 else 0<=v<=4820000)for z,t,v in zip(p[0::3],p[1::3],p[2::3]))
   J[B,a].append((i,O,r,' '.join(map(str,[*r,18,*O,*p]))))
  if i==53:
   O2,T=minimum_jobs(o);assert B==128 and O==O2
   for r,p in T:add(p,r,1)
   continue
  if i==55:
   assert B==128 and paths==[[]]
   edges=[None,2240000,2255000,2270000,2285000,2300000,*range(2320000,2440001,20000),None]
   for a,b in zip(edges,edges[1:]):add(([9,1,a]if a else [])+([9,0,b]if b else []),([210,8,896,130]if a and a>=2300000 else [220,8,896,105]),1)
   continue
  active={82:[0,4,5],92:[1,2]}.get(i,[])
  for j,(p,r,a)in enumerate(leaves):
   if j in active:continue
   if (i,j)in [(92,0),(137,0)]:
    expected={92:[12,1,2909035],137:[12,1,2909031]};assert B==128 and p==expected[i]
    missing.append((i,j));continue
   if (i,j)==(115,8):r,a=[230,8,896,140],1
   add(p,r,a)
  if active:
   assert B==128
   g=(1,0,0)if i==82 else (0,0,1)
   for a,b in combinations_with_replacement(active,2):
    r=[230,8,896,140]if (i,a,b)in [(82,0,5),(92,2,2)]else [185,8,768,105]
    add(paths[a]+mirror(o,O,paths[b],g,B),r,1)
 assert missing==[(92,0),(137,0)];return J
def main():
 if sys.flags.optimize:raise RuntimeError('assertions required')
 import argparse,concurrent.futures
 ap=argparse.ArgumentParser();ap.add_argument("--workers",type=int,default=1);w=ap.parse_args().workers;assert 1<=w<=32
 t=time.monotonic()
 o=json.loads(Path('stabs18-482.json').read_text(),object_pairs_hook=unique);assert F(o['cap'])==F(241,50)and o['marks']==21 and check_rack(o)['status']=='STRICT_STABBING'
 J=make(o,json.loads(Path('n18-482-base.json').read_text(),object_pairs_hook=unique));print('all 187 mask orbits, split/paired/reflected/minimum channel:',[(k,len(v))for k,v in sorted(J.items())],'+ 2 direct wall-pair rows',flush=True)
 # This extra routine independently constructs the same rack from the prior *coordinates*, at the NEW cap.
 old=json.loads(Path('stabs18-4815.json').read_text());old['cap']='4.82';assert old==o
 from wall_pair_terminal import run as wall
 wall()
 with tempfile.TemporaryDirectory()as td:
  d=Path(td);build(d)
  for (b,mode),rows in sorted(J.items()):
   p=d/f'i{b}';st=time.monotonic()
   if not p.exists():certified_init(o,b,p)
   # Independent fresh jobs: concatenate deterministically in frozen order,
   # whether one process or several are requested. No subset flag is exposed.
   def exec_chunk(chunk):
    return subprocess.check_output([d/f'verify{mode}',p],input=''.join(line+'\n'for i,O,r,line in chunk),text=True)
   chunks=[rows[j:j+max(1,len(rows)//(4*w))] for j in range(0,len(rows),max(1,len(rows)//(4*w)))]
   with concurrent.futures.ThreadPoolExecutor(w)as pool:out=''.join(pool.map(exec_chunk,chunks))
   rates=Counter()
   for (i,O,r,job),l in zip(rows,out.splitlines(),strict=True):
    stage,rc,who,it,bb=l.split();assert stage in ('C','F')and int(rc)in (1,2)and int(who)in O and 0<=int(it)<(r[0]if stage=='C'else r[3])and(int(bb)==b if stage=='C'else 2<=int(bb)<=r[2]),('unclosed',i,job,l)
    rates[stage,rc]+=1
   print(b,mode,len(rows),sorted(rates.items()),hashlib.sha256(out.encode()).hexdigest(),round(time.monotonic()-st,3),flush=True)
 print('GLOBAL_FIXED_CAP_EXCLUDED 18 241/50',round(time.monotonic()-t,3),flush=True)
if __name__=='__main__':main()
