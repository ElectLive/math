# M24 affine factor: exact natural AGL4(2) and automorphism/involution checks.
# Run with GAP 4.15.1: gap -q -b --quitonbreak /absolute/path/to/file
# Matrix/group and automorphism algorithms are GAP inputs; no network is used.
Check:=function(ok,label)
  if not ok then Print("FAIL: ",label,"\n");ForceQuitGap(1);fi;
end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Main:=function()
 local f,ident,zero,mx,g,iso,p,v,a,inn,cc,orders,num;
 f:=GF(2); ident:=IdentityMat(4,f); zero:=Zero(f)*[1,1,1,1];
 mx:=function(linear,translation)
  local x,i;
  x:=IdentityMat(5,f);
  for i in [1..4] do x[i]{[1..4]}:=linear[i]; od;
  x[5]{[1..4]}:=translation;
  return x;
 end;
 g:=Group(Concatenation(List(GeneratorsOfGroup(GL(4,2)),x->mx(x,zero)),
                           List(ident,x->mx(ident,x))));
 iso:=IsomorphismPermGroup(g); p:=Image(iso);
 Check(Size(p)=322560 and LargestMovedPoint(p)=16 and Size(Centre(p))=1,"affine group");
 v:=Image(iso,Group(List(ident,x->mx(ident,x))));
 Check(Size(v)=16 and IsElementaryAbelian(v) and IsNormal(p,v),"translation subgroup");
 Check(Size(SolvableRadical(p))=16 and v=SolvableRadical(p),"solvable radical");
 a:=AutomorphismGroup(p); inn:=InnerAutomorphismsAutomorphismGroup(a);
 Check(Size(a)=322560 and Size(inn)=Size(a),"all automorphisms inner");
 cc:=ConjugacyClasses(p); orders:=List(cc,c->Order(Representative(c)));
 num:=Sum(Filtered([1..Length(cc)],i->orders[i] in [1,2]),i->Size(cc[i]));
 Check(num=1696,"identity and involutions");
 Print("PASS: AGL4(2), complete automorphism group, 1696 elements of order at most two\n");
end;;
Main();;
QUIT_GAP(0);
