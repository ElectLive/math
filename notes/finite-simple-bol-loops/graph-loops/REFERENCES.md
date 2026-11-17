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

The separately owned [graph-native-loop continuation](README.md) records
its additional references in the canonical
[Bruck/Eisenstein manuscript](manuscripts/graph-eisenstein-loops.md#references-and-verified-scope),
[binary cubic manuscript](manuscripts/graph-cubic-loops.md#8-literature-and-exact-dependency-scope),
and [subloop manuscript](manuscripts/graph-associative-subloops.md#references).
These include Kepka's Bruck construction, Hsu/Vojtechovsky and
Morier-Genoud--Ovsienko for cubic methods, He--Qiao Proposition 1.2 for graph
alternating-map recovery, and the Bei et al./Qiao isotropic-space baselines.
It proves the loop identities directly and states external dependencies and
the bounded novelty-audit scope. It does not amend the classification intake.

These two primary versions were inspected for problem intake on 2026-11-13. Their arguments have not been independently re-proved or formalized in this workspace. A comprehensive subsequent-literature audit, including equivalences and possible overlaps among constructions, remains a first research obligation. No claim that every narrower classification question remains open is made.

Mira's request fixes the unrestricted non-Moufang classification as its own problem rather than an instance of a Moufang classification or a generic discovery-engine benchmark.

## JS: simple Bol permutation rank

Johnson–Smith, On the smallest simple, unipotent Bol loop, §§1.1,2.1 ([author PDF](https://jdhsmith.math.iastate.edu/math/BolBoolf.pdf)). The full multiplication-group double-transitivity question is adopted; the precise loop-character-theoretic conjugacy bridge requires checking before an equivalence claim.
