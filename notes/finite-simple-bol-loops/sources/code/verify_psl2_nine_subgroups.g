# GAP 4.15.1; run from this problem workspace:
# gap -q -b code/verify_psl2_nine_subgroups.g
Check:=function(test,msg)
 if not test then Print("FAIL: ",msg,"\n"); ForceQuitGap(1); fi;
end;;
Check(GAPInfo.Version="4.15.1","GAP version");
T:=PSL(2,9);;
Check(Size(T)=360 and IsSimpleGroup(T),"simple order 360");
maxs:=MaximalSubgroupClassReps(T);;
maxdata:=Collected(List(maxs,h->[Size(h),StructureDescription(h)]));;
Check(maxdata=[[[24,"S4"],2],[[36,"(C3 x C3) : C4"],1],[[60,"A5"],2]],"maximal subgroup class types");
ics:=Filtered(ConjugacyClasses(T),c->Order(Representative(c))=2);;
Check(Length(ics)=1,"one class of involutions");
s4:=Filtered(maxs,h->Size(h)=24);;
P:=SylowSubgroup(T,2);;
Check(Size(P)=8 and ForAll(s4,h->IsConjugate(T,P,SylowSubgroup(h,2))),"Sylow2 in each S4 class");
cls:=ConjugacyClassesSubgroups(T);;
Check(Length(cls)=22,"number of subgroup classes");
fives:=List(Filtered(cls,c->Size(Representative(c))<360 and Size(Representative(c)) mod 5=0),Representative);;
fivedata:=Collected(List(fives,h->[Size(h),StructureDescription(h)]));;
Check(fivedata=[[[5,"C5"],1],[[10,"D10"],1],[[60,"A5"],2]],"five-divisible proper subgroup classes");
Check(ForAll(Filtered(fives,h->Size(h)=5),h->Size(Normalizer(T,h))=10),"C5 normalizer D10");
S:=First(maxs,h->Size(h)=60);;
suba:=ConjugacyClassesSubgroups(S);;
Check(ForAll(suba,c->Size(Representative(c))=60 or 2^LogInt(Index(S,Representative(c)),2)<>Index(S,Representative(c))),"A5 no proper 2-power index");
Print("GAP ",GAPInfo.Version,"; T simple of order ",Size(T),"\n");
Print("maximal [order,type], number of classes: ",maxdata,"\n");
Print("involution classes: ",Length(ics),"; order-8 Sylow contained in S4: true\n");
Print("subgroup classes: ",Length(cls),"; proper 5-bearing types/classes: ",fivedata,"\n");
Print("C5 normalizer order: 10; A5 proper 2-power index: none\n");
QUIT_GAP(0);
