# Proposed C0010 Li-Xia Table 1.2 row 16 certificate. GAP 4.15.1.
# Run gap -A -q -b path/to/verify_sp6_plus36_folders.g.
# No downloaded source data, network, or loop sufficiency claim.
# Trusted GAP algorithms and installed libraries are pinned below.
# See code/README.md and nonbruck-almost-simple-radical-bridge.md for inputs.
Check:=function(b,msg) if not b then Print("FAIL: ",msg,"\n"); ForceQuitGap(1);fi;end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
f:=GF(2);; v:=Tuples(Elements(f),6);; S:=SymplecticGroup(6,2);;
q:=x->x[1]*x[6]+x[2]*x[5]+x[3]*x[4];;
forms:=List(v,u->List(v,x->q(x)+u*x));;
Check(Length(Set(forms))=64,"distinct quadratic refinements");;
gens:=GeneratorsOfGroup(S);;
perms:=List(gens,g->PermList(List(forms,z->Position(forms,List(v,x->z[Position(v,x*g^-1)])))));;
Check(not fail in perms,"generators preserve refinement family");;
P64:=Group(perms);;Check(Size(S)=1451520 and Size(P64)=Size(S),"faithful action");;
orbs:=Orbits(P64,[1..64]);;Check(SortedList(List(orbs,Length))=[28,36],"orbit sizes");;
plus:=First(orbs,o->Length(o)=36);;P:=Action(P64,plus);;Check(Size(P)=Size(S),"plus action faithful");;
Check(IsPrimitive(P,[1..36]),"plus action primitive");;
# Plus/minus certification: the zero-parameter form q has 36 zeros, so is plus.
Check(Length(Filtered(v,x->q(x)=Zero(f)))=36,"plus type");;
Check(Position(forms,List(v,q)) in plus,"the 36 orbit contains the plus form");;
T:=SylowSubgroup(P,3);; classes3:=ConjugacyClassesSubgroups(T);;
es:=Filtered(List(classes3,Representative),x->Size(x)=27 and Size(DerivedSubgroup(x))=3 and Exponent(x)=3);;
Check(Length(es)=1,"unique extraspecial exponent-3 Sylow-subgroup class");;
ex27:=es[1];;A:=Normalizer(P,ex27);;
Check(Size(A)=1296 and Size(PCore(A,3))=27 and PCore(A,3)=ex27,"upper group and 3-core");;
Check(IsTransitive(A,[1..36]),"upper group transitive");;
cs:=ConjugacyClassesSubgroups(A);;Check(Length(cs)=96,"subgroup class count");;
trans:=Filtered(List(cs,Representative),x->IsTransitive(x,[1..36]));;
Sort(trans,function(x,y) return [Size(x),Size(DerivedSubgroup(x))]<[Size(y),Size(DerivedSubgroup(y))];end);;
Check(Collected(List(trans,x->[Size(x),Size(DerivedSubgroup(x)),Size(Stabilizer(x,1))]))=
[[[216,27,6],1],[[216,54,6],1],[[432,108,12],1],[[648,216,18],1],[[1296,648,36],1]],"five transitive classes");;
CheckMarks:=function(G)
 local aut,inv,t,els,H,cl,valid,base,rest,sub,flat,n,counts,nt;
 aut:=AutomorphismGroup(G);; els:=Elements(aut);; H:=Stabilizer(G,1);;counts:=[0,0,0,0];;nt:=0;;
 for t in els do
  if Order(t) in [1,2] then
   nt:=nt+1;;inv:=Filtered(Elements(G),x->Image(t,x)=x^-1);;
   if Length(inv)>=36 and Size(Group(inv))=Size(G) then
    counts[1]:=counts[1]+1;;
    cl:=OrbitsDomain(G,inv,function(x,g) return Image(t,g^-1)*x*g;end);;
    valid:=Filtered(cl,o->Length(o)<=36 and ForAll(o,x->ForAll(o,y->x=y or not x^-1*y in H)));;
    base:=First(valid,o->One(G) in o);;
    if base<>fail then
     counts[2]:=counts[2]+1;;
     rest:=Filtered(valid,o->o<>base and Length(o)+Length(base)<=36 and ForAll(o,x->ForAll(base,y->not x^-1*y in H)));;
     for sub in Combinations(rest) do
      if Length(base)+Sum(List(sub,Length))=36 then
       counts[3]:=counts[3]+1;;flat:=Concatenation(Concatenation([base],sub));;
       if ForAll(flat,x->ForAll(flat,y->x=y or not x^-1*y in H)) and Size(Group(flat))=Size(G) then counts[4]:=counts[4]+1;fi;
      fi;
     od;
    fi;
   fi;
  fi;
 od;
 Print("group ",Size(G)," derived ",Size(DerivedSubgroup(G))," aut ",Size(aut)," involutive ",nt," stage ",counts,"\n");
 Check(counts[4]=0,"marked folder candidate survived");
 return counts;
end;;
results:=List(trans,CheckMarks);;
Check(results=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[36,0,0,0],[118,1,0,0]],"stage counts");;
for pin in [["gapdoc","1.6.7"],["primgrp","4.0.1"],["smallgrp","1.5.4"],["transgrp","3.6.5"]] do
 Check(IsBound(GAPInfo.PackagesLoaded.(pin[1])) and GAPInfo.PackagesLoaded.(pin[1])[2]=pin[2],Concatenation("loaded package ",pin[1]));
od;
Print("PASS: all five transitive subgroup classes fail the marked-folder necessary conditions\n");;
QUIT_GAP(0);
