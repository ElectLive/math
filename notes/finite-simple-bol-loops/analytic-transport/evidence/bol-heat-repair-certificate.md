# Mixed-heat marked reconstruction: exact controls and scope

This is the author-run evidence for
[HT1--HT6](../manuscripts/bol-heat-sewing-repair.md), in the continuation
of PR #438. Execution scope is recorded below.
The manuscript gives a scoped positive analytic reconstruction theorem;
it does not complete the combined charged dynamical fusion objective.

No independent acceptance is recorded here. The final scientific revision
and any actual review are to be pinned in the coordinator's review record.
The earlier reviewed charged baseline remains scientific source
`197d13d4ac2e48763ed20bf418228d7b4d16aa8c`, delivered at
`6a605decda125c2fa18e36b90b8615d9c3b2ee50`; this evidence does not change
those source or review pins.

## Source, environment and command

The executable is [verify_bol_heat_repair.py](../code/verify_bol_heat_repair.py).
Its exact deterministic report is
[bol-heat-repair-certificate.json](bol-heat-repair-certificate.json).
The author ran it under Python 3.12.14 with assertions enabled and no
third-party packages. It requires Python 3.11 or later and uses exact
integers, fractions and cyclotomic rings Q[zeta_p]. There is no random seed,
floating-point theta evaluation, external process, hidden database or
large-loop enumeration.

From the repository root:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_heat_repair.py --certificate problems/0323-finite-simple-non-moufang-bol-loops/evidence/bol-heat-repair-certificate.json
```

For an independent reproduction without overwriting the pinned report:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_heat_repair.py > /tmp/bol-heat-repair-reproduction.json
cmp /tmp/bol-heat-repair-reproduction.json problems/0323-finite-simple-non-moufang-bol-loops/evidence/bol-heat-repair-certificate.json
```

The report includes the executable's SHA-256. At author handoff the
content hashes are:

| File | SHA-256 |
| --- | --- |
| `manuscripts/bol-heat-sewing-repair.md` | `e5aac86246d5d4d5df4eff07805a74c8fde46f11f1de77a90a37f08856c4b8e9` |
| `code/verify_bol_heat_repair.py` | `8a1c206c7fe54a8035cac9ad8ebb8af9a88bed57daa6a81e80aae20bf18b66c5` |
| `evidence/bol-heat-repair-certificate.json` | `0a70181b80c7bc58840ce92851c1cdadbd16a875ae0a5fec38bab0150ab68aa4` |

The manuscript hash includes the later author clarification of the modular
operator pullback notation and the explicit theta-quotient bound for the
finite-sampling constant. These changes do not change executable or JSON
bytes. Subsequent scientific changes require a new source pin and an
updated evidence binding; these hashes are not an independent review.

## Exact test coverage

The recorded result is `PASS`. The report contains:

- 1,493 Weyl orthogonality equations, together with Hermiticity,
  involutivity and the exact sum of displaced parity operators.
- Reconstruction of 251 coefficients of arbitrary exact matrices across
  `(p,m)=(3,1),(3,2),(3,3),(5,1),(5,2)`, including the Hilbert--Schmidt
  Parseval identity and every matrix zero-mode basis element. The two
  proper controls below are additionally reconstructed in full.
- 824 exact conjugation equations for the modular S and T generators
  at p=3,5,7 and every nonzero k modulo p. The Fourier implementer is
  tested before square-root normalization through F F*=p I; no numerical
  metaplectic phase is used.
- The associative Heisenberg group of order 27, checked through all
  19,683 associativity triples. Its cyclic charged operators V and
  zeta_3 V have the same spectrum. All nine marked probe coefficients
  distinguish their phases, while 81 graph-only coefficients erase them.
- Both established cubic proper left Bol loops Q_0 and Q_1 of order 27:
  39,366 left Bol triples, an explicit nonflexibility witness for each,
  all 27 matching labeled left-translation cycle types, and 54 exact
  conjugation equations transporting the selected marked translation
  through the known F_h isotope comparison.
- The actual 9-dimensional nonzero-charge marks in those two controls
  have the common characteristic polynomial `(t^3-1)^3` and a full
  `Mat_3` zero algebra. The nontrivial zero-mode probe produces the
  unequal exact recovered coefficients `3*zeta_3` and `3`.
- 24 exact geometric-tail controls for the finite-sampling bound
  `M*((1-R^(-N))^(-2)-1)`.

The known proper controls, their nonisomorphism and principal-isotope
relation are owned by
[the cubic-isotope manuscript](../manuscripts/bol-cubic-isotopes.md),
especially (S1)--(S12), (S16)--(S19). This executable checks the formulas
used here; it neither presents those loops as new discoveries nor
claims that this marked correlation classifies unmarked Bol loops.

## Analytic result and its actual comparison class

The new observable is the coupled two-kernel trace with a separately
fixed pair-inversion/reference boundary. Its separated contour data
determine the full marked operator Q, with a Lipschitz reconstruction
bound and exponentially convergent finite contour sampling. It satisfies
the mixed heat equation and the explicitly proved modular operator law.

Its comparison class consists of operators with the same marked holonomy
pair and equal individual spectra. The controls demonstrate extra
information beyond individual spectrum-based trace functions. The full
finite coupled tensor is **not** held fixed: it is exactly what the
analytic theorem reconstructs. No stronger independence claim is made.

Replacing the fixed boundary by Q^(-1) removes a central scalar phase.
For charge-changing marks the reference J is independently retained and
transported; choosing it afresh as Q would have the same erasure defect.
The zero sector is the full matrix algebra, not a scalar residue. The
correlation is defined on the marked covering parameter space; it is not
asserted to be an unmarked scalar function on a product of elliptic curves.

## Limits of this evidence

The analytic proofs use normal convergence of the classical theta series,
the mixed Kronecker heat identity, Cauchy integrals and finite-dimensional
matrix identities. The primary theta normalization and modular generators
were inspected in NIST DLMF 20.2.1, 20.2.6, 20.2(iv), 20.7.26 and 20.7.30,
version 1.2.8 (2026-09-15). The manuscript gives its own constants and
derivations. The exact script does not prove convergence, contour
regularization independence, the universal modular law, or the operator
error estimate; those remain mathematical statements requiring independent
review of the manuscript.

This is a new analytic object. There is no claimed identification with
the original Fock traces and no claimed heat-compatible pentagon joining
it to the finite dynamical tensorator. The fixed covering-frame boundary
operator is not asserted to be a parallel morphism between arbitrary
independent insertion fibers. There is no Monster action, genus-zero
theorem, arithmetic moonshine consequence, positivity claim for signed
coefficients, or unrestricted Bol classification.
