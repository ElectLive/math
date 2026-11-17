# Exceptional full multiplication socles: completing E₆ and E₇

**Mira Cult**

## Statement and scope

Let Q be a finite simple proper left Bol loop, M its full multiplication group, and S the socle of M. Subject to the canonical-folder, almost-simple full-group, finite-group classification and embedding inputs specified in the proofs, S is not E₆(q), ²E₆(q), or E₇(q), for any field parameter for which the indicated socle is nonabelian simple.

Together with the earlier [exceptional-family exclusions](0090-exceptional-full-socle-exclusions.md), this completes the exceptional Lie-type full-socle branch under those inputs. It does not prohibit exceptional groups as sections of a different envelope, classify arbitrary canonical groups, or classify loop operations.

## Why original marks matter

Write G=LMlt(Q), I=M₁, and H=G∩I. The actual action gives M=GI. The exceptional factorization reductions force the socle-containing branch S≤G in the cases treated here. The canonical inversion τ gives a conjugacy-invariant set Λ of outside involutions satisfying

```math
|\Lambda|=[G:H],\qquad H\cap\Lambda^2=\{1\},\qquad G=\langle\tau\Lambda\rangle.
```

These conditions act together. A square of a selected class that contains an internal involution prevents H from meeting that class. Meanwhile the size of the selected union is exactly an index, not an arbitrary upper bound. Generation restricts the possible outer labels. Passing to a quotient and treating the projected marks as a loop section would discard these constraints.

## Proof organization

For characteristic-two E₆ and ²E₆, the argument first treats the diagonal-free graph classes. Root witnesses and maximal-order restrictions exclude the possible selections. The remaining diagonal extensions are handled in the original group, retaining stabilizer-surjectivity and the actual semilinear labels. The complete proofs are [diagonal-free E₆](../sources/full-socle-completion/e6-even-diagonal-free-socles.md), [split E₆](../sources/full-socle-completion/untwisted-e6-even-full-socles.md), and [twisted E₆](../sources/full-socle-completion/twisted-e6-even-full-socles.md).

In odd characteristic, the [graph-class argument](../sources/full-socle-completion/e6-odd-graph-full-socles.md) treats all twisted E₆ and the graph-only split cases. The remaining split square-field case requires a separate [semilinear proof](../sources/full-socle-completion/e6-odd-semilinear-full-socles.md). Odd-central lifting and Lang's theorem determine the actual classes and fixed-group denominators. Class-square witnesses force H∩S to have odd order. Valuations exclude most selected unions uniformly. In the residual valuation case, exact outer-label generation leaves finitely many polynomial patterns. A nonzero resultant and coefficient bounds prove a finite field-size bound; an exact certificate checks that bounded remainder. This is not extrapolation from tested fields.

For odd E₇, the [two-class diagonal argument](../sources/full-socle-completion/e7-odd-diagonal-union.md) and [single-class completion](../sources/full-socle-completion/e7-odd-diagonal-canonical.md) precede the [full-socle assembly](../sources/full-socle-completion/e7-odd-full-socles.md). Rational torus witnesses, Sylow-preimage bounds, actual field classes and the mixed index-two extension are all needed. The odd-field theorem combines with the earlier even-field exclusion.

## Evidence boundary

These are conditional research theorems with independent model mathematical reviews at their recorded exact sources. Root and arithmetic certificates check specified finite identities and bounded remainders, not the imported classifications. They are not human-refereed or formally verified results. The source and publication records retain the exact review and computation scopes. The remaining classical groups and surviving operations are separate problems.
