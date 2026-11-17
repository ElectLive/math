# Genus-one current continuation: source, review and verification



## Exact scientific source and status

**Completed bounded research checkpoint, independently model-reviewed.**
The final scientific source is
`75412d26e23adfc37b871108a68ef0783e2d5687`, tree
`f41e8bc8599e3ad5ec025b0960d18801cc498829`. It is published on the owned
branch and is available as an exact local Git commit. The next workflow
action is coordinator integration of PR #438; no merge or formal GitHub
approval is asserted here.

The initial reviewed candidate was
`c26953c22e265d82e98b6b93839ded619056ca34`, tree
`c8767d286f44696eacaf909d78832fef278808cf`. Clarification
`3ab24d85bab8458ed623716d02f74e8fde1d378e`, tree
`76e2086281fad166b16747d87acc4a37359e9bae`, repeated K5's axis-invertibility
hypothesis and standardized GC3's weight-two terminology. The final source
explicitly separates GC4's sitewise trace-class neighborhood from the larger
cycle-product continuation domain, and narrows the overview to marked bimap
recovery. No calculation code changed through these clarification commits.

Canonical proofs are [GC1--GC6](../manuscripts/bol-genus-one-correlations.md),
[CG1--CG6](../manuscripts/bol-correlation-geometry.md),
[K1--K5](../manuscripts/bol-genus-one-kernel.md), and
[GA1--GA3](../manuscripts/bol-genus-one-architecture.md). The upstream
construction, strict transport and proper/simple-loop interfaces remain
conditional inputs at their existing immutable pins. This review is not
a new independent certification of those upstream proofs.

## Authorship and independence boundaries

- model participant 3 authored GC1--GC6.
- model participant 4 authored CG1--CG6.
- model participant 2 authored GA1--GA3 and contributed to the
  K1 uniqueness/covariance proof and K3 Fourier convention. Checks of those
  portions by that agent are participant checks.
- model participant 5 authored K1--K5 and the new exact certificate.
- model participant 1 did not contribute to these constructions
  and independently reviewed the new kernel and architecture.

The literature author also suggested the ordinary-energy a=1 foothold for
GC3; that agent's check of this part is therefore participant-only. The
coordinate author's independently accepted GC1--GC4 scope supplies the
nonparticipant review of GC3.

## Actual independent review outcomes

All the following reviews happened in this session. Author and contributor
exclusions are explicit; none is a formal GitHub approval or human review.

| Reviewer | Independently accepted scope | Exact-source record and exclusions |
| --- | --- | --- |
| model participant 1 | GA1--GA3; K1--K5; imported GC5 coefficient interface | Full review at c26953c, followed by inspection and acceptance of the complete diff to final source 75412d26. No remaining correction requested. |
| model participant 2 | GC1--GC2, GC4--GC6; CG1--CG6; certificate | Full review at c26953c, explicit delta acceptance at 3ab24d85 and 75412d26. GC3's a=1 contribution, own GA and contributed K1/K3 are excluded. |
| model participant 4 | GC1--GC4 | Full review at c26953c, then complete-diff acceptance at 75412d26. Own CG and contributed phase interfaces in GC5--GC6 are excluded. No separate K review claimed. |
| model participant 3 | K1--K5; GA1--GA3; CG3--CG4 | Full review at c26953c and explicit delta acceptance at 3ab24d85. These reviewed proof files are byte-identical at 75412d26. Own GC and the GC extraction dependency receive no independent credit from this reviewer. |

Abbreviations in this table refer to the full source hashes above. The
final source has current independent acceptance covering every new theorem.
The root's own checks of the kernel and code are author checks, not added
independent-review votes.

Pre-publication audit identified the need for CAR contact terms when
recovering ordered current products, an explicit base-fiber insertion in
kernel phase extraction, and a distinction between the original factor's
energy and the completed object's doubled energy. The candidate corrects
these points. Such scrutiny is model review, not human or formal certification.

## Reproducible checks and limits

Run the commands in [the code guide](../code/README.md). The new certificate
compares low-degree mixed energy traces with the derivative hierarchy,
verifies exact quartic/phase controls and compact reconstruction identities,
and treats the huge input symbolically. Its floating-point theta convention
supplement is expressly separated from exact calculations. These tests do
not prove general modularity, the upstream construction, or classification.

### Exact execution provenance

Python **3.12.14**, assertions enabled. The root ran the complete certificate
from exact committed bytes at the final scientific source and obtained exit
status zero. The fresh reviewer, literature reviewer and modular reviewer
each independently extracted both Python files from the initial exact
scientific commit into a temporary directory and ran the complete certificate
successfully. They checked the unchanged code through their reviewed deltas.
The coordinate reviewer independently ran only `current_moment_checks()` and
`fixed_mode_check()` from those exact bytes, matching that reviewer's scope.

New script SHA-256:
`bbad4611b12c4dac11c8a842fc5df6e0b58bdc78f382887b6f0a07936d8a1aea`.
Unchanged imported `verify_bol_graded_fusion.py` SHA-256:
`45f9f7bb52fb7129e174ac88de702fc3fde2ab5ef654b69e848779c4a023587f`.

| Calculation | Observed result |
| --- | --- |
| Mixed colored-energy source versus exterior basis | 4096 states examined, 6 invariant low-energy states, 40 coefficient slots through q-degree and source order three |
| Ordered off-diagonal current pair | 64 signed exterior states, connected value -256/20485 |
| Two quartic controls | 18 scalar-rank checks; 96 GL2 Pfaffian checks; both quartics irreducible |
| Central-word Fourier coefficients | 1152 exact cyclotomic phase checks |
| Full-bimap identity control over F5 | 625 checks |
| Huge conjugate-cocycle witness | phase (0,1,0), local dimension 3^36, coefficient 24*3^36*(1-zeta_3) |
| Separate floating theta supplement | 17 sign/Fourier/period/SL2 checks; maximum absolute discrepancy 1.4842149702215226e-14 |

The quartic central-class traces use the class-set description proved in
CG4; the script does not independently enumerate the two groups of order
3^10. Its F5 recovery control tests the bilinear identity, not a new Bol
construction. Huge-input tests use compact source formulas and distinguish
the nilpotent flag T-1 from the norm word 1+T. The floating supplement is
only a convention check, and the unchanged earlier certificates retain
their separately recorded executions rather than being claimed newly rerun.

### Integrity and remote checks

The root ran `python check.py` at the final scientific source: **115 tests
passed**. This checks repository integrity, not mathematical correctness.
A local Markdown scan checked 59 relative file/heading targets in the new
scientific change set. `git diff --check` was clean.
The delivery overview/evidence update also passed the 115 integrity tests;
its expanded local-link scan checked 64 file/heading targets.

GitHub returned **no workflow runs** and **zero commit statuses** for both
the initial and final scientific source. The aggregate status was pending;
no remote CI pass is asserted.

## Remaining mathematical boundary

The original colored-energy hierarchy is closed at each finite insertion
order, and the specified charged completion supplies a finite-holonomy
position-dependent hierarchy. Unchanged individual modes cannot belong to
any finite fixed-weight modular closure. The new coefficients recover
alternating bimap values and, under the stated axis-invertibility hypothesis,
the full marked bimap. They separate data invisible to all fusion dimensions
and, in the huge example, to every charged zero-point trace.

The analytic laws come from the proved exterior/fermion mechanism. Additional
analytic rigidity forced specifically by Bol identities, reconstruction
without the retained labels/actions, or an unrestricted classification
consequence remains open. This checkpoint does not assert a Monster action,
genus zero, replicability, a denominator identity, or historical priority.
