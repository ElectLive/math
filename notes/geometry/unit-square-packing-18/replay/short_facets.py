from pathlib import Path
def transform(s):
 key=' // Direction registry'
 h=s.index(key);t=s.index(' vector<vector<vector<HP>>> Fban',h);p=s[h:t];s=s[:h]+s[t:]
 ins='for(it=0;it<rounds;it++)'
 s=s.replace(ins,p+'''
 vector<int>ord(Wn);iota(ord.begin(),ord.end(),0);
 sort(ord.begin(),ord.end(),[&](int i,int j){
   HP u=N[i],v=N[j];auto top=[](HP x){return x.b>0||(x.b==0&&x.a>0);};
   if(top(u)!=top(v))return top(u)>top(v);
   return u.a*v.b-u.b*v.a>0;
 });
 '''+ins)
 s=s.replace('for(int d=0;d<Wn;d++)if(h[d]!=inf){auto hp=N[d];hp.k=h[d]+hk[k][d];Fban[k][j].push_back(hp);}', '''
   auto &ff=Fban[k][j];auto cr=[](HP a,HP b){return a.a*b.b-a.b*b.a;};
   auto redundant=[&](HP a,HP b,HP c){I ac=cr(a,c),ab=cr(a,b),bc=cr(b,c);
    return ac>0 && ab>0 && bc>0 && (W)b.k*ac>=(W)a.k*bc+(W)c.k*ab;
   };
   for(int d:ord)if(h[d]!=inf){HP hp=N[d];hp.k=h[d]+hk[k][d];
    while(ff.size()>=2&&redundant(ff[ff.size()-2],ff.back(),hp))ff.pop_back();
    ff.push_back(hp);}
   int l=0,r=ff.size();
   while(r-l>=3){
    if(redundant(ff[r-2],ff[r-1],ff[l])){r--;continue;}
    if(redundant(ff[r-1],ff[l],ff[l+1])){l++;continue;}break;
   }
   if(r<(int)ff.size())ff.resize(r);if(l>0)ff.erase(ff.begin(),ff.begin()+l);
 ''')
 assert 'auto redundant' in s
 return s
if __name__=='__main__':
 import sys
 a,b=sys.argv[1:];Path(b).write_text(transform(Path(a).read_text()))
