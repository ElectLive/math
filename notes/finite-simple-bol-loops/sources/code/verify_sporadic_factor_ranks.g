# C0010 Li-Xia sporadic factor actions. GAP 4.15.1 and CTblLib 1.3.11.
# Run: gap -q -b /absolute/path/to/file
# Completeness and correctness of maximal-class lists and stored fusions are
# ATLAS/CTblLib data inputs; this is not an independent subgroup enumeration.
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/J2.2.html
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/HS.html
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/HS.2.html
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/Suz.2.html
Check:=function(ok,label) if not ok then Print("FAIL: ",label,"\n"); ForceQuitGap(1); fi; end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Check(LoadPackage("ctbllib")=true,"CTblLib available");;
Check(GAPInfo.PackagesInfo.ctbllib[1].Version="1.3.11","CTblLib version");;
Verify:=function(name,degree,order,expected)
 local s,names,tables,idx,h,f,c;
 s:=CharacterTable(name); Check(s<>fail and Size(s)=order,"ambient table");
 names:=Maxes(s); tables:=List(names,CharacterTable);
 Check(ForAll(tables,x->x<>fail),"all maximal tables available");
 idx:=Filtered([1..Length(names)],i->Size(tables[i])*degree=order);
 Check(List(idx,i->names[i])=expected,"all maximal classes of required order");
 for h in tables{idx} do
  f:=GetFusionMap(h,s); Check(f<>fail,"stored fusion");
  c:=InducedClassFunctionsByFusionMap(h,s,[TrivialCharacter(h)],f)[1];
  Check(c[1]=degree and ScalarProduct(s,c,c)=3,"degree and rank");
  Print(name," / ",Identifier(h),": degree ",degree,", rank 3\n");
 od;
end;;
Verify("J2.2",100,1209600,["U3(3).2"]);;
Verify("HS",100,44352000,["M22"]);;
Verify("HS.2",100,88704000,["M22.2"]);;
Verify("Suz.2",1782,896690995200,["G2(4).2"]);;
QUIT_GAP(0);
