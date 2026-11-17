# GAP 4.15.1, run: gap -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_paired_sp6_nonproduct.g
# ATLAS S6(2) version 2.0, 28-point standard generators, updated 2004-11-16:
# https://brauer.maths.qmul.ac.uk/Atlas/clas/S62/gap/S62G1-p28B0.g1
# SHA256 29ab4b3a7d106d23d2479d626560c490a30f7dc8dfbd6a453bfd079ab7f98608
# https://brauer.maths.qmul.ac.uk/Atlas/clas/S62/gap/S62G1-p28B0.g2
# SHA256 bf645103aeff0e2908f14710cfe087f6bda9e9b377b9c7a2c8e42675df645fa3
# H word from ATLAS S6(2) page, maximal-subgroups section U3(3):2:
# https://brauer.maths.qmul.ac.uk/Atlas/clas/S62/
# Explicit g,h select the S5 x C2 subgroup; assertions verify all required facts.
Check:=function(b,s) if not b then Print("FAIL ",s,"\n"); ForceQuitGap(1); fi; end;;
Check(GAPInfo.Version="4.15.1","GAP version");
a:=(2,3)(6,7)(9,10)(12,14)(17,19)(20,22);;
b:=(1,2,3,4,5,6,8)(7,9,11,13,16,18,14)(10,12,15,17,20,19,21)(22,23,24,25,26,27,28);;
g:=(2,14,19,3,15)(5,8,28,22,20)(6,11,18,23,7)(9,26,21,13,10)(12,27,17,24,25);;
h:=(1,16)(5,26)(8,21)(9,20)(10,22)(13,28);;
G:=Group(a,b);; Check(g in G and h in G,"explicit subgroup generators lie in G");
H:=Group(a*b^2*a*b*a*b^3*a*b^4*a,b);; H1:=DerivedSubgroup(H);;
K:=Group(g,a,h);; K1:=Group(g,a);; R:=Intersection(H,K);;
Check(List([G,H,H1,K,K1,R],Size)=[1451520,12096,6048,240,120,2],"orders");
Check(IsSimpleGroup(G) and IsSimpleGroup(H1) and IsNormal(H,H1) and IsNormal(K,K1),"normality/simple");
Check(IsomorphismGroups(K1,SymmetricGroup(5))<>fail,"S5");
Check(IsomorphismGroups(K,DirectProduct(SymmetricGroup(5),CyclicGroup(2)))<>fail,"S5x2");
Check(Size(Intersection(H1,K))=1 and Size(Intersection(H,K1))=1,"exact intersections");
epgroup:=Group((1,2));; ep:=GroupHomomorphismByImages(K,epgroup,[g,a,h],[(),(1,2),()]);;
Check(ep<>fail and Size(Image(ep))=2 and Size(Image(ep,R))=1,"nonzero character kills intersection");
Check(Size(Intersection(H1,Subgroup(H,GeneratorsOfGroup(R))))=1,"r outside H1");
Check(Size(H1)*Size(K)=Size(G) and Size(H)*Size(K1)=Size(G),"factorization orders");
classes:=ConjugacyClasses(G);;
Check(Length(classes)=30 and Sum(List(classes,Size))=Size(G),"complete classes");
Check(ForAll(classes,c->IsConjugate(G,Representative(c),Representative(c)^-1)),"all classes inverse-stable");
Check(Size(H)*Size(K)/2=Size(G),"fiber order");
Print("simple G, 30 complete conjugacy classes, all inverse-stable\n");
Print("nonzero K→C2 kills R; R outside H1; fiber product order 1451520 and proper projections 12096,240\n");
Print("sizes G,H,H1,K,K1,R: ",List([G,H,H1,K,K1,R],Size),"\n");
Print("H1 simple; K=S5xC2, K1=S5; intersections H1/K and H/K1 trivial\n");
QUIT_GAP(0);
