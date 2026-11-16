# Odd-order Bol envelope data

Mira Cult
This manuscript-local extension-data scheme continues [C0010](../../claims/0010.md) without allocating a claim ID. It proposes structural construction and isomorphism data for finite simple **proper left Bol loops of odd order**. It does not assert closure of [0323.CLASSIFY](../../START_HERE.md), exact-factorization exhaustiveness, novelty, or an efficient classification of the surviving groups. Scoped independent reviews are recorded below. The construction uses finite odd solvable group extensions and a subgroup geometry test; it can be extremely large and gives no bound on group order or tower length. Its fitness as a solution of the problem's structural-data endpoint remains a review obligation.

The inputs are the canonical faithful folder and isomorphism correspondence of [C0001](../../claims/0001.md), the inverting automorphism for trivial left nucleus in [C0007](../../claims/0007.md), and the [odd-folder arguments](odd-folder-radicals.md). The latter record independent reviews of the full-inverted-set and centralizer-ratio results at the recorded source revision, the odd-order canonical-envelope source application at the recorded source revision, and the simplicity criterion at the recorded source revision. For oddness of the canonical envelope use Foguel–Kinyon–Phillips, `arXiv:math/0208231v2`, Proposition 6.1 and Theorem 4.14; the published-version numbering remains unchecked. Feit–Thompson, *Solvability of groups of odd order*, *Pacific J. Math.* 13 (1963), 775–1029, supplies solvability of finite odd-order groups. Those earlier reviews cover the inputs; the

## Equivariant elementary-extension recursion

Begin with the trivial group Q and its identity automorphism α. At each finite stage choose an odd prime p, a nonzero finite-dimensional F_p Q-module V with action ρ, and an involution T of V such that

T ρ(x) T⁻¹ = ρ(α(x))  (x∈Q).

Thus V is a module for the **formal** semidirect product Q⋊⟨s⟩, with s of order 2 acting by α, even if α=1. Require V to be irreducible under this whole formal semidirect product; it need not be irreducible as a Q-module and need not be central. Choose normalized maps c:Q×Q→V and u:Q→V with

c(1,x)=c(x,1)=0,  u(1)=0,
    c(x,y)+c(xy,z)=ρ(x)c(y,z)+c(x,yz),
    T c(x,y)+u(xy)=u(x)+ρ(α(x))u(y)+c(α(x),α(y)),
    T u(x)+u(α(x))=0.

All equations hold for all indicated elements of Q. Define

(v,x)(w,y)=(v+ρ(x)w+c(x,y),xy),
    τ(v,x)=(Tv+u(x),α(x)).

The first equation makes G=V×_c Q a group; the second makes τ a homomorphism, and the third makes τ²=1. The semilinearity equation and normalization ensure these formulas are compatible with V and the identity. Replace (Q,α) by (G,τ) and repeat, allowing any finite number of stages and odd primes. All maps and equations at each fixed finite stage are finite and explicitly enumerable. Stop at any stage and retain the resulting pair (G,τ); τ=1 is allowed at intermediate stages.

This recursion is exhaustive for pairs consisting of a finite odd-order group G and an involutory automorphism τ. Feit–Thompson makes G solvable. In the formal semidirect product G⋊⟨τ̂⟩, choose a minimal nontrivial normal subgroup contained in G; it is elementary abelian of odd prime order power and is irreducible under the quotient formal semidirect product. Repeat in the quotient and reverse the resulting τ-stable series. Choosing sections gives the displayed actions, cocycles and lift maps. This does **not** assume that an arbitrary central C_p series can be chosen τ-stable.

## Stabilizer geometry

For a resulting odd-order pair define

C=C_G(τ),  K={g∈G:τ(g)=g⁻¹},  Λ=τ̂K⊂G⋊⟨τ̂⟩.

All involutions in the nonidentity coset τ̂G form the single G-conjugacy class Λ, by conjugacy of complements to the odd-order normal subgroup G. Consequently |K|=[G:C] and K⁻¹K=Λ² is G-invariant. Enumerate subgroups H≤G and retain those satisfying

Core_G(H)=1,  |H|=|C|,
    H∩H^λ=C_H(λ)  for every λ∈Λ.                              (1)

The last condition is equivalent to H∩K⁻¹K={1}. Indeed D=H∩H^λ is λ-stable. If H∩K⁻¹K=1 and d∈D is λ-inverted, then λ and λd are involutions of τ̂G and hence both lie in Λ, so d∈Λ²∩H=1. For every x∈D the element x⁻¹x^λ is λ-inverted, so it is 1; thus D=C_H(λ). Conversely, if 1≠h∈H∩Λ², write h=λλ' with λ,λ'∈Λ. Then h^λ=h⁻¹∈H, so h∈H∩H^λ; (1) makes h λ-fixed, and odd order forces h=1, a contradiction.

The equality |H|=|C| makes |K|=[G:H]; the intersection condition and G-invariance of K⁻¹K give a transversal to H and all its conjugates. The full inverted set K contains 1, is inverse closed and is closed under x y x, so it defines a faithful left Bol folder. Require additionally

⟨K⟩=G,                                                     (2)
    |H∩N|<|C_N(τ)| for every 1≠N◁G, N≠G, τ(N)=N.              (3)

The reviewed τ-stable-normal criterion makes (3) equivalent to simplicity for a faithful generating odd-order folder. Finally require the [C0001 folder Moufang criterion](../foundations/C0001.md) to fail for at least one pair: for x,y∈K, the unique z∈K∩xyH must fail z∈Hxy. This finite test retains precisely the proper left Bol outputs; it can be evaluated from group data without presenting a loop table. Every subgroup, normal subgroup and displayed equality is finite and checkable.

## Exhaustiveness and isomorphism interface

Conditional on the cited inputs, every retained datum produces a finite simple proper left Bol loop of odd order. Conversely, for such a loop the cited FKP result gives odd canonical left multiplication group; C0001 gives a faithful generating folder, and simplicity and nonassociativity give trivial left nucleus, so C0007 supplies its unique inverting τ. The reviewed odd-folder results identify K as the full inverted set and establish (3). Feit–Thompson and the recursion supply the extension data, and (1) follows from its folder transversality. Thus the construction covers the stated branch without assuming an exact-factorization theorem.

Two retained data (G,τ,H) and (G',τ',H') define isomorphic loops exactly when a group isomorphism φ:G→G' satisfies

φ(H)=H',  φτ=τ'φ.

Such a map carries the full inverted set K to K' and hence the faithful folders to one another. Conversely a loop isomorphism induces an isomorphism of canonical left multiplication groups carrying H and K to H' and K'; uniqueness of inversion on the generating set gives φτ=τ'φ. The chosen chief towers, module bases, sections, cocycles and lift maps are **not** required to match under φ. This finite isomorphism test removes their duplication.

This is a candidate extension-and-stabilizer parameterization, not a proof of a new explicit exact-factorization witness or a certified solution of the parent classification. It does not cover even-order proper Bol loops, or by itself supply the group and nonassociative Moufang portions of the broader program. The recursion, geometry equivalence and isomorphism interface have the scoped reviews below. The following exact-factorization specialization supplies an algebraic control.

## Exact-factorization control

Let X be an odd-order group with an exact factorization X=Y₀Y₁ and X′Y₀=X′Y₁=X. In the canonical construction of [C0002](../../claims/0002.md), put G={(u,v)∈X²:uv∈X′}, H=G∩(Y₀×Y₁), and τ(u,v)=(v,u). Then K={(x,x⁻¹):x∈X}. Since X/X′ has odd order, C_G(τ)=diag(X′), and the surjective map Y₀×Y₁→X/X′ gives |H|=|X′|=|C_G(τ)|.

Exact factorization implies Y₀∩xY₁x⁻¹=1 for every x∈X: write x=ab with a∈Y₀,b∈Y₁, and conjugate the intersection by a⁻¹. If (b,c)∈H∩K⁻¹K, write it as (xy,x⁻¹y⁻¹); then c=x⁻¹b⁻¹x, so b∈Y₀∩xY₁x⁻¹=1 and c=1. Hence the new stabilizer-intersection criterion holds for every λ∈Λ by its proved equivalence above. This checks the geometry directly without a loop table or a subgroup census; it does not separately prove the other admissibility conditions for an arbitrary factorization.

For the p=3,q=13 construction in [C0003, Theorem 1.1](../foundations/C0003.md), X=F₂₇⋊(C₁₃⋊⟨φ⟩), φ(v)=v³. Its trace construction gives |Y₀|=27, |Y₁|=39 and exact factorization. The relations [φ,C₁₃]=C₁₃ and [C₁₃,F₂₇]=F₂₇ give X′=F₂₇⋊C₁₃ of order 351; both Yᵢ map onto X/X′. Thus |X|=1053, |G|=369603 and |H|=|C_G(τ)|=351, and the geometry test holds by the preceding argument. The full known-example claim retains C0002/C0003's own source and review scopes; this is a specialization of the geometry test with the scoped reviews below, not a new numerical verification or a separate certification of those complete claims.

## Independent review

## Publication and verification scope

This public source preserves the mathematical argument at the revision recorded in the source crosswalk. Its conclusions retain every stated hypothesis and dependency. Source-specific automated mathematical checks are not human referee acceptance, formal verification or a literature-priority audit. Computational checks, where cited, have only their stated finite scope.

The acceptances are conditional on C0001/C0007, the pinned odd-envelope and strict-defect inputs, Feit–Thompson and the specifically used C0002/C0003 data; they do not certify all those claims afresh. Both checked that the isomorphisms need not preserve any chosen chief tower and that the control uses group arithmetic rather than a new loop-table computation. Both emphasized that the procedure still enumerates all odd solvable extension data and many stabilizers and does not describe the surviving families, establish exact-factorization necessity or close the all-order classification. No numerical computation or formal verification was performed.
