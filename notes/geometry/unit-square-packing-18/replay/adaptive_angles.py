"""Physical ragged angle recrop; trust only the verified bare initialization and branch constraints."""
from pathlib import Path
import tempfile,subprocess,sys,json
from verify_exit_lower import optimized,certified_init
from verify_rack_angle import chartrows,check_rack
def emit(original,out):
 s=Path(original).read_text();pos=s.rfind('return 0;',0,s.index('int main('));assert pos>0 and s[pos:pos+18].startswith('return 0;}')
 # Retain exactly the reached outer domains and proven interior witnesses.
 s=s[:pos]+'seed=move(H);init=move(C);'+s[pos:s.index('int main(')]
 s+=Path(__file__).with_name('ragged_half_angles.inc').read_text()+r"""
int main(int ac,char**av){try{if(ac!=2)throw runtime_error("arguments");Engine base(av[1]);string line;
while(getline(cin,line)){Engine e=base;istringstream x(line);int nr,n,F,L,fr;x>>nr>>F>>L>>fr>>n; if(!x||nr<1||nr>1000||fr<1||fr>1000||F<2||F>64||L<4||L>256||n<1||n>e.Z)throw runtime_error("input range");
vector<int>O(n);for(int &i:O){x>>i;if(!x||i<0||i>=e.Z)throw runtime_error("owner");}auto S=O;sort(S.begin(),S.end());if(unique(S.begin(),S.end())!=S.end())throw runtime_error("duplicate");restr.clear();int j,t;I h;while(x>>j>>t>>h){if(find(O.begin(),O.end(),j)==O.end()||t<0||t>5||abs(h)>10000000)throw runtime_error("cut");restr.push_back({j,t,h});}
int where=0,it=0,rc=e.run(O,nr,where,it);if(rc){cout<<"C "<<rc<<" "<<where<<" "<<it<<" "<<e.B<<endl;continue;}
if(!fine(e,O,F,L)){cout<<"OPEN 0 0 0 0"<<endl;continue;}restr.clear();rc=e.run(O,fr,where,it);cout<<(rc?"F":"OPEN")<<" "<<rc<<" "<<where<<" "<<it<<" "<<e.B<<endl;}}
catch(exception&e){cerr<<e.what()<<endl;return 2;}}
"""
 Path(out).write_text(s)
def make_exe(dir):
 d=Path(dir);subprocess.run([sys.executable,'pair_variant.py','lattice_kernel.cpp',str(d/'pair.cc')],check=True);optimized(d/'pair.cc',d/'split.cc');emit(d/'split.cc',d/'ref.cc')
 subprocess.run(['g++','-O3','-std=c++17',d/'ref.cc','-o',d/'ref'],check=True)
if __name__=='__main__':
 if sys.flags.optimize:raise RuntimeError('assertions required')
 o=json.loads(Path(sys.argv[1]).read_text());c=json.loads(Path(sys.argv[2]).read_text());n,m,B,R,F,L,fr,path=c
 assert check_rack(o)['status']=='STRICT_STABBING' and m in chartrows(o,n) and B in (32,64,96,128)
 O=[i for i in range(o['marks'])if m>>i&1];assert len(path)%3==0 and all(j in O and t in range(6)and(1<=h<B if t>=4 else 0<=h<=10**6*__import__('fractions').Fraction(o['cap']))for j,t,h in zip(path[::3],path[1::3],path[2::3]))
 with tempfile.TemporaryDirectory() as td:
  d=Path(td);certified_init(o,B,d/'init');make_exe(d);s=' '.join(map(str,[R,F,L,fr,n,*O,*path]))+'\n';out=subprocess.check_output([d/'ref',d/'init'],input=s,text=True).strip();print(out)
  assert out.startswith('F ') and int(out.split()[2])in O;print('CONDITIONAL_LEAF_EXCLUDED_ONLY')
