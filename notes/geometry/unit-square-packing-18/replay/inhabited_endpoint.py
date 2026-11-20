"""A real strict-lower endpoint terminal at a fixed rational cap ABOVE the H witness."""
import json,time,tempfile,subprocess,sys
from pathlib import Path
from fractions import Fraction as F
from verify_arc_lower import build,certified_init
from verify_rack_angle import chartrows,check_rack,marks
from wall_chord_guard import vb
from six_tilt_guard import window
from six_tilt18 import load,q
def parsed(s):
 it=iter(s.split());assert next(it)=='POSE2';n,B=int(next(it)),int(next(it));KK=[tuple(int(next(it))for _ in range(2)) for _ in range(B)]
 assert 4<=B<=1024 and len({g for k,g in KK})==1 and KK==sorted(set(KK)) and all(0<=k<g<=8192 for k,g in KK)
 S={}
 for _ in range(n):
  i=int(next(it));assert i not in S;s0=[]
  for k,g in KK:
   ps=[(int(next(it)),int(next(it)))for _ in range(int(next(it)))]
   if ps:
    X,Y=zip(*ps);s0.append((F(min(X),10**6),F(max(X),10**6),F(min(Y),10**6),F(max(Y),10**6),vb(k,g),vb(k+1,g)))
  assert s0;S[i]=s0
 assert next(it,None) is None;return S
def witness(o,m,t):
 H,P,tilt=load();l,h=F('4.81'),F(o['cap']);assert q(l)<H<q(h)
 occ={};rack=marks(o)
 for i,(f,c)in P.items():
  a=tilt if f else(q(1),q(0));rr=[]
  for x,y in rack:
   dx=c[0]-x;dy=c[1]-y;rr.append(max(abs(dx*a[0]+dy*a[1]),abs(dx*a[1]-dy*a[0])))
  j=rr.index(min(rr));assert rr[j]<q(F(1,2)) and j not in occ;occ[j]=i
 assert sum(1<<j for j in occ)==m and P[occ[5]][1][1]<q(t);return occ
def worker(root):
 build(root);p=root/'r.cc';s=p.read_text();key='cout<<(rc?"F":"OPEN")';assert s.count(key)==1
 s=s.replace(key,'''if(!rc){cout<<"POSE2 "<<O.size()<<' '<<e.B;for(auto &row:e.rows)cout<<' '<<row.ki<<' '<<row.gi;for(int j:O){cout<<' '<<j;for(int k=0;k<e.B;k++){auto &v=e.init[k][j];cout<<' '<<v.size();for(auto p:v)cout<<' '<<p.x<<' '<<p.y;}}cout<<endl;}'''+key);p.write_text(s)
 subprocess.run(['g++','-std=c++17','-O3',p,'-o',root/'geometry'],check=True)
def run():
 t0=time.monotonic();o=json.loads(Path('stabs18-endpoint-window.json').read_text());n=18;T=F(13,4);lo=F('4.81');hi=F(o['cap']);pad=hi-lo;assert hi==F(4822876,10**6)
 assert check_rack(o)['status']=='STRICT_STABBING';m=chartrows(o,n)[53];O=[j for j in range(21)if m>>j&1];occ=witness(o,m,T)
 with tempfile.TemporaryDirectory() as td:
  d=Path(td);certified_init(o,128,d/'init');worker(d)
  raw=subprocess.check_output([d/'geometry',d/'init'],input=' '.join(map(str,[160,8,640,100,n,*O,5,2,int(T*10**6)]))+'\n',text=True).splitlines()
  assert len(raw)==2 and raw[1].startswith('OPEN ');S=parsed(raw[0]);assert set(S)==set(O)
  # All possible translations of a smaller bounding square in the rational cap are allowed,
  # even after a cap-D4 move. No assumption that the corresponding translated rack stays nearest.
  V={i:[(x-pad,X,y-pad,Y,a,b)for x,X,y,Y,a,b in w] for i,w in S.items()}
  ids=(2,0,1,18,13,5,11);good,intervals=window(V,lo,hi,ids);assert good
  sy=[]
  for sw in (0,1):
   for a in(0,1):
    for b in(0,1):
     rack=marks(o);perm=[rack.index((hi-v[sw] if a else v[sw],hi-v[1-sw] if b else v[1-sw]))for v in rack]
     if {perm[j]for j in O}==set(O):sy.append((sw,a,b,perm[5]))
  assert set(sy)=={(0,0,0,5),(0,1,1,15),(1,0,0,15),(1,1,1,5)}
  print('PASS actual sqrt(7) packing in canonical mask',m,'occupancy',occ)
  print('PASS single center inequality y5<=13/4; no input orientation restriction; recovered seven roles and exact endpoint lower bound.',raw[1],intervals,'wall',round(time.monotonic()-t0,3))
if __name__=='__main__':
 if sys.flags.optimize:raise RuntimeError('assertions required')
 run()
