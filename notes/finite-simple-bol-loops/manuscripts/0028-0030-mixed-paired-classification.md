# 0028–0030. Mixed paired simple envelopes: matrices, paths and an isotopy obstruction

**Mira Cult**

## Results obtained

We classify the canonical folders in one specified mixed semisimple model: the canonical group is `A₅^(2A) × PSL₂(7)^(2B)`, with A,B positive, and its inverting automorphism exchanges the coordinates in each prescribed pair. The classification is by path lengths and a binary–ternary matrix pair, with explicit admissibility and isomorphism tests. It is not a classification of all radical-free Bol loops.

- **0028, classification.** The parameters are positive A₅-path lengths r₁,…,rₐ summing to A; positive PSL₂(7)-path lengths s₁,…,sᵦ summing to B; a binary a-by-b matrix χ; and a ternary b-by-a matrix L. The directed graph with arcs Tᵢ→Uⱼ when χᵢⱼ≠0 and Uⱼ→Tᵢ when Lⱼᵢ≠0 must be strongly connected. Every admissible datum produces a finite simple proper left Bol loop, and every loop in the stated model arises this way. Its order is `60^A 168^B`. Isomorphism is exactly length-preserving permutation of each path set together with independent signs on the **T-indexed columns** of L. Arbitrary matrix basis changes and U-row signs are not allowed.
- **0029, explicit family.** Taking one path of each type gives exactly one isomorphism class for each pair of positive lengths (A,B). It has an exact-factorization isotope precisely when A and B have the same parity. Opposite parity therefore yields loops outside that construction route; none of this family has a Bruck isotope. The case (A,B)=(2,1) has order 604800. Absence of an exact-factorization isotope is not a proof that the loop is not a G-loop.
- **0030, intrinsic obstruction.** In a paired semisimple canonical folder, splitting atoms of the actual stabilizer and coordinate-pair edges give a graph. Exact-factorization witnesses are precisely its proper two-colorings. For the matrix family this becomes a weighted-cycle parity test, with either zero or two witness subgroups. That number is not a count of loop isomorphism classes.

The proof below retains the mathematical dependencies of the source arguments. In particular its exhaustion and interpretation as a loop classification use the folder, inversion, subgroup and normal-quotient inputs below. This is a research proof exposition, not a claim of independent human refereeing, formal verification or established literature priority.

## 1. Conventions and inputs

A faithful generated canonical folder consists of a finite group G, a core-free identity stabilizer H, and a generating set K of left translations. The section K is a transversal to every conjugate of H and is closed under inverses and the operation (x,y)↦xyx. The loop product is the unique representative m∈K for which kl∈mH. The canonical automorphism τ inverts K.

We use these specific inputs; their complete proofs are not reproduced here.

1. [Folder equivalence and exact normal-subloop criterion](../update-2026-11-16/proofs/C0001.md), and [canonical inversion](../update-2026-11-16/proofs/C0007.md). In particular simplicity is tested over **every** nontrivial proper normal subgroup N of G by the strict inequality `|π(K)| > [G/N:π(H)]`. A projection is not presumed to define a quotient loop.
2. [Paired marked sets](../update-2026-11-16/manuscripts/radical-free-paired-simple-envelopes.md): in the paired model K is the full product of anti-diagonals. Its square is precisely the set of pairs of conjugate inverse entries. Consequently `|G|=|K|²`, `|H|=|K|`, and `H∩K²={1}`.
3. [Full-strip forests](../update-2026-11-16/manuscripts/radical-free-strip-forests.md), the [mixed forest/density reduction](../update-2026-11-16/manuscripts/radical-free-mixed-simple-quotients.md), and the [involution support-parity lemma](../update-2026-11-16/manuscripts/radical-free-involution-support.md). We give the further mixed-type and equality-case arguments below.
4. The subgroup and fusion data from the [A₅ path argument](../update-2026-11-16/manuscripts/radical-free-a5-path-classification.md) and [small-PSL₂ path argument](../update-2026-11-16/manuscripts/radical-free-small-psl2-paths.md). In A₅ the maximal proper subgroups are A₄, D₁₀ and S₃; in PSL₂(7) they are 7:3 and S₄. Both groups have a unique involution class. PSL₂(7) has one inverse-stable order-three class, and its two S₄ classes are fused by automorphisms. Those sources record the Dickson-classification reference and finite fusion certificates; we do not rerun those certificates here.
5. The [intrinsic exact-factorization and isotope criteria](../update-2026-11-16/manuscripts/exact-factorization-criterion.md), including the generalized-Fitting obstruction to Bruck isotopes, and the simple-Moufang primitivity input in the folder source. These supply the final route exclusions and non-Moufang conclusion, not the matrix reconstruction itself.

Write T=A₅ and U=PSL₂(7). Internal path vertices carry full diagonal simple strips; endpoints carry D₁₀,A₄ on T paths and S₄,7:3 on U paths. An edge is a τ-pair, not a generator of the resulting loop.

The endpoint quotient coordinates are d∈F₂ᵃ from D₁₀/C₅, e∈F₂ᵇ from S₄/A₄, α∈F₃ᵃ from A₄/V₄, and β∈F₃ᵇ from (7:3)/C₇. The defining equations are

```math
d=\chi e,\qquad \beta=L\alpha.
```

Normalize the last quotient by μ(y)=e when `yxy⁻¹=x^(2^e)` on a C₇ kernel. It is independent of the generator x. Choosing the sign of A₄/V₄, in contrast, is precisely the column-sign freedom of L.

## Reduction to paths and saturated endpoint groups

The full-coordinate projection of H is a product of disjoint full twisted strips, separately for T and U. Every proper subgroup of either simple group is solvable: for T its maximal proper subgroups are A4, D10, S3; for U they are 7:3 and S4. Thus the projection R onto all proper coordinates is solvable, and Goursat splits every full T or U strip independently from R, including across the two types. A singleton strip would put a normal simple coordinate into H, contradicting faithfulness. Every full strip has degree at least two.

Apply the mixed maximal-type forest counting argument separately to each type; its only use of maximal type was to obtain precisely the strip splitting just established. For each nonempty connected component C, retaining its complete τ-pairs gives a proper normal quotient because the other simple type is present. The exact simplicity criterion then gives |R_C|>|V|^(k_C−m_C), with V=T or U, k_C edges and m_C strip vertices. If C has no proper-coordinate leaves, the degree bound gives k_C≥m_C and contradiction. If it has h leaves, each proper endpoint projection has order strictly below |V|, so |R_C|<|V|^h; hence the cycle rank is zero. Thus every component is a tree with at least two leaves. Write c_T,c_U for their counts and ℓ_T,ℓ_U for total leaves. The forest identities and |H|=|T|^A|U|^B yield

```text
|R|=60^(ℓ_T−c_T)168^(ℓ_U−c_U).                                (8)
```

Both T and U have a single involution class. Let s_T=|T|_2=4 and s_U=|U|_2=8. The support-parity lemma in `radical-free-involution-support.md`, applied globally to a Sylow 2-subgroup of R with every forest component as a block, shows that each component has at most one leaf whose 2-part is deficient. The proof works with the mixed capacities: if two leaves in any one component are deficient, the product of all coordinate Sylow orders divided by one minimum per component is strictly smaller than |R|_2, giving a nonidentity involution supported constantly on each component and hence a collision after filling the independent full strips.

Every T leaf carrying a factor 5 lies in D10 and is 2-deficient; U has no factor 5. Equation (8) forces at least ℓ_T−c_T 5-bearing leaves, at most c_T by the preceding paragraph. As every tree has at least two leaves, ℓ_T=2c_T. Likewise only U leaves can carry 7, every 7-bearing U leaf lies in the odd group 7:3 and is deficient, so ℓ_U=2c_U. All components are paths; every component has exactly one such 5- or 7-bearing deficient endpoint and one endpoint with full 2-part.

For a T path, a 5-bearing endpoint lies in D10 (order 10) and its full-2-part endpoint lies in A4 (order 12). The strict projection inequality |R_C|>60 forces both actual endpoint projections to be the full D10 and A4, and then the projection itself has order 120: it divides 120 and is greater than 60. For a U path, the respective endpoints lie in 7:3 (order 21) and S4 (order 24). The strict inequality |R_C|>168 forces both to be full. The actual endpoint-pair projection has order 252 or 504. An index-two subgroup of (7:3)×S4 is the kernel of the S4 sign, since 7:3 has odd order; its S4 projection is A4, contrary to fullness. Hence the projection is all (7:3)×S4 of order 504.

Therefore R has the endpoint ambient group and order (1) below with a=c_T, b=c_U. The index in the ambient endpoint product is 2^a3^b. The coordinatewise normal C5^a and C7^b are contained in R, since the index is coprime to 5 and 7. Each simple type occurs, so a,b≥1. All strip twists may be gauged away on the trees independently by coordinate automorphisms; choices of conjugacy classes and quotient identifications must be retained in a later isomorphism analysis.

## Setup

Let there be a≥1 T=A5 path components and b≥1 U=PSL2(7) path components. Full strips on internal vertices are already split off as independent factors of H. Denote their actual endpoint projection by

```text
R ≤ D10^a × A4^a × (7:3)^b × S4^b,
 |R|=60^a 168^b.                                               (1)
```

Assume every indicated endpoint projection is the entire named group; R contains the coordinatewise normal C5^a and C7^b; and the original H misses K². Each simple type has one involution class. In an active path the internal strips can be populated by conjugate involutions, so R cannot contain a nonidentity involution whose support is constant across the two endpoints of every path. Neither R nor its Sylow subgroups are assumed to split between components.

## The equality case of support parity

Let P∈Syl2(R). By (1), |P|=2^(2a+3b). A 2-subgroup of D10 has order at most 2; the Sylow 2-subgroup of A4 is V4; 7:3 is odd; and a Sylow 2-subgroup of S4 is D8. For an involution-or-identity x∈P, let e_i(x) be 1 if endpoint i is identity and 0 otherwise. Modulo 2, the indicator that the two endpoint supports agree on a path is 1+e_left+e_right. Summing the product of these indicators over x²=1 expands into a sum, one term for each choice of zero or one endpoint per path, of counts of involutions-or-identity in a projection kernel.

Every such target has order at most |P|. Exactly one choice can have target of order |P|: choose the A4 endpoint on each T path and the S4 endpoint on each U path. All other targets have strictly smaller order, because omitting a chosen endpoint or replacing V4 by a D10 2-image costs at least 2, while replacing D8 by an odd 7:3 image costs 8. Their kernels are nontrivial 2-groups and contain an even number of solutions of x²=1, identity included. The matched-support count is exactly 1, by the collision hypothesis. Hence the unique maximal-target kernel has an odd number of such solutions, so it is trivial. Its target has order |P| and

```text
P → V4^a × D8^b                                                 (2)
```

is an isomorphism, after choosing the actual Sylow-2 D8 image in each S4. The D10-coordinate projections of P are a homomorphism from this product into C2^a. The 7:3 coordinates of P are trivial. This conclusion does not require P◁R.

## Isolating all normal Klein-four factors

Fix one A4 or S4 endpoint and a vector v in its normal V4. By (2) choose x∈P with that V4 coordinate v and every other coordinate in the target (2) equal to 1. Choose r∈R whose projection at that endpoint is a 3-cycle; this is possible by full endpoint projection. The commutator [r,x] has D10 coordinates in their commutator C5, all other A4 and S4 coordinates equal to 1, all 7:3 coordinates equal to 1, and selected V4 coordinate (g−1)v, where g is the 3-cycle action. Its fifth power removes every C5 coordinate and leaves the selected V4 coordinate unchanged. Since g−1 is invertible on V4≅F2², varying v produces that entire coordinate copy of V4 inside R. Repeat for every endpoint.

These coordinate copies are normal 2-subgroups of R, hence lie in P. Therefore the graph map in (2) vanishes on all T-side V4 and all normal S4-side V4. It factors through the independent S4 sign coordinates. There is a binary linear map

```text
χ:F2^b→F2^a                                                   (3)
```

such that the D10 sign vector of every element of R is χ applied to its S4 sign vector. To see the assertion for every element, the difference of these two sign homomorphisms vanishes on the Sylow subgroup P; a homomorphism to a 2-group that vanishes on a Sylow 2-subgroup is trivial. Full D10 endpoint projections force every row of χ to be nonzero.

## A ternary graph

Factor out the contained normal coordinate groups C5^a, C7^b, V4^a and V4^b. The quotient sits in

```text
C2^a × C3^a × C3^b × S3^b
```

and has order 3^a 6^b. Its 2-sign projection onto E=C2^b is surjective by (2); its kernel W is an E-invariant subspace of

```text
F3^a ⊕ F3^b ⊕ F3^b,
```

of dimension a+b. The first two summands are the A4/V4 and (7:3)/C7 coordinates; E acts trivially there. Its j-th generator negates the j-th coordinate of the last summand, the normal C3 of S3_j, and fixes the others. Full S4 endpoint projection forces W to project nontrivially onto every last-summand coordinate. Taking w−e_j w isolates that coordinate, so

```text
W = W0 ⊕ F3^b,       dim W0=a,       W0≤F3^a⊕F3^b.           (4)
```

The first two sets of coordinate projections of W0 are all nonzero, since the corresponding A4 and 7:3 endpoint projections are full. The chosen P supplies a complement E; after selecting compatible Sylow-2 representatives, W0 is central and the last F3^b together with E is the full S3^b. Thus (3) and (4) describe the actual quotient of R, not merely its Sylow subgroup.

Collision-freeness forces W0 to project injectively onto its first F3^a. If (0,z)∈W0 is nonzero, select in each active 7:3 coordinate an element of order 3 mapping to z_j, and in the corresponding independent S3 coordinate an order-3 element; on inactive U paths select identity. The necessary adjustments by C7^b are available inside R. Every active U endpoint pair is then a pair of conjugate inverse order-3 elements, while all T endpoints are identity. Filling active internal U strips yields a nonidentity element of H∩K². Hence this is impossible. By dim W0=a, the first projection is an isomorphism. There is a linear map

```text
L:F3^a→F3^b,       W0={(α,Lα):α∈F3^a},                       (5)
```

and every row of L is nonzero by full 7:3 endpoint projection. In these coordinates R is the full preimage of the quotient described by (3) and (5).

Conversely, under the assumed product of independent internal full strips and path geometry, the equations (3) and (5) imply H∩K²=1. For a paired T path to be active in K², its endpoint values must both be involutions (the only common nonidentity order between D10 and A4); thus its A4 C3 value is zero. On every inactive T path that value is also zero. Hence α=0, forcing all U 7:3 C3 values to zero. A nonidentity matched U pair can only have order 3, so every U path is inactive. All S4 signs are zero, so χ gives all D10 signs zero, and no T path can be active either. For full strips, propagated matched conjugacy preserves the order and identity support along the path; no assumption that an arbitrary projected subgroup is itself a folder is used.

## Simplicity criterion for all coordinate quotients

For I⊆{1,…,a}, J⊆{1,…,b}, retain all coordinates of the selected complete path components and project H. Counting the independent internal strips, full normal endpoint factors, and the extra independent sign/C3 values gives

```text
|π_{I,J}H|/(60^{number of retained T pairs} 168^{number of retained U pairs})
   = 2^rank(χ_{I,J^c}) · 3^rank(L_{J,I^c}).                    (6)
```

The binary exponent counts D10 signs on selected T paths supplied by unselected U signs; the ternary exponent counts 7:3/C7 values on selected U paths supplied by unselected T A4/V4 variables. This is independent of path lengths.

Make a directed bipartite graph whose vertices are the a T paths and b U paths: χ_ij≠0 gives T_i→U_j, and L_ji≠0 gives U_j→T_i. Equation (6) and the exact normal-subloop criterion show that strictness for every nonempty proper union of complete components is equivalent to strong connectivity of this directed graph. In particular each vertex has an outgoing edge, as already required by the endpoint projections.

For arbitrary retained individual incidences, let t_T,t_U count touched internal vertices and f_T,f_U count edges whose two incidences are retained. Let D,A,B,S denote the sets of selected endpoint coordinates of the corresponding types, with sizes d,a′,b′,s. Directly projecting (3) and (5) gives the exact ratio

```text
|π(H)| / (|G_J|/|π(K)|)
 = 60^(t_T−f_T) 168^(t_U−f_U) · 5^d 12^a′ 7^b′ 24^s
   · 2^rank(χ_{D,S^c}) · 3^rank(L_{B,A^c}).                    (7)
```

Indeed the projected binary quotient (χ(e)_D,e_S) has dimension |S|+rank(χ_{D,S^c}); the projected ternary quotient (α_A,(Lα)_B) has dimension |A|+rank(L_{B,A^c}). All normal endpoint kernels and independent internal strips are contained in H. Equation (7) applies equally to non-τ-stable normal quotients.

For each full selected T path, its baseline factor in (7) is 5·12/60=1, and for each full selected U path it is 7·24/168=1; empty paths contribute 1. Every nonempty partial path has t−f≥0: if it selects an endpoint its baseline factor is at least 5, and if it selects no endpoint then t−f≥1 and its baseline factor is at least 60. Rank factors are always at least 1. Hence any nonempty partial path forces strictness. If there are no partial paths, (6) gives strictness precisely when the directed graph is strongly connected; the full selection is the trivial kernel and is excluded. Therefore strong connectivity is necessary and sufficient for the strict normal-quotient simplicity criterion for all retained-coordinate sets, under the hypotheses and inputs in §1.

This proves exhaustion and admissibility in the stated paired A5/PSL2(7) setting, using the inputs in §1. The isomorphism action is established below. The data include the previously constructed single-cycle family but allow arbitrary strongly connected directed bipartite supports.


## Construction and properness

Conversely, choose positive path lengths summing to A and B, place full simple strips on internal vertices, and impose (3),(5) on the prescribed endpoint groups. Independent normal endpoint factors and the quotient graph equations make the stabilizer a genuine subgroup of order |K|; the argument above gives H∩K²=1, so K is a transversal to every conjugate of H. K generates G because both simple groups are perfect. All endpoint groups are proper and every internal strip has at least two-coordinate support, so H is core-free. Equation (7) and strong connectivity give strictness for every proper nontrivial coordinate quotient; C0001 gives simplicity. H is nontrivial, so the loop is nonassociative. Its canonical action is imprimitive because H lies in the proper product of the vertex groups; the cited simple-Moufang primitivity result gives properness. Its canonical group has trivial 2-core, so the [generalized-Fitting obstruction](../update-2026-11-16/manuscripts/exact-factorization-criterion.md), excludes Bruck isotopes under its stated canonical and isotopy inputs. 



## Isomorphism criterion

Use m=a and n=b for the numbers of paths in this section. Let m,n≥1, path lengths a_i,b_j≥1, and suppose endpoint projections are full and the matrices χ∈Mat_{m×n}(F₂), L∈Mat_{n×m}(F₃) define the actual subgroup H via d=χe and β=Lα. The internal full T=A5 and U=PSL₂(7) strips are independent of this endpoint subgroup. For two such simple canonical folders, the loops are isomorphic exactly if there are permutations of T paths and U paths preserving their lengths, carrying χ by the corresponding row/column permutations, and carrying L by the reversed row/column permutations followed by independent sign changes of its T-indexed columns. Equivalently, after relabeling, χ'=χ and L'=L D for a diagonal D with entries ±1. No U-indexed row signs or arbitrary linear changes of basis occur. The criterion includes strongly connected matrices from the simplicity theorem; that connectivity makes every row of both χ and L nonzero and hence gives full D10 and 7:3 endpoint projections. The preceding exhaustion proof supplies these hypotheses for every loop in the paired two-type model.

### Necessity

A loop isomorphism induces an isomorphism of canonical folders and commutes with their inverting automorphisms: the anti-diagonal K generates G and uniquely determines inversion on it. Thus it permutes simple coordinate factors in G, preserving simple type and τ-pairs, and carries actual H to H'. The endpoint group R is solvable, being a subgroup of a product of D10,A4,S4,7:3. Therefore the nonabelian minimal normal subgroups of H are exactly its independent full simple strips: an intersection of a nonabelian simple normal subgroup with R is trivial, and its image in the direct product of strips is normal and hence a product of strip factors, minimality forcing one. Their two-coordinate supports together with the τ-pair edges recover every path. In particular this remains valid for paths of length one, which have no internal strip. The proper endpoint projections have pairwise distinct orders 10,12,24,21, so the two ends of each path are intrinsically distinguished. The folder isomorphism therefore induces length-preserving permutations of the T paths and of the U paths; a coordinate flip or reversal changes only their drawing, not which endpoint is D,A,S or B.

Gauge each path so that its full strips are ordinary diagonals. A coordinate automorphism commuting with τ applies one simple-group automorphism simultaneously to the two incidences of each paired edge. Preservation of an internal diagonal forces the automorphisms on its incident edges to agree, so the induced action is one common automorphism per path after the source and target gauges. There is no ambient automorphism that linearly mixes distinct simple coordinate factors: automorphisms of a direct product of nonabelian simple groups permute its minimal normal simple factors.

On the T=A5 path, simultaneous automorphisms carrying the ordered endpoint pair D10,A4 to its target preserve the unique quotient D10→C2. On A4/V4 they induce either identity or inversion. On the U path, S4 has a unique quotient C2 and its automorphism action is trivial. Any isomorphism of B=7:3 to another such endpoint fixes its C3 quotient: its characteristic C7 kernel is sent to C7, and if generators x,y satisfy yxy⁻¹=x², an isomorphism sending x to x^t and yC7 to (yC7)^ε forces 2^ε=2 modulo 7, hence ε=1. Thus U path automorphisms cannot change the sign of β_j. After length-preserving permutations, the binary graph d=χe is unchanged, and the ternary graph β=Lα transforms only by independently changing the signs of the α_i coordinates. This proves necessity.

### Sufficiency and endpoint embeddings

All ordered pairs (D10,A4) in A5 are simultaneously Aut(A5)-conjugate. In the natural five-point action, A4 is a point stabilizer and D10 normalizes a Sylow C5 acting transitively on the five points. Fix points F5, take D10={x↦±x+b} and A4 the even permutations fixing 0. The odd permutation x↦2x normalizes both, fixes D10/C5, and inverts A4/V4. Applying it simultaneously to every edge of one T path realizes that path's independent column sign while commuting with τ and preserving all its strips.

All ordered pairs (S4,7:3) in U are simultaneously Aut(U)-conjugate. Under U=GL₃(2), the two S4 classes stabilize points and lines of the Fano plane and the graph automorphism exchanges them. A Sylow C7 acts regularly on each seven-element set because its nonidentity elements are irreducible in dimension three; its normalizer is 7:3. This proves the simultaneous endpoint transitivity. These subgroup and fusion identifications are inputs from the small-PSL₂ path argument cited in §1.

After path permutations, gauges, and these endpoint standardizations, the unique C2 quotient maps match automatically. The diagonal signs on the T columns are realized independently by the displayed A5 automorphisms; no U-row signs are needed. The resulting product of coordinate automorphisms commutes with τ, sends each full strip and both actual matrix equations to their target, and hence sends H to H'. It also preserves the anti-diagonal K. This gives the folder isomorphism and proves sufficiency.


## Splitting atoms and the exact-factorization obstruction (0030)

Here we work more generally with a canonical folder whose group is a product of paired nonabelian simple groups. The paired-section input gives the full anti-diagonal section. An **exact-factorization witness** is a normal subgroup N satisfying

```math
N\cap\tau(N)=1,\qquad [G:N]=|K|,\qquad HN\cap H\tau(N)=H. \tag{W}
```

The intrinsic criterion in §1 identifies existence of such a witness with membership in Nagy's exact-factorization construction. We now prove its graph formulation. In the following proof (*) denotes (W).

Let Ω be the set of the 2m simple coordinate factors. For A⊆Ω let π_A be the coordinate projection embedded back in G. Say A splits H when π_A(H)≤H. Then H=π_A(H)×π_{Ω\A}(H), so A splits iff its complement does. If A and B split, π_A and π_B preserve H; hence π_{A∩B}=π_Aπ_B preserves H. The splitting subsets form a finite Boolean algebra, whose atoms partition Ω into unique nonempty indecomposable blocks. A subset splits H exactly when it is a union of these atoms. Coordinates on which H projects trivially are included: they form singleton splitting atoms, and must not be discarded.

Form a multigraph Γ whose vertices are these atoms, with one edge for each τ-pair of simple coordinates, joining their respective atoms; loops and parallel edges are allowed. Then Q admits an intrinsic witness N for (*) if and only if Γ is bipartite. More precisely, all witnesses N correspond bijectively to proper two-colorings of Γ: select in N every coordinate belonging to an atom of one color. In particular, if Γ is loop-free and bipartite with c connected components, there are 2^c witnesses as actual subgroups; global color reversal gives τ(N) for N. The count is of witnesses, not of isomorphism classes of factorizations or loops.

Proof. Every normal subgroup of a direct product of nonabelian simple groups is a product of coordinate factors. If N satisfies N∩τN=1, it contains at most one coordinate of each τ-pair. Since [G:N]=|K| and |G|=|K|², |N|=|K|. Its order is at most the product of one |T_i| per pair, and equality forces exactly one from every pair, with no argument based on distribution of prime divisors. Consequently G=N×τN. Under this decomposition,

```text
HN∩HτN = π_N(H) × π_{τN}(H).
```

Thus the last equality in (*) holds exactly when the selected coordinate set splits H, equivalently is a union of atoms. Having exactly one coordinate per τ-pair means precisely that every edge of Γ joins atoms of opposite colors. Conversely every proper two-coloring selects such a normal N and verifies all three conditions in (*). A loop prohibits a coloring, so no witness exists in that case.

A canonical-folder isomorphism carries simple direct factors to simple direct factors, carries H to H′, and intertwines τ with τ′, so it sends splitting atoms to splitting atoms and preserves τ-edges. The graph up to isomorphism, its bipartiteness, and the set of witnesses are therefore loop-isomorphism invariants within the stated canonical model. Parallel edges record multiplicity of coordinate pairs. Independent reversal on connected components gives all colorings; whether different witnesses lead to isomorphic factorizations is not decided by the graph alone.

This result applies in particular to any mixed-type path folder once its H-splitting blocks have been computed from the actual stabilizer, including correlated endpoint groups. It would be invalid to infer the graph merely from a support picture that does not prove a direct-product decomposition of H. No claim is made here for its bipartiteness without that calculation.

## Isotopy invariance of the witness route

For every finite simple nonassociative Bol loop, not just the paired semisimple model, the existence of a witness for (*) is invariant under isotopy, subject to the principal-isotope interface in [the Bruck-isotopy source](../update-2026-11-16/manuscripts/exact-factorization-criterion.md#bruck-isotopy-as-a-stabilizer-conjugacy-test). Indeed a principal isotope has folder (G,H,k^-1K) with k∈K and canonical inversion τ_k=Inn(k^-1)τ. For any normal N◁G, τ_k(N)=τ(N); the cardinality of the section remains |K|, and H is unchanged. Hence all three conditions (*) hold for precisely the same normal subgroups N in both presentations. Every loop isotope is isomorphic to a principal isotope under the interface, so the exact-factorization membership characterized by (*) is isotopy invariant. This does not assert that the explicit factorizations or their parameterizations are the same. In the paired model, it follows in particular that failure of the bipartite test excludes every exact-factorization isotope. The shifted τ_k need not retain the original visible pair-swapping normal form, but normality makes the witness argument independent of that issue.



## Weighted-cycle test for the matrix family

Let T-path i have endpoints D_i,A_i and length a_i, and U-path j have endpoints S_j,B_j and length b_j. The actual endpoint subgroup is the full preimage of d=χe and β=Lα, in the notation of the matrix theorem; its directed bipartite support graph is strongly connected.

Form an undirected graph X on the D_i and S_j endpoint coordinates with edge D_i—S_j iff χ_ij≠0. Separately form Y on A_i and B_j with edge A_i—B_j iff L_ji≠0. Strong connectivity makes every endpoint vertex incident to an edge. The splitting atoms of H are exactly: each connected component of X, each connected component of Y, and each independent internal full simple strip.

Indeed the χ and L equations involve disjoint coordinate groups, and each equation system is a direct product across its support components; internal strips are independent. Conversely, if a splitting coordinate subset cut a nonzero χ edge D_i—S_j, then replacing an actual element of H by its projection to one side would turn an element with an independently chosen e_j=1 into a tuple violating d_i=Σχ_ij e_j. The other equations remain soluble because all endpoint kernels are present and the χ variables are independent. The same projection test for α_i and β_j with L_ji≠0 excludes cutting any Y edge. A full diagonal strip cannot split between its two nontrivial coordinate projections. Thus no support component or strip splits further; there is no hidden cancellation of graph coefficients.

Contract each full path to a single edge between the X-component containing its D or S endpoint and the Y-component containing its A or B endpoint. Denote the resulting bipartite multigraph by Γ₀; its edge for T path i carries parity a_i mod2 and for U path j carries b_j mod2. The splitting-atom witness theorem says an exact-factorization witness exists precisely when there are colors c(v)∈F₂ satisfying

```text
c(X_i)+c(Y_i)=a_i (mod 2),       c(X_j)+c(Y_j)=b_j (mod 2).          (1)
```

Indeed expanding a contracted edge into its full path replaces its condition by opposite colors along every original τ-pair edge; its internal strip atoms force adjacent incidences at each internal vertex to share a color. Equation (1) is solvable exactly when the xor of edge parities around every cycle of Γ₀ is zero, including parallel-edge cycles.

Strong directed support makes Γ₀ connected. More strongly, orient its T-path edges from their Y-atoms to X-atoms and its U-path edges from X-atoms to Y-atoms. Each original directed support arc T_i→U_j from χ gives a directed transition from edge i to edge j at their common X vertex; each U_j→T_i from L gives one at their common Y vertex. Strong connectivity of the original directed graph places every path edge in a directed closed walk of Γ₀, and any two such edges in the same connected component. Thus the oriented Γ₀ is strongly connected on its nonisolated vertices, and every edge lies in a cycle; in particular Γ₀ has no bridge. This is a necessary consequence of the matrix strong-connectivity hypothesis, not a general statement about arbitrary paired-folder atom graphs.

Therefore (1) has either zero or exactly two solutions: the connected graph has two global color choices if consistent. By the theorem these are exactly the two actual witness subgroups N,τN, not a count of loop or factorization isomorphism types. If (1) is inconsistent, no exact-factorization isotope exists by the separate isotope-invariance result. When m=n=1 and χ,L are both nonzero, Γ₀ has two parallel edges, and the condition reduces to a₁≡b₁ mod2, recovering the two-path family.

No projected subgroup has been assumed to define a quotient folder. These conclusions remain restricted to the paired matrix model.



## The two-path family (0029)

Take one T path of length A and one U path of length B, χ=(1) and L=(1). Their directed support is strongly connected, so the classification theorem constructs a simple proper loop of order `60^A 168^B`. The endpoint equations are the two fiber products D₁₀×_{C₂}S₄ and A₄×_{C₃}(7:3). These and the internal strips are exactly the splitting atoms.

The atom graph is a cycle of length A+B, allowing the two parallel edges when A=B=1. It is bipartite if and only if A+B is even, equivalently A≡B modulo 2. The witness theorem and its isotope invariance give the claimed exact-factorization boundary. In the same-parity case, the two colors split H as H₀×H₁ inside N×N, where N=T^A×U^B. Collision-freeness gives H₀∩H₁=1 after the coordinate identifications, and the order equation gives N=H₀H₁: this supplies the actual exact group factorization. In opposite parity there is no witness, even after isotopy.

At fixed A,B the nonzero ternary scalar is unique up to the permitted T-column sign. All endpoint embeddings, strip twists and coordinate orientations are removed by the isomorphism proof above. Thus the family has one isomorphism class for each ordered pair (A,B); different pairs have different multiplicities of the two simple factors in their canonical groups. This does not assert that arbitrary loops with those canonical groups belong to this two-path subfamily.

## Open problems and scope

1. **Other simple types.** For prescribed nonabelian simple groups T and U, determine which endpoint quotient groups can couple the path components and whether a finite collection of matrix or module data classifies the paired model.
2. **Beyond pair swapping.** Classify canonical folders with the same simple factors but an inverting automorphism not conjugate to the paired exchange action. The present exhaustion theorem does not cover these.
3. **G-loop status.** Determine the full isotope-to-isomorphism relation for the opposite-parity two-path family. The witness obstruction only excludes exact-factorization isotopes; it does not settle whether all isotopes are isomorphic to the original loop.
4. **General splitting graphs.** Determine which connected multigraphs arise as stabilizer splitting-atom graphs of simple paired folders. The matrix family has no bridges, but this does not establish a bridge exclusion for every paired folder.

Nontrivial radicals and arbitrary semisimple extensions remain outside this classification. The graph criterion recognizes a construction route, not every Bol loop. None of these statements establishes a general efficient enumeration theorem.

## References and source proofs

- [Research references](../REFERENCES.md), including Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Appendix Theorem A.1 and Lemmas A.2–A.3, and Nagy's exact-factorization construction.
- [Matrix classification source](../update-2026-11-16/manuscripts/radical-free-mixed-matrix-classification.md): exhaustion, stabilizer equations, all-coordinate simplicity, exact isomorphism law and weighted-cycle test.
- [Two-path construction source](../update-2026-11-16/manuscripts/radical-free-mixed-paths.md): explicit construction, parity boundary and endpoint-embedding calculation.
- [Splitting-atom source](../update-2026-11-16/manuscripts/radical-free-bipartite-witness.md): witness/coloring correspondence and isotope invariance.

The numbered exposition consolidates these proofs by mathematical dependency rather than their order of discovery. The input lemmas in §1 remain necessary dependencies.
