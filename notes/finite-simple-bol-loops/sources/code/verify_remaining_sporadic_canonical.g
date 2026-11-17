# Finite certificate for 0323-finite-simple-non-moufang-bol-loops:C0010.
# GAP 4.15.1 / CTblLib 1.3.11. Table identification, character-data
# correctness and complete maximal-conjugacy-class lists remain source inputs.
# Run with --quitonbreak so any assertion failure exits nonzero.
Assert(0,GAPInfo.Version="4.15.1");;
Assert(0,LoadPackage("ctbllib")=true);;
Assert(0,PackageInfo("ctbllib")[1].Version="1.3.11");;
Main:=function()
local records,fi22max,fi24max,data,nm,T,A,fusion,ord,cent,out,ins,sizes,
 irr,matrix,i,j,k,row,vals,x,y,found,mask,subset,total,h,covered,reason,
 expected,target,mt,eligible,z,pow2,part,st,at,os,oa,count;
count:=0;;
records:=[
 ["M12",[792],[[[1],120]]],
 ["McL",[113400],[[[1],7920]]],
 ["HN",[75240000],[[[1],3628800]]],
 ["M22",[330,1386],[[[1],1344],[[2],320]]],
 ["HS",[1100,23100],[[[1],40320],[[2],1920]]],
 ["Suz",[370656,2358720],[[[1],1209600],[[2],190080]]],
 ["Fi22",[61776,19459440,22239360],[[[1],1045094400],[[2],3317760],[[3],2903040],[[2,3],1548288]]],
 ["Fi24'",[306936,5686767482760],[[[1],4089470473293004800],[[2],220723937280]]]
];;
fi22max:=["2.U6(2)","O7(3)","Fi22M3","O8+(2).3.2","2^10:m22","2^6:s6f2","(2x2^(1+8)):U4(2):2","S3xU4(3).2_2","2F4(2)'","2^(5+8):(S3xA6)","3^(1+6):2^(3+4):3^2:2","A10.2","A10.2","M12"];;
fi24max:=["Fi23","2.Fi22.2","(3xO8+(3):3):2","O10-(2)","3^7.O7(3)","3^(1+10):U5(2):2","F3+M7","2^2.U6(2).3.2","2^(1+12).3_1.U4(3).2_2'","3^3.[3^10].GL3(3)","3^2.3^4.3^8.(A5x2A4).2","(A4xO8+(2).3).2","He.2","F3+M14","2^(3+12).(L3(2)xA6)","2^(6+8).(S3xA8)","(3^2:2xG2(3)).2","(A5xA9):2","A6xL2(8):3","7:6xA7","U3(3).2","U3(3).2","L2(13).2","L2(13).2","29:14"];;
for data in records do
 nm:=data[1];; T:=CharacterTable(nm);; A:=CharacterTable(Concatenation(nm,".2"));;
 Assert(0,T<>fail and A<>fail and Size(A)=2*Size(T));;
 Assert(0,IsSporadicSimple(T) and ExtensionInfoCharacterTable(T)[2]="2");;
 fusion:=GetFusionMap(T,A);; Assert(0,fusion<>fail);;
 ord:=OrdersClassRepresentatives(A);; cent:=SizesCentralizers(A);;
 os:=OrdersClassRepresentatives(T);; st:=SizesConjugacyClasses(T);;
 at:=SizesConjugacyClasses(A);;
 Assert(0,Length(fusion)=Length(os) and Sum(st)=Size(T) and Sum(at)=Size(A));;
 Assert(0,ForAll([1..Length(ord)],i->cent[i]*at[i]=Size(A)));;
 Assert(0,ForAll([1..Length(fusion)],i->os[i]=ord[fusion[i]]));;
 Assert(0,Sum(Set(fusion),i->at[i])=Size(T));;
 Assert(0,ForAll(Set(fusion),j->Sum(Filtered([1..Length(fusion)],i->fusion[i]=j),i->st[i])=at[j]));;
 Assert(0,Filtered([1..Length(ord)],i->PowerMap(A,2)[i]=1)=Filtered([1..Length(ord)],i->ord[i] in [1,2]));;
 out:=Filtered([1..Length(ord)],i->ord[i]=2 and not i in fusion);;
 ins:=Filtered(Set(fusion),i->ord[i]=2);;
 sizes:=List(out,i->Size(A)/cent[i]);; Assert(0,sizes=data[2]);;
 irr:=Irr(A);; matrix:=[];;
 for i in out do row:=[];;
  for j in out do vals:=[];;
   for k in ins do
    x:=ClassMultiplicationCoefficient(A,i,j,k);;
    y:=Size(A)/cent[i]/cent[j]*Sum(irr,ch->ch[i]*ch[j]*ComplexConjugate(ch[k])/ch[1]);;
    Assert(0,IsInt(x) and x>=0 and y=x);; Add(vals,x);;
   od; Add(row,vals);;
  od; Add(matrix,row);;
 od;
 found:=[];;
 for mask in [1..2^Length(out)-1] do
  subset:=Filtered([1..Length(out)],i->QuoInt(mask,2^(i-1)) mod 2=1);;
  total:=Sum(subset,i->sizes[i]);;
  if Size(T) mod total<>0 then continue; fi;
  h:=Size(T)/total;; Add(found,[subset,h]);; count:=count+1;;
  covered:=List([1..Length(ins)],k->ForAny(subset,i->ForAny(subset,j->matrix[i][j][k]>0)));;
  if ForAll(covered,x->x) then
   Assert(0,h mod 2=0);; reason:="all involutions captured";;
  elif (nm="Fi22" or nm="Fi24'") and subset=[1] then
   Assert(0,h mod 2=0 and ForAny(covered,x->x));;
   if nm="Fi22" then expected:=fi22max;; target:="O8+(2).3.2";;
   else expected:=fi24max;; target:="Fi23";; fi;
   Assert(0,Maxes(T)=expected);;
   mt:=List(expected,CharacterTable);; Assert(0,ForAll(mt,x->x<>fail));;
   eligible:=Filtered([1..Length(mt)],i->Size(mt[i]) mod h=0);;
   Assert(0,Length(eligible)=1 and expected[eligible[1]]=target and Size(mt[eligible[1]])=h);;
   reason:="unique maximal centralizer";;
  elif nm="Fi22" and (subset=[2] or subset=[3]) then
   Assert(0,ins=[2,3,4] and covered=[false,true,true]);;
   Assert(0,ClassMultiplicationCoefficient(A,2,2,2)=0);;
   z:=Size(A)/cent[2]^2*Sum(irr,ch->ch[2]*ch[2]*ComplexConjugate(ch[2])/ch[1]);;
   Assert(0,IsInt(z) and z=0);;
   pow2:=Filtered(ord,x->x=2^LogInt(x,2));; Assert(0,Maximum(pow2)=16);;
   part:=2^Valuation(h,2);; Assert(0,part in [8192,1024] and part/2>16);;
   reason:="unique-involution Sylow contradiction";;
  else Error("unresolved selection ",nm," ",subset); fi;
  Print(nm," ",subset," H=",h," ",reason,"\n");
 od;
 Assert(0,found=data[3]);;
od;
Assert(0,count=15);;
Print("all eight groups, all 15 integral selections: stored-data assertions passed\n");;
end;;
Main();;
QUIT_GAP(0);
