# Proposed C0010 reversed Li–Xia Table 1.2 rows 22–28 data checks.
# GAP 4.15.1, CTblLib 1.3.11. Run only after reviewing this source:
#   gap -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_reversed_finite_orthogonal.g
# Stored table names, full-Aut identifications, maximal-list completeness and
# conjugacy-class power maps are external ATLAS/CTblLib data inputs. This is
# neither a subgroup-classification proof nor a loop or folder enumeration.
# Socle metadata:
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/O7%283%29.html
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/O8%2B(2).html
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/O8%2B(3).html

Check := function(condition, label)
  if condition <> true then
    Print("FAIL: ", label, "\n");
    ForceQuitGap(1);
  fi;
end;;
Check(GAPInfo.Version = "4.15.1", "GAP version");;
Check(LoadPackage("ctbllib") = true, "CTblLib availability");;
Check(PackageInfo("ctbllib")[1].Version = "1.3.11", "CTblLib version");;

# Inspect every entry of the stored maximal-subgroup list, including those
# that cannot contain the target by Lagrange. Duplicates are retained.
CheckMaxes := function(name, order, target, expected)
  local t, names, tabs, i, actual;
  t := CharacterTable(name);
  Check(t <> fail and Identifier(t) = name and Size(t) = order,
        Concatenation(name, " socle identifier/order"));
  names := Maxes(t);
  Check(IsList(names) and Length(names) > 0, Concatenation(name, " Maxes"));
  tabs := List(names, CharacterTable);
  Check(ForAll(tabs, x -> x <> fail), Concatenation(name, " maximal tables"));
  for i in [1..Length(tabs)] do
    Check(Identifier(tabs[i]) = names[i], "maximal table identifier");
  od;
  actual := List(Filtered([1..Length(names)], i -> Size(tabs[i]) mod target = 0),
                 i -> [names[i], Size(tabs[i])]);
  Check(actual = expected, Concatenation(name, " target-containing Maxes"));
  Print(name, ", target ", target, ": ", Length(actual), " stored candidates\n");
end;;
CheckMaxes("O7(3)", 4585351680, 4245696,
  [["G2(3)",4245696], ["O7(3)M5",4245696]]);;
CheckMaxes("O7(3)", 4585351680, 1451520,
  [["2.U4(3).2_2",13063680], ["S6(2)",1451520], ["O7(3)M8",1451520]]);;
CheckMaxes("O8+(2)", 174182400, 1451520,
  [["S6(2)",1451520], ["O8+(2)M2",1451520], ["O8+(2)M3",1451520]]);;
CheckMaxes("O8+(3)", 4952179814400, 4585351680,
  [["O7(3)",4585351680], ["O8+(3)M2",4585351680],
   ["O8+(3)M3",4585351680], ["O8+(3)M4",4585351680],
   ["O8+(3)M5",4585351680], ["O8+(3)M6",4585351680]]);;
CheckMaxes("O8+(2)", 174182400, 181440,
  [["S6(2)",1451520], ["O8+(2)M2",1451520], ["O8+(2)M3",1451520],
   ["A9",181440], ["O8+(2)M8",181440], ["O8+(2)M9",181440]]);;
CheckMaxes("O8+(3)", 4952179814400, 174182400,
  [["O8+(2)",174182400], ["O8+(3)M11",174182400],
   ["O8+(3)M12",174182400], ["O8+(3)M13",174182400]]);;

# For each of the six O7(3)-subgroup classes, the induced coset character
# differs on two socle classes fused in the actual S:3 extension. A preserved
# subgroup class would make this character invariant, so each class moves.
# We do not claim the six classes form a single full-automorphism orbit.
CheckTriality := function()
  local s, ext, fusion, names, name, sub, subfusion, chi, witness, i, j;
  s := CharacterTable("O8+(3)");
  ext := CharacterTable("O8+(3).3");
  Check(ext <> fail and Identifier(ext) = "O8+(3).3" and
        Size(ext) = 3*Size(s), "triality extension identifier/order");
  fusion := GetFusionMap(s, ext);
  Check(fusion <> fail and Length(fusion) = NrConjugacyClasses(s) and
        ForAll(fusion, x -> IsInt(x) and x in [1..NrConjugacyClasses(ext)]),
        "socle-to-triality fusion");
  names := ["O7(3)", "O8+(3)M2", "O8+(3)M3", "O8+(3)M4",
            "O8+(3)M5", "O8+(3)M6"];
  for name in names do
    sub := CharacterTable(name);
    Check(sub <> fail and Identifier(sub) = name and Size(sub) = 4585351680,
          "triality target subgroup");
    subfusion := GetFusionMap(sub, s);
    Check(subfusion <> fail and Length(subfusion) = NrConjugacyClasses(sub) and
          ForAll(subfusion, x -> IsInt(x) and x in [1..NrConjugacyClasses(s)]),
          "subgroup-to-socle fusion");
    chi := InducedClassFunctionsByFusionMap(sub, s, [TrivialCharacter(sub)],
                                             subfusion)[1];
    Check(chi[1] = 1080, "induced degree");
    witness := false;
    for i in [1..Length(fusion)] do
      for j in [i+1..Length(fusion)] do
        if fusion[i] = fusion[j] and chi[i] <> chi[j] then
          witness := true;
        fi;
      od;
    od;
    Check(witness, Concatenation(name, " triality moves subgroup class"));
    Print(name, ": triality moves stored class\n");
  od;
end;;
CheckTriality();;

# i₂ includes identity. The table's full-automorphism identification is a
# separate cited input; all class sizes and all power-map entries are used.
CheckInv := function(name, order, expected)
  local t, sizes, powers, orders, n;
  t := CharacterTable(name);
  Check(t <> fail and Identifier(t) = name and Size(t) = order,
        Concatenation(name, " full-Aut identifier/order"));
  sizes := SizesConjugacyClasses(t);
  powers := PowerMap(t, 2);
  orders := OrdersClassRepresentatives(t);
  Check(IsList(powers) and IsList(orders) and
        Length(sizes) = NrConjugacyClasses(t) and Length(powers) = Length(sizes) and
        Length(orders) = Length(sizes) and
        ForAll(powers, x -> IsInt(x) and x in [1..Length(sizes)]) and
        ForAll(orders, x -> IsInt(x) and x > 0) and
        powers[1] = 1 and Sum(sizes) = order, "full class data");
  Check(Filtered([1..Length(sizes)], i -> powers[i] = 1) =
        Filtered([1..Length(sizes)], i -> orders[i] in [1,2]),
        "power-map and class-order agreement");
  n := Sum(Filtered([1..Length(sizes)], i -> powers[i] = 1), i -> sizes[i]);
  Check(n = expected, Concatenation(name, " order-at-most-two count"));
  Print(name, ": i2 = ", n, "\n");
end;;
CheckInv("G2(3).2", 8491392, 10180);;
CheckInv("S6(2)", 1451520, 5104);;
CheckInv("A9.2", 362880, 2620);;
CheckInv("O7(3).2", 9170703360, 664120);;
CheckInv("O8+(2).3.2", 1045094400, 183376);;

# Numerical necessary-capacity comparisons, using the separately proved or
# conditional kernel bounds. Row 24 uses the analytic odd-minus upper bound.
rows := [
  [22,4585351680,116640,2,10180],
  [23,4585351680,28431,2,5104],
  [24,65784756654489600,37791360,2,6*3^16],
  [25,174182400,240,6,5104],
  [26,174182400,3840,6,2620],
  [27,4952179814400,349920,8,664120],
  [28,4952179814400,767637,24,183376]
];;
for row in rows do
  Check(row[2] mod row[3] = 0, "integral degree lower bound");
  Check(row[2]/row[3] > row[4]*row[5], "strict capacity inequality");
  Print("row ", row[1], ": degree lower ", row[2]/row[3],
        ", mark upper ", row[4]*row[5], "\n");
od;
Print("PASS: specified finite-table data and capacity arithmetic\n");
QUIT_GAP(0);
