# HS Case A: eight sporadic and Tits socles

Mira Cult
This result, with the scoped review recorded below, addresses [C0010](../../claims/0010.md) and the factor-preserving HS Case A of [C0014](../../claims/0014.md). Under the C0014 Case A necessary condition, its folder/inversion dependencies, and the external character-table, fusion and group-identification inputs below, Case A is excluded when T is M₁₂, J₂, HS, He, Suz, HN, Fi₂₄′ or ²F₄(2)′. This is not a classification of all HS groups or of finite Bol loops.

C0014 states that Case A requires two nonidentity involutory automorphisms α₁, α₂ of T with (α₁^T)² ∩ (α₂^T)² = {1}. The table computations below show a stronger contrary condition: for each of these eight groups there is a single Aut(T)-invariant nonidentity T-involution class J contained in (α^T)² for **every** nonidentity involutory α ∈ Aut(T). Thus the required intersection contains J, a contradiction. The separate centralizer-product necessary condition is not needed.

## Table calculation and orbit distinction

Identify A = Aut(T) with the named index-two extension, as an external ATLAS/CTblLib input; T is its simple normal subgroup. The eight T tables each have two involution classes, numbered 2 and 3 in CTblLib. The recorded fusion T → A is injective on these two classes, so each class is A-invariant. Take J to be class 3 for M₁₂ and class 2 in every other row. For α ∈ T, the ordinary T table gives the coefficient of J in the square of its T-class. For α outside T, A = T⟨α⟩ because α is an involution and |A:T|=2; its A-class equals its T-class, since α centralizes itself. Therefore the A-table class-square coefficient at the fusion image of J calculates exactly the square of α^T, and injectivity on T-involution classes ensures the target is J rather than a fusion of J with another T-class. A positive coefficient means the entire T-class J is present, by conjugacy invariance.

The certificate checks every inner and outer involution class against the complete class-order lists and the fusion map. Entries below are class index: coefficient; an empty outer list means that the full extension has no outer involutions. `F3+` is the CTblLib name for Fi₂₄′, and `2F4(2)` is the alias of `2F4(2)'.2`.

| T | J | inner classes | outer classes in A |
|---|---:|---|---|
| M12 | 3 | 2:12, 3:30 | 13:24 |
| J2 | 2 | 2:10, 3:120 | 17:120 |
| HS | 2 | 2:110, 3:200 | 22:20, 23:260 |
| He | 2 | 2:242, 3:630 | 27:1792 |
| Suz | 2 | 2:414, 3:6480 | 38:864, 39:8640 |
| HN | 2 | 2:2200, 3:46200 | 45:79200 |
| F3+ | 2 | 2:130572, 3:111891780 | 98:2, 99:119884050 |
| 2F4(2)' | 2 | 2:10, 3:100 | none |

## Sources and reproducibility

The external input is CTblLib 1.3.11, dated 2025-05-25 in its `PackageInfo.g`, bundled in the [GAP 4.15.1 release archive](https://github.com/gap-system/gap/releases/download/v4.15.1/gap-4.15.1.tar.gz), SHA-256 `6049d53e99b12e25c2d848db21ac4a06380a46fe4c4157243d556fe06930042c`. Its `MOT` records provide ordinary tables and its `ALF` records provide the stated T → A fusions. The identification of these groups and extensions with T and Aut(T), including |Out(T)|=2, is an ATLAS input also invoked in [C0015](../../claims/0015.md) and its [proof](../foundations/C0015.md); neither the GAP test nor table order alone establishes this identification.

The files under `pkg/ctbllib/data/`, including their MOT and relevant ALF records, have these SHA-256 hashes:

| File | T / extension MOT and fusion names | SHA-256 |
|---|---|---|
| ctomathi.tbl | M12 / M12.2 | `8a4c1d706cfca4d58975b056c935d83be305fbabfb05b4f147df26b8df8c9a96` |
| ctoconja.tbl | J2 / J2.2 | `949d710a6146064f0c4336cbc61edf70f10ab2ac4cc14df84ce9f2e0e1ea9a7d` |
| ctospora.tbl | HS, He, Suz, HN / their .2 extensions | `39854ca05e13eecbb1d2c60872d8de4d77b0a1d26c3da5b64767fdd442289a09` |
| ctofisc2.tbl | F3+ / F3+.2 | `db8a850f2870b7ee3a8e40800fc2719aee2761ba8efa63d5a03a7a3887e7b577` |
| ctotwis1.tbl | 2F4(2)' / 2F4(2)'.2 | `c98913edec288dfcc671ea20a1beb48099ed63595fd1cc5e871b447db96fc8c2` |

The [certificate](../code/verify_hs_eight_common_classes.g) checks both software versions, table orders and availability, full inner/outer involution-class lists, fusion injectivity and coverage, and all displayed exact coefficients. With that GAP and package version, run from the repository root:

```sh
gap -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_hs_eight_common_classes.g
```

An isolated build from the pinned release printed eight `common-class checks passed` lines. The script exits nonzero when an explicit check fails. Its computations are conditional on the source tables and fusions and do not independently establish their correctness, the group identifications, C0014, or its upstream dependencies. The scoped independent mathematical and source review is recorded below.

## Source verification and limitations

a separate automated checker accepted all eight common-class exclusions at its recorded source revision, conditional on the C0014 Case A nondegeneracy/disjointness inputs and their folder/inversion dependencies, and the published group/table/fusion data. The reviewer independently checked all eight full-Aut `InfoText` identifications and T→A `ALF` records, the five table-file hashes, fusion injectivity, complete inner/outer class lists and the positive-coefficient interpretation. The specified GAP 4.15.1 / CTblLib 1.3.11 run exited zero and reproduced all eight rows, including the Tits empty outer-involution list. This is not an independent construction of the character tables and does not settle HS for arbitrary Lie-type socles.
