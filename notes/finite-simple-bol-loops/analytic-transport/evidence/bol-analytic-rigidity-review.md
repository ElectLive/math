# Analytic rigidity and Fourier sewing: source-bound review



## Scientific revisions

- Holonomy-rigidity checkpoint:
  `85bfbb7e02f4dedb072a0c046b99775d9569fb91`, tree
  `06545dce9586ef60ee5045a55bb9f3fe2dbe6a92`.
- Full Fourier-sewing scientific source:
  `2647c763b1c146e84486cb4b9716c482a49fd672`, tree
  `827dfb3970dec4dc7962a34913f5df9357fcb7df`.
  HR is byte-identical to its preceding checkpoint.

Both exact commits are published in the owned branch and available locally.
The source includes the complete definitions, proofs, compact coordinates,
exact executable certificate and deterministic JSON. A later delivery edit
records review and narrows one certificate sentence; it changes neither
manuscript, the executable script, nor the JSON evidence.

## Actual independent reviews

The reviewer identities below are model agents in this research session.
These are mathematical model reviews, not human acceptance, formal
verification, or a GitHub approval by a maintainer.

| Reviewer | Exact scientific source | Independent scope | Outcome |
| --- | --- | --- | --- |
| model participant 1 | `85bfbb7e02f4dedb072a0c046b99775d9569fb91` | Complete HR1--HR6, including HR2a, HR3a and HR5a; primary Mat19/MTZ locators; inherited-interface boundaries | Accepted; no mathematical correction required |
| model participant 1 | `2647c763b1c146e84486cb4b9716c482a49fd672` | Complete FS1--FS8 including FS6a; all 803 lines of the executable; both certificates; overview/reference changes and inherited generator-fixing interface | Accepted; no theorem or code correction required; the evidence-wording clarification below was inspected and resolved |
| model participant 2 | `2647c763b1c146e84486cb4b9716c482a49fd672` | FS2; FS3 including FS11a and inversion; FS5; FS6a correlation lift and modular energy subsystem conditional on the support premise; FS8 quartic-order comparison | Accepted; no mathematical correction required |

The fresh reviewer independently accepted every new theorem and the
committed executable. No acceptance is inferred from either review outside
its actual scope. Neither review was treated as acceptance of the upstream
classification or huge-loop construction.

The fresh HR reviewer read the complete exact Git source and supplied no
construction or proof. The review checked the meromorphic-field projector
argument, the trace pairing on actual orbit blocks, all pole normalizations,
the zero-mode obstruction, the finite Fourier convention and induction,
the strict enlargement of the old operator algebra, and the quadratic
graph-erasure proof. Its acceptance carries to the full source because the
HR bytes did not change.

The complete FS review checked the canonical all-charge origin and its
strict transport, the admissibility hypotheses, all signs and shifts in
the modular and current formulas, the exact support converse, the full
unlabelled transfer-family quantifier, and the right/left phase distinction.
It checked the generator-fixing argument against the pinned interface,
validated the quartic and twelve-point controls, and accepted the regular
countermodel only with the manuscript's explicitly restricted group-word
scope. It confirmed that the analytic defect remains a universal function
raised to a finite geometric count.

The literature reviewer read the new source with `git show` at the stated
commit. The independent review checked the network normalization, oscillator
logarithm and convergence; parity-dependent modular products and their
levels; exact logarithmic inversion and multiplicative faithfulness; the
BCH section, phase basis and full-charge permutation; the common-source
factorization, literal trace convergence domain and modular energy
completion; and the basis-independent order-five separation of the two
quartic controls. The conservative Gamma_0(320) level in the certificate
and the sharper Gamma_0(160) level in the manuscript are both valid.

### Authorship and excluded participant scopes

- model participant 2 authored HR. That agent also contributed
  the zero-charge factorization observation in FS4, preliminary support and
  isotope checks in FS6--FS7, and clarification of the group-word-only
  independence claim in FS8. Those contributions are not independent review.
- model participant 3 authored FS and contributed the quadratic
  control in HR6. Its checks of those arguments are participant checks.
- model participant 4 developed the finite network and full-charge
  construction, rigid and quartic controls, and exact certificate. Its
  runs and mathematical checks of those contributions are author evidence.
- model participant 5 proposed the linear spectral theorem, several support/converse
  and family tests, the common-source extension, cycle-faithfulness and
  the twelve-point ablation. Root's proof checks are not counted as
  independent acceptance of those contributions.
- model participant 1 contributed no research construction
  in this continuation and performed the fresh read-only reviews.

## Reproducible exact execution

The detailed arithmetic scope is owned by the
[calculation certificate](bol-fourier-sewing-certificate.md), with
[deterministic JSON](bol-fourier-sewing-certificate.json).
From the repository root, with assertions enabled:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_fourier_sewing.py --certificate /tmp/bol-fourier-recheck.json
python check.py
```

All recorded runs used Python 3.12.14. There is no floating-point supplement
in this new certificate. Its arithmetic is exact over F3, the two quartic
fields, integers, rational numbers and Z[zeta_3].

| Artifact | SHA-256 |
| --- | --- |
| `bol-holonomy-rigidity.md` | `abc633048d0ec178da7d6f4f8fab989178a3cb7e52f6a6d15c1793bed69627d2` |
| `bol-fourier-sewing.md` | `248bf6a19f5393756e203fc495c477faf03c7bbf7aa3e00c460a6d5f19f16e74` |
| `verify_bol_fourier_sewing.py` | `4d8a76734ecc22f014d498c4d7f5dd3b511dfce437cf5977257977b68a424b17` |
| `bol-fourier-sewing-certificate.json` | `67fbc06f510824b4060372dfca0cd97ca716184404a72cab37e04b03ed11de85` |

The author, root, fresh reviewer and literature reviewer each ran the final
script successfully. The authors and both reviewers compared their generated JSON
with the committed certificate and obtained byte-identical output. The
reviewers extracted the executable and expected output from the exact
scientific commit, rather than relying only on a working-tree filename.

The checks include 81 exact Fourier matrix entries, 6,642 directly summed
network terms, 7,680 self-adjoint power-rank calculations, 96 central-basis
relabelings, 176 logarithmic inverse coefficients, all 144 reduced rigid
regular pairs, 324 radical-restriction checks, and all 108 distinct
transfer/central tests. The common-source test directly computes eight
signed-wedge traces with 311 initial states each, retaining intermediate
states above the energy cutoff, and then implements 24 species. All 36
specified source coefficients agree in the disjoint-support control.

The fresh review identified one evidence-wording qualification: the small
explicit Fourier-product test uses T=-1=T^(-1), so it cannot distinguish
the two orientation conventions. The delivery correction attributes the
convention to the proof and the noninvolutory relative-form matrix checks,
and states the small test's limitation explicitly. The reviewer inspected
that exact working-tree correction and confirmed that it resolves the
issue. Neither the mathematical result nor any code or numerical output
needed changing.

## Integrity and remote status

At scientific source `2647c763b1c146e84486cb4b9716c482a49fd672`, root's
`python check.py` run passed all 115 tests. A separate local Markdown check
verified 55 file/heading targets in the affected overview, references,
code guide, manuscripts and calculation certificate. These checks concern
integrity and navigation; they do not prove the mathematics.
The delivery working tree also passed all 115 integrity tests and a
65-target local file/heading check. Its reviewed manuscript, executable
and JSON bytes were compared directly with the scientific commit and
are unchanged.

GitHub reported one workflow run at that scientific source:
`43784143897`, completed with conclusion **skipped**. Its combined commit
status was pending with zero individual statuses. No remote CI pass or
satisfaction of a maintainer's integration gate is asserted.

## Mathematical boundary and handoff

The strongest new result is the canonical full-charge sewing construction
and four-sector identity with an exact support converse, including every
common-source original-current correlation and a conditional invariant
existence test separating the rigid principal isotope. The equal-fusion
quartic group controls provide a separate complete-family comparison.

The extra premise is a finite polynomial support relation. The regular
action countermodel proves nonconsequence from group-valued word relations
and the universal oscillator laws; it does not preserve the original
pointwise algebra, fiber projectors or arbitrary partial-operator relations.
The latter can already encode the finite support geometry. The modular
mechanism remains the standard exterior determinant and discriminant
product, and the scalar defect is one universal function to a finite
geometric power.

Canonical-folder, simplicity, properness, strict-isomorphism, torus-label
rigidity and principal-isotope inputs retain their inherited source and
review qualifications. The new computation does not re-prove them. The
363-class model validates local arithmetic; the quartic examples are group
controls. No huge loop table, unrestricted classification, new interacting
vertex algebra, Bol-exclusive elliptic kernel, genus zero, replicability,
Monster action or literature-priority result is claimed.

The stronger open target is coherent charged sewing with a noncoincident
analytic constraint that does not reduce to finite support or spectral
identities. The bounded checkpoint is complete and independently
model-reviewed, for coordinator integration subject to the existing gates.
PR #431's branch, sources,
claim ownership and historical review pins remain unchanged.
