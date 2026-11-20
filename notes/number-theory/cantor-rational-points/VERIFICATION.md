# Verification and scope

This is a conventional mathematical proof draft for independent review. The argument and the assembled manuscript were cross-checked internally by models working separately, including a check of the uniform quantifiers in the mixed-fiber estimate, the passage from convolution to set cardinality, and the adaptive prime-power selection. The new lower-bound argument was cross-checked separately, including the Fourier error, the progression average, and the transition from triadic to all heights. This is not human peer review, formal verification, or a certification of priority.

| Mathematical assertion | Location in the [manuscript](paper/cantor-rational-points.pdf) | Dependency |
| --- | --- | --- |
| Full reduced-denominator count for the middle-third Cantor set | Theorem 1.1, proved in Section 8 | The divisor itinerary and joint small-step entropy (Section 2), a height-averaged Fourier detector and uniform mixed sums (Sections 3–4), Boolean growth and least common multiples (Sections 5–6), and the adaptive prime-power bound (Section 7) |
| Logarithmic lower bound and exact preperiod identity | Introduction and the end of the counting proof | Rahm, Solomon, Trauthwein and Weiss, Proposition 3.3, for the known lower bound; elementary ternary arithmetic for the identity |
| Superlogarithmic lower bound at all sufficiently large reduced heights | Theorem 1.2, proved in Section 9 | Baker–Harman, Theorem 1, for smooth shifted primes; a digit Fourier estimate, Chinese remaindering, and the preperiod identity. The proof is independent of the upper bound. |
| Intrinsic approximation dimension and critical Hausdorff measure for exact exponents | Final section | Counting theorem, a dyadic covering, and Beresnevich–Velani's mass transference theorem |

The main imported inputs are the subpower period bound for *represented* denominators recorded by Rahm, Solomon, Trauthwein and Weiss, the integer Boolean-cube sumset inequality, and the weighted Balog–Szemerédi–Gowers and prime-field subgroup estimates used at the indicated points in the proof. The metric corollary additionally invokes mass transference. The paper quotes the exact scopes and gives the new intermediate arguments within the paper. Nothing depends on reproducing numerical experiments. The separate [research writeup](README.md) is a guide rather than a replacement for those arguments.

The LaTeX source was compiled with pdfLaTeX and BibTeX; the bibliography and cross-references resolve. The PDF is included alongside the source. This verifies the build, not the theorem.
