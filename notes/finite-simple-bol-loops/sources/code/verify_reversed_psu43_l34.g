# Row 20 (reversed): faithful PSL3(4) normalizer in Aut(PSU4(3)).
# GAP 4.15.1; CTblLib 1.3.11; assertions enabled. Run gap -q -b FILE.
# The ATLAS identifies this faithful degree-324 action as U4(3).D8 on
# cosets of L3(4):2^2; its source identification is an external input.
# Embedded generators copied verbatim from:
# https://brauer.maths.qmul.ac.uk/Atlas/clas/U43/gap/U43D8G1-p324B0.g1
# SHA256 15c61c520a505810eaa89e780252bf15a24ba9a8538a4f0488c0a6f05f598c92
# https://brauer.maths.qmul.ac.uk/Atlas/clas/U43/gap/U43D8G1-p324B0.g2
# SHA256 58eabc48994df6189b4271363cb40306886a28580258151ab30938520bec2e97
# CTblLib's Maxes list is a source input for completeness, not a proof of the
# maximal-subgroup classification; no network or local generator files needed.
Check := function(ok, label)
  if not ok then
    Print("FAIL: ", label, "\n");
    ForceQuitGap(1);
  fi;
end;;
Check(LoadPackage("ctbllib", "1.3.11") = true, "CTblLib unavailable");
Check(GAPInfo.Version = "4.15.1", "expected GAP 4.15.1");
Check(PackageInfo("ctbllib")[1].Version = "1.3.11", "expected CTblLib 1.3.11");
g1 := (1,2)(3,7)(4,8)(5,9)(6,11)(10,19)(12,23)(13,24)(14,26)(15,28)(16,30)(17,
     32)(18,34)(20,38)(21,39)(22,41)(25,46)(27,50)(29,53)(31,56)(33,58)(35,62)
     (36,63)(37,64)(40,70)(42,73)(43,74)(44,76)(45,77)(47,48)(49,82)(51,85)
     (52,54)(55,89)(57,84)(59,95)(60,79)(61,97)(65,105)(66,106)(67,107)(68,
     108)(69,92)(71,113)(72,88)(75,117)(78,101)(80,123)(81,103)(83,111)(86,
     100)(87,116)(90,119)(91,131)(93,134)(94,135)(96,139)(98,142)(99,143)(102,
     146)(104,149)(109,155)(110,157)(112,159)(114,162)(115,163)(118,167)(120,
     170)(121,172)(122,174)(124,178)(125,179)(126,180)(127,182)(128,184)(129,
     185)(130,187)(132,190)(133,192)(136,196)(137,197)(138,198)(140,201)(141,
     202)(144,206)(145,207)(147,208)(148,209)(150,210)(151,212)(152,214)(153,
     215)(154,216)(156,204)(158,220)(160,221)(161,222)(164,224)(165,193)(166,
     211)(168,226)(169,227)(171,229)(173,233)(175,236)(176,237)(177,239)(181,
     203)(183,217)(186,243)(188,245)(189,246)(191,248)(194,250)(195,251)(199,
     254)(200,235)(205,238)(213,232)(218,249)(219,263)(223,267)(225,242)(228,
     268)(230,269)(231,270)(234,273)(240,277)(241,278)(244,279)(247,281)(252,
     284)(253,285)(255,287)(256,283)(257,288)(258,280)(259,289)(260,290)(261,
     276)(262,291)(264,292)(265,293)(266,286)(271,295)(272,275)(274,297)(282,
     303)(294,308)(296,312)(298,313)(299,314)(300,306)(301,315)(302,317)(304,
     318)(305,319)(307,320)(309,321)(310,322)(311,323)(316,324);
g2 := (1,3,4)(2,5,10,20,12,6)(7,13,25,47,27,14)(8,15,29,54,31,16)(9,17,33,59,
     35,18)(11,21,40,71,42,22)(19,36,53,88,65,37)(23,43,75,84,50,44)(24,45,78,
     90,55,30)(26,48,81,125,83,49)(28,51,86,128,87,52)(32,41,72,114,93,57)(34,
     60,96,140,98,61)(38,66,67)(39,68,109,156,110,69)(46,79,122,175,124,80)
     (56,91,132,191,133,92)(58,82,126,181,136,94)(62,99,106,152,144,100)(63,
     101,145,184,147,102)(64,103,148,116,74,104)(70,111,158,153,107,112)(73,
     115,164,183,127,85)(76,118,168,179,169,119)(77,120,171,230,173,121)(89,
     129,186,244,188,130)(95,137,161,113,160,138)(97,141)(105,150,190,247,213,
     151)(108,154)(117,165,225,240,178,166)(123,176,238,189,131,177)(134,193,
     239,212,162,194)(135,195,229,245,223,163)(139,199,255,280,246,200)(142,
     203,227,214,198,146)(143,204,256,201,159,205)(149,210,243,272,233,211)
     (155,167,221,215,207,217)(157,218,237,276,264,219)(170,228,187,180,241,
     182)(172,231,185,242,271,232)(174,234,192,249,270,235)(196,252,206,226,
     266,222)(197,253,208,220,265,224)(202,257,258)(209,259,260)(216,261,262)
     (236,274,298,282,248,275)(251,283,267)(254,286,304,285,263,268)(269,294,
     309,316,301,279)(273,296)(277,281,302,303,297,299)(278,300)(284,293,290,
     287,292,289)(288,305,318,307,291,306)(295,310,315,312,308,311)(314,321)
     (317,324)(319,320);
a := Group(g1,g2);;
Check(Size(a) = 26127360 and IsTransitive(a,[1..324]), "ambient");
s := a;;
repeat
  q := DerivedSubgroup(s);;
  if Size(q) = Size(s) then break; fi;
  s := q;;
until false;
Check(Size(s) = 3265920 and IsSimpleGroup(s), "socle");
orb := Orbits(s,[1..324]);;
Check(List(orb,Length) = [162,162], "socle orbits");
n := Stabilizer(a,1);;
t := Intersection(s,n);;
Check(Size(n) = 80640 and Size(t) = 20160, "stabilizer");
Check(IsSimpleGroup(t), "T not simple");
iso := IsomorphismGroups(t,PSL(3,4));;
Check(iso <> fail, "T is not PSL(3,4)");
ns := Normalizer(s,t);;
na := Normalizer(a,t);;
Check(Size(ns) = 20160 and Size(na) = 80640 and na = n,
      "point stabilizer is not the full normalizer");
Check(Size(Centralizer(a,t)) = 1, "nontrivial centralizer");
ct := CharacterTable("U4(3)");;
Check(ct <> fail, "U4(3) character table unavailable");
Check(Identifier(ct) = "U4(3)" and Size(ct) = Size(s),
      "ambient character-table identifier or order");
maxes := Maxes(ct);;
Check(maxes <> fail and IsList(maxes), "maximal-subgroup list unavailable");
max_tables := List(maxes, name -> CharacterTable(name));;
Check(ForAll(max_tables, table -> table <> fail),
      "a maximal-subgroup character table is unavailable");
relevant := Filtered([1..Length(maxes)], i -> Size(max_tables[i]) mod Size(t) = 0);;
Check(List(relevant, i -> maxes[i]) = ["L3(4)","L3(4)"],
      "maximal-subgroup list");
Print("A=26127360; S=3265920; S-orbits=[162,162]; N=80640; T=PSL(3,4)\n");
Print("N_S(T)=T; N_A(T)=N_A(1); C_A(T)=1; relevant CTblLib maxima=2\n");
Print("PASS (conditional on ATLAS action and CTblLib completeness)\n");
QUIT_GAP(0);
