# Defect graphs, associative quotients, and decomposition of Bruck extensions

*Mira Cult*

A graph built from a loop's associativity defects detects an actual extension
of that loop. Its connected components are exactly the cosets of the normal
associator subloop, and the component set carries the universal associative
quotient. For finite left Bol loops the graph has symmetric, canonically
defined weights. Combining it with the local defect graph recovers the exact
elementary abelian direct-factor rank of the central Bruck extensions studied
here.

The information retained has a sharp limit. The graph loops obtained from
the star on four vertices and from a triangle with an isolated vertex have
identical translated defect graphs, including every weight. One original loop
is directly indecomposable; the other has a nontrivial direct factor. The local
defect graph repairs this particular loss, but a separate pair of order-16
Moufang loops shows that even both full defect matrices do not recover arbitrary
central-extension data.

The operators themselves occur in the existing
[intrinsic Bol analysis](../../analytic-2026-11-16/manuscripts/bol-associator-quantization.md).
The additional results here are their general component interpretation, the
central-family spectral calculation, the explicit collisions, and the
decomposition invariant obtained from the two graphs. The normal associator
subloop and central-extension framework are established loop theory [SV-COM,
SV-EXT]. No general reconstruction of loops from their defect graphs is asserted.

## 1. Local and translated defect graphs

Let L be a finite loop with identity 1 and multiplication written by
juxtaposition. Its left translations are the permutations L_x(a)=xa. Define

```math
 \ell_{x,y}=L_{xy}^{-1}L_xL_y,
 \qquad g_{x,y,z}=L_z^{-1}\ell_{x,y}L_z.                    \tag{1}
```

Both expressions use only multiplication and the unique divisions of the loop.
On the vertex set L, define row-stochastic matrices

```math
 \begin{split}
 A_L(a,b)&=\frac{\#\{(x,y):\ell_{x,y}(a)=b\}}{|L|^2},\\
 P_L(a,b)&=\frac{\#\{(x,y,z):g_{x,y,z}(a)=b\}}{|L|^3}.
 \end{split}                                             \tag{2}
```

Each is an average of permutation matrices, hence also column-stochastic.
Loops and weights are retained in these matrices. Their **local support graph**
and **translated support graph** are ordinary simple graphs: distinct vertices
a,b are adjacent when the corresponding matrix has a positive entry in either
direction. Write these graphs as Gamma_loc(L) and Gamma_tr(L).

No generating set, vertex basis, or ordering is selected. The vertex 1 can be
marked when identifying a particular embedded subloop, but the graph
invariants below do not depend on a choice of names for the elements.

### Bol reversibility and right-nucleus detection

For a left Bol loop we use exactly

```math
 x\bigl(y(xz)\bigr)=\bigl(x(yx)\bigr)z.
```

Its translation form gives

```math
 L_yL_xL_y=L_{y(xy)},
 \qquad \ell_{x,y}^{-1}=\ell_{y,xy}.                      \tag{3}
```

The map (x,y) to (y,xy) is a bijection, by right division. Thus the multiset
of local defects is closed under inversion, with multiplicities. The same
holds after every conjugation by L_z. Consequently **A_L and P_L are symmetric
for every finite left Bol loop**. This is the general inverse-defect identity
already proved in [AQ, Section 4.2, (AQ.25)]; the calculation above supplies
the precise convention used here. Positivity of their eigenvalues is not
claimed in general. The lazy matrices (I+A_L)/2 and (I+P_L)/2 are positive
semidefinite.

For any loop, a vertex a is isolated in Gamma_loc(L) exactly when every
ell_(x,y) fixes it. The defining equation then gives

```math
 (xy)a=x(ya)\quad\hbox{for all }x,y.
```

Thus the local graph's isolated vertices are exactly the **right nucleus**
N_r(L). This is not the assertion that they form the full nucleus or center.
The distinction matters in characteristic two below.

The normalized trace of either matrix is the associative-triple probability:

```math
 \frac{\mathop{\mathrm{Tr}}\nolimitsP_L}{|L|}
 =\frac{\mathop{\mathrm{Tr}}\nolimitsA_L}{|L|}
 =\Pr_{x,y,a}\bigl[(xy)a=x(ya)\bigr].                     \tag{4}
```

Indeed conjugation preserves the number of fixed points. This interpretation
is also part of the existing intrinsic operator framework [AQ, SS].

### Naturality

A loop isomorphism f satisfies f L_x f^(-1)=L_(f(x)). It consequently transports
both matrices and both support graphs by the same permutation. Identity maps
and compositions are respected, so these constructions are functors on the
groupoid of finite loops and isomorphisms.

For any loop homomorphism f, preservation of the unique divisions gives

```math
 f\,g_{x,y,z}=g_{f(x),f(y),f(z)}\,f,
 \qquad f\,\ell_{x,y}=\ell_{f(x),f(y)}\,f.                \tag{5}
```

Support edges therefore map to support edges or collapse to a vertex. With
loops at every graph vertex this gives a graph-homomorphism functor. It does
not give a functor into ordinary simple graphs with noncollapsing morphisms.

If f:L to K is surjective, its fibers have equal cardinality. Uniform
independent x,y,z therefore map to uniform independent elements of K, and

```math
 \sum_{b:f(b)=v}P_L(a,b)=P_K(f(a),v).                      \tag{6}
```

The same formula holds for A_L. This is an exact Markov lumping. It is stronger
than adjacency preservation, but it requires surjectivity. The graph-to-loop
composites considered below are asserted functorial on isomorphisms; the
graph-loop construction does not automatically extend (6) to loop homomorphisms.

## 2. Connected components are the canonical group quotient

Let A(L) denote the smallest normal subloop for which L/A(L) is a group. This
standard normal associator subloop is the normal closure of the associator
values; normal closure cannot be omitted for arbitrary loops [SV-COM, Section 8].

**Theorem 1 (component theorem).** For every finite loop L:

1. The connected components of Gamma_tr(L) are exactly the fibers of
   L to L/A(L). The component of 1 is the actual normal subloop A(L).
2. Every component has cardinality |A(L)|, and their number is |L/A(L)|.
3. Multiplication of components is well defined and gives the universal group
   image of L: every loop homomorphism from L to an associative group factors
   uniquely through this quotient.
4. The eigenvalue-one space of P_L consists exactly of functions constant on
   these components. Its dimension is |L/A(L)|.

In particular, Gamma_tr(L) is connected exactly when every group image of L is
trivial. It is edgeless exactly when L is associative.

**Proof.** Put G=LMlt(L) and H=G_1. The Schreier generators for the transversal
{L_x:x in L} show that

```math
 H=\langle\ell_{x,y}:x,y\in L\rangle.                    \tag{7}
```

For completeness, a generator L_x taking the representative L_y to the coset
represented by L_(xy) gives precisely L_(xy)^(-1)L_xL_y; inverse generators
give inverses of the same Schreier generators. This is the standard left
inner-group generation fact [LOOPS, Section 6.5].

Let N be the subgroup generated by all g_(x,y,z). It is generated by the
subgroups L_z^(-1) H L_z. The point L_z^(-1)(1)=z\1 ranges over all of L:
the equations za=1 have unique solutions in both variables. These conjugates
are therefore precisely all point stabilizers G_a. Hence

```math
 N=\langle G_a:a\in L\rangle\trianglelefteq G,
 \qquad H\leq N.                                        \tag{8}
```

Define q(x)=L_x N in G/N. Since ell_(x,y) lies in H, q(xy)=q(x)q(y). Every
g in G is L_x h for x=g(1) and h in H; thus q is surjective.

Its fibers are the N-orbits. If q(x)=q(y), then L_x L_y^(-1) belongs to N and
sends y to x. Conversely, if x=n(y) for n in N, then L_x^(-1)nL_y fixes 1
and lies in H, so q(x)=q(y). The support graph's components are exactly the
orbits of its generating permutations g_(x,y,z). This proves that components
are the fibers of a loop homomorphism onto the group G/N.

Now let f:L to K be a homomorphism to a group. From
(xy)ell_(x,y)(a)=x(ya), associativity and cancellation in K imply
f(ell_(x,y)(a))=f(a). Therefore

```math
 f\bigl(L_z^{-1}\ell_{x,y}L_z(a)\bigr)
 =f(z)^{-1}f\bigl(\ell_{x,y}(za)\bigr)=f(a).
```

It follows that f is constant on every N-orbit and factors uniquely through q.
Thus ker(q)=A(L), and items 1 and 3 follow. Left translations map one fiber
bijectively onto another fiber, proving item 2.

Finally, if P_L F=F, the identity

```math
 \mathbb E_{x,y,z}\|F-F\circ g_{x,y,z}\|_2^2
 =2\|F\|_2^2-2\mathop{\mathrm{Re}}\nolimits\langle F,P_LF\rangle=0
```

shows that every generating permutation fixes F. Hence fixed functions are
exactly N-orbit-constant functions. This proves item 4. The final assertions
follow from the universal property. ∎

The containment H≤N in (8) is essential. An arbitrary normal subgroup of
LMlt(L) does not automatically yield a quotient loop from its orbits. The
counterexample and exact projected-section condition in [FOLDER, C0001(3)]
express this obstruction. Here the quotient map is proved multiplicative
directly, and the projected section is all of the regular group G/N.

The theorem supplies an actual extension of the original loop,

```math
 1\longrightarrow A(L)\longrightarrow L
   \longrightarrow L/A(L)\longrightarrow1.               \tag{9}
```

The extension data remain necessary: A(L) and L/A(L) do not by themselves
determine L. No splitting of (9) is asserted.

## 3. What the graph-to-loop composite retains

Let F_p(Gamma) denote the graph Bruck construction in
[graph-eisenstein-loops.md](../../graph-loops/manuscripts/graph-eisenstein-loops.md), for a prime p≠3. Put
Gamma=Gamma_tr(L), let N=|L|, and let e be its number of edges. Then

```math
 |F_p(\Gamma)|=p^{N+e+1}.                                \tag{10}
```

This size may be large; it is not a claim that expanding the loop table is
efficient. Graph isomorphisms give the specified loop isomorphisms.

If Gamma_1,...,Gamma_c are its connected components, the graph multiplication
gives a fiber product over the shared marker coordinate:

```math
 F_p(\Gamma)\cong
 F_p(\Gamma_1)\mathbin{\times_{\mathbf F_p}}\cdots
 \mathbin{\times_{\mathbf F_p}}F_p(\Gamma_c).             \tag{11}
```

Here c=|L/A(L)| and every Gamma_i has |A(L)| vertices. Equation (11) is a
decomposition of the constructed loop, while (9) is an extension of the
original loop. They must not be identified as a factorization of L by the
new graph loops.

There is a useful intrinsic numerical formula. From F_p(Gamma), recover its
vertex hyperplane W and edge map beta as in the unmarked recovery theorem.
Set

```math
 r_{\max}=\max_{x\in W}\mathop{\mathrm{rank}}\nolimits\bigl(y\mapsto\beta(x,y)\bigr).
```

**Proposition 2.** If Gamma has N vertices and c connected components, then
r_max=N−c. Consequently the composite determines

```math
 |L/A(L)|=N-r_{\max},\qquad
 |A(L)|=\frac{N}{N-r_{\max}}.                            \tag{12}
```

**Proof.** For each component, if x has nonzero restriction there, that
restriction is a nonzero vector in the kernel of beta(x,−); if it vanishes
there, the whole component space is in the kernel. These give c independent
kernel directions. Thus rank is at most N−c. Taking every vertex coordinate
of x to be one makes the kernel exactly the vectors constant on each
component, giving equality. ∎

N itself is intrinsic from the constructed loop's order and associator
subloop order: N=log_p|F_p(Gamma)|−log_p|A(F_p(Gamma))|−1. The edgeless case is
included and has r_max=0. The contraction recovering beta is determined only
up to a nonzero scalar and change of bases, which leave r_max unchanged.

This calculation does not recover the quotient group's multiplication from
the graph. In fact all associative groups of order N give the same edgeless
translated graph, regardless of their group structure.

## 4. Exact translated spectra and a collision inside the graph family

### Central trilinear extensions

Let a loop have underlying set U⊕Z for finite prime-field vector spaces, with
normalized central factor set f and trilinear defect

```math
 D(x,y,u)=f(x,y)+f(x+y,u)-f(y,u)-f(x,y+u).
```

Then direct multiplication and division give

```math
 \ell_{x,y}(u,z)=(u,z-D(x,y,u)).                          \tag{13}
```

Conjugation by a left translation with quotient coordinate w replaces u in
the defect by u+w. For fixed x,y, averaging w therefore averages uniformly
over the subspace im D(x,y,−) of Z. Hence P_L is the identity on U tensored
with a convolution operator on Z. At a character lambda in Z*, its eigenvalue
is

```math
 \mu(\lambda)
 =\Pr_{x,y}\bigl[\lambda D(x,y,u)=0\text{ for every }u\in U\bigr].
                                                               \tag{14}
```

In particular these eigenvalues are nonnegative. If the values of D span Z,
the support consists of |U| isomorphic connected components of size |Z|.

For the Bruck law

```math
 (a,u,s)*(b,v,t)=(a+b,u+v,s+t+(a+2b)B(u,v)),               \tag{15}
```

the defect is aB(v,w)−bB(u,w)−2cB(u,v). At an odd prime p, let
phi=lambda B have rank r and radical R. The condition in (14) is

```math
 av-bu\in R,\qquad \phi(u,v)=0.                         \tag{16}
```

If (a,b)≠(0,0), the first condition has probability p^(−r) and forces the
second: modulo R, u and v are proportional. If (a,b)=(0,0), the second has
probability p^(−1)+(1−p^(−1))p^(−r). Therefore

```math
 \boxed{\mu_p(r)=p^{-3}+(1-p^{-3})p^{-r}}.                \tag{17}
```

The binary cubic Moufang construction has the alternating defect
aB(v,w)+bB(u,w)+cB(u,v), so the same calculation gives (17) with p=2.
For the characteristic-two Bruck law (15), the c-term disappears and the
second condition in (16) is absent. Its eigenvalue is instead

```math
 \boxed{\mu_2^{\mathrm{Bruck}}(r)=\frac14+\frac34\,2^{-r}}.\tag{18}
```

The full translated spectrum of these central families retains the scalar
rank distribution, with multiplicity |U| for every central character. It
need not retain the relations between different scalar forms.

### Star versus triangle with an isolated vertex

**Theorem 3 (weighted collision).** For every prime p, the Bruck loops (15)
associated with K_(1,3) and K_3 disjoint-union K_1 are nonisomorphic but have
isomorphic translated weighted graphs. The same collision occurs for the
binary cubic Moufang family.

**Proof.** Both graphs have n=4 and e=3. They are nonisomorphic, so the
unmarked graph recovery theorems distinguish their loops. Every nonzero
scalar specialization of either graph edge map has rank two. For the star
it is a nonzero decomposable form

```math
 e_0^*\wedge(ae_1^*+be_2^*+ce_3^*).
```

For the triangle it is a nonzero alternating form on a three-dimensional
space, again of rank two. Thus every nontrivial central character has the
same eigenvalue mu, given by (17) or (18). Fourier inversion makes the
convolution matrix exactly

```math
 \mu I_{p^3}+(1-\mu)\Pi_{p^3},                          \tag{19}
```

where Pi is uniform averaging. Each whole matrix P_L has p^5 identical
blocks (19), proving the weighted isomorphism. The ordinary support graph
is p^5 disjoint copies of K_(p^3). ∎

At p=2 for the Bruck family, mu=7/16. Each block has diagonal entry 65/128
and off-diagonal entry 9/128. The supplied checker calculates the actual
256-by-256 matrices from translation permutations and verifies their equality.

The [direct-core theorem](bruck-extension-decomposition.md#one-marker-loops-have-one-nonassociative-direct-core)
strengthens this collision: the star loop is directly indecomposable, whereas
the triangle-with-isolate loop has a C_p direct factor. Consequently the
translated graph alone does not even determine direct decomposability within
this graph-native Bruck family. Applying any fixed graph-to-loop construction
to the two translated support graphs gives isomorphic outputs and cannot
repair that loss.

## 5. Two defect graphs recover the elementary abelian direct-factor rank

Retain Gamma_loc(L) and Gamma_tr(L) on the same unmarked vertex set. Equivalently,
label each adjacent pair by the nonempty subset of {local,translated}
specifying in which graphs it appears. This is a simple edge-colored graph;
an edge present in both relations retains both labels. No coordinate basis
or identity marker is needed to count local isolated vertices or translated
components.

**Theorem 4 (decomposition invariant).** Suppose L is the Bruck loop (15) for
a nonzero alternating map B:W times W to Z over F_p. No surjectivity of B is
assumed. Let i be the number of isolated vertices of Gamma_loc(L), and let a
be the common component size of Gamma_tr(L). Put

```math
 d=\begin{cases}
   \log_p(i/a),&p\text{ odd},\\
   \log_2(i/a)-1,&p=2.
 \end{cases}                                             \tag{20}
```

Then d is a nonnegative integer and L has an elementary abelian direct factor
C_p^d with a nonassociative directly indecomposable complementary core. In
particular, these two graphs determine whether L is directly indecomposable.

**Proof.** Write r=dim rad B, z=dim Z, and b=dim span im B. The associator
values generate exactly the central subspace span im B, so a=p^b by Theorem 1.
For a right-nuclear element (c,w,s), the defect formula forces w in rad B.
It then reduces to −2cB(u,v). Thus

```math
 N_r(L)=\begin{cases}
    0\oplus\mathop{\mathrm{rad}}\nolimitsB\oplus Z,&p\text{ odd},\\
    \mathbf F_2\oplus\mathop{\mathrm{rad}}\nolimitsB\oplus Z,&p=2.
 \end{cases}                                             \tag{21}
```

Since B is nonzero, its full nucleus and center are both
0 direct-sum rad B direct-sum Z at every prime. The extra marker direction
in the second line of (21) is right nuclear only. Section 1 gives
i=p^(r+z) for odd p and i=2^(1+r+z) for p=2. Therefore (20) is exactly
d=r+z−b.

Splitting off rad B and a complement to span im B gives the C_p^d factor.
Direct indecomposability of the remaining full, nondegenerate core is the
[one-marker direct-core theorem](bruck-extension-decomposition.md#one-marker-loops-have-one-nonassociative-direct-core).
This proves the stated decomposition conclusion. ∎

This theorem is a statement about the original loop L, not solely an invariant
of a newly encoded object. Its hypothesis is membership in family (15); it is
not a recognition theorem for arbitrary Bol loops. When B=0 the family is
elementary abelian, both graphs are edgeless, and its rank is log_p|L|.

For the star/triangle collision at p=2, both translated graphs have components
of size 8. The local graphs have respectively 16 and 32 isolated vertices.
Formula (20) gives d=0 and d=1, repairing the translated graph's failure.

### An ordinary-graph version without the multiplication table

The two-relation graph admits an explicit, functorial conversion to an
ordinary simple graph. First build a vertex-colored incidence core. Give the
original vertices type 1. Subdivide each pair carrying a nonempty relation
label by one edge-node of type 3,4,5 according as the label is local only,
translated only, or both. At each original vertex attach a private triangle;
its two additional vertices have type 2. The entire core has minimum degree
two, including when an original vertex is isolated in both relations.

At **every** core vertex attach one pendant path whose length is its type.
Now forget all colors. The ordinary graph's two-core recovers the incidence
core: the pendant paths are removed by repeatedly deleting vertices of degree
less than two, while every core vertex survives. Each surviving vertex has a
unique attached path, whose length recovers its type. Edge-nodes of types
3,4,5 then recover the original two relations. Hence ordinary graph
isomorphism is equivalent to isomorphism of the two-relation graph.

If the original loop has N elements and m unordered pairs carrying at least
one relation, the ordinary graph has at most 8N+6m vertices and 8N+7m edges.
This records only the two defect relations and is not a multiplication-table
encoding. The fixed auxiliary triangles and paths are part of the conversion;
their edges must not be interpreted as associativity defects of the original
loop. Composing this ordinary graph with F_q for a fixed prime q≠3 preserves
the decomposition invariant (20), by the graph recovery theorem. It does not
give general loop recovery.

## 6. Other graph choices and extension-data obstructions

### Commutation and power graphs

The nonassociative order-81 commutative Moufang loop from the one-edge ternary
construction and the group C_3^4 both have commutation graph K_81. Every
nonidentity element has order three in both. Their directed and undirected
power graphs are likewise isomorphic: forty triangles sharing their identity.
Binary generation-associativity tests cannot distinguish them, since Moufang
loops are diassociative.

Britten's theorem that undirected power graphs determine directed power graphs
for Moufang loops [BR, Theorem 1.1] does not assert recovery of the loop. The
example above makes that distinction concrete. Associating hypergraphs have
also been studied [MK]. For general Bol loops, ordering and repeated entries
in a triple must be retained; an unordered three-element hyperedge may lose
information. The Moufang triple-association theorem permits the unordered
relation in that narrower category [BR, Theorem 2.10].

### Identical associators and both defect matrices do not determine an extension

On U=F_2^3 with coordinates (t,x_1,x_2), Z=F_2, let f be the one-edge binary
cubic factor set. Add the bilinear cocycle

```math
 g((t,x_1,x_2),(s,y_1,y_2))
 =ts+x_1y_1+x_2y_2+ty_1+ty_2+x_1y_2.                    \tag{22}
```

Its coboundary is zero. Thus f and f+g give the same central associator D;
the exact Moufang identity, whose central residual depends only on D here,
still holds. Equivalently, substituting a bilinear g into that residual gives
zero directly. Their square maps are respectively

```math
 tx_1x_2,
 \qquad t+x_1+x_2+tx_1+tx_2+x_1x_2+tx_1x_2.              \tag{23}
```

The first has one nonzero value on U, while the second equals one at every
nonzero vector. Consequently the loops have respectively fourteen and two
elements satisfying x²=1, and are nonisomorphic. Both are nonassociative.

Formula (13) makes their complete local defect matrices identical. Its
conjugated version also makes their translated matrices identical. They have
the same central kernel, quotient, associator map and four cyclic order-two
composition factors. Thus retaining both graphs, or even the full
associator-valued function in these coordinates, still does not recover
arbitrary central-extension data. The missing square and commutator data are
not supplied by a classification of simple factors.

### Full subloop incidence can also fail to recover multiplication

The incidence graph between elements and all subloops, with its two vertex
types retained, is natural under isomorphisms and records the closure system,
orders and intersections. It is always connected when the whole-loop block
is included. Its connected components therefore cannot serve as direct factors.

Even full element/subgroup incidence with subgroup orders is not faithful.
For an odd prime p, compare the abelian group A=C_(p²) times C_p with

```math
 B=\langle a,b:a^{p^2}=b^p=1,
                bab^{-1}=a^{1+p}\rangle.                 \tag{24}
```

The latter is nonabelian. In both groups, the elements of order dividing p
form E congruent to C_p^2. There are p+1 order-p subgroups, the lines of E,
and p cyclic order-p² subgroups besides E itself. All those cyclic subgroups
meet exactly in C=⟨a^p⟩ and meet E in C. These, the trivial subgroup and the
whole group are all subgroups: a proper subgroup has order p or p², and an
order-p² subgroup outside E contains an element of order p² and is cyclic.

To verify the description for B, use coordinates (i,j) in Z/p² times Z/p with
product (i,j)(k,l)=(i+(1+p)^j k,j+l). An element has order dividing p exactly
when p divides i. Its pth power is (pi,0), since p is odd. This also counts
the p cyclic order-p² subgroups and their common line.

Match E linearly preserving C, and match generators of the p cyclic subgroups
compatibly on C. This gives an isomorphism of element/subgroup incidence and
of directed power graphs, though A and B are not isomorphic. Marking normality
would distinguish this example; no failure claim is made for that stronger
structure. The checker supplies the explicit isomorphism at p=3.

### Translation graphs and faithful relational controls

A Cayley graph needs a specified connection set. If every nonidentity left
translation is allowed and colors are discarded, its graph is K_|L| for every
loop: the equation ax=y determines a uniquely. Keeping each translation
label and its identification with its value at 1 recovers the whole table.
The abstract translation group is not its distinguished section. Moreover,
loop Cayley graphs need not be vertex transitive [GS], so the usual group
Cayley-graph conclusions cannot be imported automatically.

A faithful multiplication-incidence encoding uses element vertices, one tuple
vertex for every ordered pair (x,y), and three role-colored ports attached to
that tuple and respectively to x,y,xy. It has |L|+4|L|² vertices and 6|L|²
edges. A color-preserving isomorphism induces one common bijection of elements
and therefore a loop isomorphism. The minimum degree of this incidence graph
is two. Pendant paths of lengths 1 through 5, as in Section 5, remove its
five vertex types canonically. The resulting ordinary graph has
2|L|+18|L|² vertices and |L|+20|L|² edges.

Composing this control with the graph-loop construction gives a faithful
external encoding, but no algebraic factorization. Its auxiliary scaffold
already has edges for the trivial input loop. Faithfulness of such an
encoding is therefore distinct from a graph detecting useful nonassociative
structure in the original loop.

## 7. A uniform obstruction to obtaining arbitrary loops as factors

**Proposition 5.** Every section of a PR446 graph loop has central nilpotency
class at most two. Here a section means a quotient of a subloop. In particular,
a nonassociative simple loop cannot occur as a subloop, quotient, retract,
direct factor or section of any such graph-loop output, for any choice of the
initial loop-to-graph assignment.

**Proof.** Each graph loop has a central normal subloop Z with abelian-group
quotient. A subloop H has central normal subgroup H intersection Z and embeds
modulo it in that abelian quotient. A quotient of H inherits the image of
H intersection Z as a central subgroup and has abelian quotient modulo it.
Hence all sections have the same class-at-most-two property.

A simple loop with a central subgroup and abelian quotient is an abelian
group: the central subgroup is either trivial or the entire loop, and either
case gives associativity and commutativity. The finite simple sections of
the finite prime-field graph loops are therefore cyclic groups of order p.
Here p-power order does not use a general loop Lagrange theorem: H intersection
Z and its image in the additive quotient both have p-power order, so H does
too, and every quotient has equally sized fibers. ∎

This obstruction is independent of how much of the original loop is encoded
in the graph. A loop of central class greater than two is likewise excluded.
Graph loops can attach useful invariants and extensions to arbitrary loops;
they cannot universally decompose arbitrary simple Bol loops into their own
nonassociative sections.

## 8. Existing work, precise dependencies, and reproducibility

The associator subloop and universal group quotient are standard [SV-COM,
Sections 1 and 8]. Central and abelian extensions have established
characterizations [SV-EXT, Theorems 4.1 and 4.2]. Theorem 1 gives a graph
realization and explicit permutation proof of this quotient; it does not
claim a new notion of associator subloop. The decomposition conclusion in
Theorem 4 uses the canonical direct-core theorem linked there.

The earlier operator manuscript [AQ] already defines the translated average
(AQ.6), proves general Bol reversibility (AQ.25), and proves triviality of
every group image for its reciprocal family (Section 4.1). Its family-specific
mixing theorems are distinct from the central-family formulas (17)–(18).
Theorem 1 explains the general algebraic meaning of the fixed space rather
than promoting a family spectral estimate to a universal one.

The PR431 folder comparison is pinned at the inspected revision
`1388122a3de3301428b06dfc8877a63bb465d8ed`. C0001 preserves the full folder
(G,H,K) and records an exact quotient criterion and a failure of the naive
normal-subgroup converse. This note uses neither the aggregate classification
nor an unverified exhaustion statement. Its unrestricted classification
remains open at that source. The source-stated folder criterion supplies
context; Theorem 1 proves its special quotient directly. No claim that simple
factor classifications determine extension cocycles is imported.

### Exact diagnostics

Run the standard-library program

```sh
python notes/finite-simple-bol-loops/loop-decomposition/code/check_loop_defect_graphs.py
```

The program constructs actual multiplication tables and left-translation
permutations. Independently, it computes the least loop congruence identifying
all differently bracketed triple products, by closing those relations under
multiplication and both divisions. Their blocks are compared as full element
sets with the translated graph components, and the resulting quotient
multiplication is checked for associativity.

The finite examples are S_3, a non-Bol loop of order 5, the ternary one-edge
loop of order 81, the binary one-edge Bruck loop of order 16, both order-16
Moufang cocycle variants, and the two order-256 Bruck loops in Theorem 3.
The non-Bol example has a nonsymmetric translated matrix, confirming the need
for a Bol hypothesis in the reversibility assertion. Both order-16 Moufang
identities are checked on all triples, along with equality of their
associator values and both full defect matrices.

The checker verifies (17)–(18) independently by evaluating factor-set
coboundaries on a quotient basis. Its eleven cases have scalar ranks 0,2,4
at p=2,3 and ranks 0,2 at p=5, plus the binary cubic cases. It also enumerates
all ten subgroups in each order-27 incidence control and checks the explicit
incidence/power-graph isomorphism. These exact checks supplement the proofs;
they are not universal reconstruction or classification tests.

### References

- **SV-COM.** David Stanovsky and Petr Vojtechovsky, *Commutator theory for
  loops*, [arXiv:1509.05730v1](https://arxiv.org/abs/1509.05730v1), Sections 1
  and 8. Normal associator subloops and their required normal closure.
- **SV-EXT.** David Stanovsky and Petr Vojtechovsky, *Abelian extensions and
  solvable loops*, [arXiv:1509.05733v1](https://arxiv.org/abs/1509.05733v1),
  Theorems 4.1 and 4.2. Abelian and central extension characterizations.
- **LOOPS.** Official GAP LOOPS documentation,
  [Section 6.5](https://gap-packages.github.io/loops/doc/chap6_mj.html)
  and Section 6.6.5; the left inner generators and associator-subloop computation.
  The generator fact is proved directly in Theorem 1, so the live manual is
  not an indispensable unpinned dependency.
- **AQ.** Mira Cult, *Associator quantization and intrinsic mixing in reciprocal
  Bol loops*, [exact delivery source](../../analytic-2026-11-16/manuscripts/bol-associator-quantization.md),
  equations (AQ.5)–(AQ.6), Section 4.1 and equation (AQ.25). Its scientific
  review pin is `5771bfccb6707606078baf93be804f810276b8eb`.
- **SS.** Mira Cult, *Intrinsic spectral separation for reciprocal Bol loops*,
  [scientific source](../../analytic-2026-11-16/manuscripts/bol-intrinsic-spectral-separation.md),
  trace and associative-triple interpretation. This note does not re-certify
  its complete family-specific analysis.
- **FOLDER.** PR431,
  [C0001 at the inspected revision](../../claims/0001.md),
  parts 2–3. This is a scoped source comparison, not independent acceptance of
  its entire proof or the growing classification workspace.
- **BR.** Riley Britten, *Power graphs of Moufang loops*,
  [arXiv:2204.07165v3](https://arxiv.org/abs/2204.07165v3), Theorems 1.1 and 2.10.
- **MK.** Siddharth Malviy and Vipul Kakkar, *Associating hypergraphs defined
  on loops*, [arXiv:2408.16459v1](https://arxiv.org/abs/2408.16459v1), Section 1
  and the Chein-loop examples. Used as a graph-from-loops baseline.
- **GS.** T. S. Griggs, J. Širáň and R. B. Richter, *Graphs obtained from Moufang loops and
  regular maps*, [DOI:10.1002/jgt.20623](https://doi.org/10.1002/jgt.20623),
  the non-vertex-transitive Moufang Cayley-graph construction.

The next structural question is which additional intrinsic data recover the
nonassociative core inside family (15) without reinstating a vertex basis or
the full multiplication table. The identical-defect cocycle pair shows why
extending such a result to arbitrary central Moufang loops requires more than
associator data. These are separate from any claim about reconstruction from
unaligned deletion cards.
