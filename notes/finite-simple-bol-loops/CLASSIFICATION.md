# Classification coverage index

## Current full-multiplication-socle coverage

This table concerns M=Mlt(L), not the canonical G used in older parameterization tables. Every “excluded” or “reduced” label is conditional on the linked source inputs and recorded review scope.

| Soc(M) family | Completed result | Remaining boundary |
| --- | --- | --- |
| Alternating | [Natural A_m/S_m action, m=|L|≥24](manuscripts/0087-alternating-natural-full-action.md), no solvable-G assumption | Operations and existence not classified |
| All 26 sporadic groups | [Excluded](manuscripts/0088-sporadic-full-socle-exclusion.md) | Not a statement about arbitrary sporadic sections or the earlier paired construction |
| PSL₂; odd-dimensional PSL and PSU | [Excluded for the stated simple parameters](manuscripts/0089-classical-full-socle-exclusions.md) | No general even-dimensional conclusion |
| Suzuki, small Ree, G₂, F₄, E₈, ³D₄, even-characteristic E₇, large Ree and Tits | [Excluded for the exact parameter ranges](manuscripts/0090-exceptional-full-socle-exclusions.md) | E₆/²E₆, odd-characteristic E₇ and remaining classical families stay open |

The earlier canonical-group tables remain useful but are not a disjoint partition of these full-group families. Their historical pending PSL₂ and odd-dimensional residual labels are superseded by this table; their distinct extension/operation questions are not automatically settled.


This is the family-by-family index of **what has been classified, what has only been reduced, and what remains open** in the finite simple Bol-loop programme. It complements the [results overview](RESULTS.md), [claim catalogue](CLAIMS.md) and [open-problems board](OPEN_PROBLEMS.md).

**The unrestricted classification remains open. In particular, “all A₅-based loops are classified” is not a conclusion of the current work.** A theorem about an exact canonical group does not classify every group with the same socle, composition factors or quotient.

## How to read the status

- **Classified in scope:** the project gives construction, exhaustion, admissibility and an exact isomorphism relation for the stated hypotheses. This may be a structural parameterization, not an evaluated list of orbits.
- **Census in scope:** the specified parameter orbits are also evaluated or counted.
- **Excluded in scope:** a nonexistence theorem for precisely the displayed model; this is not a positive classification of its overgroups.
- **Partial:** constructions, necessary conditions or an extension-data reduction exist, but the named family is not exhausted and resolved.
- **Proposed:** a current argument awaits its stated exact-source checking; it is not included among the reviewed classified families.
- **Open:** no exhaustive classification of the named family is supplied here. This does not mean nobody has investigated it.

These statuses describe the project's research proofs. They **do not assert human referee acceptance, formal verification or literature priority**. Every row inherits its source's assumptions and imported interfaces; a recorded automated review checks only its specified source and scope. The mathematical source snapshot and public mapping are recorded in [the source crosswalk](classification-source-map.json). Read the linked theorem, not the short label, when applying a result.

Here **G** is the faithful canonical left-multiplication group with its section, identity stabilizer and inversion, not the full multiplication group. **Q** denotes a top group acting on simple factors, not a quotient loop. The families below overlap and do not constitute a proved disjoint partition.

## 1. A₅: exactly where the boundary lies

| Family and indispensable hypotheses | Status and output | Proof / next boundary |
| --- | --- | --- |
| Soc(G)=A₅ʳ, and G does **not permute** its simple factors; no initial paired-inversion assumption | **Classified in scope.** Pure paths or paired parity-code/matrix data, including selected-mark and inversion exhaustion | [0027: inversion exhaustion](sources/factor-permutation/radical-free-a5-code-inversion.md) and [parameters](sources/factor-permutation/radical-free-a5-outer-codes.md). Does not cover factor-permuting groups |
| G=A₅^Ξ⋊Q; Q odd abelian, faithful **pure factor permutations**, arbitrary orbit multiplicities and full-strip paths | **Classified in scope.** Explicit quotient modules, bijective cocycles, normal-cut tests and simultaneous coordinate equivalence; parameter orbits not all evaluated | [0068: all-path parameters](manuscripts/0068-abelian-nilpotent-path-parameters.md) |
| The same pure-permutation model, Q odd nilpotent, **zero** actual residual graph | **Classified in scope.** Cocycles bijective on the involution-inverted section, not necessarily a regular action of all Q | [0068: nilpotent extension](manuscripts/0068-abelian-nilpotent-path-parameters.md#extension-to-the-entire-nilpotent-zero-graph-branch). Now a special case of the next row |
| The same pure-permutation model, **every odd nilpotent Q**, allowing nonzero residual DAGs | **Classified in scope, structurally.** Graph-aware construction, exhaustion, original normal-cut tests and exact isomorphism data; admissible parameter orbits remain unevaluated | [0073: all-graph theorem](manuscripts/0073-all-nilpotent-path-parameters.md). This supersedes the earlier nonzero-graph normalization frontier |
| The same model, Q arbitrary odd and stabilizer H→Q **surjective** | **Classified in scope, structurally, under cited inputs.** Separate automated reviews are recorded for the arbitrary-odd extension; H→Q remains an explicit hypothesis | [0073](manuscripts/0073-all-nilpotent-path-parameters.md), [0066: pairing](manuscripts/0066-odd-top-orbit-pairing.md) |
| The same model, Q arbitrary odd, **without** stabilizer-surjectivity assumption | **Open, actively investigated.** Local-character and tensor constraints do not yet prove surjectivity or exhaust nonsurjective folders | [0074: surjectivity boundary](manuscripts/0074-odd-top-surjectivity-boundary.md), [open problems](OPEN_PROBLEMS.md) |
| A₅ socle with general factor-permuting **outer actions**, including cases not pure permutations | **Open beyond the covered slices.** The nonpermuting parity-code theorem does not supply this general extension | [0027](sources/factor-permutation/radical-free-a5-outer-codes.md), [open problems](OPEN_PROBLEMS.md) |
| A₅ factors together with other simple-factor types | **Partial.** Specified mixed models are classified below; arbitrary mixed socles are not | [Mixed models, §2](#2-other-semisimple-and-mixed-models) |
| Groups with a nontrivial solvable radical and an A₅-related quotient | **Partial / open in general.** Specified Bruck and affine extension families have separate results; the radical-free A₅ theorems do not apply automatically | [Radical branches, §5](#5-bruck-radicals-and-even-affine-branches), [open problems](OPEN_PROBLEMS.md) |

The residual graph is an actual algebraic correlation map in the stabilizer, **not a graph of proof dependencies**. Classifying its admissible data does not imply every formal DAG is realized by a simple loop, nor provide a census of all graph/module/cocycle orbits.

### Evaluated wreath-pair subfamilies

These are narrower exact canonical groups with prescribed swap inversion, not classifications of every group sharing the named top. The source defines the full group and section.

| Exact top model | Status and evaluated result | Source |
| --- | --- | --- |
| Regular cyclic top of length n | **Census:** n=1,3,5,15 only; one class of order n·60ⁿ at each length | [0032](sources/factor-permutation/radical-free-a5-cyclic-top.md) |
| Regular finite abelian top | **Classified and evaluated:** principal-unit groups Uₐ(F₃)×Uᵦ(F₅), one class for each a,b≥0 | [0033](sources/factor-permutation/radical-free-a5-abelian-top.md) |
| Odd prime-power regular top, arbitrary | **Partial:** explicit cyclic-affine module/cocycle reduction, not an evaluated classification of all such tops | [0036](sources/factor-permutation/radical-free-a5-prime-power-top.md) |
| Odd extraspecial regular top in the full anti-abelianization wreath-pair model | **Census:** 120 classes; contributions 2,6,24,88 from the four admissible top types; all other odd extraspecial tops excluded in this model | [0064](manuscripts/0064-extraspecial-regular-census.md) |
| Specified faithful transitive nonabelian class-two Camina top models | **Census:** 128 classes, comprising 120 regular and eight nonregular | [0065](manuscripts/0065-transitive-camina-tops.md) |

## 2. Other semisimple and mixed models

| Family and hypotheses | Status and output | Proof / remaining scope |
| --- | --- | --- |
| Entire canonical group G=PSL₂(q)ⁿ, q a prime power ≥4, no prescribed inversion | **Classified in scope, with counts.** Paired paths; the field-dependent counts are in the theorem | [0026](manuscripts/0026-psl2-power-classification.md). Larger canonical overgroups are not included |
| G=A₅²ᴬ×PSL₂(7)²ᴮ, A,B≥1, with the stated paired inversion | **Classified in scope.** Path lengths, binary/ternary matrices, connectivity criterion and exact equivalence | [0028–0030](manuscripts/0028-0030-mixed-paired-classification.md) |
| Arbitrary mixed simple socles, inversion and overgroups | **Open.** Mixed path constructions and restrictions are not an exhaustive classification | [0059](CLAIMS.md), [open problems](OPEN_PROBLEMS.md) |
| Pure PSL₂(q) permutation envelopes, odd q≡1 mod4 outside {5,9,29}, odd top and H→Q surjective (in particular odd nilpotent top) | **Excluded in scope.** The actual projective-tensor theorem, not an exclusion of arbitrary outer lifts | [0069](manuscripts/0069-psl2-odd-permutation-top-exclusions.md) |
| Pure PSL₂(q) envelopes with q odd and q≡1 mod4, odd faithful transitive top | **Excluded in scope**, without assuming nilpotence or H→Q surjectivity, including q=5,9,29 | [0077](manuscripts/0077-radical-free-psl2-transitive-odd-tops.md) |
| Pure PSL₂(7) envelopes with odd faithful transitive top | **Partial:** outer case excluded; inner trace and valuation constraints, not a classification | [0078](manuscripts/0078-radical-free-psl27-transitive-odd-trace.md) |
| Remaining PSL₂ permutation envelopes beyond the listed scopes, or general outer actions | **Open beyond the listed cases** | [0069](manuscripts/0069-psl2-odd-permutation-top-exclusions.md), [open problems](OPEN_PROBLEMS.md) |
| Other simple socles and general radical-free canonical groups | **Partial.** Involution-support, classical-group and path restrictions exist, but do not exhaust all groups/actions | [0071: source atlas](manuscripts/0071-primitive-and-simple-socle-reductions.md) |

## 3. Odd-order loops and derived-group structure

| Exact hypothesis | Status and output | Proof / remaining scope |
| --- | --- | --- |
| Simple nonassociative odd loop with canonical G′ of nilpotency class at most two, arbitrary exponent, no center-centrality assumption | **Classified structurally.** Finite abelian groups, bimaps, actions and positive cocycles, exact simplicity and loop-isomorphism tests | [Whole-class-two theorem](sources/odd-completion/odd-class-two-classification.md). Bimap/cocycle orbits not evaluated |
| Derived Sylows of exponent p and class<p, central centers and no common coprime fixed point off their centers | **Classified structurally under these additional hypotheses** via Lie data and finite ideal tests | [Central Lazard theorem](sources/odd-completion/odd-lazard-central-classification.md). Fixed noncentral shadows are a real uncovered case |
| G′=M⋊T with M,T coprime abelian and [T,M]=M | **Classified structurally in scope.** Extension/cocycle/stabilizer data with exact equivalence | [Coprime metabelian-derived theorem](sources/odd-completion/odd-coprime-metabelian-derived-classification.md) |
| Arbitrary metabelian G′, including prime overlap and nonsplit cases | **Partial.** A compatible residual splitting is proved; complete folder data are not classified by that group reduction alone | [Residual splitting](sources/odd-completion/odd-metabelian-residual-splitting.md) |
| Higher nilpotent class outside the Lazard slice; nonnilpotent G′ of arbitrary derived length | **Open in general.** Elementary-layer lifts and many constructions constrain the task, but do not close it | [0072: odd/affine atlas](manuscripts/0072-odd-and-affine-structural-reductions.md), [open problems](OPEN_PROBLEMS.md) |
| All odd simple proper loops are G-loops, or are G-loops or Bruck-isotopic | **False under the stated construction inputs.** A counterexample has nonisomorphic principal isotopes | [0018](0018-non-g-loop-non-bruck-existence.md), [0020](manuscripts/0020-odd-isotope-orbits.md) |
| Universal bounded nilpotency class, derived length or Fitting height for canonical groups | **False under the stated construction inputs.** Unbounded families exist; this is not a classification | [0021–0023](manuscripts/0021-0023-unbounded-complexity.md) |

## 4. Exact factorization and isotopy

| Family / question | Status | Source / boundary |
| --- | --- | --- |
| Nagy almost-simple exact-factorization family | **Classified in scope** with isomorphism data; not all proper Bol loops | [0002](claims/0002.md), [foundation proof](sources/foundations/C0002.md) |
| Arbitrary exact-factorization presentations | **Partial.** Structural presentation/isomorphism interfaces exist; this route is not proved exhaustive for proper Bol loops | [Presentation source](sources/odd-completion/factorization-presentations.md) |
| Principal isotopes in specified exponent-two and rigid odd examples | **Scoped censuses / orbit theorems.** Four-class, twenty-class and three-class results concern their named models, not a universal isotope classification | [0006](claims/0006.md), [0012](claims/0012.md), [0020](manuscripts/0020-odd-isotope-orbits.md) |
| All proper Bol loops from exact factorization, or all isotopes isomorphic | **Not established; universal G-loop assertion is refuted.** Isotopy equivalence must not be substituted for loop isomorphism | [0018](0018-non-g-loop-non-bruck-existence.md), [open problems](OPEN_PROBLEMS.md) |

## 5. Bruck radicals and even affine branches

| Family and hypotheses | Status and output | Proof / next boundary |
| --- | --- | --- |
| Specified elementary-radical S₅ Bruck envelopes | **Structural parameterization in scope.** Extension, stabilizer, section and equivalence data with actual inversion conditions | [0038](sources/bruck-completion/bruck-s5-elementary-parameterization.md), [Bruck atlas](manuscripts/0070-bruck-radical-constraints.md) |
| General Bruck radicals, multiple quotient factors and noncentral/nonsplit extensions | **Partial, not a completed unrestricted classification.** Extension-data searches and necessary chief-factor constraints retain unresolved realizability/admissibility conditions | [0070](manuscripts/0070-bruck-radical-constraints.md), [all-radical parameters](sources/bruck-completion/bruck-all-radical-parameterization.md) |
| Particular one-M, quadratic-socle, P₆ and encoded b=3 branches | **Excluded only under the exact source hypotheses.** These exclusions do not settle all radicals | [0049–0054 in catalogue](CLAIMS.md), [0070](manuscripts/0070-bruck-radical-constraints.md) |
| Regular subgroups with full projection into one root group of the specified natural affine family | **Classified in scope.** Subspace/surjection data and semilinear equivalence; prime-transvection cases are included | [Single-root theorem](sources/odd-completion/nonbruck-single-root-classification.md) |
| Nontranslation regular-subgroup constructions for V⋊(T⋊Cₚ), T nontrivial solvable p′, V faithful irreducible on T | **Classified in scope.** Fixed-free simplicity criterion and cross-data equivalence | [Cyclic-prime quotient theorem](sources/odd-completion/affine-cyclic-prime-quotient-classification.md) |
| Other affine projection/complement types; general even non-Bruck-isotopic loops | **Open beyond the listed constructions** | [0072](manuscripts/0072-odd-and-affine-structural-reductions.md), [open problems](OPEN_PROBLEMS.md) |

## 6. Primitive-action restrictions are not a classification of all loops

[0071](manuscripts/0071-primitive-and-simple-socle-reductions.md) indexes the full source families. Natural point/subspace/flag-action exclusions, conditional diagonal-socle exclusions and specified twisted-wreath restrictions concern **particular permutation actions with their normalizer and marked-involution hypotheses**. An abstract simple group may have other actions. These arguments do not turn the entire primitive-action branch into a solved classification.

The [simple-diagonal assembly, 0062](CLAIMS.md) and [twisted-wreath restrictions, 0063](CLAIMS.md) retain their conditions. The [open-problems board](OPEN_PROBLEMS.md) records the surviving directions. Associative simple loops (finite simple groups) and nonassociative simple Moufang loops (Paige loops) are classical boundaries, not new results of this project; the remaining target is proper Bol loops.

## Maintenance rule

For every new family-level result, update this index, [CLAIMS.md](CLAIMS.md) and [OPEN_PROBLEMS.md](OPEN_PROBLEMS.md) together. Record exact group/action/section hypotheses, construction versus exhaustion, true isomorphism equivalence, and whether parameter orbits are evaluated. Move a case from open to classified only when the corresponding theorem covers it; preserve superseded narrower results as special cases. A new proposal and an automated review are separate events. The index must never infer a larger solved family merely from a shared label such as “A₅,” “nilpotent,” “Bruck” or “affine.”
