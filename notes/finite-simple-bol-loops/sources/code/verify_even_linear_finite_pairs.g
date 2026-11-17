# 0323:C0010, LWX linear rows12–15. Finite checks only; see
# manuscripts/even-linear-finite-factor-pairs.md for mathematical/source inputs.
(function()
 local check,q,n,gl,j,k,ck,s,a,o,sz,f,i,glorder,weighted,R,lower,upper,T;
 check:=function(v,m) if not v then Error(m); fi; end;
 check(LoadPackage("ctbllib")<>fail,"CTblLib unavailable");
 check(GAPInfo.Version="4.15.1" and PackageInfo("ctbllib")[1].Version="1.3.11","versions");
 q:=3; n:=5;
 gl:=Product([0..n-1],i->q^n-q^i);
 # Odd characteristic: an involution is determined by its + and - eigenspaces.
 j:=Sum([0..n],k->gl/(Product([0..k-1],i->q^k-q^i)*Product([0..n-k-1],i->q^(n-k)-q^i)));
 check(gl=475566474240 and j=1783784,"GL5 order or involution count");
 check(gl/2=237783237120 and gl/2>17472*j,"capacity");
 s:=CharacterTable("L2(13)"); a:=CharacterTable("L2(13).2");
 check(s<>fail and a<>fail and Size(s)=1092 and Size(a)=2184,"table orders");
 check(OrdersClassRepresentatives(s)[2]=2 and Size(s)/SizesCentralizers(s)[2]=91,"inner X class");
 o:=OrdersClassRepresentatives(a); sz:=List([1..NrConjugacyClasses(a)],i->Size(a)/SizesCentralizers(a)[i]);
 check(Filtered([1..Length(o)],i->o[i]=2)=[2,9] and sz[2]=91 and sz[9]=78,"involution classes");
 check(Filtered([1..Length(o)],i->o[i]=3)=[3] and sz[3]=182,"order-three class");
 f:=GetFusionMap(s,a); check(f=[1,2,3,4,5,6,7,8,8],"normal fusion");
 check(ClassMultiplicationCoefficient(a,2,2,3)=6 and ClassMultiplicationCoefficient(a,9,9,3)=6,"class squares");
 glorder:=function(d,t) return Product([0..d-1],i->t^d-t^i); end;
 weighted:=Sum([0..3],k->glorder(3,3)/(glorder(k,3)*glorder(3-k,3))*3^k);
 check(weighted=1432 and 6065280/2880=2106 and 2106>weighted,"row12 capacity");
 for q in [2,4] do
  R:=q^2;
  lower:=R^5*(R^6-1)/(q-1);
  upper:=2*(q+1)*(1+(R^2+1)*(R^6-1)+R^3*(R^3+1)*(R+1));
  if q=2 then check(lower=4193280 and upper=542496,"q2 values");
  else check(lower=5864061665280 and upper=45970265600,"q4 values"); fi;
  check(lower>upper,"G2 capacity");
 od;
 T:=(4^11-1)*(4^10-1)/3;
 check(40*3*16*(16^2-1)=489600 and 489600<4^10,"reverse stabilizer");
 check(4^55>489600*3*(1+T) and 4^45>3*(1+T),"reverse scalar-kernel capacity");
 Print("PASS rows12–15: parabolic and G2 capacities; L2(13) class squares; reverse C3 kernel\n");
end)(); QUIT_GAP(0);
