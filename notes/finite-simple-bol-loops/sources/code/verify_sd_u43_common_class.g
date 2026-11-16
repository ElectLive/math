# CTblLib character-table evidence for the U4(3) common-square condition.
# The tables and recorded class fusions are external inputs.
Check := function(condition, message)
  if condition <> true then
    Print("FAIL: ", message, "\n");
    ForceQuitGap(1);
  fi;
end;;
Check(LoadPackage("ctbllib") = true, "CTblLib load");
Check(GAPInfo.Version = "4.15.1", "GAP version");
Check(PackageInfo("ctbllib")[1].Version = "1.3.11", "CTblLib version");
T := CharacterTable("U4(3)");;
A := CharacterTable("U4(3).D8");;
Check(T <> fail and A <> fail, "table availability");
Check(Size(T) = 3265920 and Size(A) = 26127360, "orders");
Check(Positions(OrdersClassRepresentatives(T),2) = [2], "unique T involution class");
Check(Positions(OrdersClassRepresentatives(A),2) = [2,15,16,39,40,53], "Aut involution classes");
Check(ClassMultiplicationCoefficient(T,2,2,2) = 66, "inner structure constant");
covered := [2];;
for datum in [ ["U4(3).2_1", [[19,15,12],[20,16,120]]],
               ["U4(3).2_2", [[19,39,2],[20,40,90]]],
               ["U4(3).2_3", [[16,53,72]]] ] do
  H := CharacterTable(datum[1]);;
  Check(H <> fail and Size(H) = 2*Size(T), "index-two table");
  ft := GetFusionMap(T,H);; fa := GetFusionMap(H,A);;
  Check(ft <> fail and fa <> fail, "fusion maps");
  Check(ft[2] = 2, "target involution class fusion");
  outer := Difference(Positions(OrdersClassRepresentatives(H),2), Set(ft));;
  Check(outer = List(datum[2], x -> x[1]), "all outer involution classes");
  for item in datum[2] do
    Check(fa[item[1]] = item[2], "outer-to-Aut fusion");
    Check(ClassMultiplicationCoefficient(H,item[1],item[1],ft[2]) = item[3], "square coefficient");
    Add(covered,item[2]);
  od;
od;
Check(Set(covered) = Positions(OrdersClassRepresentatives(A),2), "full Aut coverage");
Print("U4(3) common-class table checks passed\n");
QUIT_GAP(0);
