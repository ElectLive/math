# A Heisenberg quotient and module control

**Mira Cult**

**Independently reviewed manuscript-local continuation of [0323:C0010](../../claims/0010.md).** This fixed control tests the quotient and module constraints for a possible monolithic odd Bol envelope with a nonabelian Hall subgroup. The quotient multitransversal conditions alone do not exclude it. Neither the computation nor the module-level avoidance below constructs a Bol folder, proves simplicity, or establishes existence of a monolithic simple loop. The reviewed quotient-layer input is [odd-elementary-layer-obstructions](odd-elementary-layer-obstructions.md), source [the source revision](https://github.com/Mira-Cult/math-wip/commit/d65384d34ad0cb77635020a3bbe93dc1b3eb3b6b), with its cited [the source revision](https://github.com/Mira-Cult/math-wip/commit/958dd0d834610aa5b6a7a73b323eb62145aeec99) and odd-folder inputs.

## Quotient control

Let T be the three-dimensional Heisenberg group over F₇, of order 7³, in BCH coordinates

    (u,v,z)(u′,v′,z′)=(u+u′,v+v′,z+z′+4(uv′−vu′)),

where all three coordinates are in F₇. Let A=⟨a⟩≅C₃ act as (u,v,z)↦(2u,4v,z), and set L=T⋊A. Define θ by

    θ(u,v,z,a^i)=(v,u,−z,a^{−i}).

Let C={(u,0,0):u∈F₇} and J=C⋊A. Then |L|=1029, |J|=21, and |C_T(θ)|=7. The subgroups C and θ(C) intersect trivially but generate T, so their product is not a subgroup. This is the nonabelian obstruction to copying the abelian-Hall argument.

The [standalone verifier](../code/verify_odd_heisenberg_control.py) enumerates the 1029 elements, checks that the full θ-inverted set has 147 elements, and checks all conjugates of J. There are exactly seven conjugates, each with 49 left cosets; each such coset contains exactly three θ-inverted elements. Thus the fixed quotient satisfies the reviewed multiplicity-three necessary condition for every conjugate of J. The image of a loop section in a quotient is not asserted to be a transversal or to define a quotient loop.

## An irreducible compatible module

Let E=F₃[ζ]/(1+ζ+⋯+ζ⁶)≅F_{3⁶}. The polynomial is irreducible because ord₇(3)=6. On V=E⁷ with coordinates e_j, j∈F₇, define

    x e_j=ζ^j e_j,   y e_j=e_{j+1},   z e_j=ζ e_j,
    a e_j=e_{4j},
    σ((v_j))_i = Σ_j ζ^{ij} v_j^{27}.

With the BCH/ordered-coordinate convention in the verifier, these give the displayed L action and satisfy σ²=1 and σρ(l)σ⁻¹=ρ(θl). The verifier checks these identities on an F₃-basis and the group generators, and obtains dim_F₃ C_V(σ)=21.

The representation is faithful: the monomial permutation j↦4^i j+v is the identity only when i=v=0, after which the diagonal powers force u=z=0. It is irreducible over F₃: the central element z gives any invariant F₃-subspace an E-vector-space structure; over E, x has seven distinct eigenlines and y permutes them transitively. These observations are a direct proof, not an inference from the computed dimension.

For any two-dimensional F₃-subspace U≤E, consider

    W=Ue₀ ⊕ E e₁ ⊕ E e₂ ⊕ E e₄.                              (1)

It is J-invariant and has dimension 20, so dim C_V(σ)−dim W=1. The verifier checks the explicit choice

    U=⟨ζ⁵, ζ³+ζ⁴⟩_{F₃}

and finds W meets trivially every marked negative eigenspace obtained by the 343 elements of T. The remaining A-conjugations do not add a test: A preserves W, and every element of L has the form ta with t∈T and a∈A, so ρ(ta)W=ρ(t)W. This is a necessary module-level avoidance control only. It does not test nonidentity projected H-fibers, stabilizer cocycles, all-conjugate folder transversality, or normal-subloop simplicity.

## Corrected affine-fiber boundary

For left lifts in the affine-fiber test, the relevant minus operator is ρ(k)σ and the stabilizer subspace must be transported as tW for the quotient coset tJ. An earlier exploratory rank-42 claim used the wrong operator order and is withdrawn. In particular, no exclusion of the coordinate-support families is claimed here. The mixed rational-isotypic Grassmannian and the affine offsets/stabilizer cocycles remain unresolved; satisfying a direction condition alone would not construct a folder.

## Reproduction and limits

Run

    python3 code/verify_odd_heisenberg_control.py

from this problem workspace with Python 3.11 or later and assertions enabled. The script uses only the standard library and has no temporary-path imports or output files. It checks the quotient multiplicities, the fixed module identities and dimension, J-invariance of (1), and rank-20 avoidance for the displayed U over all 343 T elements. These finite checks support this control only. The exact-source reviews below cover the present manuscript and verifier; no computation is claimed to prove the monolithic branch or C0010.

## Independent review

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/49b2a2c248d1b492fa0b35d5784999e7f8854000), reviewers contributor 1 and contributor 2 independently accepted the complete fixed control and standalone code, and independently read and reran the pinned certificate with Python 3.12.14. They checked the BCH/ordered-coordinate conventions, faithful irreducibility, Fourier–Frobenius involution, all-conjugate quotient multiplicities and marked-space avoidance, including the A-invariance reduction. The notation in one code comment was clarified after review to display the intended direct sum; no executable code changed. The reviews do not establish a folder, affine offsets, simplicity or monolithic-loop existence, and make no formal-verification claim.
