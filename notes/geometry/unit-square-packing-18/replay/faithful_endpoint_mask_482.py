"""Complete at-cap exclusion of rack mask 53 only; previous-cap recipes are NOT inputs."""
from pathlib import Path
import tempfile,subprocess,time,sys,json
from fractions import Fraction as F
from verify_arc_lower import certified_init,build
from verify_rack_angle import chartrows,marks,check_rack
def jobs(o):
 U=4820000;r=marks(o);m=chartrows(o,18)[53];assert m==2030575
 O=[i for i in range(21)if m>>i&1]
 names=set()
 for sw in (0,1):
  for sx in (0,1):
   for sy in (0,1):
    p=[r.index((F(o['cap'])-z[sw] if sx else z[sw],F(o['cap'])-z[1-sw] if sy else z[1-sw]))for z in r]
    if {p[j]for j in O}==set(O):
     # all four transforms are involutions, so preimage of named role 5 is p[5]
     assert all(p[p[j]]==j for j in O);names.add((p[5],1-sw,sy))
 assert names=={(5,1,0),(15,0,0),(5,0,1),(15,1,1)}
 def cover(a,b):
  return [5,3,a,15,1,a,5,0,U-a,15,2,U-a]+([5,2,b]if b else [])
 coarse=[128,5,384,60];fine=[220,8,768,135]
 edges=[*range(3250000,3350000,10000),*range(3350000,3440000,5000),3440000,3450000]
 out=[(coarse,[5,2,3250000])]+[(fine if b-a==5000 else coarse,cover(a,b))for a,b in zip(edges,edges[1:])]+[(coarse,cover(3450000,None))]
 assert len(out)==31
 return O,out
def run():
 if sys.flags.optimize:raise RuntimeError('assertions required')
 t=time.monotonic();o=json.loads(Path('stabs18-4815.json').read_text());o['cap']='4.82';assert check_rack(o)['status']=='STRICT_STABBING'
 O,J=jobs(o)
 with tempfile.TemporaryDirectory()as td:
  d=Path(td);certified_init(o,128,d/'init');build(d)
  job=''.join(' '.join(map(str,[*r,18,*O,*p]))+'\n'for r,p in J)
  with subprocess.Popen([d/'verify1',d/'init'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)as child:
   result,_=child.communicate(input=job);assert child.returncode==0
  for (r,p),l in zip(J,result.splitlines(),strict=True):
   z,reason,tile,n,B=l.split();assert z in ('C','F')and reason in ('1','2') and int(tile)in O and 0<=int(n)<(r[0]if z=='C'else r[-1]);print(p,l,flush=True)
 print('PASS complete 4.82 D4-orbit of mask 53; 31 freshly initialized continuous-domain terminals.',round(time.monotonic()-t,3))
if __name__=='__main__':run()
