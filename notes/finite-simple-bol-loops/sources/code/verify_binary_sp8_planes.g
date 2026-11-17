# GAP 4.15.1, standard library only. Binary F4-line spread obstruction.
# Vectors act on the right. All assertions below are exact finite checks.
Check := function(condition, message)
  if not condition then Error(message); fi;
end;;

VerifyBinarySp8Planes := function()
  local field, zero, one, group, form, scalar, i, vectors, position,
        spread, generators, action, classes, planes, goodPair, class,
        representative, witness, witnessMatrix, witnessPermutation;
  field := GF(2); zero := Zero(field); one := One(field);
  group := Sp(8, field);
  Check(Size(group) = 47377612800, "unexpected symplectic group order");
  form := InvariantBilinearForm(group).matrix;
  Check(RankMat(form) = 8 and form = TransposedMat(form) and
        ForAll([1..8], i -> IsZero(form[i][i])), "invalid alternating form");

  # Multiplication by a root of x^2+x+1, self-adjoint for the form.
  scalar := NullMat(8, 8, field);
  for i in [0, 2, 4, 6] do
    scalar[i+1][i+2] := one; scalar[i+2][i+1] := one;
    scalar[i+2][i+2] := one;
  od;
  for i in [4, 6] do
    scalar[i+1][i+1] := one; scalar[i+2][i+2] := zero;
  od;
  Check(IsZero(scalar^2 + scalar + IdentityMat(8, field)) and
        scalar * form = form * TransposedMat(scalar), "invalid F4 scalar");

  vectors := Filtered(Tuples(Elements(field), 8), v -> not IsZero(v));
  position := v -> Position(vectors, v);
  spread := Set(List(vectors, v -> Set([position(v), position(v*scalar),
                                         position(v+v*scalar)])));
  Check(Length(vectors) = 255 and Length(spread) = 85 and
        ForAll(spread, p -> Length(p) = 3 and
          IsZero(vectors[p[1]] * form * vectors[p[2]])), "invalid spread");
  generators := List(GeneratorsOfGroup(group), g ->
    PermList(List(vectors, v -> position(v*g))));
  action := Group(generators);
  Check(Size(action) = Size(group), "nonfaithful vector action");
  planes := Orbit(action, spread[1], OnSets);
  Check(Length(planes) = 5355, "unexpected isotropic plane count");
  classes := ConjugacyClasses(action);
  Check(Length(classes) = 81 and Sum(classes, Size) = Size(action),
        "unexpected conjugacy class count");

  # Equal planes, or disjoint planes with cross-pairing rank zero or two.
  goodPair := function(p, q)
    local a, b, c, d, pair;
    if p = q then return true; fi;
    if not IsEmpty(Intersection(p, q)) then return false; fi;
    a := vectors[p[1]]; b := vectors[p[2]];
    c := vectors[q[1]]; d := vectors[q[2]];
    pair := [[a*form*c, a*form*d], [b*form*c, b*form*d]];
    return RankMat(pair) in [0, 2];
  end;
  for class in classes do
    representative := Representative(class);
    witness := First(planes, p -> goodPair(p, OnSets(p, representative)));
    Check(witness <> fail, "class without a plane witness");
  od;

  # Extracted from a symplectic permutation witness on the eight basis vectors.
  witnessMatrix := [
    [1,1,1,0,0,1,0,1], [0,0,0,1,0,1,1,0],
    [1,1,0,0,1,0,0,1], [0,0,1,1,1,0,0,1],
    [0,1,1,1,0,0,0,1], [0,1,1,1,0,1,1,1],
    [1,0,0,1,1,1,1,1], [0,1,1,0,0,0,0,0]
  ] * one;
  Check(witnessMatrix in group and
        witnessMatrix * form * TransposedMat(witnessMatrix) = form,
        "witness matrix is not symplectic");
  witnessPermutation := PermList(List(vectors, v -> position(v*witnessMatrix)));
  Check(IsEmpty(Intersection(spread,
        Set(List(spread, p -> OnSets(p, witnessPermutation))))),
        "witness spreads intersect");
  Print("PASS: Sp(8,2), 85 spread lines, 5355 isotropic planes, ",
        "81 classes; disjoint-spread witness verified\n");
end;;

VerifyBinarySp8Planes();;
QUIT;
