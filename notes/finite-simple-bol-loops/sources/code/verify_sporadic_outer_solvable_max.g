# Finite certificate for C0010: top-level maximal solvable stabilizers versus
# outside-involution class sums. GAP 4.15.1, CTblLib 1.3.11. The stored Maxes
# completeness and table identification are external inputs, not proved here.
Check:=function(b,msg) if not b then Print("FAIL ",msg,"\n");ForceQuitGap(1);fi;end;;
Check(GAPInfo.Version="4.15.1","GAP version");
Check(LoadPackage("ctbllib")=true,"CTblLib load");
Check(PackageInfo("ctbllib")[1].Version="1.3.11","CTblLib version");
Main:=function()
local sporadicNames,expectedOuter2,observedOuter2,name,t,ext,records,entry,s,a,fus,os,oa,ss,sa,i,outside,vals,sums,v,ms,id,x,deg,solv;
# Complete sporadic inventory and outer-group metadata are ATLAS/library inputs.
sporadicNames:=["M11","M12","M22","M23","M24","J1","J2","J3","J4",
 "HS","McL","He","Ru","Suz","ON","Co1","Co2","Co3","Fi22","Fi23",
 "Fi24'","HN","Ly","Th","B","M"];;
expectedOuter2:=["M12","M22","J2","J3","HS","McL","He","Suz","ON","HN","Fi22","Fi24'"];;
observedOuter2:=[];;
for name in sporadicNames do
 t:=CharacterTable(name);; Check(t<>fail and IsSporadicSimple(t),Concatenation(name," sporadic"));
 ext:=ExtensionInfoCharacterTable(t);;
 Check(ext[2] in ["","2"],Concatenation(name," outer metadata"));
 if ext[2]="2" then Add(observedOuter2,name);fi;
 Print("INVENTORY ",name," identifier=",Identifier(t)," outer=",ext[2],"\n");
od;
Check(Set(observedOuter2)=Set(expectedOuter2),"complete outer-two inventory");
records:=[
 ["M12",[792]], ["M22",[330,1386]], ["J2",[1800]],
 ["J3",[20520]], ["HS",[1100,23100]], ["McL",[113400]],
 ["He",[266560]], ["Suz",[370656,2358720]], ["ON",[2624832]],
 ["HN",[75240000]], ["Fi22",[61776,19459440,22239360]],
 ["Fi24'",[306936,5686767482760]] ];
for entry in records do
 s:=CharacterTable(entry[1]);; a:=CharacterTable(Concatenation(entry[1],".2"));;
 Check(s<>fail and a<>fail,Concatenation(entry[1]," tables"));
 Check(Size(a)=2*Size(s),Concatenation(entry[1]," index"));
 Check(ExtensionInfoCharacterTable(s)[2]="2","full automorphism group metadata");
 fus:=GetFusionMap(s,a);; Check(fus<>fail,Concatenation(entry[1]," fusion"));
 os:=OrdersClassRepresentatives(s);;oa:=OrdersClassRepresentatives(a);;
 ss:=SizesConjugacyClasses(s);;sa:=SizesConjugacyClasses(a);;
 Check(Sum(ss)=Size(s) and Sum(sa)=Size(a),"class sums");
 Check(ForAll([1..Length(sa)],i->sa[i]*SizesCentralizers(a)[i]=Size(a)),"centralizer/class size");
 Check(Sum(Set(fus),i->sa[i])=Size(s),"socle image size");
 Check(ForAll(Set(fus),j->Sum(Filtered([1..Length(fus)],i->fus[i]=j),i->ss[i])=sa[j]),"normal fusion class sums");
 Check(Filtered([1..Length(oa)],i->PowerMap(a,2)[i]=1)=Filtered([1..Length(oa)],i->oa[i] in [1,2]),"involution power map");
 Check(Length(fus)=Length(os),"fusion length");
 for i in [1..Length(fus)] do
  Check(fus[i]>=1 and fus[i]<=Length(oa) and os[i]=oa[fus[i]],"fusion/order");
 od;
 outside:=Filtered([1..Length(oa)],i->oa[i]=2 and not i in fus);;
 vals:=SortedList(List(outside,i->sa[i]));;
 Check(vals=SortedList(entry[2]),Concatenation(entry[1]," outside classes"));
 sums:=[0];;for v in vals do sums:=Union(sums,List(sums,x->x+v));od;
 Print("SOCLE ",entry[1]," outside=",vals," sums=",sums,"\n");
 for t in [s,a] do
  Check(HasMaxes(t),Concatenation(Identifier(t)," stored complete maximal list"));
  ms:=Maxes(t);; Check(ms<>fail and Length(ms)>0,Concatenation(Identifier(t)," max list"));
  Print("GROUP ",Identifier(t)," max_count=",Length(ms),"\n");
  for id in ms do
   x:=CharacterTable(id);;Check(x<>fail,Concatenation(id," table"));
   Check(Size(t) mod Size(x)=0,Concatenation(id," index integral"));
   deg:=Size(t)/Size(x);;solv:=IsSolvable(x);;
   Print("  ",id," order=",Size(x)," solv=",solv," index=",deg,"\n");
   if solv then Check(not deg in sums,Concatenation(Identifier(t)," ",id," class-sum collision"));fi;
  od;
 od;
od;
Print("All 26 sporadic outer groups and all 24 stored maximal lists checked.\n");
Print("All stored maximal-solvable indices differ from every outside class sum.\n");
end;;
Main();
QUIT_GAP(0);
