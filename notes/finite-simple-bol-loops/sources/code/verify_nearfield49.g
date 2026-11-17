# Direct GL(2,7) regular-complement control; GAP 4.15.1.
# A complement L acts regularly on F7^2 minus zero iff |L|=48 and
# every nonidentity matrix has no nonzero fixed vector. Its affine
# action on 49 points is even iff each complement generator is even;
# translations are 7-elements and hence even. An index-two kernel
# contains -I exactly when its character kills the unique central
# involution of any fixed-point-free complement. Normalizer orbits
# classify such kernels for a fixed GL2(7)-conjugacy class of L.
Check:=function(ok,msg) if not ok then Print("FAIL ",msg,"\n");ForceQuitGap(1);fi;end;;
Check(GAPInfo.Version="4.15.1","GAP version");;
Verify:=function()
 local F,G,points,I,minusI,classes,selected,cl,L,g,perms,normalizer,kernels,orbits,K,old,duplicate,counts,regularCount;
 F:=GF(7);G:=GL(2,7);points:=Cartesian(Elements(F),Elements(F));
 I:=IdentityMat(2,F);minusI:=-I;
 Check(Size(G)=2016 and Length(points)=49,"ambient group and vector space");
 classes:=ConjugacyClassesSubgroups(G);selected:=[];counts:=[];regularCount:=0;
 for cl in classes do
  L:=Representative(cl);
  if Size(L)=48 and ForAll(Elements(L),g->g=I or DeterminantMat(g-I)<>Zero(F)) then
   perms:=List(GeneratorsOfGroup(L),g->PermList(List(points,v->Position(points,v*g))));
   regularCount:=regularCount+1;
   if ForAny(perms,g->SignPerm(g)=-1) then
    Print("odd affine complement excluded, normalizer order ",Size(Normalizer(G,L)),"\n");
    continue;
   fi;
   Check(minusI in L,"central involution");
   normalizer:=Normalizer(G,L);
   kernels:=Filtered(NormalSubgroups(L),K->Index(L,K)=2 and minusI in K);
   orbits:=[];
   for K in kernels do
    duplicate:=false;
    for old in orbits do if IsConjugate(normalizer,K,old) then duplicate:=true;break;fi;od;
    if not duplicate then Add(orbits,K);fi;
   od;
   Add(selected,L);Add(counts,Length(orbits));
   Print("regular complement: normalizer order ",Size(normalizer),
         ", index-two kernels ",Length(kernels),", kernel orbits ",Length(orbits),"\n");
  fi;
 od;
 Check(regularCount=3 and Length(selected)=2 and SortedList(counts)=[1,2],"expected complement and kernel orbits");
 Print("PASS GL2(7) subgroup classes ",Length(classes),"; regular complements ",regularCount,"; even complements ",Length(selected),
       "; kernel orbit counts ",SortedList(counts),"; total ",Sum(counts),"\n");
end;;
Verify();;
QUIT_GAP(0);
