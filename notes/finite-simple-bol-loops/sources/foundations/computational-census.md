# Reproducible Computational Evidence and Census Summary (`0323`)

This record documents the deterministic, standard-library Python and C99 computations supporting claims `0323-finite-simple-non-moufang-bol-loops:C0001` through `0323-finite-simple-non-moufang-bol-loops:C0017`. Computations verify finite witnesses, finite-range case exclusions, negative/positive controls, and exact isomorphism counts; they do not by themselves prove universal theorems on unbounded families.

## Independently rerun checkpoint checks (2026-11-14)

At exact source commit [the source revision](https://github.com/Mira-Cult/math-wip/commit/cb82ee03bac4046f6a3fcfc44f556dd8f228b6ac), the agent `verify_engine` inspected the default suite and its imports and ran, from the repository root:

```bash
python3 -B -W error problems/0323-finite-simple-non-moufang-bol-loops/code/test_bol_engine.py
```

The executable was the bundled Python 3.12.14; optional C helpers used Apple clang 17.0.0 (`clang-1700.6.3.2`), with a dedicated temporary directory. Result: **23 tests passed in 71.529 seconds**, exit 0. These deterministic fast tests include the fast Wave 2/3 checks; they do not run the extended suite or full exhaustive census and do not verify universal mathematical assertions. No random seed was used. Raw logs and build products are outside Git.

At source commit [the source revision](https://github.com/Mira-Cult/math-wip/commit/6c5bd2b3e0cc79b8a11222aef359598085ebf922), independent reviewer contributor 1 compiled `code/verify_as_quandles_21_24.c` with `clang -O3` in a unique temporary directory and ran the binary (Apple clang 17.0.0). The C source SHA-256 was `3a355e88832deeb0cb62c480e2e769626aa7571dad8aa5cea6006be5a78aea2f`. Result: exit 0, 111.562 CPU seconds; degree 21, fixed-point count 11 yielded 12 solutions, all 12 fully table-isomorphic to the S7 transposition quandle, zero unknown. Other enumerated degree-21 counts and all enumerated degree-24 counts yielded zero solutions. The reviewer accepted the new full-table isomorphism check and the analytic fixed-point-count-1 exclusion under their stated hypotheses, but did **not** certify the remaining enumeration/pruning, group classification inputs, or C0011 as a whole. This is a bounded review and reproducibility record, not a claim-wide acceptance.

The remaining sections below preserve the earlier producer report. They do not supply exact source pins for every historical run. In particular, the C0011 quandle-search coverage defects recorded in the canonical claim qualify the earlier uniqueness wording until corrected and rerun.

## Toolchain and Reproduction Commands

- **Verified environment**: macOS (`Darwin`), `Python 3.9.6` and `Python 3.12.13` (`-B -W error`), standard library only; optional `${TMPDIR:-/tmp}` C99 helpers via `Apple clang 17.0.0` (`-O3`, unlinked immediately on exit).
- **Exact commands** (run from repository root):

```bash
# Fast automated unit test suite (23 tests including TestLMltExclusions, TestWave2Fast, TestWave3Fast)
python3 -B -W error problems/0323-finite-simple-non-moufang-bol-loops/code/test_bol_engine.py

# Extended higher-order certifications (orders 960, 1053, 1152, 1344, 1536 20-class census + non-simple 1536 control)
python3 -B -W error problems/0323-finite-simple-non-moufang-bol-loops/code/test_bol_engine.py --extended

# Standalone fast (< 0.1s) LMlt(Q) exclusion verifier for C0007
python3 -B -W error problems/0323-finite-simple-non-moufang-bol-loops/code/test_lmlt_exclusions.py

# #0323/S1 rank-obstruction & Wave-2/3 census suites (C0008, C0009, C0011, C0012, C0014-C0017)
python3 -B -W error problems/0323-finite-simple-non-moufang-bol-loops/code/test_s1_obstructions.py
python3 -B -W error problems/0323-finite-simple-non-moufang-bol-loops/code/test_wave2_census.py
python3 -B -W error problems/0323-finite-simple-non-moufang-bol-loops/code/test_wave3_rank3.py
python3 -B -W error problems/0323-finite-simple-non-moufang-bol-loops/code/verify_wave2_folder_s1.py
python3 -B -W error problems/0323-finite-simple-non-moufang-bol-loops/code/verify_wave3_rank3_nagy.py

# Multi-module solvable-LMlt family Q_{p,q;R} verifier (C0013, orders 1053 and 28,431)
python3 -B problems/0323-finite-simple-non-moufang-bol-loops/code/verify_q_pqr_family.py

# Exact order <= 24 uniqueness verifiers (C0011: wreath branch-and-bound + AS involutory-quandle solver)
python3 -B problems/0323-finite-simple-non-moufang-bol-loops/code/verify_24_c.py
clang -O3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_as_quandles_21_24.c \
  -o "${TMPDIR:-/tmp}/verify_as_quandles_21_24" && \
  "${TMPDIR:-/tmp}/verify_as_quandles_21_24" && rm -f "${TMPDIR:-/tmp}/verify_as_quandles_21_24"

# Constructive witness table and full Sweeps A-D discovery & deduplication census
python3 -B -W error problems/0323-finite-simple-non-moufang-bol-loops/code/known_constructions.py
python3 -B -W error problems/0323-finite-simple-non-moufang-bol-loops/code/search_folders.py
```

## Certified Constructive Witnesses and Controls (`known_constructions.py`, `verify_q_pqr_family.py`)

Every simple proper witness below is certified by left Bol verification, an explicit Moufang failure triple, simplicity verification (loop-congruence closure and/or Atkinson primitivity of $`\mathop{\mathrm{Mlt}}\nolimits(Q)`$), and group-order / permutation-rank verification:

| Witness | Construction / Family | $`|Q|`$ | $`\exp(Q)`$ | $`|\mathop{\mathrm{LMlt}}\nolimits(Q)|`$ | $`\mathop{\mathrm{LMlt}}\nolimits`$ solvable? | $`|N_\lambda|, |N_\mu|, |N_\rho|`$ | Bruck? | $`\mathop{\mathrm{Mlt}}\nolimits(Q)`$ | $`\mathop{\mathrm{rank}}\nolimits(\mathop{\mathrm{Mlt}}\nolimits)`$ |
|---|---|---:|---:|---:|---|---|---|---:|---:|
| $`Q_{24}`$ | Exact fact. $`S_4 = C_4 \cdot S_3`$ (`C0003`, `C0011` unique) | $`24`$ | $`12`$ | $`288`$ | Yes (`288>144>16>1`) | $`1, 1, 2`$ | No | $`A_{24}`$ | $`2`$ |
| $`Q_{60}`$ | Exact fact. $`A_5 = C_5 \cdot A_4`$ (`C0002`, `C0012` imprimitive) | $`60`$ | $`30`$ | $`3600`$ | No ($`A_5^2`$) | $`1, 1, 2`$ | No | $`A_{60}`$ | $`2`$ |
| $`N_{96}^{\mathrm{op}}`$ (`4` classes) | `N07E` $`k=0`$ Bruck + $`2`$ exp-$`4`$ + $`1`$ rigid exp-$`12`$ (`C0006`) | $`96`$ | $`2, 4, 12`$ | $`3840`$ | No ($`2^5 . S_5`$) | $`1, 1, 1`$ | $`1`$ Yes, $`3`$ No | $`A_{96}`$ | $`2`$ |
| $`Q_{120}`$ | Exact fact. $`S_5 = F_{20} \cdot S_3`$ (`C0002`) | $`120`$ | $`60`$ | $`7200`$ | No | $`1, 1, 2`$ | No | $`A_{120}`$ | $`2`$ |
| $`Q_{168}`$ | Exact fact. $`\mathop{\mathrm{PSL}}\nolimits_3(2) = C_7 \cdot S_4`$ (`C0002`) | $`168`$ | $`84`$ | $`28{,}224`$ | No | $`1, 1, 3`$ | No | $`A_{168}`$ | $`2`$ |
| $`Q_{960}`$ | Affine-simple $`\mathbb{F}_4^2 \rtimes \mathop{\mathrm{SL}}\nolimits_2(4)`$ (`C0004`, $`5`$ classes) | $`960`$ | $`60`$ | $`921{,}600`$ | No ($`2^8 : A_5^2`$) | $`1, 1, 4`$ | No | $`A_{960}`$ | $`2`$ |
| $`Q_{1053}`$ | Odd-order $`Q_{3,13}`$ (`C0003`, `C0013` $`k=1`$) | $`1053`$ | $`117`$ | $`369{,}603`$ | Yes (odd order) | $`1, 1, 3`$ | No | $`A_{1053}`$ | $`2`$ |
| $`Q_{1152}`$ | Solvable wreath $`S_4 \wr C_2 = \mathop{\mathrm{SD}}\nolimits_{16} \cdot (S_3 \wr C_2)`$ (`C0003`) | $`1152`$ | $`24`$ | $`331{,}776`$ | Yes | $`1, 1, 2`$ | No | $`A_{1152}`$ | $`2`$ |
| $`Q_{1344}`$ | Affine-simple $`\mathbb{F}_2^3 \rtimes \mathop{\mathrm{SL}}\nolimits_3(2)`$ (`C0004`, $`7`$ classes) | $`1344`$ | $`84`$ | $`1{,}806{,}336`$ | No ($`2^6 : \mathop{\mathrm{SL}}\nolimits_3(2)^2`$) | $`1, 1, 4`$ | No | $`A_{1344}`$ | $`2`$ |
| $`Q_{1536}`$ (`20` classes) | Deformed `N07E` $`k=1`$: $`1`$ Bruck exp-$`2`$, $`18`$ exp-$`4`$, $`1`$ rigid exp-$`12`$ (`C0006`, `C0012`) | $`1536`$ | $`2, 4, 12`$ | $`983{,}040`$ | No ($`2^{13} . S_5`$) | $`1, 1, 1`$ | $`1`$ Yes, $`19`$ No | $`A_{1536}`$ | $`2`$ |
| $`Q_{4860}`$ | Odd-char affine-simple $`3^4 \rtimes A_5`$ (`C0004`) | $`4860`$ | $`90`$ | $`23{,}619{,}600`$ | No ($`3^8 : A_5^2`$) | $`1, 1, 6`$ | No | $`A_{4860}`$ | $`2`$ |
| $`Q_{3,13;\{1,2\}}`$ | Multi-module odd-order (`C0013` $`k=2`$, $`|\mathop{\mathrm{Aut}}\nolimits|=3`$) | $`28{,}431`$ | $`117`$ | $`269{,}440{,}587`$ | Yes (odd order) | $`1, 1, 3`$ | No | $`2`$-trans. | $`2`$ |
| $`Q_{3,13;\{1,4\}}`$ | Multi-module odd-order (`C0013` $`k=2`$, $`|\mathop{\mathrm{Aut}}\nolimits|=6`$) | $`28{,}431`$ | $`117`$ | $`269{,}440{,}587`$ | Yes (odd order) | $`1, 1, 3`$ | No | $`2`$-trans. | $`2`$ |
| `ext_1536` (control) | Undeformed `N07E` Prop. 5.1 (`deformed=False`) | $`1536`$ | $`2`$ | $`983{,}040`$ | No | — | Yes | Not simple (`|N|=16`) | — |
| $`M(2)`$ (control) | Paige simple Moufang loop (`C0009`, `C0017`) | $`120`$ | $`6`$ | $`174{,}182{,}400`$ | No ($`\Omega_8^+(2)`$) | $`1, 1, 1`$ | No | $`\Omega_8^+(2)`$ (Moufang) | $`3`$ (`1,56,63`) |
| $`M(3)`$ (control) | Paige simple Moufang loop (`C0009`, `C0016`, `C0017`) | $`1080`$ | $`4`$ | $`\frac{1}{2}|\Omega_8^+(3)|`$ | No ($`\mathop{\mathrm{P\Omega}}\nolimits_8^+(3)`$) | $`1, 1, 1`$ | No | $`\mathop{\mathrm{P\Omega}}\nolimits_8^+(3)`$ (Moufang) | $`3`$ (`1,351,728`) |

## Exhaustive Discovery and Uniqueness Censuses

1. **Order $`\le 24`$ unconditional uniqueness (`verify_24_c.py`, `verify_as_quandles_21_24.c`, `test_wave2_census.py` — `C0011`)**:
   - Exhaustive wreath-imprimitive twisted-involution branch-and-bound across all transitive wreath configurations of degree $`m = b \cdot c \le 24`$ (`verify_24_c.py`, `85.6s`) finds zero simple nonassociative folders at $`m < 24`$ and `46` hits in $`S_3 \wr S_4`$ at $`m = 24`$, **every one** certified loop-isomorphic to $`Q_{24}`$.
   - Exhaustive C99 involutory-quandle search across $`M \in \{21, 24\}`$ (`verify_as_quandles_21_24.c`, `107.2s`) proves no faithful transitive `AS` involutory quandle exists at $`M = 24`$, and the unique connected one at $`M = 21`$ is the $`21`$ transpositions of $`S_7`$ (`|G| = 5040 = 240 \cdot 21`), which admits zero core-free $`H \le S_7`$ of order $`240`$ (`test_wave2_census.py`).
2. **Sweeps A–D (`search_folders.py`) & $`Q_{1536}`$ $`20`$-class isotopy census (`known_constructions.py` — `C0002`–`C0006`, `C0012`)**:
   - Sweep A (`|X| <= 720`): $`15`$ isomorphism classes ($`24(1), 60(1), 120(1), 168(1), 336(2), 360(2), 504(1), 660(2), 720(4)`$).
   - Sweep B (`N_{96}^op` & `Q_{1536}` principal isotopes): $`4`$ classes at order $`96`$ (`1 + 10 + 5 + 80 = 96`) and **$`20`$** classes at order $`1536`$ (`1 + 3*5 + 6*10 + 9*20 + 1280 = 1536`, comprising $`1`$ Bruck exp-$`2`$, $`18`$ non-Bruck exp-$`4`$ simple $`2`$-loops, and $`1`$ rigid $`|\mathop{\mathrm{Aut}}\nolimits| = 1`$ exp-$`12`$ loop).
   - Sweep C (`960, 1344`): $`5`$ classes at order $`960`$ and $`7`$ classes at order $`1344`$.
   - Sweep D (`S_4 wr C_2`): $`1`$ class ($`Q_{1152}`$).
   - Together with $`Q_{1053}`$, $`Q_{4860}`$, and $`Q_{3,13;\{1,2\}}, Q_{3,13;\{1,4\}}`$, all **$`56`$** certified simple proper left Bol loop isomorphism classes through order $`28{,}431`$ ($`53`$ up to order $`1536`$) satisfy $`\mathop{\mathrm{rank}}\nolimits(\mathop{\mathrm{Mlt}}\nolimits(Q)) = 2`$.

## `LMlt(Q)` and `#0323/S1` Rank-3 Exclusion Suites (`C0007`–`C0009`, `C0014`–`C0017`)

- **`test_lmlt_exclusions.py` (`C0007`)**: Certifies $`A_m, S_m`$ small/boundary regimes ($`5 \le m \le 45`$), $`\mathop{\mathrm{Aut}}\nolimits(A_6) = \mathop{\mathrm{P\Gamma L}}\nolimits_2(9)`$, $`\mathop{\mathrm{PSL}}\nolimits_2(7), \mathop{\mathrm{PGL}}\nolimits_2(7), \mathop{\mathrm{PSL}}\nolimits_2(8)`$, and $`|C_{\mathop{\mathrm{SU}}\nolimits_3(4)}(\phi_0)| = 60`$.
- **`test_wave2_census.py` & `verify_wave2_folder_s1.py` (`C0014`, `C0015`, `C0016`)**: Certify zero primitive nonassociative left Bol folders `LMlt(Q)` across all primitive groups of degree $`\le 50`$ (`HA, AS, HS, SD_2, PA`) and `AS` groups to degree $`120`$, full `10/10` quadratic-monomial rank on $`(4, \pm)`$ over $`\mathbb{F}_3`$, zero $`\Delta_1`$-UOD elements in $`\mathop{\mathrm{P\Gamma U}}\nolimits_4(2)`$ (`deg 40`), and exact rank $`3`$ (`1, 351, 728`) of Paige's $`M(3)`$.
- **`test_wave3_rank3.py` & `verify_wave3_rank3_nagy.py` (`C0016`, `C0017`)**: Certify all closed-form and $`18`$ individual Spectral Trace Integrality exclusions, $`\mathrm{NO}_{2m}^\varepsilon(3)`$ hyperplane bounds, $`\mathrm{NU}_{2k}(2)`$ and $`\Gamma\mathop{\mathrm{Sp}}\nolimits_{4s}(8)`$ Gauss-sum bounds, $`\mathop{\mathrm{Sp}}\nolimits_4(q)`$ Lagrangian pigeonhole exclusion, and exhaustive UOD / left-Bol transversal nonexistence across all Spectral-Trace-integral individual rank-$`3`$ `AS` actions (`G_2(2)(36)`, `PSU_3(5)(50)`, `J_2(100)`, `HS(100)`, `S_9(120)`, `Sp_4(4)(120, 136)`, `PSU_4(3)(162)`) plus `Sp_4(8).3(2016)`.

## Integrity checkpoint, 2026-11-14

At source [the source revision](https://github.com/Mira-Cult/math-wip/commit/65c54aff108cc70208bf6f7271b1e5cf6a0a76bc), Python 3.12.14 ran `python check.py --base the recorded source revision`: all 115 tool/integrity tests passed (10.605 seconds test time). This checks repository metadata and tool behavior only. The historical rank-3 completeness report above was overbroad: C0017 records the missing G₂(2), J₂ and HS action computations found at source [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). New temporary runs are not a substitute for source-pinned, independently reviewed evidence.

## Three repaired rank-three actions

At exact revision [the source revision](https://github.com/Mira-Cult/math-wip/commit/08e0fbb08fcc9b7da728e2ae6558695992ca2682), independent reviewer contributor 2 ran `python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_rank3_missing_actions.py` with Python 3.12.14. The four embedded ATLAS v3.004 byte hashes matched independent downloads. Results (subdegree: representative-coset UOD count): J₂:2 degree 100, `36:0, 63:64`; local PSU₃(3):2 degree 36, `14:4, 21:0`; HS:2 degree 100, `22:0, 77:1920`. Each zero excludes translations to that suborbit. This deterministic offline enumeration covers only the stated actions; the proof and scoped review are in C0017. No random seed, network runtime or native build is used. The same reviewer ran the repository integrity checker with Python 3.12.14: 115 tests passed.

At the earlier exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/65c54aff108cc70208bf6f7271b1e5cf6a0a76bc), reviewer contributor 3 ran `python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_24_c.py` with Python 3.12.14 and Apple clang 17.0.0: exit 0 in 88.58 seconds, zero hits for all configured below-24 cases, and all 46 order-24 hits checked isomorphic to Q₂₄. Source SHA-256: `234a9ee5ac23c4713202d5b39b7eb0393bcc7127cfdc699a29821036ef196f0e`. This run does not establish group-list completeness or the whole classification theorem. A separately found copying bug for hypothetical below-24 multiple-hit runs does not affect these zero-hit cases or the order-24 table stride; its repair is a later source change. Raw logs remain outside Git.
