# Mathematical targets beyond the proved classes

**Mira Cult · 16 November 2026**

[Overview](README.md) · [Proved results](CATALOGUE.md)

The final target is a dimension-independent constant $`C`$ for
$`H(f)\le CI(f)`$ for every Boolean function, including constants and
unbounded degree. The problems below isolate unpaid costs in the present
proofs. Solving one must not be described as solving general FEI unless
the additional deduction is supplied.

## Positive pairwise spectra of treewidth two

**Target.** Prove $`H(f)\le CI(f)`$ with one universal constant for every
Boolean $`f`$ whose full-support Fourier law factors into unary and pairwise
potentials on a graph of treewidth at most two, or give an explicit family
in this class with unbounded ratio.

The arithmetic obstacle is removed: every Walsh magnitude in this class
is a power of two. Cacti and graphs with one feedback vertex satisfy the
stronger constant-four bound. For a general feedback set $`K`$ of size
$`k`$, the current component payment leaves

```math
H(f)\le4I_{K^c}(f)+2(k-1-b),
```

where $`b`$ counts edge-containing residual components of the minimal
interaction graph. The square of an eleven-vertex path has no feedback
set with $`b\ge k-1`$. Thus choosing a better set by this single count
cannot settle even that graph. A repair could use quantitative conditional
energy deficits, the influences of the removed coordinates, or a different
decomposition. It must explain why the remaining payment does not grow
with dimension. See [cycles and cacti](cycles-and-cacti.md).

This problem concerns pairwise potentials. A general factor of arity three
on a triangle is outside the arithmetic theorem and is a separate class.

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
the current cactus and bounded-conditioning results. It would not by itself
cover arbitrary Boolean spectra, which can have zeros and higher-order
logarithmic interactions. The factor-arity-three extension of the present
logarithmic Sobolev proof fails at its absorption step; that failure is a
barrier to this argument, not a counterexample to the proposed FEI class.

## Find integer packets with a paid denominator

For a spectral subcube leaf $`L`$, let $`g_L`$ be the actual partial Fourier
section of a Boolean function, with squared norm $`p_L`$. Suppose its
normalized law is a positive forest, or a stated deterministic quotient,
and $`2^{d_L}g_L`$ is integer-valued. Applying the arbitrary-integer forest
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
