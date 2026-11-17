# C0010, Li–Xia Table 1.2 row 19: rank of all stored U3(5)/A7 actions.
# GAP 4.15.1, CTblLib 1.3.11; run: gap -q -b /absolute/path/to/this/file
# Dataset coverage is an external ATLAS/CTblLib input, not proved here:
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/U3%285%29.html
# https://brauer.maths.qmul.ac.uk/Atlas/clas/U35/
# The induced trivial character's self-inner-product is the action rank.
Check := function(condition, label)
  if not condition then Print("FAIL: ", label, "\n"); ForceQuitGap(1); fi;
end;;
Check(GAPInfo.Version = "4.15.1", "GAP version");;
Check(LoadPackage("ctbllib") = true, "CTblLib available");;
Check(GAPInfo.PackagesInfo.ctbllib[1].Version = "1.3.11", "CTblLib version");;
socle := CharacterTable("U3(5)");;
Check(socle <> fail and Size(socle) = 126000, "socle table");;
names := Maxes(socle);;
Check(names = ["A7", "U3(5)M2", "U3(5)M3", "5^(1+2)+:8", "A6.2_3", "U3(5)M6", "U3(5)M7", "2.A5.2"], "complete maximal-subgroup metadata");;
tables := List(names, CharacterTable);;
Check(ForAll(tables, x -> x <> fail), "all maximal tables available");;
indices := Filtered([1..Length(tables)], i -> Size(tables[i]) = 2520);;
Check(indices = [1,2,3], "all order-2520 maximal classes");;
Check(ForAll([4..Length(tables)], i -> Size(tables[i]) mod 2520 <> 0), "no other maximal subgroup can contain A7");;
for i in indices do
  subgroup := tables[i];;
  Check(Size(socle) / Size(subgroup) = 50, "index 50");
  Check(Identifier(subgroup) = names[i], "table identifier");
  fusion := GetFusionMap(subgroup, socle);;
  Check(fusion <> fail, "stored subgroup fusion");
  induced := InducedClassFunctionsByFusionMap(subgroup, socle, [TrivialCharacter(subgroup)], fusion)[1];;
  Check(induced[1] = 50, "induced permutation degree");
  Check(ScalarProduct(socle, induced, induced) = 3, "permutation rank 3");
  Print(names[i], ": index 50, rank 3\n");
od;
QUIT_GAP(0);
