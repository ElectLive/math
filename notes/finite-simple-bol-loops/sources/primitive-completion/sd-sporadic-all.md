# Candidate sporadic raw-F₃ screen

**Mira Cult**

This manuscript-local result, with the scoped review recorded below, for [C0010](../../claims/0010.md) uses the [raw-F₃ SD criterion](sd-raw-involution-count.md), including its primitive-folder and inversion dependencies, and the published CTblLib character-table identifications and data. For each of the 21 sporadic simple groups with n≥2²⁰ listed below, it verifies the criterion for every k≥3. The five below threshold are not covered by that criterion; their separate arguments are in [three sporadic socles](sd-three-sporadic-socles.md) and [finite common classes](sd-finite-common-classes.md), subject to their own scopes and reviews. No overall classification or census of all simple groups is claimed.

The [ATLAS sporadic index](https://brauer.maths.qmul.ac.uk/Atlas/spor/) explicitly lists the 26 groups, plus the Tits group separately. The list of 12 groups with outer automorphism group of order two, and assertion that the other 14 have trivial outer automorphism group, is in §8 of [A description of the solvable radical](https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2007/140.pdf). Compare the 26-name list and Out indices in [the GAP certificate](../code/verify_sd_sporadic_all.g). The source tables' identifications with full automorphism groups are assumptions supplied by CTblLib; their source-level checks are recorded in the review below; correctness remains an external mathematical input.

Run `gap -q problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_sporadic_all.g` under GAP 4.15.1 with bundled CTblLib 1.3.11. The certificate checks the exact group sizes, resolved identifiers, sums class sizes whose square map is the identity, and verifies b³+3ab<n² using the displayed socle orders. All 26 tables pass this inequality. Exactly five are below 2²⁰, namely M11, M12, M22, J1 and J2; raw-F3 theorem is therefore applicable only to the other 21 subject to its folder dependencies. The five have separate arguments elsewhere.

The [GAP 4.15.1 release archive](https://github.com/gap-system/gap/releases/download/v4.15.1/gap-4.15.1.tar.gz) has SHA256 6049d53e99b12e25c2d848db21ac4a06380a46fe4c4157243d556fe06930042c. Bundled CTblLib data files and SHA256: ctomathi.tbl 8a4c1d706cfca4d58975b056c935d83be305fbabfb05b4f147df26b8df8c9a96; ctoconja.tbl 949d710a6146064f0c4336cbc61edf70f10ab2ac4cc14df84ce9f2e0e1ea9a7d; ctofisc1.tbl 60cbbc37c9042af8f9c19b402556ec85ce604d1042f3dab5ece61bf75259086b; ctofisc2.tbl db8a850f2870b7ee3a8e40800fc2719aee2761ba8efa63d5a03a7a3887e7b577; ctospora.tbl 39854ca05e13eecbb1d2c60872d8de4d77b0a1d26c3da5b64767fdd442289a09; ctomonst.tbl e625b7b299b3de01f526b86758d400b1942066e0691a4534663fc84fd919231f. The name Fi24'.2 resolves to the table F3+.2. Source records and full automorphism identifications were checked in the scoped review below; the reliability of CTblLib class sizes and power maps remains an external input. The computation cannot prove those inputs or an exhaustive census by itself.


## Complete inputs

Columns: requested table, socle order n, full-automorphism order a, b including identity, resolved table identifier.

```text
M11 7920 7920 166 M11
M12.2 95040 190080 1684 M12.2
M22.2 443520 887040 2872 M22.2
M23 10200960 10200960 3796 M23
M24 244823040 244823040 43264 M24
J1 175560 175560 1464 J1
J2.2 604800 1209600 4636 J2.2
J3.2 50232960 100465920 46684 J3.2
J4 86775571046077562880 86775571046077562880 51747149312 J4
Co1 4157776806543360000 4157776806543360000 12792894976 Co1
Co2 42305421312000 42305421312000 29771776 Co2
Co3 495766656000 495766656000 2778976 Co3
Fi22.2 64561751654400 129123503308800 79466752 Fi22.2
Fi23 4089470473293004800 4089470473293004800 12895196032 Fi23
Fi24'.2 1255205709190661721292800 2510411418381323442585600 13510933563520 F3+.2
HS.2 44352000 88704000 45376 HS.2
McL.2 898128000 1796256000 135676 McL.2
He.2 4030387200 8060774400 478976 He.2
Ru 145926144000 145926144000 1846576 Ru
Suz.2 448345497600 896690995200 5644432 Suz.2
O'N.2 460815505920 921631011840 5482072 ON.2
HN.2 273030912000000 546061824000000 150843376 HN.2
Ly 51765179004000000 51765179004000000 1296826876 Ly
Th 90745943887872000 90745943887872000 976841776 Th
B 4154781481226426191177580544000000 4154781481226426191177580544000000 512299100893413376 B
M 808017424794512875886459904961710757005754368000000000 808017424794512875886459904961710757005754368000000000 5791748165751443778953445376 M
```

## Independent review

contributor 1 accepted this screen at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/f6c7e01a4337b51c703b4d9ffc94d3b84a732fe5), conditional on the raw-F₃ criterion, folder/inversion dependencies and published ATLAS/CTblLib data. The reviewer checked the 26-name ATLAS inventory, the twelve outer-index-two groups against the primary §8 source, and all twelve CTblLib `InfoText` full-Aut construction records (including Fi₂₄′ aliases). An independent GAP check matched every socle order and outer index, and the certificate reproduced all 26 inequalities with exactly 21 above threshold. All six table-file SHA-256 hashes matched. The release archive hash was not independently rechecked because that archive was unavailable to the reviewer. This is not an independent derivation of the character tables or a proof for the five below-threshold groups, whose separate arguments remain necessary.
