# Paired simple socles in radical-free Bol envelopes

Mira Cult

**Scoped continuation of [classification frontier](../../claims/0010.md).** This note derives a selected-mark obstruction for any two minimal normal blocks exchanged by the canonical inversion, and gives construction, exhaustion and isomorphism data when the *entire* canonical left multiplication group is T×T for a finite nonabelian simple T. It does not assert that all radical-free canonical groups have this form, that their left multiplication actions are primitive, or that the remaining subgroup/conjugacy data form a closed list.

The canonical faithful-folder and exact normal-subloop interfaces are [Claim 0001](../../claims/0001.md), reviewed. The canonical inversion construction is [C0007, Theorem 1.1(1)](../foundations/C0007.md); C0011 records a scoped check of that construction, while C0007 aggregate review metadata remains unreviewed. The elementary Goursat step in the first section uses the CFSG-dependent result of Fried, Guralnick and Saxl, *Schur covers and Carlitz's conjecture*, Israel J. Math. 82 (1993), Lemma 12.1, [authors' PDF §12 p. 26](https://www.math.uci.edu/~mfried/paplist-ff/sch-carlitz.pdf): a finite nonabelian simple group has an involution class invariant under all automorphisms. The lemma statement and the source's explicit CFSG assumption were checked; its classification-dependent proof was not independently verified here. Independent exact-source reviews of the deductions below are recorded at the end.

## Exchanged minimal normal blocks

Let (G,H,K,τ) be a finite simple proper left Bol loop's faithful generated canonical folder. In the formal extension E=G⋊⟨t⟩, including when τ=id, the actual marked set Λ=tK is an E-conjugacy-invariant set of outside involutions containing t, and H∩Λ²=1. In even order Λ need not be the full outside involution set.

Suppose τ exchanges two distinct minimal normal subgroups N₀,N₁ of G, each isomorphic to T^k for a nonabelian simple T. Identify them through τ, so N=N₀N₁=N₀×N₁ and τ(u,v)=(v,u). Since t^N⊂Λ, K contains every (x,x⁻¹)∈N. Products of two such elements give

    {(x,y)∈N₀×N₁ : y is N₀-conjugate to x⁻¹} ⊂ Λ².       (1)

Indeed (a,a⁻¹)(b,b⁻¹) has second coordinate conjugate to (ab)⁻¹; conversely, for y=sx⁻¹s⁻¹ take a=s⁻¹, b=sx. Hence H∩N contains no nonidentity pair in (1). In particular H∩N₀ and the τ-identified H∩N₁ have trivial intersection with every conjugate of one another in N₀.

With the cited FGS lemma, D=H∩N cannot project onto both N₀ and N₁. Otherwise Goursat's lemma gives normal subgroups A,B◁T^k and an isomorphism φ:T^k/A→T^k/B with

    D={(u,v):φ(uA)=vB}.

Choose an involution c in the Aut(T)-invariant T-class and put x=(c,…,c)∈T^k. Normal subgroups of T^k are products of coordinates, and φ permutes quotient coordinates and applies automorphisms of T. Thus every coordinate of φ(xA) lies in the class of c. Lift it to y∈T^k, choosing c in coordinates belonging to B. Then y is T^k-conjugate to x=x⁻¹, so the nonidentity (x,y)∈D contradicts (1). This proves non-subdirectness. It neither bounds the number of minimal normal blocks nor says that all blocks are exchanged.

## Exact reduction for G=T×T

Assume now that G itself is T×T, T is nonabelian simple, and τ exchanges its factors. Identify them so τ is the coordinate swap. Every outside involution is t(x,x⁻¹), and all form the single G-class t^G. Since Λ contains that class, here—and only here in this argument—the actual mark is forced to be full:

    Λ=tK,    K={(x,x⁻¹):x∈T}.                              (2)

The following subgroup data exhaust this branch. Choose nontrivial proper A,B<T, normal subgroups A₀◁A, B₀◁B, and an isomorphism φ:A/A₀→B/B₀. Put C=A/A₀ and

    H={(a,b)∈A×B : φ(aA₀)=bB₀}.                          (3)

Require

    |A||B|=|T|·|C|,                                         (4)
    b is not T-conjugate to a⁻¹ for every 1≠(a,b)∈H.      (5)

These tests are necessary and sufficient for a simple proper non-Bruck folder with the displayed canonical group and inversion. Necessity follows from Goursat, |H|=|T| and (1). Conversely (4) gives |H|=|T|, and (5) gives H∩Λ²=1 because (1) is equality for the full graph (2). Thus K is a transversal to H and all conjugates, and gives a Bol folder. T is perfect, so K generates T×T. As A and B are proper in simple T, Core_G(H)=1.

The only nontrivial proper normal subgroups of G are its factors. Their K-images each have size |T|, while the corresponding quotient stabilizer indices are [T:A] and [T:B], both strictly smaller because A,B≠1. C0001's normal-subloop criterion therefore gives simplicity. H≠1 makes the loop nonassociative. It is non-Moufang: H<A×T<G, so its canonical left multiplication action is imprimitive, contrary to C0001 Lemma 1.2 for a simple nonassociative Moufang loop. Its order is |T|, which is even by the odd-order theorem.

It is non-Bruck too. If τH=H, the canonical marked collision gives H≤C_G(τ)=ΔT. Since |H|=|T|, equality would follow, but ΔT contains (u,u)∈Λ² for any involution u∈T. Thus τH≠H, and the [Bruck-stabilizer criterion](exact-factorization-criterion.md#bruck-stabilizers-and-necessary-witness-tests), reviewed, excludes Bruckness.

For the converse, a canonical simple nonassociative folder with these G and τ has (2), |H|=|T| and (5). Neither projection of H can be trivial: then |H|=|T| makes H a normal direct factor, contradicting corefreeness. They cannot both be T by the preceding non-subdirectness theorem. If A=T and B<T, Goursat makes A₀ either 1 or T. If A₀=T then C=1 and (4) forces B=1; if A₀=1 then B has a quotient T, impossible for B<T. The symmetric case is identical. Thus the nontrivial proper hypotheses and (3)–(5) are exhaustive. The CFSG-dependent FGS input is used for the non-subdirect step; the sufficiency argument otherwise retains only its cited folder inputs.

## Isomorphism and the common intersection

A loop isomorphism induces an isomorphism of canonical folders and commutes with τ, since K generates G and τ is uniquely determined by inversion on K. Every automorphism of T×T commuting with the swap is simultaneous application of one automorphism of T, optionally followed by swapping the two factors. For fixed T, two admissible data sets give isomorphic loops exactly when they are in the same orbit under simultaneous Aut(T) and factor swap; the latter interchanges A,B, A₀,B₀ and replaces φ by φ⁻¹. Across different simple groups, isomorphism first requires T≅T′, since the canonical groups T×T and T′×T′ must be isomorphic; an identification then reduces to the fixed-T criterion.

Transversality further forces T=AB and |A∩B|=|C|. Indeed G=KH, and the representation of (g,1) as a product of an element of K and one of H shows g∈BA. Set D=A∩B and H_D=H∩(D×D). If α:A→C and β:B→C are the two quotient maps, then

    |H_D|=|D|²/|α(D)β(D)|≥|D|²/|C|=|D|.                 (6)

On the other hand (5) makes K_D={(d,d⁻¹):d∈D} inject into (D×D)/H_D, so |H_D|≤|D|. Equality holds, and α(D)β(D)=C. The same collision condition gives K_D transversality to every conjugate of H_D in D×D. This smaller Bol folder gives an actual subloop of Q of order |D|, although the subloop need not be normal and K_D need not generate D×D. Thus simplicity by itself does not remove a nontrivial common quotient C. The case C=1 is the exact-factorization product H=A×B; the existence or exclusion of C>1 remains a substantive residual problem, not a claim made by this reduction.

The known Q₆₀ supplies a control: A₅=A₄·C₅ is an exact factorization, and its folder has G=A₅×A₅ with τ exchanging the two minimal normal factors. This is the existing construction recorded in C0012, not a novelty claim. The reduction above does not cover groups properly containing T×T, blocks T^k with k>1 in place of each simple factor, τ-fixed minimal blocks, or radical-free canonical groups with additional socle factors.

## Two nonproduct exclusions

The common Goursat quotient C in (3) must be a quotient of both A and B. In particular, if either projection is perfect and the other is solvable, C is both perfect and solvable, so C=1. Thus every admissible folder in that situation has product stabilizer and comes from an exact factorization. This applies only to the specified projection hypotheses; it is not a claim that one of the projections is always perfect.

For T=A₅ the residual common quotient can be eliminated entirely, and the full T×T branch has one loop-isomorphism class. The argument is elementary. The possible proper subgroup orders are

    1,2,3,4,5,6,10,12.

Indeed the only other proper divisors of 60 are 15,20,30, and subgroups of those orders would give faithful coset actions of the simple group A₅ into S₄,S₃,S₂ respectively, impossible. Equation (4) shows that C>1 would require projection orders 12 and 10 and |C|=2. An order-12 subgroup is a point stabilizer A₄: its index-5 action embeds A₅ as A₅ in S₅. But A₄ has no quotient C₂, so this possibility is impossible. Hence C=1.

The remaining order pairs for exact factorization are (12,5) and (10,6). An order-10 subgroup has a normal Sylow 5-subgroup and an order-6 subgroup has a normal Sylow 3-subgroup, so these are the corresponding Sylow normalizers D₁₀ and S₃; A₅ has no elements of orders 10 or 6. Its 24 elements of order 5 form six Sylow 5-subgroups, and its 20 elements of order 3 form ten Sylow 3-subgroups. Thus there are six D₁₀ and ten S₃ subgroups. It has 15 involutions, all double transpositions and all conjugate; counting incidences shows each belongs to two D₁₀ and two S₃ subgroups. A D₁₀ and an S₃ share at most one involution: two distinct common involutions would have product of order 5 in D₁₀ and order 3 in S₃. There are 15·2·2=60 involution incidences across 6·10=60 such pairs, so every D₁₀/S₃ pair intersects in an involution and cannot be exact.

Thus the factors are A₄ and C₅. Their orders are coprime, so every such pair is exact. All 5·6=30 pairs (point stabilizer, Sylow 5-subgroup) form one A₅-conjugacy orbit: their common normalizer has order 2, since a D₁₀ normalizer of C₅ acts transitively on the five points. The factor swap identifies the reverse ordering. Therefore the exact isomorphism criterion above gives precisely the known Q₆₀ in this T=A₅ branch. This proof does not settle whether C>1 occurs for another simple T. The scoped independent reviews below include these deductions.

## Independent review

Three independent automated model mathematical reviewers — `audit_c9_full`, `review_paired_simple` and `review_hs_full` — accepted the manuscript at exact, conditional on its cited folder, canonical-inversion, Bruck-stabilizer and CFSG/FGS inputs. Each checked the exchanged-block obstruction, full T×T construction and exact isomorphism reduction, common-intersection subloop, and analytic A5 uniqueness. `review_paired_simple` independently accessed the authors’ indexed PDF and checked the statement of FGS Lemma 12.1; its CFSG-dependent proof was not independently certified. The other two reviewers did not perform a fresh primary-source audit. No new computation was used. These model reviews neither classify arbitrary radical-free envelopes nor exclude nonproduct stabilizers for every simple T.


## Recorded source review scope

Three independent Automated source reviewers mathematical reviewers — `audit_c9_full`, an automated checker and an automated checker — accepted the manuscript at exact source the recorded source revision, conditional on its cited folder, canonical-inversion, Bruck-stabilizer and CFSG/FGS inputs. Each checked the exchanged-block obstruction, full T×T construction and exact isomorphism reduction, common-intersection subloop, and analytic A5 uniqueness. an automated checker independently accessed the authors’ indexed PDF and checked the statement of FGS Lemma 12.1; its CFSG-dependent proof was not independently certified. The other two reviewers did not perform a fresh primary-source audit. No new computation was used. These model reviews neither classify arbitrary radical-free envelopes nor exclude nonproduct stabilizers for every simple T.
