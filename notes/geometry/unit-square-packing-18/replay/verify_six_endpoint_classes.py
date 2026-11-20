"""Fresh proof: at side 4.822876 only six unmarked D4 nearest-rack mask classes can remain."""
from verify_arc_lower import build,certified_init
from verify_rack_angle import chartrows,check_rack,covered,unique
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from concurrent.futures import ThreadPoolExecutor
import tempfile,time,hashlib,sys,argparse,json,subprocess
def run():
 if sys.flags.optimize:raise RuntimeError('assertions required')
 ap=argparse.ArgumentParser();ap.add_argument('--workers',type=int,default=1);w=ap.parse_args().workers;assert 1<=w<=32
 t=time.monotonic();o=json.loads(Path('stabs18-endpoint-window.json').read_text(),object_pairs_hook=unique);U=F(o['cap']);assert U==F(4822876,10**6)and check_rack(o)['status']=='STRICT_STABBING'
 R=chartrows(o,18);assert len(R)==187;D=json.loads(Path('n18-482-base.json').read_text(),object_pairs_hook=unique);assert set(D)=={format(r,'x')for r in R}
 keep={53,55,82,92,115,137};up={1,9,21,40,83,95,96,104,124,149};J=defaultdict(list)
 for i,m in enumerate(R):
  if i in keep:continue
  O=[j for j in range(21)if m>>j&1];B,L=D[format(m,'x')];assert len(O)==18 and B in (32,64,128)
  if i in up:assert len(L)==1 and L[0][0]==[];B=128;L=[[[],[220,8,896,130],1]]
  root=[]
  for P,r,a in L:
   assert a in (0,1)and all(type(x)is int for x in [*P,*r])and len(r)==4 and 1<=r[0]<=1000 and 2<=r[1]<=64 and 4<=r[2]<=1024 and 1<=r[3]<=1000
   assert len(P)%3==0;cuts=[P[h:h+3]for h in range(0,len(P),3)];assert all(j in O and d in range(6)and (0<v<B if d>=4 else 0<=v<=4822876)for j,d,v in cuts)
   root.append(cuts);J[B,a].append((i,O,r,' '.join(map(str,[*r,18,*O,*P]))))
  assert covered(root)
 with tempfile.TemporaryDirectory()as tmp:
  d=Path(tmp);build(d)
  for (B,a),A in sorted(J.items()):
   path=d/f'i{B}'
   if not path.exists():certified_init(o,B,path)
   def work(L):
    return subprocess.check_output([d/f'verify{a}',path],input=''.join(z+'\n'for i,O,r,z in L),text=True)
   k=max(1,len(A)//(4*w));bs=[A[n:n+k]for n in range(0,len(A),k)]
   with ThreadPoolExecutor(w)as ex:out=''.join(ex.map(work,bs))
   cnt=Counter()
   for (i,O,r,z),s in zip(A,out.splitlines(),strict=True):
    st,rc,j,it,b=s.split();assert st in ('C','F')and rc in ('1','2')and int(j)in O and 0<=int(it)<(r[0]if st=='C'else r[-1])and(int(b)==B if st=='C'else 2<=int(b)<=r[2]),(i,s)
    cnt[st,rc]+=1
   print(B,a,len(A),sorted(cnt.items()),hashlib.sha256(out.encode()).hexdigest(),flush=True)
 print('PASS 181/187 complete mask classes empty at 4.822876; remaining indices and raw masks:',[(i,R[i])for i in sorted(keep)],round(time.monotonic()-t,3),flush=True)
if __name__=='__main__':run()
