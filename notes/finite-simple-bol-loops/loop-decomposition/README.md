# Loop decomposition and intrinsic deletion decks

Mira Cult

The [graph-native loop construction](../graph-loops/README.md) leads to two distinct results: a decomposition theorem for a broader class of central Bruck loops, and an intrinsic deck whose reconstruction problem is exactly graph reconstruction in the recognized graphical family. The latter is an equivalence, not a solution of the conjecture.

## Decomposition beyond graphs

Let L be a finite Bruck loop of prime exponent p. Assume its associator subloop A is central and its induced associator D:(L/A)³→A is trilinear. Then both A and L/A are elementary abelian p-groups. The common radical and primitive idempotents of the centroid of D determine an intrinsic decomposition

```math
L\cong C_p^{\,d}\times\prod_i L_i,
```

where each L_i is nonassociative and directly indecomposable. The integer d and multiset of factor isomorphism types are intrinsic. These factors are realized as actual subquotients of L, not merely as formal tensor blocks. The proof includes primes two and three. It does not presume that every trilinear tensor integrates to a Bruck loop.

The underlying extension-rigidity theorem does not require trilinearity: two prime-exponent central Bruck extensions with the same specified elementary abelian quotient and kernel and the same associator function are isomorphic by an isomorphism inducing the identity on quotient and kernel.

In the original one-marker construction, every nonzero full radical-free alternating map gives a directly indecomposable nonassociative core. A disconnected graph therefore need not produce a direct product. Its pieces instead share a marker through a fiber product, with central quotients when outputs overlap. A component-marker modification restores an unmarked faithful graph functor carrying disjoint unions to direct products.

[Complete extension and decomposition proof](manuscripts/bruck-extension-decomposition.md).

## An intrinsic deck, with an exact boundary

At a fixed prime p≠3, admissible markers and independent associator frames can be recognized from multiplication in the graphical Bruck family. Every admissible choice, including arbitrary lifts, gives the same **multiset of abstract deletion-card types**. Embedded card subloops are not canonical.

For graphs with at least three vertices, reconstructing the parent from this deck, with competitors restricted to the same recognized graphical family, is equivalent to ordinary vertex-deleted graph reconstruction. Multiplicities are retained. This supplies a precise algebraic formulation; it does not eliminate the remaining alignment/gluing problem.

A central identification in a matching gives a nongraphical competitor with the same coordinate cards. This disproves a naive enlarged-family gluing principle, but the parent orders differ, so it does not settle the same-order enlarged-family question. The broader all-hyperplane deck detects that collision and reconstructs the stated scalar alternating-form loop family; this is a different deck and not a new reconstructible graph class.

[Recognition, deck equivalence and gluing obstruction](manuscripts/loop-deletion-decks.md).

## What can already be recovered

For every finite loop, translated associativity-defect graph components are precisely the cosets of its normal associator subloop, yielding its universal group quotient. For the central alternating-map Bruck family, two intrinsic defect relations recover the elementary abelian central direct-factor rank. Explicit collisions show that these matrices do not determine arbitrary loops.

For graphs on n≥3 vertices at a fixed prime p≠3, the unaligned graphical deck determines counts of **all** associative subloops by order, not only those containing the associator subgroup, and the maximal-associative counts. These are explicit transforms of established reconstructible graph component data. A concrete pair has identical full associative census at every allowed prime but different maximal counts.

[Defect graphs and quotient proof](manuscripts/loop-defect-graphs.md) · [Deck subloop census proof](manuscripts/loop-deck-subloop-census.md).

## Evidence and remaining work

[Publication record](PUBLICATION.md) · [Independent research reviews](evidence/loop-decomposition-review.md) · [Executable checks](code/README.md) · [References](REFERENCES.md) · [Public claim 0093](../claims/0093.md).

The decisive reconstruction obligation is to derive compatible domain/output alignments and central intersections from the unaligned card multiset, or prove parent uniqueness without recovering them. Listing simple factors does not determine extension data. No unrestricted Bol decomposition, finite-simple classification, general graph reconstruction theorem or exhaustive novelty claim is asserted.
