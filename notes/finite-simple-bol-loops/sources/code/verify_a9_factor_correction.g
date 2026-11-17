# Finite evidence for 0323:C0010, not a proof of classification.
# Canonical deduction: manuscripts/alternating-solvable-factor-correction.md.
# GAP's natural PSL(2,8) permutation model and exact subgroup algorithms are
# retained inputs. The two-class completeness input is documented in the proof.
# Run with GAP 4.15.1: gap --quitonbreak -q -b this-file.g
(function()
  local check, a, s, l, i, act, subdegrees, solv, parabolic;
  check := function(b, msg)
    if not b then Error(msg); fi;
  end;
  check(GAPInfo.Version = "4.15.1", "GAP version mismatch");
  a := AlternatingGroup(9);
  s := SymmetricGroup(9);
  l := PSL(2,8);
  check(LargestMovedPoint(l) = 9 and IsSubgroup(a,l) and Size(l) = 504,
        "natural PSL2(8) model mismatch");
  i := Normalizer(a,l);
  check(Size(i) = 1512 and DerivedSubgroup(i) = l,
        "semilinear normalizer mismatch");
  check(Normalizer(s,l) = i and Normalizer(s,i) = i,
        "S9 normalizer must lie entirely in A9");
  act := Action(a,RightCosets(a,i),OnRight);
  check(IsPrimitive(act), "constructed stabilizer must be maximal");
  check(Size(act) = Size(a) and NrMovedPoints(act) = 120,
        "faithful degree-120 action mismatch");
  subdegrees := SortedList(List(Orbits(Stabilizer(act,1),[1..120]),Length));
  check(subdegrees = [1,56,63], "rank-three subdegrees mismatch");
  # This is S4 x AGL1(5), on the source's 4+5 partition.
  solv := Normalizer(s,Group((5,6,7,8,9)));
  parabolic := Stabilizer(s,[1..4],OnSets);
  check(Size(solv) = 480 and IsSolvableGroup(solv), "S9 solvable factor");
  check(Size(parabolic) = 2880 and IsSubgroup(parabolic,solv),
        "S9 proper 4-subset overgroup");
  check(Size(Intersection(a,solv)) = 240 and
        Size(Intersection(a,parabolic)) = 1440,
        "A9 proper 4-subset overgroup");
  Print("PASS: A9 degree 120, subdegrees ",subdegrees,
        "; S9-fused pair of A9 classes; both solvable factors nonmaximal.\n");
end)();
QUIT_GAP(0);
