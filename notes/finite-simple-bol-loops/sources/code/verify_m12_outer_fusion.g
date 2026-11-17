# Supplementary finite check for the paired sporadic classification.
# GAP 4.15.1, using its MathieuGroup(12) and permutation-group algorithms.
# No external files, network calls or generated artifacts.
Check := function(ok, label)
  if not ok then Print("FAIL: ", label, "\n"); ForceQuitGap(1); fi;
end;;
Check(GAPInfo.Version = "4.15.1", "GAP version");;
VerifyFusion := function()
  local g, classes, selected, aut, inner, outer, c, h, ih, found, d;
  g := MathieuGroup(12);
  Check(Size(g) = 95040 and IsSimpleGroup(g), "M12 order and simplicity");
  classes := ConjugacyClassesSubgroups(g);
  selected := Filtered(classes, c -> Size(Representative(c)) = 144);
  Check(Length(classes) = 147 and Length(selected) = 2, "subgroup class counts");
  aut := AutomorphismGroup(g);
  inner := InnerAutomorphismsAutomorphismGroup(aut);
  Check(Size(aut) = 190080 and Size(inner) = 95040, "automorphism orders");
  outer := First(GeneratorsOfGroup(aut), x -> not x in inner);
  Check(outer <> fail, "outer automorphism exists");
  for c in selected do
    h := Representative(c);
    ih := Image(outer, h);
    Check(not IsConjugate(g, ih, h), "outer moves the class");
    found := false;
    for d in selected do
      if IsConjugate(g, ih, Representative(d)) then found := true; fi;
    od;
    Check(found, "image belongs to the other selected class");
  od;
  Print("PASS: 147 M12 subgroup classes; two order-144 classes fused by Out(M12)\n");
end;;
VerifyFusion();
QUIT_GAP(0);
