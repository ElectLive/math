# References

Source key **ALGEBRA.SIMPLE_PROPER_BOL**; stable problem ID **0323**.

## Sources

Primary construction baselines below; scope and review limits are recorded separately.

### N07

Gábor P. Nagy, *A class of simple proper Bol loops*, arXiv:math/0703919v1, 30 March 2007.
[Primary version](https://arxiv.org/html/math/0703919v1).
- §1: left/right Bol conventions, proper meaning non-Moufang, and comparison with the finite simple Moufang classification.
- §2: Bol folders, multiplication groups and normal-subloop arguments.
- §§3–4: exact-factorization construction and simple proper examples.

Used as a construction baseline, not a complete classification. The abstract's historical existence question is answered by the paper itself and must not be repeated as still open.

### N07E

Gábor P. Nagy, *A class of finite simple Bol loops of exponent 2*, arXiv:0709.4544v1, 28 September 2007.
[Primary version](https://arxiv.org/html/0709.4544v1).
- Abstract and §1: infinite right-Bol exponent-2 family; right multiplication group an extension of an elementary abelian 2-group by S5; smallest member of this family has order 96.
- §§3 and 5: initial construction and infinite family.

Translate right to left using the opposite operation, as specified in PROBLEM.md. Use N07 §1 for the standard Bol identities rather than copying ambiguous or typographically suspect formulas from rendered sources. The 96 statement is family-specific.

## Source and review limits

The separately owned [graph-native-loop continuation](../graph-loops/README.md) records
its additional references in the canonical
[Bruck/Eisenstein manuscript](../graph-loops/manuscripts/graph-eisenstein-loops.md#references-and-verified-scope),
[binary cubic manuscript](../graph-loops/manuscripts/graph-cubic-loops.md#8-literature-and-exact-dependency-scope),
and [subloop manuscript](../graph-loops/manuscripts/graph-associative-subloops.md#references).
These include Kepka's Bruck construction, Hsu/Vojtechovsky and
Morier-Genoud--Ovsienko for cubic methods, He--Qiao Proposition 1.2 for graph
alternating-map recovery, and the Bei et al./Qiao isotropic-space baselines.
It proves the loop identities directly and states external dependencies and
the bounded novelty-audit scope. It does not amend the classification intake.

The [decomposition continuation](README.md) retains precise source
versions and locators in its four canonical manuscripts:

- [Central Bruck decomposition](manuscripts/bruck-extension-decomposition.md#references-and-novelty-scope):
  Wilson's centroid and adjoint-idempotent methods, arXiv:1005.0548v1,
  Sections 5.2–5.3, and arXiv:0801.3434v2, Theorem 4.4/Corollary 4.5.
- [Intrinsic deletion](manuscripts/loop-deletion-decks.md#references-and-verification-scope):
  He–Qiao arXiv:2003.07200v2, Proposition 1.2 over any field, and Kelly's 1957
  subgraph-counting and tree-reconstruction theorem. No unknown graph class
  is asserted reconstructible.
- [Associative-subloop census](manuscripts/loop-deck-subloop-census.md):
  Qiao's isotropic-space polynomial, Tittmann–Averbouch–Makowsky
  arXiv:0812.4147v2, Theorem 27, and Kotek–Preen–Tittmann
  arXiv:1207.2430v1, Corollary 11/equation (5). The manuscript supplies its own
  isolate-aware component-count proof and the exact loop-specific transforms.
- [Defect graphs](manuscripts/loop-defect-graphs.md#references):
  Stanovský–Vojtěchovský's associator and extension framework, official LOOPS
  documentation, Britten's power-graph theorem, associating hypergraphs, and
  Griggs–Širáň–Richter's Moufang Cayley graphs. PR #431/#440 dependencies are
  pinned separately, with existing results distinguished from new consequences.

This source audit is bounded. Complete conventional proofs and exact-source
independent review do not establish exhaustive historical priority, universal
classification, or reconstruction from unaligned data beyond the stated families.

These two primary versions were inspected for problem intake on 2026-11-13. Their arguments have not been independently re-proved or formalized in this workspace. A comprehensive subsequent-literature audit, including equivalences and possible overlaps among constructions, remains a first research obligation. No claim that every narrower classification question remains open is made.

Mira's request fixes the unrestricted non-Moufang classification as its own problem rather than an instance of a Moufang classification or a generic discovery-engine benchmark.

## JS: simple Bol permutation rank

Johnson–Smith, On the smallest simple, unipotent Bol loop, §§1.1,2.1 ([author PDF](https://jdhsmith.math.iastate.edu/math/BolBoolf.pdf)). The full multiplication-group double-transitivity question is adopted; the precise loop-character-theoretic conjugacy bridge requires checking before an equivalence claim.
