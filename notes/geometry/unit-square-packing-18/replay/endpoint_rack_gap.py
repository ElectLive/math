"""A genuine gap of an intrinsic center observable on the fixed 18-owner chart; exact witnesses on both sides."""
from inhabited_endpoint import build,certified_init
from verify_rack_angle import chartrows,check_rack,marks
from six_tilt18 import Q,q,F,sub,dot,combinations,load
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess,json,time,sys
def eight():
 H=Q(F(7,2),F(1,2));u=(Q(F(1,4),F(1,4)),Q(F(-1,4),F(1,4)));v=(-u[1],u[0]);I=((q(1),q(0)),(q(0),q(1)));A=(I,(u,v))
 D={1:(q(F(1,2)),q(F(1,2))),2:(q(F(1,2)),q(F(3,2))),3:(q(F(1,2)),q(F(5,2))),4:(q(F(3,2)),q(F(1,2))),5:(q(F(1,2)),H-F(1,2)),15:(Q(F(19,16),F(1,16)),Q(F(47,16),F(3,16))),8:(Q(F(49,16),F(-3,16)),Q(F(27,16),F(9,16)))}
 D[16]=sub(D[15],v);D[9]=sub(D[8],(-v[0],-v[1]))
 for i,j in ((1,10),(2,11),(3,12),(4,13),(5,14),(15,6),(16,7),(8,17),(9,18)):D[j]=tuple(H-w for w in D[i])
 tilt={6,7,8,9,15,16,17,18}
 def rad(i,d):return (abs(dot(A[i in tilt][0],d))+abs(dot(A[i in tilt][1],d)))*F(1,2)
 for i,j in combinations(D,2):assert any(abs(dot(d,sub(D[i],D[j])))>=rad(i,d)+rad(j,d) for d in A[i in tilt]+A[j in tilt])
 for i,p in D.items():
  for d in I:assert rad(i,d)<=dot(d,p)<=H-rad(i,d)
 return H,{i:(i in tilt,p) for i,p in D.items()},u
def classify(o,pack,m):
 H,P,u=pack;assert H<q(o['cap']);O={};U=q(o['cap'])
 for i,(tilt,p) in P.items():
  a,b=(u,(-u[1],u[0])) if tilt else ((q(1),q(0)),(q(0),q(1)))
  rr=[max(abs(dot(a,sub(p,z))),abs(dot(b,sub(p,z)))) for z in marks(o)];j=rr.index(min(rr));assert rr[j]<q(F(1,2)) and rr.count(rr[j])==1 and j not in O;O[j]=p
 assert sum(1<<j for j in O)==m
 return min(O[5][1],O[15][0],U-O[5][0],U-O[15][1])
def run():
 begin=time.monotonic();o=json.loads(Path('stabs18-endpoint-window.json').read_text());assert check_rack(o)['status']=='STRICT_STABBING';U=4822876;assert F(o['cap'])==F(U,10**6)
 m=chartrows(o,18)[53];assert m==2030575;O=[i for i in range(21) if m>>i&1];t0=classify(o,load(),m);t1=classify(o,eight(),m);assert t0<q(F(13,4)) and q(F(343,100))<t1<q(F(344,100))
 # Names are actual transformed labels, verified directly by the true mark coordinates.
 sy=set();rack=marks(o)
 for sw in (0,1):
  for a in (0,1):
   for b in (0,1):
    perm=[rack.index((F(o['cap'])-z[sw] if a else z[sw],F(o['cap'])-z[1-sw] if b else z[1-sw])) for z in rack]
    if {perm[i] for i in O}==set(O):sy.add((sw,a,b,perm[5]))
 assert sy=={(0,0,0,5),(0,1,1,15),(1,0,0,15),(1,1,1,5)}
 # All four numbers >= l, and y5 <= h if finite. We need never impose the nonlinear min on a solver.
 def cut(l,h):return [5,3,l,5,0,U-l,15,2,U-l,15,1,l]+([5,2,h]if h is not None else [])
 jobs=[(cut(l,l+10000),[160,4,384,55])for l in range(3250000,3340000,10000)]+[(cut(3450000,None),[160,8,640,100])]
 with TemporaryDirectory()as td:
  d=Path(td);build(d);certified_init(o,128,d/'i');data=''.join(' '.join(map(str,[*params,18,*O,*p]))+'\n' for p,params in jobs)
  out=subprocess.check_output([d/'verify1',d/'i'],input=data,text=True)
  for line,(p,params) in zip(out.splitlines(),jobs,strict=True):
   stage,rc,who,it,B=line.split();assert rc in ('1','2') and int(who) in O and stage in ('C','F') and 0<=int(it)<(params[0] if stage=='C' else params[3]);print(p[:3],line,flush=True)
 print('PASS strict center gap: neither t in [3.25,3.34] nor t>=3.45 fits in chart 53 at 4.822876; genuine H controls on both sides.',t0,t1,round(time.monotonic()-begin,3))
if __name__=='__main__':
 if sys.flags.optimize:raise RuntimeError('assertions are required')
 run()
