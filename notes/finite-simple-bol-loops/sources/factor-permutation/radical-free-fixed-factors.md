# Fixed factors in PSL₂(q)-power canonical envelopes

**Mira Cult**

**Independently reviewed continuation of [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md).** Let G=A5^r×PSL₂(7)^s be the faithful canonical left multiplication group of a finite simple nonassociative Bol loop. The [all-powers matrix classification](radical-free-mixed-matrix-classification.md), independently reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/8aa2dc1c5f7bd3190a57118c1e7e8398587f7655), and its single-type inputs require τ to swap every pair of coordinates. Nonisomorphic A5 and PSL₂(7) factors cannot be exchanged by τ, so τ has separate involutory permutations on the two species, each with fixed points or two-cycles. This observation by itself does not forbid fixed points.

## Pinned interfaces and scope

The faithful generated-folder, all-conjugate transversal and exact normal-quotient inputs are [C0001](../../claims/0001.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45); canonical τ and conjugacy-invariance of Λ=τK are the scoped [C0007](../foundations/C0007.md) inputs at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). The [full-strip decomposition](radical-free-strip-forests.md) was reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6d3a97daa9cf20bbae0416295c8c2374c2cd8ede); the new parity proof uses the kernel-count mechanism of [the support lemma](radical-free-involution-support.md) reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e30af949531c0ebcc9f7533b04fc1e7fc6858563). Small-subgroup, automorphism and unique-involution-class inputs are as pinned in [the A₅ source](radical-free-a5-path-classification.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/ad94accf574f89bf1e8487bb046cf30fb685cd0c) and [the small-PSL₂ source](radical-free-small-psl2-paths.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/184bc5f1b24d05d4dac1860060c6189afefda70c). The deductions below have the independent mathematical reviews recorded at the end. The initial sections give necessary conditions; the reviewed exhaustion sections complete the A₅-power and PSL₂(7)-power canonical-group settings. The subsequent Fermat-prime extension retains its separate review status.

## Projected constraints and their limitation

Fix an individual τ-stable simple coordinate T, with restriction α∈Aut(T), and let L be the product of all other coordinates. Put K_T=π_T(K), H_T=π_T(H), H^T=H∩T. For G≠T, the reviewed normal-subloop criterion applied to L gives the strict inequality

 |K_T| > [T:H_T].                                             (1)

Also K_T generates T and consists of α-inverted elements, because K generates G and τ(k)=k^-1. Since K itself is a transversal but its projection need not be, (1) is a multiplicity constraint, not a smaller folder.

There is a genuinely local marked collision constraint. Let t be the formal outside involution. For every x∈T, x^-1 t x lies in Λ=tK, so [t,x]=t x^-1 t x belongs to K∩T (convention changes may invert this commutator). Hence H^T avoids every nonidentity element of the square of this local commutator set. More generally H^T∩(K∩T)^-1(K∩T)=1. This uses actual selected marks and their conjugacy, rather than an assumed local transversal.

If α=1, K_T consists only of 1 and involutions. Both T have one involution class, with 15 involutions in A5 and 21 in PSL₂(7), so |K_T|≤16 or 22 respectively. Equation (1) forces |H_T|>60/16 or >168/22, i.e. |H_T|≥4 or ≥8. These bounds concern a projection and do not force any nontrivial H∩T. Indeed if α=1, the commutator set above is trivial, illustrating exactly why the direct local collision argument does not settle this case.

If α=Inn(a) is nontrivial, simplicity and trivial center imply a is an involution. In the local extension c=at is central of order 2; the local marks arising by T-conjugation form c·a^T, so actual K∩T contains a·a^T. Thus H^T must avoid (a^T)^2, a source-backed local restriction, but H_T need not equal H^T, and neither is forced to be a full-folder stabilizer. If α is outer, the local mark restrictions similarly involve the actual α-outside involution class; no full-class assertion for all of π_TΛ is made without checking whether multiple classes occur.

The reviewed no-simple-folder theorems for G=T do not automatically apply to a τ-fixed component of a larger direct product: after projecting K, cosets may have multiplicity and the projected H need not meet K_T once. Conversely an example of an abstract fixed-factor automorphism does not establish a Bol folder. The surviving precise problem is to combine (1) for all coordinate and normal-subproduct projections with the local marked restrictions and the correlated subgroup H≤G. No valid proof of fixed-point-freeness or actual counterexample is claimed here.

## Exact outside-class support polynomial

For the entire direct-product model, τ permutes factors in two-cycles or fixes them. A two-cycle on a simple factor T has one outside involution class under T×T, of size |T|. On a fixed A5 factor, an inner or identity restriction has two local outside involution classes of weights 1 and 15; for nontrivial inner α=Inn(a), these are c and c·a^T, c=at, while for α=1 they are t and t·Inv(A5). An outer restriction has one local outside involution class of size 10: Aut(A5)=S5 and it is the class of transpositions. On a fixed PSL₂(7) factor, the corresponding inner/identity weights are 1 and 21; the outer class has size 28. For the latter, Aut(T)=PGL₂(7); a split involution diag(1,−1) has nonsquare determinant, PGL centralizer order 12, and centralizer in T order 6, so its T-class has size 28. The other PGL involution class lies in T. The two-class assertion and class size are in Siman Wong, *The maximal unramified extensions of certain complex Abelian number fields*, Publications mathématiques de Besançon (2015), pp.93–104, Lemma 1(a), printed p.95, [published PDF](https://www.numdam.org/item/10.5802/pmb.14.pdf), DOI `10.5802/pmb.14`; the project directly inspected the statement and its matrix proof on 15 November 2026; the elementary determinant and centralizer calculation identifies the outer class. The A5 statements are elementary permutation calculations.

Let a,b count fixed A5 and PSL₂(7) factors with inner-or-identity restriction, and u,v count fixed factors with outer restriction; let paired factor contributions be P=60^{p}168^{q}. Label the a+b inner/id fixed factors by I, with weights w_i=15 or 21. Since Λ is G-conjugacy invariant, its actual selected outside involutions form a union indexed by some nonempty family F⊆2^I, and

 |K|=P·10^u·28^v·W,      W=Σ_{S∈F}∏_{i∈S} w_i.            (2)

There are no multiplicities in F: each local outside involution class product is a distinct G-class, and the paired and outer factors have just one such class. The mandatory class t^G requires F to contain the set S₀ of fixed inner factors on which α is nontrivial; identity restrictions contribute the weight-1 local class. Transversality implies |K| divides |G|, so

 W divides P·60^{a+u}168^{b+v}/(10^u28^v).                       (3)

Equivalently this rational expression must be a positive integer and W one of its positive divisors. In particular every prime of W lies in {2,3,5,7}, and W≡|F| (mod 2). Formula (2) is an exact necessary finite Boolean-support description for each fixed multiplicity; it is not sufficient for a folder because closure, all-conjugate transversality, generation and strict normal-quotient inequalities remain. For instance selecting every local support gives W=16^a22^b; if b>0 its factor 11 violates (3). This eliminates that particular selected union, not a fixed PSL₂(7) factor in general. Conversely choosing only mandatory support gives W=15^a21^b when all these fixed restrictions are nontrivial inner, which satisfies the prime-support portion of (3); divisibility alone therefore does not exclude that pattern. More detailed index and normal-quotient constraints are needed before any fixed-point-free conclusion.

## Actual mark-square subgroups for fixed A5 coordinates

A stronger condition follows from independent conjugation, not merely class counting. In A5, the square of the involution class C (the 15 double transpositions) is all A5: products include identity, a double transposition, a 3-cycle and representatives of both 5-cycle classes; for example (12)(34)(12)(35)=(354), while (12)(34)(13)(25) is a 5-cycle, and both 5-cycle classes occur because the order-ten normalizer of a Sylow 5-subgroup is dihedral, whose reflections are double transpositions; every element of that Sylow 5-subgroup is a product of two reflections. Thus C²=A5.

For any selected global support S∈F in (2), let A(S) be the subset of its fixed A5 inner/id coordinates. Fix one global marked element in the selected product class, and independently conjugate its A5 components. Two chosen global marks can be taken equal in every coordinate outside A(S); their product then gives every element of N_S=∏_{i∈A(S)}A5_i, supported only on these factors. Hence

 N_S⊆Λ²,  H∩N_S=1,  |H|≤|G|/|N_S|,  |K|≥60^{|A(S)|}.   (4)

The inclusion and subgroup collision are global and use actual selected marks; there is no projection-to-folder step. In particular H∩A5_i=1 for every fixed A5 inner/id coordinate i appearing in any selected support. Every such coordinate must appear in some S: if α_i=id, otherwise its K-projection is trivial, contradicting generation; if α_i is nontrivial inner, the mandatory t^G class already activates it. Therefore H∩A5_i=1 for all fixed A5 inner/id coordinates. More generally H embeds into G/N_S for each selected S, even when H has diagonal coupling with other factors. The argument does not imply H∩∏_i A5_i=1 unless one selected support activates all these factors.

The weighted support family consequently obeys, for each S∈F,

 P·10^u·28^v·W ≥ 60^{|A(S)|},

in addition to divisibility and normal-quotient inequalities. This is a new actual H/mark collision constraint, but it still does not force τ fixed-point-free: other factors or paired-coordinate contributions may supply the needed cardinality. For fixed outer A5 coordinates the outside transposition-class square consists only of identity, 3-cycles and double transpositions, so the preceding full-factor conclusion cannot be extended to them by this argument; order-five subgroups remain locally possible.

## Global Sylow-two obstruction for selected supports

For every selected S∈F, let S_A and S_U denote its activated fixed inner/id A5 and PSL₂(7) coordinates. Then necessarily

 v₂(W) ≥ u+v+2|S_A|+3|S_U|.                                (5)

Proof. In the square of the selected global mark class, independent coordinate conjugation realizes arbitrary tuples of involutions on every fixed outer coordinate and on every fixed inner/id coordinate in S, with identity on every inactive fixed coordinate. Indeed each relevant outside-class square contains the unique inner involution class: this is immediate for A5 transpositions (two disjoint transpositions), for the inner A5/PSL₂(7) involution classes (commuting involutions in a Sylow 2-subgroup), and for the outer PSL₂(7) class, represented in PGL₂(7) by the commuting projective involutions diag(−1,1) and [[0,1],[1,0]]; both have nonsquare determinant and their product is a nonidentity inner involution. At each exchanged pair the square realizes any pair of involutions, or the identity pair, because T has a unique involution class and paired marks are anti-diagonal. Thus any involution of H with identity outside the active fixed coordinates and matched zero/nonzero support across every τ-pair lies in Λ².

Let P₂∈Syl₂(H). Count such elements including 1 modulo 2. For each pair, write e_L,e_R for the coordinate identity indicators, so matched support is indicated by 1+e_L+e_R over F2; multiply by e_i for each inactive fixed coordinate. Expansion is a sum of counts of involutions, including 1, in kernels obtained by imposing identity on all inactive fixed coordinates and at most one coordinate from each pair. Each target projection has order at most 2^{2p+3q+2(a−|S_A|)+3(b−|S_U|)}. But (2) gives

 |P₂|=2^{2p+3q+2a+3b+u+v−v₂(W)}.

If (5) fails, every projection kernel is a nontrivial 2-group, whose involution count including 1 is even. The total matched-support count is even and contains identity, so it contains a nonidentity element of H∩Λ², contradiction. No independence of H-projections is assumed.

The arithmetic bound does not by itself force fixed-point-freeness. For instance a=2,b=u=v=0 and F={{1},{1,2}} gives W=15+225=240 and v₂(W)=4, meeting (5), although the stronger full-A5-subgroup condition (4) rules it out when there are no paired factors. There are explicit further scalar controls, for example a=4,b=0, F={{1},{2},{3},{4}}, W=60, and a=1,b=2, F={{U1},{A,U1},{U2},{A,U2}}, W=672. These are numerical controls only: they are not asserted to satisfy the full folder conditions or to yield actual simple loops. No exhaustive computation is claimed for these explicit examples.

## A5-only 3/5 leaf-count bound and an arithmetic survivor

Assume G=A5^{2p+a+u}, with p τ-pairs, a fixed inner/id factors and u fixed outer factors. Under the reviewed full-strip decomposition, let m be the number of full A5 strips in H; each uses at least two coordinates because H is core-free. Every proper A5 coordinate projection is solvable and has 3-part at most 3 and 5-part at most 5, but not both. The full strips split off from the solvable residual by Goursat, and each contributes one 3 and one 5 to the order. From |H|=|G|/|K| and formula (2),

 v₃(|H|)=p+a+u−v₃(W),  v₅(|H|)=p+a−v₅(W).

After subtracting m full strips, the required distinct 3-bearing and 5-bearing leaves number at least 2p+2a+u−v₃(W)−v₅(W)−2m. The number available is at most 2p+a+u−2m. Therefore

 a≤v₃(W)+v₅(W).                                            (6)

This argument retains global residual correlations; it only bounds the order by the product of leaf projections. If ∅∈F, then every other summand of W is divisible by 15, so W≡1 mod15 and (6) forces a=0. Thus no fixed inner/id A5 factor can occur when the selected global mark set contains the weight-1 local class at all of them simultaneously.

The parity bound (5), inequality (6), activation and order divisibility do not alone imply a=0. For any integer t≥1, put a=2t,u=0 and let F consist of all sets containing a fixed t-subset S₀. Then W=15^t16^t, max_{S∈F}|S|=2t, so v₂(W)=4t=2 max|S| and v₃(W)+v₅(W)=2t=a. With p=t paired factors, W divides 60^{p+a} and the full-mark-square bound (4) also holds for every S: 60^p W=60^{2t}4^t≥60^{2t}. The mandatory support is S₀ if those t restrictions are nontrivial inner and the other t are identity; every coordinate is activated. These are formal arithmetic support data, not constructed folders. They prove that any universal arithmetic contradiction needs additional structural constraints beyond (3)–(6), not a search over only these inequalities.

## Actual-H elimination of the formal family; a 2-power-index criterion

The formal family above does not produce a folder. Its selected support S=I activates all a=2t fixed A5 coordinates, so N_S=A5^{2t}≤Λ² and H∩N_S=1. The image of H in the complementary paired A5^{2t} has index

 [G/N_S : HN_S/N_S]=|K|/|N_S|=4^t>1.

But A5^n has no proper subgroup of 2-power index. Indeed each coordinate projection would have 2-power index in A5 and hence be all of A5 (a 2-power index would divide 60 and hence be 2 or 4; simplicity would force an impossible embedding A₅→S₄). A subdirect subgroup is a product of diagonal simple strips, and a nontrivial strip makes its index divisible by 60, impossible for a 2-power. Thus the earlier infinite arithmetic control is actually excluded by the global H embedding.

More generally, in an A5-only envelope, for every selected support S let s=|S| and N_S be its full fixed-coordinate product. If |K|/60^s is a power of two, the same argument forces this index to equal 1. In fact the global support-parity bound rules out every such case with p+u>0. Here |K|=60^p10^u W and v₂(W)≥u+2s, so

 v₂(|K|/60^s)=2p+u+v₂(W)−2s ≥ 2p+2u.

Thus a 2-power index would be >1 whenever p+u>0, contradicting the subgroup theorem. If p=u=0, τ is globally inner (including identity restrictions), already excluded for radical-free canonical G by the reviewed inner-inversion/Bruck-isotope reduction in [the intrinsic source](exact-factorization-criterion.md#inner-inversion-and-the-generalized-fitting-subgroup) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/84eba0ffd4dfab4b6d64853a3131010ad2b945b8). Consequently no selected S can make |K|/60^s a power of 2 in such a simple nonassociative A5-only canonical envelope. The proof uses H∩N_S=1 as an actual global consequence of the selected mark square; it does not infer a projected folder.

This 2-power-index conclusion should not be transferred unchanged to mixed A5/PSL₂(7) complements: PSL₂(7) has a subgroup of index 8. It remains a necessary obstruction rather than a complete classification of admissible support families.

## An active-coordinate strip cannot have an independent opposite leaf

Let S be a selected support and let i∈S be a fixed inner/id A5 coordinate. Suppose H contains an independent full diagonal A5 strip Δ whose support includes i and exactly one coordinate x of a paired edge (x,y), and suppose H also contains a nontrivial subgroup L≤T_y supported only on the opposite coordinate y. Assume any other coordinates in Δ, if present, are fixed inner/id A5 coordinates in S (so their local selected class squares are full A5). Then H∩Λ²≠1. Indeed pick 1≠h∈L; use the strip parameter to make its x-coordinate conjugate to h^-1. On every active fixed coordinate of Δ, the selected class square is the whole A5. On the paired edge, the two chosen coordinates are conjugate inverses and hence lie in the pair-class square. All remaining coordinates can be identity. Independent conjugation in the selected global mark class therefore supplies this nonidentity strip-times-leaf element in Λ². The assertion includes strip twists: automorphisms preserve conjugacy classes, and a strip parameter can be chosen to realize any prescribed value at x.

The hypothesis on the other strip coordinates is essential: an additional paired edge supported on only one of its two coordinates would obstruct this particular element. Nor does a nontrivial projection to y suffice: the subgroup L must be independently supported there (or one must explicitly control all other coordinates). This is a sufficient global collision mechanism, not a proof that every support family has such a strip/leaf configuration.


## Immediate paired-inversion corollaries and remaining obligation

If a=b=0, then the only support is empty and W=1. Inequality (5) forces u=v=0. Thus in the two-type model, if τ has no fixed factor on which its restriction is inner or the identity, then it has no fixed factor at all: every factor is paired and the reviewed paired classification applies (using the single-type cases if just one type occurs).

In the A₅-only model, if the empty support belongs to F, (6) first forces a=0 and then (5) forces u=0. This is a second sufficient condition for paired inversion. Neither condition has been established for every simple loop. The remaining obligation is to control selected families without the empty support using the actual stabilizer and class-square conditions, or produce a faithful simple counterexample. Scalar divisibility and valuation controls alone do not answer that question; the explicit formal family above is excluded only after the actual subgroup-index argument. No computation or literature novelty is claimed for these reductions.


## Independent mathematical review

reviewers `review_paired_simple`, `audit_c9_full` and `review_folder_criterion` independently accepted the complete constraint package at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/59985c2e7450f7f800c4db0f8859b3a58669ee83), conditional on its pinned canonical-folder/inversion, subgroup, strip and Bruck-isotope interfaces. They checked the outside-class support polynomial and mandatory class, actual selected-mark square and complementary stabilizer embedding, global Sylow-two parity exponent, original-stabilizer A₅ leaf count, the formal-family elimination by the image-index theorem, and the stated paired-inversion corollaries. None transfers original corefreeness to a projected subgroup or assumes a projected folder. Reviewer `review_paired_simple` additionally directly inspected Wong, Lemma 1(a), printed p.95; the other two relied on the recorded source input. No new computation or full re-audit of upstream classifications was performed. These are model mathematical reviews of necessary restrictions, not human or formal certification, a counterexample construction, or a proof that all fixed factors are impossible.


## Character obstructions on the original stabilizer

**Independently reviewed continuation of C0010.** Retain the A₅-only canonical model and exact marked-support data above, with G=A₅^(2p+a+u). These arguments use the actual transversal and original H; they never assume τ(H)=H. The independent reviews above concern the earlier constraints; separate reviews of this extension are recorded below.

### A nonzero scalar forbids fixed vectors

Write S_K=Σ_{k∈K}k and e_H=Σ_{h∈H}h in the complex group algebra. Actual transversality gives S_K e_H=Σ_{g∈G}g (choose the left/right convention accordingly; K is inverse-closed). Let ρ be a nontrivial irreducible complex G-representation whose isomorphism class is τ-stable, and extend it to G⋊⟨t⟩. Such an extension exists: a chosen intertwiner has scalar square, and rescaling makes that square one. Conjugacy-invariance of Λ=tK makes its sum commute with ρ(G), so Schur's lemma gives

 ρ(Σ_{λ∈Λ}λ)=c_ρ I,       ρ(S_K)=c_ρ ρ(t)⁻¹.

If c_ρ≠0, the latter matrix is invertible. Applying ρ to the transversal identity gives ρ(e_H)=0, because ρ is nontrivial. Since |H|⁻¹ρ(e_H) is projection onto the H-fixed space, that space is zero. This argument does not require H to be normalized by t or τ.

It suffices below to use the three A₅ irreducible characters of degrees 1,4,5. For completeness, the degree-four representation is the deleted natural five-point permutation representation. The degree-five representation is the deleted permutation representation on the six Sylow-five subgroups. Both actions are doubly transitive, so their deleted characters are irreducible: for the six-point action a Sylow C₅ fixes its own subgroup and cycles the other five, because no distinct order-five subgroup can be normalized by an element of order five in its order-ten normalizer. Thus the point stabilizer is transitive on the other five points. Both representations are real, self-dual and invariant under Aut(A₅)=S₅, since these permutation actions extend to S₅.

On the A₅ classes of orders 1,2,3,5,5, their character values are respectively

 χ₄=(4,0,1,−1,−1),       χ₅=(5,1,−1,0,0).

For χ₅, an involution normalizes two Sylow-five subgroups: the six order-ten normalizers contain five involutions each, and A₅ has fifteen involutions. An order-three element normalizes none, and an order-five element normalizes just its own subgroup. These observations give the displayed values directly. In the S₅ extensions, a transposition has χ₄-value 2 and χ₅-value −1: it fixes three natural points and no Sylow-five subgroup, since its order-twenty affine normalizer has no transposition. Tensoring an extension by sign changes both signs as appropriate but never their nonvanishing.

For an inner/id fixed coordinate choose the extension so that c=at acts trivially when τ=Inn(a). The two local outside-class sums act by 1 and 15χ(involution)/χ(1). Thus their active weights for χ=1,χ₄,χ₅ are 15,0,3. For a paired edge labeled by the same χ on both coordinates, the full outside-class sum has scalar 60/χ(1): matrix-coefficient orthogonality gives Σ_xρ(x)⊗ρ(x⁻¹)=(60/χ(1))flip. Pair twists may first be removed through the canonical τ identification. For a fixed outer coordinate, the unique outside class has scalar 10, ±5 or ±2 for these three characters; signs reflect the chosen S₅ extension.

Consequently, for tensor labels chosen from 1,χ₄,χ₅, with equal labels on each paired edge, the scalar is a nonzero product of the paired and outer factors times

 P(z₁,…,z_a)=Σ_{S∈F}∏_{i∈S}z_i,       z_i∈{15,0,3}.

When all inner/id labels are 1 or χ₅, P is strictly positive. With χ₄ labels on a set J of inner/id fixed coordinates and trivial labels on all the others, P is positive exactly when some selected support S is disjoint from J. No cancellation can occur in these nonnegative evaluations; outer signs multiply the entire polynomial by one fixed nonzero factor.

### Fixed-coordinate projections and full strips

A proper subgroup J<A₅ has a χ₅-fixed vector unless J is exactly A₄. To verify this, every proper J is contained in A₄,D₁₀ or S₃ by the pinned subgroup input. The χ₅-fixed dimensions of these maximal subgroups, computed by averaging the displayed character, are 0,1,1. Proper subgroups of A₄ have orders 1,2,3 or 4, so cannot be transitive on the six Sylow-five subgroups; their deleted permutation representation therefore has a fixed vector. Finally, A₄ has a χ₄-fixed vector in the natural five-point action.

Apply the nonzero-scalar obstruction with χ₅ on one fixed coordinate and trivial labels elsewhere. Its actual stabilizer projection is therefore A₄ or A₅. If that coordinate is inner/id and some selected S omits it, the same argument with χ₄ forces its projection to be A₅. In particular this holds for every fixed coordinate with identity τ restriction, since the mandatory support omits it. Every outer fixed coordinate also has full A₅ projection, because its χ₄ and χ₅ scalars are both nonzero. A proper fixed projection must thus be A₄ on a nontrivial inner coordinate that occurs in every selected support.

No independent full strip of the original H contains two fixed coordinates. Label just those two coordinates by χ₅. The representation is τ-stable and its scalar is nonzero. Yet it has an H-fixed vector: on their common strip the two representations differ only by automorphisms of A₅, χ₅ is invariant under those automorphisms and self-dual, and χ₅⊗χ₅ contains the trivial representation. All other coordinates are labeled trivially. This contradicts the scalar obstruction.

A full strip containing a fixed coordinate i cannot also contain both ends x,y of any paired edge. Label i,x,y by χ₅; its scalar is nonzero and its strip restriction has two fixed vectors, since

 dim(χ₅^⊗3)^A₅=(125+15−20)/60=2.

If instead exactly x belongs to that strip and y is proper, then H_y must be A₄. Otherwise χ₅ on y has a fixed vector, while χ₅ on i,x has a strip-fixed vector; their tensor is fixed by the actual H, even if the proper residual coordinates are correlated. Again the scalar is nonzero.

These deductions concern the original full strips. Although the coordinate i is fixed by τ, its strip need not be τ-stable: τ need not normalize H. That additional assertion is not used and would invalidate an exhaustion argument here.

### Incidence components require specific proper leaves

Build a multigraph with one vertex for every full strip and one leaf vertex for each proper coordinate in a paired edge. The τ-pairs are its edges. Attach a leg for each fixed full coordinate to its strip. Every strip has total coordinate degree d≥2 and at most one fixed leg by the preceding result. Proper fixed coordinates lie outside this graph. A strip with no paired edge would require two fixed legs and is impossible.

Each component containing an edge has a proper A₄ leaf. Label all its paired coordinates and attached fixed legs by χ₅, and all other coordinates trivially. This is a nontrivial τ-stable representation with nonzero scalar. For every full strip in that component,

 dim(χ₅^⊗d)^A₅=(5^d+15+20(−1)^d)/60>0       (d≥2).

If every proper leaf differed from A₄, it would supply a χ₅-fixed vector as well. The full strips are independent, and the tensor of individually fixed leaf vectors is invariant under the actual correlated residual. Thus H would have a fixed vector, a contradiction. This proves the A₄-leaf assertion without assuming that the graph is a forest.

If some selected support S omits all inner/id fixed legs of that component, it also has a distinct C₅ or D₁₀ leaf. Label the same component by χ₄. Its support polynomial is positive by that condition; outer factors and paired factors remain nonzero. The full strips have fixed vectors because

 dim(χ₄^⊗d)^A₅=(4^d+20+24(−1)^d)/60>0       (d≥2).

A proper subgroup has no fixed vector in this deleted natural permutation representation exactly when it is transitive on five points, which for a proper A₅ subgroup means C₅ or D₁₀. Without such a leaf all factors would have fixed vectors, contradicting the nonzero scalar. This leaf is distinct from the already required A₄ leaf.

### Singleton strips after deleting a selected support

Fix S∈F, put s=|S| and v=v₃(W)+v₅(W). Actual mark squares give H∩N_S=1, so H embeds into the complementary A₅ power. Let k_S count original full strips whose support outside S consists of just one coordinate. Every strip has some coordinate outside S, since otherwise it lies in H∩N_S. The residual remains on proper coordinate projections, each contributing at most one to the sum of 3- and 5-valuations. Counting the projected full-strip degrees therefore gives

 v₃(|H|)+v₅(|H|)≤2p+a+u−s+k_S,
 hence  a+s≤v+k_S.

Here singleton strips in the image are explicitly allowed; original corefreeness does not pass to that image. Each such strip meets S by original corefreeness. Its sole remaining coordinate cannot be fixed, since then the original strip would have two fixed coordinates, already excluded. Thus that coordinate belongs to a paired edge. Two such strips cannot occupy opposite ends of the same paired edge: choose involutions independently in the two strips. Their fixed coordinates in S allow arbitrary values in the selected class square, and the paired entries are conjugate involutions; every other coordinate is identity. This gives a nontrivial element of H∩Λ². Since distinct strips have disjoint supports, k_S≤min(s,p). Consequently

 v₃(W)+v₅(W)≥a+max(0,s−p)       for every S∈F.

This strengthens the original leaf count through actual stabilizer structure. It does not rule out every selected family, bound p, or show that τ pairs every coordinate. No new computation or general fixed-factor classification is claimed. The character and singleton-strip deductions have the independent exact-source reviews below.


### Independent review of the character deductions

reviewers `review_paired_simple`, `audit_c9_full` and `review_folder_criterion` independently accepted the full appended character section at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/a88ce90b600f86a03163e8867c924559015fc91f), conditional on the pinned canonical-folder, marked-support, A₅ subgroup and full-strip inputs. They checked the original-transversal group-algebra identity, extension and Schur scalar without τ(H)=H, the self-contained character values and outer traces, actual stabilizer projections and strip tensor invariants, component leaf restrictions, and the count allowing projected singleton strips with k_S≤min(s,p). Their scope includes the strengthened valuation bound and explicitly excludes general fixed-factor exhaustion. No new computation or primary-source audit was performed. These are independent model mathematical reviews, not human or formal certification.


## Exhaustion of every A5-power canonical group

**Independently reviewed classification under the pinned interfaces.** Let Q be a finite simple nonassociative left Bol loop whose full canonical left multiplication group is G≅A₅^r, r≥1. Under the canonical inversion and faithful-folder inputs stated above, r is even, say r=2k, and the canonical involution exchanges every simple factor with a different factor. Consequently the [reviewed paired A₅ classification](radical-free-a5-path-classification.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/ad94accf574f89bf1e8487bb046cf30fb685cd0c) applies: for each k≥1 there is exactly one loop-isomorphism class in this model, of order 60^k, with the A₄/C₅ path stabilizer. These loops are proper. The statement concerns the entire canonical group, not an A₅ composition factor or a quotient. The removal of the inversion hypothesis and final assembly have the exact-source independent reviews recorded below.

The proof uses the character section above, independently reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/a88ce90b600f86a03163e8867c924559015fc91f), and the earlier marked-support/Sylow constraints reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/59985c2e7450f7f800c4db0f8859b3a58669ee83). No new computation or external classification input is used.

### Every incidence component is a path with at most one fixed leg

Retain p paired coordinate pairs, a fixed inner/id coordinates and u fixed outer coordinates, so r=2p+a+u. Distinguish fixed coordinates with full H-projection from fixed coordinates with proper projection. The latter are all A₄ by the reviewed character argument. They are excluded from the following graph and retained globally in the proper-coordinate residual R; they are not being discarded or ruled out at this stage.

Use the paired-edge/full-strip incidence graph from the character section: its vertices are full strips and the proper coordinates belonging to paired edges. Each fixed coordinate with full projection is a leg on its strip. Every full strip belongs to an edge-containing component, since it has at least two coordinates and cannot contain two fixed coordinates. Every component has a proper A₄ leaf by the character argument.

For one connected component C let n count its paired edges, m its full strips, ℓ its proper paired leaves, a_C its fixed full inner/id legs, and u_C its fixed full outer legs. Its cycle rank is

 d=n−m−ℓ+1≥0,       ℓ≥1.

Let G_C be the normal coordinate quotient retaining exactly these paired edges and fixed full legs. The projected marked set is a product of the full paired classes, the unique outer fixed classes and a nonempty family of inner/id supports obtained by projecting and deduplicating F. Thus

 |K_C|=60^n10^{u_C}W_C≤60^n10^{u_C}16^{a_C}.

The equality |K_C| here counts a set, with no multiplicity inherited from supports outside C. The upper bound is the full sum (1+15)^{a_C}. The original transversal projects to a cover G_C=K_C H_C, regardless of whether the projection is a folder. Therefore |H_C|≥|G_C|/|K_C|, including when C contains all coordinates. Independence of the full strips gives |H_C|=60^m|R_C|, where R_C is the actual projection of the residual to its ℓ proper paired leaves. All proper A₅ subgroups have order at most 12, so |R_C|≤12^ℓ. Combining gives

 60≥5^ℓ60^d(15/4)^{a_C}6^{u_C}.                            (7)

No strict simplicity inequality is needed here. In particular, no exceptional treatment of a component equal to the whole group is required.

Since ℓ≥1, (7) forces d=0 and ℓ≤2. If ℓ=2, it forces a_C=u_C=0, since 25·(15/4)>60 and 25·6>60. If ℓ=1, the tree degree bound forces a_C+u_C≥1: the total paired degree of full vertices is 2n−1=2m−1, whereas each full strip has total coordinate degree at least two. Inequality (7) forces a_C+u_C≤1 because (15/4)²>12, (15/4)·6>12 and 6²>12. Hence exactly one fixed full leg occurs. Equality in the degree sum now makes every full strip have total coordinate degree two.

Every component is therefore one of two types: an ordinary path with two proper paired leaves and no fixed leg, or a path with one fixed full leg and one proper A₄ leaf. An ordinary path has at least one A₄ leaf. Its other leaf may or may not contain a factor five. Fixed proper coordinates, outside the graph, remain A₄.

### A global fifth-power divisibility obstruction

Let c be the number of ordinary paths, and let m_total be the total number of full strips. An ordinary path has one fewer full strip than paired edges, while a path with one fixed leg has equally many full strips and edges. Hence

 p−m_total=c.

The original stabilizer order is

 |H|=60^{p+a+u}/(10^u W),

so after splitting off its full strips the residual has

 v₅(|R|)=c+a−v₅(W).

Every proper fixed coordinate is A₄ and every fixed-leg path has one A₄ leaf, hence none contributes a factor five. Each ordinary path has an A₄ leaf and at most one other leaf; each proper A₅ subgroup has 5-part at most five. Consequently v₅(|R|)≤c, even if R correlates all its coordinates. Thus

 v₅(W)≥a.                                                  (8)

The parameter a in this global count includes all fixed inner/id coordinates, both full legs and proper A₄ projections. This is why the fixed proper coordinates may be omitted from the component graph but not from the global order.

Let s=max{|S|:S∈F}. The actual Sylow-two obstruction (5) gives v₂(W)≥u+2s≥2s. If a>0, (8) and coprimality of 2 and 5 imply

 4^s5^a≤W=Σ_{S∈F}15^{|S|}
          ≤4^s Σ_{S⊆{1,…,a}}(15/4)^{|S|}
          =4^s(19/4)^a<4^s5^a,

a contradiction. For the middle inequality, every selected S has |S|≤s, so 15^{|S|}≤4^s(15/4)^{|S|}; then enlarge to all subsets. This does not assume F is downward closed or a product family. Therefore a=0. The only support is now empty, W=1, and (5) forces u=0.

All simple factors are paired. Gauging the two-coordinate swaps gives the standard paired canonical model, and the cited A₅ theorem supplies its full construction and isomorphism classification. The proof also covers p=0: the component count is empty, all full strips would be impossible, and the same global residual valuation and support bounds contradict a>0 or u>0. No τ-normality of H, projected corefreeness, or quotient-loop assumption is used. Other simple types and mixed fixed-factor models remain outside this result.


### Independent review of the A5-power exhaustion

reviewers `review_paired_simple`, `audit_c9_full` and `review_folder_criterion` independently accepted the complete final section at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/67cced817f7d24e36d78990c73828ade4f218091), conditional on the pinned canonical-folder, marked-support, character, strip and paired A₅ classification inputs. They checked the component cover inequality without treating projected data as a folder, the fixed-proper/full bookkeeping, path reduction, global fifth-power bound, weighted-binomial contradiction, p=0 boundary, and assembly with the paired construction and isomorphism theorem. No new computation or primary-source re-audit was performed. These are independent model mathematical reviews, not human or formal certification. The result exhausts full canonical groups A₅^r; it does not exhaust arbitrary socles, mixed types or groups with radicals.


## Exhaustion of every PSL2(7)-power canonical group

**Independently reviewed under the pinned interfaces.** Let T=PSL₂(7) and let Q be a finite simple nonassociative left Bol loop whose full canonical left multiplication group is G=T^r, r≥1. Then r=2k and the canonical involution pairs every simple factor. Consequently the [reviewed paired classification](radical-free-small-psl2-paths.md#p7) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/184bc5f1b24d05d4dac1860060c6189afefda70c) gives exactly two loop-isomorphism classes for each k≥1, of order 168^k, with endpoint pairs (7:3,D₈) and (C₇,S₄). Both are proper. No assumption on the initial inversion action is imposed; arbitrary mixed simple types and radicals remain outside this theorem.

The canonical-folder, full-strip and original-transversal character identities are pinned above. The new character-table input is [Evans–Pugh, Table9](../foundations/references.md#evans-pugh-psl27-characters); the subgroup input is pinned in the small-PSL₂ source. Write G=T^(2p+a+u), where a and u count inner/id and outer fixed factors. Set P(z)=Σ_{S∈F}∏_{i∈S}z_i and W=P(21,…,21). The reviewed marked-support and Sylow-two constraints give |K|=168^p28^uW and v₂(W)≥u+3|S| for every selected S. Their proof above also realizes arbitrary involutions in each selected class square on active inner and outer fixed coordinates, and matched involutions on paired coordinates. Proper fixed coordinates remain in the actual residual even though they are outside the incidence graph. No τ-normality of H, projected folder, or independence of proper projections is assumed.

The self-dual, Aut(T)-invariant irreducibles of degrees 6,7,8 have inner active class-sum scalar 7,-3,0 and outer scalar 0,±4,±7 respectively; their inactive inner weights are 1. Paired edge scalar is 168/d. The 6 representation is the deleted 7-point action; the 7 representation is deleted projective 8-point action. Proper inner fixed projections are C7 or 7:3: degree 6 has nonzero scalar, so the projection must be transitive on 7 points; use the cited proper subgroup classification. Both groups fix a nonzero vector of degree7. Tensor squares of the three representations contain 1, even with automorphism twists.

### One fixed leg per strip

No original full strip contains two fixed inner coordinates: degree6 on both gives a strip-invariant tensor and strictly positive support scalar. No strip contains two fixed outer coordinates: degree8 on both yields an invariant and nonzero scalar.

No strip contains an inner coordinate i and outer coordinate j. With degree8 on i,j, strip invariants force P(0_i,21_else)=0 because the outer scalar is nonzero; all terms are nonnegative, so every selected S contains i. With degree7 on i,j, strip invariants force P(-3_i,21_else)=0; but under that conclusion every term is strictly negative, contradiction. Thus every full strip has at most one fixed coordinate, and by core-freeness must meet a paired edge.

### Component cover and elimination of leafless components

Use the original full-strip/paired-edge incidence graph: each full strip is a vertex, each proper paired coordinate is a separate leaf, and each paired edge joins the corresponding vertices. Attach each fixed full coordinate as a leg. For a connected component C put m=number full strips, p_C=number paired edges, ell=number proper leaves, a_C/u_C=number inner/outer fixed legs, and c=p_C−m−ell+1≥0. The actual projected cover H_C K_C=G_C and proper subgroup order ≤24 imply

  168 ≥ 7^ell 168^c (168/22)^a_C 6^u_C.                   (*)

Indeed |G_C|=168^(2p_C+a_C+u_C), |K_C|≤168^p_C·22^a_C·28^u_C, |H_C|≤168^m·24^ell, and p_C−m=ell−1+c. A strip has total degree at least two.

Suppose ell=0. Let D be its inner fixed legs. Label all paired coordinates and all fixed legs of C by degree8. Since every strip has at least two selected coordinates, its representation has an invariant; the outer8 scalar is nonzero and the inner8 scalar is zero when active. Consequently P(0_D,21_else)=0, so every selected support intersects D. Here dim(8^⊗d)^T=(8^d+56(-1)^d+48)/168>0 for d≥2. Conversely no selected S contains D: pick nonidentity involutions independently on all strips of C. Every paired edge has two conjugate involutions; every outer leg admits an involution in the outside-class square; and every inner leg is active. Independent conjugation within the selected global outside class makes their product a nonidentity element of H∩Λ². Thus 1≤|S∩D|≤|D|−1 for every S. If |D|=2, label C by degree7 instead: dim(7^⊗d)^T=(7^d+56+63(-1)^d)/168>0, while every term in P(-3_D,21_else) is strictly negative, contradicting the resulting character-zero equation. Therefore |D|≥3. But (*) then implies 168≥(168/22)^3>168, contradiction. Hence ell≥1.

With ell≥1, (*) forces c=0, ell≤2, and at most one fixed leg; if ell=2 it forces no fixed leg. The degree bound gives ell+a_C+u_C≥2, so every component is a path with either two proper leaves and no fixed leg, or one proper leaf and exactly one fixed leg. No independence of residual leaf projections has been asserted.

### Degree-7 moments on every inner coordinate

A proper inner fixed coordinate has projection C7 or 7:3. For an inner fixed full leg i, label every coordinate of its component (the fixed leg and both ends of every paired edge) by degree6. The support scalar is strictly positive, and every full strip contributes an invariant. Its unique proper leaf must have no degree6 invariant, so it is C7 or 7:3. The component cover with |K_C|≤22·168^p_C implies that leaf's order is at least 168/22>7, hence it is 7:3.

Fix any nonempty J⊆[a]. Put degree7 on each i∈J. For each i that is a full leg, also put degree7 on the entire paired-coordinate path of its component; put trivial representations elsewhere, including every outer coordinate. Every touched strip has degree7⊗degree7 and an invariant. Each touched leaf/proper fixed projection is C7 or 7:3, hence fixes a degree7 vector. Their tensor remains invariant under the correlated proper-coordinate residual; tensoring with the strip invariants yields an H-invariant. The τ-stable irreducible is nontrivial, hence

 P(-3 on J,21 elsewhere)=0 for every nonempty J⊆[a].      (**)

Define μ(S)=21^|S|/W for S∈F and 0 otherwise. Equation (**) says E_μ∏_{i∈J}f_i=0 for all nonempty J, where f_i=1 on i∉S and -1/7 on i∈S. Since {1,f_i} is a basis of functions on one bit, these mixed moments uniquely determine μ as independent Bernoulli(7/8) coordinates. For a>0 that distribution has positive mass on all supports, so F is the whole Boolean lattice; but its actual μ is independent Bernoulli(21/22), contradiction. Thus a=0. Then F={∅}, W=1, and v₂(W)≥u forces u=0.

All factors are therefore paired, and the cited paired theorem supplies construction and the exact isomorphism count. The proof covers p=0: all fixed full strips are impossible once each strip has at most one fixed coordinate, and the same proper-coordinate moment argument and Sylow bound apply. No prime-valuation lower bound is inferred from individual proper projections. The exact-source reviews are recorded below.


### Independent review of the PSL2(7)-power exhaustion

reviewers `review_paired_simple`, `audit_c9_full` and `review_folder_criterion` independently accepted the entire PSL₂(7)-power proof and two-class assembly at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/4e99b12bc07d8e6b35e1960f42b83b05e8666f84), conditional on the pinned canonical-folder, selected-mark-square/Sylow, strip, subgroup and paired-classification inputs. Each checked the mixed-strip exclusion, actual component cover, all leafless cases, proper/full bookkeeping, degree-6 leaf identification, correlated-residual degree-7 mixed moments, the probability contradiction, p=0 and final removal of outer factors. Each independently inspected Evans–Pugh's 24 January2020 author PDF, §4.3 Table9, printed p.22/PDF index22; the cited class sizes and character traces agree. They did not reprove the character or subgroup classifications or rerun the older GAP certificate. These are independent model mathematical/source reviews, not human or formal certification or a classification of arbitrary socles and radicals.


## Fermat-prime canonical groups

**Independently reviewed under the pinned interfaces.** Let p≥17 be a prime such that p−1 is a power of two, and put T=PSL₂(p). There is no finite simple nonassociative left Bol loop whose full faithful canonical left multiplication group is T^r, for any r≥1. This statement uses the canonical-folder, inversion and strip inputs pinned in [the fixed-factor source](radical-free-fixed-factors.md), together with the [paired PSL₂ classification](radical-free-psl2-path-classification.md#all-field-paired-psl-assembly). It is confined to the full canonical group, not arbitrary PSL₂ composition factors or overgroups.

Write N=|T|=p(p²−1)/2, B=p−1=2^e, w=p(p+1)/2 and v=p(p−1)/2. Let τ exchange h pairs of factors, fix a factors with inner or identity restrictions, and fix u factors with outer restrictions. On each fixed inner/identity factor the two T-classes of outside involutions have sizes 1 and w. On each fixed outer factor there is one such class of size v, and on each pair there is one of size N. To see the outer assertion, Aut(T)=PGL₂(p), the split projective involutions are inner because −1 is a square, while the nonsplit involutions form the outer class, with centralizer of order p+1 in T. The general PGL₂(p) involution classes and centralizers are given by Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Appendix Lemma A.3, printed p.1355, [published PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf). Its PGL centralizer orders are 2(p−1) and 2(p+1), and the PSL centralizers have half those orders. The determinant identification above distinguishes the classes. Wong's Lemma1(a), used earlier for PSL₂(7), concerns that specific field and is not used for this general-p assertion.

As there, conjugacy invariance of Λ=tK gives a nonempty family F⊆2^[a] of selected supports, without multiplicity, such that

    |K|=N^h v^u W,     W=Σ_{S∈F}w^|S|.                         (1)

The class t^G is selected. This is a statement about the actual global marks, not a projected folder.

### Character and incidence components

Let χ be the deleted permutation character of T on the projective line. The doubly transitive action makes χ irreducible of degree p; it is real, self-dual, and invariant under Aut(T)=PGL₂(p). Its value on inner involutions is 1; its natural extension to PGL₂(p) has value −1 on the outer involution class. The group-algebra argument in [the fixed-factor character section](radical-free-fixed-factors.md#character-obstructions-on-the-original-stabilizer) applies to the actual transversal H: for any nontrivial τ-stable irreducible tensor representation on which the Λ class sum has nonzero scalar, its H-fixed space vanishes. No τ-normality of H is assumed.

Label each fixed coordinate by 1 or χ and both coordinates of each pair by the same one of these characters. The class-sum scalar is a product of nonzero pair and outer factors times Σ_{S∈F}∏_{i∈S}z_i, where z_i=w if coordinate i is labeled 1 and z_i=w/p if it is labeled χ. This polynomial is strictly positive. The pair factor follows from matrix-coefficient orthogonality, and an outer χ label contributes −v/p. Arbitrary pair twists can be gauged using the τ-identification; every automorphism preserves χ.

Consequently every proper fixed-coordinate projection of H acts transitively on the projective line: an intransitive projection fixes a nonzero vector of χ. Moreover, no full strip of H contains two fixed coordinates, since the invariant bilinear form gives an H-fixed vector when just those coordinates are labeled χ.

For every d≥2, χ^⊗d contains the trivial character. The invariant bilinear form settles d=2. For d≥3, every nonidentity value of χ is in {−1,0,1}, and the sum of character values is at least p^d−(N−1)>0. Build the paired-edge/full-strip incidence graph as in [the A₅ argument](radical-free-fixed-factors.md#incidence-components-require-specific-proper-leaves). Its vertices are full strips and proper coordinates occurring on pairs; fixed full coordinates are legs. Each full strip lies in an edge-containing component, because its support has at least two coordinates and it has at most one fixed leg. Every such component has a proper paired leaf acting transitively on the projective line: otherwise label that entire component by χ and tensor fixed vectors on its strips and on its proper leaves, contradicting the nonzero scalar. This allows arbitrary correlations among proper-coordinate projections.

Every proper subgroup J<T has |J|≤M=p(p−1)/2, and every proper p-bearing subgroup is intransitive on the projective line. Indeed the latter has Borel type by Dickson's classification; its Sylow p-subgroup is normal and its unique projective fixed point is therefore J-invariant. For the order bound compare the Borel and the dihedral and exceptional types, whose exceptional orders are at most 60. The subgroup input is Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Annals of Mathematics 172 (2010), Appendix Theorem A.1, printed p.1354, [published PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf); see also Lemma A.3, p.1355. The original classification is not reproved here.

Fix a component with n paired edges, m full-strip vertices, ℓ proper paired leaves and b fixed full legs. Its cycle rank d=n−m−ℓ+1 is nonnegative and ℓ≥1. Projecting the original cover G=KH to the component gives a cover, without asserting a projected folder. The projected marked set has size at most N^n(1+w)^b, because v≤1+w; the projected stabilizer has size at most N^m M^ℓ. Hence

    N ≥ (N/M)^ℓ N^d (N/(1+w))^b.                            (2)

Here N/M=p+1>p−2 and N/(1+w)>p−2. Equation (2) forces d=0, and then ℓ+b≤2 because (p−2)^3>N for p≥17. The tree degree sum, using strip support size at least two, gives ℓ+b≥2. Thus each component is a path: it has either two proper paired leaves and no fixed leg, or one proper paired leaf and one fixed leg. Every path has a transitive, hence p-free, proper paired leaf. Proper fixed-coordinate projections, kept outside this graph, are also transitive and p-free.

### Global p-valuation and Sylow-two parity

Let c be the number of paths with two proper paired leaves, and m_total the number of full strips. The paths give h−m_total=c. The full strips split off from the residual R of H on proper coordinates. In particular this remains valid when a proper projection is isomorphic to A₅: it is not necessary for all proper projections to be solvable. By Goursat, any coupling to a full T strip would require T as a quotient of the residual; every composition factor of a subgroup of the product of proper projections is a section of one of those projections, each of order strictly smaller than |T|. Thus no such T quotient occurs, and the same argument splits the full strips successively. Using (1), v_p(N)=v_p(v)=1, so

    v_p(|R|)=c+a−v_p(W).

Each ordinary path contributes at most one p-bearing leaf, while fixed-leg paths and fixed proper coordinates contribute none. Product-of-projection orders bound even a correlated R, and hence v_p(|R|)≤c. Therefore

    v_p(W)≥a.                                                   (3)

Fix S∈F. We show

    v₂(W)≥e|S|+u.                                              (4)

The square of the selected global outside class contains every involution whose fixed coordinates outside S are identity, and whose two entries on each paired orbit are simultaneously identity or nonidentity. The two selected marks may be independently conjugated in every coordinate. On a paired orbit the class square consists of pairs with conjugate inverse entries, so it contains every pair of involutions because T has one involution class. On an active inner/identity fixed factor, the square of the inner involution class contains all involutions: a dihedral Sylow 2-subgroup contains two distinct commuting involutions, and T has one involution class. For an outer factor, let a be a nonsplit projective involution and b the involution induced by Frobenius on F_{p²}/F_p. In PGL₂(p), a and b commute, a and ab are outer involutions, and b is a nonidentity inner involution (det b=−1 is a square). Thus the outer class square also contains the unique T-class of involutions. Inactive fixed coordinates are kept equal in the two marks, producing identity there.

Let P be a Sylow 2-subgroup of H. Its order has 2-valuation eh+ea+u−v₂(W), since v₂(N)=e and v₂(v)=e−1. Count elements of P of order at most two satisfying the support condition modulo two. For each paired orbit use the indicator 1+e_L+e_R over F₂, where e_L,e_R are identity indicators; for each inactive fixed coordinate multiply by its identity indicator. Expanding gives counts of elements of order at most two in kernels of coordinate projections imposing all inactive fixed coordinates and at most one coordinate of each pair. Every such projection target has order at most 2^[e(h+a−|S|)]. If (4) failed, every kernel would be a nontrivial 2-group, and its number of elements of order at most two, including identity, would be even by inverse pairing. The support-conditioned count would consequently be even. It includes identity, so there would be a nonidentity element of H∩Λ², contrary to transversality. This proves (4) using actual H, without any independence of its projections.

Let s=max_{S∈F}|S|. If a>0, equations (3) and (4) imply W≥B^s p^a. But

    W=Σ_{S∈F}w^|S| ≤ B^s(1+w/B)^a < B^s p^a,

because |S|≤s and 1+p(p+1)/(2(p−1))<p for p≥5. This contradiction gives a=0. Then W=1, and (4) forces u=0. Therefore τ pairs every factor. The cited paired table excludes these Fermat-prime folders via its other-q≡1 mod4 row: its exceptional q=5 and q=29 are not Fermat primes p≥17. This also covers h=0: the graph is empty and the global argument applies to the proper fixed projections.


The first exact-source review of this section at [the source revision](https://github.com/Mira-Cult/math-wip/commit/608f466340e94a0da0cad32ebf59bc7d54b23d94) requested correction of a general-p attribution: `review_paired_simple` found that Wong's cited lemma only covers F₇. The citation is corrected above to Guralnick–Zieve Lemma A.3; the mathematical argument is unchanged. The repaired text has the exact-source acceptances below.


### Independent review of the Fermat-prime exclusion

reviewers `review_paired_simple`, `audit_c9_full` and `review_folder_criterion` independently accepted the complete repaired theorem at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/65e41f88de8c18c09f7090677242ead5a0403719), conditional on the pinned canonical-folder, inversion, strip, subgroup and paired-classification inputs. Their full mathematical reviews covered the class weights and squares, character positivity and tensor invariants, transitive p-free leaves, separation of full strips even with proper A₅ projections, actual component cover and path count, global p-valuation, explicit Sylow-kernel parity argument, weighted-binomial contradiction and h=0. Each inspected Guralnick–Zieve Appendix Lemma A.3, printed p.1355, and confirmed the corrected general-q source. The two earlier conditional acceptances at [the source revision](https://github.com/Mira-Cult/math-wip/commit/608f466340e94a0da0cad32ebf59bc7d54b23d94) did not catch the citation defect; the requested correction and its resolution are preserved above. No new computation or independent proof of the external classifications was performed. These are model mathematical/source reviews, not human or formal certification, and the result concerns the entire canonical group only.


## Odd prime canonical groups with p congruent to 3 mod 4

**Independently reviewed under the pinned inputs.** Let p≥11 be a prime with p≡3 mod 4, and put T=PSL₂(p). If a finite simple nonassociative left Bol loop has full faithful canonical left multiplication group G=T^r, r≥1, then r is even and its canonical involution pairs all simple factors. The [paired PSL₂ classification](radical-free-psl2-path-classification.md#all-field-paired-psl-assembly) therefore gives the corresponding complete list of loop-isomorphism classes. This concerns the full canonical group, not an arbitrary composition factor or overgroup. The proof uses the faithful-folder, canonical-inversion, actual-transversal and full-strip inputs pinned in [the fixed-factor source](radical-free-fixed-factors.md). The source and independent-review qualifications are stated below.

Write N=|T|=p(p²−1)/2, w=p(p−1)/2 and v=p(p+1)/2. Suppose the canonical involution τ exchanges h pairs of coordinates, fixes a coordinates with inner or identity restrictions, and fixes u coordinates with outer restrictions. Its outside involution classes have local sizes 1,w on an inner/identity fixed coordinate, v on an outer fixed coordinate, and N on each pair. Indeed, inner involutions are nonsplit and outer involutions split; the PGL involution classes and centralizers are given in Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Annals of Mathematics 172 (2010), Appendix Lemma A.3, printed p.1355, [published PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf), with the determinant calculation distinguishing the classes. Conjugacy invariance of Λ=tK therefore gives a nonempty family F⊆2^[a] of selected supports without multiplicity and

    |K|=N^h v^u W,     W=P(w,...,w),     P(z)=Σ_{S∈F}∏_{i∈S}z_i.    (1)

As in [the fixed-factor source](radical-free-fixed-factors.md#global-sylow-two-obstruction-for-selected-supports), outside-class squares contain the unique T-class of involutions on each active inner or outer fixed coordinate, and contain each pair of involutions on a paired orbit. For completeness put e=v₂(p+1)=v₂(N). Then v₂(v)=e−1 and w is odd, so |Syl₂(H)|=2^{e(h+a)+u−v₂(W)}. For a selected support S the kernel expansion using 1+e_L+e_R on each pair and identity on every inactive fixed coordinate has projection targets of order at most 2^{e(h+a−|S|)}. If v₂(W)<u+e|S|, every kernel is a nontrivial 2-group with an even involution count including identity, producing a forbidden nonidentity H∩Λ² element. Thus v₂(W)≥u+e|S|≥u. The inner class square contains involutions by two commuting involutions in a Sylow2 subgroup; the outer split class uses the commuting projective matrices diag(−1,1) and [[0,1],[1,0]], both of nonsquare determinant, whose product is an inner involution. No independence of H-projections is used. All uses below concern the actual stabilizer H and transversal, not a projected folder.

### Three characters and a subgroup lemma

Choose a primitive character θ of the nonsplit torus C_m of T, where m=(p+1)/2. It satisfies θ(involution)=−1 and θ≠θ⁻¹. The corresponding degree-(p−1) cuspidal character χ is 2 on involutions, −1 on nonidentity p-elements, 0 on nonidentity split semisimple elements, and −θ(x)−θ(x)⁻¹ on nonidentity nonsplit torus elements. The values and irreducibility are the R′(θ) row of [Böhmler–Farrell–Lassueur, §2.5 Table1, printed p.10](../foundations/references.md#bohmler-farrell-lassueur-ordinary-characters), with the following PSL-center convention. Inflate the primitive nonsplit T-torus character to the norm-one torus of SL₂(p); it is trivial on −1, so the character descends. The original character classification is not reproved here.

The character χ is real and self-dual. It is Aut(T)=PGL₂(p)-invariant: PGL₂(p) preserves every semisimple T-class and may fuse the two unipotent classes, on which χ has the same value. On an active inner fixed coordinate its outside-class scalar is 2w/(p−1)=p, and on an inactive coordinate it is 1. Thus a τ-stable tensor with paired coordinates equally labeled 1 or χ, inner fixed coordinates labeled 1 or χ and outer coordinates labeled 1 has scalar a positive nonzero product times P(z), with every z_i equal to w or p. Pair twists cause no difficulty because χ is Aut(T)-invariant.

For a second character, take a primitive linear character λ of F_p^×, induce the character λ(a/d) of the upper triangular Borel of PGL₂(p), and restrict the resulting representation to T. The restriction η has degree p+1 and is irreducible: Mackey's two Borel double cosets give norm one because λ restricted to the square subgroup is not self-inverse. It is Aut(T)-invariant by construction and self-dual because the Weyl element inverts the parameter. The induced-character fixed-line formula gives value 0 on an inner nonsplit involution and −2 on the outer split involution diag(−1,1). Thus its active inner class scalar is zero and its outer class scalar is nonzero.

The third character St is the deleted permutation character on the projective line. It is irreducible, real, self-dual and Aut(T)-invariant, with degree p and value −1 on an inner nonsplit involution. Its natural PGL extension has value 1 on the outer split involution. Thus its active inner scalar is −w/p=−(p−1)/2 and its outer scalar is nonzero.

Every p-free proper subgroup J<T has a χ-fixed vector, and every p-bearing proper subgroup fixes a St-vector. The latter follows from Dickson's list: a proper p-bearing subgroup has a normal Sylow p-subgroup and lies in its Borel normalizer, so it fixes the Sylow subgroup's unique projective point. For the former, Dickson puts J in a torus normalizer or makes |J|≤60. A p-free subgroup of a Borel also lies in a split-torus conjugate: its affine action has a fixed point by averaging an orbit in F_p, since its order is prime to p. On the split normalizer of order p−1, the χ-average is 2: its odd-order split torus contributes p−1 at identity and zero elsewhere, and its (p−1)/2 reflections each contribute 2. On the nonsplit normalizer of order p+1, the torus sum is p+1 because θ is nontrivial, and the (p+1)/2 reflections each contribute 2; again the average is 2. Every proper subgroup of a torus normalizer consequently has a χ-fixed vector.

For the exceptional groups, all nonidentity χ-values are at least −2. Counting the three involutions of A₄ and the nine of S₄ gives character sums at least p−11, positive for p≥19. At p=11, S₄ is absent and χ has value 1 on the eight order-three elements of A₄, giving sum 24. For A₅, its 15 involutions give a lower bound p−59, positive for p≥67. Dickson's congruence criterion leaves p=11,19,31,59 below 67. A nonsplit element of order three has χ-value 1; for nonsplit elements of order five the two class values sum to 1, since θ is primitive. At those four primes, respectively, only order 3 is nonsplit, only order 5 is nonsplit, both are split, and both are nonsplit. The A₅ character sums are 60, 60, 60, and 120. Thus they are positive. The subgroup types and congruences used here are Dickson's classification in Guralnick–Zieve, Appendix Theorem A.1, printed p.1354; the classification is not reproved here. Every proper subgroup has order at most

    M=max{p(p−1)/2,60},     N/M>p−1.                           (2)

In particular M=60 at p=11, where the Borel has order 55; for p≥19, M=p(p−1)/2.

### Fixed strips and incidence components

The actual-transversal character obstruction from [the fixed-factor source](radical-free-fixed-factors.md#character-obstructions-on-the-original-stabilizer) says that a nontrivial τ-stable irreducible tensor with nonzero Λ class-sum scalar has no H-fixed vector. It does not assume τ(H)=H. Each of χ, η and St is Aut(T)-invariant and self-dual, so its tensor square, even with a strip twist, has an invariant.

No original full strip of H contains two inner fixed coordinates: put χ on them, giving a strip invariant and a positive support scalar. No full strip contains two outer fixed coordinates: put η on them. Nor can a strip contain one inner fixed coordinate i and one outer fixed coordinate j. Label i,j by η; the invariant and the zero active inner scalar imply P(0_i,w_else)=0, so every selected support contains i. Label i,j instead by St. The invariant now forces P(−(p−1)/2_i,w_else)=0, but every summand is strictly negative. Thus every full strip has at most one fixed coordinate. Since its support has at least two coordinates, it meets a paired edge.

Use the original full-strip/paired-edge incidence graph as in [the PSL₂(7) proof](radical-free-fixed-factors.md#component-cover-and-elimination-of-leafless-components): strip vertices and proper paired-coordinate leaves, with fixed full coordinates as legs. For a component C write n for its paired edges, m for its strips, ℓ for its proper paired leaves, b for all fixed full legs and d=n−m−ℓ+1≥0 for its cycle rank. Projecting the actual cover G=KH to C and applying (2) gives

    N ≥ (N/M)^ℓ N^d (p−1)^b.                                  (3)

Indeed, if b_inner and b_outer count the two kinds of fixed legs, then |K_C|≤N^n(1+w)^b_inner v^b_outer. Each inner leg contributes N/(1+w)>p−1 and each outer leg contributes N/v=p−1. Also |H_C|≤N^m M^ℓ. These are set and subgroup bounds for the actual projections; no projected corefreeness or folder structure is used.

If ℓ+b>0, (3) forces d=0. If ℓ+b=0, it forces d≤1. In the latter case d=1 is impossible: label both ends of every paired edge in the cycle by χ. Every strip has exactly two selected coordinates, hence an invariant, and the class-sum scalar is positive. When d=0, (3) and (p−1)^3>N force ℓ+b≤2, while the strip degree sum gives ℓ+b≥2.

If ℓ=0, the component is therefore a path with exactly two fixed legs and every strip has total coordinate degree two. If both legs are inner, label the whole component by χ; if both are outer, use η. In either case every strip has an invariant and the scalar is nonzero. If the legs are mixed, first label the component by η to force every selected support to contain its sole inner leg, then label by St to obtain a strictly negative scalar, as in the two-coordinate argument. All cases contradict the transversal obstruction. Thus ℓ≥1. Each component is a path with either two proper paired leaves and no fixed leg, or one proper paired leaf and one fixed leg.

### Leaf control and mixed moments

A proper inner fixed coordinate has p-bearing H-projection: otherwise it fixes a χ-vector, contradicting the positive scalar for χ on that coordinate. For a path with a fixed inner full leg, label the leg and both coordinates of every paired edge on that path by χ. Every strip has an invariant. If the sole proper leaf had a p-free projection, the subgroup lemma would supply a χ-fixed vector there; their tensor would be H-fixed, again contradicting the positive scalar. Hence that leaf is p-bearing. In both cases its projection lies in a Borel and has a St-fixed vector. Proper fixed coordinates remain in the residual even though they are outside the incidence graph.

Let J be any nonempty set of inner/identity fixed coordinates. Label each coordinate in J by St. Whenever one is a full leg, label both coordinates of every pair in its path by St as well; put the trivial label elsewhere. Each touched full strip has exactly two St factors and an invariant, while every touched proper projection has a St-fixed vector. The tensor of these vectors is fixed by the actual residual even if its coordinate projections are correlated; the full strips split off as in the cited strip decomposition. Thus the entire nontrivial τ-stable tensor has an H-fixed vector, and the scalar obstruction gives

    P(−(p−1)/2 on J, w elsewhere)=0.                           (4)

Define μ(S)=w^|S|/W for S∈F and 0 otherwise. Equation (4) says that E_μ∏_{i∈J}f_i=0 for every nonempty J, where f_i is 1 on inactive supports and −1/p on active supports. The products of 1 and these one-coordinate functions form a basis on the Boolean cube. The moment equations therefore force μ to be the independent Bernoulli distribution with activation probability p/(p+1). For a>0 this has positive mass on every support, so F is the whole Boolean lattice. But the actual weighted distribution for the full lattice has activation probability w/(1+w), which is unequal to p/(p+1) because w≠p. Hence a=0. Now W=1 and the Sylow-two bound v₂(W)≥u gives u=0. Every factor is paired.

The argument includes h=0: there are no full strips, and the same moments apply to the proper inner fixed projections. The p=7 case is already treated in [the PSL₂(7)-power theorem](radical-free-fixed-factors.md#exhaustion-of-every-psl27-power-canonical-group). No computation or claim about arbitrary nonprime fields is used.


### Independent review of the odd-prime three-mod-four exhaustion

reviewers `review_paired_simple`, `audit_c9_full` and `review_folder_criterion` independently accepted the full integrated theorem at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/21a5eb2d9f6e8a6547de0a8734b1c6ae94417f92), conditional on the pinned canonical-folder, strip, character, subgroup and paired-classification inputs. They checked the primitive cuspidal parameter and character deductions, direct principal-series extension, all p-free subgroup averages including the small exceptional cases, p=11 order bound, selected-mark Sylow parity, mixed strips, all leafless/cover cases, correlated-residual Steinberg moments, h=0 and the paired assembly. `audit_c9_full` directly inspected Böhmler–Farrell–Lassueur's stated preprint and Guralnick–Zieve's relevant appendix statements. `review_paired_simple` inspected the BFL table and following convention through an [institutional mirror](https://oa.tib.eu/renate/bitstreams/b17bf1bd-f53c-4460-81b5-1b8e94e2d25c/download) after the MFO URL timed out, and had inspected Guralnick–Zieve. `review_folder_criterion` attempted the MFO fetch, which timed out, and relied on the recorded table inspection. None independently reproved the character or subgroup classifications or reran prior GAP certificates. No new computation was performed. These are model mathematical/source reviews, not human or formal certification.


## Odd prime canonical groups with p congruent to 1 mod 4

**Independently reviewed under the pinned inputs.** Let p≥13 be prime with p≡1 mod 4 and let G=PSL₂(p)^r, r≥1, be the full faithful canonical left multiplication group of a finite simple nonassociative left Bol loop. If p≠29, no such loop exists. If p=29, every simple factor is paired by the canonical involution, and the [paired classification](radical-free-psl2-path-classification.md#all-field-paired-psl-assembly) gives one proper loop-isomorphism class for each r=2h≥2, with endpoint pair (29:7,A₅). This concerns the full canonical group, not arbitrary overgroups or composition factors. The proof uses the canonical-folder, inversion, actual-transversal and full-strip interfaces pinned in [the fixed-factor source](radical-free-fixed-factors.md).

### Nonexistence away from p=29

Let T=PSL₂(p), N=|T|=p(p²−1)/2, and χ be the deleted character of its doubly transitive action on P¹(F_p), of degree p. Thus χ is irreducible, real, self-dual and PGL₂(p)-invariant, with χ(x)=#Fix(x)−1. Every nonidentity x has χ(x)∈{−1,0,1}. Involutions of T are split because p≡1 mod4, so χ=1 on that class. An outer PGL₂ involution is nonsplit, so its trace in the natural PGL extension is −1. For every d≥2 the tensor power χ^⊗d has a T-invariant: d=2 by self-duality; d≥3 because the character sum is ≥p^d−(N−1)>0. The same holds for factors twisted by arbitrary automorphisms because χ is Aut(T)-invariant.

Label every coordinate of G by χ, giving a nontrivial τ-stable irreducible G-representation. Let t induce τ and Λ=tK as in the reviewed fixed-factor manuscript. In a fixed inner/id coordinate the two outside conjugacy classes have scalar weights 1 and w/p>0, with w=p(p+1)/2; at a fixed outer coordinate the unique outside class has scalar −v/p≠0, with v=p(p−1)/2; and each paired orbit contributes N/p≠0. Hence the scalar of the actual conjugacy-invariant Λ class sum is a nonzero product of the outer and paired terms and the strictly positive support polynomial P(w/p,...,w/p). This remains true for any selected nonempty support family and arbitrary pair twists. By the actual-transversal group-algebra argument in [the fixed-factor character section](radical-free-fixed-factors.md#character-obstructions-on-the-original-stabilizer), the tensor representation has no H-fixed vector.

On the other hand H has an H-fixed vector if each proper coordinate projection is intransitive on P¹. The reviewed full-strip decomposition splits H into independent full T strips and a residual subgroup on proper coordinate projections. Every full strip has support size d≥2 and has an invariant in its d χ factors, including when twisted; every intransitive proper projection fixes a nonzero vector in its deleted permutation representation. Taking the tensor of these local vectors is invariant even under a correlated residual. This contradicts the nonzero class-sum scalar. Thus existence of a folder forces a proper transitive subgroup J<T on P¹. This is a useful general criterion for p≡1 mod4, not dependent on a particular support family or on τ(H)=H.

Dickson excludes such a subgroup in the stated range. The precise input is Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Annals of Mathematics 172 (2010), Appendix Theorem A.1 and Lemma A.3, printed pp.1354–1355, https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf (the theorem was directly inspected; the original classification was not reproved). Prime-field proper subgroups are Borel subgroups and their subgroups, split or nonsplit torus normalizers and subgroups, or A₄, S₄, A₅. Borels fix a point. A split normalizer has order p−1 < p+1. A nonsplit normalizer has order p+1; if it were transitive it would act regularly, but it contains a nonidentity involution, and every T-involution is split and fixes two projective points. Hence it is not transitive, nor is a subgroup of it. For an exceptional group to be transitive, p+1 divides 12, 24 or 60. Under p≥13 and p≡1 mod4 this leaves only p=29 (p+1=30). Thus for all stated primes every proper projection is intransitive and the contradiction applies.

The exclusion leaves p=29, where a proper transitive A₅ can occur and the paired classification has the (29:7,A₅) path. The p=5 case is the A₅-power case treated separately.


### Fixed-factor exhaustion at p=29

Put T=PSL₂(29), N=12180=2²·3·5·7·29, w=435, v=406, and M=406. Let h, a, u count paired orbits, fixed inner/id coordinates and fixed outer coordinates. The actual selected support polynomial W=Σ_{S∈F}435^|S| satisfies |K|=N^h406^uW. Its Sylow-two bound, obtained by the kernel argument in [the global Sylow-two support bound](radical-free-fixed-factors.md#global-sylow-two-obstruction-for-selected-supports), is

  v₂(W) ≥ u+2|S|  for each S∈F.                                  (1)

The local class-square requirements for that parity proof hold: at an active inner fixed factor the square of the involution class contains all involutions, since the dihedral Sylow 2-subgroup contains two commuting distinct involutions and all T-involutions are conjugate; the outer outside involution class square also contains all inner involutions, using a nonsplit outer involution and an inner normalizer involution as in the Fermat-prime section; paired class squares contain matched involutions. v₂(N)=2 and v₂(v)=1.

The deleted projective-line character St has degree 29, active inner scalar 435/29=15 and outer scalar −406/29=−14. It is irreducible, Aut(T)-invariant and real. Every τ-stable tensor with St on both coordinates of selected paired orbits and on any chosen fixed coordinates has scalar a nonzero pair/outer factor times a positive support polynomial, as in the previous section. Its tensor powers in degrees ≥2 have invariants, including under strip twists: use self-duality for degree two, and |St(g)|≤1 off identity to bound the character sum for degree at least three.

St on any two fixed coordinates prohibits them from belonging to one original full strip; hence each full strip has at most one fixed coordinate and meets some paired edge. As in the reviewed A5/PSL₂(7) fixed-factor proof form the original strip/paired-edge graph and attach fixed full legs. Every component C has a proper paired leaf whose projection is transitive on P¹: otherwise label all its paired coordinates and fixed legs by St; all strips and all intransitive proper leaves admit fixed vectors, contradicting the nonzero scalar. A proper fixed-coordinate projection must likewise be transitive.

The subgroup analysis in the preceding section shows that every proper transitive subgroup is A₅: a Borel or torus normalizer is intransitive, and p+1=30 does not divide 12 or 24. All proper subgroup orders are at most M=406 by Dickson; notably A₅ has order 60. For a component with n paired edges, m full strips, ℓ proper paired leaves, a_C inner legs, u_C outer legs, and cycle rank d=n−m−ℓ+1, the projected original cover gives

  N ≥ 30^ℓ N^d (N/436)^a_C 30^u_C.                            (2)

Here |K_C|≤N^n436^a_C406^u_C, counting distinct projected marks, and |H_C|≤N^m406^ℓ. As ℓ≥1, (2) forces d=0; all of 30, N/436 and 30 exceed 27, and 27³>N, so ℓ+a_C+u_C≤2. Tree degree sum gives the reverse inequality. Every component is therefore a path, either with two proper leaves and no fixed leg, or one proper leaf and one fixed leg. Every proper fixed coordinate and the proper leaf of each fixed-leg path has projection A₅; no independence of residual coordinates has been assumed.

Let ψ be the degree-28 cuspidal character from a primitive parameter θ of the nonsplit T-torus C₁₅. It is irreducible, real, self-dual and PGL₂(29)-invariant. Its value on inner involutions is 0, because they are split; on nonsplit order-three elements it is 1, and the sum of its values on the two order-five classes is 1. Thus its A₅-fixed dimension is

  (28 + 15·0 + 20·1 + 12·1)/60 = 1.

The general character formula and irreducibility are [Böhmler–Farrell–Lassueur, §2.5 Table1 and following center convention](../foundations/references.md#bohmler-farrell-lassueur-ordinary-characters). Inflate θ from C₁₅ to the norm-one torus of SL₂(29); it is trivial on its center and gives a PSL character. The PGL invariance is elementary from the displayed character values: PGL preserves semisimple T-classes and fuses only the two unipotent classes, which have the same character value.

Fix any inner/id coordinate i. Label it by ψ. If it is a full leg, additionally label both coordinates of every paired edge in its fixed-leg path by ψ; all other coordinates, including all outer fixed factors, receive the trivial representation. Every touched strip has exactly two ψ factors and an invariant, and every touched proper coordinate has projection A₅ and hence a ψ-fixed vector. These individual vectors remain invariant under any correlated proper-coordinate residual; the full strips split off by the pinned decomposition. Therefore the full τ-stable tensor has an H-fixed vector. Its Λ scalar is a nonzero paired factor times P(0_i,435_else), so the actual-transversal obstruction gives P(0_i,435_else)=0. All terms are nonnegative, so every selected support contains i.

Applying this to each inner fixed i makes every selected support equal the full set of a coordinates. Therefore W=435^a is odd. Formula (1) for this support forces a=u=0. Thus τ pairs every factor; the reviewed paired PSL₂(29) classification supplies the (29:7,A₅) path class, one for each h≥1. This is not a no-loop theorem: these paired path loops exist and are proper according to the cited classification.


## Prime-field assembly without an inversion hypothesis

**Independently reviewed assembly under the pinned inputs.** For every prime p≥5 and r≥1, a finite simple nonassociative left Bol loop with full canonical left multiplication group PSL₂(p)^r has r=2h and paired canonical inversion. Its complete construction and loop-isomorphism list is therefore exactly the prime-field restriction of [the reviewed paired table](radical-free-psl2-path-classification.md#all-field-paired-psl-assembly) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e30af949531c0ebcc9f7533b04fc1e7fc6858563), with no initial inversion-action hypothesis. Every listed class is proper and has order |PSL₂(p)|^h. The dependencies are the reviewed A₅-power and PSL₂(7)-power exhaustion, the odd-prime three-mod-four theorem reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/21a5eb2d9f6e8a6547de0a8734b1c6ae94417f92), and the preceding one-mod-four theorem (including p=29). No prime p≥5 is omitted. This is a full classification for these entire canonical groups; it does not classify their overgroups, mixed socles, nonprime fields or radical extensions.


### Independent review of the prime-field completion

reviewers `review_paired_simple`, `audit_c9_full` and `review_folder_criterion` independently accepted both the one-mod-four proof (including p=29) and the all-prime assembly at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/3dd83d3983cbc62b8e8b467339f77656efd01bb8), conditional on the pinned canonical-folder, strip, character, subgroup and paired-classification inputs. They checked the global deleted-character argument and twisted-strip invariants, the proper-transitive subgroup exclusion, p=29 cover and path bookkeeping, its degree-28 A₅ average and zero-evaluation argument, the actual mark-square/Sylow bound, and complete routing of every prime p≥5. They also checked the clarification that the Fermat-prime argument uses the paired table's other-q≡1 mod4 row, preserving its p=5 and p=29 exceptions. `review_paired_simple` and `audit_c9_full` relied on their earlier direct BFL and Guralnick–Zieve inspections; `review_folder_criterion` retained the previously recorded BFL fetch limitation. No fresh source reproof, computation or rerun of upstream GAP certificates was performed. These are independent model mathematical reviews, not human or formal certification or an exhaustion of arbitrary canonical groups.


## Odd prime-power canonical groups with q congruent to 1 mod 4

**Independently reviewed under the pinned inputs.** Let q≥5 be an odd prime power with q≡1 mod 4 and q∉{5,9,29}. No finite simple nonassociative left Bol loop has full faithful canonical left multiplication group G=PSL₂(q)^r for any r≥1. No restriction on the canonical involution's factor action is imposed. This concerns the full canonical group, not an arbitrary overgroup or composition factor. The proof uses the canonical-folder, actual-transversal and full-strip interfaces pinned in [the fixed-factor source](radical-free-fixed-factors.md), together with Dickson's classification and Aut(PSL₂(q))=PΓL₂(q). The exceptions q=5,9,29 are outside this result.

Let χ be the deleted natural permutation character on P¹(F_q), degree q. It is irreducible by double transitivity, real and invariant under Aut(T). Every nonidentity element of T fixes at most two projective points, so its χ-value is 0 or ±1. Thus (χ^⊗d)^T≠0 for every d≥2: self-duality handles d=2, and the character sum for d≥3 is ≥q^d−(|T|−1)>0. As in the preceding prime-field argument, if all proper H-coordinate projections are intransitive, their χ-invariants together with strip tensor invariants give an H-fixed vector even with arbitrary correlations in the proper residual.

Label every coordinate of G by χ. Choose the natural PΓL action as the extension on each fixed factor, and the natural interchange (with τ's coordinate identification) on paired factors. The class sum of Λ=tK acts by a nonzero scalar. Indeed, the paired orbit scalar is |T|/q. On a fixed coordinate with no field part, an inner or identity restriction gives outside elements acting as either the identity or inner involutions; their χ traces are q or 1, since q≡1 mod4. A diagonal-outer restriction gives outside projective involutions in PGL₂(q)\T; these are nonsplit and have trace −1. Thus all contributing classes at such a coordinate have the same nonzero sign.

If the field part is nontrivial, it is necessarily the involution σ:x↦x^{q0}, with q=q0². Every local outside involution has the same χ trace q0, positive, even if there is more than one T-conjugacy class. To prove this, write it Aσ in PΓL₂(q). Its square is projectively trivial, so Aσ(A)=cI. Applying σ and using this identity yields c∈F_{q0}^×. Choose λ∈F_q^× with λσ(λ)=c^−1, using surjectivity of the norm; after replacing A by λA, the associated σ-semilinear linear operator squares to 1. Choose δ∈F_q^× with σ(δ)=−δ. If V is the two-dimensional F_q-space and B=Aσ, every v∈V has the unique decomposition v=x+δy with x=(v+Bv)/2 and y=(v−Bv)/(2δ), both B-fixed. Hence V=V^B⊕δV^B as F_{q0}-spaces, so dim_{F_{q0}} V^B=2, and any F_{q0}-basis of V^B is an F_q-basis of V. In this basis B=σ. Its fixed projective points form P¹(F_{q0}), so there are q0+1 and its deleted permutation trace is q0. This is a direct argument, not a claim that all local outside involutions are one T-class.

Every global selected outside class is a product of local classes; independent conjugation and Schur's lemma make its scalar a nonzero product of positive local terms and a sign contributed solely by each no-field diagonal-outer factor. This sign is constant across all selected classes. Thus their sum is nonzero and the actual-transversal group-algebra identity forbids an H-fixed vector. Therefore any such folder forces a proper T-subgroup transitive on P¹(F_q).

Dickson rules out a proper transitive subgroup outside {5,9,29}. The exact input is Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Annals of Mathematics 172 (2010), Appendix Theorem A.1 and Lemmas A.2–A.3, printed pp.1354–1355, [published PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf). A subgroup of Borel type with nontrivial p-part has a normal nontrivial p-subgroup, whose unique common projective fixed point it preserves; a p-free subgroup of Borel type is cyclic of order at most (q−1)/2. Thus both are intransitive. The split normalizer has order q−1; the nonsplit normalizer has order q+1 but, if transitive, would act regularly, whereas any of its nonidentity involutions is a T-involution, split because q≡1 mod4, and fixes two points. Exceptional A₄,S₄,A₅ require q+1 to divide 12,24,60; with odd q≡1 mod4 and q≥5, the only resulting q are 5,9,29. For an actual subfield subgroup with field size q0, write q=q0^d, d≥2. Its order is at most |PGL₂(q0)|=q0(q0²−1). If d≥3 this is strictly less than q+1. If d=2 then gcd(q0²+1,q0(q0²−1))=2, so q+1 cannot divide its order. Thus no subfield subgroup acts transitively, including PGL subfield groups and arbitrary subgroups thereof. Dickson's list is an isomorphism-type classification, but order divisibility is sufficient for the excluded cases; the Borel-type cases are handled using their normal p-subgroup or order as above.

Consequently every proper projection is intransitive, giving the H-fixed vector and contradiction. In particular this covers all q=p^(2k) except q=9 and includes field automorphisms of order two; it does not settle q=9 or p=29, and it does not assert fixed-point-freeness where proper transitive subgroups exist.


### Independent review of the odd-square-field exclusion

reviewers `review_paired_simple`, `audit_c9_full` and `review_folder_criterion` independently accepted the complete odd q≡1 mod4 theorem at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/c722d73e0eee35e4c9df6f1bd7e8cf8f5e99d7ae), conditional on the canonical-folder, full-strip, PΓL automorphism and Dickson inputs. They checked the norm rescaling and direct fixed-basis proof for every semilinear involution, its q0+1 projective fixed points, the constant nonzero sign across all selected outside classes without assuming one field class, twisted-strip and correlated-residual invariants, every proper-subgroup type, exceptional q list, and the quadratic-subfield gcd and higher-degree order bounds. `review_paired_simple` and `audit_c9_full` retained their earlier Guralnick–Zieve inspections; none reproved the external classifications or ran a new computation. These are independent model mathematical reviews, not human or formal certification. The theorem retains precisely its stated q=5,9,29 exceptions.


## Odd nonprime fields with q congruent to 3 mod 4

**Independently reviewed under the pinned inputs.** Let q=p^f be an odd prime power with f≥3 odd and q≡3 mod 4, and put T=PSL₂(q). If a finite simple nonassociative left Bol loop has full faithful canonical left multiplication group G=T^r, r≥1, then its canonical involution pairs every simple factor. The [all-field paired PSL₂ classification](radical-free-psl2-path-classification.md#all-field-paired-psl-assembly) supplies the corresponding Borel/nonsplit-normalizer path class. The statement concerns the full canonical group, not arbitrary overgroups or composition factors. It uses the canonical-folder, actual-transversal, marked-square and strip interfaces pinned in [the fixed-factor source](radical-free-fixed-factors.md), Dickson's classification and the character formulas below.

Write N=q(q²−1)/2, w=q(q−1)/2, v=q(q+1)/2; let h,a,u count paired orbits, fixed inner/id and fixed diagonal-outer factors. Since f is odd and Out(T) has cyclic field quotient of order f, an involutory fixed-factor automorphism has trivial field part. The outside classes and support polynomial have weights 1,w, v and N respectively, as in the odd-prime section.

Characters, with twists tracked. Let χ_θ be the degree q−1 cuspidal character for a primitive character θ of the nonsplit torus C_m of T, m=(q+1)/2. It is real, self-dual, PGL₂(q)-invariant, and its values are q−1 at 1, −1 at nonidentity p-elements, 0 at split semisimple elements, and −θ(x)−θ(x)^−1 at nonidentity nonsplit torus elements. Its involution value is 2, since m is even and θ is primitive. This and the analogous principal-series values are in [Böhmler–Farrell–Lassueur, §2.5 Table 1, printed p.10, row R′(θ), and the following PSL-center convention](../foundations/references.md#bohmler-farrell-lassueur-ordinary-characters), at the exact preprint pin recorded there. The original classification is not reproved. Its active inner class scalar is 2w/(q−1)=q>0. All field conjugates again have primitive parameters and the same values needed below, though χ_θ itself need not be field-automorphism invariant.

Let η be a degree q+1 principal character induced from a primitive split-torus character, chosen by restricting the PGL Borel induction. It is real, self-dual and PGL-invariant; its inner-involution value is 0 and its outer-involution trace is −2. All its field conjugates have the same properties. Let St be the deleted natural projective-line character, degree q, Aut(T)-invariant; its inner value is −1 and its outer trace +1. As in the prime proof, the actual-transversal scalar obstruction applies to any τ-stable tensor of irreducibles; its applicability does not require H to be τ-stable. Fixed restrictions are PGL, so every χ_θ or η field conjugate has an extension at that fixed coordinate.

Subgroup lemma. Every proper subgroup outside a Borel fixes χ_θ, and the same is true of every field conjugate of χ_θ. Dickson's types are in Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Annals 172 (2010), Appendix Theorem A.1, printed p.1354, https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf. A split or nonsplit torus normalizer has χ-average 2 by exactly the computations in the odd-prime proof. For any exceptional subgroup J of order at most 60, the sum is ≥q−1−2(|J|−1)>0 for q≥243. The only smaller q in scope is 27: A₅ and S₄ are absent by Dickson's congruences; in A₄ the three involutions have value 2 and the eight elements of order 3 are unipotent with value −1, giving sum 26+6−8=24.

For a subgroup J≅PSL₂(r) of subfield type, write q=r^d with d≥3 odd, so r≡3 mod4. This argument applies to every actual embedding, not merely the standard subfield matrices. Under an abstract identification of J, its split and nonsplit torus orders are (r−1)/2 and (r+1)/2. The identities gcd(r−1,q+1)=gcd(r+1,q−1)=2 force each nonidentity odd-order split element to be ambient split, and each nonidentity nonsplit element to be ambient nonsplit; the unique involution class is nonsplit in both groups and is handled separately. For r>3, a generator of the embedded nonsplit torus has order at least four and its ambient centralizer is cyclic, so that entire torus lies in an ambient nonsplit torus. The primitive ambient parameter θ restricts primitively to its subgroup of order (r+1)/2. Transport this restriction through the chosen abstract identification to define θ_r. Conjugacy of the nonsplit tori inside J then identifies the character values on every such J-element; all nontrivial p-elements have value −1 regardless of their unipotent class. Thus the following comparison needs no conjugacy theorem for subfield embeddings. The r=3 case is verified directly below from its involutions and elements of order three. The ambient and smaller-field cuspidal values agree on every nonidentity element of PSL₂(r): split and nonsplit types are preserved by odd-degree extension, and p-elements have value −1. At identity the degrees differ by q−r. Consequently, as class functions,

  χ_q|PSL₂(r) = χ_r + [2(r^(d−1)−1)/(r²−1)]·ρ_reg.        (1)

The bracket is a positive integer, because d is odd. For r>3, χ_r is the corresponding irreducible cuspidal character. For r=3, χ_r is instead the sum of the two nontrivial linear characters of A₄=PSL₂(3): its values are 2 on identity and involutions, and −1 on order-three elements. Thus (1) is a genuine character with a regular summand in every case, so χ_q has fixed vectors on PSL₂(r) and all its subgroups. For a Borel-type subgroup in Dickson’s isomorphism-type list, a nontrivial normal p-subgroup fixes a unique projective point, so the subgroup lies in its Borel normalizer. If its p-subgroup is trivial, it is cyclic of order dividing (q−1)/2 and lies in a split torus and hence in a Borel. Dickson's PGL₂(r) subfield type requires even extension degree and does not occur when f is odd. This also applies to each field conjugate of θ. Any proper projection with no χ-fixed vector must therefore lie in a Borel, and hence has a St-fixed vector. Use this precise Borel conclusion: a p-bearing proper subgroup can be a subfield subgroup, and need not lie in a Borel.

Twisted-path bookkeeping. A tensor representation may be labeled by different field conjugates of χ or η in different coordinates. Along a paired orbit transport the label through τ's isomorphism to make the G-irreducible τ-stable; along a full strip transport the label through the strip isomorphisms to make its tensor square have an invariant. On a path these constraints are compatible by propagation from one endpoint; no automorphism holonomy is assumed trivial. Every transported χ has inner active scalar q>0 and every transported η has zero inner active scalar and nonzero outer scalar. Outer coordinates are fixed by PGL-type involutions, so these transported labels remain locally τ-stable. The St representation is Aut-invariant, so its path transport is automatic.

No full strip contains two fixed inner coordinates (transport χ across the strip and obtain positive support scalar), two fixed outer coordinates (transport η), or one of each (η forces P(0_i,w_else)=0, then St produces a strictly negative scalar). This uses only two fixed labels and no path. Thus each full strip meets a paired edge.

Build the original full-strip/paired-edge incidence graph with proper-coordinate paired leaves and fixed full legs. Every proper subgroup has order at most M=q(q−1)/2: all torus and exceptional bounds are below it, and every subfield subgroup has order at most r(r²−1)<r³≤q. For a connected component with n paired edges, m strips, ℓ proper leaves, b fixed legs and d=n−m−ℓ+1, projection of the actual cover gives

 N ≥ (q+1)^ℓ N^d (q−1)^b.                                  (2)

For inner fixed legs the factor is N/(1+w)>q−1 and for outer it is N/v=q−1. If ℓ+b>0 then d=0; if ℓ=b=0 then d≤1. A leafless cycle with d=1 is impossible without needing a character around the cycle: independently choose a nonidentity involution in every full strip. All paired coordinates then form matched conjugate involutions and all coordinates outside the component are identity, producing a nontrivial H∩Λ² element. Local squares have the needed involutions: on a paired orbit as above; on an active inner fixed coordinate by commuting involutions; on an outer split involution class by a=diag(−1,1), b=[[0,1],[−1,0]] in PGL₂(q): a,ab are outer split involutions and b is an inner involution.

With d=0 the degree sum gives ℓ+b≥2, while (q−1)^3>N and (2) give ℓ+b≤2. If ℓ=0 then there are exactly two fixed full legs and the component is a path. Transport χ along it if both are inner, or η if both outer; their nonzero scalars contradict H-fixed tensors. If the ends are mixed, transport η first to force every selected support to contain the inner leg, then use St on the path to force a strictly negative scalar, contradiction. Thus ℓ≥1 and each component is a path with two proper leaves, or one proper leaf and one fixed full leg. The path-only transport avoids any field-holonomy assumption.

Every proper inner fixed projection is Borel-contained: χ has positive scalar there and the subgroup lemma. For an inner fixed full leg, transport χ along its entire fixed-leg path. Every strip tensor has an invariant; if its sole leaf were not Borel-contained, the subgroup lemma supplies a χ-fixed vector for that leaf, contradicting the positive scalar. Thus it too is Borel-contained. Correlations in the proper residual do not affect these implications.

For every nonempty J of inner fixed coordinates, label them by St and extend across each selected fixed-leg path using St on both ends of every pair. Each strip and each proper touched projection has a St-fixed vector, so the actual H fixes their tensor. The class-sum equation is P(−(q−1)/2 on J,w elsewhere)=0. Under μ(S)=w^|S|/W this gives vanishing mixed moments of 1 versus −1/q. The Boolean basis forces independent activation probability q/(q+1), hence F is the full support lattice; its actual weights instead give probability w/(1+w)≠q/(q+1). Hence a=0. Then W=1, and the [reviewed global Sylow-two kernel count](radical-free-fixed-factors.md#global-sylow-two-obstruction-for-selected-supports) yields v₂(W)≥u, since v₂(N)=v₂(q+1) and v₂(v)=v₂(q+1)−1. Thus u=0. All factors are paired.


An exact-source review at [the source revision](https://github.com/Mira-Cult/math-wip/commit/c1ba37928b08362867e66e826b11ecbb93b51a45) requested the explicit arbitrary-embedding justification, since the cited Dickson list alone states abstract subgroup types. The order, centralizer and internal-torus argument above supplies that step. Independent model reviewers contributor 1, contributor 2, and contributor 3 accepted the repaired section at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/ff6d4cbe2e351e253aa014d636102305c80076d9), conditional on its pinned folder, Dickson and character-table inputs. Each checked the added arbitrary-embedding step; their earlier full-scope reviews remain conditional as stated. No new computation or formal GitHub approval was performed.


## Even-field canonical groups without an inversion hypothesis

**Independently reviewed under the pinned inputs.** Let q=2^f with f≥3. If the entire faithful canonical left multiplication group of a finite simple nonassociative left Bol loop is G=PSL₂(q)^n, then n is even and the canonical inversion exchanges every simple factor in pairs. Consequently the reviewed [all-field paired classification](radical-free-psl2-path-classification.md#all-field-paired-psl-assembly) supplies the complete loop-isomorphism list for these q. Together with the separately reviewed q=4 case in [the A₅-power theorem](radical-free-fixed-factors.md#exhaustion-of-every-a5-power-canonical-group), this covers all even fields q≥4 for these entire canonical groups. It does not cover mixed socles or overgroups.

We use the faithful generated-folder and normal-quotient interfaces [C0001](../../claims/0001.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45), the canonical inverting automorphism and conjugacy-invariant outside marks [C0007](../foundations/C0007.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813), the full-strip decomposition in [the strip-forest source](radical-free-strip-forests.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6d3a97daa9cf20bbae0416295c8c2374c2cd8ede), and the actual-transversal character identity and strip/paired-edge graph in [the fixed-factor source](radical-free-fixed-factors.md#character-obstructions-on-the-original-stabilizer). The selected-mark Sylow counting uses the [support-parity mechanism](radical-free-involution-support.md#support-parity-lemma) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e30af949531c0ebcc9f7533b04fc1e7fc6858563). These inputs retain their stated source and CFSG qualifications.

Write T=PSL₂(q)=PGL₂(q), N=|T|=q(q²−1). All T-involutions form one class of size w=q²−1, and a Sylow 2-subgroup is elementary abelian of order q. The subgroup input is Dickson's theorem as stated in Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Annals of Mathematics 172 (2010), Appendix Theorem A.1 and Lemmas A.2–A.3, printed pp.1354–1355, https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf. The source statements were inspected; the original classification was not re-proved.

Let h count paired orbits of simple coordinates, a fixed coordinates with identity or inner restriction, and b fixed coordinates with nontrivial field restriction. When f is odd, b=0. When f is even write q=r², r=2^(f/2), and let σ be the order-2 field automorphism. Every involution in Tσ is T-conjugate to σ: if Aσ is an involution then Aσ(A)=cI with c∈Fr*. Surjectivity of the norm Fq*→Fr* allows scalar rescaling to obtain a semilinear operator F with F²=1. Choose δ∈Fq with δ+δ^r=1. For every v, both v+F(v) and δv+δ^rF(v) are F-fixed, and v is their Fq-linear combination; these fixed vectors contain an Fq-basis, in which F=σ. As T=PGL₂(q), this is T-conjugacy. The centralizer is PSL₂(r), so the class has size v=N/|PSL₂(r)|=r(q+1). Its square contains every inner involution: choose an involution u∈PSL₂(r); both σ and uσ lie in this outside class, and their product is u.

For a selected global support family F⊆2^[a], the actual outside-class union therefore has

 |K|=N^h v^b W,   W=Σ_{S∈F}w^|S|,                                  (1)

with the factor v^b absent when b=0. The global Sylow-2 kernel count of the reviewed support argument gives, for every S∈F,

 v₂(W)≥f|S|+(f/2)b.                                               (2)

On active inner/id fixed coordinates the involution-class square contains every involution: any nonzero member of an elementary abelian Sylow subgroup is a product of two distinct nonzero members. On field coordinates the preceding paragraph supplies the same inclusion; on paired coordinates the outside-class square contains matched pairs of involutions. Count actual involutions in a Sylow subgroup of H with inactive fixed coordinates equal to 1 and matched support on every paired orbit, exactly as in the support-parity source. The projection-kernel estimate yields (2), including all residual correlations. The term (f/2)b occurs only for even f.

### Principal-series and subgroup inputs

If f is odd choose θ of order q−1 on a split torus. If f is even choose θ of order r−1. Let χ=R(θ), the real irreducible principal-series character of degree q+1. [Farrell–Lassueur, *Trivial source character tables of SL₂(q), Part II*, arXiv:2205.01401v2, §3.2 Notation 3.3 and Table 1](../foundations/references.md#farrell-lassueur-even-characters) gives χ(u)=1 on involutions, χ(t)=θ(t)+θ(t)^−1 on nonidentity split semisimple t, and χ=0 on nonsplit semisimple elements. The same table gives the Steinberg character St of degree q, with St(u)=0. St is the deleted permutation character on P¹(Fq), is invariant under all automorphisms, and has a fixed vector for every subgroup of a Borel. The character table and labels were directly inspected, not independently re-proved.

For even f, θ is σ-invariant. Realize χ as Ind_B^T θ with the natural σ-extension. The σ-fixed cosets of B are the r+1 points of P¹(Fr), and representatives over Fr introduce no torus multiplier, so χ(σ)=r+1>0. The same holds after any field twist of θ. All local outside involution traces for these principal-series choices are strictly positive: q+1 or 1 on fixed identity/inner restrictions, and r+1 on field restrictions. Principal-series χ is generally NOT invariant under the whole field-automorphism group. Along any selected tree or simple path below, transport the characters and their duals through the actual strip twists and paired-coordinate identifications; their degree and the relevant positive traces remain the same. No transport around a cycle is assumed.

Every proper J<T that is not Borel-contained has a χ-fixed vector. For the two torus normalizers, averaging the displayed table values gives fixed dimension 1, so all their subgroups have fixed vectors. When f is odd, A4 is excluded by Dickson and S4 and A5 by its congruence conditions. When f is even, A4 is Borel-contained: its normal V4 lies in a unique elementary abelian Sylow 2-subgroup, whose unique common projective fixed point is then A4-stable. S4 is impossible because elements of T have order either 2 or odd. The A5 case will be checked below. Dickson's remaining subfield case is handled for actual embeddings as follows.

Suppose J≅PSL₂(s) with q=s^d, d≥2. If d is odd, gcd(s−1,q+1)=gcd(s+1,q−1)=1, so every cyclic torus of J of order s−1 is split in T and every cyclic torus of order s+1 is nonsplit in T, regardless of how J is embedded. The split torus is T-conjugate to a subgroup of a fixed split torus, and θ restricts to some character β of its order-(s−1) cyclic group. The even-characteristic table then gives equality on every element:

 χ|_J = χ₀ + ((q−s)/|J|)·regular(J),                             (3)

where χ₀=R(β) if β≠1, and χ₀=1+St_J if β=1. For s=2 use χ₀=1+St of S3. The coefficient is integral because d is odd. Thus χ|_J contains the trivial character. This proves the needed property for every embedding; no unverified conjugacy of subfield subgroups is used. If d≥4 is even, the identity contributes q+1 and every other χ-value has absolute value ≤2, so q+1−2(|J|−1)>0 for s≥2 and χ^J≠0, independently of the embedding.

For d=2, put s=r. All elements of J whose orders divide r±1 are split in T. Its r+1 torus lies in ker θ because gcd(r+1,r−1)=1. On its r−1 torus θ restricts primitively, since the embedding in the q−1 torus uses exponent r+1≡2 mod r−1. From the intrinsic even-characteristic PSL₂(r) class counts, the total character sum is

 (r²+1)+(r²−1)−r(r+1)+r²(r−1)=r³−r=|J|,

so dim χ^J=1. Again no conjugacy assumption on J is needed.

For A5 when f is even, q=16 is the preceding quadratic r=4 case, since A5≅PSL₂(4). For q=64 the order-3 elements are split and θ-trivial, the order-5 elements are nonsplit, and the average is (65+15+20·2+24·0)/60=2 for every embedding. For q≥256, q+1−2(60−1)>0 gives a fixed vector for every embedding. Hence every χ-no-fixed-vector proper subgroup is Borel-contained in both parity regimes. The exceptional and subfield cases are treated as actual representations, not simply as a list of abstract subgroup types.

### Strip graph and fixed legs

Each original full strip contains at most one fixed coordinate. Otherwise place dual transported principal-series representations on two fixed coordinates of that strip and the trivial representation elsewhere. The strip supplies an H-invariant tensor, while every selected outside-class scalar is positive. This contradicts the actual-transversal class-sum identity. Therefore every full strip occurs in an edge-containing component of the original paired-edge/strip graph; fixed full coordinates are attached as legs and proper paired coordinates as leaves.

A component with n paired edges, m full strips, ℓ proper paired leaves, z fixed full legs, and cycle rank d=n−m−ℓ+1≥0 obeys

 N ≥ (q+1)^ℓ N^d (q−1/q)^z.                                    (4)

Indeed the projected cover G=KH gives |K_C|≤N^n q^(2z) because both 1+w=q² and v≤q², and |H_C|≤N^m[q(q−1)]^ℓ. Dickson's list supplies q(q−1) as an upper bound on proper subgroup orders. These bounds apply to the actual projected sets and groups; no projected-folder assertion or independence assumption occurs.

If ℓ≥1, (4) forces d=0 and ℓ+z≤2, since (q+1)(q−1/q)²>N for q≥8. The tree degree sum gives ℓ+z≥2. Thus the component is a path with either two proper leaves or one proper leaf and one fixed leg. If ℓ=0,d≥1, (4) forces d=1,z=0, an all-strip degree-two cycle; independent involutions on its strips give an element of H∩K², impossible. If ℓ=0,d=0, the tree degree sum forces at least two fixed legs. Choose a simple path between two of them, label its paired edges and fixed endpoints with transported dual principal representations, and label everything else trivially. Every touched strip has exactly two dual factors and an invariant, while the selected outside-class scalar is positive. This contradicts the transversal identity and does not require a tensor-cube calculation or field-invariance of χ. Thus every component has a proper leaf and is one of the two path types.

Place χ on a proper fixed coordinate, with all others trivial. Positivity forces its actual H-projection to have no χ-fixed vector; the subgroup lemma makes it Borel-contained. For a fixed-leg path, place transported dual principal labels on the fixed leg and all paired coordinates of the path. If its sole proper leaf had a χ-fixed vector, the strip pairings and that leaf vector would give an H-fixed tensor; other residual coordinates are trivial, so correlations are harmless. Positivity again contradicts the transversal identity. The leaf projection is therefore Borel-contained.

### Steinberg support forcing

For each fixed identity/inner coordinate i, label it by St and, if it is a full leg, label all paired coordinates of its path by St. The touched strips have dual invariant pairings and the touched proper fixed/leaf projection is Borel-contained and has a St-fixed vector. Thus H fixes a nonzero tensor. The τ-stable selected-class scalar must vanish. Supports active at i contribute trace 0; those inactive at i contribute q. Paired factors contribute positive N/q, and field factors contribute St(σ)=r>0, by the projective-line action and the unique outside class. Every summand is nonnegative, so every selected support contains i. Repeating for all a inner/id factors forces F to consist only of their full set and W=w^a, an odd integer. Applying (2) gives 0≥fa+(f/2)b, hence a=b=0. For odd f the same conclusion uses b=0 and no field term. Every simple factor is therefore paired, as claimed. The construction and orbit list are those of the cited reviewed paired classification. Independent exact-source reviews are recorded below.


## Elimination of fixed A₆ factors

**Independently reviewed under the pinned inputs.** A deduction under [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Assume the faithful generated canonical left multiplication group G=A6^r, r≥1, with arbitrary canonical τ. Use the canonical-folder, marked scalar, full-strip and support-parity interfaces of the reviewed A5 fixed-factor source `radical-free-fixed-factors.md` at the recorded source revision, the full-strip decomposition at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6d3a97daa9cf20bbae0416295c8c2374c2cd8ede), the global Sylow-two kernel argument in this manuscript, and the paired q=9 exclusion in [the all-field paired PSL₂ source](radical-free-psl2-path-classification.md#all-field-paired-psl-assembly) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e30af949531c0ebcc9f7533b04fc1e7fc6858563). The group-theoretic inputs below are explicitly identified; the independent exact-source reviews retain their qualifications. No statement about full multiplication groups or larger almost-simple overgroups is made.

### A₆ classes and characters

A6≅PSL₂(9), and Out(A6)=C2². The inner involutions form one class of size 45; diagonal outer involutions form one class of size 36. The field outer involutions form two A6-classes of size 15 each, and the diagonal-field coset contains no involutions. For the latter assertions write σ:x↦x³ on F9. Matrix Hilbert 90, allowing projective rescaling, makes every involution in PGL₂(9)σ PGL₂(9)-conjugate to σ. Its PGL centralizer is PGL₂(3), of order 24: a σ-fixed projective matrix can be scalar-rescaled to an F3 matrix by scalar Hilbert 90. Its determinant lies in F3* and hence is a square in F9*, so the centralizer lies in T=PSL₂(9). The PGL class has 720/24=30 elements and splits into two T-classes of size 15. Every member lies in σT because det(B/σB)=det(B)^{-2} is a square. Thus the other diagonal-field coset contains no involution. Each field involution fixes a conjugate of P¹(F3). The inner and diagonal class identifications and automorphism-group input retain their exact subgroup/source qualifications.

Let χ be the irreducible degree-nine deleted permutation character of the action on P¹(F9). Its extension to Aut(A6)=PΓL₂(9) has trace 1 on inner involutions, −1 on diagonal outer involutions, and 3 on either field-outer class. The field assertion follows from the fixed four-point projective line of F3 and fusion of the two classes by PGL₂(9). It is Aut(A6)-invariant. Since the action is 2-transitive, χ is irreducible and real self-dual, so χ² has an invariant. For every d≥3, the character sum has positive numerator: χ(1)^d=9^d>359, whereas the absolute value of χ on every nonidentity element is at most 1. Hence dim(χ^d)^A6>0 for every d≥2.

Dickson's theorem at the Guralnick–Zieve Appendix Theorem A.1 locator cited above shows that the only proper 5-bearing subgroup types are C5, D10 and A5. Every other proper subgroup has order not divisible by ten and is intransitive on P¹(F9), so has a χ-fixed vector. The group C5 is too small to be transitive; if D10 acted transitively it would act regularly, but its involutions lie in the unique A6-involution class and fix two projective points. Consequently a proper projection without a χ-fixed vector must be A5. This implication is all that is required below. The inner/diagonal involution classes and automorphism input are Guralnick–Zieve, Appendix Lemma A.3 and the automorphism paragraph following Lemma A.4, together with the explicit field calculation above. The semilinear descent used there is also proved in the preceding odd-square-field section at source [the source revision](https://github.com/Mira-Cult/math-wip/commit/c722d73e0eee35e4c9df6f1bd7e8cf8f5e99d7ae).

For any subgroup L≅A5, its index-six coset action is faithful because A6 is simple. Its image has order 360 and is therefore A6 in S6. The action is 2-transitive, so its deleted permutation character χ_L has degree five, is irreducible, real and self-dual, and has an L-fixed vector. Every A6-involution is a double transposition in this six-point action, so χ_L has trace 1 on the unique inner involution class. Automorphisms transport χ_L to the corresponding coset character of the transported A5 subgroup. No classification or count of the degree-five characters or A5 conjugacy classes is required.

### Every paired A₆ component has an A₅ leaf

The full-coordinate image of H is a product of disjoint full diagonal A6 strips. It splits from the residual projection by Goursat: every proper coordinate projection has order less than 360, so the residual, filtered by coordinate kernels, has no A6 composition factor or quotient. This argument allows the proper nonsolvable A5 projections. Corefreeness makes each strip use at least two coordinates. No full strip contains two fixed coordinates: label exactly those two coordinates by χ, transporting by the strip automorphisms. The paired tensor has a strip-invariant vector because χ is Aut(A6)-invariant and self-dual; the other factors are trivial. The selected-mark scalar has a constant nonzero sign on both fixed coordinates, giving a contradiction to the scalar obstruction. Consequently every full strip meets a paired edge. On any fixed coordinate, χ has a nonzero scalar on the actual selected mark union: the inner/id contributions are positive, field-outer contributions are positive, and diagonal-outer contributions have a fixed negative sign independent of the selected class. On each τ-paired edge the corresponding swap scalar is positive. Thus the tensor χ-label on all coordinates of a paired-edge incidence component, with trivial labels elsewhere, has nonzero selected-mark scalar regardless of correlations among selected classes. Each full strip in the component has an invariant tensor, as proved above. If it had no A5 proper leaf, every proper leaf would also have a χ-fixed vector, giving an H-fixed vector. This contradicts the reviewed scalar obstruction. Hence every component has an A5 leaf. Fixed proper-coordinate projections are likewise A5, by labeling just that fixed coordinate with χ.

### Inner/id fixed A₆ coordinates are impossible

If a fixed inner/id coordinate has proper H-projection A5, choose its index-six coset character χ_L, and label every other coordinate trivially. Its selected-mark scalar is strictly positive: the weight-one local class contributes 1 and the 45-element involution class contributes 45·1/5=9. Its local character is τ-stable since τ is inner. This contradicts the scalar obstruction.

If instead a fixed inner/id coordinate belongs to a full strip, choose a simple path in its paired-edge incidence component from that strip to an A5 proper leaf. Choose at the leaf its index-six coset character χ_L, and transport its label along each paired edge via τ and through each full strip via the defining strip automorphisms. Along this simple path exactly two coordinates of each traversed full strip are labeled; choose their representations contragredient so their tensor has a strip-invariant vector. Since the transported degree-five representations are real and self-dual, this transport is possible; no fixed labeling or classification of the character family is required. The terminal fixed coordinate is τ-stable because its τ restriction is inner. Label every off-path coordinate trivially. The fixed-coordinate local scalar is again positive, while every paired-edge swap scalar is positive. Their tensor contains an H-fixed vector: residual projections may be correlated, but the chosen leaf vector is individually fixed by its entire projection. Contradiction. Thus a=0 for the number a of fixed inner/id coordinates.

### Sylow-two parity eliminates outer fixed A₆ coordinates

Let p count paired A6 factors, u fixed diagonal-outer factors and v fixed field-outer factors. Since a=0, the actual selected global mark union is indexed only by a nonempty set D⊆{0,1}^v of field-class choices. Put W=|D|, so 1≤W≤2^v. The paired local class has size 360, each diagonal outer class size 36, and each field local class size 15, hence

 |K|=360^p36^u15^vW,      |H|₂=2^{3p+u+3v−v₂(W)}.

The square of every selected local outside class contains the unique inner involution class. For the σ field class, take u=diag(−1,1) and choose δ∈F9 with δ³=−δ, so δ²=−1 and δ is a square. Then b=diag(δ,1)∈T and bσb^-1=uσ, so u is in the class square. The second class is obtained by conjugation by an element of PGL₂(9)\T, which preserves the unique T-involution class. For the diagonal outer PGL₂(9) class, use a nonsplit torus normalizer D20: its central torus involution is outer, and it has an outer reflection; their nonidentity product is an inner involution. For each τ-pair the selected mark-class square realizes pairs of conjugate involutions. Therefore a nonidentity involution of H with matched identity/nonidentity support on every paired edge gives a genuine element of H∩Λ², irrespective of its fixed-coordinate involution values.

Apply the reviewed parity-kernel expansion to Sylow₂(H): each term imposes identity on at most one coordinate of each paired edge and has target order at most 2^{3p}. If u+3v>v₂(W), every kernel is a nontrivial 2-group, so the number of matched involutions including identity is even; another involution gives a collision. Hence v₂(W)≥u+3v. Since W≤2^v, v₂(W)≤v, forcing u=v=0. Thus τ swaps all simple factors. The reviewed paired q=9 exclusion then rules out G=A6^r for all r, subject to the stated source and review qualifications.


### Independent reviews of the even-field and A₆ arguments

reviewers contributor 1, contributor 2, and contributor 3 independently accepted both sections, separately, at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/b17c2467313411fe894e1ef58c7d6c253d2e5ce3). For even fields they checked characteristic-two descent, the unique field class and positive principal trace, actual arbitrary subfield embeddings in all degree regimes, the small A₅ cases, transported path labels, actual mark-square cycles, covers and support parity. For A₆ they checked the two field classes and absent diagonal-field involutions, the degree-nine signs and component argument, Dickson's proper-transitive implication, the degree-five simple-path labels, both field-class squares and the outer diagonal square, and the final parity bound and paired-q9 consequence. The acceptances remain conditional on the pinned canonical-folder, actual-transversal, full-strip, subgroup, character-table and paired-classification inputs. Reviewers retained their prior primary-source inspections and performed no new computation or independent reproof of the external classifications. These are model mathematical reviews, not human or formal certification.

## All-prime-power assembly without an inversion hypothesis

**Independently reviewed assembly under the pinned inputs.** For every prime power q≥4 and integer n≥1, if a finite simple nonassociative left Bol loop has entire faithful canonical left multiplication group G=PSL₂(q)^n, then n=2h is even and its canonical inverting automorphism exchanges every simple factor in pairs. Its complete construction and loop-isomorphism list is exactly [the all-field paired table](radical-free-psl2-path-classification.md#all-field-paired-psl-assembly), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e30af949531c0ebcc9f7533b04fc1e7fc6858563), without an initial inversion-action hypothesis. Each listed loop is proper, non-Bruck, and has order |PSL₂(q)|^h. The q=4 and q=5 entries are the same A₅ family and are counted only once. A right Bol formulation follows by taking opposite loops.

The field regimes exhaust all prime powers: the prime-field assembly was independently reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/3dd83d3983cbc62b8e8b467339f77656efd01bb8); the odd q≡1 mod4 exclusion outside 5,9,29 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/c722d73e0eee35e4c9df6f1bd7e8cf8f5e99d7ae); the nonprime odd q≡3 mod4 pairing theorem at [the source revision](https://github.com/Mira-Cult/math-wip/commit/ff6d4cbe2e351e253aa014d636102305c80076d9); and the even-field pairing theorem and q=9 exclusion at [the source revision](https://github.com/Mira-Cult/math-wip/commit/b17c2467313411fe894e1ef58c7d6c253d2e5ce3). The remaining q=4,5 and q=29 cases are included in the reviewed A₅ and prime-field inputs. Each case either forces factor pairing or excludes the group altogether, and the cited paired theorem supplies exhaustiveness, construction and the exact isomorphism criterion in every surviving case. All dependencies and their source/CFSG qualifications remain in force.

This completes this specified family of entire canonical groups, subject to the recorded review scopes. It is not a classification of loops whose canonical group merely has PSL₂ composition factors, or of arbitrary overgroups, mixed socles or solvable radicals; the full finite-simple-Bol problem remains open.


The all-prime-power assembly was independently accepted by reviewers contributor 1, contributor 2, and contributor 3 at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/f831fb7a9cc3c1f90c2b32b94e002b5e6d06a413). They checked exhaustive field regimes, the q=4/5 identification, exact input pins, the paired-table construction/isomorphism interface, and the entire-canonical-group scope. This was an assembly-only review, retaining the previous case reviews and source/CFSG qualifications; no new computation or reproof of upstream inputs was performed.
