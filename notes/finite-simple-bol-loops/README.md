# Finite simple Bol loops: a collaborative classification project

The objective is a structural classification of finite simple Bol loops up to
isomorphism. This public workspace presents selected constructions, their proof
dependencies, and concrete gaps where collaborators can make progress.

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

## Two complementary proof routes

- [Direct existence proof](simple-existence-proof.md): a specialized construction and lemmas for the non-G-loop/no-Bruck-isotope example, without a general class-two exhaustion theorem.
- [Original class-two framework](packet/manuscripts/odd-class-two-classification.md) and [original construction](packet/manuscripts/odd-rigid-center-nongloop.md): the broader route that led to the example. The framework is retained as a proof draft; the release audit does not certify its full exhaustion theorem.

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
