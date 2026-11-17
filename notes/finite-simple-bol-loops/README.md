# Finite simple Bol loops

## Reviewed full-socle checkpoint, 17 November 2026

The newest completed publication advances whole full-multiplication-group families, not just isolated canonical groups. All conclusions retain their explicit canonical, classification, embedding and finite-data inputs. The unrestricted classification and the surviving natural-action loop operations remain open.

- [0087: Alternating full socles force the natural action](manuscripts/0087-alternating-natural-full-action.md), without assuming solvable LMlt.
- [0088: All 26 sporadic full socles excluded](manuscripts/0088-sporadic-full-socle-exclusion.md).
- [0089: PSL₂ and odd-dimensional PSL/PSU full socles excluded](manuscripts/0089-classical-full-socle-exclusions.md).
- [0090: Exceptional full-socle exclusions](manuscripts/0090-exceptional-full-socle-exclusions.md), including all F₄ and G₂.
- [0091: Odd-kernel collision lifting and canonical center constraints](manuscripts/0091-original-mark-collision-tools.md).

The [publication record](PUBLICATION-2026-11-17.md) fixes the completed source boundary, correction history, checks and remaining gaps. Later E₆/²E₆ and odd-E₇ work is not included. Earlier dated status passages below are historical where superseded by this checkpoint.


This research aims at a structural classification
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

## Current classification checkpoint

The [latest classification results](RESULTS.md#latest-classification-advances) include the odd alternating full-group theorem, the solvable-left-group full-action reduction, paired alternating classifications, and the specified two-N Bruck exclusion. Complete proofs, assumptions, pending continuations and code are linked through the [source index](sources/README.md). These are structural advances, not completion of the general classification.

## What we have achieved

The project has developed constructions and classifications in several branches:

- A proposed finite simple proper Bol loop that is neither a G-loop nor isotopic to a Bruck loop, addressing Nagy's existence question below.
- Classifications for specified radical-free envelopes, including PSL₂(q)-power and nonpermuting A₅-socle cases. The [all-path structural theorem](manuscripts/0068-abelian-nilpotent-path-parameters.md) now covers every odd abelian top, and the zero-residual-graph nilpotent branch, in the pure A₅ factor-permutation model.
- Structural results for odd-order, Bruck, affine and primitive-action branches, including families with unbounded group-theoretic complexity and concrete restrictions on possible envelopes.

Each result has specific hypotheses and review status. See the [research catalogue](RESULTS.md) for precise statements, sources and limitations. These are not a classification of all finite simple Bol loops.

## Open problems

- **Classify the remaining factor-permuting cases.** Parameterize nonzero residual graphs without changing the group or loop data; settle nonsurjective nonnilpotent tops and general outer actions. Evaluate further admissible affine-data families where useful.
- **Go beyond the known socle models.** Identify or classify simple Bol loops with canonical envelopes outside the PSL₂ and A₅ families already studied.
- **Resolve nonsplit Bruck lifting.** Prove or refute compatibility of the actual extension, inversion, stabilizer and section data in the remaining cases.
- **Make odd-layer reductions exhaustive.** Turn the current compression and extension constraints into classifications without losing multiplicity or cohomological data.

The [open problems](OPEN_PROBLEMS.md) give precise statements and starting points.

## One milestone: a simple Bol loop outside two familiar classes

Nagy's *Some remarks on simple Bol loops* (2008), §6 Problem 1, asks whether
there exists a finite simple proper Bol loop that is **neither a G-loop nor
isotopic to a Bruck loop**. Here a G-loop is isomorphic to every one of its loop
isotopes, and proper means non-Moufang.

The [rigid-center construction](packet/manuscripts/odd-rigid-center-nongloop.md)
proposes such an example of order $`3^{75}19^3`$. This existence result is one
contribution to the broader classification programme: it shows why those two
classes alone cannot suffice, if the argument is accepted. The
[construction discussion](0018-non-g-loop-non-bruck-context.md) gives its precise status.

Two presentations are available for readers investigating this result:

- [Direct existence proof](0018-non-g-loop-non-bruck-existence.md): a specialized construction
  with the lemmas needed for this example, independent of a general class-two
  exhaustion theorem.
- [Original class-two framework](packet/manuscripts/odd-class-two-classification.md)
  and [original construction](packet/manuscripts/odd-rigid-center-nongloop.md):
  the broader approach through which the example was discovered. The framework
  is retained as a proof draft; the release audit does not certify its full
  exhaustion theorem.

## Research reference

- [Start here](START_HERE.md): orientation and reading paths for human and AI researchers.
- [Shared references](REFERENCES.md): literature and tools for researchers and their AI systems. Suggestions are welcome; a link and a sentence are enough.
- [Results](RESULTS.md): constructions, subclass classifications and structural restrictions.
- [Claim index](CLAIMS.md): stable claim IDs, exact scopes and supporting proofs.
- [Classification map](CLASSIFICATION.md): what the branches mean and how they fit.
- [Open problem board](OPEN_PROBLEMS.md): specific structural questions and useful deliverables.

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

The writeups state the hypotheses and proof dependencies of each result. Some supporting arguments remain to be made fully self-contained in this collection.

This is AI-assisted research. It has not been human refereed or formally verified; novelty must be assessed separately from correctness.

## Intrinsic and analytic continuation, 2026-11-16

See the [self-contained nonisomorphism writeup](INTRINSIC_NONISOMORPHISM.md) and [public proof, code, review and validation package](analytic-2026-11-16/README.md). Claims 0079–0081 concern explicit reciprocal families, not an unrestricted classification. The package records the exact limitations, remaining analytic questions, and successful complete-checkout integrity checks separately from model mathematical reviews.


## Sparse quantum randomization

The [quantum randomization manuscript](analytic-2026-11-16/manuscripts/bol-quantum-randomization.md)
determines when actual reciprocal Bol operations can randomize a quantum state.
Every degenerate sector has a stationary-state obstruction for every native
distribution. A fixed nondegenerate family has a sharp threshold for the number
of native generators needed to have a scalar common commutant. An explicit
small-bias construction using actual translated defects gives arbitrary-state
trace-norm randomization with one operation and constant quantum depth on
fixed-size qudits. A matching Weyl control has the same physical channel and
resource costs, so no general Bol-specific efficiency advantage is claimed.

The [local claim record](claims/quantum-randomization.md) separates the exact
statements and scope. The [reproducibility and review record](analytic-2026-11-16/evidence/bol-randomization-reproducibility.md)
pins the scientific revision and the independent mathematical and resource
reviews accepting it within their stated scopes. These
results concern specified reciprocal families, not a classification of finite
simple Bol loops.
