# Exclusion for small Ree socles in all SD_k

**Mira Cult**

This manuscript-local argument on [C0010](../../claims/0010.md) is conditional on the primitive left-Bol folder and inversion results and the [SD counting and semiregularity arguments](sd-a5-all-factors.md) at source [the source revision](https://github.com/Mira-Cult/math-wip/commit/266152034b2f190313d253c4d55df0d4f85f68c2). Under those upstream hypotheses, the conclusion is that no primitive SD_k left multiplication group has socle T^k with T=²G₂(q), q=3^f≥27, f odd, and k≥3. It makes no assertion that all primitive Bol groups have diagonal type. The exceptional q=3 is not a nonabelian simple Ree group in this family and is not treated here; its derived group PSL₂(8) is covered separately.

## Group data and square classes

For T=²G₂(q), the order n=|T|=q³(q³+1)(q−1) follows by multiplying the involution-class size and centralizer order supplied by the following source. Teng Fang, Binzhou Xia, Shasha Zheng and Sanming Zhou, *Cubic graphical regular representations of Ree groups*, Communications in Algebra 51 (2023), 3729–3733, https://doi.org/10.1080/00927872.2023.2187627, §2 immediately before Proposition 2.2, Proposition 2.2(i)–(ii), and Theorem 2.1(ii), record the unique involution class, Out(T)=C_f, involution count q²(q²−q+1), and an involution centralizer C₂×PSL₂(q). In particular, T is simple for q≥27, all automorphism involutions are inner because f is odd, and

    a=|Aut(T)|=fn,    b=1+q²(q²−q+1).

The centralizer C₂×PSL₂(q) contains C₂×C₂. Two distinct nonidentity elements of this subgroup have product another involution. Because the involutions form one T-conjugacy class and all automorphism involutions are inner, I⊆(α^T)² for each nonidentity involution α∈Aut(T). Thus the fixed-identity lemma in the [general SD count](sd-a5-all-factors.md#general-counting-lemma) applies without assuming the more general [square-class lemma](sd3-involution-count.md).

Moreover 5∤n: since f is odd, q≡2 or 3 mod 5, so 5 divides none of q, q−1, q³+1.

## Uniform estimates

Put x=b/n and y=a/n²=f/n. For all q≥27,

    x=1/n+1/[q(q²−1)] < 1/1000,
    y=f/n ≤q/n=1/[q²(q³+1)(q−1)] < 1/10000000,
    a≤b².

The first bound uses n≥q(q²−1), and 2/[27(27²−1)]<1/1000. For the second, f≤q and 27²(27³+1)26>10000000. To see the third, put M=q²−q+1; then n=q³(q²−1)M and b=1+q²M. Since f≤q−1 and qM≥(q−1)(q²−1), we have fn≤q⁴M²<b².

## Folder setup and nonalternating top

Use the setup of the [SD counting manuscript](sd-a5-all-factors.md#folder-setting-and-semiregularity): the conjugation action of Λ on B is injective, |Λ|=n^(k−1), every λ∈Λ has a fixed factor on which it acts identically, Λ is invariant under the extension G̃=G⋊⟨t⟩, and every product of two Λ-elements has order dividing n^(k−1). Let P be the image of G on the factors. As in that manuscript, P is primitive; the top image of Λ lies in the coset π(t)P.

Define F_0(z)=1, F_1(z)=z and F_k(z)=zF_{k−1}(z)+(k−1)aF_{k−2}(z). The general count gives |Λ|≤F_k(b)−F_k(b−1)≤kF_{k−1}(b), with F_m(b)≤(b+√((m−1)a))^m. Thus for 3≤k≤24,

    |Λ|/n^(k−1) ≤ k[x+√((k−2)y)]^(k−1)
                 < k(1/1000+1/100)^(k−1) < 1.

The first strict inequality uses 22/10000000<1/10000. The last follows since 1/1000+1/100<1/2 and k/2^(k−1)<1 for k≥3.

If k≥25 and P does not contain A_k, Maróti, *On the Orders of Primitive Groups* (2002), Corollary 1.2, p. 3, https://www.renyi.hu/~maroti/primitive.pdf, gives |P|<2^k. This bound is classification-dependent. Since a≤b², at most k b^(k−1) actions lie over each top permutation, and hence

    |Λ|/n^(k−1) < 2k(2x)^(k−1) < 2k/500^(k−1) < 1,

contradicting |Λ|=n^(k−1). The last expression decreases for k≥25 and is already below one at 25.

## Alternating top

Suppose P≥A_k. Every λ∈Λ has a fixed factor. If its top involution s has at least two transpositions, choose two of its transpositions and a fixed point, and replace the two matchings (12)(34), fixing 5, by (23)(45), fixing 1, leaving the other cycles unchanged. Their product is a 5-cycle. The original and replacement top involutions are A_k-conjugate: their S_k conjugacy class does not split in A_k because the centralizer contains an odd transposition. Lift an even conjugator through G and conjugate λ; the product of the two Λ-elements then has order divisible by 5, contrary to 5∤n and the semiregularity consequence above. Thus only zero or one top transposition can occur.

Using the factor-action injection and the general count truncated at one transposition, and b^m−(b−1)^m≤m b^(m−1), we get

    |Λ|/n^(k−1)
      ≤ k x^(k−1) + [k(k−1)(k−2)/2] y x^(k−3).

For k≥3, each summand decreases with k: the successive ratios are ((k+1)/k)x and ((k+1)/(k−2))x, each <1 since x<1/1000. At k=3 the sum is 3x²+3y<1. This contradiction covers every k≥3.

Independent reviewer contributor 1 accepted this argument at exact revision [the source revision](https://github.com/Mira-Cult/math-wip/commit/7b1c9e8786ceb5e7d8e6a6709adee1aefe736efd), conditional on the stated prior folder, inversion, counting and semiregularity results and the CFSG-dependent Maróti bound. The reviewer inspected the cited primary group data, the square-class deduction, all inequalities and both top-group cases. This does not reprove the source group facts or upstream folder machinery.
