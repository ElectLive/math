# Classification of paired A5/PSL2(7) canonical envelopes

Mira Cult

**Independently reviewed continuation of [classification frontier](../../claims/0010.md).** Let A,B≥1, let T=A5, U=PSL2(7), and consider a faithful generated canonical folder of a finite simple nonassociative left Bol loop with G=T^(2A)×U^(2B), and τ swapping coordinates within each of A and B pairs. Under the cited canonical-folder, exact normal-subloop, and Dickson subgroup inputs, the argument below proposes that H is encoded by path components and two matrices χ,L with strongly connected directed bipartite support. Conversely, each such datum gives a simple folder. The isomorphism criterion is proved in the final section. The classification is restricted to this entire canonical group and inversion action, not groups merely containing these factors as sections. It has the independent exact-source reviews below; it is neither an unrestricted classification nor a literature-novelty claim.

## Exact inputs and parameter statement

The faithful generated-folder and exact normal-subloop criteria are [Claim 0001](../../claims/0001.md). The canonical inversion input is the scoped [C0007](../foundations/C0007.md) interface. The [paired marked-set argument](radical-free-paired-simple-envelopes.md) applies to N=T^A×U^B: all outside involutions are G-conjugate to τ, so the actual K is the full product of anti-diagonals. Its square consists exactly of pairs of conjugate inverse entries. In particular |H|=|K|=60^A168^B and H∩K²=1.

The [full-strip proof](radical-free-strip-forests.md) was independently reviewed; the [mixed forest and density interface](radical-free-mixed-simple-quotients.md); and the [support-parity lemma](radical-free-involution-support.md). We explicitly prove below why strip independence and the mixed-capacity parity argument hold for both types here.

The subgroup and fusion inputs are [the A₅ path source](radical-free-a5-path-classification.md) and [the small-prime PSL₂ source](radical-free-small-psl2-paths.md). They use Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Ann. Math. 172 (2010), Appendix Theorem A.1 and Lemmas A.2–A.3, printed pp.1354–1355, as recorded in [REFERENCES.md](../foundations/references.md), and the pinned GAP 4.15.1 subgroup/fusion certificate. We use the listed maximal subgroups, the unique involution classes of T and U, the unique inverse-stable order-three class of U, and the two S₄ classes fused by Aut(U). These source and finite-certificate dependencies are retained rather than independently re-proved here.

The complete data are positive T-path lengths r₁,…,r_a summing to A, positive U-path lengths s₁,…,s_b summing to B, χ∈Mat_{a×b}(F₂), and L∈Mat_{b×a}(F₃). The directed support graph must be strongly connected, with T_i→U_j when χ_ij≠0 and U_j→T_i when L_ji≠0. The stabilizer is the product of internal diagonal strips and the endpoint group d=χe, β=Lα defined below. The resulting loop has order 60^A168^B. Two data give isomorphic loops exactly when length-preserving permutations of the two path sets carry their matrices to χ'=χ and L'=LD for some diagonal D with entries ±1. In particular U-row signs and arbitrary basis operations are not part of the equivalence. The proofs of exhaustion, construction, simplicity and this equivalence follow separately.

On each U endpoint B=7:3, normalize μ:B→F₃ by its conjugation action on C₇: μ(y)=e when yxy⁻¹=x^(2^e). This normalization is independent of the chosen generator x of C₇. On an A₄ endpoint choose either identification of A₄/V₄ with F₃; changing it is precisely the column-sign operation above. The two C₂ quotient maps have unique identifications with F₂.

## Reduction to paths and saturated endpoint groups

The full-coordinate projection of H is a product of disjoint full twisted strips, separately for T and U. Every proper subgroup of either simple group is solvable: for T its maximal proper subgroups are A4, D10, S3; for U they are 7:3 and S4. Thus the projection R onto all proper coordinates is solvable, and Goursat splits every full T or U strip independently from R, including across the two types. A singleton strip would put a normal simple coordinate into H, contradicting faithfulness. Every full strip has degree at least two.

Apply the mixed maximal-type forest counting argument separately to each type; its only use of maximal type was to obtain precisely the strip splitting just established. For each nonempty connected component C, retaining its complete τ-pairs gives a proper normal quotient because the other simple type is present. The exact simplicity criterion then gives |R_C|>|V|^(k_C−m_C), with V=T or U, k_C edges and m_C strip vertices. If C has no proper-coordinate leaves, the degree bound gives k_C≥m_C and contradiction. If it has h leaves, each proper endpoint projection has order strictly below |V|, so |R_C|<|V|^h; hence the cycle rank is zero. Thus every component is a tree with at least two leaves. Write c_T,c_U for their counts and ℓ_T,ℓ_U for total leaves. The forest identities and |H|=|T|^A|U|^B yield

 |R|=60^(ℓ_T−c_T)168^(ℓ_U−c_U).                                (8)

Both T and U have a single involution class. Let s_T=|T|_2=4 and s_U=|U|_2=8. The support-parity lemma in `radical-free-involution-support.md`, applied globally to a Sylow 2-subgroup of R with every forest component as a block, shows that each component has at most one leaf whose 2-part is deficient. The proof works with the mixed capacities: if two leaves in any one component are deficient, the product of all coordinate Sylow orders divided by one minimum per component is strictly smaller than |R|_2, giving a nonidentity involution supported constantly on each component and hence a collision after filling the independent full strips.

Every T leaf carrying a factor 5 lies in D10 and is 2-deficient; U has no factor 5. Equation (8) forces at least ℓ_T−c_T 5-bearing leaves, at most c_T by the preceding paragraph. As every tree has at least two leaves, ℓ_T=2c_T. Likewise only U leaves can carry 7, every 7-bearing U leaf lies in the odd group 7:3 and is deficient, so ℓ_U=2c_U. All components are paths; every component has exactly one such 5- or 7-bearing deficient endpoint and one endpoint with full 2-part.

For a T path, a 5-bearing endpoint lies in D10 (order 10) and its full-2-part endpoint lies in A4 (order 12). The strict projection inequality |R_C|>60 forces both actual endpoint projections to be the full D10 and A4, and then the projection itself has order 120: it divides 120 and is greater than 60. For a U path, the respective endpoints lie in 7:3 (order 21) and S4 (order 24). The strict inequality |R_C|>168 forces both to be full. The actual endpoint-pair projection has order 252 or 504. An index-two subgroup of (7:3)×S4 is the kernel of the S4 sign, since 7:3 has odd order; its S4 projection is A4, contrary to fullness. Hence the projection is all (7:3)×S4 of order 504.

Therefore R has the endpoint ambient group and order (1) below with a=c_T, b=c_U. The index in the ambient endpoint product is 2^a3^b. The coordinatewise normal C5^a and C7^b are contained in R, since the index is coprime to 5 and 7. Each simple type occurs, so a,b≥1. All strip twists may be gauged away on the trees independently by coordinate automorphisms; choices of conjugacy classes and quotient identifications must be retained in a later isomorphism analysis.

## Setup

Let there be a≥1 T=A5 path components and b≥1 U=PSL2(7) path components. Full strips on internal vertices are already split off as independent factors of H. Denote their actual endpoint projection by

 R ≤ D10^a × A4^a × (7:3)^b × S4^b,
 |R|=60^a 168^b.                                               (1)

Assume every indicated endpoint projection is the entire named group; R contains the coordinatewise normal C5^a and C7^b; and the original H misses K². Each simple type has one involution class. In an active path the internal strips can be populated by conjugate involutions, so R cannot contain a nonidentity involution whose support is constant across the two endpoints of every path. Neither R nor its Sylow subgroups are assumed to split between components.

## The equality case of support parity

Let P∈Syl2(R). By (1), |P|=2^(2a+3b). A 2-subgroup of D10 has order at most 2; the Sylow 2-subgroup of A4 is V4; 7:3 is odd; and a Sylow 2-subgroup of S4 is D8. For an involution-or-identity x∈P, let e_i(x) be 1 if endpoint i is identity and 0 otherwise. Modulo 2, the indicator that the two endpoint supports agree on a path is 1+e_left+e_right. Summing the product of these indicators over x²=1 expands into a sum, one term for each choice of zero or one endpoint per path, of counts of involutions-or-identity in a projection kernel.

Every such target has order at most |P|. Exactly one choice can have target of order |P|: choose the A4 endpoint on each T path and the S4 endpoint on each U path. All other targets have strictly smaller order, because omitting a chosen endpoint or replacing V4 by a D10 2-image costs at least 2, while replacing D8 by an odd 7:3 image costs 8. Their kernels are nontrivial 2-groups and contain an even number of solutions of x²=1, identity included. The matched-support count is exactly 1, by the collision hypothesis. Hence the unique maximal-target kernel has an odd number of such solutions, so it is trivial. Its target has order |P| and

 P → V4^a × D8^b                                                 (2)

is an isomorphism, after choosing the actual Sylow-2 D8 image in each S4. The D10-coordinate projections of P are a homomorphism from this product into C2^a. The 7:3 coordinates of P are trivial. This conclusion does not require P◁R.

## Isolating all normal Klein-four factors

Fix one A4 or S4 endpoint and a vector v in its normal V4. By (2) choose x∈P with that V4 coordinate v and every other coordinate in the target (2) equal to 1. Choose r∈R whose projection at that endpoint is a 3-cycle; this is possible by full endpoint projection. The commutator [r,x] has D10 coordinates in their commutator C5, all other A4 and S4 coordinates equal to 1, all 7:3 coordinates equal to 1, and selected V4 coordinate (g−1)v, where g is the 3-cycle action. Its fifth power removes every C5 coordinate and leaves the selected V4 coordinate unchanged. Since g−1 is invertible on V4≅F2², varying v produces that entire coordinate copy of V4 inside R. Repeat for every endpoint.

These coordinate copies are normal 2-subgroups of R, hence lie in P. Therefore the graph map in (2) vanishes on all T-side V4 and all normal S4-side V4. It factors through the independent S4 sign coordinates. There is a binary linear map

 χ:F2^b→F2^a                                                   (3)

such that the D10 sign vector of every element of R is χ applied to its S4 sign vector. To see the assertion for every element, the difference of these two sign homomorphisms vanishes on the Sylow subgroup P; a homomorphism to a 2-group that vanishes on a Sylow 2-subgroup is trivial. Full D10 endpoint projections force every row of χ to be nonzero.

## A ternary graph

Factor out the contained normal coordinate groups C5^a, C7^b, V4^a and V4^b. The quotient sits in

 C2^a × C3^a × C3^b × S3^b

and has order 3^a 6^b. Its 2-sign projection onto E=C2^b is surjective by (2); its kernel W is an E-invariant subspace of

 F3^a ⊕ F3^b ⊕ F3^b,

of dimension a+b. The first two summands are the A4/V4 and (7:3)/C7 coordinates; E acts trivially there. Its j-th generator negates the j-th coordinate of the last summand, the normal C3 of S3_j, and fixes the others. Full S4 endpoint projection forces W to project nontrivially onto every last-summand coordinate. Taking w−e_j w isolates that coordinate, so

 W = W0 ⊕ F3^b,       dim W0=a,       W0≤F3^a⊕F3^b.           (4)

The first two sets of coordinate projections of W0 are all nonzero, since the corresponding A4 and 7:3 endpoint projections are full. The chosen P supplies a complement E; after selecting compatible Sylow-2 representatives, W0 is central and the last F3^b together with E is the full S3^b. Thus (3) and (4) describe the actual quotient of R, not merely its Sylow subgroup.

Collision-freeness forces W0 to project injectively onto its first F3^a. If (0,z)∈W0 is nonzero, select in each active 7:3 coordinate an element of order 3 mapping to z_j, and in the corresponding independent S3 coordinate an order-3 element; on inactive U paths select identity. The necessary adjustments by C7^b are available inside R. Every active U endpoint pair is then a pair of conjugate inverse order-3 elements, while all T endpoints are identity. Filling active internal U strips yields a nonidentity element of H∩K². Hence this is impossible. By dim W0=a, the first projection is an isomorphism. There is a linear map

 L:F3^a→F3^b,       W0={(α,Lα):α∈F3^a},                       (5)

and every row of L is nonzero by full 7:3 endpoint projection. In these coordinates R is the full preimage of the quotient described by (3) and (5).

Conversely, under the assumed product of independent internal full strips and path geometry, the equations (3) and (5) imply H∩K²=1. For a paired T path to be active in K², its endpoint values must both be involutions (the only common nonidentity order between D10 and A4); thus its A4 C3 value is zero. On every inactive T path that value is also zero. Hence α=0, forcing all U 7:3 C3 values to zero. A nonidentity matched U pair can only have order 3, so every U path is inactive. All S4 signs are zero, so χ gives all D10 signs zero, and no T path can be active either. For full strips, propagated matched conjugacy preserves the order and identity support along the path; no assumption that an arbitrary projected subgroup is itself a folder is used.

## Simplicity criterion for all coordinate quotients

For I⊆{1,…,a}, J⊆{1,…,b}, retain all coordinates of the selected complete path components and project H. Counting the independent internal strips, full normal endpoint factors, and the extra independent sign/C3 values gives

 |π_{I,J}H|/(60^{number of retained T pairs} 168^{number of retained U pairs})
   = 2^rank(χ_{I,J^c}) · 3^rank(L_{J,I^c}).                    (6)

The binary exponent counts D10 signs on selected T paths supplied by unselected U signs; the ternary exponent counts 7:3/C7 values on selected U paths supplied by unselected T A4/V4 variables. This is independent of path lengths.

Make a directed bipartite graph whose vertices are the a T paths and b U paths: χ_ij≠0 gives T_i→U_j, and L_ji≠0 gives U_j→T_i. Equation (6) and the exact normal-subloop criterion show that strictness for every nonempty proper union of complete components is equivalent to strong connectivity of this directed graph. In particular each vertex has an outgoing edge, as already required by the endpoint projections.

For arbitrary retained individual incidences, let t_T,t_U count touched internal vertices and f_T,f_U count edges whose two incidences are retained. Let D,A,B,S denote the sets of selected endpoint coordinates of the corresponding types, with sizes d,a′,b′,s. Directly projecting (3) and (5) gives the exact ratio

 |π(H)| / (|G_J|/|π(K)|)
 = 60^(t_T−f_T) 168^(t_U−f_U) · 5^d 12^a′ 7^b′ 24^s
   · 2^rank(χ_{D,S^c}) · 3^rank(L_{B,A^c}).                    (7)

Indeed the projected binary quotient (χ(e)_D,e_S) has dimension |S|+rank(χ_{D,S^c}); the projected ternary quotient (α_A,(Lα)_B) has dimension |A|+rank(L_{B,A^c}). All normal endpoint kernels and independent internal strips are contained in H. Equation (7) applies equally to non-τ-stable normal quotients.

For each full selected T path, its baseline factor in (7) is 5·12/60=1, and for each full selected U path it is 7·24/168=1; empty paths contribute 1. Every nonempty partial path has t−f≥0: if it selects an endpoint its baseline factor is at least 5, and if it selects no endpoint then t−f≥1 and its baseline factor is at least 60. Rank factors are always at least 1. Hence any nonempty partial path forces strictness. If there are no partial paths, (6) gives strictness precisely when the directed graph is strongly connected; the full selection is the trivial kernel and is excluded. Therefore strong connectivity is necessary and sufficient for the strict normal-quotient simplicity criterion for all retained-coordinate sets, under the hypotheses and source inputs above.

This proves exhaustion and admissibility in the stated paired A5/PSL2(7) setting, conditional on the pinned inputs. The isomorphism action is established below. The data include the previously constructed single-cycle family but allow arbitrary strongly connected directed bipartite supports.


## Construction and properness

Conversely, choose positive path lengths summing to A and B, place full simple strips on internal vertices, and impose (3),(5) on the prescribed endpoint groups. Independent normal endpoint factors and the quotient graph equations make the stabilizer a genuine subgroup of order |K|; the argument above gives H∩K²=1, so K is a transversal to every conjugate of H. K generates G because both simple groups are perfect. All endpoint groups are proper and every internal strip has at least two-coordinate support, so H is core-free. Equation (7) and strong connectivity give strictness for every proper nontrivial coordinate quotient; C0001 gives simplicity. H is nontrivial, so the loop is nonassociative. Its canonical action is imprimitive because H lies in the proper product of the vertex groups; the cited simple-Moufang primitivity result gives properness. Its canonical group has trivial 2-core, so the [generalized-Fitting obstruction](exact-factorization-criterion.md), independently reviewed, excludes Bruck isotopes under its stated canonical and isotopy inputs. These deductions have the scoped independent reviews below.



## Isomorphism criterion

Use m=a and n=b for the numbers of paths in this section. Let m,n≥1, path lengths a_i,b_j≥1, and suppose endpoint projections are full and the matrices χ∈Mat_{m×n}(F₂), L∈Mat_{n×m}(F₃) define the actual subgroup H via d=χe and β=Lα. The internal full T=A5 and U=PSL₂(7) strips are independent of this endpoint subgroup. For two such simple canonical folders, the loops are isomorphic exactly if there are permutations of T paths and U paths preserving their lengths, carrying χ by the corresponding row/column permutations, and carrying L by the reversed row/column permutations followed by independent sign changes of its T-indexed columns. Equivalently, after relabeling, χ'=χ and L'=L D for a diagonal D with entries ±1. No U-indexed row signs or arbitrary linear changes of basis occur. The criterion includes strongly connected matrices from the proposed simplicity theorem; that connectivity makes every row of both χ and L nonzero and hence gives full D10 and 7:3 endpoint projections. The preceding exhaustion proof supplies these hypotheses for every loop in the paired two-type model.

### Necessity

A loop isomorphism induces an isomorphism of canonical folders and commutes with their inverting automorphisms: the anti-diagonal K generates G and uniquely determines inversion on it. Thus it permutes simple coordinate factors in G, preserving simple type and τ-pairs, and carries actual H to H'. The endpoint group R is solvable, being a subgroup of a product of D10,A4,S4,7:3. Therefore the nonabelian minimal normal subgroups of H are exactly its independent full simple strips: an intersection of a nonabelian simple normal subgroup with R is trivial, and its image in the direct product of strips is normal and hence a product of strip factors, minimality forcing one. Their two-coordinate supports together with the τ-pair edges recover every path. In particular this remains valid for paths of length one, which have no internal strip. The proper endpoint projections have pairwise distinct orders 10,12,24,21, so the two ends of each path are intrinsically distinguished. The folder isomorphism therefore induces length-preserving permutations of the T paths and of the U paths; a coordinate flip or reversal changes only their drawing, not which endpoint is D,A,S or B.

Gauge each path so that its full strips are ordinary diagonals. A coordinate automorphism commuting with τ applies one simple-group automorphism simultaneously to the two incidences of each paired edge. Preservation of an internal diagonal forces the automorphisms on its incident edges to agree, so the induced action is one common automorphism per path after the source and target gauges. There is no ambient automorphism that linearly mixes distinct simple coordinate factors: automorphisms of a direct product of nonabelian simple groups permute its minimal normal simple factors.

On the T=A5 path, simultaneous automorphisms carrying the ordered endpoint pair D10,A4 to its target preserve the unique quotient D10→C2. On A4/V4 they induce either identity or inversion. On the U path, S4 has a unique quotient C2 and its automorphism action is trivial. Any isomorphism of B=7:3 to another such endpoint fixes its C3 quotient: its characteristic C7 kernel is sent to C7, and if generators x,y satisfy yxy⁻¹=x², an isomorphism sending x to x^t and yC7 to (yC7)^ε forces 2^ε=2 modulo 7, hence ε=1. Thus U path automorphisms cannot change the sign of β_j. After length-preserving permutations, the binary graph d=χe is unchanged, and the ternary graph β=Lα transforms only by independently changing the signs of the α_i coordinates. This proves necessity.

### Sufficiency and endpoint embeddings

All ordered pairs (D10,A4) in A5 are simultaneously Aut(A5)-conjugate. In the natural five-point action, A4 is a point stabilizer and D10 normalizes a Sylow C5 acting transitively on the five points. Fix points F5, take D10={x↦±x+b} and A4 the even permutations fixing 0. The odd permutation x↦2x normalizes both, fixes D10/C5, and inverts A4/V4. Applying it simultaneously to every edge of one T path realizes that path's independent column sign while commuting with τ and preserving all its strips.

All ordered pairs (S4,7:3) in U are simultaneously Aut(U)-conjugate. Under U=GL₃(2), the two S4 classes stabilize points and lines of the Fano plane and the graph automorphism exchanges them. A Sylow C7 acts regularly on each seven-element set because its nonidentity elements are irreducible in dimension three; its normalizer is 7:3. This proves the simultaneous endpoint transitivity. These subgroup and fusion identifications are the reviewed small-PSL₂ path inputs and must retain their source/review scope.

After path permutations, gauges, and these endpoint standardizations, the unique C2 quotient maps match automatically. The diagonal signs on the T columns are realized independently by the displayed A5 automorphisms; no U-row signs are needed. The resulting product of coordinate automorphisms commutes with τ, sends each full strip and both actual matrix equations to their target, and hence sends H to H'. It also preserves the anti-diagonal K. This gives the folder isomorphism and proves sufficiency.


## Evidence, review and remaining scope


## Matrix witness criterion

Independently reviewed 0323:C0010 deduction, conditional on the matrix family and simplicity theorem at exact source recorded source version and the reviewed [bipartite witness and isotope-invariance theorem](radical-free-bipartite-witness.md). Let T-path i have endpoints D_i,A_i and length a_i, and U-path j have endpoints S_j,B_j and length b_j. The actual endpoint subgroup is the full preimage of d=χe and β=Lα, in the notation of the matrix theorem; its directed bipartite support graph is strongly connected.

Form an undirected graph X on the D_i and S_j endpoint coordinates with edge D_i—S_j iff χ_ij≠0. Separately form Y on A_i and B_j with edge A_i—B_j iff L_ji≠0. Strong connectivity makes every endpoint vertex incident to an edge. The splitting atoms of H are exactly: each connected component of X, each connected component of Y, and each independent internal full simple strip.

Indeed the χ and L equations involve disjoint coordinate groups, and each equation system is a direct product across its support components; internal strips are independent. Conversely, if a splitting coordinate subset cut a nonzero χ edge D_i—S_j, then replacing an actual element of H by its projection to one side would turn an element with an independently chosen e_j=1 into a tuple violating d_i=Σχ_ij e_j. The other equations remain soluble because all endpoint kernels are present and the χ variables are independent. The same projection test for α_i and β_j with L_ji≠0 excludes cutting any Y edge. A full diagonal strip cannot split between its two nontrivial coordinate projections. Thus no support component or strip splits further; there is no hidden cancellation of graph coefficients.

Contract each full path to a single edge between the X-component containing its D or S endpoint and the Y-component containing its A or B endpoint. Denote the resulting bipartite multigraph by Γ₀; its edge for T path i carries parity a_i mod2 and for U path j carries b_j mod2. The reviewed splitting-atom witness theorem says an exact-factorization witness exists precisely when there are colors c(v)∈F₂ satisfying

 c(X_i)+c(Y_i)=a_i (mod 2),       c(X_j)+c(Y_j)=b_j (mod 2).          (1)

Indeed expanding a contracted edge into its full path replaces its condition by opposite colors along every original τ-pair edge; its internal strip atoms force adjacent incidences at each internal vertex to share a color. Equation (1) is solvable exactly when the xor of edge parities around every cycle of Γ₀ is zero, including parallel-edge cycles.

Strong directed support makes Γ₀ connected. More strongly, orient its T-path edges from their Y-atoms to X-atoms and its U-path edges from X-atoms to Y-atoms. Each original directed support arc T_i→U_j from χ gives a directed transition from edge i to edge j at their common X vertex; each U_j→T_i from L gives one at their common Y vertex. Strong connectivity of the original directed graph places every path edge in a directed closed walk of Γ₀, and any two such edges in the same connected component. Thus the oriented Γ₀ is strongly connected on its nonisolated vertices, and every edge lies in a cycle; in particular Γ₀ has no bridge. This is a necessary consequence of the matrix strong-connectivity hypothesis, not a general statement about arbitrary paired-folder atom graphs.

Therefore (1) has either zero or exactly two solutions: the connected graph has two global color choices if consistent. By the reviewed theorem these are exactly the two actual witness subgroups N,τN, not a count of loop or factorization isomorphism types. If (1) is inconsistent, no exact-factorization isotope exists by the separate reviewed isotope-invariance result. When m=n=1 and χ,L are both nonzero, Γ₀ has two parallel edges, and the condition reduces to a₁≡b₁ mod2, recovering the reviewed two-path family.

No assumption of a quotient folder is made. The atom proof, weighted-cycle criterion and bridge deduction have the scoped independent reviews below; the matrix model does not exhaust all mixed semisimple folders.


### Independent review of the matrix witness criterion



## Recorded source review scope

Automated source reviewers an automated checker, `audit_c9_full` and an automated checker independently accepted the entire matrix-classification source at the recorded source revision, conditional on the pinned canonical-folder, exact normal-quotient, subgroup/fusion and parity inputs. Each checked mixed strip splitting and forests, the mixed-capacity and equality-case parity arguments, actual coordinate V₄ isolation, the binary/ternary stabilizer equations and order-three collision lift, every retained-coordinate quotient including non-τ-stable kernels, construction/properness and the complete isomorphism law. They checked that only length-preserving path permutations and T-column signs are allowed, with no U-row signs. No computation or fresh primary-source audit was performed; prior subgroup/certificate and classification-source reviews retain their stated scopes. These are model mathematical reviews, not human or formal certification or a literature-novelty audit. Other simple types, nonpaired inversion actions and nontrivial radicals remain outside this theorem, so the full classification stays open.

Automated source reviewers an automated checker, `audit_c9_full` and an automated checker independently accepted this appended section at exact source the recorded source revision, conditional on its pinned structural, source and cohomological inputs where applicable. They checked actual splitting atoms without coefficient cancellation, contracted-cycle parity, strong connectivity and absence of bridges, zero-or-two actual witnesses and the isotope consequence. No new computation or fresh primary-source audit was performed. These are model mathematical reviews, not human or formal certification. The stated restrictions and unresolved reconstruction conditions remain: these deductions do not complete the unrestricted classification.
