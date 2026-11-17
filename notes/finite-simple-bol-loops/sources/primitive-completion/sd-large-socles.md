# Candidate SD exclusion for large socles with a common involution class

**Mira Cult**

This independently reviewed manuscript-local argument on [C0010](../../claims/0010.md) uses the primitive left-Bol folder and inversion results and the [SD counting and semiregularity arguments](sd-a5-all-factors.md). It proposes the following conditional conclusion, not an all-socle classification.

Let T be a finite nonabelian simple group of order n≥2²⁰. Suppose T has an Aut(T)-invariant T-conjugacy class J of involutions such that J⊆(α^T)² for every nonidentity involution α∈Aut(T). Under the upstream folder and inversion hypotheses, no primitive SD_k left multiplication group has socle T^k for any k≥3. The [common-class fixed-identity argument](sd-alternating-all-factors.md#a-common-involution-class-replaces-uniqueness) explains this hypothesis and does not require J to be the only involution class. In particular, the [single-class square lemma](sd3-involution-count.md) supplies it when T has one involution class, within the scope of that lemma and its dependencies.

The proof imports the following classification-dependent estimates. Fulman and Guralnick, *Bounds on the number and sizes of conjugacy classes in finite Chevalley groups with applications to derangements*, Transactions of the AMS 364 (2012), 3023–3070, Proposition 5.3, p. 3052, https://doi.org/10.1090/S0002-9947-2012-05427-4, prove that k(A)≤|A|^.41 for every finite almost simple group A. Stefan Kohl, *A bound on the order of the outer automorphism group of a finite simple group of given order*, Theorem 1, https://stefan-kohl.github.io/preprints/outbound.pdf, states |Out(T)|<log₂n (the 2 is the base subscript); we use the weaker consequence |Out(T)|<2 log₂n below. The accessible preprint states the theorem and proof; its final publication details have not been verified here. Maróti's primitive-group estimate is cited at its use below.

## Automorphism and prime bounds

Let A=Aut(T), a=|A|, and b=#{u∈A:u²=1}, so b is one plus the number of involutions of A. The Frobenius–Schur involution formula and Cauchy–Schwarz give

    b ≤ Σ_(χ∈Irr A) χ(1) ≤ √(k(A)a) ≤ a^.705.

Put L=log₂ n, x=b/n, y=a/n². By Kohl's bound a<2nL, so

    x < (2L)^.705 · 2^(−.295L),      y < 2L · 2^(−L).

To find an odd prime not dividing n, let M=ceil(√(2L)). Bertrand's postulate gives distinct odd primes p_j∈(2^j,2^(j+1)) for j=1,...,M. Their product exceeds 2^[M(M+1)/2]>n. Thus some odd r among them does not divide n, and

    K:=2r−1 < 2^(M+2) ≤ D:=2^(√(2L)+3).

For L≥20 both (2L)^.705 2^(−.295L) and 2L·2^(√(2L)+3−L) decrease: the logarithmic derivatives with respect to L are .705/(L ln 2)−.295 and 1/(L ln 2)+1/√(2L)−1, respectively, after expressing their logarithms in base two. At L=20 the first is <1/4: log₂40<27/5 because 40⁵<2²⁷, so its base-two logarithm is <(.705)(27/5)−(.295)(20)=−2.093<−2. At the same endpoint,

    D y < 40·2^(√40+3−20) < 40/1024 < 1/16.

Consequently, throughout L≥20,

    x<1/4,       D y<1/16,       x+√(D y)<1/2.

Also D>24 in this range.

## Both primitive top cases

In the upstream folder setting, the common-class fixed-identity lemma gives the usual count with F_0(z)=1, F_1(z)=z and F_m(z)=zF_{m−1}(z)+(m−1)aF_{m−2}(z). For 3≤k≤max(K,24), the recurrence and its derivative identity give

    |Λ|/n^(k−1)
       ≤ k F_{k−1}(b)/n^(k−1)
       ≤ k[x+√((k−2)y)]^(k−1)
       < k/2^(k−1) < 1.

Here max(K,24)<D; in particular the stronger derivative bound K F_{K−1}(b)<n^(K−1) holds. This contradicts |Λ|=n^(k−1) in the initial range.

The top image P of G on the k factors is primitive, as in the cited SD manuscript. If P contains A_k and k≥K, the forbidden-prime matching argument leaves at most j≤(r−3)/2 transpositions in an occurring top involution: a larger one with a fixed point gives an r-cycle in the product of two conjugates, and full-support involutions with at least r transpositions give two r-cycles. Such a product cannot occur because the cyclic semiregularity argument gives order dividing n^(k−1), while r∤n. The normalized derivative summand for a fixed j has successive ratio at most [2r/(r+2)]x<1. Their sum is <1 at K and stays below one thereafter.

If P does not contain A_k and k≥25, Maróti, *On the Orders of Primitive Groups* (2002), Corollary 1.2, p. 3, https://www.renyi.hu/~maroti/primitive.pdf, gives |P|<2^k. This theorem is classification-dependent. Set c=max(b,√a). The factor-action count above any top involution is at most k c^(k−1), and π(Λ) lies in a coset of P, so

    |Λ|/n^(k−1) < 2k(2c/n)^(k−1).

Since y<Dy<1/16 and x<1/4, c/n=max(x,√y)<1/4. The last expression is therefore <2k/2^(k−1)<1 for k≥25. Smaller k are in the initial range. Both cases contradict |Λ|=n^(k−1).

The result and its common-class hypothesis require independent mathematical review. It reduces only the eligible socles below 2²⁰ to a finite residual set; it neither proves that every simple group has such a class nor enumerates the residual groups. The source theorems, original folder and inversion results, and all status/review qualifications remain separate dependencies.


reviewer contributor 1 accepted this argument at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/698ce5f6d50e7186f205a63f4a2c413145775915), directly checking Fulman–Guralnick Proposition 5.3, Kohl Theorem 1 and Maróti Corollary 1.2, and checking the Frobenius–Schur estimate, prime construction, endpoint inequalities, monotonicity and both top cases. The common-class and upstream folder/semiregularity hypotheses remain explicit. A later typographical source clarification notes that Kohl actually states the stronger base-two logarithmic bound; the weaker inequality used in the reviewed proof is unchanged.
