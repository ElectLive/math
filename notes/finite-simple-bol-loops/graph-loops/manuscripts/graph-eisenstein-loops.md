# Graph-derived Bruck loops, a Moufang specialization, and Eisenstein coefficients

Mira Cult

## Scope and provenance

This manuscript constructs a finite loop from every finite simple graph. Its
central multiplication correction and its associators are calculated from the
graph's exterior edge map. Over a prime field of characteristic other than three,
the unmarked loop determines the graph. In characteristic three the same law is a
commutative Moufang law; an unmarked recovery theorem still holds, with a separate
treatment of stars. Directed, colored graphs admit faithful **marked** versions,
including over finite Eisenstein rings. Colors are not claimed to survive arbitrary
unmarked loop isomorphisms.

The general loop mechanism is an explicit specialization of Kepka's 1984
trilinear construction of Bruck loops [Kep84, Section 2, Propositions 2.4 and 2.6].
It is not a new general Bruck-loop construction. The graph specialization,
intrinsic recovery argument, and graph/subloop dictionary are the results under
investigation here. The final step of graph recovery uses the established
Baer--Lovasz--Tutte alternating-map theorem [HQ20, Proposition 1.2]; this dependency
is stated explicitly. The corresponding extremal and maximal-associative-subloop
payoff has its canonical proof in [graph-associative-subloops.md](graph-associative-subloops.md).
The characteristic-two Moufang alternative is treated separately in
[graph-cubic-loops.md](graph-cubic-loops.md).

All proofs below are algebraic. Small-instance verification is supplementary,
not a substitute for them. No permanent claim IDs are allocated by this manuscript.

## The all-ring Bruck construction

Let K be a commutative ring with identity, let W and Z be K-modules, and let

    B : W x W -> Z

be K-bilinear and alternating: B(u,u)=0 for all u. Thus
B(u,v)=-B(v,u), including in characteristic two. Put U=K m direct-sum W and
write elements of L=K direct-sum W direct-sum Z as (a,u,s). Define

```math
(a,u,s)*(b,v,t)
 =(a+b,\ u+v,\ s+t+(a+2b)B(u,v)).                 \tag{1}
```

The central coefficient 2 is the integer acting on the module. Neither 2 nor 3
needs to be invertible. The construction works over rings with zero divisors.

### Loop axioms, inverse, and exact left Bol convention

The identity is (0,0,0). If x=(a,u,s) and the desired product is z=(c,w,r), the
unique solutions to x*y=z and y*x=z are respectively

```math
\begin{split}
x\backslash z
 &=\bigl(c-a,w-u,r-s-(2c-a)B(u,w-u)\bigr),\\
z/x
 &=\bigl(c-a,w-u,r-s-(c+a)B(w-u,u)\bigr).
\end{split}                                                    \tag{2}
```

This proves both division axioms directly. The two-sided inverse of x is -x,
because B(u,-u)=0. The subgroup 0 direct-sum 0 direct-sum Z is central: inserting
a central element adds its coordinate and changes no correction term.

Here and below the left Bol identity means exactly

```math
x*(y*(x*z))=(x*(y*x))*z.                         \tag{3}
```

For a transparent verification, consider temporarily the two-parameter correction

```math
f_{\alpha,\beta}((a,u),(b,v))=(\alpha a+\beta b)B(u,v).
```

Let x=(a,u), y=(b,v), z=(c,w) denote quotient coordinates in U. In the difference
between the central coordinates of the left and right sides of (3), the coefficient
of B(u,v) cancels. The coefficients of B(u,w) and B(v,w) are respectively
(beta-2 alpha)(a+b) and (beta-2 alpha)a. Thus the exact residual is

```math
(\beta-2\alpha)\bigl((a+b)B(u,w)+aB(v,w)\bigr).   \tag{4}
```

For completeness, this is obtained by substituting in the normalized central
extension equation

```math
f(x,z)+f(y,x+z)+f(x,x+y+z)
 -f(y,x)-f(x,x+y)-f(2x+y,z).
```

With alpha=1 and beta=2, (4) vanishes over every K. This proves (3).
More generally, this entire two-parameter family is left Bol if and only if

```math
(\beta-2\alpha)B(W,W)=0.                         \tag{5}
```

Necessity follows from (4) by taking a=0, b=1 and v=0; sufficiency follows from
the same formula. In particular, over a field with B nonzero, beta=2 alpha is
forced within this explicit polynomial ansatz. A bilinear central correction
without the marker factors has zero associator and only produces a group.

Since the correction in (1) is cubic,

```math
(-x)*(-y)=-(x*y)=(x*y)^{-1}.
```

Consequently L has the automorphic inverse property and is a **left Bruck loop**,
not merely a left Bol loop. Its powers are x^j=(ja,ju,js): this follows by induction
from B(ju,u)=0. Over F_p every nonidentity element therefore has order p.

### Exact associators and commutators

Use the central additive convention

```math
(x*y)*z=x*(y*z)+(0,0,D(x,y,z)),\qquad
x*y=y*x+(0,0,C(x,y)).                            \tag{6}
```

With x=(a,u,s), y=(b,v,t), z=(c,w,r), direct expansion gives

```math
\begin{split}
D(x,y,z)&=aB(v,w)-bB(u,w)-2cB(u,v),\\
C(x,y)&=3(a+b)B(u,v).                            \tag{7}
\end{split}
```

Indeed, for a normalized central correction f the associator is
f(x,y)+f(x+y,z)-f(y,z)-f(x,y+z). For the general correction above this equals
alpha a B(v,w)+(alpha-beta)b B(u,w)-beta c B(u,v), which yields (7).
In particular,

```math
D(m,u,v)=B(u,v),\quad D(u,m,v)=-B(u,v),\quad
D(u,v,m)=-2B(u,v),\quad D(x,y,y)=-3bB(u,v).        \tag{8}
```

Thus L is associative exactly when B=0. The graph-dependent part itself produces
the nonassociativity. Nothing analogous to an independent octonion factor has
been attached.

### Precise Moufang specialization

The loop (1) is Moufang if and only if 3B(W,W)=0. For necessity, a Moufang loop is
right alternative, while (8), with b=1, forces 3B=0. Sufficiency can be proved
without invoking a converse characterization of Bol loops. Under 3B=0, (7) is
commutative and its associator becomes the alternating triadditive map

```math
T(x,y,z)=aB(v,w)-bB(u,w)+cB(u,v).                 \tag{9}
```

For such a central associator, rebracketing gives

```math
\begin{split}
(x*y)*(x*z)
 &=((x*y)*x)*z-T(x+y,x,z)\\
 &=((x*x)*y)*z-T(x+y,x,z)\\
 &=(x*x)*(y*z)+T(2x,y,z)-T(x+y,x,z)\\
 &=(x*x)*(y*z)+3T(x,y,z)\\
 &=(x*x)*(y*z).
\end{split}
```

Here quotient coordinates are used in T, all omitted terms are central, and
alternation gives T(x,y,x)=T(x,x,y)=0. Also
(x*x)*(y*z)=x*(x*(y*z)), again by alternation. Commutativity therefore yields
the precise Moufang identity

```math
(x*y)*(z*x)=x*((y*z)*x).                         \tag{10}
```

In particular K of characteristic three gives a commutative Moufang loop with
the simpler expression f((a,u),(b,v))=(a-b)B(u,v). If 3B is nonzero, the explicit
right-alternative defect in (8) proves that the left Bruck loop is not Moufang.

### Relation to Kepka's construction

On the additive group K direct-sum W direct-sum Z define a central ternary map

```math
S((a,u,s),(b,v,t),(c,w,r))=(0,0,bB(u,w)+cB(u,v)).
```

It is triadditive, symmetric in its last two arguments, and every nested S is
zero. Kepka's operation x+y+S(x,y,x+y) is exactly (1). This identifies the existing
construction being specialized; the direct proof above supplies the exact identity
and ring hypotheses needed here. The manuscript does not claim novelty for this
general operation or the characteristic-three trilinear CML method.

## A canonical construction from ordinary graphs

For a finite simple undirected graph Gamma=(V,E), let W=K^V with its standard
vertex vectors e_v. Define

```math
Z_\Gamma=\Lambda^2_K W/
 \langle e_i\wedge e_j:\ i\ne j,\ \{i,j\}\notin E\rangle,
\qquad B_\Gamma(u,v)=u\wedge v\pmod {\text{nonedges}}.             \tag{11}
```

The quotient is a free K-module of rank |E|. Writing its coordinates requires
choosing one orientation for each edge, but the module, quotient, and law do not.
Changing such an orientation changes the sign of that coordinate and gives the
specified coordinate isomorphism. There is no ordering-dependent directed graph
hidden in this definition.

Set L_K(Gamma)=K direct-sum W direct-sum Z_Gamma with law (1). For a graph
isomorphism phi, its permutation map on W induces Lambda^2 phi on the quotient
Z_Gamma. The map

```math
(a,u,s)\longmapsto(a,\phi u,(\Lambda^2\phi)s)       \tag{12}
```

preserves (1), because it preserves B_Gamma. These maps respect identity and
composition exactly, so this is a functor on the groupoid of finite simple graphs
and graph isomorphisms. It is also compatible with induced-subgraph embeddings,
as specified below. No functor on arbitrary graph homomorphisms is asserted:
a nonedge can be sent to an edge, in which case the defining quotient relation
in (11) would not be respected.

If K is finite of cardinality q and Gamma has n vertices and e edges, then

```math
|L_K(\Gamma)|=q^{n+e+1}.                         \tag{13}
```

There is one marker coordinate, n vertex coordinates, and e independent edge
coordinates, but no auxiliary graph vertices. Over Z[omega] the same loop is
infinite because the coefficient ring is infinite; the finite quotient versions
below retain the same formula.

An edge addition introduces one edge coordinate and its wedge coefficient in every
product. An edge deletion removes that correction coordinate. For an edge {i,j},
the associator D(m,e_i,e_j) is the nonzero edge generator e_i wedge e_j; for a
nonedge it is zero. Thus the graph actively determines the associators.

### Degenerate and disconnected cases

* For the edgeless n-vertex graph, Z_Gamma=0 and L_K(Gamma) is the additive group
  K^{n+1}. In particular the zero-vertex graph gives the additive group K.
* A single edge with no isolated vertices gives order q^4 and is nonassociative
  for every nonzero coefficient ring K. It is Moufang precisely when 3K=0.
* For the complete graph, Z_Gamma=Lambda^2 W and all distinct vertex pairs
  contribute. Its order is q^{1+n+n(n-1)/2}.
* Isolated vertices contribute direct additive factors K. If there are r isolated
  vertices, L_K(Gamma)=L_K(Gamma without those vertices) times K^r.
* For a disjoint union Gamma_1 disjoint-union Gamma_2, the exact relation is the
  fiber product of the two loops over their marker-coordinate maps to (K,+):
  both factors have the same marker a. A direct product would incorrectly count
  two independent marker coordinates.

All these statements follow directly from (11) and (1).

## Unmarked recovery over prime fields

Fix a prime p. In this section K=F_p and coefficients, coordinates, vertex basis,
edge basis, and marker are **not** retained as markings of the loop. The use of
a prime field matters: automorphisms of elementary abelian p-groups are F_p-linear.
No corresponding unmarked K-linearity assertion is made for an extension field
or an Eisenstein ring without a specified scalar action.

Write Z for the edge-coordinate subgroup. For a graph with an edge, (8) shows
that its associators generate exactly Z. It is therefore characteristic and
recoverable from the multiplication alone. The quotient U=L/Z is the additive
F_p-space F_p m direct-sum W, and (7) defines an intrinsic trilinear map
D:U^3 -> Z. In particular e=dim Z and n=dim U-1 are intrinsic.

The radical of B_Gamma is exactly the span R of the isolated vertices. To see
this, an element with nonzero coordinate at a nonisolated vertex i has nonzero
B-pairing with e_j for any neighbor j, as detected in the independent {i,j}
edge coordinate. Conversely an isolated coordinate never appears in (11).

### Characteristic different from three: an intrinsic marker hyperplane

Suppose p is not three and the graph has an edge. Define intrinsically

```math
Q=\{y\in U:D(x,y,y)=0\text{ for every }x\in U\}.
```

Equation (8) gives the exact set

```math
Q=W\ \cup\ (\mathbb F_p m\oplus R).              \tag{14}
```

The first subspace has dimension n and the second has dimension r+1. Since a
nonempty edge uses two nonisolated vertices, r+1<n. A vector subspace contained
in a union of two subspaces lies in one of them: otherwise vectors in the two
opposite set differences have a sum in neither. Hence W is the **unique
largest-dimensional linear subspace of Q**. This recovers W intrinsically,
even for stars, a single edge, or disconnected graphs.

Choose any t in U outside this recovered W. Then for v,w in W,

```math
D(t,v,w)=a B_\Gamma(v,w)\quad\text{for some }a\in\mathbb F_p^*.
                                                               \tag{15}
```

The alternating map B_Gamma is thus recovered up to invertible linear changes
in its domain and codomain; the unknown nonzero scalar a is absorbed in the
codomain. By [HQ20, Proposition 1.2], two graph exterior edge maps over any field
are equivalent under these changes if and only if their graphs are isomorphic.
Consequently, for any finite simple graphs Gamma and Delta,

```math
L_{\mathbb F_p}(\Gamma)\cong L_{\mathbb F_p}(\Delta)
\quad\Longleftrightarrow\quad \Gamma\cong\Delta,
\qquad p\ne3.                                    \tag{16}
```

The edgeless case causes no exception: it is characterized by associativity,
and its vertex count is log_p|L|-1. The forward implication of (16) includes
the explicit intrinsic extraction above and the external alternating-map
theorem; the backward implication is the functor (12).

For p=2 this is a Bruck loop of exponent two and is non-Moufang whenever the
graph has an edge. Sign orientation is unavailable in this field, but the
ordinary undirected construction (11) needs no sign-based orientation data.

### Characteristic three: recover a common exterior factor

When p=3, D=T in (9) is alternating. Regard the image of the dual associator map
as a subspace S of Lambda^3 U^*. In the construction's coordinates,

```math
S=\langle m^*\wedge e_i^*\wedge e_j^*: \{i,j\}\in E\rangle.
```

Both S and

```math
C=\{\ell\in U^*: \ell\wedge s=0\text{ for all }s\in S\}         \tag{17}
```

are intrinsic. For a nonzero decomposable three-form,
ell wedge (m^* wedge e_i^* wedge e_j^*)=0 holds exactly when ell lies in the
span of those three covectors; extend the three to a basis to check this.
It follows that

```math
C=\mathbb F_3m^*\ \oplus\
 \langle e_v^*:v\text{ belongs to every edge}\rangle.             \tag{18}
```

If no vertex belongs to every edge, C is the single line F_3 m^*, so its kernel
recovers W. Contraction with any transverse t recovers B as in (15), and the same
[HQ20] theorem recovers the graph. The exceptions are explicit and complete:

* If there is one edge, dim C=3. The graph is one edge and n-2 isolated vertices.
* If there are at least two edges and a vertex belongs to every edge, dim C=2.
  The graph is the star K_{1,e} and n-e-1 isolated vertices.
* If there are no edges the loop is the edgeless group already described.

The intrinsic n and e determine each exceptional graph. Thus (16) also holds
for p=3. This argument recovers an isomorphism class of graphs, not a canonical
vertex basis or a unique marker element. In the star cases even the marker
hyperplane is not recovered by (17), and none is claimed to be.

### Scope of the payoff and of the external theorem

The faithful unmarked correspondence is only the first consequence. For p not
three, the recovered W permits intrinsic statements about associative subloops
that cross its inverse image. The canonical payoff manuscript proves the exact
maximum order p^{e+1+alpha(Gamma)} and classifies all maximal such subloops by
dominating vertex supports and connected components, with an explicit counting
formula. These facts use the actual associator (7); they do not follow merely
from attaching a fixed nonassociative loop to a graph group.

The graph alternating map (11) is established literature. Its faithfulness is
not claimed as a new theorem here. Our proof identifies that map inside the
unmarked Bruck/Moufang loop and then applies the precise existing theorem.

## Why a scalar edge form loses the graph

For comparison, let Z=F_p and let B be an ordinary scalar alternating form on an
n-dimensional F_p-space. If B is nonzero, the center of (1) is

```math
Z(L)=\{(0,u,s):u\in\mathop{\mathrm{rad}}\nolimitsB,\ s\in\mathbb F_p\}.
                                                               \tag{19}
```

To prove this, an element of the left nucleus must have a=0 by varying v,w in
D(x,y,z), and then B(u,w)=0 by varying b,w. These conditions also imply membership
in the other nuclei and commutation with every element. Thus (19) follows.
The same argument applies to the edge-valued graph map, with s in Z_Gamma.

Alternating scalar forms are equivalent under a linear change of basis precisely
when they have equal rank. This elementary classification follows by splitting
off a hyperbolic pair whenever B is nonzero and iterating on its orthogonal
complement. The resulting change of basis extends to a loop isomorphism in (1).
Conversely, the loop order gives n, and (19) gives dim rad B and hence rank B.
Therefore these scalar loops classify exactly n and rank B, not general graphs.

For example, the scalar skew forms of a three-vertex directed path, a transitive
triangle, and a cyclic triangle with unit edges all have rank two over a field
of odd characteristic. Their unmarked scalar loops are isomorphic. Their marked
products and associators differ, as shown below. This is a precise loss-of-
information theorem for a natural first candidate and motivates the independent
edge coordinates in (11).

Independent edge coordinates do not magically retain colors: multiplying each
edge basis vector by its own nonzero field weight gives an equivalent B, hence
an isomorphic unmarked loop. Directed/color reconstruction below retains the
specified vertex, role, and coefficient markings.

## The alternating-associator integration obstruction

Let V and A be abelian groups and let f:V x V -> A be any normalized function.
Its central extension is a loop, but need not be Bol or Moufang. If its associator

```math
T(x,y,z)=f(x,y)+f(x+y,z)-f(y,z)-f(x,y+z)
```

is alternating, then necessarily 6T=0. Indeed, take the signed sum over all six
permutations of x,y,z. The terms f(x+y,z) cancel after swapping x,y; the terms
f(x,y+z) cancel after swapping y,z; and the remaining f(x,y) and -f(y,z) terms
cancel under cyclic permutation. The signed sum is zero. Alternation makes the
same signed sum equal to 6T(x,y,z).

Thus a prescribed nonzero alternating form T(m,e_i,e_j)=B(e_i,e_j) with values
in a torsion-free Z[omega]-module cannot be realized by such a central extension.
If 6 is a unit on A the same conclusion holds. This obstruction is about this
specific central-extension target; it is not a nonexistence theorem for arbitrary
Moufang loops over those rings, or for noncentral graph-derived constructions.

The repair in (1) is substantive: it gives up alternation outside 3-torsion and
retains a directly proved Bruck identity and graph-sensitive nonassociativity.
In characteristic three the target alternating suspension is realized by (9).
The characteristic-two code-loop route is another repair and has different square
and commutator compatibilities; see the companion cubic manuscript.

## Directed and colored inputs

### Skew encoding, color separation, and opposing arrows

For an oriented graph (at most one arrow on each unordered vertex pair), choose a
color set C contained in the nonzero elements of K with C intersection (-C) empty.
An arrow i -> j of color c defines B(e_i,e_j)=c and B(e_j,e_i)=-c. Missing edges
give zero. With the vertex basis, the coefficient ring, and its coordinate fixed,
one recovers the arrow and its color uniquely: each nonzero value lies in exactly
one of C and -C. If both c and -c are allowed as unrelated colors, reversing an
edge and changing its color produces the same tensor, so that stronger assertion
would be false.

Antisymmetrizing a general directed adjacency matrix is not faithful. In particular
two opposing arrows of the same color can cancel to zero and become indistinguishable
from an absent edge. A canonical repair uses two vertex roles. Let

```math
W=K^{V,\mathrm{out}}\oplus K^{V,\mathrm{in}},\qquad
B((x,y),(x',y'))=
 \sum_{i,j}c_{ij}(x_i y'_j-x'_i y_j),             \tag{20}
```

where c_ij is zero exactly when arrow i -> j is absent and otherwise its color.
Then B(e_i^out,e_j^in)=c_ij and B(e_j^out,e_i^in)=c_ji occupy separate entries.
No opposing arrows cancel. The law (1) is again a Bruck law. The out/in partition,
the pairing of its two copies of each vertex, the vertex basis, the marker, and
the coefficient coordinate are part of this **marked** construction.

For finite K of size q, the scalar-center doubled construction has order q^{2n+2}.
Replacing the scalar center by independent arrow coordinates is possible, but
unmarked edge rescalings still erase nonzero unit color values. No unmarked
directed-colored recovery theorem is inferred from the ordinary-graph theorem.

In characteristic two a nonzero color cannot be separated from its negative.
Formula (20) repairs orientation using the out/in roles, not a nonexistent sign.
It retains both directions and all distinct nonzero coefficient colors with the
specified marking. Conjugation can distinguish some colors in F_4, but does not
repair every fixed color and is not a replacement for the role data.

### Three canonical treatments of undirected inputs

1. Formula (11) is orientation-independent and has the strongest unmarked theorem.
2. One may replace each undirected edge by its two arrows and use (20). The two
   roles remain marked. Its scalar alternating matrix is the block matrix
   [[0,A],[-A^T,0]] for the ordinary adjacency matrix A, so over a field its rank
   is twice rank(A). Scalar-loop classification then explains its information loss.
3. Choosing an arbitrary ordering of vertices and putting positive scalar colors
   above the diagonal does not define an unmarked graph functor in general.
   Different orientations can change the skew rank. Such an output must retain
   the ordering/orientation, or use edge coordinates as in (11), where coordinate
   sign changes give an explicit isomorphism.

For an explicit failure of the third treatment, use the cycle with edges
12,23,34,14 over a field of odd characteristic. Orient from earlier to later in
the order 1<3<2<4. Its skew coefficients satisfy B_12=B_34=B_14=1 and B_23=-1,
so the Pfaffian B_12 B_34+B_14 B_23 is zero and the rank is two. The order
1<2<3<4 instead makes all four coefficients positive, so the Pfaffian is two
and the rank is four. The scalar loops therefore differ by (19), although
the underlying undirected graph is unchanged. An arbitrary vertex order cannot
be silently discarded.

## Eisenstein arithmetic and exact finite versions

Let R=Z[omega], omega^2+omega+1=0. Every element has a unique expression a+b omega
with integers a,b. Its conjugate and norm are

```math
\overline{a+b\omega}=(a-b)-b\omega,\qquad
N(a+b\omega)=a^2-ab+b^2.                          \tag{21}
```

The units are 1,-1,omega,-omega,omega^2,-omega^2. One elementary proof is to solve
N(a+b omega)=1 using (2a-b)^2+3b^2=4. Negation swaps each unit with its negative;
conjugation fixes 1 and -1, swaps omega with omega^2, and swaps -omega with
-omega^2. These actions are different. Conjugation has a fixed real subring and
does not distinguish direction for every coefficient.

For sign reversal the three-color set {1,omega,omega^2} is disjoint from its
negative over R. It encodes three colors and two directions without ambiguity.
For conjugation reversal a color set must instead be disjoint from its conjugate;
it cannot contain a conjugation-fixed coefficient such as 1. For example
{omega,-omega} and its conjugate are disjoint over R, giving two such colors.
Multiplication by omega is an order-three color rotation, not an involutive edge
reversal. The maps c -> u conjugate(c) for a unit u are involutions because
u conjugate(u)=1; pure multiplication c -> u c is an involution only for u=1 or -1.

The Bruck construction requires an alternating bilinear B. Replacing the equation
B(e_j,e_i)=-B(e_i,e_j) by conjugation or by negative conjugation does not in general
satisfy that requirement. Conjugate edge-reversal conventions should be stored in
the directed coefficient matrix and then passed through (20), or encoded using
the underlying additive module with a separately proved alternating map. No
Moufang or Bol identity is inferred directly from a Hermitian-looking matrix.

For clarity, the ring assertions used below can be checked directly from
R=Z[t]/(t^2+t+1), the norm, and reduction of this polynomial. Write lambda=1-omega.
Then lambda^2=-3 omega, so (lambda)^2=(3). The following are ring statements,
not assumptions that every quotient is a field.

| Quotient | Size and characteristic | Field/zero-divisor facts | Color and conjugation facts |
| --- | --- | --- | --- |
| R/(2) | 4; characteristic 2 | F_4, since t^2+t+1 is irreducible over F_2 | 1,omega,omega^2 remain distinct; signs collapse; conjugation is x -> x^2 |
| R/(2^k), k>1 | 2^{2k}; characteristic 2^k | local, maximal ideal (2); zero divisors are exactly its nonzero multiples of 2 | all six units are distinct; conjugation descends |
| R/(lambda) | 3; characteristic 3 | F_3; omega=1 | three positive unit colors collapse to one, negative ones to the other; conjugation is trivial |
| R/(lambda^2)=R/(3) | 9; characteristic 3 | F_3[epsilon]/(epsilon^2), with epsilon=lambda; not a field | all six units are distinct; conjugation sends epsilon to -epsilon |
| R/(lambda^k), k>=1 | 3^k; characteristic 3^{ceil(k/2)} | local; for k>1, nonzero multiples of lambda are zero divisors; units are the other 2*3^{k-1} elements | six units are distinct exactly when k>=2; conjugation descends |
| R/(p^k), p prime and p=2 mod 3 | p^{2k}; characteristic p^k | unramified quadratic local ring; field for k=1, nonzero multiples of p are zero divisors for k>1 | conjugation descends; for p>2 all six unit colors survive |
| R/(pi^k), N(pi)=p and p=1 mod 3 | p^k; characteristic p^k | isomorphic to Z/p^k; field only for k=1 | all six units survive; conjugation maps this quotient to R/(conjugate(pi)^k), not generally to itself |
| R/(p^k), p=1 mod 3 | p^{2k}; characteristic p^k | product of two copies of Z/p^k; has zero divisors even at k=1 | conjugation exchanges the two factors; all six units survive |

Here the split/inert classification follows because a root of t^2+t+1 over F_p,
p not three, is exactly a nontrivial cube root of unity, which exists precisely
when p=1 modulo three. In the split case the roots are distinct and lift uniquely
modulo p^k, giving the stated factors by the Chinese remainder theorem. In the
inert case reduction gives F_{p^2}; an element is a unit precisely when its reduction
is nonzero, using a finite geometric-series inverse for elements congruent to one
modulo p. The ramified claims follow from lambda^2=-3 omega and valuation: 3^j
first vanishes modulo lambda^k when 2j>=k. The residue field is F_3, and the
successive lambda-adic quotients have size three. The unit-separation claims follow
by inspecting pairwise differences of the six units; the only relevant primes
are 2 and lambda, and lambda divides a difference of distinct positive units to
exactly the first power.

Every row gives a finite version of (1), with no need to invert a nonunit. For
ordinary graphs with independent edge coordinates and a nonempty edge, the loop
is Moufang exactly when 3=0 in the coefficient ring. Thus R/(3) supplies a
commutative Moufang realization with all six sign/color values preserved, despite
its zero divisors. R/(lambda^k) for k>=3 gives a proper Bruck loop with unit edges;
it is not silently treated as a characteristic-three field.

For the original alternating-associator target, 6T=0 limits the coefficient
module. In R/(lambda^k), the elements annihilated by 3 form the ideal
lambda^{max(k-2,0)}R/(lambda^k), of size 3^{min(k,2)}. One can place B in that ideal
and use the Moufang specialization, but then colors are visible only through
their reductions modulo lambda^{min(k,2)} after that scaling. In R/(2^k),
the elements annihilated by 6 are exactly those annihilated by 2, namely
2^{k-1}R/(2^k); their signs coincide. If p>3 then 6 is invertible on a p-primary
quotient, so a nonzero alternating central T is impossible, while (1) still gives
a proper Bruck realization with its nonalternating associator (7).

A concrete small field with three signed Eisenstein colors is R/(3+omega)=F_7,
where omega maps to 4 and omega^2 maps to 2. The six unit values are precisely
the six nonzero field elements. Conjugation does not descend to this chosen
factor: it would send 4 to 2, whereas F_7 has no such field automorphism.
Using R/(7)=F_7 times F_7 instead retains conjugation as factor exchange.

## Actual products and directed examples

For the scalar marked version let c_ij=B(e_i,e_j), and put u_i=(0,e_i,0) and
m=(1,0,0). Then

```math
\begin{array}{ll}
(m*u_i)*u_j=(1,e_i+e_j,c_{ij}),
 &m*(u_i*u_j)=(1,e_i+e_j,0),\\
(m+u_i)*u_j=(1,e_i+e_j,c_{ij}),
 &u_j*(m+u_i)=(1,e_i+e_j,-2c_{ij}),\\
D(m,u_i,u_j)=c_{ij},
 &D(u_i,u_j,m)=-2c_{ij}.
\end{array}                                                    \tag{22}
```

Here m+u_i denotes the element with coordinate (1,e_i,0), which also equals
m*u_i. These are actual products, not only tensor labels. For ordinary graphs,
c_ij is replaced by its independent edge vector.

| Input on indicated vertices | Nonzero skew coefficients | D(m,u_1,u_3) | Effect |
| --- | --- | --- | --- |
| Empty graph | none | 0 | every correction and associator is zero |
| One arrow 1 -> 2 of color c | c_12=c | not applicable | the two bracketings in (22) differ by c |
| Path 1 -> 2 -> 3 | c_12=c_23=1 | 0 | missing pair 13 has zero associator |
| Transitive triangle 1 -> 2, 2 -> 3, 1 -> 3 | c_12=c_23=c_13=1 | 1 | adding the long edge changes the associator from zero to one |
| Directed triangle 1 -> 2 -> 3 -> 1 | c_12=c_23=1, c_13=-1 | -1 | reversing the long edge changes its signed associator |
| Same long edge recolored omega | c_13=omega | omega | distinct over R/(3), F_4, and F_7 as described above |
| Bidirected pair in (20) | B(e_1^out,e_2^in)=c, B(e_2^out,e_1^in)=d | use the two role-specific pairs | neither coefficient is canceled |

The cyclic triangle is also the smallest directed cycle supported by the skew
oriented scheme; longer directed cycles use the same edge-by-edge formula.
In characteristic two the transitive/cyclic sign table is not an orientation
encoding. Use (20) there: the long arrow is present in one out/in entry or the
other, so reversal changes its location even though -1=1. Colors 1 and omega
remain distinct in F_4. In R/(3), both signs and the three positive colors are
distinct, and (22) is genuinely nonassociative and Moufang whenever c is nonzero.

## Graph operations, quotients, and the deck limitation

For S contained in V, extension by zero embeds W_S and its edge module into
W and Z_Gamma. Coordinate restriction back to S is a left inverse on both
modules. Both maps preserve B, so they induce an embedding and a retraction

```math
L_K(\Gamma[S])\ \longrightarrow L_K(\Gamma)
 \ \longrightarrow L_K(\Gamma[S]).               \tag{23}
```

The retraction kernel consists of elements with marker zero, vertex coordinates
supported outside S, and edge coordinates zero on edges contained in S. It is
a normal additive subgroup: inside the kernel both marker factors vanish, so
the multiplication correction is zero. It need not be central. Thus an induced
vertex deletion is a split normal quotient and a specified subloop, not deletion
of one element of the loop.

If F is a collection of edges, let Z_F be its coordinate span in Z_Gamma. It is
central, and the quotient has the exact graph interpretation

```math
L_K(\Gamma)/Z_F\cong L_K(\Gamma\setminus F).       \tag{24}
```

The edge coordinates in (24) are part of the graph-derived presentation; the
unmarked theorem recovers the graph isomorphism class, but does not assert that
each particular edge coordinate line is characteristic.

For prime p, the multiset of the loop isomorphism types L_p(Gamma-v), v in V,
contains exactly the graph-deck isomorphism information, by (16) applied card by
card. This is a rigorous dictionary for a **specified family of retractions**.
It is not the ordinary element-deletion deck of a loop, nor the multiset of all
index-p subloops or all quotients. Consequently this observation does not solve
graph reconstruction or justify importing a loop reconstruction theorem without
first proving that its partial-data model agrees with (23).

## Controls and remaining scope

A graph group or a bilinear central extension gives an associative control.
Taking its product with a fixed nonassociative Moufang loop gives a second
control whose associator behavior includes an independent fixed factor. In
contrast, (1) is associative on every edgeless input, adding a nonzero graph edge
creates the nonzero associator in (22), and the full graph exterior map is
recoverable from the multiplication in the stated prime-field cases.

This does not settle the parent finite-simple-Bol classification problem. These
loops have a central edge subgroup and are deliberately class-two constructions.
It also does not classify directed colored graphs from unmarked loops, prove
graph reconstruction, or claim a new general construction in place of Kepka's.
The meaningful endpoint here is an explicit graph-native law, a complete
unmarked recovery theorem with a stated literature dependency, and the separate
domination/associative-subloop payoff.

## References and verified scope

* **[Kep84]** Tomas Kepka, *A construction of Bruck loops*, Commentationes
  Mathematicae Universitatis Carolinae **25** (1984), no. 4, 591--595.
  [Stable record](https://dml.cz/handle/10338.dmlcz/106327),
  [full text](https://dml.cz/bitstream/handle/10338.dmlcz/106327/CommentatMathUnivCarol_025-1984-4_2.pdf).
  Section 2 defines x*y=x+y+S(x,y,x+y) for a central ternary map symmetric in
  its last two arguments. Proposition 2.4 establishes Bruck; Proposition 2.6
  gives class-two, Moufang, and group criteria. Full text checked; our map S and
  direct proof are given above.
* **[HQ20]** Xiaoyu He and Youming Qiao, *On the Baer--Lovasz--Tutte construction
  of groups from graphs: isomorphism types and homomorphism notions*,
  [arXiv:2003.07200v2](https://arxiv.org/abs/2003.07200v2), 4 May 2020,
  [PDF](https://arxiv.org/pdf/2003.07200v2). Proposition 1.2, page 2, with proof
  in Section 2, pages 5--8: over any field, the graph alternating maps are
  equivalent under invertible domain/codomain maps exactly for isomorphic
  graphs. This is the external dependency in (16).
* **[Hsu00]** Tim Hsu, *Moufang loops of class 2 and cubic forms*, Mathematical
  Proceedings of the Cambridge Philosophical Society **128** (2000), 197--222,
  [doi:10.1017/S0305004199003977](https://doi.org/10.1017/S0305004199003977).
  The publisher's abstract states the exponent-dividing-six theorem for the
  associator subloop of class-two Moufang loops and the symplectic cubic-space
  classification. It is background only here; the narrower central-coboundary
  obstruction is proved directly and is not cited as a newly discovered Hsu result.

The broad literature on trilinear loop constructions and graph alternating maps
precludes any novelty claim based solely on the notation or formula (1). An
exhaustive novelty determination for the intrinsic graph-loop recovery and the
domination-counting consequence is not asserted by this source comparison.
