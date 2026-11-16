# A positive tensor obstruction on A5 socle orbits

Mira Cult
This contributes to the [classification frontier](../../claims/0010.md). Let `G=A5^Ω⋊Q`, where Q acts faithfully on Ω by pure factor permutations, and let `(G,H,K,τ)` be a faithful generated canonical folder. Assume `H→Q` is onto, τ is an involutory canonical inverting automorphism, and `Λ=τK` is the actual conjugacy-invariant outside marked set. No p-group, numerical bound, transitivity of Q on all Ω, residual independence or hypothesis τ(H)=H is assumed.

Let U⊆Ω be a nonempty τ-stable union of Q-orbits. Suppose every full diagonal A5 strip of the original `H0=H∩A5^Ω` meets U in either zero or at least two coordinates, and every coordinate in U with proper H0 projection has projection containing an element of order five. Then no such folder exists. In particular, if Q is transitive on Ω, H0 cannot have full coordinate projections or proper 5-bearing coordinate projections. The faithful-folder and strict normal-quotient inputs are C0001; canonical inversion and actual marked-class invariance use C0007. A5 subgroup and full-strip facts use [the A5 path source](radical-free-a5-path-classification.md); the character and original-transversal interface use [the inversion source](radical-free-a5-code-inversion.md). The proper-projection version was independently reviewed in [the single-orbit source](radical-free-a5-single-nilpotent-orbit.md). The full-strip tensor extension is proved here.

## The character and its invariant tensors

Let ψ be the sign twist of the deleted permutation representation of S5 on its six Sylow-5 subgroups. Its restriction to A5 is the real irreducible degree-five representation. The S5 class data needed below are

| Cycle type | Class size | ψ(g) | ψ(g²) | ψ(g³) | χ_Sym³ψ(g) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 5 | 5 | 5 | 35 |
| 2 | 10 | 1 | 5 | 1 | 3 |
| 2² | 15 | 1 | 5 | 1 | 3 |
| 3 | 20 | −1 | −1 | 5 | 2 |
| 3·2 | 20 | 1 | −1 | 1 | 0 |
| 4 | 30 | −1 | 1 | −1 | −1 |
| 5 | 24 | 0 | 0 | 0 | 0 |

The ψ values follow by counting fixed Sylow-5 subgroups: their normalizer F20 contains the identity, four 5-cycles, five double transpositions and ten 4-cycles, with no other types. For any representation χ,

`χ_Sym³(g)=(χ(g)^3+3χ(g)χ(g²)+2χ(g³))/6`.

The weighted sum in the last column is `35+30+45+40−30=120`, so `(Sym³ψ)^S5` has dimension 1. The invariant symmetric square has dimension 1 as well, for example from the real orthogonal form. Pick nonzero invariant quadratic and cubic polynomials q,c on ψ. Since their polynomial ring has no zero divisors, `q^a c^b` is nonzero for all a,b≥0; every degree d≥2 is 2a+3b. Thus `(Sym^d ψ)^S5` contains a nonzero vector for every d≥2. Over characteristic zero, symmetric polynomials and symmetric tensors are identified using the invariant real form.

## The actual outside-class sum

Place ψ on every factor in U and the trivial representation elsewhere. This is an irreducible representation of N=A5^Ω and extends to the subgroup `S5^Ω⋊(Sym(U)×Sym(Ω−U))` preserving its labels. Compose with the formal G⋊<τ> action on N; this works even if τ is inner or trivial on N. Since U is τ-stable, every outside involution λ=τk has positive trace. A fixed factor in U contributes ψ of an S5 involution, namely 5,1 or1. A swapped pair in U contributes 5: the two local operators multiply to identity because λ²=1, and the trace of their product composed with the swap is the trace of that product. The complement contributes 1. Therefore `Tr ρ(λ)>0` for every λ∈Λ.

The set Λ is N-conjugacy invariant, and the N-module is irreducible. Its actual class sum acts as a scalar by Schur's lemma; the positive total trace makes that scalar nonzero. The transversal identity `(Σ_K k)(Σ_H h)=Σ_G g` (inverse closure of K handles the convention) then gives V^H=0, since the labeled N-module is nontrivial.

## Constructing the contradictory H-fixed tensor

The original full-coordinate part of H0 splits as a product of independent twisted diagonal A5 strips, disjoint from the solvable proper-coordinate residual. To justify this even when both kinds of coordinates occur, project H0 to the full-coordinate set and to its complement. The first image A is subdirect and hence a direct product of full A5 strips; the other image R lies in a product of proper A5 subgroups and is solvable. Goursat's lemma gives a common quotient describing any correlation between A and R. Every quotient of A is perfect, while every quotient of R is solvable; the common quotient is trivial. Thus H0=A×R in these coordinate images. This does not split or assume independence within R. H normalizes H0 and maps onto Q, so it permutes these full strips and their supports. A full singleton strip at i would force all singleton factors in the Q-orbit of i into H. Their product is a nontrivial G-normal subgroup contained in H, contradicting corefreeness. Hence every full strip has size at least two, even when Q has several orbits.

For a full strip S with d=|S∩U|≥2, straighten its coordinate twists using automorphisms of A5, all induced by S5. Choose the symmetric S5-invariant tensor in Sym^d ψ constructed above. If h∈H maps this strip to another, conjugation gives the same S5 automorphism on the common simple strip parameter after those twist identifications; its possible coordinate permutation is absorbed by symmetry. The coordinates of S outside U carry the trivial representation. Since H preserves U, it carries S∩U to the corresponding intersection in its image strip. Choosing the same tensor for every strip of each intersection size makes their product invariant under the actual H action, including permutations of strips. This is an S5, not merely A5, invariant, so outer strip twists and their parity cause no sign problem.

At every proper coordinate i in U, its 5-bearing H0 projection Li lies in the unique D10 normalizer of its characteristic C5. The D10-fixed subspace of ψ is one-dimensional, by the character average `(5+5·1+4·0)/10=1`; D10 fixes that line pointwise. The point stabilizer of i in H induces an inner A5 automorphism normalizing Li, hence an element of that D10. Transport a chosen vector on the line along H to every coordinate of its Q-orbit. Return maps fix the vector, so this is well-defined and its tensor product is H-invariant. Tensor it with the full-strip vectors. The proper-coordinate residual can be correlated arbitrarily: each of its coordinate actions fixes the corresponding vector separately. The resulting nonzero vector is fixed by the actual H, contradicting V^H=0.

A strip meeting U in exactly one coordinate is the genuine boundary of this argument: its nontrivial simple diagonal action on one ψ factor has no fixed vector. A full strip need not be wholly contained in U when the intersection has at least two coordinates. The pure factor-permutation hypothesis matters at proper coordinates. In an S5 outer extension an H-coordinate normalizer can be F20 rather than D10; ψ has no F20-fixed vector. The lemma therefore does not settle arbitrary multiple-orbit groups or outer extensions.

## Consequences for inversion-stable factor orbits

Let O be a Q-orbit preserved setwise by τ. Its H0 projections are H-conjugate. If they are proper and contain 5, apply the theorem with U=O to obtain a contradiction. If they are full, H permutes the full strips and is transitive on O, so d=|S∩O| is the same for every strip S meeting O. If d≥2 the theorem again applies. Therefore d=1; each such strip must continue to another Q-orbit, since a singleton full strip would contradict corefreeness as above. This is a restriction on the original H0 and does not construct a quotient folder.

If every Q-orbit is τ-stable, take U to be the union of the full-projection orbits. If nonempty, it contains the full support of each full strip and the theorem excludes it. Applying the proper-projection consequence on each remaining orbit shows that every H0 coordinate projection is 5-free, so H0 is a 5′-group. No nilpotence of Q is used in this consequence; H surjectivity remains a hypothesis.

## Evidence and remaining obligation

All character calculations are the finite class sums displayed above; no computational enumeration or certificate is used.  The next obligation is to control the surviving proper 5-free projections and strips that connect different orbits. The application to odd nilpotent tops is in [the stable-orbit obstruction](radical-free-a5-stable-orbits.md). The unrestricted classification remains open.
