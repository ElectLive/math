# Concrete degree343 sharply two-homogeneous factor control; GAP4.15.1.
# No external files/network; finite witness only, not uniform exhaustion.
Check:=function(b,s) if not b then Print("FAIL ",s,"\n"); ForceQuitGap(1); fi; end;;
Check(GAPInfo.Version="4.15.1","version");
f:=GF(7^3);; elems:=Elements(f);; z:=Z(7^3);;
perm:=function(fun) return PermList(List(elems,x->Position(elems,fun(x)))); end;;
a:=perm(x->z^3*x);; b:=perm(x->z*x^7);;
Check(Order(a)=114 and b^3=a^19 and b^-1*a*b=a^7,"semilinear relations");
c:=a^2;; e:=a*b;;
L0:=Group(c,e);; Check(Size(L0)=171 and not IsAbelian(L0),"nonabelian complement");
v:=Group(List([One(f),z,z^2],t->perm(x->x+t)));;
B0:=ClosureGroup(v,L0);;
Check(Size(v)=343 and Size(B0)=343*171,"group orders");
Check(ForAll(GeneratorsOfGroup(B0),g->SignPerm(g)=1),"even group");
pair:=[Position(elems,Zero(f)),Position(elems,One(f))];;
orb:=Orbit(B0,pair,OnSets);;
Check(Length(orb)=343*342/2,"sharp 2-homogeneity");
Print("L0=171 nonabelian; B0=58653 even; 58653 unordered pairs form one orbit\n");
QUIT_GAP(0);
