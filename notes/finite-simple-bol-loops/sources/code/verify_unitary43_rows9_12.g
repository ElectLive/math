# C0010 unitary rows 9-12: character-table checks; CTblLib tables/fusions are inputs.
(function()
 local check, s,a,o,sz,f,i,t;
 check:=function(b,msg) if not b then Error(msg); fi; end;
 check(LoadPackage("ctbllib")<>fail,"CTblLib unavailable");
 check(GAPInfo.Version="4.15.1" and PackageInfo("ctbllib")[1].Version="1.3.11","wrong version");
 for t in ["A5","A6"] do
  s:=CharacterTable(t); o:=OrdersClassRepresentatives(s);
  check(Length(Filtered(o,x->x=2))=1,Concatenation(t," involution classes"));
 od;
 s:=CharacterTable("L2(7)");a:=CharacterTable("L2(7).2");
 check(Size(s)=168 and Size(a)=336,"L2(7) orders");
 o:=OrdersClassRepresentatives(a);sz:=List([1..Length(o)],i->Size(a)/SizesCentralizers(a)[i]);
 check(Filtered([1..Length(o)],i->o[i]=2)=[2,6] and sz[2]=21 and sz[6]=28,"L2(7) involution classes");
 check(Filtered([1..Length(o)],i->o[i]=3)=[3] and sz[3]=56,"L2(7) order-three class");
 check(OrdersClassRepresentatives(s)[2]=2 and Size(s)/SizesCentralizers(s)[2]=21,"L2(7) inner orbit");
 f:=GetFusionMap(s,a);check(f=[1,2,3,4,5,5],"L2(7) fusion");
 check(ClassMultiplicationCoefficient(a,2,2,3)=3 and ClassMultiplicationCoefficient(a,6,6,3)=3,"L2(7) squares");
 s:=CharacterTable("U4(2)");a:=CharacterTable("U4(2).2");
 check(Size(s)=25920 and Size(a)=51840,"U4(2) orders");
 o:=OrdersClassRepresentatives(a);sz:=List([1..Length(o)],i->Size(a)/SizesCentralizers(a)[i]);
 check(Filtered([1..Length(o)],i->o[i]=2)=[2,3,16,17],"U4(2) involution classes");
 check(List([2,3,16,17],i->sz[i])=[45,270,36,540],"U4(2) involution sizes");
 check(List([2,3],i->Size(s)/SizesCentralizers(s)[i])=[45,270],"U4(2) inner orbits");
 f:=GetFusionMap(s,a);check(f=[1,2,3,4,4,5,6,7,8,9,10,10,11,11,12,13,14,14,15,15],"U4(2) fusion");
 check(List([2,3,16,17],i->ClassMultiplicationCoefficient(a,i,i,3))=[2,18,2,18],"U4(2) class-three squares");
 check(ClassMultiplicationCoefficient(a,2,2,2)=0,"V4 argument");
 Print("A5/A6 single involution classes; L2(7), U4(2) fusion and class-square checks passed\n");
end)(); QUIT_GAP(0);
