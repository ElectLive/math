# Graded Bol continuation: exact-source review and verification



## Exact scientific source

The first graded scientific source was published at
`5bdbd5730b6ddfc4ca7e92da0ab2f2bbcb5fb005`.
The clarification source `9d0a75e12ec05bb532894cc78688d322d3e08a15` changed an
output-field label, review-status wording, introductory integrality scope and
bibliographic version pins, without changing proofs or numerical algorithms.

The strengthened scientific source is
[`a1d4387173169caf7c84b6062475345d7d4826e5`](https://github.com/Mira-Cult/math-wip/commit/a1d4387173169caf7c84b6062475345d7d4826e5),
tree `64b289da9376f2012495cafc9138261f3cd60fea`. It adds CF8, its two controls,
the corresponding exact calculations, and explicit genericity boundaries.
All three source commits and their complete trees are available in the owner's
local Git object database. The later delivery commit changes review/evidence
and overview status only; the scientific source remains the named revision.

## Actual independent mathematical reviews

Four model reviewers were used. Authors and construction participants are
excluded from independent credit on their own contributions. These are model
reviews, not human review, formal certification or a novelty determination.

| Reviewer | Independently accepted scope | Exact source |
| --- | --- | --- |
| model participant 2 | CF1--CF8, F-A--F-G, root's verification implementation and overview consistency; excludes own architecture audit and F-H contribution | `a1d4387173169caf7c84b6062475345d7d4826e5`, after full original review, inspection of both successive diffs, and a new exact-script execution |
| model participant 4 | F-A--F-H, architecture obstructions and equal-rank controls, root's implementation; excludes authored/coauthored CF1--CF8 | `a1d4387173169caf7c84b6062475345d7d4826e5`, after full original review and inspection of both successive diffs; final code additions statically checked, not rerun by this reviewer |
| model participant 3 | CF1--CF8, A1/A2 and the equal-rank/control calculations, root's verification implementation and summary boundaries; excludes authored F proofs and their downstream restatements | `a1d4387173169caf7c84b6062475345d7d4826e5`, including complete successive diffs and a new exact-script execution |
| model participant 1 | F-F--F-H, CF2/CF3/CF7 dependencies, CF8 and both added controls, analytic trace dependencies, equal-rank comparison, complete amended implementation and summaries | `a1d4387173169caf7c84b6062475345d7d4826e5`, after exact-source review of both earlier revisions and the complete strengthening diff |

The literature reviewer supplied the prepublication intersection/valuation
observation in F-H. Their check of that proposition is explicitly a participant
check, not independent acceptance. The coordinate reviewer and the fresh
`graded_independent_audit` reviewer supplied the independent F-H reviews.
The root proposed the fusion-projector strengthening and CF8 and authored the
new verification script; root's checks are not counted as independent reviews
of those contributions. The CF8 manuscript credits its root/coordinate
construction and proof development.

The reviewers rederived the intrinsic subgroup, class Fourier bases, true
right-charge modules, left/right induction formulas, cocycle and norm words,
huge symbolic fixed counts, CAR signs, discriminant products, augmentation
determinant and coefficient extraction, and stabilizer-count reconstruction.
They checked that the operator identity and the product-of-functions identity
have separate proofs. CF8 reviewers checked the exact submodular defect,
equality condition, zero-charge convention, basis-dependent image versus
basis-independent trace, all 51-point counts, and the separate ratio-3/4
finite-set counterexample.

No mathematical correction was requested. The requested labeling and review
scope clarifications are included in `9d0a75e...`. A fresh review pointed out
that the channel law and stabilizer-count reconstruction apply to general
finite abelian actions. That generality is now explicit. The resulting CF8
strengthening adds necessary elementary-bilinear restrictions that arbitrary
Z-sets can fail; it does not claim sufficient realizability or a uniquely Bol
analytic recursion.

## Input provenance and inherited assumptions

Reviewers inspected the pinned class-two equations, positive-cocycle condition,
strict isomorphism equation (15), rigid data, principal-isotope shift and
generator rigidity. Simplicity/properness, the canonical-folder and isotope
interfaces, and the full upstream classification remain imported dependencies.
These reviews do not certify every upstream proof or its review history.

Root freshly fetched the two input texts at
`2a25b81e3efe5bdd8a3923e27c94aef16a559094`. The supplied intake snapshots match
their full contents apart from an extra saved final blank line. The literature
reviewer independently compared the resulting text snapshots. Their SHA-256
values are `64e74f00c5fbafeca2b993a76c4585e578ef51f66a08b0a7c76026d603000c2b`
(class-two classification) and
`35b2e05c014a583f092e7b4c679e20f12da3ef917e0c0e3c1d994f0a2e04ca`
(rigid-center construction). This is a pinned-text comparison, not a local
object audit or fresh proof review of the entire upstream commit.

## Reproducible exact execution

Runtime: **Python 3.12.14**, standard library only, assertions enabled.
Run from the reviewed checkout:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_graded_fusion.py
python check.py
```

The new script at `a1d4387173169caf7c84b6062475345d7d4826e5` has SHA-256
`45f9f7bb52fb7129e174ac88de702fc3fde2ab5ef654b69e848779c4a023587f`.
Root read and ran it successfully. The literature reviewer, modular reviewer
and fresh independent reviewer each read the full committed script and
independently executed exact `git show` bytes at that source; all reported
successful execution and `PASS`.
The three original reviewers also ran the earlier exact script at `5bdbd573...`.

| Certificate component | Exact final evidence |
| --- | --- |
| Reduced rigid class seed | 363 classes; an independent BCH conjugation-orbit construction agrees with the commutator-coset construction |
| Auxiliary induction | 3267 points; left norm-word fixed counts 792/576, right phase counts 2376/1728; cocycle and involution identities checked |
| Genuine charge sectors | All 27 right charges projected exactly over Q(zeta_3) through degree 3; dimensions integral/nonnegative and degree-two charge convolution checked |
| Central-class reconstruction | All 28 center subspaces; four nonzero orbit types recovered by Möbius inversion and checked against actual commutator-image strata |
| Joint channel and rank laws | 19,683 binary/triple support identities; 784 charge-subspace inequality and prime-power-defect checks |
| Same-rank controls | 801 classes each; all central cycle profiles agree; all 48 independent ordered character pairs have fusion dimensions 9 versus 1 |
| Fusion trace coefficients | 37800/38376 for the 801-class comparison; 2376/2304 for the 51-point comparison |
| 51-point obstruction | Actual coset-orbit enumeration of the alternative Z-set; every separate character and central cycle profile agrees, but joint dimensions 1/2 exclude the alternative from elementary class-two realization |
| Actual finite exterior currents | 2560 exact cyclotomic commutator checks on all 512 exterior basis states in the stated 3-point, 3-mode model |

The fusion-trace coefficient calculation uses the proved finite spectrum; it
does not independently construct every projector matrix. The separate
three-orbit ratio-3/4 control is proved and reviewed symbolically, not claimed
as a separate executed certificate. The small rigid model replaces F_(3^18)
by F3 and uses Z semidirect C9 for induction; it is not a construction of the
huge simple loop. The 801- and 51-point comparisons are class-two group or
finite-set controls, not newly asserted simple Bol examples.

Root's final source integrity run passed **115 tests**; these check repository
integrity, not mathematics. The source Markdown check found no missing file
or heading targets among **60** local links in the continuation sources.
The source's GitHub queries returned no workflow runs and zero commit statuses;
the aggregate status was pending. No remote CI pass is claimed. Raw logs,
downloaded PDFs and generated output are not committed.

## Handoff boundary

The result is a coupled graded construction from a canonical finite Bol seed:
faithful sandwich action, actual phase sectors, integral modular isotope
traces, multiplication currents, fusion-projector traces, central-class
reconstruction and necessary joint-rank constraints. The generic finite-set,
CAR and discriminant mechanisms are credited. Full-loop reconstruction,
historical priority, a VOA, a denominator identity, genus-zero moonshine and
arbitrary-current modularity remain unproved. The next bounded mathematical
question is the closed genus-one correlation system specified in the overview.
