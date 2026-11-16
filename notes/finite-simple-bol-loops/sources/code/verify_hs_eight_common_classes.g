# Conditional on CTblLib ordinary tables, fusion maps and group identification.
Check := function(condition, message)
  if condition <> true then
    Print("FAIL: ", message, "\n");
    ForceQuitGap(1);
  fi;
end;;
Check(LoadPackage("ctbllib") = true, "CTblLib load");
Check(GAPInfo.Version = "4.15.1", "GAP version");
Check(PackageInfo("ctbllib")[1].Version = "1.3.11", "CTblLib version");
# T name, Aut name, |T|, common J, inner [class, coefficient], outer ditto
cases := [
 ["M12","M12.2",95040,3,[[2,12],[3,30]],[[13,24]]],
 ["J2","J2.2",604800,2,[[2,10],[3,120]],[[17,120]]],
 ["HS","HS.2",44352000,2,[[2,110],[3,200]],[[22,20],[23,260]]],
 ["He","He.2",4030387200,2,[[2,242],[3,630]],[[27,1792]]],
 ["Suz","Suz.2",448345497600,2,[[2,414],[3,6480]],[[38,864],[39,8640]]],
 ["HN","HN.2",273030912000000,2,[[2,2200],[3,46200]],[[45,79200]]],
 ["F3+","F3+.2",1255205709190661721292800,2,[[2,130572],[3,111891780]],[[98,2],[99,119884050]]],
 ["2F4(2)'","2F4(2)",17971200,2,[[2,10],[3,100]],[]]
];;
for datum in cases do
 T := CharacterTable(datum[1]);; A := CharacterTable(datum[2]);;
 Check(T <> fail and A <> fail, Concatenation(datum[1], " tables"));
 Check(Size(T)=datum[3] and Size(A)=2*Size(T), Concatenation(datum[1], " orders"));
 f := GetFusionMap(T,A);;
 Check(f <> fail, Concatenation(datum[1], " fusion"));
 ti := Positions(OrdersClassRepresentatives(T),2);;
 ai := Positions(OrdersClassRepresentatives(A),2);;
 Check(ti=List(datum[5], x -> x[1]), Concatenation(datum[1], " inner class list"));
 Check(Length(Set(f{ti}))=Length(ti), Concatenation(datum[1], " involution fusion injectivity"));
 Check(Difference(ai, Set(f))=List(datum[6], x -> x[1]), Concatenation(datum[1], " outer class list"));
 Check(Set(Intersection(ai, Set(f)))=Set(f{ti}), Concatenation(datum[1], " Aut coverage"));
 for item in datum[5] do
   Check(ClassMultiplicationCoefficient(T,item[1],item[1],datum[4])=item[2] and item[2]>0,
         Concatenation(datum[1], " inner coefficient"));
 od;
 for item in datum[6] do
   Check(ClassMultiplicationCoefficient(A,item[1],item[1],f[datum[4]])=item[2] and item[2]>0,
         Concatenation(datum[1], " outer coefficient"));
 od;
 Print(datum[1], " common-class checks passed\n");
od;
QUIT_GAP(0);
