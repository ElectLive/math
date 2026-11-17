# Charged Gaussian sewing, separated points, and zero modes

**Mira Cult**

Construction and proofs by model participant 2 in the owned PR
#438 continuation, 2026-11-16. Labels GS1--GS6 are manuscript-local. The
finite exterior algebra and theta identities used here are standard; the
contribution is a precise extension and limitation of the marked Bol
architecture, including its singular sectors. This manuscript does not
re-prove the inherited loop construction or claim historical priority.

## Scope and the result

The earlier [kernel hierarchy](bol-genus-one-kernel.md) retained commuting
holonomies with no common fixed vector. Products of charged sectors can
reach a common fixed space; the
[spin-product obstruction](bol-holonomy-rigidity.md#hr4-spin-products-reach-the-zero-mode-sector)
therefore requires a different treatment there. We give it explicitly.

The result has three distinct parts. Finite complex-fermion Gaussian
contraction, with incoming--outgoing quadratic propagators as in GS1, is
coherent even at singular quadratic blocks when amplitudes are kept
unnormalized. At arbitrary separated torus positions, a bordered
determinant supplies all common-fixed-space zero-mode amplitudes and
cancels the quasiperiod and modular anomalies of the trivial-line kernel.
An infinite-dimensional sewing limit inherits these statements under
specified convergence hypotheses. The finite calculation alone does not
establish those hypotheses for every geometric sewing.

This is a baseline theory, not the stronger interaction requested by the
research program. Once the quadratic kernels, determinant factors and
finite insertion tensors have been specified, its higher amplitudes have
no independent analytic data. That dependence statement is not a theorem
that every analytic relation has a known set of generators, nor a no-go
theorem for all charged Bol sewing.

## GS1. A finite Gaussian amplitude that remains defined at zero modes

All vector spaces are complex and finite dimensional in this section.
Use odd variables psi_i, barpsi_i and odd external sources eta_i,
bareta_i, for 1 <= i <= m. Distinct odd variables anticommute. Fix the
Berezin coefficient convention


```math

 \int [d\bar\psi\,d\psi]\,
           e^{-\bar\psi A\psi}=\det A.              \tag{GS1.1}

```


For example, order each internal pair as psi_i,barpsi_i and extract their
ordered top coefficient. Define the unnormalized generating amplitude


```math

 \mathcal Z_A(\bar\eta,\eta)=
 \int[d\bar\psi\,d\psi]\,
  \exp(-\bar\psi A\psi+\bar\eta\psi+\bar\psi\eta).
                                                               \tag{GS1.2}

```


The exponential is a finite exterior polynomial. Consequently (GS1.2) is
defined for every matrix A, including singular matrices.

**Theorem GS1 (minor formula and saturation).** The following hold.

1. If A is invertible, then


```math

    \mathcal Z_A=\det A\,
                    \exp(\bar\eta A^{-1}\eta).       \tag{GS1.3}

```


2. Every source coefficient of (GS1.2) is, with the sign fixed by the
   displayed exterior ordering, a complementary minor of A. In particular
   it is polynomial in A. Formula (GS1.3) is therefore an inverse-based
   expression for a polynomial amplitude, not a definition at singular A.

3. If rank A = m-h, separate its nonsingular and zero blocks by changes
   of bases on the incoming and outgoing spaces. In coordinates
   A=diag(A_1,0_h), the exact formula is


```math

    \mathcal Z_A=
       \det A_1\,e^{\bar\eta_1 A_1^{-1}\eta_1}
            \prod_{a=1}^{h}\bar\eta_{0,a}\eta_{0,a}.
                                                               \tag{GS1.4}

```


   Thus a nonzero amplitude must saturate every incoming and outgoing
   zero mode. No division by a vanishing source-free partition function
   is permitted.

**Proof.** For invertible A, complete the square by translating the odd
variables to psi-A^(-1)eta and barpsi-bareta A^(-1). Berezin top
coefficient extraction is translation invariant. The residual external
term is bareta A^(-1)eta, proving (GS1.3).

For the minor statement, expand the exponential in (GS1.2). A selected
source monomial occupies selected internal variables; the remaining
internal variables must be supplied by the quadratic term. Its top
coefficient is exactly the determinant of the complementary submatrix,
with the ordering sign. This also proves polynomiality without taking
limits.

In block coordinates the integral factors. The nonsingular block gives
(GS1.3). For one zero pair, coefficient extraction gives bareta eta;
different paired factors are even and commute. This proves (GS1.4).
Equivalently, regularize the zero block by t I_h: the limit of
t^h exp(t^(-1) sum_a bareta_(0,a) eta_(0,a)) is precisely the product in
(GS1.4). Every assertion extends across rank changes by the polynomial
formula already proved. QED.

For a concrete singular family,


```math

 A=\begin{pmatrix}a&0\\0&0\end{pmatrix},\qquad
 \mathcal Z_A=a\bar\eta_2\eta_2
              +\bar\eta_1\eta_1\bar\eta_2\eta_2.    \tag{GS1.5}

```


The source-free amplitude is zero for every a. At a != 0, one pair of
zero-mode insertions suffices; at a=0, two pairs are required. The full
amplitude varies polynomially through this jump.

### The finite determinant line

There is no choice-free numerical determinant for a map A:E -> F without
identifying the determinant lines of E and F. Intrinsically its determinant
lies in


```math

                    \det F\otimes(\det E)^*.

```


The complementary-minor coefficients of GS1 have the corresponding
exterior powers of the source spaces attached. Equivalently they are the
matrix coefficients of the exterior powers of A, paired with the top
exterior lines. This makes them basis independent as tensors. A choice
of bases or dual volume elements produces (GS1.2); its change-of-basis
Jacobian is exactly the transition factor of that line. At singular A
one retains the line-valued amplitudes rather than dividing by its zero
determinant section.

This is finite determinant-line bookkeeping. It is not a claim that a
global Quillen determinant line, its metric, or its anomaly cancellation
has been constructed for a new interacting Bol theory.

## GS2. Coherent finite sewing and its exact dependence boundary

A finite Gaussian diagram here consists of finitely many paired incoming
and outgoing odd channel spaces, quadratic exponentials of the bipartite
type in GS1, type-preserving linear identifications of matched channels,
and integration over the matched pairs. Every quadratic propagator joins
one barred and one unbarred variable; the corresponding external-source
couplings have the same type. Unbarred--unbarred and barred--barred terms
are not included as quadratic propagators. Their general Gaussian theory
would require Pfaffians rather than the determinant formulas proved here.
An ordered finite collection of arbitrary polynomial insertions is allowed. Their
coefficients may be charged multiplication tensors, marked translations,
cocycle phases, or other specified finite tensors.

For a finite abelian charge group A_0, give channel variables charges in
A_0 and dual variables the opposite charges. Require the quadratic
terms and channel evaluations to have charge zero. An insertion may
have a specified charge; a scalar closed amplitude vanishes unless its
total charge is zero. This follows by applying every character of A_0
to the variables and using invariance of the paired Berezin measure.

**Theorem GS2 (finite sewing coherence).** For a fixed such diagram:

- integrating the paired internal channels in any order gives the same
  amplitude, with the fixed exterior ordering of external insertions;
- all amplitudes are finite sums of complementary minors of one assembled
  quadratic matrix contracted with the specified finite insertion tensors;
- on an invertible internal chart, sewing is the Schur-complement rule.
  In particular,


```math

  \begin{split}
  &\int[d\bar\psi\,d\psi]\,
   e^{-\bar\psi A\psi+\bar\psi B\xi+
                 \bar\eta C\psi+\bar\eta D\xi}\\
  &\hspace{12mm}=\det A\,
        e^{\bar\eta(D+CA^{-1}B)\xi}.               \tag{GS2.1}
  \end{split}

```


  At singular internal charts one uses the minor formula, so an
  intermediate singular block is not an obstruction to contraction.

**Proof.** All quadratic terms have even exterior degree and commute;
their exponential product is the exponential of their sum. Paired
integration extracts an even number of variables. For disjoint paired
blocks the coefficient extractions commute: exchanging two such blocks
has sign (-1)^((2r)(2s))=1. This is finite Berezin Fubini and proves
associativity of contraction, including singular blocks. GS1 applied to
the assembled matrix proves the minor statement. External polynomials
select finite source derivatives, or equivalently finite sums of these
same coefficients. Completing the internal square proves (GS2.1).

The determinant-line identifications for direct sums are exterior wedge
identifications. Their associativity and their usual Koszul interchange
signs are precisely those used by coefficient extraction. Thus the
coordinate computations agree under basis transport and every bracketing
of the same contraction diagram. QED.

The scope of this coherence statement is important. It compares different
orders of contraction of a **fixed diagram**. It does not assert an F-move
or a pentagon identity for independently proposed interaction vertices.
If extra F-symbols are supplied, their coherence must be proved separately.
Inserting them as finite polynomial tensors can encode more than ranks,
but the theorem still evaluates each fixed diagram by the same Gaussian
kernel and those tensors. It does not create a new analytic engine.

Finite charge projections do not change the conclusion. A projector is
the finite character average


```math

 P_a=|A_0|^{-1}\sum_{\chi\in\widehat A_0}
                     \chi(a)^{-1}\Gamma(\chi).

```


It is a finite sum of Gaussian boundary conditions. Sewing distributes
over that sum. Such a mixture can have nonzero higher connected
coefficients, but those are already fixed by its finitely many Gaussian
terms and weights; it is not a new freely adjustable interaction.

For uninserted nonsingular Gaussian source amplitudes the normalized
logarithm is quadratic, so connected elementary-field coefficients of
degree greater than two vanish. Composite fields can have nonzero higher
connected correlations; GS2 does not set those to zero. It expresses
them as the prescribed finite derivatives and contractions.

## GS3. All zero-mode dimensions at arbitrary torus positions

Let H be a finite-dimensional Hermitian space, and let U,V be commuting
finite-order unitaries, now allowing a common fixed space


```math

 H_0=\ker(U-I)\cap\ker(V-I),\qquad h=\dim H_0.

```


Write Pi_0 for its orthogonal projector and Pi_chi for the remaining joint
spectral projectors. The scalar k_chi are the residue-one kernels of
[K1](bol-genus-one-kernel.md#k1-the-finite-holonomy-family-and-its-unique-kernel).
Put


```math

 P(z;\tau)=\partial_z\log\theta_1(z;\tau),\qquad
 \widetilde K(z;\tau)=\sum_{\chi\ne1}\Pi_\chi k_\chi(z;\tau)
                          +\Pi_0 P(z;\tau).         \tag{GS3.1}

```


The trivial-line term is deliberately quasiperiodic:


```math

 P(z+1)=P(z),\qquad P(z+\tau)=P(z)-2\pi i.          \tag{GS3.2}

```


It is not a nonexistent elliptic simple-pole inverse on H_0.

Choose n plus insertions u_i in H at z_i and n minus insertions v_j in
H* at w_j. Assume the insertion points are pairwise distinct modulo
Z+tau Z. Let e_a be any basis of H_0 and e^a its dual on H_0, extended
by zero on H_0^perp. Define


```math

 M_{ij}=v_j(\widetilde K(z_i-w_j;\tau)u_i),\qquad
 X_{ia}=e^a(u_i),\qquad Y_{aj}=v_j(e_a),

```


and the unnormalized bordered amplitude


```math

 \mathcal B^{(n)}_{U,V}=
      \det\begin{pmatrix}M&X\\Y&0_h\end{pmatrix}.   \tag{GS3.3}

```


The sign in (GS3.3) is part of this definition. In particular at n=h it
is (-1)^h det(X)det(Y), matching the corresponding ordering convention
for saturated fermion zero modes. Matching a different literal field
trace convention may require an explicitly specified constant per pair;
no such identification is silently used below.

**Theorem GS3 (separated-point zero-mode completion).**

1. The amplitude is independent of the basis e_a. It is multilinear in
   the insertions, vanishes for n<h, and has no position poles away
   from the collision divisors. At h=0 it is exactly the previous
   zero-mode-free kernel determinant.

2. The quasiperiod terms in (GS3.2) cancel inside (GS3.3). Hence the
   amplitude has the flat-bundle position monodromy prescribed by
   U,V on the insertion vectors and covectors. It is not necessary
   to divide by a partition function to state this law.

3. For gamma=(a b;c d) in SL_2(Z), set r=c tau+d and
   (U',V')=(U^d V^c,U^b V^a). The common fixed space is unchanged, and


```math

   \mathcal B^{(n)}_{U',V'}(\mathbf z/r,\mathbf w/r;\gamma\tau)
          =r^{n-h}\mathcal B^{(n)}_{U,V}
                                (\mathbf z,\mathbf w;\tau).    \tag{GS3.4}

```


**Proof.** Changing the zero-mode basis multiplies the X block on its
right by an invertible matrix and the Y block on its left by its inverse
(with transposes if one writes the basis coordinates as columns). Their
determinants cancel. If h>n, the last h rows have rank at most n, so the
border determinant is zero. Its pole claim follows from its entries.

For any matrices A of size n by h and B of size h by n,


```math

 \det\begin{pmatrix}M+AY+XB&X\\Y&0\end{pmatrix}
       =\det\begin{pmatrix}M&X\\Y&0\end{pmatrix}.    \tag{GS3.5}

```


Indeed the AY term is removed by adding combinations of the last h rows,
and the XB term by adding combinations of the last h columns. Translating
one plus point through the tau cycle changes its row by the prescribed V
action plus a row of -2 pi i XY. The latter disappears by (GS3.5).
Translating a minus point gives the corresponding column statement.
The 1-cycle has no additive term. This proves position covariance.

The theta transformation gives


```math

 P(z/r;\gamma\tau)=rP(z;\tau)+2\pi i c z.           \tag{GS3.6}

```


All nontrivial joint kernels transform with weight one by K1. Since gamma
is invertible over Z, a vector fixed by U',V' is fixed by U,V, proving
that H_0 is unchanged. Therefore the transformed top-left block is


```math

 rM+2\pi i c(D_zXY-XYD_w),

```


where D_z and D_w are the diagonal position matrices. Formula (GS3.5)
removes the two extra terms. Scaling the top n rows by r and the last h
columns by r^(-1) shows that replacing M by rM multiplies the bordered
determinant by r^(n-h). This proves (GS3.4). QED.

The lower rows and right columns are the zero-mode saturation factors of
GS1. Expanding the border determinant amounts to choosing which plus and
minus insertions saturate them, then contracting all remaining insertions
by the nonzero-mode Gaussian kernel. This is the arbitrary-dimensional
form of the scalar bordered determinant in
[MTZ07, Proposition 6.6](../REFERENCES.md#mtz07); its modular anomaly
cancellation is the same mechanism used there in Proposition 6.13.

### A specified modular normalization

Let epsilon_2(gamma) denote the weight-one multiplier of eta squared:


```math

 \eta(\gamma\tau)^2=
       \epsilon_2(\gamma)(c\tau+d)\eta(\tau)^2.

```


It has order dividing twelve. Define the **reduced determinant amplitude**


```math

 \mathcal A^{(n)}_{U,V}=\eta(\tau)^{2h}
                                   \mathcal B^{(n)}_{U,V}.     \tag{GS3.7}

```


It transforms with weight n and multiplier epsilon_2(gamma)^h, together
with the finite permutation of holonomy labels. With the existing
24-species space H=B tensor C^24, h is divisible by 24, so this scalar
multiplier is trivial. This gives a finite-holonomy modular system at
every fixed insertion number, including the previously excluded zero
sectors, at genuinely separated points.

The adjective reduced specifies what has been normalized. Eta^(2h) is
the standard nonzero-mode determinant factor of h trivial complex-fermion
lines. Nontrivial-holonomy oscillator partition factors have been omitted,
as they were in the earlier normalized kernel hierarchy. Formula (GS3.7)
is not declared to be an ordinary trace in every sector, a canonical
trivialization of a global determinant line, or by itself a geometric
sewing theorem. Literal trace conventions and geometric determinant
factors must be supplied when those stronger identifications are used.
In particular a zero-sector partition function still vanishes without
enough insertions. The modular law rescales positions; it makes no blanket
cusp statement while holding an unrescaled position fixed.

If a finite charge action commutes with U,V, H_0 and all the projectors are
charge-stable. Charged vector insertions and finite equivariant tensors
can therefore be contracted in (GS3.3). The closed scalar selection rule
and all the finite sewing statements of GS2 continue to hold. Enlarging
the zero-mode dimension, even to a very large nonabelian common-fixed
space in another representation, changes the size of the border, not
the Gaussian nature of these amplitudes.

## GS4. What an actual continuum sewing assertion requires

Finite Berezin algebra does not prove convergence of an infinite sum over
boundary modes. Here is a sufficient analytic version whose hypotheses
are explicit and checkable.

Retain the bipartite propagators and type-preserving channel maps of GS2.
Let K be a separable Hilbert space. On a parameter domain D suppose that
Q(t) is trace-class and holomorphic in trace-class norm, and, on every
compact subset, ||Q(t)|| <= r_0<1 and ||Q(t)||_1 is bounded. Let the
external channel space be finite dimensional, with bounded holomorphic
maps B:external -> K and C:K -> external, and finite matrix D_0. Define


```math

 \det(I-Q)=\exp\left(-\sum_{k\geq1}\frac{\operatorname{Tr}(Q^k)}k\right),
 \qquad D_{\rm eff}=D_0+C(I-Q)^{-1}B.               \tag{GS4.1}

```


Finite zero channels may be adjoined and treated as in GS1 rather than
inverted. Pure exterior saturation factors occur after decomposing the
assembled quadratic form into its nondegenerate and null parts. If a
proposed zero channel still has quadratic couplings to other channels,
one must first retain those couplings in the assembled form, integrate
the invertible block, and evaluate the remaining finite source polynomial
by minors. An initially named zero block is not automatically a null
block of the assembled form.

**Proposition GS4 (conditional analytic sewing).** Finite orthogonal
truncations of the nonzero-mode Gaussian amplitude converge, coefficient
by coefficient in the finitely many external sources, locally uniformly
to


```math

            \det(I-Q)\,e^{\bar\eta D_{\rm eff}\xi},  \tag{GS4.2}

```


times the finite zero-mode factors when the null channels have been
decoupled. With mixed finite additional channels the corresponding
finite polynomial or bordered-minor expression converges instead. For a
finite diagram whose assembled nonzero-mode operator satisfies these
hypotheses, all finite contraction-order identities pass to this limit.

**Proof.** Let P_m increase strongly to the identity. Trace-class
approximation gives P_m Q P_m -> Q in trace-class norm, uniformly on
compact subsets: pointwise convergence follows by approximating Q by
finite-rank operators, and uniformity follows by a finite cover of the
compact image in trace-class norm. The same finite-rank argument shows
P_m B -> B and C P_m -> C in operator norm because the external spaces
are finite dimensional.

The logarithm in (GS4.1) converges normally since
|Tr(Q^k)| <= ||Q||_1 r_0^(k-1). Telescoping powers gives convergence of
the truncated logarithms under the same bound. The resolvents converge
by the uniformly convergent Neumann series, or by the resolvent identity.
Thus both the determinant and D_eff converge locally uniformly.
An exterior source coefficient is a finite polynomial in D_eff multiplied
by the determinant. GS2's identities consequently pass to the limit.
Any residual finite block is treated by a finite polynomial in its entries
and the effective source couplings; a decoupled null block gives the
exterior factors in GS1. These polynomial operations preserve the stated
convergence. QED.

This proposition is a sufficient analytic patch, not an assertion that
every geometric degeneration has a contractive Q or that evaluating a
field distribution at a point is automatically a bounded boundary map.
For genuine surface sewing those estimates, determinant normalizations,
and transition identifications must be established on a sewing domain.
The standard free-fermion case has such results:
[Tuite--Zuevsky, Theorem 5.1 and Proposition 5.5/Theorem 5.6](../REFERENCES.md#tz11)
give respectively the sewing determinant and its separated-point
correlations. Its domain-specific estimates are a separate analytic
input, not a consequence of the finite calculation above.

## GS5. The Gaussian dependence theorem and its limits

**Corollary GS5.** Fix the complete charged bipartite Gaussian input of
GS2: the channel
spaces and pairings, quadratic boundary matrices or kernels, determinant
normalizations, finite holonomy labels and their actions, and the finite
insertion tensors. Every finite diagram constructed by the operations of
GS2, including products that reach zero holonomy, is determined by that
input. At separated torus points it is a finite sum of tensor contractions
of the standard kernels, their position derivatives, and bordered minors.
The same dependence on the specified input holds for an analytic sewing
limit satisfying GS4, now through its Fredholm determinant and resolvent.
Such a limit is not asserted to be a finite sum of the original torus
kernels; a sewn surface can have a different genus.

An isomorphism transporting all this input transports the entire amplitude
family. A finite charge average is evaluated term by term. Zero modes
supply determined exterior saturation factors, not new adjustable
higher-point couplings.

**Proof.** Assemble the quadratic matrix and use GS1--GS2. Substitute the
meromorphic kernels at the distinct insertion points; no coincidence
specialization is used. GS3 handles every common fixed space. Multilinear
transport commutes with contraction, and GS4 proves the conditional limit
statement. QED.

This statement retains all the finite tensors, not merely their ranks or
spectra. In particular it does not say that the marked loop information
has vanished. It says exactly how that information enters this specified
analytic architecture. It also does not classify all analytic relations
among the resulting theta functions: independent elliptic, modular or
algebraic relations can exist.

Coherent finite F-symbols, if actually constructed, are additional finite
tensors in this conclusion. Their appearance alone does not change the
Gaussian propagation law. Repeated finite polynomial insertions are also
covered at each fixed diagram. An infinite sum over arbitrarily many
interaction vertices, an interacting limit, or an infinite lattice of
new charge sectors is not covered merely because every finite summand
has a Wick expansion. Its convergence, renormalization, and sewing laws
would be new mathematical obligations.

Integer-charge lattice vertex formulas can likewise conceal a change of
presentation rather than an interaction: MTZ07 Proposition 6.9 derives
charged lattice expressions within the bosonized free-fermion theory,
under its stated charge-conservation condition. Such a reformulation
does not by itself escape the dependence theorem. A different lattice
extension or a dynamical exchange theory must specify the new structure
and prove its compatibility; it is not excluded by GS5.

## GS6. A minimal algebraic escape and the remaining obligation

The Gaussian class is a real restriction. With two pairs of sources,
consider


```math

       \mathcal I_\lambda
          =1+\lambda\bar\eta_1\eta_1\bar\eta_2\eta_2,
                    \qquad\lambda\ne0.             \tag{GS6.1}

```


Its constant coefficient is one, its quadratic source coefficients are
zero, and its quartic coefficient is nonzero. It cannot equal a single
normalized Gaussian exp(bareta C eta): comparison of degree two would
force C=0 and hence make degree four zero. Thus a genuinely independent
quartic vertex can leave the single-Gaussian architecture. A finite
mixture can also leave that class, but remains subject to the finite-sum
dependence statement in GS5.

Equation (GS6.1) is an algebraic diagnostic, not a proposed solution of
Bol moonshine. To turn it into the requested theory one must derive the
interaction tensor from retained loop data, define charged sewing across
all sectors including the zero spaces, and prove a noncoincident analytic
constraint that is not merely its finite tensor contraction or Gaussian
factorization. Neither adding the zero-mode border nor rewriting a
fermion determinant as a theta function supplies that missing theorem.

The baseline is therefore substantially complete within its hypotheses:
it permits arbitrary separated points, finite charged tensors, singular
quadratic blocks, and coherent finite contraction; it states an explicit
analytic sewing condition. The stronger interacting or dynamical target
remains unresolved by this manuscript.

## Exact finite validation and sources

The standard-library script
[verify_bol_gaussian_sewing.py](../code/verify_bol_gaussian_sewing.py)
uses exact rational exterior algebra. It checks inverse-based formulas
against direct coefficient extraction, singular zero blocks including
(GS1.5), contraction in three orders through an individually singular
pivot block, a nontrivial Schur complement, and the bordered identities
used for position and modular covariance. Its output states explicitly
that it does not test continuum convergence, theta transformations,
an interacting theory, or inherited Bol inputs.

The primary analytic antecedents are
[MTZ07, Propositions 6.6, 6.9 and 6.13](../REFERENCES.md#mtz07),
[Mat19, Proposition 2.3](../REFERENCES.md#mat19), and the
[Tuite--Zuevsky sewing results](../REFERENCES.md#tz11) identified in GS4.
The source details and exact inspected
versions belong in REFERENCES.md. The proofs here use elementary finite
exterior algebra, theta transformation laws, and the explicitly proved
norm estimates; none of those sources is being presented as a theorem
about the new Bol examples.
