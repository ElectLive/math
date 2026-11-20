"""All poses of full orbit 137: two independently measured rows at both ends."""
from verify_second_endpoint_mask import *
from double_probe_bridge import cert
def main():
 if sys.flags.optimize:raise RuntimeError('assertions required')
 ap=argparse.ArgumentParser();ap.add_argument('--workers',default=1,type=int);w=ap.parse_args().workers;assert 1<=w<=16
 st=time.monotonic();o=json.loads(Path('stabs18-endpoint-window.json').read_text(),object_pairs_hook=unique);U=F(o['cap']);assert U==F('4.822876')and check_rack(o)['status']=='STRICT_STABBING'
 R=marks(o);mask=chartrows(o,18)[137];assert mask==2096079;O=[i for i in range(21)if mask>>i&1]
 L=json.loads(Path('n18-482-base.json').read_text(),object_pairs_hook=unique)[format(mask,'x')];assert L[0]==128
 paths=[p for p,r,m in L[1]];assert len(paths)==6 and len({tuple(p)for p in paths})==6;ps=[list(zip(p[::3],p[1::3],p[2::3],strict=True))for p in paths]
 assert all(i in O and t in range(6) and (0<v<128 if t>=4 else 0<=v<=4822876)for cc in ps for i,t,v in cc)
 assert covered([[list(c)for c in cc]for cc in ps]);frames=[1,1,0,0,1,0];roles=[[7],[2,7],[13,16],[20,16],9,14]
 with tempfile.TemporaryDirectory()as tmp:
  d=Path(tmp);worker(d);certified_init(o,128,d/'i')
  def job(item):
   p,g=item;args=[220,8,896,130,18,*O,*p];raw=subprocess.check_output([d/'geometry',d/'i'],input=' '.join(map(str,args))+'\n',text=True).splitlines()
   assert len(raw)==2 and raw[1].startswith('OPEN');S=parsed(raw[0]);assert set(S)==set(O);X=transform(S,R,U,(0,0,g))
   assert set().union(*map(set,roles[:4]),set(roles[4:]))<=set(X)
   ok,why=cert(X,U,roles,'faces');assert ok,(p,g,why);return str([p,g,'faces'])
  with ThreadPoolExecutor(w)as ex:res=list(ex.map(job,zip(paths,frames,strict=True)))
 print('All six naked full-chart leaves of orbit 137 independently reinitialized; all use orthogonal wall rows and the two-facing-square certificate.')
 print('ORDERED',hashlib.sha256(('\n'.join(res)+'\n').encode()).hexdigest())
 print('PASS no pose in 137 has enclosing side below H; no attainment in this class is claimed.',round(time.monotonic()-st,3))
if __name__=='__main__':main()
