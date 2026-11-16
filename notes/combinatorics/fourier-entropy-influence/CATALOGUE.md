# Catalogue of results and their scopes

**Mira Cult · 16 November 2026**

This is the authoritative catalogue for the public FEI notes.
“Proved” below means a complete conventional argument with the stated
classical imports. It does not mean formal verification, journal acceptance,
or an exhaustive novelty certification. The exact model-review and
computation scopes are in [VERIFICATION.md](VERIFICATION.md).

All entropy is in bits. The [overview](README.md#the-question-and-conventions)
fixes the common Fourier and influence conventions. “Positive pairwise”
always means a full-support law with unary and two-coordinate potentials;
a general bag potential is not implicitly allowed.

## Entropy–influence theorems

| Result | Exact scope and conclusion | Canonical proof |
| --- | --- | --- |
| Positive Boolean forests | Full-support Boolean Fourier law factorizing over a forest: $`H\le4I`$. Zero-dimensional case handled separately. | [Positive forests, Theorem 5](positive-forests.md#6-the-unconditional-full-support-boolean-forest-fei-theorem) |
| Boolean forest deficit | For a nonconstant positive Boolean forest, $`H\le4I-2-2c`$, where $`c`$ counts nonconstant energy components after deleting zero interactions. | [Boolean minimum layer, Corollary 2](mixtures-and-obstructions.md#1-boolean-parity-strengthens-the-minimum-layer-bound) |
| Deterministic support extension | Remove fixed spectral bits and contract equality/complement edges. If the quotient is a positive forest, $`H\le4I`$. Three-state edges excluded. | [Deterministic contractions, Proposition 1](deterministic-contractions.md#1-all-deterministic-spectral-edges-can-be-contracted) |
| Common feedback vertex | Positive pairwise Boolean spectrum on $`G`$, with $`G-r`$ a forest: $`H\le4\sum_{i\ne r}\operatorname{Inf}_i`$. Arbitrarily many cycles may pass through $`r`$. | [Cycles, Corollary 2](cycles-and-cacti.md#1-main-statements) |
| Positive cacti | Positive pairwise Boolean spectrum on any cactus: $`H\le4I`$. When its minimal graph has a cycle, a constructed cutset $`K`$ gives $`H\le4I_{K^c}-2`$. No bound on cycle count. | [Cactus theorem and payment](cycles-and-cacti.md#6-paying-for-unboundedly-many-cactus-cycles) |
| Paid feedback sets | Positive pairwise Boolean spectrum of treewidth at most two; a feedback set $`K`$ of size $`k\ge1`$ leaves $`b`$ components containing genuine edges: $`H\le4I_{K^c}+2(k-1-b)`$. | [General component payment](cycles-and-cacti.md#6-paying-for-unboundedly-many-cactus-cycles) |
| Dyadic integer forests | Integer-valued $`h`$, positive forest spectrum, every nonzero Fourier magnitude an integer power of two: $`H_*\le4I-2c\lVert h\rVert_2^2`$. Deterministic quotients retain the bound without the stated refinement. | [Spectral conditioning, Theorem 1](spectral-conditioning.md#2-integer-forest-packets-with-unrestricted-amplitude-spread) |
| Dyadic spectral conditioning | Boolean power-of-two amplitudes and forest sections after $`k\ge1`$ spectral cuts: $`H\le4I_{K^c}+2k-2`$. Adaptive sections pay their actual mean denominator exponent. | [Fixed and adaptive conditioning](spectral-conditioning.md#3-a-spectral-cutset-theorem) |
| Arbitrary integer forests | Integer-valued $`h`$ with positive forest spectrum: $`H_{\rm raw}\le C_F I`$, $`C_F=6/\log_2(16/9)<8`$. No odd-prime or amplitude-spread hypothesis. | [Integer forests, Theorem 1](integer-forests.md#1-results-and-normalization) |
| Bounded spectral conditioning | Boolean spectrum partitioned into subcubes of codimension at most $`k\ge2`$, each positive-mass cell having a positive forest conditional law: $`H\le[32+1/\ln2+(2+8\ln2)(k-1)]I`$. Cellwise deterministic quotients allowed. | [Integer forests, Theorem 3 and proof](integer-forests.md#7-proof-of-the-general-conditioning-theorem) |
| Physical restriction trees | Arbitrary Boolean leaves: $`H-4I\le\mathbb E(H_L-4I_L)+\mathbb E D/2`$. Forest leaves give $`H\le4I+\mathbb E D/2-2P`$, with $`P`$ their nonconstant probability. | [Interpolation, Theorem 1](interpolation.md#1-the-interpolation-theorem) |
| Shared-data forest lists | First-hit lists with fresh uniform controls and nonconstant admissible forest payloads on the same data cube: $`H\le4I-1-2^{-k}`$ for $`k\ge1`$. | [Interpolation, Corollary 3](interpolation.md#1-the-interpolation-theorem) |
| Flat or bounded-spread integer packets | Boolean sum of integer-valued packets with disjoint Fourier supports: $`H\le4I`$ for flat packets, $`H\le4R^2I`$ if every packet's amplitude ratio is at most $`R`$. | [Integer flat packets, Theorems 1–3](integer-flat-packets.md) |

The positive-cactus and common-feedback-vertex conclusions also extend to
deterministic quotients when the quotient has the required positive graph.
The arbitrary-integer conditioning bound is weaker on positive pairwise
graphs with one feedback vertex, where the arithmetic theorem gives constant
four; it applies more generally to conditional forest sections without a
pairwise parent law.

## Structural estimates and exact obstructions

| Result | What is proved | What is not inferred |
| --- | --- | --- |
| [Forest odd-prime exclusion](forest-arithmetic.md#4-arithmetic-rigidity-of-boolean-spectral-forests) | Every nonzero Walsh magnitude of a Boolean forest spectrum is a power of two, including hard-zero laws. | No entropy bound for all hard-zero forests. |
| [Cycle-facet arithmetic](cycles-and-cacti.md#5-proof-of-arithmetic-rigidity) | A positive pairwise Boolean law on $`G`$ has power-of-two Walsh magnitudes when the suspension $`G^+`$ has no $`K_5`$ minor; in particular for pairwise treewidth at most two. | No FEI theorem for all treewidth two; no arbitrary triangle potentials. |
| [Boolean minimum layer](mixtures-and-obstructions.md#1-boolean-parity-strengthens-the-minimum-layer-bound) | For a noncharacter, $`\deg_{\mathbb F_2}\mathbf1[v_2(W)=m]\le m-1`$. The four-bit path core requires eight independent fair completion bits, and eight suffice. | No optimality claim for arbitrary correlated completions or for the six-bit core. |
| [Local integrality defect](integer-forests.md#32-a-paid-local-integrality-defect-on-arbitrary-graphs) | If $`K\lvert W_f\rvert`$ factors into positive integer unary/edge factors, then $`H(f)\le C_FI(f)+2\log_2K`$. | No universal influence bound on the least such $`K`$. |
| [Majority mixture obstruction](mixtures-and-obstructions.md#2-a-boolean-law-for-which-every-forest-mixture-is-a-point-mass-mixture) | Every mixture of Boolean forest laws giving the three-bit majority spectrum consists of point masses, with label cost two bits. | Does not refute a universal $`O(I)`$ mixture cost. |
| [Tree projection](mixtures-and-obstructions.md#4-tree-approximation-the-correct-identity-and-an-exact-nonrealizable-tree) | $`H(q_T)-H(p_f)=D_2(p_f\Vert q_T)`$ and equal expected weight, including zeros. Majority's tree projection is not Boolean-realizable. | Matching marginals do not permit the Boolean forest theorem to be applied to $`q_T`$. |
| [Selector closure obstruction](interpolation.md#7-what-failed-what-is-retained-and-what-remains-open) | A balanced four-bit gate gives dyadic Boolean examples with $`H/I>4`$; a 257-input character-payload selector has $`H-4I=1/8`$. | Does not refute FEI with a larger constant. |
| [Hard-zero energy obstruction](positive-forests.md#4-a-stronger-entropy-payment-really-fails-when-zeros-are-admitted) | Actual Boolean star spectra violate the proposed positive-tree energy extension to forbidden states. | The displayed examples satisfy FEI. |
| [Integer constant-four obstruction](integer-forests.md#8-failed-constant-four-and-verification-controls) | A ternary two-bit function has raw entropy/influence ratio $`3+(9/4)\log_2(16/9)>4`$. | Does not contradict the Boolean forest theorem. |
| [Cyclic proof barriers](cycles-and-cacti.md#7-scope-examples-and-next-obstruction) | A Boolean $`K_5`$-facet witness defeats unrestricted modular lifting; a path-square graph defeats the tested cutset component payment. | Neither is a Boolean counterexample to the stated cactus theorem or to FEI. |

## Boundaries of this catalogue

All these mathematical statements are unconditional under their displayed
hypotheses and the explicitly cited classical theorems. Computations
confirm examples and bounded test ranges; they are not substitutes for
the proofs. The universal conjecture and the narrower unresolved targets
are stated separately in [OPEN_PROBLEMS.md](OPEN_PROBLEMS.md).
