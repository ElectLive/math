# Refined raw-count screens for linear and unitary socles

**Mira Cult**

This manuscript-local result, with scoped review below, concerns [C0010](../../claims/0010.md) refines the linear and unitary finite residuals of the [classical raw screen](sd-classical-raw-bounds.md) at source revision [the source revision](https://github.com/Mira-Cult/math-wip/commit/95f226ac6c02b0153f3c226d823518e0891c1f1d). It inherits that screen's order and outer-automorphism formulas, prime-power grids, tail bounds, and the conditional [raw-involution criterion](sd-raw-involution-count.md), including its upstream primitive-folder and inversion assumptions. It does not claim an exclusion unconditionally or assert that a failure of this sufficient screen admits a loop. Throughout, only |T| ≥ 2²⁰ is considered.

Let T be PSL_d(q) or PSU_d(q), d ≥ 4, q = p^f, r = d−1, n = |T|, g = gcd(d,q−1) in the linear case and gcd(d,q+1) in the unitary case, and t = |Out(T)| = 2fg. Put a = tn and let b count the automorphisms α of T for which α²=1. Define rational constants

    linear:  C = min(100, (5/2)t, t(q+5)/(qg));
    unitary: C = min(100, (413/50)t, t(q+8)/(qg)) for q > 2,
             C = min(100, (413/50)t) for q = 2.

Then k(Aut(T)) ≤ Cq^r. Indeed, Fulman–Guralnick, *Bounds on the number and sizes of conjugacy classes in finite Chevalley groups with applications to derangements*, Trans. AMS 364 (2012), 3023–3070, [DOI 10.1090/S0002-9947-2012-05427-4](https://doi.org/10.1090/S0002-9947-2012-05427-4), Lemma 2.1, p. 3027, gives Gallagher's inequality k(Aut(T)) ≤ t k(T). Corollary 3.7(2), p. 3033, gives g k(PSL_d(q)) ≤ q^r + 5q^(r−1), and Corollary 3.11(2), pp. 3036–3037, gives g k(PSU_d(q)) ≤ q^r + 8q^(r−1); we invoke the latter only for q > 2. Proposition 3.6, p. 3033, and Proposition 3.10, p. 3036, give k(SL_d(q)) ≤ (5/2)q^r and k(SU_d(q)) ≤ (413/50)q^r, respectively. Passing to the projective quotient cannot increase the number of conjugacy classes. The remaining bound k(Aut(T)) ≤ 100q^r is Corollary 1.2(3), p. 3025, with the rank conventions justified in the earlier screen.

The Frobenius–Schur formula and Cauchy–Schwarz imply b ≤ √(aCq^r). Hence the exact rational inequality

    n > t³ q^(3r) C(C + 3/q^r)²                            (*)

implies b³ + 3ab < n²: substituting the upper bound for b and dividing by n² gives a positive expression whose square is the right side of (*) divided by n. Thus (*) yields the conditional raw-criterion exclusion. This argument bounds b; it does not calculate its actual value.

Because C ≤ 100, every parameter passing the original sufficient screen still passes (*). On its finite residual lists, the [certificate](../code/verify_sd_linear_unitary_refined_bounds.py) verifies (*) with exact rational arithmetic. The only parameters for which (*) fails, under the inherited |T| ≥ 2²⁰ restriction, are:

- PSL: (d,q) = (4,3), (4,4), (4,5), (4,9).
- PSU: (d,q) = (4,3), (4,4), (4,5), (4,7), (4,8), (5,2), (5,4), (6,2).

Run from the repository root:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_linear_unitary_refined_bounds.py
```

The certificate checks only the displayed finite residual arithmetic, primality and prime-power exponents of its inputs, divisibility in the group orders, and the asserted output lists. It does not check the inherited grids, tail estimates, cited results, group identifications, or upstream criterion. This refinement and its interpretation of the sources await independent mathematical review.

## Scoped independent review

reviewer contributor 1 accepted this refinement at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/1228403b62d5c6abbf31272ed4cb4e300424e9d9), conditional on the earlier classical screen and raw SD criterion. The review directly inspected Fulman–Guralnick Lemma 2.1, Corollaries 3.7(2) and 3.11(2), and Propositions 3.6 and 3.10; the projective class bounds and constants agree. The Gallagher/Frobenius–Schur/Cauchy–Schwarz deduction and squared sufficient inequality were checked. The pinned finite certificate passed independently with Python 3.12.14. The inherited tails, source theorems and folder/CFSG inputs retain their recorded qualifications; failing parameters are not assertions of loop existence.
