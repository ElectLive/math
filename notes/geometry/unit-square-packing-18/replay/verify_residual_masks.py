"""Fresh fixed-U endpoint proofs for any ONE complete registered residual-mask certificate."""
from verify_second_endpoint_mask import *
from verify_orbit_lower_482 import mirror
from double_probe_bridge import cert
from itertools import combinations_with_replacement
from wall_pair_terminal import test,boxes
def splits(p,O):
 assert len(p)%3==0 and all(type(x)is int for x in p);q=[p[z:z+3]for z in range(0,len(p),3)];assert all(j in O and k in range(6)and(0<v<128 if k>=4 else 0<=v<=4822876)for j,k,v in q);return q
def cover_roots(o,O,m,I):
 f=json.loads(Path('n18-482-base.json').read_text(),object_pairs_hook=unique);b,L=f[format(m,'x')];assert b==128;P=[p for p,r,m in L];assert covered([splits(p,O)for p in P])
 A={82:[0,4,5],92:[1,2],115:[]}[I];roots=[p for j,p in enumerate(P)if j not in A]
 if A:
  g=(1,0,0)if I==82 else(0,0,1)
  for a,b in combinations_with_replacement(A,2):roots.append(P[a]+mirror(o,O,P[b],g,128))
 assert len(set(map(tuple,roots)))==len(roots);return roots
def main():
 if sys.flags.optimize:raise RuntimeError('assertions required')
 ap=argparse.ArgumentParser();ap.add_argument('index',type=int,choices=[82,92,115]);ap.add_argument('--workers',type=int,default=1);ar=ap.parse_args();I,w=ar.index,ar.workers;assert 1<=w<=24;st=time.monotonic()
 o=json.loads(Path('stabs18-endpoint-window.json').read_text(),object_pairs_hook=unique);U=F(o['cap']);assert U==F('4.822876')and check_rack(o)['status']=='STRICT_STABBING';R=marks(o);m=chartrows(o,18)[I];O=[j for j in range(len(R))if m>>j&1];assert len(O)==18
 D=json.loads(Path('residual-'+str(I)+'-cases.json').read_text(),object_pairs_hook=unique);J=[];Z=cover_roots(o,O,m,I);assert len(D)==len(Z) and {tuple(p)for p,L in D}==set(map(tuple,Z))
 for path,L in D:
  splits(path,O);assert covered([splits(p,O)for p,r,act in L])
  for p,r,act in L:
   assert len(r)==4 and all(type(x)is int for x in r)and 1<=r[0]<=1000 and 2<=r[1]<=64 and 4<=r[2]<=1024 and 1<=r[3]<=1000
   if act not in (['empty'],['wall']):
    g,ids,how=act;assert len(g)==3 and all(type(i)is int and i in (0,1) for i in g)and how in ('faces','chord')
   J.append((path+p,r,act))
 with tempfile.TemporaryDirectory()as tmp:
  d=Path(tmp);worker(d);certified_init(o,128,d/'i')
  def job(z):
   path,r,act=z;out=subprocess.check_output([d/'geometry',d/'i'],input=' '.join(map(str,[*r,18,*O,*path]))+'\n',text=True).splitlines();stage,c,j,it,B=out[-1].split()
   if act==['empty']:
    assert len(out)==1 and stage in ('F','C') and c in ('1','2')and int(j)in O and 0<=int(it)<(r[0]if stage=='C'else r[3]);return 'empty:'+out[-1]
   assert stage=='OPEN'and len(out)==2;S=parsed(out[0]);assert set(S)==set(O)
   if act==['wall']:assert test(boxes(out[0]),4822876,10**6);return 'wall'
   g,ids,how=act;T=transform(S,R,U,g)
   if len(ids)==6:
    av,ah,bv,bh,f,h=ids;assert all(isinstance(v,list)and v and all(type(i)is int for i in v)for v in (av,ah,bv,bh));assert type(h)is int and type(f)is int and set(av+ah+bv+bh+[f,h])<=set(T);ok,why=cert(T,U,ids,how)
   else:
    assert len(set(ids))==len(ids)==7 and all(type(i)is int for i in ids)and set(ids)<=set(T);ok,why=(guard if how=='chord'else lagrange)(T,U,ids)
   assert ok,(z,why);return how+':'+str(g)+':'+str(ids)
  with ThreadPoolExecutor(w)as ex:res=list(ex.map(job,J))
 print('Whole residual orbit',I,m,'base regions',len(Z),'from-bare terminal cases',len(J),sorted(Counter(i.split(':')[0]for i in res).items()))
 print('Digest',hashlib.sha256(('\n'.join(res)+'\n').encode()).hexdigest())
 print('PASS no pose in that entire D4 class can improve on H; no attainment asserted.',round(time.monotonic()-st,3))
if __name__=='__main__':main()
