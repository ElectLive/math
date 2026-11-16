# Finite simple Bol loops: a collaborative classification project

This is a collaborative research programme aimed at a structural classification
of **all finite simple Bol loops up to isomorphism**. The goal is to identify the
families and exceptional cases, prove that they exhaust the possibilities, and
determine exactly when two constructions give isomorphic loops.

The programme combines new constructions, classifications of precisely defined
subclasses, and structural reductions that constrain the remaining cases. This
workspace collects those results and their proof sources, maps the open gaps,
and provides concrete problems for collaborators. No single construction or
proof route defines the scope of the project.

**The unrestricted classification is not complete.** A procedure that searches
all finite tables or tests all possible extension data is not, by itself, the
structural classification sought here.

## What we have achieved

The project has developed constructions and classifications in several branches:

- A proposed finite simple proper Bol loop that is neither a G-loop nor isotopic to a Bruck loop, addressing Nagy's existence question below.
- Classifications for specified radical-free envelopes, including PSL₂(q)-power and nonpermuting A₅-socle cases; constructions and classifications also treat several factor-permuting cases.
- Structural results for odd-order, Bruck, affine and primitive-action branches, including families with unbounded group-theoretic complexity and concrete restrictions on possible envelopes.

Each result has specific hypotheses and review status. See the [research catalogue](CURRENT_RESULTS.md) for precise statements, sources and limitations. These are not a classification of all finite simple Bol loops.

## What collaborators can do

- **Classify the remaining factor-permuting cases.** Determine the isomorphism orbits in the surviving exponent-25 extraspecial-top case and extend the analysis to broader regular tops.
- **Go beyond the known socle models.** Identify or classify simple Bol loops with canonical envelopes outside the PSL₂ and A₅ families already studied.
- **Resolve nonsplit Bruck lifting.** Prove or refute compatibility of the actual extension, inversion, stabilizer and section data in the remaining cases.
- **Make odd-layer reductions exhaustive.** Turn the current compression and extension constraints into classifications without losing multiplicity or cohomological data.

The [starter tasks](STARTER_TASKS.md) and [open problem board](OPEN_PROBLEMS.md) have more detail and links to the relevant work. References, counterexamples, constructions and ideas for attacking these questions are all welcome; see [how to contribute](CONTRIBUTING.md).

## One milestone: a simple Bol loop outside two familiar classes

Nagy's *Some remarks on simple Bol loops* (2008), §6 Problem 1, asks whether
there exists a finite simple proper Bol loop that is **neither a G-loop nor
isotopic to a Bruck loop**. Here a G-loop is isomorphic to every one of its loop
isotopes, and proper means non-Moufang.

The [rigid-center construction](packet/manuscripts/odd-rigid-center-nongloop.md)
proposes such an example of order $`3^{75}19^3`$. This existence result is one
contribution to the broader classification programme: it shows why those two
classes alone cannot suffice, if the argument is accepted. The
[result and review summary](RESULTS.md) gives its precise status.

Two presentations are available for readers investigating this result:

- [Direct existence proof](simple-existence-proof.md): a specialized construction
  with the lemmas needed for this example, independent of a general class-two
  exhaustion theorem.
- [Original class-two framework](packet/manuscripts/odd-class-two-classification.md)
  and [original construction](packet/manuscripts/odd-rigid-center-nongloop.md):
  the broader approach through which the example was discovered. The framework
  is retained as a proof draft; the release audit does not certify its full
  exhaustion theorem.

Scoped AI review found no defect in the example's argument. That is not human
refereeing, formal verification, or a certification of historical novelty.

## Research reference

- [Start here](START_HERE.md): orientation and reading paths for human and AI researchers.
- [Research workflow](RESEARCH_WORKFLOW.md): how to use the sources, review statuses and computational evidence.
- [Shared references](REFERENCES.md): literature and tools for researchers and their AI systems. Suggestions are welcome; a link and a sentence are enough.
- [Research catalogue](CURRENT_RESULTS.md): detailed results, public sources and review status.
- [Classification map](CLASSIFICATION.md): what the branches mean and how they fit.
- [Open problem board](OPEN_PROBLEMS.md): specific structural questions and useful deliverables.
- [Collaboration protocol](CONTRIBUTING.md): how to contribute references, proofs, constructions, counterexamples, and reviews.
- [Evidence and publication policy](VERIFICATION.md): exactly what a review label means.

## Conventions

A loop has an identity and unique left and right division. We use the **left Bol
identity**


```math
x\bigl(y(xz)\bigr)=\bigl(x(yx)\bigr)z.
```


Passing to the opposite operation gives the corresponding right Bol loop and
preserves simplicity and isomorphism classes. It does **not** assert that a loop
is isomorphic to its opposite. "Proper Bol" here means non-Moufang. A G-loop is a
loop isomorphic to each of its loop isotopes. "Has a Bruck isotope" is a separate
property, not a synonym for being Bruck.

The full multiplication group `Mlt(Q)` and the left multiplication group `LMlt(Q)`
are different objects. Primitivity claims about one must not be silently applied
to the other.

## Publication scope

This is a curated public research workspace, not a dump of private discussions or
an assertion that every branch of the internal project is correct. A construction
belongs in the results catalogue only when its statement, complete public proof
dependencies, reproducible inputs where relevant, and exact review scope are
available here. An omitted item is not necessarily disproved or abandoned.

The work uses AI-assisted conjecture generation, proof development, and review.
Model reviews are not human expert refereeing or formal verification. Contributors
are welcome to challenge any argument, including the reductions used to organize
the project. Novelty must be assessed separately from correctness.
