# Finite C0010 source and subgroup certificate. GAP 4.15.1, CTblLib 1.3.11.
# CTblLib/ATLAS class, fusion and maximal-list completeness are inputs.
# PSL(4,3) is GAP's natural degree-40 projective action. No loop enumeration.
Check:=function(c,s) if c<>true then Print("FAIL ",s,"\n");ForceQuitGap(1);fi;end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Check(LoadPackage("ctbllib")=true and PackageInfo("ctbllib")[1].Version="1.3.11","CTblLib version");;
Main:=function()
 local S,A,names,expected,inners,outerfull,k,t,sf,tf,pw,sizes,orders,outer,
       mx,tabs,P,sy,cs,os,dist,sizes1,sums,valid,F,toF,B1,B2,matX,J,D,id,
       pf,B,alpha,SLgroup,g,outerSums,dividing;
S:=CharacterTable("L4(3)");; A:=CharacterTable("L4(3).2^2");;
Check(Identifier(S)="L4(3)" and Size(S)=6065280 and Identifier(A)="L4(3).2^2" and Size(A)=24261120,"table identities");;
names:=["L4(3).2_1","L4(3).2_2","L4(3).2_3"];;expected:=[[1080],[117,117,10530],[8424]];;
inners:=[];; outerfull:=[];;
for k in [1..3] do
 t:=CharacterTable(names[k]);; sf:=GetFusionMap(S,t);;tf:=GetFusionMap(t,A);; pw:=PowerMap(t,2);; sizes:=SizesConjugacyClasses(t);; orders:=OrdersClassRepresentatives(t);;
 Check(Identifier(t)=names[k] and Size(t)=12130560,"intermediate table");;
 Check(IsClassFusionOfNormalSubgroup(S,sf,t) and IsClassFusionOfNormalSubgroup(t,tf,A),"normal index-two fusions");;
 Check(ForAll([1..Length(sf)],i->OrdersClassRepresentatives(S)[i]=orders[sf[i]]) and ForAll([1..Length(tf)],i->orders[i]=OrdersClassRepresentatives(A)[tf[i]]),"fusions preserve orders");;
 Check(Sum(sizes)=Size(t) and ForAll([1..Length(sizes)],i->sizes[i]*SizesCentralizers(t)[i]=Size(t)),"class size and centralizer totals");;
 Check(Length(sf)=NrConjugacyClasses(S) and ForAll(sf,x->IsInt(x) and x in [1..NrConjugacyClasses(t)]),"socle fusion");;
 Check(Length(tf)=NrConjugacyClasses(t) and ForAll(tf,x->IsInt(x) and x in [1..NrConjugacyClasses(A)]),"outer fusion");;
 Check(Length(pw)=Length(sizes) and ForAll(pw,x->IsInt(x) and x in [1..Length(sizes)]),"power map");;
 Check(Filtered([1..Length(sizes)],i->pw[i]=1)=Filtered([1..Length(sizes)],i->orders[i] in [1,2]),"class orders");;
 outer:=Filtered([1..Length(sizes)],i->pw[i]=1 and not i in sf);;
 Check(SortedList(List(outer,i->sizes[i]))=expected[k],"outer class roster");;
 Add(inners,List(sf,i->tf[i]));;Add(outerfull,List(outer,i->tf[i]));;
 Print(names[k]," outside class sizes ",List(outer,i->sizes[i]),"\n");;
od;
Check(inners[1]=inners[2] and inners[2]=inners[3],"consistent socle fusion");;
Check(outerfull=[[22],[34,34,35],[48]],"outer full class fusion");;
Check(List([22,34,35,48],i->SizesConjugacyClasses(A)[i])=
      [1080,234,10530,8424],"full-Aut outer class sizes");;

mx:=Maxes(S);; tabs:=List(mx,CharacterTable);;
Check(ForAll([1..Length(mx)],i->tabs[i]<>fail and Identifier(tabs[i])=mx[i]),"all Maxes tables");;
Check(List(mx)= ["3^3:L3(3)","3^3:L3(3)","U4(2).2","L4(3)M4","3^4:2(A4xA4).2","(4xA6):2","A6.2_2","S4xS4"],"complete stored Maxes");;
Check(List(Filtered([1..Length(mx)],i->Size(tabs[i]) mod 25920=0),i->[mx[i],Size(tabs[i])])=[["U4(2).2",51840],["L4(3)M4",51840]],"graph stabilizer maxima");;

P:=PSL(4,3);;Check(IsPermGroup(P) and Size(P)=6065280 and LargestMovedPoint(P)=40 and IsTransitive(P,[1..40]),"natural PSL40");;
sy:=SylowSubgroup(P,2);;Check(Size(sy)=128,"Sylow2 order");;
cs:=ConjugacyClassesSubgroups(sy);; os:=Filtered(List(cs,Representative),x->Size(x)=16);;
Check(Length(os)=43,"all Sylow subgroup conjugacy classes order16");;
dist:=Collected(List(os,x->Number(Elements(x),y->Order(y)=2 and NrMovedPoints(y)=32)));;
Check(dist=[[1,13],[3,12],[5,12],[7,4],[9,2]],"split2+2 involutions in all order16 classes");;
Print("Sylow order16 class distribution: ",dist,"\n");;

sizes1:=[117,117,10530];; sums:=Set(List(Filtered(Combinations(sizes1),x->Length(x)>0),Sum));;
valid:=Filtered(sums,x->6065280 mod x=0);;Check(valid=[117,234,10530],"graph class sums");;
Check(6065280/1080=5616 and 6065280/8424=720 and 6065280/10530=576,"non-symplectic stabilizer orders");;
Check(ForAll([5616,720,576,25920],x->x mod 16=0),"2-part criterion");;

# Exact F3 matrices from the F9=F3[i], i²=−1, trace-determinant construction.
F:=GF(3);; toF:=rows->List(rows,r->List(r,x->x*One(F)));;
B1:=toF([[0,0,2,0],[0,0,0,1],[1,0,0,0],[0,2,0,0]]);;
B2:=toF([[0,0,2,1],[0,0,1,1],[1,2,0,0],[2,2,0,0]]);;
matX:=toF([[0,2,0,0],[1,0,0,0],[0,0,0,2],[0,0,1,0]]);;
J:=toF([[0,1,0,0],[2,0,0,0],[0,0,0,1],[0,0,2,0]]);;
D:=toF([[2,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,1]]);;
id:=IdentityMat(4,F);; pf:=B->B[1][2]*B[3][4]-B[1][3]*B[2][4]+B[1][4]*B[2][3];;
Check(matX^2=-id and DeterminantMat(matX)=One(F),"matX order/determinant");;
for B in [B1,B2] do
 Check(TransposedMat(B)=-B and DeterminantMat(B)<>Zero(F),"B alternating");;
 Check(TransposedMat(matX)*B*matX=-B,"matX symplectic similitude -1");;
 Check(TransposedMat(B*matX)=-(B*matX) and pf(B)=pf(B*matX),"same Pfaffian squareclass");;
od;
Check(pf(B1)=One(F) and pf(B2)=-One(F),"both Pfaffian classes");;
Check(D^2=id and DeterminantMat(D)=One(F) and TransposedMat(D)*J*D=J and
      TransposedMat(J*D)=-(J*D) and pf(J*D)=-pf(J),"cross-class split involution");;
# Convention alpha_B(g)=B^-1*(g^-1)^T*B. Verify alpha_B alpha_BX
# is conjugation by matX on a set of SL4 generators, and similarly for J,D.
alpha:=function(B,g) return B^-1*TransposedMat(g^-1)*B;end;;
SLgroup:=SpecialLinearGroup(4,3);;
for B in [B1,B2] do
 for g in GeneratorsOfGroup(SLgroup) do
  Check(alpha(B,alpha(B*matX,g))=matX^-1*g*matX,"same-class graph product convention");
 od;
od;
for g in GeneratorsOfGroup(SLgroup) do
 Check(alpha(J,alpha(J*D,g))=D^-1*g*D,"cross-class graph product convention");
od;
# Each index-two G has two outer labels in its outside Aut(S) coset.
# Both must be represented in the selected set, since K generates G.
outerSums:=[8658,18954,19188,9504,1314,11610,11844];;
dividing:=Filtered(outerSums,x->12130560 mod x=0);;
Check(dividing=[18954],"index-two outside-label class sums");;
Check(12130560/18954=640 and ForAll([640,320],x->x mod 16=0),
      "surviving sum has split-involution obstruction");;
Print("index-two sums ",outerSums,", unique divisor ",dividing,"\n");;
Print("PASS: subgroup, outer classes, Sylow, sums, and explicit form identities\n");
end;;
Main();;
QUIT_GAP(0);
