# Exhaustive Goursat quotient-order obstruction for A7, A8, A9.
# GAP 4.15.1. The required kernels are nontrivial: if one is trivial,
# the Goursat subgroup has the order of the opposite proper projection.
# Enumerate one representative of every subgroup class, all its normal
# subgroups, and the pairs (subgroup order, quotient order). Test the
# necessary order equality; no quotient-isomorphism or embedding test is used.
Check := function(ok, label)
  if not ok then Print("FAIL: ", label, "\n"); ForceQuitGap(1); fi;
end;;
Check(GAPInfo.Version = "4.15.1", "GAP version");;
Verify := function(n, expected_classes)
  local g, classes, entries, cl, h, normal, quotient_order, candidates;
  g := AlternatingGroup(n);
  classes := ConjugacyClassesSubgroups(g);
  Check(Length(classes) = expected_classes, "subgroup class count");
  entries := [];
  for cl in classes do
    h := Representative(cl);
    if Size(h) < Size(g) then
      for normal in NormalSubgroups(h) do
        quotient_order := Index(h, normal);
        if quotient_order > 2 and quotient_order < Size(h) then
          AddSet(entries, [Size(h), quotient_order]);
        fi;
      od;
    fi;
  od;
  candidates := Number(Cartesian(entries, entries),
    pair -> pair[1][2] = pair[2][2] and
            pair[1][1] * pair[2][1] = Size(g) * pair[1][2]);
  Check(candidates = 0, "common quotient order candidate");
  Print("A", n, ": subgroup classes = ", Length(classes),
        ", quotient-order candidates = ", candidates, "\n");
end;;
Verify(7,40);;
Verify(8,137);;
Verify(9,223);;
QUIT_GAP(0);
