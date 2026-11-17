# Central Bruck extensions and intrinsic direct decompositions

*Mira Cult*

## Scope, baseline, and conclusions

This manuscript continues PR 446 at delivery revision
7653409e6155cd87c7f91ba810b155f517c7f44b, whose scientific source was
9059767c0ef28809bbe17de8a71ba0a8b11d0485. The canonical starting multiplication,
identity proofs, and graph recovery theorem are in
[graph-eisenstein-loops.md](../../graph-loops/manuscripts/graph-eisenstein-loops.md). They are not reproved or
silently modified here.

The principal result is a decomposition theorem for a broader class than the
graph family: finite Bruck loops of prime exponent, with central associators and
a trilinear associator map. Their associator tensors determine their central
extensions; primitive centroid idempotents then determine their nonassociative
direct factors. The theorem includes characteristic two and characteristic three.
Trilinearity is an explicit hypothesis, not an assertion about every class-two
Bruck loop.

A consequential obstruction follows. Every nonzero one-marker construction
L(B), after its central elementary abelian factor is removed, is directly
indecomposable, even when B has many orthogonal blocks. Thus a disconnected
graph does not usually give a direct-product decomposition of the PR 446 loop.
Orthogonal blocks instead give a fiber product over a common marker, sometimes
followed by a central quotient. A component-marker modification restores a
faithful graph functor that carries disjoint unions to genuine direct products.

The centroid and adjoint-ring methods are established bilinear/tensor methods;
see [W10, Sections 5.2--5.3] and [W08, Theorem 4.4 and Corollary 4.5]. The proofs
below establish their precise realization for these Bruck extensions. They do
not claim invention of the centroid method, a classification of all Bol loops,
or a resolution of graph reconstruction.

## Conventions and the central extension model

Use left Bruck throughout: the left Bol law is

```math
x(y(xz))=(x(yx))z,
```

and the automorphic inverse property is
$`(xy)^{-1}=x^{-1}y^{-1}`$. Bol loops are power-associative; exponent p means
that every element has p-th power one. All vector spaces in the main theorems
are finite-dimensional over the **prime field** F_p.

Suppose A is a central elementary abelian subgroup of a loop L and L/A is the
elementary abelian group U. A normalized section identifies L with U times A
and gives the multiplication

```math
(u,s)(v,t)=(u+v,s+t+f(u,v)),\qquad
f(0,u)=f(u,0)=0.                                      \tag{1}
```

Its associator, with the convention $`(xy)z=x(yz)+D(x,y,z)`$, is

```math
D(u,v,w)=f(u,v)+f(u+v,w)-f(v,w)-f(u,v+w).              \tag{2}
```

This map is independent of the section. Neither arbitrary f nor arbitrary
trilinear D is presumed to give a Bruck loop.

<a id="extension-rigidity"></a>
### Associator rigidity for prime-exponent Bruck extensions

**Theorem ER.** Let L_f and L_g be central extensions as in (1), with specified
identifications of their quotient U and central subgroup A. Suppose both are
Bruck loops of exponent p and have the same associator function (2). Then there
is a loop isomorphism L_f to L_g inducing the identity on U and on A.
Trilinearity is not required in this theorem.

**Proof.** First choose inverse-compatible sections. For odd p, choose a lift
for each pair {u,-u} and use its inverse for the other member; use one at zero.
For p=2 every element of either loop is its own inverse, so any normalized
section has this property. Their factor sets, still denoted f,g, satisfy

```math
f(u,-u)=0,\qquad f(-u,-v)=-f(u,v),                  \tag{3}
```

and the same equations for g. The second equality is precisely AIP applied to
the two section elements and the central correction.

Put c=f-g. Equality of the associators says that the operation

```math
(u,s)\circ(v,t)=(u+v,s+t+c(u,v))
```

is an associative group law. Equations (3) give its inverse as (-u,-s) and give
it AIP. A group with automorphic inversion is abelian, by comparison with
the ordinary identity $`(xy)^{-1}=y^{-1}x^{-1}`$.

For each u, the recursively computed p-th power of the lift (u,0) has central
coordinate

```math
\sum_{j=0}^{p-1}f(ju,u).
```

It is zero in L_f, and the corresponding sum is zero in L_g. Subtraction proves
that the abelian group defined by c has exponent p. It is therefore an F_p-vector
space. Its exact sequence with kernel A and quotient U splits linearly. Equivalently,
for a normalized function h:U to A,

```math
c(u,v)=h(u)+h(v)-h(u+v).
```

The map $`(u,s)\mapsto(u,s+h(u))`$ is then the required isomorphism L_f to L_g.
Transporting back from the inverse-compatible sections completes the proof. □

The assumptions carry real information. Without AIP and for odd p, an abelian
group and a nonabelian class-two exponent-p group can have the same zero associator but
different commutators. Without exponent p, C_(p^2) and C_p times C_p are Bruck
extensions of C_p by C_p with the same zero associator and different power data.
For binary code/Moufang loops, square and commutator data cannot simply be omitted:
that family is not covered solely by being Moufang.

**Automorphism consequence.** If A is characteristic, every isomorphism of
the pair of vector spaces U,A preserving D lifts to a loop automorphism. Indeed,
transporting the extension by this pair of linear maps gives another extension
with the same D, to which Theorem ER applies. The kernel consists exactly of
central shears $`(u,s)\mapsto(u,s+h(u))`$ for linear h:U to A. Thus

```math
1\longrightarrow\mathop{\mathrm{Hom}}\nolimits_{\mathbb F_p}(U,A)
 \longrightarrow\mathop{\mathrm{Aut}}\nolimits(L)
 \longrightarrow\mathop{\mathrm{Aut}}\nolimits(D)\longrightarrow1.          \tag{4}
```

No splitting of this exact sequence is claimed in general.

## Removing the central elementary abelian factor

For the rest of the general theorem let L be a finite Bruck loop of exponent p
whose associator subloop A is central. Here A is the subgroup generated by all
associators; its centrality makes the distinction between normal generation and
ordinary generation immaterial. The quotient L/A is a group and inherits AIP,
so it is abelian. Consequently both A and U=L/A are elementary abelian p-groups.
Assume that D:U^3 to A is trilinear. It is full: its values span A.

For a trilinear map define its common radical by

```math
\mathop{\mathrm{rad}}\nolimitsD=\{u:D(u,U,U)=D(U,u,U)=D(U,U,u)=0\}.           \tag{5}
```

The inverse image of (5) in L is its nucleus. For Bruck loops the nucleus is the
center. Here is the needed argument, rather than a change of terminology. If a
is nuclear, so is a^(-1), and reassociation gives

```math
(ax)(x^{-1}a^{-1})=a((xx^{-1})a^{-1})=1,
```

and similarly in the other order. Thus $`(ax)^{-1}=x^{-1}a^{-1}`$. AIP also gives
$`(ax)^{-1}=a^{-1}x^{-1}`$. Varying x proves that a commutes with every element.
The nucleus is a group, so its inverse-closure used here is valid; alternatively,
in the present central setting it follows at once from the vector subspace (5).
Therefore, with C=Z(L),

```math
C/A=\mathop{\mathrm{rad}}\nolimitsD.                           \tag{6}
```

Since C is elementary abelian, choose a vector-space complement S to A in C.
Its dimension is

```math
d=\dim C-\dim A.                                  \tag{7}
```

The image of S in U is C/A. Extend its inverse map to a linear map U to S.
Composing with L to U gives a homomorphic retraction L to S. Because S is
central, its kernel K supplies an actual direct product

```math
L\cong S\times K\cong C_p^{\,d}\times (L/S).         \tag{8}
```

The core L/S has center equal to its associator subgroup A, and its associator
is the full, radical-free map induced on U/(C/A).

**Canonicity qualification.** S is not usually characteristic. Its dimension
and the isomorphism type of L/S are intrinsic. To prove the latter, two complements
of A in C differ by a linear map C/A to A. Extend it to h:U to A. The central
shear in (4) carries one complement to the other and hence identifies the two
quotients. Thus all choices give the same core isomorphism type. An actual
chosen direct factor in (8) need not be preserved by all automorphisms.

## The centroid and the direct-decomposition theorem

Let D:U^3 to A now be full and have zero common radical. Its balanced centroid is

```math
\begin{split}
\mathcal C(D)=\{(P,Q)\in\mathop{\mathrm{End}}\nolimits(U)\times\mathop{\mathrm{End}}\nolimits(A):
&D(Px,y,z)=D(x,Py,z)\\
&=D(x,y,Pz)=Q D(x,y,z)\quad\text{for all }x,y,z\}.
\end{split}                                                     \tag{9}
```

It is a unital associative F_p-algebra under componentwise addition and
composition. It is also commutative. For (P,Q) and (P',Q') in the centroid,
evaluating D(Px,P'y,z) in the two orders gives QQ'D(x,y,z)=Q'QD(x,y,z).
Fullness gives QQ'=Q'Q. The centroid relations then put the image of
PP'-P'P in the common radical, so PP'=P'P. Fullness and zero radical also imply
that either coordinate of an element of (9) determines the other.

A complete primitive idempotent frame is a family of nonzero idempotents
epsilon_i=(e_i,f_i) whose sum is the identity, whose pairwise products are zero,
and none of which splits further into two nonzero orthogonal idempotents.
Such a frame exists by successive refinement; each refinement splits a nonzero
subspace of U, so the process terminates. The frame is unique as an unordered
family. Indeed, given two primitive frames {epsilon_i} and {delta_j}, the
products epsilon_i delta_j decompose epsilon_i into orthogonal idempotents.
Primitivity leaves exactly one nonzero term, and applying the same observation
to delta_j proves that the two frames agree.

Put U_i=e_i U and A_i=f_i A. The centroid relations give

```math
U=\bigoplus_i U_i,\qquad A=\bigoplus_i A_i,
\qquad D(U_i,U_j,U_k)=0\text{ unless }i=j=k.        \tag{10}
```

Each restricted tensor D_i:U_i^3 to A_i is full and radical-free. Its centroid
has no nontrivial idempotent: otherwise extension by zero on the other blocks
would refine epsilon_i.

**Theorem RD.** Let L satisfy the hypotheses preceding (5). Remove the central
factor (8), and let epsilon_i be the primitive frame of the centroid of its
radical-free associator. With pi:L/S to U/(C/A), set

```math
H_i=\pi^{-1}(U_i),\qquad
L_i=H_i/\bigoplus_{j\ne i}A_j.                    \tag{11}
```

Then each L_i is a nonassociative directly indecomposable Bruck loop of exponent p,
and

```math
L\cong C_p^{\,d}\times\prod_i L_i.                \tag{12}
```

The integer d and the multiset of isomorphism types of the L_i are intrinsic.
The H_i are an intrinsic family of actual subloops of the chosen core, permuted
by its automorphisms, and (11) are actual subquotients. The theorem does not
identify H_i themselves with the direct factors in (12).

**Proof.** Each H_i is a subloop because it is the inverse image of a subspace
of the elementary abelian quotient. The subgroup divided out in (11) is central.
Thus L_i inherits the Bruck and exponent-p laws. It has central subgroup A_i,
quotient U_i, and associator D_i. The product of the L_i is a central Bruck
extension of U by A with associator (10). Theorem ER identifies that product
with the core L/S. Combining with (8) proves (12).

For indecomposability, a direct product of loops induces a direct product of
their associator subgroups, quotients, and associator maps. A nontrivial direct
product decomposition of L_i therefore yields a proper centroid idempotent,
unless one factor has zero quotient by its associator subgroup. In the latter
case that factor equals its own central associator subgroup and hence is an
abelian group; its associator subgroup is then trivial, so the factor is trivial.
Equivalently, an associative factor would contribute a nonzero common-radical
summand, which D_i does not have. This proves direct indecomposability.

An isomorphism of loops induces an isomorphism of the tensor data and conjugates
their centroids. It permutes the unique primitive frame, giving the intrinsic
subquotient types in (11). The independence of the central complement S was
proved above. Conversely, any direct decomposition must give a partition of
this frame; its indecomposable nonassociative members have precisely the types
in (11). □

If L is associative, A=0, its AIP makes it abelian, and the theorem has only the
factor C_p^d=L. The empty centroid frame is used in that case.

The method is constructive once the central multiplication and tensor data are
given: solve the linear equations (9), find its idempotent frame, and use the
subquotients (11). No running-time theorem for recognizing the hypotheses from
an arbitrary succinctly presented loop is claimed. The group analogues and
computational ring machinery in [W10] are methodological baselines, not automatic
loop algorithms.

## One-marker loops have one nonassociative direct core

Let B:W times W to Z be any nonzero alternating F_p-bilinear map, not necessarily
graphical. Use the PR 446 law

```math
L(B):\quad(a,u,s)(b,v,t)
=(a+b,u+v,s+t+(a+2b)B(u,v)).                        \tag{13}
```

Its associator is

```math
D((a,u),(b,v),(c,w))
=aB(v,w)-bB(u,w)-2cB(u,v).                         \tag{14}
```

Let A be the span of the values of B and R=rad B. Equation (14) shows that the
associator subgroup is A, and the center is

```math
Z(L(B))=\{(0,r,s):r\in R,\ s\in Z\}.              \tag{15}
```

For example, membership in the left nucleus first forces a=0 by varying v,w,
and then forces u in R by varying the middle marker coordinate. The converse
follows from (14) and the commutator formula 3(a+b)B(u,v).

Choose complements and let B_red:(W/R)^2 to A be the induced full radical-free map.
Then (8) becomes

```math
L(B)\cong C_p^{\,\dim R+\dim Z-\dim A}\times L(B_{\rm red}).
                                                               \tag{16}
```

**Theorem SM.** For every prime p and every nonzero full radical-free B,
L(B) is directly indecomposable. Consequently (16) is the entire nonassociative
direct-core decomposition, not only one possible partial decomposition.

**Proof.** Compute (9) for (14), with U=F_p m direct-sum W. Let (P,Q) be in
the centroid. For u in W write Pu=phi(u)m+S u. Since D(W,W,W)=0,

```math
0=D(Pu,v,w)=\phi(u)B(v,w)
```

forces phi=0. Write Pm=a m+w_0. Then

```math
0=D(Pm,m,v)=-B(w_0,v)
```

forces w_0=0. Finally the three equalities obtained from D(m,u,v) give

```math
aB(u,v)=B(Su,v)=B(u,Sv)=Q B(u,v).
```

Nondegeneracy forces S=a I_W and fullness forces Q=a I_A. Therefore

```math
\mathcal C(D)=\{(aI_U,aI_A):a\in\mathbb F_p\}\cong\mathbb F_p.    \tag{17}
```

It has no proper idempotent, and Theorem RD proves the claim. No step divides
by 2 or 3. □

For graph B_Gamma, A=Z_Gamma and R is spanned by isolated vertices. Therefore
the central elementary abelian factor in (16) has exactly one dimension per
isolated vertex. Any graph with an edge and no isolated vertices gives a directly
indecomposable loop, including a disjoint union of two or more nontrivial components.
In particular L_p(K_(1,3)) is directly indecomposable, whereas
L_p(K_3 disjoint-union K_1) has a C_p direct factor, for every prime p.

This is a sharp obstruction to reading ordinary loop direct products off the
old graph's connected components. It also proves that the one-marker family does
not exhaust the class in Theorem RD: a product of two nonassociative reduced
one-marker loops has two primitive associator-centroid idempotents and cannot
itself be a one-marker L(B) times only an elementary abelian group.

<a id="intrinsic-alternating-map"></a>
## Recovering the reduced alternating map and its automorphisms

The unmarked recovery argument of PR 446 extends from graph maps to arbitrary
alternating maps after (16). This section records the extension because it makes
the subsequent bilinear decompositions intrinsic to the loop.

First allow R=rad B and unused central coordinates Z/A. In U=L(B)/A write
R_0=Z(L(B))/A=R direct-sum (Z/A). For p not three the right-alternative locus is

```math
\{y:D(x,y,y)=0\ (\forall x)\}
=\widehat W\ \cup\ (\mathbb F_pm\oplus R_0),
\qquad \widehat W=W\oplus(Z/A).                    \tag{18}
```

This follows directly from D(x,y,y)=-3bB(u,v). The larger component is uniquely
$`\widehat W`$, since dim(W/R) is at least two. A subspace of a union of two
subspaces lies in one of them: the sum of vectors in their opposite differences
would lie in neither. Their intersection is the intrinsic R_0. Thus
$`X=\widehat W/R_0`$ and the contraction B_red on X are intrinsic, up to invertible
changes of coordinates and a nonzero codomain scalar. A **good marker** is a
vector t outside $`\widehat W`$ with $`D(\widehat W,t,t)=0`$; exactly the nonzero
marker cosets in the smaller component have this property. These are quotient
vectors, not canonical lifts to L.

In the reduced full nondegenerate case this specializes to

```math
\{y:D(x,y,y)=0\ (\forall x)\}=W\cup M,\qquad
M=\mathbb F_pm.                                    \tag{19}
```

Consequently L(B) determines B up to invertible transformations of domain and
codomain whenever p differs from three.

For p=3, in the reduced case put S=m^* wedge im(B^*) in Lambda^3 U^*. The
common-factor space is

```math
\{\ell:\ell\wedge S=0\}
=\mathbb F_3m^*\oplus K,\qquad
K=\{\eta\in W^*:\eta\wedge\mathop{\mathrm{im}}\nolimits(B^*)=0\}.              \tag{20}
```

If K=0, (20) recovers W and contraction again recovers B. If a nonzero eta lies
in K, every scalar form B^*(z^*) has the form eta wedge f: choose a complement
to eta in W^* and compare exterior components. Choose t with eta(t)=1 and put
H=ker eta. Then B(H,H)=0 and

```math
B(at+h,bt+k)=aF(k)-bF(h),\qquad F(h)=B(t,h).        \tag{21}
```

Fullness makes F surjective, while nondegeneracy makes it injective. Thus B is
equivalent to the star map with dim Z=dim W-1, a single isomorphism type for those
dimensions. If dim K is at least two, every scalar form is a multiple of a
single decomposable eta_1 wedge eta_2; fullness and nondegeneracy then force
dim Z=1 and dim W=2. There are no other exceptions. All exceptional maps are
therefore determined by their intrinsic dimensions, even though their marker
hyperplanes are not intrinsic.

It follows, for every prime p, that nonzero loops L(B) are classified by the
intrinsic central factor dimension in (16) together with the equivalence class
of B_red. This is a classification of this explicit family, not of all loops
in Theorem RD or all Bruck loops.

For p not three, the automorphism group of a reduced one-marker loop has the
more explicit split form

```math
\mathop{\mathrm{Aut}}\nolimits(L(B))\cong
\mathop{\mathrm{Hom}}\nolimits_{\mathbb F_p}(U,Z)\rtimes
\{(\lambda,g,h):hB(u,v)=\lambda B(gu,gv)\}.         \tag{22}
```

Here lambda is nonzero, g and h are invertible, and a triple acts by
(a,u,s) to (lambda a,g u,h s). Formula (13) verifies that action directly;
(19) proves that every induced action has this form, and the remaining freedom
is exactly the linear central shear from (4). In characteristic three, marker
shifts m to m+w preserve D and lift by Theorem ER. Thus marker elements and
embedded pieces chosen using a transverse marker need not be preserved by
abstract loop automorphisms.

## Orthogonal maps, common-marker fiber products, and central quotients

Let B:W^2 to Z be full. Suppose

```math
W=\bigoplus_{i=1}^k W_i,\qquad B(W_i,W_j)=0\quad(i\ne j),
\qquad Z_i=\langle B(W_i,W_i)\rangle.               \tag{23}
```

The Z_i sum to Z but need not be independent. Let B_i be the restricted map
with codomain Z_i. Each L(B_i) maps homomorphically to the additive marker group
F_p by (a,u,s) to a. Their fiber product F consists of tuples with all marker
coordinates equal. There is an explicit surjective loop homomorphism

```math
F\longrightarrow L(B),\qquad
((a,u_i,s_i))_i\longmapsto(a,\sum_i u_i,\sum_i s_i).               \tag{24}
```

Equation (23) makes all cross terms vanish, proving multiplicative compatibility.
The kernel is the central subgroup

```math
\{((0,0,s_i))_i:\sum_i s_i=0\}.                    \tag{25}
```

Consequently L(B) is a **central quotient of a fiber product**. If Z is the
direct sum of the Z_i, (24) is an isomorphism and no central quotient remains.
The size of the kernel is p^(sum dim Z_i - dim Z). This construction is not a
central product of the L(B_i): the input is their marker fiber product, not
their ordinary direct product. Theorem SM explains why replacing it by an
ordinary direct-product assertion would be false.

For example, a nondegenerate scalar alternating form on dimension 2r is an
orthogonal sum of r hyperbolic planes, all with the same one-dimensional
codomain. Thus its loop is obtained from the fiber product of r one-edge graph
loops by a central quotient of dimension r-1. For r greater than one the result
is still directly indecomposable. The individual hyperbolic planes are not
canonical: their choices are moved by symplectic automorphisms. The
[central-amalgamation obstruction](loop-deletion-decks.md#central-amalgamation-obstruction)
shows concretely how omitting shared-output information loses parent-loop data
even when specified deletion cards remain isomorphic.

### Independent-image blocks from the bilinear centroid

For full nondegenerate B define

```math
\mathcal C(B)=\{(S,T):B(Su,v)=B(u,Sv)=T B(u,v)\}.                 \tag{26}
```

The same two-slot argument used for (9) proves that this is a commutative unital
algebra. Its unique primitive idempotent frame gives the unique finest
decomposition (23) in which the Z_i are independent. Conversely, the projection
maps of any such decomposition belong to (26). These statements follow by
moving an idempotent between arguments and codomain, exactly as in (10).
This is the established bilinear-centroid correspondence [W10, Lemma 5.19];
the loop interpretation here is (24).

For p not three, (19) makes these blocks intrinsic to the reduced loop. If
pi:L(B) to U and M is the smaller component in (19), the actual subloops

```math
J_i=\pi^{-1}(M\oplus W_i)
```

form an intrinsic family, and

```math
J_i/\bigoplus_{j\ne i} Z_j\cong L(B_i).            \tag{27}
```

Their abstract types and marker quotients give the fiber-product reconstruction
of L(B). The isomorphism in (24) generally requires choices; (27) does not claim
canonical direct-factor subloops. For p=3 the block equivalence classes remain
intrinsic by (20)--(21), but marker shifts usually move the chosen embedded J_i.

### Shared-image blocks from adjoint idempotents

The more general orthogonal decompositions (23) are encoded by self-adjoint
idempotents in the adjoint ring

```math
\mathop{\mathrm{Adj}}\nolimits(B)=\{(S,T):B(Su,v)=B(u,Tv)\},
\qquad (S,T)^*=(T,S),                              \tag{28}
```

where the second coordinate has opposite composition. An idempotent e with
B(eu,v)=B(u,ev) gives W=eW direct-sum (1-e)W with zero cross pairing; conversely
every two-block orthogonal projection has this property. Families of pairwise
orthogonal self-adjoint idempotents summing to one give all (23). This is
[W08, Theorem 4.4 and Corollary 4.5], and the elementary proof just given works
also in characteristic two. These idempotents need not belong to the commutative
centroid (26), and their decompositions need not be canonical. Shared central
images and the relation (25) are indispensable reconstruction data.

### Graph connectedness has an intrinsic bilinear meaning

For B_Gamma with isolated vertices removed, (26) is exactly

```math
\mathcal C(B_\Gamma)\cong\mathbb F_p^{\,c},          \tag{29}
```

where c is the number of connected components. Here is a direct proof. Write
S=(s_ki) in the vertex basis. If k differs from i and k has a neighbor j different
from i, compare the edge {k,j} coefficient in B(S e_i,e_j)=B(e_i,S e_j); it gives
s_ki=0 because the right side has only edges incident with i. If the only neighbor
of k is i, use B(S e_i,e_i)=T B(e_i,e_i)=0 instead. Thus S is diagonal. On every
edge {i,j}, balance forces s_ii=s_jj, and T acts by the same scalar on that edge.
These are exactly the independent component scalars in (29).

In fact every self-adjoint idempotent from (28) also comes from a union of
components. For such an idempotent e, orthogonality gives
B(eu,u)=B(eu,eu)=0, so the preceding coefficient argument applies even when
p=2. Therefore the finest orthogonal decomposition of the graphical map is
precisely its nontrivial connected components, with independent image spaces.

These bilinear component spaces are intrinsic up to permutation under arbitrary
map equivalences, and hence under the abstract loop isomorphisms described above.
For a graph with an edge, its number of isolated vertices is the dimension in
(16), its number of nontrivial components is the number of primitive idempotents
in (29), and the component vertex/edge counts are the domain/codomain dimensions
of those blocks. Connectedness is thus detected intrinsically, but corresponds
to indecomposability of the bilinear data under (23), not to direct
indecomposability of the one-marker loop.

## A graph functor that preserves disjoint unions as direct products

For an ordinary finite graph Gamma, let r be its number of isolated vertices and
let Gamma_1,...,Gamma_c be its edge-containing connected components. Define

```math
\mathscr D_p(\Gamma)=C_p^{\,r}\times
 \prod_{i=1}^c L_p(\Gamma_i).                       \tag{30}
```

This uses one marker per edge-containing component and one additive coordinate
per isolated vertex. The empty graph gives the trivial loop. All laws in each
factor are the graph-native law (13), so nonassociativity is graph-generated
and appears exactly when Gamma has an edge. For n vertices and e edges,

```math
|\mathscr D_p(\Gamma)|=p^{n+e+c}.                  \tag{31}
```

For p=3 this is a commutative Moufang loop; for p not three a graph with an edge
gives a proper Bruck loop. A graph isomorphism permutes components and applies
the PR 446 coordinate transport in each factor. Identity and composition are
respected, giving a functor on the groupoid of finite graphs and isomorphisms.
Reindexing the factors gives specified coherent isomorphisms

```math
\mathscr D_p(\Gamma\sqcup\Delta)
\cong\mathscr D_p(\Gamma)\times\mathscr D_p(\Delta).               \tag{32}
```

**Theorem CM.** For every prime p, the functor (30) is unmarked faithful on
isomorphism types. Its genuine nonassociative direct factors correspond exactly
to the edge-containing connected components, and its maximal central elementary
abelian factor has rank equal to the number of isolated vertices.

**Proof.** Each L_p(Gamma_i) has no isolated coordinates, so its center equals
its associator subgroup. By Theorem SM it is directly indecomposable. The
associator tensor of their direct product is the direct sum of their tensors,
with common radical zero. A balanced centroid endomorphism has no off-diagonal
blocks: inserting one argument from a different summand and the other two from
one fixed summand forces its off-diagonal image into the common radical of that
summand, which is zero. Its diagonal blocks are scalar by (17). Thus the
primitive frame consists exactly of the component projections. Theorem RD
recovers the component loop isomorphism types and the r central cyclic factors.
The PR 446 unmarked graph recovery theorem then recovers each connected graph
Gamma_i. Conversely a graph isomorphism gives the stated loop isomorphism. □

This is a direct-product theorem, with existence and intrinsic factor recovery,
not merely an encoding followed by a graph partition. Its graph-recovery step
retains the established He--Qiao alternating-map dependency of PR 446.

**Morphism limitation.** There is no assertion that every induced embedding is
sent to the old coordinate embedding. For example an induced matching of two
edges can lie in a connected path on five vertices. The source of (30) has two
independent markers. Sending both to the target's single marker creates a
nonzero associator between the first source marker and the second source edge,
where the source associator was zero. Thus the naive component-marker map is
not a loop homomorphism. The groupoid and disjoint-union statements (30)--(32)
are the precise functorial claims.

## Ring coefficients and limits of splitting

The law (13) and the fiber-product/central-quotient formulas (23)--(25) work over
any commutative coefficient ring with the indicated modules. If W has a module
complement to rad B and Z has a module complement to the span of the B-values,
the explicit splitting analogous to (16) also works. The prime-field theorem
does not justify assuming those complements over a general ring.

For a concrete obstruction take K=Z/4, W=K^2, Z=K and B(u,v)=2 det(u,v). The
loop has order 256, associator subgroup A=2Z of order two, and

```math
Z(L)=2K\oplus 2W\oplus Z\cong C_2^3\times C_4.
```

The center calculation follows from (14): its marker and both vertex
coordinates must be even, while the last coordinate is arbitrary. The quotient
Z(L)/A is C_2^4. A complement to A would have to be an elementary abelian subgroup
of order sixteen. But the full two-torsion subgroup of Z(L) already has order
sixteen and contains A. Hence no such complement exists. This prevents the
central splitting argument (8), despite the availability of the all-ring Bruck
law. It does not contradict the prime-exponent theorem: this loop has exponent
four.

The results concern central Bruck extensions, their associator tensors, and the
specified graph-derived families. They do not apply automatically to the
noncentral or finite-simple Bol constructions in other active 0323 workspaces;
simple-factor data do not supply the central gluing or tensor data required here.
No assertion about arbitrary finite Bol/Moufang direct decomposition, unaligned
deletion-deck reconstruction, or the general graph reconstruction conjecture
follows from this manuscript.

## Independently reproducible finite diagnostics

The standard-library checker
[check_bruck_decomposition.py](../code/check_bruck_decomposition.py) runs from
the repository root with

```sh
python notes/finite-simple-bol-loops/loop-decomposition/code/check_bruck_decomposition.py
```

It independently solves the defining linear equations for the bilinear and
trilinear centroids over F_2, F_3, and F_5. The cases are one edge, two disjoint
edges, a scalar symplectic map with shared output, and a three-leaf star. Every
one-marker associator centroid has dimension one; the two-edge graph's
bilinear centroid has dimension two. A direct product of two one-edge loops
has associator-centroid dimension two and exactly four idempotents. These
calculations distinguish the fiber-product and direct-product predictions.

For quotient dimensions two and three over F_2 and dimension two over F_3,
the checker also solves the normalized factor-set equations for the Bol law,
AIP, inverse-compatible sections, and exponent p. In each case the kernel of
the associator map has exactly the dimension of the inverse-compatible
coboundaries, as predicted by Theorem ER. The fiber-product homomorphism is
checked on all 1,024 quotient-product pairs for p=2 and all 59,049 pairs for
p=3. Finally, direct enumeration verifies the orders of the center, its
two-torsion, and the associator subgroup in the Z/4 obstruction.

These are exact, bounded diagnostics. They supplement the proofs; they do not
classify all factor sets, establish a new general identity by sampling, or
certify scientific novelty.

## References and novelty scope

* **[W10]** James B. Wilson, *Finding direct product decompositions in polynomial
  time*, [arXiv:1005.0548v1](https://arxiv.org/abs/1005.0548v1),
  [PDF](https://arxiv.org/pdf/1005.0548v1). Sections 5.2--5.3, especially
  Definition 5.16, Lemma 5.17 and Lemma 5.19, give the bilinear centroid and its
  idempotent correspondence. Theorem 5.21 gives the class-two group consequence.
  Full text inspected. These are methodological baselines; the Bruck-extension
  rigidity and loop conclusions above have their own proofs.
* **[W08]** James B. Wilson, *Finding central decompositions of p-groups*,
  [arXiv:0801.3434v2](https://arxiv.org/abs/0801.3434v2), 31 August 2008,
  [PDF](https://arxiv.org/pdf/0801.3434v2). Theorem 4.4 and Corollary 4.5 identify
  orthogonal bilinear decompositions with self-adjoint idempotent frames. Full
  text inspected. No group central-product theorem is silently applied to loops.
* **PR446 baseline.** [Graph Bruck/Eisenstein construction](../../graph-loops/manuscripts/graph-eisenstein-loops.md),
  especially its exact associator and prime-field unmarked-recovery sections,
  at the source pins given at the start. Its Kepka and He--Qiao citations and
  their original scopes remain in force.

This is a bounded literature comparison. It identifies established construction
and decomposition machinery and proves the additional loop statements explicitly;
it is not an exhaustive novelty certificate for every corollary.
