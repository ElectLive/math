# Candidate J ⊕ U stabilizer and outer-class filter

This bounded continuation with scoped independent review below of [C0010](../../claims/0010.md) assumes the setup and cohomological reductions in [the J-branch manuscript](bruck-s5-j-branch.md): a faithful simple exponent-two Bruck envelope with elementary abelian radical V=J⊕U, J=F₂⁶/1 and U the 8-dimensional N-block projective module, quotient S₅, π(H)=F=N_{S₅}(P)≅F₂₀, and the nonsplit Nagy extension. We use the [block-module identifications](bruck-s5-module-blocks.md) and earlier necessary restrictions, not a new classification of all folders. In particular L=J^P≤W=H∩V, W has dimension 5, and the entire involution class above the ten transpositions is forced into K. Hence |Q|=1536. The J-branch constraints, forced class and H-normalization argument have their separate scoped review at the same source as the review below.

## F-submodules and core-freeness

As F-modules, J=L⊕S_J and U=S_U⊕S'_U, where S is the unique 4-dimensional projective simple F-module and End_F(S)=F₂. Thus W=L⊕S⊗ℓ for one of the seven nonzero lines ℓ=⟨(x,y,z)⟩≤F₂³, with coordinates on S_J, the S₅-socle N≤U and a chosen F-complement T₁≤U. The N block is U=N⊗F₂[ε]/(ε²); its S₅-endomorphism ring has unit group {1,1+ε}, acting on the three coordinates as (x,y,z)↦(x,y+z,z). The J and N blocks have no cross homomorphisms, and Aut_{S₅}(J)=1. These automorphisms of V lift to the chosen extension because they act identically on J and the U extension is split.

The seven lines are (1,0,0), (0,1,0), (0,0,1), (0,1,1), (1,1,0), (1,0,1), (1,1,1). The stated unit action has five orbits: the first, second and fifth are fixed, while (0,0,1) is paired with (0,1,1), and (1,0,1) with (1,1,1). The line (1,0,0) gives W=J, and (0,1,0) makes W contain the G-normal N; both violate core-freeness. The remaining three core-free orbit representatives are

1. W=L⊕graph(S_J→N), line (1,1,0);
2. W=L⊕T₁, line (0,0,1);
3. W=L⊕graph(S_J→T₁), line (1,0,1).

Their core-freeness follows from the block decomposition: an S₅-submodule inside W projects to an S₅-submodule of J contained in L⊕S_J or U contained in the indicated 4-space. In case 1, both coordinate intersections are respectively L and 0, and in case 3 the same holds. In case 2, W∩U=T₁ does not contain the unique nonzero minimal S₅-submodule N, and W∩J=L is not S₅-invariant. There can be no cross-block S₅-submodule linking J and U.

## Full outer involution class and H-transversality

Let t be a transposition. The mandatory outer class contains every involution over t. If W∩(1+t)V contains w≠0, then a selected involution k over t and its conjugate by a suitable v∈V are distinct members of K whose quotient is w∈H, contrary to transversality. The first representative fails: (1+t)J has dimension 2 inside S_J, and the graph map φ:S_J→N is an F-module isomorphism. In the swapped-copy model U=N⊕N, the image (1+t)U is the graph of t_N, while the socle N is the diagonal; their intersection is the diagonal copy of C_N(t), of dimension 3. Thus φ⁻¹(C_N(t)) has dimension 3 in S_J. Its intersection with the 2-dimensional (1+t)J is nonzero, and the graph of any nonzero vector in that intersection lies in W∩(1+t)V.

The two remaining representatives pass not only this necessary same-fiber test but **all** outer–outer products: Nagy, arXiv:0709.4544v1, §5, Proposition 5.1 uses the undeformed stabilizer H₀⋉T₁ and its full class c^G in an actual Bol folder; Theorem 5.2 uses H₀⋉graph(S_J→T₁), with the same c^G, in another actual folder. Both statements prove the needed transversality against all conjugates of the respective H. The first example is nonsimple; the second is simple. Here H₀=N_E(P), and H₀∩J=L. The earlier H¹(F,V/W)=0 argument identifies any H over F with fixed W, up to V-conjugacy, with W H₀, so this comparison covers all H for those W. The two source results use right Bol conventions; only their folder transversality is used here.

These facts classify W and settle the mandatory outer-class collision filter under the stated inputs. They do not classify the choice of K∩V, all resulting folders or isomorphism types; no claim of uniqueness is made. Source links: Nagy arXiv:0709.4544v1, §5 Proposition 5.1 and Theorem 5.2, https://arxiv.org/html/0709.4544v1; the repository module-block and cohomology proofs supply the other explicitly stated dependencies.

## Independent review

an independent check accepted this stabilizer and outer-class filter at exact source the recorded source revision, conditional on the J-branch normalization, forced class and listed module inputs, which that reviewer did not separately re-prove. The review checked all seven lines and five unit orbits, core-freeness, the graph-to-socle collision and the source-based full outer-class transversality. It directly inspected Nagy arXiv:0709.4544v1 §5 Proposition 5.1 and Theorem 5.2 at k=1, including the right-sided convention. This review does not classify D=K∩V or the resulting loops. The upstream J-branch argument has the separate review by an independent check at the same source, as recorded there.

