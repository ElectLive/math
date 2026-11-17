# GAP 4.15.1, CTblLib 1.3.11; both-solvable Li-Xia v3 Table 4.1 rows 9-11.
# Assumes complete Maxes metadata and correct stored character fusions.
Check:=function(ok,label)
  if not ok then Print("FAIL: ",label,"\n"); ForceQuitGap(1); fi;
end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Check(LoadPackage("ctbllib")=true,"CTblLib");;
Check(GAPInfo.PackagesInfo.ctbllib[1].Version="1.3.11","CTblLib version");;
Verify:=function(name,outer,names,sizes)
 local s,tables,possible,inds,i,h,f,c;
 s:=CharacterTable(name); Check(Size(s)=25920*outer,"ambient");
 Check(Maxes(s)=names,"maximal metadata");
 tables:=List(names,CharacterTable); Check(ForAll(tables,x->x<>fail),"maximal tables");
 Check(List(tables,Size)=sizes,"maximal orders");
 # Union of all factor orders, including both orientations, and all outer choices.
 possible:=[80,160,320,162,324,648,1296];
 inds:=Filtered([1..Length(names)],i->sizes[i] in possible and sizes[i]<>25920);
 Check(Length(inds)=2 and ForAll(inds,i->sizes[i]=648*outer),"all survivors");
 for i in inds do
   h:=tables[i]; f:=GetFusionMap(h,s); Check(f<>fail,"stored fusion");
   c:=InducedClassFunctionsByFusionMap(h,s,[TrivialCharacter(h)],f)[1];
   Check(c[1]=40,"degree"); Check(ScalarProduct(s,c,c)=3,"rank");
   Print(name," / ",names[i],": degree 40, rank 3\n");
 od;
end;;
Verify("U4(2)",1,["P1/G1/L1/V1/ext2","A6.2_1","3^(1+2)+:2A4","3^3:S4`","b33141"],[960,720,648,648,576]);;
Verify("U4(2).2",2,["U4(2)","mo62","S6x2","3^(1+2)+:2S4","s3wrs3","w(f4)"],[25920,1920,1440,1296,1296,1152]);;
QUIT_GAP(0);
