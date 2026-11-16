# Non-scalar Bol intertwiners: source, checking and review

## Obligation and provenance

Owner: ChatGPT `/root`, session `79e8e156340f`, commissioned by Mira on
2026-11-16. Workspace: [PR #441](https://github.com/Mira-Cult/math-wip/pull/441),
branch `research/0323-bol-nonscalar-intertwiners`, stacked on PR #440.
Baseline scientific pin: `5771bfccb6707606078baf93be804f810276b8eb`;
baseline delivery: `f67b6f91c7f97fe2af1d58240de0b1debc5a2da2`.
Opening source checkpoint: `2057bc5131495f1b97fb4d851bb5809e1f6e6a9b`.
Final independently accepted scientific source:
`ec122a2a890971141caf960dd27fdb50fed77154`, tree
`29bd5d74a8211fcf7c57906dcc4a3d8db8dbd790`.
Manuscript SHA-256:
`c3a0b0a451314826b27d1ce998311dc93c6b37c0ff76a1faa1e251b5603fffbf`.

The canonical source is [Non-scalar fusion and quantum mixing](../manuscripts/bol-nonscalar-intertwiners.md).
The bounded obligation is explicit full-correction intertwiners with a new
finite analytic consequence. New manuscript-local results are Theorems I,
F, D, T, H, Q and Lemma Q1. No permanent claim IDs are allocated or changed.
Theorem Q's nondegeneracy hypothesis is essential; the other constructions
retain zero, degenerate and imprimitive sectors. The joint trace distinction
does not assert new worst-case mixing of the matched-rank degenerate sectors,
or information proved independent of the full prior AQ spectrum.

The root developed and wrote the scientific synthesis with contributors
`/root/sector_construction` and `/root/polarization_routes`. They are not
independent reviewers. `/root/independent_review` was assigned before the final
construction as a noncontributing reviewer, read the baseline, and independently
implemented a finite interface checker. The complete exact-source acceptance
and its final markup-only addendum are recorded below with actual attribution.

## Authored execution record

The coordinator read the four new programs and their relevant runtime interfaces
before execution. Toolchain: Python 3.12.14; NumPy 2.3.5 for the fusion
program's existing coupled-pencil integer implementation. Commands are in the
[code guide](../code/README.md#non-scalar-intertwiners-and-quantum-mixing).
All arithmetic is exact. Seeds are 2026111602 (fusion and independent check),
2026111631 (orbit check), and 2026111632 (quantum check).
Raw stdout/stderr stays outside Git.

The fusion check imports accepted prior implementations; the orbit check also
shares authored field/loop code. The quantum check is a fresh implementation
by a contributor. The reviewer check imports no authored checker and is
preserved byte-for-byte. These distinctions are not collapsed into a single
claim of independent verification.

| Program | Source SHA-256 | Complete stdout SHA-256 |
| --- | --- | --- |
| `verify_bol_nonscalar_fusion.py` | `3663dafcc4379bb7decf2a3cddc88b75e3eae2c50794dfe3b511bcb5ab78bded` | `99eeedebcba4e5c710bf42313579028cbc41428334cac63ea2937543ca8f7728` |
| `verify_bol_nonscalar_orbits.py` | `f17341a25f08757dc53ecf4940b1ba744ea10f48eb28db280e749ff4cb2ea797` | `39d2c1edf4c3b57aa209951546e933ed5e71c108dd3ca0a4a22f585907dce166` |
| `verify_bol_nonscalar_quantum.py` | `21f13e752411255fd320a5829a65822c99b45c7199c6a6b5b26a9895e2daae14` | `6d61fe3d15929deafc726404613a63ecf433eaa49b519d797b39b830d02e0aaa` |
| `verify_bol_nonscalar_independent.py` | `c2f6b0c38f14f92bfa3e7e2ce8cadf4537f54a51f2295f83c5bea208b5f70862` | `bad800236adc6055405fea4f62fdd8c1f6e6112c12a4499ffebf7cb06bdbdf59` |

All four runs exited zero with empty stderr. The complete finite scopes are in
the code guide and source, rather than duplicated here.
The quantum enumeration checks twelve full actual two-point orbit kernels,
not an enumeration of the entire matrix channel. Finite evidence supports
the conventional uniform proofs and cannot replace them.

## Research alternation and boundaries

The approach comparison and exact failures are preserved in the canonical
manuscript: scalar symplecticity fails, same-label invertible intertwiners
between distinct characters fail, arbitrary-unitary decoupling has a complete
radical obstruction, and degenerate quantum depolarization fails. The residual
fusion, characteristic-shear projection and actual-defect channel are the
substantive repairs. Formal reassociation is explicitly separated from the
analytic results. No category, cover, automorphic or arithmetic application
is inferred from matrix coherence alone.

The manuscript compares inspected primary Heisenberg, loop-module, higher
weak-action and quantum-expander literature at precise locators. It does
not certify literature-wide priority. Source statements, independent review,
finite checking, repository integrity, remote CI and integration are distinct.

## Independent review status

**Accepted by independent mathematical model review within the stated scope.**
The noncontributing reviewer `/root/independent_review` read the complete
manuscript and relevant dependencies, checked all decisive proof chains, and
replayed all four programs from an isolated extraction of
`d25855cc7f55c0e96f7644284c91c9897633552f`. Every replay exited zero with empty
stderr and the exact stdout hash above.

The [signed original report](bol-nonscalar-independent-review.md), dated
2026-11-16, is preserved verbatim; its SHA-256 is
`cec9e1d94aab134d73532a6563a6be72c484cbf0a1ebc96040ad6e373471249e`.
The [signed addendum](bol-nonscalar-independent-review-addendum.md) extends
acceptance to `ec122a2a890971141caf960dd27fdb50fed77154` after independently
checking the exact single-byte NI.26 set-delimiter repair. Its SHA-256 is
`df08ba8d6e5d38b576d4d3682660893ddc7bd91fc090cb78461ee9448fa2bd18`.
The programs, their dependencies and all mathematical content are unchanged
by that repair. The addendum records source inspection, not another execution
or a browser-rendering check.

This is model review of conventional proofs. No human acceptance, formal
verification, literature-wide priority certification, remote CI pass, merge,
or formal GitHub approval is claimed.

## Repository and presentation checks

The coordinator ran `python check.py --base
4ded8c4fb264235370a745100755a26a372918ba`: all 115 metadata/tool tests passed.
An initial run had failed because historical review/order Git objects were
missing in the isolated checkout. Exact content-addressed objects were restored
from the earlier checkout; no source, validation rule, permission or workflow
was changed to obtain the pass. These tests establish repository integrity,
not mathematics. The source revision remains locally available.

Manual source review and automated local navigation checks verified 81 local
file/anchor links in the scientific package and all 38 numbered equations.
A TeX-group audit of all 429 inline/display snippets found the NI.26 delimiter
typo; the final source has no unbalanced groups. The logged-out cloud browser
could not access the private repository and returned GitHub's 404 page, so
**rendered GitHub equations and page layout were not visually verified**.
Source checks are not presented as a substitute for that missing visual check.

At the final scientific source, GitHub Actions run
[43887839558](https://github.com/Mira-Cult/math-wip/actions/runs/43887839558)
reported the integrity workflow **skipped**, not passed. The current delivery
head and its live CI state belong to [PR #441](https://github.com/Mira-Cult/math-wip/pull/441).
Local test success does not change that remote status.

## Concise handoff

* **Owner and state:** ChatGPT `/root`, session `79e8e156340f`; the commissioned
  finite construction and analytic theorem are complete and independently
  reviewed. PR #441 carries the delivery; the parent PR #440 is unchanged.
* **Changed interfaces:** one canonical manuscript with local results I/F/D/T/H/Q
  and Q1; four executable checks; bibliography and overview navigation; signed
  source-bound review. No permanent claim IDs, old proofs or old reviews changed.
* **Strongest result:** unitary full-correction fusion with an arbitrary-unitary
  decoupling criterion and universal residual repair, an intrinsic two-sector
  trace distinguishing the matched-rank families, and a nondegenerate matrix
  channel with exact population rate and faster coherence bound.
* **Reproduction:** run the four commands in the
  [code guide](../code/README.md#non-scalar-intertwiners-and-quantum-mixing).
  Toolchain, finite scopes, implementation dependence and output hashes are above
  and in the signed report. Finite checks do not prove the infinite family.
* **Boundaries:** the complete old AQ spectrum can already contain joint-image
  information; no independence from that entire spectrum is asserted. The
  matched-rank sectors are degenerate and are not covered by depolarization.
  No exact off-diagonal norm, full degenerate stationary algebra, efficient
  bounded-degree channel, arithmetic application, isotopy or classification
  result is claimed.
* **Next obligation:** integration review of this exact scientific source and
  the separate delivery evidence, subject to existing repository requirements;
  rendered-page inspection remains outstanding. Substantive future research
  could determine the degenerate translated channel's stationary algebra or
  a bounded-degree approximation preserving the loop-selected estimates.
  No future research dispatch is started by this handoff.

