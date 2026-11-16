# Verification, review, and source identity

**Mira Cult · 16 November 2026**

The [catalogue](CATALOGUE.md) records the mathematical results. This note
records how their proofs and finite evidence were checked. A conventional
proof, a model mathematical review, a finite computation, and a rendered
publication check are distinct forms of evidence. None of this collection
is claimed to have an end-to-end Lean proof, human-expert review, or journal
referee acceptance.

## Positive bounded-treewidth continuation

The final scientific source for the new bounded-treewidth, connected-triangle
and zero-edge results is `566b6a1a6ac3ff0b8ef1684d467b5ec904bcbe57`.
The main theorem and its checker are unchanged from
`1aa36e65a3032077043df7558845d633ddb62d8f`; the first scientific publication
was `7c0a70be8ae23ff1b190ed4411714914d53838aa`.

Two complementary nonauthor model reviews cover the new science:

| Review scope | Exact source and outcome |
|---|---|
| Integer bag factorization, both local entropy lemmas, tensorization, width-dependent constants, raw normalization, quotient scope and the pairwise integrality-defect example | **PASS** at the initial source, with the one-block example summary corrected and rechecked at `1aa36e6…`. The review excludes its author's connected construction and separator example. |
| Connected Boolean family, separator example, forbidden-pair constant-four theorem, star-energy limitation, integer hard-zero barrier, and genuine six-bit Boolean noniterability | **PASS** at `566b6a1…`. The review excludes its author's contributions to the main bounded-treewidth proof. |

The reviews checked the actual source blobs and recorded their hashes.
One-block treewidth wording and the comparison with the earlier depth-two
product constant-four theorem were corrected before the final decisions.
The constant-four forbidden-pair theorem requires a Boolean forest parent
(or the stated power-of-two section hypothesis); missing a pair alone does
not supply that arithmetic condition.

The three added programs are byte-identical to the scientific source and
were rerun successfully from the public paths using the standard library:

- Nine exact scalar certificates and both strict constant comparisons;
  65,814 Boolean truth tables, including 33,802 positive spectra and 1,034
  eligible width-two laws; 6,654 ternary tables, including 3,574 positive
  laws; 300 seeded integer bag reconstructions and twelve defect examples.
- The complete 4,096-value base Boolean function and signed Walsh transform;
  exact connected core laws for one through four blocks, including 65,536
  core states at four blocks, and their entropy/influence and graph identities.
- 89,480 admissible physical sections, exact star-energy examples, the
  131,072-value integer hard-zero star, the seven-bit path and the six-bit
  Boolean two-star counterexample with 25 positive atoms, entropy four,
  influence two and half-integer second sections.

The optional 24-variable connected-witness calculation was run by its
constructor and independently by a nonauthor reviewer. It verified all
16,777,216 signed Walsh coefficients exactly using NumPy. The public
adaptation reran the standard-library default, not that optional full scan.

The public adaptation received complementary source-fidelity reviews at
exact file hashes. Review caught and corrected an omitted parent-forest
hypothesis in two summaries, a missing math macro backslash, and two
positivity/integrality wording shortcuts. The proofs and the hypotheses
now agree. These reviews are not a claim of independent acceptance of a
reviewer's own scientific contributions. The actual GitHub host rendering
of this continuation will be recorded after publication; prepublication
checks alone are not described as host inspection.

## Earlier scientific sources

The principal scientific revision of the earlier cactus/interpolation milestone is
`d2b95c607a1d4b21c5eace6b3d52771e74905196`, tree
`44d74cd7a1ffff4254c6801abfa8a1f2f16b9320`.
The selector's constant-function wording was corrected at
`f76b9e8c44e4f343bafaa41dd732f459db210b04`, tree
`b8cdf1c30f408d7e3592692cb2f39f5281ff32d9`.
The bridge's description of constant four was corrected from an unsupported
optimality adjective to “preserved constant four” at
`23017f19c0969367672e98d350da38d028746e7b`, tree
`b8793a200ebcafaab7649d08e66ce7e869ed144b`.
Neither wording correction changes a displayed inequality or proof.

The public manuscripts reorganize those mathematical sources, remove
research administration, supply all local proof dependencies, and adapt
math delimiters for GitHub. Their public file hashes therefore differ
from the source manuscript hashes. The original eight programs were copied
byte-for-byte. A retained source-to-public crosswalk binds the source
revision, source hash, public location and public hash for every file.
No private repository link is needed to read any proof in this collection.

## Three nonauthor reviews of the earlier cactus and interpolation results

Three separate ChatGPT model reviewers checked those earlier results at exact
source revisions. Each reviewed work they did not author. Their scopes
were deliberately separated from their own contributions.

| Review | Source and independently checked scope | Decision and exclusions |
| --- | --- | --- |
| Cycle facets and conditioning | At `d2b95c…`: modular affine-support lifting, use of Barahona–Mahjoub, odd-prime exclusion, integer dyadic forest sections, exact scaling and adaptive cuts, common-feedback-vertex FEI, cactus cutset payment, and explicit cycle/facet/graph examples. Both corresponding Python programs were rerun. | **PASS.** The fixed-cutset conversion to $`4+(8/3)(k-1)`$ and the two-bit integer counterexample were initially excluded because of reviewer participation; the separate integer reviewer checked those exact portions in a dated addendum. The old forest induction was a previously reviewed input. |
| Physical interpolation and Boolean bridges | At `d2b95c…`, with the exact prose corrections inspected at `f76b9e8…` and `23017f1…`: half-bit scalar inequality, rational Bernstein certificate, adaptive telescoping, shared-data examples, separated-amplitude estimate, explicit selector counterexamples, Boolean minimum-layer improvement, fair-completion bound, majority mixture obstruction, and tree projection with zeros. Both programs were rerun. | **PASS after the constant-function wording correction.** No independent review of the reviewer's own cycle/cactus/section work is asserted. The later “preserved constant four” wording does not assert optimality for the first-hit-list class. |
| Integer forests and bounded conditioning | At `d2b95c…`: integer local factorization, logarithmic Sobolev normalization and scalar constants, raw entropy scaling, deterministic quotients, near-constant sections, bounded conditioning, and the local integrality defect. The Python program and compiled C scan at three variables were rerun. The two ancillary dyadic-conditioning claims above were also checked at unchanged source bytes. | **PASS.** The reviewer did not author these results. Their own physical interpolation and co-derived Boolean minimum-layer improvement are outside this independent review. The optional four-variable C scan was not independently rerun. |

The cycle reviewer independently retrieved the original Barahona–Mahjoub
paper and checked the exact facet theorem used. The integer reviewer
independently checked the Gross cube normalization in the primary
O'Donnell–Wright–Zhou paper. These checks verify the cited interfaces;
they do not reprove the full classical external theorems.

## Previously reviewed proof dependencies

The public account includes the actual proofs rather than relying on a
claim that an earlier checkpoint was reviewed:

- **Forest arithmetic and completion:** the source-bound review at
  `45edf7efcece6b0e99dadcdffab5bd94111704dd` covers odd-prime exclusion,
  rational factors with zeros, min-sum localization, odd-amplitude rigidity,
  prefix/bent completion, and the explicit core and packet obstruction.
- **Positive forests:** review at
  `5bd3bfcc6f4a1a0da81021084398127b303b8ea9` covers the full
  minimum-layer, range/degree, simultaneous Gibbs/cross-field induction,
  FEI deduction, and hard-zero boundary. Its published checker rerun
  reported 65,814 Boolean functions and 37,926 integer tree energies.
- **Deterministic contraction:** review at
  `a694775cc6f9292c248ef83605da950d0eb0ec31` independently checks the
  quotient map, preserved Booleanity and entropy, and influence inequality.
  The public version includes the complete contraction proof only; it
  does not enlarge it to all hard-zero edges.
- **Integer flat packets:** review at
  `38621cb84d0a4a5cd2eba36772f3b4eea524ee05` independently checks the
  flat-packet and signed-partition argument. A separate source-bound
  review at that revision checks the determinant input used by the
  bounded-spread extension. The extension's contributing reviewer did
  not describe their own determinant work as independent.

The restored source hashes for these dependency manuscripts match the
hashes in those review records. Their historical reviews do not, by
themselves, certify later editorial changes in this public adaptation.

## Finite checks and their limits

[code/README.md](code/README.md) gives exact commands, parameters, counts,
and which comparisons use floating point. The following are particularly
important distinctions:

- The half-bit inequality is justified by an analytic reduction and
  fourteen positive **rational Bernstein coefficients**, not numerical
  minimization of a curve.
- Boolean transforms, support tests, modular lifting examples, graph
  cutsets, and the displayed rational examples use exact integers or
  fractions.
- The integer-factor program's random tensor/product tests and the C
  program's entropy ratios are numerical diagnostics. Their exact
  classification counts are a different claim.
- The four-variable ternary scan's 43,046,721-case count was an author
  run. The independent reviewer compiled and reran through three
  variables, reproducing 704 positive forests among 6,561 tables.
- The explicit 257-input selector obstruction is evaluated through an
  exact, proved composition recurrence. No enumeration of its full truth
  table is claimed.

For this public adaptation all seven byte-identical Python programs were
rerun successfully from the public note directory using Python 3.12.14.
The C scan was compiled with `cc -O3` and rerun at three variables,
again reporting 6,561 cases, 704 positive forests, and largest odd part
three. The optional four-variable C scan was not repeated. The copied
program bytes were compared to their scientific sources. The public
Markdown's local file links, heading anchors, balanced fences, and converted
math delimiters were also checked; no missing local link or anchor remained.

## Earlier public presentation check

The public rewrite has a separate statement-scope, dependency-completeness,
and source-fidelity review. This is an editorial and mathematical-interface
check of the adaptation, not an additional independent review of a
reviewer's own scientific contributions.

The initial public source was published at
`705b4ec9e281738b2bfc919b5ad904bb20dcbf9e`. Actual GitHub rendering
revealed three rejected uses of the operator-name macro. The notation-only
followup `dfd60f6d700ab1082d6323d6f7f920c760fbb824` replaced those
uses by supported upright text in the catalogue, bibliography and forest
arithmetic proof. This does not change any mathematical statement or code.
Those three public hashes differ from the prepublication review list; the
source-to-public crosswalk records the change.

At that followup the publisher visited all fifteen rendered Markdown
pages, checked their headings and formula-error messages, followed the
public proof/reference/reproduction navigation, and visually inspected the
overview equations, catalogue tables and an integer-forest proof page.
No formula-rendering error remained. The root repository index also
displayed the new entry and its public overview link. These are scoped
browser checks, not a pixel-by-pixel inspection of every line. The later
publication-record update changes only this verification prose.

The public integration request is
[Mira-Cult/math PR #4](https://github.com/Mira-Cult/math/pull/4), on branch
`research/fei-beyond-forests`. The source is available on that branch;
publication as a pull request does not assert that it has been merged
into the default branch.
