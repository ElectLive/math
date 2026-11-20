"""Generate a small exact integer initial-state filter; main lattice engine remains untouched."""
from pathlib import Path
import sys
def source(path,output):
 s=Path(path).read_text();inc=s[:s.index('int main(')]
 # Reuse reader for genuine integer initialization and exact cut+hull primitives; generate output of same format.
 code=r"""
int main(int argc,char**argv){try{
 if(argc!=3)throw runtime_error("init and nearest-facet file");Engine e(argv[1]);ifstream f(argv[2]);int B,Z;f>>B>>Z;if(B!=e.B||Z!=e.Z)throw runtime_error("shape");
 auto pp=[](const P&p){cout<<p.size();for(auto z:p)cout<<' '<<z.x<<' '<<z.y;cout<<'\n';};
 cout<<e.U<<' '<<e.D<<' '<<B<<' '<<Z<<'\n';for(auto &p:e.seed)pp(p);
 for(int k=0;k<B;k++){const auto &r=e.rows[k];for(auto h:r.axes)cout<<h.a<<' '<<h.b<<' '<<h.k<<'\n';pp(r.core);
 for(int i=0;i<Z;i++){P p=e.init[k][i];int nb;f>>nb;if(nb<0||nb>4*Z)throw runtime_error("bans");
 for(int u=0;u<nb;u++){int n;f>>n;if(n!=6)throw runtime_error("facets");vector<HP>hs(n);
 for(auto &h:hs){f>>h.a>>h.b>>h.k;if(!f||abs(h.a)>500000||abs(h.b)>500000||abs(h.k)>10000000000000ll)throw runtime_error("range");}
 if(p.empty())continue;bool leave=false;P out;
 for(auto h:hs){if(mn(p,h)>=h.k){leave=true;break;}if(mx(p,h)<h.k)continue;P a=cut(p,{-h.a,-h.b,-h.k});out.insert(out.end(),a.begin(),a.end());}
 if(!leave)p=hull(move(out));
 }pp(p);}}string x;if(f>>x)throw runtime_error("tail");}
 catch(exception&e){cerr<<e.what()<<endl;return 2;}}
"""
 Path(output).write_text(inc+code)
if __name__=='__main__':source(*sys.argv[1:])
