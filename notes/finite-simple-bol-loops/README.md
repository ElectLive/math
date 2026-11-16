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

## What has been achieved

The **[current research catalogue](CURRENT_RESULTS.md)** is the main guide to the broader programme. It includes:

- An all-field classification for paired PSL₂ canonical envelopes, with an explicit endpoint table for every prime power q and path length k.
- A complete paired A₅/PSL₂(7) matrix classification for arbitrary factor multiplicities, and mixed families outside the exact-factorization-isotope and Bruck-isotope routes.
- Intrinsic graph recognition of exact-factorization witnesses, plus restrictions on nonpaired inversion.
- Odd class-two parameterizations, isotope orbits, monolithic constructions and unbounded solvable complexity.
- Elementary S₅ Bruck parameters, uniform exclusions of specified radical families, and the remaining actual nonsplit lifting problem.
- Affine-subgroup classifications and scoped SD/TW primitive-group exclusions.

These are differently scoped results, not one completed classification. The catalogue distinguishes recorded model reviews from new unreviewed appendices and links the mathematical sources and controls. **Start there for achievements and concrete collaboration targets.**

## One milestone: a simple Bol loop outside two familiar classes

Nagy's *Some remarks on simple Bol loops* (2008), §6 Problem 1, asks whether
there exists a finite simple proper Bol loop that is **neither a G-loop nor
isotopic to a Bruck loop**. Here a G-loop is isomorphic to every one of its loop
isotopes, and proper means non-Moufang.

The [rigid-center construction](packet/manuscripts/odd-rigid-center-nongloop.md)
proposes such an example of order \(3^{75}19^3\). This existence result is one
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

## Start here

- [Selected results and constructions](RESULTS.md): precise statements and public sources.
- [Classification map](CLASSIFICATION.md): what the branches mean and how they fit.
- [Open problem board](OPEN_PROBLEMS.md): specific structural questions and useful deliverables.
- [Collaboration protocol](CONTRIBUTING.md): how to contribute proofs, constructions, counterexamples, and reviews.
- [Evidence and publication policy](VERIFICATION.md): exactly what a review label means.

## Conventions

A loop has an identity and unique left and right division. We use the **left Bol
identity**

\[
x\bigl(y(xz)\bigr)=\bigl(x(yx)\bigr)z.
\]

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
