"""Native physical side-normal contraction on independent movable angle intervals."""
from pathlib import Path
import sys
def transform(s):
 assert s.count('struct Row{')==1;s=s.replace('struct Row{','struct Row{int ki=-1,gi=0;')
 s=s.replace('Row r;for(auto&v:r.axes)','Row r;r.ki=k;r.gi=B;for(auto&v:r.axes)')
 if 'Row row;row.axes' in s:s=s.replace('Row row;row.axes','Row row;row.ki=k;row.gi=G;row.axes')
 a=s.index(' // Direction registry');b=s.index(' for(it=0;it<rounds;it++)',a)
 s=s[:a]+r"""
 auto uv=[](I k,I g){return array<I,3>{g*g-k*k,2*g*k,g*g+k*k};};
 vector<HP> N;map<pair<I,I>,int>reg;vector<vector<int>>ids(B);vector<vector<I>>av(B);
 vector<pair<array<I,3>,array<I,3>>>ends;
 for(int k=0;k<B;k++){int g=rows[k].gi,kk=rows[k].ki;if(g<4||g>8192||kk<0||kk>=g||g!=rows[0].gi||(k&&kk<=rows[k-1].ki))throw runtime_error("no certified disjoint-angle grid");
 auto l=uv(kk,g),r=uv(kk+1,g),m=uv(2*kk+1,2*g);ends.push_back({l,r});
 for(auto v:{l,r}){I gg=gcd(v[0],v[1]);I x=v[0]/gg,y=v[1]/gg;
  I aa=fl((W)D*((W)x*m[0]+(W)y*m[1]),2*m[2]);
  for(int t=0;t<4;t++){auto z=reg.emplace(make_pair(x,y),(int)reg.size());if(z.second)N.push_back({x,y,0});
   ids[k].push_back(z.first->second);av[k].push_back(aa);I h=x;x=-y;y=h;}
 }}
 int Wn=N.size();I inf=2000000000000000000ll;vector<int>ord(Wn);iota(ord.begin(),ord.end(),0);
 sort(ord.begin(),ord.end(),[&](int i,int j){auto u=N[i],v=N[j];auto top=[](HP e){return e.b>0||(e.b==0&&e.a>0);};if(top(u)!=top(v))return top(u)>top(v);return u.a*v.b-u.b*v.a>0;});
 vector<vector<I>> lit(B,vector<I>(Wn));for(int k=0;k<B;k++)for(int d=0;d<Wn;d++){
 HP n=N[d];auto [l,r]=ends[k];auto support=[&](array<I,3>v){I p=n.a*v[0]+n.b*v[1],q=-n.a*v[1]+n.b*v[0];return fl((W)D*(abs(p)+abs(q)),2*v[2]);};lit[k][d]=min(support(l),support(r));}
""" + s[b:]
 a=s.index(' vector<vector<vector<HP>>> Fban');b=s.index(' bool changed=false;auto HH=H;',a)
 s=s[:a]+r"""
 vector<vector<vector<HP>>> Fban(B,vector<vector<HP>>(Z));if(it%4==0)for(int j:O){
 vector<I> A(Wn,inf),T(Wn,inf);vector<vector<I>> self(B);
 for(int l=0;l<B;l++)if(!C[l][j].empty()){
 for(int d=0;d<Wn;d++)A[d]=min(A[d],mn(C[l][j],N[d])+lit[l][d]);
 for(size_t a=0;a<ids[l].size();a++){int d=ids[l][a];I m=mn(C[l][j],N[d]);T[d]=min(T[d],m+av[l][a]);self[l].push_back(m+2*av[l][a]);}}
 auto crossn=[](HP u,HP v){return u.a*v.b-u.b*v.a;};
 auto redundant=[&](HP a,HP b,HP c){I ac=crossn(a,c),ab=crossn(a,b),bc=crossn(b,c);return ac>0&&ab>0&&bc>0&&(W)b.k*ac>=(W)a.k*bc+(W)c.k*ab;};
 for(int k=0;k<B;k++){if(none_of(O.begin(),O.end(),[&](int i){return !C[k][i].empty();}))continue;vector<I>h(Wn,inf);
 for(int d=0;d<Wn;d++)if(T[d]!=inf)h[d]=T[d]+lit[k][d];
 for(size_t a=0;a<ids[k].size();a++){int d=ids[k][a];if(A[d]!=inf)h[d]=min(h[d],A[d]+av[k][a]);if(!self[k].empty())h[d]=min(h[d],self[k][a]);}
 auto&ff=Fban[k][j];for(int d:ord)if(h[d]!=inf){HP hp=N[d];hp.k=h[d];while(ff.size()>=2&&redundant(ff[ff.size()-2],ff.back(),hp))ff.pop_back();ff.push_back(hp);}
 int l=0,r=ff.size();while(r-l>=3){if(redundant(ff[r-2],ff[r-1],ff[l])){r--;continue;}if(redundant(ff[r-1],ff[l],ff[l+1])){l++;continue;}break;}if(r<(int)ff.size())ff.resize(r);if(l)ff.erase(ff.begin(),ff.begin()+l);
 }}
""" +s[b:]
 return s
if __name__=='__main__':Path(sys.argv[2]).write_text(transform(Path(sys.argv[1]).read_text()))
