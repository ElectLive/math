# Full-socle publication checkpoint, 17 November 2026

This is the earlier checkpoint. See the [later classification synchronization](PUBLICATION-2026-11-17-LATEST.md) for the subsequent E₆/E₇, classical, binary symplectic and odd-kernel results.

Mira Cult

## What is new

This deliberate publication batch adds five coherent claim families:

- [0087: Alternating full socles force the natural action](manuscripts/0087-alternating-natural-full-action.md).
- [0088: Every sporadic full multiplication socle is excluded](manuscripts/0088-sporadic-full-socle-exclusion.md).
- [0089: PSL₂ and odd-dimensional PSL/PSU full-socle exclusions](manuscripts/0089-classical-full-socle-exclusions.md).
- [0090: Exceptional full-socle exclusions, including all G₂ and F₄](manuscripts/0090-exceptional-full-socle-exclusions.md).
- [0091: Original-mark collision lifting and the canonical center](manuscripts/0091-original-mark-collision-tools.md).

These are conditional research theorems, not a completed classification of finite simple proper Bol loops. Exact hypotheses distinguish full multiplication groups, canonical left groups, their actual factors, and operation-level classification. The [family index](CLASSIFICATION.md) and [open-problems board](OPEN_PROBLEMS.md) now reflect those distinctions. Public numeric IDs are independent of the internal aggregate classification claim, which stays open.

## Frozen boundary and correction history

The previous public classification source pin was `47b07688a82d3df93f537946fe0780112200383b`. This batch carries the 49 changed source artifacts through completed review checkpoint `80d2ceba5672716d34068266d4966147235f31d5`, 80 source commits later. Unchanged dependencies retain their earlier exact revisions in the [source map](classification-source-map.json); the top-level pin is not a claim that every artifact changed at that revision.

The checkpoint ends with three exact-source reviews of corrected even-F₄ source `4d5ba4746ef45bdbeae9d570ee306fe04b8f7463`. The earlier version omitted the q=8 PSL₂(27) maximal case and misstated a primitive-divisor factor in the quadratic triality subfield argument. The source records both fixes and withdrawal/replacement of earlier provisional acceptances. Two unchanged GAP certificates were reused with that limitation stated. No acceptance of the faulty source is counted as acceptance of the corrected theorem.

Other recorded source acceptances include:

| Result | Exact mathematical source |
| --- | --- |
| Alternating finite homogeneous completion | `b782384e807bb07f6197b2a06fd732fe8c6e5c8a` |
| All 26 sporadic full socles | `8cd335ea73dadc72b38b75c294e690bdbeb7c155` |
| PSL₂ full socles | `47b07688a82d3df93f537946fe0780112200383b` |
| Odd-dimensional unitary full socles | `5e9382749b716b55e65928d781df40adc5f067a8` |
| Odd-dimensional linear full socles and odd-kernel lemma | `59338c6eebe69e352d561b68c870ac842d6047e0` |
| Suzuki and small Ree full socles | `016d680964c9c937ee74e93df744087746942280` |
| Uniform exceptional and G₂ full socles | `cd5bf6a31bc63eb838b3150e51dd7aaec57be838` |
| Tits full socle | `c0a78fff876603a8e2c2f4e269dd50ba8f01f693` |
| All-parity canonical center lemma | `e7476945cf987cf1c654a385ac8f78fe2beb320a` |

The complete sources preserve local review scope, external-source inspections, computation versions and limits. Recorded independent model reviews are not human refereeing, formal proof or formal repository approval. The present publication audit checked synthesis fidelity, not all mathematical proofs anew.

Later work on E₆/²E₆ and odd-characteristic E₇ is deliberately not promoted here. The remaining classical full socles, natural alternating/symmetric operations, and general extension/gluing questions remain open. Related analytic and graph-decomposition successors have separate completed checkpoints and are not claimed synchronized by this classification batch.

## Proof availability and presentation

Complete proofs, references and executable dependencies are accessible from the [source index](sources/README.md). New proofs are grouped under [full-socle completion](sources/full-socle-completion/alternating-full-action-reduction.md); existing proof URLs remain intact. The large bridge retains chronological sections, with a prominent notice distinguishing superseded residuals from the current boundary. Source “proposed” headings retain their historical wording; their exact local review records control acceptance status.

The source map retains raw content hashes and source Git blob IDs. Public presentation changes neutralize worker attribution, normalize explicit math delimiters for GitHub, and rewrite source links to public dependencies. Executable source bytes are unchanged. Public source-record copies of internal claims do not change the status of public aggregate claims 0007 or 0010.

## Checks actually performed in this publication

- A separate synthesis audit compared all five new public statements and their review pins against the source. It caught and corrected an overly strong center statement: the theorem fixes Z(G) pointwise, not that the center or its involutions are trivial. It also corrected a misleading blanket comparison between canonical-group and full-socle exclusions.
- Six standard-library certificates passed freshly under Python 3.12.14: `verify_alternating_component_bound.py`, `verify_alternating_k2.py`, `verify_alternating_k3.py`, `verify_alternating_k45.py`, `verify_alternating_solvable_stabilizer.py`, and `verify_psu9_residual.py`. These check their exact arithmetic scopes, not the imported classifications.
- Changed Python sources passed syntax parsing. Changed-page relative file links and heading/explicit anchors were checked. Source/public hashes and executable byte fidelity were checked against the frozen inputs.
- GAP/CTblLib certificates were preserved but were not freshly replayed in this publication environment; the exact-source independent runs remain documented in the proofs. The research-source report of 115 integrity tests is inherited evidence, not a fresh run of that private repository's integrity suite here.
- No complete hosted-page visual audit is certified in this batch. Static link/markup checks and valid Markdown are not evidence that every long proof, formula and catalogue renders correctly on GitHub. That rendering gap remains explicit rather than being represented as a passed gate.

The publication does not modify research workspaces, merge active research branches, or open a new public pull request.
