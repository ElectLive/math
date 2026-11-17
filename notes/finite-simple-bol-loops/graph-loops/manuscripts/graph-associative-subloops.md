# Associative subloops, dominating sets, and graph components

Mira Cult

This manuscript supplies the structural payoff for the graph loops in
[the all-ring construction](graph-eisenstein-loops.md#the-all-ring-bruck-construction)
and [the binary cubic construction](graph-cubic-loops.md#1-elements-and-multiplication).
Its results are manuscript-local; no permanent claim IDs are allocated.
The constructions and their Bol/Moufang identities are proved in those sources.
Here we classify their maximal associative subloops by graph operations and
derive exact enumeration, extremal, and information-loss results.

An **associative subloop** is a subloop whose restricted multiplication is
associative, hence a group. “Maximal” always means maximal under inclusion
among associative subloops, not largest order and not a maximal proper subloop.

## 1. The graph form and the scope of the payoff

Let Γ=(V,E) be a finite simple undirected graph, n=|V| and e=|E|.
For a field F put W=F^V and

```math
Z=\Lambda^2W/\langle e_i\wedge e_j:\{i,j\}\notin E\rangle,
\qquad \beta(x,y)=[x\wedge y].                                      \tag{1}
```

Thus dim Z=e. A choice of orientation of each edge gives the coordinate
formula β_{ij}(x,y)=x_i y_j−x_j y_i. Reversing a chosen orientation reverses
the corresponding basis vector of Z. This is a coordinate convention, not
an orientation imposed on the input graph.

Our notation W for the vertex space and Z for the central edge space agrees
with the all-ring manuscript. The binary manuscript uses X for the vertex
coordinates, U for their marker-zero hyperplane, and W for the edge space.

For S⊆V, write Γ[S] for the induced subgraph, c(S) for its number of connected
components, and N[S] for its closed neighborhood. Set c(∅)=0. A subset is
**dominating** if N[S]=V. The empty subset is dominating exactly when V is empty.

The central linear-algebra fact is a classification of *every* maximal
β-isotropic subspace, not only an equality of maximum dimensions. A subspace
H≤W is β-isotropic if β(H,H)=0. The classification identifies H with a
dominating vertex subset and a full-support line on each of its induced
components. It then identifies the group subloops of the graph-derived laws.

### Prior results and what is being proved here

The equality between graph independence number and maximum isotropic dimension
is known: Bei–Chen–Guan–Qiao–Sun, [BCGQS, Theorem 3(1), §4]. Their Theorem 3(2)
also relates graph coloring to isotropic decompositions; this manuscript does
not claim either bridge as new. Their Theorem 10 bounds maximal isotropic
spaces for general alternating matrix spaces. Qiao [Q24, Theorem 1.2 and §1.3]
constructs a polynomial counting all isotropic spaces and interprets it through
abelian subgroups of class-two groups. Rossmann [R22, Theorem A] develops
graphical-group conjugacy polynomials. These are substantive baselines.

The proofs below give the exact dominating-support classification and its
transfer to maximal associative subloops for the present graph loops. The
searched primary sources do not supply this particular classification or its
Bol/Moufang contrast. This is a bounded source comparison, not a claim of
exhaustive novelty verification. In particular, a graph invariant already
present on the group side is not newly invented by calling it a loop invariant.

## 2. Every maximal isotropic space has a dominating support

**Theorem 1 (component-line classification).** Over any field F, the maximal
β-isotropic subspaces H of W are precisely the following spaces:

```math
H(S,a)=\bigoplus_{C\in\pi_0(\Gamma[S])} F a_C,                       \tag{2}
```

where S is a dominating subset of V and a_C has support exactly C. Two such
data give the same H exactly when their subsets S agree and, for every
component C, their vectors a_C span the same line. In particular dim H=c(S).

**Proof.** Let H be isotropic and let S be its support: i∈S when coordinate
evaluation λ_i:H→F is nonzero. For an edge {i,j} inside S, isotropy gives

```math
\lambda_i(x)\lambda_j(y)-\lambda_j(x)\lambda_i(y)=0
\quad\hbox{for all }x,y\in H.
```

The nonzero functionals λ_i and λ_j are therefore proportional. Along a path
in Γ[S], proportionality propagates. On each component C there are a nonzero
functional λ_C and nonzero scalars a_i with λ_i=a_iλ_C for i∈C. Let a_C
denote the vector with these coordinates on C and zero elsewhere. Then
H⊆H(S,a). The latter space is isotropic: within a component the coordinates
of any two vectors are proportional, and no edge joins two different
components of Γ[S]. If H is maximal, H=H(S,a).

For this full component-line space, define
H^⊥={y∈W:β(h,y)=0 for every h∈H}. Its explicit value is

```math
H(S,a)^\perp=H(S,a)\oplus F^{V\setminus N[S]}.                       \tag{3}
```

Indeed, on an edge inside C the equation is a_i y_j−a_j y_i=0, so y_i/a_i
is constant on C. An edge from i∈S to j∉S forces y_j=0. No equation constrains
a coordinate outside N[S]. These give (3), including singleton components.

For any alternating β, an isotropic space is maximal iff H^⊥=H: if
y∈H^⊥\H then H+Fy is a larger isotropic space, and every larger isotropic
space lies in H^⊥. By (3), H(S,a) is maximal iff N[S]=V. Finally the support
S and its component lines can be read back from H, proving uniqueness. ∎

**Corollary 1.1 (exact count).** Over F_q, the number of maximal isotropic
spaces with support S, for a dominating S, is

```math
(q-1)^{|S|-c(S)}.                                                   \tag{4}
```

There are (q−1)^{|C|−1} full-support lines on C: choose a nonzero value at each
vertex and divide by common nonzero scaling. Multiply over components.

**Corollary 1.2 (largest and smallest dimensions).** Let κ(Γ) be the number
of connected components of Γ, with κ(∅)=0. Among all maximal isotropic H,

```math
\min\dim H=\kappa(\Gamma),\qquad \max\dim H=\alpha(\Gamma).          \tag{5}
```

A dominating S meets every component of Γ, so c(S)≥κ(Γ); equality is attained
by S=V. Picking one vertex from each component of Γ[S] gives an independent
set, so c(S)≤α(Γ). A maximum independent set is dominating and attains α(Γ).
The maximum equality is the known independence/isotropy theorem cited above;
the full classification describes all equality and nonequality cases here.

**Corollary 1.3 (intersection).** The intersection of all maximal isotropic
spaces is rad β={x:β(x,W)=0}. Every isotropic space can be enlarged by rad β.
Conversely, if x∉rad β, choose y with β(x,y)≠0 and extend Fy to a maximal
isotropic space; that space cannot contain x. For (1), rad β is exactly
the span of the isolated vertices.

## 3. Proper Bol loops: all group subloops from dominating sets

Let p be a prime different from 3. Use the loop from the all-ring manuscript:

```math
L_p(\Gamma)=F_p\oplus W\oplus Z,
\quad
(a,u,s)(b,v,t)=(a+b,u+v,s+t+(a+2b)\beta(u,v)).                        \tag{6}
```

Its central subloop is Z₀={(0,0,z):z∈Z}; write π:L→F_pm⊕W for the quotient
map, with m=(1,0). The associator *difference* of (xy)z and x(yz), using
central additive coordinates, is

```math
D((a,u),(b,v),(c,w))
  =a\beta(v,w)-b\beta(u,w)-2c\beta(u,v).                            \tag{7}
```

The convention, loop axioms and exact left Bol proof are in the canonical
construction. Here (7) is an input already proved there. Denote
K₀=π^{-1}(W), the subloop with a=0. It is an elementary abelian group.

**Theorem 2 (all maximal associative subloops).** Suppose E≠∅. The complete
list of maximal associative subloops of L_p(Γ) is:

1. K₀;
2. for every maximal β-isotropic H≤W, the elementary abelian group

```math
K_H=\pi^{-1}(F_pm\oplus H).                                        \tag{8}
```

Consequently, for each d, the number of maximal associative subloops not
contained in K₀ and having order p^{e+1+d} is

```math
\sum_{\substack{S\subseteq V:\N[S]=V\\c(S)=d}}
       (p-1)^{|S|-d}.                                              \tag{9}
```

For E=∅, the entire loop is elementary abelian and is its unique maximal
associative subloop; (8)–(9) still correctly give this unique group, whereas
K₀ is then not maximal.

**Proof.** A maximal associative subloop K contains Z₀, since adjoining
central elements to a group subloop preserves associativity. Its image
U=π(K) is an F_p-linear subspace and K=π^{-1}(U). Such a preimage is
associative iff D(U,U,U)=0. If U≤W, its preimage is contained in K₀.

If U is not contained in W, write
U=F_p(m+x)⊕H, where H=U∩W and x is defined modulo H. Put r=m+x.
From (7), for h,k∈H,

```math
D(r,h,k)=\beta(h,k),\qquad D(h,r,r)=-3\beta(h,x).                    \tag{10}
```

Thus associativity implies β(H,H)=0 and x∈H^⊥. Conversely these two
conditions make β vanish on H+F_px, so the correction in (6) vanishes on U;
the preimage is elementary abelian.

The larger space F_pm⊕(H+F_px) still satisfies these conditions and contains
U. Maximality therefore forces x∈H and makes H maximal isotropic. Conversely,
if H is maximal isotropic, any larger associative projected space crossing W
would have a larger isotropic intersection with W, impossible. This proves
the list (8). Its restriction of (6) is ordinary addition, so |K_H|=p^{e+1+d}.
Theorem 1 gives (9).

If E≠∅, no associative projected space properly contains W, because such a
space would be the whole F_pm⊕W and (10) would force β=0. Thus K₀ is maximal.
If E=∅, (6) is addition throughout, giving the exceptional statement. ∎

The hypotheses p prime and p≠3 are important. Over a nonprime field F_q,
the same argument classifies maximal subloops whose quotient images are
F_q-linear; arbitrary subloops need only be F_p-linear. At p=3, the second
condition in (10) disappears and the next section gives a different answer.

### Intrinsic interpretation and an additional recovered subspace

For E≠∅ and p≠3, the all-ring manuscript recovers W intrinsically from the
right-alternative locus; see
[unmarked recovery](graph-eisenstein-loops.md#unmarked-recovery-over-prime-fields).
Thus K₀ and the class of subloops counted by (9) are intrinsic, including
graphs that are a star together with isolated vertices. No chosen vertex
basis or marker element is used in defining the count from the loop.

Theorem 2 and Corollary 1.3 further give

```math
\bigcap_{K\not\subseteq K_0\atop K\text{ maximal associative}}K
  =\pi^{-1}(F_pm\oplus\mathop{\mathrm{rad}}\nolimits\beta).                      \tag{11}
```

Consequently a marker line is recovered after factoring out the radical,
although a particular marker representative need not be intrinsic. The
smallest and largest groups in (9) have orders

```math
p^{e+1+\kappa(\Gamma)}\quad\hbox{and}\quad p^{e+1+\alpha(\Gamma)}.     \tag{12}
```

This supplies a concrete loop-theoretic description of graph components and
independence through the full distribution of group subloops.

## 4. Moufang suspension: affine freedom changes the answer

The binary cubic loop and the characteristic-three instance of (6) have a
central elementary abelian subloop Z₀ with quotient F_pm⊕W and alternating
associator

```math
T((a,u),(b,v),(c,w))
  =a\beta(v,w)-b\beta(u,w)+c\beta(u,v).                             \tag{13}
```

For the binary construction p=2; the characteristic-three construction uses
p=3. Let K₀=π^{-1}(W), retaining the stated marking when this subloop has
not been recovered intrinsically.

**Theorem 3 (maximal associative subloops in the suspension).** The maximal
associative subloops not contained in K₀ are exactly

```math
K_{H,\bar x}=\pi^{-1}\bigl(F_p(m+x)\oplus H\bigr),                  \tag{14}
```

where H is maximal β-isotropic and x ranges over W/H. Those of order
p^{e+1+d} number

```math
p^{n-d}\sum_{\substack{S\subseteq V:\N[S]=V\\c(S)=d}}
                  (p-1)^{|S|-d}.                                  \tag{15}
```

**Proof.** The central-enlargement argument from Theorem 2 again reduces
maximal associative subloops to full preimages of subspaces. For
U=F_p(m+x)⊕H, equation (13) gives T(m+x,h,k)=β(h,k). This is necessary
for associativity. It is sufficient because T is alternating trilinear:
triples in H vanish, triples with two repeated copies of m+x vanish, and
the remaining triples reduce to β(H,H). Thus U is associative iff H is
isotropic, without a condition on x. Enlarging U is equivalent to enlarging
H while retaining the same coset representative. Maximality is therefore
equivalent to maximal isotropy of H. The q=p count is the number (4) of H
times |W/H|=p^{n-d}. ∎

This is the precise difference from the proper Bol case. There the repeated
argument in (10) forces the affine shift into H; here alternation eliminates
that obstruction. The binary groups in (14) need not be elementary abelian.
The characteristic-three groups are elementary abelian, since the loop is
commutative of exponent three.

Where the relevant construction recovers W intrinsically, (15) is an
unmarked loop invariant. Otherwise it is an invariant of the loop together
with K₀. One must not call a selected hyperplane intrinsic merely because
the input presentation names a marker. The construction manuscripts state
their precise recovery and star-exception results.

## 5. A domination polynomial and exact consequences

Define a polynomial in formal variables q,z by

```math
A_\Gamma(q,z)=
\sum_{S\subseteq V:\N[S]=V}(q-1)^{|S|-c(S)}z^{c(S)}.                \tag{16}
```

By Theorem 2, the coefficient of z^d at q=p counts maximal associative
subloops outside K₀ of the proper Bol loop with order p^{e+1+d}. For the
Moufang suspension, the corresponding polynomial is

```math
D_\Gamma(q,z)=q^n A_\Gamma(q,z/q)
 =\sum_{S\text{ dominating}}q^{n-c(S)}(q-1)^{|S|-c(S)}z^{c(S)}.      \tag{17}
```

Both are polynomials, with nonnegative integer coefficients when expanded in
q−1 and z. Evaluation at q=1 in either yields

```math
A_\Gamma(1,z)=D_\Gamma(1,z)
 =\sum_{S\text{ maximal independent}}z^{|S|}.                       \tag{18}
```

Indeed a surviving term has |S|=c(S), which says Γ[S] is edgeless; a dominating
independent set is precisely a maximal independent set. This specialization
is formal; it does not posit a field of order one or a loop over such a field.

Under disjoint union, dominating subsets and their components split, hence

```math
A_{\Gamma\sqcup\Delta}=A_\Gamma A_\Delta,
\qquad D_{\Gamma\sqcup\Delta}=D_\Gamma D_\Delta.                    \tag{19}
```

The degree in z is α(Γ), and the smallest z exponent is κ(Γ). The coefficient
of (q−1)^k z^d in A is exactly the number of dominating subsets of size k+d
with d induced components. Thus the polynomial contains the full joint
distribution of these two graph statistics. Values obtained from the family
of proper Bol loops at sufficiently many primes recover it by ordinary
polynomial interpolation. This does not claim that one evaluation at a
single prime determines every coefficient.

**Corollary 5.1 (sharp number of maximal group subloops).** For n>0 and every
prime p≠3,

```math
A_\Gamma(p,1)\leq\frac{p^n-1}{p-1},                               \tag{20}
```

with equality iff Γ=K_n. In particular compact generating sets for all maximal
associative subloops of L_p(Γ) can be listed with at most p^{O(n)} arithmetic
work up to a polynomial factor in n+e, by (2) and (8). This is a count of
generating descriptions, not a claim that every element or multiplication-table
entry of these exponentially larger subloops is output at that cost.

**Proof.** Every dominating S is nonempty. Since c(S)≥1 and p−1≥1,

```math
A_\Gamma(p,1)
 \leq\sum_{\varnothing\ne S\subseteq V}(p-1)^{|S|-1}
 =\frac{p^n-1}{p-1}.
```

Equality holds for K_n because all nonempty S dominate and are connected.
If Γ is not complete, some singleton fails to dominate, so its positive
term is absent and the inequality is strict. The generation claim follows
by scanning subsets, finding their components, and outputting the
(p−1)^{|S|−c(S)} choices with one coordinate on each component normalized to
one. Output the additional K₀ for E≠∅. ∎

This graph-specific exact enumeration is separate from the general
alternating-matrix-space bounds of [BCGQS, Theorem 10].

### Small exact examples

The table uses the proper Bol polynomial (16). Formula (17) converts it to
the Moufang suspension count without another enumeration.

| Graph | A_Γ(q,z) |
|---|---|
| Empty vertex set | 1 |
| Edgeless graph on n vertices | z^n |
| One edge | (q+1)z |
| Path on three vertices | q²z+z² |
| Complete graph K_n, n≥1 | (1+q+⋯+q^{n−1})z |
| Star K_{1,r}, r≥1 | q^r z+z^r |
| Four-cycle | (q−1)(q+1)²z+2z² |

For instance the path on three vertices gives p² maximal crossing groups
of order p^{e+2} and one of order p^{e+3}, with e=2. For the characteristic-
three Moufang suspension this becomes 3⁴ such groups of order 3⁴ and three
groups of order 3⁵, by the affine multiplicities in (15).

### Exactly what the size distribution loses

Even the entire polynomial (16), together with n and e, does not classify
graphs. Consider these graphs on {1,…,6}:

```text
Γ: 12, 15, 16, 23, 24, 25, 34
Δ: 12, 13, 15, 16, 25, 26, 34.
```

Both have seven edges and exactly two triangles. In Γ the triangles meet
in one vertex; in Δ they share an edge, so the graphs are not isomorphic.
Nevertheless both have

```math
A(q,z)=q^4(q-1)z+q^2(2q+1)z^2+(q+1)z^3.                           \tag{21}
```

For a directly checkable expansion, the following table lists the number
of dominating subsets with c(S)=d and |S|−c(S)=k; both graphs give it.

| d \ k | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 1 | 4 | 6 | 4 | 1 |
| 2 | 3 | 8 | 7 | 2 | 0 | 0 |
| 3 | 2 | 1 | 0 | 0 | 0 | 0 |

Thus these nonisomorphic loops have the same maximal-associative-subloop
order distribution in the proper Bol family, including K₀, and in the
marked suspension family. Full loop reconstruction uses more multiplication
data than this one invariant.

## 6. Chein doubling as an established comparison

This section records a second graph-sensitive construction, explicitly as a
composition of established constructions. Fix an odd prime p and let

```math
G_\Gamma=W\oplus Z,
\quad (v,s)(w,t)=(v+w,s+t+\tfrac12\beta(v,w)).                       \tag{22}
```

Bilinearity proves associativity; identity is (0,0), inverse is (−v,−s),
and [G,G]=Z. This is the Baer–Lovász–Tutte graph group, not a new group.
Chein's loop M(G,2)=G⊔Gu has products

```math
g\cdot h=gh,\quad g\cdot(hu)=(hg)u,\quad
(gu)\cdot h=(gh^{-1})u,\quad(gu)\cdot(hu)=h^{-1}g.                  \tag{23}
```

The neutral element is the group identity. Each division equation determines
the parity first and then has a unique solution by group cancellation, so
(23) is a loop. For completeness, direct substitution proves the Moufang
identity (xy)(zx)=(x(yz))x. For x=gu^a, y=hu^b, z=ku^c, both sides equal
the entry below; entries carrying u are in the second copy of G.

| abc | Both sides |
|---|---|
| 000 | ghkg |
| 001 | (kh)u |
| 010 | (hk⁻¹)u |
| 011 | gk⁻¹hg |
| 100 | k⁻¹h⁻¹ |
| 101 | (gh⁻¹k⁻¹g)u |
| 110 | (gkh⁻¹g)u |
| 111 | h⁻¹k |

For v,w∈W, the parenthesizations (g_vg_w)u and g_v(g_wu) have underlying
group factors g_vg_w and g_wg_v. Their difference is exactly β(v,w).
Thus an edge produces nonassociativity and an edgeless graph produces a
group. Unlike a product with one fixed octonion loop, this nonassociativity
depends on the graph. Nevertheless it is a known Chein mechanism.

The graph group is recovered intrinsically as the set of odd-order elements
of M(G,2), since every element of Gu squares to the identity. He–Qiao
[HQ20, Theorem 1.1] then gives unmarked graph reconstruction. The new loop
statement is a direct consequence of their graph-group theorem and Chein
doubling; it must not be presented as a new proof of graph-group rigidity.

The requested graph–loop literature contains a direct use of the same Chein
law. Griggs–Širáň–Richter [GSR12, §2 and §3, Theorem 2] relate cubic Cayley
graphs of M(G,2), with generators au,bu,cu, to regular orientable hypermaps
whose parameters are the orders of b⁻¹a,c⁻¹b,a⁻¹c. Their §4 constructs
Cayley graphs of Moufang loops that are not Cayley graphs of groups. This
is an existing substantive graph–loop bridge, but it does not give the
arbitrary-input construction or the dominating-subset classification above.

An associative subloop meeting Gu has the form
H⊔(gH)u for a subgroup H≤G. The map h↦h, hu↦(gh)u identifies it with
M(H,2), which is associative iff H is abelian. (The triple h₁,h₂,u proves
necessity, and if H is abelian the displayed Moufang law is an associative
generalized dihedral group.) A maximal such group therefore has H maximal
abelian, contains Z, and corresponds to a maximal β-isotropic subspace.
There are p^{n-d} choices of outside coset for a d-dimensional isotropic
space. Consequently D_Γ(p,z) from (17) counts its maximal even-order
associative subloops, with z^d corresponding to order 2p^{e+d}. This count
is unmarked for every graph because its odd-order group is intrinsic.

### Associativity probability is a weaker control

Let cp(G) be the probability that two uniformly chosen elements of G commute.
For the eight parity types of a triple in M(G,2), type 000 always associates.
For the other seven types, associativity is equivalent to commutation of
the following pair:

| Parities | Pair that must commute |
|---|---|
| 001 | g,h |
| 010 | g,k |
| 100 | h,k |
| 011 | g,k⁻¹h |
| 101 | h,k⁻¹g |
| 110 | k,h⁻¹g |
| 111 | h⁻¹g,h⁻¹k |

In each row the pair is uniformly independent when g,h,k are. Therefore

```math
\Pr[(xy)z=x(yz)]=\frac{1+7\mathop{\mathrm{cp}}\nolimits(G)}8.                   \tag{24}
```

For a graph group, a vector x of support S has
dim ker β(x,−)=n−|N[S]|+c(S), by the same component equations as in
Theorem 1. Hence

```math
\mathop{\mathrm{cp}}\nolimits(G_\Gamma)
 =p^{-n}\sum_{S\subseteq V}(p-1)^{|S|}p^{-|N[S]|+c(S)}.             \tag{25}
```

Equation (25) lies within the known graphical-group centralizer/conjugacy
theory of [R22]. Equations (24)–(25) are included as a directly proved
comparison, with no novelty assertion for associativity-degree formulas.

## 7. Proof and computation boundaries

The proofs above are over all graphs and the stated fields. The independent
small-instance check enumerates all RREF subspaces of F_p^n for p=2,3 and
0≤n≤4, and for each labeled simple graph tests β-isotropy and maximality
by an independently computed orthogonal-complement rank. All 152 graph/field
cases agree with (4), including all 67 subspaces of F₂⁴ and all 212 subspaces
of F₃⁴. A separate 64-subset enumeration for each graph verifies (21), and
the triangle-intersection test certifies their nonisomorphism. These finite
checks are reproducibility evidence and do not replace any general proof.

The identities of the underlying loop laws, unmarked recovery of K₀, and
orientation/color behavior are reviewed in their own construction sources.
No statement here solves the finite-simple proper-Bol classification or the
graph reconstruction conjecture. In particular, no vertex-deletion deck is
being inferred from an unmarked list of subloop orders.

## References

- **BCGQS.** X. Bei, S. Chen, J. Guan, Y. Qiao, X. Sun, *From independent sets
  and vertex colorings to isotropic spaces and isotropic decompositions:
  Another bridge between graphs and alternating matrix spaces*,
  [arXiv:1904.03950v2](https://arxiv.org/abs/1904.03950v2), 22 September 2019.
  Theorem 3 and §4: independence/coloring equivalences. Theorem 10 and §8:
  maximal isotropic spaces for arbitrary alternating matrix spaces.
  Published SIAM J. Comput. 50(3) (2021), 924–971,
  [DOI 10.1137/19M1299128](https://doi.org/10.1137/19M1299128).
- **Q24.** Y. Qiao, *A q-analogue of graph independence polynomials with a
  group-theoretic interpretation*,
  [arXiv:2408.09963v2](https://arxiv.org/abs/2408.09963v2), 11 June 2026.
  Theorem 1.2 and §1.3: all isotropic spaces and abelian-subgroup interpretation.
  Published BLMS 58(11) (2026), e70539,
  [DOI 10.1112/blms.70539](https://doi.org/10.1112/blms.70539).
- **HQ20.** X. He and Y. Qiao, *On the Baer–Lovász–Tutte construction of
  groups from graphs: isomorphism types and homomorphism notions*,
  [arXiv:2003.07200v2](https://arxiv.org/abs/2003.07200v2), 4 May 2020.
  Proposition 1.2 and §2: edge-coordinate alternating maps classify graphs
  over every field. Theorem 1.1: the graph-group version over odd prime fields.
- **R22.** T. Rossmann, *Enumerating conjugacy classes of graphical groups
  over finite fields*, BLMS 54(5) (2022), 1923–1943,
  [DOI 10.1112/blms.12665](https://doi.org/10.1112/blms.12665), Theorem A and
  centralizer discussion. Used as the baseline for (25), which is also
  proved directly above.
- **C74.** O. Chein, *Moufang loops of small order. I*, Trans. Amer. Math.
  Soc. 188 (1974), 31–51. The construction is also stated and studied in
  P. Vojtěchovský, *On the uniqueness of loops M(G,2)*, CMUC 44(4) (2003),
  629–635, [DML-CZ](https://dml.cz/handle/10338.dmlcz/119417).
  The loop and Moufang verifications for the convention used here are given
  in §6, so the result does not rely on an unchecked convention transfer.
- **GSR12.** T. S. Griggs, J. Širáň, R. B. Richter, *Graphs obtained from
  Moufang loops and regular maps*, J. Graph Theory 70(4) (2012), 427–434,
  [DOI 10.1002/jgt.20623](https://doi.org/10.1002/jgt.20623). §2 gives the
  Chein law; §3, Theorem 2 gives the Cayley-graph/regular-hypermap
  correspondence. The primary paper text was inspected through
  [the author's posted copy](https://www.academia.edu/113233049/Graphs_obtained_from_Moufang_loops_and_regular_maps).
