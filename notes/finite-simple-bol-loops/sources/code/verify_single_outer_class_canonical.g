# C0010: finite sources for canonical G2(3), J2, J3, He and ON exclusions.
# ATLAS/CTblLib complete subgroup classes, structures and character data are inputs.
Check:=function(ok,msg) if not ok then Print("FAIL ",msg,"\n");ForceQuitGap(1);fi;end;;
Check(GAPInfo.Version="4.15.1","GAP version");
Check(LoadPackage("ctbllib")=true,"CTblLib load");
Check(PackageInfo("ctbllib")[1].Version="1.3.11","CTblLib version");
Main:=function()
 local rows,row,s,a,c,f,os,oa,ss,sa,ca,outs,ms,ts,eligible,orders,u,b,unames,uo,l,lm,li;
 rows:=[
 ["G2(3)",4245696,2808,1512,
 ["U3(3).2","G2(3)M2","(3^(1+2)+x3^2):2S4","G2(3)M4","L3(3).2","G2(3)M6","L2(8).3","2^3.L3(2)","L2(13)","2^(1+4)+:3^2.2"],
 ["U3(3).2","G2(3)M2","L2(8).3"],[12096,12096,1512]],
 ["J2",604800,1800,336,
 ["U3(3)","3.A6.2_2","2^1+4b:a5","2^2+4.3xs3","a4xa5","a5xd10","L3(2).2","5^2:D12","A5"],
 ["U3(3)","L3(2).2"],[6048,336]],
 ["J3",50232960,20520,2448,
 ["L2(16).2","L2(19)","J3M3","j3m4","L2(17)","j3m6","3^2.3^(1+2):8","2^1+4b:a5","2^2+4.3xs3"],
 ["L2(17)"],[2448]],
 ["He",4030387200,266560,15120,
 ["S4(4).2","2^2.psl(3,4).s3","2^6:3.s6","2^6:3.s6","2^1+6.psl(3,2)","7^2:2psl(2,7)","3.A7.2","7^(1+2):(S3x3)","s4xpsl(3,2)","7:3xpsl(3,2)","5^2:4A4"],
 ["2^2.psl(3,4).s3","3.A7.2"],[483840,15120]],
 ["ON",460815505920,2624832,175560,
 ["L3(7).2","ONM2","J1","4_2.L3(4).2_1","ONM5","3^4:2^(1+4)D10","L2(31)","ONM8","4^3.L3(2)","M11","ONM11","A7","A7"],
 ["J1"],[175560]] ];
 for row in rows do
  s:=CharacterTable(row[1]);a:=CharacterTable(Concatenation(row[1],".2"));c:=row[4];
  Check(s<>fail and a<>fail and Identifier(s)=row[1],"identified socle tables");
  Check(ExtensionInfoCharacterTable(s)[2]="2","full outer group metadata");
  Check(Size(s)=row[2] and Size(a)=2*Size(s),"orders and extension");
  f:=GetFusionMap(s,a);Check(f<>fail,"stored socle fusion");
  os:=OrdersClassRepresentatives(s);oa:=OrdersClassRepresentatives(a);
  ss:=SizesConjugacyClasses(s);sa:=SizesConjugacyClasses(a);ca:=SizesCentralizers(a);
  Check(IsClassFusionOfNormalSubgroup(s,f,a),"normal index-two fusion");
  Check(ForAll([1..Length(f)],i->os[i]=oa[f[i]]),"fusion preserves orders");
  Check(Sum(ss)=Size(s) and Sum(sa)=Size(a),"class totals");
  Check(ForAll([1..Length(sa)],i->sa[i]*ca[i]=Size(a)),"centralizer/class sizes");
  Check(Filtered([1..Length(oa)],i->PowerMap(a,2)[i]=1)=Filtered([1..Length(oa)],i->oa[i] in [1,2]),"involution power map");
  outs:=Filtered([1..Length(oa)],i->oa[i]=2 and not i in f);
  Check(Length(outs)=1 and sa[outs[1]]=row[3],"one outside involution class");
  Check(Size(s)/row[3]=c and ca[outs[1]]=2*c and c mod 2=0,"even original centralizer order");
  Check(HasMaxes(s),"stored complete maximal list");ms:=Maxes(s);
  Check(ms=row[5],"all maximal class identifiers");ts:=List(ms,CharacterTable);
  Check(ForAll(ts,t->t<>fail),"all maximal tables available");
  orders:=List(ts,Size);eligible:=Filtered([1..Length(ms)],i->orders[i] mod c=0);
  Check(List(eligible,i->ms[i])=row[6] and List(eligible,i->orders[i])=row[7],"all eligible maximal classes");
  Check(Number(orders,x->x=c)=1,"one maximal class of centralizer order");
  Print(row[1]," outer class=",row[3]," centralizer=",c," all maxima=",List([1..Length(ms)],i->[ms[i],orders[i]]),"\n");
 od;
 u:=CharacterTable("U3(3)");b:=CharacterTable("U3(3).2");
 Check(Size(u)=6048 and Size(b)=12096,"unitary overgroup orders");
 f:=GetFusionMap(u,b);Check(f<>fail and IsClassFusionOfNormalSubgroup(u,f,b),"normal unitary subgroup");
 Check(HasMaxes(u),"complete unitary maximal list");unames:=Maxes(u);
 Check(unames=["3^(1+2):8","L3(2)","4.s4","4^2:s3"],"all unitary maximal classes");
 uo:=List(unames,n->Size(CharacterTable(n)));
 Check(uo=[216,168,96,96] and Maximum(uo)<336,"no order336 subgroup in U3(3)");
 Check(Minimum(List(uo,x->Size(u)/x))=28 and 12096/1512=8 and Size(u)>1512,"no order1512 subgroup in U3(3).2");
 l:=CharacterTable("L3(4)");Check(Size(l)=20160 and HasMaxes(l),"L3(4) order and complete maximal list");
 lm:=Maxes(l);Check(lm=["2^4:A5","2^4:A5","A6","L3(4)M4","L3(4)M5","L3(2)","L3(4)M7","L3(4)M8","3^2:Q8"],"all linear maximal classes");
 li:=List(lm,n->Size(l)/Size(CharacterTable(n)));
 Check(li=[21,21,56,56,56,120,120,120,280] and ForAll(li,x->32 mod x<>0),"no proper linear index dividing32");
 Check(483840/15120=32 and Size(l)>15120,"Held overgroup index and quotient order");
 Print("PASS: complete lists and unique outer-class centralizers for G2(3), J2, J3, He and ON.\n");
end;;
Main();
QUIT_GAP(0);
