from pathlib import Path
import sys
assert len(sys.argv)==3
s=Path(sys.argv[1]).read_text().replace('#include <vector>','#include <vector>\n#include <numeric>\n#include <map>')
key='bool changed=false;auto HH=H;'
insert=r'''
 // Direction registry and Minkowski support common to all live true neighbor angles.
 vector<HP>N;vector<vector<int>> ids(B);map<pair<I,I>,int>reg;
 for(int k=0;k<B;k++)for(auto h:rows[k].fac){
  I g=gcd(abs(h.a),abs(h.b));h.a/=g;h.b/=g;h.k=0;auto ix=reg.emplace(make_pair(h.a,h.b),reg.size());
  if(ix.second)N.push_back(h);ids[k].push_back(ix.first->second);
 }
 int Wn=N.size();I inf=2000000000000000000ll;
 vector<vector<I>> hk(B,vector<I>(Wn));for(int k=0;k<B;k++)for(int d=0;d<Wn;d++)hk[k][d]=mx(rows[k].core,N[d]);
 vector<vector<vector<HP>>> Fban(B,vector<vector<HP>>(Z));
 for(int j:O){vector<I>S(Wn,inf),T(Wn,inf);
  for(int l=0;l<B;l++)if(!C[l][j].empty()){
   for(int d=0;d<Wn;d++)S[d]=min(S[d],hk[l][d]+mn(C[l][j],N[d]));
   for(int d:ids[l])T[d]=min(T[d],hk[l][d]+mn(C[l][j],N[d]));
  }
  for(int k=0;k<B;k++){vector<I>h=T;for(int d:ids[k])h[d]=S[d];
   for(int d=0;d<Wn;d++)if(h[d]!=inf){auto hp=N[d];hp.k=h[d]+hk[k][d];Fban[k][j].push_back(hp);}
  }
 }
 '''
assert s.count(key)==1;s=s.replace(key,insert+key)
key='if(C[k][i]!=p)changed=true;'
assert s.count(key)==1;s=s.replace(key,r'''for(int j:O)if(i!=j&&!p.empty()){
   auto &fs=Fban[k][j];if(fs.empty())continue;
   vector<HP>active;bool unchanged=false;
   for(auto h:fs){if(mn(p,h)>=h.k){unchanged=true;break;}if(mx(p,h)>=h.k)active.push_back(h);}
   if(unchanged)continue;P acc;
   for(auto h:active){P q=cut(p,{-h.a,-h.b,-h.k});acc.insert(acc.end(),q.begin(),q.end());}p=hull(move(acc));
  }
 '''+key)
Path(sys.argv[2]).write_text(s)
