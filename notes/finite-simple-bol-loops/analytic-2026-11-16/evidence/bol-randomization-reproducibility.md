# Quantum randomization: reproducibility and review

Mira Cult

## Scientific revision and public scope

The canonical [theorem-and-proof manuscript](../manuscripts/bol-quantum-randomization.md)
is exported from `Mira-Cult/math-wip`, scientific revision
`f6f415a5b05ce38b51adc9d2894c9795af500b3e`, under
`problems/0323-finite-simple-non-moufang-bol-loops/`.
The public export replaces the opening provenance paragraph and its
reproducibility links, and changes 18 operator-name display macros to upright
roman text because GitHub rejects the original macro. The mathematical content
is unchanged; the recorded inverse restores the exact reviewed manuscript.
Both new programs are copied byte for byte. Authorship is Mira Cult.

The starting non-scalar scientific source is
`ec122a2a890971141caf960dd27fdb50fed77154`, with reviewed delivery
`59d77073b15a25fb2cf6915a602836be68e2c93f`.
The [non-scalar manuscript](../manuscripts/bol-nonscalar-intertwiners.md),
[associator dependency](../manuscripts/bol-associator-quantization.md) and
[earlier non-scalar review](bol-nonscalar-review.md) are already public in this
package. That earlier review does not cover the new randomization results.
The [local claim record](../../claims/quantum-randomization.md) uses local
theorem and QR equation labels without a permanent numeric allocation.

## Review status

Two noncontributing model reviewers accepted the exact scientific revision
`f6f415a5b05ce38b51adc9d2894c9795af500b3e` within their respective mathematical
and resource/comparison scopes. Both report no remaining blocker in those
remits. Their full signed reports, including the initial audits and exact-revision
addenda, are included in full. The mathematical report has three analogous
display-only macro substitutions; the resource report is copied verbatim.
The exact original mathematical report remains publicly accessible in the
[first export](https://github.com/Mira-Cult/math/blob/922ec370f033dd02f1f90d1d0cf6a6040253df72/notes/finite-simple-bol-loops/analytic-2026-11-16/evidence/bol-randomization-independent-math-review.md).
The hashes below identify the original reports accepted into the research record:

| Review | Full report SHA-256 | Scope |
| --- | --- | --- |
| [Independent mathematical review](bol-randomization-independent-math-review.md) | `53a72cf809c47713f06c6a5738bc82b59723272e6c012fcfbb0d89d52e343fb5` | The theorem family, normalizations, exceptional sectors, obstructions, sparse construction, purity and second moments; revised checkers independently replayed. |
| [Independent resource and comparison review](bol-randomization-independent-resource-review.md) | `e3469d49426a56af2946c0bc6152a2d5f812d9cf7bb3aafd46e5758d220a872c` | Error criteria, sampling, gates, precision and primary-source comparisons; revised checkers independently replayed. |

The reviewed source manuscript SHA-256 is
`fd219c96216b5b0ad43dafc08a74f131c088b173529d89cd49ba49f36dc465f7`.
The old NI/AQ dependencies are unchanged at the revised source. Review scope,
finite execution and general proofs are distinct. These reports are not
external human peer review, formal verification, physical circuit validation
or a literature-wide novelty audit.

The dense nondegenerate-sector theorem does not apply to degenerate
spread/aligned sectors. The sharp native threshold concerns the common
commutant, not a quantitative gap. Trace error and diamond error differ.
The efficient repairs have a matching Weyl/actor control with identical
physical resources; no general Bol-specific efficiency advantage is established.

## Exact executable checks

From the public repository root, using Python 3.12.14 and the standard library:

```bash
python notes/finite-simple-bol-loops/analytic-2026-11-16/code/verify_bol_randomization.py
python notes/finite-simple-bol-loops/analytic-2026-11-16/code/verify_bol_small_bias.py
```

Both public program copies also passed in a separate root replay, exit zero
with empty stderr and the identical stdout hashes below. Both revised programs
passed in the recorded source runs and in both independent
reviewers' replays of the exact scientific revision. They use exact
integer/rational/finite-field arithmetic, take no input and print deterministic
JSON. The revised independent outputs agree with the recorded source runs. These hashes
identify the exact source files and complete recorded stdout.

| File | Source SHA-256 | Recorded stdout SHA-256 |
| --- | --- | --- |
| [verify_bol_randomization.py](../code/verify_bol_randomization.py) | `1bfd231605751f5d091466dbd5557285dd79a2bb8daba6b5542a268fe8928425` | `6032535acfa0f4b41f4411e1880726e100b2d7735d48926872111c1d1e8c2afe` |
| [verify_bol_small_bias.py](../code/verify_bol_small_bias.py) | `7e542e411b57da30d370f8eee1e6b940372c3bdefaed3fbadd0195de91f58326` | `dd32bb4ad062ffd5e383240dbc6b8355fedd542fcd1e75eb38f7271e5f211960` |

The channel checker verifies the F729 presentation and order-seven actor;
800 direct conjugations; 160 fixed-pair conjugations; 100 actual shears;
214 prescribed defects and 216 complete requested Weyl-coset realizations;
531,441 scalar field-pair labels and 49 scalar ring-pair labels; all 2,401
ring Weyls; 300 degenerate covariances; 112 common-commutant witnesses; and
all 400 Lagrangian planes in F7^4, including eight purity-equality cases.
The exact dense minorization check includes 36,288 conditional ring terms,
49 field-coefficient pairs and 768 field trace-rank tests. Its seven-point
population-orbit example is a toy model, not the large reciprocal loop.
The separate fused-conjugate-sector diagnostic checks all 2,401 matrix entries
and 117,649 Gram terms for the 49-dimensional ring factor, establishing the
exact finite identity $`A^*A=I_{49}/49`$ for its chosen representatives.

The small-bias checker exhausts five cases over F3, F9 and F27, totaling
1,629 sampler seeds and 904 nonzero additive characters. It checks nine resource
cases for both Theorem S and the independent-round construction from Theorem P.
The sampler uses the standard AGHP blocked-coordinate construction, as presented
in DN Appendix B, Proposition B.1. It does not implement or benchmark the cited general
Shoup preprocessing algorithm. The actual input dimension is already
26,040,609 at n=2; neither checker constructs its full superoperator or
exhausts the large loop. The written proofs establish the general claims.

## Repository and publication validation

At the revised scientific source
`f6f415a5b05ce38b51adc9d2894c9795af500b3e`,
`python check.py --base 59d77073b15a25fb2cf6915a602836be68e2c93f`
passed all 115 repository-integrity tests, exit zero. Its complete log SHA-256 is
`ce2950a90e22d4c72a7d54aefe8171e8d645f503003c81f59836baadb929e8a0`.
This validates repository integrity, not the mathematical theorems.
The separate [GitHub Actions integrity job](https://github.com/Mira-Cult/math-wip/actions/runs/43897845414/job/133406153872)
for this scientific revision was **skipped**, not passed (check run
`133406153872`, workflow run `43897845414`). The successful local 115-test
run does not change that remote conclusion.

This export was prepared against public base
`a8c0fbcc23f3eebdc835cb6294aef5259cfd74a3` and reuses its existing proof
dependencies. The theorem/proof preservation and program hashes are checked
separately from scientific review. Hosted rendering and final public revision
are pending publication; this record does not claim they have been checked.
