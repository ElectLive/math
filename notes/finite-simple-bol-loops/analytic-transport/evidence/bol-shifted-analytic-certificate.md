# Separated charged transport: exact controls

The canonical mathematical statements and analytic estimates are
[SA1--SA5, including SA3a](../manuscripts/bol-shifted-analytic-fusion.md).
The corresponding charged/category construction is
[collective transport](../manuscripts/bol-collective-charged-transport.md).
This record distinguishes finite arithmetic checks from the analytic proofs.
The exact scientific source and actual independent review are pinned by
the continuation review record; this note itself asserts no review acceptance.

Run from the repository root with Python 3.11 or later:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_shifted_analytic.py
```

The certificate uses only the standard library and is deterministic. It prints
JSON including the executable's SHA-256. The checked-in
[JSON certificate](bol-shifted-analytic-certificate.json) is reproduced by
redirecting that output; no random seed or external data is needed.
The executable rejects Python's `-O` mode because the exact checks use
assertions. The DD matrix convention is checked directly: the form matrix
`C=((0,2),(1,0))` induces the column-coordinate linear map `C^T+lambda I`.

The checks include:

- The full 27-character register of the inherited rigid center, its exact
  graph/pure products, coboundary conjugation, and all 18 changed marked
  quadratic-response channels. A rational coefficient proxy `(c1,c2)=(1,2)`
  checks the finite inverse formula; it is not a numerical evaluation of
  the analytic constants. Their actual values and conditioning are proved
  by the integrals in SA2.
- Every graph/split word of length at most eight, 511 words in total,
  under the simultaneous marking ablation. Full conjugacy is proved
  symbolically in SA3, not inferred from that finite cutoff.
- 243 genuine small CH regular-charge fusion equations; 243 exact true-dual
  evaluation checks; the full nine-dimensional neutral tensor channel; and
  an explicit distinction between the augmented collective and primitive
  tensor symbols.
- 27 direct form/inverse checks and 19,683 compact DD shifted equations,
  of which 15,309 involve a zero or
  zero-sum later physical charge. A noncentral collective first-axis symbol
  differs under the DD tensorator on all 81 tested basis states.
- Both proper cubic controls at orders 27 and 125, equality of all their
  individual left-translation cycle types, exact inversion/translation
  commutator Hilbert--Schmidt squares, and an independently constructed
  associative additive-group control. At order 27 the script also checks
  19,683 Bol equations for each proper loop, a nonflexibility witness, and
  the complete equal family of associator-defect permutations.
- Rational enclosures verifying the displayed finite-amplitude error
  margins, the uniform transport gap, and the nonzero-third-residue margin.

No ODE quadrature, truncation-based approximation, signed-multiplicity
interpretation, huge rigid module enumeration or numerical inference of a
universal theorem occurs. The dimension-independent analytic estimates follow
from the convergent Dyson expansion and explicit norm bounds in the manuscript.
The large rigid comparison uses the existing marked-data and strict-isomorphism
source qualifications. The small proper Bol controls are known nonsimple loops.
