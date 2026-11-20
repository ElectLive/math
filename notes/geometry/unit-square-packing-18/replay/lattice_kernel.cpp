/* Geometry kernel: int64 coordinates, exact __int128 products, bounded native exporter. */
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <vector>
using namespace std;using I=int64_t;using W=__int128_t;
struct Point { I x,y;bool operator==(Point o)const{return x==o.x&&y==o.y;}bool operator<(Point o)const{return x==o.x?y<o.y:x<o.x;}};
using P=vector<Point>;struct HP{I a,b,k;};
I dot(HP n,Point p){return n.a*p.x+n.b*p.y;}I eval(HP n,Point p){return dot(n,p)-n.k;}
I cross(Point a,Point b,Point c){return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);}
P hull(P pts){sort(pts.begin(),pts.end());pts.erase(unique(pts.begin(),pts.end()),pts.end());if(pts.size()<3)return pts;
 P q(pts.size()*2);int k=0;for(auto v:pts){while(k>=2&&cross(q[k-2],q[k-1],v)<=0)k--;q[k++]=v;}
 int b=k+1;for(int j=(int)pts.size()-2;j>=0;j--){auto v=pts[j];while(k>=b&&cross(q[k-2],q[k-1],v)<=0)k--;q[k++]=v;}q.resize(k-1);return q;}
I fl(W n,W d){if(d<0){d=-d;n=-n;}return (I)(n/d-(n<0&&n%d!=0));}
P cut(const P&p,HP h){
 if(p.empty())return {};P q;auto a=p.back();I u=eval(h,a);for(auto b:p){I v=eval(h,b);
  if((u<0&&v>0)||(u>0&&v<0)){I den=u-v;W X=(W)a.x*den+(W)u*(b.x-a.x),Y=(W)a.y*den+(W)u*(b.y-a.y);I l=fl(X,den),r=-fl(-X,den),d=fl(Y,den),t=-fl(-Y,den);q.push_back({l,d});q.push_back({l,t});q.push_back({r,d});q.push_back({r,t});}
  if(v<=0)q.push_back(b);
  a=b;u=v;}return hull(move(q));}
vector<HP> facets(const P&p){vector<HP>a;if(p.size()<3)return a;auto z=p.back();for(auto v:p){HP n{v.y-z.y,z.x-v.x,0};n.k=dot(n,z);a.push_back(n);z=v;}return a;}
I mx(const P&p,HP h){I r=dot(h,p.front());for(auto v:p)r=max(r,dot(h,v));return r;}
I mn(const P&p,HP h){I r=dot(h,p.front());for(auto v:p)r=min(r,dot(h,v));return r;}
bool meets(const P&a,const P&b){if(a.size()<3||b.size()<3)return false;for(auto n:facets(a))if(mn(b,n)>n.k)return false;for(auto n:facets(b))if(mn(a,n)>n.k)return false;return true;}
struct Bound{I l,r,b,t;};Bound bbox(const P&p){Bound u{p[0].x,p[0].x,p[0].y,p[0].y};for(auto v:p){u.l=min(u.l,v.x);u.r=max(u.r,v.x);u.b=min(u.b,v.y);u.t=max(u.t,v.y);}return u;}
struct Ban{vector<HP> p;Bound b;};Ban add(const P&a,const vector<HP>&af,const P&b,const vector<HP>&bf){Ban z;auto x=bbox(a),y=bbox(b);z.b={x.l+y.l,x.r+y.r,x.b+y.b,x.t+y.t};for(auto n:af){n.k+=mx(b,n);z.p.push_back(n);}for(auto n:bf){n.k+=mx(a,n);z.p.push_back(n);}return z;}
P remove_forbidden(const P&p,const Ban&f){
 if(p.empty()||f.p.empty())return p;
 auto h=bbox(p);if(h.r<=f.b.l||h.l>=f.b.r||h.t<=f.b.b||h.b>=f.b.t)return p;
 bool all=true;for(auto n:f.p){if(mn(p,n)>=n.k)return p;if(mx(p,n)>=n.k)all=false;}if(all)return {};
 P v;for(auto n:f.p){P q=cut(p,{-n.a,-n.b,-n.k});v.insert(v.end(),q.begin(),q.end());}return hull(move(v));}
struct DPt{double x,y;};P safe(const vector<HP>&f,I U){
 vector<DPt>p={{0,0},{(double)U,0},{(double)U,(double)U},{0,(double)U}};
 for(auto h:f){if(p.empty())return {};vector<DPt>q;auto a=p.back();auto evald=[&](DPt z){return (double)h.a*z.x+(double)h.b*z.y-(double)h.k;};auto u=evald(a);for(auto b:p){auto v=evald(b);if((u<0&&v>0)||(u>0&&v<0)){double t=u/(u-v);q.push_back({a.x+t*(b.x-a.x),a.y+t*(b.y-a.y)});}if(v<=0)q.push_back(b);a=b;u=v;}p=move(q);}
 if(p.empty())return {};DPt c{0,0};for(auto v:p){c.x+=v.x;c.y+=v.y;}c.x/=p.size();c.y/=p.size();p.push_back(c);P q;
 for(auto v:p){for(double a:{1.,.999,.99,.9,.5,0.}){double X=a*v.x+(1-a)*c.x,Y=a*v.y+(1-a)*c.y;if(!isfinite(X)||!isfinite(Y)||X< -10||Y< -10||X>U+10||Y>U+10)continue;
  I x=llround(X),y=llround(Y);bool found=0;for(I dx=-1;dx<=1&&!found;dx++)for(I dy=-1;dy<=1&&!found;dy++){Point z{x+dx,y+dy};if(z.x<0||z.y<0||z.x>U||z.y>U)continue;if(all_of(f.begin(),f.end(),[&](HP h){return eval(h,z)<=0;})){q.push_back(z);found=true;}}if(found)break;}}
 return hull(move(q));}
struct Row{array<HP,4>axes;P core;vector<HP>fac;};
struct Engine{int B,Z;I U,D;vector<P>seed;vector<Row>rows;vector<vector<P>> init;
 Engine(string path){ifstream f(path);f>>U>>D>>B>>Z;if(!f||D!=1000000||U>10000000||U<2000000||B<4||B>256||Z<2||Z>100)throw runtime_error("illegal fixed grid");
 auto poly=[&](){int n;f>>n;if(!f||n<0||n>2000)throw runtime_error("polygon count");P p(n);for(auto&x:p){f>>x.x>>x.y;if(!f||abs(x.x)>10000000||abs(x.y)>10000000)throw runtime_error("coordinate");}if(p!=hull(p))throw runtime_error("hull order");return p;};
 for(int i=0;i<Z;i++)seed.push_back(poly());for(int k=0;k<B;k++){Row r;for(auto&v:r.axes){f>>v.a>>v.b>>v.k;if(!f||abs(v.a)>1000000||abs(v.b)>1000000||abs(v.k)>1000000000000ll)throw runtime_error("axis");}
 r.core=poly();if(r.core.size()<3)throw runtime_error("core");for(auto z:r.core)if(find(r.core.begin(),r.core.end(),Point{-z.x,-z.y})==r.core.end())throw runtime_error("not central");r.fac=facets(r.core);rows.push_back(r);vector<P>p;for(int i=0;i<Z;i++)p.push_back(poly());init.push_back(p);}string tail;if(f>>tail)throw runtime_error("tail");}
 int run(const vector<int>&O,int rounds,int&where,int&it){
 auto H=seed;auto C=init;for(it=0;it<rounds;it++){vector<vector<Ban>>bans(B,vector<Ban>(Z));for(int j:O)if(H[j].size()>=3){auto f=facets(H[j]);for(int k=0;k<B;k++)bans[k][j]=add(H[j],f,rows[k].core,rows[k].fac);}
 bool changed=false;auto HH=H;for(int i:O){where=i;vector<HP>all;for(int k=0;k<B;k++){P p=C[k][i];if(p.empty())continue;
 for(auto n:rows[k].axes)if(!H[i].empty()){n.k+=mn(H[i],n);if(mx(p,n)>n.k)p=cut(p,n);if(p.empty())break;}
 for(int j:O)if(j!=i&&!p.empty())p=remove_forbidden(p,bans[k][j]);
 if(C[k][i]!=p)changed=true;C[k][i]=move(p);if(C[k][i].empty())continue;
 for(auto n:rows[k].fac){n.k+=mn(C[k][i],n);all.push_back(n);}}
 if(all.empty())return 1;P q=safe(all,U);HH[i].insert(HH[i].end(),q.begin(),q.end());HH[i]=hull(move(HH[i]));if(HH[i]!=H[i])changed=true;
 for(int j:O)if(j!=i&&meets(HH[i],H[j]))return 2;
 }H=move(HH);if(!changed)break;}
 return 0;}
};
int main(int ac,char**av){try{if(ac!=2)throw runtime_error("init path");Engine e(av[1]);string line;while(getline(cin,line)){istringstream s(line);int r,k;s>>r>>k;if(r<1||r>1000||k<1||k>e.Z)throw runtime_error("job");vector<int>O(k);for(auto&i:O){s>>i;if(i<0||i>=e.Z)throw runtime_error("id");}auto test=O;sort(test.begin(),test.end());if(!s||unique(test.begin(),test.end())!=test.end())throw runtime_error("duplicate");string rest;if(s>>rest)throw runtime_error("tail");int i=0,it=0,Q=e.run(O,r,i,it);cout<<Q<<" "<<i<<" "<<it<<endl;}}catch(exception&e){cerr<<e.what()<<endl;return 2;}}
