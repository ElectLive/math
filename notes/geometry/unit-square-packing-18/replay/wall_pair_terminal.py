from itertools import combinations
from pathlib import Path
import sys
def boxes(s):
 it=iter(s.split());assert next(it)=='POSE2';n,B=int(next(it)),int(next(it));grid=[(int(next(it)),int(next(it)))for _ in range(B)];S={}
 for j in range(n):
  i=int(next(it));allp=[]
  for k,g in grid:
   pp=[(int(next(it)),int(next(it)))for _ in range(int(next(it)))]
   if pp:
    allp.extend(pp)
  xs,ys=zip(*allp);S[i]=[min(xs),max(xs),min(ys),max(ys)]
 assert next(it,None)is None;return S
def test(S,U,D):
 for i,j in combinations(S,2):
  A=S[i];B=S[j];m=lambda p:min(p[1],U-p[0],p[3],U-p[2])
  C=max(0,2*max(m(A),m(B))-D);X=max(A[1]-B[0],B[1]-A[0]);Y=max(A[3]-B[2],B[3]-A[2])
  if 7*D*X+12*C*Y<7*D**2 and 7*D*Y+12*C*X<7*D**2:return i,j,C,X,Y
def run():
 import json,time,subprocess,tempfile
 from fractions import Fraction as F
 from inhabited_endpoint import certified_init,worker
 from verify_rack_angle import chartrows,check_rack
 t=time.monotonic();o=json.loads(Path('stabs18-4815.json').read_text());o['cap']='4.82';assert check_rack(o)['status']=='STRICT_STABBING';R=chartrows(o,18)
 from ast import literal_eval
 jobs=[(137,[12,1,2909031]),(92,[12, 1, 2909035])]
 with tempfile.TemporaryDirectory()as tmp:
  d=Path(tmp);worker(d);certified_init(o,128,d/'i')
  for i,p in jobs:
   O=[j for j in range(21)if R[i]>>j&1];z=subprocess.check_output([d/'geometry',d/'i'],input=' '.join(map(str,[160,8,640,125,18,*O,*p]))+'\n',text=True).splitlines()
   assert len(z)==2 and z[-1].startswith('OPEN ');S=boxes(z[0]);assert set(S)==set(O)
   result=test(S,4820000,10**6);assert result and result[:2]==(3,8);print(i,z[-1],result,flush=True)
 print('PASS two fixed 4.82 leaves impossible by wall-angle feedback, no additional branching.',round(time.monotonic()-t,3))
if __name__=='__main__':
 if sys.flags.optimize:raise RuntimeError('assertions required')
 run()
