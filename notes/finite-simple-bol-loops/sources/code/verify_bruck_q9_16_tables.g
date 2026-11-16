# CTblLib table inputs for the 16-dimensional F2 PGL(2,9) module.
# The character tables and their identifications are external inputs.
Check := function(condition, message)
  if condition <> true then
    Print("FAIL: ", message, "\n");
    ForceQuitGap(1);
  fi;
end;;
Check(LoadPackage("ctbllib") = true, "CTblLib");
Check(GAPInfo.Version = "4.15.1", "GAP version");
Check(PackageInfo("ctbllib")[1].Version = "1.3.11", "CTblLib version");
A := CharacterTable("PGL(2,9)");;
T := CharacterTable("A6");;
Check(Identifier(A) = "A6.2_2" and Size(A) = 720 and Size(T) = 360, "groups");
ab := A mod 2;;
Check(List(Irr(ab),x->x[1]) = [1,8,8,8], "Brauer degrees");
Check(List(Irr(ab),x->x[2]) = [1,-1,-1,-1], "order-three values");
Check(Irr(ab)[3][3] + Irr(ab)[4][3] = 1 and
      Irr(ab)[3][4] + Irr(ab)[4][4] = 1, "Galois-pair values");
Check(GaloisCyc(Irr(ab)[3][3],2) = Irr(ab)[4][3] and
      GaloisCyc(Irr(ab)[3][4],2) = Irr(ab)[4][4], "Frobenius fusion");
dec := DecompositionMatrix(ab);;
Check(dec = [[1,0,0,0],[1,0,0,0],[2,1,0,0],[0,0,1,0],
             [0,0,1,0],[0,0,0,1],[0,0,0,1],[1,1,0,0],
             [1,1,0,0],[2,1,0,0],[2,1,0,0]], "decomposition matrix");
Check(SizesCentralizers(A)[7] = 20 and OrdersClassRepresentatives(A)[7] = 2,
      "outer involution class");
Check(PowerMap(A,2)[10] = 6 and PowerMap(A,2)[11] = 5 and
      PowerMap(A,5)[10] = 7 and PowerMap(A,5)[11] = 7, "torus class powers");
Check(GetFusionMap(T,A) = [1,2,3,3,4,5,6], "A6 fusion");
Check(List(Irr(T),x->x[1]) = [1,5,5,8,8,9,10], "A6 degrees");
blocks := PrimeBlocks(T,2);;
Check(blocks.block[4] <> blocks.block[1] and blocks.defect[blocks.block[4]] = 0 and
      blocks.block[5] <> blocks.block[1] and blocks.defect[blocks.block[5]] = 0,
      "A6 defect-zero characters");
ScalarRow := function(table, character)
  return List(Irr(table),x->ScalarProduct(table,character,x));
end;;
for datum in [[4,4],[6,5]] do
  chi := Irr(A)[datum[1]];;
  rest := RestrictedClassFunction(chi,T);;
  expected := List(Irr(T),x->0);;
  expected[datum[2]] := 1;;
  Check(ScalarRow(T,rest) = expected, "A6 restriction");
  Check(chi[1] = 8 and chi[7] = 2, "ordinary values");
  Check((chi[1]+2*chi[5]+2*chi[6])/5 = 2, "C5 fixed dimension");
  Check((chi[7]+2*chi[10]+2*chi[11])/5 = 0, "t trace on C5 fixed space");
od;
Print("PGL2(9) 16-dimensional table checks passed\n");
QUIT_GAP(0);
