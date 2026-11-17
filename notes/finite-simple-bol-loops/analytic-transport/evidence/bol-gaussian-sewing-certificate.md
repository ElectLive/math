# Exact finite Gaussian sewing certificate

Author execution by model participant 2, 2026-11-16, for
[Charged Gaussian sewing, separated points, and zero modes](../manuscripts/bol-charged-gaussian-sewing.md).
This record is finite validation, not an independent review or a proof of
the analytic statements. The exact scientific source pin is to be supplied
by the continuation's review record after publication.

## Reproduction and result

From the repository root, with Python 3.12.14 and assertions enabled:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_gaussian_sewing.py
```

The standard-library script exited with code zero and returned `PASS`.
Its complete output is [bol-gaussian-sewing-certificate.json](bol-gaussian-sewing-certificate.json).
Script SHA-256:

```text
363bc9ccc60635259f44c516b14d8c3208e2cf8b81e5006c0f1f4bb01ef9935d
```

All arithmetic uses exact rational numbers and exterior-algebra
coefficient extraction for the manuscript's bipartite incoming--outgoing
quadratic propagators. The executed checks were:

- Four invertible source formulas, comparing direct Berezin integration
  with the determinant/inverse expression.
- Four members of the singular family `diag(a,0)`, including the rank
  jump at `a=0`, and one nondiagonal singular matrix.
- Three contraction orders for an assembled invertible matrix whose
  first proposed scalar pivot is singular.
- One nontrivial Schur-complement identity, with effective matrix
  `[[6,1],[1,0]]`, checked as a full source polynomial.
- Seventeen bordered-determinant covariance checks, including the
  zero-mode saturation condition, null-block anomaly cancellation,
  scaling by weight `n-h`, and transport of a two-dimensional zero basis.
- The elementary non-Gaussian diagnostic: a nonzero quartic source
  coefficient with every quadratic coefficient zero.

## Limits

These instances check signs and concrete finite identities. General
Berezin Fubini, minor formulas and determinant-line transport are proved
in the manuscript. Fubini compares contraction orders of the same fixed
diagram; it does not establish an F-move for unrelated vertices.

The script does not test theta transformations, continuum sewing
convergence, a new interacting theory, or any inherited Bol-loop input.
The manuscript's analytic sewing statement has explicit trace-class and
contractivity hypotheses. Finite zero channels with mixed couplings must
first be included in the assembled quadratic form; simple saturation
factors apply only after isolating its actual null block.
