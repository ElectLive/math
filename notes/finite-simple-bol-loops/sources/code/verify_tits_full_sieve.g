# Proposed C0010 Tits full-socle finite-data sieve; CTbl classifications are inputs.
(function()
 local check,s,a,sm,am,expect,i,j,f,o;
 check:=function(c,msg) if not c then Error(msg);fi;end;
 check(LoadPackage("ctbllib")<>fail,"ctbllib unavailable");
 check(GAPInfo.Version="4.15.1" and PackageInfo("ctbllib")[1].Version="1.3.11","version mismatch");
 s:=CharacterTable("2F4(2)'");a:=CharacterTable("2F4(2)");
 check(Size(s)=17971200 and Size(a)=2*Size(s),"orders");
 check(HasMaxes(s) and HasMaxes(a),"missing maximal lists");
 sm:=Maxes(s);am:=Maxes(a);
 expect:=["L3(3).2","2F4(2)'M2","2.2^8.f20","L2(25)","2^2.2^8:s3","A6.2^2","2F4(2)'M7","5^2:4A4"];
 check(sm=expect,"socle maximal list");
 expect:=["2F4(2)'","2.[2^9]:5:4","L2(25).2_3","2^2.[2^9]:S3","Fi22N5","3^(1+2):SD16","13:12"];
 check(am=expect,"automorphism maximal list");
 for i in [1..Length(sm)] do for j in [i..Length(sm)] do
  check((2*Size(CharacterTable(sm[i]))*Size(CharacterTable(sm[j]))) mod Size(s)<>0,"potential pair");
 od;od;
 f:=GetFusionMap(s,a);check(f<>fail,"fusion absent");o:=OrdersClassRepresentatives(a);
 check(Filtered([1..Length(o)],i->o[i]=2 and not i in f)=[],"outside involution");
 Print("Tits: 8 socle maximals, 7 full maximals, zero factor-order pairs, no outside involutions\n");
end)();QUIT_GAP(0);
