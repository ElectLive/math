# Intrinsic and analytic Bol results: public proof package

This package makes the scientific sources, dependencies, review records, and executable checks public. Begin with the [self-contained construction and nonisomorphism writeup](../INTRINSIC_NONISOMORPHISM.md). These are results about explicit reciprocal Bol families; they do not complete the classification of finite simple Bol loops.

## Results and exact scope

| Claim | Source | What is established | What is not established |
|---|---|---|---|
| [0079](../claims/0079.md): intrinsic separation | [Spectral manuscript](manuscripts/bol-intrinsic-spectral-separation.md) | Every spread/aligned pair at the same h is nonisomorphic as unmarked loops; exact multiplicities and all positive trace moments differ | Within-family classification, isotopy separation, simplicity, efficient sampling, or a better worst-case norm |
| [0080](../claims/0080.md): non-scalar operator framework | [Intertwiners manuscript](manuscripts/bol-nonscalar-intertwiners.md) | Compatible residual fusion, exact decoupling obstruction, intrinsic joint trace, and two-rate matrix mixing on nondegenerate sectors | General loop representation theory, fast mixing on degenerate sectors, efficient quantum implementation, or improvement over general quantum expanders |
| [0081](../claims/0081.md): local arithmetic transfer | [Transfer manuscript](manuscripts/bol-action-compatible-transfer.md) | A specified arithmetic subloop quotient preserves actual sections/full defects; faithful induction retains upper actions; sharp quotient-kernel decay | An unrestricted quotient of the full upper loop, a full induced-space mixing gap, automorphy, Euler products, or global arithmetic consequences |

The matrix-channel theorem and the degenerate spread/aligned trace comparison concern different hypotheses. Their conclusions cannot simply be combined into a stronger mixing theorem for the spread/aligned pair.

## Source pins and mirror policy

The source repository is `Mira-Cult/math-wip`, under `problems/0323-finite-simple-non-moufang-bol-loops/`. All substantive sources are included here, so access to that private workspace is not needed to read the proofs.

- Intrinsic spectral separation scientific revision: `bb49ab24465ef82be78f2a0d9cb8d0af8caa2695`; reviewed delivery: `848d6640a7bc555c9d2814665e7ac990fdfbeef5`.
- Non-scalar intertwiners scientific revision: `ec122a2a890971141caf960dd27fdb50fed77154`; reviewed delivery: `59d77073b15a25fb2cf6915a602836be68e2c93f`.
- Action-compatible transfer scientific revision: `7beda2ab63be24ff1cca9e2a7d5407f85d71bdda`; reviewed delivery: `b68132b0892afed04f99b10176aee6385d219402`.

The shared associator and collective manuscripts are copied from the spectral scientific revision. The conductor correspondence is copied from the transfer scientific revision. Other preparatory manuscripts come from the spectral scientific revision. The references file and non-scalar review files come from its delivery revision; the metaplectic review and overview come from the spectral delivery; transfer review and shared code guide come from its delivery. Shared verifiers are taken from the transfer delivery; non-scalar verifiers from the non-scalar delivery; intrinsic verifiers from the spectral delivery. A manifest records the public file hashes. Terminal newlines may be normalized by the export; no scientific text or algorithm was intentionally changed.

The original code guide retains its source-workspace commands. In this public package, run the same basenames under `analytic-2026-11-16/code/` from the parent directory. The non-scalar programs are `verify_bol_nonscalar_fusion.py`, `verify_bol_nonscalar_orbits.py`, `verify_bol_nonscalar_quantum.py`, and `verify_bol_nonscalar_independent.py`.

## Review and validation, 2026-11-16

- The original independent **model** reviews are preserved in [spectral evidence](evidence/bol-metaplectic-review.md), [non-scalar evidence](evidence/bol-nonscalar-review.md), and [transfer evidence](evidence/bol-action-transfer-review.md).
- A fresh [targeted publication audit](evidence/intrinsic-publication-audit.md) found no error in the checked nonisomorphism proof, spectral aggregation and collective corollaries. Both intrinsic verifiers passed again. This audit uses the earlier AQ spectral derivation and is not a fresh audit of every earlier foundation or of the new claims in PRs 441/442.
- **PR440 complete-checkout repository validation:** at `848d6640a7bc555c9d2814665e7ac990fdfbeef5`, Python 3.12.13 `python check.py` passed all 115 tests, exit 0, in a clean full checkout with sparse checkout disabled (5682 tracked files). The CI-style run with `--base 4ded8c4fb264235370a745100755a26a372918ba` also passed all 115 tests.
- **PR442 complete-checkout repository validation:** at `b68132b0892afed04f99b10176aee6385d219402`, both plain `python check.py` and the CI-style check with `--base 848d6640a7bc555c9d2814665e7ac990fdfbeef5` passed all 115 tests, exit 0, in a clean full checkout.
- These successful local complete-checkout runs resolve the earlier sparse-checkout validation limitation for those exact revisions. They do not change the historical GitHub Actions outcomes: the remote jobs were **skipped**, not passed. Nor are repository-integrity tests proofs of the mathematical theorems.
- PR441's submitted report records 115 passing local integrity tests and a skipped remote run. This publication audit did not independently repeat its repository-wide run.

No external human peer review, formal proof verification, or literature-wide novelty certification is claimed. The new public note and evidence are meant to enable that scrutiny. GitHub's hosted mathematical rendering has not been visually audited in this publication pass.

## Open questions

1. Does the unfiltered translated-defect walk have a provable higher-moment collective separation? The one-step trace does not determine its second moment.
2. What is the full stationary algebra in degenerate matrix sectors? Can a sparse, implementable channel preserve a useful two-rate guarantee with a fair resource advantage?
3. Can an explicit upper-actor average connect induced cosets and control the additional fixed modes? The lifted lower distribution has centered norm one on the whole induced space.

These are research targets, not consequences of the three completed local results.
