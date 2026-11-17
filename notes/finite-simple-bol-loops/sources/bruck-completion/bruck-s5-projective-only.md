# Candidate projective-only N-block reduction

**Mira Cult**

**Scoped independent mathematical and computational review recorded below.** Let (G,H,K) be the faithful Baer envelope of a finite simple exponent-two Bruck loop, with V=O₂(G) elementary abelian, G/V≅S₅, and exactly one composition factor M in the principal {1,M}-block. Under the previously reviewed envelope and module inputs cited below, the argument establishes, under those inputs, that

    V ≅ X ⊕ U^b,    X∈{J,V₆},    b≥0,

where J=F₂⁶/⟨1⟩, V₆ is its indicated nonsplit six-dimensional extension, N is the four-dimensional natural even-weight module and U=N⊗F₂C₂. In particular, no direct N-summand survives. This is a bounded continuation of [C0010](../../claims/0010.md), with no new claim ID. It does not classify the remaining U^b branches or make a claim for arbitrarily many M factors.

The [principal stabilizer reduction](bruck-s5-principal-stabilizer-fixed.md#independent-four-model-review-and-remaining-envelope-candidates), at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/ab4059e6a9b8d5876e2bffa993bb98e7dac69025) and its stated dependencies, leaves X=J or V₆. The [N-block decomposition](bruck-s5-module-blocks.md), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499), gives the complementary block as N^a⊕U^b. The [J-branch](bruck-s5-j-branch.md), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/527aa14d458a5b7d43cef2be7faef4c90033b975), and [V₆ fiber bounds](bruck-s5-v6-fiber-bounds.md), reviewed at that same revision, provide the branch-specific W and transposition-fiber hypotheses below. The new argument has its separate review below.

## Shared fixed/image witness

Let P≅C₅, F=N_{S₅}(P)≅F₂₀, t a transposition and W=H∩V. On the six- and five-point actions, choose the generators

    t₆=(1 2)(3 4)(5 6), d₆=(2 3 4 5),
    t₅=(1 2),             d₅=(2 3 4 5), P=⟨td⟩.

Use the first five coordinates for J=F₂⁶/⟨1⟩ and the basis e₁+e₂,…,e₁+e₅ for N. In the V₆ model extend the J t-generator by the column 32 xor 21, using bit masks. In both X models, S=[P,X] is the same four-dimensional F-module. Let φ:S→N be its unique nonzero F-isomorphism. There are v=17∈S and l=4∈X^P with φ(v)=1. Their additional properties are

- for X=J, t fixes v+l=21;
- for X=V₆, (1+t)32=v+l=21;
- in N, (1+t)2=1, so 1 is fixed by t and lies in (1+t)N.

The [shared small certificate](../code/verify_bruck_s5_projective_only.py) verifies the paired action, F-normalizer, explicit intertwiner and identities in both models. It imports the previously reviewed principal-stabilizer verifier; its source and dependency must be read before execution. The specific finite identities have the independent review below. In the swapped-copy description of U=N⊕N, the U-socle vector (1,1) lies in (1+t)U, since it is (1+t)(1,0).

## Multiplicity-space obstruction

The P-idempotent splits W=W^P⊕[P,W], and the branch results give W^P=X^P. As F-modules all nonfixed constituents are the unique projective irreducible four-dimensional S, with End_F(S)=F₂. Hence

    [P,W] = S⊗B,    B≤F₂ ⊕ F₂^a ⊕ F₂^b ⊕ F₂^b,

where the coordinates (x,y,z,q) represent respectively the X constituent, the N summands, the U-socles and chosen F-complements to those socles. Put c=dim B.

Suppose B contains a nonzero (x,y,z,0). If x=0, the S₅-submodule of the N-block socle determined by the nonzero vector (y,z) is a copy of N inside W, contradicting core-freeness of H. If x=1, the vector

    w = (v+l; y₁φ(v),…,y_aφ(v); z₁(φ(v),φ(v)),…,z_b(φ(v),φ(v)))

lies in W and is nonzero. Its N and U components are in (1+t)(N^a⊕U^b). In the V₆ branch its X component is also in (1+t)X. Hence for any k∈K over t, conjugating k by a suitable element of V gives a distinct k'∈K with k⁻¹k'=w∈H, contradicting transversality. This uses no splitting of the extension.

In the J branch, w's J component is t-fixed but need not lie in (1+t)J. The reviewed J-branch result gives the mandatory base class: its fiber above t contains the **entire** J involution fiber together with the zero-label V-orbit on the N-block. Multiplication by w preserves that fiber: its J component is t-fixed and its N/U components are in the image of 1+t. Thus both k and wk belong to the base class and differ by w∈H, again contradicting transversality. This is the point at which the J argument uses more than a same-V-orbit collision.

Therefore B has trivial intersection with the kernel of projection to the U-complement coordinate, and c≤b.

## Fiber capacity

For X=V₆, the reviewed [fiber bounds](bruck-s5-v6-fiber-bounds.md#two-independent-capacity-inequalities) give a+4b≤4c. For X=J, the reviewed [J-branch count](bruck-s5-j-branch.md#nagy-extension-affine-centralizer-action) gives q=2^(1+3a+4b−4c) selected V-orbit labels. There are exactly 2·4^a=2^(1+2a) labels in total, so q≤2^(1+2a), again yielding a+4b≤4c. Combining either inequality with c≤b gives a=0 and c=b.

The two explicit a=2, b=0 obstruction computations in [the J⊕N² manuscript](bruck-s5-j-n2-exclusion.md) and [the V₆⊕N² manuscript](bruck-s5-v6-n2-exclusion.md) remain finite controls with their own review status, not prerequisites for this uniform deduction. The argument above leaves all V=X⊕U^b cases and their possible sections, simplicity and isomorphism classes to separate work.

## Independent review

contributor 1 accepted this uniform reduction at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/8b4d22c1c373a162117c0726b2faa2237fc51097), conditional on the cited prior J/V₆, cohomology, module and fiber inputs. The review read the dependency chain and independently ran the shared certificate with Python 3.12.14, reproducing the paired S₅ action, full-rank F-intertwiner and all fixed/image identities. It checked the zero-top submodule/core-freeness alternative, the extension-independent V₆ collision, the separate mandatory-base collision in J, and both capacity bounds giving a=0 and c=b. This is precisely the exactly-one-M elementary-abelian S₅-envelope reduction; no existence, multiple-M or non-elementary-radical result follows.
