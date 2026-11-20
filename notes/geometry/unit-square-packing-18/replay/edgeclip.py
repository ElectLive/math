from pathlib import Path
def transform(s):
 start=s.index('P remove_forbidden')
 end=s.index('struct DPt',start)
 s=s[:start]+r"""P noninterior_hull(const P&p,const vector<HP>&fs){
 if(p.empty()||fs.empty())return p;
 vector<uint8_t> marked(p.size());int n=p.size(),k=0;for(int i=0;i<n;i++){
   for(HP h:fs)if(eval(h,p[i])>=0){marked[i]=1;k++;break;}}
 if(k==n)return p;if(k==0)return {};
 P v;v.reserve(n*4+4);for(int i=0;i<n;i++){int j=(i+1)%n;if(marked[i])v.push_back(p[i]);if(marked[i]==marked[j])continue;
   Point a=marked[i]?p[j]:p[i],b=marked[i]?p[i]:p[j];I nt=1,dt=1;
   for(HP h:fs){I u=eval(h,b);if(u<0)continue;I g=-eval(h,a),d=g+u;
     if((W)g*dt<(W)nt*d){nt=g;dt=d;}}
   W X=(W)a.x*dt+(W)nt*(b.x-a.x),Y=(W)a.y*dt+(W)nt*(b.y-a.y);
   I l=fl(X,dt),r=-fl(-X,dt),b0=fl(Y,dt),t=-fl(-Y,dt);
   v.push_back({l,b0});v.push_back({r,b0});v.push_back({l,t});v.push_back({r,t});}
 return hull(move(v));}
P remove_forbidden(const P&p,const Ban&f){
 if(p.empty()||f.p.empty())return p;
 auto h=bbox(p);if(h.r<=f.b.l||h.l>=f.b.r||h.t<=f.b.b||h.b>=f.b.t)return p;
 return noninterior_hull(p,f.p);}
"""+s[end:]
 st=s.index('   vector<HP>active;bool unchanged=false;');en=s.index('\n  }',st)
 return s[:st]+'   p=noninterior_hull(p,fs);'+s[en:]
if __name__=='__main__':
 import sys
 a,b=sys.argv[1:];Path(b).write_text(transform(Path(a).read_text()))
