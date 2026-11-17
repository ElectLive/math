# The residual sign action and affine sections

**Mira Cult**

**Independently reviewed theorem under pinned inputs.** This is a bounded continuation of [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Its endpoint is the sign-saturation theorem below, not a classification of top lifts or simple loops.

## Scope and pinned interfaces

Let (G,H,K) be a faithful generated canonical simple nonassociative Bol folder with G=N⋊Q, N=A5^Ξ, and Q a finite odd nilpotent group acting faithfully by pure factor permutations. Let τ be its canonical inversion, θ its induced automorphism of Q, Λ=τK, H0=H∩N, and I={q∈Q:θ(q)=q^−1}. The complete pairing theorem gives H→Q surjective, Q=⟨I⟩ and k=|I|=[Q:C_Q(θ)]. The full outside class Λ=τ^G is selected and H∩Λ²={1}.

The actual path theorem splits H0 into m independent size-two full A5 strips and an endpoint residual R, on n A4-type inputs and n C5/D10-type outputs. Here “type” refers to the actual coordinate stabilizer image of H, not just the projection of H0. The actual residual order is |R|=60^n/k. Write

    B=F5^n=C5^n,       W=R∩B,
    X=R/W ≤ C2^n × A4^n,
    Pφ={(φ(x),x):x∈V4^n} ◁ X,
    C=image of X in A4^n/V4^n ≤ F3^n.

Thus Pφ is the full Sylow-2 subgroup, with φ:V4^n→F2^n, and X/Pφ=C. Put dim C=n−d and dim W=n−e, so k=3^d5^e. No independence of the coordinates of W or C is assumed.

These interfaces are the [complete pairing theorem](radical-free-a5-nilpotent-orbit-pairing.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/daca2c9ba715982cedaaa41048d4866825a9a631), the [opposite-endpoint path theorem](radical-free-a5-paired-path-residual.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/4a1fa394b8ad0e2d92d8161aab14d2c9018db8bf), and the [actual residual graph](radical-free-a5-residual-dependency-graphs.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/2c9ce30fab64a9893118f4230d296d88f5867c00). The geometric path normalization in the [all-path parameterization](radical-free-a5-abelian-path-parameters.md#exhaustion-and-path-normalization), source [the source revision](https://github.com/Mira-Cult/math-wip/commit/b7d77177234743dffcf34a82ca2f281ed4d75305), and its θ-twisted extension at [the source revision](https://github.com/Mira-Cult/math-wip/commit/15fce885e821514fbe06d7501f9746c838063cf9), are used only through simultaneous τ/strip/endpoint framing, before their zero-graph affine conclusions. Their construction and zero-graph hypotheses are not imported for a nonzero graph. Canonical-folder and marked-transversal inputs retain the pins in those sources.

## Sign-saturation theorem

Let E=im φ act on B by its coordinate signs. Then E acts trivially on B/W. Equivalently,

    φ_j ≠ 0  implies  F5 e_j ≤ W.                         (1)

All residual 5-codimension therefore lies in the zero-output-row coordinates of φ. This conclusion does not assert φ=0. It applies to correlated W and arbitrary full-strip paths. The proof below does not need a further acyclicity assumption.

### Actual endpoint and marked frames

Choose local endpoint frames and standardize the original full strips. An actual H-element transports the C5 subgroup uniquely determined by a C5 or D10 output image, and transports the characteristic V4 in each A4 input image. In a uniform frame its endpoint coefficients lie in D10=C5⋊C2 and A4=V4⋊C3. Its top permutes the respective endpoint sets. Thus it acts affinely on

    V=(B/W) ⊕ (F3^n/C),              |V|=k,               (2)

using affine C5 translations and signs at the outputs, and the A4/V4 additive quotient at the inputs. Normality of H0 makes W and C stable under the relevant monomial maps. Full strips have disjoint support and act trivially on V.

We also need the availability of actual marked pure-top classes, which is invariant under all socle gauges used below. The local outer parity of τ is constant on each Q-orbit: τ conjugates each pure q into G, whose local coefficients are inner. The two τ-paired Q-orbits have the same parity. Outer coordinate gauges constant on Q-orbits remove these parities, and commute with pure Q. A subsequent inner N conjugation makes τ a pure factor involution. It preserves G as a subgroup, so the original pure-permutation Q remains in G, even if the conjugation moves the previously chosen complement to a different complement. The now pure τ normalizes the original Q and induces θ.

Every aτ with a∈I is an outside involution. It belongs to the full class Λ, by the odd-order square-root conjugacy argument on Q and the unique inner class on exchanged factor pairs. For q=ab∈I²,

    q=(aτ)(b^−1τ) ∈ Λ².                                (3)

Every N-conjugate of pure q also lies in Λ². Later whole-folder N conjugations preserve this assertion about the N-conjugacy class; they do not require τ to remain pure. The strip and endpoint frame changes from the pinned path geometry can therefore be made freely for the following argument, carrying H, K and τ together. No assumption τ(H)=H is used.

### Residual normal form in a convenient whole-folder gauge

In X, the normal elementary abelian Pφ has 3-group quotient C. A 3-complement exists by the coprime complement theorem. Each of its A4 coordinate projections lies in a Sylow-3 subgroup. Conjugations by V4 in the input coordinates align all these to the chosen standard C3 subgroups. They can be realized by one element of Pφ, whose input projection is all V4^n; its output C2 entries commute with the other endpoint factors. The aligned complement is therefore literally C≤C3^n. Since it normalizes Pφ, every nonzero φ-column has zero coordinate projection in C: a nontrivial C3 rotation has no nonzero invariant F2-linear functional V4→F2.

The preimage of X in the endpoint ambient group is B⋊X. Modulo W, the subgroup R/W is the graph of a 1-cocycle from X to B/W. Since |X| is prime to 5, averaging makes this cocycle a coboundary. Explicitly, for a cocycle f, put v=|X|^−1Σ_x f(x); the cocycle identity gives f(g)=v−g v. A B-conjugation therefore gives

    R=W⋊(Pφ⋊C),                                        (4)

with literal zero-5-translation representatives for Pφ and C. This is a whole-folder conjugation supported on endpoints; it does not change the diagonal full strips. It can change local τ twists, which is harmless by (3). In this gauge the image of H0 on V fixes zero and is exactly E acting on B/W, and trivially on the 3-part. Denote that affine image also by E.

The residual subgroup facts alone do not imply (1). Equal nonzero sign characters can support correlated subspaces, such as a diagonal line in two F5 coordinates with the same sign character. The following step uses the actual transversal.

### A zero-fixing top lift gives an actual collision

Suppose h∈H fixes 0∈V and has nonidentity top q∈I². Its input C3 vector belongs to C and its output 5-translation belongs to W. Multiply by actual elements of C and W from (4) to make both vectors zero. These multiplications preserve top q. At every endpoint the remaining local coefficient is in V4 on the input side and in the standard C2 on the output side.

Put r=ord(q), which is odd. Since h^r∈H0, its endpoint component is an actual p∈Pφ. The complete h^r may also have nontrivial full-strip components; it is not asserted to lie in Pφ globally. Because h commutes with h^r and preserves the endpoint/strip decomposition, h centralizes this endpoint element p. Replacing h by p^−1h makes its endpoint r-th power p^(1−r)=1. For a factor cycle of length ℓ|r, its local cycle product is a 2-element and its odd (r/ℓ)-th power is now one. Therefore every endpoint cycle product is identity.

Next clear every full-strip cycle product by multiplying by original full-strip factors of H0. These factors are independent of R. On a cycle of size-two strips, the return permutation cannot swap the two coordinates: q has odd order. In standardized diagonal strip coordinates the two local return products agree, and are inner A5 elements. One strip element cancels the return product on both sides. Different strip cycles have disjoint support. This leaves all endpoint products unchanged and makes every simple-factor cycle product identity.

The resulting h'∈H has top q≠1 and identity cycle product on every factor cycle. Solving successively along each cycle conjugates h' by N to pure q. Equation (3) then gives h'∈Λ², contradicting H∩Λ²={1}. We have proved:

    No H-element over I²−{1} fixes 0 in the action (2).     (5)

This argument concerns actual H-elements and the original marked class; no projected quotient-folder assertion is made.

### Counting the inverted top labels

For each i∈I choose an actual H-lift h_i. Its E-orbit at zero is independent of the choice. If E·(h_i0)=E·(h_j0), an actual e∈H0 satisfies e h_i0=h_j0. Thus h_j^−1 e h_i fixes zero and has top j^−1i∈I², since I is inverse closed. By (5), i=j. This gives an injection

    I → V/E.

Since |I|=|V|=k, every E-orbit on V is a singleton. Hence E acts trivially on B/W. If φ_j≠0, some sign s∈E has s_j=−1. Triviality on B/W implies (s−1)B⊆W; applying it to e_j gives −2e_j∈W and hence F5 e_j≤W. The converse implication is immediate coordinatewise. This proves (1).

## Returning to simultaneous τ and path frames

The intrinsic conclusion (1) survives every allowed coordinate gauge: W and the sign representation are transported together. Now use the geometric normalization from the pinned all-path sources to make τ pure, original strips diagonal and the endpoint C5/A4 frames standard simultaneously. In detail, the strip outer parities are constant on strip Q-orbits because actual H-lifts transport them with inner local coefficients. Orbit-constant outer gauges, equal across each τ pair, remove the outer twists recursively along the forest. A τ-fixed socle gauge removes the remaining inner strip twists along each coordinate path. A common diagonal A5 gauge along each complete path then standardizes its endpoint frame pair. None of these steps uses φ=0. Pure Q remains in the same subgroup G and permutes the standardized diagonal strips.

There is no need to apply another endpoint B-conjugation after this normalization. In the new standard frame E acts trivially on B/W. The 5-translation map of R/W to B/W is therefore a homomorphism from a 2,3-group to a 5-group, and is zero. Every quotient element already has an actual zero-5 lift in R. Aligning a 3-complement by Pφ now takes place inside the same R and does not conjugate the folder. Thus (4) holds in this simultaneous τ/strip/endpoint frame as well. This avoids assuming that an arbitrary endpoint translation gauge preserves pure τ.

This last conclusion is an interface for the subsequent study of actual top lifts. It does not yet classify their 2-defects, prove an ordinary Q-cocycle parameterization, establish all nonzero-graph collision conditions or give an isomorphism relation.

## Evidence, limitations and review

The proof is analytic. Its dependencies and exact source revisions are listed above; no new computation or literature claim is used. It eliminates nontrivial sign-character contributions to the 5-deficit in the stated actual-folder model, while leaving possible nonzero dependency graphs and the unrestricted classification open. Repository integrity checks test metadata and tooling only.

reviewers contributor 1, contributor 2, contributor 3, and contributor 4 independently accepted the complete manuscript at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/09b5565e7223b0b8a9b5dafbb646dbfa3f29a0de), conditional on its pinned inputs. They checked the actual endpoint affine action, complement/averaging normalization, pure-top marked classes through whole-folder gauges, endpoint-only odd-power correction and independent full-strip cycle clearing, the injection I→V/E, sign saturation, and simultaneous-frame return. They did not independently reprove every upstream input, run computations or conduct a fresh primary-source audit. These are model mathematical reviews, not human/formal certification or GitHub approval; they establish the scoped necessary theorem and frame interface, not existence or the unrestricted classification.
