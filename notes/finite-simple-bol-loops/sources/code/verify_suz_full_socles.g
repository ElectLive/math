# C0010 Suz full-socle data certificate; maximal lists, table identification
# and stored fusion correctness/completeness are external inputs.
VerifySuz:=function()
 local check,s,a,names,tables,idx,h,f,c,rows,row,ord,cent,subord,
       subpow,superpow,i,j,ext,totals;
 check:=function(ok,label) if not ok then Print("FAIL: ",label,"\n"); ForceQuitGap(1); fi; end;
 check(GAPInfo.Version="4.15.1","GAP version");
 check(LoadPackage("ctbllib")=true,"CTblLib available");
 check(PackageInfo("ctbllib")[1].Version="1.3.11","CTblLib version");
 rows:=[["Suz",448345497600,"G2(4)"],["Suz.2",896690995200,"G2(4).2"]];
 for row in rows do
  s:=CharacterTable(row[1]); check(s<>fail and Size(s)=row[2],"ambient table");
  names:=Maxes(s); tables:=List(names,CharacterTable);
  check(ForAll(tables,x->x<>fail),"all maximal tables available");
  idx:=Filtered([1..Length(names)],i->Size(tables[i])*1782=row[2]);
  check(names{idx}=[row[3]],"unique maximal class of degree 1782");
  h:=tables[idx[1]]; f:=GetFusionMap(h,s); check(f<>fail,"stored fusion");
  c:=InducedClassFunctionsByFusionMap(h,s,[TrivialCharacter(h)],f)[1];
  check(c[1]=1782 and ScalarProduct(s,c,c)=3,"degree and rank");
  Print(row[1]," / ",row[3],": degree 1782, rank 3\n");
 od;
 s:=CharacterTable("Suz"); names:=Maxes(s); tables:=List(names,CharacterTable);
 idx:=Filtered([1..Length(names)],i->Size(tables[i])=13685760);
 check(names{idx}=["U5(2)"],"unique U5(2) maximal entry");
 h:=tables[idx[1]]; check(GetFusionMap(h,s)<>fail,"U5(2) stored fusion");
 a:=CharacterTable("Suz.2"); f:=GetFusionMap(s,a);
 check(f<>fail and Size(a)=2*Size(s),"normal fusion");
 subord:=OrdersClassRepresentatives(s); ord:=OrdersClassRepresentatives(a);
 subpow:=PowerMap(s,2); superpow:=PowerMap(a,2);
 for i in [1..Length(f)] do
  check(subord[i]=ord[f[i]] and f[subpow[i]]=superpow[f[i]],"fusion power map");
 od;
 cent:=SizesCentralizers(a);
 for j in Set(f) do
  totals:=Sum(Filtered([1..Length(f)],i->f[i]=j),i->Size(s)/SizesCentralizers(s)[i]);
  check(totals=Size(a)/cent[j],"normal fusion class-size sum");
 od;
 ext:=Filtered([1..Length(ord)],i->ord[i]=2 and not i in f);
 check(Length(ext)=2 and Set(List(ext,i->cent[i]/2))=[190080,1209600],"outside centralizers");
 Print("Suz outside S-centralizers ",List(ext,i->cent[i]/2),"\n");
 Print("Suz maximal entries, ranks and normal-fusion checks passed\n");
end;;
VerifySuz();;
QUIT_GAP(0);
