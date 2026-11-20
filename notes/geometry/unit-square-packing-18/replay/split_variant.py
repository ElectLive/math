"""Add exact, covering center-coordinate splits to the reviewed joint C++ checker. No external states."""
from pathlib import Path
import sys
def extend(source,target):
 s=Path(source).read_text()
 def sub(a,b):
  nonlocal s
  assert s.count(a)==1;s=s.replace(a,b)
 sub('struct Engine{','vector<array<I,3>> restr;struct Engine{')
 sub('auto H=seed;auto C=init;', '''auto H=seed;auto C=init;for(auto rr:restr){int j=rr[0],t=rr[1];I v=rr[2];
 HP h=t==0?HP{1,0,v}:t==1?HP{-1,0,-v}:t==2?HP{0,1,v}:HP{0,-1,-v};
 for(int k=0;k<B;k++){P&p=C[k][j];if(!p.empty()&&mx(p,h)>h.k)p=cut(p,h);}}''')
 sub('for(int j:O){vector<I>S','if(it%4==0)for(int j:O){vector<I>S')
 sub('string rest;if(s>>rest)throw runtime_error("tail");','''restr.clear();for(int q=0;q<32;q++){s>>ws;if(s.eof())break;int j,t;I v;
 if(!(s>>j>>t>>v)||find(O.begin(),O.end(),j)==O.end()||t<0||t>3||v<0||v>e.U)throw runtime_error("bad axis split");restr.push_back({j,t,v});}string tail;if(s>>tail)throw runtime_error("tail");''')
 Path(target).write_text(s)
if __name__=='__main__':extend(*sys.argv[1:])
