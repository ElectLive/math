# GAP 4.15.1 / CTblLib 1.3.11 source-data checks, conditional on ATLAS and
# CTblLib table identifications and stored fusion/quotient interpretations.
Check:=function(ok,label)
  if not ok then Print("FAIL: ",label,"\n");ForceQuitGap(1);fi;
end;;
Check(GAPInfo.Version="4.15.1","GAP version");
Check(LoadPackage("ctbllib")=true,"CTblLib load");
Check(PackageInfo("ctbllib")[1].Version="1.3.11","CTblLib version");
Main:=function()
 local a,b,s,f,q,z,sa,oa,cc,t,u,normalfusion,outer,ids,sizes,k,coef,formula,n,sol,d,x,y,w,nn,proj,ker,checkmap,checknormal;
 checkmap:=function(source,target,map,label)
   local so,to,sp,tp,i;
   so:=OrdersClassRepresentatives(source); to:=OrdersClassRepresentatives(target);
   sp:=PowerMap(source,2); tp:=PowerMap(target,2);
   Check(Length(map)=Length(so),Concatenation(label," map length"));
   for i in [1..Length(map)] do
     Check(so[i] mod to[map[i]]=0,Concatenation(label," order divisibility"));
     Check(map[sp[i]]=tp[map[i]],Concatenation(label," square consistency"));
   od;
 end;
 checknormal:=function(source,target,map,label)
   local i,j,ss,tt;
   checkmap(source,target,map,label);
   Check(IsClassFusionOfNormalSubgroup(source,map,target),Concatenation(label," normal fusion"));
   ss:=SizesConjugacyClasses(source); tt:=SizesConjugacyClasses(target);
   for j in Set(map) do
     Check(Sum(Filtered([1..Length(map)],i->map[i]=j),i->ss[i])=tt[j],
           Concatenation(label," fused class sizes"));
   od;
 end;
 a:=CharacterTable("3.Suz"); b:=CharacterTable("3.Suz.2"); s:=CharacterTable("Suz");
 Check(a<>fail and b<>fail and s<>fail,"Suz tables");
 Check(Size(a)=3*Size(s) and Size(b)=2*Size(a),"Suz cover and extension orders");
 Check(IsPerfect(a) and IsPerfect(s),"perfect Suz and cover");
 Check(ExtensionInfoCharacterTable(s)[2]="2","Suz outer order");
 z:=ClassPositionsOfCentre(a);;oa:=OrdersClassRepresentatives(a);;
 sa:=SizesConjugacyClasses(a);;
 Check(Length(z)=3 and List(z,i->sa[i])=[1,1,1] and
       SortedList(List(z,i->oa[i]))=[1,3,3],"cover center");
 f:=GetFusionMap(a,b); q:=GetFusionMap(a,s);
 Check(f<>fail and q<>fail,"cover normal fusion and quotient map");
 checknormal(a,b,f,"normal cover fusion");
 checkmap(a,s,q,"cover quotient");
 Check(Length(Set(f{z}))=2 and Length(Set(q{z}))=1 and q[z[1]]=1,
       "outside merges nontrivial center and quotient kills it");
 Check(ForAll(z,i->q[i]=1),"entire center killed by quotient");
 t:=CharacterTable("G2(4)");u:=CharacterTable("G2(4).2");
 Check(t<>fail and u<>fail and Size(t)=251596800 and Size(u)=2*Size(t),"G2 orders");
 Check(IsPerfect(t) and ExtensionInfoCharacterTable(t)[2]="2","G2 perfect and outer order");
 oa:=OrdersClassRepresentatives(t);sizes:=SizesConjugacyClasses(t);
 ids:=Filtered([1..Length(oa)],i->oa[i] in [1,2]);
 Check(ids=[1,2,3] and sizes{ids}=[1,4095,65520],"all inner involutions");
 normalfusion:=GetFusionMap(t,u);
 Check(normalfusion<>fail,"normal G2 fusion exists");
 checknormal(t,u,normalfusion,"normal G2 fusion");
 oa:=OrdersClassRepresentatives(u);sa:=SizesConjugacyClasses(u);cc:=SizesCentralizers(u);
 outer:=Filtered([1..Length(oa)],i->oa[i]=2 and not i in normalfusion);
 Check(Length(outer)=1 and sa[outer[1]]=20800 and cc[outer[1]]/2=12096,"outer involutions");
 for k in [2,3] do
   coef:=ClassMultiplicationCoefficient(t,3,3,k);
   formula:=sizes[3]^2/Size(t)*Sum(Irr(t),ch->ch[3]^2*GaloisCyc(ch[k],-1)/ch[1]);
   Check(coef=formula and coef=[1200,152][k-1],"square coefficient / character formula");
 od;
 nn:=CharacterTable("(A4xG2(4)):2");
 Check(nn<>fail and Size(nn)=24*Size(t),"Co1 normalizer table order");
 proj:=GetFusionMap(nn,u);Check(proj<>fail,"G2 graph quotient fusion");
 checkmap(nn,u,proj,"G2 graph quotient");
 ker:=Filtered([1..Length(proj)],i->proj[i]=1);
 Check(Sum(ker,i->SizesConjugacyClasses(nn)[i])=12,"normalizer quotient kernel");
 Check(Length(Set(proj))=NrConjugacyClasses(u),"normalizer quotient class coverage");
 Check(Gcd(4095,20800)=65,"class gcd");
 for n in [98280,8386560] do
   sol:=[];
   for d in [0..12] do for x in [0..12] do for y in [0..12] do for w in [0..12] do
     if d+4095*x+65520*y+20800*w=n then Add(sol,[d,x,y,w]);fi;
   od;od;od;od;
   if n=98280 then Check(sol=[[0,8,1,0]],"98280 bounded marks");
   else Check(sol=[],"8386560 bounded marks");fi;
   if n=98280 then Check(Valuation(Size(t),2)-Valuation(n,2)=9,"actual normal cut 2-adic bound");fi;
 od;
 Print("PASS: 3.Suz center fusion, G2(4) classes/squares, normalizer quotient, bounded mark counts\n");
end;;
Main();
QUIT_GAP(0);
