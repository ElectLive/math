# Mixed paired simple factors: quotient restrictions and a construction

**Mira Cult**

Independently reviewed investigation for [0323:C0010](../../claims/0010.md), using the [paired-envelope](radical-free-paired-simple-envelopes.md) and [full-strip forest](radical-free-strip-forests.md) interfaces, independently reviewed respectively at [the source revision](https://github.com/Mira-Cult/math-wip/commit/4c93742a59ccdd786f23598f0374f674c6f75fff) and [the source revision](https://github.com/Mira-Cult/math-wip/commit/6d3a97daa9cf20bbae0416295c8c2374c2cd8ede). The restrictions and the final mixed-type simple-folder construction have independent exact-source reviews recorded below. No mixed-type classification is claimed. The canonical-folder transversality and normal-subloop criterion are dependencies; the maximal-strip argument uses only elementary subgroup theory.

## Precise two-type consequence of simplicity

Let X and Y be nonisomorphic finite nonabelian simple groups, let N_X=X^k and N_Y=Y^l for k,l≥1, and put N=N_X×N_Y, G=N×N, K={(n,n^-1):n∈N}. Let H≤G have |H|=|N| and H∩K²=1, and suppose the resulting faithful generated canonical folder defines a simple loop. Write G=G_X×G_Y with G_X=N_X², G_Y=N_Y² and n_X=|N_X|, n_Y=|N_Y|. Let H_X,H_Y be the projections of H.

Then:

1. |H_X|>n_X and |H_Y|>n_Y. Indeed, retaining one full type block is a nontrivial proper normal quotient, the K-image has size n_X or n_Y, and the exact simplicity criterion makes the quotient stabilizer index strictly smaller than this size. Equivalently |H_X|>n_X, and similarly for Y.
2. By Goursat there are surjections α:H_X→C and β:H_Y→C with H={(a,b):α(a)=β(b)} and
   |C|=|H_X||H_Y|/(n_X n_Y)>1.
   Thus the two actual projections necessarily have a **nontrivial common quotient**. In particular, if one is perfect and the other solvable, no such simple folder exists. More generally it suffices to rule out every common nontrivial quotient of the two actual projections. This conclusion does not require the isotypic projections to be folders or simple loops.
3. Let Λ_X²=K_X² and Λ_Y²=K_Y², and define
   S_X=α(H_X∩Λ_X²),   S_Y=β(H_Y∩Λ_Y²).
   The collision condition is exactly S_X∩S_Y={1} together with (ker α)∩Λ_X²=(ker β)∩Λ_Y²={1}. These two kernel conditions cannot be omitted: the identity in a common image can have a nonidentity lift in the marked square. Conversely, those three tests force H∩K²=1 since K²=Λ_X²×Λ_Y².
4. Necessarily |ker α|≤n_X and |ker β|≤n_Y: their intersections with the corresponding marked square are trivial, so K_X and K_Y inject into their left-coset sets. Also each H_X and H_Y has at least one nonidentity marked-square element, since otherwise the same injectivity would imply its order at most n_X or n_Y. Their common-quotient images are nonidentity by the kernel condition. The residual problem is therefore to rule out disjoint nonidentity collision-image subsets of a nontrivial common quotient, with all actual subgroup constraints retained.

For three or more types, the first item remains valid for every nonempty proper union of types, but pairwise projections need not be subdirect products over one common quotient with all correlations captured. The same Goursat calculation applies to any chosen bipartition of the type set. It shows that the two actual block projections on either side of every bipartition have a nontrivial common quotient.

## What maximal-order splitting does and does not prove

Let T be a simple type of maximal group order among the distinct simple types, and consider the coordinates whose H-projection is all of T. Their combined projection is a product of disjoint full twisted T-strips, by the same subdirect-product argument as the strip-forest manuscript. Let R be H's projection onto all remaining coordinates, including all smaller-type coordinates and proper T-projections. No composition factor of R is isomorphic to T: filter the product projection by successive coordinate kernels. Each factor is a subquotient of a proper subgroup of T or of a distinct simple type of order at most |T|; even if that type has the same order as T, a section isomorphic to T would force the groups themselves to be isomorphic. Therefore R has no quotient T. Goursat splits these maximal-type full strips from R inside H. Faithfulness rules out singleton full strips.

This argument cannot be repeated indiscriminately for a smaller type S: a proper subgroup of T can have S as a section. In particular A5 embeds as a point stabilizer in A6. A full A5 strip may be tied to that proper A6 coordinate and need not occur as a direct subgroup of H.

There is also a strict maximal-type forest restriction. Treat the full maximal-T strips as vertices and each proper T-coordinate as a leaf; τ-pairs of T-coordinates are edges, including possible loops. For a connected component C, retain exactly its complete T-coordinate pairs and quotient out every other coordinate. Because at least one other isomorphism type occurs, this is always a proper nontrivial quotient even if C contains all T-pairs. If C has k_C edges, m_C full-strip vertices and proper-coordinate leaf projection R_C, simplicity yields

    |R_C| > |T|^(k_C-m_C).                                    (*)

Maximal-type splitting makes the projected stabilizer order exactly |T|^m_C |R_C|. If C has no leaves then k_C≥m_C because its strip vertices have degree at least two, contradicting (*). If it has h>0 leaves, each proper projection has order <|T|, so |R_C|<|T|^h. Combining with (*) yields k_C−m_C<h; the connected graph cycle rank k_C−m_C−h+1 is zero. Thus C is a tree with h≥2 leaves, and the inequality strengthens to |R_C|>|T|^(h−1) for **every** component, including when there is only one maximal-type component. This does not split R_C from the smaller types, and it gives no forest theorem for their full strips without extra hypotheses.

## Explicit order-correct coupling that fails the folder test

Take T=A6, S=A5 as its natural point stabilizer, and choose a proper subgroup B≅3²:4 of A6 of order 36 (the maximal-subgroup input is recorded with its ATLAS and GAP caveats in [the parity manuscript](radical-free-involution-support.md#paired-psl9-exclusion)). Let i:S→T be the inclusion and use paired coordinates

    G=S² × T⁴,     τ=(12)(34)(56).

Here the first pair is S² and the last two pairs are T². Define the actual subgroup

    H={ (t,t, i(t), i(a), i(b), c) : t,a,b∈S, c∈B }.

It is isomorphic to S³×B, and

    |H|=60³·36=60·360²=|S|·|T|²=|K|.

All T-coordinate projections are proper. Both S-coordinate projections are full, forming a diagonal S-strip in the projection of H. Nevertheless H∩(S²×1)=1: the first T-coordinate remembers t. Thus the diagonal strip cannot split from the other coordinates as a subgroup of H. H is core-free: it contains no whole simple coordinate, the only possible nontrivial normal subgroups of G being products of whole coordinates. This explicitly defeats an argument that derives global isotypic strip independence merely from order, faithful coordinates, and full-strip projection.

It is **not** a folder counterexample. A6 has one involution class; choose a nonidentity involution b∈S and a nonidentity involution c∈B, and take t=a=1. The resulting (1,1,1,1,i(b),c) is a nonidentity element of H∩K², because i(b) and c are conjugate involutions in A6. It also fails the simplicity-density test in the S-block: its projection has size 60, not strictly greater than n_S=60. These failures make it a control pinpointing exactly what remains to be repaired, not evidence that a mixed simple loop exists.

Next bounded obligation: in a concrete pair of types, classify possible nontrivial common quotients C of dense block projections and determine whether their marked-square images can be disjoint away from 1. The example shows that merely forbidding a smaller simple group as a subgroup of a larger proper leaf is too strong; the density and collision-image conditions must be used simultaneously.


## A simple mixed A5 and PSL2(7) folder

Independently reviewed C0010 construction, conditional on the faithful generated-folder and exact normal-subloop criteria of [C0001](../../claims/0001.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45), the scoped canonical-inversion input of [C0007](../foundations/C0007.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813), and the [Bruck-stabilizer criterion](exact-factorization-criterion.md#bruck-stabilizers-and-necessary-witness-tests) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/d9bc55095490d42e41c359bbb88b67c78f6d4998). It supplies a concrete simple proper non-Bruck loop of order 10080 with mixed paired canonical group, not an exhaustion of all mixed folders.

The subgroup embeddings D₁₀,A₄≤A₅ and 7:3,S₄≤PSL₂(7) are the Dickson inputs of the reviewed [A₅ classification](radical-free-a5-path-classification.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/ad94accf574f89bf1e8487bb046cf30fb685cd0c) and [small-prime classification](radical-free-small-psl2-paths.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/184bc5f1b24d05d4dac1860060c6189afefda70c). The latter includes the finite S₄ embedding/fusion certificate; no new computation is used here.

Let T=A5 and U=PSL2(7). Choose D=D10 and A=A4 in T, and B=7:3 and S=S4 in U. Let ε:D→C2 be the quotient by its normal C5, δ:S→C2 the sign homomorphism, λ:A→C3 the quotient by V4, and μ:B→C3 the quotient by its normal C7. Choose identifications of these quotients and put

    G=T×T×U×U,     τ(t1,t2,u1,u2)=(t2,t1,u2,u1),
    K={(t,t^−1,u,u^−1):t∈T,u∈U},
    H={(d,a,b,s)∈D×A×B×S : ε(d)=δ(s), λ(a)=μ(b)}.

The two quotient equations are independent and surjective, so |H|=(10·12·21·24)/(2·3)=10080=60·168=|K|=[G:H]. The projection of H to T² is all D×A, and to U² all B×S: the two missing variables can always be selected independently to realize prescribed C2 and C3 values. Each individual coordinate projection is its specified nontrivial proper subgroup.

We prove H∩K²=1. A pair (x,y)∈T² lies in the T-coordinate of K² exactly when y is T-conjugate to x^−1, and similarly for U. A nonidentity element of D can share an order with a nonidentity element of A only if both are involutions. A nonidentity element of B can share an order with a nonidentity element of S only if both have order 3. These assertions follow from the subgroup types, without requiring the converse that all elements of such orders are conjugate.

If (d,a,b,s)∈H∩K² and (d,a) is nonidentity, then d,a are involutions. Thus ε(d) is nonzero while λ(a)=0. The second defining equation gives b∈C7, and since (b,s) are conjugate inverses but S has no element of order 7, b=s=1. The first equation then gives ε(d)=0, contradiction. If (d,a)=1, the same second equation gives b∈C7 and the same argument forces b=s=1. Thus the intersection is trivial.

K² is invariant under conjugation by G, so H∩(K²)^g=1 for all g. Since |K|=[G:H], this proves K is a transversal to every conjugate of H. K is inverse-closed and closed under xyx, so it defines a Bol folder. It generates G: products of anti-diagonal elements generate each simple coordinate because T and U are perfect. H is core-free because a normal subgroup of G is a product of its simple direct factors and no individual simple coordinate is contained in H. Therefore the cited C0001 faithful-folder interface identifies G as the canonical left multiplication group; τ is the canonical inversion since it inverts the generating set K.

For simplicity, check the exact normal-subloop criterion on all proper nontrivial normal N◁G. Such an N is a product of coordinate factors. Retain its complementary coordinates in a quotient. For each type, if both coordinates are retained then the ratio |G/N|/|KN/N| contributes |T| or |U|, while if at most one is retained it contributes 1. If neither complete type-pair is retained, π(H) is nontrivial, hence strictly larger than this ratio 1. If exactly the full T-pair is retained, π(H) projects onto D×A and has order at least 120>60; if exactly the full U-pair is retained, its order is at least 504>168. Both complete pairs are retained only when N=1, which is excluded. Hence in every proper nontrivial normal quotient, |π(H)|>|G/N|/|π(K)|, exactly the strict inequality of C0001. The resulting loop is simple.

The loop is nonassociative because H is nontrivial in a faithful generated folder. Its left multiplication action is imprimitive: H lies in the proper subgroup D×A×B×S of G, so it is non-Moufang by C0001 Lemma 1.2, the same simple nonassociative Moufang primitivity interface used in [the path construction](radical-free-path-factorizations.md#properness-and-scope). Moreover τ does not normalize H, because its first coordinate projection is D of order 10 while its second is A of order 12; the Bruck-stabilizer criterion gives non-Bruckness. The order is |K|=10080. These assertions have the independent exact-source reviews below; there is no claim that the construction is new in the literature or that it exhausts mixed types.

### Exact-factorization identification and all normal quotients

Flip the two U coordinates. In N=T×U set L=D×_{C2}S and R=A×_{C3}B. Then |L|=10·24/2=120, |R|=12·21/3=84, and |L||R|=|N|. If (x,y)∈L∩R, then x∈D∩A has order 1 or 2 and y∈S∩B has order 1 or 3. If x is nontrivial, it is an involution: its C3-image in A is 0, so y∈C7 and, since S has no 7-elements, y=1; the C2 equation then forces x∈C5, contradiction. If x=1 the C3 equation again forces y=1. Thus L∩R=1 and N=LR is an exact factorization. The folder belongs to the existing exact-factorization construction; no literature novelty or outside-family claim is made.

For absolute precision in the simplicity check above: every normal N is a product of the four coordinate factors, whether or not τ-stable. For any proper nonempty retained coordinate set J, the projection of H has order equal to the product of the selected endpoint orders, divided by 2 if both D and S coordinates are selected and divided by 3 if both A and B coordinates are selected. Each divisor arises from one surjective independent equation. If neither whole type-pair is selected the required ratio |G/N|/|π(K)| is 1 and the image of H is nontrivial. A proper J can contain at most one full type-pair; if it contains the T-pair its H projection has order at least 120>60, and if it contains the U-pair it has order at least 504>168. Any extra retained coordinate can only enlarge a projection. This verifies the criterion for every proper coordinate subset, including non-τ-stable ones.

Thus this construction refutes single-simple-type necessity in the paired canonical setting; it remains within exact factorizations, and literature novelty is unassessed.


## Independent review

reviewers `review_hs_full`, `review_small_order_complete` and `review_s5_h3` independently accepted the complete source at [the source revision](https://github.com/Mira-Cult/math-wip/commit/ada92bab7c75898127ee367a33f68329ed3cdacc), conditional on the pinned canonical-folder, normal-subloop, paired-strip, Moufang, inversion, Bruck and subgroup-embedding inputs. Each checked the Goursat image/kernel conditions, maximal-type composition-factor splitting and strict tree bound, the failed control, and every part of the actual order-10080 construction: independent quotient equations, original-H collision, faithfulness/generation, all retained-coordinate quotients including non-τ-stable kernels, properness, non-Bruckness and exact-factorization identification. No new computation or fresh primary-source audit was performed. Their acceptances neither classify all mixed types nor establish literature novelty.


## Complete base-model exhaustion

**Independently reviewed result for 0323:C0010 under the pinned inputs.** Let T=A5, U=PSL2(7), G=T²×U², and let τ swap the coordinates within each pair. Subject to the exact folder, normal-subloop and subgroup inputs below, every faithful generated canonical folder of a finite simple nonassociative left Bol loop with these G and τ is isomorphic to the already constructed folder with

 H={(d,a,b,s)∈D10×A4×(7:3)×S4 : ε(d)=δ(s), λ(a)=μ(b)}.

In particular the base model has one loop-isomorphism class, of order 10080, and it is proper and non-Bruck. This exhaustion has the independent exact-source reviews below; it does not classify loops whose canonical group merely has T or U as a section.

### Inputs and notation

The actual marked set is K={(t,t^-1,u,u^-1):t∈T,u∈U}; its product square consists of pairs whose coordinates are conjugate inverses in each simple factor. This follows because every outside involution for the paired inversion is conjugate to the canonical involution. The faithful-folder and exact normal-subloop criteria are [C0001](../../claims/0001.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45); the mixed-density and maximal-type splitting arguments have the independent exact-source reviews in this canonical source at [the source revision](https://github.com/Mira-Cult/math-wip/commit/ada92bab7c75898127ee367a33f68329ed3cdacc). In particular |H|=|K|=60·168=10080, H∩K²=1, Core_G(H)=1, and the two type projections H_T≤T² and H_U≤U² satisfy

 |H_T|>60,    |H_U|>168.                                            (1)

The proper subgroups of A5 are contained in A4, D10 or S3, with respective orders 12,10,6; every 5-bearing proper subgroup lies in D10. The proper subgroups of PSL2(7) are contained in 7:3 or S4; every 7-bearing proper subgroup lies in 7:3. Both groups have a single involution class. These are the Dickson subgroup inputs in Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Ann. Math. 172 (2010), Appendix Theorem A.1 and Lemmas A.2–A.3, printed pp.1354–1355, https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf, with small-group interpretation as in the reviewed [the A₅ source](radical-free-a5-path-classification.md) and [the small-prime source](radical-free-small-psl2-paths.md). The latter's pinned GAP 4.15.1 certificate supplies the two S4 classes and their fusion under PGL2(7). These classification and algorithmic inputs are not re-proved here.

### All four coordinate projections are proper

Consider the U coordinates first. The subdirect group formed by full U projections is a product of disjoint full U strips. Its complement has no U composition factor, since all T factors and proper U subgroups have smaller order. Goursat therefore splits off each such strip as an independent subgroup of H. A singleton strip gives an entire normal coordinate factor of G contained in H, contradicting core-freeness. With only two U coordinates, the remaining possibility is a twisted diagonal U strip across the paired coordinates. It contains a nonidentity pair of conjugate involutions: U has one involution class, and any twisting automorphism preserves it. With the other coordinates identity this lies in H∩K², contradiction. Thus the U projections are proper and, by the subgroup input, solvable.

The same argument now applies to full T projections. Their complementary projection is solvable: it is a subgroup of the product of proper U projections and any proper T projections. It cannot have T as a quotient, so the T strips split off. A singleton violates core-freeness, while a two-coordinate twisted diagonal contains a marked-square involution. Hence all four coordinate projections are proper.

### Dense projections and actual Goursat quotient

Since 5 divides |H|, some T coordinate has 5 in its projection. Enlarge that projection to a D10; the other proper T projection is contained in an A4, D10 or S3. Since 7 divides |H|, some U coordinate projection is contained in a 7:3 and has a 7-element. The other U coordinate must be contained in S4: if both were contained in 7:3, H_U would have odd order, while the T side contributes at most 2³ and |H| has 2-part 2⁵. Thus, after swaps of τ-paired coordinates,

 H_T≤D10×X, X∈{A4,D10,S3},      H_U≤(7:3)×S4.                  (2)

If X=S3, (1) fails since 10·6=60. If X=D10, then |H_T| divides 100 and is greater than 60, so |H_T|=100. Meanwhile |H_U| divides 504 and exceeds 168, so |H_U| is 252 or 504. Goursat gives a common quotient C with

 |C|=|H_T||H_U|/10080.

The value 252 gives 5/2, impossible; 504 gives |C|=5, impossible since 5 does not divide |H_U|. Therefore X=A4. Its ambient order is 120, so (1) forces H_T=D10×A4. The only remaining |H_U| are 252 or 504, and the common quotient has order 3 or 6 respectively.

If |C|=3, the quotient map α:D10×A4→C3 kills D10 and restricts on A4 to the quotient by V4. Therefore ker α contains D10×V4. Choose nonidentity involutions d∈D10 and a∈V4. They are conjugate in A5, so (d,a) lies in K_T². The element ((d,a),1_U) lies in H∩K², contradiction. Hence |C|=6, H_U=(7:3)×S4, and both quotient maps are surjections onto a group of order 6.

The abelianization of D10×A4 is C2×C3≅C6. Since a quotient of order 6 is a common quotient with 7:3×S4, this alone needs care: could the common quotient be S3? It cannot, because D10×A4 has no S3 quotient. Indeed any nontrivial image of D10 in S3 is C2 or S3, but an S3 image would give a quotient of D10 of order 6, impossible; the A4 image is 1, C3, or A4, and S3 contains no A4. Images of the two direct factors commute, so they cannot generate S3 from C2 and C3. Thus C≅C6, the map from D10×A4 is its full abelianization, and the U-side map is the product of the unique C3 quotient of 7:3 by C7 and the unique C2 sign quotient of S4. After common identification of C, H is exactly the fiber product of these maps; the only choices are the independent inversions of the C3 identifications (the C2 identification is unique).

### Simultaneous conjugacy and sufficiency

All D10 are Sylow-5 normalizers in A5, and all A4 are point stabilizers. D10 acts transitively on the five points, so A5 is transitive on pairs (D10,A4). The normalizer N_{S5}(D10)=5:4 has a point-stabilizing subgroup C4. Its generator is an odd permutation, hence normalizes the fixed A4 and inverts its C3 quotient. It preserves D10 and its C2 quotient. Thus the two possible C3 identifications can be interchanged by a simultaneous automorphism of the two T coordinates, commuting with τ.

For U, the pinned finite certificate proves the two S4 classes fuse under PGL2(7). The 7:3 Borels are conjugate, and any fixed S4 acts transitively on the eight Sylow-7 subgroups: each point stabilizer is contained in a 7:3 and has order dividing gcd(24,21)=3, so every orbit has size at least eight. Therefore the pair (7:3,S4) is unique under Aut(U), and the coordinate automorphism acts simultaneously on each U pair. Pair swaps likewise commute with τ. It follows that every necessary H is in the same canonical-folder automorphism orbit as the displayed mixed folder.

Existence and all fourteen proper nontrivial normal-coordinate quotient checks are already established for a=b=1 in the reviewed [the mixed-path source](radical-free-mixed-paths.md), source [the source revision](https://github.com/Mira-Cult/math-wip/commit/9d1c0af909166459fbbeb87b881c28dff353aa3f) (or the base construction at [the source revision](https://github.com/Mira-Cult/math-wip/commit/ada92bab7c75898127ee367a33f68329ed3cdacc)). Those sources also establish properness, non-Bruckness, and the exact-factorization interpretation. The automorphisms above preserve τ and K, giving the claimed loop-isomorphism classification conditional on the cited inputs. No order-10080 multiplication table is enumerated.


### Independent review of the appended continuation

reviewers `review_paired_simple`, `audit_c9_full` and `review_folder_criterion` independently accepted the appended continuation at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/6f17ba6210a02e02707d49f0a47fb89de46dfffa), conditional on the cited folder, subgroup, finite-fusion and witness inputs. Their scoped reviews covered the base-model exhaustion, endpoint and family-isomorphism law, and atom-graph connectedness/bridge deductions in the three linked manuscripts. They did not perform a fresh primary-source audit or rerun the earlier finite certificates. These are model mathematical reviews, not human or formal certification, and do not establish a general classification or literature novelty.
