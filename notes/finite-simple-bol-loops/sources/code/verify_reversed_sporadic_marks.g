# M22.2 involution bound for the reversed Li–Xia sporadic factor rows.
# Input: GAP 4.15.1 and its CTblLib 1.3.11 package. See the accompanying
# manuscript for the source provenance, subgroup identifications and scope.
# This finite table check does not independently prove the table or identify
# an actual loop action.

Check := function(condition, message)
  if not condition then
    Print("FAIL: ", message, "\n");
    ForceQuitGap(1);
  fi;
end;

Check(GAPInfo.Version = "4.15.1", "GAP version");
Check(LoadPackage("ctbllib") = true, "load CTblLib");
Check(PackageInfo("ctbllib")[1].Version = "1.3.11", "CTblLib version");
t := CharacterTable("M22.2");;
Check(t <> fail, "table present");
Check(Identifier(t) = "M22.2", "exact table identifier");
Check(Size(t) = 887040, "full automorphism group order");
Check(PositionSublist(InfoText(t), "constructions: Aut(M22)") <> fail,
      "table construction identifier");
orders := OrdersClassRepresentatives(t);;
sizes := SizesConjugacyClasses(t);;
cent := SizesCentralizers(t);;
sq := PowerMap(t, 2);;
n := Length(orders);;
Check(Length(sizes) = n and Length(cent) = n and Length(sq) = n,
      "table column lengths");
Check(Sum(sizes) = Size(t) and sizes[1] = 1 and orders[1] = 1,
      "class sizes and identity");
for i in [1..n] do
  Check(IsInt(sq[i]) and sq[i] >= 1 and sq[i] <= n,
        "square-map index");
  Check(cent[i] * sizes[i] = Size(t), "centralizer and class size");
  Check(orders[sq[i]] = orders[i] / GcdInt(orders[i], 2),
        "square-map and element-order agreement");
  Check((sq[i] = 1) = (orders[i] <= 2), "identity-square agreement");
od;
marks := Sum(Filtered([1..n], i -> sq[i] = 1), i -> sizes[i]);;
Check(marks = 2872, "identity plus involutions");
# Li–Xia Proposition 4.4/Table 4.3, reversed factor roles: the three
# uses of this bound have degrees 40320, 22176, and at least 22176.
Check(10200960 / 253 = 40320, "M23 degree");
Check(44352000 / 2000 = 22176, "HS degree");
Check(88704000 / 4000 = 22176, "HS.2 lower degree");
Check(marks < 22176 and marks < 40320, "capacity comparisons");
Print("M22.2: order 887040; elements of order at most 2 = 2872; ",
      "all required degree comparisons pass\n");
QUIT_GAP(0);
