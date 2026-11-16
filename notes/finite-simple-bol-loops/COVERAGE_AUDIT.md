# Public coverage and researcher-readiness audit

**Audit date: 16 November 2026.** This is a dated coverage assessment, not a new mathematical review. It compared the public board with active research revision `ed03ee5a0a45d9087e0619b15b7ba5cd1806d57a`. Publication is ongoing: consult the research catalogue and manifests before treating any item below as still missing. Revision pins are provenance, not separate research programmes.

## Verdict

The board is usable for a focused investigation of a published construction or interface. It is **not yet sufficient to restart every branch of the full classification from public sources alone**. Making it useful requires more than copying result headlines: a researcher needs exact definitions, actual proofs and imports, reproducible inputs, failed reductions, and a precise next obligation.

[Start here](START_HERE.md) supplies the target and conventions; [research workflow](RESEARCH_WORKFLOW.md) supplies a repeatable task-and-review process. The [research catalogue](RESULTS.md) provides one coherent account of mathematical progress. Supporting source revisions remain distinguishable for reproducibility.

## Coverage dimensions

| Dimension | What a new researcher can use | Remaining obligation |
|---|---|---|
| Problem and conventions | Precise proper-left-Bol target, soundness/exhaustion/isomorphism goals, multiplication-group and isotopy distinctions | Every specialized manuscript must state its own additional model assumptions. |
| Literature | Public references linked from the catalogue, with community source contributions invited | Exact theorem locators and convention translations for every imported result; bibliographic presence is not proof validation. |
| Progress | Catalogues and frozen source packets | Reconcile later reviewed results and superseded open tasks; do not silently promote an old review to a new appendix. |
| Proof closure | Direct-example packet and many supporting manuscripts | Some broad assemblies have missing transitive inputs. The [SD map](SD_DEPENDENCIES.md) is a concrete example, not the only possible gap. |
| Reproduction | Supplied Python/GAP controls and recorded source pins | Per-result versions, commands, inputs and actual rerun outcomes; no global computational-certification claim. |
| Task selection | Open-board labels and proposed structural next steps | Keep restricted solved models separate from stronger unrestricted targets. |
| Research memory | Relevant counterexamples and limitations in manuscripts | Preserve failed reductions that prevent duplicated work, while omitting unrelated private chats and unsupported speculation. |

## Reconciliation checked in this audit

At the audited active revision, the following had advanced beyond the earlier public `67cced8` snapshot:

- Canonical `PSL₂(q)^n` models with arbitrary inversion, not merely paired inversion.
- The full **nonpermuting** A₅-socle setting, including selected marks and outer-code data.
- Exact cyclic and regular abelian A₅-top models; two distinct order-27 regular-top models.
- A uniform odd-prime-power top reduction and higher-rank extraspecial existence/exclusion.

These are **source-reported, scoped model-reviewed developments**, not independent endorsements by this coverage audit. The current mirror pass is publishing their exact statements and inputs. Neither these advances nor the older paired models classify arbitrary factor-permuting groups, mixed socles or general radical extensions.

## What “mirror everything known” should mean

Mirror the reusable mathematical record: precise problems, definitions, source references, constructions, proofs, counterexamples, useful negative results, experiments and exact limitations. Preserve links between claims and their dependencies and reviews. Keep the public account coherent as the frontier moves; retain exact source revisions in supporting provenance.

Do not mirror raw private conversations, credentials, personal data or unrelated speculation. Do not discard an important failed reduction merely because it did not yield a theorem: if it constrains future work, summarize the failure and its evidence.

A result should be distinguishable as:
- **a public proof package**, whose stated dependencies are accessible;
- **a reported research milestone**, with accessible statement and an explicit dependency gap;
- **a proposed continuation**, not yet covered by the stated review.

This distinction lets contributors choose work responsibly. It is more informative than calling the entire board “verified” or hiding every unfinished branch.

## Next maintenance priorities

1. Complete transitive source closure for a small selected theorem before claiming a fully self-contained all-family proof.
2. Keep a public supersession trail when a narrower open question becomes solved.
3. Make exact-source review and computation records easy to locate.
4. Test onboarding periodically: can someone with only this public repository reproduce a control, identify a genuine remaining lemma, and submit a scoped contribution without asking for private context?

## Subsequent factor-permutation publication

The later classification checkpoint has now been integrated as claims 0064–0069, with six result-centered expositions and the complete linked A₅ permutation-top source chain. The regular/transitive extraspecial and Camina counts, orbit pairing, residual-graph theorem, abelian/zero-graph nilpotent structural parameters and odd-top PSL₂ exclusions are public. The finite 88-orbit certificate was rerun and returned 500 substitutions, 12,400 forms and 88 orbits. The [source crosswalk](classification-source-map.json) identifies the inspected checkpoint.

This closes the previously noted public-proof gap for those counts and provides their A₅ permutation-top dependencies. It does not close older public-coverage gaps in unrelated Bruck, odd-envelope or primitive-action branches, nor certify the complete source chain mathematically. Nonzero-graph normalization remains an open theorem, not a published exhaustion result.
