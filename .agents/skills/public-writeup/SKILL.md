---
name: public-writeup
description: Turn mathematical research into coherent public Markdown writeups and research workspaces, with precise results, complete proof dependencies, meaningful open problems, references, stable claim identifiers, and checked rendering. Use for an assigned public-publication or mirroring pass in Mira-Cult/math, not for intermediate math-wip research, a formal journal-paper workflow, or a verbatim internal archive.
---

# Public research writeups

Write mathematics for a reader, not a transcript of how the workers produced it.
The public workspace is a coherent account of what is known and what remains to
be understood. Collaboration does not require a special genre of exposition.

## Publication boundary

This skill lives in `Mira-Cult/math` and belongs to a deliberate public-publication
or mirroring pass. An intermediate research edit, source milestone, or research PR
in `Mira-Cult/math-wip` does not trigger a public writeup, hosted-rendering pass,
or public-repository PR. Research workers finish their assigned proof, evidence,
and handoff work in math-wip; the publication owner coordinates public updates.
Existing authorized mirroring commitments remain in force. Batch public exposition
and rendering checks at publication checkpoints rather than repeating them after
every intermediate change. Follow the assigned publication workflow; do not open
a public PR merely because the skill was discovered.

## Establish scope before rewriting

Read the repository instructions, relevant problem contract, claim records,
proofs, references, code and review evidence at identified revisions. Inspect
the actual public destination and a few relevant existing writeups. Do not
infer a result from its filename, a worker's summary or a successful test.

Separate the mathematical assertions from their evidence:
- theorem with a complete conventional proof;
- theorem conditional on explicitly stated inputs;
- construction or computation with a stated finite range;
- proof draft with an identified gap;
- conjecture or research direction.

A restricted parameterization is not a full classification. A list of tested
instances is not an exhaustion theorem. Formalization, finite replay and
mathematical review have different scopes. Preserve these distinctions while
removing administrative clutter.

Build a private source-to-public crosswalk: claim, source revision and location,
public statement/proof location, dependencies, evidence and known gaps. Retain
the internal originals and review records. Do not publish private discussions,
credentials or unrelated material simply because it appears nearby.

## Choose a mathematical unit, not a historical unit

First outline the mathematics without referring to the old file layout.
Group lemmas around the theorem or construction they explain.

**One manuscript normally covers one coherent result or closely connected
family of results**, with enough definitions and proofs to read it continuously.
A useful short construction can be a single note. A larger programme needs
several focused manuscripts and a short overview, not one enormous dump.

Combine incremental improvements, repeated setup and dependent lemmas when the
combined argument is clearer. Split when the questions, assumptions, methods
or audiences genuinely differ, or an independently useful theorem would
otherwise be buried. Do not make one file per worker, session, claim, review
or proof step. Conversely, do not collapse genuinely different statements
merely because they came from the same project.

Keep complementary proof routes when they teach different mathematics: for
example a direct existence proof and the broader structural framework that
first produced it. Explain their relationship and different scopes, rather
than presenting them as competing versions of the same page.

## Write the research account

A typical manuscript contains the following material, with headings adapted
to the mathematics rather than imposed as a rigid template:

1. **Problem and context.** The exact question, why it matters, relevant known
   results and what this note contributes.
2. **Results obtained.** Precise theorems or constructions with quantifiers,
   conventions, hypotheses, ranges and exceptions. State the strongest
   supported result, not the aspiration.
3. **Mechanism and proof.** Explain the key idea, define the objects, then give
   the lemmas and argument in dependency order. Include illuminating examples
   and boundary cases. A proof guide must not masquerade as a complete proof.
4. **Consequences and limitations.** What follows, what does not, and which
   restrictions are structural rather than artifacts of the proof.
5. **Open problems.** Specific unresolved questions arising from these results,
   if there are substantive ones.
6. **References and reproducibility.** Usable bibliography and source/check
   instructions appropriate to the result.

Give full accessible proof dependencies or precise citations. A private link
is not a public proof dependency. Supply authorized necessary source, replace
it with a self-contained argument, or state the unresolved dependency honestly.
Keep executable generators, inputs and build recipes sufficient for the
claims about computation; do not equate source availability with a rerun.

This is a **research writeup/workspace**, not necessarily a formal paper.
A later paper may have an abstract, a selected narrative, journal conventions,
LaTeX/PDF production and a submission workflow. Do not require those to make
a useful public research account; do not duplicate the separate paper-writing
workflow. A workspace can also record precise open questions, current scope
and reusable source beyond a paper's chosen thesis.

## Organize the public workspace for both audiences

Use one canonical front page and one authoritative catalogue. The front page
should answer: **What have we achieved? What important work can I do next?**
Give short mathematical summaries, links to full proofs, and the research
objective. Do not lead with release machinery or a wall of disclaimers.

The catalogue should cover the published claims and distinguish their scopes.
For AI and specialist readers, provide navigable definitions, dependencies,
complete writeups, references and reproducible sources. These support the
human-facing page; they need not be copied into it.

Avoid parallel CURRENT_RESULTS/RESULTS catalogues, repeated status tables,
empty scaffolds, and “legacy” pages created during the first publication.
Choose names that describe the mathematics. When relocating an established
public URL, preserve a short redirecting note if needed, not a second competing
canonical exposition.

An open problem must state the objects and assumptions, the exact desired
conclusion or counterexample, the known boundary and why solving it advances
the programme. Separate subproblems when their answers differ. “Contribute a
reference,” “review our work” and routine maintenance are contribution routes,
not mathematical open problems. Put reference invitations beside the public
bibliography or in brief contribution guidance.

## Claim IDs and provenance

Where indexed manuscripts are requested, use stable four-digit claim prefixes,
such as `0007-descriptive-result.md`. Inspect the existing registry first.
Do not silently renumber, reuse or allocate someone else's reserved ID.

A claim ID identifies a mathematical assertion, not an author or a file.
A combined manuscript may contain several indexed claims; a claim may have
two complementary proof routes. Record this mapping explicitly in the
catalogue/crosswalk. An omnibus open claim does not lend its ID to all later
results. If a public namespace differs from internal IDs, label the distinction
and maintain a crosswalk; never imply a newly assigned number was the original
internal claim ID.

Use the agreed collective authorship, **Mira Cult**, for the project's own
public exposition. Preserve third-party attribution, citations and licenses.
Remove worker names, internal agent roles, handoff instructions, redaction
placeholders and review-management chatter from the mathematical narrative.
Keep recoverable internal provenance separately. Do not remove mathematical
caveats along with the chatter, or invent human review, independent review,
formal verification or historical priority. Put concise, accurate evidence
details where readers need them, without repeating them on every paragraph.

### Acknowledge model contributions

Keep the human byline separate from the account of how the work was done.
When models contributed, give readers a concise acknowledgment that names
the provider and model/version for each known contribution and says what
it contributed (for example, finding a proof, writing the paper or checking
an argument). Describe the human author’s guidance where established.
Use the author’s account or another reliable record; do not infer a model
identity from an agent name or invent an assignment. If a model or role
cannot be verified, acknowledge the assistance at the level actually known.
Keep the published acknowledgment consistent across the source and PDF.

## Validate the actual publication

Before publication, check theorem statements against their sources after
consolidation, dependencies and references, claim crosswalks, examples, and
every local link and heading anchor. Run repository integrity checks and
relevant source tests when applicable; report what was actually run.

Inspect the **rendered target pages**, not just raw Markdown or a local preview.
Check all changed prose pages, including long proofs and catalogue tables:
- formulas render with intact symbols, subscripts and delimiters;
- surrounding words have not been swallowed by math or emphasis;
- lists, tables, code, links and anchors are readable;
- there is no raw TeX, renderer error or unexpected horizontal clipping.

Use math syntax supported by the actual host. On GitHub, fenced `math` blocks
and protected inline math can avoid Markdown/TeX interactions; verify them
rather than assuming a delimiter conversion is enough. Renderer behavior can
change. Fix unsupported macros and inspect again. A clean error count alone
does not show that every intended formula and adjacent word survived.

Publish on the repository's permitted branch/PR workflow without overwriting
active work. Preserve source history. Check the published revision, links and
rendering after the push. If access or tooling prevents a rendering check,
name that exact gap; do not call it completed. Report the canonical entry
point and substantive changes, not an internal file-by-file activity log.
