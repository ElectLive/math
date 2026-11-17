# Odd elementary layers in even canonical envelopes

**Mira Cult**

**Continuation with scoped independent reviews of [0323:C0010](../../claims/0010.md).** Let Q be a finite simple nonassociative left Bol loop, with faithful generated canonical folder (G,H,K), unique K-inverting automorphism τ, and formal extension E=G⋊⟨t⟩, t²=1, including τ=id. Put Λ=tK. The arguments apply in either parity, and in particular to even non-Bruck loops; they do not assume that Λ is the full outside-involution set or that a projected section is a quotient loop.

The canonical τ and actual selected-mark framework are explained in [elementary-two-marked-lifts](elementary-two-marked-lifts.md), under the C0001/C0007 interfaces cited there. In particular, the reviewed C0001 normal-subloop criterion is at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45); the C0007 inversion construction has the scoped review at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813) recorded in C0011, while C0007 aggregate review metadata remains unreviewed. Prime-power nonexistence for finite simple nonassociative Bol loops is the scoped C0011 input at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). The deductions here have the exact-source reviews recorded below.

## The solvable-radical branch when O₂(G)=1

Assume O₂(G)=1 and Rad(G)≠1. The nontrivial nilpotent group F(Rad(G)) is characteristic in Rad(G), hence normal in G. Its Sylow 2-subgroup is characteristic in it and lies in O₂(G), so F(Rad(G)) has odd order. For some odd p, O_p(G)≠1, and

    V=Ω₁(Z(O_p(G)))≠1                                      (1)

is characteristic elementary abelian and τ-stable. Conversely, any nonzero normal elementary abelian odd subgroup lies in Rad(G). Thus, under O₂(G)=1, a nontrivial solvable radical is equivalent to existence of a nonzero characteristic elementary odd layer of the form (1).

This does not say that Rad(G) itself has odd order: abstractly S₃ has O₂=1 and even solvable radical. No simple-folder realization of that control is claimed. The radical-free branch remains outside this reduction.

## Actual marked fibers over an odd layer

Let V◁G be any nonzero τ-stable elementary abelian p-group for an odd prime p, without assuming G or Q has odd order. Put L=G/V, J=HV/V, W=H∩V, d=dim_{F_p}V and w=dim_{F_p}W. For an actual selected quotient mark λ̄∈π(Λ)⊂E/V, choose an actual marked involutory lift λ∈Λ. Write T_λ for its conjugation action on V and

    N_λ=ker(1+T_λ),       r(λ̄)=dim N_λ.                   (2)

The action depends only on λ̄ because V is abelian. Since p is odd, (1−T_λ)V=N_λ. All involutory lifts of λ̄ form one affine N_λ-space, and V-conjugation is transitive on it. As Λ is E-conjugacy-invariant, this entire fiber is selected. This says nothing about quotient involutions outside π(Λ): those involutions are outside the selected-fiber assertion.

Fix a quotient coset aJ⊂L and a lift of a to G. The actual H-cosets above aJ form an affine space for V/W_a, where W_a=aWa⁻¹; it has p^{d−w} points. Let k=tλ∈K. Left multiplication by t sends the marked fiber vλ to the section fiber τ(v)k, so its direction in V is **τ(N_λ)**, of the same dimension r(λ̄). The section fiber injects into V/W_a, and fibers over different selected quotient marks are disjoint there, because K is a transversal to H. They cover the affine space because K meets every H-coset. Consequently

    Σ_{λ̄∈πΛ, tλ̄∈aJ} p^{r(λ̄)}=p^{d−w}.                 (3)

For a fixed fiber the injectivity condition is W_a∩τ(N_λ)=0; this states the required τ-transport explicitly. The ranks in (3) may vary with the selected quotient mark, because outside involutions need not form one conjugacy class when G is even. In the odd-group/full-inversion setting the ranks are constant and the reviewed uniform multitransversal count is recovered. Equation (3) itself assumes neither full inversion nor a quotient loop.

## A strict-defect alternative

Let r₀=dim V_−(τ) and put

    δ=dim C_V(τ)−dim W=d−w−r₀.                             (4)

The marked products t^v t, v∈V, run through V_−(τ), and H∩Λ²=1. Therefore W∩V_−(τ)=0 and δ≥0.

If δ=0, some **actual selected** marked involution λ∈Λ has

    dim V_−(λ)<dim V_−(τ).                                 (5)

Otherwise every selected rank is at least r₀. Since the right side of (3) is p^{r₀}, every quotient coset aJ contains exactly one selected quotient mark. Equivalently |KV/V|=[G:HV], the quotient-transversal equality in C0001's normal-subloop criterion.

Core-freeness and V≠1 imply V⊄H. If HV=G, then |Q|=[V:W] is a prime power, contrary to the cited C0011 theorem. Hence H<HV<G. The equality |KV/V|=[G:HV] gives a proper nontrivial normal subloop by C0001, contradicting simplicity. This proves (5).

There is a more precise consequence. When δ=0, the identity J-coset contains only the mark tV: its rank-r₀ fiber alone already fills all p^{r₀} H-cosets above J. Thus any rank-decreasing mark in (5) lies above a nonidentity J-coset. In any coset with minimum selected rank r_min<r₀, reduce (3) modulo p^{r_min+1} after dividing by p^{r_min}. The number of selected marks of rank r_min is divisible by p and is therefore at least p.

Equivalently, if τ has minimum negative-space rank among **actual** selected marked involutions, then δ>0 on every nonzero τ-stable elementary odd normal layer. The odd-order canonical case has that rank equality by outside-involution conjugacy, but the present statement does not assume it. In the even case δ=0 is not excluded; it forces a second marked class with strictly larger fixed space on V and the rank distribution above.

These are necessary structural restrictions, not a classification or construction. They do not determine the solvable radical, the selected quotient marks, stabilizer cochains, or nonsplit extensions. In particular the radical-free branch and an exhaustive description of even non-Bruck canonical envelopes remain open.


## Minimum-rank repointing on one odd layer

**Continuation with the scoped reviews below.** Let Q be any finite simple nonassociative left Bol loop in the canonical setting above, without a parity or properness assumption. For any actual marked involution λ₀∈Λ put

    K′=λ₀Λ⊂G,      τ′=conj_{λ₀}|G.                         (6)

Then (G,H,K′) is again a faithful generated Bol folder of a finite simple nonassociative loop, with canonical inverting automorphism τ′ and actual marked set Λ. In particular, G, H and Λ are preserved exactly. This does **not** assert that the new loop is isomorphic to Q or that non-Moufangness is preserved.

Indeed τ′²=1, 1∈K′, τ′ inverts K′, and λ₀K′=Λ. Since Λ is a conjugacy-invariant set of involutions, K′ is inverse-closed and sandwich-closed, and

    K′⁻¹K′=Λ².                                              (7)

The original H∩Λ²=1 and G-invariance of Λ² give collision-free sections for every conjugate of H; |K′|=|Λ|=[G:H] gives the transversals. Core_G(H)=1 is unchanged. The new section also generates all of G: t∈Λ and K=tΛ generate G, so ⟨Λ²⟩=G; conversely every λμ∈Λ² equals (λ₀λ)⁻¹(λ₀μ), hence ⟨K′⟩=⟨Λ²⟩=G.

For every normal subgroup R◁G, the element λ₀t belongs to G and K′=(λ₀t)K, so

    |K′R/R|=|KR/R|.                                         (8)

C0001's exact normal-subloop criterion uses these cardinalities and HR. Thus the two folders have the same normal-subgroup quotient tests, and simplicity is preserved. The original H is nontrivial because Q is nonassociative; a group loop has regular left multiplication group and trivial stabilizer, so the new simple loop is nonassociative as well. Its canonical inversion is τ′ by uniqueness, since τ′ inverts K′ and K′ generates G.

Now fix any nonzero τ-stable elementary abelian odd normal layer V. It is also τ′-stable: λ₀=t k₀ for some k₀∈K, so τ′ differs from τ by an inner automorphism. Choose λ₀ to minimize dim V_−(λ) over the finite actual marked set Λ. The marked set for the repointed folder is still exactly Λ. Applying the strict-defect alternative above to its canonical τ′ therefore yields

    dim C_V(τ′)−dim(H∩V)>0.                                 (9)

A zero defect would require an actual marked involution of smaller negative-space rank than λ₀, contradicting the choice. This normalizes the defect for the **chosen** odd layer; minima for several layers need not be attained by the same mark. It does not prove positivity for the original τ, identify the two loop isomorphism classes, preserve properness, or supply an odd layer in a radical-free envelope. The deduction has the exact-source reviews below.

## Independent mathematical review

reviewers contributor 1, contributor 2 and contributor 3 independently accepted the full manuscript at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/17e56bdfb16097218249f42f10e91adcb9f5a4b8), conditional on the stated scoped C0001, C0007 inversion and C0011 inputs; the C0007 aggregate remains unreviewed. All checked the characteristic odd-layer dichotomy, full fibers only over actual selected marks, the tau transport and rank-weighted partition, strict-defect alternative, identity-coset saturation and minimum-rank divisibility. They checked repointing preserves the faithful generated folder and every normal-subgroup quotient count, hence simplicity and nonassociativity, and yields positive defect on one chosen layer. No full outside-set, quotient-loop, isomorphism, properness or simultaneous-minimum claim is included. No computation or edits were made by these reviewers.
