# C0010: PSU4(5) canonical S: CTblLib input and natural SU Sylow check.
(function()
 local ck,s,t,o,f,inv,idx,expected,sizes,counts,i,j,k,p,g,z,cs,m,ct,unions,n,diag;
 ck:=function(x,msg) if not x then Error(msg);fi;end;
 ck(LoadPackage("ctbllib")<>fail,"CTblLib unavailable");
 ck(GAPInfo.Version="4.15.1" and PackageInfo("ctbllib")[1].Version="1.3.11","version mismatch");
 s:=CharacterTable("U4(5)");ck(Size(s)=14742000000,"S order");
 ck(ExtensionInfoCharacterTable(s)=["2","2^2"],"extension metadata");
 o:=OrdersClassRepresentatives(s); inv:=Filtered([1..Length(o)],i->o[i]=2);
 ck(inv=[2,3] and List(inv,i->Size(s)/SizesCentralizers(s)[i])=[170625,236250],"inner classes");
 expected:=[[[72,73,74],[1575,1575,1023750],[[0,2],[0,2],[1950,1300]]],[[91],[13000],[[40,0]]],[[65],[945000],[[1800,1200]]]];
 for k in [1..3] do
  t:=CharacterTable(Concatenation("U4(5).2_",String(k)));ck(t<>fail and Size(t)=2*Size(s),"extension order");
  if k=1 then ck(PositionSublist(InfoText(t),"PSigmaU(4,5)")<>fail,"semilinear metadata"); fi;
  if k=2 then ck(PositionSublist(InfoText(t),"PGU(4,5)")<>fail,"diagonal metadata"); fi;
  f:=GetFusionMap(s,t);ck(f<>fail and Length(f)=NrConjugacyClasses(s) and f{[2,3]}=[2,3],"involution fusion");
  o:=OrdersClassRepresentatives(t);idx:=Filtered([1..Length(o)],i->o[i]=2 and not i in f);
  sizes:=List(idx,i->Size(t)/SizesCentralizers(t)[i]);
  counts:=List(idx,i->List(inv,j->ClassMultiplicationCoefficient(t,i,i,f[j])));
  ck(idx=expected[k][1] and sizes=expected[k][2] and counts=expected[k][3],"outer classes or squares");
  unions:=[];for i in [1..2^Length(idx)-1] do
   n:=Sum(Filtered([1..Length(idx)],j->QuoInt(i,2^(j-1)) mod 2=1),j->sizes[j]);
   Add(unions,[i,n,Size(s) mod n,QuoInt(Size(s),n)]);
  od;
  if k=1 then ck(List(unions,x->x[3])=[0,0,0,0,902475,902475,850500],"union residues .2_1"); fi;
  if k=2 then ck(unions[1][3]=0 and unions[1][4]=1134000,"diagonal count"); fi;
  if k=3 then ck(unions[1][3]=0 and unions[1][4]=15600,".2_3 count"); fi;
  Print(".2_",k," outside ",sizes," square coefficients ",counts," union [mask,size,remainder,H] ",unions,"\n");
 od;
 g:=SpecialUnitaryGroup(4,5);ck(Size(g)=29484000000,"SU order");p:=SylowSubgroup(g,2);z:=Centre(g);
 ck(Size(p)=256 and Size(z)=2 and IsSubgroup(p,z),"Sylow and center");
 cs:=Filtered(ConjugacyClassesSubgroups(p),x->Size(Representative(x))=128);ck(Length(cs)=7,"index-two count");
 ct:=[];for i in cs do m:=Representative(i);ck(IsNormal(p,m),"index-two normal");Add(ct,Length(Filtered(Elements(m),j->j^2 in z and j^2<>One(g))));od;
 ck(ForAll(ct,x->x>0) and Set(ct)=[20,28,36,44],"Sylow witnesses");
 Print("All seven index-two Sylow subgroups contain square-minus-one lifts: ",ct,"\n");
end)(); QUIT_GAP(0);
