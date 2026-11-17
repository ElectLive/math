# C0010 Fi22 factor orientations. GAP4.15.1, CTblLib1.3.11.
# ATLAS/CTblLib complete maximal lists, characters and fusions are inputs.
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/Fi22.html
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/Fi22.2.html
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/U6%282%29.S3.html
Check:=function(ok,label) if not ok then Print("FAIL: ",label,"\n");ForceQuitGap(1);fi;end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Check(LoadPackage("ctbllib")=true and GAPInfo.PackagesInfo.ctbllib[1].Version="1.3.11","CTblLib version");;
Run:=function()
 local s,a,u,h,names,ts,idx,f,c,o,z,out2,out4,j,pow;
 s:=CharacterTable("Fi22");a:=CharacterTable("Fi22.2");u:=CharacterTable("U6(2).S3");
 Check(Size(s)=64561751654400 and Size(a)=2*Size(s),"sporadic orders");
 Check(Identifier(u)="U6(2).3.2" and Size(u)=55180984320,"unitary automorphism table identity and order");
 # Identification with full Aut(PSU6(2)) is an ATLAS input, not proved by table order.
 names:=Maxes(s);Check(names=["2.U6(2)","O7(3)","Fi22M3","O8+(2).3.2","2^10:m22","2^6:s6f2","(2x2^(1+8)):U4(2):2","S3xU4(3).2_2","2F4(2)'","2^(5+8):(S3xA6)","3^(1+6):2^(3+4):3^2:2","A10.2","A10.2","M12"],"complete maximal metadata");
 ts:=List(names,CharacterTable);Check(ForAll(ts,x->x<>fail),"maximal tables");
 idx:=Filtered([1..Length(ts)],i->Size(ts[i]) mod 18393661440=0);
 Check(List(idx,i->names[i])=["2.U6(2)"] and Size(ts[idx[1]])=18393661440,"unique component class");
 h:=ts[idx[1]];f:=GetFusionMap(h,s);Check(f<>fail,"component fusion");
 c:=InducedClassFunctionsByFusionMap(h,s,[TrivialCharacter(h)],f)[1];
 Check(c[1]=3510 and ScalarProduct(s,c,c)=3,"degree3510 rank3");
 f:=GetFusionMap(s,a);Check(f<>fail and ForAll(f,x->IsInt(x) and x>=1 and x<=NrConjugacyClasses(a)),"sporadic extension fusion");
 Check(IsClassFusionOfNormalSubgroup(s,f,a),"normal Fi22 fusion");
 o:=OrdersClassRepresentatives(a);z:=SizesConjugacyClasses(a);
 Check(ForAll(o,IsInt) and ForAll(z,IsInt) and Sum(z)=Size(a),"Fi22.2 class data");
 pow:=PowerMap(a,2); Check(pow<>fail and ForAll(pow,x->IsInt(x) and x>=1 and x<=Length(o)),"Fi22.2 square map");
 Check(Filtered([1..Length(o)],i->pow[i]=1)=Filtered([1..Length(o)],i->o[i] in [1,2]),"Fi22.2 square consistency");
 out2:=Filtered([1..Length(o)],i->o[i]=2 and not i in f);
 out4:=Filtered([1..Length(o)],i->o[i]=4 and not i in f);
 Check(Set(List(out2,i->Size(s)/z[i]))=Set([1045094400,3317760,2903040]) and Length(out2)=3,"outside order2 centralizers");
 Check(Set(List(out4,i->Size(s)/z[i]))=Set([663552,122880,9216,6144,1536]) and Length(out4)=5,"outside order4 centralizers");
 Check(ForAll(Concatenation(out2,out4),i->Size(s)/z[i]<Size(h)),"no outside element centralizes component");
 o:=OrdersClassRepresentatives(u);z:=SizesConjugacyClasses(u);
 Check(ForAll(o,IsInt) and ForAll(z,IsInt) and Sum(z)=Size(u),"unitary class data");
 pow:=PowerMap(u,2); Check(pow<>fail and ForAll(pow,x->IsInt(x) and x>=1 and x<=Length(o)),"unitary square map");
 Check(Filtered([1..Length(o)],i->pow[i]=1)=Filtered([1..Length(o)],i->o[i] in [1,2]),"unitary square consistency");
 j:=Sum(Filtered([1..Length(o)],i->o[i] in [1,2]),i->z[i]);
 Check(j=1529056 and 2*j<3592512,"unitary involution capacity");
 Check(Size(s)=17971200*3592512,"Tits index");
 Print("Fi22: rank3 degree3510; all exterior order2/4 centralizers small; capacity 3058112<3592512\n");
end;;
Run();;
QUIT_GAP(0);
