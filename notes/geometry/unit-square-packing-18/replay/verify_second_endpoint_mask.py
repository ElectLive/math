"""All true poses of mask 55 have enclosing side at least (7+sqrt(7))/2."""
from verify_full_endpoint_mask import *
def main():
 if sys.flags.optimize:raise RuntimeError('assertions required')
 ap=argparse.ArgumentParser();ap.add_argument('--workers',default=1,type=int);w=ap.parse_args().workers;assert 1<=w<=32
 st=time.monotonic();o=json.loads(Path('stabs18-endpoint-window.json').read_text(),object_pairs_hook=unique);U=F(o['cap']);M=4822876;assert U==F(M,10**6)and check_rack(o)['status']=='STRICT_STABBING'
 R=marks(o);m=chartrows(o,18)[55];O=[j for j in range(21)if m>>j&1];assert m==2030590 and len(O)==18
 rows=json.loads(Path('second-endpoint-mask-cases.json').read_text(),object_pairs_hook=unique);edges=[];jobs=[]
 for a,b,le in rows:
  assert (not edges and a is None)or(edges and a is not None and a==edges[-1]);assert a is None or type(a)is int and 0<a<M
  assert b is None or type(b)is int and (a or 0)<b<M;edges.append(b)
  base=([9,1,a]if a else [])+([9,0,b]if b else []);paths=[]
  for ss,r,out in le:
   assert type(ss)is list and len(ss)%3==0 and all(type(x)is int for x in ss);p=[ss[k:k+3]for k in range(0,len(ss),3)];paths.append(p)
   assert all(i in O and t in range(6)and (0<x<128 if t>=4 else 0<=x<=M)for i,t,x in p)
   assert len(r)==4 and all(type(x)is int for x in r)and 1<=r[0]<=1000 and 2<=r[1]<=64 and 4<=r[2]<=1024 and 1<=r[3]<=1000
   if out!=['empty']:
    g,ids,term=out;assert len(g)==3 and all(type(v)is int and v in (0,1)for v in g)and len(ids)==len(set(ids))==7 and all(type(i)is int for i in ids)and term in ('chord','faces')
   jobs.append((base+ss,r,out))
  assert covered(paths)
 assert edges[-1]is None and len(edges)>=2
 with tempfile.TemporaryDirectory()as tmp:
  d=Path(tmp);worker(d);certified_init(o,128,d/'i')
  def job(z):
   p,r,out=z;rr=subprocess.check_output([d/'geometry',d/'i'],input=' '.join(map(str,[*r,18,*O,*p]))+'\n',text=True).splitlines();stage,c,i,it,B=rr[-1].split()
   if out==['empty']:
    assert len(rr)==1 and stage in ('C','F')and c in ('1','2')and int(i)in O and 0<=int(it)<(r[0]if stage=='C'else r[-1]);return 'empty:'+rr[-1]
   assert len(rr)==2 and stage=='OPEN';S=parsed(rr[0]);assert set(S)==set(O)
   g,ids,term=out;X=transform(S,R,U,g);assert set(ids)<=set(X)
   ok,reason=(guard if term=='chord'else lagrange)(X,U,ids);assert ok,(z,reason);return term+':'+str(g)+':'+str(ids)
  with ThreadPoolExecutor(w)as ex:ans=list(ex.map(job,jobs))
 print('All',len(rows),'x9 slabs /',len(jobs),'terminals. Ordered digest:',sorted(Counter(x.split(':')[0]for x in ans).items()),hashlib.sha256(('\n'.join(ans)+'\n').encode()).hexdigest())
 print('PASS all poses in mask 55 have side at least H. No assumption that the infimum in 55 is attained at H.',round(time.monotonic()-st,3))
if __name__=='__main__':main()
