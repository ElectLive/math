# Exceptional socles and field-involution collisions

Mira Cult

Continuation of [0323:C0010](../foundations/research-C0010.md). Three independent exact-source mathematical reviews are recorded below.

**Conditionally proved full-socle theorem.** Under the inputs below, no finite simple proper left Bol loop has full multiplication socle E₈(q), ³D₄(q), E₇(2^f), F₄(q) for odd q, or ²F₄(2^f) for odd f≥3. Here q is any prime power for which the indicated group is simple. The same argument excludes every almost-simple **canonical** group with socle G₂(q), q>2; [the separate G₂ assembly](g2-full-socles.md) handles its proper-factor cases. Nothing here excludes odd-characteristic E₇, arbitrary E₆, or even-characteristic F₄ full socles.

## Exact inputs and notation

Use the [canonical definitions](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped canonical inversion and marked-set interface at `932ead5db5f39045e2085caa6b062f6b981b2813`, C0008's primitive almost-simple full-group result at `06857e28349ca4529c31a9855ce12cfbb191c1b7`, and the inner-inversion/component obstruction at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`. These remain scoped inputs rather than aggregate claim promotions. Write M=Mlt(Q), G=LMlt(Q), I=M₁ and S=Soc(M). The original marked set Λ consists of outside involutions in the canonical split extension, is G-invariant, and satisfies |Λ|=[G:H] and Λ²∩H={1}, where H=G∩I.

The following source statements are external inputs; exact inspected versions and limits are recorded in [REFERENCES](../foundations/references.md).

* Burness–Guralnick–Harper, **arXiv:2006.01421v2**, §3.2 Table2, p.19, gives the cyclic outer groups used here: order f for E₈, even E₇, odd F₄ and G₂ in characteristic other than3; order3f for ³D₄; order2f for characteristic-three G₂; and odd order f for ²F₄. Here q=p^f. Example3.22 p.24 explicitly identifies the adjoint E₇ fixed groups with the simple finite groups in characteristic two.
* Kazarin–Martínez-Pastor–Pérez-Ramos2015, **Lemma11 proof, pp.56–57**, quotes **Liebeck–Praeger–Saxl1990 TheoremB**, its reference[19]: exceptional almost-simple proper factorizations can have only socles G₂(3^f), G₂(4) or F₄(2^f). We use this quoted general classification statement, not the lemma's conclusion about π-decomposable factors. The original LPS theorem was not freshly inspected for this deduction.
* Dudas–Michel, **Beijing lectures2015**, Theorem7.3 p.24, gives Lang–Steinberg for connected affine algebraic groups and isogenies with a Frobenius power. Section7.4 p.29 gives the exceptional isogenies whose squares are Frobenius and their Suzuki/Ree fixed groups.
* Burness–Thomas, **author PDF `BTh_revised_2.pdf`**, Remark2.2/Proposition2.3 p.8 and Table5 p.10, gives the involution classes and, for the split types E₈, E₇ and F₄ used below, their correspondence with algebraic classes. The proof of Proposition3.3 p.12 identifies the two even-G₂ classes as long- and short-root classes. The table gives one class for odd G₂ and odd ³D₄. We do not apply the blanket algebraic-class wording to split D₄ under triality.
* Aschbacher–Seitz1976, **§18(18.2) p.74 and §19(19.1)–(19.2) p.76**, gives the two even-³D₄ root representatives, and the field outside-class/centralizer statements. Their relative-root conventions are retained below.

## Cyclic outer reduction

Suppose the entire canonical G is almost simple with characteristic socle S and cyclic Out(S). Restriction Aut(G)→Aut(S) is injective: an automorphism fixing S pointwise satisfies a(g)g⁻¹∈C_G(S)=1 for every g. Under the faithful conjugation embedding, restriction β of a induces conjugation by β on G. Since Out(S) is abelian, every automorphism of G acts trivially on G/S. But canonical τ inverts the generating set K, so it induces inversion on this abelian quotient. Hence G/S has exponent at most2.

If G>S, this quotient is the unique subgroup of order2 in cyclic Out(S). The restriction of involutory τ has outer label of order at most2, so it belongs to G, which is the full inverse image of G/S in Aut(S). Injectivity of restriction now makes τ inner on G. The pinned component obstruction excludes this. Thus G=S, and τ cannot be inner. If Out(S) has odd order this is already impossible. Otherwise every admissible τ has the unique nontrivial involution label in Out(S).

## A single outside class

Let 𝔛 be connected, α a Steinberg isogeny and S=𝔛^(α²), with σ=α|S an outer involution representing that label. All involutions in Sσ form one S-class. Indeed, for (gσ)²=1, Lang–Steinberg supplies b∈𝔛 with g=b⁻¹α(b). Then

    1=gα(g)=b⁻¹α²(b),

so b∈S and gσ=b⁻¹σb. The formal canonical extension identifies faithfully with S⟨σ⟩ after conjugating τ, and its nonempty S-invariant Λ must be this entire class. Consequently

    |H|=|S|/|Λ|=|C_S(σ)|=|𝔛^α|.                 (1)

Suppose the fixed subgroup has even order and meets every S-involution class. For each fixed involution u, both σ and σu are outside involutions, hence belong to Λ. Thus u∈Λ². S-invariance makes Λ² contain every S-involution. Equation(1) makes H even, yielding a forbidden involution in H∩Λ². This is a collision in the original marked set, without a projected-folder assumption.

## Split field cases

For S=E₈(q), E₇(q) in characteristic two, F₄(q) in odd characteristic, or G₂(q) in characteristic other than3, the cyclic outer reduction leaves only even f. Put s=p^(f/2), take the connected split algebraic group of the same type, and α=F_s. Then S=𝔛^(α²) and C_S(σ) is the corresponding group over s, of even order. For even E₇ the source explicitly ensures these are the simple finite groups, including s=2; no missing diagonal quotient is discarded.

For E₈, even E₇ and odd F₄, apply the cited natural algebraic/finite involution-class correspondence twice, for s and q, in the same algebraic group. Each algebraic class has a representative in the s-group, and its q-group intersection is a single q-class. Thus every S-class meets the fixed subgroup. This is a deduction from the two correspondences, not an assumption that arbitrary subfield class fusion is surjective.

Odd G₂ has one involution class, so Cauchy's theorem in the even fixed subgroup suffices. For even G₂ the two classes have parameter-one long- and short-root representatives x_r(1), already defined over the prime field. Both lie in G₂(s). This includes q=4, s=2, where the fixed subgroup need not be simple. The collision argument therefore excludes all these canonical groups.

## Characteristic-three G₂

Let q=3^f. If f is even, the unique order-two label in cyclic Out(S) is represented by F_(3^(f/2)), so the preceding argument applies. If f is odd, take the exceptional algebraic isogeny ρ with ρ²=F₃, and put α=ρ^f. Then α²=F_q, σ is the unique outer involution label, and 𝔛^α=²G₂(q). This fixed group is even, including the nonsimple group at q=3 (order1512). Since G₂(q) has a single inner involution class, it meets the fixed subgroup. The original-mark collision excludes the canonical group for every f≥1.

## Triality

For S=³D₄(p^f), Out(S) is cyclic of order3f. Odd f is excluded by the cyclic outer reduction. If f is even put s=p^(f/2), choose the pinned order-three diagram automorphism γ of connected algebraic D₄, commuting with field maps, and set

    F=γF_q,       α=γ²F_s,       α²=F.

Its finite fixed groups are S=𝔛^F=³D₄(q) and 𝔛^α=³D₄(s), with inverse triality convention. These equalities use the standard triality construction and absence of diagonal automorphisms in the cited automorphism input. On S, F_q=γ⁻¹, so α|S=F_s³ has the nontrivial involution outer label. The fixed subgroup is even.

In odd characteristic S has one involution class, and Cauchy suffices. In characteristic two the cited Aschbacher–Seitz §18 representatives U_r₅(1), U_r₆(1) represent both classes. In the relative-root construction, a long root corresponds to a γ-fixed absolute root and a short root to an orbit of three mutually orthogonal absolute roots. At parameter1 its representative is respectively x_r(1) or the product of the three commuting x_r(1). These are fixed by γ² and F_s, and so belong to 𝔛^α. Reversing the cycle γ does not change this parameter-one product. Weyl conjugation within the relative G₂ root system gives the named r₅,r₆ representatives. Thus both finite classes meet the fixed subgroup. This explicitly verifies the subfield interface instead of appealing to an algebraic D₄ class bijection. Aschbacher–Seitz §19(19.1) separately confirms the single field-involution class and the ³D₄(s) centralizer in this characteristic. The collision lemma applies for all q.

## Full-socle consequences

For S equal to E₈(q), ³D₄(q), E₇(2^f), odd F₄(q), or ²F₄(2^f) with odd f≥3, transitivity gives M=GI. If S is not contained in G, both G and I are core-free: I cannot contain a nontrivial normal subgroup of the faithful primitive M. The quoted exceptional-factor classification excludes this proper-factor alternative for every displayed family. Hence S≤G. The first four families were excluded above; the large Ree family has cyclic odd-order Out(S), so the cyclic outer reduction excludes it immediately. This proves the stated conditional full-socle conclusions. For G₂ the proper-factor alternatives remain and are handled in the linked assembly.

## Evidence and limits

The source authors inspected the exact source statements cited above, including both field sizes in the class-correspondence deduction and the Aschbacher–Seitz relative-root/outside-class interfaces. These are source-qualified proofs, with no new finite census or research executable. The cited classifications and canonical inputs have not been rederived. Independent exact-source reviews are recorded below, and repository integrity checks do not establish the mathematical conclusions. The remaining socles and the natural alternating loop operations remain open.


### Independent review

automated-model reviewer A, reviewer B and reviewer C independently accepted this manuscript and its linked companion at exact source `cd5bf6a31bc63eb838b3150e51dd7aaec57be838`. All checked the cyclic outer reduction, original outside-class collision, split subfield correspondence, inverse-triality parameter-one roots, actual G₂ factor placements and even intersections, Ree3 derived subgroup, and the component collision without assuming faithful centralizer action. Each freshly inspected the KMP2015 Lemma11 actual-factor statement. The paired reviewer additionally freshly inspected BGH v2 Table2/Example3.22, Dudas–Michel Theorem7.3, Burness–Thomas Remark2.2/Proposition2.3 and Aschbacher–Seitz18.2/19.1–19.2; that reviewer retained the exact exceptional-isogeny construction as a cited input. The other two retained the recorded external automorphism/class/root inspections without freshly browsing those sources. None rederived the underlying classifications. No research computation was required; the source authors's separate Python3.12.14 integrity run passed115 tests. These model mathematical reviews have exactly the displayed family scope and are not formal/human certification, GitHub approvals or a solution of unrestricted C0010.
