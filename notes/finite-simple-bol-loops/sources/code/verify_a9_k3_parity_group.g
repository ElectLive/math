# C0010, G=(S6×S3)∩A9: outer-mark capacity, GAP 4.15.1.
# AutomorphismGroup, IsomorphismPermGroup and conjugacy algorithms are inputs.
Verify:=function()
 local G,A,iso,P,N,cosets,coset,left,inv,classes,t,cl,types,counts,
       masks,mask,sz,i,order,one;
 Assert(0,GAPInfo.Version="4.15.1");
 G:=Group((1,2,3),(1,2,3,4,5),(4,5,6),(7,8,9),(1,2)(7,8));
 Assert(0,Size(G)=2160 and Size(Centre(G))=1);
 Assert(0,ForAll(GeneratorsOfGroup(G),g->SignPerm(g)=1 and Set(OnSets([1..6],g))=[1..6] and Set(OnSets([7..9],g))=[7..9]));
 A:=AutomorphismGroup(G); iso:=IsomorphismPermGroup(A); P:=Image(iso);
 N:=Group(List(GeneratorsOfGroup(G),g->Image(iso,InnerAutomorphism(G,g))));
 Assert(0,Size(P)=8640 and Size(N)=2160 and IsNormal(P,N));
 cosets:=RightCosets(P,N); Assert(0,Length(cosets)=4);
 types:=[];
 for coset in cosets do
  if One(P) in coset then continue; fi;
  inv:=Filtered(AsList(coset),x->Order(x)=2); left:=Set(inv); classes:=[];
  while Length(left)>0 do
   t:=left[1]; cl:=AsSet(ConjugacyClass(N,t));
   Assert(0,IsSubset(left,cl)); Add(classes,cl); SubtractSet(left,cl);
  od;
  counts:=SortedList(List(classes,Length)); Add(types,counts);
  for mask in [1..2^Length(counts)-1] do
   sz:=Sum(Filtered([1..Length(counts)],i->QuoInt(mask,2^(i-1)) mod 2=1),i->counts[i]);
   Assert(0,sz<>120);
  od;
  Print("noninner coset: outside involution class sizes ",counts,"\n");
 od;
 Assert(0,SortedList(types)=[[3,15,15,135],[36],[108]]);
 Print("all noninner marked unions miss degree 120\n");
end;;
Verify();;QUIT_GAP(0);
