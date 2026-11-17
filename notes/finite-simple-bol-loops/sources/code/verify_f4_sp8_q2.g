# Conditional CTblLib finite endpoint for C0010 F4(2) Sp8 orientation.
Check:=function(b,s) if not b then Print("FAIL: ",s,"\n"); ForceQuitGap(1); fi; end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Check(LoadPackage("ctbllib")=true and GAPInfo.PackagesInfo.ctbllib[1].Version="1.3.11","CTblLib version");;
Main:=function() local t,o,c,p,j,n;
 t:=CharacterTable("S8(2)"); Check(Identifier(t)="S8(2)" and Size(t)=47377612800,"Sp8 table");
 o:=OrdersClassRepresentatives(t);c:=SizesConjugacyClasses(t);p:=PowerMap(t,2);
 Check(ForAll(o,IsInt) and ForAll(c,IsInt) and Sum(c)=Size(t),"class data");
 Check(p<>fail and ForAll(p,x->IsInt(x) and x>=1 and x<=Length(o)),"power map");
 Check(Filtered([1..Length(o)],i->p[i]=1)=Filtered([1..Length(o)],i->o[i] in [1,2]),"square consistency");
 j:=Sum(Filtered([1..Length(o)],i->o[i] in [1,2]),i->c[i]);n:=2^12*(2^4-1)*(2^8-1)/3;
 Check(j=1371136 and n=5222400 and 2*j<n,"capacity");
 Print("j(Sp8(2))=",j,"; 2j < ",n,".\n");
end;;Main();;QUIT_GAP(0);
