# C0010: small PSL2 full socles (A5 and A6).
# GAP 4.15.1; uses core finite-group algorithms, not stored subgroup tables.
# This proves only the finite subgroup assertions consumed by the manuscript.
Check := function(ok, label)
    if not ok then
        Print("FAIL: ", label, "\n");
        ForceQuitGap(1);
    fi;
end;;
Check(GAPInfo.Version = "4.15.1", "GAP version");;

a5 := AlternatingGroup(5);;
Check(ForAll(MaximalSubgroupClassReps(a5), IsSolvableGroup),
      "every proper A5 subgroup is solvable");;
a6 := AlternatingGroup(6);;
a6max := MaximalSubgroupClassReps(a6);;
for subgroup in a6max do
    if not IsSolvableGroup(subgroup) then
        Check(IsomorphismGroups(subgroup, a5) <> fail,
              "every nonsolvable maximal A6 subgroup is A5");
    fi;
od;

aut := AutomorphismGroup(a6);;
Check(Size(aut) = 1440, "Aut A6 order");;
permIso := IsomorphismPermGroup(aut);;
Check(IsInjective(permIso), "faithful permutation model");;
p := Image(permIso);;
s := DerivedSubgroup(p);;
Check(Size(s) = 360 and IsomorphismGroups(s, a6) <> fail,
      "derived subgroup is A6");;
q := NaturalHomomorphismByNormalSubgroup(p, s);;
out := Image(q);;
Check(Size(out) = 4 and IsElementaryAbelian(out), "outer quotient V4");;
outerClasses := ConjugacyClassesSubgroups(out);;
Check(Length(outerClasses) = 5, "all five outer subgroups");;

Run := function()
    local oc, m, max, degrees;
    for oc in outerClasses do
        m := PreImage(q, Representative(oc));
        max := MaximalSubgroupClassReps(m);
        degrees := SortedList(List(max, i -> Index(m, i)));
        Check(not (30 in degrees) and not (60 in degrees),
              "no primitive index 30 or 60");
        Print("outer order ", Size(m)/Size(s),
              "; all maximal indices ", degrees, "\n");
    od;
end;;
Run();;
Print("PASS: small-socle subgroup and primitive-index assertions\n");
QUIT_GAP(0);
