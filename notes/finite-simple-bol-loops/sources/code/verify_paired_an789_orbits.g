# Paired A7/A8/A9 orbit enumeration, GAP 4.15.1.
# Conditional on the paired normal form at c5153a7ccd4a0de8e8f700341a78ac06f3b1caf0:
# product folders are exact pairs; C2 folders have a unique orientation
# (A,A0),(B,B0) with both kernels index 2, |A cap B|=2,
# A cap B <= A0, and (A cap B) cap B0=1.
# Aut(A_n)=S_n for n=7,8,9. Enumerate S_n-orbits of subgroups and
# subgroup/kernel decorations; then enumerate their relative embeddings.
# GAP uses H^g=g^-1 H g: for N_A\S_n/N_B representative d the corresponding
# subgroup is B^(d^-1). Every accepted product has unequal factor orders,
# so the displayed index ordering removes the optional factor swap exactly.
# Set EmitRepresentatives before reading this file to print subgroup generators.
# No finite loop, T x T subgroup, external file, or network is constructed.
if not IsBound(EmitRepresentatives) then EmitRepresentatives:=false; fi;;
Check:=function(ok,label)
 if not ok then Print("FAIL: ",label,"\n");ForceQuitGap(1);fi;
end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Verify:=function(n,expectedSubgroups,expectedDecorations,expectedProducts,expectedCoupled)
 local T,S,classes,subgroups,decorations,cl,H,K,existing,g,N,duplicate,
       productPairs,coupledPairs,i,j,A,B,A0,B0,NA,NB,doubleCoset,d,
       movedB,movedB0,intersection,histogram;
 T:=AlternatingGroup(n); S:=SymmetricGroup(n);
 classes:=ConjugacyClassesSubgroups(T);subgroups:=[];decorations:=[];
 for cl in classes do
  H:=Representative(cl);
  if Size(H)>1 and Size(H)<Size(T) then
   duplicate:=false;
   for existing in subgroups do
    if Size(H)=Size(existing) and IsConjugate(S,H,existing) then
     duplicate:=true;break;
    fi;
   od;
   if not duplicate then Add(subgroups,H);fi;
   for K in NormalSubgroups(H) do
    if Index(H,K)=2 then
     duplicate:=false;
     for existing in decorations do
      if Size(H)=Size(existing[1]) then
       g:=RepresentativeAction(S,H,existing[1],OnPoints);
       if g<>fail then
        N:=Normalizer(S,existing[1]);
        if IsConjugate(N,K^g,existing[2]) then duplicate:=true;break;fi;
       fi;
      fi;
     od;
     if not duplicate then Add(decorations,[H,K]);fi;
    fi;
   od;
  fi;
 od;
 Check(Length(subgroups)=expectedSubgroups,"S_n subgroup classes");
 Check(Length(decorations)=expectedDecorations,"decorated classes");
 productPairs:=[];coupledPairs:=[];
 for i in [1..Length(subgroups)] do
  for j in [i..Length(subgroups)] do
   A:=subgroups[i];B:=subgroups[j];
   if Size(A)*Size(B)=Size(T) then
    for doubleCoset in DoubleCosets(S,Normalizer(S,A),Normalizer(S,B)) do
     d:=Representative(doubleCoset);movedB:=B^(d^-1);
     if Size(Intersection(A,movedB))=1 then
      Check(Size(A)<>Size(B),"equal-size product needs swap analysis");
      Add(productPairs,[Size(A),Size(B)]);
      if EmitRepresentatives then
       Print("product A=",GeneratorsOfGroup(A)," B=",GeneratorsOfGroup(movedB),"\n");
      fi;
     fi;
    od;
   fi;
  od;
 od;
 for i in [1..Length(decorations)] do
  for j in [1..Length(decorations)] do
   A:=decorations[i][1];A0:=decorations[i][2];
   B:=decorations[j][1];B0:=decorations[j][2];
   if Size(A)*Size(B)=2*Size(T) then
    NA:=Intersection(Normalizer(S,A),Normalizer(S,A0));
    NB:=Intersection(Normalizer(S,B),Normalizer(S,B0));
    for doubleCoset in DoubleCosets(S,NA,NB) do
     d:=Representative(doubleCoset);movedB:=B^(d^-1);movedB0:=B0^(d^-1);
     intersection:=Intersection(A,movedB);
     if Size(intersection)=2 and Size(Intersection(intersection,A0))=2
        and Size(Intersection(intersection,movedB0))=1 then
      Add(coupledPairs,[Size(A),Size(B)]);
      if EmitRepresentatives then
       Print("C2 A=",GeneratorsOfGroup(A)," A0=",GeneratorsOfGroup(A0),
             " B=",GeneratorsOfGroup(movedB)," B0=",GeneratorsOfGroup(movedB0),"\n");
      fi;
     fi;
    od;
   fi;
  od;
 od;
 Check(Length(productPairs)=expectedProducts,"product orbit count");
 Check(Length(coupledPairs)=expectedCoupled,"C2 orbit count");
 histogram:=Collected(productPairs);
 Print("A",n,": subgroup/decorated classes ",Length(subgroups),"/",Length(decorations),
       "; product ",Length(productPairs)," ",histogram,
       "; C2 ",Length(coupledPairs)," ",Collected(coupledPairs),"\n");
end;;
Verify(7,35,26,2,0);;
Verify(8,110,155,9,0);;
Verify(9,193,260,6,1);;
QUIT_GAP(0);
