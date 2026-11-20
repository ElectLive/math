"""Global-in-one-rack-class H lower, except explicitly retained min-coordinate windows."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from concurrent.futures import ThreadPoolExecutor
import sys,tempfile,time,json,subprocess,argparse
from inhabited_endpoint import parsed,worker,certified_init
from endpoint_rack_gap import eight,classify
from six_tilt18 import load,q
from verify_rack_angle import check_rack,chartrows,marks
from wall_chord_guard import guard,coords,bound
from genuine_facing_bridge import lagrange
IDS=(2,0,1,18,13,5,11)
def transform(S,R,U,g):
 sw,sx,sy=g
 def p(x):return (U-x[sw] if sx else x[sw],U-x[1-sw] if sy else x[1-sw])
 T={}
 for j,states in S.items():
  out=[]
  for x,X,y,Y,u,v in states:
   box=bound([p(z)for z in coords((x,X,y,Y))]);a,b=((v[1],v[0]),(u[1],u[0]))if sw^sx^sy else (u,v)
   out.append((*box,a,b))
  T[R.index(p(R[j]))]=out
 return T
def recipes():
 labels=[None,*range(3250000,3340001,10000),*range(3345000,3450001,5000),None]
 for a,b in zip(labels,labels[1:]):
  if a and b and a>=3405000 and b<=3435000:continue
  r=[160,8,640,100]if (a is None or b is None)else [160,4,384,55]if b<=3340000 else [210,8,896,105]
  yield a,b,r
def run():
 ap=argparse.ArgumentParser();ap.add_argument('--workers',type=int,default=1);w=ap.parse_args().workers;assert 1<=w<=16 and not sys.flags.optimize
 t=time.monotonic();o=json.load(open('stabs18-endpoint-window.json'));U=F(o['cap']);ui=int(U*10**6);assert ui==4822876 and check_rack(o)['status']=='STRICT_STABBING'
 R=marks(o);mask=chartrows(o,18)[53];O=[i for i in range(21)if mask>>i&1];assert mask==2030575 and len(O)==18
 G=[]
 for sw,sx,sy in product((0,1),repeat=3):
  h=[R.index((U-z[sw]if sx else z[sw],U-z[1-sw]if sy else z[1-sw]))for z in R]
  if {h[j]for j in O}==set(O):
   assert all(h[h[j]]==j for j in O);G.append(((sw,sx,sy),h[5],1-sw,sy))
 assert {t[1:]for t in G}=={(5,1,0),(15,0,0),(5,0,1),(15,1,1)}
 H=load()[0];assert H<q(U);J=list(recipes());assert J[0][0]is None and J[-1][1]is None and [(z[1],zz[0])for z,zz in zip(J,J[1:]) if z[1]!=zz[0]]==[(3405000,3435000)]
 with tempfile.TemporaryDirectory()as tmp:
  d=Path(tmp);worker(d);certified_init(o,128,d/'i')
  def job(z):
   a,b,r=z;P=([5,3,a,15,1,a,5,0,ui-a,15,2,ui-a]if a else [])+([5,2,b]if b else [])
   raw=subprocess.check_output([d/'geometry',d/'i'],input=' '.join(map(str,[*r,18,*O,*P]))+'\n',text=True).splitlines()
   stage,rc,who,it,B=raw[-1].split()
   if len(raw)==1:
    assert stage in ('C','F')and rc in ('1','2')and int(who)in O and 0<=int(it)<(r[0]if stage=='C'else r[-1]);return (a,b,raw[-1])
   assert len(raw)==2 and stage=='OPEN';S=parsed(raw[0]);assert set(S)==set(O)
   for g,*_ in G:
    X=transform(S,R,U,g);assert set(X)==set(O)
    for name,fn in [('chord',guard),('faces',lagrange)]:
     if fn(X,U,IDS)[0]:return(a,b,g,name)
   raise AssertionError(('no validated lower endpoint',a,b))
  with ThreadPoolExecutor(w)as ex:
   for x in ex.map(job,J):print(*x,flush=True)
 print('PASS: a below-H packing on the entire representative rack class 2030575 would need 3.405 < tau < 3.435; no hypothesis on any angle or on other coordinates.',len(J),round(time.monotonic()-t,3),flush=True)
if __name__=='__main__':run()
