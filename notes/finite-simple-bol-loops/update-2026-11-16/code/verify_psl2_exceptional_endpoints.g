# GAP 4.15.1; run from this problem workspace:
# gap -q -b code/verify_psl2_exceptional_endpoints.g
Check:=function(b,s) if not b then Print("FAIL ",s,"\n"); ForceQuitGap(1); fi; end;;
Case:=function(p, expected)
 local a,t,m,x,types,y,s;
 a:=PGL(2,p); t:=DerivedSubgroup(a);
 Check(Size(t)=p*(p^2-1)/2 and Size(a)=2*Size(t),"group orders");
 m:=MaximalSubgroupClassReps(t);
 x:=Filtered(m,g->Size(g)=p+1);
 types:=Collected(List(x,StructureDescription));
 Check(types=expected,"maximal class types/counts");
 for s in Set(List(x,StructureDescription)) do
  y:=Filtered(x,g->StructureDescription(g)=s);
  Check(ForAll(y,z->IsConjugate(a,y[1],z)),"PGL fusion");
 od;
 Print("p=",p,", maximal classes ",types,", each type PGL-fused\n");
end;;
Check(GAPInfo.Version="4.15.1","GAP version");
Case(23,[["D24",1],["S4",2]]);
Case(59,[["A5",2],["D60",1]]);
QUIT_GAP(0);
