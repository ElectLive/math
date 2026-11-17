# C0010 M12 transitive nonsolvable subgroup data certificate; GAP 4.15.1.
# Exhaustive subgroup-class and permutation/group isomorphism algorithms
# are runtime inputs; this is not an independent verification of GAP.
Run:=function()
 local Check,s,classes,ts,h,groups,n,der,expected,shapes,iso,cnt;
 Check:=function(ok,label) if not ok then Print("FAIL: ",label,"\n"); ForceQuitGap(1); fi; end;
 Check(GAPInfo.Version="4.15.1","version");
 s:=MathieuGroup(12); Check(Size(s)=95040 and IsSimpleGroup(s),"M12");
 classes:=ConjugacyClassesSubgroups(s); Check(Length(classes)=147,"complete class count");
 ts:=Filtered(List(classes,Representative),h->IsTransitive(h,[1..12]) and not IsSolvableGroup(h));
 Check(Collected(List(ts,Size))=[[60,1],[120,2],[240,1],[660,1],[720,2],[1440,1],[7920,1],[95040,1]],"orders and multiplicities");
 for h in ts do
  n:=Size(h); der:=DerivedSubgroup(h);
  if n=60 then Check(IsSimpleGroup(h) and IsomorphismGroups(h,AlternatingGroup(5))<>fail,"A5");
  elif n=120 then
   Check(Size(der)=60 and IsSimpleGroup(der),"120 residual");
   Check(Size(Centre(h)) in [1,2],"120 center");
  elif n=240 then
   Check(Size(der)=60 and IsSimpleGroup(der) and Size(Centre(h))=2,"240 residual and center");
   Check(IsomorphismGroups(h,DirectProduct(SymmetricGroup(5),CyclicGroup(IsPermGroup,2)))<>fail,"S5x2");
  elif n=660 then Check(IsomorphismGroups(h,PSL(2,11))<>fail,"PSL2(11)");
  elif n in [720,1440] then
   Check(Size(der)=360 and IsSimpleGroup(der) and Size(Centralizer(h,der))=1,"almost-simple A6");
   Check(IsomorphismGroups(der,AlternatingGroup(6))<>fail,"derived group is A6");
  elif n=7920 then Check(IsomorphismGroups(h,MathieuGroup(11))<>fail,"M11");
  elif n=95040 then Check(h=s,"full M12");
  fi;
 od;
 Check(Collected(List(Filtered(ts,h->Size(h)=120),h->Size(Centre(h))))=[[1,1],[2,1]],"both 120 types");
 h:=First(ts,h->Size(h)=120 and Size(Centre(h))=2);
 Check(IsomorphismGroups(h,DirectProduct(AlternatingGroup(5),CyclicGroup(IsPermGroup,2)))<>fail,"A5x2");
 h:=First(ts,h->Size(h)=120 and Size(Centre(h))=1);
 Check(IsomorphismGroups(h,SymmetricGroup(5))<>fail,"S5");
 Print("M12: 147 subgroup classes; all ten transitive nonsolvable classes identified\n");
end;;
Run();;
QUIT_GAP(0);
