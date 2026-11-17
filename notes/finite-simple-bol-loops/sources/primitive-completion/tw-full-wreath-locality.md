# Automatic locality for primitive full-wreath factor actions

**Mira Cult**

This independently reviewed theorem concerns the induced twisted-wreath setup of [C0010](../../claims/0010.md) and [the block-rematching theorem](tw-cross-label-block-exclusion.md). The factorwise-mark extension of that theorem was reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/61d3badf2ff9cb4896a26ae0c701020c01a81d95); that review does not cover this new locality argument. It gives a structural theorem for a **full** wreath factor group, not arbitrary subwreath complements. It uses the local-image and induced-function interfaces of Liebeck–Praeger–Saxl, *On the O'Nan–Scott theorem for finite primitive permutation groups*, J. Austral. Math. Soc. A 44 (1988), §1 III(c), p.391, https://doi.org/10.1017/S144678870003216X.

## Theorem

Let T be a finite nonabelian simple group, let A≤S_m and R≤S_b be transitive, with m,b≥2, and let P=A wr R in its natural imprimitive action on k=mb factors. Fix a point x in a distinguished block, put Q=P_x, and let θ:Q→Aut(T) have image containing Inn(T). In the induced twisted wreath G=T twr_θ P, suppose P is maximal in G (equivalently its coset action has regular socle N=T^k and is primitive). Then θ is trivial on

    J=A^(b−1)⋊R_1,

and θ(A_x) contains Inn(T), where Q=A_x×J. Consequently there are compatible induced wreath coordinates in which (i) pure R block permutations have identity local automorphism arrows, and (ii) each base A_j acts trivially, in both factor permutation and local arrows, outside block j.

*Proof.* Let B be the stabilizer of the distinguished block. Then

    Q=A_x×J,       B=A×J,       J=A^(b−1)⋊R_1,

where the direct-product symbols are literal: R_1 fixes that block and acts only on the other factors. Let L=θ(Q)≤Aut(T), and L1=θ(A_x), L2=θ(J). The subgroups L1,L2 are commuting normal subgroups of L with L=L1L2, and T=Inn(T) is a normal subgroup of L. Each L_i∩T is normal in T, hence is either 1 or T. If L_i∩T=1, then [L_i,T]≤L_i∩T=1, so L_i=1 because C_Aut(T)(T)=1. Therefore exactly one of L1,L2 contains T and the other is trivial: both trivial would contradict T≤L, and both containing T would contradict their commutation.

Suppose L2 contains T. Then L1=1, so θ extends to B=A×J by killing A and using θ|J. In the standard induced-function model, N consists of functions f:P→T satisfying f(xq)=θ(q)⁻¹(f(x)) for q∈Q, with P acting by left translation of the argument. Using the extension θ̃ on B, impose the stronger relations f(xv)=θ̃(v)⁻¹(f(x)) for v∈B. These functions form a P-invariant subgroup of N isomorphic to T^[P:B]: choose one value freely on each coset xB and extend by equivariance. It is proper and nontrivial because Q<B<P. It gives an intermediate subgroup between P and G, contradicting maximality of P. Thus L2=1 and L1≥T.

For the coordinate assertion, choose a point x in the distinguished block, elements a_y∈A with a_y(x)=y for its m points, and r_j∈R with r_j carrying the distinguished block to block j. Use the representatives obtained by first moving x to y with a_y in the distinguished A-factor and then moving that block with r_j. In the induced construction, an element’s local arrow at a factor is θ applied to the stabilizer cocycle obtained by comparing the chosen representatives before and after its action. For a pure R element, this cocycle lies in R_1≤J; θ maps it to 1. For an element of A_j acting outside block j, the factor is fixed and the stabilizer cocycle lies in a different base factor inside J, so θ again maps it to 1. Its factor permutation is already trivial outside j. This establishes (i)–(ii). ∎

## Consequence for marked involutions

Assume also that R≥A_b, Out(T) is abelian, and β=(β_i) is a factorwise outside involution normalizing G and centralizing G/N. Its outer coordinate classes are equal by transitivity; because β∉G they form a nontrivial class c. Choose α=β_1 and z=(α,…,α). Then z²=1, βG=zG, z normalizes G and centralizes G/N. No assumption z∈Λ is needed. The preceding theorem supplies precisely the full-base, block-local and pure-block-coordinate hypotheses of the block-rematching lemma in tw-cross-label-block-exclusion.md. If M bounds the number of involutions in every relevant prescribed Aut(T)/Inn(T) coset and M²≥|T|, the lemma gives

    |Λ|≤|A|^b(1+binom(b,2)) M^(mb).

Thus no marked transversal of size |T|^(mb) exists when 2|A|M^m<|T|^m. This applies, for example, to the reviewed odd-field PSL₂(s²) inversion action with its reviewed M, whenever the numerical inequality holds. It allows arbitrary transitive A and arbitrary R≥A_b, not merely the alternating-socle S_m examples, but requires equality P=A wr R and all the displayed marked-action and local-image hypotheses. It says nothing about a proper subwreath factor group or an arbitrary factor-permuting mark.

The locality theorem, induced coordinates and consequence have the exact-source reviews below. The all-marks theorem for the particular alternating wreath group does not automatically extend here; normalizers and factor-permuting marks remain separate obligations. The existing block lemma and numerical bounds retain their own exact-source review records; no status promotion or universal TW exclusion is asserted.

## Independent review

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/51b6561382dc02971f5c8e760d837c58f9316ec9), reviewers contributor 1 and contributor 2 independently accepted the complete theorem and consequence, conditional on the cited induced-function and previously reviewed block-rematching interfaces. They checked the commuting-image dichotomy, extension to B and the resulting proper invariant subgroup, explicit coordinates, common outer coset and capacity hypotheses. No computation, fresh primary-source audit or formal verification was performed. Full wreath equality, the factorwise-mark hypothesis and the numerical condition remain essential to the stated consequence.
