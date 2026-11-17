# Candidate exclusion for all alternating socles in SD_k

**Mira Cult**

This independently reviewed manuscript-local argument on [C0010](../../claims/0010.md) is conditional on the folder and inversion results and the [counting, semiregularity, and primitive-top arguments](sd-a5-all-factors.md) at source [the source revision](https://github.com/Mira-Cult/math-wip/commit/266152034b2f190313d253c4d55df0d4f85f68c2). It proposes excluding socles T^k with T=A_m, m≥7, k≥3. The cases A₅ and A₆≅PSL₂(9) are covered by the existing A₅ and PSL₂ arguments, under their own stated dependencies and review scopes. This does not classify all primitive left Bol multiplication groups.

## A common involution class replaces uniqueness

The fixed-identity lemma needs only an Aut(T)-invariant T-conjugacy class J of involutions with J⊆(α^T)² for every nonidentity involution α∈Aut(T). Indeed, given λ whose top involution has no fixed factor acted on identically, choose any v∈J. On every fixed factor, the square-class property allows a product of two B-conjugates to have coordinate v. On a transposed pair let the action be φ(x,y)=(θ⁻¹(y),θ(x)). Since θ(v) belongs to J, choose g∈T with g⁻¹θ(v)g=v. For b=(1,g⁻¹), c=(v,g⁻¹), the product of the two conjugates is bφ(b⁻¹c)c⁻¹=(v,v). Coordinates on distinct cycles are independent, so this produces the full diagonal slice at the chosen v. Thus (v,…,v) belongs to Λ²∩Δ(T), contrary to the folder hypothesis. No assertion that J is the only involution class is used.

For T=A_m, m≥7, the standard theorem Aut(A_m)=S_m gives such J: the double transpositions. J is invariant under S_m, and forms one A_m-class because the centralizer in S_m of a double transposition contains an odd transposition. For any nonidentity involution α∈S_m, its S_m-class is likewise a single A_m-class because its centralizer contains one of its transpositions. If α has one transposition, multiply it by a disjoint conjugate. If it has at least two, replace two transpositions (12)(34) with (13)(24), leaving all other transpositions unchanged. In each case the product is a double transposition, and A_m-conjugation fills J. Thus J⊆(α^T)², as required. The already recorded C0014 proof also identifies this common class; source-review of Aut(A_m)=S_m remains a standard external group-theoretic dependency.

## Scalar bounds for m≥14

Put n=|A_m|=m!/2, a=|Aut(A_m)|=m!=2n, and b=b_m=1+i₂(S_m), where b_0=b_1=1 and b_m=b_{m−1}+(m−1)b_{m−2}. We prove b/n≤1/m³ for m≥14. Let z_m=b_m/m!. Then z_m=(z_{m−1}+z_{m−2})/m. Exact base checks give 2·14³ b_14≤14! and 2·15³ b_15≤15!. If the estimate z_j≤1/(2j³) holds at j=m−1,m−2, then it holds at m because

    m²[(m−1)⁻³+(m−2)⁻³] ≤ 2m²/(m−2)³ < 1     (m≥16).

Therefore b/n=2z_m≤1/m³ for all m≥14. Also n≥2m⁶ for m≥14: it holds at 14, and n/m⁶ increases thereafter because (m+1)(m/(m+1))⁶>1. With c=max(b,√a), it follows c/n≤1/m³, since √(2/n)≤1/m³.

Choose a prime r with m<r<2m using Bertrand's postulate. It does not divide n. Set K=2r−1<4m. The general count has F_0(z)=1, F_1(z)=z, F_k(z)=zF_{k−1}(z)+(k−1)aF_{k−2}(z), and |Λ|≤F_k(b)−F_k(b−1)≤kF_{k−1}(b). From F_h(b)≤[b+√((h−1)a)]^h we obtain, for 3≤k≤K,

    [b+√((k−2)a)]/n ≤ 1/m³+√(8m/n)
                         ≤ 1/m³+2/m^(5/2) < 1/2.

Hence the unrestricted count is below n^(k−1); in particular K F_{K−1}(b)<n^(K−1).

For k≥K when the primitive top image P contains A_k, the forbidden-prime matching argument from the cited manuscript leaves only j≤(r−3)/2 transpositions. The normalized j-th derivative summand has successive ratio \[(k+1)/(k−2j)\](b/n)≤[2r/(r+2)]/m³<1, so the sum, already <1 at K, stays <1.

For P not containing A_k and k≥25, Maróti, *On the Orders of Primitive Groups* (2002), Corollary 1.2, p. 3, https://www.renyi.hu/~maroti/primitive.pdf, gives |P|<2^k. This is a CFSG-dependent input. There are at most |P| top permutations in the coset π(t)P. Since a≤c² and b≤c, at most k c^(k−1) actions lie over each one, so |Λ|/n^(k−1)<2k(2c/n)^(k−1)≤2k(2/m³)^(k−1)<1. The last expression decreases for k≥25 and is below 1 at 25. For k<25, note K≥2(m+1)−1≥29, so the unrestricted count already handles them.

## Exact checks for 7≤m≤13

The self-contained [Python certificate](../code/verify_sd_alternating_bounds.py) chooses the least prime r>m, verifies all unrestricted counts up to max(K,24), checks the derivative bound at K, and verifies b²≥a and the nonalternating bound at k=25 together with its monotonicity. Run `python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_alternating_bounds.py` from the repository root. These checks complete the finite m-range, subject to the group-theoretic dependencies above.

The certificate was executed and passed. It verifies only the stated arithmetic. The new common-class argument, inequalities, external standard group facts, and upstream folder/inversion dependencies require independent mathematical review.


reviewer contributor 1 accepted this argument at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/698ce5f6d50e7186f205a63f4a2c413145775915). The review checked the common class and twisted-pair construction, recurrence and induction, both primitive-top cases and the forbidden-prime tail; the bundled Python 3.12.14 certificate passed. Acceptance is conditional on the separately reviewed upstream folder/inversion and semiregularity results and the cited CFSG-dependent group estimates. It is not a new verification of those upstream results.
