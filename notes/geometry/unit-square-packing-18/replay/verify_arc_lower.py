"""From-bare verification of a full nearest-owner cover with selective angle refinement."""
import sys,time,json,subprocess,tempfile,hashlib
from fractions import Fraction
from pathlib import Path
from collections import defaultdict,Counter
from verify_rack_angle import check_rack,chartrows,covered,unique
from verify_exit_lower import optimized,certified_init
from adaptive_angles import emit
from arc_pair_variant import transform as angular
def build(d):
 subprocess.run([sys.executable,'pair_variant.py','lattice_kernel.cpp',d/'p.cc'],check=True);optimized(d/'p.cc',d/'s.cc');emit(d/'s.cc',d/'r.cc')
 p=d/'r.cc';s=p.read_text();assert s.count('L>256||')==1;p.write_text(s.replace('L>256||','L>1024||'))
 subprocess.run(['g++','-std=c++17','-O3',p,'-o',d/'verify0'],check=True);p.write_text(angular(p.read_text()));subprocess.run(['g++','-std=c++17','-O3',p,'-o',d/'verify1'],check=True)
def main(rack,n,case):
 t=time.monotonic();o=json.loads(Path(rack).read_text(),object_pairs_hook=unique);assert check_rack(o)['status']=='STRICT_STABBING'
 J=defaultdict(list);data=json.loads(Path(case).read_text(),object_pairs_hook=unique);rr=chartrows(o,n);assert set(data)=={format(x,'x')for x in rr}
 for m in rr:
  O=[i for i in range(o['marks']) if m>>i&1];b,c=data[format(m,'x')];assert type(b)is int and b in (32,64,96,128);paths=[]
  for path,params,mode in c:
   assert type(mode)is int and mode in (0,1)
   assert len(params)==4 and all(type(v)is int for v in params);nr,f,l,fr=params;assert 1<=nr<=1000 and 2<=f<=64 and 4<=l<=1024 and 1<=fr<=1000
   assert len(path)%3==0 and len(path)<96 and all(type(i)is int for i in path);spl=[path[h:h+3]for h in range(0,len(path),3)];assert all(i in O and y in range(6) and (1<=v<b if y>=4 else 0<=v<=10**6*Fraction(o['cap']))for i,y,v in spl)
   paths.append(spl);J[b,mode].append((O,params,' '.join(map(str,[*params,n,*O,*path]))))
  assert covered(paths)
 print('STRICT_STABBING and full chart coverage',len(rr),{b:len(q)for b,q in sorted(J.items())},flush=True)
 with tempfile.TemporaryDirectory()as td:
  d=Path(td);build(d)
  for (b,mode),jobs in sorted(J.items()):
   st=time.monotonic();p=d/f'i{b}';
   if not p.exists():certified_init(o,b,p)
   out=subprocess.check_output([d/f'verify{mode}',p],input=''.join(line+'\n' for _,_,line in jobs),text=True);rates=Counter()
   for (O,params,job),l in zip(jobs,out.splitlines(),strict=True):
    stage,rc,i,it,b2=l.split();rc,i,it,b2=map(int,(rc,i,it,b2));assert stage in ('C','F') and rc in (1,2) and i in O and 0<=it<(params[0] if stage=='C' else params[3]) and (b2==b if stage=='C' else 2<=b2<=params[2]),('unclosed',l,job);rates[stage,rc]+=1
   print(b,mode,sorted(rates.items()),hashlib.sha256(out.encode()).hexdigest(),round(time.monotonic()-st,3),flush=True)
 print('GLOBAL_FIXED_CAP_EXCLUDED',n,Fraction(o['cap']),round(time.monotonic()-t,3),flush=True)
if __name__=='__main__':
 if sys.flags.optimize or len(sys.argv)!=4:raise ValueError('requires checks on; rack.json n cases.json')
 main(sys.argv[1],int(sys.argv[2]),sys.argv[3])
