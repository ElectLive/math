# Finite orbital witnesses for the eight maximal-subgroup classes of Sp6(2).
#
# Run: gap --quitonbreak -q -b verify_binary_sp6_orbitals.g
# Tested with GAP 4.15.1 and TOMLib 1.2.11.
#
# The table-of-marks identification and completeness are input dependencies.
# The degree-28 and degree-36 representatives are identified via their unique
# indices in that table; their orthogonal geometry is an external input.
# The rank-three output at degree 120 is an input to the separately established
# rank-three result. This program does not itself infer any loop consequence.
#
# For each of the other five actions, a chosen nontrivial stabilizer orbit is
# tested. For every conjugacy class, one explicit conjugate of its representative
# is found whose base-point image lies outside that orbit. Therefore no entire
# conjugacy class has all its base-point images in that orbit. The pseudorandom
# search supplies witnesses only: failure to find one is a certificate failure,
# never a mathematical exclusion. Every reported witness is checked directly.

if LoadPackage("tomlib") <> true then
    Error("TOMLib could not be loaded");
fi;

table := TableOfMarks("S6(2)");;
if table = fail then Error("S6(2) table of marks is unavailable"); fi;
ambient := UnderlyingGroup(table);;
maximalData := MaximalSubgroupsTom(table);;
expectedIndices := [28, 36, 63, 120, 135, 315, 336, 960];;
if Size(ambient) <> 1451520 or maximalData[2] <> expectedIndices then
    Error("unexpected ambient order or maximal-subgroup indices");
fi;
classes := ConjugacyClasses(ambient);;
if Length(classes) <> 30 then Error("expected 30 conjugacy classes"); fi;
Print("Maximal indices: ", maximalData[2], "; classes: ", Length(classes), "\n");

# Return the actual right-coset permutation action and its point-stabilizer orbits.
cosetActionData := function(position)
    local subgroup, cosets, action, imageGroup, imageStabilizer, suborbits;
    subgroup := RepresentativeTom(table, maximalData[1][position]);
    cosets := RightCosets(ambient, subgroup);
    if Length(cosets) <> expectedIndices[position] then
        Error("representative has incorrect index");
    fi;
    action := ActionHomomorphism(ambient, cosets, OnRight);
    imageGroup := Image(action, ambient);
    imageStabilizer := Image(action, subgroup);
    suborbits := Orbits(imageStabilizer, [1..Length(cosets)]);
    if not IsTransitive(imageGroup, [1..Length(cosets)]) then
        Error("coset action is not transitive");
    fi;
    return rec(action := action, imageGroup := imageGroup,
               suborbits := suborbits, degree := Length(cosets));
end;;

# Verify the actual rank-three degree-120 action and its two subdegrees.
rankThree := cosetActionData(4);;
if SortedList(List(rankThree.suborbits, Length)) <> [1, 56, 63] then
    Error("degree-120 subdegrees are not [1, 56, 63]");
fi;
Print("Degree 120 subdegrees: ", SortedList(List(rankThree.suborbits, Length)), "\n");

# Each pair gives an index position and the size of an orbit to obstruct.
# There is a unique orbit of the specified size in each action.
tests := [[3,30], [5,14], [6,18], [7,20], [8,252]];;
data := fail;; target := fail;;
Reset(GlobalMersenneTwister, 123456);;
for test in tests do
    data := cosetActionData(test[1]);;
    matching := Filtered(data.suborbits, orbit -> Length(orbit) = test[2]);;
    if Length(matching) <> 1 then Error("target orbit is not unique"); fi;
    target := matching[1];;
    if 1 in target then Error("target orbit is diagonal"); fi;
    classImages := List(classes, c -> Image(data.action, Representative(c)));;
    # The identity conjugator is a legitimate first witness when it works.
    witnessed := List(classImages, x -> not (1^x in target));;
    for trial in [1..200] do
        conjugator := PseudoRandom(data.imageGroup);;
        for classIndex in [1..Length(classes)] do
            point := 1^(classImages[classIndex]^conjugator);;
            if not (point in target) then witnessed[classIndex] := true; fi;
        od;
    od;
    if not ForAll(witnessed, witness -> witness) then
        Error("failed to find witnesses for all 30 classes");
    fi;
    Print("Degree ", data.degree, ", target subdegree ", Length(target),
          ": verified outside witness for each of 30 classes\n");
od;
QUIT;
