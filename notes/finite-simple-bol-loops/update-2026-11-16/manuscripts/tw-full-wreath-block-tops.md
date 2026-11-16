# Full-wreath block tops over alternating parity bases

**Theorem with scoped independent reviews, continuing 0323:C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`].** This result uses the alternating parity-base induced TW groups and all-mark interfaces in [the parity-code manuscript](tw-parity-code-subwreath.md). In that setting let T=A_n, n≥5, m=n+1, b≥2, A_m^b≤K≤S_m^b, and let transitive R≤S_b normalize K. Let P=K⋊R and G=N⋊P, N=T^(mb), be primitive on its regular-socle cosets, with local image containing Inn(T). Under the cited folder, local-map and finite-coset inputs, the following exclusions hold for **every outside involution** β∈Aut(T) wr S_(mb) normalizing G:

1. R=S_c wr D in its natural action on b=cd original blocks, where c≥3, d≥2 and D≤S_d is any transitive group.
2. R=S₂ wr S_d on b=2d original blocks, d≥2.
3. R=(S₂ wr S_c) wr D in its natural action on b=2cd original blocks, where c,d≥2 and D≤S_d is any transitive group.
4. Any transitive A_c^d≤R≤S_c wr S_d on b=cd original blocks, with c≥5 and d≥2, without requiring a split extension over the unit action.

The first three families are full wreath products at the displayed levels; the fourth assumes the independent alternating higher base. These conditions do not cover arbitrary proper or diagonal subgroups of those wreath products or all TW groups. The first two cases include and sharpen the separate full-iterated-wreath control; the third is a nested binary extension.

The preceding parity-code all-marks theorem has scoped reviews at `123933cc594b601dd317d62b333a949d20431d35`; the arbitrary-transitive-R primitive-local-map and normalizer reductions have scoped reviews at `cdfe466523a3358d1636f517f51664f3c7c51e22`, as recorded in that manuscript. These pins do not review the new deductions below. This note imports those inputs: after an Aut(T)-conjugation the local map is the natural pointed-block action, and the induced P embedding is the restriction of the full S_m wr S_b embedding in compatible point/block representatives. The group has soc(P)=A_m^b. A normalizing β has factor permutation σ in the full block stabilizer and normalizing P; its compatible full-wreath lift pσ normalizes G. Thus βG=z pσG, where z=(γ,…,γ), γ² is inner and γ may be 1 or have order 4. Involutions in a fixed permutation fibre have at most M^(mb) elements, with M=16 for n=5, M=46 for n=6 and M=i_n for n≥7, and

    3m! M^m < |T|^m.                                          (1)

In n=6 this includes all four outer cosets, including the one with no involutions. No representative z is assumed to lie in Λ. The normalizer, hierarchical collision and counting deductions below have the scoped reviews recorded at the end.

## Intrinsic minimal units

For R=S_c wr D with c,d≥2 and D transitive, the c-block units form the unique **minimal** nontrivial R-block system. To see this, let Q be an original-block stabilizer and B its unit stabilizer. Q is maximal in B because S_(c−1) is maximal in S_c. If Q<L is not contained in B, choose g∈L moving the distinguished unit. Q and gQg⁻¹ contain every independent S_c base factor between them, and Q contains D_1; hence they generate B. Thus every proper overgroup of Q contains B, and the c-unit system is the unique smallest nontrivial block system. Larger systems can exist when D is imprimitive. A permutation normalizing R preserves this unique minimal system.

Associativity of full imprimitive wreath products identifies R=(S₂ wr S_c) wr D with S₂ wr (S_c wr D). Applying the same argument to its binary base, the original two-block units form the unique minimal nontrivial system. Any normalizer induces a normalizer of S_c wr D on these two-block units, which preserves its unique minimal c-subunit system. Consequently it preserves both the two-block units and the larger 2c-block units. These conclusions use transitivity of D and do not assume D is symmetric or primitive.

## Collision on equal-parity block edges

Let Λ⊂βG consist of involutions, be G-conjugacy invariant and satisfy P∩Λ²={1}. A member has an involutory factor permutation h∈σP. At every wreath level used below, its unit action is an involution because the corresponding system is preserved. The natural induced coordinates have pure R permutations with identity local arrows, and θ ignores base elements supported outside the pointed original block.

Suppose h exchanges two c-block units in case 1. Conjugate by the full S_c base on those units to make their two unit arrows identify the c original-block positions. Each corresponding lower block edge has inverse S_m arrows and a parity sign. Since c≥3, two signs agree. Use A_m^b≤K gauges supported at one end of each chosen edge to make both edges' arrows r,r, where r=1 for even sign and r is a fixed transposition for odd sign. These gauges have even sign. Orient the edges positive→negative and conjugate by N, supported only on their four original blocks, so that their forward local arrows at each point x are the same Γ_x and their reverse arrows Γ_x⁻¹. This is possible because the coherent local outer-arrow patterns agree on the normalized edges and the marked outer class is constant; Γ_x need not be an involution.

A pure transposition in the S_c base inside the positive unit swaps the two positive original blocks, fixes all others and has identity local arrows. Its conjugate of the normalized Λ-element has a different matching. Their product is identity away from the four selected blocks, and on them has identity local arrows and point labels since Γ_xΓ_x⁻¹=1 and r²=1. Its block permutation is the nonidentity product of the corresponding positive- and negative-unit transpositions. It belongs to R≤P, contradicting P∩Λ²={1}. Thus no unit exchange can occur.

If an unexchanged c-block unit has three or more original-block transpositions, two have equal parity; exactly the same local rematching inside that unit excludes them. Hence every usable h acts trivially on the d units and has at most two original-block transpositions in each unit. These statements are invariant under the allowed G-conjugations and do not require the factor-permutation label h to lie in P rather than σP.

## Binary units

For a transposed pair of two-block units, the same local collision shows that its two lower block edges must have opposite signs. Conjugate by pure S₂ base permutations at both endpoints to normalize their order to (+,−); then the induced unit arrows still identify positions. If two unit pairs occur within an S₂ wr S_c group acting inside a fixed 2c-block unit, normalize both signatures, orient their unit pairs, and use A_m^b and N gauges as above. A pure S_c transposition swaps the two positive two-block units; it has identity local arrows, changes the matching, and forces a nontrivial element of P∩Λ². Hence inside such a group at most one two-block unit pair can be exchanged.

This proves case 2 directly. For case 3, suppose h exchanges two larger 2c-block units. First use the full S_c base at the larger-unit level to identify their c two-block positions. Each of those c pairs of two-block units must have opposite lower-edge signs, or the first collision applies. Using pure S₂ gauges at both endpoints, put every signature in the common order (+,−). Since c≥2, two of these two-block-unit edges can then be normalized to the same oriented Γ-pattern. A pure S_c transposition inside the positive larger unit rematches them and gives the same forbidden product. Thus no larger-unit exchange is usable in case 3. Each fixed larger unit, acting as S₂ wr S_c, has at most one exchanged pair of two-block units by the preceding paragraph.

## Capacity

Let f₂(c)=1+binom(c,2)+3binom(c,4). It is at most 3^c by encoding the zero, one or two transpositions as a ternary string with canonically ordered pairs. In case 1, at most f₂(c)^d≤3^(cd)=3^b original-block permutations survive.

In an S₂ wr S_c unit with at most one exchanged pair of two-block units, there are at most 2^c(1+binom(c,2))≤2^(2c−1)<3^(2c) permutations: the first factor counts its binary base, and 1+binom(c,2)≤2^(c−1) counts even subsets of size zero or two. This gives fewer than 3^b top labels in cases 2 and 3, using c=d for case 2 and one such bound per fixed larger unit in case 3.

For each top permutation there are at most (m!)^b factor-permutation labels h in σP, and each h fibre contains at most M^(mb) involutions. By (1), |Λ|≤(3m!M^m)^b<|T|^(mb), contrary to the transversal cardinality. The inequalities count all remaining choices, even if they fail further collision or conjugacy conditions.

The unique-minimal-block, nested normalizer, actual arrow cancellation and capacity arguments have the exact-source reviews below. They depend on the precise cited induced-coordinate, automorphism and folder interfaces; they do not resolve the unrestricted TW frontier.

## Independent alternating higher bases

**Further independently reviewed family.** In the same parity-base induced TW setting, let b=cd, c≥5, d≥2, and suppose the transitive block-top group R satisfies

    A_c^d ≤ R ≤ S_c wr S_d.

Assume R normalizes K, and retain all group, local-image, primitive regular-socle, marked-involution and folder hypotheses from the opening statement. Then the same all-marks exclusion holds. No splitting of R over its induced unit permutation group and no parity-code restriction on R/A_c^d is assumed. This does not cover diagonal A_c strips in place of the independent product A_c^d.

The socle of R is A_c^d: it is minimal normal because transitivity of R on the cd original blocks makes its induced action on the d units transitive, and every disjoint normal subgroup would centralize it, whereas C_{S_b}(A_c^d)=1. Thus its unit orbits are characteristic under N_{S_b}(R). As in the prior normalizer reduction, the factor permutation of any outside normalizing involution β preserves the original blocks and induces a normalizer of R, so it also preserves these units. The unit permutation of its coset labels h∈σP need not belong to R's unit image; it only needs to be an involution.

Suppose a usable h exchanges two c-block units. Its unit arrow is an arbitrary π∈S_c; no assumption that π is even and no attempt to gauge it away are needed. It matches the c original blocks of one unit with those in the other. Each lower block edge has an internal S_m-arrow and its inverse, hence one parity sign. Since c≥5, among these edges we can choose two disjoint pairs of edges, with equal signs within each pair: otherwise at most 3+1=4 edges are possible across the two parity classes. For each selected pair, use independent A_m^b gauges to make the two edges' internal arrows equal to r,r, with r=1 for even sign and a fixed transposition for odd sign. The two pairs may use different r. In compatible induced coordinates, corresponding normalized edges in each pair have identical local outer-arrow patterns at each m-point label; use N-conjugation on their eight original blocks to put their arrows into matching Γ_x,Γ_x⁻¹ form, separately for each pair. All other blocks retain their original restriction.

Let ρ be the product of the two disjoint transpositions of the chosen positive original blocks inside one of the exchanged units. It belongs to the independent A_c factor of that unit, hence to R≤P; it has identity local arrows in the coherent coordinates. Its conjugation simultaneously rematches both pairs while leaving all other original blocks fixed. The product of the normalized Λ-element with its ρ-conjugate has identity local arrows and point-label action, and has a nonidentity block permutation: ρ in the positive unit and its π-transport in the negative unit, both even. Thus it lies in A_c^d≤R≤P and contradicts P∩Λ²={1}. This proves that no exchanged unit pair is usable. The conclusion is independent of the parity of π.

Within a fixed unit, suppose the original-block involution has at least five transpositions. Their signs contain two disjoint pairs of equal sign. The same A_m/N gauges and an even ρ equal to the product of the two positive-block transpositions give a nontrivial forbidden product in that unit's A_c. Hence at most four original-block transpositions survive per unit. The number of these involutions is

    f₄(c)=Σ_{j=0}^4 binom(c,2j)(2j−1)!!≤3^c,

where the explicit base checks and inductive ratio proof are in the [parity-code manuscript](tw-parity-code-subwreath.md#alternating-block-tops). Since no unit exchange survives, there are at most f₄(c)^d≤3^(cd)=3^b top permutations to count, even if the coset σP contains more. At most (m!)^b factor-permutation labels lie over each, and at most M^(mb) involutions lie in each fibre. The existing inequality 3m!M^m<|T|^m now contradicts |Λ|=|T|^(mb). The proof uses the independent A_c factors and does not establish a corresponding statement for subdirect or diagonal strips. ∎

This fourth family and its simultaneous even-rematching, intrinsic unit system and capacity deductions have the exact-source reviews below. They inherit, without promoting, the exact C0007, induced-coordinate, normalizer and coset-count reviews recorded in the parity-code manuscript.

## Independent review

At exact source `123a301135a04a53738f904fce3fcc76b6394111`, GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted all four stated families, conditional on the pinned transitive-top induced-coordinate/local-map, marked-folder and all-coset capacity inputs. All checked the minimal and nested unit systems, normalizers, even base gauges, actual forward/reverse arrow cancellation including order-four representatives, opposite-sign binary signatures and nested unit exchanges. They also checked the independent alternating higher base without a split unit action, retaining arbitrary odd unit arrows and using two even rematchings, plus all label-capacity inequalities. No new computation or primary-source audit was needed. Their scope is the four specified families and all normalizing involution marks, not diagonal strips, arbitrary proper subwreaths or general TW groups.
