# GAP 4.15.1, CTblLib 1.3.11. Uses class sizes without subgroup fusion.
if LoadPackage("ctbllib") <> true then Error("CTblLib missing"); fi;
table := CharacterTable("S8(2)");;
sizes := SizesConjugacyClasses(table);;
stabilizerOrder := 2448;;
if Size(table) <> 47377612800 or Length(sizes) <> 81 or sizes[1] <> 1 then
    Error("unexpected Sp8(2) table");
fi;
smallClasses := Filtered([2..Length(sizes)], i -> sizes[i] <= stabilizerOrder^2);;
smallUnion := Sum(sizes{smallClasses});;
covered := stabilizerOrder * (smallUnion + 1);;
if smallUnion <> 15928575 or covered <> 38993154048 or covered >= Size(table) then
    Error("double-coset union bound failed");
fi;
Print("Small-class union size ", smallUnion, ", covered at most ", covered,
      " of ", Size(table), " elements\n");
QUIT;
