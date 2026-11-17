# C0010 finite row 26: an actual order-three outer extension moves A9 class.
# GAP 4.15.1, CTblLib 1.3.11. Run: gap -q -b /absolute/path/to/file.
# Maximal-subgroup lists and stored class fusions are ATLAS/CTblLib inputs:
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/O8%2B(2).html
# https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/O8%2B(2).3.html
Check:=function(ok,label) if not ok then Print("FAIL: ",label,"\n"); ForceQuitGap(1); fi; end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Check(LoadPackage("ctbllib")=true,"CTblLib available");;
Check(GAPInfo.PackagesInfo.ctbllib[1].Version="1.3.11","CTblLib version");;
s:=CharacterTable("O8+(2)");; t:=CharacterTable("O8+(2).3");;
Check(Size(s)=174182400 and Size(t)=3*Size(s),"ambient orders");;
names:=Maxes(s);; ts:=List(names,CharacterTable);;
Check(ForAll(ts,x->x<>fail),"all maximal tables");;
idx:=Filtered([1..Length(ts)],i->Size(ts[i]) mod 181440=0);;
Check(List(idx,i->names[i])=["S6(2)","O8+(2)M2","O8+(2)M3","A9","O8+(2)M8","O8+(2)M9"],"maximal divisibility coverage");;
Check(List(idx,i->Size(ts[i]))=[1451520,1451520,1451520,181440,181440,181440],"maximal orders");;
# Sp6(2) is simple, and cannot have an index-8 subgroup: 1451520 > 8!.
Check(1451520>Factorial(8),"index-eight simple-group bound");;
h:=CharacterTable("A9");; f:=GetFusionMap(h,s);; g:=GetFusionMap(s,t);;
Check(f<>fail and g<>fail,"stored fusion maps");;
chi:=InducedClassFunctionsByFusionMap(h,s,[TrivialCharacter(h)],f)[1];;
Check(chi[1]=960,"degree");;
witness:=Filtered(Combinations([1..Length(g)],2),pair->g[pair[1]]=g[pair[2]] and chi[pair[1]]<>chi[pair[2]]);;
Check(Length(witness)>0,"triality moves A9 class");;
Print("A9 class moved; fused socle classes ",witness[1]," have values ",chi[witness[1][1]],", ",chi[witness[1][2]],"\n");
QUIT_GAP(0);
