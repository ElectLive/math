# Raw-count screens for linear, unitary and symplectic socles

Mira Cult
This result, with the scoped review below, concerns [C0010](../../claims/0010.md) applies the [raw-involution criterion](sd-raw-involution-count.md). Its exclusions are conditional on that criterion and its upstream primitive left-Bol folder and inversion results. It gives sufficient parameter ranges for simple linear, unitary and symplectic socles; an R-failure below is not a possible-loop assertion, and the lists are not a census of all finite simple groups. Dimension-three linear/unitary groups and PSL₂ groups have separate candidate treatments.

## The general R estimate

Let T be a finite nonabelian simple Chevalley group in the field q and ambient algebraic rank r conventions of Fulman and Guralnick, *Bounds on the number and sizes of conjugacy classes in finite Chevalley groups with applications to derangements*, Transactions of the AMS 364 (2012), 3023–3070, Corollary 1.2(3), p. 3025, https://doi.org/10.1090/S0002-9947-2012-05427-4. Put n=|T|, t=|Out(T)|, a=tn and b=#{α∈Aut(T):α²=1}. Their result gives k(Aut(T))≤100q^r. The Frobenius–Schur formula and Cauchy–Schwarz therefore give b≤10√(tnq^r). Setting R=n/(t³q^(3r)),

    (b³+3ab)/n² ≤ 1000/√R + 30/(q^r√R) ≤ 1030/√R.

Thus n≥2²⁰ and R>1030² imply b³+3ab<n² and hence the raw criterion's conditional exclusion for every k≥3. No common involution class is assumed.

In the three families below the field q=p^f is the natural classical-group parameter. For linear and unitary groups r=d−1, where d is the natural matrix dimension, not the rank of a permutation action; for symplectic groups r is half the natural dimension. Fulman–Guralnick §6.2 explicitly views U(d,q) inside GL(d,q²), and Proposition 3.10 uses q^(d−1); their Table 2, p. 3050, uses q^r for Sp(2r,q). The order and outer-automorphism formulas used below are read from Kleidman and Liebeck, *The Subgroup Structure of the Finite Classical Groups* (1990), Tables 2.1.C–D, printed p. 19, and Theorems 2.1.3–2.1.4, p. 16, [publisher preview](https://api.pageplace.de/preview/DT0400.9780511892394_A23680360/preview-9780511892394_A23680360.pdf). In particular, the exceptional even-characteristic Sp₄ graph automorphism is included explicitly below. The source interpretations and original deductions have the scoped review below; subsequent additions have separate review boundaries.

## Linear groups

For T=PSL_d(q), d≥4, set g=gcd(d,q−1). Then

    n=q^[d(d−1)/2]∏_(i=2)^d(q^i−1)/g,       t=2fg.

The inequality ∏_(i≥1)(1−2^(−i))>1/4, g≤d and f≤log₂q imply

    R > q^[(d−1)(d−2)]/[32d⁴(log₂q)³].

For the product bound, retain the first three factors and use ∏(1−x_i)≥1−∑x_i on the tail: the resulting lower bound is (1/2)(3/4)(7/8)(1−1/8)=147/512>1/4.

For d≥4 this lower bound increases with real q≥2 and with integer d: its logarithmic derivative in q has the sign of (d−1)(d−2)−3/ln q, and the successive d-ratio is at least 2^(2d−2)(d/(d+1))⁴>1. The exact endpoint comparisons at (d,q)=(8,2) and (4,256) show that every d≥8 for all q, and every d≥4 with q≥256, has R>1030² and n≥2²⁰.

For the remaining grid d=4,...,7 and prime powers q<256, exact integer comparison under n≥2²⁰ gives the R-fail parameters:

- d=4: q∈{3,4,5,7,8,9,11,13,16,17,19,25,27,29,49};
- d=5: q∈{2,3,4};
- d=6: q=2; d=7: none.

The grid point d=4,q=2 is simple but has order below 2²⁰, so it is outside the threshold rather than an R-failure in this list.

## Unitary groups

For T=PSU_d(q), d≥4, put g=gcd(d,q+1). Then

    n=q^[d(d−1)/2]∏_(i=2)^d(q^i−(−1)^i)/g,       t=2fg.

The product of normalized factors is at least ∏_(i≥1)(1−q^(−2i))>2/3, so

    R > q^[(d−1)(d−2)]/[12d⁴(log₂q)³].

Here the product is bounded below by (1−1/4)(1−∑_(i≥2)4^(−i))=11/16>2/3. The same estimate is used in the symplectic case.

The same monotonicity argument applies. Exact endpoint comparisons at (d,q)=(8,2) and (4,128) give R>1030² and n≥2²⁰ for every d≥8 for all q, and every d≥4 with q≥128.

The finite grid d=4,...,7 and prime powers q<128 gives, under n≥2²⁰, precisely these R-fail parameters:

- d=4: q∈{3,4,5,7,8,9,11,13,16,17,19,23,25,27,31};
- d=5: q∈{2,3,4};
- d=6: q=2; d=7: none.

The grid point d=4,q=2 is simple but has order below 2²⁰ and is excluded from this list on that ground.

## Symplectic groups

For T=PSp_(2r)(q), r≥2, put g=gcd(2,q−1). Then

    n=q^(r²)∏_(i=1)^r(q^(2i)−1)/g,
    t=2f if r=2, and t=gf if r≥3.

For r=2 and q odd, g=2; for q even, the additional graph automorphism supplies the same factor 2. The product bound ∏_(i≥1)(1−q^(−2i))>2/3 yields

    R ≥ q^[2r(r−1)]/[24(log₂q)³].

This lower bound increases in integer r≥2; as a function of q it increases for q≥2 when r≥3 and for q≥3 when r=2. Exact endpoint comparisons give R>1030² for r≥5 and all q, r=4 with q≥3, r=3 with q≥7, and r=2 with q≥1024. The single r=4,q=2 point also passes an exact comparison, so every r≥4 passes for every q. All these passing cases have n≥2²⁰.

Exact integer comparison in the remaining prime-power grid, restricted to n≥2²⁰, yields the R-fail parameters:

- r=2: q∈{5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53,59,61,64,81,125,128,256};
- r=3: q∈{2,3}.

For r=2, q=3,4 the simple group order is below 2²⁰; PSp₄(2) itself is not simple. They are outside the displayed threshold screen, not additional entries in its R-fail list.

## Exact arithmetic and limits

The self-contained [Python certificate](../code/verify_sd_classical_raw_bounds.py) enumerates prime powers in each finite grid, evaluates the exact group-order and outer-order expressions, checks the displayed residual sets, the r=4,q=2 comparison, and the integer endpoint inequalities. Run from the repository root:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_classical_raw_bounds.py
```

The certificate was run and printed `classical R-screen arithmetic passed`. It checks only the explicit arithmetic and finite enumerations; it does not execute or verify the cited theorems, group identifications, monotonicity proofs, or upstream folder results. The orthogonal and exceptional families are outside this manuscript. automated reviewers a separate automated checker accepted the original linear, unitary and symplectic R-screens at its recorded source revision, conditional on the previously reviewed raw criterion and cited CFSG-dependent group-theoretic results. The review checked the Frobenius–Schur/Cauchy–Schwarz bound, natural-field and rank conventions, order and outer-automorphism formulas including the even Sp4 graph factor, product estimates, monotonicity and tail endpoints, finite residuals and subthreshold cases. The pinned certificate passed independently under Python 3.12.14. The reviewer directly inspected Fulman–Guralnick Corollary 1.2(3) and Kleidman–Liebeck pp. 16 and 19; the preview table OCR was imperfect, but the named tables and exceptional graph factor were visible. This accepts only the original three-family screens, not later appended refinements or other Lie types.

## Candidate refinement of the symplectic residual

This section is an addition, with its separate scoped review below, to the source previously pinned at its recorded source revision; it does not change the preceding screen or inherit any review attributed to that earlier revision. It uses the same n≥2²⁰ and primitive-folder hypotheses, and makes no assertion that a parameter failing the new sufficient inequality admits a loop.

For T=PSp_(2r)(q), let n=|T|, t=|Out(T)|, a=tn and b=#{α∈Aut(T):α²=1}. Fulman–Guralnick, Table 2, p. 3050, Table 3, p. 3051, Corollary 1.2(3), p. 3025, and Lemma 2.1, p. 3027, give

    k(Aut(T)) ≤ Cq^r,
    C = min(100, (76/5)t)                if q=2,
        min(100, (54/5)t)                if q=3,
        min(100, t(1+12/q))              if q>3 is odd,
        min(100, t(1+5/q))               if q>2 is even.

The table bounds k(Sp_(2r)(q)); k(T)≤k(Sp_(2r)(q)) because T is a quotient. Gallagher's inequality, recorded in Fulman–Guralnick Lemma 2.1, gives k(Aut(T))≤t k(T); Corollary 1.2 supplies the other entry of each minimum. Frobenius–Schur and Cauchy–Schwarz now give b≤√(aCq^r). Therefore the exact rational inequality

    n > t³ q^(3r) · C(C+3/q^r)²

implies b³+3ab<n² and the raw criterion, without a common-class assumption. This follows by dividing n² into the two upper bounds for b³ and 3ab and squaring their positive sum.

The self-contained [refined symplectic certificate](../code/verify_sd_symplectic_refined_bounds.py) checks this inequality with exact rational arithmetic on every prime-power parameter in the previous finite grid. The earlier tails remain valid because C≤100. Subject to the same n≥2²⁰ threshold, the refined sufficient inequality fails only for PSp₄(q) with q∈{5,7,8,9,16,32} and PSp₆(2); all r≥4 pass. The code separately checks the prior small-order and nonsimple exclusions and the tail endpoints. Run from the repository root:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_symplectic_refined_bounds.py
```

The script printed `refined symplectic screen passed`. It verifies arithmetic only; the source-table interpretation, quotient and Gallagher arguments, and upstream raw criterion require independent mathematical review of this addition.

automated reviewers a separate automated checker accepted the refined symplectic section at its recorded source revision, including its primary FG table interpretations, Gallagher and involution bounds, exact rational criterion, finite grids and inherited tail coverage. The pinned refined script passed independently with Python 3.12.14. The [finite-residual manuscript](sd-symplectic-finite-residuals.md) records the simultaneously reviewed exact counts and conditional symplectic-family conclusion.
