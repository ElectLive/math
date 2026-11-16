# Code and reproducibility

## Running code

From the repository root, using Python 3.11 or later:

```bash
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_section_mixing.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_section_local.py
python check.py
```

Both research scripts use only the Python standard library, accept no inputs,
and print deterministic JSON. They use exact integers and `fractions.Fraction`;
no floating-point eigensolver or approximate equality is used. A failed check
raises an assertion and exits nonzero. The integrity checker validates
repository structure and tool behavior, not these mathematical theorems.

The [finite verifier](verify_bol_section_mixing.py) checks
(Q,m,d)=(3,2,1),(3,2,2),(5,2,1),(5,4,1),(7,3,1),(7,6,1). It builds transition
matrices from the original loop law. It checks the integer cubic identity,
all starting rows at steps one and two, a point at steps one through six,
exact signed multiplicities from the polynomial and traces, and one-step
mixing on each exceptional component. For the 54-element first loop it checks
all Latin rows/columns, inverses, 157464 Bol triples, 1944 correction
pair/state choices and 216 coherence triples. Each larger case uses 512
sampled triples with fixed seed 20261116 for loop/correction tests. Properness
has an explicit witness in every case.

The [local verifier](verify_bol_section_local.py) checks the exact Fourier
orbit action over Z/3, Z/9 and Z/49 at zero, primitive and nonprimitive
coefficients. It counts every two-step history for (p,A)=(3,1),(3,2),(3,3),
(5,1),(5,2),(7,1), up to 250000 histories in a case, and compares the resulting
total variation with the closed formula. The proof covers all finite valuation
rings and all stated dimensions; this script checks only the displayed prime
rings and dimension one.

An independently written supplementary verifier is preserved as
[verify_bol_section_independent.py](verify_bol_section_independent.py). It uses
NumPy 2.3.5 in addition to the standard library and may be run with the same
Python command. It builds original-coordinate matrices and path counts without
importing either authored checker. Besides six finite cases and nine ring
path enumerations, it checks the 486-state Z/9 spectrum by an integer
annihilating polynomial and six moments. Its bounded integer arithmetic is
within signed 64-bit range. This records an actual independent review
experiment; it is not a formal verification of the general theorem.

## Reproducibility

The sources specify all parameters and seeds. The delivered run used Python
3.12.14. Exact source hashes, commands, outputs summarized by case, and the
independent review revision are recorded in the
[review and execution evidence](../evidence/bol-metaplectic-review.md). Raw output files and downloaded source PDFs remain outside Git.

The scripts are finite evidence. They do not establish a theorem for all
prime powers, prove the compact local limit or certify historical novelty.
Those results require the proofs in the
[finite](../manuscripts/bol-section-mixing.md) and
[local](../manuscripts/bol-section-local.md) manuscripts. The reviewed family
is proper but not claimed simple; these scripts are not simplicity or
isomorphism-deduplication tests for the classification programme.

## Full-pencil collective cancellation

```bash
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_collective.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_collective_independent.py
```

This standard-library checker accompanies
[the collective manuscript](../manuscripts/bol-collective-cancellation.md).
It uses exact arithmetic in F3[lambda]/Phi7 and Q(zeta21), with no
floating-point calculation. It checks all 729 field traces and nonzero
inverses, all 27 scalar ranks of both six-dimensional pencils, tuple
independence, zero common radical, maximizing image incidences, all 13
projective hyperplane masses, the original Gauss-period weights and the
seven roundtrip Fourier weights. It samples 64 Bol triples and 64 actual
word/displacement pairs per family with seed 20261116.

A directly enumerated restriction has 27 inputs, 729 outputs and 19683
readout pairs. It uses u in lambda*F3^3 and y in F3^3, with the second
E^3 block zero, and checks every Gram difference and Fourier multiplier.
Using both arguments in F3^3 would trivialize the trace, since Tr(1)=0.
This is an actual restricted loop observable, not an enumeration of the
full E^6 matrix. The general h-block, degree-filtration, counting and
reduction-obstruction statements rely on their written proofs. The tensor
checkpoint was independently accepted at `6437948a7c3a1d0e437f2fa51b114875351ae7d8`;
the stronger complete continuation was separately reviewed at
`ab2af8ae4f8437ca9451bb71a1bc66592daa57ce`, including all five delivered
collective verifiers. Exact hashes and run scopes are in the review record.

The reviewer-authored [independent incidence checker](verify_bol_collective_independent.py)
uses no authored checker imports. It independently counts the incidence and
two-way correlations on the actual 27-input restriction: 19683 word differences,
137781 correlation terms, and every one of its 27 Fourier multipliers. It uses
only exact standard-library arithmetic.

## Coupled pencils on all mean-zero inputs

```bash
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_coupled.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_plane_mass.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_coupled_independent.py
```

The first two scripts require NumPy (delivered version 2.3.5), used for bounded
integer field tables and exact finite-field Gaussian elimination. They use
no floating-point arithmetic or approximate rank. The plane-mass script imports
the adjacent coupled-field implementation; these two are authored checks, not
independent of one another.

The [coupled checker](verify_bol_coupled.py) checks all 27 and 243 scalar
parameters for h=1,2: alternating matrices, linearity over F3, identical ranks
4 and 8, zero common radicals, and an aligned frequency in every nonzero image.
For 260 sampled/constructed linearized polynomials per h, it checks every
parameter and independently computes the restriction's F3 nullity. It compares
324 and 2916 image memberships directly by augmented matrix ranks. The random
seeds are recorded in the source (2026111600+h and 20261116).

For h=2 it uses L=E[T]/(T²-d), with d=2+lambda+lambda² a certified nonsquare,
and M=E[S]/(S³-S-lambda), irreducible because the absolute trace of lambda is
2. The latter has Tr_(M/E)(1)=0, while its trace pairing remains nondegenerate.
The parameter bases alternate extension coordinates; the theorem permits every
injective F3-linear parameter map, not only the lexicographic example.

The [plane-mass checker](verify_bol_plane_mass.py) exhausts the 13 planes of
F3³ and the 1210 planes of F3⁵ in reduced row-echelon form, using exact
Q(sqrt(21)) weights. Their maximum masses are 13/27 and 127/729. It checks
the attaining plane (s,...,s,t), its explicit degree-nine subspace polynomial,
and the corresponding nonzero frequency's membership in exactly eight scalar
images. It obtains the exact nonzero masses 343/729 and 10255/59049.

The reviewer-authored [independent coupled checker](verify_bol_coupled_independent.py)
uses only the standard library and imports no authored checker. It tests the
h=3 Artin--Schreier trace edge at 71 nonzero sampled parameters, with seed
20261117, and exhausts the 2187-point parameter space for the attaining
subspace polynomial. It verifies zero common radical, rank 6 for a single
copy, rank 12 after duplication, and independence over F3. The E-rank of this
tuple is only four, illustrating why E-independence must not be assumed.
It also independently enumerates the 13 and 1210 parameter planes.

These extension-field checkers do not recompute the external 18/49 word factor;
the collective and independent incidence checkers above cover that interface.
They are finite evidence for Theorem D and Lemma M, whose general statements
are proved in the manuscript. No full huge operator matrix is enumerated.

## Arithmetic conductor correspondences

```bash
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_conductor_central.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_conductor_vector.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_conductor_independent.py
```

These accompany the [conductor manuscript](../manuscripts/bol-conductor-correspondence.md).
The central program requires NumPy 2.3.5 in the delivered run, used only for
bounded exact integer arrays. The vector program uses only the standard
library and imports the adjacent authored `verify_bol_collective.py` field
implementation. These are authored checks; sharing that implementation is
explicitly distinguished from independent review.

The [central checker](verify_bol_conductor_central.py) uses exact cyclotomic
reduction to check every absolute trace power and central Fourier character
at orders 7, 49, 343 and 2401, together with all relative trace powers where
applicable. It checks zero, primitive and every imprimitive conductor weight,
the shell autocorrelation, every central transfer between those levels,
and compatible eta-phase shifts for k=1,3,5. All arithmetic is integral or
rational; no approximate Fourier transform is used.

It computes the histogram weights at every parameter character for k=3,5
and exhausts the 13 and 1210 two-planes. The exact squared norm ratios are
26/53 and 350/1511. It checks the full finite central Gram and the normalized
histogram-isometry identity at (A,k)=(3,3),(4,5),(3,5), including the sharper
range 7^(A-1)>k². The preserved failure at (2,3) is the collision of
histograms (0,0,3) and (1,2,0) modulo seven. The source output identifies
the earlier scientific/delivery pins as baselines, not as the new review pin.

The [vector checker](verify_bol_conductor_vector.py) implements the actual
extension E2=E1[t]/(t^7-lambda), E1=F729. It checks order 49, all 49 trace
powers, sampled Frobenius/absolute-trace calculations, the trace-pairing rank
seven and trace-zero rank six. For every one of 27 character labels of both
six-dimensional cross-product/star controls from `verify_bol_collective.py`
it checks the base, transverse and full
ranks, and the corresponding kernel density and Heisenberg dimension.
The finite theorem's general coupled pencils remain covered by their earlier
proofs and checkers; this experiment tests the new trace interface on the
specified six-dimensional controls.

With seed 20261116 it checks 32 trace-splitting samples per pencil, and 12
original Bol triples and actual word/readout samples per pencil at each of
the two ring levels 7 and 49. The compatible scalar is eta2=30. An exact
restriction to F3³ coefficients in the actual t/t^6 and t²/t^5 trace blocks
checks 19683 phase terms, all 27 character sectors, and coisometry/coherence
with rational normalization. This restriction is not the full transverse
fiber, and is not used to infer its cardinality experimentally.

The [independent checker](verify_bol_conductor_independent.py) uses only the
standard library and imports no authored checker. It constructs the actual
fields F3[X]/Phi_(7^A) at A=1,2 and checks 48 Bol/word cases at each level for
an explicit n=2,k=1 alternating pencil, all 42 relative-trace basis elements,
trace-kernel ranks, and 64 trace splittings. It checks translated-readout
Grams at A=3,4,5, normalized image energies, the exact 6/7 old-projection
energy fraction, the histogram weights and all two-planes for k=3,5, and
the below-threshold collision at A=2. Its seed is 2026111607.

All three programs passed on Python 3.12.14. The all-level operator identities,
constant corrections, mixture inequality, Hilbert limit, asymptotic and
counting consequence depend on the written proofs and the new independent
exact-source review. No full huge field or operator is enumerated.

## Intrinsic associator quantization and mixing

```bash
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_associator_bilinear.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_associator_weyl.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_associator_independent.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_associator_ring_independent.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_nonbol_reversibility_control.py
```

These accompany the [associator manuscript](../manuscripts/bol-associator-quantization.md).
All five passed under Python 3.12.14. The independent ring program uses
NumPy 2.3.5 only for bounded exact integer arrays; the other four use the
standard library. Source and complete-output hashes are preserved with
the exact-source review, separately from the earlier conductor evidence.

The authored [bilinear checker](verify_bol_associator_bilinear.py) imports
no other program. It checks 6561 alternating bilinear sums over F3³:
all 27 cross-pencil matrices, all 27 coefficient vectors, all nine
scalar-coefficient pairs, and all 729 summands for each. It then checks
156 ring-plane averages modulo seven and 134 modulo 49, including zero,
primitive and imprimitive characters, both module-image cases and all
three acting labels on the selected boundary cases. Ring histograms use
exact coordinate-pair counts and convolution; the output distinguishes
represented four-variable summands from actually enumerated scalar pairs.
The program checks the sharp 1/9 mode. This is authored finite evidence.

The authored [Weyl checker](verify_bol_associator_weyl.py) imports the
adjacent authored `verify_bol_conductor_vector.py`, which uses the earlier
authored field implementation. It checks 96 actual permutation samples
and 480 basis-vector/character samples over the six-dimensional cross/star
controls at levels seven and 49. It verifies direct left-division defects,
the full shear-and-dilation composition, corrected Weyl phases, the Bol
sandwich and palindrome identities, inverse defects, genuine loop
isomorphisms obtained by simultaneous pencil/basis changes, and a nonlinear
change of coset representatives. The latter is a section gauge, not a
claimed loop isomorphism. The seed is 2026111609. Shared implementation
is not independent review, and no full representation matrix is enumerated.

The reviewer-authored [independent defect checker](verify_bol_associator_independent.py)
imports no authored checker. It constructs F3[X]/Phi_(7^A) independently
at A=1,2 for the n=2,k=1 reciprocal family and checks 96 and 32 samples,
respectively, with seed 2026111609. It uses actual multiplication and raw
left division, checks the Bol identity, defect formula and inverse law,
the shear composition, Weyl phases before character evaluation, the
palindrome and right-nucleus equivariance. These are finite sampled
identities; general admissibility and naturality are proved in the text.

The reviewer-authored [independent ring checker](verify_bol_associator_ring_independent.py)
directly enumerates every pair in ((Z/49)²)² for every one of nine acting
coordinate pairs in eight selected conductor/module-image cases, totaling
415065672 exact character terms. It imports neither the authored Gaussian
formula nor another checker. Cyclotomic reduction is exact. The zero,
primitive and imprimitive examples include the incompatible value 1/441,
the compatible value 1/49, an annihilated-character value 1, and 1/2401.

The reviewer-authored [non-Bol control](verify_nonbol_reversibility_control.py)
checks an explicit order-five Latin loop by all 125 point compositions.
Its inner-defect transition counts are not symmetric (5 versus 6 at
the displayed pair), and 57 triples fail the left Bol identity. This
shows why reversibility cannot be attributed to generic loop averaging.

The complete all-conductor spectrum, exact global mixing norm and sharp
energy inequalities rely on the written proofs and their independent
review, not extrapolation from these finite checks. In particular, the
global theorem's nonzero right-nucleus-character blocks are bounded;
only its zero-character blocks are fully diagonalized. Earlier accepted
proofs, checkers and review pins remain unchanged.

## Intrinsic spectral separation

```bash
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_intrinsic_spectrum.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_intrinsic_incidence_independent.py
```

These accompany the [intrinsic separation manuscript](../manuscripts/bol-intrinsic-spectral-separation.md).
Both use only Python's standard library and exact integer/Fraction arithmetic.
The coordinator read and ran both under Python 3.12.14. No enormous loop
table, floating-point rank calculation, or random sampling of the parameter
pairs is used. Their source and full-output hashes are recorded with the
separate exact-source review in the existing evidence record.

The [spectrum checker](verify_bol_intrinsic_spectrum.py), authored by the
contributing agent `/root/incidence_derivation`, checks h=1,2,3,4 for total
dimension, all spectral multiplicities, the exact upward transfer measure,
the common fixed space, moments 1 through 4, the canonical low cutoff,
its top multiplicity, and both the power and fixed-quadratic collective
bounds. The quadratic energy is computed both directly and from moments
2,3,4. At h=1 it also enumerates every allowed character/support label and
the actual sixteen nonzero three-cycles in F7². At h=8 it checks that the
squared RMS ratio divided by 729·9^(−h) differs from one by less than 1/1000.
That final test illustrates the limit; the asymptotic proof is in the text.

The [independent incidence checker](verify_bol_intrinsic_incidence_independent.py)
was authored separately by noncontributing reviewer
`/root/independent_spectral_review`. It imports no authored checker.
For h=1 it constructs both actual 6×6 pencils over
F3[lambda]/Phi7, checks all 729 ordered parameter pairs in each family,
and calculates image intersections by exact matrix ranks. The histogram
of intersection dimensions is {0:53,2:624,4:52} for spread and
{0:53,3:624,4:52} for aligned. It verifies the absolute trace pairing has
rank six even though Tr(1)=0, the common radicals are zero, and the
nonzero scalar ranks are all four. It enumerates the actual order-seven
scalar orbits in one E-line and the order-three plane orbits, then
aggregates 181440 AQ.27--AQ.29 label contributions per family using the
matrix-derived counts. It checks total and per-nucleus-sector dimensions,
the fixed space, canonical low band and top ranks, and moments 1 through 4.
An order-five Latin-loop control checks arbitrary relabeling, the trace
as associative-triple count, and trace preservation by translation
conjugation; a cyclic group supplies the associative control.

For h=1 the common loop order is 3337453428382706771853981 and the
exact trace difference is 6207245000998912/22235661. The programs support
the uniform proof rather than substitute for it. They take the prior
AQ.29 block formula as mathematical input; the independent program
reconstructs its new image-incidence and orbit aggregation, not its entire
earlier proof. No higher-moment formula for the global operator M is claimed.

## Action-compatible arithmetic transfer

The canonical proof is [the action-transfer manuscript](../manuscripts/bol-action-compatible-transfer.md).
Run from the repository root with Python 3.12.14 (standard library only):

```bash
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_action_transfer_envelope.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_action_transfer_polarized.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_action_transfer_independent.py
```

The first two are authored checks, reusing the earlier exact field/conductor
implementation. The envelope program checks 48 actual group/section/quotient
cases for both earlier pencils, 2,352 full section/correction charge cases,
all 16,807 scalar-coset cocycle cases, 30,618 scalar-orbit support cases, and
three exact normalization towers. It checks all 49 upper ring charges,
including lifts of zero and all imprimitive cases.

The polarization program checks all 49 relative trace-pairing entries,
pairing ranks 7/6/1, dimensions 4/25/172 through gaps one/two/three,
396 complementary exponents, all three tower splittings through gap three,
and 48 actual upper polarized loop/Bol/quotient samples in both pencils.
Its field kernel is explicitly nonzero.

The independent program imports no project checker. It separately implements
F729 and its degree-seven Kummer extension. Its finite scope includes 96
basic and 96 polarized actual-loop triples with full correction, inverse
and Bol checks; 192 basic-fiber bijections; all conductor labels at levels
(1,2), (1,3), (2,3); exact normalized transfer identities; 6,353,046
direct mixed-ring character terms; all 49 relative pairing entries;
polarization and tower checks through relative degree343; and 1,458
polarized scalar-excursion coefficient checks. The final stdout is the
authoritative detailed count if a named subcheck counts multiple identities.

The enormous full loop, induced coset space and spectral matrices are not
enumerated. Sampled identities and bounded exhaustive sums support the
written all-parameter proofs; they do not prove them by extrapolation.
Source pins, hashes, independent-review attribution and exact replay results
belong to [the evidence record](../evidence/bol-action-transfer-review.md).


## Non-scalar intertwiners and quantum mixing

For the non-scalar continuation, run `verify_bol_nonscalar_fusion.py`, `verify_bol_nonscalar_orbits.py`, `verify_bol_nonscalar_quantum.py`, and `verify_bol_nonscalar_independent.py` from this directory. See the [full manuscript](../manuscripts/bol-nonscalar-intertwiners.md) and [review and reproduction evidence](../evidence/bol-nonscalar-review.md).


## Sparse quantum randomization

For the [randomization manuscript](../manuscripts/bol-quantum-randomization.md),
run these commands from the public repository root:

```bash
python notes/finite-simple-bol-loops/analytic-2026-11-16/code/verify_bol_randomization.py
python notes/finite-simple-bol-loops/analytic-2026-11-16/code/verify_bol_small_bias.py
```

Both are standalone Python standard-library programs, accept no input and use
exact integer, rational and finite-field arithmetic. The recorded runs used
Python 3.12.14. A failed assertion exits nonzero; successful execution prints
deterministic JSON. Exact source and stdout hashes, scientific revision and
review status appear in the [reproducibility record](../evidence/bol-randomization-reproducibility.md).

The channel checker covers the specified F729 presentation, actual translated
defects, one-call Weyl-coset realizations, degenerate covariances, native
commutant witnesses, the ring channel, purity equality cases and the exact
dense depolarizing weight. A separate fused-conjugate-sector diagnostic checks
all 2,401 entries and 117,649 Gram terms of the 49-dimensional ring factor.
The small-bias checker covers the blocked-coordinate sampler and nine resource
cases for both one-call and independent-round constructions, as detailed in its
JSON output and the evidence record. It
does not implement the cited general Shoup irreducible-polynomial construction.
Neither checker constructs the full superoperator, whose input dimension is
already 26,040,609 at n=2. The finite scopes corroborate the written general
proofs; they are not an exhaustive proof or independent mathematical review.
