# Sharper orthogonal raw-F₃ screen using class numbers

Mira Cult
This conditional argument for [C0010](../../claims/0010.md) has scoped independent review below and is conditional on the no-common-class raw-F₃ criterion and its primitive Bol-folder and inversion inputs. It refines the exact R≤1030² finite grid in [the orthogonal raw screen](sd-orthogonal-raw-bounds.md); a remaining parameter is only a failure of the sufficient upper bound, not evidence for an SD loop. Only simple groups of order n≥2²⁰ are considered.

Let T be one of the B_r(q) or D_r^±(q) groups and t=|Out(T)|, a=tn. Fulman–Guralnick, *Bounds on the number and sizes of conjugacy classes in finite Chevalley groups*, Trans. AMS 364 (2012), Lemma 2.1(1)–(2), p.3027, Table 2, p.3050, and Corollary 1.2(3), p.3025, https://doi.org/10.1090/S0002-9947-2012-05427-4, give k(Aut T)≤min(t k(T),100q^r), with these Table 2 bounds:

- B_r(q) with q odd: k(T)≤7.3q^r, since the projective quotient has no more classes than Ω(2r+1,q);
- B_r(q)=C_r(q) with q even: k(T)≤15.2q^r;
- D_r^±(q) with q odd: k(T)≤6.8q^r;
- D_r^±(q) with q even: k(T)≤14q^r.

Let c10 be ten times the appropriate listed constant, and set C10=min(1000,c10 t). Frobenius–Schur and Cauchy–Schwarz give b²≤a k(Aut T)≤a q^r C10/10, where b counts automorphisms squaring to one, including identity. Thus the least integer B with 10B²≥a q^r C10 is a safe upper bound on b. If B³+3aB<n², the raw-F₃ criterion applies with no common-class hypothesis.

The exact integer script [the arithmetic certificate](../code/verify_sd_orthogonal_refined_bounds.py) checks every R-fail parameter in the finite grid, using the exact n,t formulas, threshold/tail proof, and source qualifications of [the orthogonal raw screen](sd-orthogonal-raw-bounds.md). It reports the following newly passing parameters:

- B₂: q∈{17,19,23,29,31,37,41,43,47,49,53,59,61,125,256};
- B₃: q=3;
- D₄^−: q=3.

The remaining parameters of this specific sufficient-bound screen are:

- B₂: q∈{5,7,8,9,11,13,16,25,27,32,64,81,128};
- B₃: q=2;
- D₄^+: q∈{2,3};
- D₄^−: q=2.

No previously R-passing case is reclassified. B₂(3) and B₂(4) lie below n threshold and are outside this screen; B₂(2) is not simple. The computation and all exact group-order/outer-order conventions, source interpretation, and upstream no-common-class criterion need independent mathematical review. The finite script checks rational upper bounds rather than claiming exact involution counts.

## Three full-automorphism table checks

The following additional checks use the full automorphism groups, including triality. Let b include the identity. Each centralizer listed is for a nonidentity class whose square is the identity.

| T | n | a=|Aut(T)| | b | Centralizers |
|---|---:|---:|---:|---|
| PΩ₈⁺(2) | 174182400 | 1045094400 | 183376 | 663552, 92160, 18432, 2903040, 9216 |
| PΩ₈⁺(3) | 4952179814400 | 118852315545600 | 93148624 | 209018880, 7962624, 97044480, 4147200, 18341406720, 2488320 |
| PΩ₈⁻(2) | 197406720 | 394813440 | 112592 | 368640, 92160, 6144, 2903040, 9216 |

The input is GAP 4.15.1's bundled CTblLib 1.3.11: [release archive](https://github.com/gap-system/gap/releases/download/v4.15.1/gap-4.15.1.tar.gz), SHA-256 `6049d53e99b12e25c2d848db21ac4a06380a46fe4c4157243d556fe06930042c`. In `pkg/ctbllib/data/`, `ctoorth2.tbl` has SHA-256 `cf250c9b4ada37a8c8e5fc93570ba3c24c9cd9197baf8a646e568194de2afdce` and `ctoorth3.tbl` has SHA-256 `736b8f34211dd8a20c51312015fa72c1bb0a4931db19b317ea436ac0e9644626`. The respective records are `O8+(2).3.2`, `O8+(3).S4`, and `O8-(2).2`; [CTblLib table descriptions](https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/) identify the tables. The source records supply centralizer orders and the square power map. A format-specific extraction takes the two lists following each unique `MOT("name",` record and selects positions mapping to the identity. The certificate independently checks divisibility, sums the listed class sizes plus one, and verifies b³+3ab<n² exactly. The published data and their identification with these full automorphism groups are inputs, not consequences of the arithmetic certificate.

Combining these checks with the preceding class-bound screen eliminates the four displayed D₄ residual parameters, and B₃(3); B₃(2) and the displayed B₂ residuals require other arguments. The [refined symplectic screen](sd-classical-raw-bounds.md) supplies additional overlapping B₂/B₃ checks, subject to its stated scope. No census is claimed. These additions have not received independent mathematical review.

## Source verification and limitations

automated reviewers a separate automated checker accepted the refined orthogonal screen at its recorded source revision, conditional on the raw criterion, inherited group-order and tail inputs, and published CTblLib identifications. The review checked the FG constants and Gallagher deduction, ran the Python 3.12.14 certificate, and independently queried all three full automorphism tables with GAP 4.15.1 / CTblLib 1.3.11. Sizes, square-map selections, centralizers and both table-file SHA-256 hashes agree. The remaining B2/B3 entries are covered by the separately reviewed symplectic route; no other primitive action type is excluded here.
