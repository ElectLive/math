# 0323:C0010, reversed F4(2) triality row: finite table checks only.
# GAP 4.15.1, CTblLib 1.3.11. ATLAS/CTblLib identifications, complete Maxes,
# subgroup fusions and character values remain external inputs.
Check:=function(ok,label)
 if not ok then Print("FAIL: ",label,"\n");ForceQuitGap(1);fi;
end;;
Check(GAPInfo.Version="4.15.1","GAP version");
Check(LoadPackage("ctbllib")=true,"CTblLib load");
Check(PackageInfo("ctbllib")[1].Version="1.3.11","CTblLib version");
Main:=function()
 local t,s,i,h,u,v,names,tables,orders,elig,f,oh,ot,ct,cs,ids,j,k,coef,independent;
 t:=CharacterTable("3D4(2)");s:=CharacterTable("F4(2)");
 i:=CharacterTable("S8(2)");h:=CharacterTable("S3xL2(8)");
 u:=CharacterTable("U3(3)");v:=CharacterTable("U3(3).2");
 Check(ForAll([t,s,i,h,u,v],x->x<>fail),"tables available");
 Check(List([t,s,i,h,u,v],Identifier)=["3D4(2)","F4(2)","S8(2)",
    "S3xL2(8)","U3(3)","U3(3).2"],"table identifiers");
 Check(Size(t)=211341312 and Size(s)/Size(i)=69888 and Size(t)/69888=3024,
       "actual intersection order");
 Check(ExtensionInfoCharacterTable(t)[2]="3","triality outer order");
 Check(HasMaxes(t),"triality maximal list available");names:=Maxes(t);
 tables:=List(names,CharacterTable);Check(ForAll(tables,x->x<>fail),"maximal tables available");
 orders:=List(tables,Size);
 Check(orders=[258048,86016,12096,3024,2352,1296,1176,216,52],"triality complete maximal orders");
 elig:=Filtered([1..Length(names)],j->orders[j] mod 3024=0);
 Check(List(elig,j->names[j])=["U3(3).2","S3xL2(8)"],"all eligible maximal classes");
 Check(Size(h)=3024 and Size(v)=12096 and Size(u)=6048 and IsPerfect(u),"eligible group metadata");
 f:=GetFusionMap(u,v);Check(f<>fail and IsClassFusionOfNormalSubgroup(u,f,v),"normal U3 fusion");
 Check(HasMaxes(u),"U3 maximal list available");
 names:=Maxes(u);tables:=List(names,CharacterTable);
 Check(ForAll(tables,x->x<>fail),"U3 maximal tables available");
 orders:=List(tables,Size);Check(Maximum(orders)=216,"U3 proper subgroup bound");
 Check(Size(u)/Maximum(orders)>4,"no index at most four in U3");
 f:=GetFusionMap(h,t);Check(f<>fail,"intersection fusion");
 oh:=OrdersClassRepresentatives(h);ot:=OrdersClassRepresentatives(t);
 ct:=SizesConjugacyClasses(t);cs:=SizesConjugacyClasses(h);
 ids:=Filtered([1..Length(ot)],j->ot[j]=2);
 Check(ids=[2,3] and ct{ids}=[819,68796],"all triality involution classes");
 ids:=Filtered([1..Length(oh)],j->oh[j]=2);
 Check(List(ids,j->f[j])=[3,2,3] and List(ids,j->cs[j])=[63,3,189],
       "actual involution fusion and root-class witness");
 for j in [2,3] do
   k:=2;coef:=ClassMultiplicationCoefficient(t,j,j,k);
   independent:=ct[j]^2/Size(t)*Sum(Irr(t),ch->ch[j]^2*GaloisCyc(ch[k],-1)/ch[1]);
   Check(coef=independent and coef=[18,2268][j-1],"class square / character formula");
 od;
 Print("PASS: exact degree/intersection, full maximal screen, root fusion, both class squares\n");
end;;
Main();
QUIT_GAP(0);
