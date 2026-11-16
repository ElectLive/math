# Mathematical targets beyond the proved classes

**Mira Cult · 16 November 2026**

[Overview](README.md) · [Proved results](CATALOGUE.md)

The final target is a dimension-independent constant $`C`$ for
$`H(f)\le CI(f)`$ for every Boolean function, including constants and
unbounded degree. The problems below isolate unpaid costs in the present
proofs. Solving one must not be described as solving general FEI unless
the additional deduction is supplied.

## Positive pairwise spectra of treewidth two

The dimension-independent FEI target for positive width-two laws is now
[proved with constant below fourteen](bounded-treewidth.md), even for
genuine triangle potentials. Every fixed width is covered as well.

**Sharper target.** Prove $`H(f)\le4I(f)`$ for every Boolean $`f`$ whose
positive Fourier law factors into unary and pairwise potentials on a graph
of treewidth at most two, or give a Boolean counterexample to this constant.
This target is strictly stronger than the dimension-independent theorem.

Pairwise arithmetic already forces power-of-two Walsh magnitudes. Cacti
and common-feedback-vertex graphs have constant four. The older cutset
bound leaves $`2(k-1-b)`$, and the eleven-vertex path-square graph defeats
the proposed component-count payment. An unrestricted zero-loss two-bit
boundary transfer also fails. Neither is a Boolean counterexample to the
sharper target. A proof must retain a stronger energy invariant or exploit
more Boolean structure than the general integer theorem.

## A uniform payment beyond bounded width

**Target.** Replace the width-dependent entropy payment by a universal
constant for arbitrary positive Boolean Fourier laws, or construct an
explicit diverging family in this class. The proved constant is
$`O(4^{w+1}/(w+1)+\log(w+2))`$ at width $`w`$.

Positive integer factors of any fixed arity already give a constant even when their
factor graph has unbounded treewidth. The missing step is a bounded-load
integer representation, or a different paid entropy inequality, for
arbitrary Boolean Walsh tensors. Grouping a large bag into one factor
retains its arity cost; it does not give a dimension-independent theorem.

## Genuine three-state forest edges

**Target.** Prove a dimension-independent FEI bound for every Boolean
Fourier distribution with a unary/edge forest factorization, allowing
arbitrary nonnegative factors, or produce an unbounded-ratio family.

Fixed bits and deterministic equality/complement edges reduce to a positive
quotient and are already covered. Odd-prime exclusion also holds for the
remaining zero cases. What fails is the positive-tree energy inequality:
the explicit Boolean star in [positive forests, Section 4](positive-forests.md#4-a-stronger-entropy-payment-really-fails-when-zeros-are-admitted)
violates it, while still satisfying $`H=2I`$. A successful proof must
charge forbidden-state selection in some additional way. Taking a limit
of arbitrary positive probability models does not suffice, because those
models need not be Boolean-realizable.

The [forbidden-pair theorem](zero-edges.md) now handles a missing pair whose
nonzero sections reduce to positive forests, preserving constant four.
This includes nonproduct forest pieces. The remaining arbitrary-zero
problem must account for two exact failures: a six-bit Boolean forest
produces half-integer sections on its second forbidden-edge cut, and an
integer hard-zero star defeats every positive-proof invariant
$`D_2(p\Vert U)\le\eta L+CJ`$ with $`\eta<1`$. The latter still satisfies
raw FEI. A repair should use Boolean normalization before cutting, track a
stronger norm/lattice invariant, or pay the actual later denominators.


## Pay the local integrality defect

For a positive pairwise integer amplitude array $`A=|W_f|`$, define
$`\Gamma(A)`$ as the least $`\log_2K`$ over positive integers $`K`$ for
which $`KA`$ is a product of positive integer unary and pairwise factors,
including an integer constant factor. Rational local factorization shows
that some finite $`K`$ exists. For forests, $`K=1`$ is possible. The
[integer-factor theorem](integer-forests.md#32-a-paid-local-integrality-defect-on-arbitrary-graphs)
proves

```math
H(f)\le C_FI(f)+2\Gamma(|W_f|),
\qquad C_F=6/\log_2(16/9).
```

**Target.** Prove $`\Gamma(|W_f|)\le CI(f)`$ for all positive pairwise
Boolean Fourier laws, or find an explicit Boolean family disproving this
particular sufficient estimate. A weaker defect with the same entropy
inequality would also be useful.

This would give FEI for all positive pairwise spectra, a larger class than
the current bounded-width and bounded-conditioning results. It would not by itself
cover arbitrary Boolean spectra, which can have zeros and higher-order
logarithmic interactions. A triangle can have arbitrarily large pairwise integer-factor defect as
an abstract integer tensor. The bounded-width theorem bypasses that defect
by allowing integer triangle factors and an influence-paid entropy bound;
it does not bound the Boolean pairwise defect in general.

## Find integer packets with a paid denominator

For a spectral subcube leaf $`L`$, let $`g_L`$ be the actual partial Fourier
section of a Boolean function, with squared norm $`p_L`$. Suppose its
normalized law is a positive forest, or a stated deterministic quotient,
and $`2^{d_L}g_L`$ is integer-valued. Positive bounded-width sections
can now also be used, with their stated larger constant. Applying the arbitrary-integer forest
theorem with its exact scaling cost gives

```math
H(f)\le C_F\mathbb E\bigl[|S\setminus K_L|\bigr]
       +2\mathbb E d_L,
```

where $`C_F=6/\log_2(16/9)`$ and $`K_L`$ is the set of fixed spectral
coordinates. If the actual scaled packets also have power-of-two Fourier
magnitudes, the dyadic theorem gives constant four and its stated component
deficits. No approximation or label term has been omitted in either bound.

**Target.** Construct, for a larger Boolean class or for all Boolean
functions, a partition into suitable actual sections with
$`\mathbb E d_L\le CI(f)`$, or another integer-packet decomposition with
a proved raw entropy bound and a comparable influence payment.

Singleton leaves always exist. With the least nonnegative denominator
exponent, write each nonzero coefficient as $`a_S2^{-d_S}`$ with odd
integer $`a_S`$. Their cost is

```math
2\mathbb E d_S=H(f)+2\mathbb E\log_2|a_S|\ge H(f),
```

with equality when every magnitude is a power of two. This is circular
as a route to FEI. Equal-magnitude Fourier layers need not have integer-valued
inverses, even when every magnitude is a power of two. The
[integer-packet argument](integer-flat-packets.md) cannot be applied to
those layers without paying for the lost integrality. A theorem for a
bounded number of conditioning coordinates is already proved in
[integer forests](integer-forests.md); the unresolved task is a cost that
does not grow with the required number of cuts.

## Low-information mixtures and physical selection

**Mixture target.** Find a class of Boolean Fourier laws $`p_j`$ with a
proved universal entropy–influence bound and a useful decomposition

```math
p_f=\sum_j\lambda_jp_j,
\qquad I(S;J)\le CI(f).
```

The exact chain rule then pays the total entropy. A universal mixture into
Boolean forest laws can be trivial even for three-bit majority: all
positive-weight components must be point masses. Its cost is exactly two
bits, so the example does not disprove an $`O(I)`$ bound. Allowing plateaued
components removes this particular obstruction. The challenge is a
noncircular information estimate from Boolean structure, not existence
of a mixture.

**Physical-tree target.** For an appropriate restriction tree, replace or
pay the half-bit expected-depth cost in

```math
H(f)-4I(f)\le
\mathbb E_L[H(g_L)-4I(g_L)]+\tfrac12\mathbb E D.
```

The actual leaf label has entropy $`\mathbb E D`$. Its coarsening to the
identity of the selected payload does not retain the spectral cost: an
explicit two-payload example violates that replacement. Ordinary convex
combinations of sign-valued functions cannot produce a different
sign-valued function without pointwise agreement, and physical selectors
have Fourier cross terms. The [interpolation proof](interpolation.md)
retains those terms exactly. A universal constant-four closure is
impossible, so a general repair must allow a real additional payment.

## Boolean defects of a tree projection

The tree distribution $`q_T`$ matching selected singleton and edge
marginals satisfies, including support-zero cases,

```math
H(q_T)-H(p_f)=D_2(p_f\Vert q_T),
\qquad \mathbb E_{q_T}|S|=I(f).
```

**Target.** Give a structural Boolean estimate controlling the
realizability defect of $`q_T`$ together with the divergence correction.
The displayed target $`H(q_T)\le CI(f)+D_2(p_f\Vert q_T)`$ alone is only
an equivalent rewriting of FEI. Majority's uniform three-bit projection
is not a Boolean Fourier law, so applying the forest theorem to it is
invalid. Any useful theorem must introduce a separately bounded structural
quantity rather than discard the correction or assume realizability.
