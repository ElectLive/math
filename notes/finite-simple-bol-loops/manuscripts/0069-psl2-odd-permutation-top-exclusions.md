# 0069. Projective-tensor exclusions for odd PSL₂ permutation tops

Mira Cult

## Results obtained

The projective-character tensor argument below excludes the stated pure PSL₂(q) factor-permutation canonical groups for q ≡ 1 (mod 4), outside q = 5, 9, 29, under its exact hypotheses. It extends the power-group exclusions to permutation envelopes; it is not a claim about arbitrary outer actions or every canonical group with PSL₂ composition factors.

This contributes to the [classification frontier](../sources/factor-permutation/../../claims/0010.md). Let q≥5 be an odd prime power with q≡1 mod4 and q∉{5,9,29}, and put T=PSL2(q). Let Ω be nonempty, Q a finite odd group acting faithfully by pure permutations of the T factors, and G=T^Ω⋊Q. There is no faithful generated canonical folder (G,H,K,τ) of a finite simple nonassociative left Bol loop with H→Q onto. Consequently no such folder exists for any finite odd nilpotent Q. The result allows arbitrary unequal and nonregular factor orbits and all canonical inverting automorphisms. It does not cover arbitrary outer lifts, mixed socles, or a different group merely containing these composition factors.

The folder/transversal and canonical inversion inputs are C0001 and C0007. The exact projective representation, automorphism, involution-trace and proper-subgroup inputs are in [the odd one-mod-four field proof](../sources/factor-permutation/../../update-2026-11-16/manuscripts/radical-free-fixed-factors.md). In particular that proof uses Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Annals 172 (2010), Appendix Theorem A.1 and Lemmas A.2–A.3, printed pp.1354–1355, at the source locator recorded there. The original classification and its automorphism interface are not reproved here. Unlike that source's direct-power conclusion, the argument below treats the entire factor-permutation extension and the actual H-action.

Write N=T^Ω and H0=H∩N. For nilpotent Q, H→Q follows from the original normal-subloop criterion: if its image were proper, it would lie in a proper normal maximal subgroup of Q. The preimage in G is proper normal, contains H, and is strictly larger than H by corefreeness. The actual K-image fills the quotient because G=KH, giving the forbidden normal-subloop equality. For general odd Q, surjectivity remains an explicit hypothesis.

## An actual H-fixed tensor

Let V be the deleted permutation representation on P1(F_q), with character χ and dimension q. It is irreducible for T by double transitivity, real and self-dual, and has its natural extension to Aut(T)=PΓL2(q). The cited subgroup proof says every proper J<T is intransitive on these q+1 points, hence fixes a nonzero vector of V. The exceptional list is essential: the Borel and torus cases are intransitive, the exceptional subgroup orders leave 5,9,29, and subfield subgroup orders cannot be divisible by q+1, as proved in the pinned source.

At a proper H0 coordinate projection L_i<T, let J_i be the image in T of the actual H-stabilizer of i. Then L_i◁J_i. If L_i≠1, simplicity makes J_i proper. If L_i=1, J_i is an image of an odd subgroup of Q, so cannot be the even group T. Thus every proper coordinate admits an actual J_i-fixed V-vector.

The subdirect image on the full-coordinate projections is a product of disjoint twisted diagonal T strips. It splits from the correlated proper-coordinate residual by Goursat. Indeed a subgroup of a product of proper T-subgroups has no composition factor isomorphic to T: a coordinate-kernel filtration has sections that are subgroups of individual proper T-subgroups, whose orders are smaller than |T|. Every nontrivial quotient of a direct product of T strips has a T composition factor. Their common Goursat quotient is therefore trivial. A singleton strip would put its whole Q-orbit of individual simple factors in H, contradicting corefreeness. All strips have size at least two.

On the sum-zero permutation space V, the symmetric quadratic and cubic power sums are nonzero Aut(T)-invariant polynomials. Nonzero products in the polynomial ring give symmetric invariants in every degree d≥2. By the invariant inner product they give invariant tensors in Sym^d(V). On each strip straighten its twists by Aut(T), and choose the corresponding tensor. Its symmetry and Aut(T)-invariance make it fixed by the actual strip normalizer, including permutations of coordinates and of strips after coherent transport. At proper coordinates transport the chosen J_i-fixed vector around its H-orbit; point-stabilizer invariance makes the transport well-defined. The product is a nonzero actual H-fixed vector of

    W = tensor over i∈Ω of V_i.

This retains arbitrary correlations in the proper residual. W is irreducible for N and extends by the natural projective-line wreath action to G and the formal outside action of τ.

## Constant trace sign across the actual marked set

Let π be τ's factor permutation and θ its induced automorphism of Q. Any outside top involution qθ satisfies θ(q)=q^−1; if t is its odd-order square root, then tθt^−1=qθ. Thus these top involutions are Q-conjugate. The actual selected set Λ=τK consequently has the same number of fixed coordinates in each Q-orbit for all its elements. Fixed coordinates can occur only in π-stable Q-orbits; π-paired Q-orbits contribute swapped pairs only.

It is also necessary to control local outer labels, since the group need not normalize the chosen pure top complement under τ. Identify the simple factors with T, and write τ's coordinate map from i to π(i) as α_i∈Aut(T). For a pure factor permutation u∈Q, the element τuτ^−1 belongs to G and has local outer label [α_{ui}][α_i]^−1 from π(i) to π(ui). All local components of elements of G are inner, so [α_{ui}]=[α_i]. The outer label is therefore constant along each Q-orbit. For λ=τ(nu), a fixed coordinate i has local outer label [α_{ui}], unchanged by n∈N and equal to this orbit's constant label.

The pinned projective calculation gives the trace at each fixed coordinate. In the inner coset it is q at identity or 1 at an inner involution, since q≡1 mod4. In the no-field diagonal-outer coset it is −1. If the field part is nontrivial, necessarily q=q0², the local semilinear involution fixes a conjugate of P1(F_q0) and its trace is q0>0. The source proves this by norm rescaling and a fixed-basis descent, without assuming one T-conjugacy class. Thus every fixed-coordinate trace is nonzero, with sign depending only on its local outer coset. Every swapped coordinate pair contributes q>0, because the two local maps of the involution compose to identity.

The number of fixed factors in each Q-orbit and its outer label are independent of the selected λ. Hence Tr_W(λ) is nonzero of one constant sign throughout the actual Λ. Its G-conjugacy-invariant class sum acts as a scalar on W, since W is already N-irreducible, and the total trace makes that scalar nonzero. The original transversal identity, multiplied by the τ-operator, says that this class sum annihilates W^H because W has nontrivial N-action. This contradicts the H-fixed tensor and proves the theorem.

## Evidence and scope

This is an analytic extension of the pinned projective-subgroup and character inputs; no computational census or formal verification is claimed. The result excludes an infinite collection of entire pure factor-permutation envelopes, not merely direct powers or bounded orders. The exceptions 5,9,29, other field congruences, arbitrary outer lifts, mixed socles, radicals and general tops without H-surjectivity remain outside its conclusion. C0010 and the unrestricted classification remain open.

## Source and verification scope

This exposition preserves the mathematical arguments of the linked research sources. Separate automated mathematical checks were recorded for specified source revisions, conditional on their upstream inputs. They are not human referee acceptance, a fresh literature-priority audit or formal verification. The publication crosswalk records the source-to-public mapping.
