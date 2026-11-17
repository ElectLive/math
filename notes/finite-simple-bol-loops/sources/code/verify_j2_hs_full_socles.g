# C0010 J2/HS stored-data certificate; maximal-list completeness is an input.
VerifyJ2HS := function()
 local rows, r, a, b, f, chi, nam, t, ext, ord, cent, ct, target,
       lists, item, names, tables, wanted, selected, size, i, j, targetsize,
       subord, superord, subpow, superpow, pair, u, v;
 Assert(0,LoadPackage("ctbllib")=true);
 Assert(0,GAPInfo.Version="4.15.1" and PackageInfo("ctbllib")[1].Version="1.3.11");
 lists:=[
  ["J2",["U3(3)","3.A6.2_2","2^1+4b:a5","2^2+4.3xs3","a4xa5","a5xd10","L3(2).2","5^2:D12","A5"]],
  ["J2.2",["J2","U3(3).2","3.A6.2^2","2^(1+4).S5","2^(2+4):(S3xS3)","(A4xA5):2","(A5xD10).2","L3(2).2x2","5^2:(4xS3)","A5.2"]],
  ["HS",["M22","U3(5).2","HSM3","L3(4).2_1","A8.2","2^4.s6","4^3:psl(3,2)","M11","HSM9","4.2^4.S5","2xa6.2^2","5:4xa5"]],
  ["HS.2",["HS","M22.2","L3(4).2^2","S8x2","2^5.S6","4^3:(L3(2)x2)","2^(1+6)_+:S5","(2xA6.2^2).2","HS.2N5","5:4xS5"]]
 ];
 for item in lists do
  t:=CharacterTable(item[1]); Assert(0,t<>fail and Maxes(t)=item[2]);
  names:=Maxes(t); tables:=List(names,CharacterTable); Assert(0,ForAll(tables,x->x<>fail));
  for i in [1..Length(tables)] do Assert(0,Size(t) mod Size(tables[i])=0); od;
  if item[1]="J2" then wanted:=[[6048,["U3(3)"]]];
  elif item[1]="J2.2" then wanted:=[[12096,["U3(3).2"]]];
  elif item[1]="HS" then wanted:=[[443520,["M22"]],[252000,["U3(5).2","HSM3"]]];
  else wanted:=[[887040,["M22.2"]]]; fi;
  for target in wanted do
   selected:=Filtered([1..Length(names)],j->Size(tables[j])=target[1]);
   Assert(0,names{selected}=target[2]);
   Print(item[1]," maximal order ",target[1]," entries ",names{selected},"\n");
  od;
 od;
 rows:=[["J2","U3(3)"],["J2.2","U3(3).2"],["HS","M22"],["HS.2","M22.2"]];
 for r in rows do
  a:=CharacterTable(r[1]); b:=CharacterTable(r[2]); f:=GetFusionMap(b,a);
  Assert(0,f<>fail and Size(a)/Size(b)=100);
  chi:=InducedClassFunctionsByFusionMap(b,a,[TrivialCharacter(b)],f)[1];
  Assert(0,chi[1]=100 and ScalarProduct(a,chi,chi)=3);
  Print(r[1],"/",r[2]," degree 100 rank 3\n");
 od;
 for nam in ["J2","HS"] do
  t:=CharacterTable(nam); a:=CharacterTable(Concatenation(nam,".2"));
  f:=GetFusionMap(t,a); Assert(0,f<>fail and Size(a)=2*Size(t));
  subord:=OrdersClassRepresentatives(t); superord:=OrdersClassRepresentatives(a);
  subpow:=PowerMap(t,2); superpow:=PowerMap(a,2);
  for i in [1..Length(f)] do
   Assert(0,subord[i]=superord[f[i]] and f[subpow[i]]=superpow[f[i]]);
  od;
  for j in Set(f) do
   targetsize:=Size(a)/SizesCentralizers(a)[j];
   Assert(0,Sum(Filtered([1..Length(f)],i->f[i]=j),i->Size(t)/SizesCentralizers(t)[i])=targetsize);
  od;
  ord:=OrdersClassRepresentatives(a); cent:=SizesCentralizers(a);
  ext:=Filtered([1..Length(ord)],i->ord[i]=2 and not i in f);
  ct:=List(ext,i->cent[i]/2);
  if nam="J2" then Assert(0,ct=[336]); else Assert(0,Set(ct)=[1920,40320] and Length(ct)=2); fi;
  Print(nam," outside S-centralizers ",ct,"\n");
 od;
 for pair in [["U3(3)","J2"],["M22","HS"],["U3(5).2","HS"],["HSM3","HS"],["U3(5)","U3(5).2"]] do
  a:=CharacterTable(pair[2]); b:=CharacterTable(pair[1]); f:=GetFusionMap(b,a);
  Assert(0,f<>fail and Size(a) mod Size(b)=0);
  Print("stored fusion ",pair," index ",Size(a)/Size(b),"\n");
 od;
 # HSM3 structure as the second U3(5).2 class is a cited metadata input;
 # equality of ordinary character tables alone would not establish it.
 Assert(0,PositionSublist(InfoText(CharacterTable("HSM3")),"differs from HSM2 only by fusion map")<>fail);
 Print("all stored maximal filters, ranks, fusions, and centralizers passed\n");
end;;
VerifyJ2HS();;
QUIT_GAP(0);
