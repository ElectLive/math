# Suzuki and small Ree full multiplication socles

Mira Cult

Continuation of [0323:C0010](../foundations/research-C0010.md), with three independent exact-source reviews recorded below.

**Conditionally proved theorem.** For every finite simple proper left Bol loop Q, its full multiplication group M cannot have socle Sz(2^f) or ²G₂(3^f), for any odd integer f≥3, under the inputs below. Both actual factor orientations and all field-outer lifts are included. This concerns full Mlt(Q), without identifying it with the canonical G=LMlt(Q). The nonsimple ²G₂(3) is outside the socle statement; its derived PSL₂(8) is covered by the separate full-PSL₂ result.

## Exact inputs

Use the [canonical definitions](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped canonical inversion from C0007 at `932ead5db5f39045e2085caa6b062f6b981b2813`, C0008's primitive almost-simple full-group result at `06857e28349ca4529c31a9855ce12cfbb191c1b7`, and the reviewed inner-inversion/component obstruction at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`. These are scoped inputs, not aggregate claim promotions. Write I=M₁, S=Soc(M), G₀=G∩S and I₀=I∩S.

[Li–Xia arXiv:1408.0350v3](https://arxiv.org/html/1408.0350v3), Proposition4.2, printed p.28, rules out a factorization of an almost-simple exceptional group by two core-free factors when either factor is solvable. [Patassini2009](https://msp.org/pjm/2009/240-1/pjm-v240-n1-p07-p.pdf), Theorems10–11, printed p.192, gives the complete maximal-subgroup lists for Suzuki and small Ree groups, attributing them to Suzuki1962 and Kleidman1988. The standard order formulas and cyclic outer order f are retained from the pinned BPP17-outer source in [REFERENCES](../foundations/references.md). These classification statements are external inputs. The source authors freshly inspected Li–Xia Proposition4.2 and both Patassini lists; their original classification proofs have not been rederived.

## Actual factors and the socle-containing orientation

Transitivity of G gives M=GI, with I core-free. If S≤G, then G is almost simple with characteristic socle S. The canonical involutory automorphism τ restricts to an inner automorphism of S, since Out(S) is cyclic of odd order f. Choose s∈S realizing that restriction. An automorphism β of G fixing S pointwise is trivial: for every g∈G, β(g)g⁻¹ centralizes S, while C_G(S)=1. Thus composing τ with the inverse of conjugation by s gives the identity on G, so τ is inner. This contradicts the pinned component obstruction. Therefore S is not contained in G.

Both G and I are now core-free in M. Li–Xia excludes either being solvable. Their quotients by G₀ and I₀ respectively embed in cyclic M/S, so G₀ and I₀ are nonsolvable proper subgroups of S. Here I₀=S is impossible since I is core-free and S is nontrivial normal in M. If d=|M/S|, the actual factorization gives

    |S|=|M|/d ≤ |G||I|/d ≤ d |G₀||I₀| ≤ f |G₀||I₀|.

No factorization S=G₀I₀ is asserted or needed.

## Suzuki groups

Put q=2^f. Every nonsolvable proper subgroup lies in a proper subfield Suzuki subgroup Sz(q₀), where q=q₀^r for an odd prime r, by Patassini Theorem10. All other maximal types in that list are solvable. Consequently

    |G₀|, |I₀| < q^(5/3),

because |Sz(q₀)|=q₀²(q₀²+1)(q₀−1)<q₀⁵ and q₀≤q^(1/3). The nonsimple Sz(2) subfield, if present in the list, is solvable and cannot contain either nonsolvable intersection. Hence |S|<f q^(10/3). On the other hand

    |S|=q²(q²+1)(q−1)>q⁵/2.

For f≥3, 2f≤2^f=q<q^(5/3); the first inequality follows at f=3 and persists by doubling. Thus f q^(10/3)<q⁵/2, a contradiction.

## Small Ree groups

Put q=3^f. Patassini Theorem11 leaves only C₂×PSL₂(q) and proper subfield Ree groups among the nonsolvable maximal types. The first has order q(q²−1)<q³. A subfield group has q=q₀^r with r an odd prime and

    |²G₂(q₀)|=q₀³(q₀³+1)(q₀−1)<q₀⁷≤q^(7/3)<q³.

This explicitly retains the nonsimple but nonsolvable subfield ²G₂(3)≅PSL₂(8):3 of order1512 when it occurs; it is not discarded at q=27. Therefore |G₀|,|I₀|<q³ and |S|<f q⁶, whereas

    |S|=q³(q³+1)(q−1)>q⁷/2.

The elementary inequality 2f<3^f=q for f≥3 gives f q⁶<q⁷/2, a contradiction.

## Scope and evidence

Apart from the canonical G≥S case, the proof shows that no almost-simple overgroup of either family admits a factorization by two proper core-free subgroups, conditional on the quoted classifications. Its inequalities hold for all stated field degrees; no numerical census or research-code execution is used. It excludes these two full multiplication socle families and leaves the other Lie-type families and the natural alternating loop operations open. Independent exact-source mathematical reviews are recorded below; repository integrity checks alone cannot certify this deduction.


### Independent review

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `016d680964c9c937ee74e93df744087746942280`. Each checked the socle-containing inner-inversion deduction, the actual-factor order inequality, both uniform subgroup bounds and the nonsolvable Ree3 subfield at q=27. Each directly inspected Li–Xia v3 Proposition4.2 and Patassini2009 Theorems10–11 on printed p.192. All retained the pinned canonical/component and cyclic odd-Out descriptions as inputs; none newly proved the underlying subgroup classifications or freshly audited the separate outer-group source. No research computation was required. The source authors's separate Python3.12.14 integrity run passed115 tests. These are model mathematical reviews of the two displayed full-socle families, not formal/human certification or GitHub approvals, and do not settle other Lie types or C0010.
