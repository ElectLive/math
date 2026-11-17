# C0010, Li-Xia Table 1.2 row 11: primitive stabilizer ranks.
# GAP 4.15.1, CTblLib 1.3.11; run gap -q -b /absolute/path/to/file.
# Completeness and identification of maximal classes and fusion maps are
# external ATLAS/CTblLib data inputs, not derived by this certificate:
# https://www.math.rwth-aachen.de/homes/Thomas.Breuer/ctbllib/ctbltoc/data/U4%282%29.html
# https://www.math.rwth-aachen.de/homes/Thomas.Breuer/ctbllib/ctbltoc/data/U4%282%29.2.html
Check:=function(ok,label)
  if not ok then Print("FAIL: ",label,"\n"); ForceQuitGap(1); fi;
end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Check(LoadPackage("ctbllib")=true,"CTblLib available");;
Check(GAPInfo.PackagesInfo.ctbllib[1].Version="1.3.11","CTblLib version");;
Verify:=function(name,index,expectedNames,expectedSizes,expectedSurvivors)
 local s,names,tables,sizes,possible,inds,i,h,f,c;
 s:=CharacterTable(name); Check(s<>fail and Size(s)=25920*index,"ambient order");
 names:=Maxes(s); Check(names=expectedNames,"complete maximal metadata");
 tables:=List(names,CharacterTable); Check(ForAll(tables,x->x<>fail),"maximal tables");
 sizes:=List(tables,Size); Check(sizes=expectedSizes,"maximal orders");
 # In the outer case I projects onto M/S, excluding the maximal subgroup S.
 possible:=List([60,120,360,720,960], n->n*index);
 inds:=Filtered([1..Length(names)],i->sizes[i] in possible and sizes[i]<>25920);
 Check(List(inds,i->names[i])=expectedSurvivors,"all eligible maximal classes");
 Check(List(inds,i->Size(s)/sizes[i])=[27,36],"degrees and uniqueness");
 for i in inds do
   h:=tables[i]; f:=GetFusionMap(h,s); Check(f<>fail,"stored fusion");
   c:=InducedClassFunctionsByFusionMap(h,s,[TrivialCharacter(h)],f)[1];
   Check(c[1]=Size(s)/Size(h),"induced degree");
   Check(ScalarProduct(s,c,c)=3,"permutation rank");
   Print(name," / ",names[i],": degree ",Size(s)/Size(h),", rank 3\n");
 od;
end;;
Verify("U4(2)",1,["P1/G1/L1/V1/ext2","A6.2_1","3^(1+2)+:2A4","3^3:S4`","b33141"],[960,720,648,648,576],["P1/G1/L1/V1/ext2","A6.2_1"]);;
Verify("U4(2).2",2,["U4(2)","mo62","S6x2","3^(1+2)+:2S4","s3wrs3","w(f4)"],[25920,1920,1440,1296,1296,1152],["mo62","S6x2"]);;
QUIT_GAP(0);
