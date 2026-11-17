# Candidate orthogonal raw-R screen

**Mira Cult**

This manuscript-local result, with scoped review below, concerns [C0010](../../claims/0010.md) checks the B_r and D_r^± raw-R screen. It assumes the candidate [raw-F₃ SD criterion](sd-raw-involution-count.md), the [classical R estimate](sd-classical-raw-bounds.md) and their folder, inversion and classification-dependent inputs. Put q=p^f, n=|T|, t=|Out(T)|, R=n/(t³q^(3r)); only n≥2²⁰ and R>1030² are in scope. These are sufficient screens and their failure is not evidence for a loop.

## Sources and group formulas

Kleidman–Liebeck, *The Subgroup Structure of the Finite Classical Groups* (1990), [publisher preview](https://api.pageplace.de/preview/DT0400.9780511892394_A23680360/preview-9780511892394_A23680360.pdf), Tables 2.1.C–D, printed p.19, give the orders and indices for odd and even orthogonal types; Theorems 2.1.3–2.1.4, p.16, identify full automorphisms and explicitly add the triality factor three in plus-type dimension eight. These pages were visually inspected. Fulman–Guralnick, *Bounds on the number and sizes of conjugacy classes in finite Chevalley groups with applications to derangements*, Trans. AMS 364 (2012), Corollary 1.2(3) and Table 2, p.3050, https://doi.org/10.1090/S0002-9947-2012-05427-4, use q^r for SO(2r+1,q) and SO±(2r,q); this audit does not cover ³D₄(q).

For B_r(q) with q odd, n=q^(r²)∏_(i=1)^r(q^(2i)−1)/g and t=gf, where g=gcd(2,q−1)=2. For q even use the B_r=C_r isomorphism: n has the same formula with g=1, t=f for r≥3, and t=2f for r=2 because of the exceptional graph automorphism. The r=2,q=2 group is not simple. These yield t≤2f and n≥q^(2r²+r)/3.

For D_r^ε(q), r≥4 and ε=+1 (plus), −1 (minus), put g=gcd(4,q^r−ε). Then

    n=q^[r(r−1)](q^r−ε)∏_(i=1)^(r−1)(q^(2i)−1)/g,
    t=2fg, except t=6fg for plus type D₄.

The latter accounts for triality, giving the uniform safe bound t≤24f. The table indices give the same t in odd and even characteristic after their case-dependent 2-factors are combined. The product ∏_(i≥1)(1−q^(−2i))>2/3 and 1−q^(−r)≥1/2 imply n≥q^(2r²−r)/12. Source interpretation and these formulas require independent mathematical review.

## Tails and finite-grid correction

For B_r,

    R≥q^[2r²−2r]/(24f³)≥q^[2r²−2r]/[24(log₂q)³].

The last expression increases in q≥3 for r=2, and in q≥2 for r≥3; it also increases with r. This yields r≥5 all q from (5,2), r4 q≥3 from (4,3), r3 q≥7 from (3,7), and r2 q≥512 from (2,512). Check r3,q5 separately using f=1: 5^12>24·1030². As q=6 is not a prime power, this extends the r3 passing range to q≥5. An earlier claim that the log-bound itself passed at q=5 was false; 5^12/[24(log₂5)³] is below 1030².

For D_r^±,

    R≥q^[2r²−4r]/(12·24³ f³)
     ≥q^[2r²−4r]/[12·24³(log₂q)³].

This increases in q≥2 and r≥4, so endpoint tests prove r≥6 for all q, r5 q≥3, and r4 q≥7. All stated tail ranges have n≥2²⁰.

## Exact residual comparisons

Using the exact n,t formulas above, [the exact arithmetic certificate](../code/verify_sd_orthogonal_raw_bounds.py) verifies the finite grid with integer arithmetic. With n≥2²⁰, its R≤1030² parameters are

- B₂: q∈{5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53,59,61,64,81,125,128,256};
- B₃: q∈{2,3}; B₄: none;
- D₄^+(q): q∈{2,3}; D₄^−(q): q∈{2,3}; D₅^±: none.

B₂ with q=3,4 has n<2²⁰ and q=2 is nonsimple; these are not included in that R-failure list. B_r(q)=C_r(q) for q even, and B₂(q)=C₂(q) for odd q as well; avoid double counting with the symplectic screen. The r3,q5 check was explicitly added after finding the faulty conservative endpoint. Run `python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_orthogonal_raw_bounds.py` from the repository root; the script passed. Its finite comparisons do not certify the cited source theorems, monotonicity, the folder argument, or any global simple-group census.

## Scoped independent review

reviewer contributor 1 accepted the orthogonal raw-R screen at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/1228403b62d5c6abbf31272ed4cb4e300424e9d9), conditional on the earlier raw SD criterion and displayed group-theoretic inputs. The review inspected Kleidman–Liebeck's order/index tables and automorphism theorem, including plus-D4 triality and B/C identifications, and checked the product bounds, corrected rank-three endpoint, monotone tails and finite-grid coverage. The pinned exact-arithmetic certificate passed independently under Python 3.12.14. This covers only the stated ranges and retains all folder and CFSG dependencies; it is not a global simple-group census.
