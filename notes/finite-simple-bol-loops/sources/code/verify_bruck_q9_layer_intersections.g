# PGL2(9) module-level control for the noncentral Frattini-layer obstruction.
# Run with GAP 4.15.1. No Bruck envelope or Frattini realization is constructed.
# Uses GAP's irreducible-module construction and MeatAxe submodule algorithms.

CheckLayer := function(condition, label)
    if not condition then
        Print("FAIL: ", label, "\n");
        ForceQuitGap(1);
    fi;
end;;

a := PGL(2, 9);;
CheckLayer(Size(a) = 720, "PGL group order");
moduleData := IrreducibleModules(a, GF(2), 16);;
CheckLayer(SortedList(List(moduleData[2], x -> x.dimension)) = [1, 8, 16],
           "binary simple dimensions");
v := First(moduleData[2], x -> x.dimension = 16);;
CheckLayer(MTX.IsIrreducible(v), "irreducibility of selected module");
matrixGroup := Group(v.generators);;
representation := GroupHomomorphismByImages(
    a, matrixGroup, moduleData[1], v.generators);;
CheckLayer(representation <> fail and IsGroupHomomorphism(representation)
           and Size(Image(representation)) = 720,
           "faithful generator-matched representation");

b := Stabilizer(a, 1);;
socle := DerivedSubgroup(a);;
CheckLayer(Size(b) = 72 and Size(socle) = 360, "Borel and PSL orders");
bMatrices := List(GeneratorsOfGroup(b), x -> Image(representation, x));;
bModule := GModuleByMats(bMatrices, GF(2));;
submoduleBases := MTX.BasesSubmodules(bModule);;
CheckLayer(SortedList(List(submoduleBases, Length)) = [0, 8, 8, 8, 16],
           "complete Borel submodule lattice");
bLines := List(Filtered(submoduleBases, x -> Length(x) = 8),
               x -> VectorSpace(GF(2), x));;

outerInvolutions := Filtered(Elements(a), x -> Order(x) = 2 and not x in socle);;
CheckLayer(Length(outerInvolutions) = 36, "prescribed outer involutions");
CheckLayer(Length(Orbit(b, outerInvolutions[1], OnPoints)) = 36,
           "Borel transitivity on the outer class");
identityMatrix := IdentityMat(16, GF(2));;
ranks := [];;
intersectionDimensions := [];;
for t in outerInvolutions do
    displacement := VectorSpace(GF(2),
        BaseMat(identityMatrix + Image(representation, t)));;
    Add(ranks, Dimension(displacement));
    for u in bLines do
        Add(intersectionDimensions, Dimension(Intersection(u, displacement)));
    od;
od;
CheckLayer(Set(ranks) = [6], "all outer displacement ranks");
CheckLayer(Length(intersectionDimensions) = 108
           and Set(intersectionDimensions) = [0], "all Borel-line intersections");
Print("PGL2(9) layer control: binary simples 1,8,16; B-submodules 0,8,8,8,16;\n");
Print("36 outer ranks = 6; all 108 line intersections = 0.\n");
QUIT_GAP(0);
