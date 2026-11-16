# Current research: constructions, classifications and structural obstructions

**Snapshot: 16 November 2026, source revision `67cced817f7d24e36d78990c73828ade4f218091`.** This page is the front door to the broader programme, not just the rigid-center example. It records what the manuscripts claim, their mathematical scope and the reviews they report. The expansion is a publication and reconciliation pass, **not a fresh independent proof audit**. Recorded reviews are by AI models, not human referees or formal proof checkers. A later appendix does not inherit an earlier section's acceptance automatically.

## 1. Radical-free envelopes: a substantial classification programme

Here the canonical group means the faithful **left multiplication group**, with its marked left translations, identity stabilizer and canonical inversion. It must not be replaced by the full multiplication group or just an abstract composition-factor list.

### All fields for the paired PSL₂ model

[The all-field assembly](update-2026-11-16/manuscripts/radical-free-psl2-path-classification.md#all-field-paired-psl₂-assembly) classifies the paired canonical model
`G = PSL₂(q)^k × PSL₂(q)^k`, with inversion exchanging paired factors, for every prime power q≥4 and k≥1. All survivors are single paths, with explicit endpoint groups and exact within-model isomorphism classes:

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

The endpoint table and subgroup hypotheses are in the manuscript. q=4 and q=5 describe the same A₅ family and must not be counted twice. The assembly reports three mathematical/source/code acceptances at `e30af949531c0ebcc9f7533b04fc1e7fc6858563`; its q=9 certificate is included. This does **not** classify arbitrary loops merely having PSL₂ composition factors, or remove the paired-inversion assumption.

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

### Restrictions toward removing paired inversion

[Fixed-factor and character constraints](update-2026-11-16/manuscripts/radical-free-fixed-factors.md) use actual stabilizer transversality, marked class sums, representation characters, valuations and Sylow-two bounds. The earlier fixed-factor restrictions and character section have their own recorded reviews. **The newest A₅-power inversion-exhaustion appendix at this snapshot awaits review** and is a proposed continuation, not a newly accepted classification. Mixed fixed-factor models remain open. [Involution-support restrictions](update-2026-11-16/manuscripts/radical-free-involution-support.md) also exclude the specified paired Suzuki/small-Ree cases and A₅/Suzuki mixtures. [Prime-field PSL₃ restrictions](update-2026-11-16/manuscripts/radical-free-psl3-prime-paths.md) extend the approach beyond PSL₂, within their stated model.

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

## 4. Affine and primitive-permutation directions

[The cyclic-prime affine-quotient classification](update-2026-11-16/manuscripts/affine-cyclic-prime-quotient-classification.md) handles the stated nontranslation regular-subgroup constructions in V⋊(T⋊C_p), with T solvable of order prime to p and V faithful and irreducible on T, including p=2. Simplicity becomes a fixed-free action condition on T's abelianization, with exact cross-data isomorphism criteria. This complements the already public single-root theorem; it is not exhaustion of all affine complements.

For the primitive left-multiplication-group route, [the all-simple-socle SD source](update-2026-11-16/manuscripts/sd-all-simple-socles.md) assembles a **conditional SD_k exclusion for k≥3**, assuming its explicit folder/inversion and cyclic-semiregularity interface, CFSG, and the listed family-specific results and external source facts. **The public packet does not yet reproduce those family proofs, so it is not a self-contained, externally auditable proof of the all-socle exclusion.** The [SD dependency map](SD_DEPENDENCIES.md) identifies the 19 direct missing manuscripts, the logical routes and review boundaries. The recorded assembly review is conditional on those inputs; it neither re-proves them all nor settles other primitive types.

The twisted-wreath (TW) programme has several uniform exclusions rather than just low-order computation:

- [Parity-code subwreaths](update-2026-11-16/manuscripts/tw-parity-code-subwreath.md), including its specified primitive block tops and all normalizing involution marks.
- [Hierarchical full-wreath block tops](update-2026-11-16/manuscripts/tw-full-wreath-block-tops.md), in its four stated hierarchical families.
- [Diagonal-grid block tops](update-2026-11-16/manuscripts/tw-diagonal-block-tops.md), including the stated primitive column groups, transitive columns when c≥d, and specified large independent column-unit families.

These manuscripts carry section-specific model review records and precise numerical/action hypotheses. Arbitrary large imprimitive column groups with d>c, unrestricted TW, other base groups and induced embeddings remain gaps. This list does not promote the aggregate CFSG-free or primitive-group programme to a completed theorem.

## 5. What collaborators can attack next

1. Remove paired-inversion hypotheses and settle the proposed fixed-factor exhaustion; then move beyond the already classified simple types.
2. Solve the actual nonsplit Bruck extension/inversion/stabilizer/marked-section compatibility problem, or prove it impossible. Do not substitute a toy shadow solution.
3. Turn odd-layer compression into structural classification without dropping extension cochains, multiplicities or stabilizer data.
4. Audit complete proof closures and the cited group-theoretic inputs; simplify proofs and independently reproduce the small exact certificates.
5. Establish literature novelty separately. None of these publication labels certifies priority.

The unrestricted classification still needs sound constructions, exhaustion and exact isomorphism criteria across **all** envelopes. Efficient generation remains a subsequent objective.

## Source and reproducibility boundary

[The update manifest](update-2026-11-16/MANIFEST.json) and [supplement manifest](update-2026-11-16/SUPPLEMENT_MANIFEST.json) record the original GitHub blobs and original/exported SHA-256 values. The update contains selected manuscripts and exact control programs from one frozen head. Earlier public sources remain available rather than silently overwritten. Links to them are explicitly marked as earlier snapshots. Some administrative/contextual references and additional dependencies are not reproduced; those are labeled in the source and listed in the manifest. This is not a claim that every source's full proof closure has now been re-audited or reproduced. Unreviewed continuations retain their labels. No private conversations or speculative moonshine material are included.

Publication checks for this update: Python sources parsed; the included Bruck toy control independently reran with 64 group-word solutions and 4,096 ordered polar pairs. This is a toy residual check, not an actual Bruck-loop construction. GAP certificates are supplied but were not rerun in this publication pass.
