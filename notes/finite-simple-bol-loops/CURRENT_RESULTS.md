# Research results: constructions, classifications and structural obstructions

This is the integrated account of the classification programme: achievements, exact scopes and important remaining questions. Read the [research front page](README.md) for a shorter overview; [Start here](START_HERE.md) and the [research workflow](RESEARCH_WORKFLOW.md) support a deeper investigation.

Statements below report the manuscripts and their recorded AI-model reviews. This reconciliation is not a fresh proof audit, human refereeing or formal verification. Exact source revisions and missing dependencies remain recorded in the supporting packets and [coverage audit](COVERAGE_AUDIT.md). The latest incorporated source is `ed03ee5a0a45d9087e0619b15b7ba5cd1806d57a`.

## 1. Radical-free envelopes: a substantial classification programme

Here the canonical group means the faithful **left multiplication group**, with its marked left translations, identity stabilizer and canonical inversion. It must not be replaced by the full multiplication group or just an abstract composition-factor list.

### Every field and every inversion for canonical PSL₂ powers

[The arbitrary-inversion assembly](advances-2026-11-16/manuscripts/radical-free-fixed-factors.md) classifies the setting where the **entire canonical group** is `G = PSL₂(q)^n`, for every prime power q≥4 and n≥1, without assuming paired inversion. Every survivor has n=2k and paired inversion, and the [path classification](update-2026-11-16/manuscripts/radical-free-psl2-path-classification.md) gives explicit endpoints and exact classes:

| q | Number of classes for each k |
|---|---:|
| Even q | 1 |
| 5 | 1 |
| 7 | 2 |
| 11 | 3 |
| 23 | 2 |
| 29 | 1 |
| 59 | 2 |
| Other odd q≡3 mod4 | 1 |
| Other odd q≡1 mod4 | 0 |

The endpoint table and subgroup hypotheses are in the manuscript. q=4 and q=5 describe the same A₅ family and must not be counted twice. The paired assembly reports three mathematical/source/code acceptances at `e30af949531c0ebcc9f7533b04fc1e7fc6858563`; the arbitrary-inversion assembly reports three at `f831fb7a9cc3c1f90c2b32b94e002b5e6d06a413`, retaining the case-specific inputs. This does **not** classify arbitrary loops merely having PSL₂ composition factors or larger canonical overgroups.

### Arbitrarily many factors, and genuinely mixed simple types

- [Path-factorization construction](update-2026-11-16/manuscripts/radical-free-path-factorizations.md): any stated exact factorization T=AB of a finite nonabelian simple group produces simple proper non-Bruck loops of order |T|^k, for every k≥1, with canonical group T^(2k). Thus a fixed bound on the number of simple factors cannot be a general strategy. The connected graph-model reduction and its external classification dependencies are separately scoped.
- [Mixed A₅/PSL₂(7) construction](update-2026-11-16/manuscripts/radical-free-mixed-simple-quotients.md): an order-10080 example already defeats a single-simple-type reduction. The base model has a separate exhaustion argument.
- [Mixed path family](update-2026-11-16/manuscripts/radical-free-mixed-paths.md): orders **60^a168^b for all a,b≥1**. Opposite parity of a,b gives neither an exact-factorization isotope nor a Bruck isotope, already at order **604800**. This is a different result from the odd non-G-loop example; no non-G-loop conclusion is inferred here. Full sources report three acceptances at `9d1c0af909166459fbbeb87b881c28dff353aa3f`, with later continuation scopes preserved.

### All-powers mixed matrix classification

[The matrix classification](update-2026-11-16/manuscripts/radical-free-mixed-matrix-classification.md) covers every A,B≥1 in the canonical model
`G = A₅^(2A) × PSL₂(7)^(2B)` with paired inversion. Construction data are path lengths and binary/ternary matrices. **Strong directed connectivity is exactly the simplicity condition.** Length-preserving path permutations and the specified ternary column signs give the exact isomorphism relation. The full proof reports three acceptances at `8aa2dc1c5f7bd3190a57118c1e7e8398587f7655`, conditional on its stated inputs. It is not a classification of arbitrary radical-free groups or all inversion actions.

### A graph test that recognizes a construction route

[The intrinsic splitting-atom graph theorem](update-2026-11-16/manuscripts/radical-free-bipartite-witness.md) recognizes exact-factorization witnesses by **bipartiteness**, in the paired semisimple setting, and establishes the corresponding isotopy invariance. It counts actual witness subgroups, not isomorphism classes. The matrix family's [weighted-cycle criterion](update-2026-11-16/manuscripts/radical-free-mixed-matrix-classification.md#independent-review-of-the-matrix-witness-criterion) sharpens this to parity equations. These give structural explanations for the mixed counterexamples, not just computations.

### A global reduction before the case split

[The general inner-inversion reduction](update-2026-11-16/manuscripts/exact-factorization-criterion.md#inner-inversion-and-the-generalized-fitting-subgroup) forces the Bruck structural regime under its conjugate-stabilizer hypothesis. In particular **O₂(G)=1 forces outer inversion**, removing inner-inversion casework from radical-free envelopes. Its three recorded acceptances at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8` retain the Bruck-isotope interface and the CFSG-dependent published Bruck theorem. It does not classify the outer inversions or radical extensions.

### The full nonpermuting A₅-socle setting

[Inversion exhaustion](advances-2026-11-16/manuscripts/radical-free-a5-code-inversion.md) and [outer-code/selected-mark classification](advances-2026-11-16/manuscripts/radical-free-a5-outer-codes.md) cover the entire setting `Soc(G)=A₅^r` in which G does not permute the simple factors, without an initial inversion assumption. The data are the pure-A₅ path or positive path lengths and a strongly connected binary matrix, modulo length-preserving simultaneous permutation. This includes the selected-mark and outer-code correlations, not just the direct-power group.

The full inversion assembly reports three reviews at `42e39c3cfbb5ded0d294a1a01fd6ab7dea8d6c0e`; the arbitrary-mark theorem reports three at `820e678f92b42fe80d9e6c47cfd7e3afe3536815`. The earlier unreviewed A₅ appendix is no longer the current status. Factor-permuting groups and other or mixed socles remain separate.

### Factor-permuting A₅ families and exact regular-top classifications

[The factor-permutation construction](advances-2026-11-16/manuscripts/radical-free-factor-permutation-construction.md) gives an order-648000 example and unbounded prime cycle lengths. Its reported review is `ad7b7d0df9910463839b2e8607fbfec3ddbe2f5e`. Thus nonpermuting results cannot finish the programme.

The following classifications concern their **displayed exact wreath-pair canonical groups and swap inversion**, not every group having the same permutation quotient:

| Regular top/model | Classification in that precise model | Source |
|---|---|---|
| Cyclic length n | Exactly n=1,3,5,15; one class of order n·60^n for each | [Cyclic tops](advances-2026-11-16/manuscripts/radical-free-a5-cyclic-top.md) |
| Every finite abelian regular top A | Exactly A≅U_a(F₃)×U_b(F₅), one class per a,b≥0; n=3^a5^b and loop order n·60^n | [Abelian tops](advances-2026-11-16/manuscripts/radical-free-a5-abelian-top.md) |
| Modular nonabelian order-27 top C₉⋊C₃, full anti-abelianization envelope | Exactly six classes of order 27·60^27 | [Modular top](advances-2026-11-16/manuscripts/radical-free-a5-nonabelian-27.md) |
| Exponent-three nonabelian order-27 top | Exactly two classes of order 27·60^27 | [Exponent-three top](advances-2026-11-16/manuscripts/radical-free-a5-extraspecial-27.md) |

Here U_e(F_p)=1+tF_p[t]/(t^(e+1)). The corresponding full-source model-review pins are `62b423556eaa751273b360f256c388859e63bb86`, `7eb6be15aa8854884eafc6f71e825d50eb149aba`, `430f1d14db2cc7f56228c8f5f2401488d4c0cf3f` and `417e94ec31bdba48c0ed4f6b18b34e69f13621f7`. Each retains its own inputs.

[The odd prime-power regular-top reduction](advances-2026-11-16/manuscripts/radical-free-a5-prime-power-top.md) gives construction, exhaustion and actual coordinate-isomorphism data for every odd p-group P in its stated model: p is 3 or 5, a cyclic module has dimension log_p|P|, and an explicit top-cocycle test remains. Review is pinned to `d17efc105793622b54eb899ccac67919a555a9f8`. It is a uniform parameterization, not a solution of all module/cocycle orbits.

[The higher-rank extraspecial theorem](advances-2026-11-16/manuscripts/radical-free-a5-extraspecial-tops.md) excludes every odd extraspecial top of rank m≥2 except order 5^5 and exponent 25, where admissible data exist. Its review is `417e94ec31bdba48c0ed4f6b18b34e69f13621f7`. **The surviving isomorphism orbits remain open.**

[Involution-support restrictions](update-2026-11-16/manuscripts/radical-free-involution-support.md) and [prime-field PSL₃ restrictions](update-2026-11-16/manuscripts/radical-free-psl3-prime-paths.md) supply further scoped exclusions and directions beyond these classifications.

## 2. Odd-order envelopes: whole families and unavoidable complexity

The [earlier catalogue](RESULTS.md) already supplies full public manuscripts for unbounded derived nilpotency class, derived length and Fitting height, matrix-pair embeddings, noncentral centers, and monolithic higher-defect constructions. These are structural constraints on any classification, not incidental examples.

The expanded source set adds:

- [Whole class-two parameters](update-2026-11-16/manuscripts/odd-class-two-classification.md): abelian bimap/action/positive-cocycle data, admissibility, normal-subgroup tests, exhaustion and exact actual-loop isomorphism criteria for the stated class-two canonical-derived-group branch, including arbitrary exponent and noncentral centers. Its manuscript reports three full reviews at `226a8dc1eb503026c350ffe3b7ac93da9077a593`; the separate publication audit did not independently certify that full closure.
- [Isotope orbits](update-2026-11-16/manuscripts/odd-class-two-isotope-orbits.md): the rigid-center example has exactly **three** isotope isomorphism classes under the reviewed interfaces, not merely two distinguishable presentations. Two reviews are recorded at `7530ae6eeeb0614d7c94ed6ab1f6761f3493ab88`.
- [All-defect elementary layers](update-2026-11-16/manuscripts/odd-elementary-layer-all-defects.md) and [uniform multiplicity layers](update-2026-11-16/manuscripts/odd-uniform-multiplicity-layers.md): projected inverted sets must retain actual multiplicities; projection is not automatically a quotient loop. Full-shadow compression and monolithic reinsertion reduce a branch without discarding original extension data. The latter continuation reports three acceptances at `dd2f0fc5c4db866f93afe898d3a9a25382774489`. Arbitrary modules, extensions, cohomology and incidence constraints remain unsolved.

## 3. Bruck envelopes: effective parameters and an actual lifting problem

- [Elementary S₅ parameterization](update-2026-11-16/manuscripts/bruck-s5-elementary-parameterization.md): bounded active module data, with arbitrary passive multiplicity, extension/stabilizer/section tests and an exact equivalence relation. This is not merely a finite census. The original exponent-two endpoint and later all-exponent extension must be read separately.
- [Inversion and relative derivations](update-2026-11-16/manuscripts/bruck-s5-elementary-inversion.md): in the specified elementary-radical S₅ setting, exponent divides four and the inversion defect is encoded by a relative derivation. This does not show exponent two or equivalence to an exponent-two loop; the appended parameterization records the additional data.
- [Two-N actual-lift residual](update-2026-11-16/manuscripts/bruck-two-n-cross-residual.md): the remaining nonsplit class-two/exponent-four configuration is constrained by actual affine equations, a cokernel obstruction, ordinary-extension uniqueness at fixed data and a stabilizer torsor. Its full actual residual and appended cokernel/gauge sections have distinct review pins. **The affine compatibility problem remains open.** A consistent shadow is not an actual loop.

### Uniform exclusions are also results

The [one-M noncentral reduction](update-2026-11-16/manuscripts/bruck-one-m-noncentral-reduction.md) ultimately excludes its entire displayed class-two/exponent-at-most-four S₅ family with Φ(P)=M and shadow J⊕U^b or P₆⊕U^b for every b≥0. The [quadratic socle collision](update-2026-11-16/manuscripts/bruck-n-socle-quadratic-collision.md) and [all-b P₆ exclusion](update-2026-11-16/manuscripts/bruck-n-p6-all-u-exclusion.md) close the corresponding stated Φ(P)=N families. These are analytic original-folder exclusions without a split-envelope assumption, not merely bounded searches. They do not exclude other Frattini modules or larger radical classes. Read their module conventions and exact hypotheses before applying them.

A further [concrete nonsplit b=3 obstruction](advances-2026-11-16/manuscripts/bruck-b3-concrete-obstruction.md) excludes all stabilizer shadows for **one encoded group** under explicit layer, augmentation, size and selected-orbit hypotheses. It reports three mathematical/code reviews at `2bbb921c38fa006f0a9b134bbd43f90508ab012b`. Other quadratic models and the unrestricted Bruck branch remain open.

## 4. Affine and primitive-permutation directions

[The cyclic-prime affine-quotient classification](update-2026-11-16/manuscripts/affine-cyclic-prime-quotient-classification.md) handles the stated nontranslation regular-subgroup constructions in V⋊(T⋊C_p), with T solvable of order prime to p and V faithful and irreducible on T, including p=2. Simplicity becomes a fixed-free action condition on T's abelianization, with exact cross-data isomorphism criteria. This complements the already public single-root theorem; it is not exhaustion of all affine complements.

For the primitive left-multiplication-group route, [the all-simple-socle SD source](update-2026-11-16/manuscripts/sd-all-simple-socles.md) assembles a **conditional SD_k exclusion for k≥3**, assuming its explicit folder/inversion and cyclic-semiregularity interface, CFSG, and the listed family-specific results and external source facts. **The public packet does not yet reproduce those family proofs, so it is not a self-contained, externally auditable proof of the all-socle exclusion.** The [SD dependency map](SD_DEPENDENCIES.md) identifies the 19 direct missing manuscripts, the logical routes and review boundaries. The recorded assembly review is conditional on those inputs; it neither re-proves them all nor settles other primitive types.

The twisted-wreath (TW) programme has several uniform exclusions rather than just low-order computation:

- [Parity-code subwreaths](update-2026-11-16/manuscripts/tw-parity-code-subwreath.md), including its specified primitive block tops and all normalizing involution marks.
- [Hierarchical full-wreath block tops](update-2026-11-16/manuscripts/tw-full-wreath-block-tops.md), in its four stated hierarchical families.
- [Diagonal-grid block tops](update-2026-11-16/manuscripts/tw-diagonal-block-tops.md), including the stated primitive column groups, transitive columns when c≥d, and specified large independent column-unit families.

These manuscripts carry section-specific model review records and precise numerical/action hypotheses. Arbitrary large imprimitive column groups with d>c, unrestricted TW, other base groups and induced embeddings remain gaps. This list does not promote the aggregate CFSG-free or primitive-group programme to a completed theorem.

## 5. What collaborators can attack next

1. Classify the surviving order-5^5 exponent-25 extraspecial-top orbits, and extend beyond the classified exact regular-top models to general factor-permuting groups and other/mixed socles. The entire canonical PSL₂-power and nonpermuting A₅-socle settings are no longer pending paired-inversion tasks.
2. Solve the actual nonsplit Bruck extension/inversion/stabilizer/marked-section compatibility problem, or prove it impossible. Do not substitute a toy shadow solution.
3. Turn odd-layer compression into structural classification without dropping extension cochains, multiplicities or stabilizer data.
4. Audit complete proof closures and the cited group-theoretic inputs; simplify proofs and independently reproduce the small exact certificates.
5. Contribute references that researchers and their AI tools should know about. Our [shared reading list](REFERENCES.md) welcomes papers, theses, errata and computational resources. A link and a sentence about its relevance are enough; no literature survey or priority assessment is required.

The unrestricted classification still needs sound constructions, exhaustion and exact isomorphism criteria across **all** envelopes. Efficient generation remains a subsequent objective.

## Source and reproducibility boundary

[The update manifest](update-2026-11-16/MANIFEST.json) and [supplement manifest](update-2026-11-16/SUPPLEMENT_MANIFEST.json) record the original GitHub blobs and original/exported SHA-256 values. The supporting packets contain selected manuscripts and exact control programs pinned to their respective source revisions. Earlier public sources remain available rather than silently overwritten. Links to them are explicitly marked as earlier snapshots. Some administrative/contextual references and additional dependencies are not reproduced; those are labeled in the source and listed in the manifest. This is not a claim that every source's full proof closure has now been re-audited or reproduced. Unreviewed continuations retain their labels. No private conversations or speculative moonshine material are included.

Publication checks for this update: Python sources parsed; the included Bruck toy control independently reran with 64 group-word solutions and 4,096 ordered polar pairs. This is a toy residual check, not an actual Bruck-loop construction. GAP certificates are supplied but were not rerun in this publication pass.
