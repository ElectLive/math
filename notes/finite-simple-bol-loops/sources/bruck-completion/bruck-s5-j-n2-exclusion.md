# Candidate exclusion for the J ⊕ N² radical

**Mira Cult**

**Scoped independent review recorded below.** In a faithful Baer envelope of a finite simple exponent-two Bruck loop, suppose V=O₂(G) is elementary abelian, G/V≅S₅, and V≅J⊕N² as an F₂S₅-module, with J=F₂⁶/⟨1⟩ and N the four-dimensional even-weight five-point module. The following finite outer-class collision would exclude this case, conditional on the cited envelope, module and J-branch results. It concerns [C0010](../../claims/0010.md), introduces no claim ID, and does not classify other S₅ radicals or all loops of order 1536.

## Structural reduction

The [J-branch manuscript](bruck-s5-j-branch.md), reviewed at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/527aa14d458a5b7d43cef2be7faef4c90033b975) subject to its recorded dependencies, supplies π(H)=F=N_{S₅}(P)≅F₂₀, a nonsplit Nagy extension E of S₅ by J with split N² component, L=J^P≤W=H∩V, and V-conjugacy of H to WH₀, where H₀=N_E(P). It also gives dim W=1+4c and e=1+3a+4b−4c≥0 for a=2,b=0. The full fiber has only 32 orbit labels, so 2^e≤32 and e≤5. Combined with e=7−4c≥0, this forces c=1, dim W=5 and e=3.

Let S_J=[P,J] and let S_N be the unique irreducible four-dimensional nonfixed F-module. Since End_F(S_N)=F₂, the nonfixed part of W is S_N⊗ℓ for one nonzero line ℓ in a three-dimensional multiplicity space. A pure J line makes W=J; a line wholly in N² puts a nonzero S₅-submodule N in W. Either contradicts core-freeness. Every remaining line is the graph of an F-isomorphism S_J→N² with nonzero image in the two-copy multiplicity space. The [N-block decomposition](bruck-s5-module-blocks.md) gives Aut_{S₅}(N²)=GL₂(F₂), transitive on its three nonzero multiplicity vectors; these automorphisms lift to the split N² factor. Hence, up to an automorphism, take

    W = L ⊕ graph(ψ:S_J → first N),    H = W H₀.

The [J-branch manuscript](bruck-s5-j-branch.md) proves that the transposition-lift orbit labels comprise a two-element base orbit and five six-element orbits. Since the number of selected labels is 2^e=8, K must contain the base and exactly one of the five other orbits. In particular the base class alone is mandatory.

## Finite certificate

The [self-contained certificate](../code/verify_bruck_s5_j_n2_exclusion.py) builds E using the explicit permutations c,d in Nagy, *A class of finite simple Bol loops of exponent 2*, [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 3.2. It checks |E|=3840, builds the paired six- and five-point actions, verifies their composition and the five basis-vector conjugation relations, and forms G=N²⋊E. With P=cd it computes H₀=N_E(P), verifies |H₀|=40, constructs ψ and W and checks linearity and F-stability. It constructs H and verifies |H|=640 and subgroup closure against its displayed generators.

The script enumerates the full G-conjugacy classes of involutions over a fixed transposition, and verifies coverage of all 512 lifts in that fiber. It finds the six class sizes

    320, 960, 960, 960, 960, 960.

The 320-element class contains (c,0) and is the mandatory base class. The program verifies directly that even this class contains distinct k,kh with 1≠h∈H, contradicting H-transversality. It additionally checks each union of the base with one of the five 960-element classes and prints a collision witness for each. Thus no choice of the required outer part of K can work; the radical set D=K∩V need not be enumerated.

A deterministic base witness is printed as E-words in c,d together with eight-bit N² coordinates:

    k  = (dcddcddcd, 0)
    h  = (cddcdcddcddcdcdd, 5)
    kh = (cdcdcdcdddcddcddd, 5).

Words are multiplied in the order implemented by `compose`; the program checks the displayed multiplication and membership rather than relying on the printed strings. The source's original 40-point cycles are embedded, not fetched at run time.

## Reproduction and scope

Read the code, then run with assertions enabled:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_s5_j_n2_exclusion.py
```

Python 3.12.14 reproduced the six class sizes, the base collision, five further collision witnesses, and `all five outer choices violate transversality`. The executable verifies the represented finite-group model and the displayed collisions. Independent review must still check the J-branch and W-reduction interfaces, the correspondence between Nagy's source and the constructed module, exhaustive class coverage, and the code at an exact source revision. The calculation is not a classification of loops or an independent proof of those upstream results.

## Independent review

contributor 1 accepted this finite control at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/8b4d22c1c373a162117c0726b2faa2237fc51097), conditional on its cited envelope, module and fiber reductions. The reviewer read the code and independently ran it with Python 3.12.14. For J⊕N² the review checked the capacity-derived c=1, all F-line cases and GL₂ normalization, Nagy group and module pairing, coverage of the 512 involution lifts and the mandatory-base/WH₀ collision. For V₆⊕N² it checked all seven F-stable subspaces and their nonzero displacement intersections, including the extension-independent collision argument. The two controls do not replace or independently prove the broader projective-only reduction.
