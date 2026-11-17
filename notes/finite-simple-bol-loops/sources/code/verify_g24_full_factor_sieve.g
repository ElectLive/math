# Proposed C0010 CTblLib data check; completeness and table identifications are external.
(function()
 local ck,s,a,u,t,ms,mt,expected,actual,x,y,pairs,names,i,cs,chi,p;
 ck:=function(b,msg) if not b then Error(msg);fi;end;
 ck(LoadPackage("ctbllib")<>fail,"CTblLib unavailable");
 ck(GAPInfo.Version="4.15.1" and PackageInfo("ctbllib")[1].Version="1.3.11","versions");
 for names in [["G2(4)","U3(4).2"],["G2(4).2","U3(4).4"]] do
  t:=CharacterTable(names[1]);u:=CharacterTable(names[2]);
  ck(t<>fail and u<>fail and HasMaxes(t),"missing table/max list");
  ms:=Maxes(t); pairs:=[];
  if names[1]="G2(4)" then expected:=["J2","2^(2+8):(3xA5)","2^(4+6):(A5x3)","U3(4).2","3.L3(4).2_3","U3(3).2","A5xA5","L2(13)"];
  else expected:=["G2(4)","J2.2","2^(2+8):(3xA5):2","2^(4+6):(A5x3):2","U3(4).4","3.L3(4).2^2","2xU3(3).2","(A5xA5):2","L2(13).2"];fi;
  ck(ms=expected,"complete stored maximal list changed");
  for i in [1..Length(ms)] do for x in [i..Length(ms)] do
   y:=CharacterTable(ms[i]);p:=CharacterTable(ms[x]);
   if ms[i]<>"G2(4)" and ms[x]<>"G2(4)" and Size(y)<Size(t) and Size(p)<Size(t) and Size(p) mod (Size(t)/Size(y))=0 then Add(pairs,Set([ms[i],ms[x]]));fi;
  od;od;
  if names[1]="G2(4)" then expected:=List([["J2","U3(4).2"],["3.L3(4).2_3","U3(4).2"],["U3(3).2","U3(4).2"]],Set);
  else expected:=List([["J2.2","U3(4).4"],["3.L3(4).2^2","U3(4).4"],["2xU3(3).2","U3(4).4"]],Set);fi;
  ck(Set(pairs)=Set(expected),Concatenation("max pairs ",names[1]));
  ck(GetFusionMap(u,t)<>fail,"fusion unavailable");chi:=InducedClassFunction(TrivialCharacter(u),t);
  ck(chi[1]=2016 and ScalarProduct(t,chi,chi)=3,"rank");
  Print(names[1],": three maximal order-compatible pairs; degree 2016 rank 3\n");
 od;
 s:=CharacterTable("G2(4)");ms:=Maxes(s);pairs:=[];
 for i in [1..Length(ms)] do for x in [i..Length(ms)] do
  if (2*Size(CharacterTable(ms[i]))*Size(CharacterTable(ms[x]))) mod Size(s)=0 then Add(pairs,Set([ms[i],ms[x]]));fi;
 od;od;
 expected:=List([["J2","U3(4).2"],["3.L3(4).2_3","U3(4).2"],["U3(3).2","U3(4).2"]],Set);
 ck(Set(pairs)=Set(expected),"socle intersection order sieve");
 Print("S intersection sieve holds even allowing outer factor 2\n");
 u:=CharacterTable("U3(4)");ck(Size(u)=62400 and HasMaxes(u),"U3 input");
 ck(Maxes(u)=["2^(2+4):15","5xA5","5^2:S3","13:3"],"U3 maximal metadata");
 ck(GetFusionMap(u,CharacterTable("U3(4).2"))<>fail and GetFusionMap(u,CharacterTable("U3(4).4"))<>fail,"U3 embedding fusions");
 actual:=Filtered(Maxes(u),x->Size(CharacterTable(x)) mod 13=0);
 ck(actual=["13:3"],"U3 13-maximal list");
 a:=CharacterTable("G2(4).2");cs:=SizesCentralizers(a);
 actual:=List(Filtered([1..Length(cs)],i->OrdersClassRepresentatives(a)[i]=2),i->cs[i]);
 ck(actual=[122880,7680,24192],"involution centralizers");
 ck(ForAll(actual,x->x mod 62400<>0),"centralizer divisibility");
 Print("U3: unique 13-maximal 13:3; no involution centralizer contains U3\n");
 ck(GetFusionMap(s,a)<>fail,"normal fusion");
 ck(Filtered([1..Length(OrdersClassRepresentatives(s))],i->OrdersClassRepresentatives(s)[i]=2)=[2,3] and List([2,3],i->GetFusionMap(s,a)[i])=[2,3],"socle involution classes/fusion");
 ck(Filtered([1..Length(cs)],i->OrdersClassRepresentatives(a)[i]=2 and not i in GetFusionMap(s,a))=[25],"outer involution class");
 ck(Size(a)/cs[25]=20800 and cs[25]/2=12096,"outer class size and socle centralizer");
 ck(List([2,3],i->ClassMultiplicationCoefficient(a,25,25,i))=[320,80],"outer-square coefficients");
 Print("canonical outer class square covers both socle involution classes\n");
end)();
QUIT_GAP(0);
