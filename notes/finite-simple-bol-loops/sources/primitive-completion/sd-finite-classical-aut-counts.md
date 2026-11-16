# Finite classical automorphism involution counts

Mira Cult
This application, with scoped independent review below, concerns [C0010](../../claims/0010.md) uses the [raw-involution criterion](sd-raw-involution-count.md) for finite simple socles T of order n ≥ 2²⁰. Its exclusions remain conditional on that criterion and its upstream primitive-folder, inversion and group-theoretic assumptions. The complete character tables identified below are external computational inputs, not proofs of their own correctness or of those assumptions.

Let a = |Aut(T)| and let b count elements α ∈ Aut(T) with α² = 1, including the identity. The following full automorphism-group table data give the exact b values conditional on the tables and their identifications. The strict raw criterion b³ + 3ab < n² passes for six rows and fails for the starred row. A failure is not evidence that a loop exists.

| CTblLib table | n | a | b | Raw screen |
|---|---:|---:|---:|---|
| L4(3).2^2 | 6,065,280 | 24,261,120 | 27,640 | pass |
| L4(4).2^2 | 987,033,600 | 3,948,134,400 | 414,704 | pass |
| U4(3).D8 | 3,265,920 | 26,127,360 | 28,576 | fail* |
| U4(4).4 | 1,018,368,000 | 4,073,472,000 | 335,856 | pass |
| U4(5).2^2 | 14,742,000,000 | 58,968,000,000 | 2,391,776 | pass |
| U5(2).2 | 13,685,760 | 27,371,520 | 22,144 | pass |
| U6(2).3.2 | 9,196,830,720 | 55,180,984,320 | 1,529,056 | pass |

Here Ld(q) and Ud(q) denote PSL_d(q) and PSU_d(q). For the failure PSU₄(3), the two sides are 25,574,658,605,056 and 10,666,233,446,400. The common-class section below supplies an alternative route, using the simple-group table and the independently computed fusion evidence. The inspected table files did not reveal full-Aut MOT entries for PSL₄(5), PSL₄(9), PSU₄(7), PSU₄(8), or PSU₅(4). That observation does not prove such tables unavailable.

## Source and extraction

The source is CTblLib 1.3.11, bundled with the [GAP 4.15.1 release archive](https://github.com/gap-system/gap/releases/download/v4.15.1/gap-4.15.1.tar.gz), archive SHA-256 `6049d53e99b12e25c2d848db21ac4a06380a46fe4c4157243d556fe06930042c`. The package's `PackageInfo.g` identifies version 1.3.11 dated 2025-05-25. Each selected `MOT` record's construction text explicitly identifies it as Aut(T). In `pkg/ctbllib/data/` the source files and SHA-256 hashes are:

| File | MOT names | SHA-256 |
|---|---|---|
| ctoline5.tbl | L4(3).2^2 | `f8b9c5ca373967a4da847dd25fdedae54818b5852bd86b2a39032a0d07013418` |
| ctoline6.tbl | L4(4).2^2 | `5a2e4062716a0f14e1ecaf284c8797a5f39d4a78a98b0f9e327fd93f75970392` |
| ctounit1.tbl | U4(3).D8 | `231520234a02003db512a9022e059716115f76852e36a623c59cf8ce739a0227` |
| ctounit5.tbl | U4(4).4, U4(5).2^2 | `10993cac030d835624440787bef4d40d03e3ebdecba3b620c1f5b39e0b7158e2` |
| ctounit3.tbl | U5(2).2 | `7f269dcf70f83359a657b67e0c00279c8791f51b8a4a665156b540e9ee64a1cf` |
| ctounit4.tbl | U6(2).3.2 | `9c6ec1dd961331c50bde92e4faca85b8646f23f6cf5fa263f9f36c1463a1adf4` |


For each named MOT record, read its first integer list as class centralizer orders and the first populated list in the following power-map list as the square map, with 1-based class indices. Select exactly those positions whose square map equals 1, including the identity; each selected class contributes a divided by its centralizer order. Check that both lists have equal lengths, indices lie in range, the identity maps to itself, and all centralizers divide a. The [arithmetic certificate](../code/verify_sd_finite_classical_aut_counts.py) records just the selected centralizers and independently checks their sums, the threshold, and the seven inequalities. It does not itself parse the downloaded tables or verify that those selected entries are complete.

Run from the repository root:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_finite_classical_aut_counts.py
```

The table extraction, source identification, and this application await independent review; the certificate checks only integer arithmetic on the supplied extracted entries.

## PSU₄(3): common-class route

This separately reviewed addition uses the CTblLib ordinary character table `U4(3)` as an external input. It has order 3,265,920 and exactly one involution class, class 2. Therefore that class J is invariant under Aut(T). The reviewed single-class square lemma in [the SD₃ manuscript](sd3-involution-count.md#candidate-extension-all-psl₂q) gives J ⊆ (α^T)² for every nonidentity involutory α ∈ Aut(T). Since n ≥ 2²⁰, the reviewed common-class theorem in [the large-socle manuscript](sd-large-socles.md) conditionally excludes SD_k for every k ≥ 3, subject to its folder, inversion, semiregularity, CFSG and source assumptions. This is an alternative to the raw inequality, which still fails as recorded above. Together with the other separately established cases of the linear/unitary screen, this addresses its PSU₄(3) residual, subject to all their respective dependencies and reviews.

As a separate computational check of the square condition, use the ordinary tables and recorded fusions for T, A = Aut(T), and the index-two extensions H = `U4(3).2_1`, `.2_2`, `.2_3`. In each H, the class of an outer involution α equals α^T because H = T⟨α⟩ and α centralizes itself. Thus its class-square coefficient in H, at the image of J, tests the required T-orbit square; merely squaring an A-class would not suffice. For inner involutions the coefficient at J in T is 66. For outer classes the certificate checks:

| H | H class | A class | coefficient at J |
|---|---:|---:|---:|
| U4(3).2_1 | 19 | 15 | 12 |
| U4(3).2_1 | 20 | 16 | 120 |
| U4(3).2_2 | 19 | 39 | 2 |
| U4(3).2_2 | 20 | 40 | 90 |
| U4(3).2_3 | 16 | 53 | 72 |

The complete A-table involution classes are 2, 15, 16, 39, 40, 53; their coverage by the table and fusion entries above, together with Aut(T)-invariance of J, transfers the property to every involution. The T, H and A tables and the relevant recorded fusions are in `pkg/ctbllib/data/ctounit1.tbl`, whose SHA-256 is `231520234a02003db512a9022e059716115f76852e36a623c59cf8ce739a0227`, from the pinned GAP 4.15.1 / CTblLib 1.3.11 archive identified above. Table and fusion identification and correctness are external inputs.

The [GAP certificate](../code/verify_sd_u43_common_class.g) checks versions, group orders, involution-class lists, fusions, coefficients and coverage. With GAP 4.15.1 and CTblLib 1.3.11 installed, run from the repository root:

```sh
gap -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_u43_common_class.g
```

The isolated build from the pinned archive printed `U4(3) common-class table checks passed`. The script exits with a nonzero status on a failed check. Its table calculations do not verify the external tables or replace review of the lemma and upstream hypotheses.

## Source verification and limitations

automated reviewers a separate automated checker accepted the six raw-count applications and the PSU4(3) common-class argument at its recorded source revision, conditional on external CTblLib tables/fusions and the prior raw, square-class and large-socle results. The reviewer independently extracted all seven centralizer lists using GAP 4.15.1 / CTblLib 1.3.11, checked all six file hashes and all seven MOT full-Aut identification texts, and ran both pinned certificates. The PSU4(3) proof correctly uses T-conjugacy through index-two extensions and complete Aut-fusion coverage. The raw PSU4(3) inequality still fails; the common-class alternative is the accepted route. Published table correctness remains an external input.
