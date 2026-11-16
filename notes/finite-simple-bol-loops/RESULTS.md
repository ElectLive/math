# Results

The project seeks a classification of finite simple Bol loops up to isomorphism. Its results fall into three groups: **examples that enlarge the landscape**, **classifications of defined subclasses**, and **structural restrictions on the remaining cases**. The unrestricted classification remains open.

The statements below describe the project's manuscripts. They are research proof drafts, not human-refereed or formally verified results. Some assemblies still depend on unpublished supporting arguments. The linked proofs state their hypotheses and limitations; [verification status](VERIFICATION.md) and the [dependency audit](COVERAGE_AUDIT.md) explain the remaining gaps.

Throughout, “canonical group” means the faithful left multiplication group with its distinguished translations, identity stabilizer and inversion. It does not mean the full multiplication group.

## 1. Examples that change the classification problem

### Outside both G-loops and Bruck isotopes

Nagy asked whether a finite simple proper Bol loop can be **neither a G-loop nor isotopic to a Bruck loop**. Here “proper” means non-Moufang, and a G-loop is isomorphic to every one of its loop isotopes.

The project gives a proposed example of order **3⁷⁵·19³**. Its principal isotopes occupy exactly three isomorphism classes under the stated interfaces. Acceptance of the argument would answer Nagy's existence question, without classifying all such loops or establishing that this example is sporadic.

- [Direct existence proof](0018-non-g-loop-non-bruck-existence.md)
- [Construction and proof explanation](0018-non-g-loop-non-bruck-context.md), including the original class-two route
- [Three isotope classes](update-2026-11-16/manuscripts/odd-class-two-isotope-orbits.md)

### Mixed simple factors and factor-permuting groups

The [mixed path construction](update-2026-11-16/manuscripts/radical-free-mixed-paths.md) gives simple proper loops of order **60ᵃ·168ᵇ for every a,b≥1**. When a and b have opposite parity, the loops have neither an exact-factorization isotope nor a Bruck isotope; the smallest displayed case has order **604800**. This is not a claim that these loops are non-G-loops.

The [factor-permutation construction](advances-2026-11-16/manuscripts/radical-free-factor-permutation-construction.md) gives an order-648000 example and examples with unbounded prime cycle lengths in the action on simple factors. These constructions show why neither a single simple-factor type nor an assumption that all factors are fixed can suffice for the full classification.

## 2. Subclasses with explicit classification data

“Classification” in this section means construction data, an exhaustion argument and an isomorphism criterion **inside the stated hypotheses**. It does not extend automatically to groups with the same composition factors or permutation quotient.

### Canonical groups that are powers of PSL₂

[0026: Classification theorem and proof](manuscripts/0026-psl2-power-classification.md) presents the following result and its construction uniformly.

For every prime power q≥4, the [arbitrary-inversion assembly](advances-2026-11-16/manuscripts/radical-free-fixed-factors.md) treats the entire canonical group **G=PSL₂(q)ⁿ**, without assuming the inversion action. Survivors have n=2k, paired inversion and loop order |PSL₂(q)|ᵏ. The [path classification](update-2026-11-16/manuscripts/radical-free-psl2-path-classification.md) gives the following number of classes for each k≥1:

| q | Classes |
|---|---:|
| Even q | 1 |
| 5 | 1 |
| 7, 23, 59 | 2 |
| 11 | 3 |
| 29 | 1 |
| Other odd q≡3 mod 4 | 1 |
| Other odd q≡1 mod 4 | 0 |

The q=4 and q=5 descriptions give the same A₅ family. Larger canonical overgroups and mixed simple-factor types are not covered by this table.

### A₅ socles and mixed A₅/PSL₂(7) groups

| Hypotheses | Classification data | Proof |
|---|---|---|
| Soc(G)=A₅ʳ and G does not permute its simple factors; no prescribed inversion action | Pure-A₅ paths, or positive path lengths and a strongly connected binary matrix, with the stated equivalence and selected-mark data | [Inversion](advances-2026-11-16/manuscripts/radical-free-a5-code-inversion.md), [classification](advances-2026-11-16/manuscripts/radical-free-a5-outer-codes.md) |
| G=A₅²ᴬ×PSL₂(7)²ᴮ, A,B≥1, with paired inversion | Path lengths and binary/ternary matrices; strong directed connectivity characterizes simplicity; path permutations and specified ternary signs give isomorphism | [Mixed paired classification](manuscripts/0028-0030-mixed-paired-classification.md) |

These results classify substantial families of canonical data. The first allows more than direct powers of A₅, but excludes factor-permuting actions; the second does not remove its paired-inversion assumption.

### Regular permutation tops in the A₅ construction

The next results concern the **exact wreath-pair models and swap inversion specified in their manuscripts**. A “regular top” is the quotient group acting regularly on the factor positions.

| Top group in that model | Result | Proof |
|---|---|---|
| Cyclic of order n | Exactly n=1,3,5,15; one loop class of order n·60ⁿ for each | [Cyclic tops](advances-2026-11-16/manuscripts/radical-free-a5-cyclic-top.md) |
| Finite abelian A | Exactly A≅Uₐ(F₃)×Uᵦ(F₅), where Uₑ(Fₚ)=1+tFₚ[t]/(tᵉ⁺¹); one class for each a,b≥0, of order n·60ⁿ with n=3ᵃ5ᵇ | [Abelian tops](advances-2026-11-16/manuscripts/radical-free-a5-abelian-top.md) |
| Modular nonabelian C₉⋊C₃, with the specified full anti-abelianization envelope | Six classes of order 27·60²⁷ | [Modular order-27 top](advances-2026-11-16/manuscripts/radical-free-a5-nonabelian-27.md) |
| Exponent-three nonabelian top of order 27 | Two classes of order 27·60²⁷ | [Exponent-three top](advances-2026-11-16/manuscripts/radical-free-a5-extraspecial-27.md) |

For [arbitrary odd prime-power regular tops](advances-2026-11-16/manuscripts/radical-free-a5-prime-power-top.md), the construction reduces to p=3 or 5 and explicit module/cocycle tests. This is a parameterization, not a solution of all resulting orbits. The public [higher-rank extraspecial theorem](advances-2026-11-16/manuscripts/radical-free-a5-extraspecial-tops.md) establishes existence in its sole surviving higher-rank case, order 5⁵ and exponent 25. Subsequent research reports **88 isomorphism classes** in that case and the following completed extraspecial-top table:

| Extraspecial top P | Reported loop classes |
|---|---:|
| Order 3³, exponent 3 | 2 |
| Order 3³, exponent 9 | 6 |
| Order 5³, exponent 5 | 24 |
| Order 5⁵, exponent 25 | 88 |
| Every other odd extraspecial top | 0 |

The total is **120 classes in these exact regular-top models**, not 120 classes of all simple Bol loops. More precisely, set S=A₅ᴾ⋊P for the regular action and take G to be the subgroup of S×S whose two top images multiply to the identity in P/[P,P], with inversion swapping the two factors. The table concerns this specified canonical group and inversion, not arbitrary groups with an extraspecial permutation quotient.

**Proof availability.** The subsequent 24-class proof, 88-class orbit theorem and complete assembly are not yet published here. These counts are reported results, not conclusions established by the older linked public manuscript or independently verified by this catalogue. Their full proofs and computational certificate remain to be presented publicly. The orbit counts are therefore no longer research targets in this programme, but general nonabelian regular tops remain open.

### Odd, Bruck and affine branches

| Subclass | What the project supplies | Boundary |
|---|---|---|
| Odd branch with class-two canonical derived group | Bimap, action and positive-cocycle data; admissibility, normal-subgroup tests, exhaustion and actual-loop isomorphism criteria | Does not classify higher derived-group classes. [Proof](update-2026-11-16/manuscripts/odd-class-two-classification.md) |
| Specified elementary-radical S₅ Bruck envelopes | Extension, stabilizer and section parameters with exact equivalence; the general-exponent treatment records the extra inversion data | Not all radicals, quotients or Bruck loops. [Parameters](update-2026-11-16/manuscripts/bruck-s5-elementary-parameterization.md), [inversion and section bounds](manuscripts/0038-elementary-s5-inversion.md) |
| Regular affine subgroups with nontrivial projection in a single root group | Explicit subspace/surjection data and semilinear equivalence, with the stated loop-interface hypotheses | Other projection types remain. [Proof](packet/manuscripts/nonbruck-single-root-classification.md) |
| Stated nontranslation constructions in V⋊(T⋊Cₚ), T solvable of order prime to p and V faithful irreducible on T | A fixed-free action criterion for simplicity and cross-data isomorphism tests, including p=2 | Not all affine complements. [Proof](update-2026-11-16/manuscripts/affine-cyclic-prime-quotient-classification.md) |

## 3. Structural results guiding the remaining work

### Complexity cannot be bounded away

The odd-order constructions force any classification to accommodate:

- [Every derived-subgroup nilpotency class c≥2](manuscripts/0021-0023-unbounded-complexity.md).
- [Unbounded derived length](manuscripts/0021-0023-unbounded-complexity.md) and [unbounded Fitting height](manuscripts/0021-0023-unbounded-complexity.md) of the canonical group.
- [Alternating-form tuples](manuscripts/0025-alternating-form-construction.md) yield simple proper odd Bol G-loops of order p^(nr+k)q^(2k+1), with an exact semilinear-congruence isomorphism test under the stated class-two interfaces.
- [Simultaneous similarity of arbitrary matrix pairs](manuscripts/0024-matrix-pair-embedding.md) inside a specified loop-isomorphism problem. This is a structural encoding, not a complexity-class hardness theorem.
- [Noncentral derived centers](packet/manuscripts/odd-noncentral-jordan-center-family.md), [fixed-shadow phenomena](packet/manuscripts/odd-fixed-shadow-simple-example.md), and [monolithic higher-defect constructions](packet/manuscripts/odd-monolithic-higher-defect-isomorphism.md).

The [elementary-layer](update-2026-11-16/manuscripts/odd-elementary-layer-all-defects.md) and [multiplicity-layer](update-2026-11-16/manuscripts/odd-uniform-multiplicity-layers.md) reductions preserve extension and multiplicity information. They constrain the problem without yet solving all module, cohomology and incidence conditions.

### Recognizing and excluding construction routes

The [splitting-atom graph](update-2026-11-16/manuscripts/radical-free-bipartite-witness.md) recognizes exact-factorization witnesses by bipartiteness in its paired semisimple setting; the [mixed matrix criterion](update-2026-11-16/manuscripts/radical-free-mixed-matrix-classification.md) expresses this through weighted-cycle parity. This explains why some mixed examples cannot come from that route.

The [inner-inversion reduction](update-2026-11-16/manuscripts/exact-factorization-criterion.md) puts inner inversion in the Bruck structural regime under its stated hypothesis; in particular, O₂(G)=1 forces outer inversion. Its published Bruck-theory inputs are CFSG-dependent. Further [involution-support](update-2026-11-16/manuscripts/radical-free-involution-support.md) and [PSL₃ restrictions](update-2026-11-16/manuscripts/radical-free-psl3-prime-paths.md) address other specified families.

### Bruck lifting and primitive actions

Several proposed Bruck radical families are excluded uniformly, not just by bounded search: the stated [one-M](update-2026-11-16/manuscripts/bruck-one-m-noncentral-reduction.md), [quadratic-socle](update-2026-11-16/manuscripts/bruck-n-socle-quadratic-collision.md) and [P₆](update-2026-11-16/manuscripts/bruck-n-p6-all-u-exclusion.md) families. A [concrete nonsplit b=3 obstruction](advances-2026-11-16/manuscripts/bruck-b3-concrete-obstruction.md) excludes all stabilizer shadows for one encoded group under its explicit hypotheses. None is an exclusion of all Bruck extensions.

The [two-N residual](update-2026-11-16/manuscripts/bruck-two-n-cross-residual.md) isolates actual affine compatibility conditions for a remaining nonsplit extension. Solving a simplified shadow is not enough to construct a loop.

For primitive canonical actions, the [simple-diagonal assembly](update-2026-11-16/manuscripts/sd-all-simple-socles.md) gives a **conditional** SDₖ exclusion for k≥3. Its [dependency map](SD_DEPENDENCIES.md) identifies missing family proofs, so this is not yet a self-contained public proof. Twisted-wreath exclusions cover specified [parity-code](update-2026-11-16/manuscripts/tw-parity-code-subwreath.md), [hierarchical](update-2026-11-16/manuscripts/tw-full-wreath-block-tops.md) and [diagonal-grid](update-2026-11-16/manuscripts/tw-diagonal-block-tops.md) actions. The unrestricted primitive-action problem remains open.

## Further reading

The [claim index](CLAIMS.md) records exact scopes and stable IDs. The [open problems](OPEN_PROBLEMS.md) state the next mathematical targets. The [references](REFERENCES.md) provide literature, and the [contribution guide](CONTRIBUTING.md) explains how to share a proof, counterexample, construction or useful source.
