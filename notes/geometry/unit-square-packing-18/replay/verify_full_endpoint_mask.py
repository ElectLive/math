"""Fresh all-pose certificate of exact minimum H in one full unmarked D4 mask class."""
from verify_endpoint_orbit_window import transform,IDS
from verify_rack_angle import covered,unique,check_rack,chartrows,marks
from inhabited_endpoint import parsed,worker,certified_init
from endpoint_rack_gap import classify,eight
from six_tilt18 import load,q
from wall_chord_guard import guard
from genuine_facing_bridge import lagrange
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
import json,sys,time,tempfile,argparse,subprocess,hashlib
def run():
 if sys.flags.optimize:raise RuntimeError('assertions required')
 ap=argparse.ArgumentParser();ap.add_argument('--workers',default=1,type=int);w=ap.parse_args().workers;assert 1<=w<=32
 started=time.monotonic();o=json.loads(Path('stabs18-endpoint-window.json').read_text(),object_pairs_hook=unique);U=F(o['cap']);M=4822876;assert U==F(M,10**6)and check_rack(o)['status']=='STRICT_STABBING'
 R=marks(o);m=chartrows(o,18)[53];O=[j for j in range(21)if m>>j&1];assert m==2030575
 sy=set();gg=set()
 for g in product((0,1),repeat=3):
  sw,sx,sy0=g;h=[R.index((U-z[sw]if sx else z[sw],U-z[1-sw]if sy0 else z[1-sw]))for z in R]
  if {h[i]for i in O}==set(O):
   assert all(h[h[j]]==j for j in O);gg.add(g);sy.add((h[5],1-sw,sy0))
 assert sy=={(5,1,0),(15,0,0),(5,0,1),(15,1,1)} and len(gg)==4
 W=load();H=W[0];assert H==eight()[0]and H<q(U);small=classify(o,W,m);big=classify(o,eight(),m);assert small<q(F('3.25')) and q(F('3.43'))<big<q(F('3.435'))
 rows=json.loads(Path('full-endpoint-mask-cases.json').read_text(),object_pairs_hook=unique);edges=[]
 jobs=[]
 for a,b,L in rows:
  assert edges==[]and a is None or edges and a==edges[-1] and a is not None
  assert a is None or type(a)is int and 0<=a<=M
  assert b is None or type(b)is int and (a or 0)<b<=M;edges.append(b)
  base=([5,3,a,15,1,a,5,0,M-a,15,2,M-a]if a else [])+([5,2,b]if b else []);paths=[]
  for p,r,out in L:
   assert type(p)is list and len(p)%3==0 and all(type(x)is int for x in p);cp=[p[j:j+3]for j in range(0,len(p),3)]
   assert all(i in O and t in range(6)and(0<x<128 if t>=4 else 0<=x<=M)for i,t,x in cp)
   assert len(r)==4 and all(type(x)is int for x in r)and 1<=r[0]<=1000 and 2<=r[1]<=64 and 4<=r[2]<=1024 and 1<=r[3]<=1000
   assert out==['empty']or(len(out)==2 and tuple(out[0])in gg and out[1]in ('chord','faces'));jobs.append((a,b,base+p,r,out));paths.append(cp)
  assert covered(paths),(a,b)
 assert edges[-1]is None and len(edges)>=2
 with tempfile.TemporaryDirectory()as tmp:
  d=Path(tmp);worker(d);certified_init(o,128,d/'i')
  def job(z):
   a,b,p,r,out=z;rr=subprocess.check_output([d/'geometry',d/'i'],input=' '.join(map(str,[*r,18,*O,*p]))+'\n',text=True).splitlines()
   st,c,i,it,B=rr[-1].split()
   if out==['empty']:
    assert len(rr)==1 and st in ('C','F')and c in ('1','2')and int(i)in O and 0<=int(it)<(r[0]if st=='C'else r[-1]),(z,rr[-1]);return 'empty:'+rr[-1]
   assert len(rr)==2 and st=='OPEN';S=parsed(rr[0]);assert set(S)==set(O)
   g,name=out;X=transform(S,R,U,g);assert set(X)==set(O)
   ans=(guard if name=='chord'else lagrange)(X,U,IDS);assert ans[0],(a,b,p,g,name,ans[1])
   return name+':'+str(g)
  with ThreadPoolExecutor(w)as ex:ans=list(ex.map(job,jobs))
 print('Exact H achieved by two physical squares layouts; D4 minimum covers all 18-square poses on mask',m,flush=True)
 print('All',len(rows),'coordinate slabs /',len(jobs),'full from-bare terminals:',sorted(Counter(x.split(':')[0]for x in ans).items()),hashlib.sha256(('\n'.join(ans)+'\n').encode()).hexdigest(),flush=True)
 print('PASS: exact optimum (7+sqrt(7))/2 in entire endpoint rack class; no globally smaller packing can belong to this class.',round(time.monotonic()-started,3),flush=True)
if __name__=='__main__':run()
