# C0010: finite source checks for the proposed canonical G2(4) exclusion.
# The complete maximal lists, identifications, character/power/fusion data and
# perfect-cover structure are ATLAS/CTblLib inputs, not classifications proved here.
Check:=function(b,msg) if not b then Print("FAIL ",msg,"\n");ForceQuitGap(1);fi;end;;
Check(GAPInfo.Version="4.15.1","GAP version");
Check(LoadPackage("ctbllib")=true,"CTblLib load");
Check(PackageInfo("ctbllib")[1].Version="1.3.11","CTblLib version");
Main:=function()
 local s,a,f,os,oa,ss,sa,ca,ids,ms,maxord,eligible,j,l,d,b,u,t,names,orders,x,name;
 s:=CharacterTable("G2(4)");a:=CharacterTable("G2(4).2");
 Check(Size(s)=251596800 and Size(a)=503193600,"group orders");
 Check(ExtensionInfoCharacterTable(s)[2]="2","outer group");
 f:=GetFusionMap(s,a);Check(f<>fail,"stored socle fusion");
 os:=OrdersClassRepresentatives(s);oa:=OrdersClassRepresentatives(a);
 ss:=SizesConjugacyClasses(s);sa:=SizesConjugacyClasses(a);ca:=SizesCentralizers(a);
 Check(Length(f)=Length(os),"fusion length");
 Check(ForAll([1..Length(f)],i->os[i]=oa[f[i]]),"fusion preserves orders");
 Check(Sum(ss)=Size(s) and Sum(sa)=Size(a),"class totals");
 Check(IsClassFusionOfNormalSubgroup(s,f,a),"normal socle fusion");
 Check(ForAll([1..Length(sa)],i->sa[i]*ca[i]=Size(a)),"centralizer/class sizes");
 Check(Filtered([1..Length(oa)],i->PowerMap(a,2)[i]=1)=Filtered([1..Length(oa)],i->oa[i] in [1,2]),"square map");
 ids:=Filtered([1..Length(oa)],i->oa[i]=2 and not i in f);
 Check(Length(ids)=1 and sa[ids[1]]=20800 and ca[ids[1]]/2=12096,"unique outer class");
 Check(HasMaxes(s),"complete G2(4) maximal list");ms:=Maxes(s);
 maxord:=List(ms,n->Size(CharacterTable(n)));
 Check(maxord=[604800,184320,184320,124800,120960,12096,3600,1092],"all maximal orders");
 eligible:=Filtered([1..Length(ms)],i->maxord[i] mod 12096=0);
 Check(List(eligible,i->ms[i])=["J2","3.L3(4).2_3","U3(3).2"],"all eligible maximal classes");
 Check(Number(maxord,x->x=12096)=1,"unique maximal class of required order");
 j:=CharacterTable("J2");l:=CharacterTable("L3(4)");
 d:=CharacterTable("3.L3(4)");b:=CharacterTable("3.L3(4).2_3");u:=CharacterTable("U3(3).2");
 Check(Size(j)=604800 and Size(l)=20160 and Size(d)=60480 and Size(b)=120960 and Size(u)=12096,"overgroup and cover orders");
 Check(IsPerfect(d),"perfect central cover");
 Check(Sum(ClassPositionsOfCentre(d),i->SizesConjugacyClasses(d)[i])=3,"cover center");
 f:=GetFusionMap(d,b);Check(f<>fail and IsClassFusionOfNormalSubgroup(d,f,b),"normal index-two cover");
 for t in [j,l] do
  Check(HasMaxes(t),Concatenation(Identifier(t)," complete maximal list"));
  names:=Maxes(t);orders:=List(names,n->Size(CharacterTable(n)));
  for x in [1..Length(names)] do
   Print(Identifier(t)," maximal=",names[x]," order=",orders[x],"\n");
  od;
  if Identifier(t)="J2" then Check(Maximum(orders)=6048,"J2 maximum proper subgroup order");
  else Check(Minimum(List(orders,x->Size(l)/x))=21,"L3(4) least proper index");fi;
 od;
 Print("G2(4): one outside class of size20800, centralizer12096; all maximal and cover checks passed.\n");
end;;
Main();
QUIT_GAP(0);
