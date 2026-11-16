# GAP 4.15.1: gap -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_unitary_four_two_maximals.g
Check := function(test, msg)
  if not test then Print("FAIL: ", msg, "\n"); ForceQuitGap(1); fi;
end;;
G := PSp(4,3);;
Check(GAPInfo.Version="4.15.1", "GAP version");
Check(Size(G)=25920 and IsSimpleGroup(G), "group");
M := MaximalSubgroupClassReps(G);;
counts := Collected(List(M,Size));;
Check(counts=[[576,1],[648,2],[720,1],[960,1]], "maximal classes");
S := Filtered(M,x->Size(x)=720);;
Check(Length(S)=1 and IsomorphismGroups(S[1],SymmetricGroup(6))<>fail, "S6 class");
P := SylowSubgroup(S[1],5);;
Check(Size(Normalizer(S[1],P))=20, "5-normalizer");
Print("GAP ",GAPInfo.Version,"; group order ",Size(G),"; simple ",IsSimpleGroup(G),"\n");
Print("maximal (order, class count): ",counts,"\n");
Print("unique order-720 maximal isomorphic to S6; Sylow-5 normalizer order ",Size(Normalizer(S[1],P)),"\n");
QUIT_GAP(0);
