# Fixed factors in A5/PSL₂(7) canonical envelopes

**Independently reviewed continuation of 0323-finite-simple-non-moufang-bol-loops:C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`].** Let G=A5^r×PSL₂(7)^s be the faithful canonical left multiplication group of a finite simple nonassociative Bol loop. The [all-powers matrix classification](radical-free-mixed-matrix-classification.md), independently reviewed at `8aa2dc1c5f7bd3190a57118c1e7e8398587f7655`, and its single-type inputs require τ to swap every pair of coordinates. Nonisomorphic A5 and PSL₂(7) factors cannot be exchanged by τ, so τ has separate involutory permutations on the two species, each with fixed points or two-cycles. This observation by itself does not forbid fixed points.

## Pinned interfaces and scope

The faithful generated-folder, all-conjugate transversal and exact normal-quotient inputs are [C0001](../proofs/C0001.md) at `9431ade99316d6bc62efb389492fef385b510b45`; canonical τ and conjugacy-invariance of Λ=τK are the scoped [C0007](../proofs/C0007.md) inputs at `932ead5db5f39045e2085caa6b062f6b981b2813`. The [full-strip decomposition](radical-free-strip-forests.md) was reviewed at `6d3a97daa9cf20bbae0416295c8c2374c2cd8ede`; the new parity proof uses the kernel-count mechanism of [the support lemma](radical-free-involution-support.md) reviewed at `e30af949531c0ebcc9f7533b04fc1e7fc6858563`. Small-subgroup, automorphism and unique-involution-class inputs are as pinned in [the A₅ source](radical-free-a5-path-classification.md) at `ad94accf574f89bf1e8487bb046cf30fb685cd0c` and [the small-PSL₂ source](radical-free-small-psl2-paths.md) at `184bc5f1b24d05d4dac1860060c6189afefda70c`. The deductions below have the independent mathematical reviews recorded at the end. They give necessary conditions, not construction or exhaustion.

## Projected constraints and their limitation

Fix an individual τ-stable simple coordinate T, with restriction α∈Aut(T), and let L be the product of all other coordinates. Put K_T=π_T(K), H_T=π_T(H), H^T=H∩T. For G≠T, the reviewed normal-subloop criterion applied to L gives the strict inequality

 |K_T| > [T:H_T].                                             (1)

Also K_T generates T and consists of α-inverted elements, because K generates G and τ(k)=k^-1. Since K itself is a transversal but its projection need not be, (1) is a multiplicity constraint, not a smaller folder.

There is a genuinely local marked collision constraint. Let t be the formal outside involution. For every x∈T, x^-1 t x lies in Λ=tK, so [t,x]=t x^-1 t x belongs to K∩T (convention changes may invert this commutator). Hence H^T avoids every nonidentity element of the square of this local commutator set. More generally H^T∩(K∩T)^-1(K∩T)=1. This uses actual selected marks and their conjugacy, rather than an assumed local transversal.

If α=1, K_T consists only of 1 and involutions. Both T have one involution class, with 15 involutions in A5 and 21 in PSL₂(7), so |K_T|≤16 or 22 respectively. Equation (1) forces |H_T|>60/16 or >168/22, i.e. |H_T|≥4 or ≥8. These bounds concern a projection and do not force any nontrivial H∩T. Indeed if α=1, the commutator set above is trivial, illustrating exactly why the direct local collision argument does not settle this case.

If α=Inn(a) is nontrivial, simplicity and trivial center imply a is an involution. In the local extension c=at is central of order 2; the local marks arising by T-conjugation form c·a^T, so actual K∩T contains a·a^T. Thus H^T must avoid (a^T)^2, a source-backed local restriction, but H_T need not equal H^T, and neither is forced to be a full-folder stabilizer. If α is outer, the local mark restrictions similarly involve the actual α-outside involution class; no full-class assertion for all of π_TΛ is made without checking whether multiple classes occur.

The reviewed no-simple-folder theorems for G=T do not automatically apply to a τ-fixed component of a larger direct product: after projecting K, cosets may have multiplicity and the projected H need not meet K_T once. Conversely an example of an abstract fixed-factor automorphism does not establish a Bol folder. The surviving precise problem is to combine (1) for all coordinate and normal-subproduct projections with the local marked restrictions and the correlated subgroup H≤G. No valid proof of fixed-point-freeness or actual counterexample is claimed here.

## Exact outside-class support polynomial

For the entire direct-product model, τ permutes factors in two-cycles or fixes them. A two-cycle on a simple factor T has one outside involution class under T×T, of size |T|. On a fixed A5 factor, an inner or identity restriction has two local outside involution classes of weights 1 and 15; for nontrivial inner α=Inn(a), these are c and c·a^T, c=at, while for α=1 they are t and t·Inv(A5). An outer restriction has one local outside involution class of size 10: Aut(A5)=S5 and it is the class of transpositions. On a fixed PSL₂(7) factor, the corresponding inner/identity weights are 1 and 21; the outer class has size 28. For the latter, Aut(T)=PGL₂(7); a split involution diag(1,−1) has nonsquare determinant, PGL centralizer order 12, and centralizer in T order 6, so its T-class has size 28. The other PGL involution class lies in T. The two-class assertion and class size are in Siman Wong, *The maximal unramified extensions of certain complex Abelian number fields*, Publications mathématiques de Besançon (2015), pp.93–104, Lemma 1(a), printed p.95, [published PDF](https://www.numdam.org/item/10.5802/pmb.14.pdf), DOI `10.5802/pmb.14`; the coordinator directly inspected the statement and its matrix proof on 15 November 2026; the elementary determinant and centralizer calculation identifies the outer class. The A5 statements are elementary permutation calculations.

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

Thus a 2-power index would be >1 whenever p+u>0, contradicting the subgroup theorem. If p=u=0, τ is globally inner (including identity restrictions), already excluded for radical-free canonical G by the reviewed inner-inversion/Bruck-isotope reduction in [the intrinsic source](exact-factorization-criterion.md#inner-inversion-and-the-generalized-fitting-subgroup) at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`. Consequently no selected S can make |K|/60^s a power of 2 in such a simple nonassociative A5-only canonical envelope. The proof uses H∩N_S=1 as an actual global consequence of the selected mark square; it does not infer a projected folder.

This 2-power-index conclusion should not be transferred unchanged to mixed A5/PSL₂(7) complements: PSL₂(7) has a subgroup of index 8. It remains a necessary obstruction rather than a complete classification of admissible support families.

## An active-coordinate strip cannot have an independent opposite leaf

Let S be a selected support and let i∈S be a fixed inner/id A5 coordinate. Suppose H contains an independent full diagonal A5 strip Δ whose support includes i and exactly one coordinate x of a paired edge (x,y), and suppose H also contains a nontrivial subgroup L≤T_y supported only on the opposite coordinate y. Assume any other coordinates in Δ, if present, are fixed inner/id A5 coordinates in S (so their local selected class squares are full A5). Then H∩Λ²≠1. Indeed pick 1≠h∈L; use the strip parameter to make its x-coordinate conjugate to h^-1. On every active fixed coordinate of Δ, the selected class square is the whole A5. On the paired edge, the two chosen coordinates are conjugate inverses and hence lie in the pair-class square. All remaining coordinates can be identity. Independent conjugation in the selected global mark class therefore supplies this nonidentity strip-times-leaf element in Λ². The assertion includes strip twists: automorphisms preserve conjugacy classes, and a strip parameter can be chosen to realize any prescribed value at x.

The hypothesis on the other strip coordinates is essential: an additional paired edge supported on only one of its two coordinates would obstruct this particular element. Nor does a nontrivial projection to y suffice: the subgroup L must be independently supported there (or one must explicitly control all other coordinates). This is a sufficient global collision mechanism, not a proof that every support family has such a strip/leaf configuration.


## Immediate paired-inversion corollaries and remaining obligation

If a=b=0, then the only support is empty and W=1. Inequality (5) forces u=v=0. Thus in the two-type model, if τ has no fixed factor on which its restriction is inner or the identity, then it has no fixed factor at all: every factor is paired and the reviewed paired classification applies (using the single-type cases if just one type occurs).

In the A₅-only model, if the empty support belongs to F, (6) first forces a=0 and then (5) forces u=0. This is a second sufficient condition for paired inversion. Neither condition has been established for every simple loop. The remaining obligation is to control selected families without the empty support using the actual stabilizer and class-square conditions, or produce a faithful simple counterexample. Scalar divisibility and valuation controls alone do not answer that question; the explicit formal family above is excluded only after the actual subgroup-index argument. No computation or literature novelty is claimed for these reductions.


## Independent mathematical review

GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted the complete constraint package at exact source `59985c2e7450f7f800c4db0f8859b3a58669ee83`, conditional on its pinned canonical-folder/inversion, subgroup, strip and Bruck-isotope interfaces. They checked the outside-class support polynomial and mandatory class, actual selected-mark square and complementary stabilizer embedding, global Sylow-two parity exponent, original-stabilizer A₅ leaf count, the formal-family elimination by the image-index theorem, and the stated paired-inversion corollaries. None transfers original corefreeness to a projected subgroup or assumes a projected folder. Reviewer [model reviewer] additionally directly inspected Wong, Lemma 1(a), printed p.95; the other two relied on the recorded source input. No new computation or full re-audit of upstream classifications was performed. These are model mathematical reviews of necessary restrictions, not human or formal certification, a counterexample construction, or a proof that all fixed factors are impossible.


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

GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted the full appended character section at exact source `a88ce90b600f86a03163e8867c924559015fc91f`, conditional on the pinned canonical-folder, marked-support, A₅ subgroup and full-strip inputs. They checked the original-transversal group-algebra identity, extension and Schur scalar without τ(H)=H, the self-contained character values and outer traces, actual stabilizer projections and strip tensor invariants, component leaf restrictions, and the count allowing projected singleton strips with k_S≤min(s,p). Their scope includes the strengthened valuation bound and explicitly excludes general fixed-factor exhaustion. No new computation or primary-source audit was performed. These are independent model mathematical reviews, not human or formal certification.


## Exhaustion of every A5-power canonical group

**Proposed, unreviewed classification under the pinned interfaces.** Let Q be a finite simple nonassociative left Bol loop whose full canonical left multiplication group is G≅A₅^r, r≥1. Under the canonical inversion and faithful-folder inputs stated above, r is even, say r=2k, and the canonical involution exchanges every simple factor with a different factor. Consequently the [reviewed paired A₅ classification](radical-free-a5-path-classification.md) at `ad94accf574f89bf1e8487bb046cf30fb685cd0c` applies: for each k≥1 there is exactly one loop-isomorphism class in this model, of order 60^k, with the A₄/C₅ path stabilizer. These loops are proper. The statement concerns the entire canonical group, not an A₅ composition factor or a quotient. This new removal of the inversion hypothesis and final assembly still require exact-source independent review.

The proof uses the character section above, independently reviewed at `a88ce90b600f86a03163e8867c924559015fc91f`, and the earlier marked-support/Sylow constraints reviewed at `59985c2e7450f7f800c4db0f8859b3a58669ee83`. No new computation or external classification input is used.

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
