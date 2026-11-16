# GAP 4.15.1 with CTblLib 1.3.11. Published table identification is an input.
Check := function(condition, message)
  if condition <> true then
    Print("FAIL: ", message, "\n");
    ForceQuitGap(1);
  fi;
end;;
Check(GAPInfo.Version = "4.15.1", "GAP 4.15.1 required");
Check(LoadPackage("ctbllib") = true, "CTblLib required");
Check(PackageInfo("ctbllib")[1].Version = "1.3.11", "CTblLib 1.3.11 required");
rows := [
  ["M11", 7920, 7920, 166, "M11"],
  ["M12.2", 95040, 190080, 1684, "M12.2"],
  ["M22.2", 443520, 887040, 2872, "M22.2"],
  ["M23", 10200960, 10200960, 3796, "M23"],
  ["M24", 244823040, 244823040, 43264, "M24"],
  ["J1", 175560, 175560, 1464, "J1"],
  ["J2.2", 604800, 1209600, 4636, "J2.2"],
  ["J3.2", 50232960, 100465920, 46684, "J3.2"],
  ["J4", 86775571046077562880, 86775571046077562880, 51747149312, "J4"],
  ["Co1", 4157776806543360000, 4157776806543360000, 12792894976, "Co1"],
  ["Co2", 42305421312000, 42305421312000, 29771776, "Co2"],
  ["Co3", 495766656000, 495766656000, 2778976, "Co3"],
  ["Fi22.2", 64561751654400, 129123503308800, 79466752, "Fi22.2"],
  ["Fi23", 4089470473293004800, 4089470473293004800, 12895196032, "Fi23"],
  ["Fi24'.2", 1255205709190661721292800, 2510411418381323442585600, 13510933563520, "F3+.2"],
  ["HS.2", 44352000, 88704000, 45376, "HS.2"],
  ["McL.2", 898128000, 1796256000, 135676, "McL.2"],
  ["He.2", 4030387200, 8060774400, 478976, "He.2"],
  ["Ru", 145926144000, 145926144000, 1846576, "Ru"],
  ["Suz.2", 448345497600, 896690995200, 5644432, "Suz.2"],
  ["O'N.2", 460815505920, 921631011840, 5482072, "ON.2"],
  ["HN.2", 273030912000000, 546061824000000, 150843376, "HN.2"],
  ["Ly", 51765179004000000, 51765179004000000, 1296826876, "Ly"],
  ["Th", 90745943887872000, 90745943887872000, 976841776, "Th"],
  ["B", 4154781481226426191177580544000000, 4154781481226426191177580544000000, 512299100893413376, "B"],
  ["M", 808017424794512875886459904961710757005754368000000000, 808017424794512875886459904961710757005754368000000000, 5791748165751443778953445376, "M"]
];;
CheckRows := function(rows)
local small, row, t, sizes, pm, b;
small := [];
for row in rows do
  t := CharacterTable(row[1]);;
  Check(t <> fail and Identifier(t) = row[5] and Size(t) = row[3], Concatenation("table mismatch: ",row[1]));
  sizes := SizesConjugacyClasses(t);; pm := PowerMap(t,2);;
  Check(Length(sizes) = Length(pm) and pm[1] = 1, "invalid map");
  b := Sum(Filtered([1..Length(sizes)],i->pm[i]=1),i->sizes[i]);;
  Check(b = row[4] and b^3+3*row[3]*b < row[2]^2, Concatenation("count or F3 mismatch: ",row[1]));
  if row[2] < 2^20 then Add(small,row[1]); fi;
od;
Check(small = ["M11","M12.2","M22.2","J1","J2.2"], "threshold set mismatch");
end;;
CheckRows(rows);;
Print("26 full-Aut table counts pass F3; 21 meet threshold\n");
QUIT_GAP(0);
