# Evidence and publication policy

**Latest completed batch:** [17 November full-socle publication](PUBLICATION-2026-11-17.md). The dated checks below describe the earlier mirror, not this later batch.

The public workspace distinguishes:

- **Classical imported theorem:** an existing published result, with exact locator.
- **Proof draft:** a proposed new argument available for inspection.
- **Scoped model review:** a separate model examined named statements at a named revision.
- **Reproduced finite check:** a stated command and input were rerun; this does not certify a universal theorem.
- **Human expert review:** only claimed when a named, consenting expert actually supplied it.
- **Formal verification:** only claimed for an identified theorem checked by a specified kernel and imports.

These labels are not a single confidence ladder. A computation cannot repair a
missing universal argument; a proof review does not establish novelty; a source
statement can change after the reviewed revision.

## Release gate for each result

Before describing an entry as a self-contained public proof package, include its complete proof
dependencies or immutable accessible public references. A research milestone may be
listed before that closure is complete only if its statement and source are available,
its missing inputs are identified, and it is explicitly labeled a reported result or
conditional assembly rather than a fully auditable public proof. Proposed continuations
must remain separately labeled. Record the source commit,
exported file hashes, transformations made during export, exact reviewed source
revisions, and this release's audit limits. Do not publish an inaccessible private
link as a substitute for an argument.

Read every exported file for unrelated private content and credentials. Do not
export raw conversations, private collaborator information, or speculative
projects merely because they share a source workspace. Preserve mathematical
counterexamples and limitations relevant to the published claims.

The source research remains active. A public snapshot is not a claim that every
later branch update is covered by its review. Corrections should name the affected
statement and revisions and explain whether downstream results change.

## Intrinsic and analytic continuation, 2026-11-16

See the [self-contained nonisomorphism writeup](INTRINSIC_NONISOMORPHISM.md) and [public proof, code, review and validation package](analytic-2026-11-16/README.md). Claims 0079–0081 concern explicit reciprocal families, not an unrestricted classification. The package records the exact limitations, remaining analytic questions, and successful complete-checkout integrity checks separately from model mathematical reviews.
