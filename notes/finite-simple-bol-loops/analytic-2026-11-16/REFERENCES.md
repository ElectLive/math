# References

Source key **ALGEBRA.SIMPLE_PROPER_BOL**; stable problem ID **0323**.

## Sources

Primary construction baselines below; scope and review limits are recorded separately.

### N07

Gábor P. Nagy, *A class of simple proper Bol loops*, arXiv:math/0703919v1, 30 March 2007.
[Primary version](https://arxiv.org/html/math/0703919v1).
- §1: left/right Bol conventions, proper meaning non-Moufang, and comparison with the finite simple Moufang classification.
- §2: Bol folders, multiplication groups and normal-subloop arguments.
- §§3–4: exact-factorization construction and simple proper examples.

Used as a construction baseline, not a complete classification. The abstract's historical existence question is answered by the paper itself and must not be repeated as still open.

### N07E

Gábor P. Nagy, *A class of finite simple Bol loops of exponent 2*, arXiv:0709.4544v1, 28 September 2007.
[Primary version](https://arxiv.org/html/0709.4544v1).
- Abstract and §1: infinite right-Bol exponent-2 family; right multiplication group an extension of an elementary abelian 2-group by S5; smallest member of this family has order 96.
- §§3 and 5: initial construction and infinite family.

Translate right to left using the opposite operation, as specified in PROBLEM.md. Use N07 §1 for the standard Bol identities rather than copying ambiguous or typographically suspect formulas from rendered sources. The 96 statement is family-specific.

## Source and review limits

These two primary versions were inspected for problem intake on 2026-11-13. Their arguments have not been independently re-proved or formalized in this workspace. A comprehensive subsequent-literature audit, including equivalences and possible overlaps among constructions, remains a first research obligation. No claim that every narrower classification question remains open is made.

Mira's request fixes the unrestricted non-Moufang classification as its own problem rather than an instance of a Moufang classification or a generic discovery-engine benchmark.

## JS: simple Bol permutation rank

Johnson–Smith, On the smallest simple, unipotent Bol loop, §§1.1,2.1 ([author PDF](https://jdhsmith.math.iastate.edu/math/BolBoolf.pdf)). The full multiplication-group double-transitivity question is adopted; the precise loop-character-theoretic conjugacy bridge requires checking before an equivalence claim.


## Analytic transfer sources (2026-11-16)

These sources support [the analytic application](BOL_METAPLECTIC.md). They do
not alter the classification status above. The
[intake inventory](manuscripts/bol-metaplectic-intake.md#scope-and-inspected-sources)
records inspected Git revisions and the exact imported folder dependencies.

### BOL-0025

Mira Cult, *Alternating-form construction*, manuscript 0025, inspected at
Mira-Cult/math commit `f54b5376cb098e52d56ba0e599598d92ff6978a3`.
[Pinned source](https://github.com/Mira-Cult/math/blob/f54b5376cb098e52d56ba0e599598d92ff6978a3/notes/finite-simple-bol-loops/manuscripts/0025-alternating-form-construction.md).
Section 4, especially equation (8), supplies the displayed restricted proper
section used as the seed. The underlying alternating family and class-two
folder interfaces, equations (6), (7)--(10), (14)--(15), were also inspected.
Their simplicity, exhaustion, G-loop and strict-isomorphism assertions retain
their stated dependencies; the analytic loop family is re-proved directly.

### GH-Q

Shamgar Gurevich and Ronny Hadani, *Quantization of symplectic vector spaces
over finite fields*, arXiv:0705.4556v4, 20 August 2009.
[Primary version](https://arxiv.org/html/0705.4556v4).
Sections 2.2--2.4 and 2.7: canonical intertwiners, their multiplicativity,
tensor products, duality and symplectic reduction. Used only after verifying
the radical quotient; it does not assert regularity of a vector-valued pencil.
For the conductor continuation, Propositions 2.7.1 and 2.7.5 give the exact
tensor-product and isotropic-invariant interfaces used as the comparison
baseline for the explicit kernel construction.

### GH-SR

Shamgar Gurevich and Ronny Hadani, *Bounds on certain Higher-Dimensional
Exponential Sums via the Self-Reducibility of the Weil Representation*,
arXiv:math/0612765v2, 8 February 2010.
[Primary version](https://arxiv.org/html/math/0612765v2).
Sections 2.2--2.4 and Theorems 3.1--3.4: torus structure, multiplicities,
self-reducibility and Wigner bounds. Eigenstate and displacement hypotheses
are retained; no bound for an arbitrary Bol section is inferred.
Proposition 2.9 and Theorem 2.10 identify trace-center pullback and the
corresponding Weil representation; Theorem 2.13 treats the product case.
These are restriction-of-scalars interfaces, not an automatic reduction of
the full reciprocal section across conductor levels.

### JS-ACTION

Kenneth W. Johnson and Jonathan D. H. Smith, *Matched pairs, permutation
representations, and the Bol property*, Communications in Algebra 38(8)
(2010), 2903--2914, DOI 10.1080/00927870903095590.
[Author PDF](https://jdhsmith.math.iastate.edu/math/MPBLPR.pdf).
Theorem 6.1 and Section 7 give prior stochastic/permutation-action machinery;
the analytic work does not claim to invent this interface.

### SYMPLECTIC-GRAPH

Bart De Bruyn, Sergey Goryainov, Willem H. Haemers and Leonid Shalaginov,
*Divisible design graphs from the symplectic graph*, arXiv:2404.09902v1,
15 April 2024.
[Primary version](https://arxiv.org/html/2404.09902v1).
Section 2.4, Lemma 4 gives the polar-graph eigenvalues used for the existing
finite 1/m norm bound. The affine-slab identification and the comparison are
proved in [the controls](manuscripts/bol-section-controls.md).

### NICA

Bogdan Nica, *Unimodular graphs and Eisenstein sums*, arXiv:1505.05034v2,
26 September 2016; Journal of Algebraic Combinatorics 45 (2017), 423--454.
[Pinned primary PDF](https://arxiv.org/pdf/1505.05034v2).
Definition 1.6, Theorems 1.7--1.8 and Section 6 supply the explicit
projective finite-valuation-ring baseline. The full-unit affine compression
and its compact-limit Schatten upper bound are inferences proved/explained
in the controls, not results attributed verbatim to Nica.

### DR-SCHATTEN

Julio Delgado and Michael Ruzhansky, *Schatten classes and traces on compact
groups*, arXiv:1303.3914v2, 8 February 2016.
[Primary deposited PDF](https://backoffice.biblio.ugent.be/download/8585438/8585439).
Theorem 3.5, printed page 8, and Remark 3.6 give the compact invariant-operator
symbol criterion. This is established spectral machinery; it does not compute
the thin Bol-section operator's conductor blocks or their multiplicities.

### CUBIC-THETA

Alexander Dunn and Maksym Radziwill, *Bias in cubic Gauss sums: Patterson's
conjecture*, arXiv:2109.07463v3.
[Primary version](https://arxiv.org/pdf/2109.07463v3).
Section 5 supplies the cubic-theta cusp-expansion interface followed in the
quasi-RH source audit. Only that unconditional input is used in the audit;
no GRH-dependent prime asymptotic is imported into our analytic theorem.

### KUBOTA

Tomio Kubota, *Topological covering of SL(2) over a local field*, Journal of
the Mathematical Society of Japan 19 (1967), 114--121.
[Primary PDF](https://www.jstage.jst.go.jp/article/jmath1924/19/1/19_1_114/_pdf).
Pages 114--115: local Hilbert-symbol cocycle and global product-formula
compatibility. This explains an actual missing cubic bridge, rather than
identifying the oscillator double cover with a cubic cover.

### QUASI-RH

*The Quasi Riemann Hypothesis*, September 30, 2026 source in openai/math,
last file revision `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.
[Pinned PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).
PDF blob `8132b77eeb270a70b25df8d6609f008e83e65d91`; inspected TeX blob
`268c4e3206d460c617d3d2129742a72b831b3def`. Proposition 5.1, Corollary 14.1
and Lemma 14.2 are audited with masks, conductor branches and coefficient
independence intact. This is a mechanism comparison, not certification of
the paper's claimed global zero-free theorem.

Further partial-geometric-design, Radon and p-adic symbol-class comparisons,
including the explicitly inaccessible full theorem of Chai--Feng--Zeng,
are documented with their access limits in the controls. The bounded search
does not establish literature-wide priority for our exact thin-group family.

## Collective-pencil comparison sources (2026-11-16)

The [collective cancellation manuscript](manuscripts/bol-collective-cancellation.md)
uses the following established tools and comparisons. The specific marked
Bol-word norm is calculated there; no reference below is asserted to state
that theorem, and the search does not certify historical priority.

### SUBSPACE-FRAMES

Peter G. Casazza and Gitta Kutyniok, *Frames of subspaces*,
arXiv:math/0311384v1, 21 November 2003; Contemporary Mathematics 345 (2004).
[Primary PDF, displaying v1](https://arxiv.org/pdf/math/0311384).
Definition 3.15 and Proposition 3.16, printed page 9, give the weighted
orthogonal-projection frame operator and its bounds. The collective Gram
is a commuting coordinate-projection instance, possibly with a kernel.
The general mechanism is known; the marked pencil's overlap is computed
in the manuscript.

### MACWILLIAMS

Jessie MacWilliams, *A theorem on the distribution of weights in a systematic
code*, Bell System Technical Journal 42 (1963), 79--94.
[Original-paper PDF](https://www.terpconnect.umd.edu/~abarg/ECC/macwilliams1963.pdf).
Lemma 2.7, printed page 88, gives complete-symbol character duality;
Theorem 2.8 specializes it to the Hamming weight enumerator. This is the
source of the weighted subspace-mass transform, not a new identity claimed
by the present work.

### GOW-QUINLAN

Rod Gow and Rachel Quinlan, *On the vanishing of subspaces of alternating
bilinear forms*, Linear and Multilinear Algebra 54 (2006), 415--428.
[Author PDF](https://maths.ucd.ie/~rodgow/alternatingnew.pdf).
Theorem 10 and the paragraph immediately following, printed page 11,
identify the projective radical-line correspondence for an n-dimensional
constant-rank-(n-1) alternating pencil, n odd over a finite field. This
explains why the preliminary unweighted tight-frame proposal was a known
incidence calculation.

### RANK-SUPPORT

Elisa Gorla, Relinde Jurrius, Hiram H. López and Alberto Ravagnani,
*Rank-metric codes and q-polymatroids*, arXiv:1803.10844v4,
5 September 2019; Journal of Algebraic Combinatorics 52 (2020), 1--19.
[Primary version](https://arxiv.org/html/1803.10844v4).
Definitions 2.2, 2.6 and Notation 4.1/Section 4 give generalized weights
and restrictions by row/column support. They supply prior context for
information beyond individual matrix ranks; they do not compute our
reciprocal-weighted image-membership statistic.

### DOUBLE-EXPONENTIAL

John B. Friedlander and Igor E. Shparlinski, *Double exponential sums over
thin sets*, Proceedings of the AMS 129 (2001), 1617--1621,
DOI [10.1090/S0002-9939-00-05921-9](https://doi.org/10.1090/S0002-9939-00-05921-9).
[Original-paper facsimile](https://scispace.com/pdf/double-exponential-sums-over-thin-sets-1pcv5fb9un.pdf).
The Theorem on printed page 1618 bounds scalar double-exponential sums
over arbitrary subsets of the exponent ring. The varying-prime scalar
parameter regime differs from the fixed-prime, growing-block,
vector-pencil norm proved here. The comparison does not claim improvement
of their theorem.

### LINEARIZED-POLYNOMIALS

John Sheekey, *A new family of linear maximum rank distance codes*,
arXiv:1504.01581v2, 7 June 2016; Advances in Mathematics of Communications
10 (2016), 475--488.
[Primary version](https://arxiv.org/pdf/1504.01581v2).
Section 2, printed page 4, the root-count paragraph before Theorem 2,
and Remark 2 on pages 4--5, explain the linearized-polynomial kernel bound
and evaluation on a parameter subspace. This is the established
Moore/Delsarte--Gabidulin mechanism used in the coupled pencil. The
collective manuscript proves its special degree-nine case directly and
does not claim a new rank-metric code construction.

### GALOIS-ALTERNATING

Rod Gow and Rachel Quinlan, *Galois extensions and subspaces of alternating
bilinear forms with special rank properties*, arXiv:0709.0741v1,
5 September 2007.
[Primary version](https://arxiv.org/pdf/0709.0741v1).
Section 2, especially Lemma 1, Corollary 1 and Lemma 2, uses Galois traces
and the perfect trace pairing to construct alternating forms and determine
their radicals. This supplies prior context for trace-valued alternating
families. Our trace-determinant pencil and its exact reciprocal-word norm
are explicitly constructed and proved in the collective manuscript.

## Conductor correspondence sources (2026-11-16)

### HW-SHINTANI

Guy Henniart and Chun-Hui Wang, *Weil representations over finite fields
and Shintani lift*, arXiv:1303.5141v1, 21 March 2013.
[Primary version](https://arxiv.org/pdf/1303.5141).
Lemma 3.1(i), printed page 3, gives the exact isometry for normalized
conjugation-invariant class-function inner products. Theorem 4.1, on the
same page, gives the twisted-character identity for the Jacobi-group
Weil representation with the additive character pulled back by field trace.
Section 4, page 4, gives the Frobenius action in the Schrödinger model.
The connected algebraic-group and class-function hypotheses matter: these
results apply to the scalar Heisenberg quotients, and do not automatically
transport a marked reciprocal Bol word or its selected matrix coefficients.
The conductor manuscript proves its additional kernel and Gram compatibilities
directly. Its literature comparison also uses the exact GH-Q and GH-SR
locators above; it does not assert a new general Shintani theorem.

## Intrinsic associator and representation comparisons (2026-11-16)

### SMITH-QR

Jonathan D. H. Smith, *Four Lectures on Quasigroup Representations*,
Loops '07 lecture notes, Prague, 13--17 August 2007.
[Author PDF](https://jdhsmith.math.iastate.edu/math/4LQR.pdf), inspected
16 November 2026. Sections 2.1.3--2.1.4 describe the association-scheme
framework; Section 3.2 treats Markov actions; Sections 4.2.2--4.2.4,
printed pages 25--27, distinguish universal multiplication groups and
stabilizers and state the module-equivalence theorem. This is established
quasigroup representation theory, not the naive multiplicative map from a
loop to a group ruled out for our family. No claim of inventing quasigroup
representations or their permutation realization is made here.

### SMITH-MARKOV

Jonathan D. H. Smith, *Quasigroup Actions: Markov Chains, Pseudoinverses,
and Linear Representations*, Southeast Asian Bulletin of Mathematics 23
(1999), 719--729.
[Author facsimile](https://jdhsmith.math.iastate.edu/math/QAMCPLR.pdf).
The abstract and Section 1, printed page 719, describe Markov actions from
incidence pseudoinverses and an associated linear representation. This
is prior context for loop-derived Markov operators; the comparison does
not identify it with our uniform associator law or assert a new general
Markov representation theory. Only the stated first-page interface is used.

### BMS-2REP

Severin Bunk, Lukas Müller and Richard J. Szabo, *Geometry and 2-Hilbert
Space for Nonassociative Magnetic Translations*, arXiv:1804.08953v2,
17 January 2019. [Primary PDF](https://arxiv.org/pdf/1804.08953).
The inspected PDF's arXiv header identifies v2. Definitions 4.12 and 4.16
specify higher weak 2-cocycles and weak projective 2-representations;
Theorem 5.7, printed page 23, proves the translation-group construction.
This supplies a materially different categorical architecture whose
coefficient category, action and coherence must actually be constructed.
It is not already a Bol-loop representation theorem, and the ordinary
matrix transport identities in our manuscript do not establish its axioms.

### BL-3COCYCLE

Ioannis Bakas and Dieter Lüst, *3-Cocycles, Non-Associative Star-Products
and the Magnetic Paradigm of R-Flux String Vacua*, arXiv:1309.3172v3,
5 December 2013. [Primary PDF](https://arxiv.org/pdf/1309.3172).
The inspected PDF's arXiv header identifies v3; its typeset title page
separately says 11 October 2018. Sections 3.3 and 4.2 concern group
3-cocycles and nonassociative star-products. These are alternative targets,
not consequences of reassociating products in an associative matrix
algebra. No transfer from that setting to the present Bol family is assumed.

The new manuscript also compares GH-Q and GH-SR at their existing pinned
locators. Ordinary Weyl quantization on a doubled finite abelian phase space
is the implementation tool. The new endpoint is the exact intrinsic
associator spectrum and translated-defect coercivity for the explicit
reciprocal family. This bounded source comparison does not certify
literature-wide priority or a new local metaplectic cover.

## Non-scalar fusion and quantum-channel comparisons (2026-11-16)

The [intertwiner manuscript](manuscripts/bol-nonscalar-intertwiners.md)
rechecks GH-Q, Theorem 2.2.3, Propositions 2.3.1--2.3.2, Section 2.4 and
Propositions 2.7.1, 2.7.3, 2.7.5; SMITH-QR, Section 4.2.4, equations
(4.8)--(4.12); and JS-ACTION, Definition 7.1 and Theorem 6.1. These are
established representation frameworks, not sources asserted to contain the
new reciprocal-loop trace and channel formulas. The BMS-2REP PDF's
Definitions 4.12/4.16, Theorem 5.7 and Remark 5.9 are the comparison
locators; the arXiv HTML conversion has different numbering. Its
[primary accepted manuscript](https://pure.hw.ac.uk/ws/portalfiles/portal/24423231/NMT_final_Rev.pdf)
was also inspected. The bounded comparison does not certify historical priority.

### BST-QE

Avraham Ben-Aroya, Oded Schwartz and Amnon Ta-Shma, *Quantum Expanders:
Motivation and Constructions*, Theory of Computing 6 (2010), 47--79,
DOI [10.4086/toc.2010.v006a003](https://doi.org/10.4086/toc.2010.v006a003).
[Author PDF](https://www.cs.tau.ac.il/~amnon/Papers/BST.TOC08.pdf).
Definitions 1.1--1.2, printed pages 48--49, specify mixed-unitary channels
and contraction on trace-zero Hilbert--Schmidt space. The introduction,
printed pages 50--51, distinguishes a degenerate direct classical lift
from constructions addressing quantum coherences, and Section 4 supplies
explicit constant-degree constructions. This is the general baseline;
our exact loop-selected channel makes no degree/circuit improvement claim.

### HASTINGS-QE

Matthew B. Hastings, *Random Unitaries Give Quantum Expanders*,
arXiv:0706.0556v1, 5 June 2007; Physical Review A 76 (2007), 032315,
DOI [10.1103/PhysRevA.76.032315](https://doi.org/10.1103/PhysRevA.76.032315).
[Primary version](https://arxiv.org/pdf/0706.0556v1).
The opening discussion and equations (1)--(2), printed pages 1--2, define unitary-conjugation
channels, the spectral-gap target and the low-degree requirement. The
random-unitary construction is prior quantum-expander theory, not a result
being improved by our dense average over actual Bol defects.

