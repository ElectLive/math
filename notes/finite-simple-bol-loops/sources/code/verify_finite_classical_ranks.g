# C0010 finite classical rows 22, 25 and 27. GAP 4.15.1, CTblLib 1.3.11.
# Run: gap -q -b /absolute/path/to/verify_finite_classical_ranks.g
# Completeness of stored maximal lists and fusions is an ATLAS/CTblLib input:
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/O8%2B(2).html
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/O8%2B(3).html
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/O7%283%29.html
# The inner product of the induced trivial character is the coset-action rank.
Check := function(condition,label)
  if not condition then Print("FAIL: ",label,"\n"); ForceQuitGap(1); fi;
end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Check(LoadPackage("ctbllib")=true,"CTblLib available");;
Check(GAPInfo.PackagesInfo.ctbllib[1].Version="1.3.11","CTblLib version");;
Verify := function(name, target, degree, expected)
  local s, names, tables, candidates, i, h, fusion, induced;
  s := CharacterTable(name);
  Check(s<>fail,"socle table");
  names := Maxes(s);
  tables := List(names, CharacterTable);
  Check(ForAll(tables, x -> x<>fail),"all maximal tables available");
  candidates := Filtered([1..Length(tables)], i -> Size(tables[i]) mod target=0);
  Check(List(candidates,i->names[i])=expected,"complete target-containing maximal list");
  for i in candidates do
    h := tables[i];
    Check(Size(h)=target and Size(s)/Size(h)=degree,"maximal order and index");
    Check(Identifier(h)=names[i],"stored table identifier");
    fusion := GetFusionMap(h,s);
    Check(fusion<>fail,"stored subgroup fusion");
    induced := InducedClassFunctionsByFusionMap(h,s,[TrivialCharacter(h)],fusion)[1];
    Check(induced[1]=degree,"induced degree");
    Check(ScalarProduct(s,induced,induced)=3,"rank 3");
    Print(name," / ",names[i],": index ",degree,", rank 3\n");
  od;
end;;
Verify("O8+(2)",1451520,120,["S6(2)","O8+(2)M2","O8+(2)M3"]);;
Verify("O8+(3)",4585351680,1080,["O7(3)","O8+(3)M2","O8+(3)M3","O8+(3)M4","O8+(3)M5","O8+(3)M6"]);;
Verify("O7(3)",4245696,1080,["G2(3)","O7(3)M5"]);;
# U4(3): two L3(4) Maxes entries use the SAME table name and stored fusion.
# Inducing twice checks one fusion twice, not coverage of two subgroup classes;
# the separate outer-conjugacy input is needed and is not certified here.
QUIT_GAP(0);
