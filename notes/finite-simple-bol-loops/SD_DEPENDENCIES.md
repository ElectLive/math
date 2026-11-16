# SDₖ exclusion: dependency and audit map

The [current-results guide](CURRENT_RESULTS.md) reports a **conditional assembly**, not a self-contained proof in this public packet. The [published SD assembly](update-2026-11-16/manuscripts/sd-all-simple-socles.md) states its hypotheses explicitly. Its family-specific proofs have not all been reproduced here. This is a publication-closure gap, not evidence of a mathematical error.

## Exact conclusion being assembled

For a finite simple nonassociative left Bol loop Q with primitive G = LMlt(Q), the assembly aims to exclude simple-diagonal type with socle Tᵏ for k≥3. Its assumptions include:

1. The displayed canonical folder and inversion interface, including an automorphism τ inverting all marked left translations.
2. Stabilizer intersection B∩H = Δ(T), generation and sandwich closure, and the displayed cardinality and collision conditions.
3. The **cyclic-semiregularity / forbidden-prime consequence** for products in Λ². The assembly expressly warns that this does not follow from the collision condition alone.
4. CFSG, the family arguments below, and their external source facts.

It does not address SD₂ or eliminate other primitive types.

## Logical route

```
folder/inversion interface and semiregularity
    → primitive action on factors + faithful action on the socle
    → family-specific common-class or counting contradiction
    → CFSG coverage matrix
    → conditional SDₖ exclusion for k≥3
```

The common-class route needs a suitable Aut(T)-invariant involution class satisfying the stated square-containment condition. The raw counting route instead uses n=|T|≥2²⁰ and b³+3ab<n², where a=|Aut(T)| and b counts its elements of square one. Small cases have separate criteria. These routes and hypotheses are not interchangeable.

## Public source coverage

**Available:** the [assembly and its case-coverage matrix](update-2026-11-16/manuscripts/sd-all-simple-socles.md#case-coverage-matrix), including the local centralizer/factor-action argument, precise interfaces, and scoped assembly-review record.

**Not reproduced in the current public packet:** the following 19 distinct named family-input manuscripts. File names identify the exact source obligations; they are not links to unavailable private material.

| Obligation | Family-input manuscripts required |
|---|---|
| A₅; common folder, factor-top and semiregularity arguments | `sd-a5-all-factors.md` |
| PSL₂(q), including A₆ routing | `sd-psl2-all-factors.md` |
| Alternating Aₘ for m≥7 | `sd-alternating-all-factors.md` |
| PSL₃ and PSU₃, including small cases | `sd-rank-three-linear-unitary.md`; `sd-unitary3-even.md` |
| Higher linear/unitary families and finite residuals | `sd-classical-raw-bounds.md`; `sd-linear-unitary-refined-bounds.md`; `sd-finite-classical-aut-counts.md`; `sd-linear-unitary-final-five.md` |
| Symplectic families and small common-class cases | `sd-classical-raw-bounds.md`; `sd-symplectic-finite-residuals.md`; `sd-finite-common-classes.md` |
| Orthogonal families and finite residuals | `sd-orthogonal-raw-bounds.md`; `sd-orthogonal-refined-bounds.md` |
| Suzuki and small Ree families | `sd-suzuki-all-factors.md`; `sd-ree-all-factors.md` |
| Exceptional Lie-type families and Tits group | `sd-exceptional-class-bounds.md`; `sd-exceptional-remaining.md` |
| Sporadic groups | `sd-sporadic-all.md`; `sd-three-sporadic-socles.md`; `sd-finite-common-classes.md` |

These are direct dependencies of the assembly, not a claim that the list is its complete transitive proof closure. The missing manuscripts may import further lemmas, code, data and sources. The all-field **paired radical-free PSL₂ classification**, published elsewhere in this workspace, is a different result and must not be substituted for the missing SD/PSL₂ argument.

## External inputs and review limits

CFSG, full-automorphism-group identifications, character tables and power maps, and particular source inequalities retain their own obligations. Rerunning integer inequalities alone would not validate those identifications. In particular the assembly directs PSU₄(3) through an appended common-class argument rather than a failing raw inequality, and preserves a source discrepancy in the even-PSU₃ route.

The recorded assembly review at source `f6c7e01a4337b51c703b4d9ffc94d3b84a732fe5` accepts the synthesis **conditional on the family results and source facts**. It is not an independent reproof of every family. The public publication pass adds no mathematical acceptance, human refereeing, formal verification or novelty certification.

This coverage check inspected the public guide and assembly on 16 November 2026 and compared the source assembly on the active research branch at `c722d73e0eee35e4c9df6f1bd7e8cf8f5e99d7ae`. The public mathematical snapshot remains the earlier `67cced817f7d24e36d78990c73828ade4f218091`; checking a later branch does not silently update its proof status.

## Concrete next publication/review task

Publish and audit one complete subcase first, beginning with A₅: include the family proof, every folder/semiregularity input it actually uses, exact source pins, all finite certificates and their data, and a checkable dependency list. Then expand to the other rows. Until those closures are available, external collaborators can inspect the assembly and its coverage logic here, but cannot independently audit the all-socle theorem solely from this packet.
