# 0323:C0010 Held/Rudvalis supporting data. GAP 4.15.1, CTblLib 1.3.11.
# Stored maximal-list completeness, class fusion and names are external inputs.
Check:=function(b,s) if not b then Print("FAIL: ",s,"\n"); ForceQuitGap(1); fi; end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Check(LoadPackage("ctbllib")=true and GAPInfo.PackagesInfo.ctbllib[1].Version="1.3.11","CTblLib version");;
Main:=function()
 local f,l,id,inv,ct,he,he2,sp,sp2,names,ts,fus,ord,cs,idx,k,cl,sz;
 f:=GF(7); l:=GL(2,7); id:=One(l); inv:=Filtered(AsList(l),x->x*x=id);
 ct:=List(inv,x->7^Length(NullspaceMat(x+id)));
 Check(Size(l)=2016 and Length(inv)=58,"GL2(7) involutions");
 Check(Number(ct,x->x=1)=1 and Number(ct,x->x=7)=56 and Number(ct,x->x=49)=1 and Sum(ct)=442,"affine involutions");
 he:=CharacterTable("He"); he2:=CharacterTable("He.2"); sp:=CharacterTable("S4(4)"); sp2:=CharacterTable("S4(4).2");
 Check(Size(he)=4030387200 and Size(he2)=2*Size(he) and Size(sp)=979200 and Size(sp2)=2*Size(sp),"table orders");
 names:=Maxes(he); Check(names=["S4(4).2","2^2.psl(3,4).s3","2^6:3.s6","2^6:3.s6","2^1+6.psl(3,2)","7^2:2psl(2,7)","3.A7.2","7^(1+2):(S3x3)","s4xpsl(3,2)","7:3xpsl(3,2)","5^2:4A4"],"complete maximal list");
 ts:=List(names,CharacterTable); Check(ForAll(ts,x->x<>fail),"maximal tables");
 Check(Filtered([1..Length(ts)],i->Size(ts[i]) mod 979200=0)=[1] and Size(ts[1])=1958400,"unique Sp4 normalizer candidate");
 Check(Filtered([1..Length(ts)],i->Size(ts[i]) mod 16464=0)=[6] and Size(ts[6])=16464,"unique 7-local maximal candidate");
 for k in [[he,he2,15120,266560],[sp,sp2,720,1360]] do
  fus:=GetFusionMap(k[1],k[2]); ord:=OrdersClassRepresentatives(k[2]); cs:=SizesCentralizers(k[2]);
  Check(fus<>fail and ForAll(fus,x->IsInt(x) and x>=1 and x<=Length(ord)),"valid fusion");
  Check(IsClassFusionOfNormalSubgroup(k[1],fus,k[2]),"normal subgroup fusion");
  Check(ForAll(ord,IsInt) and ForAll(cs,IsInt),"integer class data");
  sz:=SizesConjugacyClasses(k[2]); Check(ForAll(sz,IsInt) and Sum(sz)=Size(k[2]),"class size sum");
  idx:=Filtered([1..Length(ord)],i->ord[i]=2 and not i in fus);
  Check(Length(idx)=1 and cs[idx[1]]/2=k[3] and Size(k[2])/cs[idx[1]]=k[4],"outside involution class");
  cl:=PowerMap(k[2],2); Check(cl<>fail and ForAll(cl,x->IsInt(x) and x>=1 and x<=Length(ord)),"valid power map");
  Check(Filtered([1..Length(ord)],i->cl[i]=1)=Filtered([1..Length(ord)],i->ord[i] in [1,2]),"square consistency");
 od;
 Check(15120<16464 and 15120<979200 and 1360<2058 and 442<2058,"capacity inequalities");
 Print("He maximal list and both outside involution classes verified; affine count 442; bounds 1360,442 < 2058.\n");
end;;
Main();;
QUIT_GAP(0);
