# Candidate exclusion of V₆ ⊕ N²

**Mira Cult**

**Scoped independent review recorded below.** Let (G,H,K) be the faithful Baer envelope of a finite simple exponent-two Bruck loop, with elementary abelian V=O₂(G), G/V≅S₅, and V≅V₆⊕N² as S₅-modules in the conventions of [bruck-s5-v6-fiber-bounds.md](bruck-s5-v6-fiber-bounds.md). The following computation proposes to exclude this case for both the split and nonsplit extensions; it does not assume a quotient by N² defines a loop.

Let P=C₅ and F=N_{S₅}(P)≅F₂₀. The independently reviewed P-fixed feasibility and fiber bounds reviewed by contributor 1 at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/527aa14d458a5b7d43cef2be7faef4c90033b975) give W^P=V₆^P of dimension 2 and dim W=6, where W=H∩V. P averaging yields W=W^P⊕W₁. The latter is an F-submodule of the 12-dimensional P-nonfixed part, a direct sum of three copies of the projective simple 4-dimensional F-module S. End_F(S)=F₂, so W₁ is S tensored with one of the seven lines of F₂³.

The new certificate [verify_bruck_s5_v6_n2_exclusion.py](../code/verify_bruck_s5_v6_n2_exclusion.py) imports [verify_bruck_s5_principal_stabilizer_fixed.py](../code/verify_bruck_s5_principal_stabilizer_fixed.py), byte-identical to source [the source revision](https://github.com/Mira-Cult/math-wip/commit/ab4059e6a9b8d5876e2bffa993bb98e7dac69025) (SHA-256 `ddc95f03dc7be0e605452e16ff0639f3d84866a81104aa2d0306c6ba245dc985`). Its classifier and enumerator dependencies retain the exact digests recorded in the [P-fixed manuscript](bruck-s5-principal-stabilizer-fixed.md). It constructs the paired six-point and natural five-point permutation generators and checks that both generate the same faithful group of order 120. It computes the actual F-normalizer action and the 3-dimensional space Hom_F(S,V), and for each of its seven nonzero linear combinations checks irreducibility, dimension 6, F-stability, distinctness and the intersection with (1+t)V. The resulting seven intersection dimensions are 3,1,1,1,1,1,1. In the workspace, a Python 3.12 run took 0.70 seconds. This new certificate and its mathematical deductions remain unreviewed.

Reproduce from the repository root:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_s5_v6_n2_exclusion.py
```

In any extension, if an involution k∈K maps to t then conjugation by v∈V changes k by (1+t)v. A nonzero w∈W∩(1+t)V therefore gives two distinct conjugate members k,k^v of K whose quotient belongs to H, contradicting the transversal property. Since K projects onto the transposition class, the fiber is nonempty. All seven W have such a w, excluding both extension classes without inspecting the four possible fiber labels or the radical section. The conclusion is conditional on the cited reviewed inputs and independent verification of the finite module calculation.

No independent review of this manuscript or certificate has occurred; the prior reviews apply only to their pinned inputs. No permanent claim ID is allocated.

## Independent review

contributor 2 accepted this finite control at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/8b4d22c1c373a162117c0726b2faa2237fc51097), conditional on its cited envelope, module and fiber reductions. The reviewer read the code and independently ran it with Python 3.12.14. For J⊕N² the review checked the capacity-derived c=1, all F-line cases and GL₂ normalization, Nagy group and module pairing, coverage of the 512 involution lifts and the mandatory-base/WH₀ collision. For V₆⊕N² it checked all seven F-stable subspaces and their nonzero displacement intersections, including the extension-independent collision argument. The two controls do not replace or independently prove the broader projective-only reduction.
