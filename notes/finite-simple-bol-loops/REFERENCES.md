# References for the Bol-loop classification programme

A shared reading list for human researchers and the AI systems they use. **A useful reference is a contribution in its own right.** If you know a paper, book chapter, thesis, erratum, lecture note, dataset or implementation that belongs here, open an issue or a small pull request. A link and a sentence about its relevance are enough; you do not need to undertake a literature review or resolve a project question.

This is a curated starting list, not an exhaustive bibliography or a certification of priority. Sources below are external literature and tools; our own proposed results are separated at the end. Inclusion does not validate every statement in a source or every use we make of it.

## Reading routes

- **Start with simple proper Bol loops:** Nagy's construction and remarks papers, then the exponent-two family.
- **Understand the Bruck branch:** Aschbacher–Kinyon–Phillips and Baumeister–Stein–Stroth / Baumeister–Stein.
- **Follow the radical-free branch:** exact factorization literature, then the PSL₂ subgroup reference.
- **Check computations or find examples:** GAP, LOOPS and ATLAS.
- **Review a particular project theorem:** use its manuscript's exact version and theorem locators, not this short annotation alone.

## Simple loops, constructions and historical questions

| Source | Why it belongs here |
| --- | --- |
| G. P. Nagy, [*A class of simple proper Bol loops*](https://arxiv.org/abs/math/0703919v1), preprint 2007; *Manuscripta Mathematica* 127 (2008), 81–88. | Exact-factorization constructions and finite simple non-Moufang examples. A central baseline for the programme. |
| G. P. Nagy, [*Some remarks on simple Bol loops*](https://cmuc.karlin.mff.cuni.cz/pdf/cmuc0802/nagy.pdf), *Commentationes Mathematicae Universitatis Carolinae* 49 (2008), 259–270. | Folders, constructions and explicit research questions. §6, Problem 1 is the question about a simple proper loop that is neither a G-loop nor isotopic to a Bruck loop. |
| G. P. Nagy, [*A class of finite simple Bol loops of exponent 2*](https://arxiv.org/abs/0709.4544v1), preprint 2007; *Transactions AMS* 361 (2009), 5331–5343. | Infinite exponent-two family with an elementary-abelian extension of S₅ as its right multiplication group. Translate right/left conventions explicitly. |
| M. W. Liebeck, [*The classification of finite simple Moufang loops*](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/classification-of-finite-simple-moufang-loops/02FBE39338FC77C639059653939B48F4), *Mathematical Proceedings of the Cambridge Philosophical Society* 102 (1987), 33–47. | The classified Moufang baseline, using Paige's simple loops. Publisher metadata/extract available; full-text access may be restricted. |
| K. W. Johnson and J. D. H. Smith, [*On the smallest simple, unipotent Bol loop*](https://jdhsmith.math.iastate.edu/math/BolBoolf.pdf), *Journal of Combinatorial Theory, Series A* 117 (2010), 959–969. | Explicit combinatorial and geometric description of the smallest simple unipotent example; a different perspective from abstract group constructions. |
| M. K. Kinyon, G. P. Nagy and P. Vojtěchovský, [*Bol loops and Bruck loops of order pq*](https://arxiv.org/abs/1611.05785v3), *Journal of Algebra* 473 (2017), 481–512. | A precise small-order classification, with structural and isotopy information. |
| A. Grishkov, M. Kinyon and P. Vojtěchovský, [*Bol loops of order 27*](https://arxiv.org/abs/2504.14646v2), preprint, revised September 2025. | Theory plus computation classifying the 15 loops, including five groups; useful as an example of reproducible bounded classification. |

Classical background also includes A. A. Albert, *Quasigroups. I* (1943); L. J. Paige, *A class of simple Moufang loops* (1956); R. H. Bruck, *A Survey of Binary Systems* (1958); and D. A. Robinson, *Bol loops* (1966). Reliable open copies, theorem locators and helpful introductory references would be welcome additions.

## Bruck loops and twisted subgroups

| Source | Why it belongs here |
| --- | --- |
| M. Aschbacher, M. K. Kinyon and J. D. Phillips, [*Finite Bruck loops*](https://authors.library.caltech.edu/records/c4adw-9py07), *Transactions AMS* 358 (2006), 3061–3075. | Structural decomposition and the group-theoretic approach to finite Bruck loops. Institutional record includes a published copy. |
| B. Baumeister, A. Stein and G. Stroth, [*On Bruck loops of 2-power exponent*](https://arxiv.org/abs/0908.2596v2), *Journal of Algebra* 327 (2011), 316–336. | Envelope structure and the simple-group inputs behind the two-power branch. Its assumptions and companion results matter. |
| B. Baumeister and A. Stein, [*The finite Bruck loops*](https://arxiv.org/abs/0908.2597v2), *Journal of Algebra* 330 (2011), 206–220. | Structural results used by the Bruck-envelope reductions. Read the envelope hypotheses, not only the quotient description. |
| T. Foguel, M. K. Kinyon and J. D. Phillips, [*On twisted subgroups and Bol loops of odd order*](https://arxiv.org/abs/math/0208231v2), *Rocky Mountain Journal of Mathematics* 36 (2006), 183–212. | Twisted-subgroup machinery and odd-order loop questions. Pin the version and inspect each imported statement: the preprint revision itself notes corrections, and our manuscripts retain statement-specific dependency cautions rather than treating the whole source as a blanket guarantee. |

Glauberman's *On loops of odd order. I, II* (1964, 1968) is foundational background for the odd-order Bruck branch. Suggestions of accessible editions and precise locators are particularly useful.

## Group factorizations, affine structure and permutation methods

| Source | Why it belongs here |
| --- | --- |
| C. H. Li, L. Wang and B. Xia, [*The exact factorizations of almost simple groups*](https://arxiv.org/abs/2012.09551v6), *Journal of the London Mathematical Society* 108 (2023), 1417–1447; linked preprint revised 2024. | Exact-factorization input. Distinguish the journal article from later preprint revisions and record the actual version used. |
| T. C. Burness and C. H. Li, [*On solvable factors of almost simple groups*](https://arxiv.org/abs/1910.00644v2), *Advances in Mathematics* 377 (2021), 107499. | Solvable factors and exact factorizations with a solvable factor. |
| T. Feng, C. H. Li, C. Li, L. Wang, B. Xia and H. Zou, [*A complete classification of solvable factors of almost simple groups*](https://arxiv.org/abs/2407.12416v2), preprint revised August 2025. | Later development of the factorization programme. Compare precise scope with earlier papers rather than assuming their classifications are interchangeable. |
| R. M. Guralnick and M. E. Zieve, [*Polynomials with PSL(2) monodromy*](https://annals.math.princeton.edu/2010/172-2/p11), *Annals of Mathematics* 172 (2010), 1315–1359. | Appendix A provides subgroup, normalizer and automorphism facts used in the paired-PSL₂ work. |
| A. Caranti, F. Dalla Volta and M. Sala, [*Abelian regular subgroups of the affine group and radical rings*](https://arxiv.org/abs/math/0510166v2), *Publicationes Mathematicae Debrecen* 69 (2006), 297–308. | A bridge between regular affine subgroups and algebra structures. The abelian hypothesis is essential to its scope. |
| A. Maróti, [*On the orders of primitive groups*](https://www.renyi.hu/~maroti/primitive.pdf), *Journal of Algebra* 258 (2002), 631–640. | Permutation-group order bounds used in primitive-action arguments. The linked author version is dated February 2002; record its locators separately from journal pagination. |

Further foundations include Dixon–Mortimer's *Permutation Groups* and Liebeck–Praeger–Saxl's work on O'Nan–Scott types, maximal factorizations and regular subgroups. The [SD dependency map](SD_DEPENDENCIES.md) identifies where additional family-specific proof inputs are still needed in the public packet.

## Computational resources

- [GAP reference manual](https://docs.gap-system.org/doc/ref/chap39_mj.html): group algorithms and their documented interfaces. Record the actual GAP version, package versions, inputs and commands for every certificate.
- [LOOPS](https://gap-packages.github.io/loops/), by G. P. Nagy and P. Vojtěchovský: quasigroup/loop computation and libraries in GAP. Follow the package's citation guidance.
- [ATLAS of Finite Group Representations](https://brauer.maths.qmul.ac.uk/Atlas/): group representations and finite-group data. Cite the particular group page and data version; honor its completeness and verification warnings.

## Project manuscripts are separate evidence

Our [results catalogue](RESULTS.md) and [verification policy](VERIFICATION.md) describe the project's own claims and their review status. They are not additions to the established literature merely because they are public. Model review, computational reproduction, human refereeing, and formal proof checking are distinct.

## How to contribute a reference

An issue or pull request can be as small as:

- Author, title and a stable URL, DOI or bibliographic citation.
- One sentence saying which construction, question or method it concerns.
- Optionally, a theorem/page locator, version, convention difference, erratum, or better open-access copy.

References to earlier examples, related approaches, contrary results and overlooked terminology are all welcome. You need not demonstrate overlap or adjudicate novelty. We will integrate useful pointers into this list and the relevant manuscript dependencies.

For AI-assisted research, read the actual cited statement before using it, retain its hypotheses and version, and mark inaccessible or unchecked sources. A bibliography entry is a route to evidence, not a substitute for it.

*Bibliography assembled 16 November 2026. Linked landing pages or documents were checked during this pass; this was not a full proof audit. The classical background items without links are reading leads whose accessible editions remain to be added.*


## Quantum randomization and implementation

These primary-source locators support the matched-norm comparison in
[Section 8 of the randomization manuscript](analytic-2026-11-16/manuscripts/bol-quantum-randomization.md#8-benchmarks-in-matched-criteria).
The versions and theorem locators below delimit that comparison; current-source
checking is distinct from a literature-wide novelty audit.

| Source | Version and locator | Use and scope |
| --- | --- | --- |
| P. A. Dickinson and A. Nayak, *Approximate Randomization of Quantum States With Fewer Bits of Key* | [Author PDF](https://www.math.uwaterloo.ca/~anayak/papers/DickinsonN06.pdf), 1 June 2006, Theorems 1.2/1.4, Section 2 and Appendix B, Proposition B.1 | Explicit qubit Pauli state randomization, a random-sampling benchmark and the standard Alon--Goldreich--Hastad--Peralta blocked-coordinate small-bias construction. Trace-norm state security is distinct from diamond-norm security. |
| A. Ben-Aroya, O. Schwartz and A. Ta-Shma, *Quantum Expanders: Motivation and Constructions* | [Theory of Computing 6 (2010), 47--79](https://theoryofcomputing.org/articles/v006a003/), Theorem 4.6; DOI 10.4086/toc.2010.v006a003 | Explicit constant-degree quantum expanders with efficient circuits in the stated dimensions; not a constant-depth theorem. |
| A. Anshu, S. Balasubramanian, J. Haferkamp, A. W. Harrow and X. Tan, *Depth-1 expanders on the unitary group and applications* | [arXiv:2609.01605v1](https://arxiv.org/abs/2609.01605v1), 1 September 2026, Theorem 2.2 | Sixteen depth-one Pauli/CNOT choices in the stated qubit dimensions, with a constant Hilbert--Schmidt gap. The full primary manuscript was inspected through an [arXiv mirror](https://arxiv.cnoctave.top/pdf/2609.01605) after the official PDF endpoint failed. Periodic bounded range is not strict nearest-neighbor depth one. |
| V. Iyer, S. Jain, S. Jordan and R. D. Somma, *Efficient quantum circuits for high-dimensional representations of SU(n) and Ramanujan quantum expanders* | [arXiv:2602.15180v1](https://arxiv.org/html/2602.15180v1), 16 February 2026, Theorem 1.1, Corollary 1.2, Sections 1.1/6.1, Algorithm 1, equation (92) and Appendix C | An efficient degree-six expander in every logical dimension. The comparison charges the oscillator encoding, ancillary registers, angle preprocessing, per-use circuit precision and accumulated channel error; the spectral rate alone is not the implementation cost. |
| S. Jain, *Ramanujan quantum expanders from the Weil representation* | [arXiv:2609.38075v1](https://arxiv.org/html/2609.38075v1), 29 September 2026, Theorems D.1/E.1 and Section E.1 | Expander circuits on specified odd logical subspaces; the input-subspace promise is part of the operation model. |
| C. Lancien, *Optimal quantum (tensor product) expanders from unitary designs* | [arXiv:2409.17971v3](https://arxiv.org/html/2409.17971v3), 19 February 2026, Corollaries 2.5/3.5; IMRN 2026, rnaf383 | Sampling from exact designs yields first-moment or tensor-product expanders in induced Hilbert--Schmidt norm; design-sampler costs remain part of the implementation. |
| V. Shoup, *New Algorithms for Finding Irreducible Polynomials over Finite Fields* | [Author PDF](https://www.shoup.net/papers/detirred.pdf), Mathematics of Computation 54 (1990), 435--447, Theorem 3.2; DOI 10.1090/S0025-5718-1990-0993933-0 | Deterministic polynomial-time irreducible-polynomial construction in fixed characteristic. The theorem was checked on rendered PDF page 3 because text extraction was corrupt. |
| J. A. Tropp, *User-Friendly Tail Bounds for Sums of Random Matrices* | [arXiv:1004.4389v7](https://arxiv.org/abs/1004.4389v7), 15 June 2011, Theorem 1.3; Foundations of Computational Mathematics 12 (2012), 389--434 | Matrix concentration supplies a sparse-channel existence benchmark, not an explicit efficient sample or certification algorithm. |
| C. M. Dawson and M. A. Nielsen, *The Solovay--Kitaev algorithm* | [arXiv:quant-ph/0505030v2](https://arxiv.org/abs/quant-ph/0505030v2), 23 August 2005, Sections 2--3; Quantum Information and Computation 6 (2006), 81--95 | Conservative finite-gate compilation bounds for the encoded qudit operations; exact qubit implementation is not assumed. |

The exact Weyl twirl, the phase-randomization/permutation control, and the
state/Choi rank lower bounds are proved directly in the randomization
manuscript. Qubit-only constructions are not silently padded to the odd
logical dimension of the reciprocal family.
