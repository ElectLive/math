# Alternating-base parity subwreaths: candidate TW exclusions

Mira Cult
This bounded theorem, with scoped reviews below, concerns [C0010](../../claims/0010.md). Let n≥5, m=n+1, b≥2, T=A_n. Let K be **any** S_b-invariant subgroup with A_m^b≤K≤S_m^b, and put P=K⋊S_b acting naturally on k=mb factors. Thus K/A_m^b is an arbitrary S_b-invariant binary parity code; no classification of those codes is needed. Form the induced twisted wreath G=T^k⋊P using any local map whose image contains Inn(T), and assume its regular-socle coset action is primitive. The local-map reduction below shows that this is conjugate to the natural local map. Subject to C0007 and the local automorphism/coset counts in tw-psl2-factorwise-inversion.md and [the cross-label theorem](tw-cross-label-block-exclusion.md), the candidate excludes a marked transversal for every factorwise outside involution β normalizing G and acting trivially on G/N, N=T^k. It does not cover factor-permuting marks or arbitrary subwreath groups.

The [full-wreath cross-label theorem](tw-cross-label-block-exclusion.md) was independently reviewed at its recorded source revision; its nonconstant factorwise-mark reduction at its recorded source revision; and the separate [primitivity control](tw-imprimitive-capacity-control.md) at its recorded source revision. Those scoped reviews do not cover this parity-code theorem or its local-map exhaustion. The exact-source reviews below cover the parity-code theorem and local-map exhaustion; the later all-marks extension has separate status.

## Construction and primitivity

Let Q=P_x for x in the first m-point block. Projection of Q to that block lies in S_{m−1}=S_n. Define θ:Q→Aut(A_n) by this projection followed by conjugation on A_n. The image contains Inn(T), because the subgroup A_n in the pointed A_m factor lies in Q. The construction and local-image interface are Liebeck–Praeger–Saxl, J. Austral. Math. Soc. A 44 (1988), §1 III(c), p.391, DOI 10.1017/S144678870003216X; the local image condition by itself does not assert primitivity.

Let B be the first-block stabilizer. Its image on that block is A_m or S_m and is primitive, so Q is maximal in B. Every L>Q not contained in B contains B: choose g∈L moving the first block. Q and gQg⁻¹ together contain the full even factor A_m in every block. Further Q maps onto K/A_m^b, since each prescribed sign in the first block can be represented by a point-fixing permutation and other blocks can realize the remaining prescribed signs. Thus Q and gQg⁻¹ generate K, and with the block-top stabilizer already in Q they generate B.

The map θ cannot extend to B. The pointed A_m lies in B; an extension restricts to A_m→Aut(A_{m−1}) and agrees with its nontrivial natural conjugation action on A_{m−1}. For n≠6, Aut(A_n)=S_n; |A_{n+1}|>n!, so simplicity of A_{n+1} forces the restriction to be trivial, contradiction. For n=6, |A7|=2520>|Aut(A6)|=1440 gives the same conclusion. Therefore θ extends to no L>Q. As proved via subdirect diagonal subgroups in [the primitivity control](tw-imprimitive-capacity-control.md), this nonextension and θ(Q)≥Inn(T) force P maximal in the induced group, hence the regular-socle action is primitive.

Choose compatible induced coordinates by using representatives in the independent A_m^b factors to move points within blocks and pure S_b representatives to move blocks. In these coordinates pure block permutations have identity local arrows, and a base element supported away from a given block has identity arrows there, because θ ignores all other blocks. In particular, if two block pairs have the same internal permutation r in each direction, their local outer-arrow patterns coincide pointwise. This locality and representative claim is essential to the proof below.

## Marks and parity gauge

Out(A_n) is abelian: C2 for n≠6, C2² for n=6. For a factorwise β as in the proposition, its coordinate outer classes are constant by transitivity of P and [β,P]≤N. The common class is nontrivial since β∉G, and every β_i is an outer involution. With α=β_1 and z=(α,...,α), we have zG=βG, z²=1, and z normalizes G and centralizes G/N. We do not assume z∈Λ.

If λ∈Λ∩zNh, then h²=1. Suppose its block permutation has at least three transposed pairs. In each pair the two internal S_m arrows of h are inverse, and hence have equal sign. Select two pairs with equal signs. Let r=1 if this sign is even, and let r be a fixed transposition if it is odd. Conjugation by independent elements of A_m^b≤K, supported at one endpoint of each selected pair, turns both pairs' arrows into r,r: the required adjustment has even sign. This P-conjugation replaces λ by another member of Λ. All other blocks are untouched.

The normalized h sends point label x to rx in each direction of each selected pair. Its local outer-arrow pattern is identical on the two pairs by the coherent-coordinate property above. Orient both pairs positive→negative. Since λ²=1, each λ-arrow on one of these factor pairs is inverse to its partner, and the corresponding forward arrows on the two block pairs lie in the same Aut(T)/Inn(T) coset. Choose a representative Γ_x for each x and independently conjugate by N supported on the four selected blocks to make the forward arrows Γ_x and reverse arrows Γ_x⁻¹. Call the result μ∈Λ. Its restriction to every other block is unchanged and squares to 1.

A pure block transposition ρ swapping the two positive blocks belongs to S_b≤P, has identity local arrows and fixes all other blocks. The conjugate ν=ρμρ⁻¹∈Λ has a different matching but the same r and Γ_x on the selected pairs. The product μν is identity outside those blocks; on them, point permutations give r²=1 and local arrows cancel Γ_xΓ_x⁻¹. It is a nonidentity pure block permutation in P, contradicting P∩Λ²={1}. Thus every usable label h has at most two transposed block pairs.

## Capacity

There are at most 1+binom(b,2)+3binom(b,4) involutions of S_b with at most two transpositions. This is ≤3^b: encode a matching of zero, one, or two pairs as a ternary string, labeling the first pair 1, the second 2 in a fixed canonical order, and all other positions 0. Each such block permutation has at most (m!)^b lifts to P. If M bounds every involution fibre by M^k, then

    |Λ| ≤ (m!)^b 3^b M^(mb).

For n≥7 use M=i_n, the number of elements of S_n of order dividing 2. The recurrence and product-of-two-involutions argument in [the cross-label theorem](tw-cross-label-block-exclusion.md) give M²≥|T| and |T|/M≥m. Since 3m!<m^m for m≥8, the right side is strictly below |T|^(mb).

For n=5, |T|=60 and M=16 bounds both inner and outer involutions in S5 and satisfies M²≥60; exact arithmetic gives 3·6!·16^6<60^6. For n=6, the four Aut(A6)/Inn(A6) cosets have respectively 46,30,36 and 0 elements of order dividing 2, so M=46 and 3·7!·46^7<360^7. A transposed factor pair contributes |T| choices; therefore these M values indeed bound every full fibre. This contradicts |Λ|=|T|^k.

The nonextension, induced-coordinate, parity-gauge and collision arguments above have the scoped reviews below. The separate local-map argument below extends the exclusion to every primitive θ with image containing Inn(T), up to conjugation by Aut(T). The result does not rely on identifying the S_b-invariant binary codes, and it makes no claim for nonfactorwise marks, non-full top S_b or complements not containing A_m^b.

## Exhaustion of primitive local maps

This subsection is included in the scoped factorwise reviews below. Let θ:Q→Aut(T) be any homomorphism with θ(Q)≥Inn(T), and suppose the induced twisted-wreath group is primitive on its regular-socle cosets. We show that θ is the natural pointed-block map conjugated by a single element of Aut(T), including a possibly exceptional outer automorphism when n=6.

Put D=Q∩A_m^b=A_n×A_m^(b−1). The restriction of θ to each other-block A_m factor is trivial: A_m is simple and |A_m|>|Aut(A_n)|, including |A₇|=2520>|Aut(A₆)|=1440. The restriction to the pointed A_n is either trivial or injective.

Suppose first it is trivial. Then θ(D)=1, and Q/D≅C⋊S_(b−1), with C=K/A_m^b the parity code. The image of C is an abelian normal subgroup of θ(Q). Its intersection with the nonabelian simple Inn(T) is trivial, so their commutator is trivial. Since C_Aut(T)(Inn(T))=1, the image of C is trivial. Thus θ factors through S_(b−1) and extends to the block stabilizer B=K⋊S_(b−1) by killing K. Here Q<B<P. The induced-function nonextension argument in [the primitivity control](tw-imprimitive-capacity-control.md) then gives a nontrivial proper P-invariant subgroup of the regular base, contradicting primitivity.

Hence θ injects on the pointed A_n. Its image intersects Inn(T) in a normal subgroup of that simple image. If the intersection were trivial, the nonabelian simple image would embed in the abelian group Out(T), impossible. Its image is therefore Inn(T), by equality of orders. Identify T with Inn(T), and choose γ∈Aut(T) so that θ(a)=γaγ⁻¹ for each a in the pointed A_n.

For any q∈Q let g_q∈S_n be its permutation on the pointed block. For each pointed a∈A_n, the homomorphism property gives

    θ(q)γaγ⁻¹θ(q)⁻¹=γg_q a g_q⁻¹γ⁻¹.

The quotient of θ(q) by γg_qγ⁻¹ centralizes Inn(T), so it is 1. Thus θ(q)=γg_qγ⁻¹ for every q∈Q. Compatible induced-coordinate constructions for θ and the natural map are conjugate by coordinatewise γ. This conjugacy transports the factorwise-mark, normalization and quotient-centrality hypotheses as well as Λ. The earlier exclusion therefore applies to every primitive local map with the stated image condition. This conclusion neither covers marks that permute factors nor asserts that arbitrary local maps produce primitive groups.


## All normalizing involution marks

**Extension with the scoped independent reviews below.** Keep n≥5, m=n+1, b≥2, T=A_n, A_m^b≤K≤S_m^b normalized by S_b, and P=K⋊S_b in its natural action on k=mb points. Let G=N⋊P, N=T^k, use the coherent induced embedding and primitive local-map reduction above. At exact source the recorded source revision the factorwise theorem and local-map exhaustion received scoped independent reviews; those reviews do not cover this extension. Under their group, automorphism and local-coset inputs, the following argument excludes a marked transversal for **any** involution β∈Aut(T) wr S_k normalizing G with β∉G. In particular β may permute factors and may act nontrivially on G/N. The result remains restricted to these parity subwreaths, not all TW groups.

### Normalizer and full-wreath lift

The socle of the permutation group P is A_m^b. The product A_m^b is a minimal normal subgroup of P because the full block top S_b permutes its simple factors transitively. If another minimal normal subgroup had trivial intersection with A_m^b it would centralize A_m^b, whose centralizer in S_k is trivial (each A_m is transitive on its block and has trivial centralizer in its natural symmetric action, and commuting with the independent factors prevents block movement). Thus there is no other minimal normal subgroup. Its orbits are exactly the given blocks, and any element of N_{S_k}(P) belongs to the full block stabilizer W=S_m wr S_b.

The factor permutation σ of β normalizes P and therefore lies in W. The natural pointed-block local homomorphism for P is the restriction of the corresponding local homomorphism for W. Choose compatible coset representatives using the independent A_m factors and pure block permutations. With these representatives, the induced embeddings agree on P; equivalently G is a subgroup of the induced full-wreath group N⋊W. Let p_σ be the W-complement lift of σ. Because σ normalizes P, p_σ normalizes the actual G=N⋊P: its conjugation maps N to itself and maps the embedded P complement to itself. This claim uses the full-wreath extension and compatible coordinates, not just the permutation action.

Set δ=βp_σ⁻¹. It is factorwise, normalizes G and centralizes G/N: its conjugation preserves the factor permutation of every element of P, and the factor action P→S_k is faithful. As Out(T) is abelian, the outer cosets of its coordinates form a P-invariant tuple, hence are constant by transitivity. Call the common class c; unlike the previous factorwise-outside case, c is allowed to be trivial because β can be outside G solely through σ∉P.

The involutivity of β gives σ²=1, hence p_σ²=1. Taking outer coordinates in β²=δ(p_σδp_σ⁻¹) gives c²=1. Choose γ∈Aut(T) in c, including γ=1 if c=1, and set z=(γ,...,γ). Then γ² is inner, z normalizes G, centralizes G/N, and z²∈N. Moreover δz⁻¹∈N, so

    βG=z p_σ G.                                                (1)

No involutory representative γ of c is required; γ may have order 4, for example in the A6 diagonal-field coset. Neither z nor p_σ is assumed to be in Λ, and no isotopy is used.

### Cross-label collision for a coset of P

Every λ∈Λ⊂βG has a unique factor permutation h∈σP, and λ²=1 forces h²=1. Suppose h's block permutation has at least three transposed block pairs. Its two internal S_m arrows on each pair are inverse, hence have equal sign. Two pairs have the same sign. Let r=1 for even sign and let r be a fixed transposition for odd sign. Conjugation by suitable elements of A_m^b≤P, supported at one endpoint per chosen pair, changes their internal arrows to r,r. The required gauges are even. G-conjugacy invariance permits the same replacement of λ; all other blocks remain unchanged. The new factor permutation still lies in σP because σ normalizes P.

In the compatible coordinates, p_h has the same local arrows on the two normalized pairs as functions of the within-block point x, since these depend only on the common internal permutation r. From (1) the corresponding λ-arrows have the same outer class, namely c times that local class. Orient both block pairs positive→negative. For each point x choose a representative Γ_x of the common forward outer coset; since λ²=1, the reverse arrow is in the inverse coset and is inverse to its forward partner. Independently conjugating by N on the selected four blocks makes both forward arrows Γ_x and the reverse arrows Γ_x⁻¹. The restriction to every other block is untouched; call the resulting element μ∈Λ.

Let ρ be the pure block transposition swapping the two positive blocks. It is in P, has identity local arrows and fixes all other blocks. Then ν=ρμρ⁻¹∈Λ has a different matching on the selected four blocks, with the same r and Γ_x arrows. Outside these blocks μ and ν agree and their product is 1. On them the point permutations compose to r²=1, and arrows cancel as Γ_xΓ_x⁻¹. Their block matching product is nontrivial. Thus μν is a nonidentity pure block permutation in P, contradicting P∩Λ²={1}. Consequently usable h∈σP have at most two transposed block pairs.

The counting labels are elements h of the permutation coset σP, not elements of P and not labels in G/N. This distinction is necessary when σ∉P. The argument only conjugates elements of Λ by G; it does not assume β commutes with P modulo N or that β itself is in any chosen factorwise coset representative.

### Capacity

There are at most 1+binom(b,2)+3binom(b,4) possible involutions in the block top with at most two transpositions, and this is ≤3^b by the ternary matching encoding in the parity-code manuscript. The full wreath has at most (m!)^b lifts of each block permutation, so the same holds for σP. On a transposed factor pair, one automorphism arrow lies in a prescribed coset of Inn(T) and the other is forced; there are |T| choices. On a fixed factor, it is an involution in a prescribed coset. The finite bounds used in the parity-code manuscript apply to **all** outer cosets: M=16 for A5, M=46 for A6 (including the empty diagonal-field involution coset), and M=i_n for n≥7, where i_n counts involutions including 1 in S_n. In each case M²≥|T| and 3m!M^m<|T|^m. Thus the entire set of involutions in any h fibre has size ≤M^k and

    |Λ| ≤ (m!)^b 3^b M^(mb) < |T|^(mb),

contradiction. The numerical inequalities, PSL₂(9) counts and alternating automorphism inputs retain their cited review/source qualifications; the new reduction has the scoped independent reviews below.

## Source verification and limitations

At exact source the recorded source revision, automated reviewers a separate automated checker and a separate automated checker independently accepted the complete parity-code theorem and primitive local-map exhaustion, conditional on the cited C0007, induced-group and local automorphism/coset inputs. Both checked the parity-code surjectivity and nonextension/primitivity proof, arbitrary local maps including A₆, the same-sign endpoint gauge and actual Γ-arrow cancellation for odd as well as even r, and the uniform capacity bound including the A₅/A₆ endpoints. Their scope is full top S_b, the stated alternating-base subwreaths, and factorwise outside marks centralizing G/N; it does not cover the later all-marks extension. Neither review constitutes a fresh audit of all primary inputs, all-TW exclusion or formal verification.

At exact source the recorded source revision, the same two reviewers independently accepted the complete all-normalizing-involution extension, under the preceding cited inputs and source qualifications. Both checked the characteristic socle and full-wreath normalizer, the actual compatible complement lift, the constant outer class including the trivial case, representatives whose square is inner, involution labels in σP, and the actual Γ-arrow cancellation and all-coset capacity bound. The scope includes factor-permuting marks for the stated parity subwreaths, not arbitrary TW groups. Neither review was a fresh primary-source audit or formal verification.


## Alternating block tops

**Extension with the independent reviews below.** Let n≥5, m=n+1, b≥3, T=A_n, A_m^b≤K≤S_m^b, and A_b≤R≤S_b normalize K. Put P=K⋊R in its natural action on k=mb factors. For b≥3 the block action is transitive; the b=2 symmetric-top case is covered by the preceding result. Let G=N⋊P, N=T^k, be a primitive induced twisted-wreath group with local image containing Inn(T). Subject to the same stated induced-construction, folder and automorphism inputs, this extension excludes marked transversals for every involutory outside normalizer mark β∈Aut(T) wr S_k. The symmetric-top all-marks theorem was independently reviewed at its recorded source revision; that review does not cover the new alternating-top argument below. This is not an exclusion of arbitrary TW groups.

### Local map, primitivity and full-wreath lift

Fix x in the first block and Q=P_x. The parity-code proof applies with R_1 in place of S_(b−1). The natural local map projects Q to its first-block point stabilizer S_n and acts by conjugation on A_n. Since R is transitive, the first-block stabilizer B acts on that block as A_m or S_m, so Q is maximal in B. Any L>Q not contained in B contains K: Q and a block-moving conjugate contain all independent A_m factors and Q realizes every parity code vector. They also contain R_1, hence B. The map does not extend to B, by restriction to the first A_m and the simplicity/order argument from the parity-code theorem. Thus the natural induced action is primitive by the same subdirect-diagonal nonextension criterion.

Conversely, for any primitive local map θ:Q→Aut(A_n) with image containing Inn(T), the all-local-map proof in the parity-code manuscript applies verbatim: θ kills the other-block A_m factors by the order bound; if it kills pointed A_n, it also kills the abelian normal parity code and factors through R_1, hence extends to B, contradiction. Otherwise it is conjugate by a single γ∈Aut(T) to the natural pointed-block map. Thus every such primitive induced embedding is conjugate to the natural one. No assumption is made that all homomorphisms are primitive.

For this natural embedding, the local homomorphism is the restriction of that for the full wreath W=S_m wr S_b. Shared point/block transversals exist in A_m^b⋊R because A_m is transitive and R is transitive. Hence the actual P complement embeds as a subgroup of the full W complement in compatible wreath coordinates, and pure block permutations in R have identity local arrows; base elements supported on other blocks have identity arrows on a given block.

The socle of P is A_m^b, by the same centralizer argument as in tw-parity-code-subwreath.md: it is a minimal normal subgroup by transitivity of R, and any disjoint minimal normal subgroup would centralize it, impossible in S_k. Its orbits are the blocks. Therefore the factor permutation σ of any β normalizing G belongs to the full block stabilizer W. As it also normalizes P, its W-complement lift pσ normalizes the actual G. Put δ=βpσ⁻¹. It is factorwise and induces the identity on G/N by faithful factor action; Out(A_n) is abelian, so its coordinate outer classes are a single common c. The class may be trivial if σ∉P. From β²=1 follow σ²=1 and c²=1. Choose any γ in c, with γ=1 when c=1, and put z=(γ,...,γ). Then z²∈N and βG=z pσ G. No involutory γ or selected marked element is required.

### Two simultaneous even rematchings

Let Λ⊂βG consist of involutions, be G-conjugacy invariant, and satisfy P∩Λ²={1}. Each λ∈Λ has an involutory factor permutation h∈σP. Suppose the induced block involution has at least five transposed pairs. Each pair's internal S_m arrows are inverse and have the same sign. Among at least five pairs, two disjoint collections of two pairs each have a common sign within the collection: the counts by sign are either at least 4+1 or at least 3+2 (including larger distributions).

For each of these two collections separately, use gauges from A_m^b≤K at one endpoint of each pair to make its pair arrows r,r, where r=1 for even sign and r is a fixed transposition of the m point labels for odd sign. The required gauges are even. The two collections may use different r. All other blocks are untouched.

Orient each selected pair positive→negative. Within either collection, coherent induced coordinates give identical local outer-arrow classes at corresponding point labels. By independent N-conjugation supported on the selected eight blocks, make each collection's forward arrows Γ_x (chosen for its relevant coset) and reverse arrows Γ_x⁻¹. The Γ_x for the two collections may differ, may have order 4, and their cosets may be inner or outer. Let μ be the resulting member of Λ.

Let ρ be the product of the two disjoint transpositions that swap the two positive blocks within each collection. It is even, lies in A_b≤R, and has identity local arrows. The conjugate ν=ρμρ⁻¹ lies in Λ. On each collection it changes the matching while preserving positive/negative orientation; on all unselected blocks it fixes μ. On each selected collection the product μν has identity point-label action since r²=1 and identity local arrows since Γ_x and Γ_x⁻¹ cancel. On unselected blocks it is μ²=1. Its block permutation is the nonidentity product of the two distinct matching products, so μν∈P\{1}, contradiction. Hence every usable h∈σP has at most four block transpositions.

This is not an application of the one-transposition rematching lemma for A_b: the product of two positive-block transpositions is needed to remain in A_b when the constant representative is not involutory. The proof uses full independent A_m^b and pure A_b explicitly.

### Counting

The number of involutions of S_b with at most four transpositions is

    f4(b)=Σ_{j=0}^4 binom(b,2j)(2j−1)!! ≤ 3^b,                (2)

with terms having 2j>b omitted and (−1)!!=1. For b=0,...,11 the values are 1,1,2,4,10,26,76,232,764,2620,8551,25301, each ≤3^b. For b≥11, each nonzero j-term satisfies f_j(b+1)/f_j(b)=(b+1)/(b+1−2j)≤3, so the inequality propagates. Thus at most (m!)^b 3^b factor permutations h∈σP survive.

For each h, the local fibre bound is M^(mb): n=5 has M=16; n=6 has M=46, bounding all four outer cosets including the diagonal-field coset with zero involutions; n≥7 has M=i_n, the number of involutions in S_n including 1. In each case M²≥|T|. The inequalities in the parity-code manuscript imply 3m!M^m<|T|^m (for n=5 and 6 by the explicit integer endpoints, and for n≥7 by |T|/i_n≥m and 3m!<m^m). Therefore

    |Λ|≤(m!)^b 3^b M^(mb)<|T|^(mb),

contradiction. The proof imports the parity-code/local-map and local-count inputs, and the new top-A_b, normalizer and even-rematching deductions have the scoped independent reviews below.

At exact source the recorded source revision, automated reviewers a separate automated checker and a separate automated checker independently accepted the alternating-top extension, conditional on the reviewed preceding induced-group, local-map, folder and local-count inputs. Both checked the transitive R local-map and actual full-wreath lift, the two disjoint same-parity pair-pairs, simultaneous even rematching with actual arrow cancellation, and the finite bases and inductive proof of f4(b)≤3^b. Their scope is the specified A_b≤R≤S_b parity subwreaths and every normalizing involution mark, not arbitrary TW groups. No fresh primary-source audit or formal verification was claimed.

## Primitive block tops not containing the alternating group

**Extension with the scoped independent reviews below.** Let n≥5, m=n+1, b≥2, T=A_n, A_m^b≤K≤S_m^b, and let a transitive R≤S_b normalize K. Put P=K⋊R in its natural action on k=mb factors, and N=T^k. Under the induced twisted-wreath, local-image, C0007 marked-folder and local involution-count inputs used above, suppose G=N⋊P is primitive on its regular-socle cosets and R is primitive with R⊉A_b. Then no marked transversal exists for any outside involution β∈Aut(T) wr S_k normalizing G. Combining this branch with the previously reviewed alternating-top theorem at its recorded source revision covers **every primitive block-top group R** in this specified parity-subwreath family. It does not cover arbitrary imprimitive block-top groups, other subwreath bases, or general TW actions.

The external group-order input is Attila Maróti, *On the orders of primitive groups*, J. Algebra **258** (2002), 631–640, [DOI 10.1016/S0021-8693(02)00646-4](https://doi.org/10.1016/S0021-8693(02)00646-4), Corollary 1.2: if R≤S_b is primitive and does not contain A_b, then |R|<3^b. The [author version dated 21 February 2002](https://www.renyi.hu/~maroti/primitive.pdf), printed p.3, was directly inspected; this citation retains the qualification that the author version rather than the publisher's typeset text was examined. Its proof uses the classification of finite simple groups. This source also appears in the canonical [references](../foundations/references.md). The deductions below and their source application have the scoped reviews recorded below.

### Primitive local maps and normalizer

The local-map exhaustion above also holds for arbitrary transitive R. For Q=P_x, write D=Q∩A_m^b=A_n×A_m^(b−1) and C=K/A_m^b, so Q/D≅C⋊R_1. Every other-block A_m maps trivially to Aut(A_n), by simplicity and order, including the exceptional n=6 order comparison. If θ kills the pointed A_n too, it kills D. The image of C is abelian and normal in θ(Q), whose image contains Inn(T); it intersects that nonabelian simple group trivially, centralizes it, and is trivial because C_Aut(T)(Inn(T))=1. Thus θ factors through R_1 and extends to the block stabilizer B=K⋊R_1 by killing K. The induced-function argument then gives a nontrivial proper P-invariant subgroup of N, contradicting primitivity. Otherwise θ injects the pointed A_n onto Inn(T), since Out(T) is abelian; the centralizer of Inn(T) forces θ to be the natural pointed-block map conjugated by one γ∈Aut(T). Coordinatewise conjugation reduces to the natural embedding without changing the marked-action hypotheses.

Transitivity of R makes A_m^b the unique minimal normal subgroup of P. Indeed it is minimal by the transitive permutation of its simple factors; a different minimal normal subgroup would centralize it, while C_Sk(A_m^b)=1. Its orbits are the blocks. Thus the factor permutation σ of any normalizing β normalizes P and lies in W=S_m wr S_b. The natural local map is the restriction of the natural W local map. Point/block representatives can be chosen in A_m^b⋊R, so the induced embeddings use the same coordinates. Hence the W-complement lift pσ normalizes the actual G whenever σ normalizes P.

Put δ=βpσ⁻¹. It is factorwise, normalizes G, and acts trivially on G/N because the factor action is faithful. Since Out(T) is abelian and P is transitive, the outer classes of δ's coordinates are a common class c; c may be trivial when σ∉P. Involutivity gives σ²=1 and c²=1. Choose any representative γ∈Aut(T) of c and set z=(γ,…,γ). Then z²∈N, z normalizes G and centralizes G/N, and βG=z pσG. The representative γ need not be an involution; in the A₆ diagonal-field case it may have order 4. No claim that z∈Λ is needed.

### Cardinality

Every λ∈βG has a factor-permutation label h∈σP. Involutivity forces h²=1, but we bound the number of labels by the entire coset size |P|. Since |K|≤(m!)^b, Maróti's inequality yields

    |σP|=|P|=|K||R| < (m!)^b 3^b.

In each h fibre, fixed factors allow involutions in one prescribed outer coset, and a transposed factor pair has at most |T| choices for one arrow, with the inverse forced. The all-coset bounds from the preceding proof give M=16 for n=5, M=46 for n=6, and M=i_n for n≥7, with M²≥|T|. In n=6 the bound includes all four outer cosets, including the diagonal-field coset with no involutions. Hence each fibre has at most M^(mb) involutions. The preceding parity-code argument proves the exact numerical inequality 3m!M^m<|T|^m in every case. Consequently

    |Λ| < (m!)^b 3^b M^(mb) < |T|^(mb),

contrary to the marked-transversal cardinality. This branch uses no rematching or collision condition; no assertion is made for imprimitive R on the basis of the primitive-group order bound. ∎


### Order-threshold corollary for transitive block tops

The preceding proof needs primitivity of R only to invoke Maróti's order bound. Thus, for any transitive R normalizing K, the same all-marks conclusion follows whenever |R|≤3^b. The primitive local-map argument, normalizer reduction, and fibre estimate above use transitivity of R and primitivity of G, not primitivity of the block action R. This is a numerical sufficient condition; it does not cover every transitive R.

A source-backed class of possibly imprimitive examples satisfies that condition. Maróti, in the same author version and publication cited above, Corollary 1.5, printed p.4, states for d≥4 that any permutation group R of degree b with no composition factor isomorphic to an alternating group of degree greater than d obeys

    |R| ≤ (d!)^((b−1)/(d−1)).

Setting d=4 gives |R|≤24^((b−1)/3)<3^b, since 24<27. Hence every transitive R with no composition factor isomorphic to A_j for j>4 satisfies the order threshold, including every solvable R and potentially nonsolvable groups. This Corollary 1.5 statement was inspected in the cited author version; its CFSG-dependent source and the current application have the scoped reviews below. It does not establish the order bound or an exclusion for arbitrary transitive R with larger alternating composition factors.

At exact source the recorded source revision, automated reviewers a separate automated checker and a separate automated checker independently accepted the primitive-nonalternating and order-threshold extensions, conditional on the preceding induced-group, folder and local-count inputs. Both checked that local-map exhaustion and compatible normalizer lifting use only transitivity of R, the arbitrary outer class including the A6 order-four representative, and the raw label/fibre capacity inequality. Both independently inspected Maroti’s 21 February 2002 author PDF, Corollary 1.2 on printed p.3 and Corollary 1.5 on printed p.4, and confirmed the stated bounds and their application. The source uses CFSG; neither reviewer inspected publisher typesetting. This covers the stated parity-subwreath family with primitive block top and the stated transitive order threshold, not arbitrary imprimitive tops or general TW actions. No new computation was claimed.
