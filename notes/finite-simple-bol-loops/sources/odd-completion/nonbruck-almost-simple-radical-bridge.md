# Candidate almost-simple / non-Bruck radical bridge

Mira Cult
Scope: finite simple nonassociative left Bol Q, with G=LMlt(Q), H=G_1, n=|Q|, M=Mlt(Q), I=M_1, and τ the C0007 canonical inverting automorphism. Use C0001 for primitivity of M and C0008 for its almost-simple conclusion; the C0008 aggregate review metadata remains unreviewed. Write S=Soc(M), e=|Out(S)|, and use the classification-dependent Schreier theorem that Out(S) is solvable. This is a reduction with scoped independent review below, not a solved classification or new claim. It applies in particular to 0323.NONBRUCK_EVEN and does not require τ(H)=H.

## Factorization and τ-stable core

S is nontrivial normal in primitive M, hence transitive. Thus M=SI and n=[S:S∩I]. Set A=G∩S and J=A∩τ(A). Since S◁M, A◁G and G/A embeds in M/S≤Out(S). As τ is an automorphism, J◁G is τ-stable and J≤S. Indeed, [G:J]=[G:A][A:J], and the map A/J→G/τ(A) is injective, so [A:J] divides [G:τ(A)]=[G:A]. Consequently [G:J] divides [G:A]² and hence e². The J-orbits form a G-invariant block system: their number d=[G:JH] divides both n and [G:J], so d divides gcd(n,e²). Under Q≅S/(S∩I), this is the number of double cosets J\S/(S∩I). The analogous A-orbit number divides gcd(n,e).

If gcd(n,e)=1 then J is transitive, so S=J(S∩I). If Rad(G)≠1, J<S: indeed, if G≥S, then Rad(G)∩S is a solvable normal subgroup of simple S and is trivial, and [Rad(G),S]≤Rad(G)∩S=1. But C_M(S)=1 since M≤Aut(S) in its almost-simple embedding; hence Rad(G)=1, contradiction. Also S∩I<S because S is transitive on more than one point. Thus in the coprime, nontrivial-radical case S factors as a product of two proper subgroups, one J normal in G and τ-invariant.

Moreover Rad(G)∩J≠1 in that case. Otherwise Rad(G) injects into G/J, so its order divides e². Its orbits have a common size, dividing both n and |Rad(G)|; this common size is 1. Faithfulness then gives Rad(G)=1, contradiction. More generally, without coprimality the number of J-double cosets is bounded by gcd(n,e²), a concrete low-double-coset structural problem. If C0005's evenness is available and S=A_n in the natural degree-n action, G≤A_n=S, so J=G and S=G(S∩I) without a coprimality assumption. This can still be weak: for the order-24 loop the resulting ambient factorization A24=G A23 is a transitive-subgroup factorization, and alone does not classify folders.

The solvable residual G^(∞) is characteristic in G, hence τ-stable, and lies in A≤S: its image in the solvable group G/A is trivial. Do not assume A itself τ-stable; that is why J is used. For any prime p not dividing e, the normal p-subgroup O_p(G) lies in J, because its image in G/J is a p-subgroup of a group of order dividing e².

## A free commutator section of a radical

Let E◁G be τ-stable elementary abelian of order p^m; one canonical choice when P=O_p(G)≠1 is E=Ω₁(Z(P)), which is nonzero and characteristic in G. Put W=[E,τ]=im(τ−1)≤E. In the external semidirect product G̃=G⋊⟨t⟩, both t and t^x lie in Λ for x∈E, so each commutator t t^x lies in Λ²; these commutators constitute W. The C0007 folder identities give that Λ² is G-conjugacy invariant, closed under powers, and has trivial intersection with H. Therefore every nonidentity element of Λ² is semiregular on Q: a power fixing a point belongs to a conjugate of H and must equal 1. In particular W acts freely. It follows that |W| divides n and

rank_Fp(τ−1 on E) ≤ v_p(n).

If p∤e, the preceding paragraph places P and E inside the τ-stable subgroup J≤S. For odd p, W is the −1-eigenspace of τ on E; for p=2, W⊆C_E(τ). No nontriviality of W follows: τ may centralize E, so this alone gives no universal bound on |E| or the radical.

## Next bounded mathematical obligation

For a selected almost-simple socle/action (S,S∩I) with n even, classify or bound τ-stable subgroups J≤S with at most gcd(n,e²) orbits and a nonzero normal elementary-abelian p-subgroup E≤J for p∤e, while imposing the free τ-commutator condition above. In the coprime, nontrivial-radical case this becomes S=J(S∩I) with J and S∩I proper. Work first in one nonalternating almost-simple action with an accessible factorization/subgroup theorem; do not assume J is a loop multiplication group by itself. A successful group-theoretic classification would supply structural envelope data; failure of a sufficient screen is not a loop construction. The derived bounds have the scoped independent review below, conditional on the stated inputs.

## First source check: the PSL₂ natural action is already excluded

The natural projective-line action is not a fruitful unresolved test for the preceding radical reduction. Aleš Drápal, *Multiplication Groups of Loops and Projective Semilinear Transformations in Dimension Two*, Journal of Algebra **251** (2002), 256–278, [doi:10.1006/jabr.2001.9120](https://doi.org/10.1006/jabr.2001.9120), Theorem 5.1, printed p. 276, proves that if $`F`$ is finite with $`|F|\notin\{3,4\}`$ and $`\mathop{\mathrm{Mlt}}\nolimits(Q)\le\mathop{\mathrm{P\Gamma L}}\nolimits_2(F)`$ in its natural action on $`F\cup\{\infty\}`$, then $`Q`$ is a group (indeed cyclic). The theorem concerns the **full** multiplication group and all loops; it does not follow merely from the left multiplication group embedding. The theorem statement and its exceptions were checked in the published text; the underlying proof, including its stated finite computation at $`|F|=8`$, was not independently reverified here.

Consequently a finite simple nonassociative left Bol loop cannot have its full multiplication group in the natural $`\mathop{\mathrm{P\Gamma L}}\nolimits_2(q)`$ action for $`q\ge5`$. For $`q=2,3,4`$ the respective degrees are $`3,4,5`$ and the prime-power nonexistence part of [C0011](../../claims/0011.md) excludes the target. This application does not assume C0008, any radical hypothesis, or the non-Bruck condition. It is stronger than the proposed first radical test in this action and prevents presenting that test as an open structural advance. It does not exclude other permutation representations of $`\mathop{\mathrm{PSL}}\nolimits_2(q)`$, other almost-simple socles, or groups whose left multiplication group alone has this embedding. A useful next test should choose an action outside this source theorem, after checking the corresponding known exclusions.

## Stabilizer intersections for arbitrary parity

A further necessary condition does not use almost-simplicity or odd order. Under the canonical C0007 marked-section hypotheses, for every λ∈Λ one has H∩H^λ=C_H(λ). Indeed, if h∈H∩H^λ, then h^λ∈H and λ^hλ=h⁻¹h^λ lies in H. Both λ^h and λ belong to Λ, so H∩Λ²=1 forces h^λ=h. The reverse inclusion is immediate. In particular H∩τ(H)=C_H(τ). This does not force that intersection to be trivial or equal to H.

The odd-order parameterization's converse uses oddness essentially. At even order, an element h=λλ′∈H that is centralized by λ can be a nonidentity involution; the displayed intersection equalities alone do not exclude it. Thus this necessary condition does not replace the full H∩Λ² collision test for even folders. This deduction has the scoped independent review below; no stronger centralizer dichotomy is asserted.

## Independent review

## Publication and verification scope

This public source preserves the mathematical argument at the revision recorded in the source crosswalk. Its conclusions retain every stated hypothesis and dependency. Source-specific automated mathematical checks are not human referee acceptance, formal verification or a literature-priority audit. Computational checks, where cited, have only their stated finite scope.

The review checked the subgroup index and orbit bounds, coprime factorization, radical intersection, p-subgroup placement and free commutator section. C0008's aggregate review remains unreviewed, and the C0005 evenness input applies only within its own stated exact-factorization hypotheses. The reviewer did not inspect Drápal's primary theorem; that application retains the separate source-reading limits above. No computation, formal verification, general radical bound or classification was accepted.
