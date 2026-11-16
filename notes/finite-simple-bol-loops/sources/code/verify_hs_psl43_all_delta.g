# GAP 4.15.1 / CTblLib 1.3.11; published tables and group identifications are inputs.
LoadPackage("ctbllib");;
if GAPInfo.Version<>"4.15.1" then Error("GAP version"); fi;
if PackageInfo("ctbllib")[1].Version<>"1.3.11" then Error("CTblLib version"); fi;
Check := function()
local t,full,subs,n,ts,f,maps,e,ext,classes,i,j,counts,bounds,ce;
 t:=CharacterTable("L4(3)"); full:=CharacterTable("L4(3).2^2");
 subs:=List(["L4(3).2_1","L4(3).2_2","L4(3).2_3"],CharacterTable);
 if t=fail or full=fail or fail in subs then Error("missing table"); fi;
 n:=Size(t); if n<>6065280 or Size(full)<>4*n then Error("orders"); fi;
 ts:=Filtered([1..NrConjugacyClasses(t)],i->OrdersClassRepresentatives(t)[i]=2);
 if ts<>[2,3] or SizesCentralizers(t){ts}<>[2880,1152] then Error("inner classes"); fi;
 maps:=[]; counts:=[];
 for e in subs do
  if Size(e)<>2*n then Error("index-two order"); fi;
  f:=GetFusionMap(t,e); if f=fail then Error("T fusion"); fi;
  ext:=Filtered([1..NrConjugacyClasses(e)],i->OrdersClassRepresentatives(e)[i]=2 and not i in f);
  ce:=SizesCentralizers(e){ext};
  if not ForAll(ce,x->x mod 2=0) then Error("centralizers"); fi;
  Add(counts,List(ce,x->x/2));
  f:=GetFusionMap(e,full); if f=fail then Error("full fusion"); fi;
  Add(maps,Set(f));
 od;
 if counts<>[[5616],[51840,51840,576],[720]] then Error("external centralizers"); fi;
 if Length(Set(maps))<>3 then Error("distinct cosets"); fi;
 e:=subs[1]; f:=GetFusionMap(t,e);
 if 25 in f or OrdersClassRepresentatives(e)[25]<>2 or Positions(f,f[3])<>[3] or ClassMultiplicationCoefficient(t,2,2,3)<>18 or
  ClassMultiplicationCoefficient(t,3,3,3)<>72 or ClassMultiplicationCoefficient(e,25,25,f[3])<>24 then Error("common class"); fi;
 if not (2880*720<n and 5616*576<n and 5616*720<n and 576*720<n and 2880*1152<n and 720^2<n) then Error("thresholds"); fi;
 if not ForAll([2880,1152,5616,51840,576,720],c->n mod c=0) then Error("class divisibility"); fi;
 classes:=List([2880,1152,5616,51840,576,720],c->n/c);
 if classes<>[2106,5265,1080,117,10530,8424] then Error("class sizes"); fi;
 bounds:=[1+2*(classes[1]+classes[2])+2*classes[4]^2+4*classes[4]*classes[5],
  2*classes[3]+4*classes[4]*classes[6],
  4*(classes[1]+classes[2])*classes[4]+2*(2*classes[4]+classes[5]),
  2*classes[6]+4*classes[3]*classes[4]];
 if bounds<>[4970161,3944592,3471156,522288] or not ForAll(bounds,x->x<n) then Error("bounds"); fi;
 Print("HS PSL4(3) four bounds: ",bounds," < ",n,"\n");
end;;
Check();;
QUIT;
