# Candidate exclusion for Suzuki socles in all SD_k

Mira Cult
This manuscript-local argument on [C0010](../../claims/0010.md) is conditional on the primitive left-Bol folder and inversion results used by the [SD₃ manuscript](sd3-involution-count.md) and [general SD counting argument](sd-a5-all-factors.md) at repository revision the recorded source revision. It uses no new permanent IDs. It claims that, subject to those upstream results and the cited Suzuki data, no primitive SD_k left multiplication group has socle Sz(q)^k, for q=2^f≥8 with f≥3 odd and k≥3.

## Suzuki data and square-class property

Let T=Sz(q). Basheer, *On a group extension involving the Suzuki group Sz(8)*, Afrika Matematika 34 (2023), article 96, §1, https://doi.org/10.1007/s13370-023-01130-z, records |T|=n=q²(q²+1)(q−1), 3∤n, and Out(T)=C_f. Since f is odd, every involution of Aut(T) belongs to the inner group T, and a=|Aut(T)|=fn. Arumugam, Bamberg and Giudici, *Low Rank Groups of Lie Type Acting Point- and Line-Primitively on Finite Generalised Quadrangles*, Electronic J. Combin. 32(1) (2025), #P1.43, https://doi.org/10.37236/12993, Lemmas 10–11, give one involution class I with centralizer order q². Therefore the number of involutions is n/q²=(q²+1)(q−1), and b=1+n/q².

The same paper, Theorem 9, records a subgroup of shape E_q.E_q.C_(q−1), containing an elementary abelian subgroup E_q of order q. The [general square-class lemma](sd3-involution-count.md) also supplies this property under the unique-class hypothesis; the direct argument here avoids that external theorem for this family. Take two distinct nonidentity elements of E_q; their product is a nonidentity involution. Since every involution of T is T-conjugate, for each nonidentity involution α of Aut(T), the square (α^T)² contains I. This verifies the square-class premise used below.

## Folder consequences

Use the standard upstream setting: G is primitive of simple diagonal type on Ω with socle B=T^k and H a point stabilizer. In the extension G̃=G⋊⟨t⟩ there is a G̃-conjugation-invariant set Λ=tK of involutions with |Λ|=|Ω|=n^(k−1), Λ²∩H={1}, 1∈K and G=⟨K⟩. Conjugation of Λ on B is injective. The unique-class/square-class argument gives that every λ∈Λ has a factor fixed by its top permutation on which λ acts identically. In particular every top permutation from Λ has a fixed point. Write P for G's image on the factors. P is primitive: a nontrivial invariant partition of the factors yields an H-normalized subgroup strictly between H∩B=Δ(T) and B, hence a subgroup strictly between H and G.

Every z∈Λ² has order dividing n^(k−1). Indeed all powers of z lie in Λ², since for z=λμ and each integer h, z^(2h)=(z^hλz^(−h))λ and z^(2h+1)=(z^hλz^(−h))μ. Conjugation invariance puts each factor in Λ. Since Λ²∩H={1} and Λ² is G-invariant, every nonidentity such power is fixed-point-free; the cyclic group ⟨z⟩ therefore acts freely on Ω. In particular, |z| is not divisible by 3.

## Alternating top

Suppose P≥A_k. If a λ∈Λ has nontrivial top involution s, it has a transposition and a fixed point. An A_k-conjugate u of s may swap that fixed point with one point of the transposition, agreeing with s on all other points; su is a 3-cycle. The necessary conjugator is even: the S_k conjugacy class of s is one A_k class since its centralizer contains an odd transposition. Lift that conjugator through G. Conjugation invariance then supplies μ∈Λ whose top permutation is u, so λμ has order divisible by 3, a contradiction.

Consequently every λ∈Λ has trivial factor permutation. Since 1∈K, t∈Λ; then every element of K=tΛ also has trivial factor permutation, and G=⟨K⟩ has trivial top image. This contradicts P≥A_k for k≥3.

## Nonalternating top

Suppose P does not contain A_k. The unrestricted count is A_k=F_k(b)−F_k(b−1), where F_0(x)=1, F_1(x)=x and F_m(x)=xF_{m−1}(x)+(m−1)aF_{m−2}(x). It satisfies A_k≤kF_{k−1}(b), and F_m(b)≤(b+√((m−1)a))^m: the former follows from F'_k(b)=kF_{k−1}(b) and nonnegative coefficients, and the latter by induction on the recurrence.

For 3≤k≤24, use

    b/n=1/q²+1/n < 1/60,
    a/n²=f/n ≤ q/n ≤ 1/3640,
    [b+√((k−2)a)]/n < 1/60+1/10 < 1/2.

Here q≥8, n≥29120, f≤q, and 22/3640<1/100. Hence A_k/n^(k−1)<k/2^(k−1)<1.

For k≥25, Maróti, *On the Orders of Primitive Groups*, Corollary 1.2, p. 3, https://www.renyi.hu/~maroti/primitive.pdf, gives |P|<2^k. Since t normalizes B, the top image of Λ lies in the coset π(t)P, even if π(t) is not in P. Let M=(q²+1)(q−1); then b=M+1 and a=fq²M≤M²<b², since f≤q−1 and M>q²(q−1). Each possible top permutation contributes at most k b^(k−1) induced actions. Therefore

    |Λ|/n^(k−1) < 2k (2b/n)^(k−1) < 2k/30^(k−1) < 1,

again a contradiction. The final expression decreases for k≥25 and is below one at 25.

This group-theoretic exclusion has the scoped independent review below. The source citations are for the group facts indicated; they do not certify the folder reduction or this proof.

## Source verification and limitations

automated reviewers a separate automated checker accepted this argument at its recorded source revision, conditional on the stated folder/inversion hypotheses, the earlier fixed-identity counting lemma and the CFSG-dependent Maróti bound. The review checked the finite criterion and/or all-Suzuki inequalities as applicable, the top-coset count, forbidden-cycle argument, and directly inspected the cited Suzuki sources. The embedded Sz(8) integer certificate in the scalar-criterion manuscript passed with Python 3.12.14. This is a review of the displayed conditional argument, not an independent reproof of the external group results or a classification of all primitive Bol folders.
