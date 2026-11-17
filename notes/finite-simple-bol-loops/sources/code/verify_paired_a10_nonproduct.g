# Finite input for the paired A10 nonproduct construction.
# Run with GAP 4.15.1; no packages, network, random choices or output files.
# The canonical manuscript proves ambivalence and the classification separately.
# Explicit generators were obtained during exploration from MathieuGroup(10),
# but every property used below is checked in their actual permutation group.
# No MathieuGroup or ATLAS identification is a runtime input.
Check:=function(b,s) if not b then Print("FAIL ",s,"\n"); ForceQuitGap(1); fi; end;;
Check(GAPInfo.Version="4.15.1","version");;
u:=(1,9,6,7,5)(2,10,3,8,4);; v:=(1,10,7,8)(2,9,4,6);;
Zgrp:=Group(u,v);; A:=AlternatingGroup(7);; Y:=Group(Concatenation(GeneratorsOfGroup(A),[(1,2)(9,10)]));; T:=AlternatingGroup(10);;
D:=DerivedSubgroup(Zgrp);; R:=Intersection(Y,Zgrp);;
Check(u in T and v in T and IsSubgroup(T,Y),"ambient membership");;
Check(List([T,A,Y,Zgrp,D,R],Size)=[1814400,2520,5040,720,360,2],"orders");;
Check(IsSimpleGroup(T) and IsNormal(Y,A) and IsNormal(Zgrp,D),"normality/simple");;
Check(ForAll(GeneratorsOfGroup(Zgrp),x->SignPerm(x)=1),"even");;
Check(Size(Intersection(A,Zgrp))=1 and Size(A)*Size(Zgrp)=Size(T),"exact factorization");;
Check(IsSubgroup(D,R),"involution in derived kernel");;
Check(Transitivity(Zgrp)=3,"sharp triple transitivity");;
Print("A10 exact A7 M10, Y=S7, R2 in Zderived, orders, 3-transitivity and even generators pass\n");
QUIT_GAP(0);
