# Cross-label exclusion for a twisted-wreath control

**Mira Cult**

This manuscript-local continuation, with exact-source reviews below, of [C0010](../../claims/0010.md) excludes marked transversals in the specific primitive twisted-wreath family of [the imprimitive capacity control](tw-imprimitive-capacity-control.md). The latter supplies the group construction, its primitivity argument and the marked field-involution embedding; those additions have their own exact-source review status and are assumptions here. The local PSL₂(9) fibre bound used below is in [the factorwise inversion manuscript](tw-psl2-factorwise-inversion.md), with scoped independent reviews at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6033272fbbd42f39c07ae59808ca122c9d60348e). This is not an exclusion of arbitrary twisted-wreath actions or arbitrary inversion automorphisms.

## A block-rematching lemma

Let T be a finite centerless group, identified with Inn(T), and N=T^(mb). Suppose P=A wr R acts faithfully on mb factors in its natural block action, with m≥2, b≥2, A≤S_m transitive, and A_b≤R≤S_b. Work in a coherent wreath embedding N⋊P≤Aut(T) wr S_(mb) with the following explicit properties:

1. The full base A^b lies in P; every pure block permutation ρ∈R has identity local automorphism arrows in the chosen factor coordinates. Each base factor A_j acts trivially, both in factor permutation and in local automorphism arrows, outside its own block.
2. An outside involution b₀=(α,…,α), with α∈Aut(T) of order 2, normalizes G=N⋊P and centralizes G/N. The set Λ⊂b₀G consists of involutions and is invariant under G-conjugation, and P∩Λ²={1}.
3. Each nonempty fibre b₀Nh contains at most M^(mb) involutions, for a stated numerical constant M. Set t=|T|.

Then every h∈P with Λ∩b₀Nh≠∅ has at most one transposition in its induced block permutation. Consequently

    |Λ| ≤ |A|^b (1+binom(b,2)) M^(mb).                         (1)

If in addition |Λ|=t^(mb) and 2|A|M^m<t^m, these conditions are impossible for every b≥2.

*Proof.* For λ∈Λ∩b₀Nh, centrality of b₀ modulo N, λ²=1 and P∩N=1 imply h²=1. Suppose its block permutation has at least two transposed pairs. In each such pair, the two A-valued internal arrows of h are inverse. Conjugation by an element of the full base A^b makes both arrows identity on every moved pair, and acts separately on fixed blocks. Replace λ by the same P-conjugate; it remains in Λ. By property 1 the normalized h has identity local T-automorphism arrows on the moved blocks: its remaining base components are supported on fixed blocks and act trivially outside them. Its fixed blocks may have arbitrary internal involutions.

On a moved pair of factors, λ has two inverse arrows in the outer coset α Inn(T), because b₀ supplies α and the normalized h supplies identity there. Independently conjugating by elements of the two T factors makes both arrows α: for one arrow x choose the inner adjustment x⁻¹α, and involutivity forces the opposite arrow. Do this using an element of N supported only on the moved blocks. The resulting μ remains in Λ and has α on every moved arrow; its entire restriction to the fixed blocks is unchanged. In particular that restriction squares to 1.

Choose a 3-cycle ρ on three points from two distinct moved block pairs. It lies in A_b≤R, is supported on moved blocks, and changes the matching. Property 1 makes ρ a pure block permutation with identity local arrows. Thus ν=ρμρ⁻¹∈Λ agrees with μ on every fixed block and has α-arrows on a distinct matching of the moved blocks. The product μν is identity on fixed blocks and has identity local arrows on moved blocks, since α²=1. Its block permutation is a nonidentity product of the two distinct matchings, so μν is a nonidentity pure block permutation in P. This contradicts P∩Λ²={1}.

The admissible block permutations are the identity and at most binom(b,2) transpositions. For each, at most |A|^b elements h∈P project to it, including labels which are not involutions; summing the assumed fibre bound gives (1). The number 1+binom(b,2) is at most 2^(b−1), since it counts subsets of sizes 0 and 2 among the even subsets of a b-set. Therefore, if 2|A|M^m<t^m, the right side of (1) is strictly less than t^(mb), as required. ∎

The lemma uses the coherent pure-block arrows, full base and block-local base arrows explicitly. It does not apply automatically to an arbitrary subgroup of a wreath product, a nonconstant marked automorphism or a block action whose required 3-cycle is unavailable.

## The S₇ family

Let T=A₆≅PSL₂(9), t=360, A=S₇ and m=7. The [capacity control](tw-imprimitive-capacity-control.md) constructs, for every b≥2, P=S₇ wr S_b and a primitive regular-socle group G=T^(7b)⋊P in coherent induced coordinates. Its constant marked involution b₀ has the PSL₂(9) field automorphism α on every factor, normalizes G and centralizes G/N; pure block permutations have identity local arrows, and each S₇ base factor acts trivially outside its own block. The latter follows from the induced construction because the local homomorphism is trivial on all other base factors. These structural assertions remain inputs with the review scope of that manuscript, rather than consequences of the numerical bound here.

The reviewed [factorwise capacity result](tw-psl2-factorwise-inversion.md#odd-characteristic-field-actions-a-transversal-capacity-obstruction) gives M=1+3·15=46 for every involution fibre, including fibres with fixed factors or swapped pairs. Exact arithmetic gives

    2·7!·46^7 < 360^7,

or equivalently 10080·23^7<180^7. Thus the lemma rules out a set Λ with |Λ|=360^(7b) and the stated conjugacy and collision properties for every b≥2. In particular the cardinality-only control does not produce a marked Bol transversal. Under the canonical folder/inverting-automorphism interface of C0007, this excludes a simple nonassociative left Bol folder with this exact group, complement and marked inversion action. It does not exclude other actions on the same socle, all imprimitive factor actions, or all TW groups.

The block-rematching lemma, its induced-coordinate application and the integer comparisons have the exact-source reviews recorded below. The numerical comparisons are exact integer arithmetic; no loop census or formal verification is claimed.

## An infinite alternating-socle family

This specialization is included in the exact-source reviews below. Let n≥5 and b≥2. For n≠6 take T=A_n, P=S_(n+1) wr S_b in its natural action on k=(n+1)b factors, Q=(S_n×S_(n+1)^(b−1))⋊S_(b−1), and θ:Q→Aut(T)=S_n the pointed S_n conjugation action, trivial on the other base factors and S_(b−1). Choose any odd involution α∈S_n and use the constant marked action b₀=(α,…,α). For n=6 take the same S₇ wreath construction as above but allow any constant outer involution α∈Aut(A₆), including field and diagonal types. Under these precise induced embeddings and the canonical folder interface, no marked transversal Λ exists for any n≥5 and b≥2.

For the alternating-group automorphism input, R. Lyons, *Notes for Math 555, Spring 1999: Finite Group Theory*, version 30 March 1999, Theorem 11.2, printed p.42, [primary notes](https://sites.math.rutgers.edu/~lyons/math555/nnotes.pdf), states Aut(A_n)≅S_n for n≥5, n≠6, with the exceptional index-two extension of S₆ in Aut(A₆). The PSL₂(9) field identification is the separate source input of the capacity control. No global classification of primitive TW groups follows from this family.

The induced group G=T^k⋊P is primitive on its regular-socle cosets by the same nonextension argument as in the capacity control. The local map θ has image containing Inn(T), and cannot extend to the pointed block stabilizer: an extension would restrict to S_(n+1)→Aut(T)=S_n extending its faithful S_n subgroup. The only nontrivial proper normal subgroup of S_(n+1) is A_(n+1), so every such homomorphism has image of order at most 2. The point stabilizer is maximal in the block stabilizer; any larger subgroup moving the pointed block contains the full base, by conjugating Q. The subdirect-diagonal argument in the control then gives maximality of P in G. The case n=6 uses that control's separate Aut(A₆) calculation.

For n≠6, Out(T)=C₂; therefore conjugation by α changes every local arrow of P only by an inner automorphism. The constant b₀ normalizes G and centralizes G/N; it is outside G because P's action on factors is faithful and α is outer. For n=6, Out(A₆)≅C₂² is abelian, so the same argument applies to every constant outer involution α, whether field or diagonal. The local S₆ embedding is unchanged. The full inverted-element generation argument in the field-type control is not asserted for the diagonal case. The standard compatible induced coordinates have pure block permutations with identity local arrows, and each base S_(n+1) factor acts trivially outside its own block: the local homomorphism θ is trivial on every other base factor. Thus the block-rematching lemma applies as soon as a uniform fibre bound M is supplied.

Let i_n be the number of involutions **including the identity** in S_n. At every fixed factor, an involutory arrow is among these i_n elements. On a swapped pair, one arrow determines the inverse and has at most t=|A_n| choices in its prescribed inner coset. Every permutation is a product of two involutions (reverse the order in each cycle), so i_n²≥n!≥t. Hence M=i_n bounds each fixed-site capacity and satisfies M²≥t; every fibre has at most M^k involutions.

For n≥7 put a_n=i_n/n!. The recurrence i_n=i_(n−1)+(n−1)i_(n−2) gives a_n=(a_(n−1)+a_(n−2))/n. Directly i_7=232 and i_8=764, so a_7≤1/16 and a_8≤1/18. Induction yields a_n≤1/[2(n+1)] for all n≥7: using the two preceding bounds, the recurrence gives

    a_n ≤ (1/(2n)+1/(2(n−1)))/n ≤ 1/(2(n+1)).

Therefore t/M=(n!/2)/i_n≥n+1. Since 2(n+1)!<(n+1)^(n+1), the lemma's inequality 2|A|M^(n+1)<t^(n+1) follows with A=S_(n+1).

For n=5, the inner involutions including identity number 16, the outer involutions number 10, and 16²≥60; take M=16 and verify 2·6!·16^6<60^6. For n=6 the PSL₂(9) local counts give at most 46 involutions in every outer coset, so M=46: the inner coset has 46 including the identity; the field coset has 30; the diagonal coset has 36 (its unique involution class has T-centralizer 10); and the diagonal-field coset has none. The centralizer and empty-coset statements are the Guralnick–Zieve Appendix A inputs and deductions recorded in the [factorwise manuscript](tw-psl2-factorwise-inversion.md#local-involutions); for q=9 a split involution has determinant class −1, a square, so it is inner; the diagonal involution is nonsplit and its T-centralizer is q+1=10. Swapped factor pairs contribute t choices, with 46²≥360. The preceding section gives 2·7!·46^7<360^7. The lemma therefore gives the claimed marked-transversal exclusion for all listed parameters. In n=6 the diagonal-field coset contains no involutions, so the field and diagonal cases exhaust all outer involutions. The conclusion is restricted to constant outer involutions in the specified embedding.

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/e5e802101798e02d6fe6204ecaa94a629a0919c5), reviewers contributor 1, contributor 2 and contributor 3 independently accepted the entire block-rematching theorem and alternating-socle specialization under the cited induced TW, C0007 marked-folder, alternating automorphism and A₆ local-count inputs. All three checked full-base normalization, the explicit block-locality hypothesis, paired inner-arrow conjugation, unchanged fixed-block restrictions and the 3-cycle collision; the surviving label count; the uniform factorial recurrence; and the n=5,6 endpoint counts. They also checked the stated induced embeddings and their primitivity argument. The n=6 conclusion includes constant field and diagonal involutions without importing full inverted-element generation for the diagonal case. No reviewer claimed a fresh primary-source audit, computational census or formal verification. Arbitrary subwreath actions, nonconstant marked involutions and general TW groups remain outside the theorem.

## Nonconstant factorwise marks in the same embeddings

**Further deduction, with its separate exact-source reviews below.** Keep the specified alternating-socle induced groups G=N⋊P above, with k=(n+1)b. Suppose β=(βᵢ)∈Aut(T)^k is a factorwise involution outside G, normalizes G and satisfies [β,P]≤N. Then the same exclusion holds for Λ⊂βG. No equality of the T-conjugacy classes of the βᵢ is assumed.

To prove this, take the coordinate images in Out(T), which is abelian for every listed T. The commutator condition implies that P preserves their tuple. Local arrow conjugation has no effect in this abelian outer group, so transitivity forces one common outer class c. It is nontrivial, since otherwise β∈N≤G. Every βᵢ is therefore an outer involution. Put α=β₁ and γ=(α,…,α); then βγ⁻¹∈N and βG=γG. The constant γ normalizes G and is trivial on G/N, because conjugating each local arrow changes it only by an inner automorphism. It is outside G because its factor permutation is trivial and P acts faithfully on factors.

The proved constant-mark theorem applies to the same set Λ⊂γG: it requires involutions, G-conjugacy invariance, P∩Λ²={1} and |Λ|=|T|^k, but does not require γ∈Λ. Thus Λ is impossible. At n=6 the field and diagonal cases exhaust the outer cosets containing involutions, and both are covered above. This argument changes neither the distinguished canonical mark nor the loop by isotopy; it uses equality of the ambient cosets only. Marks permuting factors, marks acting nontrivially on G/N, and other complements remain outside the result. The earlier source reviews cover the constant theorem; this deduction has its own review record below.

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/61d3badf2ff9cb4896a26ae0c701020c01a81d95), reviewers contributor 1 and contributor 2 independently accepted the appended factorwise-mark reduction, conditional on the reviewed constant theorem. They checked the common outer class, nontriviality from β outside G, coset equality, normalization by the constant representative and applicability without selecting that representative into Λ. Neither review changes the canonical mark or invokes isotopy. Factor-permuting marks, nontrivial quotient action and other embeddings remain outside this extension. No computation, fresh primary-source audit or formal verification was performed.


## All normalizing involution marks for these wreath groups

**Independently reviewed extension.** Let n≥5, b≥2, m=n+1, k=mb, T=A_n, P=S_m wr S_b in its natural action on k factors, N=T^k, and G=N⋊P in the coherent induced wreath embedding above. For n=6 use the A₆≅PSL₂(9) embedding specified there. Under the folder and local involution-count inputs above, there is no Λ⊂βG consisting of involutions, invariant under G-conjugation, with P∩Λ²={1} and |Λ|=|T|^k, for any involution β∈Aut(T) wr S_k that normalizes G and lies outside G. The exact-source review below covers this extension separately from the preceding reviews. It applies only to this full S_b block action and the specified groups, not all TW groups.

### Factor permutation and outside coset

The factor permutation σ of β normalizes the faithful factor action P. In fact N_{S_k}(P)=P. To see this, soc(P)=A_m^b: the product of the simple alternating groups in the base is a minimal normal subgroup because S_b is transitive on the blocks. Any other minimal normal subgroup must intersect the base; if it were disjoint, it would centralize the base, whose centralizer in S_k is trivial. Its intersection with the base contains the product of A_m factors and hence is not a different minimal normal subgroup. Thus soc(P) is characteristic and its orbits are exactly the given m-point blocks. Every element of N_{S_k}(P) therefore preserves that partition and lies in its full stabilizer S_m wr S_b=P.

Let p_σ∈P be the element with factor permutation σ, and set δ=βp_σ⁻¹. Then δ is factorwise and normalizes G. Since P acts faithfully on factors, δ induces the identity on G/N: conjugating an element of P preserves its factor permutation. Out(T) is abelian (C2 for n≠6 and C2² for n=6), and δ's outer tuple is P-invariant because [δ,P]≤N. Transitivity of P makes all its outer entries equal to a common c∈Out(T). It is nontrivial, since otherwise δ∈N and β∈G. Moreover c²=1: σ²=1 follows from β²=1, so p_σ²=1; taking outer coordinates in β²=δ(p_σδp_σ⁻¹) gives c² at every factor.

Choose γ∈Aut(T) representing c, for instance one coordinate of δ, and put z=(γ,…,γ). We need not assume γ²=1; in particular γ may have order 4. Coordinatewise δz⁻¹∈N, so βG=δG=zG. As Out(T) is abelian, z normalizes G and centralizes G/N; it lies outside G because c≠1 and P is faithful. Also z²∈N. This is only equality of outside cosets: no replacement of a distinguished Λ-element, no isotopy, and no assertion z∈Λ is used.

### Oriented block-rematching

Let λ∈Λ∩zNh. Since z acts trivially on G/N, z²∈N, and λ²=1, the label h∈P is an involution. Suppose its block action has at least two transposed pairs. Full base conjugation in P makes the internal S_m arrows of h identity on every moved block pair. In the compatible coordinates, pure block arrows are identity, and the remaining base components lie on fixed blocks and act trivially outside their blocks. By G-conjugacy invariance we may replace λ by the corresponding conjugate.

Orient each moved block pair by selecting a positive and a negative block. On each corresponding pair of T factors, the two λ-arrows have outer class c=c⁻¹ and are inverse, because λ²=1. Independent inner conjugation, supported only on moved factors, makes the arrow from positive to negative equal γ and the reverse arrow γ⁻¹. Denote the result by μ∈Λ. The restriction of μ to the fixed blocks is untouched and squares to the identity.

Choose a pure block transposition ρ swapping the two positive blocks of two different pairs, fixing the negative blocks and all fixed blocks. This is in S_b and has identity local arrows. Then ν=ρμρ⁻¹∈Λ has a different matching but retains the same positive/negative orientation and agrees with μ on fixed blocks. A composition of the two matching maps crosses the bipartition twice. Its local arrows are one γ and one γ⁻¹, so their product is the identity regardless of the order of γ. Its restriction to fixed blocks is μ²=1, while its block permutation is the nonidentity product of two distinct matchings. Hence μν is a nonidentity pure block permutation in P, contradicting P∩Λ²={1}. Thus labels with nonempty Λ∩zNh have at most one block transposition.

The transposition ρ may be odd; this step uses the **full** S_b top, not merely A_b. A 3-cycle does not generally preserve a chosen bipartition, so the earlier involutory-α lemma cannot simply be reused for arbitrary γ. The present argument explicitly handles γ² merely inner.

### Capacity

At most (m!)^b(1+binom(b,2)) labels h have the required block permutation, and 1+binom(b,2)≤2^(b−1). At fixed factors the possible λ-arrows lie in a prescribed outer coset of Aut(T); at a transposed pair one arrow has |T| choices and the other is forced. For n≠6 all outer cosets are subsets of S_n, so the number i_n of involutions including 1 in S_n bounds every fixed site, and i_n²≥|T|. The same recurrence and inequalities from tw-cross-label-block-exclusion.md give 2m! i_n^m<|T|^m for n≥7, and the sharper fixed-site bound M=16 works for n=5.

For n=6 the four outer cosets have, respectively, 46, 30, 36 and 0 involutions including 1 in the inner coset, so M=46 bounds all; 46²≥360 and 2·7!·46^7<360^7. In particular this handles the diagonal-field coset c even though that coset has no involutory single-coordinate representative. In all cases the number of possible elements of Λ is strictly less than |T|^k, contradiction. The coset involution counts and their source are recorded in tw-cross-label-block-exclusion.md.

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/1f6ec90b98eb67b6966ea4a4455dbd2f999d0311), reviewers contributor 1, contributor 2 and contributor 3 independently accepted the entire all-marks extension, conditional on the cited induced embedding, marked-folder interface and local coset counts. They checked the permutation normalizer, common outer coset without an involutory representative, oriented rematching and all-coset capacity, including the A₆ diagonal-field case. No fresh primary-source audit, computation or formal verification was performed. This result does not classify all TW embeddings, all Bol loops, or all groups with these socles.
