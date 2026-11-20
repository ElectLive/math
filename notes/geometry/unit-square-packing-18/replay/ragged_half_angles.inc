// Construct genuine half-angle children only of coarse strips physically still live.
// No work file may provide these domains in the certifying entry point.
struct Dir{I c,s,d;};
Dir cs(I p,I q){return {q*q-p*p,2*p*q,q*q+p*p};}
I nearq(W n,W d){return fl(2*n+d,2*d);}
bool fine(Engine &e,const vector<int>&O,int factor,int limit){
 int old=e.B;vector<int>use;for(int k=0;k<old;k++)if(any_of(O.begin(),O.end(),[&](int j){return !e.init[k][j].empty();}))use.push_back(k);
 factor=min(factor,limit/(int)max(size_t(1),use.size()));if(factor<2)return false;
 int G=old*factor;if(G>8192||e.U>6000000||e.D!=1000000)throw runtime_error("range");
 vector<Row>R;vector<vector<P>>C;for(int l:use)for(int g=0;g<factor;g++){
   int k=l*factor+g;auto d=cs(2*k+1,2*G);I M=100000,px=nearq((W)M*d.c,d.d),py=nearq((W)M*d.s,d.d),h=-fl(-(W)e.D*(M*(G+1)+2*G),2*G);
   Row row;row.axes={HP{px,py,h},HP{-py,px,h},HP{-px,-py,h},HP{py,-px,h}};
   P core;for(int a:{-1,1})for(int b:{-1,1})core.push_back({nearq((W)(e.D-6)*G*(a*d.c-b*d.s),2*(W)(G+1)*d.d),nearq((W)(e.D-6)*G*(a*d.s+b*d.c),2*(W)(G+1)*d.d)});
   row.core=hull(core);for(auto v:row.core)if(find(row.core.begin(),row.core.end(),Point{-v.x,-v.y})==row.core.end())throw runtime_error("central");
   row.fac=facets(row.core);R.push_back(row);auto v=e.init[l];auto u0=cs(k,G),u1=cs(k+1,G);
   I d0=min(fl((W)e.D*(u0.c+u0.s),2*u0.d),fl((W)e.D*(u1.c+u1.s),2*u1.d));
   for(int i:O)for(auto h:vector<HP>{{1,0,e.U-d0},{-1,0,-d0},{0,1,e.U-d0},{0,-1,-d0}})if(!v[i].empty()&&mx(v[i],h)>h.k)v[i]=cut(v[i],h);
   C.push_back(move(v));}
 e.B=C.size();e.rows=move(R);e.init=move(C);return true;}
