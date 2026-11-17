# 0323:C0010 G2 antiflag endpoint: table arithmetic and an ATLAS matrix.
# GAP 4.15.1, CTblLib 1.3.11. No network access or AtlasRep is required.
# This does not verify the source's module completeness or geometric embedding.
# Matrix: https://brauer.maths.qmul.ac.uk/Atlas/exc/G22/gap/U33G1-f2r6B0.g1
# Downloaded source SHA256:
# 1bc35417e67f777488139d79bc9848939f2c40466c3060ca2983bb874277a65e
(function()
 local check,t,aTable,orders,classes,sizes,j,a,one;
 check:=function(b,msg) if not b then Error(msg);fi;end;
 check(LoadPackage("ctbllib")<>fail,"CTblLib unavailable");
 check(GAPInfo.Version="4.15.1" and PackageInfo("ctbllib")[1].Version="1.3.11","version mismatch");
 t:=CharacterTable("U3(3).2");
 check(t<>fail and Size(t)=12096,"automorphism table order");
 orders:=OrdersClassRepresentatives(t);
 classes:=Filtered([1..Length(orders)],i->orders[i]=2);
 sizes:=List(classes,i->SizesConjugacyClasses(t)[i]);
 check(sizes=[63,252],"involution class sizes");
 j:=1+Sum(sizes);check(j=316,"involution count");
 check(6048 mod 6=0 and 2*j<6048/6,"capacity");
 aTable:=CharacterTable("U3(3)");
 check(Size(aTable)=6048 and Number(OrdersClassRepresentatives(aTable),x->x=2)=1,"unique inner involution class");
 a:=[
 [1,0,0,0,0,0],
 [0,1,0,0,0,0],
 [0,0,0,0,0,1],
 [0,0,1,1,0,1],
 [1,1,0,0,1,0],
 [0,0,1,0,0,0]
 ]*Z(2);
 one:=IdentityMat(6,GF(2));
 check(a<>one and a*a=one,"published generator is an involution");
 check(RankMat(a-one)=2,"published involution rank");
 Print("U3(3).2: involution sizes 63,252; j=316; 632<1008; unique inner class; ATLAS rank 2\n");
end)();
QUIT_GAP(0);
