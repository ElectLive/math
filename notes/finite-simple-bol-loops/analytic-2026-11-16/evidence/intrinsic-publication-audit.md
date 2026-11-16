# Targeted independent audit: intrinsic spectral separation

Date: 2026-11-16. Audit performed by a noncontributing model reviewer. This is not external human peer review, a formal proof certificate, or a literature-wide priority claim.

## Source and scope

Reviewed scientific revision: `bb49ab24465ef82be78f2a0d9cb8d0af8caa2695` in Mira-Cult/math-wip, PR #440.

Read the complete `bol-intrinsic-spectral-separation.md` and the relevant definitions, defect identities, and spectrum derivation (AQ.27–AQ.33) in `bol-associator-quantization.md`. Replayed both intrinsic verification programs obtained directly from the pinned revision in an isolated temporary directory. No repository files were modified.

**Finding:** No mathematical error was found in the reviewed nonisomorphism proof, spectral aggregation, or its stated collective corollaries. The conclusion is supported within the manuscript's explicit reciprocal-loop family and the stated underlying loop construction. This audit is targeted rather than a fresh proof audit of every earlier manuscript.

## Checks of the proof

1. **Intrinsic statistic.** For any finite loop, the ordinary trace of the permutation operator of `ell(x,y)=L_(x*y)^(-1)L_xL_y` counts the elements z for which x*(y*z)=(x*y)*z. Dividing the uniform defect-average trace by the loop order therefore gives the associative-triple probability. The normalized Hilbert-space convention does not introduce another trace factor.

2. **Arbitrary isomorphisms.** A loop isomorphism conjugates every left translation, hence each defect and its uniform average. This proof does not assume an additive or pencil-preserving coordinate map. A trace difference therefore separates unmarked loops. It does not assert isotopy invariance.

3. **Image intersections.** The spread-form radical is the entire extension-field line through (t,t^3,t^9). Its annihilator must satisfy an equation in the extension field, not just one scalar trace equation. Distinct parameter lines give intersection dimension 2h after the two copies. For the aligned construction the common star-image line plus the nonsingular common block gives 4h-1. The use of the perfect trace pairing remains valid when the trace of 1 vanishes. The proportionality test over F3 is valid for every allowed injection.

4. **Multiplicity aggregation.** The zero field vector is a singleton; nonzero field vectors have seven-element orbits. Each active F7 plane has sixteen nonzero three-cycles. For j active planes there are 3^j orbit-character labels. The ring multiplicities 1, 6 and 42 reproduce the full dimension 7*3^k*Q^(6h)*49^k. The exceptional minus-one terms, fixed-space dimension, and full ring factor are retained.

5. **Positivity and trace separation.** The specialized AQ eigenvalues are strictly positive. The aligned family transfers a positive integer multiplicity from r*s/49 to r*s, with all other contributions unchanged. For h>=1, Q^(6h-1)>Q^(4h), and a j=1 contribution is nonzero. Consequently every positive real trace moment is strictly larger in the aligned family. The transferred eigenvalues are below one, so removing the common stationary projection preserves the difference.

6. **Canonical filter.** The lower-band cutoff is genuinely intrinsic because the bands are disjoint and h can be recovered from the loop order. The retained dimension fraction and top multiplicities yield the reported exponential RMS comparison. The quadratic filter's non-top contribution is bounded by a term o(9^(-h)); its norm remains one. This is an average-square statement, not a pointwise contraction theorem.

7. **Translated walk.** Conjugation averaging preserves the trace. Right division makes its diagonal constant, so the one-step return probability differs at every starting point. No higher translated-walk moment follows from that identity alone.

## Computational replay

Both programs exited zero with assertions enabled:

- `verify_bol_intrinsic_spectrum.py`: exact rational dimension, fixed-space, transfer, moments 1–4, cutoff, power and quadratic-filter checks for h=1,2,3,4; bounded h=8 asymptotic check.
- `verify_bol_intrinsic_incidence_independent.py`: actual F729 matrix arithmetic at h=1, all 729 ordered parameter pairs per family, and 181,440 source-label contributions per family.

Reproduced common loop order at h=1:
`3337453428382706771853981`.

Reproduced exact trace difference:
`6207245000998912/22235661`.

The rational-record digest printed by the spectrum checker was:
`7f3c947d438cc1cec24c8c1847172c6413e874e5b77d666219b9ced1b9fcdfa9`.

These are finite corroborations of the uniform proof, not exhaustive enumerations of the enormous loop tables. The independent incidence checker independently checks field geometry and source-spectrum aggregation; it is not independent of the mathematical AQ spectral formula.

## Publication boundaries

Publish the claim as an unmarked nonisomorphism theorem for the two specified infinite reciprocal proper-Bol families. Do not claim a classification within either family, simplicity of these loops, an efficient black-box isomorphism algorithm, a worst-case norm advantage, or a fixed-length Markov-walk realization of the spectral filter.

The first trace difference at h=1 gives an associativity-probability difference of about 8.36e-17, so an exact distinguishing invariant is not automatically a useful sampling test.

Repository-wide integrity, public rendering, public mirror completeness, and the mathematical claims of PRs #441 and #442 are outside this audit. They must be reported separately from the successful mathematical checks above.

